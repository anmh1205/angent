---
name: ak-vibe
description: Orchestrate scoped issue-to-PR development with optional explicitly authorized beta/stable shipping, advisory gates and post-merge CI convergence.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# Vibe — Portable Fallback

Stable Engineer 2.19.0 Vibe is an **orchestrator** for request/issue → isolated worktree → plan → implement/fix → review → PR → optional merge and CI convergence. It must honor the called skills' approval, security, tests, branch and merge gates. Do not implement a duplicate task pipeline simply because a Skill is named Vibe.

Read `references/pipeline-state.md` and `references/modes-and-safety.md`.

## Inputs and intent

Accept an issue URL or feature description with optional native-like modes:
- default: work through stable PR readiness, **do not merge**.
- `--beta`: beta/dev PR readiness target.
- `--ship`: optional merge/post-merge CI convergence **only when concretely authorized** by user and repo policy.
- `--both`: explicitly authorized two-stage beta then stable progression, with beta CI green/accepted before stable promotion; implicitly requests shipping behavior but **cannot override user prohibition on merging**.
- `--advice`: independent hard-decision/advisory review through a genuinely available Kongming-equivalent route; not an invented second model or automatic approval.

Mode and target branch must be resolved against current repo and the user's **latest** branch/merge instructions. If a user says 'do not merge', neither `--both` nor a historical default may silently merge.

## Execution sequence

1. Recover real issue/goal, acceptance criteria, repo/ref, current work and permission scope. Confirm target branch; never infer the active user work from the last branch you happened to inspect.
2. Create an isolated worktree/branch only when authorized and supported, preserving unrelated working tree state.
3. Plan nontrivial change with sources, ownership and dependency/rollback gates; keep a minimal resumable frontier.
4. Implement or fix within owned scope; use current tooling without bypassing tests, security or actual code-review blockers.
5. Verify meaningful unit/integration/system behavior and acceptance; code review the actual patch/diff with actionable findings, then repair and re-verify.
6. Create/update an authorized PR using the real provider. Inspect its CI status, review comments and changed files; fix legitimate issues and reply with evidence. A 'ready to ship' label is a status claim only when gates are fulfilled.
7. When the user explicitly authorizes merge: verify base/head, branch protection and required approvals again, merge only the intended PR and watch actual post-merge CI. For a failing run, use a fresh bounded fix branch and read failure logs before a follow-up PR; never amend or reset unrelated branch history to force green.
8. Dual-stage shipping: complete and verify beta stage **before** stable PR. Preserve artifact/commit lineage so stable release contains the tested changes; stop on unresolved blockers instead of advancing.
9. Report actually observed endpoint, PR(s), CI, commits, artifacts, remaining gates and rollback/recovery. Do not call 'complete' because a PR was opened or a status label was applied.

## Native-first and host boundary

Prefer native AgentKit Vibe only when its real CLI/skill runtime is available and its effects are permitted. Otherwise reuse ANGENT's Contract → Context → Execution → Quality/Continuity with the corresponding real repo tools. If no PR/merge tool is available, report the boundary; do not manufacture a PR link.

Vibe completion is measured by accepted user outcome and explicitly requested Git endpoint, **not** automatic shipping.
