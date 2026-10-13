---
name: ak-scenario
description: Generate risk-focused behavioral and test scenarios across relevant dimensions until additional cases add little coverage value.
metadata: {port: angent-fallback, mode: portable}
---

# Scenario — Portable Fallback

Use before implementation, QA planning or regression design when edge-case coverage matters.

## Candidate dimensions

Select only relevant dimensions:
- happy path;
- empty/null/missing input;
- numeric/size boundaries;
- invalid/untrusted input;
- state transitions/order;
- concurrency/races;
- timeout/retry/partial failure;
- permissions/tenant/privacy;
- migration/backward compatibility;
- locale/time/timezone/encoding;
- responsive/UI states;
- recovery/restart/cancellation.

## Saturation

Add scenarios until new cases stop introducing a new mechanism, boundary or acceptance risk.

Do not force exactly twelve dimensions or produce a huge combinatorial matrix with no prioritization.

## Output

For each important scenario provide trigger, expected behavior and why it matters.
