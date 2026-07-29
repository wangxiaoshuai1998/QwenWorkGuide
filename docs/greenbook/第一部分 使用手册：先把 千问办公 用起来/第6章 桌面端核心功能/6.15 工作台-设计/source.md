# **6.15 工作台-设计**

## <span style="color: rgb(24, 24, 27);">**设计**</span>

<span style="color: rgb(73, 70, 65);">设计工作台是 QwenWork 自定义工作台的首个细分领域模式——一个 AI 原生的"设计即代码"画布：用自然语言（或语音）描述需求，就能在无限画布上获得可运行、可编辑、可交付的设计产物。</span>

<span style="color: rgb(73, 70, 65);">不同于以"云端协作矢量编辑"为核心的传统设计工具，设计工作台把成果物视为团队共同维护的代码资产：从第一步起设计师与研发就操作同一份可运行文件，设计产物可以一键交付到 ，省去设计到代码之间的有损交接。</span>

## <span style="color: rgb(24, 24, 27);">**使用场景**</span>

### <span style="color: rgb(24, 24, 27);">**设计师——定向迭代、多端协作**</span>

<span style="color: rgb(73, 70, 65);">传统流程中，每一处修改都意味着重新导出切图、更新标注、同步研发、验收还原。设计工作台把迭代压缩到画布之内：圈选区域、标注意图，Agent 基于画面上下文即时调整；通过 Nudge 实时微调配色与间距，反复精修直到满意。设计产物保留可读、可接手的工程文件结构。</span>

### <span style="color: rgb(24, 24, 27);">**产品经理——随时更新高保真原型**</span>

<span style="color: rgb(73, 70, 65);">高保真原型能直观展现产品方向，但通常依赖设计排期。设计工作台为产品经理提供了第三条路径：信息不足时 Agent 先结构化追问对齐意图，再经设计计划确认方向，即可在画布上获得具备设计品质的可交互原型，直接用于需求评审或团队汇报。</span>

### <span style="color: rgb(24, 24, 27);">**市场运营——多方向并行生成**</span>

<span style="color: rgb(73, 70, 65);">单场活动涉及主视觉、Banner、落地页等多项产出，设计资源有限往往只能交付单一方向。设计工作台支持多方向并行：输入主题与调性，通过设计计划确认方向后即可生成；通过 自动选择风格参考 切换风格即获得不同方向，覆盖海报、Banner、落地页等高频需求。</span>

## <span style="color: rgb(24, 24, 27);">**工作原理**</span>

<span style="color: rgb(73, 70, 65);">设计工作台通过三个机制重构了 AI 生产设计的流程：</span>
- <span style="color: rgb(73, 70, 65);">Questions——输入不足时 Agent 先追问对齐意图，而非猜测执行，把无效迭代降到最低。</span>
- <span style="color: rgb(73, 70, 65);">Design Plan——Agent 在生成前会在 计划 标签下输出结构化设计计划（布局、风格、内容层级），经你确认后才执行。</span>
- <span style="color: rgb(73, 70, 65);">Nudge——生成后，配色、间距、圆角等关键决策以可调参数暴露，无需重新描述就能微调。</span>

## <span style="color: rgb(24, 24, 27);">**工作区**</span>

![](https://alidocs2.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOk25NBEd97q4B/img/f5710ada-a942-440e-9dbd-c8ccc0a73a52.webp?Expires=1785348749&OSSAccessKeyId=LTAI5tKTjg4Kq1HCdBJ8qpSp&Signature=Gg4%2BUVpBkCnjiuPXlvUf3OVMe48%3D "")

<span style="color: rgb(73, 70, 65);">右侧画布提供 5 个标签：</span>

| <span style="color: rgb(39, 42, 38); background-color: rgb(245, 247, 243);">**标签**</span> | <span style="color: rgb(39, 42, 38); background-color: rgb(245, 247, 243);">**用途**</span> |
|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <span style="color: rgb(64, 61, 56);">画布</span> | <span style="color: rgb(64, 61, 56);">无限画布，Agent 在这里生成与编辑</span> |
| <span style="color: rgb(64, 61, 56);">设计文件</span> | <span style="color: rgb(64, 61, 56);">画布背后的工程文件</span> |
| <span style="color: rgb(64, 61, 56);">预览</span> | <span style="color: rgb(64, 61, 56);">把设计当作真实界面预览运行效果</span> |
| <span style="color: rgb(64, 61, 56);">风格参考</span> | <span style="color: rgb(64, 61, 56);">查看和切换设计当前使用的风格参考</span> |
| <span style="color: rgb(64, 61, 56);">计划</span> | <span style="color: rgb(64, 61, 56);">Agent 生成前所依据的结构化设计计划</span> |

## <span style="color: rgb(24, 24, 27);">**创建设计**</span>

<span style="color: rgb(73, 70, 65);">切换到设计工作台</span>

<span style="color: rgb(73, 70, 65);">在 QwenWork 首页底部输入框点击工作台切换器（默认 通用），选 设计。</span>

![](https://alidocs2.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOk25NBEd97q4B/img/85150bd1-d905-4b7c-904b-f550bbc68ee9.webp?Expires=1785348749&OSSAccessKeyId=LTAI5tKTjg4Kq1HCdBJ8qpSp&Signature=VgissSGqyYHOwASMG3ZPY2iq3CA%3D "")

<span style="color: rgb(80, 100, 127); background-color: rgb(248, 249, 251);">**示例**</span>

<span style="color: rgb(85, 81, 75); background-color: rgb(248, 249, 251);">默认工作台可以在 QwenWork 设置里调整——主要在设计场景里工作时，把"设计"设为默认更顺手。</span>

<span style="color: rgb(73, 70, 65);">描述需求</span>

<span style="color: rgb(73, 70, 65);">用自然语言或语音描述需求，尽量明确目的、关键模块和调性，例如：</span><span style="color: rgb(73, 70, 65);">*"设计一个高保真的 AI 产品官网首页，包含品牌导航、强主标题、产品价值说明、主 CTA、辅助 CTA、产品界面预览和客户信任信息。整体现代、可信、精致。"*</span>

![](https://alidocs2.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOk25NBEd97q4B/img/62e62b15-3418-4e6b-b526-da746d1fcee4.webp?Expires=1785348749&OSSAccessKeyId=LTAI5tKTjg4Kq1HCdBJ8qpSp&Signature=77youQF3nlS0Xb3%2BjP6SBhzYxnE%3D "")

<span style="color: rgb(73, 70, 65);">选择风格参考、固定工作目录（可选）</span>

<span style="color: rgb(73, 70, 65);">输入框下方有一行工作台可选项：选择工作目录、自动选择风格参考、保真度、组件库。</span>
- <span style="color: rgb(73, 70, 65);">点击 自动选择风格参考 在生成前先锁定整体调性——保持 自动选择风格参考 让画布从 161 个参考中自动挑选；也可以选择 Airbnb、Airtable、Apple、Carbon、Cloudscape 等具体风格，顶部搜索框可按名称过滤。</span>
- <span style="color: rgb(73, 70, 65);">点击 选择工作目录 可把任务绑定到本地一个目录——Agent 会把设计的工程文件落到该目录下，方便长期维护并与 Qwen IDE 协同。</span>
- <span style="color: rgb(73, 70, 65);">点击 保真度 可在 线框图（先梳理低保真结构，尽量减少视觉样式）与 高保真（使用接近最终交付的视觉设计与细节样式，默认）之间切换。</span>
- <span style="color: rgb(73, 70, 65);">点击 组件库 选择目标组件库——默认 不指定组件库（HTML-first，除非需求里明确要求 React 或其他框架）；也可以从 shadcn/ui、Spark Design、Ant Design 三个 React 组件库中选一个，Agent 会基于所选库生成。</span>

<span style="color: rgb(73, 70, 65);">选择直接运行或进入设计计划</span>

<span style="color: rgb(73, 70, 65);">提交后，Agent 会先理解需求、做一轮简短的分析（你可以在左侧的 深度思考 中看到推理过程），随后给出 进入设计规划 的决策卡，并列两个按钮：</span>
- <span style="color: rgb(73, 70, 65);">直接运行：跳过澄清与计划，Agent 用现有上下文直接落到画布。适合需求已足够明确，或只想先快速看到效果的场景。</span>
- <span style="color: rgb(73, 70, 65);">进入：开启设计计划模式——Agent 会先问问题、再写 Design Plan，确认后才生成。复杂或高保真项目推荐走这条路径。</span>

![](https://alidocs2.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOk25NBEd97q4B/img/9f852310-a9d4-4fc9-90c9-10bda7b48267.webp?Expires=1785348749&OSSAccessKeyId=LTAI5tKTjg4Kq1HCdBJ8qpSp&Signature=VQIGyFwcNnFVjYzUXdF%2FzaFW0Oc%3D "")

<span style="color: rgb(73, 70, 65);">回答 Agent 的澄清问题</span>

<span style="color: rgb(73, 70, 65);">进入设计计划模式后，Agent 会在 Questions 标签下结构化追问——目标用户、产品定位、保真度、品牌资产等，每题给几个备选项并支持「其他（请填写）」自由输入。回答能让计划贴合实际场景；想跳过细化，可点击底部的 AI 自行决定。</span>

![](https://alidocs2.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOk25NBEd97q4B/img/b032a906-bf50-4f6d-9e96-da5a2cd7d3a9.webp?Expires=1785348749&OSSAccessKeyId=LTAI5tKTjg4Kq1HCdBJ8qpSp&Signature=Pmte9oVD1YqhwgAA3EAgHV8qxKs%3D "")

<span style="color: rgb(73, 70, 65);">确认设计计划</span>

<span style="color: rgb(73, 70, 65);">Agent 接着在 计划 标签下输出 Design Plan：开头是设计意图与视觉方向，再是 契约 面板（产物 / 平台 / 输出 / 组件库 / 保真度 / 风格）和 产物 列表（每个文件的目标说明）。审核无误点 运行计划；如需调整，点 要求修改 让 Agent 重写。</span>

![](https://alidocs2.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOk25NBEd97q4B/img/1778c8a6-79a4-45ae-bcb0-236d1da3fd1a.webp?Expires=1785348749&OSSAccessKeyId=LTAI5tKTjg4Kq1HCdBJ8qpSp&Signature=nTFuVoM1KeKzPtJQGSKiD6L8pVo%3D "")

<span style="color: rgb(73, 70, 65);">查看画布生成过程</span>

<span style="color: rgb(73, 70, 65);">Agent 在 画布 上生成。左侧面板会以 深度思考 形式实时显示推理过程，画布上每一个组件落位后即时更新。</span>

<span style="color: rgb(73, 70, 65);">预览运行效果</span>

<span style="color: rgb(73, 70, 65);">切换到 预览，把设计当作真实界面交互——点击 CTA、查看 hover 状态、走查导航流。</span>

![](https://alidocs2.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOk25NBEd97q4B/img/a5a0a46d-b7f2-4ea3-bb1c-ffea5eed961a.webp?Expires=1785348749&OSSAccessKeyId=LTAI5tKTjg4Kq1HCdBJ8qpSp&Signature=c1OL4dGDOTmuEg17pSAltzdJBmE%3D "")

## <span style="color: rgb(24, 24, 27);">**继续迭代**</span>

<span style="color: rgb(73, 70, 65);">不需要从头重写需求，迭代直接在原画布上进行。</span>
- <span style="color: rgb(73, 70, 65);">追加任务：在底部输入框继续追加指令，Agent 会在当前步完成后接着处理。</span>
- <span style="color: rgb(73, 70, 65);">打断当前生成：输入框旁的停止按钮可以中断正在进行的生成。</span>
- <span style="color: rgb(73, 70, 65);">画布上圈选并标注：选择某一区域，告诉 Agent 改什么——它会基于画面上下文调整，而不是整体重新生成。</span>
- <span style="color: rgb(73, 70, 65);">Nudge 微调关键参数：生成后配色、间距、圆角等以可调参数暴露，无需重新描述就能微调。</span>
- <span style="color: rgb(73, 70, 65);">中途切换模型：输入框旁的模型下拉（例如 标准 / 旗舰）可以为下一步切换模型。</span>
- <span style="color: rgb(73, 70, 65);">直接编辑工程文件：进入 设计文件 检查或编辑源码，必要时切到代码层处理。</span>

<span style="color: rgb(80, 100, 127); background-color: rgb(248, 249, 251);">**示例**</span>

<span style="color: rgb(85, 81, 75); background-color: rgb(248, 249, 251);">Agent 会保留完整的对话上下文，所以"保留布局，但把 hero 区配色调暗、CTA 加宽"这种就地迭代可以精确改动现有画面。</span>

## <span style="color: rgb(24, 24, 27);">**典型场景**</span>

### <span style="color: rgb(24, 24, 27);">**产品落地页**</span>

<span style="color: rgb(155, 93, 7); background-color: rgb(255, 249, 237);">**说明**</span>

<span style="color: rgb(108, 87, 55); background-color: rgb(255, 249, 237);">设计一个 SaaS 产品的落地页，面向企业用户。 包含：顶部导航、hero 区（大标题 \+ 副标题 \+ 主 CTA）、 三列产品优势、客户 logo 条、定价对比表、底部 CTA 和 footer。 风格：干净、留白多、使用冷色调。</span>

### <span style="color: rgb(24, 24, 27);">**营销视觉套件**</span>

<span style="color: rgb(155, 93, 7); background-color: rgb(255, 249, 237);">**说明**</span>

<span style="color: rgb(108, 87, 55); background-color: rgb(255, 249, 237);">为一场线上产品发布会设计一套营销视觉素材： 1. 16:9 宣传 Banner（标题 \+ 倒计时 \+ 二维码区域） 2. 方形社媒配图（适合朋友圈和微博） 3. 活动落地页（包含议程、嘉宾、报名入口） 统一使用品牌色 #1A73E8，现代科技风格。</span>

### <span style="color: rgb(24, 24, 27);">**Dashboard 重设计**</span>

<span style="color: rgb(155, 93, 7); background-color: rgb(255, 249, 237);">**说明**</span>

<span style="color: rgb(108, 87, 55); background-color: rgb(255, 249, 237);">重新设计一个数据分析 Dashboard。 包含：侧边栏导航、顶部筛选器栏、核心指标卡片（4 个）、 折线趋势图、环形分布图、数据表格。 风格参考 Linear，暗色主题，信息密度高但层次清晰。</span>



<span style="color: rgb(73, 70, 65); background-color: rgb(245, 247, 240);">***来源：千文办公 官方指南。***</span>
