Hooks 让你可以在 QwenWork 执行的关键节点插入自定义逻辑，而无需修改任何代码。你只需编辑 JSON 配置文件，就能实现诸如：
- 在工具执行前拦截危险操作
- 写文件后自动跑 lint，保持代码风格一致
- Agent 完成任务时弹出桌面通知，不用一直盯着屏幕

与 Prompt 指令不同，Hooks 是确定性的——只要事件触发，脚本就一定执行，不受模型理解偏差的影响。

## 快速开始

下面用一个例子，演示如何拦截 `rm -rf` 这类危险命令。

**1\. 创建脚本**

\`mkdir -p ~/.qwenwork/hooks
 cat \> ~/.qwenwork/hooks/block-rm.sh \<\< 'EOF'
 #!/bin/bash
 input=\$(cat)
 command=$(echo $
input" \| jq -r '.tool\_input.command')

if echo "\$command" \| grep -q 'rm -rf'; then
 echo "危险命令已被阻止: \$command" \>&2
 exit 2
 fi

exit 0
 EOF
 chmod \+x ~/.qwenwork/hooks/block-rm.sh\`

**2\. 添加配置**

在 `~/.qwenwork/settings.json` 中添加：

`{ "hooks": { "PreToolUse": [ { "matcher": "Bash", "hooks": [ { "type": "command", "command": "~/.qwenwork/hooks/block-rm.sh" } ] } ] } }`

**3\. 验证效果**

打开 QwenWork，让 Agent 执行包含 `rm -rf` 的命令。Hook 会阻止执行，并把错误信息反馈给 Agent。

## 配置 Hooks

### 配置文件位置

QwenWork 从以下用户级配置文件加载 Hook 配置：

| 位置 | 作用域 | 说明 |
|------|---------|------|
| `~/.qwenwork/settings.json` | 用户级（全局） | 用户个人配置，对所有 QwenWork 会话生效 |

**说明**

当前版本暂不支持热加载，修改配置文件后需要重启 QwenWork 才能生效。

### 配置格式

`{ "hooks": { "事件名": [ { "matcher": "匹配条件", "hooks": [ { "type": "command", "command": "要执行的命令", "timeout": 60 } ] } ] } }`

| 字段 | 必填 | 说明 |
|------|------|------|
| `type` | 是 | 固定为 `"command"` |
| `command` | 是 | 要执行的 shell 命令 |
| `timeout` | 否 | 超时时间（秒），默认 60 |
| `matcher` | 否 | 匹配条件，不填则匹配所有 |

一个事件下可以配置多个 matcher 分组，每个分组可以包含多个 Hook 命令。

### matcher 匹配规则

`matcher` 用于过滤 Hook 的触发范围，不同事件匹配不同的字段（见各事件说明）。

| 写法 | 含义 | 示例 |
|------|------|------|
| 不填或 `"&#42;"` | 匹配所有 | 所有工具都会触发 |
| 精确值 | 精确匹配 | `"Bash"` 只在 Bash 工具时触发 |
| \` | \` 分隔 | 匹配多个值 |
| 正则表达式 | 正则匹配 | `"mcp&#95;&#95;.&#42;"` 匹配所有 MCP 工具 |

## 编写 Hook 脚本

Hook 脚本通过 stdin 接收 JSON 输入，通过 exit code 和 stdout 输出来控制行为。本节说明所有事件通用的输入输出格式，各事件的额外字段见 Hooks 事件。

**说明**

QwenWork 目前不会向 Hook 脚本注入环境变量。所有数据通过 stdin JSON 传递。如需会话 ID、工作目录或工具信息，请从 stdin JSON 输入中解析。

### 输入

Hook 脚本通过 **stdin** 接收 JSON 数据。所有事件都包含以下通用字段：

| 字段 | 说明 |
|------|------|
| `session&#95;id` | 当前会话 ID |
| `cwd` | 当前工作目录 |
| `hook&#95;event&#95;name` | 触发的事件名称 |

不同事件会在此基础上附加额外字段（见各 Hooks 事件）。

用 `jq` 解析输入：

`#!/bin/bash input=$(cat) tool_name=$(echo "$input" | jq -r '.tool_name')`

### 输出

Hook 通过 exit code 和 stdout 控制行为。

exit code 决定基本行为：0 成功，2 阻塞（stderr 内容注入对话，仅对支持阻塞的事件生效），其他值为非阻塞错误。

stdout JSON（仅 exit 0 时解析）可为部分事件提供精细控制，具体支持的字段见各事件说明。exit 非 0 时 stdout 被忽略。

## Hooks 事件

### SessionStart

会话开始时触发。

**matcher 匹配：** 会话来源

| matcher 值 | 触发场景 |
|-----------|------------|
| `startup` | 新会话启动 |
| `resume` | 恢复已有会话 |
| `compact` | 上下文压缩完成后 |

**额外输入字段：**

`{ "source": "startup", "model": "Auto" }`

### SessionEnd

会话结束时触发。

**matcher 匹配：** 结束原因

| matcher 值 | 触发场景 |
|-----------|------------|
| `prompt&#95;input&#95;exit` | 用户退出输入（Ctrl\+D 等） |
| `other` | 其他原因 |

**额外输入字段：**

`{ "reason": "prompt_input_exit" }`

### UserPromptSubmit

用户提交 Prompt 后、Agent 处理前触发。

**额外输入字段：**

`{ "prompt": "帮我写一个排序函数" }`

### PreToolUse

工具执行前触发。可以阻止工具执行。

**matcher 匹配：** 工具名（如 `Bash`、`Write`、`Edit`、`Read`、`Glob`、`Grep`，MCP 工具名如 `mcp__server__tool`）

**额外输入字段：**

`{ "tool_name": "Bash", "tool_input": {"command": "rm -rf /tmp/build"}, "tool_use_id": "toolu_01ABC123" }`

**阻止工具执行：** exit code 2，stderr 内容作为错误返回给 Agent。

### PostToolUse

工具执行成功后触发。

**matcher 匹配：** 工具名

**额外输入字段：**

`{ "tool_name": "Write", "tool_input": {"file_path": "/path/to/file.ts", "content": "..."}, "tool_response": "File written successfully", "tool_use_id": "toolu_01ABC123" }`

### PostToolUseFailure

工具执行失败后触发。

**matcher 匹配：** 工具名

**额外输入字段：**

`{ "tool_name": "Bash", "tool_input": {"command": "npm test"}, "tool_use_id": "toolu_01ABC123", "error": "Command exited with non-zero status code 1", "is_interrupt": false }`

### Stop

Agent 完成响应后触发（主 Agent，无待执行的工具调用时）。可以阻止 Agent 停止，让其继续工作。

**阻止 Agent 停止：** exit code 2，stderr 内容作为消息注入对话，Agent 继续工作。

### SubagentStart / SubagentStop

子 Agent 启动和完成时触发。SubagentStop 与 Stop 类似，可以阻止子 Agent 停止。

**matcher 匹配：** Agent 类型名

**额外输入字段：**

`{ "agent_id": "a1b2c3d4", "agent_type": "task" }`

### PreCompact

上下文压缩前触发。

**matcher 匹配：** 触发方式

| matcher 值 | 触发场景 |
|-----------|------------|
| `manual` | 用户手动执行 /compact |
| `auto` | 上下文窗口满时自动触发 |

**额外输入字段：**

`{ "trigger": "manual", "custom_instructions": "保留所有工具调用结果" }`

### Notification

通知事件触发（权限请求、任务完成等）。

**matcher 匹配：** 通知类型

| matcher 值 | 触发场景 |
|-----------|------------|
| `permission` | 权限请求通知 |
| `result` | Agent 产出结果通知 |

**额外输入字段：**

`{ "message": "Agent is requesting permission to run: rm -rf node_modules", "title": "Permission Required", "notification_type": "permission" }`

### PermissionRequest

工具执行需要用户授权时触发。

**matcher 匹配：** 工具名

**额外输入字段：**

`{ "tool_name": "Bash", "tool_input": {"command": "rm -rf node_modules"} }`

## 场景示例

### 桌面通知提醒

当 Agent 完成任务或需要授权时，弹出桌面通知。

脚本 `~/.qwenwork/hooks/notify.sh`（macOS）：

\`#!/bin/bash
input=\$(cat)
message=$(echo $
input" \| jq -r '.message')

if echo "\$message" \| grep -q "^Agent"; then
 osascript -e 'display notification "任务执行完成" with title "QwenWork"'
else
 osascript -e 'display notification "任务需要授权" with title "QwenWork"'
fi

exit 0\`

配置：

`{ "hooks": { "Notification": [ { "hooks": [ { "type": "command", "command": "~/.qwenwork/hooks/notify.sh" } ] } ] } }`

### 写文件后自动 Lint

每次 Agent 写入或编辑文件后，自动执行 lint 检查。

脚本 `${project}/.qwenwork/hooks/auto-lint.sh`：

\`#!/bin/bash
input=\$(cat)
file\_path=$(echo $
input" \| jq -r '.tool\_input.file\_path')

case "\$file\_path" in  *.js\|*.ts\|*.jsx\|*.tsx)
 npx eslint "\$file\_path" --fix 2\>/dev/null
 ;;
esac

exit 0\`

配置：事件 `PostToolUse`，matcher `Write|Edit`，command `.qwenwork/hooks/auto-lint.sh`。

### 让 Agent 继续工作

在 Agent 停止时检查是否还有未完成的任务，如果有则注入消息让 Agent 继续。

脚本 `~/.qwenwork/hooks/check-continue.sh`：

\`#!/bin/bash
if \[ -n "\$(git status --porcelain 2\>/dev/null)" \]; then
 echo "检测到未提交的变更，请完成 git commit" \>&2
 exit 2
fi

exit 0\`

配置：事件 `Stop`，command `~/.qwenwork/hooks/check-continue.sh`。



<span style="color: rgb(73, 70, 65); background-color: rgb(245, 247, 240);">***来源：千文办公 官方指南。***</span>
