# Evidence-based change history, not a hidden event log

**Provenance:** Adapted from MIT Dev BA Kit / rules/changelog.md (Edward Ngo, 2026), https://github.com/nv-minh/dev-ba-kit. ANGENT intentionally does not port an automatic Claude hook or universal append-only activity file.

## Where change history comes from

For tracked project files, use actual Git commits and diffs with pinned branch/commit IDs. For Jira and Confluence, use the provider's issue/page versions and changelog; for Figma, read the file/node state and relevant provider history. A generated BA report has no special authority over these sources.

Distinguish observed edits, accepted product decisions, code deployments and provider publication. A document updated on Tuesday does not imply a system was deployed on Tuesday.

## Change record for a specific task

Capture affected artifact IDs, source revision before/after, what actually changed, owner/authorization and verified target state. Where material, include consequences for downstream FR, tests, screens and provider issues; use the existing read-only compare_artifact_revisions.py tool for a versioned BA graph.

Do not automatically create a second project-wide history repository or infer authorship from a username string. A Git commit author may not be the business approver.

## Concurrent edits and reconciliation

Re-read the latest target before mutation. When another author made a change, preserve both versions and reconcile at field or paragraph level. A stale timestamp or a hash mismatch is a reason to inspect, not a reason to overwrite.

## Example

A new BR changes who may read a rental vehicle's status. The change report links the accepted BR decision, affected FR/AC/TC and actual Git or Jira changes. It does not claim the new policy is deployed until runtime evidence exists.

A historical source log from another framework may be inspected as evidence if it actually exists, but never be installed as a compulsory ANGENT workflow.
