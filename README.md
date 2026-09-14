# Counso Docs

Counso 的英文和中文文档，逐篇关联原文章和原始 URL。文章范围以 [ByteCodeMonkey/counso-docs](https://github.com/ByteCodeMonkey/counso-docs/tree/4bf686cfa77adaa9799318f9a903fcca7aa29437) 的原文索引为准，展示名称使用 Counso。

- [English documentation](en/SUMMARY.md)
- [中文文档](zh-cn/SUMMARY.md)
- [原 URL → 原文 → 中英文正文](translations.json)
- [文档发布范围与准备稿](PUBLICATION-STATUS.md)

## 文件对应

| 文件 | 用途 |
| --- | --- |
| `source/` | 原始 Markdown、sitemap 和 URL 索引，保持来源版本不变。 |
| `en/` | 英文改写；文件和目录名称中的旧品牌已改为 Counso。 |
| `zh-cn/` | 中文改写，与英文正文逐篇对应。 |
| `prepared/` | 暂未进入站点的双语集成稿，保留品牌化正文，供对应集成交付时使用。 |
| `translations.json` | 每个原 URL、原文标题与文件、双语展示标题、文件、发布路径和校验值。 |
| `redirects.json` | 旧品牌路径、现有短链接及已知拼写错误的跳转目标。 |
| `en/UPDATING.md`、`zh-cn/UPDATING.md` | 暂缺教程共用的“更新中”提示。 |
| `PUBLICATION-STATUS.md` | 逐项列出配置教程、准备稿与其发布前提、本版不提供的资料。 |

例如：

```text
https://docs.dust.tt/docs/user-documentation/getting-started/dust-rollout-guide/welcome-to-dust
  → source/docs/user-documentation/getting-started/dust-rollout-guide/welcome-to-dust.md
  → en/docs/user-documentation/getting-started/counso-rollout-guide/welcome-to-counso.md
  → zh-cn/docs/user-documentation/getting-started/counso-rollout-guide/welcome-to-counso.md
```

`source/url-index.json` 保留原仓库的映射，里面的文件路径相对于 `source/`。`translations.json` 的文件路径相对于仓库根目录，可直接读取，无需再按标题匹配。

## 接入文档站

按 `translations.json` 中的状态处理页面：

| 状态 | 页面处理 |
| --- | --- |
| `publish` | 使用 `translations` 中相应语言的 `title`、`file` 和 `route`。 |
| `updating` | 使用 `notice` 中相应语言的 `title`、`file` 和 `route`，只显示文档更新提示；不加入正常导航、搜索索引或推荐入口。 |
| `exclude_api`、`exclude_upstream` | 不发布对应原文，也不加入用户文档导航。 |

页面标题、浏览器标题、侧栏名称和面包屑使用相应语言的 `title`，与 Markdown 的一级标题一致。文档目录见 `en/SUMMARY.md` 和 `zh-cn/SUMMARY.md`。不要使用 `original_title`、`source/manifest.json` 的标题或旧文件名生成用户可见名称；它们属于原文资料。

### 品牌名称与旧链接

改写版将路径中独立的 `dust` 品牌词改为 `counso`，其余层级和文章对应关系不变；中文在英文路径前加 `/zh-cn`。因此部分改写文件的路径与原文不同，这是品牌更名，不是缺少文章。三个例子如下：

| 原文路径末尾 | 英文展示名称 | 中文展示名称 | 新路径末尾 |
| --- | --- | --- | --- |
| `dust-rollout-guide` | Counso rollout guide | Counso 团队落地指南 | `counso-rollout-guide` |
| `dust-rollout-guide/welcome-to-dust` | Welcome to Counso | 欢迎使用 Counso | `counso-rollout-guide/welcome-to-counso` |
| `dust-rollout-guide/admin-guide-set-up-your-dust-workspace` | Set up your Counso workspace | 设置 Counso 工作区 | `counso-rollout-guide/admin-guide-set-up-your-counso-workspace` |

例如欢迎页的完整发布路径为：

```text
英文 /docs/user-documentation/getting-started/counso-rollout-guide/welcome-to-counso
中文 /zh-cn/docs/user-documentation/getting-started/counso-rollout-guide/welcome-to-counso
```

旧域名对应的本站路径继续通过 `redirects.json` 跳转到新路径；这些跳转须与正文一起接入，不能只部署新文件。这里的跳转发生在 Counso 自己托管的域名下，不控制原站。已有短链接也直接指向新路径。

不要从标题重新生成 slug，也不要按原文路径猜测改写文件名。按 `translations.json` 直接读取文件和路由；目录的 `index.md` 对应目录本身的 URL。正文中的相对 `.md` 链接可直接在 GitHub 阅读，接入网站时按同一清单转换为页面地址，并保留链接的章节锚点。映射版本为 3。

`source/` 是查阅原文的资料，保留原始标题和文件名，不作为 Counso 网站正文发布。`prepared/` 和 `PUBLICATION-STATUS.md` 也不加入用户文档站；页面不展示映射中的内部状态字段或更名说明。此仓库提供 Markdown 与对应关系，页面渲染沿用现有文档系统。

## 发布范围

原文索引中的 356 个页面和 2 份接口规范均有记录，其中 193 页提供双语正文。通用远程 MCP 接入、管理员可配置的第三方工具、数据连接及相关使用说明在发布范围内。配置教程不因某个工作区尚未完成授权而隐藏；正文会写清管理员需要完成的配置。

另外 19 篇集成教程已准备中英文稿件，当前 URL 显示“文档更新中”。这些主题仍适用于 Counso，但发布可执行教程前还需提供专用应用、分发包、导入脚本或服务配置。具体缺项与稿件链接见[文档发布范围与准备稿](PUBLICATION-STATUS.md)。137 份公开 API 及配套开发资料本版不提供；9 份原产品更新历史、实验仓库说明和已弃用框架资料不纳入 Counso 文档。

原文和原始 URL 均保留。用户页面只展示正文或简短的文档更新提示，不展示内部交付说明。

准备稿由 `translations.json` 的 `prepared` 字段关联，不能代替当前的 `notice` 发布。对应集成提供后，核对实际安装入口、运行步骤和结果，将稿件移到 `en/`、`zh-cn/`，把条目改为 `publish` 并更新目录、文件路径和校验值。原始 URL、正式路由和兼容跳转继续沿用；不需要重建文章对应关系。准备稿介绍产品使用方式，不包含尚未交付的程序包，也不代表集成已经上线。

文档中的第三方工具与数据连接按各工作区实际启用的能力使用。OAuth 应用、回调地址和部署出口地址须取当前环境的配置值。

## 检查

```sh
python3 scripts/check.py
```

检查覆盖全部原文索引、双语配对、文件校验值、页面路径、跳转目标及 Markdown 内链。修改正文后，运行 `python3 scripts/check.py --update-hashes`，通过检查后会同步更新正文校验值。
