# Connect Slack knowledge

The Slack connection indexes messages from selected channels for agent knowledge searches. It is separate from the interactive Slack bot and from Slack tools that search or act using a user's account.

## Prepare the Slack app

You need Counso workspace admin access and permission to create and install apps in the Slack workspace. Data synchronization uses a workspace-specific Slack app and must be enabled for your Counso workspace. If the Slack connection is absent, first ask an administrator to confirm availability. Once enabled, use the Counso app manifest supplied for the deployment; ask the administrator for it if the setup does not provide one. The manifest must contain the OAuth callback, event URL, and interaction URL for your deployment; a manifest belonging to another service will not connect to Counso.

1. Open [Slack's app dashboard](https://api.slack.com/apps), choose **Create New App > From a manifest**, and select the workspace.
2. Paste the supplied manifest in the JSON tab, review the requested scopes, and create the app.
3. Open **Install App** and install it to the workspace. If app approval is required, a Slack administrator must approve the request in the workspace's app management settings.
4. From **Basic Information > App Credentials**, copy the Client ID, Client Secret, and Signing Secret into the corresponding fields in **Spaces > Connections > Slack**.
5. Choose **Connect** and complete Slack authorization.

The manifest configures channel/message access, users, files, search, and the events needed to keep the selected content synchronized. Preserve its scopes and endpoints during installation; changes must match the server configuration.

## Select channels

In **Spaces > Connections > Slack > Add / Remove data**, select the channels to index and save. For a private channel, invite the configured data-sync bot first so the channel can appear in the selector. Private-channel indexing must also be enabled for your workspace; an invitation alone does not enable the feature.

## Content and freshness

The connection indexes messages, threads, and channel metadata for the selected channels. Bot-generated messages, direct messages, and external files are not indexed. Do not assume historical messages from before the bot joined are included; check the history available for the channel after setup.

New messages normally appear soon after they are posted. Changes to selected channels can take seconds or minutes, depending on volume. Use threads for related discussion: unthreaded content may link to an approximate channel location rather than a precise message.

Channel labels use `channelId:...` and `channelName:...` and can filter the [knowledge search tool](../../agents/knowledge/search-data-sources.md).

## Maintain the connection

Change the channel selection in **Add / Remove data**, and control which Spaces receive Slack knowledge through **Manage Permissions**. If app credentials must be rotated, update the corresponding values immediately in **Manage > Edit** so the connection can resume.

For authorization, migration, or missing-channel problems, see [Slack troubleshooting](../admin-troubleshooting/slack-troubleshooting.md). For live Slack actions, see [Slack tools](../../agents/tools/slack-tools.md).
