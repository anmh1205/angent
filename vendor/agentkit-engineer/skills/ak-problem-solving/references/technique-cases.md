# Problem-solving technique mechanisms

These are the six stable Engineer 2.19.0 routes reduced to their load-bearing process, preserving use-case distinctions instead of copying all upstream prose. Choose only the mechanism matching the observed stuck pattern.

## Simplification cascades

Collect at least two or more recurring special cases or duplicated owner paths. Identify what changes and what remains invariant. Propose a common state/contract boundary that could remove multiple compensating rules. Compare the proposed abstraction to all important counterexamples; if it adds configuration or hidden coupling, it is not a simplification cascade.

## Collision-zone thinking

Pick a distant domain that shares a potentially useful **mechanism**, not just familiar language (e.g., queue backpressure vs traffic control). Transfer the mechanism as a hypothesis, map what corresponds and what breaks, then test it against concrete requirements. Do not publish a metaphor as a technical architecture without validating causal fit.

## Meta-pattern recognition

Observe the repeated sequence in multiple contexts: trigger, affected state owner, intervention, outcome. Abstract the relationship that predicts the outcomes, list cases where it would fail, and avoid prematurely building a generic framework. The useful result is a reusable decision rule or small shared mechanism with clear boundaries.

## Inversion exercise

State the alleged hard constraint (X must be true), invert it (suppose X is false), and trace the implications. Classify the original condition as a physical invariant, external contractual requirement, design choice or habit. Reconsider the solution space only for constraints shown to be optional; inversion cannot override law, user authorization or demonstrated system limits.

## Scale game

Explore multiple orders of magnitude, from zero/single to peak concurrency/size, fast vs slow external dependency, transient vs persistent state, days versus months of retention. Identify the point where the existing algorithm, ownership or retry mechanism changes character. Follow with measured load/reliability checks when possible; hypothetical extremes are not benchmarks.

## When stuck

Classify lack of progress: missing evidence, inaccurate system model, wrong ownership, dependency gap, unconstrained options or repeated unproductive trials. Choose direct measurement/reproduction, smaller scope, boundary tracing, counterexample or explicit owner decision accordingly. Escalation is justified when another round of the same method cannot improve the evidence.

## Combined use

Simplification + meta-pattern can locate common mechanism before removing duplicated cases. Collision + inversion can reveal an alternative architecture, then test its premise. Scale + simplification can show which abstraction fails under load. Combine only when the additional technique exposes a **new independent uncertainty**, not to inflate the process.
