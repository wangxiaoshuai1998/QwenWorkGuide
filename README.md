<p align="center">
  <a href="https://github.com/OWNER/QwenWorkGuide">
    <img src="./assets/workbuddy-guide-banner.png" alt="千问办公绿皮书：首页预览" width="100%">
  </a>
</p>

<h1 align="center">千问办公绿皮书</h1>

<p align="center"><strong>千问办公中文使用手册与实战指南（QwenWork Guide）</strong></p>

<p align="center">
  简体中文 · <a href="./README_en.md">English</a> ·
  <a href="https://github.com/OWNER/QwenWorkGuide">在线阅读</a> ·
  <a href="https://github.com/OWNER/QwenWorkGuide/tree/main/docs/cases">社区案例集</a> ·
  <a href="https://github.com/OWNER/QwenWorkGuide/tree/main/docs/help">帮你解决</a> ·
  <a href="./docs/reading-guide.md">阅读指南</a> ·
  <a href="./CONTRIBUTING.md">参与共创</a>
</p>

> 这不是官方功能说明书的改写，而是一本以真实任务为主线的实战读本。当前内容为第一篇「使用手册」（篇导读 + 第 1～4 章），帮你从初识千问办公开始，跑通 Web 端与桌面端的完整使用链路，并把账号设置调到最顺手；后续篇章持续更新。

## 项目背景

本项目源自开源项目 WorkBuddy Bluebook（[AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)），在其站点框架基础上重构为「千问办公绿皮书」。正文内容基于钉钉知识库导出，围绕千问办公的真实使用链路编写与维护。

## 在线阅读

推荐访问 **[OWNER/QwenWorkGuide](https://github.com/OWNER/QwenWorkGuide)** 阅读。网站提供完整侧边栏、全文搜索、章节目录、深色模式、流程图和移动端适配。

GitHub 适合了解项目和参与贡献；真正阅读绿皮书时，网站体验更完整。

## 你会在这里看到什么

当前已上线 **第一篇 · 使用手册（篇导读 + 第 1～4 章）**，后续篇章持续更新：

| 章节 | 内容 |
| --- | --- |
| 篇导读 | 阅读路线、章节总览与学习目标 |
| 第 1 章 初识千问办公 | 核心能力、与传统 AI 对话的区别、典型使用场景 |
| 第 2 章 Web 端使用链路 | 登录进入、创建任务、多轮沟通、网盘与网页发布 |
| 第 3 章 桌面端使用链路 | 下载安装、登录账号、熟悉界面并提交第一个本地任务 |
| 第 4 章 通用设置 | 个人资料、语言与外观、订阅及积分使用管理 |

## 推荐阅读方式

- **第一次使用**：从[第 1 章](./docs/bluebook/第一篇%20使用手册：先把%20千问办公%20用起来/第1章%20初识%20千问办公/index.md)开始，按顺序读完第一篇。
- **想直接上手**：先看第 2 章（Web 端）或第 3 章（桌面端），跑通第一个任务后再回头补齐其他章节。
- **关注后续内容**：案例篇、进阶篇等后续篇章会持续更新，欢迎 Watch 本仓库或关注[社区案例集](https://github.com/OWNER/QwenWorkGuide/tree/main/docs/cases)。

更完整的路线见[如何阅读这本绿皮书](./docs/reading-guide.md)。

## 帮你解决

如果你有真实的工作场景，却不知道怎样用千问办公完成，可以前往 **[帮你解决](https://github.com/OWNER/QwenWorkGuide/tree/main/docs/help)** 提交场景问卷。

请在问卷中说明你遇到的问题、目前的处理方式、会用到的资料、期望结果和安全边界。我们会阅读并评估每一份需求；如果需要补充信息，会通过你主动留下的联系方式与你沟通。

具有代表性和复用价值的问题，我们会尝试制作成完整的开源 Case，写清所用 Skill、安装与使用方法、任务描述、操作过程和最终效果，并发布到[社区案例集](https://github.com/OWNER/QwenWorkGuide/tree/main/docs/cases)，帮助更多遇到类似问题的人。

## 本地阅读与开发

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

## 参与共创

我们优先收集真实、可复现的千问办公使用案例。提交 Case 前，请先搜索[社区案例集](https://github.com/OWNER/QwenWorkGuide/tree/main/docs/cases)和[绿皮书目录](https://github.com/OWNER/QwenWorkGuide/tree/main/docs/bluebook)，确认场景或任务没有重复。若目标相同但使用了不同的 Skill、方法或交付形式，请在 PR 中说明差异。

每个案例至少需要写清：

- **场景与问题**：谁在什么任务中遇到了什么困难。
- **使用的 Skill**：Skill 的作用、来源、安装方式和必要配置。
- **任务描述**：在千问办公中输入的提示词、步骤或自动化设置。
- **执行过程**：关键操作、权限要求、输入资料和安全边界。
- **实际效果**：使用截图或其他结果证明展示最终输出。
- **验收标准**：怎样判断任务已经正确完成。

投稿时，在 `docs/cases/submissions/` 下为案例新建独立目录，使用 [Case 正文模板](./.github/CASE_TEMPLATE.md)编写内容，并通过 [Case PR 模板](./.github/PULL_REQUEST_TEMPLATE/case.md)提交。审核合并后，案例会自动出现在网站左侧目录；具有代表性的经典案例经过进一步复现和编辑后，可能进入绿皮书正式章节。

完整流程请阅读 [Case 投稿指南](https://github.com/OWNER/QwenWorkGuide/blob/main/docs/community/case-contributing.md)和[贡献指南](./CONTRIBUTING.md)。准备或提交 PR 后，也可以按网站提示加入共创群，交流选题并获得内容完善建议。

## 目录结构

```text
QwenWorkGuide
├─ .github/
│  ├─ CASE_TEMPLATE.md             # Case 正文模板
│  └─ PULL_REQUEST_TEMPLATE/       # Pull Request 模板
├─ docs/
│  ├─ .vitepress/                  # 网站配置、主题、导航与 SEO
│  ├─ bluebook/                    # 绿皮书正式章节
│  ├─ cases/
│  │  └─ submissions/              # 社区提交的独立 Case
│  ├─ community/                   # Case 投稿与社区共创指南
│  ├─ help/                        # “帮你解决”场景问卷页面
│  ├─ public/                      # 网站图片、二维码等静态资源
│  ├─ index.md                     # 网站首页
│  └─ reading-guide.md             # 阅读指南
├─ scripts/                        # 钉钉知识库导出与辅助工具
├─ CONTRIBUTING.md                 # 完整贡献规范
├─ README.md                       # 中文项目说明
└─ README_en.md                    # English README
```

## 部署

本站使用 **VitePress + Cloudflare Pages + GitHub**。Cloudflare Pages 连接本仓库的 `main` 分支后，每次推送都会自动构建部署。配置见 [DEPLOYMENT.md](./DEPLOYMENT.md)。

## 作者们

感谢以下作者共同参与上游《WorkBuddy 蓝皮书》（[AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)）的创作与维护。点击名片可查看原图并扫描二维码。

<p align="center">
  <a href="./assets/authors/jia-mu-wei-lai-pai.png"><img src="./assets/authors/jia-mu-wei-lai-pai.png" alt="甲木未来派" width="48%"></a>
  <a href="./assets/authors/mo-yu-xiao-li.png"><img src="./assets/authors/mo-yu-xiao-li.png" alt="摸鱼小李" width="48%"></a>
</p>

<p align="center">
  <a href="./assets/authors/dai-shu-di-ai-ke-zhan.png"><img src="./assets/authors/dai-shu-di-ai-ke-zhan.png" alt="袋鼠帝AI客栈" width="48%"></a>
  <a href="./assets/authors/cang-he.png"><img src="./assets/authors/cang-he.png" alt="苍何" width="48%"></a>
</p>

<p align="center">
  <a href="./assets/authors/liu-cong-nlp.png"><img src="./assets/authors/liu-cong-nlp.png" alt="刘聪NLP" width="48%"></a>
</p>

## 声明

本项目是社区维护的千问办公实战知识库。涉及产品功能、界面、价格、可用范围和安全策略等时效性信息时，请以千问办公官方渠道为准。


## 开源协议

本项目采用 [MIT License](./LICENSE) 开源。你可以自由使用、复制、修改和分发本项目，但需要保留原始版权声明和许可证文本。
