# Microsoft 连接与工具

# Microsoft 连接与工具

## Microsoft Connection

Microsoft **Connection** 用于将选定的 SharePoint、OneDrive 和 Microsoft 365 资料提供给 Space 检索。它使用组织账号，范围受该账号能看到的文件、站点、群组和 Teams channel 限制。

1. 请 Entra 管理员确定账号、sites、libraries、文件夹和群组范围。
2. 打开 **Spaces → Connections → Add connection → Microsoft**，完成组织账号 consent。
3. 需要管理员同意时，批准 Microsoft Graph 委派权限 `Files.Read.All`、`Sites.Read.All`、`User.Read`、`offline_access`。如需使用 `Sites.Selected` 限定站点，请由管理员另行配置服务主体连接，并授予对应站点的访问权限。
4. 选择 sites 或文件夹并分配到目标 Space。
5. 刷新后搜索一个已知文档，对比 SharePoint 路径和可见性。

Microsoft 365 群组继承的成员关系可能扩大范围；要同时检查直接站点成员和群组成员。Connection 按周期刷新，最近修改可能不会立即出现。

## SharePoint、OneDrive 和 Excel Tool

这些实时工具使用当前用户的 Microsoft 委派身份。Entra 管理员先在 **Spaces → Tools → Add Tools** 选择工具并完成 consent。所需权限包括：

- SharePoint/OneDrive：`User.Read`、`Files.ReadWrite.All`、`Sites.Read.All`、`ExternalItem.Read.All`、`offline_access`。
- Excel：`User.Read`、`Files.ReadWrite.All`、`Sites.Read.All`、`offline_access`。

将工具加入 Agent，并用应当承担动作的用户登录。先读取已知 site、drive、file、workbook、worksheet 和 range，再上传或更新；写入后按同一稳定 ID 读取。

## Outlook

Outlook Mail 请求委派权限 `Mail.ReadWrite`、`Mail.Send`、`User.Read`、`SensitivityLabel.Read` 和 `offline_access`。访问共享或委派邮箱时，按需增加 `Mail.ReadWrite.Shared` 和 `Mail.Send.Shared`；访问联系人时，按需增加 `Contacts.ReadWrite` 和 `Contacts.ReadWrite.Shared`。Outlook Calendar 请求 `Calendars.ReadWrite`、`Calendars.ReadWrite.Shared`、`MailboxSettings.Read`、`User.Read`、`offline_access`。先读取或创建草稿，发送或更新后检查邮箱、文件夹、收件人或事件。

## Teams Tool 与 Teams Bot

Teams Tool 是使用委派身份列出、搜索和发送消息的实时工具，常见权限包括 `Team.ReadBasic.All`、`Channel.ReadBasic.All`、`Chat.Read`、`Chat.ReadWrite`、`ChatMessage.Read`、`ChatMessage.Send`、`ChannelMessage.Read.All`、`ChannelMessage.Send`、`User.Read`、`User.ReadBasic.All`、`offline_access`，实际以所选能力为准。

Teams Bot 是独立的渠道集成。管理员安装或批准应用，关联目标工作区并定义可接收的 teams、channels 或 threads。先在专用 channel 测试，并把 Bot 身份与 Teams Tool 的用户身份分开。

## Power BI

Power BI 有独立的设置和 API 权限。参阅 [Power BI](/zh-cn/integrations/power-bi/#power-bi-工具) 完成 Entra 应用、租户设置和 MCP 字段。应用注册本身不等于 Power BI 已连接，要验证一个允许的 workspace 或 model 读取。

## 常见问题

- consent 成功但找不到站点：检查 library、Graph scope、群组成员和 Space。
- 可以搜索但不能上传或更新 Excel：检查精确 site、文件夹、workbook 或 range 的写权限。
- Teams 消息身份不对：确认使用的是 Teams Tool 还是 Teams Bot。
- Outlook 从错误邮箱发送：检查实际账号和 shared mailbox 范围。

参阅[连接与工具](/zh-cn/integrations/connections-and-tools/#连接与工具)和[个人与共享访问](/zh-cn/integrations/personal-and-shared/#个人与共享授权)。
