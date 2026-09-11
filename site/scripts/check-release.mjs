import { readFile, readdir } from 'node:fs/promises';
import { dirname, join, relative, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const siteDir = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const docsRoot = resolve(siteDir, 'src/content/docs');
const publicRoot = resolve(siteDir, 'public');
const distRoot = resolve(siteDir, 'dist');
const fail = (message) => { throw new Error(`[release check] ${message}`); };

async function walk(dir) {
	try {
		const entries = await readdir(dir, { withFileTypes: true });
		const files = [];
		for (const entry of entries) {
			const path = join(dir, entry.name);
			if (entry.isDirectory()) files.push(...await walk(path));
			else files.push(path);
		}
		return files;
	} catch { return []; }
}

const releaseManifestPath = resolve(publicRoot, 'release-manifest.json');
let releaseManifest;
try { releaseManifest = JSON.parse(await readFile(releaseManifestPath, 'utf8')); }
catch (error) { fail(`missing or invalid ${relative(siteDir, releaseManifestPath)}: ${error.message}`); }
if (releaseManifest.schemaVersion !== 2 || !Array.isArray(releaseManifest.pages)) fail('release manifest schemaVersion/pages are invalid');
if (!releaseManifest.topicCount || releaseManifest.pageCount !== releaseManifest.pages.length) fail('release manifest counts do not match pages');

const pageKeys = new Set();
const aliases = new Set();
for (const page of releaseManifest.pages) {
	if (!['en', 'zh-cn'].includes(page.locale) || !page.topicId || !page.route) fail(`invalid page record: ${JSON.stringify(page)}`);
	const key = `${page.locale}|${page.route}`;
	if (pageKeys.has(key)) fail(`duplicate page route ${key}`);
	pageKeys.add(key);
	for (const alias of page.aliases ?? []) {
		const aliasKey = `${page.locale}|${alias}`;
		if (pageKeys.has(aliasKey) || aliases.has(aliasKey)) fail(`duplicate legacy route ${aliasKey}`);
		aliases.add(aliasKey);
	}
}
const topicLocales = new Map();
for (const page of releaseManifest.pages) {
	if (!topicLocales.has(page.topicId)) topicLocales.set(page.topicId, new Set());
	topicLocales.get(page.topicId).add(page.locale);
}
for (const [topicId, locales] of topicLocales) if (locales.size !== 2) fail(`topic ${topicId} does not have both locales`);

const localRoutes = new Set([...pageKeys, ...aliases, 'en|index', 'zh-cn|index']);
const markdownFiles = (await walk(docsRoot)).filter((path) => /\.(md|mdx)$/.test(path));
if (markdownFiles.length < releaseManifest.pageCount + 2) fail(`generated docs are incomplete: found ${markdownFiles.length} files`);

function localTarget(target, source) {
	if (!target || target.startsWith('#')) return null;
	if (!target.startsWith('/')) return null;
	const clean = target.split('?')[0];
	const [path, anchor] = clean.split('#');
	const parts = path.replace(/^\/+|\/+$/g, '').split('/');
	const locale = parts.shift();
	if (!['en', 'zh-cn'].includes(locale)) fail(`local link has unsupported locale in ${relative(siteDir, source)}: ${target}`);
	const route = parts.join('/') || 'index';
	return { key: `${locale}|${route}`, anchor: anchor ?? '' };
}

const localLinks = [];
for (const file of markdownFiles) {
	const source = await readFile(file, 'utf8');
	if (/\bDust\b/i.test(source)) fail(`Dust brand text remains in ${relative(siteDir, file)}`);
	if (/https?:\/\/[^\s)<>]*(?:feishu|larksuite|larkoffice)[^\s)<>]*/i.test(source)) fail(`Feishu URL remains in ${relative(siteDir, file)}`);
	for (const match of source.matchAll(/\]\((<[^>]+>|[^)\s]+)\)/g)) {
		const raw = match[1].replace(/^<|>$/g, '');
		const local = localTarget(raw, file);
		if (local) {
			if (!localRoutes.has(local.key)) fail(`broken local route ${raw} in ${relative(siteDir, file)}`);
			localLinks.push({ ...local, source: file });
		}
	}
}

const llms = await readFile(resolve(publicRoot, 'llms.txt'), 'utf8');
if (/\bDust\b/i.test(llms) || /https?:\/\/[^\s)<>]*(?:feishu|larksuite|larkoffice)[^\s)<>]*/i.test(llms)) fail('llms.txt contains forbidden visible brand/source links');
const sitemap = await readFile(resolve(publicRoot, 'sitemap.xml'), 'utf8');
if ((sitemap.match(/<loc>/g) ?? []).length !== releaseManifest.pageCount) fail('sitemap URL count does not match canonical pages');

const distFiles = await walk(distRoot);
if (distFiles.length) {
	const htmlFiles = distFiles.filter((path) => path.endsWith('.html'));
	for (const file of htmlFiles) {
		const html = await readFile(file, 'utf8');
		const body = html.match(/<body[^>]*>([\s\S]*?)<\/body>/i)?.[1] ?? html;
		const visibleText = body.replace(/<script[\s\S]*?<\/script>/gi, '').replace(/<style[\s\S]*?<\/style>/gi, '').replace(/<[^>]+>/g, ' ');
		if (/\bDust\b/i.test(visibleText)) fail(`Dust brand text remains visible in ${relative(siteDir, file)}`);
		if (/https?:\/\/[^\s"'<>]*(?:feishu|larksuite|larkoffice)[^\s"'<>]*/i.test(body)) fail(`Feishu URL remains in ${relative(siteDir, file)}`);
	}
	const htmlByRoute = new Map();
	for (const file of htmlFiles) {
		const rel = relative(distRoot, file).replace(/\\/g, '/');
		const route = rel.replace(/\/index\.html$/, '').replace(/\.html$/, '');
		htmlByRoute.set(route || 'index', file);
	}
	for (const page of releaseManifest.pages) {
		const route = `${page.locale}/${page.route === 'index' ? '' : `${page.route}/`}`.replace(/\/$/, '');
		if (!htmlByRoute.has(route)) fail(`missing built HTML for ${route}`);
		for (const alias of page.aliases ?? []) {
			const aliasRoute = `${page.locale}/${alias}`;
			if (!htmlByRoute.has(aliasRoute)) fail(`missing built HTML for legacy route ${aliasRoute}`);
		}
		for (const rootAlias of page.rootAliases ?? []) {
			if (rootAlias === 'index') continue;
			if (!htmlByRoute.has(rootAlias)) fail(`missing built HTML for root legacy route ${rootAlias}`);
		}
	}
	const idsByFile = new Map();
	for (const [route, file] of htmlByRoute) {
		const html = await readFile(file, 'utf8');
		idsByFile.set(route, new Set([...html.matchAll(/\sid=["']([^"']+)["']/g)].map((match) => match[1])));
	}
	for (const link of localLinks) {
		if (!link.anchor) continue;
		const ids = idsByFile.get(link.key.replace('|', '/'));
		if (ids && !ids.has(link.anchor)) fail(`broken anchor #${link.anchor} in ${relative(siteDir, link.source)}`);
	}
}
console.log(`[release check] passed ${releaseManifest.topicCount} topics, ${releaseManifest.pageCount} canonical pages, ${localLinks.length} local links${distFiles.length ? ', built HTML and anchors checked' : ''}`);
