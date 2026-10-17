# Composition and representation

Authoring translates an established solution model into an explanation without inventing missing logic.

The same composition engine serves chat and documents. Surface changes may alter scale, pacing and navigation; they do not replace relation-driven paragraph construction with a separate “document voice”.

## Section explanatory spine

Before composing a substantive section, select the dominant relation that must become usable: a mechanism, object/data trace, state transition, contrast, diagnosis path, dependency or procedure.

Every paragraph should either:
- advance that relation;
- establish a prerequisite needed for the next step;
- interpret evidence/example that makes the relation inspectable;
- state an exception/boundary that materially changes the relation;
- close a consequence/inference.

Do not let source order, note order or the full subject graph become section order.

If several unrelated relations remain equally primary, create a real section boundary or stage one after the other. “Everything is relevant” is not an explanatory spine.

## Whole-answer argument and reading cost

An individual paragraph can be accurate while the overall report fails to justify its conclusion. Before composing a substantial analysis, connect the central answer to its material evidence, warranted inferences, conditions, alternatives and recommended actions. Do not use source order or an issue list as the document's argument. If an important action cannot be justified by a demonstrated cause or decision constraint, revise the conclusion or return the missing relation to Reasoning/Research.

For chat, build a short reading path to the supported answer and a longer path to the mechanism and evidence without repeating the same summary. A concise response still carries all decisive qualifiers; a long explanation must keep creating useful distinctions, not only new headings. Information density concerns knowledge gained per reading effort, not word count.

## Paragraph jobs

A paragraph may:
- establish a mechanism;
- repair a prerequisite;
- follow an object/event through layers;
- contrast a nearby case;
- interpret evidence/code/trace;
- explain a decision consequence;
- close an inference.

Do not force these into a visible template.

## Paragraph continuity

A paragraph is not a bag of individually correct sentences.

Choose the technical relation doing the work, then let each sentence advance, qualify, instantiate, contrast, or conclude that relation.

Prefer visible given→new progression:
- reuse the active object/state/referent where possible;
- introduce a new concept because the previous sentence creates a need for it;
- keep cause, condition, ownership, sequence or contrast explicit when it is the reason the sentences belong together;
- close the inference before switching to another relation.

Do not insert meta-teaching commentary between connected technical propositions merely to create a transition. If a sentence says only that something is important, should be remembered, will be discussed later, or should not be memorized, replace it with the rule/relation/consequence that justifies the comment or remove it.

This applies equally to a short response and a book chapter.

## Semantic economy

Keep sentences that contribute a necessary fact, relation, definition, evidence, boundary, exception, decision consequence or genuinely needed navigation.

Remove stock commentary that only announces importance, sophistication, lesson choreography or author intention.

Navigation is legitimate when document scale actually requires it—for example a cross-reference or scope boundary that changes how the reader should interpret the material. It should not become a narrator voice.

## Stable traces

For multi-layer mechanisms, preserve one stable object/event/value when possible.

Referential continuity often teaches better than catalogues of unrelated examples.

## Work from the missing inference

Suppose a reader knows that a program saves numbered revisions but believes
`current.json` must always identify the newest one. The missing relation is
between authoritative revision records and the replaceable shortcut. A
definition of each filename will not repair it. Follow one interruption across
the two writes, then distinguish coherent content from a fresh pointer.

A Vietnamese explanation can make that relation usable directly:

> Chương trình lưu nội dung revision 3 trước rồi mới cập nhật `current.json`.
> Nếu bị ngắt giữa hai lần ghi, revision 3 đã tồn tại nhưng con trỏ vẫn chỉ
> revision 1. Vì vậy, đọc được con trỏ không chứng minh nó mới nhất. Khi phục
> hồi, chương trình phải kiểm tra các revision hợp lệ và chọn số lớn nhất.
> Nếu bản khôi phục bị thiếu revision 2, chỉ kiểm tra “có revision kế tiếp hay
> không” vẫn có thể bỏ sót revision 3.

The trace earns the general rule: a cached locator and its underlying records
can disagree, so freshness needs an independent condition. A nearby transfer
probe asks which revision is recoverable if revision 3 is malformed and revision
1 is valid. The answer is 1, not blindly the highest filename. This example is
an illustration, not evidence that any reader or model passed a trial.

If the question instead asks only what a pointer does, a short exact definition
may suffice. If it asks for the implementation's behavior, inspect that code;
the explanatory example cannot establish runtime facts. A table is useful when
comparing restore states on the same axes; a diagram is optional when the
temporal gap is already clear in prose.

For an audit report, the same subject has a different job: establish the
observed stale-pointer fixture, the promised recovery invariant, why checking
only N+1 misses a gap, the supported consequence and the regression probe.
Keep normal sequential crash recovery distinct from partial-restore behavior.
Do not copy the teaching paragraph as a finding without that evidence boundary.

For a curriculum, first establish immutable records and pointers at the precision
needed for this inference; revisit concurrency only when the next unit actually
depends on it. Record that deferred dependency rather than treating a previewed
term as mastered. When a premise changes, revisit dependent units and examples,
preserving unrelated accepted material.

## Representation fit

Use:
- prose for a small set of connected claims;
- flow/state/sequence diagrams for inspectable relationships;
- tables for shared comparison axes;
- bullets for genuinely parallel peers;
- numbered lists for real procedures;
- code/source when exact implementation is evidence;
- logs/traces when runtime observation is evidence;
- screenshots/photos when exact UI/physical state matters.

## Probes

Ask:
- would another form reduce reader reconstruction work?
- if this representation disappears, is meaningful structure lost?
- can the reader tell what conclusion to draw?
- does every arrow/group/axis correspond to a real relation?

Mermaid is not a substitute for authentic schematics, waveforms or UI evidence.

For a consequential figure or a choice among flowchart, sequence, state, quantitative chart and sourced imagery, use `visual-explanation.md`. A visual must be validated in the destination; a source code block alone is not a rendered figure.
