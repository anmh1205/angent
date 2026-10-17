---
name: ba-userguide
description: Business analysis userguide specialist.
---

# ANGENT BA: userguide

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/userguide/SKILL.md

## Portability and authority

Use domain-specific steps below as methodology, not as authority or proof of tool execution. Original Claude-specific scripts, hooks, subagents, filesystem paths and approval levels are illustrative until verified in the current environment. ANGENT Root owns intent and routing; Execution owns writes and read-back; Quality verifies outcomes. Honor project naming and do not invent decisions. Validate completed Markdown with extensions/angent-ba/scripts/validate_documents.py when applicable. Jira and Confluence writes require current provider versions, granted permissions, idempotency review and read-back. Original agent-specific lifecycle or helper scripts are not assumed installed; report any validation that could not run.


# /userguide — End-user manual

## Goal

Produce an end-user manual: one externally-exposed entry `docs/userguide/{feature}-userguide.html` (or `userguide.html` for the whole product) + a same-name bundle folder (`index.md` metadata, `data.js` content, `pages/*.md` zero-frontmatter, `images/`). Light mode only. The entry is the only file the user opens.

## Constraints

- **Group C** (`feature-bootstrap.md`): project-level or feature-scoped; an empty vault → friendly placeholder ("nothing to document yet").
- **Phased, scan-project shape** — Phase 1: scan the vault (docs/wireframes) → outline the manual (sections + page list) → HARD STOP (confirm the outline). Phase 2: generate the bundle.
- **Light mode ONLY** (`naming-conventions.md` line 82) — docs-style black/white + blue highlight; NO dark mode. End-users read printed/light screens.
- **Compact structure (entry + bundle)** — only `*.html` visible at top level; everything else in the bundle folder of the same name. Don't use bare `preview.html`/`index.md` at top level.
- **Pages are zero-frontmatter** (`naming-conventions.md`) — content only; metadata in the bundle's `index.md`.
- **Self-contained entry** — no CDN; inline CSS + the `data.js` content; double-click to run.
- **Source = the vault** — task guidance from the SRS/use cases/wireframes; screenshots from `images/` if provided. No fabricated steps.
- **Resolve-oqs Phase E** — the userguide is a downstream doc; inherit unresolved OQs from the chain (`resolve-oqs.md` globs `skills/userguide/**`).
- **Validate before done** — BA Markdown validation on the bundle index (step 8).

## Inputs

```
/userguide                          # whole product
/userguide --feature atlas-re       # one feature
/userguide --lang vi                # force language
```

## Approach

1. **Scope + scan** — whole product or `--feature`. Read the docs (SRS/use cases), wireframes (screen purposes → manual sections), URD personas (audience → altitude).
2. **Outline (Phase 1)** — the manual's sections + the page list per section + which screens/screenshots each needs. **HARD STOP** — confirm before generating.
3. **Generate (Phase 2)** — per confirmed page: task-oriented prose (how to do X, not how the system works), zero-frontmatter, image refs. Build `data.js` (content embedded) + the entry `.html` (light, self-contained, sidebar TOC).
4. **scoped change preview** (post-outline) — section/page count + audience altitude + screenshot gaps.
7. **Output report** — entry path + page count + screenshot gaps.

## Gotchas

- **Task-oriented, not system-oriented** — "How to approve a claim", not "The approval service records a transition". End-users care about their job, not the architecture.
- **Light mode is non-negotiable** — a dark manual printed on paper or read on a bright desk is hostile; don't "improve" it with dark mode.
- **The entry is the contract** — `docs/userguide/` top level shows only `*.html`; the bundle keeps it tidy (and Obsidian/IDE quick-switcher sane).
- **Don't skip the outline HARD STOP** — generating 20 pages from a guessed outline wastes a full run; confirm the shape first.
