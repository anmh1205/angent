# Abstraction and invariants

Use this when reasoning becomes symptom-driven, local fixes keep failing, or later plans begin violating earlier constraints.

## Abstraction ladder

```text
requested outcome
    ↓
system / reader / project boundary
    ↓
decision boundary
    ↓
causal mechanism
    ↓
implementation location
```

The lowest level is not automatically the right level.

Zoom out when a local fix cannot plausibly explain the requested outcome, several local failures share a pattern, or the latest example is narrower than the requested scope.

Zoom in when the owner/interface is identified and a bounded observation or change can validate the model.

## Invariant ledger

An invariant may come from:
- explicit user constraint;
- canonical source/spec;
- accepted architecture decision;
- safety/authority boundary.

Preserve the statement, provenance, scope, dependent decisions, and an observation that would show violation.

When a new plan conflicts with an invariant:
1. check whether the invariant is still current;
2. if current, revise/reject the plan;
3. if superseded by newer authority, explicitly update dependent decisions.

A constraint disappearing from later planning is a reasoning failure, not a harmless implementation detail.
