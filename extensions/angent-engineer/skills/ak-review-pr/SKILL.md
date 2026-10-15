---
name: ak-review-pr
description: Review one or more pull requests end to end; optionally repair, publish a formal review, or merge only after explicit authority and fresh readiness evidence.
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Review PR — Portable Fallback

Use for an existing GitHub pull request or equivalent provider change set.

Default mode is **review-only** and therefore read-only.

## Modes

- **review** — inspect and report findings/readiness only.
- **fix** — repair accepted findings on the PR branch, then retest and re-review.
- **reply** — publish the final review/comment through the provider.
- **merge** — merge only after review/fix/reply requirements and merge-readiness gates pass, then verify required post-merge CI/state.

Modes may compose only when authority covers each effect. Review authority does not imply branch-write, review-posting or merge authority.

## Preflight

For each PR:
- resolve exact repository/PR identity;
- read description, linked issue/spec and applicable `AGENTS.md`;
- establish base/head and current provider state;
- inspect the complete diff plus relevant full files/consumers;
- inspect required checks/reviews/branch protection;
- preserve unrelated user work when fix mode is requested.

Do not review a stale cached diff when fresh provider state is available.

## Review

Use Code Review semantics:
1. spec/acceptance compliance;
2. changed behavior and state transitions;
3. indirect consumers/edge/error paths;
4. security/public-contract/migration risks;
5. test/build/CI evidence;
6. material findings verified before reporting.

A green CI run does not override a verified material defect.

## Fix loop

Only with fix authority:

1. establish the initial findings first;
2. change the smallest causal scope on the PR branch;
3. run materially affected tests/checks;
4. re-review repaired scope and relevant blast radius;
5. repeat only while new evidence converges.

Repeated non-converging cycles return to Reasoning/Debug rather than patching indefinitely.

## Reply

Only with provider review/comment authority.

Build the review body from the verified final findings/verdict. Avoid duplicate provider posts when the same review state was already published.

If the provider prevents self-approval/formal review, degrade honestly to an allowed comment/status route instead of fabricating approval.

## Merge

Only with explicit merge authority and when:
- no blocking findings remain;
- required checks are terminal-green;
- required reviews/branch protection are satisfied;
- base/head are current enough to merge safely.

After merge, observe required post-merge CI/provider state before claiming a merged-and-green endpoint.

Merge does not imply deployment/release health.

## Multiple PRs

Treat each PR as an independent provider object with its own base/head, findings, effects and endpoint evidence. Do not let one green PR certify another.

## Provider boundary

Do not hard-require `gh`; use the active GitHub connector/API/CLI capability.

If the required provider effect is unavailable, stop at the strongest verified read-only result.

## Final result

Return:
- PR identity/base/head;
- review scope;
- material findings and repairs;
- verification/check state;
- review-post state if requested;
- merge/post-merge state if requested;
- residual blockers/uncertainty.
