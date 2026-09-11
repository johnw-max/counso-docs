---
title: "Filter, inspect, and export audit logs"
topicId: "administration/audit-logs"
contentRevision: "15"
---

# Filter, inspect, and export audit logs

Audit Logs give an administrator a time-ordered record of significant workspace actions. When the feature is enabled for a workspace, administrators and groups with the corresponding permission can use the viewer.

## Before you begin

Define the question you need to answer: a failed login, a changed agent, a membership change, an unexpected tool call, or a directory-sync event. Note the approximate time, actor, resource, and action. If the Audit Logs control is absent, ask an administrator to confirm that the feature and your access are enabled rather than treating an empty view as evidence that no events exist.

## Find the relevant events

1. Open the administration area and choose Audit Logs when that control is available.
2. Set the narrowest useful time range first. Use full-text search for a known actor, resource, action, or identifier, then widen the range only if necessary.
3. Filter the results around the event family. Useful families include agent creation or execution, tool execution, trigger and wake-up changes, space permissions, member and role changes, data-source authorization, user login, OAuth, SSO or directory sync, and conversation access.
4. Open a result and read the action, timestamp, actor, targets, context, and metadata together. The actor can be a human user or a system process. For agent and tool events, metadata can identify whether the initiating action was user-driven or AI-driven.
5. Compare a suspicious event with nearby events from the same actor and target. This helps separate one configuration change from the follow-up execution it caused.

Opening the viewer itself is recorded as `audit_log.viewed`. Include that fact when documenting an investigation.

## Export a review set

After the filters show the correct range, use the CSV export control if it is present in your viewer. Open the exported file and check its time range, row count, and representative events before sending it to the review team. Keep the filtered query and export timestamp with the file so another administrator can reproduce the selection.

## Key event groups

- **Identity:**`user.login`, `user.login_failed`, `user.logout`, identity merges, domain verification, SSO connection removal, and SCIM user or group changes.
- **Access:** member invitations and revocations, membership creation, role updates, space permission changes, and agent scope changes.
- **Agent activity:**`agent.created`, `agent.updated`, `agent.archived`, `agent.restored`, `agent.executed`, and `tool.executed`.
- **Automations:** trigger created, enabled, disabled, deleted, or fired; wake-up created, cancelled, expired, or fired.
- **Credentials and connections:** OAuth authorization or revocation, data-source reauthorization, external connector credential changes, MCP connection changes, and credential invalidation.

## Common questions

### Why can I not open Audit Logs?

Ask the workspace administrator to confirm that Audit Logs are enabled and check your administrator role or delegated audit-log permission.

### Does the actor field say whether AI was involved?

For agent and tool events, inspect the event metadata as well as the actor. The initiating user can remain the actor while metadata records the action type and initiating identity.

### Why did opening the viewer add an event?

The viewer access is itself recorded as `audit_log.viewed`, so an investigation should expect that event near the time it began.
