# Connections and tools

## Choose the access path

Counso uses two different ways to make outside information available to an Agent:

- A **Connection** brings a selected provider source into a Space for search and retrieval. The connection controls what source material is available and when it is refreshed.
- A **Tool** lets an Agent call provider operations, such as reading one file, querying a record, or preparing an update. A tool acts with the credentials and permissions assigned to it.

Adding a Connection does not add the provider’s Tool, and adding a Tool does not make the whole provider source searchable. For Google Drive, for example, the Connection is for synchronization and retrieval while the native Google Drive Tool is for precise file and Sheets operations. Start from [Personal and shared access](./personal-and-shared.md#personal-and-shared-credentials) when the credential owner matters.

## Prepare a connection

1. Confirm that a workspace administrator can manage the target Space and the provider account.
2. Decide whether the source belongs in an Open Space or a Restricted Space. Give the source only the smallest page, folder, channel, database, or project scope needed for the task.
3. Open the connection controls from **Spaces** and select the provider when it is available in the workspace.
4. Complete the provider’s own consent or administrator setup. Keep the selected source, account, and permission boundary recorded with the connection.
5. Wait for the first refresh, then ask an Agent to find a known, non-sensitive item. Compare the result with the provider and check the item’s access boundary.

A successful connection setup screen only means that the configuration was accepted. It does not prove that every item is indexed, that a user can see the same data, or that an Agent can write back to the provider.

## Websites and folders

A website source is a connection to public material that an Agent may retrieve; it is not a live browser session. In **Spaces → Connections → Add connection → Website**, enter a public starting URL, choose the target Space, and choose one crawl scope: **Follow all links within the domain**, **Only child pages of the provided URL**, or a single page with **Page limit = 1**. Use **Depth of search** to bound link traversal and set a page limit no higher than the current form allows. The crawler follows links found in the starting page; it does not guess unlinked pages. PDFs below the crawled URL can be included, while a Google Docs URL is included only when entered directly or reachable on the same domain. Login-protected pages are not public sources, and provider-blocked sites may fail. After the first refresh, check one known page and its URL in the target Space.

Use folders to keep related sources under a clear access boundary. A folder move or membership change can change what an Agent can find without changing the provider itself, so check the folder, Space, and source permissions together.

Custom imports from Dropbox, Front, Guru, HubSpot, Jira, Linear, Salesforce, or an automation service are source-ingestion routes. Set the source collection, import owner, refresh behavior, and destination Space; an imported source does not automatically grant live write operations.

### Configure website crawling

1. Add a website source in **Spaces → Connections** and enter a starting URL that can be read without signing in.
2. Choose **Follow all links within the domain** for linked pages across a site. For one section, start from its section URL and choose **Only child pages of the provided URL**.
3. Use **Page Limit** to bound the number of pages; set it to 1 to index only the starting page. Use **Depth of Search** to limit how many links the crawler follows. Use the maximum offered by the current form.
4. Save and wait for crawling, then check one expected page and one page that should be excluded.
5. After the website changes, check the connection’s refresh state before asking the Agent to use the new material.

The crawler follows links that actually appear in pages; it does not guess unlinked addresses. PDFs within the allowed crawl path can be included. Links to another domain, such as a Google Docs link from a website, are generally not followed. A site requiring login, refusing crawling, or blocking public access cannot be synchronized as an ordinary website source.

## Prepare a tool

1. Choose the Space where the tool should be available.
2. Select the tool in the Agent’s capabilities or tools configuration.
3. Choose Personal or Shared credentials according to who should be accountable for the provider action.
4. Start with a read-only request against a known record. For a write-capable tool, require a clear confirmation before the action.
5. Check the provider’s receipt and read the same object back by its stable identifier. Treat the provider record as the source of truth.

## Understand refresh and access

A connection can have a different refresh time from the provider’s live tool. A recently changed provider item may therefore be available to a tool before it appears in a synchronized source. Removing a user from a Space, changing a provider share, or changing the credential owner also needs a small access check after the next refresh.

Keep these three questions separate:

- **Can the connection find the item?** Check the source scope and refresh.
- **Can the tool act on the item?** Check the tool credential and provider permission.
- **Did the provider accept the action?** Check the provider receipt and the same object after the action.

## Common connection problems

- **The provider is missing from the list:** confirm the workspace role and whether the provider is enabled for this environment.
- **The first refresh is empty:** check the selected Space, source scope, provider share, and refresh state before widening access.
- **A tool sees less than a connection:** compare credential ownership and provider permissions; the two paths can have different scopes.
- **A write appears to succeed but cannot be found:** use the provider’s stable ID to read it back. Do not rely on the assistant message alone.

For provider-specific procedures, see [Google](./google.md#google-connections-and-tools), [Microsoft](./microsoft.md#microsoft-connections-and-tools), [Slack](./slack.md#slack-connections-and-tools), [Notion](./notion.md#notion-connection-and-tools), [Confluence](./confluence.md#confluence-connection-and-tools), [Gong](./gong.md#gong-connection-and-tools), and [data platforms](./data-platforms.md#data-platform-connections-and-tools).
