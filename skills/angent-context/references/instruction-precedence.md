# Instruction precedence

Different context sources answer different questions. Do not flatten them into one recency-sorted list.

## Current explicit instruction

Newest explicit user instruction controls the current task within higher-level safety/system constraints, but it does not automatically erase older still-active obligations. Contract classifies whether it adds, refines, supersedes, scopes or conflicts with prior instruction state.

It also outranks inferred or historical collaboration patterns when the user changes how the task should proceed.

## Task frontier

Continuity explains what work is active, completed, pending, or ambiguous.

It may preserve a collaboration-state pointer/subset for resume, but neither the frontier nor that pointer grants permission beyond the current instruction.

## Collaboration state

Collaboration state explains the task-relevant way of working: interaction mode, initiative expectation, evidence/verification bar, explanation job, checkpoint/reporting expectation and applicable working-method mechanisms.

It is assembled from current instruction first, then still-applicable task decisions and Learning. It is not a permanent personality profile and is separate from effect authority.

## AGENTS.md

AGENTS.md supplies stable project-specific instruction within its scope.

Nested AGENTS.md may refine a subtree while applicable root instructions remain in force.

## Canonical source/provider state

Git, Jira, Notion, deployment providers, and other systems establish facts about their own current state.

They do not know ANGENT's intended next frontier or interaction mode unless explicitly used as a task store.

## Memory

Memory supplies scoped prior context.

It is advisory when inferred, stronger when user-confirmed, and subordinate to current explicit instruction. A memory item does not automatically select the current collaboration mode.

## Learning

Promoted Learning mechanisms guide how a decision or working method tends to succeed under stated conditions.

They are not facts about the current project and do not apply when their boundary does not match.

## Conflict examples

- Current user says “do not deploy”; old frontier says deploy next → do not deploy.
- Current user says “audit only”; an earlier autonomous mode says continue through fixes → stay audit-only.
- AGENTS.md says one production image; specialist plan introduces a second → reconsider the plan.
- Project memory says branch X; live Git says branch Y → update project state.
- Inferred preference says concise; user asks comprehensive → current instruction wins.

Preserve unresolved conflict when comparable-authority sources disagree and current evidence cannot resolve it.
