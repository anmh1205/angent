---
name: ak-deploy
description: Detect the project's actual deployment target and perform an explicitly authorized deployment with environment, artifact, migration, health and rollback verification.
license: MIT
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Deploy — Portable Fallback

Deployment is a high-impact effect. Credentials/capability do not imply authority.

## Scope

Own:
- deployment-target detection;
- platform/project/environment selection;
- deployment preflight;
- deployment effect;
- post-deploy provider and user-facing verification;
- authoritative deployment documentation updates.

Do not silently expand into infrastructure provisioning, DNS, database-migration authoring, certificate management or CI/CD design; route those to DevOps/owning workflow unless explicitly included.

## Load progressively

- `references/environment-detection.md` — resolve provider/environment/artifact.
- `references/provider-catalog.md` — known provider signals and portable routing.
- `references/deployment-gate.md` — preflight checks.
- `references/release-verification.md` — post-deploy state and smoke evidence.

## Detect target

Prefer in order:
1. explicit current target;
2. authoritative project deployment docs/config;
3. provider-specific config files;
4. CI/CD/provider state;
5. project type only as a recommendation signal;
6. ask when several materially different targets remain credible.

Never deploy to an "obvious default" when provider/environment/account/project identity is material.

## Execute

1. Resolve exact provider/account/project/environment and canonical endpoint.
2. Resolve reproducible artifact/build/version.
3. Revalidate authority for the exact target/material arguments.
4. Check config/secret presence without exposing values.
5. Check migration/dependency compatibility and rollback/forward-fix route.
6. Run required build/tests/pre-deploy gates.
7. Use current project/provider-native deployment tooling.
8. Observe provider deployment/revision state.
9. Verify health/readiness and the critical user/API path at the endpoint users actually reach.
10. Record deployed version and update the authoritative deployment doc when useful.

If the exact provider command/API is uncertain or versioned, inspect live help/current official documentation instead of copying a stale command.

## Platform coverage

The pinned package includes guidance for Vercel, Netlify, Cloudflare, Railway, Fly.io, Render, Heroku, TOSE, GitHub Pages, Coolify, Dokploy, GCP, AWS, DigitalOcean and Vultr.

The portable fallback preserves provider recognition/routing in one catalog rather than copying fifteen large command files. Current provider docs/project config own exact commands, product names, limits and pricing.

## Failure

A deploy command returning success is transport evidence, not completion.

If provider state is still converging, represent it as waiting. If health fails, diagnose/rollback/forward-fix according to authority and project policy.

## Completion

Deployment is verified only when the requested provider/environment reports the intended revision/artifact and required health/user-facing checks pass.

Local build success or a returned URL alone is insufficient.
