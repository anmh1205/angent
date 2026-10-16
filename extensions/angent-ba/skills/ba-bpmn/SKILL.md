---
name: ba-bpmn
description: Build a business-process model in BPMN 2.0 with semantic review, independently verified XML interchange, and explicit layout/runtime limits.
---

# BA BPMN: requirements, semantics, XML interchange and diagram review

## Task contract

Use this method when the user needs BPMN semantics rather than an informal flowchart. ANGENT Root owns intent and authorization; BA owns business-process correctness; Execution produces authorized artifacts; Quality checks independent results.

**Provenance:** Adapted in concept from the MIT Dev BA Kit BPMN method by Edward Ngo (2026): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/bpmn/SKILL.md. Its Claude Code hooks, TypeScript engine, auto-layout package and editor are NOT automatically bundled into ANGENT; the portable implementation below is separately written.

## Supported source IR and actual executable tool

The portable compiler at extensions/angent-ba/scripts/build_bpmn.py consumes a JSON IR with process, lanes, nodes, and flows:

- process: id and title. IDs must be XML NCNames and unique across process, lane, node and flow.
- lanes: optional actor/owner columns. Each node requires one valid lane when lanes exist.
- nodes: id, kind (start/task/gateway/end), lane and name.
- flows: id, src, tgt and name for each outgoing branch of a diverging gateway.

The output is a BPMN 2.0 XML document with a semantic process, incoming/outgoing references, optional laneSet, exclusive gateway direction, sequence flow, and BPMN DI shape/edge coordinates. It is a **file compiler**, not an executable business process engine.

Check IR before generation:

    python extensions/angent-ba/scripts/build_bpmn.py PATH/claim.ir.json --check

Write a real file in an authorized project location:

    python extensions/angent-ba/scripts/build_bpmn.py PATH/claim.ir.json --output PATH/claim.bpmn

A worked multi-lane source is at extensions/angent-ba/examples/atlas-re/bpmn/claim-approval.ir.json. The test suite checks this model and independently verified its XML interchange with bpmn-moddle version 9, without parser warnings. That test does not certify every diagram layout.

### Critical limits: reject, do not misrepresent

The current compiler supports one NONEXECUTABLE process, one start event, one or more ends, tasks, exclusive split/join gateways, and ACYCLIC directed sequence flow. It intentionally rejects loopbacks, parallel/inclusive constructs, subprocesses, cross-pool message flow, timer/boundary/cancellation/compensation events and executable process definitions. It uses basic deterministic geometry; this is NOT equivalent to a professional auto-layout modeler.

If the requirements need unsupported elements, use a real advanced BPMN generator only when installed and verified, or return a reviewed IR and a precise pending-tool boundary. Do not silently replace a timer or message interaction with a normal task.

## Authoring sequence

1. Pin accepted SRS/use-case revision. List business actors, events, decisions, normal outcomes, faults and errors with source IDs. Distinguish observed behavior from proposed behavior.
2. Decide whether to model one process with lanes or collaboration with independent pools. A lane is an owner within one process; sequence flow must not cross distinct pools.
3. Normalize nodes and flows. Give one owner to each task, use named conditions for every divergent gateway, preserve explicit errors and recovery states, and assign stable IDs.
4. Compare the IR against its source facts: actors versus lanes, business-rule branches versus gateway guards, errors versus end/recovery nodes. Unresolved rules remain visible.
5. Run structural validation. Fix unknown edges, duplicates, dangling paths, orphan tasks, unreachable ends, and split gateways without labels BEFORE compiling XML.
6. Use the portable compiler only for its supported subset. Independently parse generated XML with a BPMN model parser where available and compare lane, node, edge and DI counts.
7. Visually inspect a real renderer: look for overlapping nodes, clipped text, crossed connectors and detached labels. Do not treat a successful XML import as a visual review.
8. If a native Figma renderer is requested, check the current Figma tool's actual capabilities and file permissions. The six public Reqwise OSS diagram types do not include BPMN; a native canvas edit requires different tooling and read-back.
9. When modifying an accepted process, show a bounded diff, preserve ID meaning, and verify that unaffected states/lanes remain intact.
10. Report source revision, output path, IR checks, XML/parser checks, visual review evidence, unimplemented features and remaining decisions.

## Review matrix

| Area | Acceptance | Typical failure |
|---|---|---|
| Event | Clear source trigger and terminal effects | Missing error termination |
| Roles | Lane accurately represents responsible participant | External service wrongly owned by internal team |
| Gateway | Guarded, mutually meaningful alternatives | Two anonymous arrows from a decision |
| Data | Branches reflect current BR and error rules | Invalid retry threshold invented |
| Reachability | Every allowed path has a valid continuation or end | Orphaned exception path |
| XML | Independent parser imports and preserves identities | Dangling flow reference |
| DI | Actual modeler displays readable flow | Crossing connectors and clipped titles |
| Runtime | Deployment tested independently | Parser success claimed as execution |

This method prioritizes true process semantics over document volume or attractive but unverified drawings. Do not claim editors, native Figma writes, or BPMN automation from instructions alone.
