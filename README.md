# ANGENT

ANGENT is a cognitive layer that helps an agent understand the requested outcome, reason from evidence, act with permission, verify results, preserve unfinished work and learn from recurring successes or failures.

## How it works

ANGENT has one small Root router and focused supporting skills. **Every request receives the complete cognitive standard; only effort and supporting capabilities adapt.** Skills are responsibilities, not a prescribed workflow or mandatory agent instances. Short questions may have short, direct answers after the same intent, context, evidence, reasoning and accuracy checks; extra capabilities activate only where useful:

- Contract and Context: objective, active constraints, authority and relevant state.
- Reasoning and Research: decisions, uncertainty, dependencies and evidence when needed.
- Execution: provider/tool actions and observed effects.
- Authoring and Format: coherent explanations and accurate destination representation.
- Quality: silent fit/accuracy checking always; explicit evidence-bound evaluation for consequential work, accepted revisions and broad changes.
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

For ambiguous or consequential work, ANGENT can distinguish the underlying need from a proposed solution, examine current and desired states, conflicting stakeholder value, nontechnical alternatives and change impacts. It maintains only material links among obligations, decisions, artifacts and supporting evidence; no universal BRD, PRD or workflow is required. A narrow question may receive a direct answer without reducing cognitive fidelity, and an explicitly required method remains binding. See `skills/angent-reasoning/references/needs-and-change-analysis.md` for the conditional analysis method and `skills/angent/references/core-fixtures.md` for representative behavioral counter-cases.

## Authoring and reporting evidence

Version 1.4.0 deepens whole-answer argumentation, coherent chat responses and decision-oriented research/audit/status reports without another agent or mandatory writing pipeline. Authoring composes a supported explanation; Quality checks whether claims, evidence, impacts and recommended actions actually align; Format preserves meaning in Notion, Docs and other destinations.

Behavioral case definitions and the reviewed-output comparator are under `evals/authoring/` and `scripts/evaluate_authoring.py`. Tests can validate schemas and comparator mechanics but cannot replace running actual baseline/candidate model outputs with human or evidence-backed review. The release identity and provider activation must also be verified separately.

For current provider activation, use `scripts/verify_activation.py` with a complete live observation; see `docs/release-activation.md`. Source CI, an archive build and a provider-installed release are distinct proof levels.

## Installation and package identity

The two supported plugin manifests are plugin.json and .codex-plugin/plugin.json. Their package identity and prompt must be consistent. Version strings are package metadata, not a task checkpoint or a substitute for checking the actual source/runtime.

This repository does not store private plugin release identifiers, past branch HEADs or live next-action pointers as project instructions. Check the running plugin or Git branch directly when that identity matters.

## Decision-to-outcome capability boundaries

ANGENT sharpens diagnostic discrimination, reversible evidence selection, requested-endpoint verification and the transfer of conceptual understanding across long documents. These remain responsibilities of Reasoning, Execution, Authoring, Research, Quality and Learning, not a separate routing or evaluation service.

Core fixtures are calibration prompts and counter-cases, not automatically executed behavioral proof. Package version belongs to the manifests; installed ChatGPT plugin releases must be verified from the actual provider. Pull-request validation packages candidate source as a CI artifact without merging or installing it.

## Validation

The repository checks deterministic structure and manifest consistency, and exercises Memory/Continuity filesystem races, process-exit lock release, revision conflicts and interrupted pointer recovery on CI. For cognitive method changes, use evidence-backed behavioral cases and counter-cases appropriate to the actual consequence. Green structural and runtime CI checks cannot establish that a model's reasoning, writing or cross-session Learning activation improved.

ANGENT 1.3.0 is built as **one installable plugin**. Run `python3 scripts/package_unified.py --output dist/angent-chatgpt.zip`; this deterministic artifact combines 12 Core and 103 Engineer Skills in one discoverable `skills/` root. The Engineer source and 16 role contracts remain under `extensions/angent-engineer/` for maintainability. The archive includes its support material but contains **no second installable Engineer manifest**. Tests check the exact catalog, runtime selector, stable bytes and missing/colliding skill failures. A raw source checkout is not the unified distribution artifact.

When native AgentKit Engineer is usable, route the task to native; otherwise use the bundled portable `ak-*` Skills. Agent Plugins v1 cannot conditionally hide these Skills if another native catalog is visible, so do not claim automatic catalog exclusivity. Do not install the former `angent-engineer-fallback` package alongside ANGENT.
