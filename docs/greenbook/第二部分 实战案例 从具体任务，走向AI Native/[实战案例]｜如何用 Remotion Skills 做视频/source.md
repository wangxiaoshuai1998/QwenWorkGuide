# \[实战指南\]｜如何用 Remotion Skills 做视频

## Remotion 是什么?

Remotion 是一个用 React 编程式创建视频的框架。不用学AE、达芬奇，也不用去研究怎么在时间轴上拖拽素材,你可以直接通过vibe coding来定义动画、转场和特效。可以理解为"视频版的 React"——用组件、props 和你熟悉的 Web 技术来构建视频合成。

Remotion Skills 的出现打破了传统视频制作的边界，让 vibe video 像 vibe coding 一样通过对话就可以快速实现。

## 可以在 千问办公 里做什么？

在 千问办公 中使用 Remotion 的 Agent Skills 可以让你实现通过自然语言来 vibe code 出一个完整视频。你可以直接描述你想要的元素：动画、转场、UI 效果等等，千问办公 就可以帮你在几分钟内生成 Remotion 代码，完全不用打开传统的视频编辑器!

适用场景：使用这个 Skills 生成的视频非常适合用来做 **产品演示、功能发布和宣传视频**。

我们先看一段完全由 Remotion Skill 生成的 千问办公 Skills 视频片段:

## 实操
> 本次演示使用 千问办公 IDE。   

### 把 Remotion 添加到你的 千问办公 Skills
- 首先你需要在 千问办公 里面打开一个新的项目
- 安装 Remotion Skills有两种方式：
    - 方式 1:从 GitHub 仓库下载 zip: [https://github.com/remotion-dev/remotion/tree/main/packages/skills](https://github.com/remotion-dev/remotion/tree/main/packages/skills)
    - 方式 2:用 Skill.sh 命令行安装，直接把下面的指令复制粘贴到千问办公的终端里面
```Markdown
npx skills add https://github.com/remotion-dev/skills --skill remotion-best-practices

```

在 "Which agents do you want to install to", 选择 「千问办公 国际版」或者「千问办公 中国版」



在 installation scope中, 选择 "Project" ，这里Remotion Skills 只用于当前项目。



在选择安装方式中, 选择 "Symlink":



### 开始生成你的开场视频片段

首先要想好你想怎么呈现视频开场的关键元素,然后在提示词里明确这些关键信息，包括
- **主题**：你要展示什么
- \*\*视频尺寸：\*\*Remotion 支持不同尺寸,但中途切换很麻烦,所以推荐先提前给出清晰的视频尺寸要求
- \*\*起始画面：\*\*保持简洁（比如一个打开文件目录的命令）
- \*\*视觉风格：\*\*定义你的视频风格
```Markdown
我们要为 千问办公 Skills 的新功能做一个 remotion 动画,这个功能支持全局和项目级别的 skills。

首先创建一个新的 composition:
1920px x 1080px 的 macOS 终端窗口样式的控制台,带有打字机动画,输入 "cd ./千问办公/skills"

浅色主题,极简。

```



### 转场到截图并添加下一个动效

你可以附上产品截图让 Remotion 创建视觉元素。

比如在 千问办公 Skills 视频里,我们附上了 千问办公 Skills 面板的截图,然后让 agent 根据截图生成下一帧动画：
```Markdown
添加一个动效转场到我提供的截图中显示的面板

```



另外,你还可以通过提示词在截图内部添加动效。这里我们添加动画来高亮 Skills 面板下的两个不同标签页 Global 和 Project:
```Markdown
现在根据截图,高亮 项目 标签,可以往里面添加几个 Agent Skills。

然后切换到高亮 全局 标签页并打开它,也可以往里面添加几个 Agent Skills

```

### 继续添加截图或 UI 元素来打磨细节

你可以继续添加更多截图或 UI 元素来完善视频细节。现在我们在打磨列表中单个 Skill 的细节,让它完美对齐 千问办公 的 原装UI:


```Markdown
现在把添加 Skills 面板的 UI 改成和我提供的截图里的 UI 一致。确保每个 skill 文件显示正确的 logo(左边橙色的那个),右边是开关和设置按钮。

Skill 名称不需要和我截图里的一致

```

然后添加动效来展示每个 Skill 的开关切换:
```Markdown
现在在 全局 项目里,切换开关 1-2 个 skills 来展示开关按钮。

```

现在，一个初始的 千问办公 Skills 的产品更新动态视频就完成啦。

## 其他实用的 Remotion Skills 提示词推荐

你可以直接在 AI 对话框输出这些提示词即可。
- 查看视频时间轴，用于调整局部帧的细节
```Markdown
展示一下全部动画效果的时间轴

```
- 添加一个滑入屏幕的字幕
```Markdown
显示文字 "Agent Skills now available in 千问办公" 2 秒,用 Inter 字体
给文字添加一个缩放动画,用 easing out 曲线

```
- 给元素添加 3D 旋转效果
```Markdown
在开场场景的终端窗口添加 3D 旋转,用 rotateX(20deg) 和 rotateY(-20deg)

```
- 在视频中添加背景图
```Markdown
把视频的白色背景替换成深绿色背景图

```

借助 Skill，我们可以大胆探索更多使用场景，不再局限于写代码，它为大家带来了无限可能。如果你还没开始体验，不妨从第一个视频入手，把它当作一个起点：也许从今天起，你解决问题的思路、创造价值的方式，都会悄悄发生变化。
