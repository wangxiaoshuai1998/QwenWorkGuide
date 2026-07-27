#!/usr/bin/env python3
"""Recursively export a DingTalk Wiki (dws CLI) tree with offline media.

Output layout is 100% compatible with the previous Feishu exporter:
  <output-dir>/<root title>/.../<page title>/
      source.md      raw markdown as returned by the CLI
      index.md       localized markdown (media rewritten to ./assets/...)
      assets/        downloaded images / attachments (NNN_name.ext)
      metadata.json  per-page manifest
  <output-dir>/<root title>/manifest.json   whole-tree manifest
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime
import html
import json
import mimetypes
import re
import subprocess
import sys
import threading
import time
import urllib.parse
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


INVALID_FILENAME = re.compile(r"[\x00-\x1f/\\]")
RATE_LIMIT = re.compile(r"429|too\s*many\s*requests|rate.?limit", re.I)
# Markdown image: ![alt](url "title") — url may not contain spaces or ')'.
MD_IMAGE = re.compile(r"!\[([^\]\n]*)\]\((\S+?)(?:\s+\"[^\"]*\")?\)")
# HTML <img src="..."> tags occasionally embedded in exported markdown.
HTML_IMG = re.compile(r"<img\b[^>]*?\bsrc=[\"']([^\"']+)[\"'][^>]*>", re.I)
# Plain links; filtered by looks_like_asset() so wiki page links stay intact.
MD_LINK = re.compile(r"(?<!!)\[([^\]\n]*)\]\((https?://[^\s)]+)\)")
# dentryUuid inside DingTalk drive/attachment URLs, used for CLI fallback.
DENTRY_UUID = re.compile(r"(?:dentryUuid|dentry_uuid|dentryId)=([A-Za-z0-9_-]+)")
PAGE_TOKEN_KEYS = ("pageToken", "nextToken", "nextCursor", "cursor")

# --- DingTalk markdown dialect cleanup (applied to index.md only) ---
# Meaningless color wrappers: <span style="color: rgb(...)">…</span> or the
# degenerate <span style="color: ;">…</span>. Inner text is kept as-is.
COLOR_SPAN = re.compile(
    r"<span style=\"color:\s*(?:rgb\([^)\"]*\))?\s*;?\s*\">((?:(?!</?span\b).)*?)</span>"
)
# Auto-generated image captions occupying a whole line, e.g.
# <span style="background-color: rgb(255, 255, 255);">image.png</span>
CAPTION_LINE = re.compile(
    r"^[ \t]*<span style=\"background-color:[^\"\n]*\">[^<\n]*</span>[ \t]*\n?",
    re.M,
)
# Heading lines that still carry HTML span wrappers after color cleanup.
HEADING_LINE = re.compile(r"^#{1,6}[ \t].*$", re.M)
# Only spans whose style sets color/background-color are machine noise; spans
# the author wrote intentionally (class/data-* etc., no color style) are kept.
STYLED_SPAN = re.compile(
    r"<span\b[^>]*\bstyle=\"[^\"]*(?:background-)?color\s*:[^\"]*\"[^>]*>"
    r"((?:(?!</?span\b).)*?)</span>"
)
# Empty image title left by the exporter: ![](url "") -> ![](url)
EMPTY_IMG_TITLE = re.compile(r"(!\[[^\]\n]*\]\(\S+?)\s+\"\"\)")


def clean_dingtalk_markdown(markdown: str) -> str:
    """Strip DingTalk export dialect noise from markdown (conservative).

    Only the well-known machine-generated patterns above are touched; any
    other HTML the author wrote intentionally is left untouched.
    """
    result = CAPTION_LINE.sub("", markdown)
    while True:  # color spans may be nested; unwrap innermost first
        unwrapped = COLOR_SPAN.sub(r"\1", result)
        if unwrapped == result:
            break
        result = unwrapped

    def unwrap_heading(match: "re.Match[str]") -> str:
        line = match.group(0)
        while True:  # styled spans may be nested; unwrap innermost first
            unwrapped_line = STYLED_SPAN.sub(r"\1", line)
            if unwrapped_line == line:
                return line
            line = unwrapped_line

    result = HEADING_LINE.sub(unwrap_heading, result)
    result = EMPTY_IMG_TITLE.sub(r"\1)", result)
    return result


def _self_test() -> int:
    """Inline assertions for clean_dingtalk_markdown (run with --self-test)."""
    # Auto-generated caption line is dropped entirely.
    assert clean_dingtalk_markdown(
        '<span style="background-color: rgb(255, 255, 255);">image.png</span>\n正文\n'
    ) == "正文\n"
    # Meaningless color wrappers are unwrapped, inner text kept.
    assert clean_dingtalk_markdown('<span style="color: rgb(38, 38, 38);">正文</span>') == "正文"
    # Heading spans carrying color/background-color styles are unwrapped.
    assert clean_dingtalk_markdown(
        '# <span style="background-color: rgb(245, 247, 240);">第 1 章 标题</span>'
    ) == "# 第 1 章 标题"
    # User-authored spans (class/data-*, no color style) must survive.
    kept = '## <span class="anchor" data-id="x">自写标题</span>'
    assert clean_dingtalk_markdown(kept) == kept
    # Empty image title left by the exporter is stripped.
    assert clean_dingtalk_markdown('![](https://example.com/a.png "")') == "![](https://example.com/a.png)"
    print("self-test passed")
    return 0


class Throttler:
    """Global adaptive backoff shared by every CLI call and download."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self.delay = 0.0

    def wait(self) -> None:
        with self._lock:
            delay = self.delay
        if delay:
            time.sleep(delay)

    def penalize(self) -> None:
        with self._lock:
            self.delay = min(15.0, self.delay * 2 if self.delay else 2.0)
        print(f"[限流] 检测到限流，退避延迟提升到 {self.delay:.1f}s", file=sys.stderr, flush=True)


class ConcurrencyGate:
    """Semaphore whose effective size shrinks when rate limiting is detected."""

    def __init__(self, workers: int) -> None:
        self.workers = max(1, workers)
        self._sem = threading.BoundedSemaphore(self.workers)
        self._lock = threading.Lock()
        self._reserved = 0

    def shrink(self) -> None:
        with self._lock:
            if self.workers - self._reserved <= 1:
                return
            if self._sem.acquire(blocking=False):
                self._reserved += 1
                print(
                    f"[限流] 并发下载降至 {self.workers - self._reserved}",
                    file=sys.stderr,
                    flush=True,
                )

    def __enter__(self) -> "ConcurrencyGate":
        self._sem.acquire()
        return self

    def __exit__(self, *exc: Any) -> None:
        self._sem.release()


THROTTLE = Throttler()
GATE: ConcurrencyGate  # initialized in main()


def cli_json(args: list[str], retries: int = 3) -> dict[str, Any]:
    """Run a dws command with --format json, 3 attempts + incremental backoff."""
    command = ["dws", *args, "--format", "json"]
    last_error = ""
    for attempt in range(1, retries + 1):
        THROTTLE.wait()
        proc = subprocess.run(command, text=True, capture_output=True)
        if proc.returncode == 0:
            try:
                payload = json.loads(proc.stdout)
            except json.JSONDecodeError as exc:
                raise RuntimeError(
                    f"CLI returned invalid JSON: {exc}\n{proc.stdout[:500]}"
                ) from exc
            if payload.get("success", True):
                return payload
            last_error = json.dumps(payload, ensure_ascii=False)[:800]
        else:
            last_error = (proc.stderr or proc.stdout).strip()[:800]
        if RATE_LIMIT.search(last_error):
            THROTTLE.penalize()
            if "GATE" in globals():
                GATE.shrink()
        if attempt < retries:
            time.sleep(attempt + THROTTLE.delay)
    raise RuntimeError(f"Command failed: {' '.join(command[:4])}\n{last_error}")


def safe_name(value: str, fallback: str) -> str:
    value = INVALID_FILENAME.sub("／", value).strip().rstrip(".")
    return value or fallback


def extension_for(name: str, mime: str, kind: str) -> str:
    suffix = Path(name).suffix
    if suffix and len(suffix) <= 12 and re.fullmatch(r"\.[A-Za-z0-9]+", suffix):
        return suffix
    normalized = mime.split(";", 1)[0].strip().lower()
    aliases = {
        "image/jpeg": ".jpg",
        "image/png": ".png",
        "image/gif": ".gif",
        "image/webp": ".webp",
        "image/svg+xml": ".svg",
        "application/pdf": ".pdf",
    }
    if normalized in aliases:
        return aliases[normalized]
    guessed = mimetypes.guess_extension(normalized) if normalized else None
    if guessed:
        return guessed
    return ".png" if kind == "image" else ".bin"


@dataclass
class Node:
    data: dict[str, Any]
    parent: "Node | None" = None
    children: list["Node"] = field(default_factory=list)
    directory: Path | None = None
    export_method: str = "folder"

    @property
    def title(self) -> str:
        return str(self.data.get("name") or "未命名页面")

    @property
    def node_id(self) -> str:
        return str(self.data.get("nodeId") or "")

    @property
    def is_virtual_root(self) -> bool:
        return not self.node_id


@dataclass
class Asset:
    page: Node
    kind: str  # image | attachment
    raw: str  # exact URL text as it appears in the markdown
    href: str  # unescaped URL used for downloads
    token: str  # dentryUuid for dws drive download fallback ("" if unknown)
    output: Path


def check_auth() -> None:
    try:
        payload = cli_json(["auth", "status"], retries=1)
    except Exception as exc:
        raise SystemExit(f"无法执行 dws auth status，请确认已安装 dws CLI：{exc}")
    if not (payload.get("authenticated") and payload.get("token_valid", True)):
        raise SystemExit(
            "dws 未登录或 token 已过期，请先运行 `dws auth login` 完成钉钉认证后重试。"
        )
    print(
        f"[认证] {payload.get('corp_name', '')} / {payload.get('user_name', '')}",
        flush=True,
    )


def warn_truncated_pagination(context: str) -> None:
    """hasMore is true but no pagination token was found: results may be cut."""
    print(
        f"[警告] {context} 返回 hasMore 但未找到分页 token（{'/'.join(PAGE_TOKEN_KEYS)} 均为空），结果可能被截断",
        file=sys.stderr,
        flush=True,
    )


def list_children(workspace: str, folder: str | None) -> list[dict[str, Any]]:
    """Paginated `dws wiki node list` (50/page); loops until hasMore is false."""
    items: list[dict[str, Any]] = []
    cursor = ""
    while True:
        args = ["wiki", "node", "list", "--workspace", workspace, "--limit", "50"]
        if folder:
            args.extend(["--folder", folder])
        if cursor:
            args.extend(["--cursor", cursor])
        payload = cli_json(args)
        items.extend(payload.get("nodes") or [])
        if not payload.get("hasMore"):
            return items
        cursor = next(
            (str(payload[key]) for key in PAGE_TOKEN_KEYS if payload.get(key)), ""
        )
        if not cursor:  # defensive: avoid infinite loop on unknown token key
            warn_truncated_pagination(f"wiki node list（folder={folder or '根节点'}）")
            return items


def workspace_name(workspace: str) -> str:
    for space_type in ("orgWikiSpace", "myWikiSpace"):
        cursor = ""
        while True:
            args = ["wiki", "space", "list", "--type", space_type, "--limit", "50"]
            if cursor:
                args.extend(["--cursor", cursor])
            try:
                payload = cli_json(args)
            except Exception:
                break
            for space in payload.get("wikiSpaces") or []:
                if str(space.get("workspaceId")) == workspace:
                    return str(space.get("name") or workspace)
            if not payload.get("hasMore"):
                break
            cursor = next(
                (str(payload[key]) for key in PAGE_TOKEN_KEYS if payload.get(key)), ""
            )
            if not cursor:
                warn_truncated_pagination(f"wiki space list（type={space_type}）")
                break
    return workspace


def build_root(workspace: str, root_id: str | None) -> Node:
    if root_id:
        data: dict[str, Any] = {
            "nodeId": root_id,
            "name": root_id[:12],
            "hasChildren": True,
            "contentType": "ALIDOC",
            "workspaceId": workspace,
        }
        try:  # doc read also yields the real title for a node id
            payload = cli_json(["doc", "read", "--node", root_id])
            if payload.get("title"):
                data["name"] = str(payload["title"])
        except Exception:
            pass
        return Node(data)
    return Node(
        {
            "nodeId": "",
            "name": workspace_name(workspace),
            "hasChildren": True,
            "contentType": "",
            "workspaceId": workspace,
        }
    )


def crawl(workspace: str, root_id: str | None) -> Node:
    root = build_root(workspace, root_id)

    def visit(parent: Node) -> None:
        if not parent.is_virtual_root and not parent.data.get("hasChildren"):
            return
        for item in list_children(workspace, parent.node_id or None):
            child = Node(dict(item), parent=parent)
            parent.children.append(child)
            visit(child)

    visit(root)
    return root


def assign_directories(root: Node, base: Path) -> None:
    root.directory = base / safe_name(root.title, (root.node_id or "wiki")[:8])

    def visit(parent: Node) -> None:
        assert parent.directory is not None
        used: set[str] = set()
        for child in parent.children:
            candidate = safe_name(child.title, child.node_id[:8])
            key = candidate.casefold()
            if key in used:
                candidate = f"{candidate}__{child.node_id[:8]}"
            used.add(candidate.casefold())
            child.directory = parent.directory / candidate
            visit(child)

    visit(root)


def walk(root: Node) -> list[Node]:
    nodes: list[Node] = []

    def visit(node: Node) -> None:
        nodes.append(node)
        for child in node.children:
            visit(child)

    visit(root)
    return nodes


def looks_like_asset(url: str) -> bool:
    """True when the URL points at a downloadable resource, not a wiki page."""
    parsed = urllib.parse.urlsplit(url)
    host = parsed.netloc.lower()
    path = parsed.path
    if "/i/nodes/" in path or "/i/spaces/" in path:
        return False  # links to other wiki pages
    if "aliyuncs.com" in host:
        return True
    if "dingtalk.com" in host and (
        DENTRY_UUID.search(url)
        or "/attachment" in path
        or "/download" in path
        or "/file/" in path
    ):
        return True
    return False


def infer_asset_name(alt: str, href: str) -> str:
    if alt and Path(alt).suffix and len(Path(alt).suffix) <= 12:
        return alt
    basename = Path(urllib.parse.unquote(urllib.parse.urlsplit(href).path)).name
    return basename or alt or "asset"


def parse_assets(node: Node, markdown: str) -> list[Asset]:
    assert node.directory is not None
    assets: list[Asset] = []
    seen: set[str] = set()

    def add(kind: str, alt: str, raw_url: str) -> None:
        href = html.unescape(raw_url)
        if not href.startswith(("http://", "https://")):
            return
        if kind == "attachment" and not looks_like_asset(href):
            return
        if raw_url in seen:
            return
        seen.add(raw_url)
        original_name = safe_name(infer_asset_name(alt, href), "asset")
        ext = extension_for(original_name, "", kind)
        stem = safe_name(Path(original_name).stem, "asset")[:60]
        match = DENTRY_UUID.search(href)
        token = match.group(1) if match else ""
        filename = f"{len(assets) + 1:03d}_{stem}{ext}"
        assets.append(
            Asset(
                page=node,
                kind=kind,
                raw=raw_url,
                href=href,
                token=token,
                output=node.directory / "assets" / filename,
            )
        )

    for alt, url in MD_IMAGE.findall(markdown):
        add("image", alt, url)
    for url in HTML_IMG.findall(markdown):
        add("image", "", url)
    for alt, url in MD_LINK.findall(markdown):
        add("attachment", alt, url)
    return assets


def append_children_nav(markdown: str, node: Node) -> str:
    if not node.children:
        return markdown
    assert node.directory is not None
    lines = []
    for child in node.children:
        assert child.directory is not None
        relative = child.directory.relative_to(node.directory).as_posix() + "/index.md"
        href = urllib.parse.quote(relative, safe="/._-()")
        lines.append(f"- [{child.title}]({href})")
    body = markdown.rstrip()
    section = "\n".join(lines)
    if body:
        return f"{body}\n\n## 子页面\n\n{section}\n"
    return f"# {node.title}\n\n{section}\n"


def localize_markdown(markdown: str, node: Node, assets: list[Asset]) -> str:
    assert node.directory is not None
    result = markdown
    for asset in assets:
        relative = asset.output.relative_to(node.directory).as_posix()
        local_href = "./" + urllib.parse.quote(relative, safe="/._-()")
        result = result.replace(asset.raw, local_href)
        if asset.href != asset.raw:
            result = result.replace(asset.href, local_href)
    return append_children_nav(result, node)


def read_markdown(node: Node) -> tuple[str, str]:
    """Fast path via `dws doc read`; fall back to `dws doc export`."""
    errors: list[str] = []
    try:
        payload = cli_json(["doc", "read", "--node", node.node_id])
        return str(payload.get("markdown") or ""), "doc read"
    except Exception as exc:
        errors.append(f"doc read: {exc}")

    assert node.directory is not None
    target = node.directory / "source.md"
    proc = subprocess.run(
        [
            "dws",
            "doc",
            "export",
            "--node",
            node.node_id,
            "--export-format",
            "markdown",
            "--output",
            str(target),
            "--yes",
        ],
        text=True,
        capture_output=True,
    )
    if proc.returncode == 0 and target.exists() and target.stat().st_size > 0:
        return target.read_text(encoding="utf-8"), "doc export"
    errors.append(f"doc export: {(proc.stderr or proc.stdout).strip()[:300]}")
    raise RuntimeError("; ".join(errors))


def write_file_upload_placeholder(node: Node) -> None:
    """Uploaded files (pdf/docx/jpg/mp4/…) are not readable via `dws doc read`;
    emit a placeholder index.md instead of failing the whole page."""
    assert node.directory is not None
    extension = str(node.data.get("extension") or "") or "未知类型"
    doc_url = str(node.data.get("docUrl") or "")
    lines = [
        f"# {node.title}",
        "",
        f"> 本节点是知识库中的上传文件（类型：{extension}），不是钉钉在线文档，",
        "> 因此无法导出为 Markdown 正文。",
        "",
        f"- 文件名：{node.title}",
        f"- 文件类型：{extension}",
    ]
    if doc_url:
        lines.append(f"- 在线地址：{doc_url}")
    (node.directory / "index.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


def export_page(node: Node) -> list[Asset]:
    assert node.directory is not None
    node.directory.mkdir(parents=True, exist_ok=True)
    print(f"[页面] {node.directory}", flush=True)

    method = "folder"
    source_markdown = ""
    if not node.is_virtual_root:
        content_type = str(node.data.get("contentType") or "")
        extension = str(node.data.get("extension") or "").lower()
        if content_type == "ALIDOC" or extension == "adoc":
            source_markdown, method = read_markdown(node)
        elif not node.children:
            # Leaf without doc content: an uploaded file (pdf/docx/jpg/mp4/…).
            method = "file_upload"
    node.export_method = method

    metadata = {
        **node.data,
        "export_method": method,
        "exported_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }

    if method == "file_upload":
        write_file_upload_placeholder(node)
        metadata["extension"] = node.data.get("extension")
        metadata["docUrl"] = node.data.get("docUrl")
        metadata["asset_count"] = 0
        (node.directory / "metadata.json").write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return []

    assets = parse_assets(node, source_markdown)

    (node.directory / "source.md").write_text(source_markdown, encoding="utf-8")
    (node.directory / "index.md").write_text(
        localize_markdown(clean_dingtalk_markdown(source_markdown), node, assets),
        encoding="utf-8",
    )
    metadata["asset_count"] = len(assets)
    (node.directory / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return assets


def download_via_url(asset: Asset) -> None:
    asset.output.parent.mkdir(parents=True, exist_ok=True)
    temp = asset.output.with_suffix(asset.output.suffix + ".part")
    proc = subprocess.run(
        [
            "curl",
            "-L",
            "--fail",
            "--silent",
            "--show-error",
            "--retry",
            "2",
            "--output",
            str(temp),
            asset.href,
        ],
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        error = proc.stderr.strip() or f"curl exited {proc.returncode}"
        if RATE_LIMIT.search(error):
            THROTTLE.penalize()
            if "GATE" in globals():
                GATE.shrink()
        raise RuntimeError(error)
    if not temp.exists() or temp.stat().st_size == 0:
        raise RuntimeError("empty response")
    temp.replace(asset.output)


def download_via_cli(asset: Asset) -> None:
    if not asset.token:
        raise RuntimeError("media has neither a working URL nor a dentryUuid")
    asset.output.parent.mkdir(parents=True, exist_ok=True)
    cli_json(
        [
            "drive",
            "download",
            "--node",
            asset.token,
            "--output",
            str(asset.output),
            "--yes",
        ]
    )


def download_asset(asset: Asset) -> tuple[Asset, str, str]:
    if asset.output.exists() and asset.output.stat().st_size > 0:
        return asset, "skipped", ""
    errors: list[str] = []
    with GATE:
        THROTTLE.wait()
        try:
            download_via_url(asset)
            return asset, "downloaded", ""
        except Exception as exc:  # fallback to authenticated CLI download
            errors.append(f"URL: {exc}")
        try:
            download_via_cli(asset)
            if asset.output.exists() and asset.output.stat().st_size > 0:
                return asset, "downloaded", ""
            errors.append("CLI returned success but output file is missing")
        except Exception as exc:
            errors.append(f"CLI: {exc}")
    return asset, "failed", "; ".join(errors)


def tree_manifest(root: Node, base: Path) -> dict[str, Any]:
    def serialize(node: Node) -> dict[str, Any]:
        assert node.directory is not None
        return {
            "title": node.title,
            "node_id": node.node_id,
            "content_type": node.data.get("contentType"),
            "export_method": node.export_method,
            "path": node.directory.relative_to(base).as_posix(),
            "children": [serialize(child) for child in node.children],
        }

    return serialize(root)


def load_failed_ids(manifest_path: Path) -> set[str]:
    """Node ids that failed last run (page export or any of its assets)."""
    if not manifest_path.exists():
        raise SystemExit(
            f"--retry-failures 需要已有清单 {manifest_path}，请先执行一次完整导出。"
        )
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    failed: set[str] = set()
    for item in manifest.get("export_failures", []):
        failed.add(str(item.get("node_id") or ""))
    for item in manifest.get("asset_failures", []):
        failed.add(str(item.get("node_id") or ""))
    failed.discard("")
    return failed


def main() -> int:
    parser = argparse.ArgumentParser(
        description="递归导出钉钉知识库为本地 Markdown（依赖 dws CLI）。"
    )
    parser.add_argument("--workspace", required=True, help="知识库 workspaceId（dws wiki space list 可查）")
    parser.add_argument("--root", default=None, help="可选：只导出该 nodeId 子树")
    parser.add_argument("--output-dir", default=".", help="输出目录（默认当前目录）")
    parser.add_argument("--workers", type=int, default=6, help="媒体并发下载数（默认 6）")
    parser.add_argument(
        "--retry-failures",
        action="store_true",
        help="读取已有 manifest.json，仅重试上次失败的页面与素材",
    )
    args = parser.parse_args()

    global GATE
    GATE = ConcurrencyGate(args.workers)

    base = Path(args.output_dir).resolve()
    base.mkdir(parents=True, exist_ok=True)

    print("[0/4] 检查 dws 认证状态", flush=True)
    check_auth()

    print("[1/4] 读取知识库页面树", flush=True)
    root = crawl(args.workspace, args.root)
    assign_directories(root, base)
    nodes = walk(root)
    print(f"      共 {len(nodes)} 个页面，workspace={args.workspace}", flush=True)

    assert root.directory is not None
    manifest_path = root.directory / "manifest.json"
    retry_ids: set[str] | None = None
    if args.retry_failures:
        retry_ids = load_failed_ids(manifest_path)
        print(f"      重试模式：上次失败 {len(retry_ids)} 个页面", flush=True)

    print("[2/4] 导出 Markdown", flush=True)
    all_assets: list[Asset] = []
    export_failures: list[dict[str, str]] = []
    for node in nodes:
        if retry_ids is not None:
            assert node.directory is not None
            already_ok = (node.directory / "index.md").exists() and (
                node.directory / "metadata.json"
            ).exists()
            if node.node_id not in retry_ids and already_ok:
                continue
        try:
            all_assets.extend(export_page(node))
        except Exception as exc:
            export_failures.append(
                {"page": node.title, "node_id": node.node_id, "error": str(exc)}
            )
            print(f"[失败] {node.title}: {exc}", file=sys.stderr, flush=True)

    print(f"[3/4] 下载 {len(all_assets)} 个图片/附件", flush=True)
    asset_failures: list[dict[str, str]] = []
    downloaded = 0
    skipped = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = [pool.submit(download_asset, asset) for asset in all_assets]
        for index, future in enumerate(concurrent.futures.as_completed(futures), start=1):
            asset, status, error = future.result()
            if status == "downloaded":
                downloaded += 1
            elif status == "skipped":
                skipped += 1
            else:
                asset_failures.append(
                    {
                        "page": asset.page.title,
                        "node_id": asset.page.node_id,
                        "file": asset.output.relative_to(base).as_posix(),
                        "url": asset.href,
                        "error": error,
                    }
                )
            if index % 25 == 0 or index == len(all_assets):
                print(f"      素材进度 {index}/{len(all_assets)}", flush=True)

    print("[4/4] 写入清单并校验", flush=True)
    file_upload_pages = [
        {
            "page": node.title,
            "node_id": node.node_id,
            "extension": node.data.get("extension"),
        }
        for node in nodes
        if node.export_method == "file_upload"
    ]
    manifest = {
        "workspace_id": args.workspace,
        "root_node_id": args.root or "",
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "page_count": len(nodes),
        "file_upload_count": len(file_upload_pages),
        "file_upload_pages": file_upload_pages,
        "asset_count": len(all_assets),
        "assets_downloaded": downloaded,
        "assets_skipped": skipped,
        "export_failures": export_failures,
        "asset_failures": asset_failures,
        "tree": tree_manifest(root, base),
    }
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    missing_pages = [
        node.title
        for node in nodes
        if node.directory is None
        or not (node.directory / "index.md").exists()
        or not (node.directory / "metadata.json").exists()
    ]
    summary = {
        "pages_expected": len(nodes),
        "pages_missing": missing_pages,
        "file_uploads": len(file_upload_pages),
        "assets_expected": len(all_assets),
        "assets_failed": len(asset_failures),
        "export_failures": len(export_failures),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2), flush=True)
    return 1 if missing_pages or export_failures or asset_failures else 0


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        raise SystemExit(_self_test())
    raise SystemExit(main())
