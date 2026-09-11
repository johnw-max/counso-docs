# Review usage and seat access

# Review usage and seat access

Seats determine which workspace features a member can use. Credits and spending limits determine how much resource a run can consume. Check them separately. Prices, included credits, billing periods, and cancellation terms come from the workspace’s current subscription page and agreement.

## Check members and seats

1. As an administrator, open the member or seat area in **Admin**.
2. Find the affected member and inspect their role, seat type, invitation status, and active access.
3. If the interface allows seat assignment or removal, confirm the required features and billing effect before saving a change.
4. Ask the member to reopen the workspace and try one ordinary request.

Opening the Agent list alone does not establish that a seat is working. Sending messages and using particular features can have additional limits.

## Check credits and run consumption

Open the workspace’s Usage, Credits, or consumption area. Confirm the reporting period, used credits, remaining balance, or spending cap. When filters for members, Agents, models, or run types are available, compare the same period to identify the largest sources of consumption.

For schedules and Webhooks, check whether the trigger uses personal or workspace credits. A person being able to send an interactive message does not establish that the trigger’s selected pool has credit available. For API and other programmatic runs, check the workspace, executing identity, and associated consumption record.

Reduce unnecessary consumption by disabling duplicate automations, lowering unhelpful run frequency, and narrowing the source set. Then compare available models on the same request for quality and consumption. Keep the evidence needed to perform the task correctly.

## Change a subscription or stop renewal

Only a person with billing permissions should change a subscription. Open the current billing or subscription page and check the effective date, outstanding charges, seat changes, and effect on data access before completing its confirmation. Reopen the subscription status afterward and confirm that the requested change and effective date appear.

Stopping renewal, removing a member, and deleting a workspace are separate actions. Use the workspace’s actual terms for when access ends, how usage is billed, and how long material is retained. If the page does not establish those details, contact the billing owner before proceeding.

## Separate a member issue from a workspace issue

Suppose Alice can open an Agent but cannot send a message, while Bob can complete the same request. Compare their access status, credit attribution, and source permissions first. If all members are blocked, inspect workspace consumption, spending limits, and service status.

Record when the error occurred, the reporting period, and who is affected. This helps an administrator decide whether to change member access, run settings, or workspace credits.

See [Schedules](/en/automations/schedules/#schedule-an-agent), [Trigger filters and limits](/en/automations/filters-and-limits/#filter-automation-events-and-manage-limits), and [Support](/en/administration/support/#get-help-from-counso).
