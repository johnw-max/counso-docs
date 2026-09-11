---
title: "Notion 连接与工具"
topicId: "integrations/notion"
contentRevision: "45"
---

# Notion 连接与工具

## Notion Connection

由同时具备 Notion 管理员和工作区管理员权限的人员选择目标 Space 要暴露的顶层页面、数据库和块。打开 **Spaces → Connections → Add connection → Notion**，在权限对话框选择顶层页面；敏感内容使用单页面选择。选择页面后，Connection 会同步并检索该页面树中的内容。创建、更新或评论内容需要另行配置 Notion Tool；保存前确认授权范围和同步边界。

首次刷新后搜索一个已知页面，对比父页面、数据库可见性和更新时间。链接视图不足时要分享数据库本身。页面出现在 **Orphaned resources** 时，恢复正确父页面分享并刷新。

## Notion Tool

Connection 可用后，在 **Agent Builder → Add tool** 添加 Notion。先决定 Agent 是否可以读取、创建、更新、评论或归档。工具支持页面读写、数据库行和 schema、块、页面/数据库搜索、评论与用户读取。

最小读取使用已知 page ID 或窄搜索，确认 parent 和 page ID。写入时先读取目标和父对象，说明要改的属性或 block，只做一次有边界改动，再按同一稳定 ID 读取检查内容、父级和权限。

## 常见问题

- 顶层页面分享后看不到子页面：分享正确的父或子页面并刷新。
- 能看到数据库但没有行：分享数据库本身，不只分享 linked view。
- 能读不能编辑：检查页面写权限和凭据负责人。
- 数据库有多个 data source：改用受支持的单一 data-source 数据库，或先拆分内容。

参阅[个人与共享访问](/zh-cn/integrations/personal-and-shared/#个人与共享授权)和[连接与工具](/zh-cn/integrations/connections-and-tools/#连接与工具)。
