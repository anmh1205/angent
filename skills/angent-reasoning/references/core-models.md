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

```text
input → interface → transformation → owned state → output / observation
```

Localize the first point where actual behavior diverges from expectation.

## Hypothesis model

Use explicit hypotheses only when alternative mechanisms would lead to different action.

For each live hypothesis keep:
- claim/mechanism;
- current support;
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

Do not substitute feature inventories or generic pros/cons for a decision model.

## Adaptive plan

A plan is a provisional consequence of the current model.

Represent:
- prerequisites;
- critical path;
- parallelizable independent work;
- waiting dependencies;
- uncertainty-reducing probes;
- side-effect boundaries;
- verification points;
- stop/replan conditions.

Prefer next actions that unblock a dependency, reduce decisive uncertainty, advance the critical path, and remain safe/reversible when uncertainty is high.

For substantive iterative work, reason about a progress delta: new evidence, model change, dependency change, accepted-work advancement, endpoint-evidence advancement, or material uncertainty reduction.

Repeated activity with no such delta is a replan signal.

Progress tokens such as commits, generated files, issue transitions, command success, repeated status checks, or added source count prove the requested endpoint only when the Contract defines them as endpoint evidence.
