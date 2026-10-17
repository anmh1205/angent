# Choosing diagrams by the question the reader must answer

**Provenance:** Adapted from MIT Dev BA Kit / rules/diagram-selection.md (Edward Ngo, 2026), https://github.com/nv-minh/dev-ba-kit. ANGENT Root selects specialist methods using the existing Hub manifest.

## Prefer the smallest accurate representation

| Question | Representation and relevant specialist | Concrete acceptance concern |
|---|---|---|
| Which business actor owns each step and decision? | Activity or swimlane: ba-activity, ba-activity-swimlane, ba-d2-activity | Guarded branches and real owner handoffs |
| Does a process need formal BPMN interchange? | ba-bpmn | Supported BPMN subset, XML/XSD, modeler support |
| Which message happens in which order, and who replies? | ba-sequence or figma-sequence | Participant identity, alt/loop semantics, failures |
| What states may one entity enter or leave? | ba-state or figma-state | Event guards and impossible transitions |
| How are business entities/fields related? | ba-erd, ba-d2-erd, ba-dbdiagram or figma-erd | PK/FK, optionality, cardinality and source schema |
| Which subsystem sends data to another? | ba-d2-architect | Protocol/trust boundary and owner |
| Which screens can a user reach? | ba-user-flow or figma-userflow | Branch targets, denied/recovery paths |
| What pages belong under a site section? | figma-sitemap, or a text tree | Hierarchy, orphans, depth |
| Which actor goal is in the product boundary? | ba-usecase-diagram or capable native Figma provider | Correct include/extend and ownership |
| Is an actual interactive screen or UI component needed? | ba-wireframe-html, ba-prototype-html, ba-prototype-next, ba-figma | Rendered controls and verified interaction, not a graph |

A diagram is optional. Plain prose, an error matrix or a table often makes a small policy clearer. Avoid turning every paragraph into a generic flowchart.

## Choose the format by actual output

Mermaid is convenient when the current viewer demonstrably renders it. D2 is appropriate when its real CLI can be run. BPMN is appropriate when the consumer needs BPMN XML, not merely a pretty workflow image. PlantUML is optional and requires a verified local runtime for actual rendering.

Reqwise OSS has six diagram types: activity, sequence, state, ERD, userflow and sitemap. Use-case, BPMN, journey/persona, design system and demo features advertised for Pro must not be falsely described as supported by the OSS diagram tool.

## Data-to-visual contract

Build a semantic source model first, including stable IDs, actor or field ownership, error paths and source references. Compile/render where a real tool exists, inspect the output and recheck it against the source. A diagram valid for one synthetic fixture says nothing about an unrelated live product.

For Figma editing, verify the actual plugin/MCP session and file, authorize target writes, then read back node identities, relationships and layout. A generated JSON candidate cannot replace that read-back.

## Examples of wrong choices

A fleet vehicle authorization problem is primarily a business rule and negative test, not a C4 architecture diagram. A database FK mismatch is best explained by ERD/DDL, not a screen userflow. An incident-response playbook may need detailed BPMN only if the organization actually uses BPMN interchange.
