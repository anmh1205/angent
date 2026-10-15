# Defensive security audit

Consider, when applicable:
- authentication/session weaknesses;
- authorization/IDOR/tenant isolation;
- injection;
- XSS/CSRF;
- SSRF;
- unsafe deserialization/file handling;
- secret exposure;
- cryptographic misuse;
- supply-chain/dependency risk;
- insecure defaults/configuration;
- logging/privacy leakage;
- race/replay/idempotency weaknesses.

For each finding record:
- affected boundary;
- trigger;
- impact;
- evidence;
- severity rationale;
- remediation;
- verification.

Keep threat modeling tied to the real deployment and data flow.
