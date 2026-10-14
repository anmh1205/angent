# Security mode guidance

## Comprehensive vs fast triage

Use `ak-security` as the current public workflow.

For narrow automated triage:
- `--secrets-only` checks secret/credential patterns only;
- `--deps-only` checks dependency/advisory evidence only;
- combining the fast selectors still does not establish code-pattern, STRIDE, OWASP, or red-team coverage.

Use the default comprehensive `ak-security` workflow when the task requires source patterns, trust-boundary reasoning, STRIDE/OWASP coverage, reachability analysis, or remediation judgment.

Do not invoke retired `ak-security-scan`.

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
- rerun the relevant scan/audit path where useful.

Fix mode does not authorize push, PR, merge, deploy, production requests, or offensive external testing.

## Severity

Use consequence + reachability/exploitability in the actual deployment.

Do not inflate severity because a vulnerability class has a famous name or because a scanner assigned a label.
