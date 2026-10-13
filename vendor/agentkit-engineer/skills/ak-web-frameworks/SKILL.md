---
name: ak-web-frameworks
description: Build and review modern web applications and monorepos using the project's actual framework/version, rendering model, caching and build system.
license: MIT
metadata: {port: angent-fallback, mode: portable}
---

# Web Frameworks — Portable Fallback

## Load progressively

- `references/rendering-caching.md` — rendering/data/cache boundaries.
- `references/monorepo-build.md` — package ownership and build graph.

## Workflow

1. Identify framework/runtime/build versions.
2. Understand rendering and server/client boundary.
3. Model data fetching, cache/revalidation and errors.
4. Respect package/module ownership.
5. Keep environment/server-only/client-only code separated.
6. Verify clean build and runtime behavior.
7. Measure before performance optimization.

Do not apply patterns from another framework generation without checking current docs/source.
