# 筛选 Webhook 负载

筛选条件决定收到的 Webhook 事件是否启动智能体运行。对于受支持的集成，构建器可能可以根据自然语言描述生成筛选条件。自定义 Webhook 则需要使用发送方实际提供的负载字段编写表达式。

## 表达式格式

筛选语言使用 Lisp 风格的 S-expression：`(操作符 参数 ...)`。每个表达式返回 `true`（处理事件）或 `false`（忽略事件）。字符串使用双引号，数字不加引号，布尔值写作 `true` 或 `false`，列表用括号括起。

使用以点分隔的路径引用字段，例如 `"action"`、`"issue.state"` 或 `"pull_request.head.ref"`。引用数组中每个对象的字段时使用 `*`，例如 `"tags.*.name"`。字段路径必须与实际 JSON 负载一致。

## 操作符

| 操作符 | 用途 | 示例 |
|---|---|---|
| `and` | 所有子表达式都为真 | `(and (eq "action" "opened") (eq "issue.state" "open"))` |
| `or` | 至少一个子表达式为真 | `(or (eq "action" "opened") (eq "action" "edited"))` |
| `not` | 对一个表达式取反 | `(not (eq "issue.state" "closed"))` |
| `eq` | 精确比较字符串、数字或布尔值 | `(eq "issue.number" 42)` |
| `starts-with` | 字符串以指定前缀开头 | `(starts-with "pull_request.head.ref" "feature/")` |
| `has` | 数组包含指定值 | `(has "issue.labels" "bug")` |
| `has-all` | 数组包含列出的全部值 | `(has-all "issue.labels" ("bug" "critical"))` |
| `has-any` | 数组至少包含一个指定值 | `(has-any "issue.labels" ("bug" "enhancement"))` |
| `gt`、`gte`、`lt`、`lte` | 数值比较 | `(gte "pull_request.changed_files" 5)` |
| `exists` | 字段存在且不为 null/undefined | `(exists "issue.milestone")` |

“不等于”可写作 `(not (eq "field" value))`。`starts-with` 用于字符串；数值比较的参数必须是数字。

## 示例：筛选重要的 Pull Request

```text
(and
  (eq "action" "opened")
  (starts-with "pull_request.head.ref" "release/")
  (gte "pull_request.changed_files" 2))
```

该表达式只接受从 `release/` 分支新建、且至少修改两个文件的 Pull Request。请根据发送方实际负载调整字段路径和值。

## 使用筛选前先测试

准备应该匹配的样例事件，以及应该被拒绝的事件。检查字段名称、数据类型、大小写、嵌套路径和数组内容。字段缺失或类型不匹配时，表达式可能无法命中。保持表达式易读，并逐步添加条件。
