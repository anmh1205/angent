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

## Evidence limit

These are source-based design improvements. Structure tests, icon validation and textual review cannot establish that a live activated plugin has measurably better answers or Mermaid rendering. Claims of behavioral gain require comparable actual responses and destination-specific rendered figures on suitable positive and negative cases.
