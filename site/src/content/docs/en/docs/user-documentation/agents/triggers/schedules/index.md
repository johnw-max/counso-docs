---
title: "Schedule an Agent"
topicId: "automations/schedules"
contentRevision: "9"
sidebar:
  hidden: true
---

# Schedule an Agent

Use a schedule when an agent should perform the same kind of work at a predictable time: a daily brief, a weekly report, or a periodic Pod refresh.

## Before you begin

Choose the agent, target Pod or destination, message, timezone, and frequency. Define what happens when the source is unavailable or the work needs human review. Check the expected number of runs and the credit pool before enabling a high-frequency schedule.

## Create a schedule

1. Open the agent in the builder and open **Triggers**.
2. Choose **Add trigger** and select a schedule.
3. Give the schedule a name and describe the frequency in plain language.
4. Add the optional message the agent should receive at each run.
5. Choose the timezone and inspect the human-readable confirmation of the effective schedule.
6. Save the agent. The schedule is registered only after the agent is saved.
7. Run a low-risk first cycle and read the resulting conversation, task, or file before increasing the frequency.

Schedules are attached to the agent. Keep the prompt explicit about the destination and about whether the agent may create, update, or only draft content.

## What you should see afterward

The trigger shows its name, effective frequency, timezone, and status. A run creates the result in the destination allowed to the agent. Keep a human review step for external writes, customer communication, or financial actions.

## Common questions

### Why did it run at the wrong local time?

Reopen the trigger and check the selected timezone and the interpreted schedule. Daylight-saving changes can alter a local clock time.

### Why was no conversation created?

Check that the agent is saved and enabled, the destination is explicit and accessible, and the trigger's credit pool has capacity.

### Can every Pod member see the schedule?

Visibility and run history depend on the workspace's automation permissions. Document the owner and destination, and have an administrator verify the audience before using a shared schedule.
