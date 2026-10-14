# Correction interpretation

A user correction is not automatically a local edit request.

Treat the user's wording and examples as evidence about a failed property, failed mechanism, or failed working method. First determine what level actually failed; only then choose repair scope and owner.

## Interpret before repairing

For a meaningful correction, distinguish:

- **observed example** — the sentence, file, section, tool action, or output the user pointed to;
- **failed property** — what is wrong about the observed result;
- **candidate mechanism** — what process/model/owner behavior plausibly generated it;
- **abstraction level** — local artifact, repeated artifact pattern, working method, owner/interface/state model, or collaboration model;
- **causal scope** — other places that share the same mechanism;
- **protected properties** — accepted strengths that must survive repair.

Do not infer that the observed example is the entire affected scope.

## Signals that the complaint is not local

Escalate interpretation before editing when one or more are present:

- the same complaint or close variant has appeared before;
- the user says the system is “again”, “still”, “keeps”, “already told”, “not local”, “systemic”, “method”, “thinking”, “workflow”, or otherwise criticizes the way the work is being produced;
- several examples from different outputs share the same failure;
- a previous repair fixed one instance but the defect reappeared elsewhere;
- fixing one symptom repeatedly causes another accepted property to regress;
- the user points to a stronger positive baseline and asks why current output diverges from it.

These are recurrence/mechanism signals, not invitations to append more local rules.

## Reconstruction for recurring or method-level corrections

Before proposing another patch:

1. recover the relevant accepted/positive baseline;
2. retrieve prior complaints and promoted mechanisms for the same decision/failure class;
3. compare the current behavior with that baseline;
4. identify the common generating mechanism, not only the newest symptom;
5. inspect the controlling owner/interface/state model;
6. determine which downstream artifacts are affected by that shared mechanism;
7. choose the smallest systemic change that can prevent recurrence;
8. use the user's examples as calibration cases for the mechanism.

If the mechanism is not yet established, keep alternatives live and gather discriminating evidence instead of hard-coding a guessed rule.

## Example versus rule

Weak interpretation:

> “The user disliked the sentence ‘Điểm quan trọng là’, so ban that phrase.”

Better interpretation:

> “The document generator is inserting author-commentary/meta-teaching sentences that do not advance the technical model. The repair target is the prose-generation method and sentence utility, not one lexical phrase.”

Weak interpretation:

> “The user says the chapter is shallow, so increase length.”

Better interpretation:

> “The authoring method is treating topic mention as explanatory closure. Restore mechanism, relation, trace, and reader capability where the active model requires them.”

## Scope discipline

Systemic does not mean global rewrite.

Expand only across units sharing the failed mechanism. Preserve unrelated accepted work. A broad architectural correction may still result in a small code/doc delta when one controlling rule/interface causes the behavior.

## Completion

A correction is not complete when the pointed example is gone.

It is complete when:

- the inferred failure mechanism is repaired at its causal scope;
- the original example and analogous cases no longer exhibit the defect;
- protected strengths remain intact;
- recurrence risk is reduced by changing the generating method or controlling state, not by memorizing the complaint wording.
