# Filter webhook payloads

Filters decide whether an incoming webhook event should start an Agent run. For a supported integration, the builder may help generate a filter from a plain-language description. For a custom webhook, write an expression using the payload fields the sender actually provides.

## Expression format

The filter uses Lisp-style S-expressions: `(operator argument ...)`. Each expression evaluates to `true` (process the event) or `false` (ignore it). Strings use double quotes, numbers are unquoted, booleans are `true` or `false`, and lists use parentheses.

Refer to fields by dot-separated paths, such as `"action"`, `"issue.state"`, or `"pull_request.head.ref"`. For a field inside each object in an array, use `*`, for example `"tags.*.name"`. Paths must match the JSON payload.

## Operators

| Operator | Purpose | Example |
|---|---|---|
| `and` | All nested expressions must be true | `(and (eq "action" "opened") (eq "issue.state" "open"))` |
| `or` | At least one nested expression is true | `(or (eq "action" "opened") (eq "action" "edited"))` |
| `not` | Negates one expression | `(not (eq "issue.state" "closed"))` |
| `eq` | Exact equality for strings, numbers, or booleans | `(eq "issue.number" 42)` |
| `starts-with` | String begins with a prefix | `(starts-with "pull_request.head.ref" "feature/")` |
| `has` | Array contains a value | `(has "issue.labels" "bug")` |
| `has-all` | Array contains every listed value | `(has-all "issue.labels" ("bug" "critical"))` |
| `has-any` | Array contains at least one listed value | `(has-any "issue.labels" ("bug" "enhancement"))` |
| `gt`, `gte`, `lt`, `lte` | Numeric comparison | `(gte "pull_request.changed_files" 5)` |
| `exists` | Field exists and is not null/undefined | `(exists "issue.milestone")` |

To express “not equal”, use `(not (eq "field" value))`. `starts-with` applies to string values; numeric comparisons require a number.

## Example: route important pull requests

```text
(and
  (eq "action" "opened")
  (starts-with "pull_request.head.ref" "release/")
  (gte "pull_request.changed_files" 2))
```

This accepts only newly opened pull requests from a `release/` branch with at least two changed files. Adapt the field paths and values to the sender's actual payload.

## Test before relying on a filter

Use sample events that should match and events that should be rejected. Check exact field names, types, case, nested paths, and array contents. A missing field or type mismatch may cause the expression not to match. Keep the expression readable and add conditions gradually.
