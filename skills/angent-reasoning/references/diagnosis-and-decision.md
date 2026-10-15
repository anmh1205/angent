# Diagnostic reasoning and decision quality

Load only when competing explanations, meaningful cross-layer uncertainty, or a consequential solution choice could change the work. The purpose is to select a justified action from causal evidence, not to require a formal hypothesis tree for every task.

## Locate the observed divergence

Begin with the actual requested outcome and a concrete discrepancy: stimulus, context, expected state and observed state. Trace only interfaces that could generate the discrepancy. At each boundary distinguish what goes in, the controlling state/configuration, what transforms it, and what is observed coming out. Preserve the exact version, timing and conditions when those affect causality.

A system description lists components. A diagnosis identifies the earliest boundary at which a competing mechanism would produce different evidence. Do not assume the first visible symptom is where the fault originates.

## Discriminate without anchoring

Retain plausible alternatives until an observation distinguishes them. Give each live explanation a prediction that could be wrong. Choose an available, safe test by the degree to which its possible results change the decision, weighed against cost, delay, disturbance and reversibility. An experiment that would produce the same result under every hypothesis is not a discriminator.

For a vehicle telemetry delay: source timestamps show whether the device generated stale samples; sequence numbers and broker receive times can separate transport buffering from upstream sampling; ingestion and query times can separate cloud persistence from UI refresh. Actual available signals vary. An apparently healthy parser unit test narrows one hypothesis but does not certify the device-to-dashboard path. If diagnostic instrumentation is missing, identify the observable gap without pretending a measurement was taken.

When evidence contradicts the current model, update affected dependencies and preserve unrelated accepted facts. If no decisive observation can be obtained, state the competing explanations and the safest reversible next action.

## Choose solutions against needs and constraints

Separate the stakeholder's problem and desired change from the suggested implementation. Ask which decision, burden or failure the solution should improve, and what evidence could show improvement. Consider a simpler nontechnical process or a limited pilot where it could meet the need better than an immediate full system.

Compare feasible options with attention to hard constraints, integration cost, failure modes, reversibility, scope of uncertain assumptions and switching cost. A recommendation should disclose the assumption that most threatens it and the evidence or threshold that would change it. Do not invent weights, adoption metrics, customer interviews, or test outcomes.

An explicit user-required means stays binding. Needs analysis can refine execution and warn about value risk; it cannot silently replace an authorized requested method.

## Connect choice to completion

A selected repair or design is not an observed endpoint. Return a bounded action and its success predicate to Execution, including the interface or failure mode that must be rechecked. Quality assesses which outcome has actually been established: edit/source, local test, integrated behavior or realized stakeholder benefit.

Use the minimal path for trivial known facts, deterministic local faults and reversible low-risk choices. The absence of a full diagnostic study is not a defect in those cases.
