#!/usr/bin/env python3
"""Build the Counso documentation route ledger.

The script only reads source snapshots.  It emits a route ledger that keeps
the acquired Dust URL (including aliases and fragments) attached to its
original bytes while separately describing the reviewed Counso target.  A
target is never inferred from a title alone: the reviewed legacy URL table or
an explicitly listed delivery addition must provide it.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = PACKAGE_ROOT / "reference/original/manifest-final.json"
DEFAULT_URL_INDEX = PACKAGE_ROOT / "reference/url-to-original.json"
DEFAULT_CONTENT_MANIFEST = PACKAGE_ROOT / "content/manifest.json"
DEFAULT_TOPICS = DEFAULT_CONTENT_MANIFEST
DEFAULT_CROSSCHECK = PACKAGE_ROOT / "mapping/inputs/source-crosscheck.json"
DEFAULT_ATTACHMENT = PACKAGE_ROOT / "mapping/inputs/application-legacy-urls.txt"
DEFAULT_ADDITIONS = PACKAGE_ROOT / "content/additions-manifest.json"
DEFAULT_RELEASE_POLICY = PACKAGE_ROOT / "content/release-policy.json"


# The section ids are deliberately locale-neutral.  The site can resolve the
# displayed heading in each language, while redirect consumers can use these
# ids as stable compatibility anchors.  These cover every provider section
# used by the reviewed legacy tool entries.
TARGETS: dict[str, dict] = {
    "/developers": {"topic": "developers/overview", "section": "steps"},
    "/docs/ashby-mcp": {"topic": "integrations/tools-catalog", "section": "ashby"},
    "/docs/bigquery": {"topic": "integrations/data-platforms", "section": "bigquery-connection"},
    "/docs/client-side-mcp-server": {"topic": "developers/client-side-mcp", "section": "steps"},
    "/docs/confluence-connection": {"topic": "integrations/confluence", "section": "confluence-connection"},
    "/docs/confluence-tool": {"topic": "integrations/confluence", "section": "confluence-tool"},
    "/docs/context-compaction": {"topic": "agents/context-and-compaction", "section": "compact-and-continue-the-same-task"},
    "/docs/credit-management": {"topic": "administration/usage-and-seats", "section": "check-credits-and-run-consumption", "partial": True},
    "/docs/credits": {"topic": "administration/usage-and-seats", "section": "check-credits-and-run-consumption", "partial": True},
    "/docs/data": {"topic": "agents/data-and-access", "section": "set-the-smallest-useful-scope", "related": [{"topic": "integrations/connections-and-tools", "section": "understand-refresh-and-access"}]},
    "/docs/databricks": {"topic": "integrations/data-platforms", "section": "databricks-sql-and-genie-tools"},
    "/docs/dust-in-teams": {"topic": "integrations/channels", "section": "microsoft-teams"},
    "/docs/email-agents": {"topic": "integrations/channels", "section": "email-agents"},
    "/docs/filter-webhooks-payload": {"topic": "automations/filters-and-limits", "section": "write-a-filter"},
    "/docs/freshservice": {"topic": "integrations/tools-catalog", "section": "freshservice"},
    "/docs/front-mcp": {"topic": "integrations/tools-catalog", "section": "front"},
    "/docs/github-connection": {"topic": "integrations/tools-catalog", "section": "github"},
    "/docs/gmail": {"topic": "integrations/google", "section": "gmail-and-calendar-tools"},
    "/docs/gong-connection": {"topic": "integrations/gong", "section": "gong-connection"},
    "/docs/gong-mcp": {"topic": "integrations/gong", "section": "gong-tool"},
    "/docs/google-calendar": {"topic": "integrations/google", "section": "gmail-and-calendar-tools"},
    "/docs/google-drive": {"topic": "integrations/google", "section": "google-drive-connection"},
    "/docs/google-drive-connection": {"topic": "integrations/google", "section": "google-drive-connection"},
    "/docs/google-sheets": {"topic": "integrations/google", "section": "google-drive-and-sheets-tool", "partial": True},
    "/docs/hubspot": {"topic": "integrations/tools-catalog", "section": "hubspot"},
    "/docs/intercom-connection": {"topic": "integrations/tools-catalog", "section": "intercom"},
    "/docs/intro": {"topic": "getting-started/introduction", "section": "start-at-the-application"},
    "/docs/jira": {"topic": "integrations/tools-catalog", "section": "jira"},
    "/docs/knowledge": {"topic": "knowledge/overview", "section": "knowledge-is-a-source-not-a-conclusion"},
    "/docs/microsoft-connection": {"topic": "integrations/microsoft", "section": "microsoft-connection"},
    "/docs/microsoft-drive-tool-setup": {"topic": "integrations/microsoft", "section": "sharepoint-onedrive-and-excel-tools"},
    "/docs/microsoft-teams-tool-setup": {"topic": "integrations/microsoft", "section": "teams-tool-and-teams-bot"},
    "/docs/monday": {"topic": "integrations/tools-catalog", "section": "monday"},
    "/docs/netsuite": {"topic": "integrations/netsuite", "section": "configure-netsuite"},
    "/docs/notion-connection": {"topic": "integrations/notion", "section": "notion-connection"},
    "/docs/notion-mcp": {"topic": "integrations/notion", "section": "notion-tool"},
    "/docs/outlook-tool-setup": {"topic": "integrations/microsoft", "section": "outlook"},
    "/docs/personal-vs-workspace-credentials-for-tools-mcp-servers": {"topic": "integrations/personal-and-shared", "section": "personal-credentials"},
    "/docs/power-bi": {"topic": "integrations/power-bi", "section": "add-the-tool"},
    "/docs/productboard": {"topic": "integrations/tools-catalog", "section": "productboard"},
    "/docs/programmatic-usage": {"topic": "administration/usage-and-seats", "section": "check-credits-and-run-consumption", "partial": True},
    "/docs/remote-mcp-server": {"topic": "integrations/remote-mcp", "section": "add-the-server"},
    "/docs/salesforce": {"topic": "integrations/tools-catalog", "section": "salesforce"},
    "/docs/salesloft-mcp": {"topic": "integrations/tools-catalog", "section": "salesloft"},
    "/docs/scheduling-your-agent-beta": {"topic": "automations/schedules", "section": "create-a-schedule"},
    "/docs/seat-management": {"topic": "administration/usage-and-seats", "section": "check-members-and-seats", "partial": True},
    "/docs/self-improving-skills": {"topic": "skills/improve", "section": "review-and-apply-an-improvement", "partial": True},
    "/docs/skills": {"topic": "skills/overview", "section": "when-a-skill-helps", "related": [{"topic": "skills/create-and-configure", "section": "create-a-skill"}, {"topic": "skills/access-and-versions", "section": "set-access-and-review-history"}]},
    "/docs/slab-mcp": {"topic": "integrations/tools-catalog", "section": "slab"},
    "/docs/slack": {"topic": "integrations/slack", "section": "slack-workflows-and-channel-apps"},
    "/docs/slack-connection": {"topic": "integrations/slack", "section": "slack-connection-synchronized-messages"},
    "/docs/slack-mcp": {"topic": "integrations/slack", "section": "slack-tool-personal-actions"},
    "/docs/snowflake-connection": {"topic": "integrations/data-platforms", "section": "snowflake-connection"},
    "/docs/snowflake-tool": {"topic": "integrations/data-platforms", "section": "snowflake-tool"},
    "/docs/statuspage-mcp": {"topic": "integrations/tools-catalog", "section": "statuspage"},
    "/docs/structured-output-format": {"topic": "agents/structured-output", "section": "steps"},
    "/docs/subscriptions": {"topic": "administration/usage-and-seats", "section": "change-a-subscription-or-stop-renewal", "partial": True},
    "/docs/triggers": {"topic": "automations/schedules", "section": "create-a-schedule"},
    "/docs/ukg-ready": {"topic": "integrations/tools-catalog", "section": "ukg-ready"},
    "/docs/understanding-llms-context-windows": {"topic": "agents/context-and-compaction", "section": "inspect-context-usage", "partial": True},
    "/docs/use-cases": {"topic": "guides/knowledge-work", "section": "before-you-begin", "partial": True},
    "/docs/user-documentation/agents/model-selection": {"topic": "agents/model-selection", "section": "steps"},
    "/docs/user-documentation/agents/triggers/credits-usage": {"topic": "automations/filters-and-limits", "section": "understand-limits-and-credits", "partial": True},
    "/docs/user-documentation/pods/overview": {"topic": "pods/overview", "section": "create-and-orient-yourself-in-a-pod"},
    "/docs/val-town": {"topic": "integrations/tools-catalog", "section": "val-town"},
    "/docs/vanta": {"topic": "integrations/tools-catalog", "section": "vanta"},
    "/docs/website-connection": {"topic": "integrations/connections-and-tools", "section": "websites-and-folders"},
    "/docs/zendesk-connection": {"topic": "integrations/tools-catalog", "section": "zendesk"},
    "/reference/developer-platform-overview": {"topic": "developers/overview", "section": "steps"},
}

# The three legacy reference routes intentionally receive new, separately
# authored pages.  The source response observed for these routes was often
# GetCurrentUser; it is retained as a source match but never treated as the
# semantic Apps source.
ADDED_TARGETS: dict[str, dict] = {
    "/reference": {"topic": "developers/api-reference", "section": "choose-an-integration", "observed_current_user": True},
    "/reference/introduction-to-dust-apps": {"topic": "developers/legacy-apps", "section": "understand-the-saved-workflow", "observed_current_user": True},
    "/reference/post_api-v1-w-wid-vaults-vid-apps-aid-runs": {"topic": "developers/app-runs", "section": "create-a-run", "observed_current_user": True},
    "/runs": {"topic": "developers/app-runs", "section": "create-a-run", "observed_current_user": False},
}

APP_RUN_TARGETS = {
    "https://docs.dust.tt/api-reference/apps/create-an-app-run": {"topic": "developers/app-runs", "section": "create-a-run"},
    "https://docs.dust.tt/api-reference/apps/get-an-app-run": {"topic": "developers/app-runs", "section": "retrieve-and-check-the-result"},
    "https://docs.dust.tt/api-reference/apps/list-apps": {"topic": "developers/app-runs", "section": "routes"},
    "https://docs.dust.tt/docs/developer-platform/legacy-dust-apps/what-is-a-dust-app": {"topic": "developers/legacy-apps", "section": "understand-the-saved-workflow"},
    "https://docs.dust.tt/docs/developer-platform/legacy-dust-apps/dust-apps-core-concepts": {"topic": "developers/legacy-apps", "section": "understand-the-saved-workflow"},
}


def load(path: Path):
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def split_url(url: str) -> tuple[str, str, str]:
    p = urlsplit(url)
    path = p.path or "/"
    fragment = p.fragment or None
    # URL fragments are not sent to the server.  Keep the exact fragment in
    # the ledger, while using path-only matching for semantic aliases.
    clean = urlunsplit((p.scheme, p.netloc, path, p.query, ""))
    return clean, path, fragment


def path_key(url: str) -> str:
    _, path, _ = split_url(url)
    if path.endswith("/") and path != "/":
        path = path[:-1]
    return path


def read_topics(path: Path) -> dict[tuple[str, str], dict]:
    result = {}
    if not path.exists():
        return result
    raw = load(path)
    items = raw.get("topics", []) if isinstance(raw, dict) else raw
    for item in items:
        result[(item["topicId"], item["locale"])] = item
    return result


def read_additions(path: Path) -> dict[tuple[str, str], dict]:
    result = {}
    if not path.exists():
        return result
    for item in load(path):
        result[(item["topicId"], item["locale"])] = item
    return result


def read_publication_policy(
    content_manifest_path: Path,
    additions_path: Path,
    release_policy_path: Path,
) -> dict:
    """Read the package publication hold before resolving any target.

    The release policy is authoritative when present.  The content and
    additions manifests also carry per-topic ``publicationStatus`` values so
    a rebuild remains safe if the policy file is regenerated separately.
    """
    content_raw = load(content_manifest_path) if content_manifest_path.exists() else {}
    additions_raw = load(additions_path) if additions_path.exists() else []
    policy = load(release_policy_path) if release_policy_path.exists() else {}
    manifest_items = content_raw.get("topics", []) if isinstance(content_raw, dict) else []
    manifest_items = [*manifest_items, *(additions_raw if isinstance(additions_raw, list) else [])]
    held_topic_ids = {
        item.get("topicId")
        for item in manifest_items
        if item.get("topicId") and item.get("publicationStatus") == "hold_api"
    }
    manifest_statuses = sorted({item.get("publicationStatus") for item in manifest_items if item.get("publicationStatus")})
    prefixes = [p for p in policy.get("excludedTopicPrefixes", []) if isinstance(p, str)]
    original_paths = [p for p in policy.get("excludedOriginalPaths", []) if isinstance(p, str)]
    # A policy prefix is authoritative.  The manifest status is retained as
    # evidence and is also enough to keep held topics excluded if a policy
    # file is absent in an older package.
    hold_api = bool(prefixes) or "hold_api" in manifest_statuses
    return {
        "publicationStatus": "hold_api" if hold_api else "publish",
        "holdApi": hold_api,
        "excludedTopicPrefixes": prefixes,
        "excludedOriginalPaths": original_paths,
        "heldTopicIds": sorted(held_topic_ids),
        "manifestStatuses": manifest_statuses,
        "policyFilePresent": release_policy_path.exists(),
        "reason": policy.get("reason") or "API 文档暂不发布。" if hold_api else None,
        "reasonEn": policy.get("reasonEn") or "API documentation is not included in this release." if hold_api else None,
    }


def is_api_held(topic: str | None, path: str, publication: dict) -> bool:
    """Return whether this route's authored destination is held from release."""
    if path in publication.get("excludedOriginalPaths", []):
        return True
    if not topic:
        return False
    if topic in publication.get("heldTopicIds", []):
        return True
    return any(topic.startswith(prefix) for prefix in publication.get("excludedTopicPrefixes", []))


def read_attachment_urls(path: Path) -> list[str]:
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    urls = re.findall(r"https?://[^\s`|)]+", text)
    # The requested application list is the contiguous docs.counso.ai block
    # in the attachment.  Assets, blog images and marketing URLs are outside
    # this route ledger.
    return list(dict.fromkeys(u.rstrip(".,") for u in urls if urlsplit(u).netloc == "docs.counso.ai"))


def source_file_map(url_index_path: Path) -> dict[str, dict]:
    result = {}
    if not url_index_path.exists():
        return result
    for item in load(url_index_path):
        result[item["recordId"]] = item
    return result


def section_for_target(target: dict, locale: str, topics: dict, additions: dict) -> dict:
    topic = target["topic"]
    source = topics.get((topic, locale)) or additions.get((topic, locale))
    section_id = target.get("section")
    source_file = (source or {}).get("file")
    if source_file and not source_file.startswith("content/"):
        source_file = f"content/{source_file}"
    item = {
        "topicId": topic,
        # The alias is injected by the site build into both locale pages.  It
        # avoids pretending that an English slug is automatically a valid
        # Chinese heading slug while keeping redirects stable.
        "section": {
            "alias": section_id,
            "anchor": section_id,
            "anchorStrategy": "stable_alias",
        },
        "url": f"https://docs.counso.ai/{locale}/{topic}/",
        "file": source_file or f"content/topics/{locale}/{topic}.md",
    }
    target_hash = (source or {}).get("hash") or (source or {}).get("sha256")
    if target_hash:
        item["targetHash"] = target_hash
    elif source and source.get("path"):
        source_file = Path(source["path"])
        if source_file.exists():
            item["targetHash"] = sha256(source_file)
    if target.get("related"):
        item["related"] = [
            section_for_target({"topic": r["topic"], "section": r["section"]}, locale, topics, additions)
            for r in target["related"]
        ]
    return item


def reason_for_archive(record: dict, cross: dict | None) -> tuple[str, str]:
    if cross:
        status = cross.get("authoring_status")
        if status == "no_exact_archive_match":
            return "archive_only_no_exact_match", cross.get("reason") or "No exact archived source match was found."
        if status == "internal_api_hold":
            return "archive_only_internal_api", "The legacy route was observed as an internal GetCurrentUser response; retain the source match without treating it as an Apps article."
        if status == "upstream_service_specific_exclude":
            return "archive_only_upstream_claims", cross.get("reason") or "Commercial or upstream service claims need Counso-specific confirmation."
    if record.get("source_type") == "api":
        return "archive_only_api_contract", "Retain the acquired API snapshot for traceability; a Counso endpoint, authentication, error, and publication contract is not established."
    canonical = record.get("canonical_url", "")
    if "/api-reference/private" in canonical:
        return "archive_only_private_api_contract", "Retain the private API snapshot for traceability; it is an internal upstream contract and is not a public Counso reference."
    if "/api-reference/" in canonical or canonical.endswith(".json"):
        return "archive_only_api_contract", "Retain the acquired API reference for traceability; do not publish it as a Counso API without a verified contract."
    if "/deprecated/" in canonical or "legacy-dust-apps" in canonical:
        return "archive_only_upstream_deprecated", "The upstream page is deprecated or service-specific and has no approved Counso rewrite target."
    return "archive_only_no_reviewed_rewrite", "No reviewed Counso rewrite target exists for this source page; keep the original archive and hide the legacy help entry until a specific article is authored."


def target_status(target: dict, cross: dict | None, source_type: str, legacy: bool = False) -> tuple[str, str]:
    if legacy:
        if target.get("observed_current_user"):
            return "legacy_alias_to_topic", "The old route was observed as GetCurrentUser or an outdated Apps page; serve the authored Counso topic while keeping the observed source match explicit."
        return "legacy_alias_to_topic", "Serve the old English path through the authored Counso topic and preserve any incoming fragment."
    if source_type == "api":
        return "archive_only_api_contract", "The source is an API snapshot; the authored topic is not an endpoint contract."
    if cross:
        status = cross.get("authoring_status")
        if status == "covered_by_local_draft":
            return "mapped_to_counso_draft", "A reviewed Counso draft covers this source topic."
        if status == "upstream_service_specific_exclude":
            return "mapped_partial_upstream_claims_excluded", "The Counso article keeps the operational topic but excludes unverified upstream pricing, privacy, support, or retention claims."
        if status == "needs_product_verification":
            return "mapped_to_counso_draft_needs_product_verification", "A reviewed Counso draft exists, but provider availability, permissions, and online behavior still require product verification."
    return "mapped_to_counso_addition", "An explicitly authored Counso delivery addition provides the target article."


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--url-index", type=Path, default=DEFAULT_URL_INDEX)
    parser.add_argument("--topics", type=Path, default=DEFAULT_CONTENT_MANIFEST if DEFAULT_CONTENT_MANIFEST.exists() else DEFAULT_TOPICS)
    parser.add_argument("--crosscheck", type=Path, default=DEFAULT_CROSSCHECK)
    parser.add_argument("--attachment", type=Path, default=DEFAULT_ATTACHMENT)
    parser.add_argument("--additions", type=Path, default=DEFAULT_ADDITIONS)
    parser.add_argument("--release-policy", type=Path, default=DEFAULT_RELEASE_POLICY)
    parser.add_argument("--output", type=Path, default=PACKAGE_ROOT / "mapping/routes.json")
    args = parser.parse_args()

    manifest = load(args.manifest)
    records = manifest["records"]
    records_by_id = {r["record_id"]: r for r in records}
    topics = read_topics(args.topics)
    additions = read_additions(args.additions)
    publication = read_publication_policy(args.topics, args.additions, args.release_policy)
    url_index = source_file_map(args.url_index)
    crosscheck_rows = load(args.crosscheck) if args.crosscheck.exists() else []
    cross_by_id = {r["archived_record"]: r for r in crosscheck_rows if r.get("archived_record")}
    cross_by_path = {path_key(r["original_url"]): r for r in crosscheck_rows}
    app_urls = read_attachment_urls(args.attachment)
    app_urls = [u for u in app_urls if urlsplit(u).path in ("", "/") or urlsplit(u).path.startswith(("/docs/", "/reference", "/runs", "/developers"))]

    # Explicit source aliases are retained one-for-one.  A second index keeps
    # the source record reachable when an audited legacy URL is not present in
    # the sitemap or source_urls list.
    routes: list[dict] = []
    seen: set[tuple[str, str | None]] = set()
    source_url_index: dict[str, str] = {}
    for record in records:
        rid = record["record_id"]
        urls: list[tuple[str, str]] = []
        for url in [record.get("canonical_url"), *record.get("source_urls", []), *record.get("candidate_aliases", []), *record.get("sitemap_urls", [])]:
            if url:
                urls.append((url, "manifest"))
        for item in record.get("llms_entries", []):
            if item.get("url"):
                urls.append((item["url"], "llms"))
        for url, _ in urls:
            source_url_index.setdefault(path_key(url), rid)
        for url, origin in urls:
            clean, path, fragment = split_url(url)
            key = (clean, fragment)
            if key in seen:
                continue
            seen.add(key)
            routes.append({"_url": url, "_origin": origin, "_record": record, "_fragment": fragment})

    # Attach every reviewed legacy URL, including fragments and old paths that
    # disappeared from the current sitemap.
    route_by_key = {(split_url(r["_url"])[0], r.get("_fragment")): r for r in routes}
    for row in crosscheck_rows:
        url = row.get("original_url")
        if not url:
            continue
        clean, _, fragment = split_url(url)
        key = (clean, fragment)
        rid = row.get("archived_record") or source_url_index.get(path_key(url))
        record = records_by_id.get(rid) if rid else None
        if key in seen:
            existing = route_by_key.get(key)
            if existing is not None:
                existing.setdefault("_crosses", []).append(row)
            continue
        seen.add(key)
        item = {"_url": url, "_origin": "crosscheck_legacy", "_record": record, "_cross": row, "_crosses": [row], "_fragment": fragment}
        routes.append(item)
        route_by_key[key] = item

    # Add the requested 31 application URLs.  Their host is already Counso,
    # but their path is the old English compatibility path.
    for url in app_urls:
        clean, path, fragment = split_url(url)
        key = (clean, fragment)
        if key in seen:
            continue
        seen.add(key)
        dust_url = urlunsplit(("https", "docs.dust.tt", path, "", fragment or ""))
        cross = cross_by_path.get(path)
        rid = cross.get("archived_record") if cross else source_url_index.get(path)
        record = records_by_id.get(rid) if rid else None
        routes.append({"_url": dust_url, "_deployment_url": url, "_origin": "application_legacy31", "_record": record, "_cross": cross, "_fragment": fragment})

    # A source record may have several crosscheck paths.  The semantic mapping
    # comes from the legacy path when available, then from the canonical path.
    def target_for(route: dict) -> tuple[dict | None, dict | None, str | None]:
        url = route["_url"]
        path = path_key(url)
        cross = route.get("_cross")
        if route["_origin"] == "application_legacy31":
            if path == "/":
                return {"index": True}, cross, None
            if path in ADDED_TARGETS:
                return ADDED_TARGETS[path], cross, route["_record"]["record_id"] if route.get("_record") else None
            target = TARGETS.get(path)
            if target:
                return target, cross, route["_record"]["record_id"] if route.get("_record") else None
        if cross and path in TARGETS:
            return TARGETS[path], cross, route["_record"]["record_id"] if route.get("_record") else None
        if cross and path in ADDED_TARGETS:
            return ADDED_TARGETS[path], cross, route["_record"]["record_id"] if route.get("_record") else None
        if route.get("_record"):
            record = route["_record"]
            canonical_path = path_key(record.get("canonical_url", ""))
            # Most acquired records use the current canonical destination
            # (for example /docs/user-documentation/...); the reviewed table
            # stores the legacy URL that led there. Reuse that reviewed path
            # only for a semantic target, never for the internal
            # GetCurrentUser fallback recorded under /reference.
            reviewed = cross_by_id.get(record["record_id"])
            if reviewed:
                reviewed_path = path_key(reviewed.get("original_url", ""))
                if reviewed_path in TARGETS:
                    return TARGETS[reviewed_path], reviewed, record["record_id"]
            if record.get("canonical_url") in APP_RUN_TARGETS:
                return APP_RUN_TARGETS[record["canonical_url"]], cross_by_id.get(record["record_id"]), record["record_id"]
            if canonical_path in TARGETS:
                return TARGETS[canonical_path], cross_by_id.get(record["record_id"]), record["record_id"]
            # Developer platform legacy concepts are additional authored pages.
            if "legacy-dust-apps/what-is-a-dust-app" in record.get("canonical_url", "") or "legacy-dust-apps/dust-apps-core-concepts" in record.get("canonical_url", ""):
                return APP_RUN_TARGETS.get(record["canonical_url"]), cross_by_id.get(record["record_id"]), record["record_id"]
        return None, cross, route["_record"]["record_id"] if route.get("_record") else None

    # Build deterministic, reviewable route rows.
    final_routes: list[dict] = []
    for route in routes:
        original_url = route["_url"]
        deployment_url = route.get("_deployment_url")
        clean, path, fragment = split_url(original_url)
        record = route.get("_record")
        crosses = route.get("_crosses") or ([route["_cross"]] if route.get("_cross") else [])
        cross = route.get("_cross") or (crosses[0] if crosses else None) or (cross_by_id.get(record["record_id"]) if record else None)
        target, _, _ = target_for(route)
        is_legacy = route["_origin"] in {"crosscheck_legacy", "application_legacy31"}
        held_target_obj = None
        held_topic = None
        held_section = None
        if target and target.get("index"):
            status = "legacy_alias_to_index"
            reason = "Serve the documentation home and preserve the old English root entry."
            target_obj = {loc: {"topicId": None, "section": None, "url": f"https://docs.counso.ai/{loc}/", "file": f"content/indexes/{loc}.md"} for loc in ("en", "zh-cn")}
            primary_topic = None
            primary_section = None
        elif target:
            status, reason = target_status(target, cross, record.get("source_type", "page") if record else "page", legacy=is_legacy)
            target_obj = {loc: section_for_target(target, loc, topics, additions) for loc in ("en", "zh-cn")}
            primary_topic = target.get("topic")
            primary_section = target.get("section")
            if target.get("partial") and not is_legacy:
                reason = "The target is a scoped Counso rewrite; upstream claims are not carried over without Counso evidence."
        else:
            status, reason = reason_for_archive(record or {"source_type": "page", "canonical_url": clean}, cross)
            target_obj = {}
            primary_topic = None
            primary_section = None

        # Publication policy is evaluated after the ordinary source-to-topic
        # mapping.  This keeps the reviewed destination and hashes available
        # under ``heldTarget`` for audit while exposing no held API target to
        # the site router.  It also handles an old package where the authored
        # addition is absent but the legacy path is explicitly excluded.
        api_held = is_api_held(primary_topic, path, publication)
        published = bool(target) and not api_held
        if api_held:
            held_target_obj = target_obj or None
            held_topic = primary_topic or (target.get("topic") if target and not target.get("index") else None)
            held_section = primary_section or (target.get("section") if target and not target.get("index") else None)
            status = "excluded_api_not_public"
            reason = publication.get("reasonEn") or "API documentation is not included in this release."
            target_obj = {}
            primary_topic = None
            primary_section = None

        # The friendly, byte-checked markdown path is the primary sourceFile.
        # Fall back to the original manifest raw body if an older package does
        # not yet include url-to-original.json.
        source_file = source_archive_file = source_hash = source_record_id = None
        source_repository_url = source_snapshot_url = None
        source_canonical = None
        source_type = None
        source_title = None
        if record:
            source_record_id = record["record_id"]
            source_canonical = record.get("canonical_url")
            source_type = record.get("source_type")
            source_title = record.get("title")
            source_hash = record.get("source_hash")
            idx = url_index.get(source_record_id, {})
            source_file = idx.get("originalFile")
            source_archive_file = idx.get("archiveFile")
            source_repository_url = idx.get("sourceRepositoryUrl")
            source_snapshot_url = idx.get("snapshotDownloadUrl")
            if not source_file:
                source_file = f"reference/original/{record.get('raw_path')}"
            if not source_archive_file:
                source_archive_file = f"reference/original/{record.get('raw_path')}"

        source_match_note = None
        if target and target.get("observed_current_user"):
            source_match_note = "Observed response is the archived GetCurrentUser page; it is a source match only and is not semantic Apps content."

        row = {
            "routeId": hashlib.sha1(f"{original_url}\\0{source_record_id or ''}".encode()).hexdigest()[:16],
            "origin": route["_origin"],
            "originalUrl": original_url,
            **({"deploymentUrl": deployment_url} if deployment_url else {}),
            "originalPath": path,
            "fragment": fragment,
            "canonicalUrl": source_canonical,
            "sourceRecordId": source_record_id,
            "sourceType": source_type,
            "sourceTitle": source_title,
            "sourceFile": source_file,
            "archiveFile": source_archive_file,
            "sourceHash": source_hash,
            **({"sourceRepositoryUrl": source_repository_url} if source_repository_url else {}),
            **({"snapshotDownloadUrl": source_snapshot_url} if source_snapshot_url else {}),
            "targetTopicId": primary_topic,
            "targetSection": primary_section,
            "target": target_obj,
            "published": published,
            "publicationStatus": "hold_api" if api_held else ("published" if published else "archive_only"),
            "status": status,
            "reason": reason,
        }
        if api_held:
            row["excludedReasonCode"] = "api_not_public"
            row["excludedTargetTopicId"] = held_topic
            row["excludedTargetSection"] = held_section
            if held_target_obj:
                row["heldTarget"] = held_target_obj
        if cross:
            row["crosscheckId"] = cross.get("id")
            row["crosscheckStatus"] = cross.get("authoring_status")
            row["crosscheckReason"] = cross.get("reason")
            row["auditedDestination"] = cross.get("audited_destination")
            if len(crosses) > 1:
                row["crosscheckIds"] = [c.get("id") for c in crosses]
        if source_match_note:
            row["sourceMatchNote"] = source_match_note
        final_routes.append(row)

    # Sort by source record, then the original URL so the output is stable
    # across runs and easy to diff.
    final_routes.sort(key=lambda r: (r["sourceRecordId"] or "", r["originalUrl"], r["fragment"] or ""))
    status_counts = Counter(r["status"] for r in final_routes)
    origin_counts = Counter(r["origin"] for r in final_routes)
    target_records = {r["sourceRecordId"] for r in final_routes if r["targetTopicId"] and r["sourceRecordId"]}
    held_api_records = {r["sourceRecordId"] for r in final_routes if r["status"] == "excluded_api_not_public" and r["sourceRecordId"]}
    application_routes = [r for r in final_routes if r["origin"] == "application_legacy31"]
    manifest_page_ids = {r["record_id"] for r in records if r.get("source_type") == "page"}
    manifest_record_ids = {r["record_id"] for r in records}
    traced_ids = {r["sourceRecordId"] for r in final_routes if r["origin"] == "manifest" and r["sourceRecordId"]}
    attached_crosscheck_ids = set()
    for route in final_routes:
        attached_crosscheck_ids.update(route.get("crosscheckIds", []))
        if route.get("crosscheckId"):
            attached_crosscheck_ids.add(route["crosscheckId"])
    payload = {
        "schemaVersion": "2026-09-11.routes.v1",
        "generatedAt": manifest.get("generated_at", "2026-09-11"),
        "description": "Machine-readable legacy URL to Counso rewrite and archive disposition ledger.",
        "targetHosts": {"documentation": "https://docs.counso.ai", "application": "https://app.counso.ai"},
        "publicationPolicy": {
            "publicationStatus": publication["publicationStatus"],
            "holdApi": publication["holdApi"],
            "excludedTopicPrefixes": publication["excludedTopicPrefixes"],
            "excludedOriginalPaths": publication["excludedOriginalPaths"],
            "source": "content/release-policy.json plus content/manifest.json and content/additions-manifest.json publicationStatus",
            "reason": publication.get("reason"),
            "reasonEn": publication.get("reasonEn"),
        },
        "sourceSnapshots": {
            "manifest": "reference/original/manifest-final.json",
            "urlIndex": "reference/url-to-original.json",
            "sitemap": "reference/original/raw/index/sitemap.xml",
            "llms": "reference/original/raw/index/llms.txt",
            "topics": "content/manifest.json",
            "crosscheck": "mapping/inputs/source-crosscheck.json",
            "applicationInput": "mapping/inputs/application-legacy-urls.txt",
            "additions": "content/additions-manifest.json",
            "releasePolicy": "content/release-policy.json",
        },
        "inputs": {
            "manifestVersion": manifest.get("manifest_version"),
            "manifestCounts": manifest.get("counts"),
            "reviewedLegacyUrlCount": len(crosscheck_rows),
            "applicationLegacyUrlCount": len(app_urls),
            "topicCountByLocale": {loc: sum(1 for t, l in topics if l == loc) for loc in ("en", "zh-cn")},
            "manifestPublicationStatuses": publication["manifestStatuses"],
            "heldTopicIds": publication["heldTopicIds"],
        },
        "summary": {
            "manifestRecords": len(records),
            "manifestPageRecords": sum(1 for r in records if r.get("source_type") == "page"),
            "manifestApiRecords": sum(1 for r in records if r.get("source_type") == "api"),
            "manifestPageRecordsWithManifestRoute": len(traced_ids & manifest_page_ids),
            "allManifestPageRecordsTraceable": traced_ids >= manifest_page_ids,
            "allManifestRecordsTraceable": traced_ids >= manifest_record_ids,
            "routeCount": len(final_routes),
            "originCounts": dict(sorted(origin_counts.items())),
            "statusCounts": dict(sorted(status_counts.items())),
            "targetedSourceRecords": len(target_records),
            "excludedApiRoutes": sum(1 for r in final_routes if r["status"] == "excluded_api_not_public"),
            "excludedApiSourceRecords": len(held_api_records),
            "publishedRoutes": sum(1 for r in final_routes if r["published"]),
            "applicationPublishedRoutes": sum(1 for r in application_routes if r["published"]),
            "applicationExcludedApiRoutes": sum(1 for r in application_routes if r["status"] == "excluded_api_not_public"),
            "legacyFragmentsPreserved": sum(1 for r in final_routes if r["fragment"] is not None),
            "toolCatalogSectionAliases": sum(1 for r in final_routes if r["targetTopicId"] == "integrations/tools-catalog"),
            "reviewedCrosscheckRows": len(crosscheck_rows),
            "reviewedCrosscheckIdsAttached": len(attached_crosscheck_ids),
        },
        "routes": final_routes,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload["summary"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
