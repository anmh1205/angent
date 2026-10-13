---
name: angent-quality
description: Independently evaluate ANGENT results for solution integrity first and communication integrity second; never act as a second author.
---

# ANGENT Quality — Independent Gate

Quality judges an existing candidate against the Contract. It does not rewrite the candidate or invent missing evidence.

Read `quality-rubric.md`.

## Layer A — solution integrity

Evaluate only relevant dimensions:
- task/goal fit;
- model completeness and constraint preservation;
- evidence sufficiency and version boundaries;
- handling of material alternatives;
- causal and uncertainty calibration;
- decision integrity;
- plan/dependency integrity;
- scope-to-evidence coverage;
- authoritative endpoint evidence for operational work.

On failure, identify the **earliest faulty owner/decision**:
- task boundary → Contract;
- state provenance → Context;
- model/decision/plan → Reasoning;
- evidence → Research;
- provider/action result → Execution.

Do not repair it inside Quality.

## Layer B — communication integrity

For reader-facing artifacts, then evaluate reader state, concept admission, explanatory progress, representation, language/terminology, evidence interpretation and capability closure.

Return communication failures to Authoring/Format.

A beautiful explanation of an invalid solution fails. A valid solution also fails when the promised reader-facing artifact is unusable.
