import { readFileSync, readdirSync } from "node:fs";
import { fileURLToPath } from "node:url";

import type { DefaultTheme } from "vitepress";

const route = (...segments: string[]): string =>
  encodeURI(`/greenbook/${segments.map((segment) => segment.trim()).join("/")}/`);

const part1 = "第一部分 使用手册：先把 千问办公 用起来";
const part2 = "第二部分 实战案例 从具体任务，走向AI Native";
const part3 = "第三部分 进阶使用案例";
const part4 = "第四部分 认知与方法论";

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

export const greenbookSidebar: DefaultTheme.Sidebar = {
  "/greenbook/": [
    { text: "绿皮书总览", link: "/greenbook/" },
    {
      text: "第一部分 · 使用手册",
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
            child(`${part1}/第6章 桌面端核心功能`, "6.13 工作台-写作"),
            child(`${part1}/第6章 桌面端核心功能`, "6.14 工作台-幻灯片"),
            child(`${part1}/第6章 桌面端核心功能`, "6.15 工作台-设计"),
          ],
        },
        child(part1, "第7章 概念普及：理解AI是怎么干活的"),
      ],
    },
    {
      text: "第二部分 · 实战案例",
      collapsed: false,
      items: [
        item(part2, "本篇导读"),
        child(part2, "实战指南｜Excel 表格数据处理"),
        child(part2, "实战指南｜4个场景教你用 千问办公 告别重复工作"),
        child(part2, "实战指南｜数据分析全流程实战教程"),
        child(part2, "实战指南｜5个技巧教你用 TRAE 做复杂数据分析"),
        child(part2, "【文档类】｜高效整理资料、加工文档"),
        child(part2, "【文档类】｜快速写好通知／请示／公告等材料"),
        child(part2, "电商运营-电商经营数据大屏「官方案例」"),
        child(part2, "自媒体-上传录音，克隆自己的声音做口播"),
        child(part2, "[实战案例]｜如何用 Remotion Skills 做视频"),
      ],
    },
    {
      text: "第三部分 · 进阶使用案例",
      collapsed: false,
      items: [
        item(part3, "本篇导读"),
        child(part3, "自媒体运营-公众号排版推送"),
        child(part3, "内容创作者｜从选题到复盘全流程"),
        child(part3, "内容创作者｜图片设计、生成和编辑"),
        child(part3, "[实战案例]｜从 UI 到可交付前端原型"),
        child(part3, "实战指南｜由需求直接生成原型图"),
      ],
    },
    {
      text: "第四部分 · 认知与方法论",
      collapsed: false,
      items: [
        item(part4, "本篇导读"),
        child(part4, "把真实任务变成 AI 工作流：一套可复用的方法论"),
        child(part4, "怎么写出一个skill"),
        child(part4, "【IP 配图 Skill 必看】全网独一份的架构详解"),
        child(part4, "【自媒体学 AI 必看】公众号排版 skill 详解"),
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
  ...greenbookSidebar,
  "/cases/": casesSidebar,
  "/community/case-contributing": casesSidebar,
};
