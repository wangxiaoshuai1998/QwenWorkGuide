# scripts 使用说明

## download_dingtalk_wiki.py — 钉钉知识库导出脚本

递归导出钉钉知识库（Wiki）为本地 Markdown，图片/附件离线化，依赖 [dws CLI](https://alidocs.dingtalk.com)。

### 前置条件

1. 已安装 `dws` CLI，并完成登录：

   ```bash
   dws auth login      # 首次登录
   dws auth status     # 确认 authenticated: true
   ```

2. Python 3.10+（无第三方依赖），系统需有 `curl`。

### 获取 workspaceId

```bash
dws wiki space list --format json
```

输出中每个知识库的 `workspaceId` 字段即为脚本所需的 ID，例如：

```json
{
  "wikiSpaces": [
    { "name": "QwenWorkGuide", "workspaceId": "w0oXWj28Mp90gz1J", ... }
  ]
}
```

个人空间可加 `--type myWikiSpace` 查询。

### 运行示例

```bash
# 导出整个知识库到 export/ 目录
python3 scripts/download_dingtalk_wiki.py --workspace w0oXWj28Mp90gz1J --output-dir export

# 只导出某个节点子树，8 并发下载媒体
python3 scripts/download_dingtalk_wiki.py --workspace w0oXWj28Mp90gz1J \
  --root vy20BglGWOvv4oaNfggjk9Oe8A7depqY --output-dir export --workers 8

# 只重试上次失败的页面与素材（读取已有 manifest.json）
python3 scripts/download_dingtalk_wiki.py --workspace w0oXWj28Mp90gz1J \
  --output-dir export --retry-failures
```

### 参数说明

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `--workspace` | 是 | 知识库 workspaceId，`dws wiki space list` 可查 |
| `--root` | 否 | 仅导出该 nodeId 及其子树；缺省导出整个知识库 |
| `--output-dir` | 否 | 输出目录，默认当前目录 |
| `--workers` | 否 | 媒体并发下载数，默认 6；检测到限流时自动降低 |
| `--retry-failures` | 否 | 读取已有 manifest.json，仅重导上次失败的页面与素材 |

### 输出结构

```
<output-dir>/<知识库或根节点标题>/
├── manifest.json          # 全树清单：页面树、成功/失败统计、失败明细
└── <页面标题>/
    ├── source.md          # CLI 返回的原始 Markdown
    ├── index.md           # 本地化 Markdown（媒体已替换为 ./assets/ 相对路径）
    ├── metadata.json      # 页面元数据：nodeId、标题、导出时间、媒体统计
    ├── assets/            # 001_xxx.png 等按序号命名的图片/附件
    └── <子页面标题>/...    # 目录层级与知识库树一致
```

脚本退出码：全部成功为 0；存在任何页面或素材失败为 1（失败明细见 manifest.json，可用 `--retry-failures` 重试）。

### 常见错误排查

| 现象 | 原因 | 解决方案 |
| --- | --- | --- |
| 启动即提示「dws 未登录或 token 已过期」 | 未执行登录或 token 过期 | 运行 `dws auth login`，再用 `dws auth status` 确认 |
| `wiki node list` 报错 / 返回空 | 账号对该知识库无权限，或 workspaceId 写错 | 用 `dws wiki space list` 核对 ID；请管理员授予知识库访问权限 |
| 大量页面报 `doc read` 失败后走 `doc export` 且很慢 | 文档类型不支持快速读取，触发导出任务轮询（单篇最长约 5 分钟） | 属正常降级；可减小范围（`--root`）分批导出 |
| 日志出现「检测到限流」 | 触发钉钉接口限流（429 / too many requests） | 脚本会自动降并发、加大退避；也可手动调低 `--workers` 后用 `--retry-failures` 续跑 |
| 图片下载失败（URL 带 Expires 签名过期） | OSS 签名 URL 有时效 | 直接重跑 `--retry-failures`，脚本会重新读取文档获取新签名 |
