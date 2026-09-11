# Choose search, extraction, or table queries

Finding a policy, reviewing recent updates, extracting fields from records, and calculating table totals call for different methods. When configuring an Agent's knowledge capabilities, define the result first, then select the corresponding tools and sources available in your workspace.

## Match the method to the question

| Task | Suitable method | What to specify |
| --- | --- | --- |
| Find a relevant explanation among many documents | Knowledge search | Topic, period, source scope, and citations |
| Read known documents or recent updates | Include selected material or read files | File list, time range, and priorities |
| Collect consistent fields from unstructured records | Data extraction | Field definitions, missing-value rules, and source identifiers |
| Calculate counts, totals, groups, or ratios | Table queries or file analysis | Tables, fields, filters, joins, and units |

Search selects relevant material for an answer; it does not establish that every source was read. Including recent material is also different from ranking it by relevance to the question. Large collections remain subject to the amount of content that can be processed.

## Configure a bounded knowledge task

1. Open an Agent you can edit and select an appropriate knowledge capability under **Capabilities and knowledge**.
2. Choose the required sources. Where specific folders, pages, channels, or tables can be selected, begin with material directly relevant to the task.
3. State the period and output requirements. If the selected capability provides label or time filters, check that the inclusion and exclusion rules match the source's actual labels.
4. For extraction, define each field's meaning and type. For calculations, explain the meaning of a row, date conventions, currency units, and duplicate handling.
5. Preview a small sample with a known answer. Compare sources, extracted fields, or calculations before expanding the scope.

## Extract fields from text

For example, organize a week's support records into request ID, issue category, resolution status, next owner, and source link. Define the categories and leave an absent resolution status empty instead of inferring it from tone. Where the tool accepts a structure definition, JSON Schema can describe fields and allowed values; generated schemas also need review.

Keep results traceable to their source records. If a request has several updates, state whether to retain each update or merge by request ID, and which point in time determines its status. Valid structure alone does not establish completeness or accuracy.

## Query tables

Specify the calculation precisely: “Group completed orders by month, sum their net amount, exclude canceled orders, preserve the original currency, and return the order count.” For joins, identify the matching fields and whether the relationship is one-to-one or one-to-many so duplicated rows do not inflate totals.

Check row counts, filters, missing values, date boundaries, and units. If complete coverage matters, confirm the actual tables and period used instead of relying on the reported total alone. To change a source table, use the corresponding operation tool and separately identify the records and fields to update.

## Resolve unexpected results

For missing information, check [source selection](./choose-sources.md#choose-knowledge-sources) and [the difference between synchronization and operation tools](../integrations/connections-and-tools.md#connections-and-tools). For incorrect numbers, check whether text search was used for a quantitative task and whether the table contains duplicates, numbers stored as text, or mixed currencies. Split long periods into explicit batches and reconcile their coverage; do not present a smaller range as a complete result.

[Documentation index](../../../indexes/en.md) · [简体中文](../../../indexes/zh-cn.md#知识来源与回答核对)
