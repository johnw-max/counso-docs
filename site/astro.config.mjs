// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { sidebar } from './src/generated/sidebar.mjs';

const docsSiteUrl = process.env.DOCS_SITE_URL ?? 'https://docs.counso.ai';

export default defineConfig({
	site: docsSiteUrl,
	integrations: [
		starlight({
			title: {
				en: 'Counso AI documentation',
				'zh-CN': 'Counso AI 文档',
			},
			description: 'Product documentation for Counso AI.',
			defaultLocale: 'en',
			locales: {
				en: { label: 'English', lang: 'en' },
				'zh-cn': { label: '简体中文', lang: 'zh-CN' },
			},
			pagefind: true,
			disable404Route: true,
			customCss: ['./src/styles/custom.css'],
			sidebar,
		}),
	],
});
