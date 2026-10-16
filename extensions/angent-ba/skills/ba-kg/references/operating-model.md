# Portable BA evidence and traceability contract

This is a **project-specific artifact model**, not a new ANGENT global memory or mandatory tracker. The real project provider remains authoritative. Portable methods use it as a small common vocabulary:

- **Artifact**: stable ID, kind (NEED, BO, CAP, FR, NFR, BR, UC, US, AC, SCREEN, API, TEST, DECISION, EVIDENCE), title, revision, status, source links, and *depends_on* IDs.
- **Evidence**: source URI/path, version or commit, location/line when actually read, observed quotation or behavior, confidence, captured time only if known.
- **Decision**: stakeholder/owner if known, explicit acceptance state, alternatives and tradeoffs, timestamp only if factual.
- **Relationship**: `derives_from`, `implements`, `verifies`, `visualizes`, `supersedes`, or `depends_on`. Every referenced ID must resolve within inspected scope or carry `external_ref`.

## Workflow invariants

1. Separate proposed requirements, observed implementation and approved commitments; do not infer approval from code.
2. Do not silently renumber stable IDs across revisions; use explicit supersession mapping.
3. Coverage requires a real semantic link, not just presence of a matching number in a paragraph. One test can verify multiple FRs; not all FRs need a UI screen.
4. When requirements change, walk *reverse dependency* links, show impact and proposed diffs, and seek appropriate approval before writes.
5. Approval or status on Jira, Confluence, GitHub, Figma, and file system must be read from the actual provider when material.
6. Preserve the user's existing artifact schema if equivalent; the model is an interop convention, not a forced migration.
7. Rendered diagrams and generated code must be checked with the corresponding runtime where possible; parsing or generation is not execution evidence.

## Minimal exchange JSON

```json
{
  "artifacts": [
    {"id":"FR-AUTH-001","kind":"FR","title":"Authenticate known account","depends_on":["BR-AUTH-001"],"source_refs":["DOC-3"],"status":"proposed"},
    {"id":"BR-AUTH-001","kind":"BR","title":"Rate limit failed logins","depends_on":[],"source_refs":["DOC-3"],"status":"approved"},
    {"id":"TC-AUTH-001","kind":"TEST","title":"Verify invalid password handling","depends_on":["FR-AUTH-001"],"source_refs":["DOC-3"],"status":"draft"}
  ],
  "sources":[{"id":"DOC-3","uri":"docs/authentication.md","revision":"example-only"}]
}
```

Use the actual artifact validator under `extensions/angent-ba/scripts/validate_artifacts.py` if runtime access exists. Graph validation cannot establish correctness of the natural-language claim.
