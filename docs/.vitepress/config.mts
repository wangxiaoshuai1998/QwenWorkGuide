import { defineConfig } from "vitepress";

import { siteSidebar } from "./sidebar";
import { configureMermaidMarkdown } from "./mermaid-markdown";
import { createPageDescription, createSeoHead } from "./seo";

const siteUrl = process.env.VITEPRESS_SITE_URL || "https://qwenwork.guide";
const base = process.env.VITEPRESS_BASE || "/";

export default defineConfig({
    base,
    lang: "zh-CN",
    title: "千问办公绿皮书",
    titleTemplate: ":title · 千问办公绿皮书",
    description: "千问办公中文使用手册与实战指南：涵盖产品初识、Web 端与桌面端使用链路、通用设置。",
    cleanUrls: true,
    lastUpdated: true,
    srcExclude: ["**/source.md", "plans/**"],
    sitemap: {
      hostname: siteUrl,
    },
    transformPageData: (pageData, { siteConfig }) => {
      if (pageData.relativePath.startsWith("cases/")) {
        pageData.frontmatter.aside = false;
        pageData.frontmatter.outline = false;
      }

      return {
        description: createPageDescription(siteConfig.srcDir, pageData),
      };
    },
    transformHead: (context) => createSeoHead(siteUrl, context),
    head: [
      ["link", { rel: "icon", type: "image/png", href: "/favicon.png" }],
      ["meta", { name: "theme-color", content: "#4add86" }],
      ["meta", { name: "author", content: "QwenWork Guide Contributors" }],
      [
        "meta",
        {
          name: "baidu-site-verification",
          content: "codeva-RF1ZqL4g90",
        },
      ],
      [
        "meta",
        {
          name: "keywords",
          content:
            "千问办公,QwenWork,QwenWork Guide,AI 办公,AI Agent,AI 工作系统,自动化,职场 AI"
        },
      ],
    ],
    markdown: {
      config: configureMermaidMarkdown,
      image: {
        lazyLoading: true,
      },
      theme: {
        light: "github-light",
        dark: "github-dark",
      },
    },
    themeConfig: {
      siteTitle: "QwenWork Guide",
      nav: [
        { text: "首页", link: "/" },
        { text: "开始阅读", link: "/bluebook/" },
        { text: "案例集", link: "/cases/" },
        { text: "帮你解决", link: "/help/" },
        { text: "阅读指南", link: "/reading-guide" },
        {
          text: "交流联系",
          items: [{ component: "GroupQrMenu" }],
        },
      ],
      sidebar: siteSidebar,
      socialLinks: [
        { icon: "github", link: "https://github.com/wangxiaoshuai1998/QwenWorkGuide" },
      ],
      search: {
        provider: "local",
      },
      outline: {
        level: [2, 3],
        label: "本页目录",
      },
      docFooter: {
        prev: "上一篇",
        next: "下一篇",
      },
      lastUpdated: {
        text: "最后更新",
        formatOptions: {
          dateStyle: "medium",
          timeStyle: "short",
        },
      },
      editLink: {
        pattern: "https://github.com/wangxiaoshuai1998/QwenWorkGuide/edit/main/docs/:path",
        text: "在 GitHub 上改进此页",
      },
      footer: {
        message:
          '以真实任务为主线的千问办公社区实战读本 · Pixel icons by <a href="https://pixeliconlibrary.com/" target="_blank" rel="noreferrer">HackerNoon</a>',
        copyright: "Copyright © 2026 QwenWork Guide Contributors",
      },
    },
  });
