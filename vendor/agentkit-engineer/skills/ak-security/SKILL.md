---
name: ak-security
description: Run a bounded defensive security workflow covering secrets, dependencies, source patterns, STRIDE/OWASP threat reasoning, optional red-team discovery and authorized fix-and-reverify work.
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Security — Portable Fallback

Use only within authorized defensive scope.

Read:
- `references/security-audit.md`;
- `references/security-modes.md`.

## Mode contract

Preserve these stable 2.19.0 workflow distinctions:

- default scoped audit — secrets + dependencies + relevant code/config patterns + STRIDE/OWASP reasoning;
- `--secrets-only` — secret/credential triage only;
- `--deps-only` — dependency/advisory triage only;
- both fast flags — still a fast scan; do not silently add code-pattern/STRIDE/red-team work;
- `--red-team` — add bounded attacker-perspective discovery;
- `--iterations N` — user-selected cap for iterative red-team/fix work; do not invent a universal default cap;
- `--fix` — apply only validated targeted fixes with an explicit guard after each bounded iteration;
- `--red-team --fix` — discover broadly, then fix only the confirmed findings within the authorized severity/scope boundary.

The fallback preserves these semantics even when the exact upstream helper scripts, report files, hooks or commit automation are unavailable.

## Scope and preparation

Resolve:
- exact file/directory/project scope;
- source/manifests/lockfiles/CI/deployment evidence needed;
- whether network-backed advisory tools may run;
- whether local edits and local commits are allowed;
- trusted verification commands;
- files/behavior that must not change.

Do not let `full` or a broad glob silently expand into unrelated secret stores or external systems.

## Audit

1. Resolve and inventory the authorized source scope.
2. Map assets, trust boundaries, auth/authz, sensitive data/secret flows and external dependencies.
3. Run the selected secret/dependency/code-pattern checks.
4. Apply STRIDE/OWASP reasoning unless a fast flag intentionally skips it.
5. Validate findings against reachable code/config/runtime evidence.
6. Deduplicate by root cause and rank by consequence + actual reachability/exploitability.
7. Return redacted evidence, bounded remediation and verification.

Scanner output or a suspicious pattern is not automatically a vulnerability.

## Red-team discovery

When explicitly requested, use materially different defensive perspectives such as external/unauthenticated, low-privilege/authenticated, supply-chain, and internal/infrastructure.

These are analytical lenses, not permission to attack third-party systems.

Preserve partial coverage when an iteration cap or missing evidence prevents completion.

## Fix and reverify

Only when fixes are authorized.

1. Start from validated findings.
2. Change the smallest responsible code/config boundary.
3. Run the agreed guard after each bounded fix iteration.
4. Stop when the guard fails; do not weaken verification to continue.
5. Reproduce/rescan the original finding when safe.
6. Report residual risk, unresolved findings and any intentionally deferred issue.

If the harness/project supports commits and the user authorized them, a local commit may record a successful fix iteration. This does not authorize push, PR, merge, release or deployment.

## Secrets and external services

Never emit raw secrets. Redact secret evidence as an opaque marker; do not preserve suffixes, lengths or credential fragments merely for display.

Dependency auditors may contact advisory registries and update caches. Their network access, freshness and failures are evidence boundaries.

Static/source analysis does not authorize production requests, credential use, exploit execution, data exfiltration or destructive testing.
