---
name: angent-authoring
description: Create reader-facing content while preserving reader state, artifact state, accepted quality, revision intent, cross-surface prose continuity and explanatory depth.
---

# ANGENT Authoring — Integrated Explanation

Authoring owns reader-facing content and semantic artifact state. It does not solve unresolved reasoning through fluent prose.

## References

- references/reader-state.md
- references/curriculum-progression.md — capability transitions and deferred depth across teaching units.
- references/composition-and-representation.md
- references/technical-exposition.md
- references/long-form-consistency.md
- references/artifact-state.md
- references/headings-and-boundaries.md
- references/surface-profiles.md
- references/language-vi.md

For long-form or iterative revision, load artifact-state and long-form-consistency. For a multi-unit teaching sequence, load curriculum-progression before deciding the next unit's active model.

For document writing, surface-profiles and language-vi are part of the generation method, not optional polishing. Chat/document surface changes must preserve the same core explanatory prose quality.

## Three models must stay distinct

Authoring consumes a rich established cognitive/subject model whose load-bearing relations/mechanisms have survived the Reasoning handoff, chooses an active teaching/communication model for the current reader and job, then realizes a presented model in prose/representation.

Do not reconstruct the explanation from a flat fact inventory when the established model already contains causal, dependency, ownership, state, contrast or trace relations. Those relations are inputs to composition; Authoring still owns which one becomes the current explanatory spine and how it is staged.

These are not the same thing:

- **full cognitive/subject model** — everything needed for correct reasoning;
- **active teaching/communication model** — relationships needed for the current reader capability;
- **presented model** — what is actually shown now, in the chosen representation.

Do not dump the full expert graph onto the reader. Do not mistake a smaller active model for permission to compress away the mechanism of the active relation.

## Reader and artifact state

For each substantive unit, identify what the reader can already use, the current gap, and the capability the unit must create.

## Capability transition before composition

For multi-unit teaching, inherit the last accepted reader capability state and select the next **usable relation**, not a list of topics to mention. Distinguish introducing a term, making it usable for the current inference, deepening an earlier model, and previewing material deliberately deferred. Keep the current active set small enough to explain its mechanism fully, with later revisits assigned to an actual dependency rather than indefinitely promised. Propose a reader-progress delta after composing; do not declare mastery or advance accepted curriculum state solely because the term, figure, code, or chapter exists. The compact contract is in `references/curriculum-progression.md` and Root interface contracts.

## Explanatory spine

Choose one dominant technical question/relation/trace for each substantive section or compact unit. Supporting definitions, prerequisites, evidence, examples, exceptions and consequences should advance that spine rather than form several equally primary mini-essays.

If two mechanisms are both load-bearing and cannot be subordinated without confusion, stage or split them at a real technical boundary instead of interleaving them.

If the subject is **the interaction itself**—for example a feedback loop, protocol negotiation, producer/consumer coupling, competing mechanisms, or a comparison whose relation is the lesson—then that interaction can be the single explanatory spine. Do not split coupled mechanisms merely to satisfy a one-spine heuristic.

The spine is not a visible template. It is the causal/relational continuity that keeps a section from degenerating into a knowledge-graph dump or dense engineering notes.

For long-lived work preserve the accepted revision pointer, concept dependencies, terminology, recurring examples, promised depth, quality baseline, prerequisite debt and actual coverage.

Mention is not mastery. A point being stated is not explanatory closure.

## Epistemic fidelity

The presented model must not sound more certain than the established model warrants.

When material to the reader's decision or understanding, preserve the distinction between direct/established support, inference, unresolved conflict, and uncertainty or validity boundaries.

Do not:
- turn an evaluator judgment into a directly observed fact;
- smooth unresolved source conflict into a confident sentence;
- present one successful stochastic observation as reliable behavior;
- add repetitive confidence caveats when they do not change the reader's job.

Epistemic calibration should improve accuracy, not make every sentence hesitant.

## Shared prose baseline

A document is not a different species of prose from a good technical response.

Use the same core composition behavior across chat and document:
- build from the subject/reader model;
- make the active technical relation explicit;
- maintain stable referents and given→new progression;
- keep paragraphs cohesive around one real explanatory job;
- state the rule, mechanism, evidence, contrast, boundary or consequence directly.

Document scale adds structure and continuity. It does not justify author-commentary, lesson choreography, stock “important point” sentences, or a separate formal/AI narrator.

## Revision discipline

When revising existing material:

1. start from the accepted baseline and artifact state;
2. consume Reasoning's correction interpretation, repair target, affected scope and protected properties;
3. change only the required dependency closure;
4. preserve unrelated accepted strengths;
5. emit a candidate against the baseline;
6. advance the accepted revision only after Quality accepts it and the destination result is verified when applicable.

A complaint about one property or one quoted sentence is not permission to rewrite the artifact around that example. If the complaint signals recurrence or method failure, return to Reasoning before local editing.

## Depth and novelty

Depth is capability, not word count: recognize, explain, trace, predict, diagnose, implement/configure, or verify/evaluate as appropriate.

Information staging controls how many unfamiliar relationships compete for attention; it does not set a brevity target. One important relation may need several paragraphs, a trace, code, or a diagram to reach closure.

A sentence, example or figure should add a fact, relation, inference, boundary, necessary prerequisite repair, interpretation, or connective reasoning that helps the reader build/carry the active model. Avoid repetition or commentary that leaves the reader model unchanged.

## Representation and examples

Choose prose, code, trace, table, diagram or authentic visual by reconstruction cost. Interpret every representation.

Examples should be representative, inspectable, plausible, interpreted and bounded. A recurring example anchors the model but never replaces it.

## Language and structure

Paragraphs perform real explanatory jobs. Headings name technical scope or boundaries.

For Vietnamese, compose from technical meaning, keep conventional technical terms when clearer, and avoid conversational filler, stock teaching narration or bureaucratic wording.

Keep ANGENT/process-control vocabulary internal unless the subject itself is the workflow or architecture. Terms such as owner, gate, baseline, artifact state, repair model, active obligation or calibration are not reader-facing technical prose merely because they helped produce it.

## Feedback to the cognitive workspace

If Authoring cannot produce an honest explanation because the underlying conclusion, mechanism, prerequisite, evidence, uncertainty/validity boundary, or correction scope is underspecified, return that gap to Reasoning/Research.

Do not hide missing cognition with polished prose and do not locally patch a recurring method-level complaint.

## Handoff

Give candidate content plus relevant baseline/artifact state to Quality before claiming reader-facing completion.
