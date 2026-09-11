---
title: "Confluence connection and tools"
topicId: "integrations/confluence"
contentRevision: "45"
---

# Confluence connection and tools

## Confluence connection

A Confluence administrator selects the global spaces to synchronize. Private spaces, pages with view restrictions, and their child pages are not synchronized. In **Spaces → Connections → Add connection → Confluence**, complete the administrator authorization and select the allowed scope. After refresh, search for one known page and compare its space key, parent, labels, and version in Confluence.

If the connection is updated, review permissions and selected labels again. A page can be visible through a parent space while a page restriction still prevents content access.

## Confluence tool

Open **Spaces → Tools → Add Tools → Confluence**, complete the provider authorization, and add the tool to an Agent. Decide whether the Agent may retrieve, create, update, move, or comment on pages. The tool supports page operations, user operations, and CQL search.

For a read test, use a known page ID or a narrow CQL query such as a single space and title. For a write, read the page and destination first, apply one change or move, and reopen the same page ID. Personal credentials preserve the acting user’s Confluence permissions; shared credentials make the shared account the effective actor.

## Common issues

- The connection finds a page the user cannot open: check both Space membership and Confluence restrictions.
- CQL returns too much: add a space key, title, label, or page ID constraint.
- Move or update fails: check destination permission and page restrictions.
- Refresh does not show a new page: check parent scope, labels, and refresh state.

See [personal and shared access](/en/integrations/personal-and-shared/#personal-and-shared-credentials).
