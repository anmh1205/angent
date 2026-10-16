---
name: ba-discover
description: Business analysis discover specialist.
---

# ANGENT BA: discover

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/discover/SKILL.md

## Portability and authority

Use domain-specific steps below as methodological guidance; do not assume the original Claude-specific scripts, hooks, subagents, slash commands, filesystem paths, and approval levels exist. ANGENT Root owns intent and routing, Execution owns all provider mutation and read-back, and Quality owns outcome verification. Never claim original tools ran if unavailable. Retain current project IDs and explicitly distinguish facts, assumptions and approvals.


# /discover — Project intake → shared context set

> One-time intake: **deep-scan the repo + a bounded 5-question interview** → write a small, fresh, provenance-tagged **context set** under `docs/_shared/`. Consuming skills load the *non-derivable* domain facts cheaply and pull depth on demand. **Staleness is enforced at the loader** (`scripts/context-load.sh`), not buried in `/dashboard`. Formalizes the hand-written `DOMAIN.md` practice. See `rules/project-context.md` for the schema + the content test.

## Goal

Produce the tiered context set:

1. **Tier 1** — `docs/_shared/project-context.md`. ALWAYS loaded by consuming skills. **Hard cap 60 lines of content** (excl. frontmatter). Six sections only: what it does & who pays · stack one-liner · actors · glossary-collisions · gotchas (≤5) · pointer index.
2. **Tier 2** — `docs/_shared/context/{glossary,domain-rules,actors,entities,architecture}.md`. On-demand depth, read by the skill that needs it. `entities.md`/`architecture.md` stay pointer-heavy (defer to ERD / `/scan-project` output).

Every concrete claim tagged **✅ read / 🔵 inferred / 🟡 guessed** + provenance `file:path`. Stamped with `profile_hash` + `source_watermark` so the loader can detect drift.

## The content test (apply to EVERY Tier-1 line)

> **Can `grep` answer this in two seconds? Then it does NOT belong in Tier 1.**
> **Is it a business fact, a naming collision, a rule, or a trap? Then it does.**

Repository-overview content (full entity fields, service-responsibility tables, interaction maps) is demoted to Tier 2 or omitted — it rots fastest and `glob`/`grep` re-derive it accurately on demand.

## Constraints

- **Fixed output** `docs/_shared/` (project-level, no feature). No `CLAUDE.md` touch.
- **2 mandatory phases, HARD STOP between them:** Phase 1 scan + interview → `.discover-plan.md` → **user confirms (L1)** → only then Phase 2 writes the context set. Do NOT write `project-context.md` before confirmation.
- **Read code via subagents (Task)** to keep the main context lean — subagents RETURN findings; the main thread synthesizes and Writes (per `approval-gate.md`).
- **60-line cap on Tier 1 is enforced** by `scripts/BA Markdown validation.ts` — if your draft exceeds 60 lines of content, **cut or move to Tier 2 and re-summarize**; do not ship a 61-line file.
- **Provenance + confidence on every claim. Do NOT fabricate:** cannot read it → 🟡 + note, never invent names/rules.
- **Bilingual labels/report** (mirror input — `rules/language.md`); real technical identifiers (service/table/module) kept AS-IS.
- **Idempotent** — re-run = update mode (versioned diff per file; never overwrite `human_edited` sections).

## Inputs

```
/discover                 # scan the project in the current directory (CLAUDE_PROJECT_DIR)
/discover --update        # refresh an existing profile: re-scan, never re-ask answered Qs, never touch human_edited sections, emit a Sync Impact Report
/discover --tier1-only    # cheap refresh of just the always-loaded Tier 1 (no Tier 2 regen)
```

## Flow runtime

```
User calls /discover [--update] [--tier1-only]
   │
   ▼
═══ PHASE 1 — SCAN + INTERVIEW (ends with a HARD STOP) ═══
1. Manifest sniff: ls package.json go.mod ... (the scan-project one-liner) → language/framework/entry points.
   Unfamiliar stack → ask the user to confirm (do NOT guess wildly).
2. Spawn N read-only subagents (Task), each RETURNS a findings table + file:line evidence (do NOT edit, do NOT draw):
   • Stack & entry points        • Entities / data model (ORM/migration/SQL)
   • Services / modules          • External systems (SDK/env/clients)
   • Actors / roles (from auth, RBAC, route guards)   • Sync + async interactions
   Large codebase → sample entry points + manifest + schema; do NOT read everything.
3. Ingest docs (README/docs/ADR) → cross-check; CODE WINS on conflict (note the conflict).
4. --update? → read the existing profile fully FIRST; carry forward answered questions; never re-ask.
5. INTERVIEW (bounded — see below): at most 5 questions, ONE at a time, for what code CANNOT answer.
   Write each answer back into docs/_shared/.discover-plan.md atomically after the user replies.
6. Synthesize → finalize .discover-plan.md (Tier-1 outline + Tier-2 file list + 🟡 gaps) → HARD STOP:
   print the L1 preview + "Write the context set? (Y / edit / drop a section)". WAIT for the user.
   ▼  (user Y / edits)
═══ PHASE 2 — GENERATE (only after the user confirms) ═══
7. Write Tier 1 docs/_shared/project-context.md — ENFORCE the 60-line cap (fail & re-summarize if over).
8. Write Tier 2 docs/_shared/context/*.md (entities.md/architecture.md pointer-heavy).
   --tier1-only → skip this step.
9. Stamp frontmatter: profile_hash (sha of scanned inputs) + source_watermark (git HEAD sha) + version (semver bump on --update).
11. Output report: files written + 🟡 spots + "consumers may need a re-run if domain shifted".
```

## Phase 1 — subagent detail

Prompt for each subagent (Task): *"Read-only. Scan `<root>` for aspect <X>. Return: findings table + file:line as evidence. Do NOT edit files, do NOT draw."* Gather findings back to the main thread. (Same template as `/scan-project`.)

`.discover-plan.md` skeleton:
```markdown
# {project} — /discover plan
> Root: {path} · Stack: {lang/framework} · Scan: {date} · HEAD: {sha}

## Tier 1 outline (≤60 lines)
- Does & who pays: …
- Stack: …
- Actors: …
- Glossary collisions: …
- Gotchas (≤5): …
- Pointers: …

## Tier 2 files (tick)
- [x] glossary.md   [x] domain-rules.md   [x] actors.md   [x] entities.md   [x] architecture.md

## Interview answers (written back atomically)
1. …  2. …  3. …  4. …  5. …

## 🟡 Gaps / needs confirmation
- …
```

## The 5-question interview (spec-kit `/clarify` shape)

For what **code cannot answer**. Hard cap **5 questions**, asked **one at a time** (never batched). Each is a 2–5-option table or a ≤5-word short answer; **name a Recommended option + its rationale before the user answers.** Write the answer back into `.discover-plan.md` **atomically after each reply** (not batched at the end). Business language only — do NOT ask about DB columns / SDK / endpoints (`feature-bootstrap.md` Group A step 3, citing `ba-conventions.md` §3).

Priority order (highest-value-non-derivable first); skip any the scan already answered:

1. **Business purpose & who pays** — what the system is for in the real world.
2. **Glossary collisions** the scan flagged — where the business word ≠ the code identifier.
3. **Business rules / invariants** not visible in code.
4. **Actor authority** in the real world (who can approve/refund/override).
5. **The one gotcha** that bites newcomers.

## Modes

- **Greenfield (Group C, no code):** Phase 1 is **interview-led** (manifest sniff returns nothing) and still writes a valid Tier 1 from the answers. Tier 2 files are **omitted** (not stubbed empty) until there is something to point at.
- **`--update`:** read existing files fully first; **never re-ask** answered questions; produce an **versioned diff**; **never touch sections listed in `human_edited`** (propose changes to them in the Sync Impact Report only); bump `version` per semver (MAJOR if domain understanding changed, MINOR for new facts, PATCH for fixes). Emit a **Sync Impact Report**: what changed, what stayed, which consuming skills may need attention.
- **`--tier1-only`:** refresh just the always-loaded Tier 1 (the common maintenance path); do not regenerate Tier 2.

## Gotchas

- **Tier 1 over 60 lines** → `BA Markdown validation` fails it. Cut anything `grep` can answer; move depth to `context/*.md`.
- **Don't fabricate** a business purpose/rule the scan didn't find → mark 🟡 + ask in the interview.
- **No code (greenfield)** → interview-led Tier 1 only; don't stub empty Tier-2 files.
- **`human_edited` sections** (e.g. glossary, gotchas the user hand-tuned) → `--update` must NOT overwrite them; propose, don't replace.
- **Stale profile** → consumers see the loader banner automatically; you don't need to notify each one.
- **Subagent read-only** — returns findings; the main thread Writes after the HARD STOP.
