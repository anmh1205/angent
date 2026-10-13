---
name: ak-react-best-practices
description: Review and improve React/Next.js performance using evidence, current framework semantics and established rendering/data/bundle patterns.
metadata: {port: angent-fallback, mode: portable}
---

# React Best Practices — Portable Fallback

Use for performance/architecture review, not as a generic style linter.

## Check only relevant areas

- server/client boundary;
- data fetching and waterfalls;
- Suspense/streaming behavior;
- unnecessary rerenders;
- component state locality;
- expensive computation;
- bundle/code splitting;
- image/font/resource loading;
- caching/revalidation;
- list virtualization for genuinely large views.

Measure or inspect profiler/build evidence before asserting a performance problem.

Confirm current React/Next.js version because recommended patterns change.

Do not rewrite working components merely to match a fashionable pattern.
