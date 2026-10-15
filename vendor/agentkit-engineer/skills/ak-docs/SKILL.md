---
name: ak-docs
description: Initialize, update, summarize or audit project docs and root agent context from current evidence without imposing a universal file layout.
metadata: {port: angent-fallback, mode: adapted}
---

# Documentation Management — Portable Fallback

Code, tests, schemas and observed runtime state are the **evidence owners** of current implementation facts. Project documentation must still explain the relevant **what, how and why** in a way a reader can understand and use: system mechanisms, user workflows, data/control flow and consequences. It should not become a second mutable implementation authority or a disconnected index of source files. Root AGENTS.md is **agent behavior instruction**, not a project overview.

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
4. Apply `references/docs-audit.md`: remove stale competing declarations and copied mutable inventories, but preserve the explanatory mechanisms a reader needs. A verified code example or causal trace can teach behavior without claiming to replace the code's authority.
5. Edit only impacted authority surfaces. Do not invent ADRs, file trees, governance machinery or docs-only gates merely for completeness.
6. Verify links, paths, configuration keys, commands and current claims against actual owners; inspect whether the resulting prose **explains the requested behavior coherently** rather than devolving into isolated lists. Preserve uncertainty when source evidence is incomplete and report validated changes.

Use host-native documentation delegation only if actually available; otherwise do the same work directly. Never claim an upstream named agent ran when it did not. Do not implement product code in a docs-only operation.
