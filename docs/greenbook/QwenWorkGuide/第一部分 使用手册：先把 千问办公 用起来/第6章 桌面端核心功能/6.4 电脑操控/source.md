# <span style="color: rgb(73, 70, 65);">**6.4 电脑操控**</span>

<span style="color: rgb(73, 70, 65);">让 QwenWork 直接操作你电脑上的应用程序</span>

<span style="color: rgb(73, 70, 65);">除了在对话中处理文件和数据，QwenWork 还能直接"看到"和"操控"你的电脑屏幕——点击按钮、填写表单、切换应用。这项能力称为 Computer Use（电脑操控），它让 QwenWork 能完成那些需要在图形界面中操作的任务。</span>

## <span style="color: rgb(24, 24, 27);">**核心能力**</span>

<span style="color: rgb(73, 70, 65);">屏幕感知 — 读取目标应用窗口的可见内容，理解布局、按钮文字、表单状态等视觉信息。操作过程中持续截屏确认上一步是否成功，再决定下一步动作。</span>

<span style="color: rgb(73, 70, 65);">鼠标与键盘控制 — 支持完整的人类输入方式：点击、双击、拖拽、文字输入和键盘快捷键。操作精度达到像素级别，能准确点击小型 UI 元素。</span>

<span style="color: rgb(73, 70, 65);">后台自主执行 — 在后台驱动鼠标、键盘和截屏，不会抢占你的前台焦点。你可以继续使用电脑做其他事情，AI 在背后默默完成任务。</span>

<span style="color: rgb(73, 70, 65);">跨应用流程 — 在多个桌面应用之间切换，将多步操作串联成完整的工作流。根据实时反馈动态调整下一步，而非照搬固定脚本。</span>

## <span style="color: rgb(24, 24, 27);">**使用场景**</span>
- <span style="color: rgb(73, 70, 65);">操作没有 API 的桌面应用 — 当目标应用没有命令行或插件时，AI 直接操作图形界面。比如在设计工具中调参数、在管理后台批量修改设置。</span>
- <span style="color: rgb(73, 70, 65);">跨应用工作流 — 任务跨越多个应用时，AI 自动切换窗口、复制数据、填写表单，端到端完成。</span>
- <span style="color: rgb(73, 70, 65);">GUI 验证与测试 — 确认界面变更是否按预期工作，复现仅在 GUI 中出现的问题，或检查应用对特定操作序列的响应。</span>
- <span style="color: rgb(73, 70, 65);">信息收集整合 — 从没有导出功能的应用中提取数据，或汇总散落在多个应用中的信息。</span>

<span style="color: rgb(73, 70, 65);">对于网页任务，优先使用浏览器自动化——它比电脑操控更快更精准。</span>

## <span style="color: rgb(24, 24, 27);">**系统要求**</span>
- <span style="color: rgb(73, 70, 65);">macOS 14 或更高版本</span>
- <span style="color: rgb(73, 70, 65);">需要授予辅助功能和屏幕录制权限</span>

## <span style="color: rgb(24, 24, 27);">**使用方式**</span>

<span style="color: rgb(73, 70, 65);">在对话中直接描述需要在图形界面中完成的任务，QwenWork 会自动判断并启用电脑操控：</span>

<span style="color: rgb(80, 100, 127); background-color: rgb(248, 249, 251);">**示例**</span>

<span style="color: rgb(85, 81, 75); background-color: rgb(248, 249, 251);">打开系统偏好设置，截个屏让我看看当前的网络配置</span>

<span style="color: rgb(80, 100, 127); background-color: rgb(248, 249, 251);">**示例**</span>

<span style="color: rgb(85, 81, 75); background-color: rgb(248, 249, 251);">打开 Finder，在 Documents 文件夹中找到最近修改的 Excel 文件</span>

<span style="color: rgb(80, 100, 127); background-color: rgb(248, 249, 251);">**示例**</span>

<span style="color: rgb(85, 81, 75); background-color: rgb(248, 249, 251);">帮我在 Numbers 中打开"预算表.xlsx"，把 B 列的数字格式改为货币</span>

## <span style="color: rgb(24, 24, 27);">**开启电脑操控**</span>

<span style="color: rgb(73, 70, 65);">使用电脑操控前，需要先在连接器中开启「计算机控制」：</span>

<span style="color: rgb(73, 70, 65);">1\. 打开连接器</span>

<span style="color: rgb(73, 70, 65);">进入 扩展 → 连接器，找到「计算机控制」卡片并点击开启。</span>

![](https://alidocs2.oss-cn-zhangjiakou.aliyuncs.com/res/MAeqxe6KAm1aDO8j/img/4bc396ea-e810-488f-a480-6725e99961c7.webp?Expires=1785260307&OSSAccessKeyId=LTAI5tKTjg4Kq1HCdBJ8qpSp&Signature=fWMWNxKEoy6zwExl5IGnVodRlps%3D "")

<span style="color: rgb(161, 157, 150); background-color: rgb(248, 248, 247);">image.png</span>

<span style="color: rgb(73, 70, 65);">2\. 确认权限说明</span>

<span style="color: rgb(73, 70, 65);">弹窗会显示该连接器的能力说明：</span>
- <span style="color: rgb(73, 70, 65);">AI 增强工具 — 提供桌面自动化能力：点击、输入、滚动、截图等桌面操控工具</span>
- <span style="color: rgb(73, 70, 65);">始终遵守权限 — Computer Use 运行时会在需要时自行处理系统权限</span>
- <span style="color: rgb(73, 70, 65);">一切由你掌控 — 你可以随时在此弹窗关闭该连接器</span>

## <span style="color: rgb(24, 24, 27);">**系统权限授权**</span>

<span style="color: rgb(73, 70, 65);">开启连接器后，首次使用电脑操控时 QwenWork 会引导你授予两项系统权限：</span>

<span style="color: rgb(73, 70, 65);">1\. 辅助功能权限</span>

<span style="color: rgb(73, 70, 65);">让 QwenWork 能读取应用的 UI 元素树，并执行点击、输入等操作。在系统弹出的提示中允许即可。</span>

<span style="color: rgb(73, 70, 65);">2\. 屏幕录制权限</span>

<span style="color: rgb(73, 70, 65);">让 QwenWork 能截取应用窗口的屏幕画面，使 AI 能"看到"当前界面状态。在系统设置的「隐私与安全性」→「屏幕录制」中添加 QwenWork。</span>

<span style="color: rgb(73, 70, 65);">授权完成后，当 AI 尝试操控某个应用时，QwenWork 会征求你的确认。你可以在设置中选择执行策略：</span>

| <span style="color: rgb(39, 42, 38); background-color: rgb(245, 247, 243);">**策略**</span> | <span style="color: rgb(39, 42, 38); background-color: rgb(245, 247, 243);">**说明**</span> |
|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <span style="color: rgb(64, 61, 56);">每次询问（默认）</span> | <span style="color: rgb(64, 61, 56);">AI 每次需要操控桌面时都会先征求你的确认</span> |
| <span style="color: rgb(64, 61, 56);">自动执行</span> | <span style="color: rgb(64, 61, 56);">AI 直接执行桌面操作，无需逐次确认</span> |
| <span style="color: rgb(64, 61, 56);">禁用</span> | <span style="color: rgb(64, 61, 56);">完全关闭电脑操控功能</span> |

## <span style="color: rgb(24, 24, 27);">**操作过程**</span>

<span style="color: rgb(73, 70, 65);">当 QwenWork 执行电脑操控时，你会在对话中看到完全透明的操作流程：</span>
1. <span style="color: rgb(73, 70, 65);">截屏 — AI 截取当前屏幕画面来了解界面状态</span>
2. <span style="color: rgb(73, 70, 65);">操作描述 — 每一步操作前说明即将做什么</span>
3. <span style="color: rgb(73, 70, 65);">实际操作 — 执行点击、输入、滚动等动作</span>
4. <span style="color: rgb(73, 70, 65);">结果确认 — 操作后再次截屏确认结果是否符合预期</span>

<span style="color: rgb(73, 70, 65);">电脑操控过程中，避免手动操作当前被 AI 控制的应用或窗口——你的操作可能与 AI 的动作冲突。等 AI 完成当前步骤后再介入。</span>

## <span style="color: rgb(24, 24, 27);">**典型场景**</span>

### <span style="color: rgb(24, 24, 27);">**从应用中提取数据**</span>

<span style="color: rgb(80, 100, 127); background-color: rgb(248, 249, 251);">**示例**</span>

<span style="color: rgb(85, 81, 75); background-color: rgb(248, 249, 251);">打开 Mac 的活动监视器，帮我查看当前占用 CPU 和内存最多的 5 个进程， 把结果整理成表格</span>

### <span style="color: rgb(24, 24, 27);">**系统设置调整**</span>

<span style="color: rgb(80, 100, 127); background-color: rgb(248, 249, 251);">**示例**</span>

<span style="color: rgb(85, 81, 75); background-color: rgb(248, 249, 251);">帮我检查一下系统是否开启了自动更新， 如果没有就帮我打开</span>

### <span style="color: rgb(24, 24, 27);">**跨应用信息整合**</span>

<span style="color: rgb(80, 100, 127); background-color: rgb(248, 249, 251);">**示例**</span>

<span style="color: rgb(85, 81, 75); background-color: rgb(248, 249, 251);">查看我的日历中今天的所有会议安排， 然后在备忘录中创建一个"今日会议准备"笔记， 列出每个会议的时间和我需要准备的内容</span>

## <span style="color: rgb(24, 24, 27);">**使用建议**</span>

<span style="color: rgb(73, 70, 65);">描述清楚目标应用和路径</span>

<span style="color: rgb(73, 70, 65);">告诉 QwenWork 要操作哪个应用、去哪个位置，比"帮我设置一下"要清晰得多。</span>

<span style="color: rgb(73, 70, 65);">分步骤下达复杂指令</span>

<span style="color: rgb(73, 70, 65);">如果操作步骤很多，可以分几次告诉 AI——先做第一步，确认无误后再继续。</span>

<span style="color: rgb(73, 70, 65);">配合 Skill 实现自动化</span>

<span style="color: rgb(73, 70, 65);">经常重复的界面操作流程，可以保存为</span>  [Skill](https://docs.qoder.com/zh/qoderwork/skills)<span style="color: rgb(73, 70, 65);">，以后一句话就能触发整个流程。</span>

## <span style="color: rgb(24, 24, 27);">**注意事项**</span>

<span style="color: rgb(73, 70, 65);">授予访问权限意味着授予操控权限。启用后，AI 能以你的身份驱动电脑上的其他应用，效果等同于你本人操作。不需要时请在设置中禁用。</span>
- <span style="color: rgb(73, 70, 65);">部分操作不可撤销 — AI 在桌面应用中执行的操作（如发送消息、删除文件）可能无法撤回。对于高风险场景，建议使用「每次询问」策略。</span>
- <span style="color: rgb(73, 70, 65);">屏幕内容会被截取 — AI 通过截屏感知界面，屏幕上可见的任何内容（包括敏感信息）都可能被捕获。运行自动化前请关闭含密码或私密数据的窗口。</span>
- <span style="color: rgb(73, 70, 65);">网络操作谨慎 — 如果 AI 操作了含有你登录状态的应用，它可以代你发送邮件、提交表单等。对此类操作保持警惕。</span>

## <span style="color: rgb(24, 24, 27);">**使用限制**</span>
- <span style="color: rgb(73, 70, 65);">验证码和二步验证 — AI 无法完成 CAPTCHA、短信验证码、人脸识别等操作，需要你手动介入。</span>
- <span style="color: rgb(73, 70, 65);">速度 — 电脑操控需要截屏和分析画面，比纯文本操作慢。</span>
- <span style="color: rgb(73, 70, 65);">精确度 — 界面复杂或元素密集时，AI 的点击精度可能不够高。如果操作失败，尝试描述得更具体。</span>



<span style="color: rgb(73, 70, 65); background-color: rgb(245, 247, 240);">***来源：千文办公 官方指南。***</span>
