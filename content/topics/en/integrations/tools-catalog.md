# Provider tools catalog

## Before adding a provider tool

A workspace administrator confirms that the provider, account type, and intended operation are available. Select the smallest Space and Agent capability. Create the provider credential in the provider’s own admin console, use only the scopes below that match the task, enter it in the current **Spaces → Tools → Add Tools** form, and begin with one known object. A provider import or Connection is separate from a live Tool.

## Ashby

In **Ashby Admin → API Keys**, create a key for the intended recruiting workspace. Grant Candidates read/write only when notes or referrals are required; grant Jobs, Reports, Organization, and Hiring Process read for job, report, user, and referral-form lookups. Add confidential-job or private-field access only when explicitly needed. In **Spaces → Tools → Add Tools → Ashby**, paste the API key and add it to the Agent. The first check is a candidate search or job list. A key can authenticate while omitting the object permission needed by the request.

## Freshservice

Use a Freshservice account with the **Agent** role, not Requester. In Freshservice, assign access to Tickets, Service Catalog, Knowledge Base, and Approvals. In the tool form enter the Freshservice domain URL and organisation URL, start OAuth, accept the requested scopes, and add the tool to the Agent. Read one ticket by ID and one field definition before any reply or update. A ticket that is visible but missing fields usually means role or field visibility is too narrow; rate limits also apply.

## Front

In **Front → Settings → Integrations → API**, create a Personal Access Token. For reads grant `conversations:read`, `messages:read`, `contacts:read`, `tags:read`, and `teammates:read`; add `messages:send`, `comments:write`, `drafts:write`, `conversations:write`, or `tags:write` only for those actions. In the Front tool form paste the token and add the tool to an Agent with the intended inbox/team scope. Start with `list inboxes`, one conversation ID, and its messages. Missing conversations often means the token’s team membership or inbox scope is incomplete. A Front import remains a separate source-ingestion path.

## GitHub

**Connection:** A workspace administrator installs or approves the GitHub app, selects repositories in the provider OAuth flow, and assigns the synchronized repository scope to a Space. Check one known repository file or issue after refresh.

**Tool:** Decide whether actions use workspace credentials or personal credentials: workspace actions use the configured app identity; personal actions are limited by both the app and the invoking user. GitHub has no per-Agent secret field in the source setup. Add GitHub under **Agent Builder → Add Tool**, name the allowed repositories in the Agent instructions, and start with one repository, issue, or pull request read. A repository missing from results means app installation or user membership is insufficient.

## HubSpot

In HubSpot developer or app settings, create or select the approved app and grant only the CRM object scopes required by the Agent: contacts, companies, deals, tickets, or the relevant custom object. In **Spaces → Tools → Add Tools → HubSpot**, complete OAuth and select the workspace account, then add the tool to the Agent. Use `Get Object Properties` first, then read one known object by ID; the properties response identifies writable fields. Authentication with no object results indicates a missing app scope or private-app policy.

## Intercom

**Connection:** An administrator chooses the Intercom teams or Help Centre collections, authorizes access, assigns the source to a Space, and checks one conversation and article after refresh.

**Tool:** Create or select the provider app with the required conversation, contact, and Help Centre scopes, complete OAuth in **Spaces → Tools**, and add it to the Agent. Start with one conversation and one article collection. A collection share does not expose every conversation; verify team, collection, field, and refresh boundaries separately.

## Jira

In Jira, choose the site and project, then create or select the approved OAuth/PAT credential owner. Grant Browse Projects and issue read for search; add Create/Edit Issues and Transition Issues only for write tasks. In the Jira tool form select the site and credential type, then add the tool to the Agent. Read one project, issue, and workflow transition before editing. A transition can fail even when issue read works because the workflow condition or project permission is separate.

## Monday

In Monday, create or select the account credential in the approved workspace and choose the boards, groups, items, columns, subitems, comments, and users the Agent needs. In the tool form complete OAuth or paste the provider credential required by the current form, select personal or shared ownership, and add Monday to the Agent. Read one board and item, including column IDs, before an update. Board membership, private boards, and column visibility commonly explain partial results.

## Productboard

A Productboard administrator enables the approved integration and authorizes feedback, users, companies, and features as needed. In **Spaces → Tools → Add Tools → Productboard**, complete the authentication fields shown by the current form and add the tool to the Agent. Start by reading one feature and its ID, then create or link one feedback item only when the target user/company/feature is visible. A valid login with no target feature usually means workspace or object permission is missing.

## Salesforce

In Salesforce Setup, create an **External Client App** or the approved connected application. Enable the OAuth flow required by the current tool, set the current callback value supplied by the setup form, and grant the minimum object and field permissions through a permission set. Record the consumer key/secret and complete the Salesforce authorization in **Spaces → Tools**. Start with one Account or Contact read and inspect the API name and record ID. Package edition, API limits, field-level security, and the user’s permission set can each block a field after login succeeds.

## Salesloft

In Salesloft administration, create an API key for the intended owner and grant cadence, task, people, and activity scopes only as required. In the Salesloft tool form paste the API key, select the account ownership mode, and add the tool to the Agent. Read one cadence and one task before creating or updating activity. A key can authenticate while lacking cadence or task scope.

## Slab

A Slab workspace administrator authorizes the integration and grants read access to the topics and articles the Space may search. In the Slab tool form complete the provider authorization, add Slab to the Agent, and start with one topic search and article read. Private topics not shared with the integration remain absent; broad workspace membership is not proof of article access.

## Statuspage

In the Statuspage provider administration, create or select a credential with page and component read; add incident create/update only when an approved operator needs those actions. Enter the page/account field and credential in the current Statuspage tool form, then add it to a restricted Agent. Read one page and component before any incident change, and read the same incident back by ID after a write. Page ownership and role level are common blockers.

## UKG Ready

In UKG Ready administration, create an OAuth application for the tenant and grant the read-only workforce scopes approved by the administrator. Record the tenant/application values and complete OAuth in **Spaces → Tools → Add Tools → UKG Ready**. Add the tool to an Agent and read one permitted employee or workforce record. Tenant configuration, role grants, and personal-data restrictions can prevent an otherwise valid authorization.

## Vanta

In Vanta administration, create an application and select the security-test, control, and failed-resource scopes required for the task. Complete the current OAuth fields in **Spaces → Tools → Add Tools → Vanta**, choose the account owner, and add it to a restricted Agent. Read one test and its status before asking for remediation data. Organisation ownership or test ownership can limit results.

## Zendesk

**Connection:** Select brands, categories, ticket status, retention, redaction, tag filters, and refresh settings in the Zendesk connection form, then check one ticket and article after refresh.

**Tool:** Create or select the provider credential with ticket, user, and Help Centre scopes, complete OAuth or token entry, and add the live tool to the Agent. Read one ticket and one article in the selected brand/category before a reply or update. Rate limits, hidden customer fields, and brand scope commonly cause partial results. A Zendesk channel app is separate from both paths.

## Val Town

In Val Town, authorize the intended account and choose the permitted vals and files. In the Val Town tool form complete the current OAuth fields, add the tool to an Agent, and start with `list vals`, `get val`, or `list val files`. Review code and endpoint effects before `run`, file writes, deletion, or HTTP calls. A val may be visible while its files or endpoint permissions are not.

## Power BI and NetSuite

Use the dedicated [Power BI](./power-bi.md#power-bi-tool) and [NetSuite](./netsuite.md#netsuite-tool) pages. Power BI needs an Entra app, delegated permissions, tenant MCP setting, and a bounded model read. NetSuite needs SuiteCloud features, the MCP SuiteApp, a dedicated role, and an OAuth integration record; do not use an Administrator role.

## Airtable

Choose one authentication model in Airtable. For a shared setup, create a Personal Access Token in `airtable.com/create/tokens`, grant only `data.records:read` (add write and comment scopes only when needed), `schema.bases:read`, and the selected bases. For per-user access, register an OAuth integration and use the current callback values in its setup form. In the Airtable tool form use server `https://mcp.airtable.com/mcp`, select the authentication type, enter the token or OAuth client fields, and add the tool to the Agent. Start with one base schema read and one record lookup; a base that authenticates but has no table access indicates token base selection or scope is incomplete.

## Asana

In Asana, create or select the approved app, complete OAuth, and have an Asana administrator use **My Apps → Manage distribution** to select the workspace. In the tool form choose Personal or Workspace credentials and complete the OAuth fields shown by the current setup. Add Asana to an Agent and read one project and task before creating or updating a task. “Connected but no data” usually means the app was not distributed to the target workspace or the user is not a project member.

## Attio

Add Attio as a remote MCP server using `https://mcp.attio.com/mcp` and Automatic OAuth, then choose the target Space and credential owner. Add the tool to an Agent and run `whoami`, `search-records`, or `list-attribute-definitions` for one object. Keep record create/update, tasks, notes, and emails behind the workspace’s write confirmation policy. If the tools do not appear, rerun the add-server flow and check Space sharing.

## Canva

A Canva administrator enables the AI Connector under **Controls and permissions**, then chooses the approved account in the OAuth flow. Add the Canva remote tool from the current tool picker and share it only with intended Spaces. Start with `Search designs` or `Get a design` by ID; generation, resize, autofill, and export are write or artifact actions that need a review owner. Feature availability depends on the Canva plan and template permissions.

## Fathom

Open **Spaces → Tools → Add Tools → Fathom**, complete OAuth, choose Personal or Shared credentials, and share the tool with the intended Space. The read-only minimum is `list_meetings` with a date range or team filter, followed by `get_transcript` for one `recording_id`. Meeting, transcript, summary, and CRM visibility can differ; check the recording identity before sharing a transcript.

## Miro

For Miro MCP, an administrator opens **Spaces → Tools → Add Tools → Miro MCP** and completes OAuth 2.1. An Enterprise organisation must enable the Miro MCP server first. Add it to an Agent and read one board or board item before creating a diagram or editing content. Board sharing and team membership determine the visible scope; provider-operated MCP support follows the provider’s current controls.

## Semrush

Open **Spaces → Tools → Add Tools → Semrush MCP** and use the provider API key or OAuth option available for the account plan. Semrush One, SEO, or Trends API access and available API units are prerequisites. Add the tool to the Agent and run one keyword or domain report with a bounded date range. Check the returned report, units, and account identity before using competitive or backlink data.

## Computer

A workspace administrator opens the **Computer** admin page and configures **Network → Allowed domains** with exact domains or approved wildcard subdomains. Configure non-secret values under **Environment variables → Config** using the `DST_` name prefix. Put API keys and tokens under **HTTPS secret**, using the `DSEC_` prefix and at least one allowed domain; the raw secret is not shown to the Agent. Enable Agent-requested domains only when users may approve a temporary one-conversation domain. A minimum check is a read from one allowed URL; invalid or duplicate domains should be rejected before a task runs.

## Browser extension

Install the approved browser extension from the browser’s official extension store, sign in to the intended workspace, and enable browser-tab access only after the user grants permission. The first check is attaching the current tab’s text or screenshot to a conversation; the extension should not read a page without an explicit request or permission.

## Files, execution, and automation

For Computer, File Generation, Image Generation, and Voice/sound generation, define the input files, output format, destination, and review owner before adding the capability. The minimum result is an artifact that opens and matches the requested format; inspect formulas, links, dimensions, and content before sharing.

For Web Search & Browse, specify allowed sites, date range, and evidence needs; a result is a source-backed answer, not a private connected source. For JIT tools, browser extensions, meeting transcripts, create the provider-side installation, identity, callback/webhook, and event scope first, then run one traceable event. Check the provider run log and guard against duplicate events.

## Custom imports

Dropbox, Front, Guru, HubSpot, Jira, Linear, Salesforce, and Zapier imports are source-ingestion paths. Select the provider collection, import owner, refresh behavior, and destination Space; verify one imported object and its source ID. An imported record does not automatically enable the provider’s live Tool.

For Agent Memory, delegation, and scheduled prompts, use [advanced work modes](../agents/advanced-work-modes.md#choose-an-advanced-agent-work-mode).

## Common issues

- The tool is listed but unusable: check Space, Agent capability, provider credential, and object scope in that order.
- Read works but write does not: check the exact object permission and read the provider record back.
- A provider requests a callback or webhook: copy the current value from the setup form and verify it in the provider console.
- A source is stale: determine whether the task uses a Connection or Tool, then check refresh and provider activity logs.

See [connections and tools](./connections-and-tools.md#connections-and-tools), [personal and shared access](./personal-and-shared.md#personal-and-shared-credentials), and [remote MCP](./remote-mcp.md#add-a-remote-mcp-server).
