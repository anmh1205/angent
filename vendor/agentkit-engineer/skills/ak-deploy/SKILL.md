---
name: ak-deploy
description: Detect the project's actual deployment target and perform an authorized deployment with environment, migration, health and rollback verification.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# Deploy — Portable Fallback

Deployment is a high-impact effect. Do not infer authority from credentials being available.

## Load progressively

- `references/environment-detection.md` — resolve provider/environment/artifact.
- `references/deployment-gate.md` — preflight checks.
- `references/release-verification.md` — post-deploy state and smoke evidence.

## Workflow

1. Identify exact target environment/provider.
2. Identify immutable or reproducible artifact/version.
3. Confirm current authority.
4. Check config/secrets/migrations/dependencies.
5. Run required build/tests.
6. Deploy through project/provider-native tooling.
7. Verify provider state and user-facing health.
8. Record deployed version and rollback/forward-fix path.

A command returning success is transport evidence, not deployment completion.
