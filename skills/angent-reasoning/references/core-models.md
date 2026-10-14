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

## Hypothesis model

Use explicit hypotheses only when alternative mechanisms would lead to different action.

For each live hypothesis keep:
- claim/mechanism;
- current support and support type;
- material evidence lineage/dependency;
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
- decisive evidence/assumptions;
- validity boundary;
- reconsideration trigger.

Do not substitute feature inventories or generic pros/cons for a decision model.

### Decision robustness

Prefer a decision that remains justified across the credible residual uncertainty that matters, rather than one that merely has a confident narrative.

Before a consequential decision, ask:

- which assumption/evidence dependency could reverse the choice?
- is decisive evidence direct, inferred, evaluator-produced, or environmentally confounded?
- would a plausible alternate environment/version/context change the ranking?
- is a reversible probe cheaper than pretending uncertainty is resolved?

Do not invent numeric confidence when the evidence does not support it.

### Reconsideration

Reopen a decision when a material part of its basis changes, for example:

- decisive evidence is contradicted, downgraded, or shown to share a weaker lineage;
- source/model/provider/version or relevant environment changes;
- Context reveals a previously missing active obligation or decision-relevant fact;
- Execution observes a state inconsistent with the model;
- Quality cannot distinguish subject defect from evaluator/environment defect;
- an accepted baseline's validity boundary no longer matches the current system.

Reconsider only dependent decisions. A changed measurement condition does not invalidate unrelated reasoning.

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

Progress tokens such as commits, generated files, issue transitions, command success, or repeated pending polls prove the requested endpoint only when the Contract defines them as endpoint evidence.
