---
name: ak-review-pr
description: Review a pull request end to end against requirements, diff behavior, indirect consumers, tests and merge readiness; optionally publish/fix/merge only when authorized.
metadata: {port: angent-fallback, mode: adapted}
---

# Review PR — Portable Fallback

Use for a concrete PR or equivalent change set.

## Workflow

1. Read PR description, linked issue/spec and applicable AGENTS.md.
2. Inspect base/head and full diff.
3. Use Code Review semantics for correctness, edge cases and indirect consumers.
4. Inspect CI/test state and required checks.
5. Verify material findings before reporting them.
6. Produce a readiness verdict.

## Optional actions

Only when authorized:
- post review comments/verdict;
- apply accepted fixes;
- update branch;
- merge;
- monitor required post-merge CI.

Do not hard-require `gh`; use the active GitHub connector/API/CLI capability.

A green CI run does not override a material review finding, and a review pass does not prove post-merge deployment health.
