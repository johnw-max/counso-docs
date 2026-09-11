---
title: "Gong connection and tools"
topicId: "integrations/gong"
contentRevision: "45"
---

# Gong connection and tools

## Gong connection

The Gong Connection syncs all workspace transcripts by default, excluding those marked Private. A Gong administrator and workspace administrator should review that scope and decide which Space members may access the synchronized content. Open **Spaces → Connections → Add connection → Gong**, complete Gong consent, and add the connection to the Spaces that need it. The connection synchronizes transcript text; it is not a live recording control. Private Gong transcripts are excluded from synchronization.

After refresh, find one known call and compare its participants, date, transcript availability, and visibility in Gong. Treat transcript freshness separately from live call retrieval.

## Gong tool

Open **Spaces → Tools → Add Tools → Gong**, complete OAuth, and add the tool to a restricted Space. Gong API results can include workspace calls beyond the authenticating user’s own calls, so Space membership is the access boundary. The live tool supports:

- `list_calls` with optional ISO-8601 `fromDateTime`, `toDateTime`, and pagination cursor;
- `get_call` with a Gong `callId`;
- `get_call_transcript` with that same `callId`.

Start with a narrow date range and one call ID returned by `list_calls`. A transcript may be unavailable while Gong is still processing it. Before sharing a transcript, check the Space audience and provider sensitivity.

## Common issues

- A call is missing from synchronized results: check selected teams, date range, transcript privacy, and refresh.
- A call is listed but its transcript is unavailable: wait for Gong processing and check transcript permission.
- Results are broader than expected: restrict the Space; the personal OAuth identity does not by itself limit workspace call results.

See [personal and shared access](/en/integrations/personal-and-shared/#personal-and-shared-credentials) and [connections and tools](/en/integrations/connections-and-tools/#connections-and-tools).
