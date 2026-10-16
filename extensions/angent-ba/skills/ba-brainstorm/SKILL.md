---
name: ba-brainstorm
description: Business analysis brainstorm specialist.
---

# ANGENT BA: brainstorm

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/brainstorm/SKILL.md

## Portability and authority

Use domain-specific steps below as methodological guidance; do not assume the original Claude-specific scripts, hooks, subagents, slash commands, filesystem paths, and approval levels exist. ANGENT Root owns intent and routing, Execution owns all provider mutation and read-back, and Quality owns outcome verification. Never claim original tools ran if unavailable. Retain current project IDs and explicitly distinguish facts, assumptions and approvals.


# /brainstorm — Idea exploration (BA discovery doc)

## Goal

Turn ONE raw idea into a structured brainstorm document — problem, affected users, idea sketch, success criteria, explorations, decisions, and explicit Open Questions. **Single output**: `docs/{feature}/brainstorms/{idea-slug}.md`. This doc is the root of the OQ cascade (`resolve-oqs.md`) — downstream `/urd` and `/brd` inherit its unresolved OQs.

## Constraints

- **1 fixed output** — `docs/{feature}/brainstorms/{idea-slug}.md` (type `brainstorm`). One idea = one file; a second idea for the same feature = a second file.
- **`--feature` optional** — auto-detect; **feature does not exist + an idea → derive slug + create** (entry point, `feature-bootstrap.md` group A — `/brainstorm` is THE comprehensive-interview skill, the one place a wide-ranging interview is its job).
- **Facilitate, don't dictate** — offer elicitation angles (SCAMPER-style what-if, role-play "how would {persona} react", constraint-flip) one round at a time; the user's answers are the content. Never fill sections with invented business facts.
- **L3 iterate allowed** — the doc is prose + ASCII sketches, it renders in chat; iterate on the sketch before L1 if the user engages.
- **OQs are first-class** — anything the user can't answer becomes an `- [ ] OQ-n:` item, never a guess. The OQ section format must match `resolve-oqs.md` (checkbox list, `[ ]`/`[~]`/`[x]`).
- **No-re-ask (`ba-conventions.md` §2)** — scan the idea seed + previous answers before each question round.
- **Idempotent** — same idea-slug re-run → update mode (versioned diff).
- **Validate before done** — run BA Markdown validation (step 9); exit 1 = fix before reporting.

## Inputs

```
/brainstorm "<idea>"                        # derive feature slug from the idea
/brainstorm "<idea>" --feature <slug>       # explicit feature (existing or new)
/brainstorm "<idea>" --feature payment      # second idea in an existing feature
```

## Approach

1. **Resolve feature + idea slug.** Derive the feature slug from the idea's domain noun (group A); derive the idea-slug from the idea itself. Both confirmable at L1.
2. **Interview — round 1 (the frame):** problem/opportunity · who is affected + their situation today · what success looks like. Batched, ≤5 questions.
3. **Interview — round 2 (exploration):** pick 1-2 elicitation angles that fit the idea (what-if flips, persona role-play, "what breaks at 10× scale", constraint removal). Offer the menu; the user picks or skips.
4. **Fact-list** — every answer + its origin (user round 1/2); unanswered items become OQ candidates.
5. **Draft sections** per the template: problem, affected users (table), idea sketch (prose or ASCII), success, explorations, decisions (table with rationale), out-of-scope, Open Questions.
6. **scoped change preview** — feature + idea slug + section fill summary + OQ count.
7. **Write** — create `docs/{feature}/brainstorms/` on first Write.
10. **Output report** — OQ count called out + the next step in the chain (`/urd {feature}`).

## Gotchas

- **Don't interrogate** — two rounds max by default; the doc can grow on a later run. A brainstorm that takes an hour of questions kills the idea's momentum.
- **Sketch ≠ spec** — the idea sketch stays at business altitude; "how would the API look" belongs to `/srs` or `/api-design` later.
- **One idea per file** — a second idea mid-interview → offer to split into its own file.
- **OQ format matters** — `resolve-oqs.md` parses the checkbox list; freeform prose OQs won't cascade.
