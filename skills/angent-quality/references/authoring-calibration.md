# Authoring calibration

Quality evaluates communication by failure mechanism, not by word count, heading count, visual density, or a forbidden-phrase list.

## Failure classes

### Correct facts, weak explanation

Symptoms:
- facts are individually true;
- causal/ownership/state relations remain implicit;
- reader must assemble the mechanism alone.

First locate the loss boundary. If Research/Reasoning established the relation but the candidate flattened it, return to Authoring. If the handoff itself lost or never established the load-bearing relation/mechanism, return to Reasoning/Research rather than asking prose to invent it.

Return to Authoring only when the established subject model is sufficient and the realization failed to expose the relation and interpretation.

### Surface-induced prose regression

Symptoms:
- chat/response prose is cohesive and natural;
- the same material becomes fragmented, ceremonial, generic or “AI-document-like” when moved into a document;
- document-specific narration/commentary appears even though the underlying subject model did not require it.

Return to Authoring: restore the shared response-quality prose/composition baseline, then add only document-scale structure/depth. Do not invent a separate formal-document voice.

### Multiple competing explanatory spines

Symptoms:
- every paragraph is individually relevant/correct;
- the section alternates among several mechanisms, layers or examples without one dominant relation;
- the reader must decide which details are central and reconstruct the path themselves;
- source/note order is visible in the prose.

Return to Authoring: choose the dominant explanatory spine, subordinate prerequisites/evidence/exceptions to it, and split only at a real technical boundary.

Counter-case: do **not** flag multiple named mechanisms merely because more than one appears. When their interaction, feedback, negotiation, coupling or comparison is itself the load-bearing relation, that relation is one valid spine. A forced split would destroy the mechanism being taught.

### Internal process vocabulary leakage

Symptoms:
- reader-facing technical prose contains ANGENT/workflow terms such as owner, gate, baseline, artifact state, repair target, active obligation or calibration even though those are not concepts in the subject;
- the document narrates its own quality/reasoning process instead of the domain mechanism.

Return to Authoring: translate internal control state into the subject's objects, relations, evidence and consequences. Keep process vocabulary internal unless the document is actually about that process.

### Meta-commentary replacing technical progression

Symptoms:
- sentences announce importance, what to memorize, what “we” will learn, or the author's intention;
- neighboring technical claims become separated by coaching/commentary;
- prose sounds conversational or AI-generated despite correct facts.

Return to Authoring: replace commentary with the actual rule, relation, mechanism, boundary, evidence or consequence. Do not create a lexical blacklist.

### False reader-state promotion and curriculum compression

Symptoms:
- a concept is marked established because a glossary/heading/diagram mentioned it;
- a chapter jumps from a definition to advanced design without the intermediate inference;
- later chapters rely on an expert-level concept that was only previewed earlier;
- the whole book is declared covered from chapter counts or a few acceptable samples.

Check an actual target inference or representative diagnosis using only what prior units have equipped the reader to know. Return missing subject relations to Reasoning/Research, premature admission or absent explanatory closure to Authoring, and unsupported quality claims to Quality's coverage gate. A narrow introductory overview is a negative control: it may legitimately preview concepts without promising mastery.

### Outline decay

Symptoms:
- later sections become short bullet catalogs;
- code/commands appear without explanation;
- chapter depth falls below comparable earlier material.

Return to Authoring with artifact/curriculum state. Do not pad sentences.

### Generic AI prose

Symptoms:
- paragraphs announce importance instead of conveying knowledge;
- repetitive stock commentary;
- polished but interchangeable prose;
- many abstract nouns and weak technical subjects.

Return to Authoring: replace commentary with concrete object, mechanism, evidence or consequence.

### Translation-shaped language

Symptoms:
- unnatural Vietnamese clause order;
- forced translations of established technical terms;
- administrative wording with no precision gain.

Return to the language profile and reconstruct from the technical proposition.

### Example without model

Symptoms:
- one case walks through commands/code;
- the reader cannot say which part generalizes.

Return to Authoring: establish/generalize the model and boundary.

### Model without example/evidence

Symptoms:
- dense abstractions and terms;
- no concrete trace, operation or observation.

Return to Authoring: add the smallest representative case or evidence.

### Decorative representation

Symptoms:
- Mermaid/image/table looks relevant but does not encode a decisive relationship;
- arrows/groups have weak semantics;
- an image is merely about the same product/category.

Remove or replace the representation.

### Bad heading architecture

Symptoms:
- headings are slogans, coaching or author commentary;
- navigation does not reveal the technical subject;
- micro-headings fragment one mechanism.

Return to Authoring: restructure by technical boundary.

### Repetition without information gain

Symptoms:
- later paragraphs restate established facts in new wording;
- examples repeat the same relation without adding a new consequence;
- reminders are longer than the inference they support.

Return to Authoring: retain only necessary prerequisite repair or new context-dependent consequence.

### Overcorrection

Symptoms:
- a complaint about one dimension causes the revision to maximize the opposite property;
- adding depth becomes adding length;
- adding visuals becomes diagram saturation;
- removing conversational prose makes the text bureaucratic;
- simplifying repetition removes prerequisite explanation.

Return to Reasoning: reconstruct the failed function, repair target and protected properties before another edit.

### Local patch without conceptual closure

Symptoms:
- a complaint causes one sentence to be patched;
- the same failure mechanism remains elsewhere;
- the revision contradicts neighboring sections;
- user examples are treated as the complete scope even though they expose a repeated generating pattern.

Return to Reasoning and load correction-interpretation. Repair the shared mechanism/affected dependency closure, not only the named example.

### Recurring failure despite an existing rule

Symptoms:
- the relevant rule/mechanism already exists in Authoring/Learning/Quality;
- the same behavior still appears;
- another wording tweak to the rule is proposed.

Do not strengthen wording by default. Audit whether the mechanism was retrieved, activated, routed early enough, owned by the correct component, or contradicted by another instruction/state.

### Repair regression

Symptoms:
- the requested defect improved;
- an accepted strength, constraint or neighboring explanation became worse;
- the candidate is good in isolation but worse than the accepted baseline on a protected dimension.

Reject the candidate. A repair must pass both target and preservation checks.

### Oscillating revision

Symptoms:
- successive revisions alternate between previously rejected states;
- fixing A repeatedly reintroduces B;
- the user restates the same mechanism-level complaint.

Stop local Authoring repair and return a recurrence/oscillation finding to Reasoning.

### Chat turned into a document

Symptoms:
- simple answer gets many headings/stages/frameworks;
- explanation overhead exceeds the question.

Return to the Chat surface profile and compress visible structure, not reasoning quality.

## Calibration questions

For reader-facing technical output ask:

1. What capability did this unit create?
2. Which sentence/figure/code example carries the decisive mechanism?
3. Is every new premise actually established?
4. Does each repeated passage add information needed here?
5. For a revision, what improved relative to baseline and what protected property could regress?
6. Did any fluent passage hide unresolved reasoning/evidence?
7. For long-form work, is depth comparable with earlier units of similar difficulty?
8. Did the surface change preserve the same core prose/composition quality?
9. Did a complaint get interpreted at the correct abstraction level, or merely patched at the latest example?
10. If the same failure recurred despite an existing rule, did the repair investigate activation/routing/ownership rather than add another guard?

A candidate fails when it makes the reader reconstruct too much, violates active obligations, regresses a protected property, or preserves the generating mechanism behind a recurring complaint even if the named example was fixed.

## Conversation repair and representation counter-cases

When a user says an earlier explanation did not make sense, compare the changed answer against the actual conceptual gap. A successful revision changes the reader's usable model with a grounded distinction or trace; a longer paraphrase is not evidence of improvement. A previously correct short expert answer is a negative control: do not inflate it into an elaborate tutorial.

For visual work, test both selection and fidelity. A protocol interaction may need a sequence diagram, while a stateful lifecycle needs guarded state transitions; substituting one for the other can fabricate semantics. A photo of a similar board is not an exact connector reference. A source Mermaid block that never renders is not an accepted illustration. Equally, a simple two-sentence distinction should remain prose when an extra diagram offers no new information.

Check source/model/revision match, arrow and axis meaning, destination renderer support, actual legibility, rights and nearby interpretation. Distinguish a better documented method from observed gains in real outputs; do not claim behavioral improvement from these checks alone.
