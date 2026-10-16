---
name: ba-confluence
description: ANGENT BA specialist for confluence with source evidence, host authorization and real tool boundaries.
---

# Confluence documentation synchronization without destructive overwrite
**Source:** Maintained adaptation of the MIT Dev BA Kit by Edward Ngo (2026), https://github.com/nv-minh/dev-ba-kit/blob/main/skills/sync-confluence/SKILL.md. ANGENT Root/Core retains final authority.



## Purpose

Align a specific Confluence page section with accepted requirements or independently checked code behavior. Do not erase rich macros, tables, restricted content or existing teaching-quality prose merely to achieve text similarity.

## Safe provider workflow

1. Identify the exact page URL/site, audience, source feature, SRS or code revision and intended section. Distinguish approved product intent from source-observed implementation and proposed changes.
2. Through the actual authorized Atlassian connector, retrieve the exact page, current version, edit permissions and representation (storage HTML, rich markup or supported alternative). Do not assume an old Rovo tool name is available.
3. Read the complete relevant section and its surrounding anchors, heading hierarchy, macros and tables. If the connector only returns lossy Markdown, do not assume a whole-page Markdown-to-HTML rewrite will preserve its structure.
4. Compare each candidate statement with precise source evidence and provider revision. If the target section cannot be identified, propose a new section and its insertion point; do not replace arbitrary text.
5. Generate a focused before/after diff including changed FR/BR/error data, affected links and consequences. Preserve unrelated headings, macros, attachments, permissions and author notes.
6. Re-read the live page version immediately before any authorized mutation. Detect concurrent edits from the provider itself rather than an invented local sync-state hash.
7. Use only provider-supported update operations with version preconditions and the correct storage representation. If a safe section-preserving mutation is impossible, stop and provide a patch proposal instead.
8. Read back and inspect the edited page. Verify target text, existing macros, section boundaries, version and links; distinguish confirmed effects from uncertain outcomes.
9. Report page URL, actual revision, changed sections, source evidence, any unresolved content and verified read-back.

## Boundaries

Review-only requests stop before step 7. Changes to source code or implementation are separate tasks needing their own permission. Neither a recent Git commit nor a passing mocked test proves deployed business behavior. Do not hardcode cloud IDs, copy a private page into another tenant, add an automatic sync footer, or maintain .claude/state/atlassian/sync-state.yaml as a shadow source of truth.

## Example

A verified change to vehicle telemetry freshness can affect the API error/last-known-value section of a Confluence page. It does not authorize updating unrelated maintenance policy or claiming a production rollout. Keep conflicting requirements and unresolved owner decisions visible.

ANGENT Root retains source authority and user intent; Execution owns provider effects and version safety; BA owns section-to-requirement correspondence; Quality verifies content after write.
