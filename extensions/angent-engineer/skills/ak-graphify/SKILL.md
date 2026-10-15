---
name: ak-graphify
description: Construct and query provenance-aware knowledge graphs from code/documents/media using a verified Graphify installation or a bounded portable replacement.
metadata: {port: angent-fallback, mode: degraded}
---

# Graphify — Portable Fallback

Use for **repeated structural queries** over unfamiliar codebases, cross-file dependencies, requirements and concepts: module ownership, calls/imports, high-degree nodes, influence/impact paths and unanticipated relationships. Graphify produces a **queryable knowledge graph**, not merely a pretty architecture image. For a single local question, Scout/search is cheaper; for publishable architecture visuals, Tech Graph may fit better.

Stable Engineer 2.19.0 packages Graphify as a **beta external dependency**. The native Python package was documented as graphifyy (double y), distinct from unrelated similarly named packages. Treat installed package help and current provider docs as authority; do not assume its CLI, Python version or optional integrations are available from the presence of this fallback Markdown.

Read **references/graph-schema.md** and **references/extraction-and-runtime.md**.

## Selection and capability preflight

Determine source boundaries, graph questions, expected node/edge kinds, file versions, privacy constraints, scale, persistence and required query interface. Check actual Graphify installation, CLI/version and available provider/processing extensions. Ask before installing software, running resource-intensive scans, processing private media with external models or starting long-lived watch/MCP services.

### Native path — if Graphify really exists

- Build from the authorized path using installed Graphify help; a typical upstream command is **graphify <path>**, with optional **--watch**.
- Expect a generated graph representation, visual navigation and summary; stable upstream names include graphify-out/graph.json, graph.html, GRAPH_REPORT.md and cache/. Verify actual outputs rather than assuming those files were created.
- Use the graph for node search, neighbor exploration, influence paths and shortest paths. If the active runtime and installation support MCP, the upstream server pattern is **python -m graphify.serve <graph.json>**, with capabilities such as query_graph, get_node, get_neighbors and shortest_path. Do not claim an MCP server/tool was registered merely from a JSON graph.
- For incremental updates, check source-hash tracking **and deletion of stale nodes/edges**, not just addition of changed files.

### Portable replacement — when native Graphify is absent

1. Fix a small schema and extraction scope before traversing files. Record source identity, revision and trust boundary.
2. Extract deterministic code relations (imports, definitions, calls, inheritance, known schema links) with a real parser/symbol index when possible; substring matches are lower-certainty observations, not verified AST edges.
3. For documents/papers/requirements, create concept links with exact section/page/source references. For imagery or media, only invoke an actually available and authorized extractor.
4. Tag each edge **EXTRACTED**, **INFERRED**, or **AMBIGUOUS** with provenance and confidence; avoid conflating LLM hypotheses with syntax facts.
5. Store a portable queryable representation (JSON with an index, GraphML, SQLite or another available format), supporting at least node lookup, neighbors, search and reachable/shortest paths when required.
6. Answer actual architecture/impact questions and trace any decisive graph-derived assertion back to original source.
7. Track revisions/incremental invalidation and ensure removal of stale edges after source edits.

This portable path can preserve analytical goals but does **not** reproduce the upstream tree-sitter/Whisper/media pipeline, optional clustering/Neo4j integration, interactive web graph, or packaged MCP server unless those capabilities were independently executed and verified. No fixed 'token reduction factor' or language coverage is guaranteed.

## External processing/privacy

The upstream three-pass model distinguishes local AST extraction, optional local audio/video transcription, and **external-model semantic extraction of documents/images**. Disclosure/authorization should reflect the actual provider, selected sources and destination. Never tell the user everything remains local if docs/images were submitted to a model provider.

## Output and limits

Report scope/source revision, extraction methods, provenance classes, counts only when measured, artifact location/format, query examples and actual results, validation of high-impact edges, stale-data risks and missing native features. Neither graph generation nor visual density certifies architecture correctness; compare material findings against code/tests/current docs before basing a plan on them.

Do not create a large persistent graph or start continuous watchers without a real user need and permission.
