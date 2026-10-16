# Project artifact knowledge graph

**Project and source revisions:**  
**Included: URD, BRD, PRD, SRS, use cases/stories, AC, checklist, tests:**  

## Source-indexed nodes

| ID | Kind: UN/BO/CAP/FR/BR/AC/CHK/TC | Title | File and line | Approval/evidence status |
|---|---|---|---|---|
| | | | | |

## Declared relationships

| Child ID | Relationship | Parent ID | Exact source cell/line | Meaning and uncertainty |
|---|---|---|---|---|
| | depends_on / covers / verifies | | | |

Never invent graph links from co-occurring words. External references without inspected definitions remain unresolved, not fake internal nodes.

## Full lifecycle metrics

| Metric | Actual count | Source scope | IDs not covered |
|---|---|---|---|
| UN/BO/CAP indexed | | | |
| FR traced via CAP→BO→UN | | | |
| FR linked to downstream TC | | | |
| FR with complete structural chain | | | |

## Verification

Check duplicates, missing dependencies, cycles, source file revisions and invalid local paths. When running inside the ANGENT source tree, use extract_markdown_graph.py with optional --urd, --brd, --prd and mandatory --srs plus existing test files; validate output using validate_artifacts.py.

This graph proves structural reference integrity only. A linked test is not an executed test, and a source's approved status is not evidence of a deployed behavior.
