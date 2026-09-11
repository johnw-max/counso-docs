---
title: "NetSuite 工具"
topicId: "integrations/netsuite"
contentRevision: "45"
sidebar:
  hidden: true
---

# NetSuite 工具

## 前提

NetSuite 管理员需要启用 SuiteCloud 功能、安装 MCP Standard Tools SuiteApp、创建专用角色和 OAuth 集成记录。连接不能使用内置 Administrator 角色。

## 配置 NetSuite

1. 打开 **Setup → Company → Enable Features → SuiteCloud**，启用 **Server SuiteScript**、**REST Web Services**、**Token-Based Authentication** 和 **OAuth 2.0**。
2. 打开 **Customization → SuiteBundler → Search & Install Bundles**，搜索并安装 **MCP Standard Tools**。
3. 打开 **Setup → Users/Roles → Manage Roles → New**，创建专用 MCP 角色，将 `MCP Server Connection`、`Log in using OAuth 2.0 Access Tokens`、`REST Web Services`、`Perform Search` 权限设为 **Full**，并将角色分配给操作用户。
4. 打开 **Setup → Integration → Manage Integrations → New**。启用记录，选择 **Authorization Code Grant**、**Public Client**、**Dynamic Client Registration**，使用当前设置页提供的回调值，client name 填 `Counso`，scope 选择 **NetSuite AI Connector Service**。保存并复制 Consumer Key/Client ID 和 Consumer Secret。

## 连接工具

在管理员工具控制中选择 **Add tools → Add MCP server → Static OAuth**。将服务商 server URL 设为 `https://<accountid>.suitetalk.api.netsuite.com/services/mcp/v1/suiteapp/com.netsuite.mcpstandardtools`，把 `<accountid>` 换成 NetSuite account ID。授权 URL 使用 `https://<accountid>.app.netsuite.com/app/login/oauth2/authorize.nl`，令牌 URL 使用 `https://<accountid>.suitetalk.api.netsuite.com/services/rest/auth/oauth2/v1/token`；填入不带显示前缀的 Consumer Key、Consumer Secret 和 `mcp` scope。保存后用专用 NetSuite 角色认证，再把工具加入 Agent。

先进行一次该角色有权限的只读搜索或记录读取，再回到 NetSuite 检查同一记录。角色权限应小于 Administrator；写操作遵循工作区现有的确认和权限规则。

## 常见问题

- 找不到 MCP Server Connection：确认已安装 MCP Standard Tools SuiteApp。
- 登录无效：同意时选择专用 MCP 角色，不要选择 Administrator。
- 账号或角色错误：选择 **Choose another role** 后改用新建角色。
- Client ID 被拒绝：只填写 Consumer Key，不要加 `ID` 前缀。
- 回调不匹配：将所有回调值与当前设置页逐项比对。
