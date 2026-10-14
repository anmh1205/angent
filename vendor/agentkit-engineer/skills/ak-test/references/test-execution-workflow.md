# Test execution workflow

Testing starts from the acceptance claim, not from a universal suite or coverage target.

## 1. Resolve the operation

Determine whether the job is:
- focused/broad validation;
- new test coverage for accepted behavior;
- test-suite audit/repair;
- CI/runtime optimization while preserving signal;
- UI/browser/accessibility validation;
- build/type/lint/coverage evidence.

Establish the relevant environment and whether test-source edits are authorized.

## 2. Discover project-native evidence

Inspect project instructions, package/build configuration, CI workflow, test directories, and known-good commands.

Prefer project-native checks. Do not add a new test framework or dependency merely because a generic example uses one.

## 3. Preflight only when useful

Syntax/type/lint/build preflight can catch failures cheaply, but it is not universally required before every test.

Choose ordering by:
- cost;
- expected information value;
- project convention;
- dependency on generated/build artifacts.

## 4. Execute proportionally

Run the smallest checks that can establish or falsify the current claim.

Widen when:
- an interface/shared dependency changed;
- failures expose wider impact;
- release/merge policy requires it;
- the Contract promises broad coverage.

For UI/browser behavior, use the dedicated UI workflow and actual visual/runtime evidence when required.

## 5. Interpret results

Separate:
- product defect;
- test defect;
- flaky/noisy result;
- environment/configuration/provider failure;
- missing prerequisite;
- unresolved attribution.

A failing test is not automatically the root cause.

A passing test establishes only the behavior/environment/assertions it actually exercised.

## 6. Coverage

Use the project's accepted coverage policy or task-specific threshold when one exists.

Do **not** invent universal line/branch/function percentages.

Coverage helps find unexercised code; it does not prove behavior outside the assertions or runtime conditions.

Prioritize coverage gaps by risk and promised behavior, especially critical error/authorization/data-mutation paths.

## 7. Build and delivery checks

Run build/package checks when the requested gate requires them.

Warnings/deprecations are findings only when they violate the current quality/release contract or represent material risk; do not fail work from generic warning-count rules.

## Completion

Report what was executed, what changed if test files were edited, outcomes, material failures, limitations, and whether the original acceptance claim is established.

Do not convert a green command into a broader PASS than its evidence supports.
