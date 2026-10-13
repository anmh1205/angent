---
name: ak-security
description: Perform an authorized defensive security audit, adversarial discovery pass, or fix-and-reverify cycle using threat models, trust boundaries and reachable evidence.
metadata: {port: angent-fallback, mode: adapted}
---

# Security — Portable Fallback

Use only within authorized defensive scope.

Read:
- `references/security-audit.md`;
- `references/security-modes.md`.

## Modes

### Audit

Default.

1. Define assets, trust boundaries and attacker-relevant entry points.
2. Map authentication, authorization, data/secret flows and external dependencies.
3. Inspect relevant vulnerability classes.
4. Validate findings against reachable code/config/runtime evidence.
5. Rank by impact and exploitability in the actual system.
6. Recommend containment/fix and verification.

### Adversarial discovery

Use when the user explicitly wants deeper defensive red-team-style discovery on an authorized codebase/system.

Examine the same system from several materially different attacker positions, for example:
- unauthenticated/external;
- authenticated low-privilege;
- supply-chain/dependency;
- internal/operator/configuration.

These are analytical lenses, not autonomous offensive personas.

Correlate duplicate findings by root cause.

### Fix and reverify

Only when fixes are authorized.

1. start from validated findings;
2. route each fix to the correct code/config owner;
3. preserve behavior and compatibility requirements;
4. run targeted security regression verification;
5. rescan/retest the original finding;
6. report residual risk and anything intentionally deferred.

## Evidence discipline

Scanner output or a suspicious pattern is not automatically a vulnerability.

For each material finding establish:
- affected boundary;
- trigger/reachability;
- impact;
- evidence;
- severity rationale;
- remediation;
- verification.

## Safety

Do not provide invasive exploitation instructions against third-party targets.

Do not expose secrets collected during an audit.

Do not let a “fix” weaken security checks merely to silence a scanner.
