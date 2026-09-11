# Google 连接与工具

# Google 连接与工具

## Google Drive Connection

当 Agent 需要在 Space 中搜索已索引文件时使用 Google Drive **Connection**。它使用管理员选择的 Google 账号和 Drive、文件夹或文件范围，不提供实时编辑。Workspace 管理员应：

1. 选择专用 Google Workspace 账号，确定目标 Space 可暴露的 Shared Drive、文件夹和文件。
2. 打开 **Spaces → Connections → Add connection → Google Drive**，用该账号完成 Google OAuth。
3. 选择 Drive 或文件夹范围并分配到目标 Space。
4. 首次刷新后搜索一个已知文件，和 Google Drive 对比标题、父路径、标签和可见性。

原生 Excel 文件需要先转换为 Google Sheets，才能通过 Google Drive Connection 同步并用于表格查询。提取文本超过 2 MB 的文件不会纳入索引；扫描图片类 PDF 不会自动进行 OCR。刷新时间和标签也会影响检索；找不到文件时检查账号能否打开文件以及父文件夹是否在范围内。

## Google Drive 与 Sheets Tool

原生 Google Drive Tool 是由当前用户授权的实时工具，适合精确文件操作。它与 Drive Connection 以及已弃用的 Google Sheets 工具分开。

1. 管理员打开 **Spaces → Tools → Add Tools → Google Drive**，填写当前设置表单要求的 Client ID 和 Client Secret。
2. 完成管理员 OAuth，使工具在 Space 可用。
3. 将 Google Drive 加入 Agent；首次使用时由实际操作用户连接自己的 Google 账号。
4. 从稳定 file ID 或精确标题开始。Sheets 请求要写明 spreadsheet、worksheet 和 range。
5. 写入前读取文档结构或 worksheet，完成有边界的改动，再在 Google Drive 重新读取同一文件和 range。

工具可以列出 Shared Drives、搜索文件、读 Docs/Sheets/Slides、查看表格范围、创建或复制文件、评论及更新文档/表格/演示文稿。它不提供整个 Drive 的语义检索；需要索引检索时使用 Connection。超过文档大小或单次返回字符限制时应分页处理。

## Gmail 与 Calendar 工具

Gmail 和 Google Calendar 是个人账号工具。实际执行者在添加工具时授权所需邮件或日历范围。先读取一封邮件、草稿或一个事件；发送、更新或创建事件后回到同一邮箱或日历检查。能读取但不能写入时检查账号写入范围和服务商权限。

## BigQuery

BigQuery 是数据平台 Connection，不是 Drive 文件来源。在 **IAM & Admin → Service Accounts** 创建专用 Google Cloud service account，按项目和数据集授予最低 `roles/bigquery.user` 与 `roles/bigquery.dataViewer`，安全保管 JSON key。在 **Spaces → Connections → Add connection → BigQuery** 粘贴 key，选择一个数据集 location，再选择数据集或表。一个 Connection 的数据集必须在同一 location。先检查一个已知表和有边界的只读查询。参阅[数据平台](/zh-cn/integrations/data-platforms/#数据平台连接与工具)。

## 常见问题

- 同步文件过期：检查 Drive 范围和刷新状态。
- Tool 能找到文件但不能更新：检查实际用户 Drive/Sheets 权限和 file ID。
- Sheets range 错误：先读取 worksheet，不要从标题推断行列。
- BigQuery 为空：检查 project、dataset location、角色和选中的表。

参阅[连接与工具](/zh-cn/integrations/connections-and-tools/#连接与工具)和[个人与共享访问](/zh-cn/integrations/personal-and-shared/#个人与共享授权)。
