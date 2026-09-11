---
title: "NetSuite tool"
topicId: "integrations/netsuite"
contentRevision: "45"
---

# NetSuite tool

## Requirements

A NetSuite administrator must enable SuiteCloud features, install the MCP Standard Tools SuiteApp, create a dedicated role, and create an OAuth integration record. The built-in Administrator role is not used for this connection.

## Configure NetSuite

1. Open **Setup → Company → Enable Features → SuiteCloud** and enable **Server SuiteScript**, **REST Web Services**, **Token-Based Authentication**, and **OAuth 2.0**.
2. Open **Customization → SuiteBundler → Search & Install Bundles**, find **MCP Standard Tools**, and install it.
3. Open **Setup → Users/Roles → Manage Roles → New**. Create a dedicated MCP role and set `MCP Server Connection`, `Log in using OAuth 2.0 Access Tokens`, `REST Web Services`, and `Perform Search` to **Full**. Assign the role to the users who may operate the tool.
4. Open **Setup → Integration → Manage Integrations → New**. Enable the record and choose **Authorization Code Grant**, **Public Client**, **Dynamic Client Registration**, the current callback values supplied by the setup form, client name `Counso`, and scope **NetSuite AI Connector Service**. Save and copy the Consumer Key/Client ID and Consumer Secret.

## Connect the tool

In the administrator tool controls, choose **Add tools → Add MCP server → Static OAuth**. Set the provider server URL to `https://<accountid>.suitetalk.api.netsuite.com/services/mcp/v1/suiteapp/com.netsuite.mcpstandardtools`; replace `<accountid>` with the NetSuite account ID. Use authorization URL `https://<accountid>.app.netsuite.com/app/login/oauth2/authorize.nl`, token URL `https://<accountid>.suitetalk.api.netsuite.com/services/rest/auth/oauth2/v1/token`, the Consumer Key without any display prefix, the Consumer Secret, and scope `mcp`. Save, authenticate using the dedicated NetSuite role, and add the resulting tools to an Agent.

Start with one read-only search or record lookup that the role can access. Check the same record in NetSuite before reporting the result. Keep the role’s permissions narrower than Administrator; apply the workspace’s normal confirmation and permission rules to write-capable actions.

## Common issues

- MCP Server Connection permission is missing: verify that the MCP Standard Tools SuiteApp is installed.
- Invalid login: choose the dedicated MCP role at consent time, not Administrator.
- Wrong account or role: use **Choose another role** and select the role created above.
- Client ID rejected: enter only the Consumer Key value, without an `ID` prefix.
- Redirect mismatch: compare all callback values with the current setup page and use the current environment’s value.
