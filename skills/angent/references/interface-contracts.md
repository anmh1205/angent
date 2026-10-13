# Owner interface contracts

Owners exchange semantic deltas, not narrative hand-offs.

## TaskModel

```yaml
outcome:
source_of_truth:
active_obligations: []
instruction_changes: []
scope:
authorization:
success_state:
completion_evidence:
```

Instruction changes preserve relation: ADD, REFINE, SUPERSEDE, SCOPED_EXCEPTION or CONFLICT.

## StateDelta

```yaml
verified_state: []
active_obligations: []
task_frontier:
accepted_baseline:
artifact_state_pointer:
stale_or_recheck: []
provenance: []
uncertainty: []
```

Active obligations needed by the next decision cannot be removed by context minimization.

## EvidenceQuery / EvidenceDelta

Research receives the blocked question, live alternatives, discriminating observation and required boundary. It returns established facts, source roles/boundaries, hypothesis updates, conflicts and residual uncertainty.

## RepairModel

Use when changing previously accepted work.

```yaml
accepted_baseline:
failure_observation:
failure_mechanism:
repair_target:
affected_scope: []
protected_properties: []
invalidated_dependents: []
acceptance_evidence: []
```

## ActionNode / ObservationDelta

An action carries intent, target, authority, active obligations, preconditions, expected observation, success predicate, replan condition, verification target and effect class.

Observation returns actual state, changed versions/identifiers, checks, expectation match and residual uncertainty.

## SolutionModel / ArtifactCandidate

Reasoning gives Authoring the established model, evidence, boundaries, reader capability and RepairModel when relevant.

Authoring gives Quality the candidate, accepted baseline, artifact state, repair target, protected properties and active obligations.

The baseline advances only after required gates pass.

## QualityVerdict

```yaml
status:
phase:
findings: []
target_repaired:
protected_properties_preserved:
dependencies_reconciled:
endpoint_verified:
```

Each finding carries dimension, evidence, affected scope, earliest fault owner and required repair property. Several findings may share one causal mechanism.

## PromotedMechanism

Learning records mechanism, decision/failure class, owner, applicability, boundary, evidence and disconfirming observation so Context can activate it for the right future decision.

## Frontier

```yaml
work_key:
revision:
lifecycle:
outcome:
phase:
active_obligations: []
verified_completed: []
unfinished:
accepted_baseline_pointer:
artifact_state_pointer:
stale_or_recheck: []
unresolved_dependencies: []
source_versions: []
next_safe_action:
```

Continuity stores only the compact subset needed to resume safely. Recovered state never overrides current authority or live external state.
