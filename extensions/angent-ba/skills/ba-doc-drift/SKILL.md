---
name: ba-doc-drift
description: Specialized ANGENT business-analysis procedure for doc-drift.
---

# Evidence-based drift audit between specification and implementation

## Scope

Detect mismatches between an accepted specification and a pinned code revision with four distinct verdicts: ALIGNED, DIVERGENT, NOT IMPLEMENTED, and UNVERIFIABLE. Treat documentation and code as two separate evidence sources. Do not treat a missing search hit as proof of missing implementation.

## Examination

1. Resolve the actual accepted SRS version and target repository SHA, target service/branch and runtime. Read the feature's FR, BR, error matrix, API contract, linked AC and tests.
2. Build an inspection map by business action: entrypoints, guards, domain services, data schemas, async consumers, frontend states, integration contracts and feature flags. Resolve dynamic routing and generated code.
3. For each requirement, follow the live implementation path and extract source-linked behavior. Record a minimal witness: file/line or symbol, condition, resulting state and unexecuted alternatives. Corroborate with tests or controlled runtime probe when possible.
4. Compare semantic predicates, not names. Check thresholds and units, timing, authorization, duplicate delivery, retry, error shape, external contracts and state persistence.
5. When the code path is unavailable (private dependency, remote service, runtime config, flag unknown), mark UNVERIFIABLE and name precise missing evidence. Do not mark NOT IMPLEMENTED solely because static search failed.
6. Cross-check testing: a passing mocked test does not establish real external integration. Treat skipped tests, disabled checks and fallback code explicitly.
7. For every mismatch, propose one bounded fix owner: update implementation, amend spec by stakeholder decision, or gather more evidence. Changes need separate authorization.
8. Produce a reviewable register ordered by consequence and traceability, including reproduction or next test.

## Finding record

```text
FR-ID: FR-PAY-008
Spec: duplicate capture request must return original transaction ID
Code: services/payments/capture.ts:46-63 @ SHA
Observed: idempotency key is generated per attempt
Status: DIVERGENT (code inspection, not deployed runtime)
Impact: duplicate charge risk under retry
Next check: mock + sandbox payment retry test
```

The example is *illustrative* and does not cite an actual inspected repository file.

## Gates

No invented code references, no unsupported production-deployed conclusions, no automatic spec rewrite, and no false test pass. Review uncovered requirements and report denominator/scope.


## ANGENT cooperation

ANGENT Root/Reasoning owns interpretation and decisions; Authoring owns narrative quality; Execution handles authorized external effects; Quality verifies the outcome. Method selection is optional and context-dependent, never a forced workflow.
