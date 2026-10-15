---
name: ak-project-management
description: Reconcile durable multi-phase plans with optional live task tracking, verify completion, update all affected phases and coordinate meaningful docs/status changes.
metadata: {port: angent-fallback, mode: adapted}
---

# Project Management — Portable Fallback

Use when plans, issues, phases or teams need reliable status, dependency and resumption information. Stable Engineer 2.19.0 separates durable plan files from ephemeral runtime task tracking, supplies **hydration and whole-plan sync-back**, and coordinates actual documentation changes only when triggered by a meaningful contract change.

Read **references/plan-task-reconciliation.md** and **references/progress-and-docs.md**. This is not a requirement to create a project manager agent or duplicate plans on every task.

## Authorities

The active implementation plan (and its phases) owns durable work intent and completion criteria; authoritative provider tasks own their live statuses/assignments; Git/tests/artifacts own observed implementation evidence. ANGENT Continuity supplies the active, interruption-safe frontier, **not** a second permanent copy of every plan item. Reconcile disagreements and mark uncertain mappings rather than accepting the newest prose status at face value.

## Operations

### Status and resume

Locate the actual active plan according to project instructions; inspect its full phase set, dependencies, checked/unchecked work, current branch, known blockers, acceptance gates and any live task view. Do not assume an upstream `./plans` directory if the consuming repo has a different owner.

### Hydration and work tracking

Discover a live task system at runtime; never infer it from a client name or historical tool list. If available, map unfinished phase items to unique operational tasks with source location, owner and dependencies. Reuse existing mappings; do not create duplicates. Without it, work from the durable plan and keep progress there.

### Verified completion and sync-back

Verify observed code/artifact/test/review results against the **specific task acceptance contract**. When syncing back, scan every phase file under the target plan, reconcile completed provider items to their exact source entries, repair stale earlier checkboxes, and update aggregate plan status only from verified phase state. Report unmapped completed items and blockers; do not claim a fully completed plan with unresolved mappings. Update the **actual owning plan or task surface** using the available authorized file, document or provider tools, then read it back. Treat AgentKit's `ak plan` as an optional product-specific adapter **only if the project's authoritative plan store is really managed by AgentKit**; its binary being installed does not make it the default path. No CLI or shadow plan store is required for status reasoning.

### Docs and communication

Determine whether new behavior, API/schema, architecture, security, command or operator knowledge changes demand documentation; ordinary checkbox or internal refactor does **not** automatically trigger a documentation rewrite. Route the changed contract to the actual doc owner and verify its final claims. Generate concise status reports only at a real requested checkpoint or useful milestone. No automatic issue updates or externally delivered reports unless authorized.

## Outputs

Return evidence-backed completed/in-progress/blocked counts, provenance, scope changes, risks and dependency implications; first valid next unit with owner/gate; live/durable mismatch; provider/write action results and limitations. Avoid percentage claims when no verified denominator is available.

## Boundaries

Project Management coordinates state, not strategic product decisions. Do not override user approval, merge policy, branch restrictions or artifact ownership to satisfy a plan checkbox.
