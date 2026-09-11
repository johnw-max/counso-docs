# Slack connections and tools

# Slack connections and tools

## Slack connection: synchronized messages

A Slack Owner or Admin and a workspace administrator are required. Create a dedicated Slack app from the current regional manifest in the setup form, install it into the intended Slack workspace, and copy its **Client ID**, **Client Secret**, and **Signing Secret** from **Basic Information → App Credentials**. Do not edit scopes, redirect URLs, or event URLs after creation; if a secret must be rotated, replace it immediately in the connection form.

In **Spaces → Connections → Add connection → Slack**, enter those three fields and complete Slack authorization. Then open **Add / Remove data**, choose the channels, and assign the connection to the target Space. For a private channel, invite the sync app to the channel first. Start with one non-sensitive channel, post one threaded test message, and check that the same channel name, ID, and thread appear after refresh.

The connection syncs selected channel messages and threads plus channel metadata. It does not sync bot messages (including Slack Workflow messages), direct messages, or external files, and history before the app joined a channel is unavailable. New messages and channel changes may take seconds to minutes to appear.

## Slack tool: personal actions

The Slack tool uses the acting user’s personal OAuth identity. An administrator opens **Spaces → Tools → Add Tools → Slack**, completes the user OAuth flow, and adds the tool to an Agent. Start with a channel search or one thread read. The tool can search messages and channels, list users, read threads, post or schedule messages, and use semantic search only when the Slack plan exposes it.

For a write, name the channel ID or user ID, message text, and optional thread timestamp. Use `<@USER_ID>` and `<#CHANNEL_ID>` references rather than display names. Scheduled messages cannot include file attachments; read the posted message back in Slack.

## Slack workflows and channel apps

Slack Workflow, auto-join, auto-reply, and an app that calls an Agent are separate from both the synchronized Connection and the personal Tool. An administrator should choose the workflow trigger, channel, Agent, and reply policy. Publish the Agent before enabling auto-reply; auto-join must be enabled for the workspace. Test the configuration with a non-sensitive event in a dedicated channel. Keep each listener’s identity and destination distinct to avoid duplicate replies.

## Common issues

- A channel is absent: check app invitation, selected channel scope, approval, and connection refresh.
- Search links to an approximate message: post the topic first and continue in a thread.
- A tool is missing: check Space access, Agent capability, and personal OAuth.
- Replies appear twice: check Workflow, auto-reply, Tool, and webhook listeners separately.

See [channels](/en/integrations/channels/#channels-and-message-integrations) and [personal and shared access](/en/integrations/personal-and-shared/#personal-and-shared-credentials).
