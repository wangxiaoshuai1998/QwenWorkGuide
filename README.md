<p align="center">
  <a href="https://qwenwork.ink/greenbook/">
    <img src="./assets/qwenwork-guide-banner.png" alt="千问办公绿皮书：首页预览" width="100%">
  </a>
</p>

<h1 align="center">千问办公绿皮书</h1>

<p align="center"><strong>千问办公中文使用手册与实战指南（QwenWork Greenbook）</strong></p>

<p align="center">
  简体中文 · <a href="./README_en.md">English</a> ·
  <a href="https://qwenwork.ink/greenbook/">在线阅读</a> ·
  <a href="https://github.com/wangxiaoshuai1998/QwenWorkGuide/tree/main/docs/cases">社区案例集</a> ·
  <a href="https://github.com/wangxiaoshuai1998/QwenWorkGuide/tree/main/docs/help">帮你解决</a> ·
  <a href="./docs/reading-guide.md">阅读指南</a> ·
  <a href="https://github.com/wangxiaoshuai1998/QwenWorkGuide/blob/main/CONTRIBUTING.md">参与共创</a>
</p>

> 这不是官方功能说明书的改写，而是一本以真实任务为主线的实战读本。全书分为四部分：使用手册、实战案例、进阶使用案例、认知与方法论，帮你从初识千问办公到掌握 AI 工作流方法论。

## 项目背景

本项目源自开源项目 QwenWork Greenbook（[wangxiaoshuai1998/QwenWorkGuide](https://github.com/wangxiaoshuai1998/QwenWorkGuide)），在其站点框架基础上重构为「千问办公绿皮书」。正文内容基于钉钉知识库导出，围绕千问办公的真实使用链路编写与维护。

## 在线阅读

推荐访问 **[qwenwork.ink/greenbook](https://qwenwork.ink/greenbook/)** 阅读。网站提供完整侧边栏、全文搜索、章节目录、深色模式、流程图和移动端适配。

GitHub 适合了解项目和参与贡献；真正阅读绿皮书时，网站体验更完整。

## 你会在这里看到什么

全书分为四部分，内容持续更新：

| 部分 | 内容 |
| --- | --- |
| 第一部分 · 使用手册 | 初识千问办公、Web 端与桌面端使用链路、通用设置、网页端与桌面端核心功能、概念普及（共 7 章） |
| 第二部分 · 实战案例 | Excel 数据处理、数据分析全流程、文档整理与写作、电商数据大屏、声音克隆、Remotion 视频等 |
| 第三部分 · 进阶使用案例 | 公众号排版推送、内容创作全流程、图片设计生成、UI 到前端原型、需求生成原型图等 |
| 第四部分 · 认知与方法论 | AI 工作流方法论、如何写 Skill、IP 配图架构详解、公众号排版 Skill 详解 |

## 推荐阅读方式

- **第一次使用**：从第一部分第 1 章开始，按顺序读完使用手册。
- **想直接上手**：先看第 2 章（Web 端）或第 3 章（桌面端），跑通第一个任务后再回头补齐其他章节。
- **想看实战案例**：直接前往第二部分或第三部分，选择感兴趣的方向。
- **想提升认知**：阅读第四部分的方法论和 Skill 详解。
- **关注后续内容**：各部分持续更新，欢迎 Watch 本仓库或关注[社区案例集](https://github.com/wangxiaoshuai1998/QwenWorkGuide/tree/main/docs/cases)。

更完整的路线见[如何阅读这本绿皮书](./docs/reading-guide.md)。

## 帮你解决

如果你有真实的工作场景，却不知道怎样用千问办公完成，可以前往 **[帮你解决](https://github.com/wangxiaoshuai1998/QwenWorkGuide/tree/main/docs/help)** 提交场景问卷。

请在问卷中说明你遇到的问题、目前的处理方式、会用到的资料、期望结果和安全边界。我们会阅读并评估每一份需求；如果需要补充信息，会通过你主动留下的联系方式与你沟通。

具有代表性和复用价值的问题，我们会尝试制作成完整的开源 Case，写清所用 Skill、安装与使用方法、任务描述、操作过程和最终效果，并发布到[社区案例集](https://github.com/wangxiaoshuai1998/QwenWorkGuide/tree/main/docs/cases)，帮助更多遇到类似问题的人。

## 技术栈

- **VitePress** v1.6.4 — 静态网站生成引擎
- **Vue 3** — 前端渲染基础（由 VitePress 隐式依赖）
- **Mermaid** — 流程图与图表渲染
- **Algolia DocSearch** — 站内搜索
- **Node.js** 22（推荐）

## 本地开发

需要 Node.js 20～24，推荐 Node.js 22。

```bash
npm install
npm run dev
```

本地构建：

```bash
npm run docs:build
npm run docs:preview
```

## 部署

本站使用 **VitePress + Cloudflare Pages + GitHub Pages** 部署。

- **Cloudflare Pages**：连接仓库 `main` 分支，每次推送自动构建部署
- **构建命令**：`npm run docs:build`
- **输出目录**：`docs/.vitepress/dist`
- **Node.js 版本**：22

详细配置见 [DEPLOYMENT.md](./DEPLOYMENT.md)。

## 参与共创

我们优先收集真实、可复现的千问办公使用案例。提交 Case 前，请先搜索[社区案例集](https://github.com/wangxiaoshuai1998/QwenWorkGuide/tree/main/docs/cases)和[绿皮书目录](https://github.com/wangxiaoshuai1998/QwenWorkGuide/tree/main/docs/greenbook)，确认场景或任务没有重复。若目标相同但使用了不同的 Skill、方法或交付形式，请在 PR 中说明差异。

每个案例至少需要写清：

- **场景与问题**：谁在什么任务中遇到了什么困难。
- **使用的 Skill**：Skill 的作用、来源、安装方式和必要配置。
- **任务描述**：在千问办公中输入的提示词、步骤或自动化设置。
- **执行过程**：关键操作、权限要求、输入资料和安全边界。
- **实际效果**：使用截图或其他结果证明展示最终输出。
- **验收标准**：怎样判断任务已经正确完成。

投稿时，在 `docs/cases/submissions/` 下为案例新建独立目录，使用 [Case 正文模板](./.github/CASE_TEMPLATE.md)编写内容，并通过 [Case PR 模板](./.github/PULL_REQUEST_TEMPLATE/case.md)提交。审核合并后，案例会自动出现在网站左侧目录；具有代表性的经典案例经过进一步复现和编辑后，可能进入绿皮书正式章节。

完整流程请阅读 [Case 投稿指南](https://github.com/wangxiaoshuai1998/QwenWorkGuide/blob/main/docs/community/case-contributing.md)和[贡献指南](https://github.com/wangxiaoshuai1998/QwenWorkGuide/blob/main/CONTRIBUTING.md)。

## 社区交流

加入千问办公交流联系（备注：千问办公 共创），联系人 **wangxiaoshuai**。

准备或提交 PR 后，也可以按网站提示进行交流联系，交流选题并获得内容完善建议。

如有问题或建议，欢迎前往 [Issues](https://github.com/wangxiaoshuai1998/QwenWorkGuide/issues) 提交。

## 目录结构

```text
QwenWorkGuide
├─ .github/
│  ├─ CASE_TEMPLATE.md             # Case 正文模板
│  └─ PULL_REQUEST_TEMPLATE/       # Pull Request 模板
├─ docs/
│  ├─ .vitepress/                  # 网站配置、主题、导航与 SEO
│  ├─ greenbook/                    # 绿皮书正式章节（四部分）
│  ├─ cases/
│  │  └─ submissions/              # 社区提交的独立 Case
│  ├─ community/                   # Case 投稿与社区共创指南
│  ├─ help/                        # "帮你解决"场景问卷页面
│  ├─ public/                      # 网站图片、二维码等静态资源
│  ├─ index.md                     # 网站首页
│  └─ reading-guide.md             # 阅读指南
├─ scripts/                        # 钉钉知识库导出与辅助工具
├─ CONTRIBUTING.md                 # 完整贡献规范
├─ README.md                       # 中文项目说明
└─ README_en.md                    # English README
```

## 作者们

感谢以下作者共同参与上游《千问办公绿皮书》（[wangxiaoshuai1998/QwenWorkGuide](https://github.com/wangxiaoshuai1998/QwenWorkGuide)）的创作与维护。点击名片可查看原图并扫描二维码。

<p align="center">
  <a href="./assets/authors/wangxiaoshuai.jpg"><img src="./assets/authors/wangxiaoshuai.jpg" alt="王小帅" width="48%"></a>
</p>

## 声明

本项目是社区维护的千问办公实战知识库。涉及产品功能、界面、价格、可用范围和安全策略等时效性信息时，请以千问办公官方渠道为准。

## 开源协议

本项目采用 [MIT License](./LICENSE) 开源。你可以自由使用、复制、修改和分发本项目，但需要保留原始版权声明和许可证文本。
