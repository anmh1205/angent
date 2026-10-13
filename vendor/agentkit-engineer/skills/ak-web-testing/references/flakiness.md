# Test flakiness

Do not solve flaky tests by raising retry count first.

## Classify

Common causes:
- race/timing;
- shared mutable state;
- order dependence;
- unstable external dependency;
- animation/render settling;
- non-deterministic data;
- environment/resource contention.

## Diagnose

Re-run with:
- isolated test;
- repeated iterations;
- trace/log capture;
- controlled data/time;
- reduced concurrency.

Fix the synchronization/state contract where possible.

Retries are acceptable for a genuinely unreliable external boundary when the product itself also tolerates that boundary and the retry policy is explicit.
