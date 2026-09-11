# Microsoft connections and tools

# Microsoft connections and tools

## Microsoft connection

Use a Microsoft **Connection** for selected SharePoint, OneDrive, and Microsoft 365 material that should be searchable in a Space. It uses an organisational account and the files, sites, groups, and Teams channels visible to that account.

1. Ask an Entra administrator to identify the account, sites, libraries, folders, and groups that may be exposed.
2. Open **Spaces → Connections → Add connection → Microsoft** and complete organisational-account consent.
3. If admin consent is requested, approve the Microsoft Graph delegated permissions for `Files.Read.All`, `Sites.Read.All`, `User.Read`, and `offline_access`. For site-limited access with `Sites.Selected`, have an administrator configure a separate service-principal connection and grant access to the selected sites.
4. Select the sites or folders and assign the connection to the target Space.
5. Refresh, search for one known document, and compare its SharePoint path and visibility with the provider.

Membership inherited through Microsoft 365 groups can broaden the visible scope. Review group membership as well as direct site membership. Connection refresh is periodic; a recent change may not appear immediately.

## SharePoint, OneDrive, and Excel tools

These live tools use the acting user’s delegated Microsoft identity. An Entra administrator first opens **Spaces → Tools → Add Tools**, selects the required Microsoft tool, and grants consent. The recorded permissions are:

- SharePoint/OneDrive: `User.Read`, `Files.ReadWrite.All`, `Sites.Read.All`, `ExternalItem.Read.All`, `offline_access`.
- Excel: `User.Read`, `Files.ReadWrite.All`, `Sites.Read.All`, `offline_access`.

Add the tool to the Agent, then sign in as the user who should own the action. Start with a known site, drive, file, workbook, worksheet, and range. Read the object before an upload or update, then read the same stable ID back.

## Outlook

For Outlook Mail, request delegated `Mail.ReadWrite`, `Mail.Send`, `User.Read`, `SensitivityLabel.Read`, and `offline_access`. Add `Mail.ReadWrite.Shared` and `Mail.Send.Shared` when shared or delegated mailboxes are needed, and `Contacts.ReadWrite` and `Contacts.ReadWrite.Shared` when contact access is needed. For Outlook Calendar, request `Calendars.ReadWrite`, `Calendars.ReadWrite.Shared`, `MailboxSettings.Read`, `User.Read`, and `offline_access`. The operator should begin with a read or draft. Verify the mailbox, folder, recipient, or event after every send or update.

## Teams tool and Teams Bot

The Teams tool is a live delegated tool for listing, searching, and sending messages. Its recorded permissions include `Team.ReadBasic.All`, `Channel.ReadBasic.All`, `Chat.Read`, `Chat.ReadWrite`, `ChatMessage.Read`, `ChatMessage.Send`, `ChannelMessage.Read.All`, `ChannelMessage.Send`, `User.Read`, `User.ReadBasic.All`, and `offline_access`, subject to the selected capability.

A Teams Bot is a separate channel integration. An administrator installs or approves the app, associates it with the intended workspace, and defines the teams, channels, or threads it may receive. Test in a dedicated channel and keep the bot identity separate from the user identity used by the Teams tool.

## Power BI

Power BI has its own setup and API permissions. Follow [Power BI](/en/integrations/power-bi/#power-bi-tool) for Entra app registration, tenant setting, and the MCP connection fields. An Entra app alone is not a working Power BI connection; verify one permitted workspace or model read.

## Common issues

- Consent succeeds but no site is searchable: check the selected library, Graph scope, group membership, and Space.
- Search works but upload or Excel update fails: check write permission on the exact site, folder, workbook, or range.
- Teams messages use the wrong identity: determine whether the request used the Teams tool or Teams Bot.
- Outlook sends from the wrong mailbox: check the acting account and shared-mailbox scope.

See [connections and tools](/en/integrations/connections-and-tools/#connections-and-tools) and [personal and shared access](/en/integrations/personal-and-shared/#personal-and-shared-credentials).
