# Gong 连接与工具

## Gong Connection

Gong Connection 默认同步工作区中的全部转录，标记为 Private 的转录除外。Gong 管理员和工作区管理员应先确认这一范围，并选择可以访问这些资料的 Space 成员。打开 **Spaces → Connections → Add connection → Gong**，完成 Gong consent，再将连接加入需要使用的 Space。Connection 同步转录文本，不控制实时录音；Gong 标记为 Private 的转录不会同步。

刷新后查找一个已知通话，对比参与者、日期、转录可用性和 Gong 中的可见性。转录新鲜度与实时读取分开检查。

## Gong Tool

打开 **Spaces → Tools → Add Tools → Gong** 完成 OAuth，并加入受限 Space。Gong API 结果可能包含认证用户之外的工作区通话，因此用 Space 成员关系控制访问。实时工具支持：带 ISO-8601 `fromDateTime`、`toDateTime` 和分页 cursor 的 `list_calls`；使用 `callId` 的 `get_call`；以及使用同一 `callId` 的 `get_call_transcript`。

先限定日期范围，再读取 `list_calls` 返回的一条 call ID。Gong 处理期间转录可能尚未可用。分享前检查 Space 受众和服务商敏感性。

## 常见问题

- 同步结果没有通话：检查团队、日期范围、Private 状态和刷新。
- 能列出通话但没有转录：等待 Gong 处理并检查转录权限。
- 结果范围过宽：限制 Space；个人 OAuth 不会自动限制工作区通话结果。

参阅[个人与共享访问](./personal-and-shared.md#个人与共享授权)和[连接与工具](./connections-and-tools.md#连接与工具)。
