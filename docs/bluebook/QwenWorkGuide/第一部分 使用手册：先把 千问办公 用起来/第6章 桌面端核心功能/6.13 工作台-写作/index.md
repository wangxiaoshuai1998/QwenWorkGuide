# **6.13 工作台-写作**

# **写作**

写作工作台是面向长文场景的垂类工作台——文章、报告、推文、技术指南、内部文档皆可。Agent 生成的产物会以 Markdown 文件的形式落到本地  `outputs/`  目录，每一轮迭代都会保留为可回溯的版本；你可以随时切到 编辑 模式直接改正文，Agent 在后续轮次会基于你的修改继续。

## **工作区**

![](./assets/001_be195fae-cac5-4fcd-b72c-add93476b35b.webp)

Document 工作区把 Markdown 文件树和编辑器组合在一起：

| <span style="color: rgb(39, 42, 38); background-color: rgb(245, 247, 243);">**元素**</span> | <span style="color: rgb(39, 42, 38); background-color: rgb(245, 247, 243);">**用途**</span> |
|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| 文件树 | 产出以 Markdown 文件组织（`outputs/your-doc.md`）。顶部搜索框按名称过滤，文件夹图标可打开所在目录 |
| 编辑器 | 文档正文，右上角有 只读 / 编辑 切换、最新版本 工作区文件 选择器（可在多个版本之间切换）和 导出（导出为 PDF 文件） |

## **创建文档**

切换到写作工作台

在输入框点击工作台切换器（默认 通用），选 写作。

![](./assets/002_4854a8bc-bb93-4d33-bc90-7f5a6331621a.webp)

<span style="color: rgb(80, 100, 127); background-color: rgb(248, 249, 251);">**示例**</span>

<span style="color: rgb(85, 81, 75); background-color: rgb(248, 249, 251);">默认工作台可以在 QwenWork 设置里调整——主要做长文写作时，把"写作"设为默认更顺手。</span>

描述需求

描述主题、受众、调性、要点。如有需要可以点击麦克风使用  [语音输入](https://qwenwork.cn/docs/features/voice-input)。切换到写作工作台后，输入框下方会出现「\\*\\*选择工作目录\\*\\*」和「\\*\\*语气\\*\\*」两个可选项，可在描述任务时按需配置。

![](./assets/003_a58b5050-e28a-442e-8c27-5590842e2985.webp)

挑选语气、固定工作目录（可选）
- 点击「语气」按钮，可在 不指定语气 / 正式 / 轻松 / 技术 / 创意 之间选一种作为整体调性；不选时由 Agent 自行判断。
- 点击「选择工作目录」可把任务绑定到本地一个目录——Agent 在该目录下读写文件，把过程沉淀到磁盘。适合需要长期迭代或与现有素材结合的文档。

![](./assets/004_b17c835a-c73f-4cae-9b0e-eeace70b7bc6.webp)

阅读或编辑文档

产物会落到 outputs/ 目录下的 Markdown 文件中。切换到 只读 阅读渲染后的 Markdown，切换到 编辑 直接修改正文。

![](./assets/005_979764de-8285-4830-8ff6-86ea560613fb.webp)

## **继续迭代**
- 追加任务：在底部输入框追加指令，例如  *"补一节关于权限的内容"*——Agent 会就地更新文件中相应位置。
- 打断当前生成：输入框旁的停止按钮可以中断生成。
- 对比版本：用 最新版本 工作区文件 下拉在最新版与早期版本之间切换，多轮迭代后比较思路时尤其有用。
- 直接动手改：切换到 编辑 自己改一句或重写一段，Agent 在后续轮次会基于你的修改继续。
- 中途切换模型：模型下拉可以为下一步切换模型。

<span style="color: rgb(80, 100, 127); background-color: rgb(248, 249, 251);">**示例**</span>

<span style="color: rgb(85, 81, 75); background-color: rgb(248, 249, 251);">受众越明确，初稿越准。</span><span style="color: rgb(85, 81, 75); background-color: rgb(248, 249, 251);">*"给平台团队的内部复盘，聚焦经验教训、不追责"*</span>  <span style="color: rgb(85, 81, 75); background-color: rgb(248, 249, 251);">比</span>  <span style="color: rgb(85, 81, 75); background-color: rgb(248, 249, 251);">*"把这次故障写一下"*</span>  <span style="color: rgb(85, 81, 75); background-color: rgb(248, 249, 251);">效果好得多。</span>

## **导出成果**

点击右上角 导出 即可将当前文档导出为 PDF 文件，也可以把渲染后的文本直接复制到下游工具——文档系统、博客 CMS、内部 wiki 或聊天软件均可。

## **典型场景**

### **把零散笔记变成技术指南**

<span style="color: rgb(154, 100, 27); background-color: rgb(252, 250, 246);">**注意**</span>

<span style="color: rgb(85, 81, 75); background-color: rgb(252, 250, 246);">@oss-notes.md 把这份零散笔记整理成面向阿里云 OSS 新手的技术指南。 覆盖核心概念、存储类型、权限管理、上传下载机制、生命周期、监控 和最佳实践。需要带上代码示例和对比表格。</span>

### **起草内部复盘**

<span style="color: rgb(155, 93, 7); background-color: rgb(255, 249, 237);">**说明**</span>

<span style="color: rgb(108, 87, 55); background-color: rgb(255, 249, 237);">@incident-2026-05-19-timeline.md @slack-thread.txt 为 5 月 19 日的故障起草一份无追责的复盘文档。 章节：摘要、影响、时间线、根因、做得好的地方、做得不好的地方、 带 owner 的行动项。语气：中立、就事论事。</span>

### **由 PR 列表生成发布说明**

<span style="color: rgb(155, 93, 7); background-color: rgb(255, 249, 237);">**说明**</span>

<span style="color: rgb(108, 87, 55); background-color: rgb(255, 249, 237);">@merged-prs-2026-w20.md 基于这些 PR 写一份面向客户的发布说明。 按 Features / Improvements / Fixes 分组，每条一句简短的描述， 强调对用户的实际影响。</span>

### **撰写技术博客**

<span style="color: rgb(155, 93, 7); background-color: rgb(255, 249, 237);">**说明**</span>

<span style="color: rgb(108, 87, 55); background-color: rgb(255, 249, 237);">写一篇关于"如何用 QwenWork 构建自动化数据分析流水线"的技术博客。 受众：有一定技术背景的产品经理和数据分析师。 结构：引子（痛点）→ 方案概览 → 分步教程（带截图占位）→ 效果展示 → 总结与延伸阅读。 字数控制在 1500-2500 字，语气专业但不晦涩。</span>

### **产品用户文档**

<span style="color: rgb(155, 93, 7); background-color: rgb(255, 249, 237);">**说明**</span>

<span style="color: rgb(108, 87, 55); background-color: rgb(255, 249, 237);">@api-spec.yaml 基于这份 API 规范，为开发者写一份集成指南。 包含：概述、鉴权方式、快速开始（cURL 示例）、 核心接口说明（请求/响应示例）、错误码表、FAQ。 风格参照 Stripe 文档：简洁、示例驱动。</span>



<span style="color: rgb(73, 70, 65); background-color: rgb(245, 247, 240);">***来源：千文办公 官方指南。***</span>
