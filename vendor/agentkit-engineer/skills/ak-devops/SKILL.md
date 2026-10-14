---
name: ak-devops
description: Prepare and verify containers, CI/CD, Kubernetes, cloud and GitOps changes through explicit plan/apply, environment, deployment and deletion gates.
license: MIT
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# DevOps — Portable Fallback

Use for infrastructure, containerization, CI/CD, Kubernetes/cloud and GitOps work.

Preparing an artifact, plan or manifest is not deployment authority.

## Load progressively

- `references/containers-ci.md` — container builds and CI pipelines.
- `references/kubernetes-cloud.md` — cluster/cloud resources and deployment controllers.
- `references/rollout-recovery.md` — rollout, health, rollback and incident-safe changes.

## Contract

Resolve:
- current IaC/config/controller and source of truth;
- target account/project/cluster/region/namespace/environment;
- desired state and resource owner;
- secret/config/provider dependencies;
- whether this turn may only prepare/plan or may also apply;
- replacement/deletion blast radius;
- verification and rollback/forward-fix boundary.

Do not infer apply, deployment, restart, scaling, deletion or provider-admin authority from permission to edit configuration.

## Workflow

1. Inspect repository instructions, existing IaC/GitOps/config and live state when the claim depends on it.
2. Establish current versus desired state and the source that owns reconciliation.
3. Prefer the existing declarative/reproducible mechanism over adding a parallel deployment path.
4. Validate syntax/static policy and generated artifacts.
5. Produce a plan/diff/preview when tooling supports it.
6. Review create/update/replace/delete consequences and secret/provider boundaries.
7. Apply only when the exact target and operation are currently authorized.
8. Observe controller/provider/runtime state until the acceptance claim is established or a real blocker appears.
9. Verify health/readiness/traffic/error behavior rather than equating apply success with service readiness.
10. Preserve rollback or forward-fix guidance appropriate to data/schema/state changes.

## Boundaries

Network/provider commands can incur cost, change production state or delete resources.

A plan is not an apply; an apply is not application readiness; rollback is not always safe after schema/data/state transitions.

Avoid introducing a second deployment/config mechanism when the project already has one.
