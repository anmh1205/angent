---
name: ak-coding-level
description: Set an explicit 0–5 explanation/style preference while calibrating technical depth to the user's domain and respecting runtime persistence limits.
metadata: {port: angent-fallback, mode: adapted}
---

# Coding Level — Portable Fallback

Stable Engineer 2.19.0 exposes a **user-settable coding level from 0 through 5**. It affects explanations, examples and presentation; it is not a measure of intelligence, a replacement for project instructions, or permission to omit required technical truth. The upstream Claude implementation saves `codingLevel` in `.claude/.ck.json`, injects guidelines on session start, and optionally installs discoverable output styles. None of those runtime effects exists merely because this fallback text is present.

## Explicit level contract

| Level | Upstream label | Reader model and output |
|---|---|---|
| 0 | ELI5 | No presumed programming background; explain vocabulary and mechanism through concrete situations, progressive steps and limited jargon |
| 1 | Junior | Build concept-to-code relationships, explain why decisions work and show complete small examples with expected behavior |
| 2 | Mid-Level | Cover common abstractions and patterns, cross-component interaction, failure modes and trade-offs |
| 3 | Senior | Prioritize architecture, dependencies, alternatives, scaling, integration and production implications |
| 4 | Tech Lead | Include delivery risk, ownership, migration, business/operational consequences and decision criteria |
| 5 | Expert | Default efficient technical language and deep trade-off analysis without forced introductory scaffolding |

These are **presentation defaults**, not qualifications tied to years of experience; users may be experienced in one area and new in another. Do not reduce level 0/1 to superficial notes or suppress important mechanisms at level 5.

## Use

When a user explicitly asks to set level N, validate it is an integer 0–5, use it for the requested conversation/task and confirm its scope. Explicit user direction outranks inferred experience. When no level is given, calibrate from the actual task and demonstrated domain competence; do not pretend a global level was written.

Within one topic, develop from prerequisites through examples, system relationships and limitations as needed for comprehension. Level changes exposition, not the acceptance standard for code, citations, tests, security or factual claims.

## Persistence and native integration

Use the active runtime's **actual** authorized preference/configuration mechanism if the user requests persistent behavior. The Claude/AgentKit-specific file `.claude/.ck.json` and optional `output-styles/` are native-only surfaces; inspect active setup before touching them. Preserve existing user-owned styles on normal updates and distinguish normal update, explicitly selected force replacement and fresh reset. Never overwrite user preferences or claim hooks/injection succeeded without read-back.

On a runtime without compatible persistent settings, apply the level to the current interaction and say the persistence limit when it matters. Do not embed a global self-declared competency level into AGENTS.md, hidden checkpoints or other unrelated project files.

## Output

Honor user requested detail/format, technical correctness and authorial coherence first. Use examples, vocabulary explanations, code and diagrams when they advance understanding; avoid mechanical checklists or ritual 'key takeaways'. 
