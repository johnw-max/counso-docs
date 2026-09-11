# Power BI 工具

# Power BI 工具

## 前提

需要 Entra 管理员、Power BI 账号，以及租户中可用的 Power BI MCP 设置。Entra 应用、Power BI 租户设置和工具连接是三个独立步骤。

## 注册 Entra 应用

1. 在 **Microsoft Entra 管理中心 → Identity → Applications → App registrations → New registration** 创建仅限组织目录的应用。
2. 记录 **Application (client) ID** 和 **Directory (tenant) ID**。
3. 在 **Authentication → Add a platform → Web** 中加入当前 Counso 设置页为工作区区域显示的每个回调值，不要复制其他环境的值。
4. 仅当当前表单要求时启用 public client flows 并保存。
5. 在 **Certificates & secrets → Client secrets → New client secret** 创建短有效期密钥，并立即复制 **Value**。

在 **API permissions → APIs my organisation uses → Power BI Service → Delegated permissions** 增加 `Dataset.Read.All`、`Report.Read.All`、`Dashboard.Read.All`、`Workspace.Read.All`，然后授予管理员同意。删除任务不需要的范围。

## 启用 Power BI MCP

在 Power BI 或 Fabric 管理门户打开 **Tenant settings → Integration settings**，为目标安全组或租户启用 **Users can use the Power BI Model Context Protocol server endpoint (preview)**。测试期间保持范围最小；若目标模型要求 XMLA，再单独启用对应租户设置。

## 添加工具

1. 打开管理员工具控制，选择 **Add remote MCP server**。
2. 填写服务商 MCP server URL：`https://api.fabric.microsoft.com/v1/mcp/powerbi`。
3. 选择 OAuth，填入 Entra client ID、client-secret value、授权 URL `https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/authorize`、令牌 URL `https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token`，以及 scope `https://analysis.windows.net/powerbi/api/.default offline_access`。将 `{TENANT_ID}` 换成 Directory (tenant) ID。
4. 保存并完成 Microsoft 登录。
5. 将工具加入 Agent，对一个已知 workspace、report、dataset 或 model 做只读请求。

最小成功结果是读取到当前用户在 Power BI 中可打开的 workspace 或 model。应用注册或 consent 成功本身不能证明模型可用。

## 常见问题

- `AADSTS700016`：使用 Application (client) ID，不要用 Object ID 或 secret ID。
- 功能不可用：启用 MCP 租户设置并检查安全组。
- 没有模型或报告：检查 workspace 成员、dataset 权限、租户策略和 XMLA 设置。
- 同意循环：逐项比较当前回调、租户 ID、secret value 和 scope。
