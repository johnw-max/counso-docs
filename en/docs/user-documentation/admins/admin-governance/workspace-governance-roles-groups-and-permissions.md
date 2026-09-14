# Workspace roles, groups, and permissions

Workspace roles set a member's baseline responsibilities. Group permissions add selected administrative capabilities. Access to a specific Space, Agent, or Skill is a separate resource-level decision. Review all three when someone can or cannot perform an action.

## Workspace roles

- **Admin:** manages workspace configuration, membership, and security settings. Some governance controls are reserved to admins.
- **Manager:** handles delegated membership and operational tasks, such as invitations and member requests, when those permissions are enabled. Billing and security management are not automatically part of the Manager role.
- **Member:** uses workspace resources according to assigned permissions and access to each resource.

The roles shown in your workspace determine the current actions available. Avoid assuming that a title alone grants access to every Space or connected data source.

## Groups and permission modes

Workspace groups can be maintained manually or synchronized from an identity provider when directory provisioning is configured. Permissions are commonly granted to groups so an organization can manage a team without editing each member individually. A member of several groups receives the combination of group permissions available to them; a group grant does not cancel access granted elsewhere.

A governance permission may be set for **Everyone**, selected **Groups**, or **Admin only**. Use the narrowest audience that can carry out the task. To grant an exception to one person, use an appropriately managed group if the workspace supports it.

## Common delegated permissions

Depending on the workspace, governance controls can include creating or publishing Agents and Skills, viewing audit records or analytics, managing billing or security, and publishing or sharing Frames. These permissions are independent: giving a Manager permission to publish an Agent does not necessarily give billing or security access.

## Review effective access

When diagnosing access, check the member's workspace role, group membership and grants, and the specific resource's audience and source permissions. Save one change at a time, then ask the affected member to retry the action. For controls that are not shown, ask an administrator to verify the workspace configuration.
