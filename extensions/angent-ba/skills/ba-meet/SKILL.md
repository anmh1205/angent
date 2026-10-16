---
name: ba-meet
description: Source-driven BA meet method with independent decision evidence, output validation and safe provider boundaries.
---

# Meeting evidence, decisions and accountable follow-up

**Method origin:** An independent adaptation of MIT Dev BA Kit's meeting method by Edward Ngo (2026): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/meeting/SKILL.md. Recorded human decisions remain authoritative only to the extent supported by the actual meeting evidence and stakeholder approval.

## Before writing minutes

1. Identify whether the user wants notes, decision extraction, action tracking or a meeting preparation brief. Read provided transcript/notes, actual calendar details if connected and relevant earlier decisions. Do not invent a meeting date, attendee, quote or speaker assignment.
2. Distinguish direct statements from paraphrases, analyst inferences and decisions confirmed by an authorized owner. A participant saying "we could" is not the same as approving a budget, a policy or a product change.
3. If the transcript is incomplete or contains unclear attribution, preserve uncertainty and quote only short decisive phrases where necessary. Keep confidential meeting details within their authorized project/provider context.
4. Identify the underlying business issue, decisions and rationale, competing options, blocked dependencies, unanswered questions, risks and follow-ups. Avoid dumping a chronological chat transcript when a coherent written record is needed.
5. Give every decision a stable local ID where useful, its source/time anchor, decision owner, affected CAP/FR/BR and explicit status (**proposed, confirmed, superseded or disputed**). A decision about vehicle-control permission may require safety/privacy review before it becomes a BR.
6. Turn follow-ups into action records with outcome, responsible owner, requested date/deadline if **actually specified**, dependencies and completion evidence. If no owner or deadline was agreed, mark it **unassigned/undated**, not secretly assign one.
7. For already recorded minutes, compare with their current version, avoid duplicate decisions and preserve participant corrections. Do not overwrite an approved decision history or create a hidden \`activity.log\` as a side effect.
8. Route approved changes to the relevant source document or provider only when authorized. A meeting decision affecting an FR may require SRS/AC/TC review, but a meeting note by itself does not establish code implementation or deployment.

## Deliverable

Write a readable summary of purpose and discussion, then explicit **confirmed decisions, contested/proposed decisions, actions, blockers and unresolved questions**, with evidence/source anchors and responsible owners where known. Existing project style governs the artifact; no compulsory \`docs/meetings/YYYY-MM-DD-...\` path, artificial "captured→processed" status or date-inventing file name.

## Example distinction

A participant says "We should probably warn the rental operator if telemetry has not arrived recently." Record that as a **proposal** and an open policy decision about acceptable freshness. If the authorized operator later confirms a precise value and behavior, record the approved rule with its evidence and downstream effects. Do not add a five-minute threshold from common intuition.

## Verification

Check traceability of named decisions, explicit actor ownership, absent/fabricated dates, competing proposals, confidentiality, and whether follow-up work is genuinely authorized. A plan to create Jira tasks is not proof tasks were created. ANGENT Core owns interpretation and editorial quality; BA supplies accountability structure, Execution performs permitted provider actions and Quality reads back any actual changes.
