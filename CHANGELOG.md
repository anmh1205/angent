# Changelog

## 1.0.0 — Unreleased candidate

The 1.0.0 implementation is merged and validated on `main`, but it is **not released yet**.

### Cognitive architecture

- Established ANGENT as a cognitive layer with first-class Contract, Context, Reasoning, Research, Execution, Quality, Authoring, Format, Learning, Continuity, and Shell ownership.
- Deepened Reasoning with abstraction control, invariant preservation, decision sensitivity, specialist synthesis, and model-first replanning.
- Deepened Context with AGENTS.md project instructions, scoped memory, provenance, conflict handling, and progressive retrieval.
- Expanded Continuity from chat-loss checkpointing into proactive active-work frontier persistence and resume/reconciliation semantics.
- Expanded Learning from complaint-driven feedback into evidence-backed experience → mechanism → transfer/retirement.
- Expanded Authoring/Quality for chat, technical exposition, long-form consistency, Vietnamese technical writing, heading/section boundaries, coverage, endpoint evidence, and render fidelity.

### Skill architecture

- Added canonical repository `AGENTS.md`.
- Moved ANGENT toward owner-local `references/` and progressive disclosure.
- Added validation for owner-local reference architecture and project-instruction boundaries.

### Engineer fallback

- Adopted native-first / port-fallback semantics for AgentKit Engineer capability.
- Added `vendor/agentkit-engineer/` with explicit upstream provenance and license boundary.
- Completed the portable fallback surface for **102/102 Engineer Skills** and **16/16 Agent roles** without vendoring raw upstream source.
- Added PORTABLE / ADAPTED / DEGRADED semantics so runtime-specific upstream capabilities retain the best portable behavior instead of being dropped.
- Added native AgentKit guidance pointing to the official AgentKit installation and Engineer Kit documentation.
- Added validation to prevent native/fallback packaging regressions.
- Normalized all 102 fallback Skills to Agent Skills v1 frontmatter/name constraints: fallback names now match their `ak-*` directories, and AgentKit-only top-level metadata no longer sits in portable frontmatter.
- Packaged the fallback as its own Agent Plugins root and ChatGPT/Codex companion package while keeping one canonical 102-Skill tree.
- Added a read-only native/fallback selector contract: active-harness visibility selects native; absent/unproven native uses fallback.
- Added a cross-harness adapter contract without introducing a generic capability broker.

### Context and Continuity persistence

- Added revisioned local project/user memory storage with provenance and compare-and-swap conflict detection.
- Added immutable-revision local Continuity frontier persistence with stale-writer detection and resume from the highest coherent revision.
- Replaced the stale completed-release checkpoint with the active unreleased upgrade frontier.

### Validation

- Updated repository behavioral/structural validation for the new architecture.
- Added source-selection behavior checks and local memory/Continuity conflict/resume checks.
- The earlier superficial line/reference-count quality gate was removed; fallback quality is reviewed by capability semantics instead.

### Validated on merged candidate

- Live SERVER/local-harness validation passes package/reference architecture, owner boundaries, Reasoning, full Engineer inventory, native/fallback separation and local state-store behavior.
- The Engineer selector was exercised against native-usable, native-unusable and unknown states; AgentKit offline doctor was healthy on SERVER.
- Stale release-state claims were scanned and removed.
- Final branch integration review passed `git diff --check`, JSON manifest parsing, Skill/reference integrity, stale/runtime leakage scans, and Agent Skills conformance for all 114 Skills.

### Release boundary

The implementation and acceptance work for this candidate is complete:

- PR #1 was reviewed and merged into `main`;
- native/fallback selection was exercised on SERVER;
- the fallback companion was discovered, installed, and enabled by Codex CLI in an isolated environment;
- representative long-form Authoring/Quality acceptance passed;
- post-merge validation passed.

The remaining step is **not more implementation**. Publishing/tagging/updating the private ChatGPT plugin is a separate release action and requires explicit release approval from the exact merged source.
