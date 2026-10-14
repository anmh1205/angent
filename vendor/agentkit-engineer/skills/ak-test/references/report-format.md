# Test report semantics

A test report should make the acceptance evidence inspectable without forcing one rigid template.

## Include what matters

Depending on the job, preserve:
- scope/acceptance question;
- environment or target identity when material;
- commands/tools actually used;
- test/build/type/lint outcomes;
- failed checks with enough evidence to reproduce or investigate;
- coverage evidence and **the policy/threshold source**, when coverage is relevant;
- UI/browser artifacts and what each proves;
- tests created/changed/removed and why, when mutation was authorized;
- flaky/noisy/environment failures separately from product failures;
- evidence gaps and unverified states;
- final verdict limited to the tested scope.

## Coverage reporting

Never inject universal 80/70/etc. thresholds.

If a project/task defines a threshold, name its source.

If no threshold exists, report observed coverage and risk-relevant gaps without inventing a PASS/FAIL policy.

## Failure detail

Preserve exact failure identity and the evidence needed for diagnosis, but avoid dumping enormous logs into the main report.

Use pointers/artifacts for large traces.

Do not state “cause” unless the evidence establishes a cause; otherwise report the observed failure and current hypothesis/attribution status.

## UI evidence

For visual/responsive/accessibility work, record:
- tested routes/states/viewports/interactions;
- screenshots/traces/reports where useful;
- console/network/accessibility evidence when material;
- what was not testable.

A screenshot path alone is not a visual verdict.

## Writing quality

Use clear technical prose and compact structure.

Do not sacrifice grammar, semantic boundaries, or uncertainty merely to make the report terse.

Do not depend on a hook-injected naming convention unless the active harness/project actually provides that convention.
