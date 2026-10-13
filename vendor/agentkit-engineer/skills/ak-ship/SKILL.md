---
name: ak-ship
description: Move a verified change through the repository's delivery gates toward the explicitly authorized PR/merge endpoint, with fresh provider checks and failure convergence.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# Ship — Portable Fallback

Use when implementation is ready to move from verified working-tree/branch state into repository delivery.

Read `references/shipping-pipeline.md`.

## Boundary

“Ship” does not automatically authorize merge, deployment or public release.

Resolve the exact endpoint from Contract, for example:
- pushed branch;
- PR created;
- PR ready with checks/review satisfied;
- merged;
- post-merge CI verified.

Deployment/release is a separate effect unless explicitly included.

## Pipeline

1. Reconcile branch/base and changed scope.
2. Run the required verification for the requested gate.
3. Ensure material review findings are resolved.
4. Create coherent commits/history.
5. Push the intended branch.
6. Create/update PR and linked issue state when in scope.
7. Observe required checks/reviews from provider state.
8. If the endpoint includes merge, merge only when authorized and gates are satisfied.
9. If required, observe post-merge checks/state before claiming completion.

Use the project's established Git/GitHub/provider workflow.

## Convergence

Do not stop merely because:
- the branch pushed;
- the PR was created;
- CI started;
- one check is green.

When a gate fails and a safe authorized repair path exists:
- diagnose/fix through the owning workflow;
- rerun materially affected verification;
- update the branch/PR;
- observe the gate again.

Stop at verified endpoint, genuine external blocker, required decision, or authority boundary.

## Safety

Do not bypass branch protection, required review, security policy or release controls.

Do not include unrelated local changes in a shipping commit.
