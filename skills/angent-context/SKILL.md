---
name: angent-context
description: Reconstruct the smallest relevant working state from current instruction, active task frontier, project instructions, scoped memory and authoritative sources.
---

# ANGENT Context — Working-State Reconstruction

Context is not a history dump and not a memory database. Cross-harness state access follows the Root `harness-contract.md`; Context semantics do not change per client.

It assembles the smallest high-signal working set the current owner needs.

## Load references progressively

- references/context-assembly.md — build the working set and manage provenance.
- references/memory-loop.md — capture, synthesize, retrieve and persist scoped durable memory.
- references/instruction-precedence.md — resolve current instruction, AGENTS.md, task state, and memory conflicts.

## Four state classes

- **current interaction** — newest explicit user instruction and current conversation facts;
- **task state** — active-work frontier, decisions, unresolved dependencies, artifacts from Continuity;
- **project state** — AGENTS.md, architecture, conventions, project knowledge;
- **user/learning memory** — scoped dynamic knowledge that materially affects the present decision.

Do not preload all four layers wholesale.

## AGENTS.md is project instruction, not memory

AGENTS.md is the canonical project instruction surface for local/project work.

Memory should not duplicate AGENTS.md. Task progress should not be appended to AGENTS.md.

## Assemble by relevance

Start from current instruction and task frontier.

Retrieve only knowledge that can change scope, interpretation, decision, execution constraints, or communication requirements.

If a reference is not needed for the current decision, leave it out until needed.

## Provenance and freshness

For material context preserve source/scope, whether it is explicit/inferred/source-grounded, freshness/version when relevant, and unresolved conflict.

Do not choose between conflicting records by timestamp alone.

## Memory behavior

Capture memory candidates during normal work without interrupting the task, then synthesize/update them at meaningful boundaries.

Memory is organized by topic + scope + provenance, not append-only chronology.

A candidate may create, merge, update/supersede, remain contested, or be rejected as task-local noise.

## History

Raw session history, journals, and archived chats are evidence sources that may be searched when compact memory is insufficient.

They are not automatically authoritative and should not be loaded into every turn.

## Resume

On resume:
1. recover active frontier from Continuity;
2. apply newest explicit instruction;
3. load relevant AGENTS.md scope and memory;
4. reconcile external state that may have changed;
5. return a compact working state to Reasoning.

External Git/Jira/Notion/provider state validates outside-world facts. It does not replace ANGENT's active-work state.

Context does not mutate external systems, own strategy, or infer authorization from historical momentum.
