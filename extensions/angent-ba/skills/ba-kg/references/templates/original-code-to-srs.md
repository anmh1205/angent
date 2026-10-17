# Source-observed SRS reconstruction

**Source:** repository / immutable SHA / target feature / configuration:
**Purpose:** reconstruct current behavior for review, NOT approve a new rule.

## Inspection map

| Entry/role | Source file, symbol and line | Configuration/flag | Evidence status | Not inspected |
|---|---|---|---|---|
| API/command | | | observed/inferred/unknown | |
| Domain and guards | | | | |
| Persistence/event | | | | |
| External integration | | | | |

## Candidate requirements

| Candidate FR/BR/E ID | Actor/trigger and observable outcome | Precondition | Postcondition/state mutation | Source witness at SHA | Test evidence | Status |
|---|---|---|---|---|---|---|
| FR-CAND-001 | | | | | | SOURCE-OBSERVED / UNVERIFIED |

Give each path its acceptance-relevant negative cases: unauthorized actor, validation failure, missing integration, duplicate request, concurrent updates and stale flags. Separate current implementation from approved target semantics.

## Contradictions and evidence gaps

| Source A | Source B or accepted SRS | Consequence | What must be decided or tested |
|---|---|---|---|
| | | | |

## Review result

Which code paths were really read? Which tests ran (exact command, environment and output)? Which decisions are still inferred? What was deliberately excluded? What is the precise diff against the existing SRS? Never overwrite an accepted SRS because code appears to implement a different rule.
