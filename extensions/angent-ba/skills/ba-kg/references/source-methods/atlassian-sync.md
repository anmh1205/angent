# Jira and Confluence synchronization by live provider evidence

**Provenance:** Adapted from MIT Dev BA Kit / rules/atlassian-sync.md (Edward Ngo, 2026), https://github.com/nv-minh/dev-ba-kit. Tool names and capabilities below must be discovered from the currently connected Atlassian provider, not assumed from a previous host.

## Source, destination and identity

For Jira, map a stable accepted US identifier to an actual issue key and project. For Confluence, use an exact page identifier plus site/space. Never infer authorization from a similar issue title or reuse a tenant ID from an example.

Read current provider state first. Record issue/page version, source requirement revision, actor roles and intended changed fields. Confirm the user authorized the relevant write scope.

## Jira-specific controls

Find existing issues before creating anything. Compare summary, AC, description, source requirement IDs, status and rights. Build create/update/no-op actions. On unknown write outcome, query for the stable source ID or key before retrying; blind retries can duplicate tickets.

After any mutation, read back exact key, project, fields and workflow state. “Done” is delivery workflow metadata, not stakeholder requirement approval or production acceptance. Do not fabricate issue links.

## Confluence-specific controls

Read the page in a representation preserving its existing macros, tables and attachments. Compose a section-level diff while preserving unrelated human content. Use a provider-supported version precondition and content format; if only destructive whole-page overwrite is available, stop and provide a safe patch proposal.

After writing, retrieve the exact page again and confirm that the intended sections changed while macros, headings, links and permissions were preserved. A successful HTTP response alone is not a content-integrity check.

## Provenance without shadow synchronization state

Store actual issue/page links in an existing authorized project story index or accepted documentation when useful. Provider versions and source Git revisions are sufficient for conflict checks during the task; no second database or mandatory local watermark ledger is needed.

## Failure examples

Two stories with the same title may represent different vehicle roles. A changed Confluence page may have been edited by an author since the initial read. In both cases, resolve identity and revision instead of overwriting on a guess.

The BA specialist supplies requirement meaning and mapping; ANGENT Execution performs provider calls and authorized mutations; Quality validates the real provider read-back.
