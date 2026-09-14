# 文档发布范围与准备稿

当前提供 327 篇中英文正文、2 份接口规范和 Postman 导入文件，另有 20 篇中英文准备稿。是否进入用户目录，按教程依赖的内容判断；工作区尚未完成配置，本身不是隐藏配置教程的理由。

## 配置与使用说明

以下 10 篇配置与使用说明列入正常目录。使用前需完成相应的部署配置和工作区授权。应用注册、凭据、回调、事件接收、后台服务及功能开关，由部署管理员完成；普通用户按正文执行授权、选择范围和使用步骤。

| 主题 | 类型 | 部署前提 | 文章 |
| --- | --- | --- | --- |
| GitHub 工具 | 应用配置 | 注册并配置相应用途的 GitHub App、凭据与回调，再授权仓库。 | [EN](en/docs/user-documentation/agents/tools/github.md) · [中文](zh-cn/docs/user-documentation/agents/tools/github.md) |
| Monday 工具 | OAuth 配置 | 注册自己的 Monday OAuth 应用，填写部署回调和凭据；从 Counso 发起授权，不沿用原教程的固定应用 ID。 | [EN](en/docs/user-documentation/agents/tools/monday-com.md) · [中文](zh-cn/docs/user-documentation/agents/tools/monday-com.md) |
| 外部客户端连接 Counso MCP | 服务与 OAuth 配置 | 配置 MCP 服务与 OAuth 授权，客户端按文档连接实际端点。 | [EN](en/docs/user-documentation/agents/integrations/counso-mcp-server.md) · [中文](zh-cn/docs/user-documentation/agents/integrations/counso-mcp-server.md) |
| Slack 自动回复 | 配置与部署 | 配置独立 Slack Bot 应用及消息接收服务，再选择频道和智能体；与数据同步连接分开。 | [EN](en/docs/user-documentation/agents/integrations/counso-in-slack/slack-auto-reply.md) · [中文](zh-cn/docs/user-documentation/agents/integrations/counso-in-slack/slack-auto-reply.md) |
| Slack Workflow | 管理员授权 | 配置 Slack Bot，并由部署管理员登记 Workflow 名称及允许访问的受限 Space。 | [EN](en/docs/user-documentation/agents/integrations/counso-in-slack/slack-workflows.md) · [中文](zh-cn/docs/user-documentation/agents/integrations/counso-in-slack/slack-workflows.md) |
| Slack 自动加入频道 | 配置与开关 | 先配置 Slack 数据连接和事件接收，再启用自动加入并设置匹配规则。 | [EN](en/docs/user-documentation/agents/integrations/counso-in-slack/slack-auto-join.md) · [中文](zh-cn/docs/user-documentation/agents/integrations/counso-in-slack/slack-auto-join.md) |
| 会议转录 | 使用与自动化配置 | 普通使用说明保留；自动处理另外要求转录来源、后台处理服务和工作区设置。 | [EN](en/docs/user-documentation/agents/integrations/meeting-transcripts.md) · [中文](zh-cn/docs/user-documentation/agents/integrations/meeting-transcripts.md) |
| GitHub 数据同步 | 应用配置 | 注册并配置相应用途的 GitHub App、凭据与回调，再授权仓库。 | [EN](en/docs/user-documentation/admins/connections-management/github.md) · [中文](zh-cn/docs/user-documentation/admins/connections-management/github.md) |
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
| Counso CLI | 命令行客户端 | [https://docs.dust.tt/docs/developer-platform/dust-cli/dust-cli](https://docs.dust.tt/docs/developer-platform/dust-cli/dust-cli) | 提供按 Counso 服务地址和登录配置构建的 CLI。已检查的 `@dust-tt/dust-cli@0.4.6` 把默认服务配置编译进包内，不能仅用运行时环境变量切换。 | [EN](prepared/en/docs/developer-platform/counso-cli/counso-cli.md) · [中文](prepared/zh-cn/docs/developer-platform/counso-cli/counso-cli.md) |

导入概念、资料整理和核对方法可以介绍；当前保留为准备稿的是具体脚本教程。仅将源平台凭据填入原脚本，不会自动把原站上传目标改成 Counso。数据导入可使用已提供的 API 说明；这里列的是具体导入脚本及其使用稿。

## API 与开发资料

126 篇接口参考、8 篇开发指南和 2 份接口规范已纳入中英文文档。原始 URL、原文文件与改写正文仍逐篇对应；CLI 使用稿另列在准备稿中。普通配置尚未完成，不再作为排除 API 或连接器说明的理由。

| 材料 | 内容 |
| --- | --- |
| API 参考 | 工作区 API、用户会话接口、客户端 MCP、登录流程与 Webhook；按各接口的认证方式使用。 |
| OpenAPI / Swagger | 两个文件均为 OpenAPI 3.0 格式，统一包含 126 个操作，默认服务地址为 `https://app.counso.ai`。 |
| Postman | 集合与环境文件包含完整请求，分别使用工作区 API key、用户 token 或接口自身的认证参数；凭据值留空。 |
| JavaScript SDK | 使用已发布的客户端包，并在初始化时明确指定 Counso 地址。包名、类名和 API 字段保留可执行的技术标识。 |

[英文 API 入口](en/docs/developer-platform/counso-api-documentation/openapi-and-postman.md) · [中文 API 入口](zh-cn/docs/developer-platform/counso-api-documentation/openapi-and-postman.md)

接口规范中有三处原始资料差异一并修正：

- `openapi.json` 原先少了列出触发器、获取触发器两个操作，已按同一来源的 `swagger.json` 补齐。
- 两个用量筛选接口使用 Path Item 引用，原文章未展开请求定义。现已展开个人与智能体两个路径，并为智能体路径补上必填的 `aId` 参数，原文章 URL 不变。
- Webhook 接收接口按实现保留生成 URL 的密钥路径，不再写成普通 Bearer 认证；配置签名校验时还需提交对应签名。会话 API 的用户身份与工作区 API key 也分别说明。

认证和 Webhook 修正参考[认证中间件](https://github.com/dust-tt/dust/tree/c0dd3d7/front-api/middlewares)及[Webhook 路由](https://github.com/dust-tt/dust/tree/c0dd3d7/front-api/routes/v1/w/%5BwId%5D/triggers/hooks)。部署时，API 服务和身份服务须使用同一 Counso 环境的配置；这里的文档与格式校验不代表生产接口已逐项调用验收。

资料源视图的父节点更新存在一处源契约歧义：`parentsIn` 的 OpenAPI `oneOf` 分支与实现中的联合校验不完全一致。本版保留原字段定义，Postman 使用 `parentsToAdd` / `parentsToRemove` 请求；不把文档改写当成服务端问题已修复。

Postman 页面提供文件和 URL 导入方式，不再引用原产品的公共集合 ID。若需要一键 Fork 的 Run in Postman 按钮，应从 Counso 管理的公开 Postman 集合生成真实链接；现有集合文件可直接导入使用。

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
