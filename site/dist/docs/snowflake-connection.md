# Data platform connections and tools

# Data platform connections and tools

## BigQuery connection

BigQuery connections keep metadata such as project, dataset, and table names; they do not synchronize or store all query rows. A Google Cloud administrator should:

1. Open **IAM & Admin → Service Accounts → Create service account** in the selected project.
2. Grant the account the minimum `roles/bigquery.user` and `roles/bigquery.dataViewer` roles for the query project and datasets.
3. Create a JSON key only if the current connection form requires it, and store the downloaded key securely.
4. In **Spaces → Connections → Add connection → BigQuery**, paste the key, choose one dataset location (`US`, `EU`, or a region), and select the datasets and tables.
5. Optionally enable the setting that uses BigQuery table and column descriptions.

Test one known table and a bounded read-only query. All datasets used by one connection must share the selected location; a query cannot join `US` and `EU` datasets. If metadata appears but rows do not, check the project, dataset-level `dataViewer` grant, and query job permission.

## Databricks SQL and Genie tools

On the Databricks side, copy the **workspace URL** from the workspace configuration, not the Account Console URL. In **Account Console → Settings → App Connections → Add connection**, create a named app connection, add the current OAuth redirect value supplied by the setup form, keep client-secret generation enabled, and add:

- `sql` plus `offline_access` for Databricks SQL;
- `genie` plus `offline_access` for Databricks Genie;
- both pairs when both tools are needed.

Copy the generated client ID and secret. Confirm that the authenticating users can access the Unity Catalog catalogs, schemas, tables, SQL warehouses, or Genie resources required by the task. In **Spaces → Tools → Add Tools**, select Databricks SQL or Databricks Genie, enter the workspace URL, client ID, and client secret, then complete OAuth. The tool derives its endpoint from the workspace URL. Test catalog/schema discovery or one Genie question before widening scope. IP access lists must allow the current outbound service addresses when the workspace uses them.

## Snowflake connection

For a synchronized table-query source, create a dedicated Snowflake role, service user, and warehouse. Grant the role `USAGE` on the intended database and schemas and `SELECT` on the intended tables. Password authentication may be used for a test; key-pair authentication is preferred for an enduring setup. In **Spaces → Connections → Add connection → Snowflake**, enter the account identifier, warehouse, role, user, and the selected password or key-pair fields. Select the tables and run `list databases`, `list schemas`, `list tables`, and `describe table` checks.

The Connection is admin-selected and supports larger bounded table results. It does not expose arbitrary SQL writes.

## Snowflake tool

For a live Snowflake Tool, an administrator creates an OAuth security integration and records the client ID and secret. Grant the integration only the roles that should be available. In **Spaces → Tools → Add Tools → Snowflake**, enter the account/host, client ID, client secret, and current OAuth fields, then choose personal or shared credentials. The effective Snowflake role determines access.

The tool supports schema browsing and read-only single-statement SQL. Begin with a known database, schema, table, or view and a bounded `SELECT`. Results are limited per execution; multi-statement SQL and `INSERT`, `UPDATE`, `DELETE`, `MERGE`, and `COPY` are not supported. Use the Tool for views and per-user role enforcement; use the Connection for a deliberately selected table set.

## Common issues

- Metadata is visible but rows are not: check the provider role and exact dataset/catalog/schema/table grant.
- A query cannot run: check warehouse or job quota, project/location, OAuth consent, and IP allowlists.
- Personal and shared results differ: compare effective provider account, role, warehouse, and Space.
- A query requests a write: stop; these paths are documented for read-only checks.

See [personal and shared access](/en/integrations/personal-and-shared/#personal-and-shared-credentials) and [connections and tools](/en/integrations/connections-and-tools/#connections-and-tools).
