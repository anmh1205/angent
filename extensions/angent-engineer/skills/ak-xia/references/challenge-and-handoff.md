# Xia cross-repository challenge and handoff

## Original source and target mapping

Record source owner/repository, ref/commit when available, narrowed paths, entrypoints, dependencies, data/authorization and state owner. Compare to the destination repository's actual contracts. Every significant missing library, API, migration or integration belongs to a dependency map with EXISTS, NEW or CONFLICT status. Cross-stack similarity by filename is not proof of semantic equivalence.

## Challenge before implementing

Before turning analysis into a plan, explicitly evaluate:
1. Is the requested **outcome** genuinely required or is the mechanism optional?
2. Can a simpler destination-native path deliver the complete requested behavior?
3. Does the target already implement a meaningful subset?
4. Who maintains the port and its upstream compatibility?
5. Which dependencies/services/data/schema/permissions are introduced?

Add higher-impact questions for authentication, data corruption, concurrency, backward compatibility, runtime cost and licensing where relevant. For a real fork, show source approach, target approach, compromise, evidence, risk and provisional recommendation. Do not invent a numerical risk score or fixed question count when evidence is insufficient.

## Modes and approval

Compare returns just evidence/choice and stops. Copy/improve/port hand off an approved design to the actual Planner/Execution pipeline. A fast/auto flag from a skill runner is not authority to create commits, install packages, merge or expose private source; the user and host retain control over side effects.

## Handoff contract

Provide source manifest, behavior/state/control flow, destination owners, dependency matrix, risk/decision matrix, accepted assumptions, implementation phases with ownership, test oracle/acceptance and migration/rollback. If output artifacts are requested, save to authorized actual project paths and read back their contents. Do not invent `plans/<slug>/plan.md` or a specialist handoff if no plan file/team exists.
