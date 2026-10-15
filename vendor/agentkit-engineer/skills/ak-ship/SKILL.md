---
name: ak-ship
description: Move a completed branch through repository delivery gates to an authorized push/PR/merge endpoint, with official/beta/dry-run modes and optional explicitly gated publication side effects.
license: MIT
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Ship — Portable Fallback

Use when implementation is ready to move from verified branch state into repository delivery.

Read `references/shipping-pipeline.md`.

## Endpoint and mode

Resolve the requested endpoint first:
- pushed branch;
- PR created/updated;
- PR ready with required checks/review;
- merged;
- post-merge CI verified.

Deployment is separate unless explicitly included.

Preserve useful stable modes:

- **official** — target the repository's official/default release branch and include required docs/release metadata gates;
- **beta** — target the project's dev/beta branch when such a branch actually exists; do not invent one;
- **auto** — infer only from reliable repository/branch evidence; ask when ambiguous;
- **dry-run** — report the resolved pipeline/effects without mutating anything.

Optional skip-tests/skip-review/docs/journal behavior is honored only when explicitly requested and compatible with repository/Contract gates. A convenience skip flag cannot bypass required provider/branch protection or a user-required acceptance gate.

## Preflight

Reconcile:
- canonical repo/current branch/base/remote;
- dirty/unrelated work;
- changed scope and linked issues/plan;
- required tests/builds;
- review status;
- sensitive files/secrets;
- version/changelog/docs impact.

Unlike the pinned package's aggressive convenience default, do **not** automatically include unrelated uncommitted changes.

## Pipeline

1. Update/reconcile target-base state without discarding user work.
2. Run required tests unless explicitly and validly deferred.
3. Run required independent review unless explicitly and validly deferred.
4. Apply version/changelog/docs changes only when owned by this release flow.
5. Reconcile plan/task state when the branch is plan-backed.
6. Create coherent commit(s) and push the intended branch.
7. Create/update the PR with evidence/linked work.
8. Observe required provider checks/reviews.
9. Merge only if merge is part of current authority and provider gates are satisfied.
10. Observe required post-merge CI/state.

## Optional public/social publication

Public build-in-public/social posting is a separate external/publication effect.

Only perform when explicitly requested. Preview/dry-run content before publication when appropriate. For a private repository, require explicit authority to disclose non-public work.

Never quote or publish untrusted external comments/credentials/private data merely because they appear on the PR.

Social publication is not required for Ship completion.

## Convergence

If a gate fails and a safe authorized repair path exists:
- diagnose through the owning workflow;
- repair the causal issue;
- rerun materially affected verification;
- update branch/PR;
- observe the gate again.

Do not tight-poll provider checks while independent useful work remains.

## Safety

- never blind force-push;
- do not bypass required review/branch protection/security controls;
- do not silently bump a semantic version when version policy requires a user decision;
- do not include unrelated local changes;
- do not treat PR creation as merged/released.

## Completion

Stop at the exact verified endpoint, a genuine provider blocker, required decision, or authority boundary.
