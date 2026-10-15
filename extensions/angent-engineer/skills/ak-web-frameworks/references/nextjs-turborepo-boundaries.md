# Next.js and Turborepo boundaries

## Version first

Read the installed Next.js, React, Node, Turborepo and package-manager versions before prescribing APIs or cache behavior.

Do not assume App Router, React Server Components, a particular cache default, or a specific Turborepo pipeline syntax merely because the Skill supports them.

## Next.js execution boundary

For a route/feature identify:
- Server vs Client Component ownership;
- build-time vs request-time work;
- static/dynamic/ISR behavior;
- loading/error/not-found boundaries;
- auth/personalization impact on caching;
- image/font/script/resource behavior;
- server actions/route handlers if used.

Keep server-only secrets and privileged providers outside client bundles.

## SEO / GEO surfaces

When the requested outcome includes discoverability, keep canonical metadata, sitemap, robots, structured data, social cards and optional llms/Markdown surfaces consistent with the same content/source-of-truth.

Do not generate search/AI surfaces that disagree with the visible page or expose private content.

## Turborepo

Preserve:
- package ownership and dependency direction;
- task dependency graph;
- outputs and cache inputs;
- environment variables that affect cache correctness;
- generated artifacts;
- remote cache authority/credentials.

A fast cached build is not evidence of correctness when material inputs were omitted from the cache key.

## Effects

Scaffolding, migration, package installation and remote caching are separate effects from editing source.

Deployment/provider configuration remains a DevOps boundary.
