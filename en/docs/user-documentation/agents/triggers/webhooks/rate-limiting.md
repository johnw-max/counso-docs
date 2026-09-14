# Set limits for webhook triggers

A webhook trigger can limit how many accepted events start an Agent run during a rolling 24-hour period. This helps prevent a busy source from creating more runs than intended. The current limit and any editable override are shown in the trigger settings.

## Set a per-trigger limit

Open the webhook trigger in Agent Builder and review its **Rate limits** field. Keep the default while testing a new source; raise it only when the normal event volume requires it. Scheduled triggers use their schedule to control frequency and are not governed by a webhook event cap.

The trigger's rate limit is independent of its credit pool. Changing who pays for a run does not raise the allowed request rate. For credit-source details, see [Credits usage](../credits-usage.md).

## Workspace limits

The workspace may also enforce an aggregate limit or resource cap depending on its plan and configuration. Check the current Usage or trigger settings for the applicable ceiling rather than assuming that increasing one trigger's limit removes a workspace-level restriction.

## When a limit is reached

The trigger may mark a request as rate-limited and reject it. Requests can be dropped rather than queued, so they may not run later when the rolling window clears. Review the trigger's run details to confirm the behavior in your workspace. If it reaches the limit frequently, reduce unnecessary source events with a payload filter or adjust the per-trigger limit where permitted.
