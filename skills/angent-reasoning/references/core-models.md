# Core reasoning models

This reference contains the stable models used by ANGENT Reasoning. Load narrower references when a task needs deeper treatment.

## Problem model

Represent only decision-relevant structure:

- objective / target state;
- actors / objects;
- relevant states;
- relations such as ownership, causality, dependency, topology, sequence, or mapping;
- established observations;
- assumptions;
- unknowns that can change a decision;
- constraints / invariants;
- possible actions.

A symptom is an observation, not the problem boundary. A file path is a location, not automatically the causal owner.

## System model

When interactions matter, trace:

- boundary;
- components;
- interfaces;
- data/control flow;
- state ownership;
- dependencies;
- invariants;
- failure boundaries;
- observability;
- side effects.

When possible follow one stable object/event:

~~~text
input → interface → transformation → owned state → output / observation
~~~

Localize the first point where actual behavior diverges from expectation.

## Epistemic state

Use explicit status only for propositions whose status can change a decision or quality verdict:

- **OBSERVED** — directly seen in authoritative runtime/provider/artifact evidence;
- **ESTABLISHED** — adequately supported by evidence at the required boundary/precision;
- **INFERRED** — derived from established facts but not directly established itself;
- **ASSUMED** — provisionally accepted to proceed;
- **UNKNOWN** — evidence is insufficient;
- **CONFLICTED** — credible evidence disagrees within the relevant boundary;
- **STALE** — formerly usable support may no longer describe current state.

Keep the supporting source/observation boundary when it matters.

Status does not automatically improve through repetition or hand-off. An inference copied into a plan, artifact and checkpoint is still an inference until new evidence establishes it.

Do not manufacture numeric confidence where the evidence does not support meaningful calibration.

## Hypothesis model

Use explicit hypotheses only when alternative mechanisms would lead to different action.

For each live hypothesis keep:
- claim/mechanism;
- current support and epistemic status;
- material evidence lineage or measurement dependency when it can change confidence;
- predicted observation;
- best discriminator;
- status;
- residual uncertainty.

A useful evidence item supports, weakens, rejects, or leaves a hypothesis undistinguished.

Stop expanding hypotheses when the current decision is robust despite remaining uncertainty.

## Decision model

Keep:
- goal;
- hard constraints;
- soft preferences;
- materially distinct options;
- consequences on shared decision axes;
- uncertainty that can reverse ranking;
- reversibility;
- cost of error;
- selected decision;
- reconsideration trigger.

For consequential or resumable decisions also preserve the **decision basis**: decisive premises/evidence pointers and the constraints or observations that made important alternatives non-viable.

The decision basis is a compact reconstructable rationale, not hidden chain-of-thought.

Do not substitute feature inventories or generic pros/cons for a decision model.

### Decision robustness

Prefer a decision that remains justified across the credible residual uncertainty that matters, not one that merely has a confident narrative.

For consequential decisions, ask:
- which decisive premise or evidence dependency could reverse the choice?
- is the decisive support observed/established, derived, evaluator-produced, or measurement-sensitive?
- could a plausible version/environment/context difference change the ranking?
- would a reversible probe reduce decisive uncertainty more cheaply than pretending it is resolved?

Do not manufacture numeric confidence when the evidence does not support meaningful calibration.

### Reconsideration

Reopen only the dependent decision when a material part of its basis changes, for example:
- decisive evidence is contradicted, downgraded, or found to share a weaker lineage;
- a relevant source/model/provider/harness/environment condition changes;
- Context reveals a previously missing active obligation or decision-relevant fact;
- Execution observes a state inconsistent with the model;
- Quality cannot distinguish subject defect from evaluator/environment defect;
- the validity boundary of an accepted baseline no longer matches the current system.

A changed measurement condition does not invalidate unrelated reasoning.

## Adaptive plan

A plan is a provisional consequence of the current model.

Represent:
- prerequisites;
- critical path;
- parallelizable independent work;
- uncertainty-reducing probes;
- side-effect boundaries;
- verification points;
- stop/replan conditions.

Prefer next actions that unblock a dependency, reduce decisive uncertainty, advance the critical path, and remain safe/reversible when uncertainty is high.

## Progress dimensions

Do not collapse all progress into “work happened”.

When useful distinguish:

- **epistemic** — material uncertainty or hypothesis state changed;
- **dependency** — a blocker/prerequisite changed;
- **artifact** — required implementation/document/state changed;
- **capability** — promised reader/user/system capability improved;
- **validation** — endpoint evidence improved.

A single action can advance several dimensions. It can also create an artifact without moving validation or capability at all.

If a sequence advances none of the dimensions relevant to the Contract, treat it as a stall signal and re-model rather than spending more steps on equivalent activity.

Progress tokens such as commits, generated files, issue transitions, or command success prove the requested endpoint only when the Contract defines them as endpoint evidence.

## Propagation risk

When the same method will modify many units, estimate whether one bad assumption could replicate widely.

If propagation risk is material, use representative calibration before scaling:
- choose units spanning the important difficulty/failure classes;
- include a counter-case when over-triggering is plausible;
- compare against the accepted baseline;
- proceed only when the method is sound enough for the intended scale.

Calibration validates the method, not the unseen remainder of the scope.
