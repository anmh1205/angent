# Stable 2.19.0 Preview mode-to-evidence table

| Mode | Required input | Actual output | Proof |
|---|---|---|---|
| View file/directory | Existing readable resource | Browser/native file view | Source opened, no file overwritten |
| explain | Concept/source basis | Explanatory Markdown or HTML | Concept and mechanism transfer |
| diagram | Verified nodes/edges | Editable source or rendered diagram | Syntax plus real visual check |
| slides | Audience and narrative | Presentation content | Slide sequence and viewport review |
| html diff | Git ref/base and changed source | Self-contained diff explorer | Diff matches commit/ref |
| html plan-review | Active plan plus source/acceptance | Evidence-linked comparison | No false done statuses |
| html recap | Real Git/continuity/project state | Project summary | Provenance/timestamps stated |

In native Preview, HTML mode can use templates, theme toggle, zoom/navigation and styled interactive examples. These are **requirements for the generated artifact**, not capabilities that the portable SKILL.md itself already implements. If a requested format cannot be rendered, return the source and specific missing runtime, not a made-up link.

View mode should never create a slideshow simply because the user wants to inspect a file.
