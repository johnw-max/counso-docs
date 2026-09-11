# Improve a Skill from real use

Improve a Skill from observed work: a correction, a missed tool call, an unclear result, or repeated user feedback is more useful than a broad rewrite.

## Before you begin

Collect a few representative conversations and remove unnecessary sensitive data from examples. Separate a problem in the Skill from a problem in the agent's audience, data access, or external system.

## Review and apply an improvement

1. Open the Skill Builder and review recent feedback, corrections, and failed or incomplete outcomes.
2. If improvement suggestions are available, inspect each proposed diff and identify the behaviour it is meant to change.
3. Accept a suggestion only when its rule is correct for the intended audience; decline suggestions that broaden access or add an unrelated process.
4. If you edit manually, change one instruction, tool, or knowledge reference at a time.
5. Run the same representative request before and after the change. Check both the result and any external write or file update.
6. Save the smallest useful revision and record what changed in the Skill description or change note.

Self-improvement can analyse conversations on a recurring cycle and propose diffs for editors. An editor must approve a proposal before it changes the Skill. Review workspace and Skill settings before enabling it, especially when conversation content includes confidential information.

## What you should see afterward

The Skill has a new, reviewable version and the same procedure is available to every agent that uses it. The improvement can be traced to a concrete example and can be reverted through history.

## Common questions

### Should every correction become a new rule?

No. Add a rule when the correction represents a repeatable requirement. Keep one-off preferences in the conversation.

### Why did a suggestion not appear?

Suggestions depend on the feature being enabled, enough usable conversations, and the workspace's processing cycle. Continue manual review when a decision is urgent.

### Can self-improvement train a public model?

It proposes changes to your workspace Skill. It is not a replacement for your own review of data processing, retention, and access settings.

[Documentation index](../../../indexes/en.md) · [简体中文](../../../indexes/zh-cn.md#技能管理)
