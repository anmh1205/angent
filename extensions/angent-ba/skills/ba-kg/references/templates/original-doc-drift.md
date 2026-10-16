# Accepted requirements versus inspected implementation

**Accepted SRS revision:**
**Repository / pinned commit and environment:**
**Scope and actor:**

## Line-level comparison

| Accepted FR/BR/E and exact predicate | Source code path/symbol/line | Implementation effect and state mutation | Observed test/runtime | Verdict | Business consequence |
|---|---|---|---|---|---|
| FR-… | | | | ALIGNED / DIVERGENT / NOT IMPLEMENTED / UNVERIFIABLE | |

ALIGNED needs matching observable behavior. DIVERGENT needs a contradictory source witness. NOT IMPLEMENTED requires sufficient execution-path coverage. UNVERIFIABLE names unavailable provider, feature flag, private module or environment evidence. A missing search hit does not prove absence.

## Exception and trust-boundary coverage

| Scenario | Expected authorization/response | Observed source or runtime behavior | Test gap | Recommended next evidence |
|---|---|---|---|---|
| Allowed | | | | |
| Forbidden | | | | |
| Invalid/duplicate | | | | |
| Downstream failure | | | | |

## Decision record

List each mismatch, severity and affected downstream docs/test cases. Decide whether to fix implementation, request stakeholder amendment, or inspect missing evidence first. Never automatically change requirements to match defective code. Differentiate implemented-at-SHA from deployed-in-environment.
