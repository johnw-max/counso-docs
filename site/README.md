# Counso AI documentation

This is the deployable Astro + Starlight documentation site for Counso AI. The default entry is English at `/en/`; Simplified Chinese is available at `/zh-cn/`. Historical unprefixed paths such as `/docs/intro` are materialised as compatibility pages and point to the corresponding authored Counso article.

The build reads the sibling `content/` and `mapping/` directories in this release package. It uses only the authored Markdown under `content/topics/` and `content/additions/`, their manifests, and `mapping/routes.json`; it does not read source archives, online documents. `COUNSO_DOCS_INPUT_ROOT` can point at another release root when developing, but is not needed for the packaged source tree.

`content/release-policy.json` is applied during generation. Topics marked
`hold_api` and excluded `developers/` topics are omitted from pages, indexes,
and legacy compatibility copies.

## Build and check

Use Node.js 22.12 or newer and Python 3. The checked-in `.nvmrc` selects
Node.js 24; `package.json` records the supported Node and npm ranges.

The packaged rebuild uses the existing Node.js and Python 3 runtimes only. The
offline prebuild sequence refreshes Markdown titles and hashes, rebuilds
`mapping/routes.json` from the package inputs, and then generates the Astro
pages. It reads local inputs without accessing the network.

```sh
npm ci
npm run build
npm run check:release
```

Run `npm run generate:release` when only the page generator needs to be
iterated. A complete release build always runs the metadata and route steps
above first.

`npm run build` regenerates bilingual pages, local Markdown copies, the sidebar, `public/llms.txt`, `public/sitemap.xml`, and `public/release-manifest.json`, then builds `dist/`. `npm run check:release` checks topic pairs, route coverage, local links, anchors, compatibility pages, and visible source or brand leakage.

To preview the static output:

```sh
npm run preview -- --host 127.0.0.1 --port 4321
```

Deploy the contents of `dist/` to a static host. The included `docker/nginx.conf` serves `/` with an HTTP 302 to `/en/`, matching the Astro root page. Set `DOCS_SITE_URL` for canonical metadata and `COUNSO_APP_URL` for the application link before building when the host differs from the defaults.
