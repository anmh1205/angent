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

## AK CLI decoupling audit — 2026-10-15

Direct stable 2.19.0 help inspection established that `ak plan create` scaffolds plan.md and a phase file, `ak journal create` creates collision-safe Markdown, `ak run` dispatches a Skill to an adapter, and `ak orchestrate` provides distinct observation/process-control actions. The fallback now maps those intents through Skills rather than treating the `ak` binary as a prerequisite. `ak-journal` is reclassified as **VERIFIED_ADAPTED**, changing the ledger to **75 adapted, 24 degraded and 3 portable**.

The [CLI-to-Skill crosswalk](skills/ak-ak/references/cli-workflow-crosswalk.md) and [orchestration dispatch contracts](skills/ak-orchestrate/references/cli-free-dispatch.md) distinguish files-first workflows and actual host-tool dispatch from native-only signed-kit, authentication, license, proprietary telemetry, dashboard/server, durable process-supervisor or provider effects. This is a **workflow-source migration**; it does not demonstrate execution of every host file/provider operation on every harness. Runtime and cross-harness acceptance remain open.

## CLI-independent file and workflow execution — 2026-10-15

Reviewing native AgentKit 2.19.0 help established that `ak plan create/validate` are ordinary local plan file operations, `ak journal create` creates a collision-safe Markdown file, `ak run` resolves a Skill through an adapter, and `ak orchestrate` has distinct process-observation and effectful supervision modes. We corrected the earlier *binary-as-prerequisite* fallacy by adding an explicit [command-to-Skill crosswalk](skills/ak-ak/references/cli-workflow-crosswalk.md) and corresponding routing in Plan, Journal, Engineer Router, Help, Orchestrate, Plans Kanban and Team.

Unlike a documentation-only remap, the bounded local fallback now has `ak-plan/scripts/plan_files.py` (create/list/status/validate/add-phase of plan.md and phase files) and `ak-journal/scripts/journal_files.py` (collision-safe create/list/show/validate). Both use project-scoped standard files, independent of `ak`, avoid overwrites, and separate source-state markers from verified acceptance. CLI-administration-specific product behaviors and live process supervision still require a real provider.

The branch CI [run 38657510858](https://github.com/anmh1205/angent/actions/runs/38657510858), commit `d9c5c768b881b2a746a04e0f32374ddae11b5b3f`, **PASS**: structural inventory and selector, 8 structural fixture tests, 10 Repomix tests, 6 Watzup tests, 7 GKG AST tests, 6 Journal tests and 8 Plan tests, plus actual-checkout smoke checks. This establishes behavior of these local deterministic subsets under GitHub Ubuntu/Python 3.12. It does not establish multi-harness proprietary AgentKit control-plane parity, provider services, native dashboard, live teams or background job control.

## Remaining runtime acceptance

The 25 `VERIFIED_DEGRADED` skills are intentionally not considered fully equivalent. The most consequential missing surfaces include authenticated browser/profile operations and live team/AgentKit hooks; provider-bound image/video/audio and Stitch/HeyGen services; Graphify/GKG/Repomix indexing and query backends; SVG/Excalidraw/Preview/Remotion/Three.js rendering, searchable example/prompt corpora, and native viewer/dashboard/server utilities. See each identity's manifest row and skill-specific capability boundary.

A valid future operational acceptance run should select **the actual harness**, verify one source (native or fallback) is active, execute a representative happy path and failure/authorization case for the specific capability, inspect the real artifact/side effect and record observed versions and provider identities. Repeat only where stochastic reliability or cross-platform claims make repetitions necessary. For a degraded skill, either prove a complete host-native replacement or keep the degraded label. A successful Markdown/CI parse must never promote a runtime claim.

## Git isolation and release policy

All audit/port commits targeted only `engineer-semantic-parity-2.19.0` using an expected-head lease and fast-forward update; no merge, release, plugin publication or force push was requested or performed. The fallback plugin semantic version remains unchanged. The canonical `main` branch is separate; this audit does not change its installed ChatGPT plugin or release state.

The next valid work is **targeted runtime acceptance and remediation of degraded capabilities**, not another blanket identity-count ceremony.
