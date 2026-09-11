#!/usr/bin/env python3
"""Refresh local Markdown metadata before generating routes and the website."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
content = ROOT / 'content'
for name, collection in [('manifest.json', 'topics'), ('additions-manifest.json', None)]:
    file = content / name
    document = json.loads(file.read_text())
    rows = document[collection] if collection else document
    for row in rows:
        if row.get('publicationStatus') == 'hold_api':
            continue
        source = content / row['file']
        body = source.read_bytes()
        title = next((line[2:].strip() for line in body.decode().splitlines() if line.startswith('# ')), None)
        if title:
            row['title'] = title
        field = 'sha256' if collection else 'hash'
        row[field] = hashlib.sha256(body).hexdigest()
    if collection:
        document['source'] = {'provider': 'local-markdown', 'maintenance': 'Markdown files in this repository are the maintained source.'}
    file.write_text(json.dumps(document, ensure_ascii=False, indent=2) + '\n')
print('Updated local Markdown titles and checksums.')
