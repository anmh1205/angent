# Designing, auditing, and optimizing effective test suites

Test work is a reasoning task. Establish what production behavior is promised, how it can fail, which observation would detect the failure, and what the available testing environment can truly reproduce. Use the project-native test framework, CI pipeline and owners; this Skill does not recreate `ak test`.

## Create missing tests

First reconstruct the requirements and actual code/test boundaries. Map a small set of **distinct failure mechanisms** (incorrect state transitions, incompatible contracts, invalid data, authorization, timeout/cancellation, concurrency, persistence or hardware behavior when relevant) to the narrowest trustworthy test layer. Preserve or improve existing test patterns rather than generating an unrelated test framework.

For each added test, ask **what wrong implementation would pass it?** If the answer includes the plausible regression of interest, improve the test: exercise the real condition, assert an observable result or use a contract fixture from the real peer. If safe, prove test sensitivity by a controlled failing implementation in an isolated workspace; restore all modified product files before accepting the test. Do not inject a fault into a shared or production environment.

For cross-layer behavior, a mock is useful for local isolation but cannot establish real peer compatibility without a separately grounded contract or integrated observation. When the target hardware/cloud/provider cannot be exercised, state the simulation/fixture boundary rather than claiming end-to-end coverage.

## Audit a suite's trustworthiness

Inspect more than passing counts. A test may be green because it never reached the condition, asserts its own mock, ignores exceptions, uses stale snapshots, leaks shared state, is skipped, or checks an obsolete specification. Trace the actual test setup → action → assertion and the production behavior it claims to prove. For a material suspected weak test, demonstrate why a plausible invalid implementation could still pass it or locate concrete contrary source/runtime evidence.

Differentiate **product defect**, **test defect**, **test environment/confound** and **unresolved attribution**. A production change should not be made merely because a test is wrong. Audit normally produces findings; test/CI repairs require the user's requested effect authority, and product fixes return to Debug/Fix or Cook as appropriate.

Use mutation-style experiments only on an isolated throwaway worktree/fixture with rollback verified. If cleanup fails, stop the dependent mutation path and report the altered state. An unexecuted thought experiment is a review hypothesis, not observed mutation coverage.

## Optimize without erasing evidence

Identify whether the bottleneck is test execution, environment setup, redundant jobs, CI queue, flaky retries, fixture contention or needless full-suite reruns. Measure the baseline in the same relevant context before and after where feasible; otherwise report an unverified proposal rather than an established speedup.

Preserve hard safety and release gates, critical integration tests and tests for changed high-fan-out contracts. If selecting tests from a diff, account for indirect consumers, renamed files, generated code, schema changes and stale test-impact mappings. When selection confidence is insufficient, **widen** to the required full suite rather than treating unknown impact as zero. Compare false-negative risk and operational cost, not runtime alone. Parallelism helps only when resources, shared test state and dependency ordering make it safe.

External semantic providers, test-impact backends, parallel agents and their costs/telemetry exist only when actually available and authorized. Do not claim a native optimizer or shadow AI evaluation ran because the Skill describes these methods.

## Optional advisory and independent comparison

When multiple analyses could materially improve a difficult test-suite decision, an actually available independent reviewer may compare assumptions and evidence. An advisor has no authority to mutate or certify the tests. User-requested approval/interview mode means pause at the material test/CI change decision, not after every fixture. If the user explicitly requests native `--ultra`-style independent parallel candidates, do not substitute sequential copies and call it equivalent; require a runtime with the requested independent capability or report that particular mode unavailable while preserving the normal single-agent method.

## Transfer examples

- **Create:** an API rejects expired sessions. A test that merely asserts the mocked auth service returned "expired" does not prove the API rejects the request; test the application boundary and relevant response contract.
- **Audit:** a green test catches and discards all exceptions, then asserts a value unaffected by failure. Identify the missing observable error assertion and verify the original intended behavior before editing it.
- **Optimize:** a quick PR test selector skips integration checks after a shared schema change. Even if past CI appears fast and green, preserve mandatory integration checks or broaden impact selection until the consumer contract is verified.
- **Counter-case:** a local documentation typo cannot justify generating a new integration suite or running a full benchmark. Do only the tests that support the requested change, if any.
