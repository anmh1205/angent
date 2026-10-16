# ANGENT

ANGENT is a portable cognitive layer for AI agents. It helps an agent understand user intent, reason from evidence, execute authorized actions, verify outcomes, carry unfinished work forward, and improve from reusable lessons. The repository combines Core cognitive skills with portable Engineer capabilities in one plugin distribution.

## Explore and use ANGENT

**Start with the source:** [Root skill](skills/angent/SKILL.md) explains how ANGENT selects its capabilities, while [AGENTS.md](AGENTS.md) describes repository-level working instructions and [ARCHITECTURE.md](ARCHITECTURE.md) provides the architecture. [CHANGELOG.md](CHANGELOG.md) records the evolution of the project.

**Package the unified plugin:** with Python 3 available in a checkout of this repository, run:

```sh
python3 scripts/package_unified.py --output dist/angent-chatgpt.zip
```

This produces a distribution archive from the source. Integration and installation depend on the agent host and plugin support; a Git clone by itself is not an installed ChatGPT plugin. See the installation and package-identity notes below before distributing a build.

## ANGENT Root gateway for ChatGPT

The OpenAI plugin exposes one discoverable Skill: `angent`. Other Core methods and Engineer/Frontend extensions live in its internal reference catalogue and are chosen by ANGENT, preventing independent discovery of bundled `ak-*` as peers. The platform can still select another separately installed plugin, and installation does not imply ANGENT will run automatically on every message.

`extensions/angent-frontend/` adds visual frontend art direction informed by [ClaudeKit's frontend demo](https://github.com/claudekit/frontend-design-pro-demo): coherent style selection, composition, typography, imagery and rendered verification. Product-level UI/UX diagnosis remains with the existing Engineer capability.

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

Version 1.4.0 established whole-answer argumentation, coherent chat responses and decision-oriented research/audit/status reports without another agent or mandatory writing pipeline. Authoring composes a supported explanation; Quality checks whether claims, evidence, impacts and recommended actions actually align; Format preserves meaning in Notion, Docs and other destinations.

Behavioral case definitions and the reviewed-output comparator are under `evals/authoring/` and `scripts/evaluate_authoring.py`. Tests can validate schemas and comparator mechanics but cannot replace running actual baseline/candidate model outputs with human or evidence-backed review. The release identity and provider activation must also be verified separately.

For current provider activation, use `scripts/verify_activation.py` with a complete live observation; see `docs/release-activation.md`. Source CI, an archive build and a provider-installed release are distinct proof levels.

## Installation and package identity

Version 1.5.x adds separate install-ready platform bundles without duplicating ANGENT's maintained Skills or introducing another canonical plugin identity. `platforms/` holds runtime adapters and `packages/` is generated. See the supported targets and safe installation instructions in [docs/platform-installation.md](docs/platform-installation.md).


The two supported plugin manifests are plugin.json and .codex-plugin/plugin.json. Their package identity and prompt must be consistent. Version strings are package metadata, not a task checkpoint or a substitute for checking the actual source/runtime.

This repository does not store private plugin release identifiers, past branch HEADs or live next-action pointers as project instructions. Check the running plugin or Git branch directly when that identity matters.

## Decision-to-outcome capability boundaries

ANGENT sharpens diagnostic discrimination, reversible evidence selection, requested-endpoint verification and the transfer of conceptual understanding across long documents. These remain responsibilities of Reasoning, Execution, Authoring, Research, Quality and Learning, not a separate routing or evaluation service.

Core fixtures are calibration prompts and counter-cases, not automatically executed behavioral proof. Package version belongs to the manifests; installed ChatGPT plugin releases must be verified from the actual provider. Pull-request validation packages candidate source as a CI artifact without merging or installing it.

## Validation

The repository checks deterministic structure and manifest consistency, and exercises Memory/Continuity filesystem races, process-exit lock release, revision conflicts and interrupted pointer recovery on CI. For cognitive method changes, use evidence-backed behavioral cases and counter-cases appropriate to the actual consequence. Green structural and runtime CI checks cannot establish that a model's reasoning, writing or cross-session Learning activation improved.

ANGENT continues to ship **one OpenAI plugin identity**, not one plugin per platform. The compatibility builder `python3 scripts/package_unified.py --output dist/angent-chatgpt.zip` remains available. ANGENT exposes **12 Core and 102 discoverable Engineer Skills**. All 103 Engineer source identities are preserved under `extensions/angent-engineer/`; the overlapping `ak-explain` is no longer a separately discoverable Skill. Reasoning and Authoring own ordinary explanations.

For the multi-platform release run:

```bash
python3 scripts/build_packages.py --all
python3 -m unittest discover -s tests -p 'test_multi_packages.py' -v
```

This creates copy-ready `packages/local-agent/`, `packages/gemini-web/`, `packages/gemini-skills/`, `packages/gemini-extension/`, `packages/claude-code/` and `packages/openai-plugin/`, alongside deterministic ZIPs in `dist/`. Both output directories are generated and Git-ignored. Download the matching [GitHub Release](https://github.com/anmh1205/angent/releases) ZIPs when no build environment is available. Each release provides individual target ZIPs and one `angent-all-targets.zip` containing all seven distributions, plus checksums. Personal ChatGPT plugin updates require a separate upload. Tagged releases use the guarded publication workflow and include SHA256 checksums; ordinary CI artifacts are short-lived candidates.

**Gemini Web:** upload `angent-gemini-web.zip` to Gemini Apps → Customize → Skills → Upload. It has one top-level `SKILL.md` and references for all 114 discoverable Core/Engineer skill texts; unlike Gemini CLI it does not import 115 independently callable Skills. See the Gemini Apps installation section for limitations.

Core Skills remain canonical under `skills/`; the maintained Engineer fallback remains under `extensions/angent-engineer/`. `platforms/` owns only native bootstrap/manifest projections. Do **not** edit generated packages or maintain separate copies of core reasoning per host. See [Installation and platform differences](docs/platform-installation.md).

When native AgentKit Engineer is usable, route the task to native; otherwise use the portable `ak-*` Skills. No package claims it can automatically hide its bundled fallback Skills when a native catalog is installed. The source tree and generated packages are not evidence that a particular runtime has activated ANGENT.
