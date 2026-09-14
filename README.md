# Counso Docs

Counso 的英文和中文文档，按原文章路径逐篇对应。目录以 [ByteCodeMonkey/counso-docs](https://github.com/ByteCodeMonkey/counso-docs/tree/4bf686cfa77adaa9799318f9a903fcca7aa29437) 的原文索引为准。

- [English documentation](en/SUMMARY.md)
- [中文文档](zh-cn/SUMMARY.md)
- [原 URL → 原文 → 中英文正文](translations.json)

## 文件对应

| 文件 | 用途 |
| --- | --- |
| `source/` | 原始 Markdown、sitemap 和 URL 索引，保持来源版本不变。 |
| `en/` | 英文改写，目录和文件名与原文一致。 |
| `zh-cn/` | 中文改写，目录和文件名与原文一致。 |
| `translations.json` | 每个原 URL、原文文件、双语文件、发布路径和校验值。 |
| `redirects.json` | 现有短链接及已知拼写错误的跳转目标；不替代原文索引。 |

例如：

```text
https://docs.dust.tt/docs/user-documentation/agents/create-your-first-agent
  → source/docs/user-documentation/agents/create-your-first-agent.md
  → en/docs/user-documentation/agents/create-your-first-agent.md
  → zh-cn/docs/user-documentation/agents/create-your-first-agent.md
```

`source/url-index.json` 保留原仓库的映射，里面的文件路径相对于 `source/`。`translations.json` 的文件路径相对于仓库根目录，可直接读取，无需再按标题匹配。

## 接入文档站

只发布 `translations.json` 中 `status: publish` 的正文。英文沿用原 URL 路径，中文在相同路径前加 `/zh-cn`；实际路径已逐项写在 `translations` 的 `route` 字段中。例如：

```text
英文 /docs/user-documentation/agents/create-your-first-agent
中文 /zh-cn/docs/user-documentation/agents/create-your-first-agent
```

不要从标题重新生成 slug。原目录的 `index.md` 对应目录本身的 URL；具体以 `route` 为准。正文中的相对 `.md` 链接可直接在 GitHub 阅读，接入网站时按同一清单转换为页面地址，并保留链接的章节锚点。

`source/` 是查阅原文的资料，不作为 Counso 网站正文发布。原路径中保留的历史产品名称用于兼容链接，不决定页面标题或品牌。此仓库提供 Markdown 与对应关系，页面渲染沿用现有文档系统。

## 发布范围

原文索引中的 356 个页面和 2 份接口规范均有记录。其中 196 页提供完整的双语文件。公开 API、依赖该 API 的扩展与导入脚本暂不发布；上游发布历史和已弃用开发框架也不作为 Counso 文档发布。这些条目保留原文及排除原因，不生成占位文章。

文档中的第三方工具与数据连接按各工作区实际启用的能力使用。OAuth 应用、回调地址和部署出口地址须取当前环境的配置值。

## 检查

```sh
python3 scripts/check.py
```

检查覆盖全部原文索引、双语配对、文件校验值、页面路径、跳转目标及 Markdown 内链。修改正文后，运行 `python3 scripts/check.py --update-hashes`，通过检查后会同步更新正文校验值。
