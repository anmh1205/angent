# Adaptive planning — dependency-aware action under changing evidence

A plan is a provisional consequence of the current model, not a script to finish regardless of observations.

## Action graph

Represent the next work in terms of:
- prerequisites;
- critical path;
- independent/parallelizable work;
- uncertainty-reducing probes;
- side-effect boundaries;
- verification points;
- stop/replan conditions.

## Choose the next action

Prefer an action that:
1. unblocks a required dependency;
2. reduces decision-relevant uncertainty;
3. advances the critical path;
4. is safe/reversible when uncertainty is high.

Do not create a long plan when one discriminating action determines the rest.

## Observation loop

```text
model → decision → plan → action → observation
  ↑                                  │
  └──────── update / replan ─────────┘
```

After an unexpected observation:
- identify which assumption/dependency changed;
- update the problem/system model;
- invalidate dependent plan nodes;
- preserve still-valid completed work;
- choose the new frontier.

## Completion versus progress

Progress tokens include commits, comments, generated files, command success, intermediate reports and status changes. They count only as evidence for the requested endpoint when the Contract says they do.

## Stop conditions

Stop at:
- verified requested endpoint;
- genuine blocker;
- required user decision;
- authorization/safety boundary;
- unavailable capability.

A convenient progress summary is not a stop condition.
