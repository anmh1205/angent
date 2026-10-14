---
name: ak-docs
description: Initialize, update, summarize or audit project docs and root agent context from current evidence without imposing a universal file layout.
metadata: {port: angent-fallback, mode: adapted}
---

# Documentation Management — Portable Fallback

Code, tests and schemas own current WHAT/HOW. Project docs preserve non-derivable WHY/WHERE: rationale, business constraints, terminology, decisions and navigation. Root AGENTS.md is **behavioral process memory**, not a project overview.

## Select operation

- `init`: inspect the existing docs route and create only needed ownership surfaces. Read `references/docs-modes.md`.
- `update`: reconcile changed contracts with impacted documents only. Read `references/docs-modes.md`.
- `summarize`: provide a sourced answer without creating a file unless explicitly asked or an existing file owns it.
- `agent-context`: author/audit root AGENTS.md via keep/cut/migrate tests. Read `references/agent-context.md`.
- If the operation is unclear and changes the deliverable, resolve it; never assume init.

## Opening, authority and evidence gates

1. Recover accepted scope, audience, decision purpose and validation bar. Do not restart already settled brainstorming.
2. Inspect root instructions, README, existing docs navigation and the relevant code, tests, configs, scripts and generated owner before choosing paths.
3. Separate evergreen rationale from time-bound audits, plans or release records.
4. Apply `references/docs-audit.md`: remove implementation paraphrases, stale duplicates, copied mutable inventories and counts; link executable owners.
5. Edit only impacted authority surfaces. Do not invent ADRs, file trees, governance machinery or docs-only gates merely for completeness.
6. Verify links, paths, configuration keys, commands and current claims against actual owners; report validated changes and uncertainties.

Use host-native documentation delegation only if actually available; otherwise do the same work directly. Never claim an upstream named agent ran when it did not. Do not implement product code in a docs-only operation.
