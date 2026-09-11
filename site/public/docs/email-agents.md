# Channels and message integrations

# Channels and message integrations

## Slack

Slack data synchronization, personal tools, and channel workflows have different identities and scopes. Use the [Slack guide](/en/integrations/slack/#slack-connections-and-tools) for channel selection, message permissions, and the difference between a connection and a tool.

## Microsoft Teams

A Teams tool can search, list, and send messages as an authorized user. A Teams Bot is a separate channel integration that requires an administrator to install or approve the app, associate it with the intended workspace, and define which conversations and threads it may receive. Test with a dedicated channel before inviting users. Keep the bot identity and tool identity distinct.

## Email agents

When the workspace offers **Email Agents**, an administrator enables it in **Capabilities** and checks the receiving address and sending identity. Members use the email address associated with their workspace identity to send a new message, copy an Agent into a thread, or forward an existing email. Use the exact Agent address displayed by the workspace.

State the task in the message and attach the files needed for this request. The Agent can read attachments actually included in that email; it cannot automatically retrieve attachments from earlier messages. It replies in the same thread to the initiating member. Other To or CC recipients do not automatically receive the Agent’s answer; the member can review and forward it when appropriate.

For example, forward an anonymized support thread and ask: “Summarize the symptom, steps already tried, and missing information. Return a reply draft first.” The Agent keeps its usual instructions, tools, and access scope. External actions that require confirmation request it first. A non-member cannot obtain Agent access simply by sending an email.

## Front

The Front tool can search conversations and contacts and may expose tags, assignment, replies, or comments when its token scopes allow them. A Front conversation import is a separate data-source path. Decide whether the task needs synchronized conversations or a live Front operation, then use the minimum inbox and team scope.

## Webhooks and other channels

Webhook filters select which incoming events may start a run. Define the event fields, authentication or signature requirements, and destination before enabling a source. See [Webhook triggers](/en/automations/webhooks/#trigger-an-agent-with-a-webhook).

## Common issues

- A channel receives duplicate messages: check Bot, workflow, tool, and webhook listeners separately.
- A message arrives without the expected identity: check the channel app and the credential owner.
- Email is received but no reply is sent: check outbound identity, routing, and provider permission.
- Front data is missing: distinguish imported conversation scope from live Front search.

[Documentation index](/en/) · [简体中文](/zh-cn/#连接与工具)
