---
name: ak-docs-seeker
description: Discover current versioned library/framework/API documentation from canonical sources, llms.txt indexes and installed package evidence.
metadata: {port: angent-fallback, mode: adapted}
---

# Documentation Discovery — Portable Fallback

Use for external library/API questions. For authoring the project's own docs use `ak-docs`. Read `references/docs-research.md` and `references/source-routing.md` when needed.

## Topic and library workflows

1. Specify the exact API, behavior or feature question and the installed/target library version.
2. Resolve canonical docs/source from trusted package or publisher evidence. Use `llms.txt` and `llms-full.txt` as navigation, not as proof of behavior.
3. For a narrow topic, inspect the official versioned API page, examples and changelog. For general library investigation, analyze the index then retrieve bounded relevant sections.
4. If documentation is incomplete or contradictory, inspect canonical source/tests, release notes and migration guides; don't manufacture URLs.
5. Verify version applicability, platform constraints and deprecations. Community reports are supplementary evidence.
6. Return decisive guidance with precise source/version pointers and unresolved conflicts.

## Harness boundary

The upstream package supplies Node scripts for topic detection, context7 fetching and URL analysis; those scripts are **not packaged in this fallback**. Use available native browser/search/source tools. Never imply the upstream scripts executed, that a provider token exists, or that delegated agents ran unless actually observed. Offline results must carry a freshness limitation.

Multiple URLs are a retrieval-ranking task, not automatic justification for spawning 3 or 7 subagents.
