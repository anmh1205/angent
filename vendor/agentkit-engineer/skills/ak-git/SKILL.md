---
name: ak-git
description: Perform disciplined Git history, branch, staging, commit, push and merge operations without hiding unrelated work or unsafe history rewrites.
metadata: {port: angent-fallback, mode: portable}
---

# Git — Portable Fallback

## Load progressively

- `references/commit-boundaries.md` — coherent staging and commit design.
- `references/history-safety.md` — rebase/merge/force-push/shared-history safety.

## Workflow

1. Inspect branch, status and diff.
2. Separate unrelated work.
3. Stage a coherent unit.
4. Scan staged content for accidental secrets/sensitive files.
5. Use project commit conventions.
6. Verify the commit contains exactly the intended change.
7. Push/rebase/merge only within current authority.
8. Report exact branch/commit state.

A commit is intermediate evidence unless the Contract defines it as the endpoint.
