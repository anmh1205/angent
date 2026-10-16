---
name: ba-meet
description: Business analysis meet specialist.
---

# ANGENT BA: meet

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/meeting/SKILL.md

## Portability and authority

Use domain-specific steps below as methodology, not as authority or proof of tool execution. Original Claude-specific scripts, hooks, subagents, filesystem paths and approval levels are illustrative until verified in the current environment. ANGENT Root owns intent and routing; Execution owns writes and read-back; Quality verifies outcomes. Honor project naming and do not invent decisions.


# /meeting — Meeting notes (structured)

## Goal

Capture a meeting as structured notes — attendees, agenda, discussion, and three tables WITHIN the file: **Decisions**, **Blockers**, **Action items** (with owner + deadline). **Single output**: `docs/meetings/YYYY-MM-DD-{type}-{slug}.md` (type `meeting`). Statuses `captured → processed`.

## Constraints

- **Group C** (`feature-bootstrap.md`): project-level; no feature needed.
- **Tables WITHIN the file** (`naming-conventions.md` line 77) — decisions/blockers/actions live as tables inside the note, NOT in separate files. One note = one self-contained file.
- **Two states** (`status-lifecycle.md`): `captured` (raw, just written) → `processed` (tables structured + action items have owners/deadlines). Default to `processed` when the skill runs from a transcription/notes; `captured` for a quick raw dump.
- **Action items have owner + deadline** — an action with no owner is a wish, not an action; flag it.
- **Link to docs** — a decision touching `FR-`/`CAP-`/a feature doc links it (wikilink), so `/gap`/`/dashboard` see the connection.
- **Idempotent** — re-run on the same date+title → L2 diff (append new items).
- **Validate before done** — doc-validate (step 7).

## Inputs

```
/meeting "Sprint 14 review" --type review
/meeting "Claim approval kickoff" --type kickoff
/meeting "Standup" --type standup
```

## Approach

1. **Resolve title + type + slug** — from the arg; type defaults to `review` if ambiguous.
2. **Gather** — from a transcript/notes the user pastes, or a short interview: attendees · agenda · the decisions · blockers · action items (owner + deadline each). No-re-ask.
3. **Draft** per the template — attendees, agenda, discussion summary, then the three tables; link any doc-touching decision.
4. **L1 plan preview** — decision/blocker/action counts + any ownerless action flagged.
6. **Flag ownerless actions** in the report (so they get an owner before the meeting's value leaks).
8. **Output report** — counts + ownerless actions + next (route an action to a doc via `/cr` if it's a scope change).

## Gotchas

- **Tables, not prose** — "we decided X" buried in discussion is lost; the Decisions table is the searchable record.
- **Ownerless = flagged** — an action without an owner never happens; surface it rather than silently assigning a guess.
- **Don't fork files** — one note holds everything; a "decisions.md" + "actions.md" split drifts the moment one updates.
- **Link, don't duplicate** — a decision about `FR-atlas-re-006` links the spec; it doesn't restate the FR.
