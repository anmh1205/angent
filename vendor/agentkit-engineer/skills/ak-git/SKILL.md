---
name: ak-git
description: Perform disciplined Git commit, push, PR, merge, merge-PR and stacked-PR operations without hiding unrelated work, secrets or unsafe history rewrites.
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Git — Portable Fallback

Git owns repository-history mechanics. Provider-wide issue/Actions/admin work belongs to GitHub.

## Load progressively

- `references/commit-boundaries.md` — staging and coherent commit design.
- `references/history-safety.md` — rebase/merge/rewrite/delete safety.
- `references/operations.md` — commit/push/PR/merge/merge-PR/stacked-PR semantics.

## Operations

Support the useful stable workflow surface:

- **commit** (`cm`) — stage selected/coherent changes and commit;
- **commit + push** (`cp`) — commit, then push the intended branch;
- **PR** (`pr`) — create/update a PR from resolved source/base;
- **merge** — merge branches when authorized;
- **merge PR** — provider-readiness-gated PR merge plus required post-merge CI observation;
- **stack** — stacked-PR lifecycle only when the active provider/tooling exposes it safely.

If the request is ambiguous and current context does not identify the operation, ask/select once rather than guessing a history mutation.

## Common preflight

Before mutation:
1. resolve canonical repository/worktree;
2. inspect branch, status, upstream and relevant diff;
3. separate unrelated user work;
4. resolve exact operation/base/head/remote;
5. scan the intended staged/pushed content for accidental secrets/sensitive files;
6. revalidate current authority.

Do not use `git add -A` as a universal policy when unrelated work exists.

## Commit

Create reviewable commits around one coherent reason for change while preserving atomic migrations when splitting would create a broken intermediate state.

Use project commit conventions. Verify the staged diff before commit and the resulting commit afterward.

## Push/rebase/merge

- protect shared/protected history;
- do not blind force-push;
- use force-with-lease semantics only when rewriting is explicitly authorized and appropriate;
- resolve conflicts from actual file/state evidence;
- do not discard unrelated local work to "get clean".

## PR / merge-PR

Use current provider state for base/head/checks/reviews.

Creating a PR is not merge completion. Merge only when explicitly in scope and provider gates are satisfied. Observe required post-merge state before claiming a merged-and-green endpoint.

## Stacked PRs

Use only when the live Git/provider surface actually supports a stacked-PR lifecycle.

Preserve:
- stack ordering/dependencies;
- base/head relationships;
- safe rebase/sync;
- user gates for history rewriting and multi-PR merge.

If stacked tooling is unavailable, report that capability boundary; do not emulate a stack with unsafe ad-hoc force pushes.

## Result

Return exact repository/branch/commit/PR state and any unresolved conflict/gate.

A commit or push is intermediate evidence unless it is the requested endpoint.
