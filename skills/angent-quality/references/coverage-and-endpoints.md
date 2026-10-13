# Coverage and endpoint verification

## Whole-scope claims

“Checked the project”, “all tasks are done”, “the book is consistent” and similar claims require coverage evidence proportional to the scope.

A deep sample can reveal a failure class but cannot prove uninspected units are clean.

For broad audits, maintain enough inventory/coverage state to know what was actually checked.

## Endpoint hierarchy

Separate:
- action attempted;
- action returned success;
- intermediate artifact/state changed;
- requested endpoint verified.

Examples:
- commit created ≠ feature done;
- tests passed ≠ deployment healthy;
- page update API succeeded ≠ page rendered correctly;
- code written ≠ Jira task acceptance satisfied.

## Authoritative evidence

Use the provider/artifact that can establish the requested endpoint.

When no authoritative read-back exists, preserve the result as unverified rather than manufacturing certainty.

## Samples

Label samples as samples.

Do not extrapolate local quality to whole-scope quality without evidence.
