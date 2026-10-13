# AGENTS.md — ANGENT repository instructions

ANGENT is a cognitive layer for agents. The 1.0.0 line is an active candidate under development; do not treat a package, preview, branch, or private integration as a public release unless release state is explicitly changed.

## Canonical project instructions

This file is the canonical project instruction surface for this repository. Nested AGENTS.md files may refine instructions for their subtree.

Harness-specific instruction files, when needed for compatibility, must project from AGENTS.md rather than become independent sources that can drift.

Newest explicit user instruction and live repository state outrank historical notes.

## Architecture ownership

- Contract owns outcome, scope, authority, constraints, and success semantics.
- Context owns the smallest relevant working state.
- Reasoning owns the problem/system model, uncertainty, decisions, and adaptive plan.
- Research acquires evidence that can change a decision.
- Execution performs authorized effects and returns observations.
- Continuity owns active-work persistence and ambiguous-effect recovery.
- Learning turns meaningful experience into reusable causal mechanisms.
- Authoring owns reader-facing explanation and language realization.
- Quality independently checks solution integrity before communication integrity.
- Format owns destination/render fidelity.
- Root routes and must not become a second implementation of every owner.

Specialist agents and vendored Engineer skills do not take strategic ownership away from ANGENT Reasoning.

## AGENTS.md, memory, Continuity, and Learning are different

AGENTS.md stores stable project instructions: architecture maps, conventions, known-good commands, and durable repository constraints.

Memory stores scoped dynamic knowledge that should survive sessions but does not belong in project instructions.

Continuity stores the frontier of active work so interrupted tasks can resume safely.

Learning stores promoted reusable mechanisms after evidence supports transfer.

Do not turn AGENTS.md into a transcript, task journal, or append-only memory file.

## Skill architecture

Use progressive disclosure:

- SKILL.md contains the operating model, owner boundary, workflow, and important decision points.
- references/ contains deeper owner-specific guidance loaded when needed.
- scripts/ contains deterministic helpers only.
- assets/ or templates contain non-instruction support content.

Prefer owner-local references. Root references should remain only for genuinely cross-cutting contracts.

Do not lengthen skills merely to appear comprehensive. Add instruction when it improves a real decision or failure mode.

## Engineer integration

Engineering capability follows a native-first / port-fallback policy.

1. If AgentKit Engineer is installed and usable in the current environment, prefer native upstream skills/agents.
2. If native Engineer is absent or unusable, expose the canonical fallback port under vendor/agentkit-engineer/.
3. Do not expose native and fallback Engineer libraries simultaneously by default.
4. Maintain one canonical fallback fork, not separate Claude/Codex/Cursor reasoning forks.
5. Preserve workflow behavior before branding or mass renaming.
6. If a runtime dependency cannot be ported, document the capability it provided and implement the smallest replacement that preserves the workflow outcome.

## Context and continuity

Recognize active work early for long or non-trivial tasks. Maintain a durable frontier at meaningful work boundaries rather than waiting for a predicted disconnect.

External systems such as GitHub, Jira, Notion, or deployment providers are used to reconcile facts about the world. They do not replace ANGENT's task frontier.

Local memory should follow capture → synthesis/update → scoped retrieval rather than append-only notes. Keep user/global memory, project memory, active task state, and promoted learning distinct.

## Execution and verification

A commit, generated file, issue transition, command success, or report is intermediate evidence unless the Contract defines it as the requested endpoint.

After consequential external effects, reconcile authoritative state before declaring success or retrying an uncertain write.

When an observation invalidates a plan assumption, return to Reasoning before continuing dependent steps.

## Change discipline

Prefer coherent commits over many tiny commits.

For architecture changes:
1. inspect current source and relevant references;
2. preserve useful behavior unless intentionally replacing it;
3. migrate callers/references before deleting compatibility files;
4. read back changed files from GitHub;
5. compare the branch with its base;
6. run available validation/tests before claiming a phase complete.

Do not publish/release 1.0.0 while it remains a candidate.
