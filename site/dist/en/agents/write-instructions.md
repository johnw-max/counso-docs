# Write Agent instructions

# Write Agent instructions

Instructions tell an Agent how to approach its work. Good instructions are specific enough to guide a repeatable task and flexible enough to handle the information provided in each conversation.

## A practical structure

Write instructions in this order:

1. **Role and purpose:** say who the Agent helps and what outcome it owns.
2. **Inputs:** name the sources it may use and what it should do when a source is missing.
3. **Process:** describe the checks or decisions it should make in order.
4. **Output:** specify the format, level of detail, and items that need human review.
5. **Boundaries:** state what it must not infer, disclose, or change without confirmation.

Use plain language and short sections. Give one representative example only when it clarifies the expected result. Keep credentials and secrets out of instructions and conversations; use the designated connection method for authorised services.

## Review the configuration

In the Agent editor, use the **Instructions** area and the available formatting controls to make the text readable. Choose a model option provided by your workspace. Before saving, ask whether the Agent can complete the task with the data and tools you selected. If not, narrow the task or adjust the access plan rather than adding broad access by default.

Try a small, non-sensitive request and compare the result with the source. If the result is incomplete, improve one instruction at a time: clarify the input, add a missing check, or make the output format explicit. If the task could affect an external system, require confirmation and destination-system verification in the instructions.

For the surrounding configuration, read [Add capabilities and knowledge](/en/agents/capabilities-and-knowledge/#add-capabilities-and-knowledge) and [Preview and improve an Agent](/en/agents/preview-and-improve/#preview-and-improve-an-agent).
