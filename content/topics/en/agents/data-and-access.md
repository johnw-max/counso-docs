# Manage Agent data and access

Data and access settings determine what an Agent can reach and which members can use it. Treat these settings as part of the Agent design, not as a final step after you add instructions.

## Set the smallest useful scope

1. Open the Agent editor and go to **Data and access**.
2. Select **Manage**.
3. Add only the Spaces or Pods required for the task.
4. Review the access note before confirming the selection.
5. Save the configuration and check that the selected scope is still shown when you reopen the Agent.

Adding a Space or Pod can expose its data to the Agent. The editor also explains that access is limited to members who have access to all the listed Spaces or Pods. Use this intersection as a reason to keep the list short and intentional. Do not add a broad company area when a restricted source is sufficient.

## Check the people who can use the Agent

Data access and Agent access are related but different. An Agent can have a narrow data scope and still be visible to more people than intended, or it can be correctly shared but lack access to the data needed for its task. Review both settings with the workspace administrator.

Test with non-sensitive material first. Ask the Agent to identify which source it used, then compare that result with the access settings. If the Agent should not see a source, remove it and confirm the configuration again before continuing.

For the Agent's name, editors, unpublished access, and tags, read [Manage and share an Agent](./manage-and-share.md#manage-and-share-an-agent).
