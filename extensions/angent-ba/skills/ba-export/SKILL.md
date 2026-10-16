---
name: ba-export
description: Business analysis export specialist.
---

# ANGENT BA: export

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/export/SKILL.md

## Portability and authority

Use domain-specific steps below as methodology, not as authority or proof of tool execution. Original Claude-specific scripts, hooks, subagents, filesystem paths and approval levels are illustrative until verified in the current environment. ANGENT Root owns intent and routing; Execution owns writes and read-back; Quality verifies outcomes. Honor project naming and do not invent decisions. Validate completed Markdown with extensions/angent-ba/scripts/validate_documents.py when applicable. Jira and Confluence writes require current provider versions, granted permissions, idempotency review and read-back. Original agent-specific lifecycle or helper scripts are not assumed installed; report any validation that could not run.


# /export — Stakeholder package

## Goal

Bundle a feature's (or the whole vault's) BA documents into one stakeholder-facing package — md/html/pdf/docx — with a "Change history" section rendered from `docs/_shared/activity.log` (filtered by scope, per `changelog.md`). **Single output**: `docs/exports/{date}-{scope}{-feature}-package.{ext}` (type `export-package`).

## Constraints

- **Group B** (`feature-bootstrap.md`): needs ≥1 feature doc; empty vault → friendly abort.
- **Excluded from the activity log** (`changelog.md`) — exports are regenerated artifacts; the hook skips `docs/exports/`.
- **Change history from the log** — render the package's "Change history" by grepping `activity.log` for the scope's paths; do NOT stuff history into the source docs.
- **Formats** — md (always); html (single self-contained file); pdf/docx need `pandoc` (doctor checks it; missing → degrade to md+html, report).
- **Scope** — `--scope all` (every feature, project-level docs last) or `--scope <feature>` (that feature's set).
- **Idempotent** — re-run regenerates (a new dated package); old packages stay (they're snapshots).
- **Validate before done** — BA Markdown validation on the package (step 7, md format only).

## Inputs

```
/export --scope atlas-re --format pdf       # one feature, PDF
/export --scope all --format html           # whole vault, HTML
/export                                     # default: scope all, format md
```

## Approach

1. **Gate.** Empty vault → friendly abort. Resolve scope (feature set or all) + format.
2. **Collect the docs** — the scope's docs in reading order (URD → BRD → PRD → SRS → use cases → stories → tests).
3. **Render change history** — grep `activity.log` for the scope's paths; format per `changelog.md` (date · skill · @author · path · note).
4. **Assemble** — the docs concatenated (md) or converted (html/pdf/docx via pandoc) + the change-history section + a cover/TOC.
5. **scoped change preview** — doc count + format + change-history entry count.
6. **Write** the package. **Activity log** — NOT set for the export itself (excluded), but the env is set if any source doc is touched (it isn't — read-only over sources).
8. **Output report** — the package path + format + degraded (if pandoc missing) + next.

## Gotchas

- **Exports are snapshots** — they go stale; the source docs are the truth. Don't edit an export to "fix" content — fix the source, re-export.
- **Change history is derived, not stored** — it comes from the activity log each run; never hand-edit it into a doc.
- **PDF/DOCX need pandoc** — degrade gracefully (md+html) and say so; a silent pdf-missing is confusing.
- **Scope order matters** — stakeholders read top-down (why → what → system → tests); don't dump files alphabetically.
