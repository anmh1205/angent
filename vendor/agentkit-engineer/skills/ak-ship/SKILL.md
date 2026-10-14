---
name: ak-ship
description: Move a verified feature branch through repository delivery gates to an explicitly authorized pull-request endpoint, with fresh Git/GitHub evidence and no hidden unrelated work.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# Ship — Portable Fallback

Use when implementation is ready to move from verified branch/worktree state into repository delivery.

Use `ak-review-pr` when the pull request already exists and needs review/repair/reply/merge handling. Use `ak-deploy` for application publication after repository/release gates.

Read `references/shipping-pipeline.md`.

## Boundary

“Ship” does not automatically authorize merge, deployment, release, or unrelated issue/project mutations.

Resolve the exact endpoint from Contract, for example:
- branch prepared/committed;
- branch pushed;
- PR created/updated and ready;
- another explicitly named repository-delivery endpoint.

If the requested endpoint extends to merge, treat that as an explicit consequential effect with current repository policy/provider evidence; do not infer it from “ship”.

Deployment is separate unless explicitly included through its owning workflow.

## Working-tree preflight

Inspect branch, base, tracked/untracked changes, and every worktree-visible modification that the shipping pipeline would stage/include.

If unrelated work is present:
- do not silently include it;
- do not silently discard/stash/move it;
- isolate/reconcile it through an authorized safe route before shipping.

The ship candidate should represent the complete intended branch change, not a selectively hidden subset.

## Pipeline

1. Reconcile branch/base and intended changed scope.
2. Run required verification for the requested repository gate.
3. Ensure material review findings are resolved.
4. Revalidate staged content/secret policy.
5. Create coherent commit/history through the repository's accepted Git workflow.
6. Push only when push is inside current authority.
7. Create/update PR only when that provider write is inside the endpoint.
8. Observe required checks/reviews from provider state.
9. Stop at the requested verified repository-delivery endpoint.

If later merge/deploy work is requested, enter the owning workflow/gate with fresh authority and provider state.

## Convergence

Do not stop merely because:
- a commit exists;
- a branch pushed;
- the PR was created;
- CI started;
- one check is green.

When a gate fails and a safe authorized repair path exists:
- diagnose/fix through the owning workflow;
- rerun materially affected verification;
- update the branch/PR when authorized;
- observe the gate again.

Stop at verified endpoint, genuine external blocker, required decision, or authority boundary.

## Safety

Do not bypass branch protection, required review, security policy, or release controls.

A feature-branch ship pipeline must not rewrite protected/shared history merely to converge.
