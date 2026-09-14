# What Agents can do in a Pod

An Agent may be able to work with the Pod where it is used, subject to its configuration and the acting user’s permissions. Available actions can include finding accessible Pods, reading or posting to conversations, searching Pod knowledge, working with tasks, and creating or updating files.

## Common actions

| Work area | Possible Agent action |
|---|---|
| Pod details | Read a Pod’s purpose and accessible membership; some configurations may allow an Editor to update details. |
| Conversations | Start a conversation or add a message where the user has access. |
| Knowledge | Search shared files and conversations that are within the Agent’s permitted scope. |
| Tasks | Create, assign, update, start, or complete a task when that action is enabled. |
| Files | Read, create, or update a Pod file when file access is enabled. |
| Shared display | Create a Frame or pin one only when the relevant capability and role are available. |

The exact set is visible in the Agent’s configuration and, where available, its activity details. Do not assume every Agent has all these capabilities.

## Permissions still apply

An Agent does not gain access to a Restricted Pod merely because it can search Pods. It works within the current user’s accessible Pods and the Agent’s configured data scope. Actions that change membership, settings, or shared content require the appropriate role and capability.

Before allowing an Agent to write, specify which file, task, or conversation it may change and what must remain untouched. Review the resulting item in the Pod. An Agent action is not automatically an external approval, payment, posting, or sent message.
