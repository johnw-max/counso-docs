# Work with documents, images, and tables

# Work with documents, images, and tables

Use conversation attachments for a one-off analysis, Pod Files for ongoing work around a shared topic, and a configured data connection for material that should follow changes in an external source. Choose the location based on who needs access and whether future updates should synchronize.

## Prepare the material

Keep the original files and use recognizable names. When several versions exist, specify the version and date in your request. Tables should have clear column names, units, and a defined meaning for each row. Scanned pages should be legible; avoid combining rotated pages into a single very long image.

The model and available tools determine how an Agent can read the material. A completed upload confirms that the file was submitted; check that the answer used the intended page or worksheet. If the upload interface reports a size or format limit, split or convert a copy while keeping the original.

## Use files in a conversation

1. Open a conversation and choose an Agent for the task.
2. Add files through the attachment control and wait for the upload to finish. For an existing Pod file, identify it by name in the request.
3. State the task, source range, and desired output. For example: “Compare the reimbursement conditions in these two policies. List changed clauses with the file and section. Omit unchanged material.”
4. For a long document, start with a section, period, or question before expanding the scope. For an image, identify the area, text, or visual feature to inspect.
5. Compare important findings with the original before saving, downloading, or sharing the result.

## Extract fields and tables

Define the fields before specifying the output format. For a set of sample invoices, you might request supplier, invoice number, date, currency, total including tax, source file, and page. Ask the Agent to leave missing values empty and retain original currencies and dates instead of filling gaps from similar documents.

For a spreadsheet, identify the worksheet, data range, filters, units, and aggregation rules. When comparing totals, request the included row count and reasons for exclusions. A task that needs the complete table should use an appropriate file analysis capability or table tool; a few knowledge search excerpts are not a substitute for the full dataset.

## Keep the result

Check whether the response contains text, a downloadable file, or a file saved to a Pod. When requesting a save, specify the location and filename. Writing to Google Drive or Microsoft file storage requires the corresponding operation tool and authorization; a synchronization connection alone does not provide write access.

For ongoing collaboration, keep the result in a Pod with the appropriate membership and refer to the same file in later requests. See [Pod files](/en/pods/files/#work-with-pod-files) and [Connections and operation tools](/en/integrations/connections-and-tools/#connections-and-tools).

## Common questions

**A scanned page was not read.** Provide a clearer page or a searchable text copy, retaining the image for comparison. Text document support does not establish that the selected model can inspect images.

**Another conversation cannot find the attachment.** Conversation attachments do not automatically become workspace knowledge. Save reusable material to an appropriate Pod or knowledge source and check its access scope.

**The generated file differs from the original table.** Compare columns, formulas, filters, dates, and units. Ask for an explanation of the discrepancy before regenerating the file. A download link does not establish that its contents are correct.
