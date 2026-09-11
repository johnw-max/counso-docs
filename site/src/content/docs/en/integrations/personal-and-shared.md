---
title: "Personal and shared credentials"
topicId: "integrations/personal-and-shared"
contentRevision: "45"
---

# Personal and shared credentials

## Personal credentials

Personal credentials make the signed-in user the provider actor. Use them when each person should see only the provider data they already have and when the provider must attribute an action to that person. The user must authorize the requested scope and may need to reconnect after a provider permission change.

## Shared credentials

Shared credentials make an administrator-owned account or service identity the provider actor. Use them only when the organisation has approved the shared scope, understands who can use it, and can remove or rotate the credential. A shared tool can expose more data than any one user normally sees, so keep it in the smallest suitable Space and Agent set.

## Select the model

Before adding a provider tool, answer:

1. Who should be accountable for the provider action?
2. Should the result follow each user’s provider membership?
3. Which Space and Agent may use the credential?
4. How will the administrator rotate or revoke it?
5. Which read-only and write/read-back checks will be repeated after a change?

Personal and Shared are provider-specific. A provider may support one mode, both modes, or neither. Do not infer support from the tool being listed.

## Reconnect and remove

When an owner leaves, a provider grant changes, or the Space membership changes, revoke or reconnect the affected credential, then run a small access check. For an external write, keep the provider receipt and read back the same object by stable ID. A configuration screen or assistant message is not an external acceptance receipt.

See [Connections and tools](/en/integrations/connections-and-tools/#connections-and-tools) for the general model and [remote MCP](/en/integrations/remote-mcp/#add-a-remote-mcp-server) for server-specific ownership.
