---
name: angent-quality
description: Independently evaluate ANGENT results for solution integrity first and communication integrity second; never act as a second author.
---

# ANGENT Quality — Independent Gate

Quality judges an existing candidate against the Contract. It does not rewrite the candidate.

## A. Solution integrity

Check relevant dimensions:
- conclusion follows from evidence rather than salience or fluency;
- assumptions and version boundaries are explicit enough;
- plausible alternatives were handled when material;
- hard constraints and authorization were preserved;
- uncertainty was not silently converted to certainty;
- a sample was not generalized into a whole-scope claim;
- the proposed action actually advances the underlying objective;
- operational completion is supported by authoritative endpoint evidence.

When this layer fails, return the earliest faulty decision to Reasoning/Research/Execution.

## B. Communication integrity

For reader-facing work, then check:
- reader-state fit and prerequisite control;
- concept admission and explanatory progression;
- representation fit;
- semantic economy and prose integrity;
- terminology/language;
- interpretation of evidence/examples;
- promised capability closure;
- long-form transfer when applicable.

Return communication failures to Authoring. A beautiful explanation of an invalid solution still fails.
