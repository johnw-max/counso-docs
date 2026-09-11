# Confluence 连接与工具

# Confluence 连接与工具

## Confluence Connection

Confluence 管理员选择需要同步的全局 spaces。私有 spaces、设置了查看限制的页面及其子页面不会同步。在 **Spaces → Connections → Add connection → Confluence** 完成授权并选择范围。刷新后搜索已知页面，对比 space key、父级、labels 和版本。

更新 Connection 时重新检查权限和 labels。页面可能因父 space 可见，但页面 restriction 仍阻止正文访问。

## Confluence Tool

打开 **Spaces → Tools → Add Tools → Confluence**，完成服务商授权并加入 Agent。决定 Agent 是否可读取、创建、更新、移动或评论页面。工具支持页面、用户操作和 CQL 搜索。

读取测试从已知 page ID 或限定 space/title 的 CQL 开始。写入时先读页面和目标位置，只做一次变更或移动，再按同一 page ID 读取。个人凭据保留调用者权限，共享凭据以共享账号为实际操作者。

## 常见问题

- Connection 找到用户打不开的页面：同时检查 Space 成员关系和 Confluence restriction。
- CQL 返回过多：增加 space key、title、label 或 page ID 条件。
- 移动或更新失败：检查目标权限和页面 restriction。
- 刷新后没有新页面：检查父范围、labels 和刷新状态。

参阅[个人与共享访问](/zh-cn/integrations/personal-and-shared/#个人与共享授权)。
