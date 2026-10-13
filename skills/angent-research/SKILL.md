---
name: angent-research
description: Acquire and structure evidence that reduces decision-relevant uncertainty, with source roles, version boundaries, conflicts and provenance explicit.
---

# ANGENT Research — Epistemic Evidence Engine

Research answers evidence questions; it does not replace reasoning with source collection.

Read `evidence-model.md`.

## Input

Prefer a question from Reasoning:
- blocked claim/decision;
- plausible alternatives;
- discriminating observation;
- required precision/version/platform boundary.

For a simple factual task, Root may route directly to Research without a separate Reasoning pass.

## Evidence targeting

Seek the smallest evidence set that materially changes confidence, eliminates an alternative or establishes the required fact. Prefer information gain over source count.

Classify sources by role rather than generic prestige: normative, primary implementation, vendor specification, observed runtime evidence, independent analysis, community experience or illustrative only.

## Conflicts

Do not average disagreement. Check version, platform/configuration, normative-vs-implementation role, staleness, scope and observation quality.

## Output to Reasoning

Return an **evidence delta**:
- established/updated facts;
- source roles and version boundaries;
- hypotheses supported/weakened/rejected;
- unresolved conflict/uncertainty;
- any new question exposed by the evidence.

Keep source fact, interpretation, example and verified observation distinct.
