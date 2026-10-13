---
name: ak-code-review
description: Review software changes independently against requirements, AGENTS.md, system behavior, edge cases, and fresh verification evidence; report only actionable findings with clear impact.
license: MIT
metadata:
  author: ANGENT fallback
  port: angent-fallback
  inspired-by: AgentKit Engineer ak-code-review
---

# Code Review — Portable Fallback

Code Review is an independent technical judgment, not a second implementation pass and not a rubber stamp.

The reviewer checks whether the change satisfies the intended behavior without introducing material defects.

This fallback does not require AgentKit CLI, a dedicated reviewer subagent, or a specific task-management surface.

## Load references progressively

- `references/review-scope.md` — determine baseline, requirements, affected surface, and what is actually under review.
- `references/edge-cases-and-impact.md` — inspect indirect consumers, boundary/error/concurrency/security cases.
- `references/finding-quality.md` — write evidence-backed, actionable findings.
- `references/verification-and-verdict.md` — use fresh evidence and produce a defensible final verdict.
- `references/parallel-review.md` — use multiple reviewers only when scopes are genuinely independent.

## Establish the review contract

Identify:
- what changed;
- baseline versus head/current state;
- requirements/plan/acceptance criteria;
- applicable `AGENTS.md`;
- files and indirect consumers in scope;
- tests/evidence already available;
- whether the user asked only for review or also authorized fixes.

Do not assume the diff alone contains the full affected surface.

## Review in two passes

### Pass 1 — behavior/spec compliance

Check whether the implementation actually satisfies the intended behavior:
- missing requirement;
- wrong state transition;
- incompatible interface;
- incorrect error/edge path;
- broken authorization/security boundary;
- stale or partial migration;
- unhandled consumer.

### Pass 2 — implementation quality

Then inspect relevant quality risks:
- correctness;
- concurrency;
- resource lifecycle;
- validation;
- maintainability where it affects defect risk;
- test adequacy;
- observability/recovery;
- performance when material.

Do not flood the review with style nits that do not affect the requested quality bar.

## Scout edge cases when the change warrants it

For multi-file, shared-utility, cross-layer, stateful, async, security-sensitive, or complex bug-fix changes, inspect beyond the modified lines.

Use the available Scout capability or direct repository search to find:
- callers/consumers;
- data/control flows;
- related schema/config;
- error paths;
- untested boundaries;
- analogous code paths.

A one-line isolated change may not need a separate scout ceremony.

## Independent evidence

Do not trust:
- implementation author's summary;
- specialist “done” claim;
- passing lint as proof of runtime correctness.

Read the changed code and relevant surrounding code. Run/inspect targeted verification when it can confirm or reject a finding.

## Findings

A finding should contain:
- severity/importance proportional to impact;
- exact location;
- mechanism;
- concrete consequence;
- evidence or reproduction path;
- remediation direction when useful.

Do not report speculative defects without enough evidence to make them actionable.

## Fix authority

If the task is review-only, do not silently modify code.

If fixes are authorized, accepted findings can be handed to Execution after the review result is established.

Reviewer and fixer should remain conceptually separate even if the same model performs both sequentially.

## Final verdict

Return:
- reviewed scope;
- material findings;
- rejected/uncertain findings when important;
- verification performed;
- coverage limitations;
- readiness verdict relative to the requested gate.

“No findings” means no material findings were established in the reviewed scope. It does not prove unreviewed scope is clean.
