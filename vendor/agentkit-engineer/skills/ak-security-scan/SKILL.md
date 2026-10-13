---
name: ak-security-scan
description: Run a bounded defensive scan for secrets, vulnerable dependencies and common code/config security patterns, then validate findings before reporting.
metadata: {port: angent-fallback, mode: adapted}
---

# Security Scan — Portable Fallback

Use project/native scanners when available.

Possible classes:
- secret scanning;
- dependency/advisory scanning;
- SAST/lint security rules;
- IaC/container configuration checks;
- custom repository search for known risky patterns.

## Workflow

1. Define authorized scope.
2. Detect installed/project-standard scanners.
3. Run non-destructive checks.
4. Deduplicate and validate high-impact findings.
5. Separate confirmed, likely, false-positive and unverified results.
6. Route confirmed issues to Security/Fix.

A scan is triage evidence, not a complete security audit.
