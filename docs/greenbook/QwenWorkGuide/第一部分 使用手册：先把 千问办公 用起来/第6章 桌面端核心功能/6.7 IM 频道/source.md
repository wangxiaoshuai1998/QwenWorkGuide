# <span style="color: rgb(73, 70, 65);">**6.7 IM 频道**</span>

<span style="color: rgb(73, 70, 65);">QwenWork 默认在桌面端完成对话和任务。但你的工作沟通大多发生在 IM 里——打开 IM 频道，QwenWork 就能接入你常用的聊天工具。走在路上、开会间隙，随手在 IM 里 @一下，AI 就能帮你跑任务、查数据、整理文档，结果直接回到当前聊天窗口。</span>

<span style="color: rgb(73, 70, 65);">桌面端依然是管控中心：所有 IM 会话在桌面端都有对应的会话窗口，你可以随时查看进度、接管操作，或调整 MCP、Skill、连接器等配置——这些配置对所有 IM 会话同样生效。</span>

<span style="color: rgb(73, 70, 65);">QwenWork 目前支持以下 IM 平台：</span>

| <span style="color: rgb(39, 42, 38); background-color: rgb(245, 247, 243);">**平台**</span> | <span style="color: rgb(39, 42, 38); background-color: rgb(245, 247, 243);">**接入方式**</span> | <span style="color: rgb(39, 42, 38); background-color: rgb(245, 247, 243);">**适用场景**</span> |
|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <span style="color: rgb(64, 61, 56);">钉钉</span> | <span style="color: rgb(64, 61, 56);">扫码绑定</span> | <span style="color: rgb(64, 61, 56);">企业团队协作</span> |
| <span style="color: rgb(64, 61, 56);">飞书</span> | <span style="color: rgb(64, 61, 56);">扫码自动创建应用</span> | <span style="color: rgb(64, 61, 56);">个人或团队快速接入</span> |
| <span style="color: rgb(64, 61, 56);">Lark</span> | <span style="color: rgb(64, 61, 56);">扫码自动创建应用</span> | <span style="color: rgb(64, 61, 56);">个人或团队快速接入（海外）</span> |
| <span style="color: rgb(64, 61, 56);">微信</span> | <span style="color: rgb(64, 61, 56);">扫码绑定，即开即用</span> | <span style="color: rgb(64, 61, 56);">移动端轻量交互</span> |
| <span style="color: rgb(64, 61, 56);">企业微信</span> | <span style="color: rgb(64, 61, 56);">扫码快捷绑定或手动配置</span> | <span style="color: rgb(64, 61, 56);">企业内部协作与自动化</span> |
| <span style="color: rgb(64, 61, 56);">Slack</span> | <span style="color: rgb(64, 61, 56);">填入 Token</span> | <span style="color: rgb(64, 61, 56);">海外团队协作</span> |
| <span style="color: rgb(64, 61, 56);">WhatsApp</span> | <span style="color: rgb(64, 61, 56);">扫码绑定</span> | <span style="color: rgb(64, 61, 56);">面向客户 / 移动端沟通</span> |

<span style="color: rgb(73, 70, 65);">所有 IM 频道均在 IM 频道 页面统一管理。</span>

![](https://alidocs2.oss-cn-zhangjiakou.aliyuncs.com/res/mxPOG5vdxd6XAnKa/img/ddb2e32e-9726-409a-885e-29dcbac744b1.webp?Expires=1785260309&OSSAccessKeyId=LTAI5tKTjg4Kq1HCdBJ8qpSp&Signature=2XXep8ybW3OL%2FU1HlYNlPLsxVZ4%3D "")

<span style="color: rgb(161, 157, 150); background-color: rgb(248, 248, 247);">image.png</span>

<span style="color: rgb(155, 93, 7); background-color: rgb(255, 249, 237);">**说明**</span>

<span style="color: rgb(108, 87, 55); background-color: rgb(255, 249, 237);">如果你的组织使用了 Teams 版，团队管理员可以管控成员可使用的 IM 频道类型。</span>

<span style="color: rgb(73, 70, 65);">详见</span>  [IM Channel 管控](https://qwenwork.cn/docs/desktop/im-channels)<span style="color: rgb(73, 70, 65);">。</span>

## <span style="color: rgb(24, 24, 27);">**工作原理**</span>

<span style="color: rgb(73, 70, 65);">IM 集成遵循一个核心原则：哪里来的，回哪里去。</span>

<span style="color: rgb(73, 70, 65);">你在某个 IM 聊天窗口中发送的消息，QwenWork 处理完后，结果会自动回传到同一个聊天窗口。桌面端直接创建的任务，结果则留在桌面端，不会推送到任何 IM。每个 IM 会话在 QwenWork 桌面端映射为一个独立的会话窗口，上下文完全隔离——不同 IM 平台、不同聊天窗口之间互不干扰。你可以在桌面端查看所有 IM 会话的历史和状态，也可以在桌面端对应的会话窗口中继续操作，产出结果依然会同步回 IM。</span>

## <span style="color: rgb(24, 24, 27);">**支持的消息类型**</span>

<span style="color: rgb(73, 70, 65);">在任意已连接的 IM 频道中，你可以发送以下类型的消息：</span>

| <span style="color: rgb(39, 42, 38); background-color: rgb(245, 247, 243);">**消息类型**</span> | <span style="color: rgb(39, 42, 38); background-color: rgb(245, 247, 243);">**说明**</span> |
|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <span style="color: rgb(64, 61, 56);">文本消息</span> | <span style="color: rgb(64, 61, 56);">直接发送文字指令</span> |
| <span style="color: rgb(64, 61, 56);">图片</span> | <span style="color: rgb(64, 61, 56);">发送图片，支持 OCR 识别、背景替换等处理</span> |
| <span style="color: rgb(64, 61, 56);">文件</span> | <span style="color: rgb(64, 61, 56);">支持 PDF、Excel、PPT、Word、CSV、TXT 等常见格式</span> |
| <span style="color: rgb(64, 61, 56);">语音消息</span> | <span style="color: rgb(64, 61, 56);">发送语音，自动识别内容并执行操作</span> |
| <span style="color: rgb(64, 61, 56);">合并转发消息</span> | <span style="color: rgb(64, 61, 56);">转发的多条消息会被正确解析</span> |
| <span style="color: rgb(64, 61, 56);">图片 \+ 文字组合</span> | <span style="color: rgb(64, 61, 56);">图片和文字指令关联理解，比如发一张图说「提取表格」</span> |

<span style="color: rgb(73, 70, 65);">连续发送多条消息时，系统会按顺序依次处理，不会丢消息或乱序。</span>

<span style="color: rgb(80, 100, 127); background-color: rgb(248, 249, 251);">**示例**</span>

<span style="color: rgb(85, 81, 75); background-color: rgb(248, 249, 251);">IM 频道和定时任务 可以配合使用。创建定时任务时指定结果发送到某个 IM 会话，任务执行完毕后结果会自动推送到该聊天窗口。比如「每天早上 9 点生成数据日报，发送到钉钉群」。</span>

## <span style="color: rgb(24, 24, 27);">**准入策略**</span>

| <span style="color: rgb(39, 42, 38); background-color: rgb(245, 247, 243);">**策略**</span> | <span style="color: rgb(39, 42, 38); background-color: rgb(245, 247, 243);">**说明**</span> |
|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <span style="color: rgb(64, 61, 56);">开放模式</span> | <span style="color: rgb(64, 61, 56);">所有人和群可直接与机器人对话，无需额外操作</span> |
| <span style="color: rgb(64, 61, 56);">配对模式</span> | <span style="color: rgb(64, 61, 56);">需经你允许后，对应会话才能使用机器人</span> |

<span style="color: rgb(73, 70, 65);">开放模式适合团队内部快速推广使用；配对模式适合需要控制使用范围的场景，比如只允许特定人员使用。</span>

<span style="color: rgb(73, 70, 65);">配对模式下，用户私聊机器人或在群中 @机器人 时会自动触发配对请求。你可以在频道卡片的「配对管理」中点击 允许 来通过请求。配对以会话为单位：私聊允许后该用户可对话，群聊允许后群内所有成员均可对话。</span>

## <span style="color: rgb(24, 24, 27);">**接入钉钉**</span>

<span style="color: rgb(73, 70, 65);">可以通过钉钉机器人接收并回复用户消息。QwenWork 提供了连接钉钉机器人的方式：在 QwenWork 中配置。</span>

### <span style="color: rgb(24, 24, 27);">**在 QwenWork 中配置**</span>

<span style="color: rgb(73, 70, 65);">打开钉钉配置页面</span>

<span style="color: rgb(73, 70, 65);">在 QwenWork 中进入 IM 频道，找到「钉钉」卡片，点击 配置。</span>

<span style="color: rgb(73, 70, 65);">扫码完成绑定</span>

<span style="color: rgb(73, 70, 65);">在弹出的「配置钉钉」窗口中，默认显示扫码界面。</span>

<span style="color: rgb(73, 70, 65);">打开钉钉，扫描二维码完成应用注册和绑定。如果二维码过期，可点击底部的 刷新二维码。</span>

<span style="color: rgb(73, 70, 65);">选择准入策略</span>

<span style="color: rgb(73, 70, 65);">绑定成功后，选择准入策略：</span>
- <span style="color: rgb(73, 70, 65);">开放模式：所有人 / 群可直接对话</span>
- <span style="color: rgb(73, 70, 65);">配对模式：需经你允许后，对应会话才能使用机器人</span>

<span style="color: rgb(73, 70, 65);">完成配置</span>

<span style="color: rgb(73, 70, 65);">回到 QwenWork，确认钉钉状态显示为「已连接」。现在可以在钉钉中使用机器人了。</span>

### <span style="color: rgb(24, 24, 27);">**使用方式**</span>

<span style="color: rgb(73, 70, 65);">单聊：在钉钉顶部搜索框中搜索机器人名称，点击进入对话窗口，直接发送消息。</span>

<span style="color: rgb(73, 70, 65);">群聊：将机器人添加到群聊后，在群里 @机器人 发送消息。添加方式：点击群设置（右上角） → 机器人 → 添加机器人 → 搜索并选择你创建的机器人。</span>

<span style="color: rgb(155, 93, 7); background-color: rgb(255, 249, 237);">**说明**</span>

<span style="color: rgb(108, 87, 55); background-color: rgb(255, 249, 237);">群聊的「归属组织」需要与创建机器人时的组织一致，否则搜索不到机器人。</span>

## <span style="color: rgb(24, 24, 27);">**接入飞书 / Lark**</span>

### <span style="color: rgb(24, 24, 27);">**在 QwenWork 中配置**</span>

<span style="color: rgb(73, 70, 65);">打开配置页面</span>

<span style="color: rgb(73, 70, 65);">在 QwenWork 中进入 IM 频道，找到「飞书」或「Lark」卡片，点击 配置。</span>

<span style="color: rgb(73, 70, 65);">扫码授权</span>

<span style="color: rgb(73, 70, 65);">页面上方会显示一个二维码。打开飞书 / Lark App，扫描二维码并确认授权。系统会自动在你的组织下创建应用，并配置好所需的权限和事件回调。</span>

<span style="color: rgb(73, 70, 65);">选择准入策略</span>

<span style="color: rgb(73, 70, 65);">授权成功后，选择准入策略：</span>
- <span style="color: rgb(73, 70, 65);">开放模式：所有人 / 群可直接对话</span>
- <span style="color: rgb(73, 70, 65);">配对模式：需经你允许后，对应会话才能使用机器人</span>

<span style="color: rgb(73, 70, 65);">完成配置</span>

<span style="color: rgb(73, 70, 65);">回到 QwenWork，确认状态显示为「已连接」。现在可以在飞书 / Lark 中使用机器人了。</span>

### <span style="color: rgb(24, 24, 27);">**使用方式**</span>

<span style="color: rgb(73, 70, 65);">单聊：在飞书 / Lark 搜索框中搜索机器人名称，点击进入对话窗口。</span>

<span style="color: rgb(73, 70, 65);">群聊：将机器人添加到群聊中，@机器人 发送消息。</span>

## <span style="color: rgb(24, 24, 27);">**接入微信**</span>

<span style="color: rgb(73, 70, 65);">扫码即可完成绑定，无需额外配置。</span>

<span style="color: rgb(73, 70, 65);">打开微信配置页面</span>

<span style="color: rgb(73, 70, 65);">在 QwenWork 中进入 IM 频道，找到「微信」卡片，点击 配置。</span>

<span style="color: rgb(73, 70, 65);">扫码授权</span>

<span style="color: rgb(73, 70, 65);">页面会显示一个二维码。打开微信，扫描二维码并确认授权。</span>

<span style="color: rgb(73, 70, 65);">开始使用</span>

<span style="color: rgb(73, 70, 65);">绑定完成后，等待状态变为「已连接」，在微信中直接向 QwenWork 发送消息即可开始对话。</span>

## <span style="color: rgb(24, 24, 27);">**接入企业微信**</span>

<span style="color: rgb(73, 70, 65);">可以通过企业微信机器人接收并回复用户消息。QwenWork 提供了两种连接企业微信机器人的方式：快捷绑定和手动配置。</span>

### <span style="color: rgb(24, 24, 27);">**方式一：扫码绑定（推荐）**</span>

<span style="color: rgb(73, 70, 65);">最简单快捷的接入方式，只需扫码即可完成绑定。</span>

<span style="color: rgb(73, 70, 65);">打开企业微信配置页面</span>

<span style="color: rgb(73, 70, 65);">在 QwenWork 中进入 IM 频道，找到「企业微信」卡片，点击 配置。</span>

<span style="color: rgb(73, 70, 65);">扫码完成绑定</span>

<span style="color: rgb(73, 70, 65);">在弹出的「配置企业微信」窗口中，选择 快捷绑定（推荐）。</span>

<span style="color: rgb(73, 70, 65);">打开企业微信，扫描二维码完成机器人创建和绑定。如果二维码过期，可点击底部的 刷新二维码。</span>

### <span style="color: rgb(24, 24, 27);">**方式二：手动配置**</span>

<span style="color: rgb(73, 70, 65);">获取机器人凭证</span>

<span style="color: rgb(73, 70, 65);">在企业微信管理后台创建机器人，并获取机器人的 Bot ID 和 Secret。</span>

<span style="color: rgb(73, 70, 65);">填写配置信息</span>

<span style="color: rgb(73, 70, 65);">在 QwenWork 的「配置企业微信」窗口中选择 手动配置，填入获取到的 Bot ID 和 Secret，点击 保存。</span>

## <span style="color: rgb(24, 24, 27);">**接入 Slack**</span>

<span style="color: rgb(73, 70, 65);">接收和回复 Slack 消息，需要提供 Slack 的 Bot Token 和 App-Level Token。</span>

<span style="color: rgb(73, 70, 65);">打开 Slack 配置页面</span>

<span style="color: rgb(73, 70, 65);">在 QwenWork 中进入 IM 频道，找到「Slack」卡片，点击 配置。</span>

<span style="color: rgb(73, 70, 65);">填写 Token</span>

<span style="color: rgb(73, 70, 65);">在「配置 Slack」窗口中填入以下两个 Token（均来自你在 Slack 创建的 App）：</span>
- <span style="color: rgb(73, 70, 65);">Bot Token（</span>`xoxb-`  <span style="color: rgb(73, 70, 65);">开头）</span>
- <span style="color: rgb(73, 70, 65);">App-Level Token（</span>`xapp-`  <span style="color: rgb(73, 70, 65);">开头）</span>

<span style="color: rgb(73, 70, 65);">选择准入策略</span>

<span style="color: rgb(73, 70, 65);">选择 准入策略：</span>
- <span style="color: rgb(73, 70, 65);">配对：需经你允许后，对应会话才能使用机器人</span>
- <span style="color: rgb(73, 70, 65);">开放：所有人可直接对话</span>

<span style="color: rgb(73, 70, 65);">测试并保存</span>

<span style="color: rgb(73, 70, 65);">可点击 测试连接 验证配置，然后点击 保存。状态显示为「已连接」后，在 Slack 中私聊机器人或在频道中 @机器人 即可对话。</span>

## <span style="color: rgb(24, 24, 27);">**接入 WhatsApp**</span>

<span style="color: rgb(73, 70, 65);">打开 WhatsApp 配置页面</span>

<span style="color: rgb(73, 70, 65);">在 QwenWork 中进入 IM 频道，找到「WhatsApp」卡片，点击 配置。</span>

<span style="color: rgb(73, 70, 65);">扫码绑定</span>

<span style="color: rgb(73, 70, 65);">打开手机上的 WhatsApp，扫描 QwenWork 显示的二维码完成绑定。</span>

<span style="color: rgb(73, 70, 65);">完成配置</span>

<span style="color: rgb(73, 70, 65);">绑定完成后，等待状态变为「已连接」，在 WhatsApp 中直接向机器人发送消息即可开始对话。</span>

## <span style="color: rgb(24, 24, 27);">**管理 IM 频道**</span>

<span style="color: rgb(73, 70, 65);">所有 IM 频道的配置和状态均在 IM 频道 页面集中管理。</span>

### <span style="color: rgb(24, 24, 27);">**开启与关闭**</span>

<span style="color: rgb(73, 70, 65);">每个频道卡片上都有一个开关。打开开关后状态显示为「已连接」，IM 端即可正常使用；关闭后 IM 端发送消息将不再收到回复。关闭不会清除配置，重新打开即可恢复。</span>

### <span style="color: rgb(24, 24, 27);">**删除频道**</span>

<span style="color: rgb(73, 70, 65);">如果需要彻底移除某个频道的配置，点击频道卡片上的 移除配置。移除后该频道的所有配置信息将被清除，IM 端不再响应。如需启用，需要重新配置。</span>

### <span style="color: rgb(24, 24, 27);">**切换准入策略**</span>

<span style="color: rgb(73, 70, 65);">钉钉、飞书和 Lark 频道支持在开放模式和配对模式之间随时切换：</span>
- <span style="color: rgb(73, 70, 65);">从开放切换到配对：切换后，之前未配对的用户将无法继续使用，需要重新触发配对请求并获得允许。</span>
- <span style="color: rgb(73, 70, 65);">从配对切换到开放：切换后，所有用户可直接使用，无需配对。</span>

### <span style="color: rgb(24, 24, 27);">**多频道并行**</span>

<span style="color: rgb(73, 70, 65);">可以同时开启所有 IM 频道。各频道之间完全独立，互不干扰——钉钉、飞书、Lark、微信的会话各自拥有独立的上下文和历史记录。</span>

## <span style="color: rgb(24, 24, 27);">**任务绑定（远程接管）**</span>

<span style="color: rgb(73, 70, 65);">QwenWork 支持通过 IM 介入桌面端的普通任务，实现远端与任务进行交互的功能，让你随时随地都能操作 QwenWork。</span>

<span style="color: rgb(73, 70, 65);">前提条件：</span>
1. <span style="color: rgb(73, 70, 65);">已开通任意一个 IM 频道（如钉钉、微信等）。</span>
2. <span style="color: rgb(73, 70, 65);">QwenWork 桌面端已创建并存在普通任务。</span>

<span style="color: rgb(73, 70, 65);">在任意已连接的 IM 频道中，你可以使用以下指令来管理任务绑定：</span>
- `/bind`<span style="color: rgb(73, 70, 65);">：查看当前可绑定的任务列表。回复</span>  `/bind <编号>`<span style="color: rgb(73, 70, 65);">（例如</span>  `/bind 1`<span style="color: rgb(73, 70, 65);">）即可将当前 IM 会话绑定到指定的桌面端任务。绑定后，你在 IM 中发送的消息将直接转发至该任务，任务的回复也会实时同步到 IM 中。</span>
- `/unbind`<span style="color: rgb(73, 70, 65);">：解除当前 IM 会话与桌面端任务的绑定。解除后，IM 会话将恢复为普通的独立会话。</span>

<span style="color: rgb(155, 93, 7); background-color: rgb(255, 249, 237);">**说明**</span>

<span style="color: rgb(108, 87, 55); background-color: rgb(255, 249, 237);">绑定任务后，你可以在手机上继续与电脑上正在运行的任务对话，例如让它汇报当前进度、补充新的指令或提供所需的验证码。</span>

## <span style="color: rgb(24, 24, 27);">**典型场景**</span>

### <span style="color: rgb(24, 24, 27);">**移动端轻量对话**</span>

<span style="color: rgb(73, 70, 65);">在 IM 中直接向机器人提问，适合简单的问答和快速查询：</span>

<span style="color: rgb(80, 100, 127); background-color: rgb(248, 249, 251);">**示例**</span>

<span style="color: rgb(85, 81, 75); background-color: rgb(248, 249, 251);">帮我找一下给 XX 公司的报价单发过来</span>

<span style="color: rgb(73, 70, 65);">机器人会调用已配置的 MCP 工具和数据源，在 IM 中直接回复结果。</span>

### <span style="color: rgb(24, 24, 27);">**图片和文件处理**</span>

<span style="color: rgb(73, 70, 65);">手机上收到或拍摄的图片、文件，直接发给机器人就能处理：</span>

<span style="color: rgb(154, 100, 27); background-color: rgb(252, 250, 246);">**注意**</span>

<span style="color: rgb(85, 81, 75); background-color: rgb(252, 250, 246);">（发送一份 PDF 合同）审核一下这份合同，重点看违约责任条款的风险点</span>

<span style="color: rgb(73, 70, 65);">支持 OCR 文字识别、背景替换、票据信息提取、文件摘要、格式转换、数据分析等处理能力。</span>

### <span style="color: rgb(24, 24, 27);">**远程派活**</span>

<span style="color: rgb(73, 70, 65);">人在外面，临时想让电脑上的 QwenWork 干活：</span>

<span style="color: rgb(80, 100, 127); background-color: rgb(248, 249, 251);">**示例**</span>

<span style="color: rgb(85, 81, 75); background-color: rgb(248, 249, 251);">帮我把桌面上的「Q1 销售数据.xlsx」整理成一份分析报告， 包含销售趋势、客户分布和环比变化，保存为 PDF 到桌面。</span>

<span style="color: rgb(73, 70, 65);">QwenWork 在后台执行，完成后将结果摘要和文件自动回传到 IM 会话。</span>

### <span style="color: rgb(24, 24, 27);">**定时任务结果推送**</span>

<span style="color: rgb(73, 70, 65);">配合</span>[定时任务](https://qwenwork.cn/docs/desktop/scheduled-tasks)<span style="color: rgb(73, 70, 65);">使用，让执行结果自动推送到 IM：</span>

<span style="color: rgb(80, 100, 127); background-color: rgb(248, 249, 251);">**示例**</span>

<span style="color: rgb(85, 81, 75); background-color: rgb(248, 249, 251);">帮我创建一个定时任务：每天早上 9 点生成昨日运营数据摘要， 完成后将结果发送到钉钉「运营日报」群。</span>

### <span style="color: rgb(24, 24, 27);">**群聊协作**</span>

<span style="color: rgb(73, 70, 65);">在团队群聊中 @机器人，所有群成员都能使用：</span>

<span style="color: rgb(80, 100, 127); background-color: rgb(248, 249, 251);">**示例**</span>

<span style="color: rgb(85, 81, 75); background-color: rgb(248, 249, 251);">@QwenWork 帮我总结一下今天群里讨论的要点</span>



<span style="color: rgb(73, 70, 65); background-color: rgb(245, 247, 240);">***来源：千文办公 官方指南。***</span>
