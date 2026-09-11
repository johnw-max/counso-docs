---
title: "Filter automation events and manage limits"
topicId: "automations/filters-and-limits"
contentRevision: "9"
sidebar:
  hidden: true
---

# Filter automation events and manage limits

Filters decide which webhook payloads should start an Agent. Limits protect a workspace from a busy source and are separate from the credit pool that pays for a run.

## Before you begin

Obtain a sample payload from the source. Mark the exact field and value that identify a useful event. Decide whether a trigger serves one person or the whole workspace so that its credit pool matches its owner.

## Write a filter

1. Open the webhook trigger and review its filter field.
2. For a managed source, describe the event in plain language when the builder can generate a filter.
3. For a custom source, use the expression syntax with field paths such as `issue.state` and operators such as `and`, `or`, `not`, `eq`, `starts-with`, `has`, `has-all`, `has-any`, `gt`, and `gte`.
4. Test the expression with both an event that should pass and one that should be ignored.
5. Save the trigger and monitor the first accepted and rejected events.

For example, this expression accepts only open issues labelled `bug`:

```text
(and (eq "issue.state" "open") (has "issue.labels" "bug"))

```

## Understand limits and credits

Webhook triggers have a per-trigger run cap over a sliding 24-hour window. Requests received while the cap is reached are dropped rather than replayed. Scheduled triggers are governed by their schedule instead of that webhook cap.

The trigger's credit setting chooses **My credits** or **Workspace credits**. Use the workspace pool for team-wide work, and a member pool for a personal digest or report. A run stops when its selected pool or spend limit is exhausted; missed runs are not replayed automatically.

## What you should see afterward

The trigger accepts only matching payloads, and its details show whether it is rate-limited. Usage records identify the selected credit pool. Adjust the filter before raising a limit when noise is the cause.

## Common questions

### Why was a webhook event dropped?

It may have failed the filter, arrived after the rate limit was reached, or had no available credit. Check the trigger details and source payload.

### Does changing the credit pool change the filter?

No. The pool controls billing; the filter controls which events run.

### Why does a nested field not match?

Check the exact JSON path, data type, and array shape. Use a wildcard path for a field inside an array, and test both true and false examples before saving.

[Documentation index](/en/) · [简体中文](/zh-cn/#自动化运行)
