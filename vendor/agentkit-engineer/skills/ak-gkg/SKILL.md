---
name: ak-gkg
description: Use GitLab Knowledge Graph semantic code analysis when available; otherwise reproduce the needed definition/usage/impact analysis with repository-native search.
metadata: {port: angent-fallback, mode: degraded}
---

# GKG — Portable Fallback

If GitLab Knowledge Graph tooling is installed and usable, use it for semantic definition, usage, impact and architecture queries.

If unavailable, degrade to:
- language-server/indexer tools when available;
- symbol/AST-aware repository search;
- textual search + source tracing.

## Output

Return the semantic question, evidence path and confidence/limitations.

Do not claim semantic graph completeness when using textual fallback.

This Skill preserves the **analysis outcome**, not the dependency on one graph product.
