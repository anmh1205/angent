---
name: ak-graphify
description: Build and query evidence-linked knowledge graphs from code, documents and other artifacts using Graphify when available or a portable local graph representation otherwise.
metadata: {port: angent-fallback, mode: adapted}
---

# Graphify — Portable Fallback

Use when repeated relationship/path/impact queries justify a persistent graph.

For publish-grade architecture diagrams, use Tech Graph instead.

Read:
- `references/graph-schema.md`;
- `references/extraction-and-runtime.md`.

## Native Graphify path

If a compatible Graphify installation is available:

1. inspect the installed/current CLI/package version;
2. build the graph from the bounded source path;
3. use incremental/watch mode only when ongoing updates are actually useful;
4. retain generated graph/report artifacts;
5. expose/query through MCP only when the active runtime benefits from it.

Do not hard-code one historical package command without checking current help.

## Portable path

When Graphify itself is unavailable:

1. define the questions the graph must answer;
2. select a bounded source set;
3. extract deterministic relationships locally where possible;
4. add semantic relationships only with provenance/confidence;
5. store portable JSON/GraphML/CSV/SQLite or another available graph representation;
6. query paths/neighbors/impact;
7. validate important edges back to source.

## Provenance classes

Distinguish at least:

- **EXTRACTED** — directly derived from code/schema/metadata;
- **INFERRED** — semantic model inference with source pointer;
- **AMBIGUOUS** — identity/relation requires human verification.

Do not flatten all edges into the same certainty.

## Privacy

Keep source/code processing local when possible.

If documents/images are sent to an external model for semantic extraction, make that boundary visible when privacy matters.

## Output

Return graph artifact location/format, extraction scope, important structural findings, confidence limitations and useful queries.

Do not build a large persistent graph when Scout/search can answer the question more cheaply.
