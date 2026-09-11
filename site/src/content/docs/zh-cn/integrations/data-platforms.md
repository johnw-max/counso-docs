---
title: "数据平台连接与工具"
topicId: "integrations/data-platforms"
contentRevision: "45"
---

# 数据平台连接与工具

## BigQuery Connection

BigQuery Connection 保存 project、dataset、table 名称等元数据，不同步或存储全部查询行。Google Cloud 管理员应在目标项目 **IAM & Admin → Service Accounts → Create service account** 创建专用账号，授予最低 `roles/bigquery.user` 和 `roles/bigquery.dataViewer`，只有表单要求时才创建 JSON key 并安全保管。

在 **Spaces → Connections → Add connection → BigQuery** 粘贴 key，选择一个 dataset location（`US`、`EU` 或区域），再选择 datasets/tables；可开启使用 BigQuery 表和列描述的设置。先检查一个已知表和有边界的只读查询。同一 Connection 的数据集必须在同一 location，不能混合 `US` 与 `EU`。有元数据但没有数据时检查 project、数据集级 dataViewer 和查询 job 权限。

## Databricks SQL 与 Genie 工具

在 Databricks workspace 配置中复制 **workspace URL**，不要使用 Account Console URL。在 **Account Console → Settings → App Connections → Add connection** 创建命名 app connection，添加当前 OAuth 设置页提供的回调，保留 client-secret 生成，并按需要加入 `sql` + `offline_access`、`genie` + `offline_access` 或两组。复制 client ID 和 secret。

确认登录用户能访问目标 Unity Catalog catalog、schema、table、SQL warehouse 或 Genie 资源。在 **Spaces → Tools → Add Tools** 选择 Databricks SQL 或 Genie，输入 workspace URL、client ID 和 secret，完成 OAuth。先做 catalog/schema 发现或一次 Genie 提问。若有 IP access list，还需允许当前出站服务地址。

## Snowflake Connection

为同步表查询源创建专用 Snowflake role、service user 和 warehouse。给 role 授予目标 database/schema 的 `USAGE` 和目标 table 的 `SELECT`。测试可用密码，长期设置更适合 key-pair。在 **Spaces → Connections → Add connection → Snowflake** 填 account identifier、warehouse、role、user 和密码或 key-pair 字段，选择 tables，再执行 `list databases`、`list schemas`、`list tables`、`describe table`。

Connection 由管理员选择表范围，不提供任意 SQL 写入，并可返回更大的有边界结果。

## Snowflake Tool

实时 Snowflake Tool 需要管理员创建 OAuth security integration 并取得 client ID/secret，只给应有角色。在 **Spaces → Tools → Add Tools → Snowflake** 填 account/host、client ID、secret 和当前 OAuth 字段，选择个人或共享凭据。实际 Snowflake role 决定可见性。

工具支持 schema 浏览和只读单语句 SQL。先读取已知 database、schema、table 或 view，并使用有边界的 `SELECT`。每次执行有行数上限，不支持多语句及 `INSERT`、`UPDATE`、`DELETE`、`MERGE`、`COPY`。需要 view 或按用户 role 控制时用 Tool；需要管理员选择固定表集时用 Connection。

## 常见问题

- 有元数据但无行：检查精确的 provider role 和 dataset/catalog/schema/table grant。
- 查询不能执行：检查 warehouse/job quota、project/location、OAuth consent 和 IP allowlist。
- 个人与共享结果不同：比较实际 provider account、role、warehouse 和 Space。
- 查询要求写入：停止；本页仅覆盖只读检查。

参阅[个人与共享访问](/zh-cn/integrations/personal-and-shared/#个人与共享授权)和[连接与工具](/zh-cn/integrations/connections-and-tools/#连接与工具)。
