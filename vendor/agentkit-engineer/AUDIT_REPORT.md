# Engineer portable fallback — second-pass audit

Audit date: **2026-10-15**. Baseline: signed AgentKit Engineer **stable 2.19.0**. GitHub branch: **`engineer-semantic-parity-2.19.0`**. This report is a dated evidence snapshot; the living per-identity statuses remain in [PORTING_MANIFEST.md](PORTING_MANIFEST.md).

## Result and acceptance boundary

The fallback now contains the same **102 Skill identities** and **16 Agent role identities** as the pinned stable package. A first-pass workflow-semantic comparison is complete for all identities: 74 skills are adapted to the available host contract, 3 have portable semantics without material dependency substitution and 25 are explicitly degraded by absent native tooling, proprietary/provider services, dataset/scripts or rendering facilities. All 16 agent sidecars have been reviewed as role contracts, not certified as installed parallel agent runtimes.

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

Two independent fallback utilities were implemented on the Engineer branch, without vendoring AgentKit code or requiring a network provider:

- **Repomix local subset:** `skills/ak-repomix/scripts/pack_local.py` packages selected local Git files into Markdown, JSON or XML; limits total/file bytes; avoids symlinks, obvious credentials and binary/control bytes; preserves skip/incomplete metadata; tracks dirty worktree and per-file SHA-256; refuses to overwrite existing outputs. Its security filter is heuristic, not equivalent to upstream Secretlint, and cannot prove absence of every credential.
- **Watzup local subset:** `skills/ak-watzup/scripts/scan_local.py` reads current branch/HEAD, dirty state, worktree list, local and cached remote refs and plan/roadmap checkboxes. It neither fetches remote refs nor mutates branches/worktrees; cached remote freshness and other worktree cleanliness remain unverified.

The test suite uses fresh temporary Git repositories, real commits/worktrees, symlink and sensitive-file counterexamples, dirty/detached scenarios, malformed XML input and escaped Markdown paths. The branch-only CI also runs both executables on its **actual checked-out source tree**, verifying that snapshots and current Git status agree and no working-tree mutation results.

**Actual evidence:** [GitHub Actions run 38655909604](https://github.com/anmh1205/angent/actions/runs/38655909604) passed for commit `2d35dafe90b4f63ce1618b1bacf15779c1b5aa98` after repairs to faulty test assertions exposed by CI. This proves successful source-level execution in the GitHub Ubuntu/Python 3.12 runner for the bounded subsets. It is not evidence of Windows/macOS behavior, remote Repomix exports, native Watzup scoring, authenticated provider operations, graphics/media rendering or comparative improvement on all 102 Skills.

## Remaining runtime acceptance

The 25 `VERIFIED_DEGRADED` skills are intentionally not considered fully equivalent. The most consequential missing surfaces include authenticated browser/profile operations and live team/AgentKit hooks; provider-bound image/video/audio and Stitch/HeyGen services; Graphify/GKG/Repomix indexing and query backends; SVG/Excalidraw/Preview/Remotion/Three.js rendering, searchable example/prompt corpora, and native viewer/dashboard/server utilities. See each identity's manifest row and skill-specific capability boundary.

A valid future operational acceptance run should select **the actual harness**, verify one source (native or fallback) is active, execute a representative happy path and failure/authorization case for the specific capability, inspect the real artifact/side effect and record observed versions and provider identities. Repeat only where stochastic reliability or cross-platform claims make repetitions necessary. For a degraded skill, either prove a complete host-native replacement or keep the degraded label. A successful Markdown/CI parse must never promote a runtime claim.

## Git isolation and release policy

All audit/port commits targeted only `engineer-semantic-parity-2.19.0` using an expected-head lease and fast-forward update; no merge, release, plugin publication or force push was requested or performed. The fallback plugin semantic version remains unchanged. The canonical `main` branch is separate; this audit does not change its installed ChatGPT plugin or release state.

The next valid work is **targeted runtime acceptance and remediation of degraded capabilities**, not another blanket identity-count ceremony.
