# Response-method study — transfer without copying a model persona

This study informs Authoring and Reasoning; it is not a mandatory response template, a reproduction of any vendor system prompt, or a claim that a package instruction changes model weights.

## Sources and scope

- [Anthropic: publicly documented Claude Opus 5.5 system prompt](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-opus-5-5) — primary source for the published response instructions. It supports claims about the released text, **not** exhaustive knowledge of private production conditioning or observed reliability.
- [Anthropic: prompting for Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) — vendor guidance on task framing, agent work, output control and visual input; examples are product-specific rather than cross-platform requirements.
- Earlier Cogent source: `cogent-unified` authoring and `cogent/references/explanation-composition.md`, `representation.md`, `visual-research.md`, plus `cogent-exposition/references/chat-exposition-study.md` — prior designs retrieved from the user's owned plugin releases. Those texts are design evidence, not independently validated response outcomes.

## Reusable principles

Good chat responses control the reader's *next inference*, rather than maximizing visible headings, restating every premise, or narrating the assistant's effort. A useful answer may be a short verdict, a sustained mechanism, a concrete trace, or a discriminating comparison. The question and the reader's demonstrated understanding determine which.

On a follow-up, a request for clarification differs from a rejection of facts. If the user remains confused, distinguish a missing prerequisite, a wrong mental model, and a missing link between otherwise familiar concepts. Repair that local gap using a new explanatory route; do not recycle the same bullet inventory. Conversely, a brief expert follow-up should not reopen an introductory tutorial.

Uncertainty belongs next to the specific claim whose strength is limited. Explain what changes a decision, not generic caveats. In operational work, report meaningful progress or a verified effect rather than repeatedly describing activity. A finished answer does not need a promotional closing line.

Visuals should express a relation or evidence the text cannot convey as easily: temporal interactions, guarded state transitions, causal branches, numeric trends or actual physical/UI identity. Mermaid is an effective abstraction for some of these; authentic images, accurate plots, traces and schematics remain separate tools. Check actual render and attribution when these are material.

## Decisions in ANGENT

ANGENT already had the core decision/reader model, paragraph coherence, error/authority boundaries, and rule against mandatory visuals. These are protected baselines, not gaps requiring a new specialist or duplicated prose engine.

Changes concentrate on conversation repair, distinction between visualization types, source-matched image retrieval and rendered figure acceptance. They are integrated with existing Authoring, Research, Format and Quality responsibilities, not an additional sequential pipeline. Short ChatGPT starter prompts are separate from the actual skill instructions.

## Learning from ClaudeKit's task methods — target-aware transfer

The useful transferable mechanisms are not ClaudeKit's command count or repository organization. [Problem-first brainstorming](https://github.com/claudekit/claudekit-engineer/blob/main/claude/skills/brainstorm/references/problem-first.md) challenges a proposed solution by reconstructing the need and falsifiable assumptions; [scenario exploration](https://github.com/claudekit/claudekit-engineer/blob/main/claude/skills/ck-scenario/SKILL.md) widens a consequential decision to plausible state, actor, failure and timing counter-cases; [code review](https://github.com/claudekit/claudekit-engineer/blob/main/claude/skills/ck-code-review/references/spec-compliance-review.md) checks fidelity to requested outcomes before assessing polish; and [writing style guidance](https://github.com/claudekit/claudekit-engineer/blob/main/claude/skills/copywriting/references/writing-styles.md) analyzes dimensions of expression rather than imposing one voice.

ANGENT already has analogous abilities in Core Reasoning/Quality/Authoring and portable Engineer's Brainstorm, Predict and Scenario. The design opportunity is more accurate **selection, integration and transfer**: challenge unconfirmed means without overriding binding decisions; feed plausible disconfirming cases into a recommendation; test report relevance against the user's requested target; study strong prose for reader-state progression and paragraph dependency, not copywriting formulas. Keep specialist expansion conditional. ClaudeKit's hard gates, preset persona counts and specific tool commands are implementation choices, not universal mandates.

A representative comparison should include both a solution-first proposal whose underlying problem matters and a committed implementation request where problem reframing must not hijack scope; a long source audit whose details distract from target improvements; a short direct-answer counter-case; and the same explanation transferred into a technical document. Assess warranted recommendations and preserved reader understanding, not merely number of citations, styles or diagrams.

## Evidence limit

These are source-based design improvements. Structure tests, icon validation and textual review cannot establish that a live activated plugin has measurably better answers or Mermaid rendering. Claims of behavioral gain require comparable actual responses and destination-specific rendered figures on suitable positive and negative cases.

## Zephyr publishing regression, 2026-10

Three beginner Zephyr chapters on a structured document surface illustrate a potential **conversion of explanation to outline**. The first carries many technically relevant topics but sometimes crosses prerequisite boundaries too quickly; the second mixes build/runtime arrows and uses a hardware-dependent GPIO example in a simulator-first curriculum; the third is mostly a procedural build walkthrough with a mismatched code fence language for CMake. These observations were checked against the actual published text. They do not establish a causal trace of every preceding drafting step or justify a global verdict for uninspected chapters.

The repair is at the active reader/authoring method and destination conversion boundary: preserve the local reader-state delta, introduce mechanisms before using them, add working traces where they unlock understanding, and read back destination blocks independently. Treat the published artifact as the real outcome, not a successful write acknowledgement. A useful regression comparison needs a *previously understandable chat explanation* of the same subject relation and one actual published chapter; a source-only policy update is not an observed behavioral win.

The destination must also retain code-language identity and separate logical correctness of source from whether Mermaid renders as a figure. The code language mismatch is an observable formatting defect, not a reason to add more Mermaid.

## External writing-method crosschecks — 1.4.0

These are **design sources**, not proof that ANGENT has achieved the behavior.

- [Google Technical Writing: Paragraphs](https://developers.google.com/tech-writing/one/paragraphs) emphasizes logical dependency order and a coherent topic per paragraph. Apply the semantic connection principle, not a mechanical sentence-count target.
- [GAO Government Auditing Standards](https://www.gao.gov/assets/a76947.html) describes criteria, condition, cause and effect for relevant audit findings, and recommends action grounded in the finding. The applicable elements depend on the audit objective; do not fabricate an unsupported cause or force all reports into this framework.
- [Diátaxis](https://diataxis.fr/) distinguishes tutorial, how-to, reference and explanation by reader purpose. Use it to diagnose genre confusion, not to generate empty templates or prohibit legitimate mixtures of explanation and procedure.
- [Nielsen Norman Group: How Users Read on the Web](https://www.nngroup.com/articles/how-users-read-on-the-web/) supports early meaning and scannable navigation. Do not apply its word-count suggestions as a reason to delete a load-bearing mechanism in technical teaching.
- [Anthropic: Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) and [Skills for enterprise](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise) distinguish trigger accuracy, skill coexistence and output quality. A benchmark catalog and passing schema/structure CI do not establish improved answers; compare actual activated outputs with appropriate baselines.

ANGENT's generalization is to make the report or answer's decisive **claim → warranted explanation/evidence → inference/decision** understandable at appropriate reading depths. This is not a mandatory formatting pipeline. When source guidance conflicts with the actual task, preserve correctness and user intent rather than copying a vendor-specific stylistic heuristic.
