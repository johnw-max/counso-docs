---
title: "Review a data set with an Agent"
topicId: "guides/data-review"
contentRevision: "12"
---

# Review a data set with an Agent

## Before you begin

Know the source of truth, review period, and key fields. Decide which actions may be prepared and which require human confirmation.

## Steps

1. Select Agent and source scope; state period, entity, filters, and output.
2. Ask for used records and missing, duplicate, or conflicting values.
3. Review a small sample and correct filters before the full review.
4. Request exceptions with record ID, issue, evidence, next step, and confidence.
5. For an external update prepare a proposed change, confirm destination, inspect receipt, and read the same ID back.

## Result

### Worked example: reconcile a small data set

Input: an anonymised CSV of 40 supplier rows with invoice_id, supplier_id, invoice_date, amount, and status, plus a policy file defining the review period. Ask the Agent to find duplicate invoice IDs, dates outside the period, and status conflicts; inspect five rows manually before requesting the full table. Expected output: an exceptions table and a count by exception type.

Reusable prompt:

```text
Review the CSV for 2026-08 using the policy file as the rule source.
Return exception_type | invoice_id | supplier_id | evidence row | proposed next step.
Do not edit the CSV or post a correction. If policy and row disagree, show both values.

```

The output separates records needing correction, records needing more information, and next steps for the responsible person.

## Common questions

**Can it review every record at once?** Start small; large inputs can hide exceptions.

**What counts as write success?** Require destination receipt and exact same-record read-back.

**Can it run unattended?** Only after the workspace, Agent, connector, and owner approve and test it.
