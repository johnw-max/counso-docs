# Choose a model for a conversation or Agent

## Before you begin

You need Work access and an Agent or conversation. The current picker exposes Basic (GPT 5.6 Luna, Light) and Standard (GPT 5.6 Luna, High); Premium is visible but disabled, and More models is available. Treat the current picker as authoritative because availability can change.

## Steps

1. Open Work and start a conversation or open an editable Agent.
2. Confirm the Agent, open the composer model picker, and choose a shown option.
3. For a reusable default, use the model selector in Agent > Instructions and save after a small test.
4. Compare a representative request; if an option disappears, use one shown or ask an administrator to review access.

### A practical choice

For a monthly policy comparison, start with Standard and ask for a two-column evidence table. If the answer misses exceptions, repeat the same prompt with a stronger option exposed by **More models**. For short classification or routing, test Basic first. Compare the same input, not different prompts, and record latency, citation quality, and whether required tools were used.

Reusable prompt:

```text
Compare the two policy excerpts below. Return: (1) changed rule, (2) affected role,
(3) effective date, and (4) source quote. If a field is absent, say "not found".

```

## Result

You selected a model for the next message or saved one for the Agent.

## Common questions

**Does changing a model update the Agent?** A change in the composer applies to that conversation. Editing and saving the model in the Agent builder updates its default configuration.

**Why do people see different options?** Policy, access, region, or provider status may differ; the current picker is authoritative.

**Where should I start?** Use the general-purpose option shown, then test a stronger one for demanding work.
