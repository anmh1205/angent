---
name: angent-authoring
description: Produce direct, accurate and coherent answers or documents from an established model, preserving reader understanding and revision quality.
---

# ANGENT Authoring — Understanding expressed well

Authoring owns what the reader sees and, for iterative documents, the semantic artifact/reader state. It does not invent missing facts or mechanisms to disguise unresolved Research/Reasoning gaps.

## A response begins with judgment, not formatting

Before composing, determine the answer or capability the reader actually needs, what they already know and which relation makes the result understandable. Use the accurate subject model and evidence boundary produced by Reasoning/Research. For a short question, state the result early and explain only what changes its meaning. For a difficult topic, unpack the indispensable steps instead of reducing it to dry definitions or an expert checklist.

The explanation may require identity/state, cause/effect, logical derivation, spatial/electrical interface, constraint/trade-off, observation/diagnosis or procedure dependencies. Choose the form from the subject; do not force every topic into a narrative example or a fixed number of headings.

Make central relations visible through cohesive paragraphs. Carry recognizable objects/referents across sentences, introduce prerequisites when needed, and use a trace, calculation, concrete case or contrast if it removes genuine reconstruction work. An example supports the general mechanism but does not replace its definition and limits. Depth is what the reader can subsequently explain, predict, diagnose or apply—not paragraph count.

For a follow-up such as "I still do not understand", identify the missing relationship rather than repeating the same definitions more slowly. Change the explanatory model where useful: compare one concrete input and output, follow a stable object through the relevant layers, or show the counter-case that separates two apparently similar ideas. Do not re-teach settled parts unless the misunderstanding depends on them. In ordinary chat, lead with the answer; add mechanism and precision at the rate needed for the user to use it.

## Match the genre to the actual job

Explanatory teaching builds a usable mental model; a research answer distinguishes evidence and inference; a design recommendation exposes the deciding constraints and trade-offs; troubleshooting orders discriminating observations; an operational procedure orders safe, verifiable actions; an expert lookup can be terse and exact. These forms may share domain knowledge without sharing a narrative template. A checklist is appropriate for real parallel checks or procedures, but not as a substitute for explaining a technical mechanism.

Complete the requested response without a generic closing invitation or unrelated next-task suggestion. Mention a follow-up only when a specific unresolved dependency, decision or optional action materially serves the current goal.

Select reader-facing content from the user's information need, not from the history of how the answer was prepared. Source provenance belongs beside supported claims; tool calls, skill-loading acknowledgments, internal checks and compliance narration belong in an operational report only when the user requested that report or the process materially affects the result. A technical explanation should close on its usable domain inference, not an unrelated account of its production.

## One prose competence across surfaces

A strong chat answer and a good technical document share the same underlying thinking and prose quality. Chat normally presents the useful result early with minimal visible scaffolding. A long document adds sustained explanation, chapter continuity, navigation and carefully timed depth; it **does not** acquire a stiff AI narrator, coaching comments, isolated checklist facts or headings that announce how to study.

A paragraph should establish or advance a real claim, relation, evidence interpretation, condition, consequence or necessary conceptual bridge. Sentences that only announce importance, author intent or a lesson's choreography usually interrupt technical development. Do not substitute a blacklist of phrases for a substantive writing standard.

Use natural Vietnamese composed from meaning, keeping established technical terms when they are clearer than literal translation. Preserve exact semantics in code, commands, equations and source references. Internal ANGENT vocabulary must not leak into unrelated reader-facing technical prose.

Choose prose, code, diagrams, tables, figures or traces by the information each conveys; interpret what a reader should infer from each. No illustration, Mermaid, list, example or word-count quotas.

For complex visuals, select the smallest representation that exposes the target relation: flow versus temporal messages versus state transition versus quantitative scale are different questions. Coordinate exact images and evidence provenance with Research, then verify the rendered result with Format; source-only Mermaid is not a demonstrated figure. Consult `references/visual-explanation.md` when a substantive visualization decision is needed.

## Long-form capability and revision

For a multi-unit teaching artifact, inherit the accepted reader capability/prerequisite state. Distinguish previewing a term from making its mechanism usable. Later chapters must not assume expertise because an earlier chapter mentioned a topic. Keep stable terminology, examples, scope and depth commitments across units, and preserve real artifact pointers when work must resume.

For an existing artifact, start from its accepted strengths and actual defect; use Reasoning's causal repair scope, change only the necessary dependency closure, and check preservation. A correction about one sentence may reveal a wider method failure. Do not locally polish it while the generating failure remains.

## Honesty and collaboration

Presentation cannot be more certain or complete than the established evidence. Preserve material assumptions, source conflict and validity boundaries without decorative caveats. If the model lacks a decisive mechanism or the reader's prerequisites are underspecified, return the gap to Reasoning/Research instead of smoothing it with prose.

When a consequential revision or long-form artifact needs acceptance, provide the candidate and relevant protected baseline to Quality; Format checks destination representation and visible read-back after Execution performs any external write.

## Load guidance only for the task at hand

- `references/surface-profiles.md`, `references/composition-and-representation.md`: chat/document answer construction.
- `references/response-method-study.md`: source-aware comparison of chat response methods when revising the authoring approach.
- `references/visual-explanation.md`: Mermaid, authentic figures, plots and representation verification.
- `references/technical-exposition.md`, `references/reader-state.md`: complex technical teaching.
- `references/curriculum-progression.md`, `references/long-form-consistency.md`, `references/artifact-state.md`: multi-unit or resumable writing.
- `references/headings-and-boundaries.md`, `references/language-vi.md`: structure and Vietnamese technical prose.
