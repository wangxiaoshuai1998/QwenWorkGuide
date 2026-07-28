# **第7章 概念普及：理解AI是怎么干活的**

## **一、什么是LLM**

![result_00 (1).png](https://alidocs2.oss-cn-zhangjiakou.aliyuncs.com/res/jP2lRY2pmGNNJO8g/img/545fb7b7-5b8c-4a8a-9643-3b173b64bb2e.png?Expires=1785260317&OSSAccessKeyId=LTAI5tKTjg4Kq1HCdBJ8qpSp&Signature=zYxYFZlddR%2FLdbsBGeoLjdkz2wo%3D "")

## **二、Token与Tokenizer**

![result_00 (2).png](https://alidocs2.oss-cn-zhangjiakou.aliyuncs.com/res/jP2lRY2pmGNNJO8g/img/cb15e3f9-fefe-4607-8f4b-18cdab23195e.png?Expires=1785260317&OSSAccessKeyId=LTAI5tKTjg4Kq1HCdBJ8qpSp&Signature=Os4yPWHPdM3XCRvp356I9yf9TNU%3D "")

## **三、Prompt与Prompt工程**

![result_00 (3).png](https://alidocs2.oss-cn-zhangjiakou.aliyuncs.com/res/jP2lRY2pmGNNJO8g/img/e175947b-8683-4e86-9fc4-e6c4812de8ff.png?Expires=1785260317&OSSAccessKeyId=LTAI5tKTjg4Kq1HCdBJ8qpSp&Signature=w2ct5S%2B57yfEdd83ea88cPMyXzQ%3D "")

## **四、知识库、RAG、记忆/意识**

![result_00 (8).png](https://alidocs2.oss-cn-zhangjiakou.aliyuncs.com/res/jP2lRY2pmGNNJO8g/img/9d526b70-0737-449a-b78d-f2292a293505.png?Expires=1785260317&OSSAccessKeyId=LTAI5tKTjg4Kq1HCdBJ8qpSp&Signature=ju00SC1gPUS6AoywSqwQSKtOMZc%3D "")

## **五、Agent、MCP、SKill**

![result_00 (5).png](https://alidocs2.oss-cn-zhangjiakou.aliyuncs.com/res/jP2lRY2pmGNNJO8g/img/5c836eab-3efc-4186-9d3a-7b4e04fa3a5b.png?Expires=1785260317&OSSAccessKeyId=LTAI5tKTjg4Kq1HCdBJ8qpSp&Signature=8rJi1aestxmOO3cT1x2xZpDp27g%3D "")

## **六、API与CLI**

![result_00 (7).png](https://alidocs2.oss-cn-zhangjiakou.aliyuncs.com/res/jP2lRY2pmGNNJO8g/img/1faf013f-dbc1-4ef4-aee8-ffbd3df2b534.png?Expires=1785260317&OSSAccessKeyId=LTAI5tKTjg4Kq1HCdBJ8qpSp&Signature=3knTxj93g55mBWOQO8LuoXVVUpA%3D "")

## **七、Harness架构是怎么工作的？**

![result_00 (9).png](https://alidocs2.oss-cn-zhangjiakou.aliyuncs.com/res/jP2lRY2pmGNNJO8g/img/9aa32d17-063c-4cd2-a2dd-d575f5d48bd8.png?Expires=1785260317&OSSAccessKeyId=LTAI5tKTjg4Kq1HCdBJ8qpSp&Signature=6B%2FzE3q9z3xeWA4M9iG8SvadyJ0%3D "")

## **八、一张图讲解清楚Agent是怎么工作的**

![result_00 (6).png](https://alidocs2.oss-cn-zhangjiakou.aliyuncs.com/res/jP2lRY2pmGNNJO8g/img/5f0698ad-4ab4-47f8-963a-727413fee44a.png?Expires=1785260317&OSSAccessKeyId=LTAI5tKTjg4Kq1HCdBJ8qpSp&Signature=O6qyJcb26kXjA2b8hN7E4qDGctI%3D "")

## <span style="color: rgb(34, 34, 34);">**🎨 ✏️ 一句话总结**</span>

<span style="color: rgb(34, 34, 34);">AI的本质是一个"</span><span style="color: rgb(34, 34, 34);">**预测下一个词**</span><span style="color: rgb(34, 34, 34);">"的引擎（LLM），通过最小单元（</span><span style="color: rgb(34, 34, 34);">**Token**</span><span style="color: rgb(34, 34, 34);">）处理信息，在有限的记忆空间（</span><span style="color: rgb(34, 34, 34);">**Context**</span><span style="color: rgb(34, 34, 34);">）里，根据你的指令（</span><span style="color: rgb(34, 34, 34);">**Prompt/Harness**</span><span style="color: rgb(34, 34, 34);">），借助外部能力（</span><span style="color: rgb(34, 34, 34);">**Tool/MCP**</span><span style="color: rgb(34, 34, 34);">），自主完成任务（Agent/Skill）。</span>

## **用一张表总结一下**

| 概念 | 一句话定义 | 生活类比 |
|------|---------------|------------|
| LLM | AI的核心引擎 | 大脑——负责思考和生成 |
| Token | 数据处理的最小单元 | 乐高积木的最小颗粒 |
| Context | 大模型的临时记忆 | RAM内存——关机就清空 |
| Prompt | 给大模型的指令 | 领导交给你的任务书 |
| Harness | Prompt的进化版，AI的完整工作手册 | SOP手册体系——定义整套工作模式 |
| Tool | 感知外部世界的函数 | 手机上的APP——大脑没有的功能靠它补 |
| MCP | 统一的工具接入标准 | Type-C接口——统一标准，一次开发全平台通用 |
| Agent | 自主规划\+调用工具的系统 | 私人助理——你说需求，他自己规划步骤去执行 |
| Agent Skill | Agent的说明书 | SOP操作手册——不用每次都教，写好它自己看 |


