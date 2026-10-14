---
name: ak-code-review
description: Review a diff, pull request, commit, pending workspace, or codebase independently for production risk, requirement fit, edge cases, and verification gaps.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# Code Review — Portable Fallback

Code Review is independent technical judgment, not a second implementation pass or a rubber stamp.

## Review contract

Establish:
- exact review target/base/head;
- implementation intent, plan/spec/acceptance criteria;
- applicable `AGENTS.md`;
- changed surface and indirect consumers;
- fresh evidence/tests already available;
- whether the task is review-only or fixes are separately authorized.

Do not assume the diff alone contains the whole affected behavior.

## Core passes

### 1. Specification / behavior

Check:
- missing or contradicted requirement;
- wrong state transition/interface;
- migration/config compatibility;
- authorization/security boundary;
- error/edge path;
- affected consumer.

### 2. Production-risk quality

Inspect only material risk:
- correctness/concurrency/resource lifecycle;
- validation and error handling;
- security/privacy;
- observability/recovery;
- maintainability where it changes defect risk;
- performance when material;
- test adequacy.

Do not inflate the report with style nits.

## Edge-case scouting

For cross-layer/shared/stateful/async/security-sensitive changes, inspect callers, analogous paths, schema/config, failure paths, and untested boundaries.

For a genuinely isolated trivial diff, do not add a ceremony-only scout pass.

## Review strategies

- ordinary target review is the default;
- codebase-parallel review is valid only when scopes are independent and the runtime can execute the required strategy honestly;
- **ultra** is a stronger multi-reviewer evidence strategy and must fail closed when its required independent candidate pool cannot be produced; do not silently replace missing reviewers with sequential/self-review and still call the result ultra;
- do not combine mutually exclusive strategies such as ultra with another strategy that owns the same multi-reviewer phase;
- **advice** may add advisory checkpoints when that route is actually available;
- **yagni** allows scope-cut findings where unnecessary work is itself the risk; without it, accepted requested scope remains a constraint unless unsafe/broken/duplicative.

When exact current flags or reviewer-count mechanics matter, inspect the installed stable Skill/help rather than reconstructing them from memory.

## Evidence and findings

Do not trust:
- implementer summary;
- worker “done” claim;
- lint alone as runtime proof.

Read the code and relevant surrounding behavior. Run/inspect targeted verification when it can confirm or reject a finding.

A material finding contains:
- severity proportional to consequence;
- exact location/scope;
- mechanism;
- concrete consequence;
- evidence/reproduction path;
- bounded remediation direction when useful.

Unverified confidence is a review gap, not a high-confidence defect.

## Fix authority

Review-only means no silent code edits.

If fixes are authorized, establish the review result first, then hand accepted findings to the implementation/fix owner. Keep reviewer and fixer responsibilities conceptually distinct.

## Verdict

Return:
- reviewed scope;
- material findings;
- uncertain/rejected findings when useful;
- verification performed;
- coverage limitations;
- readiness verdict relative to the requested gate.

“No findings” means no material findings were established in the reviewed scope. It does not prove unreviewed scope clean.
