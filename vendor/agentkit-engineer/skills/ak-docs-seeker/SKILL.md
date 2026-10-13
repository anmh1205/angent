---
name: ak-docs-seeker
description: Find current library, framework and repository documentation through official docs, llms.txt, canonical source and installed-version evidence.
metadata: {port: angent-fallback, mode: adapted}
---

# Docs Seeker — Portable Fallback

Read `references/docs-research.md`.

## Workflow

1. State the exact API/behavior/version question.
2. Identify installed/target version when possible.
3. Prefer official docs and canonical repository.
4. Use llms.txt/indexes/search for discovery.
5. Inspect source/changelog when docs are ambiguous.
6. Return only the decisive information plus source/version pointer.

If web access is unavailable, inspect installed package/source and clearly mark the limitation.
