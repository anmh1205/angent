# Owner interface contracts — preserve cognition across hand-offs

Owners exchange structured semantic deltas, not narrative hand-offs. These are conceptual contracts, not mandatory serialized schemas for trivial tasks.

The contracts describe views into one shared cognitive workspace. They do not imply that ANGENT must execute owners as a fixed pipeline.

## Contract → workspace: TaskModel

~~~yaml
outcome:
underlying_objective:
target:
source_of_truth:
hard_constraints: []
active_obligations: []
instruction_changes: []
soft_preferences: []
scope:
authorization:
success_state:
completion_evidence:
open_ambiguity: []
~~~

Material instruction changes preserve their relation to existing obligations: ADD, REFINE, SUPERSEDE, SCOPED_EXCEPTION or CONFLICT.

## Context → workspace: CollaborationState

Use only when collaboration method can change the current work.

~~~yaml
interaction_mode:
initiative_expectation:
evidence_expectation:
explanation_expectation:
progress_checkpoint_expectation:
working_method_mechanisms: []
task_scoped_exceptions: []
provenance: []
confidence:
~~~

CollaborationState shapes how authorized work proceeds. It does not grant effect authority and is not a permanent personality profile.

## Context → workspace: StateDelta

~~~yaml
verified_state: []
active_obligations: []
collaboration_state:
project_decisions: []
task_frontier:
accepted_baseline:
artifact_state_pointer:
coverage_pointer:
stale_or_recheck: []
active_long_running_operations: []
pending_or_ambiguous_effects: []
artifact_pointers: []
provenance: []
uncertainty: []
~~~

Ordinary history can be minimized. Active obligations and collaboration constraints needed by the next decision cannot be dropped.

## Reasoning → Research: EvidenceQuery

~~~yaml
question:
decision_blocked:
current_model_fragment:
live_alternatives: []
discriminating_observation:
required_precision:
version_or_platform_boundary:
~~~

## Research → workspace/Reasoning: EvidenceDelta

~~~yaml
established: []
subject_model_delta:
  objects_or_states: []
  relations: []
  mechanisms: []
  assumptions_or_boundaries: []
  discriminating_observations: []
source_roles: []
provenance: []
instruction_trust_classes: []
version_boundaries: []
supported_hypotheses: []
weakened_hypotheses: []
rejected_hypotheses: []
conflicts: []
residual_uncertainty: []
~~~

Research returns evidence and evidence-grounded domain structure, not executable instructions, strategic authority, or a reader-facing teaching path.

## Reasoning → downstream: RepairModel

Use when changing previously accepted work.

~~~yaml
accepted_baseline:
failure_observation:
failure_mechanism:
repair_target:
affected_scope: []
protected_properties: []
candidate_delta:
invalidated_dependents: []
acceptance_evidence: []
~~~

A complaint is evidence feeding this model; it is not itself the repair model.

## Reasoning → Execution: ActionNode

~~~yaml
intent:
target:
authorization:
active_obligations: []
collaboration_constraints: []
preconditions: []
capability_required:
input_artifact_pointers: []
expected_observation:
action_success_predicate:
replan_condition:
verification_target:
effect_class:
~~~

## Execution → workspace/Reasoning: ObservationDelta

~~~yaml
attempted:
observed_state:
changed_identifiers_or_versions: []
artifacts_or_checks: []
expectation_match:
new_evidence: []
residual_uncertainty: []
provider_evidence: []
enumeration_evidence:
~~~

An acknowledgement or exit code without authoritative state is not automatically success.

## Authoring/Execution wait state

For a long-running external operation whose result is not yet available:

~~~yaml
operation_identity:
provider_or_tool:
state: RUNNING | PENDING | UNKNOWN
last_observation:
dependent_work: []
independent_runnable_work: []
next_informative_check_condition:
~~~

This state is descriptive. It does not create a polling schedule. Execution decides when another check can add information.

## Reasoning → Authoring: SolutionModel

~~~yaml
established_model:
conclusion:
decisive_evidence: []
boundaries: []
uncertainty: []
reader_capability_target:
collaboration_expectations:
repair_model:
~~~

Authoring may choose teaching order and representation but cannot silently alter the established conclusion or protected repair properties.

## Authoring → Quality: ArtifactCandidate

~~~yaml
candidate:
accepted_baseline:
artifact_state:
repair_target:
protected_properties: []
active_obligations: []
coverage_state:
~~~

The accepted baseline advances only after required Quality/destination gates pass.

## Quality → owner: QualityVerdict

~~~yaml
status: PASS | FAIL | BLOCKED
phase: solution | candidate | endpoint
findings:
  - dimension:
    evidence:
    affected_scope:
    earliest_fault_owner:
    required_repair_property:
    regression_risk:
target_repaired:
protected_properties_preserved:
dependencies_reconciled:
endpoint_verified:
~~~

Quality may return several findings. Findings sharing one mechanism should be grouped instead of forcing one-at-a-time repair.

## Learning → Context/owner: PromotedMechanism

~~~yaml
mechanism:
decision_or_failure_class:
owner:
applicability:
boundary:
supporting_experience: []
transfer_evidence:
disconfirming_observation:
collaboration_effect:
superseded_rules: []
~~~

collaboration_effect is optional. Use it only when the causal mechanism should alter task-relevant collaboration state under matching conditions.

A promoted mechanism changes behavior only when Context can retrieve it for the matching decision/failure class.

## Continuity → workspace: Frontier

~~~yaml
work_key:
revision:
lifecycle: ACTIVE | PAUSED | BLOCKED | COMPLETED | SUPERSEDED | ABANDONED
repair_state: NONE | REPAIRING | UNSTABLE
outcome:
scope:
phase:
active_obligations: []
collaboration_state_pointer:
verified_completed: []
unfinished:
decisions: []
accepted_baseline_pointer:
artifact_state_pointer:
coverage_pointer:
stale_or_recheck: []
active_long_running_operations: []
artifact_pointers: []
pending_or_ambiguous_effects: []
unresolved_dependencies: []
source_versions: []
next_safe_action:
~~~

Continuity stores only the compact subset needed to resume safely, not full owner-internal state. Persist collaboration state or a pointer only when losing it could change resume behavior.

Recovered state never overrides current authorization or live external state.
