---
name: ak-security-scan
description: Run a bounded read-only source security scan for secrets, vulnerable dependencies, common code patterns and repository exposure, then validate and report findings without modifying code.
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Security Scan — Portable Fallback

This is a distinct packaged stable 2.19.0 workflow. Do not collapse it into `ak-security`.

Use it for fast/bounded repository triage. Use `ak-security` when the task requires broader threat-model reasoning, adversarial discovery, or authorized fix-and-reverify work.

## Load progressively

- `references/scan-patterns.md` — secret/code-pattern triage categories and false-positive handling.
- current project-native dependency/advisory scanner when available.

## Modes

- default/full source scan — secrets → dependencies → code patterns → repository exposure checks;
- `--secrets-only` — secret/credential path only;
- `--deps-only` — dependency/advisory path only;
- explicit path/scope — restrict every scan category to that authorized repository boundary.

Do not silently turn this read-only scan into red-team activity or automatic remediation.

## Workflow

1. Resolve the authorized repository/path scope and project languages/package manifests.
2. Run secret detection first when included.
3. Run the project-appropriate dependency/advisory audit when included and available.
4. Search relevant high-risk code/config patterns when included.
5. Check accidental environment/credential-file tracking or equivalent repository exposure.
6. Read surrounding code/config before promoting a pattern match to a finding.
7. Classify findings by evidence and consequence; preserve unverified/false-positive status.
8. Return a concise report with locations, redacted evidence, severity rationale and suggested fix/verification.

## Evidence discipline

A regex/pattern match is triage evidence, not proof of exploitability.

Dependency-audit failure, unavailable registry access or an incomplete manifest/lockfile set means the dependency verdict is incomplete.

Never print a discovered live secret. Redact as an opaque secret marker; location/provider class is enough for remediation.

## Effects

The default workflow is read-only.

Do not modify files, rotate credentials, install remediation packages, commit, push or invoke external targets automatically.

A confirmed issue needing remediation can be routed to `ak-security --fix` or `ak-fix` under separate authority.

## Boundary

This Skill covers repository secret/dependency/common-pattern triage.

It does not claim penetration testing, runtime exploit validation, infrastructure/compliance audit, or comprehensive threat-model coverage.
