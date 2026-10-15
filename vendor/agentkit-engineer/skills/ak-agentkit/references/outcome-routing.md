# Engineer capabilities: decide by outcome, not the native CLI verb

AgentKit 2.19.0 offers command wrappers for some workflows. The **portable unit is the agent's judgment and operating method**, with real local/project tools used only where the chosen task needs an effect. The command surface is not part of the Engineer Skill contract.

## Recover the actual question

When a user says "run", "plan", "status", "journal", "doctor", "install", "recover" or supplies a native command example, distinguish:

1. **What must be understood or decided?** The relevant Skill may act entirely through analysis: plan a change, test the assumptions, diagnose failure, inspect dependencies, evaluate quality, record causal history.
2. **What must become true in the outside world?** Identify the authoritative repository, file, issue, provider or runtime. A Skill can guide a write, but it cannot prove one happened without tools and read-back.
3. **Who owns that state?** A project plan, current task frontier, journal, runtime worker, user account and native AgentKit installation are different objects. Do not create a parallel file/index/registry simply to mimic a native command.
4. **What would demonstrate the requested outcome?** Source evidence for claims, accepted design decisions for planning, tests for code, provider read-back for mutations and actual worker handles for delegation.

## Choose the smallest owning Skill

| Desired outcome | How the agent should approach it | Primary Skill |
|---|---|---|
| Understand what work is needed / build a credible roadmap | Inspect current reality and existing plans; reason about architecture, scope, dependencies, risk, verifiable phase outcomes; revise the plan as evidence changes | `ak-plan` |
| Track progress or decide the next phase | Compare planned and observed state, expose blockers and dependency effects; keep checked markers distinct from validated results; present a board only when it helps the decision | `ak-plan`, optionally `ak-plans-kanban` |
| Capture an important engineering event | Select historically meaningful facts, attempts, failed hypotheses, decisions and actual evidence; qualify uncertainty and store in the project's existing journal owner when needed | `ak-journal` |
| Execute, debug, test or review a change | Load the matching Skill, apply its reasoning method and use the real code/provider/test tools under granted authority; do not launch a CLI as a proxy for thinking | `ak-cook`, `ak-debug`, `ak-test`, `ak-code-review` |
| Coordinate several branches of work | Decide whether independence justifies parallelism, establish ownership/dependencies, capture and reconcile effects, verify integrated artifacts; use real workers only when supported | `ak-orchestrate`, ANGENT Continuity |
| Find available Skills/roles or develop a new Skill | Inspect actual installed inventory, determine domain/capability ownership, design discovery and behavioral examples before packaging | `ak-agentkit`, `ak-skill-creator` |
| Diagnose a project/tool environment | Identify observable failure, inspect actual project/config/runtime and test a hypothesis; do not confuse missing AgentKit telemetry with project health | `ak-debug`, `ak-scout`, `ak-test` |
| Manage AgentKit product itself | Resolve exact installed binary, kit/target/adapter, user/global scope, version, real effect and rollback; use native AgentKit only when needed and actually available | `ak-ak` |

Native commands for login, license, kit receipts, installed AgentKit binary, proprietary telemetry, process supervision and dashboards have no *Skill-only* equivalent as product services. Their **reasoning discipline** can be taught; effects require the corresponding product/provider.

## Example of the method

A user asks: "Use AgentKit to plan a feature and continue phase 2." The agent inspects accepted scope, repository reality and any existing plan; verifies whether phase 1 evidence satisfies phase 2 prerequisites; resolves assumptions and owner boundaries; then carries out phase 2 using Cook and actual tools if the user authorized implementation. It updates whichever source of work state the project already uses, and reports observed verification. The existence or absence of the `ak plan` binary is irrelevant to this engineering judgment.

Contrast: "Restore the previous installed AgentKit kit" asks to change an actual AgentKit installation. This requires a real provider, known backup and confirmed mutation scope; reasoning via `ak-ak` alone cannot restore it.

Do not turn these examples into a fixed mandatory chain. A single straightforward task may need one Skill and one tool; complex work may need a genuinely different analysis path.
