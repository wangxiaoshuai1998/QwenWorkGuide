import { readFileSync, readdirSync } from "node:fs";
import { fileURLToPath } from "node:url";

import type { DefaultTheme } from "vitepress";

const route = (...segments: string[]): string =>
  encodeURI(`/bluebook/${segments.map((segment) => segment.trim()).join("/")}/`);

const part1 = "第一篇 使用手册：先把 千问办公 用起来";

const item = (directory: string, text = directory): DefaultTheme.SidebarItem => ({
  text,
  link: route(directory),
});

const child = (
  parent: string,
  directory: string,
  text = directory,
): DefaultTheme.SidebarItem => ({
  text,
  link: route(parent, directory),
});

export const bluebookSidebar: DefaultTheme.Sidebar = {
  "/bluebook/": [
    { text: "绿皮书总览", link: "/bluebook/" },
    {
      text: "第一篇 · 使用手册",
      collapsed: false,
      items: [
        item(part1, "本篇导读"),
        child(part1, "第1章 初识 千问办公"),
        child(part1, "第2章 Web端使用链路"),
        child(part1, "第3章 桌面端使用链路"),
        child(part1, "第4章 通用设置"),
        child(part1, "第5章 网页端核心功能"),
        {
          text: "第6章 桌面端核心功能",
          link: route(part1, "第6章 桌面端核心功能"),
          collapsed: false,
          items: [
            child(`${part1}/第6章 桌面端核心功能`, "6.1 系统设置"),
            child(`${part1}/第6章 桌面端核心功能`, "6.2 意识"),
            child(`${part1}/第6章 桌面端核心功能`, "6.3 应用快照"),
            child(`${part1}/第6章 桌面端核心功能`, "6.4 电脑操控"),
            child(`${part1}/第6章 桌面端核心功能`, "6.5 模型选择"),
            child(`${part1}/第6章 桌面端核心功能`, "6.6 语音输入"),
            child(`${part1}/第6章 桌面端核心功能`, "6.7 IM 频道"),
            child(`${part1}/第6章 桌面端核心功能`, "6.8 定时任务"),
            child(`${part1}/第6章 桌面端核心功能`, "6.9 Hooks"),
            child(`${part1}/第6章 桌面端核心功能`, "6.10 连接器"),
            child(`${part1}/第6章 桌面端核心功能`, "6.11 技能"),
            child(`${part1}/第6章 桌面端核心功能`, "6.12 专家套件"),
          ],
        },
      ],
    },
  ],
};

const casesDirectory = fileURLToPath(
  new URL("../cases/submissions/", import.meta.url),
);

const caseItems = readdirSync(casesDirectory, { withFileTypes: true })
  .filter((entry) => entry.isDirectory())
  .map((entry) => {
    const markdown = readFileSync(
      new URL(`../cases/submissions/${entry.name}/index.md`, import.meta.url),
      "utf8",
    );
    const frontmatter = markdown.match(/^---\s*\n([\s\S]*?)\n---/)?.[1] || "";
    const readField = (field: string): string =>
      frontmatter
        .match(new RegExp(`^${field}:\\s*(.+)$`, "m"))?.[1]
        ?.trim()
        .replace(/^['"]|['"]$/g, "") || "";

    return {
      date: readField("date"),
      item: {
        text: readField("title") || entry.name,
        link: encodeURI(`/cases/submissions/${entry.name}/`),
      } satisfies DefaultTheme.SidebarItem,
    };
  })
  .sort((left, right) => left.date.localeCompare(right.date))
  .map(({ item: caseItem }) => caseItem);

const casesSidebar: DefaultTheme.SidebarItem[] = [
  { text: "案例集首页", link: "/cases/" },
  { text: "如何提交 Case", link: "/community/case-contributing" },
  {
    text: "社区 Case",
    collapsed: false,
    items: caseItems,
  },
];

export const siteSidebar: DefaultTheme.Sidebar = {
  ...bluebookSidebar,
  "/cases/": casesSidebar,
  "/community/case-contributing": casesSidebar,
};
