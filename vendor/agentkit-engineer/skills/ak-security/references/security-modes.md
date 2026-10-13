# Security mode guidance

## Audit vs scan

Use `ak-security-scan` for broad automated triage.

Use `ak-security` when findings require threat-boundary reasoning, reachability analysis or remediation judgment.

## Adversarial discovery

Choose perspectives based on the system rather than always running a fixed list.

Useful questions:
- what can an unauthenticated actor influence?
- what does a valid low-privilege account gain?
- what happens if a dependency/build artifact is compromised?
- which internal/admin capability has dangerous ambient privilege?
- where can data cross tenant/trust boundaries?

Do not equate “think like an attacker” with permission to attack external systems.

## Fix mode

Group fixes by root cause when several findings are manifestations of one broken invariant.

After fixing:
- reproduce the old vulnerable path when safe;
- run targeted regression/security checks;
- verify neighboring trust boundaries were not weakened;
- rerun the relevant scan where useful.

## Severity

Use consequence + reachability/exploitability in the actual deployment.

Do not inflate severity because a vulnerability class has a famous name.
