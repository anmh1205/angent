# Repair and regression control

Use this model when revising an existing artifact, plan, implementation, explanation or workflow after a complaint, defect or new constraint.

A repair is a state transition from an accepted baseline to a candidate. It is not a fresh optimization around the newest symptom.

## Repair state

Keep only what is needed:

- **accepted baseline** — the last state that was accepted or verified enough to preserve;
- **failure observation** — what is actually wrong;
- **failure mechanism** — why the observation occurs, when known;
- **repair target** — the property/state that must change;
- **affected scope** — units that actually depend on the failed mechanism;
- **preservation ledger** — properties/constraints/decisions that must not regress;
- **candidate delta** — what the proposed repair changes;
- **invalidation set** — previously verified work that becomes stale because a dependency changed;
- **acceptance evidence** — what proves the target improved without violating preserved properties.

## Do not optimize the opposite extreme

A complaint is evidence of a failed function, not an instruction to maximize a scalar in the opposite direction.

Examples:

- too shallow → restore missing mechanisms/depth, not indiscriminately add length;
- too repetitive → remove duplicate reasoning, not delete necessary prerequisite repair;
- too few diagrams → expose hard-to-reconstruct relations, not diagram every paragraph;
- too conversational → replace low-information commentary, not turn prose bureaucratic.

## Baseline-preserving repair loop

1. Identify the accepted baseline or reconstruct the strongest current baseline from canonical state.
2. State the exact failed function/mechanism.
3. Determine the smallest causal scope that must change.
4. Record the preservation ledger before editing.
5. Produce a candidate delta.
6. Verify the repair target.
7. Verify every protected property that the delta could plausibly affect.
8. Accept the candidate only when it improves the target without crossing a protected floor.
9. If a dependency changed, mark dependent verified work stale and re-evaluate only that affected closure.

## Invalidation propagation

Verified work is conditional on the decisions/models/artifacts it depended on.

When a dependency changes:

```text
changed premise / model / interface
          ↓
direct dependents become STALE
          ↓
transitive dependents become RECHECK_REQUIRED when the changed relation can affect them
```

Do not invalidate unrelated verified work.

## Oscillation and convergence

Treat repeated reversal as evidence that the model is wrong, not as a reason for another local patch.

Escalate from local repair to model/interface analysis when:

- the same defect reappears after a repair;
- fixing dimension A repeatedly breaks B and vice versa;
- the repair scope keeps expanding;
- successive candidates alternate between previously rejected states;
- the user has to restate the same underlying complaint.

At that point, stop editing the symptom. Reconstruct the controlling model, constraints, interfaces and quality baseline first.

## Completion

A repair is complete only when:

- the original failure mechanism is no longer present at the required scope;
- preserved properties remain valid;
- affected dependent work has been reconciled;
- no material new regression was introduced by the delta.
