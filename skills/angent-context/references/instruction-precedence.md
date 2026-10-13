# Instruction precedence

Different context sources answer different questions. Do not flatten them into one recency-sorted list.

## Current explicit instruction

Newest explicit user instruction controls the current task within higher-level safety/system constraints.

## Task frontier

Continuity explains what work is active, completed, pending, or ambiguous.

It does not grant permission beyond the current instruction.

## AGENTS.md

AGENTS.md supplies stable project-specific instruction within its scope.

Nested AGENTS.md may refine a subtree while applicable root instructions remain in force.

## Canonical source/provider state

Git, Jira, Notion, deployment providers, and other systems establish facts about their own current state.

They do not know ANGENT's intended next frontier unless explicitly used as a task store.

## Memory

Memory supplies scoped prior context and preference.

It is advisory when inferred, stronger when user-confirmed, and subordinate to current explicit instruction.

## Learning

Promoted Learning mechanisms guide how a decision should be made.

They are not facts about the current project.

## Conflict examples

- Current user says “do not deploy”; old frontier says deploy next → do not deploy.
- AGENTS.md says one production image; specialist plan introduces a second → reconsider the plan.
- Project memory says branch X; live Git says branch Y → update project state.
- Inferred preference says concise; user asks comprehensive → current instruction wins.

Preserve unresolved conflict when comparable-authority sources disagree and current evidence cannot resolve it.
