---
name: ak-web-frameworks
description: Build, migrate and review Next.js or Turborepo projects using the installed versions, explicit render/cache/build contracts, SEO/GEO surfaces and bounded package/deployment effects.
license: MIT
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Web Frameworks — Portable Fallback

The stable Engineer workflow is specifically about Next.js and Turborepo-oriented architecture and implementation. Do not generalize these references into a universal framework cookbook.

Use Frontend Development when framework architecture is incidental to component/UI behavior, Frontend Design when visual direction is primary, and DevOps when provider/deployment configuration is the main outcome.

## Load progressively

- `references/rendering-caching.md` — Next.js rendering/data/cache boundaries.
- `references/monorepo-build.md` — Turborepo/package ownership and build graph.
- `references/nextjs-turborepo-boundaries.md` — version/package/deployment/SEO-GEO boundaries.

## Contract

Resolve:
- installed Next.js/Turborepo/React/Node/package-manager versions;
- App Router/server-client/rendering model actually used;
- current route/layout/loading/error conventions;
- data/cache/revalidation contract;
- monorepo package/task/output ownership when applicable;
- metadata/SEO/GEO outcome when requested;
- allowed package install, scaffold/migration utility, remote cache, local process and network effects;
- deployment authority and required verification.

There is no default framework version, package manager, hosting provider or deployment mode.

## Workflow

1. Inspect repository instructions and the installed framework/build graph before choosing patterns.
2. Preserve the actual Server/Client Component, SSR/static/ISR/data-cache semantics of the installed Next.js generation.
3. Keep server-only secrets and privileged code out of client bundles.
4. Define cache keys/scope/revalidation/invalidation where freshness affects correctness.
5. For Turborepo, preserve package ownership, dependency direction, task dependencies, outputs and material cache inputs.
6. Use optional scaffold/migration utilities only inside an authorized file/package boundary; inspect generated changes before acceptance.
7. For SEO/GEO surfaces, derive sitemap/robots/llms/metadata/social/structured-data outputs from a coherent content source where the product contract requires them.
8. Verify clean build plus representative runtime/render behavior for the changed route/package/task.
9. Measure before performance optimization and compare the same workload/configuration.
10. Report package/config/generated-file impact, cache/remote-service assumptions and unverified deployment/runtime gaps.

## Boundaries

Framework installation, dev servers, builds and migration utilities can use network, processes, disk and lifecycle scripts.

Remote Turborepo caching requires explicit service/network/credential authority.

Preparing an artifact does not authorize deployment.

For frameworks outside the documented Next.js/Turborepo scope, use the project's current official documentation or another appropriate Skill instead of projecting these rules blindly.
