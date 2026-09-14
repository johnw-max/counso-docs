# 文档发布范围与准备稿

当前提供 193 篇中英文正文，另有 19 篇中英文准备稿。是否进入用户目录，按教程依赖的内容判断；工作区尚未完成配置，本身不是隐藏配置教程的理由。

## 配置与使用说明

以下 10 篇配置与使用说明列入正常目录。使用前需完成相应的部署配置和工作区授权。应用注册、凭据、回调、事件接收、后台服务及功能开关，由部署管理员完成；普通用户按正文执行授权、选择范围和使用步骤。

| 主题 | 类型 | 部署前提 | 文章 |
| --- | --- | --- | --- |
| GitHub 工具 | 应用配置 | 注册并配置相应用途的 GitHub App、凭据与回调，再授权仓库；上游已有对应工具或同步实现。 | [EN](en/docs/user-documentation/agents/tools/github.md) · [中文](zh-cn/docs/user-documentation/agents/tools/github.md) |
| Monday 工具 | OAuth 配置 | 注册自己的 Monday OAuth 应用，填写部署回调和凭据；从 Counso 发起授权，不沿用原教程的固定应用 ID。 | [EN](en/docs/user-documentation/agents/tools/monday-com.md) · [中文](zh-cn/docs/user-documentation/agents/tools/monday-com.md) |
| 外部客户端连接 Counso MCP | 服务与 OAuth 配置 | 部署 MCP 服务及其 OAuth 授权后提供实际端点；这篇是客户端使用说明，不开放 API/SDK 文档。 | [EN](en/docs/user-documentation/agents/integrations/counso-mcp-server.md) · [中文](zh-cn/docs/user-documentation/agents/integrations/counso-mcp-server.md) |
| Slack 自动回复 | 配置与部署 | 配置独立 Slack Bot 应用及消息接收服务，再选择频道和智能体；与数据同步连接分开。 | [EN](en/docs/user-documentation/agents/integrations/counso-in-slack/slack-auto-reply.md) · [中文](zh-cn/docs/user-documentation/agents/integrations/counso-in-slack/slack-auto-reply.md) |
| Slack Workflow | 管理员授权 | 配置 Slack Bot，并由部署管理员登记 Workflow 名称及允许访问的受限 Space。 | [EN](en/docs/user-documentation/agents/integrations/counso-in-slack/slack-workflows.md) · [中文](zh-cn/docs/user-documentation/agents/integrations/counso-in-slack/slack-workflows.md) |
| Slack 自动加入频道 | 配置与开关 | 先配置 Slack 数据连接和事件接收，再启用自动加入并设置匹配规则。 | [EN](en/docs/user-documentation/agents/integrations/counso-in-slack/slack-auto-join.md) · [中文](zh-cn/docs/user-documentation/agents/integrations/counso-in-slack/slack-auto-join.md) |
| 会议转录 | 使用与自动化配置 | 普通使用说明保留；自动处理另外要求转录来源、后台处理服务和工作区设置。 | [EN](en/docs/user-documentation/agents/integrations/meeting-transcripts.md) · [中文](zh-cn/docs/user-documentation/agents/integrations/meeting-transcripts.md) |
| GitHub 数据同步 | 应用配置 | 注册并配置相应用途的 GitHub App、凭据与回调，再授权仓库；上游已有对应工具或同步实现。 | [EN](en/docs/user-documentation/admins/connections-management/github.md) · [中文](zh-cn/docs/user-documentation/admins/connections-management/github.md) |
| Slack 数据同步 | 配置与部署 | 自建 Slack App 的凭据、当前部署的 OAuth 回调和事件接收地址；运行已有同步服务并开启相应设置。 | [EN](en/docs/user-documentation/admins/connections-management/slack.md) · [中文](zh-cn/docs/user-documentation/admins/connections-management/slack.md) |
| Slack 排障 | 使用说明 | 分别排查数据同步、对话机器人、个人工具，不把一类连接的权限套用到另一类。 | [EN](en/docs/user-documentation/admins/admin-troubleshooting/slack-troubleshooting.md) · [中文](zh-cn/docs/user-documentation/admins/admin-troubleshooting/slack-troubleshooting.md) |

Slack、GitHub 和 Monday 的源码提供配置自有应用的入口。原教程中的固定域名和应用 ID 是托管环境的值，不能直接用作 Counso 配置。注册并配置自己的应用后，可沿用已有集成实现。

## 已准备、暂不进入用户目录的文章

以下文章的双语品牌化稿件保存在 `prepared/`。正文保留用途、配置前提和使用流程；尚未提供的安装包、分发地址、脚本命令或服务地址不凭空补写。它们是适用的集成主题，并非永久排除的功能。

`translations.json` 的 `prepared` 字段关联这些稿件；当前站点只使用 `notice` 显示简短的“文档更新中”。提供对应交付物并核对具体步骤后，可将准备稿移入正常正文并开放入口。

| 主题 | 类别 | 原始 URL | 发布前还需补齐 | 准备稿 |
| --- | --- | --- | --- | --- |
| 产品支持指引 | 产品帮助 Skill | [https://docs.dust.tt/docs/user-documentation/agents/dust-support](https://docs.dust.tt/docs/user-documentation/agents/dust-support) | 将内置帮助检索来源和支持入口指向 Counso 文档，不沿用原产品知识源。 | [EN](prepared/en/docs/user-documentation/agents/counso-support.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/counso-support.md) |
| 通过邮件联系智能体 | 邮件服务 | [https://docs.dust.tt/docs/user-documentation/agents/integrations/send-and-forward-email-to-agents](https://docs.dust.tt/docs/user-documentation/agents/integrations/send-and-forward-email-to-agents) | 原实现包含固定收件域名；需设置 Counso 地址、邮件解析回调及回复服务。 | [EN](prepared/en/docs/user-documentation/agents/integrations/send-and-forward-email-to-agents.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/integrations/send-and-forward-email-to-agents.md) |
| 通过 Zapier 运行智能体 | 专用应用 | [https://docs.dust.tt/docs/user-documentation/agents/integrations/zapier](https://docs.dust.tt/docs/user-documentation/agents/integrations/zapier) | 提供 Counso Zapier 应用/动作及目标环境连接，不能使用原品牌应用代替。 | [EN](prepared/en/docs/user-documentation/agents/integrations/zapier.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/integrations/zapier.md) |
| 通过 Make 运行智能体 | 专用应用 | [https://docs.dust.tt/docs/user-documentation/agents/integrations/make-com](https://docs.dust.tt/docs/user-documentation/agents/integrations/make-com) | 提供 Counso Make 模块及连接配置。 | [EN](prepared/en/docs/user-documentation/agents/integrations/make-com.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/integrations/make-com.md) |
| 在 n8n 中使用 Counso | 节点包 | [https://docs.dust.tt/docs/user-documentation/agents/integrations/n8n](https://docs.dust.tt/docs/user-documentation/agents/integrations/n8n) | 现有节点固定连接原站的 US/EU 地址，需提供支持 Counso 地址和凭据的节点包。 | [EN](prepared/en/docs/user-documentation/agents/integrations/n8n.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/integrations/n8n.md) |
| 在 Power Automate 中使用 Counso | 连接器安装包 | [https://docs.dust.tt/docs/user-documentation/agents/integrations/power-automate](https://docs.dust.tt/docs/user-documentation/agents/integrations/power-automate) | 提供 Counso Solution 包及其中的主机、认证和动作配置。 | [EN](prepared/en/docs/user-documentation/agents/integrations/power-automate.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/integrations/power-automate.md) |
| 在 Google Sheets 中使用 Counso | 表格插件 | [https://docs.dust.tt/docs/user-documentation/agents/integrations/google-sheets-add-on](https://docs.dust.tt/docs/user-documentation/agents/integrations/google-sheets-add-on) | 提供 Counso 插件及安装、连接入口；原 Marketplace 插件不能视为我们的版本。 | [EN](prepared/en/docs/user-documentation/agents/integrations/google-sheets-add-on.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/integrations/google-sheets-add-on.md) |
| 在 Zendesk 中使用 Counso | Zendesk 应用 | [https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-zendesk](https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-zendesk) | 提供连接 Counso 服务与授权的应用包或分发入口。 | [EN](prepared/en/docs/user-documentation/agents/integrations/counso-in-zendesk.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/integrations/counso-in-zendesk.md) |
| 在浏览器中使用智能体 | 浏览器扩展 | [https://docs.dust.tt/docs/user-documentation/agents/integrations/browser-extension](https://docs.dust.tt/docs/user-documentation/agents/integrations/browser-extension) | 提供 Counso 扩展构建、登录配置和实际分发入口。 | [EN](prepared/en/docs/user-documentation/agents/integrations/browser-extension.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/integrations/browser-extension.md) |
| 通过 Raycast 使用 Counso | Raycast 扩展 | [https://docs.dust.tt/docs/user-documentation/agents/integrations/raycast-extension](https://docs.dust.tt/docs/user-documentation/agents/integrations/raycast-extension) | 扩展中的服务地址与 OAuth 客户端需指向 Counso，并提供安装来源。 | [EN](prepared/en/docs/user-documentation/agents/integrations/raycast-extension.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/integrations/raycast-extension.md) |
| 在 Microsoft Teams 中使用智能体 | Teams 应用包 | [https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-teams](https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-teams) | 提供 Counso Teams 应用包及对应机器人注册、消息服务和授权。 | [EN](prepared/en/docs/user-documentation/agents/integrations/counso-in-teams.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/integrations/counso-in-teams.md) |
| 将 Dropbox 文件导入 Counso | 导入脚本 | [https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-dropbox-files](https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-dropbox-files) | 提供面向 Counso 的脚本与运行配置，确认目标地址、授权、来源范围及更新处理方式；数据源本身可以使用。 | [EN](prepared/en/docs/user-documentation/data-sources/custom-connections/beta-import-dropbox-files.md) · [中文](prepared/zh-cn/docs/user-documentation/data-sources/custom-connections/beta-import-dropbox-files.md) |
| 将 Front 会话导入 Counso | 导入脚本 | [https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-front-conversations](https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-front-conversations) | 提供面向 Counso 的脚本与运行配置，确认目标地址、授权、来源范围及更新处理方式；数据源本身可以使用。 | [EN](prepared/en/docs/user-documentation/data-sources/custom-connections/beta-import-front-conversations.md) · [中文](prepared/zh-cn/docs/user-documentation/data-sources/custom-connections/beta-import-front-conversations.md) |
| 将 Guru 卡片导入 Counso | 导入脚本 | [https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-guru-cards](https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-guru-cards) | 提供面向 Counso 的脚本与运行配置，确认目标地址、授权、来源范围及更新处理方式；数据源本身可以使用。 | [EN](prepared/en/docs/user-documentation/data-sources/custom-connections/beta-import-guru-cards.md) · [中文](prepared/zh-cn/docs/user-documentation/data-sources/custom-connections/beta-import-guru-cards.md) |
| 将 HubSpot 公司摘要导入 Counso | 导入脚本 | [https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-hubspot-data](https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-hubspot-data) | 提供面向 Counso 的脚本与运行配置，确认目标地址、授权、来源范围及更新处理方式；数据源本身可以使用。 | [EN](prepared/en/docs/user-documentation/data-sources/custom-connections/beta-import-hubspot-data.md) · [中文](prepared/zh-cn/docs/user-documentation/data-sources/custom-connections/beta-import-hubspot-data.md) |
| 将 Jira Issue 导入 Counso | 导入脚本 | [https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-jira-issues](https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-jira-issues) | 提供面向 Counso 的脚本与运行配置，确认目标地址、授权、来源范围及更新处理方式；数据源本身可以使用。 | [EN](prepared/en/docs/user-documentation/data-sources/custom-connections/beta-import-jira-issues.md) · [中文](prepared/zh-cn/docs/user-documentation/data-sources/custom-connections/beta-import-jira-issues.md) |
| 将 Linear Issue 导入 Counso | 导入脚本 | [https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-linear-issues](https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-linear-issues) | 提供面向 Counso 的脚本与运行配置，确认目标地址、授权、来源范围及更新处理方式；数据源本身可以使用。 | [EN](prepared/en/docs/user-documentation/data-sources/custom-connections/beta-import-linear-issues.md) · [中文](prepared/zh-cn/docs/user-documentation/data-sources/custom-connections/beta-import-linear-issues.md) |
| 将 Salesforce 客户摘要导入 Counso | 导入脚本 | [https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-salesforce-data](https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-salesforce-data) | 提供面向 Counso 的脚本与运行配置，确认目标地址、授权、来源范围及更新处理方式；数据源本身可以使用。 | [EN](prepared/en/docs/user-documentation/data-sources/custom-connections/beta-import-salesforce-data.md) · [中文](prepared/zh-cn/docs/user-documentation/data-sources/custom-connections/beta-import-salesforce-data.md) |
| 通过 Zapier 上传文档 | 专用应用 | [https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/zapier-automatically-add-datasource](https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/zapier-automatically-add-datasource) | 提供 Counso Zapier 上传动作、凭据和目标资料库配置。 | [EN](prepared/en/docs/user-documentation/data-sources/custom-connections/zapier-automatically-add-datasource.md) · [中文](prepared/zh-cn/docs/user-documentation/data-sources/custom-connections/zapier-automatically-add-datasource.md) |

导入概念、资料整理和核对方法可以介绍；当前保留为准备稿的是具体脚本教程。仅将源平台凭据填入原脚本，不会自动把原站上传目标改成 Counso。公开 API 文档暂缓也不等于这些数据源不能连接。

## 本版不提供的开发资料（137 项）

公开 API、SDK、CLI、客户端开发接口及配套参考资料本版不对外提供，也不作为“更新中”页面展示。以下保留全部原始条目供查阅，其中 135 项来自站点地图，另有两份接口规范。

| 原文标题 | 原始 URL |
| --- | --- |
| Is there a Dust conversation API? | [https://docs.dust.tt/docs/user-documentation/getting-started/faq/managing-agents/is-there-a-dust-conversation-api](https://docs.dust.tt/docs/user-documentation/getting-started/faq/managing-agents/is-there-a-dust-conversation-api) |
| Client Side MCP Server (Preview) | [https://docs.dust.tt/docs/user-documentation/developers/client-side-mcp-server](https://docs.dust.tt/docs/user-documentation/developers/client-side-mcp-server) |
| Developer platform | [https://docs.dust.tt/docs/developer-platform/overview/developer-platform](https://docs.dust.tt/docs/developer-platform/overview/developer-platform) |
| JavaScript SDK | [https://docs.dust.tt/docs/developer-platform/overview/javascript-sdk](https://docs.dust.tt/docs/developer-platform/overview/javascript-sdk) |
| Datasources | [https://docs.dust.tt/docs/developer-platform/core-concepts/datasources](https://docs.dust.tt/docs/developer-platform/core-concepts/datasources) |
| Chunks and Documents | [https://docs.dust.tt/docs/developer-platform/core-concepts/chunks-and-documents](https://docs.dust.tt/docs/developer-platform/core-concepts/chunks-and-documents) |
| Rate Limits | [https://docs.dust.tt/docs/developer-platform/core-concepts/rate-limits](https://docs.dust.tt/docs/developer-platform/core-concepts/rate-limits) |
| OpenAPI & Postman | [https://docs.dust.tt/docs/developer-platform/dust-api-documentation/openapi-and-postman](https://docs.dust.tt/docs/developer-platform/dust-api-documentation/openapi-and-postman) |
| Get current user | [https://docs.dust.tt/api-reference/private-user/get-current-user](https://docs.dust.tt/api-reference/private-user/get-current-user) |
| Update current user | [https://docs.dust.tt/api-reference/private-user/update-current-user](https://docs.dust.tt/api-reference/private-user/update-current-user) |
| Export workspace analytics | [https://docs.dust.tt/api-reference/analytics/export-workspace-analytics](https://docs.dust.tt/api-reference/analytics/export-workspace-analytics) |
| List agents | [https://docs.dust.tt/api-reference/agents/list-agents](https://docs.dust.tt/api-reference/agents/list-agents) |
| Export agent configuration as YAML | [https://docs.dust.tt/api-reference/agents/export-agent-configuration-as-yaml](https://docs.dust.tt/api-reference/agents/export-agent-configuration-as-yaml) |
| Get agent configuration | [https://docs.dust.tt/api-reference/agents/get-agent-configuration](https://docs.dust.tt/api-reference/agents/get-agent-configuration) |
| Archive agent configuration | [https://docs.dust.tt/api-reference/agents/archive-agent-configuration](https://docs.dust.tt/api-reference/agents/archive-agent-configuration) |
| Update agent configuration | [https://docs.dust.tt/api-reference/agents/update-agent-configuration](https://docs.dust.tt/api-reference/agents/update-agent-configuration) |
| Import agent configuration | [https://docs.dust.tt/api-reference/agents/import-agent-configuration](https://docs.dust.tt/api-reference/agents/import-agent-configuration) |
| Search agents by name | [https://docs.dust.tt/api-reference/agents/search-agents-by-name](https://docs.dust.tt/api-reference/agents/search-agents-by-name) |
| Cancel message generation in a conversation | [https://docs.dust.tt/api-reference/conversations/cancel-message-generation-in-a-conversation](https://docs.dust.tt/api-reference/conversations/cancel-message-generation-in-a-conversation) |
| Create a content fragment | [https://docs.dust.tt/api-reference/conversations/create-a-content-fragment](https://docs.dust.tt/api-reference/conversations/create-a-content-fragment) |
| Get the events for a conversation | [https://docs.dust.tt/api-reference/conversations/get-the-events-for-a-conversation](https://docs.dust.tt/api-reference/conversations/get-the-events-for-a-conversation) |
| Download a conversation-scoped file by path | [https://docs.dust.tt/api-reference/conversations/download-a-conversation-scoped-file-by-path](https://docs.dust.tt/api-reference/conversations/download-a-conversation-scoped-file-by-path) |
| Get a conversation | [https://docs.dust.tt/api-reference/conversations/get-a-conversation](https://docs.dust.tt/api-reference/conversations/get-a-conversation) |
| Update a conversation | [https://docs.dust.tt/api-reference/conversations/update-a-conversation](https://docs.dust.tt/api-reference/conversations/update-a-conversation) |
| Answer a user question in a conversation message | [https://docs.dust.tt/api-reference/conversations/answer-a-user-question-in-a-conversation-message](https://docs.dust.tt/api-reference/conversations/answer-a-user-question-in-a-conversation-message) |
| Edit an existing message in a conversation | [https://docs.dust.tt/api-reference/conversations/edit-an-existing-message-in-a-conversation](https://docs.dust.tt/api-reference/conversations/edit-an-existing-message-in-a-conversation) |
| Get events for a message | [https://docs.dust.tt/api-reference/conversations/get-events-for-a-message](https://docs.dust.tt/api-reference/conversations/get-events-for-a-message) |
| Validate an action in a conversation message | [https://docs.dust.tt/api-reference/conversations/validate-an-action-in-a-conversation-message](https://docs.dust.tt/api-reference/conversations/validate-an-action-in-a-conversation-message) |
| Create a message | [https://docs.dust.tt/api-reference/conversations/create-a-message](https://docs.dust.tt/api-reference/conversations/create-a-message) |
| Create a new conversation | [https://docs.dust.tt/api-reference/conversations/create-a-new-conversation](https://docs.dust.tt/api-reference/conversations/create-a-new-conversation) |
| Create a file upload URL | [https://docs.dust.tt/api-reference/conversations/create-a-file-upload-url](https://docs.dust.tt/api-reference/conversations/create-a-file-upload-url) |
| Get feedbacks for a conversation | [https://docs.dust.tt/api-reference/feedbacks/get-feedbacks-for-a-conversation](https://docs.dust.tt/api-reference/feedbacks/get-feedbacks-for-a-conversation) |
| Submit feedback for a specific message in a conversation | [https://docs.dust.tt/api-reference/feedbacks/submit-feedback-for-a-specific-message-in-a-conversation](https://docs.dust.tt/api-reference/feedbacks/submit-feedback-for-a-specific-message-in-a-conversation) |
| Delete feedback for a specific message | [https://docs.dust.tt/api-reference/feedbacks/delete-feedback-for-a-specific-message](https://docs.dust.tt/api-reference/feedbacks/delete-feedback-for-a-specific-message) |
| Get mention suggestions for a conversation | [https://docs.dust.tt/api-reference/mentions/get-mention-suggestions-for-a-conversation](https://docs.dust.tt/api-reference/mentions/get-mention-suggestions-for-a-conversation) |
| Parse mentions in markdown text | [https://docs.dust.tt/api-reference/mentions/parse-mentions-in-markdown-text](https://docs.dust.tt/api-reference/mentions/parse-mentions-in-markdown-text) |
| Get mention suggestions | [https://docs.dust.tt/api-reference/mentions/get-mention-suggestions](https://docs.dust.tt/api-reference/mentions/get-mention-suggestions) |
| Deregister a client-side MCP server | [https://docs.dust.tt/api-reference/mcp/deregister-a-client-side-mcp-server](https://docs.dust.tt/api-reference/mcp/deregister-a-client-side-mcp-server) |
| Update heartbeat for a client-side MCP server | [https://docs.dust.tt/api-reference/mcp/update-heartbeat-for-a-client-side-mcp-server](https://docs.dust.tt/api-reference/mcp/update-heartbeat-for-a-client-side-mcp-server) |
| Register a client-side MCP server | [https://docs.dust.tt/api-reference/mcp/register-a-client-side-mcp-server](https://docs.dust.tt/api-reference/mcp/register-a-client-side-mcp-server) |
| Stream MCP tool requests for a workspace | [https://docs.dust.tt/api-reference/mcp/stream-mcp-tool-requests-for-a-workspace](https://docs.dust.tt/api-reference/mcp/stream-mcp-tool-requests-for-a-workspace) |
| Submit MCP tool execution results | [https://docs.dust.tt/api-reference/mcp/submit-mcp-tool-execution-results](https://docs.dust.tt/api-reference/mcp/submit-mcp-tool-execution-results) |
| Search for nodes in the workspace (streaming) | [https://docs.dust.tt/api-reference/search/search-for-nodes-in-the-workspace-streaming](https://docs.dust.tt/api-reference/search/search-for-nodes-in-the-workspace-streaming) |
| Search for nodes in the workspace | [https://docs.dust.tt/api-reference/search/search-for-nodes-in-the-workspace](https://docs.dust.tt/api-reference/search/search-for-nodes-in-the-workspace) |
| Upload a tool file | [https://docs.dust.tt/api-reference/search/upload-a-tool-file](https://docs.dust.tt/api-reference/search/upload-a-tool-file) |
| Archive a skill | [https://docs.dust.tt/api-reference/skills/archive-a-skill](https://docs.dust.tt/api-reference/skills/archive-a-skill) |
| List skills | [https://docs.dust.tt/api-reference/skills/list-skills](https://docs.dust.tt/api-reference/skills/list-skills) |
| Import skills from uploaded files | [https://docs.dust.tt/api-reference/skills/import-skills-from-uploaded-files](https://docs.dust.tt/api-reference/skills/import-skills-from-uploaded-files) |
| Get an app run | [https://docs.dust.tt/api-reference/apps/get-an-app-run](https://docs.dust.tt/api-reference/apps/get-an-app-run) |
| Create an app run | [https://docs.dust.tt/api-reference/apps/create-an-app-run](https://docs.dust.tt/api-reference/apps/create-an-app-run) |
| List apps | [https://docs.dust.tt/api-reference/apps/list-apps](https://docs.dust.tt/api-reference/apps/list-apps) |
| Get a data source view | [https://docs.dust.tt/api-reference/datasourceviews/get-a-data-source-view](https://docs.dust.tt/api-reference/datasourceviews/get-a-data-source-view) |
| Delete a data source view | [https://docs.dust.tt/api-reference/datasourceviews/delete-a-data-source-view](https://docs.dust.tt/api-reference/datasourceviews/delete-a-data-source-view) |
| Update a data source view | [https://docs.dust.tt/api-reference/datasourceviews/update-a-data-source-view](https://docs.dust.tt/api-reference/datasourceviews/update-a-data-source-view) |
| Search the data source view | [https://docs.dust.tt/api-reference/datasourceviews/search-the-data-source-view](https://docs.dust.tt/api-reference/datasourceviews/search-the-data-source-view) |
| List Data Source Views | [https://docs.dust.tt/api-reference/datasourceviews/list-data-source-views](https://docs.dust.tt/api-reference/datasourceviews/list-data-source-views) |
| Check the upsert queue status for a data source | [https://docs.dust.tt/api-reference/datasources/check-the-upsert-queue-status-for-a-data-source](https://docs.dust.tt/api-reference/datasources/check-the-upsert-queue-status-for-a-data-source) |
| Retrieve a document from a data source | [https://docs.dust.tt/api-reference/datasources/retrieve-a-document-from-a-data-source](https://docs.dust.tt/api-reference/datasources/retrieve-a-document-from-a-data-source) |
| Upsert a document in a data source | [https://docs.dust.tt/api-reference/datasources/upsert-a-document-in-a-data-source](https://docs.dust.tt/api-reference/datasources/upsert-a-document-in-a-data-source) |
| Delete a document from a data source | [https://docs.dust.tt/api-reference/datasources/delete-a-document-from-a-data-source](https://docs.dust.tt/api-reference/datasources/delete-a-document-from-a-data-source) |
| Update the parents of a document | [https://docs.dust.tt/api-reference/datasources/update-the-parents-of-a-document](https://docs.dust.tt/api-reference/datasources/update-the-parents-of-a-document) |
| Get documents | [https://docs.dust.tt/api-reference/datasources/get-documents](https://docs.dust.tt/api-reference/datasources/get-documents) |
| Search the data source | [https://docs.dust.tt/api-reference/datasources/search-the-data-source](https://docs.dust.tt/api-reference/datasources/search-the-data-source) |
| Get a table | [https://docs.dust.tt/api-reference/datasources/get-a-table](https://docs.dust.tt/api-reference/datasources/get-a-table) |
| Delete a table | [https://docs.dust.tt/api-reference/datasources/delete-a-table](https://docs.dust.tt/api-reference/datasources/delete-a-table) |
| Get a row | [https://docs.dust.tt/api-reference/datasources/get-a-row](https://docs.dust.tt/api-reference/datasources/get-a-row) |
| Delete a row | [https://docs.dust.tt/api-reference/datasources/delete-a-row](https://docs.dust.tt/api-reference/datasources/delete-a-row) |
| List rows | [https://docs.dust.tt/api-reference/datasources/list-rows](https://docs.dust.tt/api-reference/datasources/list-rows) |
| Upsert rows | [https://docs.dust.tt/api-reference/datasources/upsert-rows](https://docs.dust.tt/api-reference/datasources/upsert-rows) |
| Get tables | [https://docs.dust.tt/api-reference/datasources/get-tables](https://docs.dust.tt/api-reference/datasources/get-tables) |
| Upsert a table | [https://docs.dust.tt/api-reference/datasources/upsert-a-table](https://docs.dust.tt/api-reference/datasources/upsert-a-table) |
| Get data sources | [https://docs.dust.tt/api-reference/datasources/get-data-sources](https://docs.dust.tt/api-reference/datasources/get-data-sources) |
| List available MCP server views. | [https://docs.dust.tt/api-reference/tools/list-available-mcp-server-views](https://docs.dust.tt/api-reference/tools/list-available-mcp-server-views) |
| List available spaces. | [https://docs.dust.tt/api-reference/spaces/list-available-spaces](https://docs.dust.tt/api-reference/spaces/list-available-spaces) |
| Get a trigger | [https://docs.dust.tt/api-reference/triggers/get-a-trigger](https://docs.dust.tt/api-reference/triggers/get-a-trigger) |
| Receive external webhook to trigger flows | [https://docs.dust.tt/api-reference/triggers/receive-external-webhook-to-trigger-flows](https://docs.dust.tt/api-reference/triggers/receive-external-webhook-to-trigger-flows) |
| List triggers | [https://docs.dust.tt/api-reference/triggers/list-triggers](https://docs.dust.tt/api-reference/triggers/list-triggers) |
| List consumption analytics facets | [https://docs.dust.tt/api-reference/private-analytics/list-consumption-analytics-facets](https://docs.dust.tt/api-reference/private-analytics/list-consumption-analytics-facets) |
| List consumption analytics facets | [https://docs.dust.tt/api-reference/private-analytics/list-consumption-analytics-facets-1](https://docs.dust.tt/api-reference/private-analytics/list-consumption-analytics-facets-1) |
| List consumption analytics facets | [https://docs.dust.tt/api-reference/private-analytics/list-consumption-analytics-facets-2](https://docs.dust.tt/api-reference/private-analytics/list-consumption-analytics-facets-2) |
| List agent configurations | [https://docs.dust.tt/api-reference/private-agents/list-agent-configurations](https://docs.dust.tt/api-reference/private-agents/list-agent-configurations) |
| Create an agent configuration | [https://docs.dust.tt/api-reference/private-agents/create-an-agent-configuration](https://docs.dust.tt/api-reference/private-agents/create-an-agent-configuration) |
| Cancel message generation | [https://docs.dust.tt/api-reference/private-conversations/cancel-message-generation](https://docs.dust.tt/api-reference/private-conversations/cancel-message-generation) |
| Compact a conversation | [https://docs.dust.tt/api-reference/private-conversations/compact-a-conversation](https://docs.dust.tt/api-reference/private-conversations/compact-a-conversation) |
| Get a conversation credit attribution | [https://docs.dust.tt/api-reference/private-conversations/get-a-conversation-credit-attribution](https://docs.dust.tt/api-reference/private-conversations/get-a-conversation-credit-attribution) |
| Create a content fragment | [https://docs.dust.tt/api-reference/private-conversations/create-a-content-fragment](https://docs.dust.tt/api-reference/private-conversations/create-a-content-fragment) |
| Get conversation feedbacks | [https://docs.dust.tt/api-reference/private-conversations/get-conversation-feedbacks](https://docs.dust.tt/api-reference/private-conversations/get-conversation-feedbacks) |
| Get a conversation | [https://docs.dust.tt/api-reference/private-conversations/get-a-conversation](https://docs.dust.tt/api-reference/private-conversations/get-a-conversation) |
| Delete or leave a conversation | [https://docs.dust.tt/api-reference/private-conversations/delete-or-leave-a-conversation](https://docs.dust.tt/api-reference/private-conversations/delete-or-leave-a-conversation) |
| Update a conversation | [https://docs.dust.tt/api-reference/private-conversations/update-a-conversation](https://docs.dust.tt/api-reference/private-conversations/update-a-conversation) |
| Get conversation participants | [https://docs.dust.tt/api-reference/private-conversations/get-conversation-participants](https://docs.dust.tt/api-reference/private-conversations/get-conversation-participants) |
| Add a participant to a conversation | [https://docs.dust.tt/api-reference/private-conversations/add-a-participant-to-a-conversation](https://docs.dust.tt/api-reference/private-conversations/add-a-participant-to-a-conversation) |
| List selectable Spaces | [https://docs.dust.tt/api-reference/private-conversations/list-selectable-spaces](https://docs.dust.tt/api-reference/private-conversations/list-selectable-spaces) |
| Select Spaces for a conversation | [https://docs.dust.tt/api-reference/private-conversations/select-spaces-for-a-conversation](https://docs.dust.tt/api-reference/private-conversations/select-spaces-for-a-conversation) |
| Cancel a wake-up | [https://docs.dust.tt/api-reference/private-conversations/cancel-a-wake-up](https://docs.dust.tt/api-reference/private-conversations/cancel-a-wake-up) |
| List wake-ups for a conversation | [https://docs.dust.tt/api-reference/private-conversations/list-wake-ups-for-a-conversation](https://docs.dust.tt/api-reference/private-conversations/list-wake-ups-for-a-conversation) |
| List conversations | [https://docs.dust.tt/api-reference/private-conversations/list-conversations](https://docs.dust.tt/api-reference/private-conversations/list-conversations) |
| Create a conversation | [https://docs.dust.tt/api-reference/private-conversations/create-a-conversation](https://docs.dust.tt/api-reference/private-conversations/create-a-conversation) |
| Stream conversation events | [https://docs.dust.tt/api-reference/private-events/stream-conversation-events](https://docs.dust.tt/api-reference/private-events/stream-conversation-events) |
| Stream message events | [https://docs.dust.tt/api-reference/private-events/stream-message-events](https://docs.dust.tt/api-reference/private-events/stream-message-events) |
| Stream sandbox function invocation events | [https://docs.dust.tt/api-reference/private-events/stream-sandbox-function-invocation-events](https://docs.dust.tt/api-reference/private-events/stream-sandbox-function-invocation-events) |
| Get a single action | [https://docs.dust.tt/api-reference/private-messages/get-a-single-action](https://docs.dust.tt/api-reference/private-messages/get-a-single-action) |
| Get an agent message credit attribution | [https://docs.dust.tt/api-reference/private-messages/get-an-agent-message-credit-attribution](https://docs.dust.tt/api-reference/private-messages/get-an-agent-message-credit-attribution) |
| Edit a message | [https://docs.dust.tt/api-reference/private-messages/edit-a-message](https://docs.dust.tt/api-reference/private-messages/edit-a-message) |
| Submit message feedback | [https://docs.dust.tt/api-reference/private-messages/submit-message-feedback](https://docs.dust.tt/api-reference/private-messages/submit-message-feedback) |
| Delete message feedback | [https://docs.dust.tt/api-reference/private-messages/delete-message-feedback](https://docs.dust.tt/api-reference/private-messages/delete-message-feedback) |
| Get a message | [https://docs.dust.tt/api-reference/private-messages/get-a-message](https://docs.dust.tt/api-reference/private-messages/get-a-message) |
| Delete a message | [https://docs.dust.tt/api-reference/private-messages/delete-a-message](https://docs.dust.tt/api-reference/private-messages/delete-a-message) |
| Retry an agent message | [https://docs.dust.tt/api-reference/private-messages/retry-an-agent-message](https://docs.dust.tt/api-reference/private-messages/retry-an-agent-message) |
| List messages in a conversation | [https://docs.dust.tt/api-reference/private-messages/list-messages-in-a-conversation](https://docs.dust.tt/api-reference/private-messages/list-messages-in-a-conversation) |
| Post a message to a conversation | [https://docs.dust.tt/api-reference/private-messages/post-a-message-to-a-conversation](https://docs.dust.tt/api-reference/private-messages/post-a-message-to-a-conversation) |
| Resolve a conversation go template draft | [https://docs.dust.tt/api-reference/private-assistant/resolve-a-conversation-go-template-draft](https://docs.dust.tt/api-reference/private-assistant/resolve-a-conversation-go-template-draft) |
| Get mention suggestions | [https://docs.dust.tt/api-reference/private-mentions/get-mention-suggestions](https://docs.dust.tt/api-reference/private-mentions/get-mention-suggestions) |
| Get extension configuration | [https://docs.dust.tt/api-reference/private-extension/get-extension-configuration](https://docs.dust.tt/api-reference/private-extension/get-extension-configuration) |
| Get workspace feature flags | [https://docs.dust.tt/api-reference/private-workspace/get-workspace-feature-flags](https://docs.dust.tt/api-reference/private-workspace/get-workspace-feature-flags) |
| Get or download a file | [https://docs.dust.tt/api-reference/private-files/get-or-download-a-file](https://docs.dust.tt/api-reference/private-files/get-or-download-a-file) |
| Upload file content | [https://docs.dust.tt/api-reference/private-files/upload-file-content](https://docs.dust.tt/api-reference/private-files/upload-file-content) |
| Delete a file | [https://docs.dust.tt/api-reference/private-files/delete-a-file](https://docs.dust.tt/api-reference/private-files/delete-a-file) |
| Create a file upload | [https://docs.dust.tt/api-reference/private-files/create-a-file-upload](https://docs.dust.tt/api-reference/private-files/create-a-file-upload) |
| Get a data source view | [https://docs.dust.tt/api-reference/private-spaces/get-a-data-source-view](https://docs.dust.tt/api-reference/private-spaces/get-a-data-source-view) |
| Delete a data source view | [https://docs.dust.tt/api-reference/private-spaces/delete-a-data-source-view](https://docs.dust.tt/api-reference/private-spaces/delete-a-data-source-view) |
| Update a data source view | [https://docs.dust.tt/api-reference/private-spaces/update-a-data-source-view](https://docs.dust.tt/api-reference/private-spaces/update-a-data-source-view) |
| List data source views | [https://docs.dust.tt/api-reference/private-spaces/list-data-source-views](https://docs.dust.tt/api-reference/private-spaces/list-data-source-views) |
| Create a data source view | [https://docs.dust.tt/api-reference/private-spaces/create-a-data-source-view](https://docs.dust.tt/api-reference/private-spaces/create-a-data-source-view) |
| Get a space | [https://docs.dust.tt/api-reference/private-spaces/get-a-space](https://docs.dust.tt/api-reference/private-spaces/get-a-space) |
| Delete a space | [https://docs.dust.tt/api-reference/private-spaces/delete-a-space](https://docs.dust.tt/api-reference/private-spaces/delete-a-space) |
| Update a space | [https://docs.dust.tt/api-reference/private-spaces/update-a-space](https://docs.dust.tt/api-reference/private-spaces/update-a-space) |
| Get project notification preference | [https://docs.dust.tt/api-reference/private-spaces/get-project-notification-preference](https://docs.dust.tt/api-reference/private-spaces/get-project-notification-preference) |
| Set project notification preference | [https://docs.dust.tt/api-reference/private-spaces/set-project-notification-preference](https://docs.dust.tt/api-reference/private-spaces/set-project-notification-preference) |
| List spaces | [https://docs.dust.tt/api-reference/private-spaces/list-spaces](https://docs.dust.tt/api-reference/private-spaces/list-spaces) |
| Create a space | [https://docs.dust.tt/api-reference/private-spaces/create-a-space](https://docs.dust.tt/api-reference/private-spaces/create-a-space) |
| Initiate WorkOS login | [https://docs.dust.tt/api-reference/private-authentication/initiate-workos-login](https://docs.dust.tt/api-reference/private-authentication/initiate-workos-login) |
| Exchange code or refresh token | [https://docs.dust.tt/api-reference/private-authentication/exchange-code-or-refresh-token](https://docs.dust.tt/api-reference/private-authentication/exchange-code-or-refresh-token) |
| Revoke a session | [https://docs.dust.tt/api-reference/private-authentication/revoke-a-session](https://docs.dust.tt/api-reference/private-authentication/revoke-a-session) |
| Dust CLI | [https://docs.dust.tt/docs/developer-platform/dust-cli/dust-cli](https://docs.dust.tt/docs/developer-platform/dust-cli/dust-cli) |
| openapi | [https://docs.dust.tt/docs/developer-platform/dust-api-documentation/openapi.json](https://docs.dust.tt/docs/developer-platform/dust-api-documentation/openapi.json) |
| swagger | [https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json](https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json) |

## 不纳入 Counso 的历史内容（9 项）

这些内容属于原产品更新历史、实验仓库导航或已弃用框架，不作为 Counso 使用文档。原文继续保留。

| 原文标题 | 原始 URL | 原因 |
| --- | --- | --- |
| Changelog | [https://docs.dust.tt/docs/changelog](https://docs.dust.tt/docs/changelog) | 原产品的更新历史，不属于 Counso 更新记录。 |
| Dust-Labs repository | [https://docs.dust.tt/docs/developer-platform/dust-labs/dust-labs-repository](https://docs.dust.tt/docs/developer-platform/dust-labs/dust-labs-repository) | 原产品实验仓库的导航说明，不作为 Counso 使用文档。 |
| Creating Google Calendar events from a Dust agent | [https://docs.dust.tt/docs/user-documentation/deprecated/legacy-dust-apps/creating-google-calendar-events-from-a-dust-agent](https://docs.dust.tt/docs/user-documentation/deprecated/legacy-dust-apps/creating-google-calendar-events-from-a-dust-agent) | 已弃用的旧应用框架或其示例，不纳入 Counso 文档。 |
| Allowing an agent to send an email | [https://docs.dust.tt/docs/user-documentation/deprecated/legacy-dust-apps/allowing-an-agent-to-send-an-email](https://docs.dust.tt/docs/user-documentation/deprecated/legacy-dust-apps/allowing-an-agent-to-send-an-email) | 已弃用的旧应用框架或其示例，不纳入 Counso 文档。 |
| Dev : pre-configuring a custom MCP server | [https://docs.dust.tt/docs/user-documentation/deprecated/dev-pre-configuring-a-custom-mcp-server](https://docs.dust.tt/docs/user-documentation/deprecated/dev-pre-configuring-a-custom-mcp-server) | 已弃用的开发端 MCP 预配置方式；现行 MCP 接入说明已保留。 |
| What is a Dust App? | [https://docs.dust.tt/docs/developer-platform/legacy-dust-apps/what-is-a-dust-app](https://docs.dust.tt/docs/developer-platform/legacy-dust-apps/what-is-a-dust-app) | 已弃用的旧应用框架或其示例，不纳入 Counso 文档。 |
| Dust Apps: Core Concepts | [https://docs.dust.tt/docs/developer-platform/legacy-dust-apps/dust-apps-core-concepts](https://docs.dust.tt/docs/developer-platform/legacy-dust-apps/dust-apps-core-concepts) | 已弃用的旧应用框架或其示例，不纳入 Counso 文档。 |
| Build your first Dust App | [https://docs.dust.tt/docs/developer-platform/legacy-dust-apps/build-your-first-dust-app](https://docs.dust.tt/docs/developer-platform/legacy-dust-apps/build-your-first-dust-app) | 已弃用的旧应用框架或其示例，不纳入 Counso 文档。 |
| Core Blocks | [https://docs.dust.tt/docs/developer-platform/legacy-dust-apps/blocks/core-blocks](https://docs.dust.tt/docs/developer-platform/legacy-dust-apps/blocks/core-blocks) | 已弃用的旧应用框架或其示例，不纳入 Counso 文档。 |
