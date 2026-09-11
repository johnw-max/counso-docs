# Counso Docs

Counso 的中英文文档、原 URL 对应关系和可部署静态站点，共 61 个主题、122 篇中英文文章。

**Markdown 是正式维护源。** 在这里修改和审阅文章，再从同一版本生成网站。飞书用于展示和审阅，不参与网站构建。

## 阅读文档

- [English documentation](content/indexes/en.md)
- [中文文档](content/indexes/zh-cn.md)
- [URL 映射说明](mapping/README.md)

## 直接部署

`site/dist/` 是已构建的静态目录。将其中的内容部署到 `docs.counso.ai`，不要把整个仓库作为网站根目录。

重新构建：

```sh
cd site
npm ci
npm run build
npm run check:release
```

构建环境与 Nginx 配置见 [site/README.md](site/README.md)。构建读取仓库内的 Markdown 和映射，不需要飞书账号。

## 原地址如何对应到新文章

```text
原 sitemap / llms.txt
        ↓
reference/url-to-original.json
        ↓ 原地址、原 Markdown、固定来源版本
mapping/routes.json
        ↓ 对应主题、语言、章节和文件
content/topics/ + content/additions/
        ↓
site/dist/
```

- [原文索引](reference/url-to-original.json)记录原 URL、原始 Markdown 文件路径、内容校验值及固定版本的源文件链接。
- [路由映射](mapping/routes.json)将原地址与 Counso 中英文文章对应起来；有多篇相关说明的入口会同时记录关联文章。
- [正文清单](content/manifest.json)与[补充文章清单](content/additions-manifest.json)记录本地文件和校验值。
- 本次发布的 26 个应用文档入口保留路径，不要求应用改成另一套文章路径。章节兼容方式见路由说明。

原始文档已有独立归档，本仓库用固定版本链接关联，避免维护第二份原文。需要在本地查看全部原始 Markdown 时，可运行：

```sh
python3 scripts/fetch_originals.py
```

脚本恢复 356 篇原始 Markdown 和 2 份规范，并逐份核对校验值。它不参与 Counso 网站构建。原始文档是来源资料，不是直接发布的 Counso 正文；原始资料中未采用的页面会在映射里保留明确状态。

## 日常维护

1. 修改 `content/topics/en/`、`content/topics/zh-cn/` 或 `content/additions/` 中对应文章；文档互链使用相对 `.md` 路径，在 GitHub 上也能阅读。
2. 文章改名或新增时，同时更新清单和映射。保留已有入口，避免应用帮助链接失效。
3. 重新构建并检查，然后提交正文、映射与对应静态输出。
4. 将已确认的内容同步到飞书展示副本，避免用旧展示稿覆盖这里的新改动。

API 文档暂不发布。相关的 5 个旧入口及开发者稿件已从本次发布范围移除；依赖 Counso API 密钥的外部插件说明也不包含在内。应用中的对应入口应先隐藏，具体范围记录在 `content/release-policy.json` 和路由映射中。
