# Team protocol

A Team run requires a live lifecycle surface capable of the team semantics the job depends on.

Before dispatch, verify the needed subset of:
- team creation;
- teammate creation/identity;
- shared work/task state;
- teammate/lead messaging;
- waiting/joining;
- shutdown/cancellation;
- cleanup.

If a required lifecycle operation is unavailable, stop rather than substituting generic subagents under the Team name.

For each teammate define:
- role;
- exact question/work unit;
- owned scope/files;
- inputs;
- allowed effects;
- acceptance evidence;
- return format.

Avoid overlapping writers.

Prefer artifact/evidence pointers over transcript exchange.

At join:
- deduplicate repeated findings;
- detect shared assumptions;
- preserve contradictions;
- integrate compatible work;
- route strategic disagreement to Reasoning.

Do not majority vote.

A successful set of one-shot subagents is not evidence that the live Team lifecycle exists.
