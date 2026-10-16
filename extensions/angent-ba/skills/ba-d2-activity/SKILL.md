---
name: ba-d2-activity
description: Source-traceable BA d2-activity D2 modeling using tested JSON-to-D2 and real SVG rendering when available.
---

**Method origin:** maintained independent adaptation of the MIT Dev BA Kit /d2-activity skill, copyright 2026 Edward Ngo, https://github.com/nv-minh/dev-ba-kit/blob/main/skills/d2-activity/SKILL.md. Original ANGENT generator; no commercial AI4BA source included.

# D2 Activity and swimlane process modeling

## Outcome

Produce a semantically defensible D2 activity source file and, only when a real D2 CLI is available, a rendered SVG. Activity diagrams model task sequences, ownership, decisions and alternative paths. They are not executable BPMN processes.

## Process evidence

1. Read the accepted SRS, business rules and use case. Fix source revision, scope, users, decision authority and failure outcomes.
2. Describe the start trigger, meaningful tasks, guarded decisions and terminal results. Record authorization rejection, cancellation and recovery paths where the accepted contract requires them.
3. Normalize a stable node list. Supported kinds are start, task, decision and end. A decision needs two or more transitions each with a guard; a terminal has no outgoing edges; each reachable nonterminal has an exit.
4. For swimlanes, assign each node to a genuine actor or system owner. Cross-lane transitions model a real handoff, not an aesthetic grouping. Every node must have a lane when lanes are used.
5. Convert the accepted process to JSON containing type activity, title, direction, nodes (id, label, kind, optional lane), and edges (from, to, guard on decision exits). Review this conversion against the source; free-form requirement extraction is not automated here.
6. Run the ANGENT compiler. It validates reachability, decisions, lanes, targets and labels before generating D2 code. If there is an installed D2 CLI, render SVG and examine direction, clipping, labels and branch paths against the decision table.
7. Preserve existing accepted diagrams on updates: compare the previous D2 and model with the proposed diff before authorized overwrite. The generator deliberately refuses to overwrite outputs.

## Real commands

    python extensions/angent-ba/scripts/build_d2.py extensions/angent-ba/examples/d2-activity.json --output output/activity.d2

    python extensions/angent-ba/scripts/build_d2.py INPUT.json --output output/activity.d2 --svg output/activity.svg --d2 PATH_TO_D2

    python tests/integration/check_d2_cli.py --d2 PATH_TO_D2

## Acceptance

Exactly one start, no stranded nodes, guarded decision alternatives, accurate actor ownership, source-backed messages, successful real renderer exit and visual read-back. Generated D2 syntax alone does not prove correct business interpretation. Use BA BPMN for standards-compliant process exchange and plain prose if a diagram is not useful.

## ANGENT boundary

ANGENT Root retains task choice, approval and overall reasoning. BA supplies specialist modeling methods; Execution handles file changes and real CLI invocations, and Quality validates the semantic result. This implementation does not support arbitrary parallel BPMN gateways, Mermaid round-tripping or automatic process discovery.
