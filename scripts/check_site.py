#!/usr/bin/env python3
"""Check generated documentation links and fragments without network access."""
import argparse
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.canonical = set(), [], []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if tag == 'a' and attrs.get('name'):
            self.ids.add(attrs['name'])
        if tag == 'a' and attrs.get('href'):
            self.links.append(attrs['href'])
        if tag in ('img', 'script', 'source') and attrs.get('src'):
            self.links.append(attrs['src'])
        if tag == 'link' and attrs.get('href') and attrs.get('rel') in ('stylesheet', 'icon', 'modulepreload', 'preload'):
            self.links.append(attrs['href'])
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical.append(attrs.get('href', ''))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dist', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    root = args.dist.resolve()
    pages = {p: Page(p.read_text()) for p in root.rglob('*.html')}
    errors, checked, external, legacy = [], 0, set(), set()
    for file, page in pages.items():
        path = '/' + file.relative_to(root).as_posix()
        if path.endswith('/index.html'):
            path = path[:-10]
        base = 'https://docs.counso.ai' + path
        for href in page.links:
            url = urlsplit(urljoin(base, href))
            if url.scheme not in ('http', 'https'):
                continue
            if url.netloc != 'docs.counso.ai':
                external.add(url.netloc)
                if url.netloc in ('docs.dust.tt', 'dust.tt', 'app.dust.tt'):
                    legacy.add(href)
                continue
            requested = root / unquote(url.path).lstrip('/')
            candidates = [requested, requested / 'index.html']
            if not requested.suffix:
                candidates.append(requested.with_suffix('.html'))
            target = next((p for p in candidates if p.is_file()), None)
            checked += 1
            if target is None:
                errors.append({'from': path, 'href': href, 'reason': 'missing file'})
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append({'from': path, 'href': href, 'reason': 'missing fragment'})
    result = {
        'htmlFiles': len(pages), 'internalLinksChecked': checked,
        'brokenLinks': errors, 'externalHosts': sorted(external),
        'upstreamDocumentationLinks': sorted(legacy),
    }
    if args.output:
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(1 if errors else 0)


if __name__ == '__main__':
    main()
