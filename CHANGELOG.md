# Changelog

## Unreleased — reliability hardening

ANGENT 1.0.0 remains an unreleased project candidate. Core hardening and cognitive-collaboration alignment are canonical. Reliability hardening strengthens evidence/belief/decision continuity, correction interpretation, work-conserving frontier scheduling and behavioral change validation without adding runtime infrastructure.

### Reliability semantics

- Added explicit material epistemic states: OBSERVED, ESTABLISHED, INFERRED, ASSUMED, UNKNOWN, CONFLICTED and STALE.
- Prevented inference promotion by repetition across owners, summaries or checkpoints.
- Added claim-support/entailment boundaries so a citation cannot silently support a stronger claim than its source establishes.
- Added compact **decision basis** for consequential/resumable decisions: decisive premises/evidence pointers, governing constraints, decision and reconsideration trigger.
- Context compaction and Continuity preserve decision basis when downstream correctness depends on it, without persisting private chain-of-thought.
- Added multidimensional progress semantics: epistemic, dependency, artifact, capability and validation progress.
- Added general stall detection: repeated activity with no relevant state change returns to Reasoning instead of churning.
- Restored **calibration-before-scaling** as a risk-triggered reasoning/Quality pattern rather than a static test suite.
- Added representative behavioral calibration with target cases, accepted-success cases and counter-cases to detect overcorrection.
- Strengthened Quality independence against producer-rationale anchoring and separated capability gains from regression protection.
- Clarified that restrictive collaboration modes such as audit-only/report-before-edit also create Contract obligations when they limit actions.
- Added long-form authoring method calibration before bulk propagation when one bad method could reproduce defects across many chapters.

### Work-conserving frontier scheduling

- Moved long-running-operation branch selection from Execution-local polling discipline into Reasoning-owned frontier scheduling.
- Added semantic branch states: RUNNABLE, WAITING_EXTERNAL, BLOCKED and DONE.
- A RUNNING/PENDING observation returns control to Reasoning before another equivalent status call can be selected.
- WAITING_EXTERNAL branches are excluded from immediate next-action selection until their informative-observation condition is satisfied.
- One waiting branch no longer makes the whole task blocked while independent useful work remains.
- Continuity preserves branch scheduling state when losing it would change safe resume behavior.
- Quality calibration now covers pending+independent-work, pending-only, eligible-recheck, resume, several-runnable, and direct-completion cases.
- Promoted the general control-point lesson: a behavioral invariant must be owned or activated before the decision it needs to control; downstream guidance cannot reliably correct an already-selected behavior.
- Plugin bootstrap 1.0.4 activates the scheduling semantics at the entrypoint rather than relying on a deep Execution reference.
- No queue, scheduler service, background runtime, fixed timer or polling-count mechanism was added.

### Decision-boundary reliability

- Added invocation-bound authority: consequential effects revalidate current authority after concrete operation/target/material arguments are known.
- Capability, stale plans, generic prior approval and operation IDs no longer substitute for authorization of changed effects.
- Added observation-admission semantics so partial, stale, mismatched or ambiguous tool/provider results cannot silently mutate established state beyond their evidence boundary.
- Added target identity, observation boundary and scope/completeness fields to the conceptual ObservationDelta.
- Made multi-branch independence conditional on the current dependency/shared-state model; material shared-state changes reclassify only affected branches.
- Added decision-point Context sufficiency and trust-boundary handling for natural-language content returned by tools/providers.
- Added behavioral calibration cases for plan→invocation drift, observation mismatch/partiality, branch dependency invalidation and low-consequence counter-cases.
- No permission runtime, transaction engine, event journal, observation database or scheduler service was added.

### Reproducible behavioral acceptance

- Behavioral calibration used for later propagation/regression claims now preserves a recoverable evidence pointer/record rather than a bare PASS memory.
- The record links case/contract, baseline and candidate identity, material environment boundary, observable trajectory/tool-state evidence, artifacts/outcome, applied criteria and verdict validity.
- Hidden chain-of-thought is explicitly excluded; a smaller externalizable action/state trace is sufficient when it proves the behavior.
- Static keyword/count checks remain insufficient for semantic acceptance, while deterministic endpoint checks remain valid when they actually establish the requested property.

### Systemic correction interpretation

- Added an explicit correction-interpretation step before repair scope/owner selection.
- A user-named sentence/file/chapter/tool action is treated as failure evidence, not automatically the complete repair scope.
- Recurrence or method-level feedback triggers retrieval of relevant prior complaints, positive baselines and promoted Learning mechanisms before another edit.
- Persistent recurrence despite an existing rule now audits retrieval, activation, routing, ownership and competing instructions before strengthening wording or adding another guard.
- Repair remains causally bounded: systemic means fixing the generating mechanism across affected units, not global rewriting.

### Authoring surface continuity

- Made response-quality prose the shared composition baseline across chat and documents.
- Document adaptation may add scale-dependent depth, curriculum continuity, section structure, citations, figures, examples and navigation without introducing a separate generic “formal document” voice.
- Added calibration for meta-commentary that announces importance, memorization advice, author intention or lesson choreography instead of advancing the technical model.
- Explicitly avoids phrase blacklists; the failure property is missing technical progress/cohesion, not specific lexical tokens.

### Quality verdict consumption

- Required Quality phases now act as explicit dependencies of the baseline/effect/propagation transition they protect.
- PASS satisfies only that dependency and only within its verdict-validity boundary.
- FAIL/BLOCKED cannot be silently ignored to advance a dependent accepted baseline or consequential write/publish-as-accepted.
- Independent work remains runnable, and direct low-consequence tasks do not acquire mandatory Quality ceremony.

### Learning activation observability

- Added compact mechanism-activation evidence for recurrence diagnosis: mechanism pointer, matched decision/failure class, applicability basis, control point and current effect.
- Context can now distinguish “rule existed/retrieved” from “rule actually activated for this decision”.
- Missing activation evidence is treated as UNKNOWN rather than reverse-inferred from the final failure/success.
- Continuity carries only the activation pointer/subset when resume or recurrence diagnosis depends on it; no event log or Learning-store duplication is added.

### Explanatory-spine authoring

- Restored the v13.2-style relation-driven explanatory spine at section/chapter level rather than relying only on paragraph cohesion.
- Added Quality failure classes for multiple competing explanatory spines and internal process-vocabulary leakage.
- Kept source/log/API detail subordinate to the technical relation being taught unless source/runtime navigation is itself the reader task.
- Prevented ANGENT control vocabulary such as owner/gate/baseline/artifact-state/repair terms from leaking into unrelated technical documents.
- Preserved one response/document composition engine rather than introducing a separate document voice.

### Cognitive collaboration alignment

- Added task-scoped Collaboration State and a shared cognitive workspace without adding a new owner/runtime.
- Restored evidence-grounded subject modeling in Research.
- Restored full cognitive/subject model ≠ active teaching model ≠ presented model.
- Restored staging ≠ compression and point-stated ≠ explanatory-closure semantics.
- Added causal working-method Learning.

### Engineer boundary

Engineer implementation remains intentionally unchanged during reliability hardening.

### Release boundary

The project remains unreleased and not release-ready. Private plugin package version is tracked separately from the project candidate version.

Before project release:
1. complete reliability hardening and read-back;
2. complete the deferred Engineer inventory/parity refresh;
3. reconcile cross-harness behavior and plugin package against exact canonical source;
4. resolve project release/version strategy explicitly.

## Previous candidate history

Earlier PRs #1/#2 established the pre-hardening candidate. PR #3 integrated core hardening. PR #5 integrated cognitive-collaboration alignment.
