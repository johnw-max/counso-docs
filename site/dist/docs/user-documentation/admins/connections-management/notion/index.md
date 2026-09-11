# Notion connection and tools

# Notion connection and tools

## Notion connection

A Notion administrator who is also a workspace administrator should choose the top pages, databases, and blocks for the target Space. Open **Spaces → Connections → Add connection → Notion**, select the top pages in the permission dialog, and use individual page selection for sensitive material. Selecting a page makes its page tree available for synchronization and retrieval through the Connection. Configure the Notion Tool separately to create, update, or comment on content. Review the authorization scope and synchronization boundary before saving.

After the first refresh, search for a known page and compare its parent, database visibility, and last update in Notion. Share the database itself when a linked view is not enough. If a page moves to **Orphaned resources**, restore the correct parent share and refresh.

## Notion tool

After the connection is available, add **Notion** under **Agent Builder → Add tool**. Decide whether the Agent may read, create, update, comment on, or archive content. The tool can retrieve and create pages, query or update database rows and schema, retrieve or delete blocks, search pages/databases, and create or fetch comments and users.

For a minimum read test, use a known page ID or a narrow search and confirm the parent and page ID. For a write:

1. Name the target page, database, block, or discussion ID.
2. Read the object and its parent first.
3. State the properties or blocks to change and apply one bounded change.
4. Reopen the same stable ID in Notion and check content, parent, and permissions.

## Common issues

- A shared top page does not expose a child: share the correct parent or child and refresh.
- A database is visible but rows are missing: share the database, not only a linked view.
- Reading works but editing fails: check page-level write permission and the credential owner.
- A database has multiple data sources: use a supported single data-source database or split the content before connecting.

See [personal and shared access](/en/integrations/personal-and-shared/#personal-and-shared-credentials) and [connections and tools](/en/integrations/connections-and-tools/#connections-and-tools).
