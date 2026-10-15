---
name: ak-fix
description: Repair a concrete software failure from bounded intent through scout, root-cause diagnosis, cause-aligned implementation, regression/side-effect verification and review.
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Fix — Portable Fallback

Use for a concrete bug, error, failing test, CI failure, type/lint defect, runtime/log failure, or UI behavior that needs a code/config repair.

Use Debug instead when diagnosis is the endpoint. Use Cook for feature/refactor delivery.

## Load progressively

- `references/failure-routing.md` — choose quick/standard/deep/parallel route from evidence.
- `references/repair-verification.md` — original-path, blast-radius, contract and prevention evidence.

## Repair contract

Before solution selection, establish or reuse:
- expected repaired behavior;
- exact observed symptom;
- constraints and compatibility/safety boundaries;
- non-goals;
- acceptance evidence;
- Git/provider/production effect authority.

Do not choose a fix merely from the complaint text.

## Modes

- **auto** — default for ordinary repairs; continue through routine authorized steps, but user-owned decisions/authority boundaries still stop.
- **review** — surface meaningful diagnosis/repair/review gates for production/security/public-contract-sensitive work.
- **quick** — trivial/local deterministic defects; scout/diagnose are smaller, never skipped.
- **parallel** — only for two or more independent failures or truly disjoint evidence/repair branches with explicit ownership.
- **advice** — optional independent advisory review at high-risk/stuck points; advisor never owns implementation or bypasses gates.

Modes alter collaboration and effort, not the requirement to establish cause and verify the repair.

## 1. Scout before solution

Inspect enough current state to establish:
- project/runtime type;
- exact failure surface and owning path;
- direct callers/dependents;
- related tests;
- recent changes when "why now" matters;
- existing implementation conventions.

Use `ak-scout` semantics when ownership/flow is not already clear.

Quick mode may keep this narrow. It still does not authorize guess-and-patch.

## 2. Diagnose

Before a non-trivial fix, establish as concretely as the evidence allows:

1. exact symptom/observation;
2. minimal reproduction;
3. expected vs actual;
4. root-cause mechanism and earliest correct owner;
5. triggering condition/change when material;
6. blast radius / code paths sharing the cause.

Use `ak-debug` when competing hypotheses remain.

If material items remain unknown, gather discriminating evidence rather than writing a speculative patch.

## 3. Route by repair complexity

- **direct/quick** — cause established, bounded owner, straightforward verification;
- **standard** — multi-file or non-trivial blast radius but one accepted direction;
- **deep** — repair exposes architecture/product choice; return to Brainstorm/Plan/Reasoning before coding;
- **parallel** — independent issues/branches only, with separate ownership and integrated verification.

Repeated failed repair attempts are evidence the current model may be wrong. Stop equivalent patching and revisit diagnosis/architecture instead of treating another attempt as progress.

## 4. Implement cause-aligned repair

Change the smallest causal scope.

Preserve:
- non-goals;
- public/shared contracts unless an explicit decision changes them;
- unrelated accepted behavior;
- user work outside the repair.

Do not suppress an error, retry a deterministic defect, weaken a test, or add a consumer-side workaround when the producer/earlier owner is the established cause unless evidence justifies that boundary.

## 5. Verify and prevent recurrence

Fresh verification must cover as relevant:

- original pre-fix reproduction no longer fails;
- a regression test/guard captures the fixed bug class when practical;
- affected/transitive blast-radius tests/flows still work;
- public API/schema/env/state contracts are unchanged or intentionally reconciled;
- type/lint/build/integration/UI/runtime checks required by the affected surface;
- no new material side effect/regression.

If verification reveals a side effect whose resolution changes accepted behavior or scope, return to Reasoning/user decision rather than silently patching dependents.

## 6. Independent review and finalize

For material repairs, use Code Review semantics to check:
- root cause actually addressed;
- blast radius preserved;
- no new failure mode;
- project conventions/acceptance preserved;
- verification is strong enough for the claim.

Reconcile plan/task/Continuity state when used.

Commit/push/PR/deploy are separate effects unless explicitly requested.

## Completion

Report:
- established root cause;
- repaired causal scope;
- changed artifacts;
- regression/prevention evidence;
- blast-radius verification;
- review status;
- residual uncertainty/deferred work.

A green test that does not exercise the original failure is not proof that the bug is fixed.
