# Test execution workflow

## 1. Resolve the acceptance surface

Determine what evidence is needed from:
- requested behavior/bug;
- changed interfaces/state;
- applicable plan/spec;
- repository CI/release gates.

Examples:
- new feature → focused new tests + relevant regression/build evidence;
- bug fix → reproduce old failure + regression test + fix verification;
- refactor → existing behavior protection + affected consumer checks;
- release gate → repository-defined required suites/checks.

## 2. Discover project commands and environment

Prefer:
- `AGENTS.md`;
- package/build config;
- CI workflows;
- existing test scripts;
- fixture/setup documentation.

Do not invent generic commands or thresholds when the project already owns them.

## 3. Pre-flight where useful

Run cheap compile/type/static checks when they can reject an invalid candidate before expensive suites.

Examples are project-specific: TypeScript typecheck, Python compile/lint, Go vet, Rust check, Flutter analyze, etc.

Do not treat these as runtime/behavioral verification unless they actually establish the requested claim.

## 4. Execute tests

Choose the narrowest meaningful set first.

Widen based on:
- changed public/shared interface;
- cross-layer behavior;
- migration/schema impact;
- release/merge requirements;
- failures that expose a larger blast radius.

Preserve exact failing output/identity needed for diagnosis.

## 5. Distinguish which layer the evidence actually reaches

When a claim crosses boundaries, start with a small causal trace: triggering input → producer/state transition → serialization or API → receiving layer → user-visible or device-visible result. Ask which invariants each check covers and what failure could pass despite a green result. A serializer unit test might pass while the deployed consumer expects a different schema; a cloud handler test can pass while a device silently drops records; a browser test on mock responses can pass while production authentication fails. Choose an integrated/contract observation where the missing guarantee matters.

If a target environment is absent, a contract fixture, simulation or local replay may establish **partial** compatibility evidence but must not be renamed a field/device or production run. For hardware-facing work, distinguish simulated timing, electrical/peripheral drivers and real target behavior when timing or I/O affects the claim. Test selection should follow the actual risk and available system, not require all these layers for every small change.

## 6. Interpret results

Inspect:
- deterministic failures;
- flaky/intermittent behavior;
- skipped/xfail cases;
- slow/performance regressions when material;
- test isolation/shared-state pollution;
- environment/provider confounds.

A single run cannot establish a reliability rate for stochastic behavior.

## 7. Coverage

Use the project's accepted coverage policy when one exists.

When no threshold exists, do not invent a universal percentage. Inspect whether critical changed behavior, error paths and security/data mutations have meaningful protection.

Coverage percentage is supporting evidence; it is not proof of behavioral correctness.

## 8. Build/runtime verification

Run the project-native build or runtime smoke path when required by the acceptance gate.

Check for:
- dependency/config errors;
- production-only compilation/build failures;
- generated artifact drift;
- deprecation/warnings that are material to the requested gate.

## Quality conditions

- required tests/checks pass;
- no failing test is silently ignored;
- changed critical/error paths are exercised enough for the claim;
- test data/state is isolated/cleaned where relevant;
- environment conditions are stated when they affect validity;
- unresolved flaky/confounded results remain visible.
