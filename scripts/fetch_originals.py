#!/usr/bin/env python3
"""Optionally restore the original reference files from their fixed snapshot."""
import concurrent.futures
import hashlib
import json
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]


def fetch(row):
    destination = ROOT / row['originalFile']
    if destination.is_file() and hashlib.sha256(destination.read_bytes()).hexdigest() == row['sha256']:
        return 'present'
    request = Request(row['snapshotDownloadUrl'], headers={'User-Agent': 'Counso-Docs-source-restore'})
    with urlopen(request, timeout=60) as response:
        body = response.read()
    if hashlib.sha256(body).hexdigest() != row['sha256']:
        raise ValueError(f"Source checksum differs: {row['originalUrl']}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_suffix(destination.suffix + '.download')
    temporary.write_bytes(body)
    temporary.replace(destination)
    return 'restored'


if __name__ == '__main__':
    rows = json.loads((ROOT / 'reference/url-to-original.json').read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(fetch, rows))
    print(f"Verified {len(results)} source files; restored {results.count('restored')}.")
