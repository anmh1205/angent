# Changelog

## Unreleased — reliability hardening

ANGENT 1.0.0 remains an unreleased project candidate. Core hardening and cognitive-collaboration alignment are canonical. Reliability hardening strengthens evidence/belief/decision continuity and behavioral change validation without adding runtime infrastructure.

### Reliability semantics

- Added explicit material epistemic states: OBSERVED, ESTABLISHED, INFERRED, ASSUMED, UNKNOWN, CONFLICTED and STALE.
- Prevented inference promotion by repetition across owners, summaries or checkpoints.
- Added claim-support/entailment boundaries so a citation cannot silently support a stronger claim than its source establishes.
- Added compact **decision basis** for consequential/resumable decisions: decisive premises/evidence pointers, governing constraints, decision and reconsideration trigger.
- Context compaction and Continuity now preserve decision basis when downstream correctness depends on it, without persisting private chain-of-thought.
- Added multidimensional progress semantics: epistemic, dependency, artifact, capability and validation progress.
- Added general stall detection: repeated activity with no relevant state change returns to Reasoning instead of churning.
- Restored **calibration-before-scaling** as a risk-triggered reasoning/Quality pattern rather than a static test suite.
- Added representative behavioral calibration with target cases, accepted-success cases and counter-cases to detect overcorrection.
- Strengthened Quality independence against producer-rationale anchoring and separated capability gains from regression protection.
- Clarified that restrictive collaboration modes such as audit-only/report-before-edit also create Contract obligations when they limit actions.
- Added long-form authoring method calibration before bulk propagation when one bad method could reproduce defects across many chapters.

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
