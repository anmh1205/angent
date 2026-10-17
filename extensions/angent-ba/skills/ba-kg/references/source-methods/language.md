# Language and terminology across BA artifacts

**Provenance:** Adapted from MIT Dev BA Kit / rules/language.md (Edward Ngo, 2026), https://github.com/nv-minh/dev-ba-kit. Language choice follows the user and project, not a forced runtime flag.

## Choose language and register

An explicit requested language or an established approved document style takes precedence. Otherwise mirror the user's main language while maintaining the current project's glossary. When the audience includes both business stakeholders and engineers, explain specialist terms at first use and keep later usage consistent.

Use natural Vietnamese or English as appropriate, without mechanically translating established domain terminology. Do not mix languages because a source template happens to have English headings. A bilingual output needs clear alignment of concepts, not alternating literal fragments.

## Preserve literal technical identities

Never translate code identifiers, HTTP paths, JSON field names, test IDs, product/vendor names or diagram-language syntax. An actor-visible explanation may translate surrounding prose while keeping exact system/API labels for traceability.

Error messages shown to a customer should be sourced from accepted localization policy. Do not invent translations of security-sensitive UI messages or promise localization for a product that does not implement it.

## Updates and visual materials

Preserve the accepted language of an existing file unless the user requests a rewrite. Diagram labels should use the same glossary as the related FR/BR/userflow. Use readable font size and avoid ambiguous abbreviations in compact nodes.

## Quality

Review for coherent paragraph flow, natural terms, consistent role names and avoidance of mechanical word-for-word calques. Completeness and precision matter more than template section count.

The final user-facing response remains ANGENT Root's responsibility, and this rule only supplies specialist writing standards.
