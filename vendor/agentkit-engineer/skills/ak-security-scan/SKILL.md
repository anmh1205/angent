---
name: ak-security-scan
description: Compatibility route for the retired ak:security-scan identity; use the canonical ak-security workflow with its fast secret/dependency modes or bounded comprehensive audit.
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0", compatibility: "retired-route"}
---

# Security Scan — Compatibility Route

Stable AgentKit documentation retires `ak:security-scan` as a separate public workflow and routes security scanning through `ak:security`.

This fallback keeps the packaged identity because it exists in the pinned stable 2.19.0 artifact, but it must not evolve a second competing security workflow.

## Route

Use `ak-security` and preserve the user's requested scan intent:

- secret-only request → `ak-security --secrets-only`;
- dependency/advisory-only request → `ak-security --deps-only`;
- both fast checks → both fast flags;
- broad source security scan/audit → canonical `ak-security` comprehensive audit;
- confirmed finding needing a fix → canonical `ak-security --fix` or `ak-fix` according to the task boundary.

Do not silently add STRIDE/red-team/fix behavior to a request that selected a fast scan.

## Boundary

This Skill is an identity/compatibility adapter, not an independent acceptance surface.

All scope, redaction, advisory-network, finding-validation, severity, fix-authority and verification semantics come from `ak-security`.

A scan result remains triage evidence until the canonical security workflow validates the material finding.
