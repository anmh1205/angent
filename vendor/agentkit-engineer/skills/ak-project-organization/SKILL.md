---
name: ak-project-organization
description: Route artifacts to project-owned paths and safely plan explicit restructures without imposing a universal folder layout.
metadata: {port: angent-fallback, mode: adapted}
---

# Project Organization — Portable Fallback

Use when selecting paths for plans, reports, journals, generated assets, docs and implementation files, or when the user expressly requests a file/directory reorganization. Treat upstream `src/docs/plans/assets` and kebab-case defaults as examples, not mandatory conventions.

## Advisory mode — requested by another skill

1. Read the existing structure, root/nested AGENTS.md, manifest, ignore patterns and comparable artifacts.
2. Classify each artifact by owner, lifecycle and consumer: code, tests, decision docs, plans/reports/journals, assets, configuration, generated output, transient evidence or secrets.
3. Recommend one path, name and nesting level consistent with existing naming/toolchain and nearby artifacts.
4. Use evergreen names for stable truth and dated identities only for chronological material. Do not store task progress in evergreen docs.
5. Advise only; do not move or create directories for aesthetic symmetry.

## Organize mode — explicit restructure

1. Inventory only the authorized scope. Identify duplicate owners, misplaced assets and broken references.
2. Produce concrete from/to moves, collision risks, cross-links/imports and build/generator effects.
3. Obtain authorization for material moves when not already granted; advisory use is never permission to reorganize.
4. Move only scoped files without overwriting, touching secrets, `.git`, dependency caches or unrelated ignored files.
5. Update imports, links and config; validate tree, scripts or tests as relevant; report actual changes and unresolved issues.

Markdown type-specific structure should improve readability; rigid templates and forced bullet-only prose are not acceptance criteria.
