# Test results — evidence-based reporting

Choose report depth from the requested test outcome. A concise result for one module does not require a full QA dossier; a release or multi-environment audit may. Use the project's established report destination and naming convention **only when they exist and a persisted report is actually required**. Do not infer one from absent AgentKit hooks.

## Report structure, when material

- **Acceptance claim and inspected scope:** behavior/requirement, baseline, changed area, relevant test layer(s), project/runtime identity and known environment limits.
- **Execution evidence:** commands or provider operations that actually ran, exit/result, individual outcomes including failed and skipped cases, duration when measured, logs/artifact paths that actually exist. No invented metrics.
- **Coverage:** measured values and critical missing behavior, with a **threshold only if supplied by current project policy or an accepted task-specific gate**. The number of executed tests is not automatically the number that meaningfully exercise the claim.
- **Failure interpretation:** observed error and reproduction first; a suspected cause is labeled a hypothesis until established by evidence. Do not report a fix when the operation was review-only.
- **UI and end-to-end:** exact tested URL/environment, flows, viewports, auth/test-data boundary, screenshots, console, accessibility and skipped states *when actually observed*.
- **Decision:** PASS only for the checked claim whose required gates passed; FAIL for observed failed requirements; BLOCKED/UNVERIFIED where required evidence or provider capability was unavailable. List the smallest next discriminating check when it matters.

For suite **create**, include which requirement-to-failure paths gained tests and how protection was demonstrated; for **audit**, record concrete ineffective tests and the evidence that they could pass incorrectly; for **optimize**, include baseline and resulting measurements plus the protected check groups and fallback when selection confidence is low.

Never pre-fill an 80%/70% coverage gate, a test count, clean console, screenshot path, build success, performance result or "all dependencies resolved". If the user did not supply a report file path, a supported chat response can be the complete deliverable.

## Illustrative compact result (not a completed run)

```text
Scope: expired session → API rejects refresh (fixture/environment identified)
Observed: focused session tests passed; real browser flow not run
Coverage: measured only if coverage tooling was actually executed
Verdict: local test behavior checked; deployed auth behavior NOT VERIFIED
Next proof if required: exercise real client ↔ deployed auth endpoint
```
