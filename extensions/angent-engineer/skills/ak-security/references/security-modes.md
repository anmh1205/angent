# Security mode guidance

## Fast modes

### --secrets-only
Scan for credentials/secrets within the authorized source boundary.

Do not add dependency audit, code-pattern, STRIDE or red-team work.

Redact matches as opaque secret markers. File/location and public issuer prefix may be enough for triage; never expose a live value.

### --deps-only
Run the stack-appropriate dependency/advisory audit when the tool/network boundary is available.

Do not claim the dependency tree is clean when the auditor is missing, its registry is unreachable, or the lock/manifest scope was incomplete.

### Fast-flag precedence
If either fast flag is present, run only the selected fast evidence path(s). Fast flags win over red-team/comprehensive behavior when combined.

Do not silently expand a fast request into code-pattern review, STRIDE, OWASP or attacker-persona work.

## Default comprehensive audit

Use source/config evidence plus:
- secret and dependency evidence;
- relevant code-pattern review;
- STRIDE;
- OWASP categories;
- reachability/impact reasoning.

## Red-team mode

Choose materially different attacker positions based on the system. The stable workflow commonly uses external, supply-chain, insider/internal and infrastructure perspectives.

`--iterations N` is a user-selected bound. If the run stops before all intended perspectives/paths are examined, report partial coverage rather than a full audit.

Do not equate “think like an attacker” with permission to attack external systems.

## Fix mode

Group fixes by root cause when several findings share one broken invariant.

After each bounded change:
- run the agreed test/lint/security guard;
- stop visibly if the guard fails;
- reproduce/rescan the original path when safe;
- verify neighboring trust boundaries were not weakened.

Local commit creation is a separate bounded effect and never implies push/PR/merge/deploy authority.

## Severity

Use consequence + reachability/exploitability in the actual deployment.

Do not inflate severity because a vulnerability class has a famous name.
