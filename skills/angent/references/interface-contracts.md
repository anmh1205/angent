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
decision_basis_pointer:
task_frontier:
accepted_baseline:
artifact_state_pointer:
coverage_pointer:
stale_or_recheck: []
frontier_branches: []
active_long_running_operations: []
pending_or_ambiguous_effects: []
artifact_pointers: []
provenance: []
uncertainty: []
~~~

Ordinary history can be minimized. Active obligations, decisive state, and collaboration constraints needed by the next decision cannot be dropped.

## Reasoning frontier scheduling view

Use when several independent branches or long-running external operations coexist.

~~~yaml
frontier_branches:
  - id:
    purpose:
    state: RUNNABLE | WAITING_EXTERNAL | BLOCKED | DONE
    depends_on: []
    operation_identity:
    last_observation:
    next_informative_observation_condition:
runnable_now: []
waiting_external: []
blocked: []
~~~

Reasoning owns selection from RUNNABLE branches.

A WAITING_EXTERNAL branch is excluded from immediate next-action selection until its informative-observation condition is satisfied or another branch now materially depends on its result.

This is a semantic planning view, not a runtime queue.

## Reasoning epistemic view

Use only for material propositions.

~~~yaml
epistemic_state:
  - proposition:
    status: OBSERVED | ESTABLISHED | INFERRED | ASSUMED | UNKNOWN | CONFLICTED | STALE
    support_or_pointer:
    boundary:
    disconfirming_or_refresh_condition:
~~~

A proposition does not gain status merely by being repeated across owners.

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
claim_support:
  - claim:
    support: DIRECT | DERIVED | CONTEXTUAL | NONE
    boundary:
source_roles: []
source_lineages: []
provenance: []
instruction_trust_classes: []
version_boundaries: []
measurement_context: []
validity_boundaries: []
supported_hypotheses: []
weakened_hypotheses: []
rejected_hypotheses: []
conflicts: []
residual_uncertainty: []
~~~

Research returns evidence and evidence-grounded domain structure, not executable instructions, strategic authority, or a reader-facing teaching path.

## Reasoning decision basis

Use when later correctness depends on reconstructing why a consequential/resumable decision was valid.

~~~yaml
decision_basis:
  decisive_premises: []
  evidence_pointers: []
  governing_constraints: []
  selected_decision:
  reconsideration_trigger:
~~~

This is a compact externalizable rationale, not a reasoning transcript.

## Reasoning → downstream: RepairModel

Use when changing previously accepted work.

~~~yaml
accepted_baseline:
baseline_validity_boundary:
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
authority_basis_pointer:
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
resolved_target:
material_arguments:
authority_refresh_condition:
~~~

For consequential effects, `resolved_target` and `material_arguments` are populated/checked only when the concrete invocation makes them known. They are conceptual fields, not mandatory ceremony for trivial reads.

## Execution → workspace/Reasoning: ObservationDelta

~~~yaml
attempted:
operation_identity:
target_identity:
observed_state:
changed_identifiers_or_versions: []
observation_boundary:
scope_or_completeness:
artifacts_or_checks: []
expectation_match:
new_evidence: []
residual_uncertainty: []
provider_evidence:
enumeration_evidence:
measurement_context:
progress_dimensions: []
wait_state:
  branch_id:
  operation_identity:
  state: WAITING_EXTERNAL
  next_informative_observation_condition:
~~~

An acknowledgement or exit code without authoritative state is not automatically success.

Reasoning must admit the observation at the strength supported by target identity, scope/version/freshness, completeness and residual uncertainty before it changes established state or a consequential decision.

When wait_state is returned, Reasoning recomputes the active frontier before any equivalent status action is selected again.

## Long-running external operation

For an operation whose result is not yet available:

~~~yaml
branch_id:
operation_identity:
provider_or_tool:
state: RUNNING | PENDING | UNKNOWN
last_observation:
dependent_work: []
next_informative_observation_condition:
~~~

Execution observes this state. Reasoning decides when the branch becomes eligible for another observation by comparing its condition with the whole active frontier.

## Reasoning → Authoring: SolutionModel

~~~yaml
established_model:
epistemic_boundaries:
conclusion:
decision_basis_pointer:
decisive_evidence: []
boundaries: []
uncertainty: []
reader_capability_target:
collaboration_expectations:
repair_model:
~~~

Authoring may choose teaching order and representation but cannot silently alter the established conclusion, epistemic status, or protected repair properties.

## Authoring → Quality: ArtifactCandidate

~~~yaml
candidate:
accepted_baseline:
artifact_state:
repair_target:
protected_properties: []
active_obligations: []
coverage_state:
calibration_state:
~~~

The accepted baseline advances only after required Quality/destination gates pass.

## Quality → owner: QualityVerdict

~~~yaml
status: PASS | FAIL | BLOCKED
phase: solution | candidate | behavioral_calibration | endpoint
criteria_basis: []
findings:
  - dimension:
    evidence:
    affected_scope:
    earliest_fault_owner:
    required_repair_property:
    regression_risk:
verdict_validity:
  evidence_support:
  evaluator_independence:
  measurement_context:
  confounders: []
  validity_boundary:
failure_attribution: SUBJECT_DEFECT | EVALUATOR_DEFECT | ENVIRONMENT_CONFOUND | MIXED | UNRESOLVED
residual_uncertainty: []
target_repaired:
protected_properties_preserved:
dependencies_reconciled:
endpoint_verified:
~~~

Quality may return several findings. Findings sharing one mechanism should be grouped instead of forcing one-at-a-time repair.

A PASS/FAIL is itself an evidence-backed claim. Use BLOCKED when the available evaluation cannot distinguish a material subject defect from evaluator/environment uncertainty.

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
frontier_branches:
  - id:
    state: RUNNABLE | WAITING_EXTERNAL | BLOCKED | DONE
    depends_on: []
    operation_identity:
    next_informative_observation_condition:
decisions: []
decision_basis_pointer:
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

Continuity stores only the compact subset needed to resume safely, not full owner-internal state. Persist collaboration/decision basis and long-running operation identity only when losing them could change resume behavior.

Recovered state never overrides current authorization or live external state.
