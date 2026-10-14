# Learning versus memory, collaboration, project instruction, and task state

These stores may share infrastructure but represent different semantics.

## AGENTS.md

Stable project instruction: architecture map, repository conventions, known-good commands, durable hard constraints.

## User/project memory

Durable context: stable user context, recurring project fact, accepted durable project decision, contextual knowledge useful across sessions.

## Collaboration state

Task-relevant way ANGENT should work with the user now: interaction mode, initiative expectation, evidence/verification bar, explanation job, progress/checkpoint expectation and applicable working-method mechanisms.

Collaboration state is assembled by Context. It is not a permanent user profile and does not grant authority.

## Continuity

Active task frontier: work in progress, verified completed units, unfinished unit, blockers, pending effects, next safe action, plus a collaboration-state pointer/subset only when losing it would change resume behavior.

## Learning

Reusable causal mechanism: why a behavior tends to produce an outcome, applicability boundary, evidence/transfer support, reopen/retire conditions.

Working-method mechanisms are a valid Learning class when they are causal and conditional. They may inform collaboration state for a matching task without becoming blanket preferences.

## Boundaries

Do not:
- promote task status into memory;
- promote project-specific convention into global user memory;
- promote task-scoped collaboration mode into a permanent profile;
- infer effect authority from autonomy/initiative expectation;
- promote an untested complaint directly into Learning;
- put dynamic memory into AGENTS.md merely because it appeared repeatedly.

Context retrieves from these classes according to the current task. Durable does not mean globally relevant.

## Persistence classes

When the local ANGENT store is used, promoted mechanisms live in learning-user or learning-project scope. Ordinary user/project memory uses its own scopes.

Task-scoped collaboration state belongs with current task/context state; Continuity may persist a compact pointer/subset only when resume correctness depends on it.

A mechanism may be active, reopened or retired without changing user/project memory state.

Do not persist secrets or unrelated sensitive data as Learning evidence; keep only the minimum provenance needed to reconstruct why the mechanism was promoted or reopened.
