---
title: "服务商工具目录"
topicId: "integrations/tools-catalog"
contentRevision: "45"
sidebar:
  hidden: true
---

# 服务商工具目录

## 添加服务商工具前

工作区管理员先确认服务商、账号类型和所需操作可用，再选择最小 Space 与 Agent 能力。在服务商管理控制台创建凭据，只授予下列任务所需范围；在当前 **Spaces → Tools → Add Tools** 表单中填写；先读取一个已知对象。导入或 Connection 与实时 Tool 分开。

## Ashby

在 **Ashby Admin → API Keys** 创建目标招聘工作区的密钥。只有需要写备注或推荐时才给 Candidates 读写；职位、报表、组织和招聘流程查找分别需要对应读取权限。只有确实要读取机密职位或私有候选人字段时才打开相应开关。在 **Spaces → Tools → Add Tools → Ashby** 粘贴 API key 并加入 Agent。最小检查是候选人搜索或职位列表。能认证但缺少对象结果，通常是对象权限不足。

## Freshservice

使用 Freshservice **Agent** 角色账号，不要用 Requester。确保角色可访问 Tickets、Service Catalog、Knowledge Base、Approvals。在工具表单填写 Freshservice domain URL 和 organization URL，启动 OAuth，接受请求的范围并加入 Agent。先按 ID 读取一个工单和字段定义，再执行回复或更新。工单可见但字段缺失通常是角色或字段可见性问题，另有服务商速率限制。

## Front

在 **Front → Settings → Integrations → API** 创建 Personal Access Token。读取需要 `conversations:read`、`messages:read`、`contacts:read`、`tags:read`、`teammates:read`；只有确需写入时才增加 `messages:send`、`comments:write`、`drafts:write`、`conversations:write` 或 `tags:write`。在 Front 工具表单粘贴 token，选择目标 inbox/team 并加入 Agent。先列出 inboxes，再读取一个会话及消息。缺少会话通常是 token 的团队成员关系或 inbox 范围不足。Front 导入仍是独立的资料来源路径。

## GitHub

**Connection：** 工作区管理员安装或批准 GitHub 应用，在 provider OAuth 中选择仓库，并把同步仓库范围分配到 Space。刷新后检查一个已知仓库文件或 Issue。

**Tool：** 明确使用工作区凭据还是个人凭据：前者使用配置的应用身份，后者同时受应用和调用用户权限限制。源设置没有逐 Agent 密钥字段；在 **Agent Builder → Add Tool** 添加 GitHub，并在 Agent 指令中写明允许的仓库。最小检查是读取一个仓库、Issue 或 Pull Request。缺仓库通常是应用安装范围或用户成员关系不足。

## HubSpot

在 HubSpot developer 或 app 设置中创建或选择已批准应用，只授予 Agent 需要的 CRM 对象范围，例如 contacts、companies、deals、tickets 或自定义对象。在 **Spaces → Tools → Add Tools → HubSpot** 完成 OAuth，选择工作区账号并加入 Agent。先调用 `Get Object Properties`，再按 ID 读取一个对象；属性结果可识别可写字段。能认证但没有对象结果通常是 app scope 或 private-app 政策问题。

## Intercom

**Connection：** 管理员选择 Intercom 团队或 Help Centre collections，完成授权并分配到 Space；刷新后检查一条会话和一篇文章。

**Tool：** 在服务商侧创建或选择应用，授予所需 conversation、contact、Help Centre 范围，在 **Spaces → Tools** 完成 OAuth 后加入 Agent。共享集合不等于所有会话都可见，需分别核对团队、集合、字段和刷新范围。

## Jira

在 Jira 选择 site 和 project，创建或选择凭据负责人。搜索至少需要 Browse Projects 与 issue read；只有需要写入时才增加 Create/Edit Issues 和 Transition Issues。在 Jira 工具表单选择 site 和凭据类型，再加入 Agent。先读取一个项目、Issue 和 workflow transition，再编辑。读取成功但 transition 失败，往往是 workflow 条件或项目权限不同。

## Monday

在 Monday 已批准的 workspace 中创建或选择凭据，选择 Agent 需要的 boards、groups、items、columns、subitems、comments 和 users。在工具表单完成 OAuth 或当前表单要求的凭据，选择个人或共享归属并加入 Agent。先读取一个 board 和 item（包括 column IDs）再更新。board 成员关系、私有 board 和列可见性常造成结果不完整。

## Productboard

Productboard 管理员启用已批准集成，按任务授权 feedback、users、companies、features。在 **Spaces → Tools → Add Tools → Productboard** 填写当前表单的认证字段并加入 Agent。先读取一个 feature 及其 ID；只有目标用户、公司和 feature 可见时才创建或关联一条反馈。登录成功但找不到 feature，通常是工作区或对象权限不足。

## Salesforce

在 Salesforce Setup 创建 **External Client App** 或已批准的 connected application。启用当前工具需要的 OAuth 流程，使用当前设置页提供的回调，并通过 permission set 授予最小对象和字段权限。记录 consumer key/secret，在 **Spaces → Tools** 完成 Salesforce 授权。先读取一个 Account 或 Contact，检查 API name 和 record ID。套餐、API 限额、字段级安全和 permission set 都可能在登录成功后阻止字段访问。

## Salesloft

在 Salesloft 管理中为目标负责人创建 API key，只授予所需 cadence、task、people、activity 范围。在 Salesloft 工具表单粘贴 API key，选择账号归属并加入 Agent。先读取一个 cadence 和一个 task，再创建或更新活动。能认证但缺少 cadence/task 结果，通常是 key scope 不足。

## Slab

Slab 管理员授权集成，并给目标 Space 可搜索的 topics 和 articles 读取权限。在 Slab 工具表单完成服务商授权，加入 Agent，先做一次 topic 搜索和 article 读取。没有共享给集成的私有 topic 仍不可见；工作区成员身份不代表文章可读。

## Statuspage

在 Statuspage 管理中创建或选择只读 page/component 凭据；只有获批操作员确实要改事故时才增加 incident create/update。填写当前工具表单的 page/account 和凭据，加入受限 Agent。先读取一个 page 和 component；写入事故后按 ID 读取同一事故。页面所有权和角色级别是常见阻塞点。

## UKG Ready

在 UKG Ready 管理中为租户创建 OAuth 应用，授予管理员批准的只读 workforce 范围。记录租户和应用值，在 **Spaces → Tools → Add Tools → UKG Ready** 完成 OAuth，加入 Agent 后读取一个允许的员工或 workforce 记录。租户配置、角色和个人数据限制可能阻止成功授权后的读取。

## Vanta

在 Vanta 管理中创建应用，选择安全测试、控制项和失败资源所需范围。在 **Spaces → Tools → Add Tools → Vanta** 填写当前 OAuth 字段，选择账号负责人并加入受限 Agent。先读取一个 test 及其状态，再请求整改数据。组织或测试所有权会限制结果。

## Zendesk

**Connection：** 在连接表单选择 brands、categories、工单状态、保留、隐藏、标签过滤和刷新设置；刷新后检查一个工单和一篇文章。

**Tool：** 在服务商侧创建或选择具备 ticket、user、Help Centre 范围的凭据，完成 OAuth 或 token 填写并加入 Agent。先读取所选 brand/category 内一个工单和一篇文章，再回复或更新。限速、客户字段隐藏和 brand 范围常造成结果不完整。Zendesk 渠道应用与这两条路径分开。

## Val Town

在 Val Town 授权目标账号并选择允许的 vals 和 files。在工具表单完成当前 OAuth 字段，加入 Agent，先执行 `list vals`、`get val` 或 `list val files`。执行、写文件、删除或 HTTP 调用前检查代码和端点影响。val 可见但其文件或端点权限可能不可用。

## Power BI 与 NetSuite

使用独立的 [Power BI](/zh-cn/integrations/power-bi/#power-bi-工具) 与 [NetSuite](/zh-cn/integrations/netsuite/#netsuite-工具) 页面。Power BI 需要 Entra 应用、委派权限、租户 MCP 设置和受限模型读取。NetSuite 需要 SuiteCloud 功能、MCP SuiteApp、专用角色和 OAuth 集成记录；不要使用 Administrator 角色。

## Airtable

在 Airtable 选择认证方式。共享设置可在 `airtable.com/create/tokens` 创建 Personal Access Token，授予 `data.records:read` 和读取结构所需的 `schema.bases:read`，需要写入或评论时再增加相应范围，并选择目标 bases；按用户授权则注册 OAuth integration，使用当前设置页的回调值。在 Airtable 工具表单使用 `https://mcp.airtable.com/mcp`，选择认证类型并填写 token 或 OAuth client 字段，再加入 Agent。先读取一个 base schema 和一条记录；能认证但没有表结果通常是 base 选择或 scope 不足。

## Asana

在 Asana 创建或选择已批准应用，完成 OAuth，并由管理员在 **My Apps → Manage distribution** 选择目标 workspace。在工具表单选择个人或工作区凭据，使用当前设置的 OAuth 字段，加入 Agent 后先读取一个 project 和 task，再创建或更新。能连接但无数据通常是应用未分发到目标 workspace 或用户不是项目成员。

## Attio

使用 `https://mcp.attio.com/mcp` 添加 Attio 远程 MCP，选择 Automatic OAuth，再选择目标 Space 和凭据负责人。加入 Agent 后先执行 `whoami`、`search-records` 或 `list-attribute-definitions`。创建/更新记录、任务、笔记和邮件遵循工作区写入确认规则。工具不出现时重新执行添加服务器流程并检查 Space 分享。

## Canva

Canva 管理员在 **Controls and permissions** 启用 AI Connector，再在 OAuth 流程选择已批准账号。从当前工具选择器添加 Canva 远程工具，仅分享给目标 Space。先用 `Search designs` 或按 ID `Get a design`；生成、调整尺寸、autofill 和导出属于产物操作，需要复核负责人。能力还取决于 Canva 套餐和模板权限。

## Fathom

打开 **Spaces → Tools → Add Tools → Fathom**，完成 OAuth，选择个人或共享凭据并分享给目标 Space。只读最小检查是带日期或团队过滤的 `list_meetings`，再用一个 `recording_id` 调用 `get_transcript`。会议、转录、摘要和 CRM 可见性可能不同，分享转录前检查录音身份。

## Miro

对于 Miro MCP，管理员打开 **Spaces → Tools → Add Tools → Miro MCP** 并完成 OAuth 2.1。Enterprise 组织需要先启用 Miro MCP server。加入 Agent 后先读取一个 board 或 board item，再创建图表或编辑内容。可见范围由 board 分享和团队成员关系决定；服务商托管的 MCP 支持以其当前控制台为准。

## Semrush

打开 **Spaces → Tools → Add Tools → Semrush MCP**，使用账号套餐可用的 API key 或 OAuth。前提是 Semrush One、SEO 或 Trends API 方案及足够 API units。加入 Agent 后先在有限时间范围运行一次关键词或域名报告，核对报告、units 和账号身份，再使用竞争或反向链接数据。

## Computer

工作区管理员打开 **Computer** 管理页面，在 **Network → Allowed domains** 中加入精确域名或批准的通配子域。在 **Environment variables → Config** 中保存非敏感值，变量名使用 `DST_` 前缀。API key 和 token 放在 **HTTPS secret**，使用 `DSEC_` 前缀并至少绑定一个允许域名；原始 secret 不会展示给智能体。只有需要让用户临时批准本次会话域名时才启用 Agent-requested domains。最小检查是读取一个允许 URL；无效或重复域名应在任务运行前被拒绝。

## 浏览器扩展

从浏览器官方扩展商店安装已批准扩展，登录目标工作区；只有用户明确许可后才启用浏览器标签访问。最小检查是将当前标签文本或截图附加到会话；扩展不应在没有请求或许可时读取页面。

## 文件、执行和自动化

对于 Computer、File Generation、Image Generation、Voice/sound generation，先定义输入文件、输出格式、目的地和复核负责人。最小结果是能打开且符合格式的产物；分享前检查公式、链接、尺寸和内容。

对于 Web Search & Browse，先指定允许的网站、时间范围和证据要求；结果是有来源的回答，不是私有连接资料。对于 JIT tools、浏览器扩展、会议转录，先完成服务商侧安装、身份、回调或 webhook 与事件范围，再运行一条可追踪事件，并检查服务商运行日志以防重复事件。

## 自定义导入

Dropbox、Front、Guru、HubSpot、Jira、Linear、Salesforce、Zapier 导入属于资料来源路径。选择服务商集合、导入负责人、刷新方式和目标 Space；核验一条导入对象及其 source ID。导入记录不会自动启用服务商实时 Tool。

Agent Memory、委派和定时提示词的配置，请参阅[高级工作方式](/zh-cn/agents/advanced-work-modes/#选择高级助手工作方式)。

## 常见问题

- 工具已列出但不可用：依次检查 Space、Agent 能力、服务商凭据和对象范围。
- 能读取但不能写入：检查精确对象权限，并回到服务商按稳定 ID 读取。
- 服务商要求回调或 webhook：复制当前设置页的值，并在服务商控制台核对。
- 资料过期：先确认使用的是 Connection 还是 Tool，再查刷新和服务商活动日志。

参阅[连接与工具](/zh-cn/integrations/connections-and-tools/#连接与工具)、[个人与共享访问](/zh-cn/integrations/personal-and-shared/#个人与共享授权)和[远程 MCP](/zh-cn/integrations/remote-mcp/#添加远程-mcp-服务器)。
