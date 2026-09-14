# Troubleshoot the Slack integration

Slack features use different parts of the integration. First identify whether the problem is with message synchronization, the interactive Counso app, or a Slack Tool. Installing one component does not automatically enable the others.

| Component | What it does | What to check first |
|---|---|---|
| Data-sync app and connection | Joins selected channels and makes synchronized messages available to Agents | Is the app in the channel, and is the channel selected for sync into the intended Space? |
| Counso app | Lets members invoke Agents from Slack | Is the integration enabled, is the app in the channel, and are you mentioning it in a supported channel? |
| Slack Tools | Lets an Agent search or act in Slack | Is the Slack Tool connected and attached to the Agent, and which Slack identity will perform the action? |

## A channel does not appear or sync

- **Private channel missing:** Add the data-sync app to the private channel, then refresh the connection's channel list. A private channel stays private until an authorized member adds the app.
- **Channel visible but not syncing:** Being in the channel does not select it for synchronization. In **Spaces > Connections > Slack**, add the channel to the connection and the intended Space. If it is already selected, save the change and check sync status again.
- **Older messages missing:** A newly added app may only receive messages from the point it joined the channel. Check the channel's integration history and the provider's current sync behavior.
- **Permission list fails to load:** Confirm the Slack account has permission to manage the app and channels. If the workspace has many channels, the initial list may take time to load; retry after it finishes.
- **Channel is not available to an Agent:** Check which Space receives the synced data and whether the Agent and its user can access that Space.

## The Counso app does not reply

Confirm the Slack integration is enabled in workspace settings, the app is installed in the intended Slack workspace, and it has been added to the channel. Mention the app and include the question in the same message. Direct messages may not be supported by the workspace integration; use a channel or thread if that is the case.

The app typically receives the thread where it was mentioned, not the full channel history. Put relevant context in the message or mention it within a thread that contains the discussion. To call a specific Agent, use the Agent selector or the configured syntax such as `@Counso +agent-name`. A default Agent may be configurable for public channels; private channels may require explicitly selecting the Agent.

If the Agent should respond without a mention, a workspace administrator must enable automatic replies for that Agent and channel. Check whether the setting applies to every message or only top-level posts.

## A Slack Tool is missing or uses the wrong identity

- **Tool absent in Agent Builder:** Open **Spaces > Tools > Add Tools**, select Slack, and complete the personal authorization flow. Then add the Tool to the Agent.
- **Search misses results:** Check whether the Agent has a semantic-search option or only keyword search. With keyword search, try exact terms and alternate wording.
- **A post appears under your name:** A personal Slack connection performs actions as the authorizing user. If a bot identity is needed, check whether the workspace provides a Slack Bot Tool; it can act only in channels where the bot has been invited.
- **An action is denied:** Confirm the connected Slack identity has permission to perform that action and access the channel.

## Setup or authorization fails

Slack app installation or management may require an Owner, Admin, or App Manager. If a new app is pending approval, ask the Slack administrator to review it in the organization's app request area. When creating or editing a Slack app, follow the workspace's current Counso setup instructions and do not change OAuth scopes, redirect URLs, or signing credentials unless the setup guide instructs you to. If credentials were rotated, update them in the saved connection settings.

For an older connection, use the current workspace connection instructions to check whether it needs updating; do not rely on an old migration date.

## Known behavior

Synchronized bot messages may be excluded to avoid indexing Agent-generated text as source material. A workspace may support only one interactive Counso bot even if it synchronizes multiple Slack workspaces. Default-Agent behavior can be limited in private channels. When a message is not in a thread, a link to it may point near its location rather than to an exact message. Use threads when precise context and links matter.

## Prepare a useful support report

If the issue persists, record the steps, expected and actual behavior, error text, workspace name, Slack channel or thread link, and whether the issue affects one person or everyone. Share this through the support route provided by your organization. Do not include passwords or app secrets.
