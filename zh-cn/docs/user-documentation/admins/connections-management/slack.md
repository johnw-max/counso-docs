# 连接 Slack 知识

Slack 数据连接索引所选频道的消息，供助手搜索知识。它与 Slack 中的交互机器人、以及使用用户账号搜索或操作 Slack 的工具是分别配置的能力。

## 准备 Slack 应用

需要 Counso 工作区管理权限，以及在 Slack 工作区创建和安装应用的权限。数据同步使用工作区专用的 Slack 应用，并且需要在 Counso 工作区启用。如果看不到 Slack 连接选项，先请管理员确认是否已开通。启用后，使用当前部署提供的 Counso 应用清单；页面未提供时，再向管理员取得。清单中的 OAuth 回调、事件地址和交互地址必须对应当前部署；其他服务的清单无法直接连接 Counso。

1. 打开 [Slack 应用管理页](https://api.slack.com/apps)，选择 **Create New App > From a manifest**，再选择工作区。
2. 在 JSON 标签中粘贴提供的清单，核对权限后创建应用。
3. 打开 **Install App**，将应用安装到工作区。如果需要应用审批，由 Slack 管理员在工作区应用管理设置中批准。
4. 在 **Basic Information > App Credentials** 中取得 Client ID、Client Secret 和 Signing Secret，填入 **Spaces > Connections > Slack** 的对应字段。
5. 点击 **Connect**，完成 Slack 授权。

清单定义频道与消息、用户、文件、搜索相关权限，以及同步所需事件。安装时保留清单中的权限和地址，任何变更都需要与服务端配置一致。

## 选择频道

在 **Spaces > Connections > Slack > Add / Remove data** 中选择需要索引的频道并保存。私人频道需先邀请已配置的数据同步机器人，才可能出现在选择列表中。工作区还必须启用私人频道索引；仅邀请机器人并不会开启这项功能。

## 内容与刷新

连接索引所选频道的消息、线程和频道元数据。不索引机器人生成的消息、私信和外部文件。不要默认机器人加入前的历史消息已经全部导入，应在配置后检查频道实际可用的历史范围。

新消息通常会较快出现。调整所选频道后，可能需要几秒到几分钟，具体取决于资料量。建议把同一主题的讨论放在线程中；未使用线程时，搜索结果可能链接到频道中的大致位置，而不是精确消息。

频道标签使用 `channelId:...` 和 `channelName:...`，可用于[知识搜索工具](../../agents/knowledge/search-data-sources.md)的筛选。

## 维护连接

在 **Add / Remove data** 中调整频道，通过 **Manage Permissions** 控制哪些 Space 可使用 Slack 知识。如果需要轮换应用凭据，请立即在 **Manage > Edit** 中更新对应值，使连接能够恢复。

授权、迁移或频道缺失问题可查看 [Slack 故障排查](../admin-troubleshooting/slack-troubleshooting.md)；需要实时操作时，查看 [Slack 工具](../../agents/tools/slack-tools.md)。
