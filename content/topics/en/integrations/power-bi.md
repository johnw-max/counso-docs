# Power BI tool

## Requirements

Use an Entra administrator, a Power BI account, and a tenant where the Power BI MCP setting is available. The Entra app, Power BI tenant setting, and Counso tool connection are three separate steps.

## Register the Entra application

1. In **Microsoft Entra admin center → Identity → Applications → App registrations → New registration**, create an organisational-directory application.
2. Record the **Application (client) ID** and **Directory (tenant) ID**.
3. In **Authentication → Add a platform → Web**, add each redirect URI shown by the current Counso setup form for the workspace region. Do not copy a value from another environment.
4. Enable public client flows only when required by the current form and save.
5. In **Certificates & secrets → Client secrets → New client secret**, create a secret with the shortest acceptable lifetime and copy its **Value** immediately.

Under **API permissions → APIs my organisation uses → Power BI Service → Delegated permissions**, add `Dataset.Read.All`, `Report.Read.All`, `Dashboard.Read.All`, and `Workspace.Read.All`, then grant administrator consent. Remove any permission not needed by the selected tool.

## Enable Power BI MCP

In the Power BI or Fabric admin portal, open **Tenant settings → Integration settings** and enable **Users can use the Power BI Model Context Protocol server endpoint (preview)** for the intended security group or tenant. Keep the scope narrow while testing. If the tenant requires XMLA access for the selected model, enable that separately under the tenant settings.

## Add the tool

1. Open the administrator tool controls and choose **Add remote MCP server**.
2. Enter the provider MCP server URL `https://api.fabric.microsoft.com/v1/mcp/powerbi`.
3. Choose OAuth and fill the form with the Entra client ID, client-secret value, authorization URL `https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/authorize`, token URL `https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token`, and scope `https://analysis.windows.net/powerbi/api/.default offline_access`. Replace `{TENANT_ID}` with the Directory (tenant) ID.
4. Save and complete Microsoft sign-in.
5. Add the tool to an Agent and make one read-only request against a known workspace, report, dataset, or model.

The minimum successful result is a readable workspace or model object that the signed-in user can open in Power BI. An app registration or successful consent screen alone does not prove model access.

## Common issues

- `AADSTS700016`: use the Application (client) ID, not Object ID or secret ID.
- Feature unavailable: enable the MCP tenant setting and check the assigned security group.
- No model or report: check workspace membership, dataset permissions, tenant policy, and XMLA setting.
- Consent loops: compare the current callback, tenant ID, client secret value, and scope exactly with the setup form.
