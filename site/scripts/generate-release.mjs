import { mkdir, readdir, readFile, rm, writeFile } from 'node:fs/promises';
import { dirname, extname, join, relative, resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

const siteDir = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const releaseRoot = resolve(siteDir, '..');
const inputRoot = process.env.COUNSO_DOCS_INPUT_ROOT
	? resolve(process.env.COUNSO_DOCS_INPUT_ROOT)
	: releaseRoot;
const contentRoot = resolve(inputRoot, 'content');
const mappingRoot = resolve(inputRoot, 'mapping');
const docsRoot = resolve(siteDir, 'src/content/docs');
const publicRoot = resolve(siteDir, 'public');
const generatedRoot = resolve(siteDir, 'src/generated');
const locales = ['en', 'zh-cn'];

const fail = (message) => {
	throw new Error(`[counso release] ${message}`);
};

const exists = async (path) => {
	try {
		await readFile(path);
		return true;
	} catch {
		return false;
	}
};

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
	} catch {
		return [];
	}
}

const asObject = (value) => value && typeof value === 'object' && !Array.isArray(value) ? value : {};

function normaliseLocale(value) {
	const locale = String(value ?? '').trim().toLowerCase().replace('_', '-');
	if (locale === 'zh' || locale === 'zh-cn' || locale === 'zh-hans') return 'zh-cn';
	if (locale === 'en' || locale === 'en-us' || locale === 'en-sg') return 'en';
	return locale;
}

function scalar(value) {
	if (value === undefined || value === null) return '';
	return typeof value === 'string' || typeof value === 'number' ? String(value).trim() : '';
}

function sourceUrlsOf(value) {
	const raw = value?.sourceUrls ?? value?.FeishuURL ?? value?.feishuURL ?? value?.sourceUrl ?? value?.sourceURL ?? value?.url;
	const values = Array.isArray(raw) ? raw : [raw];
	return values.map(scalar).filter(Boolean);
}

function revisionOf(value) {
	return scalar(value?.revision ?? value?.contentRevision ?? value?.revisionId ?? value?.revision_id);
}

function rawRecords(document) {
	const root = asObject(document);
	for (const key of ['entries', 'topics', 'documents', 'items', 'pages', 'records']) {
		if (Array.isArray(root[key])) return root[key];
	}
	if (Array.isArray(document)) return document;
	const nested = Object.entries(root).filter(([, value]) => value && typeof value === 'object');
	if (nested.length) return nested.map(([topicId, value]) => ({ topicId, ...asObject(value) }));
	return [];
}

function flattenRecord(record, inherited = {}) {
	const value = asObject(record);
	const parent = { ...inherited, ...value };
	const topicId = scalar(value.topicId ?? value.id ?? inherited.topicId);
	const localeValue = value.locale ?? value.language;
	const localeFiles = value.locales ?? value.files ?? value.translations ?? value.byLocale;
	if (!localeValue && localeFiles && typeof localeFiles === 'object' && !Array.isArray(localeFiles)) {
		return Object.entries(localeFiles).flatMap(([locale, child]) => flattenRecord({
			...asObject(child),
			topicId: asObject(child).topicId ?? topicId,
			title: asObject(child).title ?? value.title,
		}, { ...parent, locale })).map((entry) => entry);
	}
	if (!localeValue && (value.en || value['zh-cn'] || value.zh || value.zhCN)) {
		return Object.entries({ en: value.en, 'zh-cn': value['zh-cn'] ?? value.zh ?? value.zhCN })
			.filter(([, child]) => child)
			.flatMap(([locale, child]) => flattenRecord({
				...asObject(child),
				topicId: asObject(child).topicId ?? topicId,
				title: asObject(child).title ?? value.title,
			}, { ...parent, locale }));
	}
	if (!localeValue) return [];
	const merged = { ...inherited, ...value };
	return [{
		topicId: scalar(merged.topicId ?? topicId),
		title: scalar(merged.title ?? merged.name),
		locale: normaliseLocale(localeValue),
		file: scalar(merged.file ?? merged.path ?? merged.sourceFile ?? merged.markdown),
		sourceUrls: sourceUrlsOf(merged),
		docToken: scalar(merged.docToken ?? merged.documentId ?? merged.document_id ?? merged.token),
		revision: revisionOf(merged) || scalar(merged.hash ?? merged.sha256),
		hash: scalar(merged.hash ?? merged.sha256),
		section: scalar(merged.section ?? merged.category ?? merged.group),
		publicationStatus: scalar(merged.publicationStatus ?? merged.publication_status ?? merged.status),
	}];
}

async function readJson(path) {
	try {
		return JSON.parse(await readFile(path, 'utf8'));
	} catch (error) {
		fail(`cannot parse ${relative(inputRoot, path)}: ${error.message}`);
	}
}

async function findManifestFiles() {
	const preferred = [
		join(contentRoot, 'manifest.json'),
		join(contentRoot, 'topics-manifest.json'),
		join(contentRoot, 'additions-manifest.json'),
		join(inputRoot, 'manifest.json'),
	];
	const files = (await walk(contentRoot)).filter((path) => /manifest.*\.json$/i.test(path));
	const candidates = [...new Set([...preferred, ...files])]
		.filter((path) => path.startsWith(contentRoot + sep));
	return (await Promise.all(candidates.map(async (path) => await exists(path) ? path : null))).filter(Boolean);
}

function resolveInputFile(file) {
	if (!file) return '';
	if (file.startsWith('/') || /^[A-Za-z]:[\\/]/.test(file)) fail(`source file must be relative: ${file}`);
	const candidates = [
		resolve(contentRoot, file),
		resolve(inputRoot, file),
		resolve(contentRoot, file.replace(/^content[\\/]/, '')),
		resolve(siteDir, file),
	];
	for (const path of candidates) {
		const safe = path === contentRoot || path === inputRoot || path === siteDir || path.startsWith(contentRoot + sep) || path.startsWith(siteDir + sep);
		if (safe && /\.(md|mdx)$/.test(path)) return path;
	}
	return candidates[0];
}

function cleanRoute(value, locale) {
	let route = scalar(value);
	if (!route) return '';
	try {
		if (/^https?:\/\//i.test(route)) route = new URL(route).pathname;
	} catch {
		fail(`invalid route URL: ${value}`);
	}
	route = route.split('#')[0].split('?')[0].replace(/\\/g, '/').replace(/^\/+|\/+$/g, '');
	if (route.endsWith('.html')) route = route.slice(0, -5);
	if (route.endsWith('.md')) route = route.slice(0, -3);
	if (route === locale) route = 'index';
	if (route.startsWith(`${locale}/`)) route = route.slice(locale.length + 1);
	if (!route || route === 'index') return 'index';
	if (route.includes('..') || route.split('/').some((part) => !part || part === '.' || part === '..')) fail(`invalid route: ${value}`);
	return route;
}

function mappingRecords(document) {
	const root = asObject(document);
	// routes.json is an address ledger: one row can carry the English and
	// Chinese target independently, plus a legacy path without a locale prefix.
	// Expand it here so the rest of the generator can use the same compact
	// topic-locale mapping shape as other mapping producers.
	if (Array.isArray(root.routes) && root.routes.some((entry) => entry?.originalPath || entry?.target)) {
		return root.routes.flatMap((entry) => Object.entries(asObject(entry.target)).map(([locale, target]) => ({
			topicId: asObject(target).topicId || entry.targetTopicId || '',
			locale,
			route: asObject(target).url || asObject(target).path || '',
			legacyPaths: entry.originalPath ? [entry.originalPath] : [],
			sourceUrls: entry.originalUrl ? [entry.originalUrl] : [],
			docToken: docTokenFromUrl(asObject(target).url || ''),
			anchorMap: entry.fragment && entry.fragment !== '/' ? { [entry.fragment]: entry.targetSection || entry.fragment } : {},
		}))).filter((entry) => entry.topicId || entry.legacyPaths.some((path) => path === '/'));
	}
	for (const key of ['entries', 'routes', 'mappings', 'routeMap', 'pages', 'items']) {
		if (Array.isArray(root[key])) return root[key];
		if (root[key] && typeof root[key] === 'object') {
			return Object.entries(root[key]).map(([topicId, value]) => ({ topicId, ...asObject(value) }));
		}
	}
	if (Array.isArray(document)) return document;
	const values = Object.entries(root).filter(([, value]) => value && typeof value === 'object');
	return values.map(([topicId, value]) => ({ topicId, ...asObject(value) }));
}

function flattenMapping(record, inherited = {}) {
	const value = asObject(record);
	const merged = { ...inherited, ...value };
	const topicId = scalar(merged.topicId ?? merged.id);
	const nested = value.locales ?? value.routes ?? value.byLocale;
	if (!value.locale && nested && typeof nested === 'object' && !Array.isArray(nested)) {
		return Object.entries(nested).flatMap(([locale, child]) => flattenMapping({
			...asObject(child), topicId: asObject(child).topicId ?? topicId,
		}, { ...merged, locale }));
	}
	if (!value.locale && (value.en || value['zh-cn'] || value.zh || value.zhCN)) {
		return Object.entries({ en: value.en, 'zh-cn': value['zh-cn'] ?? value.zh ?? value.zhCN })
			.filter(([, child]) => child)
			.flatMap(([locale, child]) => flattenMapping({ ...asObject(child), topicId: asObject(child).topicId ?? topicId }, { ...merged, locale }));
	}
	const locale = normaliseLocale(merged.locale ?? merged.language);
	if (!locale) return [];
	const canonical = scalar(merged.route ?? merged.path ?? merged.canonical ?? merged.canonicalPath ?? merged.slug ?? merged.target);
	const aliases = [
		...(Array.isArray(merged.legacyRoutes) ? merged.legacyRoutes : []),
		...(Array.isArray(merged.legacyPaths) ? merged.legacyPaths : []),
		...(Array.isArray(merged.aliases) ? merged.aliases : []),
		...(Array.isArray(merged.oldPaths) ? merged.oldPaths : []),
		...(Array.isArray(merged.oldRoutes) ? merged.oldRoutes : []),
		...([merged.legacyRoute, merged.legacyPath, merged.oldPath, merged.oldRoute].filter(Boolean)),
	].map((route) => cleanRoute(route, locale));
	const rootAliases = [
		...(Array.isArray(merged.legacyRoutes) ? merged.legacyRoutes : []),
		...(Array.isArray(merged.legacyPaths) ? merged.legacyPaths : []),
		...(Array.isArray(merged.aliases) ? merged.aliases : []),
		...(Array.isArray(merged.oldPaths) ? merged.oldPaths : []),
		...(Array.isArray(merged.oldRoutes) ? merged.oldRoutes : []),
		...([merged.legacyRoute, merged.legacyPath, merged.oldPath, merged.oldRoute].filter(Boolean)),
	].filter((route) => {
		const normal = scalar(route).replace(/\\/g, '/').replace(/^\/+/, '');
		return !locales.includes(normaliseLocale(normal.split('/')[0]));
	}).map((route) => cleanRoute(route, locale));
	return [{
		topicId,
		locale,
		route: cleanRoute(canonical, locale),
		aliases: [...new Set(aliases.filter(Boolean))],
		rootAliases: [...new Set(rootAliases.filter(Boolean))],
		sourceUrls: sourceUrlsOf(merged),
		docToken: scalar(merged.docToken ?? merged.documentId ?? merged.document_id ?? merged.token),
		anchor: scalar(merged.anchor ?? merged.hash ?? merged.fragment),
		anchorMap: asObject(merged.anchorMap ?? merged.fragmentMap ?? merged.hashMap),
	}];
}

function routeFromFile(file, locale) {
	const normal = file.replace(/\\/g, '/');
	const marker = `/content/`;
	const afterContent = normal.includes(marker) ? normal.slice(normal.indexOf(marker) + marker.length) : normal;
	const withoutLocale = afterContent.replace(/^(topics|additions)\//, '').replace(new RegExp(`^${locale}/`), '');
	return cleanRoute(withoutLocale.replace(/\.(md|mdx)$/i, ''), locale);
}

function parseFrontmatter(source) {
	const match = source.match(/^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)/);
	if (!match) return { fields: {}, body: source.trim() };
	const fields = {};
	for (const line of match[1].split(/\r?\n/)) {
		const field = line.match(/^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$/);
		if (field) fields[field[1]] = field[2].replace(/^['"]|['"]$/g, '').trim();
	}
	return { fields, body: source.slice(match[0].length).trim() };
}

function yamlString(value) {
	return JSON.stringify(String(value));
}

function withFrontmatter(source, record, hidden = false) {
	const parsed = parseFrontmatter(source);
	if (parsed.fields.title && parsed.fields.title !== record.title) fail(`${record.topicId}/${record.locale} title differs between manifest and source`);
	if (parsed.fields.topicId && parsed.fields.topicId !== record.topicId) fail(`${record.topicId}/${record.locale} topicId differs between manifest and source`);
	if (parsed.fields.contentRevision && parsed.fields.contentRevision !== record.revision) fail(`${record.topicId}/${record.locale} revision differs between manifest and source`);
	const rawLines = source.match(/^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)/)?.[1]?.split(/\r?\n/) ?? [];
	const lines = rawLines.filter((line) => !/^(slug|title|topicId|contentRevision|sidebar):\s*/.test(line));
	const frontmatter = [
		`title: ${yamlString(record.title)}`,
		...(parsed.fields.description ? [`description: ${yamlString(parsed.fields.description)}`] : []),
		`topicId: ${yamlString(record.topicId)}`,
		`contentRevision: ${yamlString(record.revision)}`,
		...(hidden ? ['sidebar:', '  hidden: true'] : []),
		...lines,
	];
	return `---\n${frontmatter.join('\n')}\n---\n\n${parsed.body}\n`;
}

function titleCase(value) {
	return value.split('-').map((part) => part ? part[0].toUpperCase() + part.slice(1) : part).join(' ');
}

const sectionTranslations = {
	'getting-started': ['Getting started', '快速开始'],
	agents: ['Agents', '智能体'],
	knowledge: ['Knowledge', '知识'],
	skills: ['Skills', '技能'],
	'administration': ['Administration', '管理'],
	connections: ['Connections and tools', '连接与工具'],
	pods: ['Pods', 'Pods'],
	'automated-runs': ['Automated runs', '自动运行'],
	developers: ['Developer guide', '开发者指南'],
	'practical-workflows': ['Practical workflows', '实用工作流'],
};

// The maintained index files use descriptive section anchors. Keep those
// anchors on the generated home pages so older bilingual links remain valid
// after the index becomes a generated page.
const homeAnchorAliases = {
	'getting-started': ['getting-started', '快速开始'],
	agents: ['working-with-agents', '智能体配置与使用'],
	knowledge: ['knowledge-and-sources', '知识来源与回答核对'],
	skills: ['working-with-skills', '技能管理'],
	'administration': ['workspace-access', '工作区访问管理'],
	integrations: ['connections-and-tools', '连接与工具'],
	pods: ['working-in-pods', 'pod-协作'],
	automations: ['automated-runs', '自动化运行'],
	developers: ['developer-guide', '开发者指南'],
	guides: ['practical-workflows', '工作案例'],
};

function localLink(locale, route, anchor = '') {
	return `/${locale}/${route === 'index' ? '' : `${route}/`}${anchor ? `#${anchor.replace(/^#/, '')}` : ''}`;
}

function normaliseUrl(value) {
	try {
		const url = new URL(value);
		return `${url.origin}${url.pathname}${url.search}${url.hash}`;
	} catch {
		return value;
	}
}

function isFeishu(value) {
	try {
		const host = new URL(value).hostname.toLowerCase();
		return host.includes('feishu') || host.includes('larksuite') || host.includes('larkoffice');
	} catch {
		return false;
	}
}

function docTokenFromUrl(value) {
	try {
		const parts = new URL(value).pathname.split('/').filter(Boolean);
		const marker = parts.findIndex((part) => ['docx', 'wiki', 'document', 'docs'].includes(part.toLowerCase()));
		return marker >= 0 ? parts[marker + 1] ?? '' : '';
	} catch {
		return '';
	}
}

function aliasKey(locale, route) {
	return `${locale}|${route}`;
}

const manifestFiles = await findManifestFiles();
if (!manifestFiles.length) fail(`no content manifest found under ${relative(releaseRoot, contentRoot)}`);
const records = [];
for (const path of manifestFiles) {
	const raw = await readJson(path);
	for (const item of rawRecords(raw)) records.push(...flattenRecord(item));
}
const publicationStatus = (record) => record.publicationStatus.toLowerCase().replace(/[-\s]+/g, '_');
const policyPath = resolve(contentRoot, 'release-policy.json');
const releasePolicy = await exists(policyPath) ? await readJson(policyPath) : {};
const excludedTopicPrefixes = Array.isArray(releasePolicy.excludedTopicPrefixes) ? releasePolicy.excludedTopicPrefixes.map(scalar).filter(Boolean) : [];
const isExcluded = (record) => {
	const status = publicationStatus(record);
	return status === 'hold_api'
		|| status === 'excluded_api_not_public'
		|| excludedTopicPrefixes.some((prefix) => record.topicId.startsWith(prefix));
};
const excludedRecords = records.filter(isExcluded);
const validRecords = records.filter((record) => (record.topicId || record.file || record.title) && !excludedRecords.includes(record));
if (!validRecords.length) fail('content manifests contain no locale records');
const byKey = new Map();
for (const record of validRecords) {
	if (!locales.includes(record.locale)) fail(`unsupported locale ${record.locale} for ${record.topicId}`);
	if (!record.topicId || !record.title || !record.file || !record.revision) fail(`manifest entry is incomplete: ${JSON.stringify(record)}`);
	const path = resolveInputFile(record.file);
	if (!await exists(path)) fail(`missing source file for ${record.topicId}/${record.locale}: ${record.file}`);
	const key = `${record.topicId}|${record.locale}`;
	if (byKey.has(key)) fail(`duplicate topic locale: ${key}`);
	byKey.set(key, { ...record, sourcePath: path });
}

const topicIds = new Set([...byKey.values()].map((record) => record.topicId));
for (const topicId of topicIds) {
	for (const locale of locales) if (!byKey.has(`${topicId}|${locale}`)) fail(`topic ${topicId} is missing ${locale}`);
}

const mapFiles = (await walk(mappingRoot)).filter((path) => path.endsWith('.json'));
const mapping = [];
for (const path of mapFiles) mapping.push(...mappingRecords(await readJson(path)).flatMap((item) => flattenMapping(item)));
const mappingByKey = new Map();
for (const item of mapping.filter((entry) => entry.topicId && entry.locale)) {
	const key = `${item.topicId}|${item.locale}`;
	const existing = mappingByKey.get(key);
	if (!existing) {
		mappingByKey.set(key, { ...item, aliases: [...item.aliases], rootAliases: [...(item.rootAliases ?? [])], sourceUrls: [...item.sourceUrls], anchorMap: { ...item.anchorMap } });
		continue;
	}
	// A route map can have one row per legacy entry. Collapse rows by topic and
	// locale while retaining every alias, source URL, and fragment mapping.
	const extraRoute = item.route && item.route !== existing.route ? [item.route] : [];
	mappingByKey.set(key, {
		...existing,
		route: existing.route || item.route,
		aliases: [...new Set([...existing.aliases, ...item.aliases, ...extraRoute])],
		rootAliases: [...new Set([...(existing.rootAliases ?? []), ...(item.rootAliases ?? [])])],
		sourceUrls: [...new Set([...existing.sourceUrls, ...item.sourceUrls])],
		docToken: existing.docToken || item.docToken,
		anchor: existing.anchor || item.anchor,
		anchorMap: { ...existing.anchorMap, ...item.anchorMap },
	});
}
const routeByKey = new Map();
for (const record of byKey.values()) {
	const routeMap = mappingByKey.get(`${record.topicId}|${record.locale}`);
	const route = routeMap?.route || routeFromFile(record.sourcePath, record.locale);
	if (!route || route === 'index') fail(`no route for ${record.topicId}/${record.locale}`);
	const aliases = routeMap?.aliases ?? [];
	routeByKey.set(`${record.topicId}|${record.locale}`, { route, aliases, rootAliases: routeMap?.rootAliases ?? [], map: routeMap });
}

const routeOwners = new Map();
const aliasOwners = new Map();
const rootAliasOwners = new Map();
for (const [key, routeInfo] of routeByKey) {
	const [topicId, locale] = key.split('|');
	const routeKey = aliasKey(locale, routeInfo.route);
	if (routeOwners.has(routeKey) && routeOwners.get(routeKey) !== key) fail(`route collision: ${routeKey}`);
	routeOwners.set(routeKey, key);
	for (const alias of routeInfo.aliases) {
		const aliasRoute = aliasKey(locale, alias);
		if (aliasOwners.has(aliasRoute) && aliasOwners.get(aliasRoute) !== key) fail(`legacy route collision: ${aliasRoute}`);
		aliasOwners.set(aliasRoute, key);
	}
	for (const alias of routeInfo.rootAliases ?? []) {
		if (alias === 'index') continue;
		const previous = rootAliasOwners.get(alias);
		if (previous && previous !== key && previous.split('|')[0] !== key.split('|')[0]) fail(`root legacy route collision: ${alias}`);
		rootAliasOwners.set(alias, key);
	}
}

const routeEntries = [...byKey.values()].map((record) => {
	const key = `${record.topicId}|${record.locale}`;
	const info = routeByKey.get(key);
	return { ...record, route: info.route, aliases: info.aliases, rootAliases: info.rootAliases, routeMap: info.map };
});
const fileRoutes = new Map(routeEntries.map((record) => [resolve(record.sourcePath), { locale: record.locale, route: record.route }]));
for (const indexFile of (await walk(resolve(contentRoot, 'indexes'))).filter((path) => /\.(md|mdx)$/.test(path))) {
	const locale = normaliseLocale(indexFile.split(/[\\/]/).at(-1).split('.')[0]);
	if (locales.includes(locale)) fileRoutes.set(resolve(indexFile), { locale, route: 'index' });
}
const exactLinks = new Map();
const tokenLinks = new Map();
const sourceForRecord = (record) => [...record.sourceUrls, ...(record.routeMap?.sourceUrls ?? [])].filter(Boolean);
for (const record of routeEntries) {
	const target = { locale: record.locale, route: record.route, map: record.routeMap };
	for (const url of sourceForRecord(record)) exactLinks.set(normaliseUrl(url), target);
	if (record.docToken && !tokenLinks.has(`${record.locale}|${record.docToken}`)) tokenLinks.set(`${record.locale}|${record.docToken}`, target);
}
for (const mapEntry of mapping) {
	const target = routeEntries.find((record) => record.topicId === mapEntry.topicId && record.locale === mapEntry.locale);
	if (!target) continue;
	for (const url of mapEntry.sourceUrls) exactLinks.set(normaliseUrl(url), { locale: target.locale, route: target.route, map: mapEntry });
	if (mapEntry.docToken) tokenLinks.set(`${mapEntry.locale}|${mapEntry.docToken}`, { locale: target.locale, route: target.route, map: mapEntry });
}
// The two published indexes are not topic pages, but their document links are
// common navigation targets in the source copy. Resolve those links to the
// local bilingual home page instead of exposing the cloud source URL.
for (const indexFile of (await walk(resolve(contentRoot, 'indexes'))).filter((path) => /\.(md|mdx)$/.test(path))) {
	const locale = normaliseLocale(indexFile.split(/[\\/]/).at(-1).split('.')[0]);
	if (!locales.includes(locale)) continue;
	const indexSource = await readFile(indexFile, 'utf8');
	for (const sourceUrl of indexSource.match(/https?:\/\/[^)\s<>]+/g) ?? []) {
		if (!isFeishu(sourceUrl)) continue;
		const target = { locale, route: 'index', map: {} };
		exactLinks.set(normaliseUrl(sourceUrl), target);
		const token = docTokenFromUrl(sourceUrl);
		if (token) tokenLinks.set(`${locale}|${token}`, target);
	}
}

function resolveLink(rawUrl, locale) {
	let url;
	try { url = new URL(rawUrl, 'https://docs.counso.ai'); } catch { return rawUrl; }
	if (isFeishu(rawUrl)) {
		const exact = exactLinks.get(normaliseUrl(rawUrl));
		const tokenTarget = tokenLinks.get(`${locale}|${docTokenFromUrl(rawUrl)}`) ?? tokenLinks.get(`en|${docTokenFromUrl(rawUrl)}`);
		const target = exact ?? tokenTarget;
		if (!target) fail(`unmapped Feishu link in ${locale}: ${rawUrl}`);
		const anchor = target.map?.anchorMap?.[url.hash.replace(/^#/, '')] ?? target.map?.anchor ?? '';
		return localLink(target.locale, target.route, anchor);
	}
	if (url.hostname === 'docs.counso.ai' || url.hostname === 'docs.dust.tt') {
		const path = url.pathname.replace(/^\/+|\/+$/g, '');
		const parts = path.split('/');
		const linkLocale = locales.includes(normaliseLocale(parts[0])) ? normaliseLocale(parts.shift()) : locale;
		const route = parts.join('/') || 'index';
		const owner = routeOwners.get(aliasKey(linkLocale, route)) ?? aliasOwners.get(aliasKey(linkLocale, route));
		if (owner) {
			const target = routeEntries.find((record) => `${record.topicId}|${record.locale}` === owner);
			return localLink(target.locale, target.route, url.hash.replace(/^#/, ''));
		}
		return localLink(linkLocale, route, url.hash.replace(/^#/, ''));
	}
	if (rawUrl.startsWith('/')) {
		const pieces = rawUrl.replace(/^\/+/, '').split('#');
		const linkLocale = locales.includes(normaliseLocale(pieces[0])) ? normaliseLocale(pieces.shift()) : locale;
		const route = pieces.shift() || 'index';
		const owner = routeOwners.get(aliasKey(linkLocale, route)) ?? aliasOwners.get(aliasKey(linkLocale, route));
		if (owner) {
			const target = routeEntries.find((record) => `${record.topicId}|${record.locale}` === owner);
			return localLink(target.locale, target.route, pieces[0] ?? '');
		}
	}
	return rawUrl;
}

function rewriteLinks(body, locale, sourcePath, sourceLabel) {
	const rewritten = body.replace(/(\]\()(<[^>]+>|[^)\s]+)(\))/g, (match, open, raw, close) => {
		const wrapped = raw.startsWith('<') && raw.endsWith('>');
		const target = wrapped ? raw.slice(1, -1) : raw;
		let converted = resolveLink(target, locale);
		if (!/^https?:\/\//i.test(target) && !target.startsWith('/') && /\.(?:md|mdx)(?:#.*)?$/i.test(target)) {
			const [relativePath, anchor = ''] = target.split('#');
			const sourceTarget = resolve(dirname(sourcePath), relativePath);
			const routeTarget = fileRoutes.get(sourceTarget);
			if (!routeTarget) fail(`unmapped relative Markdown link in ${sourceLabel}: ${target}`);
			converted = localLink(routeTarget.locale, routeTarget.route, anchor);
		}
		return `${open}${wrapped ? `<${converted}>` : converted}${close}`;
	});
	const dangling = rewritten.match(/https?:\/\/[^\s)<>]*(?:feishu|larksuite|larkoffice)[^\s)<>]*/i);
	if (dangling) fail(`unmapped Feishu URL remains in ${sourceLabel}: ${dangling[0]}`);
	return rewritten;
}

for (const file of await walk(publicRoot)) {
	// Root-level Markdown files are generated compatibility copies. Remove
	// them before writing the current set so a held or retired topic cannot
	// survive in public output after a rebuild.
	if (/\.md$/i.test(file)) await rm(file, { force: true });
}
await rm(docsRoot, { recursive: true, force: true });
await rm(resolve(publicRoot, 'en'), { recursive: true, force: true });
await rm(resolve(publicRoot, 'zh-cn'), { recursive: true, force: true });
await mkdir(docsRoot, { recursive: true });
await mkdir(generatedRoot, { recursive: true });

const canonicalPages = [];
for (const record of routeEntries) {
	const source = await readFile(record.sourcePath, 'utf8');
	const withMeta = withFrontmatter(source, record);
	const parsed = parseFrontmatter(withMeta);
	const body = rewriteLinks(parsed.body, record.locale, record.sourcePath, record.file);
	const rendered = `${withMeta.slice(0, withMeta.indexOf(parsed.body))}${body}\n`;
	const outputPath = resolve(docsRoot, record.locale, `${record.route}.md`);
	await mkdir(dirname(outputPath), { recursive: true });
	await writeFile(outputPath, rendered);
	const publicPath = resolve(publicRoot, record.locale, `${record.route}.md`);
	await mkdir(dirname(publicPath), { recursive: true });
	await writeFile(publicPath, `# ${record.title}\n\n${body}\n`);
	canonicalPages.push({ ...record, outputPath, publicPath });
	for (const alias of record.aliases) {
		if (alias === record.route) continue;
		const aliasPath = resolve(docsRoot, record.locale, `${alias}.md`);
		await mkdir(dirname(aliasPath), { recursive: true });
		const aliasRecord = { ...record, route: alias };
		await writeFile(aliasPath, withFrontmatter(`${withMeta.slice(0, withMeta.indexOf(parsed.body))}${body}\n`, aliasRecord, true));
	}
	// Unprefixed legacy addresses represent the historical English host. Keep
	// one deterministic root page while the locale-prefixed aliases cover both
	// languages.
	if (record.locale !== 'en') continue;
	for (const alias of record.rootAliases ?? []) {
		if (alias === record.route || alias === 'index') continue;
		const aliasPath = resolve(docsRoot, `${alias}.md`);
		await mkdir(dirname(aliasPath), { recursive: true });
		const aliasRecord = { ...record, route: alias };
		await writeFile(aliasPath, withFrontmatter(`${withMeta.slice(0, withMeta.indexOf(parsed.body))}${body}\n`, aliasRecord, true));
		const aliasPublicPath = resolve(publicRoot, `${alias}.md`);
		await mkdir(dirname(aliasPublicPath), { recursive: true });
		await writeFile(aliasPublicPath, `# ${record.title}\n\n${body}\n`);
	}
}

const groups = new Map();
for (const page of canonicalPages) {
	const group = page.route.split('/')[0];
	if (!groups.has(group)) groups.set(group, []);
}
const sidebar = [...groups.entries()].sort(([a], [b]) => a.localeCompare(b)).map(([group]) => {
	const [en, zh] = sectionTranslations[group] ?? [titleCase(group), titleCase(group)];
	return {
		label: en,
		translations: { en, 'zh-CN': zh },
		items: [{ autogenerate: { directory: group } }],
	};
});
await writeFile(resolve(generatedRoot, 'sidebar.mjs'), `// Generated from the release mapping.\nexport const sidebar = ${JSON.stringify(sidebar, null, 2)};\n`);

function homeSource(locale) {
	const isZh = locale === 'zh-cn';
	const title = isZh ? 'Counso AI 文档' : 'Counso AI documentation';
	const description = isZh ? '面向日常工作的清晰、可核对产品指南。' : 'Clear, source-backed guidance for everyday work.';
	const cta = isZh ? '进入 Counso AI' : 'Open Counso AI';
	const heading = isZh ? '从这里开始' : 'Start here';
	const groupsForHome = new Map();
	for (const page of canonicalPages.filter((item) => item.locale === locale)) {
		const group = page.route.split('/')[0];
		if (!groupsForHome.has(group)) groupsForHome.set(group, []);
		groupsForHome.get(group).push(page);
	}
	const lines = [
		'---',
		`title: ${yamlString(title)}`,
		`description: ${yamlString(description)}`,
		`topicId: "home"`,
		`contentRevision: "2026-09-11"`,
		'template: splash',
		'hero:',
		`  title: ${yamlString(title)}`,
		`  tagline: ${yamlString(description)}`,
		'---',
		'',
		"import AppEntry from '../../../components/AppEntry.astro';",
		'',
		`<AppEntry>${cta}</AppEntry>`,
		'',
		`## ${heading}`,
		'',
	];
	for (const [group, pages] of [...groupsForHome.entries()].sort(([a], [b]) => a.localeCompare(b))) {
		const translated = sectionTranslations[group]?.[isZh ? 1 : 0] ?? titleCase(group);
		const anchor = homeAnchorAliases[group]?.[isZh ? 1 : 0];
		if (anchor) lines.push(`<a id="${anchor}"></a>`);
		lines.push(`### ${translated}`, '');
		for (const page of pages.sort((a, b) => a.title.localeCompare(b.title))) lines.push(`- [${page.title}](${localLink(locale, page.route)})`);
		lines.push('');
	}
	return `${lines.join('\n')}\n`;
}
for (const locale of locales) {
	const path = resolve(docsRoot, locale, 'index.mdx');
	await mkdir(dirname(path), { recursive: true });
	await writeFile(path, homeSource(locale));
}

const siteUrl = (process.env.DOCS_SITE_URL ?? 'https://docs.counso.ai').replace(/\/$/, '');
const markdownEntries = canonicalPages.map((page) => ({
	topicId: page.topicId,
	title: page.title,
	locale: page.locale,
	route: page.route,
	file: relative(siteDir, page.outputPath).replace(/\\/g, '/'),
	hash: page.hash,
	aliases: page.aliases,
	rootAliases: page.rootAliases,
}));
const llms = [
	'# Counso AI documentation',
	'',
	'> Product guides in English and Simplified Chinese. Each link is a local rendered Markdown copy.',
	'',
	...canonicalPages.sort((a, b) => `${a.locale}/${a.route}`.localeCompare(`${b.locale}/${b.route}`)).map((page) => `- [${page.title}](${siteUrl}${localLink(page.locale, page.route)}.md)`),
	'',
].join('\n');
await writeFile(resolve(publicRoot, 'llms.txt'), llms);
const urls = canonicalPages.map((page) => `${siteUrl}${localLink(page.locale, page.route)}`);
const xmlEscape = (value) => value.replace(/[&<>"']/g, (character) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&apos;' }[character]));
await writeFile(resolve(publicRoot, 'sitemap.xml'), [
	'<?xml version="1.0" encoding="UTF-8"?>',
	'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
	...urls.map((url) => `  <url><loc>${xmlEscape(url)}</loc></url>`),
	'</urlset>',
	'',
].join('\n'));
await writeFile(resolve(publicRoot, 'release-manifest.json'), JSON.stringify({
	schemaVersion: 2,
	product: 'Counso AI',
	generatedAt: new Date().toISOString(),
	locales,
	topicCount: topicIds.size,
	pageCount: canonicalPages.length,
	pages: markdownEntries,
}, null, 2) + '\n');
console.log(`[counso release] generated ${topicIds.size} topics, ${canonicalPages.length} canonical pages, ${mapping.length} mapping records`);
