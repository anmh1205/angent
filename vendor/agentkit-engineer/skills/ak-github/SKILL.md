---
name: ak-github
description: Operate GitHub issues, PRs, Actions, Projects and repository administration through the best available GitHub API, connector or CLI capability.
metadata: {port: angent-fallback, mode: adapted}
---

# GitHub — Portable Fallback

Use the strongest available GitHub-native capability in the active harness; do not hard-require `gh`.

## Preflight and evidence

Before a write:
- resolve the exact repository/org/project;
- read current provider state relevant to the operation;
- detect duplicates/current status when that changes the action;
- preserve provider IDs/URLs returned by successful writes.

After consequential writes, read back state when completion matters.

## Issues

Search/deduplicate before creating when duplicates matter.

Preserve evidence, acceptance criteria and links to code/artifacts.

For updates, avoid overwriting unrelated user-authored issue content.

## Pull requests

Inspect base/head, diff/checks/reviews and linked requirement/issue.

Create/update/review/rebase/merge only within authority.

Do not infer merge readiness from one green check.

## Actions

Read exact workflow/run/job/log evidence.

Retry only when the failure mechanism makes retry sensible.

When a workflow is changed, distinguish validating the workflow definition from observing a real provider run.

## Projects

Use Projects as a coordination view when the user/project uses it.

Preserve links between project items and their underlying issue/PR when possible.

Do not let a board status override the actual issue/PR/artifact evidence.

## Administration

Repository/org/environment/branch-protection/secret operations have higher blast radius.

Confirm target and effect before mutation.

Never expose secret values; use provider secret-setting surfaces directly.

## Authority model

Provider state is authoritative for GitHub facts.

ANGENT Continuity records what work is being pursued and why; it does not replace GitHub's current repository/PR/issue state.
