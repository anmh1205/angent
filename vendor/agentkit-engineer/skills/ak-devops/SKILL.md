---
name: ak-devops
description: Work with containers, CI/CD, Kubernetes, cloud and GitOps infrastructure while preserving reproducibility, least privilege and operational safety.
license: MIT
metadata: {port: angent-fallback, mode: portable}
---

# DevOps — Portable Fallback

Use for infrastructure, containerization, CI/CD and cloud operations.

## Load progressively

- `references/containers-ci.md` — container builds and CI pipelines.
- `references/kubernetes-cloud.md` — cluster/cloud resources and deployment controllers.
- `references/rollout-recovery.md` — rollout, health, rollback and incident-safe changes.

## Workflow

1. Inspect existing IaC/config and AGENTS.md.
2. Establish current and desired state.
3. Prefer declarative/reproducible changes.
4. Validate syntax/static policy.
5. Preview/diff plan where tooling supports it.
6. Apply only to the authorized target/environment.
7. Verify runtime state and health.
8. Record rollback/recovery path.

Avoid introducing a second deployment/config mechanism when the project already has one.
