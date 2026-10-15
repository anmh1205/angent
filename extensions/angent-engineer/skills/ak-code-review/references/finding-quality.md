# Finding quality

A code-review finding should help the implementer understand and fix a real defect.

## Finding anatomy

Include:
- **location** — file/symbol/line range when possible;
- **mechanism** — why current code is wrong or unsafe;
- **impact** — what behavior/user/system can fail;
- **trigger** — condition/reproduction when useful;
- **evidence** — code path, test, trace, spec, or authoritative constraint;
- **remediation direction** — concise guidance, not a full rewrite unless asked.

## Severity

Severity is based on consequence and likelihood within the actual system, not on how much text the reviewer writes.

Useful broad levels:
- blocking/critical;
- important;
- minor.

Do not inflate stylistic preference into an Important defect.

## Avoid low-quality findings

Do not submit:
- vague “this may cause issues”;
- unsupported hypothetical failures;
- formatting/style nits already covered by automated tooling;
- duplicate manifestations of the same root issue;
- complaints that contradict project AGENTS.md conventions.

## Uncertain findings

If a concern is plausible but not established, label it as needing verification rather than presenting it as a defect.
