# Plan lifecycle without AgentKit

The portable `ak-plan` Skill can implement plan creation, parsing, validation, phase changes and archive directly through **authorized project file tools**. It does not need `ak plan` installed. Confirm the actual plan owner, project root, existing files and accepted plan convention first; don't impose a second store when Jira/Notion or a project-native plan layout is authoritative.

## Durable plan layout when the project has no convention

Use `plans/<descriptive-id>/plan.md` as a readable overview. If independent phases materially help execution, create `phase-01-<slug>.md`, `phase-02-<slug>.md`, etc. AgentKit 2.19.0 `ak plan create` uses timestamped names, YAML `plan.md` and a phase-01 stub; reproducing the exact filename is optional unless an existing consumer requires the pinned convention. Never overwrite an existing plan.

The overview holds outcome, scope/exclusions, evidence/current state, critical decisions and assumptions, architecture, phase dependencies, constraints, acceptance criteria, risks and unresolved authority. Each phase contains result, prerequisites, owned files/interfaces, actionable work, validation proof and a distinct state: pending/active/blocked/verified. Mark an item verified **only after** the actual acceptance evidence exists.

## Operations and read-back

| Intent | Skill behavior, without CLI |
|---|---|
| create / add-phase | Inspect active work, choose unique plan/phase path, write coherent Markdown through host file or connector action, reopen written files |
| parse / show / list / search / status / resolve | Inspect source files, enumerate only readable scoped plans, resolve current project by authoritative root and active task; report excluded/unreadable paths |
| validate | Check title, objective, phase presence/number uniqueness, dependency acyclicity, scope/acceptance and versioned evidence; no mutation |
| update / check / uncheck / phase | Locate a specific phase/item and authority; edit exactly the selected state; do not replace a source with an unrelated generated checklist |
| use / reindex / kanban | Store active-plan pointer in existing project state when actually writable, rebuild **derived views** from plan files, route board view to Plans Kanban; never invent a running dashboard |
| close / archive / cleanup / migrate | Confirm closure evidence and source destination; preserve history and references, prefer non-destructive archival. Cleanup/deletion, migration and index rewrites require concrete scope/authority |

ANGENT Continuity may point to the active plan but does **not** replace the plan artifact. A checked box is a user's recorded status; it is not independently tested proof. When the active project uses another plan system, use that system's actual tools rather than duplicating or silently migrating it.

## Scenario test for a reviewing agent

Given a partially checked plan and two overlapping workstreams, `status` must report the checkbox count **separately** from verification evidence and must not merge/overwrite either plan. Given an updated dependency, verify downstream phase assumptions before claiming plan validation passed. For `archive`, confirm explicit allowed target and path/read-back; `parse` must never create or mutate any file.

## Tested deterministic local subset

`../scripts/plan_files.py` provides optional `create`/`list`/`status`/`validate`/`add-phase` for a project whose approved plans owner is `plans/`. It refuses unsafe plan identifiers, escaping symlinks, duplicate phase numbers and overwrites; `list`, `status` and `validate` are read-only. The output distinguishes checkbox state from accepted/verified work. This is **file lifecycle**, not AgentKit global plan registry, archive/index/HTML dashboard or full structural-semantic plan validation; use the Skill plus available project tools for those outcomes.
