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
- worker says tests passed ≠ tests were observed;
- document drafted ≠ destination artifact verified.

## Completion claims

Use precise status when the distinction matters:

- **drafted** — candidate content/artifact exists;
- **implemented** — requested change exists in the implementation/artifact;
- **checked** — relevant inspection was performed;
- **tested** — relevant test procedure executed with observed result;
- **verified** — requested endpoint itself was established with appropriate evidence;
- **unable to verify** — work may exist, but required endpoint evidence is unavailable.

Do not collapse these states into “done”.

## Authoritative evidence

Use the provider/artifact that can establish the requested endpoint.

When no authoritative read-back exists, preserve the result as unverified rather than manufacturing certainty.

Specialist/worker narration is weaker than direct source/provider/runtime evidence when direct inspection is available.

## Samples

Label samples as samples.

Do not extrapolate local quality to whole-scope quality without evidence.
