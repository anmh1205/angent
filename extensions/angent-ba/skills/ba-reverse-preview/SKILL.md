---
name: ba-reverse-preview
description: Specialized ANGENT business analysis reverse-preview method.
---

# Reverse-engineering preview with source confidence

## Purpose

Present reconstructed requirements without laundering hypotheses into facts. Every material assertion from legacy documents or code must carry an evidence class and version: SOURCE-OBSERVED, INFERRED, UNCONFIRMED, CONTRADICTORY, or APPROVED-DECISION (only with real approval).

## Reader model

For each claim, show (1) reconstructed behavior in plain language, (2) the supporting file/page or code symbol and revision, (3) confidence rationale, (4) conflicting witnesses, (5) impact if wrong, and (6) next validation action. Do not replace this with a single document-level percentage.

## Method

1. Confirm the exact historical system/release/repository and scope; distinguish source snapshots from deployed runtime.
2. Consume source ledger from reverse-doc or code-to-srs. Reject requirements without a traceable source path, except clearly labeled proposals from stakeholders.
3. Group content into actors/roles, features/FR, policy/BR, NFR, error behavior, state machine, data entities, open questions and disagreements.
4. Keep inferred claims visually distinct even when fluent prose is used; maintain source links and explanatory uncertainty.
5. For contradictions, display both versions with timestamp/commit, not a fabricated resolution. Provide decision or targeted runtime-test pathways.
6. Escape all raw source content in HTML; do not embed executable fragments captured from legacy systems.
7. Reopen and validate navigation, source references and confidence labels. Never mark external verification successful without tool evidence.

## Acceptance

The reviewer can answer: 'Which requirements come from inspected code? Which were guessed? Which disagree? What should be tested next?' If the preview hides those distinctions, it fails regardless of styling.


## Ownership

ANGENT Root/Core retains reasoning, stakeholder intent, source authority and final Quality. This method is a task-specific support skill and does not create a second runtime, memory system or autonomous scheduler.
