# Scoped authorization and change safety for BA work

**Provenance:** Method adapted from MIT Dev BA Kit / rules/approval-gate.md (Edward Ngo, 2026), https://github.com/nv-minh/dev-ba-kit. ANGENT Root and the host own permissions; this note creates no new gate service.

## Authority is defined by the user and host

Read-only investigation, writing an explicitly requested review draft, changing source-controlled files, overwriting an accepted decision and mutating Jira/Figma/Confluence have different risks. Do not force a confirmation before every individual file when the user has already authorized the entire well-defined implementation scope. Conversely, a broad request to research BA methods does not authorize publishing to external systems.

Before consequential changes identify: target repository/branch or provider resource, allowed action, what will be preserved, expected side effects and verification method. A user instruction that forbids merge or publication remains binding even if all tests are green.

## File changes and conflict control

Read the latest target before editing. Prefer a targeted diff over rewriting the complete document. Keep stable requirement IDs and human-edited paragraphs. For source-control work, preserve the branch ref expected SHA and stop on concurrent updates instead of force pushing.

When a source is approved, note its revision and whether a decision is superseded; changing a document does not automatically change business approval. Where safe rollback is not possible, take a read-only snapshot or offer a proposed patch before writing.

## External providers

Confirm the exact page/file/site/issue, current version and permissions through the actual tool. Create/update only the authorized scope. For uncertain writes, read back before retrying to prevent duplicate Jira issues or duplicate Figma frames. Record confirmed, failed and uncertain results separately.

If a provider cannot preserve rich content, support conflict detection or read back critical effects, do not pretend the update is safe. Deliver a reviewable diff and disclose the missing operation.

## Review and iteration

Iterate when evidence, business semantics, rendering or tests show a defect. A fixed count of revisions or a mandatory prompt ceremony is not a quality measure. The final review compares the output to the user request and inspected sources, not just to a generated template.

The controlling rules are ANGENT Core, the actual project instructions and current host permissions. This methodological note cannot bypass them.
