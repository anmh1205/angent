---
name: ak-project-organization
description: Organize files, folders and project artifacts around ownership and retrieval without imposing a generic layout on an existing codebase.
metadata: {port: angent-fallback, mode: portable}
---

# Project Organization — Portable Fallback

Use when creating new artifacts or reorganizing an existing project.

## Workflow

1. Read current structure and AGENTS.md.
2. Identify ownership/lifecycle of the artifact.
3. Place it near the code/domain/process that owns it.
4. Reuse existing conventions before creating a new top-level category.
5. Separate generated, source, docs, tests, temporary and secret material appropriately.
6. Update links/imports/config after moves.
7. Verify no stale duplicate remains as an accidental second source of truth.

Avoid broad reshuffles whose only benefit is aesthetic folder symmetry.
