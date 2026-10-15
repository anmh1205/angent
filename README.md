# ANGENT

ANGENT is a cognitive layer that helps an agent understand the requested outcome, reason from evidence, act with permission, verify results, preserve unfinished work and learn from recurring successes or failures.

## How it works

ANGENT has one small Root router and focused supporting skills. **Skills are responsibilities, not a prescribed workflow or a mandatory collection of agent instances.** Ordinary questions stay direct. Larger tasks activate only what is necessary:

- Contract and Context: objective, active constraints, authority and relevant state.
- Reasoning and Research: decisions, uncertainty, dependencies and evidence when needed.
- Execution: provider/tool actions and observed effects.
- Authoring and Format: coherent explanations and accurate destination representation.
- Quality: verification for consequential work, accepted revisions and broad changes.
- Continuity and Learning: resumable unfinished work and reusable conditional lessons.

Root does not ask every skill to produce a handoff document. A consequential mutation or long-running task carries only the identity, evidence, constraints and dependency information needed for safe action or recovery.

The complete routing entry is in skills/angent/SKILL.md. Owner-specific details live alongside the relevant skill. Repository-level rules are in AGENTS.md.

## Operating principles

- Current authority and canonical provider facts outrank remembered plans or saved checkpoint text.
- Research supplies evidence and domain relationships, not automatic authority.
- A pending operation does not monopolize the work loop when independent useful work remains.
- Corrections preserve accepted properties and address the generating failure, not only an example sentence.
- Documents and chat should share coherent technical explanation quality; authoring is not a checklist generator.
- Only verified outcomes satisfy the requested endpoint. Samples and structural checks do not establish full behavioral acceptance.
- Persist active-work state in harness/local ignored storage, never in committed project files.

## Cross-domain analysis

For ambiguous or consequential work, ANGENT can distinguish the underlying need from a proposed solution, examine current and desired states, conflicting stakeholder value, nontechnical alternatives and change impacts. It maintains only material links among obligations, decisions, artifacts and supporting evidence; no universal BRD, PRD or workflow is required. A narrow question still receives a direct answer, and an explicitly required method remains binding. See `skills/angent-reasoning/references/needs-and-change-analysis.md` for the conditional analysis method and `skills/angent/references/core-fixtures.md` for representative behavioral counter-cases.

## Installation and package identity

The two supported plugin manifests are plugin.json and .codex-plugin/plugin.json. Their package identity and prompt must be consistent. Version strings are package metadata, not a task checkpoint or a substitute for checking the actual source/runtime.

This repository does not store private plugin release identifiers, past branch HEADs or live next-action pointers as project instructions. Check the running plugin or Git branch directly when that identity matters.

## Validation

The repository checks deterministic structure and manifest consistency, and exercises Memory/Continuity filesystem races, process-exit lock release, revision conflicts and interrupted pointer recovery on CI. For cognitive method changes, use evidence-backed behavioral cases and counter-cases appropriate to the actual consequence. Green structural and runtime CI checks cannot establish that a model's reasoning, writing or cross-session Learning activation improved.

ANGENT 1.3.0 is built as **one installable plugin**. Run `python3 scripts/package_unified.py --output dist/angent-unified.zip`; this deterministic artifact combines 12 Core and 103 Engineer Skills in one discoverable `skills/` root. The Engineer source and 16 role contracts remain under `extensions/angent-engineer/` for maintainability. The archive includes its support material but contains **no second installable Engineer manifest**. Tests check the exact catalog, runtime selector, stable bytes and missing/colliding skill failures. A raw source checkout is not the unified distribution artifact.

When native AgentKit Engineer is usable, route the task to native; otherwise use the bundled portable `ak-*` Skills. Agent Plugins v1 cannot conditionally hide these Skills if another native catalog is visible, so do not claim automatic catalog exclusivity. Do not install the former `angent-engineer-fallback` package alongside ANGENT.
