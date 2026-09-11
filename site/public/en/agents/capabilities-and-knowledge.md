# Add capabilities and knowledge

# Add capabilities and knowledge

An Agent can be configured with more than instructions. The editor groups capabilities and knowledge so you can decide what the Agent may use for a task.

## Choose what the Agent needs

Open the Agent editor and review **Capabilities and knowledge**. Consider the task in three parts:

- **Skills** provide reusable instructions and tools for a type of work.
- **Tools** represent actions the Agent may be able to perform.
- **Knowledge** gives the Agent sources to consult when preparing an answer.

Add only the items that serve the Agent's stated purpose. A larger configuration can make access and review harder. For a first version, start with the knowledge source and one clear capability needed for the result, then expand after you understand the output.

## Review the boundary

Read the description of each item before adding it. Check whether it can expose data, call an external service, or change a record. If the task requires a connection, make sure the relevant workspace access is configured separately and that the people who will use the Agent are authorised.

The editor also shows a **Triggers** section with an **Add triggers** control. A trigger can change when an Agent runs, so configure one only when your workspace has an approved use and you understand who owns the run and its result. Confirm any consequential result in the destination system.

Use a small, non-sensitive request to review the configured Agent. For access boundaries, read [Manage Agent data and access](/en/agents/data-and-access/#manage-agent-data-and-access); for the editor's inspection tools, read [Preview and improve an Agent](/en/agents/preview-and-improve/#preview-and-improve-an-agent).
