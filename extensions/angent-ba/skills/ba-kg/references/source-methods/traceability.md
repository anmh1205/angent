# Traceability from need to design, acceptance and observed delivery

**Provenance:** Adapted from MIT Dev BA Kit / rules/traceability.md (Edward Ngo, 2026), https://github.com/nv-minh/dev-ba-kit; aligned with IIBA requirements/design traceability.

## Typed evidence lineage

Use the project-relevant subset of UN → BO → CAP → FR/NFR/BR → actor/story/design behavior → AC/CHK → TC. A directed dependency means that the downstream item explicitly cites the upstream item; it is **not** a task execution dependency. Distinguish source rows from calculated graph edges.

Read actual accepted URD/BRD/PRD/SRS and relevant story/test indexes. The ANGENT extractor supports a bounded set of Markdown table structures:

    python extensions/angent-ba/scripts/extract_markdown_graph.py --urd USER_NEEDS.md --brd BUSINESS_RULES.md --prd CAPABILITIES.md --srs SRS.md --checklist CHECKLIST.md --cases CASES.md --root PROJECT_ROOT --output REVIEW_GRAPH.json

Use the existing Python validator to reject missing references, cycles and reversed evidence types. An unresolved cross-file ID must be reported; never generate a missing requirement to make the model appear complete.

## Count claims and proof paths

For each FR, show the actual upstream UN/BO/CAP route and the actual path to a linked TC, with source file revision. Report missing upstream links and missing test artifacts separately. The presence of a TC is **structural coverage only**: it is not a passed test, an implemented feature or an approved stakeholder decision.

A story may cover several FRs, so a TC attached to the story alone does not prove that every FR has a specific test. Preserve exact relationships and avoid propagating coverage via unrelated story memberships.

## Change impact and drift

Use compare_artifact_revisions.py to compare two validated source graph snapshots and identify changed IDs and dependent artifacts. Validate code-to-requirement witnesses against pinned Git blobs only when code evidence is needed. A changed commit or updated Jira issue is not automatically a changed policy.

When code, documentation and stakeholder decisions conflict, show each source and its trust boundary. The correct resolution comes from actual owners, not from arbitrarily choosing the newest timestamp.

## Example

A fleet ownership BR can support FR access rules and a TC denying unauthorized vehicle status. A successful mock test shows its fixture enforces the example, but live data isolation still requires actual API/device/cloud testing.

No mandatory singleton report or separate state store is created by this method. Output can be a concise cited analysis, or an existing authorized document when persistence is genuinely useful.
