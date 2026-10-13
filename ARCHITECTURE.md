# ANGENT Architecture

ANGENT is a cognitive layer for intelligent agents. Its job is to preserve intent and authority, reconstruct relevant state, model systems and uncertainty, seek evidence, reason, decide, repair existing work without regression, act, verify, communicate and learn.

## Cognitive loop

```text
Intent
  ↓
Contract ← Context
  ↓
Reasoning ↔ Research
  ↓
Solution Quality Gate
  ↓
Decision / Repair Model
  ├────────────── operational action ──────────────┐
  │                                                ↓
  │                                      Execution + Continuity
  │                                                ↓
  │                                           Observation
  │                                                └──→ Reasoning / replan
  │
  └──────────── reader-facing candidate ─→ Authoring
                                             ↓
                                  Comparative Candidate Gate
                                             ↓
                              Format representation when needed
                                             ↓
                                 Execution write when external
                                             ↓
                                  Format visible read-back
                                             ↓
                                    Endpoint Quality Gate
                                             ↓
                                       Verified outcome
                                             ↓
                                           Learning
```

Quality is one owner with several phases, not one fixed node before or after Authoring.

Continuity is cross-cutting. It persists the compact active-work frontier, accepted baseline pointers, stale/recheck state, verified progress and ambiguous effects, then reconciles them on resume.

## Revision loop

Existing work is changed relative to an accepted baseline.

```text
accepted baseline + active obligations
              ↓
      failure observation
              ↓
     Reasoning RepairModel
 target + affected scope + protected properties
              ↓
           candidate
              ↓
    comparative Quality gate
       ↙                 ↘
   reject                 accept
     ↓                      ↓
re-model/repair      advance baseline
```

A complaint is evidence of a failed property. It does not automatically supersede earlier requirements or justify maximizing the opposite property.

## Ownership

- **Contract**: task boundary, authority, evolving obligations and success semantics.
- **Context**: smallest relevant working state while retaining active obligations, baseline pointers, provenance and trust class.
- **Reasoning**: problem/system model, hypotheses, decisions, dependency-aware plans, repair model and invalidation propagation.
- **Research**: evidence that changes decision-relevant uncertainty.
- **Execution**: authorized effects, observation, retry/reconciliation and provider evidence.
- **Quality**: independent solution, comparative-candidate and endpoint judgment.
- **Authoring**: reader-facing explanation plus semantic artifact state.
- **Format**: destination representation requirements and visible-render verification.
- **Learning**: causal mechanisms with activation, recurrence, narrowing and retirement.
- **Continuity**: durable active-work frontier and interruption-safe recovery.
- **Shell**: one compact ANGENT signature.

## Interface principle

Owners exchange semantic deltas, not long narrative hand-offs.

The cross-owner contracts preserve the information that must not disappear between owners:

- active obligations;
- accepted baseline;
- repair target and protected properties;
- dependency invalidation;
- artifact-state pointers;
- endpoint evidence.

Detailed owner-internal models stay with their owner rather than being copied into Continuity.

## Architectural invariants

1. Current explicit authority and active obligations cannot be silently weakened by later planning.
2. A newer instruction supersedes an older obligation only when its relation actually implies replacement.
3. Reasoning owns decision and repair state.
4. Research supplies evidence; source count is not a decision.
5. Execution cannot continue a stale dependent plan after an observation invalidates its assumptions.
6. External/retrieved content is evidence, not instruction authority by itself.
7. Authoring cannot hide missing reasoning with fluent prose.
8. A revision must improve its repair target without regressing protected accepted properties.
9. Repeated repair oscillation returns to Reasoning instead of causing more local patches.
10. Quality judges; it does not become a second producer.
11. Continuity persists resume-critical semantics and pointers, not duplicate owner state.
12. Learning is operational only when a promoted mechanism can be activated for the matching future decision.
13. Direct tasks remain direct; architecture complexity must not leak into trivial answers.

## Canonical references

Owner-specific guidance lives beside each owner under `skills/angent-*/references/`.

Root references keep only genuinely cross-cutting contracts such as owner interfaces, core fixtures and the harness adapter contract.
