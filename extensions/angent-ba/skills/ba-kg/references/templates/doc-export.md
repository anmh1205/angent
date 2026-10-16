---
type: export-package
updated: {{date}}
links: []
---

# {{scope}} — stakeholder delivery

## Source inventory and precedence

| Document | Exact source path | Revision or SHA-256 | Approval state |
|---|---|---|---|
| {{doc}} | {{path}} | {{verified_source_revision}} | {{approved_or_draft}} |

## Delivered artifact

| Format | Actual output file | Generator and runtime | Validation evidence |
|---|---|---|---|
| {{md_html_docx_or_pdf}} | {{existing_output_path}} | {{command_and_version}} | {{opened_and_checked_or_not_run}} |

For reviewed Markdown files, use the real ANGENT exporter:

    python extensions/angent-ba/scripts/build_export.py DOC.md --root PATH_TO_DOC_ROOT --output OUTPUT.md --format md --title "Stakeholder review"

DOCX/HTML and PDF are available only when their actual dependencies succeed. Do not claim to have generated a PDF without a real PDF engine and reader check; do not automatically download remote fonts/images or overwrite an accepted previous export.

## Changes included

| Decision or section | Previous source | Current source | Actual change | Evidence |
|---|---|---|---|---|
| {{item}} | {{revision}} | {{revision}} | {{difference}} | {{source}} |

This history comes from inspected source revisions or real provider records, **not** a non-existent activity.log, automatic history file or guessed timestamp.

## Review outcome

{{audience_check_accessibility_sensitive_data_and_missing_evidence}}
