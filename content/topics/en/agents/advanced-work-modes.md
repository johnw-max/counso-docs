# Choose an advanced Agent work mode

Advanced work modes solve different collaboration problems. Availability depends on the workspace, your role, and the relevant Agent or Skill configuration. Use a mode only when its control is available; an administrator may need to enable a capability or grant access. Choose the smallest mode that fits the job.

## Before you begin

Write the goal, the allowed sources, the destination, and the point at which a person must review the result. Then choose a mode:

| Need | Use |
| --- | --- |
| Explore a different route without changing the original | **Branch** a conversation |
| Correct an Agent while it is working | **Steering** |
| Build or refine an Agent interactively | **Sidekick** in the Agent Builder |
| Research a complex question across sources | **@deep-dive** or the **Go Deep** Skill |
| Reuse a proven starting point | **Templates** in the Agent Builder |
| Run another Agent as a focused capability | **Run agent** configured for the Agent |
| Preserve user-specific preferences across conversations | **Memory** enabled for the Agent |
| Repeat a future action or check back later | **Wake-ups** available to the Agent |

## Branch and steer a conversation

Branch when you want a separate work stream, a transfer to another work line, or an alternative approach. When the Branch control is available, the new conversation starts from the selected point with a generated summary; the parent continues independently. Check the branch's files and permissions before sharing the result.

Steer when the current run is useful but needs new direction. If the live conversation accepts a message while the Agent is working, send the correction; it finishes its current action and then incorporates the queued message. Use steering for scope, source, or output corrections rather than starting over.

## Build with Sidekick or Templates

1. From the Agent Builder, open **Sidekick** when your role and workspace expose it, then describe the job in plain language.
2. Review its proposed instruction, tool, Skill, and knowledge changes as diffs.
3. Accept only the changes you want; edit or reject the rest.
4. If you start from **Templates**, treat the template as a starting point and tailor the instructions to your actual workflow before saving.
5. Preview the resulting Agent with safe sample material.

Sidekick suggestions are reviewable and do not replace the builder's decision. Sidekick can help configure an Agent, while Triggers and Skills still require their own setup.

## Use @deep-dive or Go Deep

Use **@deep-dive** when that workspace agent is available and a complex investigation needs multiple sources, data exploration, web research, or specialist sub-work. Use **Go Deep** when the Skill is available in the workspace and your role lets you add it to a custom Agent. State the scope, sources, exclusions, and desired deliverable. Read the cited evidence and review any created file or Frame before sharing it.

## Run an Agent as a capability

Use **Run agent** when the Agent has that capability configured and a focused specialist should perform an isolated subtask and return its result. Give it a self-contained brief, the allowed data, and a clear return format. Use this for independent research or a reusable specialist behavior; keep the parent Agent responsible for combining and checking the result.

## Use Memory and Wake-ups

Enable the **Memory** capability in the Agent Builder when an Agent should retain user-specific preferences or continuity across conversations. Ask it explicitly to remember a preference, and review or delete memories from the Agent details when those controls are available. Memory is user-specific; do not use it as a shared Pod record.

Use a **Wake-up** when the capability is available and an Agent should act at a future time, check for an answer, or refresh a Pod artifact. Ask the Agent to schedule it with a reason and cadence. Review the destination, owner, and repeat limit; cancel it from the conversation that created it when the work is no longer needed. A wake-up runs with the initiating user's authority.

## What you should see afterward

When a mode is enabled and used, the original conversation remains available after a branch, an in-progress run reflects a steering message, and the Agent Builder shows accepted configuration changes. A deep investigation returns a researched result, a sub-agent returns a bounded result, memory appears in the Agent's memory area, and a wake-up appears as a pending future action.

## Common questions

### Should I use a Skill or Run agent for a reusable procedure?

Use a Skill when several Agents should share instructions and tools. Use Run agent when the work needs a separate conversation and isolated investigation.

### Is a Frame automatically live after a deep investigation?

A generated Frame is a snapshot and needs to be regenerated or overwritten. A configured data-reading view can reflect saved Pod records and Tasks when it opens or when you use **Refresh**; it does not execute tasks while closed.

### Can another person change my wake-up?

Wake-ups use the initiating user's authority. Review or cancel one from the conversation that created it.

[Documentation index](../../../indexes/en.md) · [简体中文](../../../indexes/zh-cn.md#智能体配置与使用)
