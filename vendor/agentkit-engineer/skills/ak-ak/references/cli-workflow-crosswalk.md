# AgentKit 2.19.0 CLI functions → portable Engineer capabilities

This routing model is grounded in direct read-only native `ak --help`, `ak plan --help`, `ak plan create/validate --help`, `ak journal create --help`, `ak run --help`, `ak skill --help` and `ak orchestrate --help` inspection of the stable 2.19.0 installation. It maps **user outcomes**, not necessarily byte-compatible commands. Never require installing the AgentKit CLI to accomplish an outcome already supported by the host's Skills, files and provider tools.

## Route to Skills, not the AgentKit command-line surface

| Native CLI intent | Portable owner and actual mechanism | Semantic boundary |
|---|---|---|
| `ak run engineer/<skill>` | `ak-agentkit` selects and loads the matching `ak-*` Skill through installed Skill discovery or harness adapter; ANGENT Execution uses real tools | Preserve arguments/outcome, tool authority and timeout; no fake NDJSON or adapter process |
| `ak plan create/parse/validate/status/show/add-phase/update/phase/check/uncheck/resolve/list/search/use/reindex/kanban/close/archive/cleanup/migrate` | `ak-plan` for accepted plan meaning and file operations; `ak-plans-kanban` for read-only board; Context/Continuity own relevant active-work pointers | A plan file is source of truth; source edits only with authority; unchecked != blocked, checked != verified; no fabricated index/dashboard |
| `ak journal create/list/show/validate` | `ak-journal` creates/reads/validates collision-safe Markdown in an authorized project journal directory | Journal is history, not live Continuity state or automatically promoted Learning |
| `ak orchestrate prepare/start/advance/events/status/output/accept/resume/stop/probe/diagnose/plan-status` | `ak-orchestrate` for dependency/evidence model; ANGENT Continuity for resumable frontier/handles; host process/job API for **actual** start, status, logs or cancel | No process supervision, persistent worker, event stream or SIGTERM semantics without verified harness capability |
| `ak agents`, `ak commands`, `ak skills` catalog | Available Skill/role inventory and `ak-agentkit` routing; `ak-agentize` or `ak-skill-creator` for authored Skill/role definitions | A role file is not a spawned agent; runtime installation/enablement is a separate provider effect |
| `ak skill verify/install/repair/upgrade/remove` per-Skill Node/Python env | Target-Skill dependency check via installed tools; `ak-test` for actual environment smoke; project dependency manager for permitted install/update | Cannot assert a per-Skill venv exists; no silent installer/download or environment repair |
| `ak test`, `ak eval`, `ak audit`, `ak doctor`, `ak insights` | `ak-test`, `ak-code-review`, ANGENT Quality/Research and actual runtime probes. Use actual tests, trace and evidence. | Full proprietary analytics, provider telemetry, native signed-kit drift and shadow evaluators remain unavailable where no backend exists |
| `ak sessions`, `ak activity`, `ak analytics`, `ak data`, `ak content-search`, `ak usage` | ANGENT Context/Continuity, `ak-watzup`, `ak-scout`, `ak-gkg` and authenticated observability/usage tools where present | Host storage and sources only; absence of AgentKit's telemetry/index is a reported gap, not a zero reading |
| `ak kit`, `ak setup`, `ak init`, `ak new`, `ak onboard`, `ak projects`, `ak update`, `ak migrate`, `ak backups`, `ak recover`, `ak uninstall`, `ak self-update`, `ak versions` | For user intent **to start or maintain an ANGENT-enabled project**, use project-native files, `AGENTS.md`, package manager, Git and backups. For intent to administer AgentKit itself, use official native CLI | ANGENT cannot claim to modify AgentKit registry, binary, kit receipt/signature, backups or recovery state |
| `ak login/logout/whoami/licenses/secrets/policy/config/api/mcp/codex-agent-runtime` | Native product admin remains native; general equivalent outcomes use host account/config/secret manager or `ak-use-mcp` only with actual connected provider | No synthetic login/session/license/server status; never log/display secrets |
| `ak content`, `ak feedback`, `ak watch`, `ak gui`, `ak diagnostics` | `ak-copywriting`/`ak-journal` for content drafts, authorized publishing connector, `ak-retro` for feedback, host scheduling or viewer if truly available | Publishing, background watch, GUI services and support bundles are independent external effects requiring real capabilities |

Some commands have modes not reproduced by these adapters. A Skill preserving the *useful task* is not a binary-compatible substitute for the proprietary AgentKit **control plane**. Do not rename these gaps as successes.

## Dispatch and state principles

1. Identify the requested operation's outcome, effect scope and persistence requirements. If the user literally wants to configure or repair **AgentKit the product**, do not substitute ANGENT project state.
2. Prefer a directly installed/callable Skill, existing project-native files and actual provider APIs. Do not shell out to `ak` as an undocumented prerequisite to normal Engineer work.
3. Route only the workflow owner; for ordinary plans/journals use the existing repo plan/journal layout. No second database or blanket shadow CLI. Use ANGENT Continuity only for the in-progress frontier, not to replace historical journal/plan documents.
4. Preserve read-only versus mutation boundaries: discovery, validation and status are read-only; create/close/archive/reindex/checkout/publish/deploy/service start or stop can change actual state and require suitable authorization.
5. Verify created files, expected branch/provider state, material outputs and downstream acceptance; a pasted command, sample JSON or an agent's completion message is not executed evidence.
6. Degrade specifically by feature: if parallel workers, a dashboard or proprietary telemetry are unavailable, keep sequential/text alternatives truthful and avoid advertising equivalent backend capability.
7. Check for existing work and preserve unrelated files before creating new plan/journal/skill resources. Never emulate `--force`/global install by overwriting work.

## Minimal local scenario (no AgentKit)

A user asks to "create a plan, implement phase 1, run tests and write a journal." ANGENT routes Plan → Cook → Test → Journal. Plan writes an authorized ordinary Markdown plan with phase checkpoints, Cook executes the accepted phase under project instructions, Test runs real project checks, and Journal writes one chronological evidence entry. Continuity preserves the unfinished frontier. No `ak init`, `ak plan create`, `ak run`, `ak journal create` or AgentKit-managed store is required. If the environment has no writable file/provider capability, report that blockage rather than declaring the files created.
