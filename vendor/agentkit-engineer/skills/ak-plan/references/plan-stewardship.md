# Stewardship of a technical implementation plan

A plan is an **explanation of how an accepted outcome can be reached and demonstrated**. Its format is secondary. A board, checklist, database index or `plan.md` is useful only if it preserves enough of the accepted reasoning to support the next decision.

## Building or revising a plan

Read the authoritative requirements, accepted direction, relevant project source/tests and overlapping unfinished work. Establish the desired post-change behavior, constraints and current system behavior before decomposing tasks. If an architectural choice remains open and changes the work graph, resolve or expose that decision first rather than recording one arbitrary assumption as fact.

Shape phases by deliverable and dependency. For each phase, explain the capability/state being established, its prerequisite, the part of the system it owns or affects, the failure modes that could invalidate it, and what observation would prove its acceptance. In migrations, separate preparation, compatibility coexistence, cutover and recovery where the domain requires them; a chronological list of files is not a plan.

A good plan lets the next agent answer **why this phase is ordered here**, which contracts it must preserve and what would cause replanning. Recheck dependent phases after changing a shared schema, source version or system assumption.

## Inspecting progress

Do not infer real completion from unchecked/checked task lists alone. Compare phase claims with tests, commits, deployments, issue/provider state or other authoritative evidence appropriate to the task. Distinguish `not started`, `in progress`, `waiting on an external dependency`, `blocked by a decision`, `reported complete` and `verified` when the distinction changes the next action.

When work overlaps existing plans, determine whether the dependency runs forward, backward or both ways. Reconcile competing plans rather than making one hidden source the new authority. When the user asks for "next", select the first feasible phase **from the validated dependencies**, not merely the next numerical phase.

## Updating or closing a plan

Use the project's existing file, document or task provider and its actual edit affordances; do not create a new plan store or run a scaffolding script merely because upstream has `ak plan create`. Inspect before altering source, respect the scope/approval boundary, edit the smallest coherent affected set, then read back the resulting artifacts. Avoid overwrite, deletion or archival on a status inquiry.

Close/archive only when the governing workflow's acceptance and remaining obligations are reconciled. Preserve the reasoning and implementation evidence for a successor. An archived plan's past decision is historical context, not automatic authority for a new requirement.

## Calibration cases

- **Fast task:** a two-file low-risk fix may need an inline implementation sequence and test, not a new phase directory.
- **Cross-service contract change:** planning must model consumer versions, rollout/rollback and live verification rather than splitting by module filenames.
- **Stale plan:** if a phase checkbox says done but the integration test fails, report conflict and reopen verification; do not claim verified completion.
- **Blocked upstream task:** if phase B needs a provider migration not yet accepted, mark the dependency and continue independent runnable work rather than guessing provider success.
