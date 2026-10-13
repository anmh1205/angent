---
name: ak-predict
description: Pre-mortem a proposed change from several expert perspectives to surface architectural, security, performance, operational and UX risks before implementation.
metadata: {port: angent-fallback, mode: adapted}
---

# Predict — Portable Fallback

Use before a major or risky change when independent perspectives can reveal failure modes cheaply.

## Perspectives

Select only relevant lenses, for example:
- architecture/integration;
- security/privacy;
- performance/reliability;
- operations/migration;
- UX/product.

These may be delegated to separate Agents when the harness supports it, or evaluated sequentially.

## Workflow

1. Preserve the actual proposal and constraints.
2. For each relevant lens, state plausible failure mechanism and triggering condition.
3. Distinguish evidence-backed risk from speculation.
4. Identify mitigations or pre-implementation probes.
5. Rank by consequence and plausibility.

Do not create exactly five personas as a ritual.

Return risks to Reasoning/Plan; Predict does not veto by role authority.
