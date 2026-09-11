import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const siteDir = resolve(fileURLToPath(new URL('.', import.meta.url)), '..');
const distRoot = resolve(siteDir, 'dist');
const manifest = JSON.parse(await readFile(resolve(distRoot, 'release-manifest.json'), 'utf8'));

// Astro treats a Markdown file named index.md as the directory index. A few
// historical hosts also address that same page as /path/index. Materialise
// that spelling in the static output so nginx and object-storage hosts agree.
for (const page of manifest.pages ?? []) {
	for (const alias of page.aliases ?? []) {
		if (!alias.endsWith('/index')) continue;
		const localeSource = resolve(distRoot, page.locale, `${alias.slice(0, -6)}/index.html`);
		const localeTarget = resolve(distRoot, page.locale, `${alias}/index.html`);
		try {
			const html = await readFile(localeSource);
			await mkdir(dirname(localeTarget), { recursive: true });
			await writeFile(localeTarget, html);
		} catch {
			// The source route may already have been emitted by Astro; check-release
			// reports a missing target if neither spelling exists.
		}
	}
	for (const alias of page.rootAliases ?? []) {
		if (!alias.endsWith('/index')) continue;
		const source = resolve(distRoot, `${alias.slice(0, -6)}/index.html`);
		const target = resolve(distRoot, `${alias}/index.html`);
		try {
			const html = await readFile(source);
			await mkdir(dirname(target), { recursive: true });
			await writeFile(target, html);
		} catch {
			// See the locale-prefixed branch above.
		}
	}
}
console.log('[counso release] materialised legacy /index compatibility paths');
