#!/usr/bin/env python3
"""Validate source coverage, translations, routes, hashes, and Markdown links."""
import argparse
import hashlib
import json
import re
import sys
import urllib.parse
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--update-hashes", action="store_true", help="Refresh translation hashes after all other checks pass")
args = parser.parse_args()
errors = []
def require(condition, message):
    if not condition:
        errors.append(message)
def read_json(path):
    return json.loads((ROOT / path).read_text())
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def branded_path(path):
    return re.sub(r'(?<![A-Za-z0-9])dust(?![A-Za-z0-9])', 'counso', path, flags=re.I)
def check_title(file, entry):
    headings = re.findall(r'^# (.+)$', file.read_text(), re.M)
    require(len(headings) == 1 and entry.get('title') == headings[0], 'Display title differs from article: ' + str(file.relative_to(ROOT)))
def strip_code(text):
    return re.sub(r'^\s*(```|~~~).*?^\s*\1\s*$', '', text, flags=re.M | re.S)
def anchors(text):
    names = set(re.findall(r'<(?:a|span)\s+(?:id|name)=[\'"]([^\'"]+)', text))
    counts = Counter()
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', strip_code(text), re.M):
        clean = re.sub(r'<[^>]+>', '', heading)
        clean = re.sub(r'\[([^]]+)\]\([^)]+\)', r'\1', clean)
        clean = re.sub(r'[^\w\-\s]', '', clean.lower()).replace(' ', '-')
        suffix = '' if counts[clean] == 0 else '-' + str(counts[clean])
        counts[clean] += 1
        names.add(clean + suffix)
    return names

data = read_json('translations.json')
index = read_json('source/url-index.json')
manifest = read_json('source/manifest.json')
source_titles = {r['path']: r['title'] for r in manifest}
require(data['schema_version'] == 3, 'Unexpected mapping version')
require(data['publication'].get('route_policy') == 'counso-brand-slugs-with-legacy-redirects', 'Unexpected route policy')
rows = data['pages']
status_counts = Counter(r['status'] for r in rows)
require(set(status_counts) <= {'publish', 'exclude_api', 'exclude_upstream', 'updating'}, 'Unknown publication status')
require(data['counts'] == {'source_files': len(rows), 'sitemap_urls': sum(r['in_sitemap'] for r in rows), **dict(status_counts)}, 'Publication counts differ from page records')
require(len(rows) == len(manifest), 'Source manifest count mismatch')
require(len({r['original_file'] for r in rows}) == len(rows), 'Duplicate original file')
require({r['original_repository_path'] for r in rows} == {r['path'] for r in manifest}, 'Source manifest paths differ')
sitemap = ET.parse(ROOT / 'source/sitemap.xml')
urls = {e.text for e in sitemap.iter() if e.tag.endswith('}loc')}
require(urls == set(index['routes']), 'Source sitemap and URL index differ')
require(urls == {r['original_url'] for r in rows if r['in_sitemap']}, 'Sitemap URL missing from translations')
require(digest(ROOT / 'source/sitemap.xml') == index['source']['sitemap_sha256'], 'Source sitemap hash changed')
expected = set()
notice_files = set()
notice_routes = set()
routes = {}
for row in rows:
    path = row['original_repository_path']
    original = ROOT / row['original_file']
    require(row.get('original_title') == source_titles.get(path), 'Original title differs from source manifest: ' + path)
    require(row['original_file'] == 'source/' + path, 'Original path changed: ' + path)
    require(original.is_file(), 'Original file missing: ' + path)
    if original.is_file():
        require(digest(original) == row['original_sha256'], 'Original hash changed: ' + path)
    if row['in_sitemap']:
        require(index['routes'].get(row['original_url']) == path, 'Peer URL mapping changed: ' + path)
    translations = row['translations']
    if row['status'] == 'updating':
        require(translations is None, 'Updating page must not claim a completed translation: ' + path)
        notice = row.get('notice', {})
        require(set(notice) == {'en', 'zh-cn'}, 'Missing notice language: ' + path)
        require(row['in_sitemap'], 'Notice needs an original page URL: ' + path)
        for lang, t in notice.items():
            require(t['file'] == lang + '/UPDATING.md', 'Unexpected notice file: ' + path)
            file = ROOT / t['file']
            notice_files.add(t['file'])
            require(file.is_file(), 'Notice file missing: ' + t['file'])
            canonical = branded_path(urllib.parse.urlparse(row['original_url']).path)
            require(t['route'] == (canonical if lang == 'en' else '/zh-cn' + canonical), 'Unexpected notice route: ' + path)
            require(t['route'] not in routes, 'Duplicate notice route: ' + t['route'])
            routes[t['route']] = t['file']
            notice_routes.add(t['route'])
            if file.is_file():
                check_title(file, t)
                if args.update_hashes:
                    t['sha256'] = digest(file)
                else:
                    require(digest(file) == t['sha256'], 'Notice hash stale: ' + t['file'])
        continue
    if row['status'] != 'publish':
        require(translations is None and bool(row['reason']), 'Excluded source requires a reason and no translations: ' + path)
        require('notice' not in row, 'Excluded source must not promise an update: ' + path)
        continue
    require('notice' not in row, 'Published article still contains a notice: ' + path)
    require(set(translations) == {'en', 'zh-cn'}, 'Missing language: ' + path)
    for lang, t in translations.items():
        file = ROOT / t['file']
        expected.add(t['file'])
        require(t['file'] == lang + '/' + branded_path(path), 'Unexpected translation path: ' + path)
        require(file.is_file(), 'Translation missing: ' + t['file'])
        canonical = branded_path(urllib.parse.urlparse(row['original_url']).path)
        require(t['route'] == (canonical if lang == 'en' else '/zh-cn' + canonical), 'Unexpected route: ' + t['route'])
        require(t['route'] not in routes, 'Duplicate published route: ' + t['route'])
        routes[t['route']] = t['file']
        if file.is_file():
            check_title(file, t)
            if args.update_hashes:
                t['sha256'] = digest(file)
            else:
                require(digest(file) == t['sha256'], 'Translation hash stale: ' + t['file'])
actual = {str(f.relative_to(ROOT)) for lang in ['en', 'zh-cn'] for f in (ROOT / lang).rglob('*.md') if f.name != 'SUMMARY.md'}
require(actual == expected | notice_files, 'Unexpected or missing Markdown: ' + str(sorted(actual ^ (expected | notice_files))))
redirects = read_json('redirects.json')
seen = set()
for r in redirects['redirects']:
    require(r['from'] not in seen, 'Duplicate redirect: ' + r['from'])
    require(r['to'] in routes, 'Redirect destination absent: ' + r['to'])
    require(r['from'] not in routes, 'Redirect shadows article: ' + r['from'])
    seen.add(r['from'])
redirect_targets = {r['from']: r['to'] for r in redirects['redirects']}
for row in rows:
    if row['status'] not in {'publish', 'updating'}:
        continue
    entries = row['translations'] if row['status'] == 'publish' else row['notice']
    original_path = urllib.parse.urlparse(row['original_url']).path
    for lang, entry in entries.items():
        old_route = original_path if lang == 'en' else '/zh-cn' + original_path
        if old_route != entry['route']:
            require(redirect_targets.get(old_route) == entry['route'], 'Missing legacy brand redirect: ' + old_route)
        require(entry['route'] == branded_path(entry['route']), 'Old brand in published route: ' + entry['route'])

link_count = 0
all_files = sorted(expected | notice_files | {'en/SUMMARY.md', 'zh-cn/SUMMARY.md', 'README.md', 'PUBLICATION-STATUS.md'})
for rel in all_files:
    file = ROOT / rel
    require(file.is_file(), 'Missing index: ' + rel)
    if not file.is_file():
        continue
    text = file.read_text()
    require(len(re.findall(r'^# ', text, re.M)) == 1, 'Expected one main heading: ' + rel)
    if rel not in {'README.md', 'PUBLICATION-STATUS.md'}:
        visible = re.sub(r'\]\([^)]*\)', ']', text)
        require(not re.search(r'\bdust\b|\baduster\b|未部署|飞书|Feishu|TODO|TBD|整改安排|需要适配|待适配|hold_integration|upstream implementation', visible, re.I), 'Brand or scaffolding in copy: ' + rel)
        require(not re.search(r'https?://(?:[^/\s]+\.)?dust\.tt', text), 'Upstream product link in copy: ' + rel)
    for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^\s)]+)(?:\s+"[^"]*")?\)', strip_code(text)):
        parsed = urllib.parse.urlparse(target.strip('<>'))
        if parsed.scheme or parsed.netloc:
            continue
        link_count += 1
        require(not parsed.path.startswith('/'), 'Use relative Markdown links: ' + rel + ' → ' + target)
        linked = (file.parent / urllib.parse.unquote(parsed.path)).resolve() if parsed.path else file
        require(linked.is_relative_to(ROOT), 'Link leaves repository: ' + rel + ' → ' + target)
        require(linked.exists(), 'Broken file link: ' + rel + ' → ' + target)
        if linked.is_relative_to(ROOT) and (rel in {'en/SUMMARY.md', 'zh-cn/SUMMARY.md'} or rel in expected):
            require(str(linked.relative_to(ROOT)) not in notice_files, 'Unreleased capability linked from user documentation: ' + rel)
        if parsed.fragment and linked.is_file() and linked.suffix == '.md':
            require(urllib.parse.unquote(parsed.fragment) in anchors(linked.read_text()), 'Broken anchor: ' + rel + ' → ' + target)
status_text = (ROOT / 'PUBLICATION-STATUS.md').read_text()
listed_urls = re.findall(r'^\|[^\n]*\| \[(https?://[^\]]+)\]\(', status_text, re.M)
require(Counter(listed_urls) == Counter(r['original_url'] for r in rows if r['status'] != 'publish'), 'Unpublished URL inventory differs from mapping')
summary = {'source_files': len(rows), 'sitemap_urls': len(urls), 'published_pairs': len(expected) // 2, 'language_files': len(expected), 'published_routes': len(routes) - len(notice_routes), 'updating_pages': len(notice_routes) // 2, 'notice_routes': len(notice_routes), 'redirects': len(seen), 'relative_links_checked': link_count, 'errors': errors}
if args.update_hashes and not errors:
    temporary = ROOT / '.translations.json.tmp'
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    temporary.replace(ROOT / 'translations.json')
print(json.dumps(summary, ensure_ascii=False, indent=2))
sys.exit(bool(errors))
