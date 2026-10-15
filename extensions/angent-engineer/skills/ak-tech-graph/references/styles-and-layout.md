# Technical SVG style and layout contracts

Based on the seven visual styles and SVG layout guidance in the stable Engineer 2.19.0 Tech Graph package. These are **style choices**, not bundled rendering templates or mandatory pixel constraints. Use authorized current brand tokens when the user supplies them.

## Seven style families

| Family | Visual principle | Appropriate uses | Main caution |
|---|---|---|---|
| 1 — Flat icon | Plain shapes, clear hierarchy and restrained accents | General architecture, process and component diagrams | Avoid cartoon-like icon overload |
| 2 — Dark terminal | Dark canvas, high-contrast boundaries | Developer/infrastructure presentations | Contrast and print legibility |
| 3 — Blueprint | Drafting/grid-inspired, precise connectors | Formal architecture, UML, topology | Grid can compete with labels |
| 4 — Notion clean | Light, simple cards and typography | Documentation, dense sequence or ER | Keep boundaries visible at small size |
| 5 — Glassmorphism | Transparency and layered surfaces | Sparse concept/product diagrams | Usually poor for dense data flows, lifelines and technical labels |
| 6 — Claude-inspired warm | Warm neutrals and restrained warm accents | Explanations and selected technical documentation | Follow actual brand usage permissions, not a claim of official affiliation |
| 7 — OpenAI-inspired clean | Minimal open surfaces and controlled accents | API/architecture and comparison documents | Brand resemblance is not an official logo |

Selection depends on content density, target background, reader and accessibility. Never assume colors/themes are official brand assets merely because upstream describes an aesthetic family.

## Diagram-specific layout rules

- **Architecture:** group by trust/ownership/deployment layer; request/data arrows follow actual direction. Show separately where logical and deployment boundaries differ.
- **Data flow:** label payload/operation where important. Distinguish data transfer, control trigger and transformation by explicitly defined arrow semantics.
- **Sequence:** fixed participant lifelines, downward time, nonoverlapping message label bands, activation/alt/loop frames aligned with events.
- **State:** actual states, trigger/guard/action, initial/terminal nodes; draw valid transitions, not just workflow order.
- **UML class/ER:** member/field legibility, correct inheritance/composition/cardinality, prevent arrowheads from colliding with type labels.
- **Use case:** system boundary contains actions; human/external actors outside; use include/extend semantics only when warranted.
- **Agent/memory:** distinguish input/core/tool/output and only the actually implemented memory stores and read/write/consolidation paths.
- **Timeline/matrix:** grounded values and correct time/units; a true comparison table is often clearer than decorative SVG.

## Spacing, connectors and layering

Prefer a single reading direction and clear visual hierarchy. Plan node bounds, text bounds, legend, container boundaries and dedicated edge corridors **before** routing connectors.

The upstream guide uses indicative clearances around 80–120 px between components/layers on a ~960 px canvas and smaller label padding. These are starting heuristics, not invariants; adjust to actual font metrics, viewBox and final display size.

Anchor connectors on node **edges/ports**, not through component interiors or corners. Route around groups, prefer orthogonal paths where possible, stagger parallel lines and use jump/bridge semantics only for genuinely unavoidable crossings. Prevent crossing lines from masquerading as junctions.

Arrow labels need legible background separation, especially over lines; leave distance from node edges and other labels. SVG paints in document order: background, containers, connectors, label backdrops, nodes, text/labels and final legend/annotations, adjusted so arrowheads and label backdrops are not accidentally hidden.

When multiple arrow types carry meaning (request, async, memory read/write, feedback), express that in shape/dash/labels as well as color; explain it in a legend. Preserve accessible contrast and alt/title description where the destination supports them.

## Final rendered acceptance

At actual reading scale, verify:
- no arrow traverses unrelated component interiors;
- line crossings have unambiguous topology;
- arrowheads touch intended target ports;
- text and note labels are not clipped or hidden by nodes/arrows;
- loop/alt captions do not overlap messages;
- legends and annotations are outside active flow;
- raster export preserves fonts, colors and edges from SVG.

If any test fails, expand the canvas or reorganize layout instead of continuously shrinking type. An SVG parser or CLI success is only a syntactic check, not a visual acceptance result.
