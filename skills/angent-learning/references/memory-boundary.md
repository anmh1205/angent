# Learning versus memory, project instruction, and task state

These stores may share infrastructure but represent different semantics.

## AGENTS.md

Stable project instruction: architecture map, repository conventions, known-good commands, durable hard constraints.

## User/project memory

Durable context: user preference, recurring project fact, accepted durable project decision, contextual knowledge useful across sessions.

## Continuity

Active task frontier: work in progress, verified completed units, unfinished unit, blockers, pending effects, next safe action.

## Learning

Reusable causal mechanism: why a behavior tends to produce an outcome, applicability boundary, evidence/transfer support, reopen/retire conditions.

## Boundaries

Do not:
- promote task status into memory;
- promote project-specific convention into global user memory;
- promote an untested complaint directly into Learning;
- put dynamic memory into AGENTS.md merely because it appeared repeatedly.

Context retrieves from these classes according to the current task. Durable does not mean globally relevant.


## Persistence classes

When the local ANGENT store is used, promoted mechanisms live in `learning-user` or `learning-project` scope. Ordinary user/project memory uses its own scopes.

A mechanism may be active, reopened or retired without changing user/project memory state.

Do not persist secrets or unrelated sensitive data as Learning evidence; keep only the minimum provenance needed to reconstruct why the mechanism was promoted or reopened.
