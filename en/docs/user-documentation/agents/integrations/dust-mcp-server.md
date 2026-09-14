# Connect an MCP client to Counso

Counso's MCP server lets a compatible external application work with your workspace. From an IDE or another AI assistant, you can find Agents, work with conversations, search Knowledge, and access Pod files and tasks using your Counso identity. Your workspace must have MCP server access enabled.

To give a Counso Agent access to an external service instead, see [Add a remote MCP server](../../admins/tools-management/adding-an-mcp-server.md).

## Connect your application

1. Obtain the MCP server URL for your Counso deployment from your workspace administrator. Use the published MCP endpoint, which ends in `/mcp`; a documentation URL is not a server endpoint.
2. In your application's MCP settings, add a remote server with that URL. The application must support remote MCP servers with OAuth.
3. Follow the sign-in prompt, sign in to Counso, and select the workspace you want to connect.
4. Once connected, ask the application to identify your workspace or list the Agents available to you.

The connection uses OAuth, not an API key. The application's instructions may differ, but it should start authorization when you add or connect the server.

## What you can do

The server can expose tools to:

- Identify the signed-in user and workspace, and list available Agents.
- List or start conversations, send messages, and retrieve conversation messages.
- Read Pod details and tasks.
- List, read, create, search, and resolve files associated with conversations or Pods.
- Search Knowledge across accessible Spaces.

The server's tool list depends on the version enabled in your workspace. It does not automatically expose every third-party Tool configured in Counso.

## Access and authentication

The application acts as the Counso user who authorized it. It can access only the Spaces, conversations, Pods, and files available to that user. Connecting an external client does not give it access to another member's private content.

Compatible clients can register through Dynamic Client Registration or identify themselves using a Client ID Metadata Document. They must send the OAuth `resource` parameter in both authorization and token requests so the token is issued for the intended MCP server. MCP tokens are scoped to this connection and are not interchangeable with workspace API keys.

Workspace administrators can disable MCP server access and control the redirect URIs permitted during authorization.

## If the connection fails

Check the server URL and confirm that your client supports remote MCP with OAuth, including the `resource` parameter. If authorization fails before the Counso sign-in screen, update the client and check its OAuth discovery support. If access is denied or a callback is rejected, ask your administrator to check that MCP server access is enabled and the client's redirect URI is allowed.

See [Access controls and permissions](../../admins/admin-governance/access-controls-and-permissions.md) for workspace access rules, and the [MCP authorization specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) for client compatibility requirements.
