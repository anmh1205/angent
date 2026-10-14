---
name: ak-code-review
description: Review pending changes, commits, pull requests or codebase scope independently against requirements, system behavior, edge cases and fresh verification evidence.
license: MIT
metadata:
  author: ANGENT fallback
  port: angent-fallback
  mode: adapted
  inspired-by: AgentKit Engineer ak-code-review
  baseline: "AgentKit Engineer 2.19.0"
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

## Resolve the review target

Support the useful upstream target modes through whatever repository/provider capability exists:

- **pending** — staged/unstaged/current workspace changes;
- **commit** — one commit/range;
- **pull request** — provider PR diff plus relevant full files/metadata;
- **codebase** — bounded whole-codebase audit;
- **parallel codebase** — independent scoped reviewers only where ownership is separable.

If the target is ambiguous and cannot be inferred from the current task, ask once rather than reviewing the wrong surface.

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
- unhandled consumer;
- unjustified extra behavior.

Requested scope is a constraint, not a finding. Do not recommend cutting requested behavior merely to simplify the implementation.

### Pass 2 — implementation quality

Then inspect relevant quality risks:
- correctness;
- concurrency;
- resource lifecycle;
- validation;
- maintainability where it affects defect risk;
- test adequacy;
- observability/recovery;
- performance/security when material.

Do not flood the review with style nits that do not affect the requested quality bar.

## Scout edge cases when warranted

For multi-file, shared-utility, cross-layer, stateful, async, security-sensitive, or complex bug-fix changes, inspect beyond the modified lines.

Look for callers/consumers, data/control flow, schema/config, error paths, untested boundaries and analogous implementations.

A one-line isolated change does not require parallel-review ceremony.

## Independent evidence

Do not trust implementation summaries, worker "done" claims, polished comments or happy-path tests as proof.

Read the changed code and relevant surrounding code. Run/inspect targeted verification when it can confirm or reject a material finding.

## Findings

A finding should contain:
- severity/importance proportional to impact;
- exact location;
- mechanism;
- concrete consequence;
- evidence/reproduction path;
- remediation direction when useful.

Do not report speculative defects without enough evidence to make them actionable.

## Fix authority

Review-only is read-only.

If fixes are authorized, establish the review result first, then hand accepted findings to Execution/Fix and re-review relevant repaired scope.

## Final verdict

Return:
- reviewed scope/target mode;
- material findings;
- rejected/uncertain findings when important;
- verification performed;
- coverage limitations;
- readiness verdict relative to the requested gate.

"No findings" means no material findings were established in the reviewed scope. It does not certify unseen scope.
