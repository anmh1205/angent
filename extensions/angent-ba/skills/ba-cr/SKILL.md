---
name: ba-cr
description: Business analysis cr specialist.
---

# ANGENT BA: cr

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/cr/SKILL.md

## Portability and authority

Use domain-specific steps below as methodology, not as authority or proof of tool execution. Original Claude-specific scripts, hooks, subagents, filesystem paths and approval levels are illustrative until verified in the current environment. ANGENT Root owns intent and routing; Execution owns writes and read-back; Quality verifies outcomes. Honor project naming and do not invent decisions. Validate completed Markdown with extensions/angent-ba/scripts/validate_documents.py when applicable. Jira and Confluence writes require current provider versions, granted permissions, idempotency review and read-back. Original agent-specific lifecycle or helper scripts are not assumed installed; report any validation that could not run.


# /cr — Change Request (record + impact + rollback + guided apply)

## Goal

Record a scope change as a self-contained Change Request — `docs/cr/CR-{YYYYMMDD}-{NNN}.md` (type `change-request`) — carrying the Impact Matrix (affected IDs across the spine), the Detailed Impact, and the Rollback Plan. With `--apply`, walk the Apply order and edit each affected doc as an versioned diff.

## Constraints

- **Group C\*** (`feature-bootstrap.md`): project-level; consumes any doc. The CR file is **self-contained** — Impact Matrix + Detailed Impact + Rollback live INSIDE it (no separate `docs/impacts/` file, per `naming-conventions.md`).
- **Mint `CR-{YYYYMMDD}-{NNN}`** — date-based, project-wide, max+1 for the day.
- **Record first, apply second** — `/cr "<change>"` writes the CR record (L1); `--apply CR-...` executes the Apply order (per-doc versioned diffs). Never apply without a recorded CR.
- **Impact Matrix cites real IDs** — every affected row names an existing FR/US/E-/…; `/gap` later flags a CR whose Impact names a nonexistent ID (drift).
- **Rollback is mandatory** — every CR carries a rollback plan (revert the IDs, restore prior states); an apply without a rollback path is BLOCKING.
- **Validate before done** — BA Markdown validation on the CR file (step 7).

## Inputs

```
/cr "<change description>"            # record the CR (Impact + Rollback), no edits yet
/cr --apply CR-20260801-001           # execute the Apply order (per-doc versioned diffs)
```

## Approach

### Record mode (`/cr "<change>"`)
1. **Understand the change** — interview (one batched round): what changes, why, which features/IDs are affected, is it reversible.
2. **Build the Impact Matrix** — scan the vault for the affected IDs (FR/US/E-/screens…); each row: ID + doc + nature of impact (add/modify/remove) + the new value.
3. **Draft the Apply order** — the sequence of per-doc edits (dependencies first; e.g. SRS before the stories that slice it).
4. **Draft the Rollback Plan** — the reverse sequence + prior values to restore.
5. **scoped change preview** — affected-ID count + apply-order summary + rollback confidence.
8. **Output report** — CR id + next (`--apply` when ready).

### Apply mode (`--apply CR-...`)
1. **Read the CR** — the Apply order + Impact Matrix.
3. **Walk the Apply order** — per doc: show the versioned diff → on approval, Edit → set the activity log env → next. A step whose target doc changed since the CR was recorded → HARD STOP (re-assess impact).
4. **Tick the CR's applied-status** per step; on completion stamp `applied: {date}`.
5. **Output report** — steps applied + any that needed re-assessment.

## Gotchas

- **Apply ≠ record** — a recorded CR with no apply is a normal "logged but not done yet" state; don't auto-apply.
- **Stale impact is the killer** — if a target doc changed after the CR was recorded, the Apply order's diffs are wrong; HARD STOP and re-assess rather than apply a stale diff.
- **Rollback or don't ship** — an irreversible change with no rollback path must be called out at record time, not discovered at apply.
