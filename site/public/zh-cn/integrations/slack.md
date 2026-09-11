# Slack 连接与工具

# Slack 连接与工具

## Slack Connection：同步消息

需要 Slack Owner 或 Admin 以及工作区管理员。根据当前区域设置页的 manifest 创建专用 Slack app，安装到目标 Slack workspace，并在 **Basic Information → App Credentials** 复制 **Client ID**、**Client Secret**、**Signing Secret**。创建后不要修改 scopes、redirect URL 或 event URL；必须轮换 secret 时立即在 Connection 表单替换。

在 **Spaces → Connections → Add connection → Slack** 填入三个字段并完成授权。然后进入 **Add / Remove data** 选择 channel，分配到目标 Space。同步私有 channel 前先把 app 邀请进去。先用一个非敏感 channel 发一条带 thread 的测试消息，刷新后核对相同 channel 名称、ID 和 thread。

Connection 同步所选 channel 的消息、thread 和元数据，不同步机器人消息（包括 Slack Workflow 生成的消息）、私信或外部文件；app 加入前的历史消息不可用。新消息和 channel 变更可能需要几秒到几分钟。

## Slack Tool：个人操作

Slack Tool 使用实际用户的个人 OAuth 身份。管理员打开 **Spaces → Tools → Add Tools → Slack**，完成个人 OAuth 并加入 Agent。先搜索一个 channel 或读取一个 thread。工具可以搜索消息和 channel、列出用户、读取 thread、发送或定时发送消息；语义搜索只有 Slack 方案提供时可用。

写入时给出 channel ID 或 user ID、消息和可选 thread timestamp。用户用 `<@USER_ID>`，channel 用 `<#CHANNEL_ID>`，不要用展示名。定时消息不能附带文件；发送后回 Slack 读取。

## Slack Workflow 与渠道应用

Slack Workflow、auto-join、auto-reply 以及从 Slack 调用 Agent 的应用，都与同步 Connection 和个人 Tool 分开。管理员选择触发器、channel、Agent 和回复策略。启用 auto-reply 前先发布 Agent；auto-join 需要工作区已开通。配置完成后，在专用 channel 用非敏感事件测试。区分每个监听器的身份和目的地，避免重复回复。

## 常见问题

- 找不到 channel：检查 app 邀请、channel 范围、审批和刷新。
- 搜索链接只到近似消息：先发主题，再在 thread 中继续。
- 工具不显示：检查 Space、Agent 能力和个人 OAuth。
- 回复重复：分别检查 Workflow、auto-reply、Tool 和 webhook 监听器。

参阅[渠道](/zh-cn/integrations/channels/#渠道与消息集成)和[个人与共享访问](/zh-cn/integrations/personal-and-shared/#个人与共享授权)。
