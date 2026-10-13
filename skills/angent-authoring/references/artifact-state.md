# Artifact state

Long-form and iterative work must preserve semantic state across units and revisions.

Track when relevant:

- accepted revision pointer or digest;
- reader capabilities and established concepts;
- concept dependencies;
- terminology and notation;
- recurring examples;
- promised depth;
- accepted quality baseline;
- prerequisite debt;
- deferred promises;
- actual coverage.

This is compact semantic state, not a transcript.

## Revision rule

When revising an existing artifact:

1. load the accepted artifact state and canonical content;
2. identify the requested change and affected dependency closure;
3. produce a candidate against that baseline;
4. preserve unrelated established concepts, terminology and accepted strengths;
5. give candidate, baseline and repair intent to Quality;
6. advance the accepted revision only after the candidate is accepted and the destination result is verified.

## Concept dependency

Mention is not establishment. Record prerequisite relations when downstream understanding depends on them.

If a prerequisite model changes, units that rely on it must be reconsidered; unrelated units stay valid.

## Depth

Depth is measured by the capability created, not word count.

Useful capability levels are:

- recognize;
- explain;
- trace;
- predict;
- diagnose;
- implement or configure;
- verify or evaluate.

A unit should reach the level promised by its role.

## Novelty

A sentence, figure or example should add a fact, relation, inference, boundary or necessary prerequisite repair.

Repeated wording that does not change the reader model is noise. A compact reminder is justified only when the concept is fragile for the current inference or the new context changes its consequence.

## Examples

A technical example should be representative, inspectable, plausible, interpreted and bounded. State what generalizes and what is specific to the case.

A recurring example anchors the model but never replaces the general model.
