# Owner interface contracts — preserve cognition across hand-offs

ANGENT owners share structured semantic deltas, not long narrative hand-offs. These are conceptual contracts, not mandatory serialized schemas for simple tasks.

## Contract → Reasoning: TaskModel

```yaml
outcome:
underlying_objective:
target:
source_of_truth:
hard_constraints: []
soft_preferences: []
scope:
authorization:
success_state:
completion_evidence:
open_ambiguity: []
```

## Context → Reasoning: StateDelta

```yaml
verified_state: []
project_decisions: []
task_frontier:
pending_or_ambiguous_effects: []
artifact_pointers: []
provenance: []
uncertainty: []
```

Only return state that can change the current decision.

## Reasoning → Research: EvidenceQuery

```yaml
question:
decision_blocked:
live_alternatives: []
discriminating_observation:
required_precision:
version_or_platform_boundary:
```

Research should know what evidence would change the model.

## Research → Reasoning: EvidenceDelta

```yaml
established: []
source_roles: []
version_boundaries: []
supported_hypotheses: []
weakened_hypotheses: []
rejected_hypotheses: []
conflicts: []
residual_uncertainty: []
```

Do not return a source dump when a smaller evidence delta is sufficient.

## Reasoning → Execution: ActionNode

```yaml
intent:
target:
authorization:
preconditions: []
expected_observation:
replan_condition:
verification_target:
```

The action describes what evidence should return, not only what command/tool should run.

## Execution → Reasoning: ObservationDelta

```yaml
attempted:
observed_state:
changed_identifiers_or_versions: []
expectation_match:
new_evidence: []
residual_uncertainty: []
provider_evidence: []
```

An acknowledgement without authoritative state is not automatically an observation of success.

## Reasoning → Authoring: SolutionModel

```yaml
established_model:
conclusion:
decisive_evidence: []
boundaries: []
uncertainty: []
reader_capability_target:
```

Authoring may choose teaching order and representation but must not alter the established technical conclusion silently.

## Quality → owner: QualityVerdict

```yaml
status: PASS | FAIL | BLOCKED
layer: solution | communication
failed_dimension:
earliest_fault_owner:
evidence:
required_repair:
```

Quality points to the earliest faulty decision and does not become a repair writer.

## Learning → owner: PromotedMechanism

```yaml
mechanism:
applicability:
boundary:
supporting_experience: []
transfer_evidence:
negative_control:
superseded_rules: []
```

Only promoted mechanisms alter production behavior.

## Continuity → Context/Reasoning: Frontier

```yaml
work_key:
verified_units: []
saved_artifacts: []
pending_operation:
unresolved: []
source_versions: []
next_action:
```

Recovered state never overrides current authorization or live source truth.
