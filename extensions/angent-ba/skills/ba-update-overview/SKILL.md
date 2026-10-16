---
name: ba-update-overview
description: Specialized ANGENT business analysis update-overview method.
---

# Scoped update of a project-wide overview

## Purpose

After approved changes to a feature, recompute only the overview sections that depend on altered source facts. The overview is a read model, not the repository of decisions. Do not regenerate an entire project history from an isolated feature or overwrite manual stakeholder narrative.

## Reconciliation

1. Read current overview and capture revision/ETag if a remote provider is involved. Determine authoritative source for each section (PRD, SRS, provider issue state, deployment, customer decision).
2. Collect accepted change set with stable artifact IDs and exact source revisions; calculate reverse dependencies and affected overview statements.
3. Compare baseline to candidate statement by statement. Classify unchanged, updated, removed, new and blocked-by-uncertainty. Keep unaffected prose and links byte-for-byte where practical.
4. Check whether status counts are real: use actual project issue data and explicit filters, not fabricated percentages. Unknown/awaiting-approval must be distinct from done.
5. Present a reviewable diff and reasons, especially for business objective, roadmap, scope, release, actor role or risk changes.
6. Perform an external write only with current permission and an authoritative latest revision. For Confluence/Google Docs read after writing and compare the changed sections, safeguarding concurrent edits.
7. Report changed IDs, skipped or conflicting sections, final provider version if confirmed and remaining actions.

## Failures to catch

Stale release dates, duplicated feature counts, broken section anchors, unrelated content removed by regeneration, optimistic completion labels and silent edits to a different project or environment.

## Example

A newly approved authentication recovery path affects the SRS error matrix, userflow, checklist and 'Capabilities' summary; it does not justify rewriting the vehicle telemetry section or inventing a released status.


## Ownership

ANGENT Root/Core retains reasoning, stakeholder intent, source authority and final Quality. This method is a task-specific support skill and does not create a second runtime, memory system or autonomous scheduler.


## Actual impact input

For two validated revisions of project requirements, derive an evidence-bound update scope using the portable read-only comparator:

    python extensions/angent-ba/scripts/compare_artifact_revisions.py BEFORE.json AFTER.json

Use direct_review and dependent_review to find the *candidate* overview sections that need checking. Preserve all other overview paragraphs. Even when an artifact ID exists in both versions, its title, status, dependencies and source provenance may change. The comparator does not infer current Jira, deployment or customer approval; reconcile such facts with the actual provider and an authorized read-back. Never interpret a source revision change as proof of production behavior or unilaterally update the overview.
