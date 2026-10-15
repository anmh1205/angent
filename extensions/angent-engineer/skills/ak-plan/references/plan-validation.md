# Plan validation

Validation tests the roadmap against reality; it is not a formatting review.

## Evidence verification

Before implementation, sample or inspect material claims proportional to risk:
- referenced files/symbols/endpoints exist;
- current interfaces/state match the plan;
- generated/migration artifacts are accounted for;
- external/versioned assumptions remain current;
- acceptance commands actually exercise the promised behavior.

Label unresolved claims instead of silently correcting them from guesswork.

## Adversarial review

For hard/deep/parallel/two-approach work, challenge:
- hidden scope expansion/reduction;
- unsupported assumptions;
- wrong ownership/dependency order;
- migration/backward-compatibility gaps;
- security/performance/operational failure modes;
- verification that can pass without proving the outcome;
- rollback/recovery gaps;
- parallel branches that actually share mutable state.

The reviewer proposes findings; Reasoning/Plan decides the repair.

### Load-bearing uncertainty and reversible choice

Find premises the plan **needs** and that may fail during its lifetime: schema compatibility, vendor behavior, data shape, throughput, device availability, account permissions or deployment timing. For each high-consequence premise, distinguish observed evidence, unsupported assumption, an early discriminating experiment, and the **observable signal that should trigger replanning**. Compare options by the cost of leaving them (migration, rollback, contract lock-in, irreversible writes) if the premise fails, not merely by initial implementation effort.

When no option dominates and evidence cannot yet settle the fork, prefer an approach with a safer escape path *if it still meets the accepted requirements*. Record the trade-off and its boundary; this is not blanket avoidance of ambitious architecture or permission to weaken requested capabilities. A plan that names a risk but has no observation or feasible response does not manage that risk.

## Decision validation

Ask the user only about genuine choices whose answer changes implementation, authority, or accepted trade-offs.

Do not interview for facts that can be established from source/provider evidence.

When an answer changes the plan, propagate it to every dependent phase.

## Whole-plan consistency sweep

After any red-team/validation/replan change, re-read the roadmap and all phase artifacts.

Search for:
- renamed files/APIs/fields;
- rejected assumptions still present;
- duplicated embedded contracts;
- stale phase ordering/dependency edges;
- acceptance criteria based on superseded behavior;
- old scope/non-goal statements.

Do not recommend implementation while a material contradiction remains.

## Readiness verdict

Use:
- **ready** — no blocking contradiction/unverified decisive premise at the requested consequence level;
- **revise** — known plan defect remains;
- **decision required** — user-owned trade-off blocks a valid plan;
- **blocked** — required evidence/capability is unavailable.
