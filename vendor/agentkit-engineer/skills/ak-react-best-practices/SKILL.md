---
name: ak-react-best-practices
description: Audit or improve React/Next.js performance using an explicit baseline, installed-version compatibility, ranked evidence, bounded mutation and comparable before/after verification.
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# React Best Practices — Portable Fallback

Use for evidence-led React/Next.js performance work, not as a generic style linter or automatic rewrite pass.

Read `references/measurement-contract.md`.

## Prepare

Resolve:
- installed React/Next.js/bundler/server/browser/data-library versions;
- affected route/component/user path;
- representative workload and current performance evidence;
- performance budget or user-visible symptom;
- server/client/cache/hydration/CSP boundaries;
- audit-only versus allowed mutation scope;
- whether package install, config change, profiling, local server, remote telemetry or deployment is authorized;
- behavioral tests that must stay green.

The upstream rule set is a static guideline set, not a live compatibility database and not proof of impact in this application.

## Review dimensions

Inspect only dimensions supported by evidence:
- async/network waterfalls;
- unnecessary initial bundle cost;
- server serialization/duplicate work;
- client fetching/global subscription duplication;
- expensive or excessive rerenders;
- rendering/hydration/layout work;
- hot-path computation/allocation;
- cache/freshness behavior;
- list virtualization for genuinely large views;
- compatible advanced callback/subscription patterns.

Rank findings by expected user impact, evidence strength, compatibility and behavior risk.

## Workflow

1. Reproduce the representative workload and record the baseline method/result.
2. Build a compatibility map for any referenced API/pattern against installed versions.
3. Identify the highest-impact supported cause; do not start from fashionable micro-optimizations.
4. In audit-only mode, stop after ranked findings and verification plan.
5. If mutation is authorized, change one bounded cause while preserving data dependencies, error behavior, accessibility, hydration, freshness and server/client ownership.
6. Run focused behavioral tests.
7. Repeat the **same** measurement procedure/configuration.
8. Keep noisy/inconclusive results visible rather than declaring improvement.
9. Report before/after evidence, changed files/config/dependencies and rejected/deferred findings.

## Semantic risk

A faster implementation can be wrong.

- Parallelize only proven-independent operations; preserve failure/ordering semantics.
- Cache only with explicit key, lifetime, invalidation, tenant and deployment-model boundaries.
- Moving code across server/client boundaries can change privacy, freshness, CSP and hydration behavior.
- Dynamic/direct imports can change loading/error/offline behavior and may require packages/config.
- Do not install dependencies only to imitate an example.

Bundle/profiler/build/browser evidence can consume significant resources; remote telemetry can send project/user data.

Commit, rollout and deployment remain separate effects.
