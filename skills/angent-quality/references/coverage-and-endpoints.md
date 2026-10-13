# Coverage and endpoint verification

## Whole-scope claims

“Checked the project”, “all tasks are done”, “the book is consistent” and similar claims require coverage evidence proportional to the scope.

A deep sample can reveal a failure class but cannot prove uninspected units are clean.

For broad audits, maintain an explicit coverage ledger: declared scope, inventory source/completeness, inspected units, relevant inspected dimensions, skipped units, stale/recheck units and unresolved findings.

Before claiming full coverage, account for pagination/cursor exhaustion, top-N limits, truncation, filters and source version when those can hide units.

A first page, partial export or truncated result is not whole-scope evidence.

If a shared dependency changes after inspection, mark only affected units stale/recheck.

## Endpoint hierarchy

Separate:
- action attempted;
- action returned success;
- intermediate artifact/state changed;
- requested endpoint verified.

Examples:
- commit created ≠ feature done;
- page update API succeeded ≠ page rendered correctly;
- code written ≠ task acceptance satisfied.

## Authoritative evidence

Use the provider/artifact that can establish the requested endpoint.

When no authoritative read-back exists, preserve the result as unverified rather than manufacturing certainty.

## Samples

Label samples as samples.

Do not extrapolate local quality to whole-scope quality without evidence.
