# Google connections and tools

# Google connections and tools

## Google Drive connection

Use a Google Drive **Connection** when an Agent should search indexed files in a Space. A connection uses an administrator-selected Google account and selected Drives, folders, or files; it does not provide a live edit operation. A Workspace administrator should:

1. Choose a dedicated Google Workspace account and identify the Shared Drive, folders, and files that the target Space may expose.
2. Open **Spaces → Connections → Add connection → Google Drive** and complete Google OAuth for that account.
3. Select the allowed Drive or folder scope, then assign the connection to the intended Space.
4. Refresh once, search for a known file, and compare its title, parent, labels, and visibility with Google Drive.

Convert native Excel files to Google Sheets before syncing them through the Google Drive Connection for table queries. Files with more than 2 MB of extracted text are excluded from indexing, and scanned-image PDFs are not automatically OCR-indexed. Refresh timing and labels also affect what is searchable. If the file is absent, check that the selected account can open it and that its parent folder is in scope.

## Google Drive and Sheets tool

The native Google Drive Tool is a live, user-authorized tool for precise file operations. It is separate from the Drive Connection and from the deprecated Google Sheets tool.

1. An administrator opens **Spaces → Tools → Add Tools → Google Drive** and enters the Client ID and Client Secret required by the current setup form.
2. Complete the administrator OAuth step so the tool is available in the Space.
3. Add Google Drive to an Agent. On first use, each acting user connects their own Google account.
4. Start with a stable file ID or exact title. For Sheets, name the spreadsheet, worksheet, and range.
5. For a write, first read the document structure or worksheet, perform the bounded change, then reopen the same file and range in Google Drive.

The tool can list Shared Drives, search files, read Docs/Sheets/Slides, inspect spreadsheet ranges, create or copy files, add comments, and update documents, spreadsheets, or presentations. It does not provide semantic search across all Drive files; use the Connection for indexed retrieval. A file over the documented size limit or a content response over the per-call character limit must be paginated or handled separately.

## Gmail and Calendar tools

Gmail and Google Calendar are personal-account tools. The person whose account will act should authorize the requested mail or calendar scopes when adding the tool. Start with one message, draft, or event in a non-sensitive test range. For a send, update, or event creation, check the same mailbox or calendar afterward. A user who can read but cannot write needs the account’s write scope and provider-side permission checked.

## BigQuery

BigQuery is a data-platform connection, not a Drive file source. Create a dedicated Google Cloud service account in **IAM & Admin → Service Accounts**, grant the minimum `roles/bigquery.user` and `roles/bigquery.dataViewer` needed for the selected project and datasets, and protect the JSON key. In **Spaces → Connections → Add connection → BigQuery**, enter the key, select one dataset location, and select the datasets or tables. A query cannot combine datasets in different locations. Check one known table and bounded read-only query before relying on the result. See [data platforms](/en/integrations/data-platforms/#data-platform-connections-and-tools).

## Common issues

- A synchronized file is stale: check selected Drive scope and refresh state.
- A Tool finds a file but cannot update it: check the acting user’s Drive or Sheets permission and the exact file ID.
- A Sheets range is wrong: read the worksheet first; do not infer row or column indexes from the title.
- BigQuery is empty: check project, dataset location, role, and the selected table.

See [connections and tools](/en/integrations/connections-and-tools/#connections-and-tools) and [personal and shared access](/en/integrations/personal-and-shared/#personal-and-shared-credentials).
