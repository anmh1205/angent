# Coverage and endpoint verification

## Whole-scope claims

“Checked the project”, “all tasks are done”, “the book is consistent” and similar claims require coverage evidence proportional to the scope.

A deep sample can reveal a failure class but cannot prove uninspected units are clean.

For broad audits, maintain an explicit coverage ledger: declared scope, inventory source/completeness, inspected units, relevant inspected dimensions, skipped units, stale/recheck units and unresolved findings. When the audit spans turns/sessions, persist a durable coverage-ledger pointer through Continuity.

Before claiming full coverage, account for pagination/cursor exhaustion, top-N limits, truncation, filters and source version when those can hide units.

A first page, partial export or truncated result is not whole-scope evidence.

If a shared dependency changes after inspection, mark only affected units stale/recheck.

## Endpoint hierarchy

Separate:
- action attempted;
- action returned success;
- intermediate artifact/state changed;
- implementation/draft exists;
- relevant checks/tests passed;
- requested endpoint verified.

Examples:
- commit created ≠ feature done;
- page update API succeeded ≠ page rendered correctly;
- code written ≠ task acceptance satisfied;
- worker says tests passed ≠ the relevant test result was directly observed;
- document drafted ≠ destination artifact verified.

When the distinction matters, report state precisely:
- **drafted** — candidate content/artifact exists;
- **implemented** — requested change exists in the implementation/artifact;
- **checked** — relevant inspection was performed;
- **tested** — relevant test procedure executed with an observed result;
- **verified** — requested endpoint itself was established with appropriate evidence;
- **unable to verify** — work may exist, but required endpoint evidence is unavailable.

Do not collapse these states into “done”.

## Authoritative evidence

Use the provider/artifact that can establish the requested endpoint.

When no authoritative read-back exists, preserve the result as unverified rather than manufacturing certainty.

A grader prediction about endpoint state is weaker than authoritative endpoint observation when the provider can be queried directly.

Specialist/worker narration is also weaker than direct source/provider/runtime evidence when direct inspection is available.

## Measurement conditions

When environment or harness conditions can affect the observation, preserve enough context to interpret it: relevant model/provider version, runtime/tool/harness version, configuration, resources, test data/input distribution, or rubric version.

A changed measurement condition does not automatically invalidate the artifact; it may invalidate the inference previously drawn from the measurement.

## Stochastic/repeated evidence

A single success can establish that an outcome occurred once. It does not by itself establish a reliability rate or regression absence for variable behavior.

Use representative repeated observations only when the claim or consequence requires them. Do not impose a fixed number of repetitions.

## Samples

Label samples as samples.

Do not extrapolate local quality to whole-scope quality without evidence.
