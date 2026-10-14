---
name: ak-journal
description: Maintain chronological technical journals as historical evidence without treating them as current authority, task state or promoted learning.
metadata: {port: angent-fallback, mode: adapted}
---

# Journal — Portable Fallback

## Load progressively

- `references/journal-semantics.md` — what a journal is and is not.
- `references/incident-entry.md` — capture hard failures/incidents.
- `references/using-journals.md` — retrieval, retrospective and Learning use.

## Use for

- meaningful implementation milestones;
- failed approaches worth preserving;
- production/staging incidents;
- difficult debugging sessions;
- important environment/provider observations;
- retrospective evidence.

Keep entries compact and linked to artifacts/commits/issues.

A journal is historical evidence—not AGENTS.md, not Continuity, not a current architecture decision and not an automatic global lesson.

## Stable 2.19.0 lifecycle and publication boundary
The native workflow offers `ak journal create` (stdin-compatible), `validate`, `list`, and `show` with dated collision-safe filenames. Use them only if native `ak` is installed; otherwise write and read back a local journal in the project's existing journal owner. Explicit journal requests are not suppressed by automatic closeout preferences. For automatic journal steps respect `--skip-journal` (when supported), then project/user `journal.auto`, then default. Record actual session evidence, changed artifacts, decisions, results and next steps, while keeping durable decisions and current work state in their separate owners.

For optional social distribution load `references/publication-boundaries.md`. Upstream Zernio CLI scripts, config cascade, media generation and idempotent post state are not bundled. Require an actual provider, per-channel content, exact effect authorization, dry-run where available, success URLs and reconciliation of uncertain writes. Without a provider, journal locally and do not claim publication.
