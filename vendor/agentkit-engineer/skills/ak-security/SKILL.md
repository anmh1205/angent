---
name: ak-security
description: Run a bounded defensive secrets/dependency/code-pattern audit with STRIDE/OWASP analysis, optional red-team discovery, and explicitly authorized fix-and-reverify work.
metadata: {port: angent-fallback, mode: adapted}
---

# Security — Portable Fallback

Use only within authorized defensive scope.

This is source-led defensive analysis; it is not authorization for penetration testing, credential use, production requests, exploitation, exfiltration, or destructive testing.

## Select depth and mutation separately

- **default/comprehensive** — secrets + dependency + code-pattern review plus STRIDE/OWASP threat modeling;
- **secrets-only** — credential/secret scan only;
- **deps-only** — dependency/advisory audit only;
- **red-team** — add bounded attacker-perspective discovery to the selected comprehensive path;
- **iterations N** — cap an explicitly iterative red-team/fix mode when the user sets the bound;
- **fix** — apply targeted validated remediations and rerun a guard; local commit creation is allowed only when current authority explicitly includes it;
- **red-team + fix** — broad discovery followed by authorized remediation of confirmed high-impact findings.

Fast scan modes do not silently claim the omitted threat-model/code-pattern coverage.

## Audit workflow

1. Resolve the smallest authorized scope and relevant trust boundaries.
2. Read selected source/config/manifests/CI/deployment files and project instructions.
3. Map authn/authz, secrets/data flows, external dependencies, integrity/availability boundaries, and attacker-relevant entry points.
4. Run available secret/dependency scanners only when their network/cache/tool effects are acceptable.
5. Inspect relevant code-pattern and STRIDE/OWASP classes for comprehensive mode.
6. In red-team mode, use materially distinct attacker perspectives to discover/validate source-reachable findings; do not perform live offensive exploitation.
7. Deduplicate findings by mechanism/root cause.
8. Establish severity from reachability, impact, evidence, and confidence—not scanner labels alone.

## Evidence discipline

A scanner match is not automatically a vulnerability.

For each material finding preserve:
- affected boundary/location;
- trigger/reachability;
- attack scenario;
- impact;
- supporting evidence;
- confidence/severity rationale;
- bounded remediation;
- verification method.

Redact entire live secrets. Do not emit trailing characters/lengths that aid reconstruction; retain only a harmless public prefix when it materially aids triage.

## Fix and reverify

Only when edits are authorized:

1. start from validated findings;
2. route each change to the correct code/config owner;
3. preserve compatibility/behavior requirements;
4. run a trusted guard for each accepted repair;
5. commit successful iterations only when local commit authority was explicit;
6. stop on a failing guard rather than weakening it;
7. rerun the original finding/scanner path;
8. report residual risk and deferred findings.

Fix mode never grants push/PR/merge/release/deploy authority.

## Completion

Report files/scope inspected, available/unavailable scanner evidence, findings by severity, coverage limitations, red-team iteration evidence when used, and fix/guard/commit evidence when authorized.

Partial persona/scanner coverage is reported as partial, never as a full clean audit.
