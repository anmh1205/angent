# Containers and CI

## Containers

Prefer:
- deterministic base/version pinning where appropriate;
- multi-stage builds when they reduce attack surface/artifact size;
- non-root runtime when feasible;
- explicit health/startup behavior;
- minimal secret exposure during build.

Verify the image actually starts under production-like configuration.

## CI

Keep pipeline stages aligned with project acceptance:
- dependency restore;
- lint/type/static checks;
- unit/integration;
- build/package;
- security/policy when required;
- deployment gate.

Do not duplicate local and CI commands unnecessarily; share scripts where possible.
