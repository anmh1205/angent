# Problem model — represent what must be reasoned about

The problem model is Reasoning's compact internal representation of the current task. It should contain enough structure to support inference and action without mirroring every available fact.

## Elements

- **actors / objects** — entities that participate in the problem;
- **states** — relevant conditions or values;
- **relations** — dependency, ownership, causality, topology, sequence, mapping or constraint;
- **observations** — evidence already available;
- **constraints / invariants** — conditions that must remain true;
- **unknowns** — missing facts that could change the conclusion;
- **assumptions** — provisional premises not yet verified;
- **actions** — possible interventions or information-gathering steps;
- **target state** — the outcome that resolves the task.

## Build around the objective, not the latest symptom

A symptom is an observation, not the problem boundary. A file path is a location, not automatically the causal boundary. Choose the smallest model that preserves the relationships needed for the user's objective.

## State transitions

When actions change the system, model:

```text
state_before --action--> state_after
```

Include expected observations that distinguish success from partial or unrelated change.

## Assumption discipline

Keep assumptions separate from observations. When an assumption is decision-critical, either verify it or carry the uncertainty into the decision.

## Model revision

The problem model is provisional. New evidence may:
- add/remove an actor or relation;
- invalidate an assumption;
- move an unknown to established fact;
- change the relevant boundary;
- alter the target path.

Update the model before continuing a plan that depended on invalidated structure.
