---
name: ak-sumup
description: Provide a requested post-implementation handoff recap grounded in actual artifacts, test evidence, delivery status and unresolved risks.
metadata: {port: angent-fallback, mode: portable}
---

# Sum Up — Portable Fallback

Use for a requested delivery/handoff recap after implementation, especially when fresh artifact, test and release evidence matters. General conversational summaries remain owned by ANGENT Authoring.

## Evidence

Use the strongest available sources:
- current diff/artifact;
- observed test/build/runtime results;
- accepted decisions;
- issue/plan state when relevant;
- conversation evidence only where fresher direct evidence is unavailable.

Do not call source changes deployed, shipped, or running unless current provider/runtime evidence establishes that state.

## Workflow

1. Establish the implementation period or feature being summarized.
2. Separate implemented + verified work from proposed, inferred, untested, unshipped, or unresolved work.
3. Preserve material failures, recovery attempts, and their outcomes.
4. Include only decisions/trade-offs that explain the resulting behavior.
5. Explain the main flow or usage when it helps the next reader.
6. Put unresolved items and next steps last.

Use a compact table/diagram only when it lowers reconstruction cost.

## Boundary

This Skill summarizes evidence; it does not implement, mutate files, or fabricate current status.

Use `ak-bro` to simplify only the immediately previous answer, `ak-sowat` for a product-priority judgment, and `ak-watzup` when fresh live status is the actual question.
