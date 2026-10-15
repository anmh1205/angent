# UX/AX review contract

## UX dimensions

Inspect only dimensions relevant to the product:
- first impression and task clarity;
- information hierarchy and content density;
- navigation and user flow;
- component/state consistency;
- responsive/touch behavior;
- loading/empty/error/auth states;
- accessibility and keyboard use;
- motion/feedback;
- trust and visual coherence.

Use representative desktop/tablet/mobile viewports when the surface is responsive.

## AX dimensions

Check observable discoverability signals relevant to the app:
- crawl/index boundaries;
- canonical and structured metadata;
- semantic headings/content structure;
- quotable and stable content;
- machine-readable public documentation or markdown twins when the product intentionally exposes them;
- sitemap/robots/canonical URL consistency;
- share/preview metadata;
- agent-facing actions only when actually implemented.

Do not manufacture SEO/AX rules disconnected from current evidence.

## DONE contract

A review is DONE only when:
- ranked findings cite the observed surface/code;
- each Must/Should has a concrete acceptance condition;
- unavailable checks are marked unverified;
- auto/loop mode rechecks every touched surface;
- unresolved questions are explicit.

A screenshot or build PASS alone does not establish the whole contract.
