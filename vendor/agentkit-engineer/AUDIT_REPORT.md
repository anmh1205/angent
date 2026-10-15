# Engineer portable fallback — second-pass audit

Audit date: **2026-10-15**. Baseline: signed AgentKit Engineer **stable 2.19.0**. GitHub branch: **`engineer-semantic-parity-2.19.0`**. This report is a dated evidence snapshot; the living per-identity statuses remain in [PORTING_MANIFEST.md](PORTING_MANIFEST.md).

## Result and acceptance boundary

The fallback now contains the same **102 Skill identities** and **16 Agent role identities** as the pinned stable package. A first-pass workflow-semantic comparison is complete for all identities: 75 skills are adapted to the available host contract, 3 have portable semantics without material dependency substitution and 24 are explicitly degraded by absent native tooling, proprietary/provider services, dataset/scripts or rendering facilities. All 16 agent sidecars have been reviewed as role contracts, not certified as installed parallel agent runtimes.

**Accepted result:** coherent *source-level skill and role contracts*, native-first/fallback selection discipline, verified frontmatter/identity/reference packaging and branch CI. **Not accepted:** full end-to-end operational parity across unavailable browsers, external services, datasets, model backends or installed AgentKit runtimes. Nor does the evidence prove that all 102 workflows produce outputs of higher quality than upstream.

## What the audit actually exercised

The second pass read all 102 fallback `SKILL.md` entrypoints and 16 agent role files, checked the declared identities/statuses and validated local reference targets against the GitHub tree. Four inconsistent frontmatter modes were corrected (`ak-agent-browser`, `ak-chrome-profile`, `ak-journal` and `ak-copywriting`); five additional legacy multi-line frontmatter blocks lacked an explicit mode (`ak-code-review`, `ak-debug`, `ak-handoff`, `ak-scout`, `ak-test`). The former static README review count of 47/102 was removed to prevent subsequent drift.

A more consequential issue was the fallback selector's previous readiness decision: a correctly named plugin with 102 directories and 16 sidecar filenames could be declared ready despite broken skill metadata or references. `scripts/select_engineer.py` now requires an independent structural validator to pass. `scripts/verify_port.py` checks the manifest, names, metadata, counts, entrypoints, direct/local Markdown links and source isolation. Deliberately invalid fixtures exercise wrong names/modes, missing paths, link failures and reference traversal.

GitHub Actions evidence, under the **branch-only** workflow [Engineer fallback parity structure](https://github.com/anmh1205/angent/actions/workflows/engineer-fallback-validation.yml):

- [Run 38654179197](https://github.com/anmh1205/angent/actions/runs/38654179197): initial failure correctly detected the five missing mode declarations.
- [Run 38654290908](https://github.com/anmh1205/angent/actions/runs/38654290908): after repair, structural audit, fixture tests, selector smoke and diff hygiene all passed.
- [Run 38654531631](https://github.com/anmh1205/angent/actions/runs/38654531631): expanded secondary-link and traversal counterexamples also passed.

These runs establish observed GitHub CI behavior for those commits only. They are not substitutes for real model/UI/media/provider task execution.

## Functional and safety improvements

Compared with a blind portable export, ANGENT now has **one authoritative per-Skill capability ledger**, a fail-closed structural selector, explicit native-versus-fallback arbitration, branch-scoped regression checks and consistent evidence boundaries. The fallback also strengthens user-authority handling in multi-stage Vibe shipping, Xia feature port analysis versus actual implementation, Loop Git experiment isolation, external media/privacy processing and CTI investigation scope.

These are concrete *safety, portability and maintainability improvements to the fallback*. They do not establish a global comparative performance advantage over native AgentKit. Full capability claims require successful representative task execution on each claimed host and native provider.

## Executable local capability acceptance — follow-up audit

Three independent fallback utilities were implemented on the Engineer branch, without vendoring AgentKit code or requiring a network provider:

- **Repomix local subset:** `skills/ak-repomix/scripts/pack_local.py` packages selected local Git files into Markdown, JSON or XML; limits total/file bytes; avoids symlinks, obvious credentials and binary/control bytes; preserves skip/incomplete metadata; tracks dirty worktree and per-file SHA-256; refuses to overwrite existing outputs. Its security filter is heuristic, not equivalent to upstream Secretlint, and cannot prove absence of every credential.
- **Watzup local subset:** `skills/ak-watzup/scripts/scan_local.py` reads current branch/HEAD, dirty state, worktree list, local and cached remote refs and plan/roadmap checkboxes. It neither fetches remote refs nor mutates branches/worktrees; cached remote freshness and other worktree cleanliness remain unverified.
- **GKG Python subset:** `skills/ak-gkg/scripts/search_python_ast.py` parses Python AST without running repository code and returns exact definition/import/name/attribute candidate locations, together with skipped-file diagnostics. It is not a resolved call graph or multi-language indexed GKG server: aliases, dynamic dispatch, reflection, transitive reachability and other languages remain unsupported.

The test suite uses fresh temporary Git repositories, real commits/worktrees, symlink and sensitive-file counterexamples, dirty/detached scenarios, malformed XML input and escaped Markdown paths, as well as valid/invalid Python AST, import-binding, source scope and truncated-index cases. The branch-only CI also runs all three executables against its **actual checked-out source tree**, verifying snapshot correctness, Git status and AST definition discovery without mutating the working tree.

**Actual evidence:** [GitHub Actions run 38656278657](https://github.com/anmh1205/angent/actions/runs/38656278657) passed for commit `c3ab16d8517505b51b10881e266ed91a3ad713bb`, including 8 structural/selector tests, 10 Repomix tests, 6 Watzup tests, 7 Python AST/GKG tests and smoke executions on real checkout. Earlier red runs surfaced faulty test assertions and were repaired. This establishes successful execution of these bounded local subsets on GitHub Ubuntu/Python 3.12. It does **not** prove Windows/macOS behavior, native provider CLI and remote services, resolved graph semantics, graphics/media rendering or a general quality advantage over all 102 upstream Skills.

## AK CLI dependency and Skill-first correction — 2026-10-15

Direct inspection of AgentKit stable 2.19.0 established that `ak plan` provides scaffolding/status mechanics, `ak journal` handles journal files, `ak run` invokes runtime adapters and `ak orchestrate` includes real process-supervisor operations. The **transferable value** is not any of these commands: it is the agent's ability to design a plan, decide what history matters, select capabilities, coordinate dependencies and independently verify effects.

The initial conversion attempted command-by-command crosswalking and added standalone Plan/Journal file-management scripts. Those local utilities passed [historical CI run 38657510858](https://github.com/anmh1205/angent/actions/runs/38657510858), but that demonstrated file mechanics **rather than the user's intended Skill competence**. Both helpers and their tests were deliberately removed. `ak-agentkit` now teaches [outcome routing](skills/ak-agentkit/references/outcome-routing.md), with [plan stewardship](skills/ak-plan/references/plan-stewardship.md), [journal judgment](skills/ak-journal/references/journal-judgement.md) and [coordination judgment](skills/ak-orchestrate/references/coordination-judgement.md). `ak-ak` retains only the reasoning/safety boundary for **real AgentKit product administration**.

Original Repomix, Watzup and GKG local tools remain optional aids to deterministic observation, not Skill substitutes. No CLI simulator, new plan database, shadow runner, fake job ID or enforced per-task scripting convention is part of the fallback. This revision has structural CI evidence and source-level reasoning examples, **not** measured end-to-end model behavioral parity with upstream.

## Whole-entrypoint follow-up and remaining acceptance gaps — 2026-10-15

The follow-up inspected all 102 Engineer fallback Skill entrypoints for residual AgentKit-CLI-first instructions and mismatch with the user's **Skill-as-transferable-thinking** requirement. The prior Plan/Journal command-layer emulation is gone, while real product administration remains scoped to `ak-ak`. One specific inconsistency survived: `ak-project-management` told agents to prefer `ak plan --help` whenever a native CLI happened to be installed during sync-back. That is now corrected: select the project's actual plan/task owner and use its existing tools; native AgentKit is considered only when it owns that store.

**This is not full-quality certification.** The CI covers structure, available local deterministic helper tests and repository hygiene. It does not execute and comparatively evaluate model behavior for all 102 Skill workflows, 16 role lifecycles or real users' target environments. The ledger still identifies 24 genuinely degraded identities. Cross-harness side effects, browser/provider/editor outputs, and multi-agent coordination remain to be observed on real hosts. The original upstream support-asset gap is a research signal; exact file-path mismatches cannot establish knowledge equivalence or loss without comparing the corresponding decisions, examples and failure modes.

Operational acceptance requires representative user-goal cases for each **distinct capability family**, including a counter-case that should block, reroute or preserve prior state. Check the agent's decision and observable effects, not the presence of headings/links, a script command equivalent or a green structural workflow. Treat `VERIFIED_ADAPTED` as an inspected semantic contract, **not** evidence of exhaustive runtime competence.

## Remaining runtime acceptance

The 25 `VERIFIED_DEGRADED` skills are intentionally not considered fully equivalent. The most consequential missing surfaces include authenticated browser/profile operations and live team/AgentKit hooks; provider-bound image/video/audio and Stitch/HeyGen services; Graphify/GKG/Repomix indexing and query backends; SVG/Excalidraw/Preview/Remotion/Three.js rendering, searchable example/prompt corpora, and native viewer/dashboard/server utilities. See each identity's manifest row and skill-specific capability boundary.

A valid future operational acceptance run should select **the actual harness**, verify one source (native or fallback) is active, execute a representative happy path and failure/authorization case for the specific capability, inspect the real artifact/side effect and record observed versions and provider identities. Repeat only where stochastic reliability or cross-platform claims make repetitions necessary. For a degraded skill, either prove a complete host-native replacement or keep the degraded label. A successful Markdown/CI parse must never promote a runtime claim.

## Git isolation and release policy

All audit/port commits targeted only `engineer-semantic-parity-2.19.0` using an expected-head lease and fast-forward update; no merge, release, plugin publication or force push was requested or performed. The fallback plugin semantic version remains unchanged. The canonical `main` branch is separate; this audit does not change its installed ChatGPT plugin or release state.

The next valid work is **targeted runtime acceptance and remediation of degraded capabilities**, not another blanket identity-count ceremony.
