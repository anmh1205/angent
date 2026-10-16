---
name: figma-bpmn
description: Specialized bpmn analysis and editable Figma presentation when actual host tools permit.
---

# BPMN 2.0.2 model and editable Figma process visualization

## What BPMN means
A BPMN process models operational work, decisions, events, collaborations and their consequences. A Figma drawing is a visualization; an importable BPMN 2.0 XML model carries process semantics. Do not confuse image quality with Camunda/Bizagi importability or execution compatibility.

## Required source model
Specify process ID, pools/participants, lanes and owners, start events, task types, exclusive/parallel/inclusive gateways, intermediate events, end events, sequence flows, message flows across pools, data objects and exception handling. For every gateway define its decision semantics; for split concurrency supply a justified join or explain deliberately independent branches.

## Generation and review
1. Extract the accepted process and actor interactions from BA SRS and use case; record every success and recovery path, deadline and compensation requirement.
2. Normalize the semantic model: valid node types, unique IDs, actor ownership, branch guards, event/message correlation, correlation keys and permissible terminal states.
3. Run reachability checks before layout. A process with a missing end, orphan gateway branch or unhandled error event is not complete, however elegant its diagram.
4. Generate BPMN 2.0 XML using an actual compliant writer. Validate well-formedness and schema against the normative OMG XSD; import with a compatible modeler for interoperability evidence. BPMN XML without BPMNDI coordinates may import but will not have a useful layout.
5. For a separate Figma visualization, map the validated model to editable pools, lanes, tasks, events, gateways and connectors. Only use native tools that exist in the host. Reqwise OSS does NOT support BPMN as one of its six figma_diagram kinds.
6. Read back the edited Figma canvas and compare node/edge inventory, lane ownership and layout against the semantic model. Report independent XML and Figma verification results.

## Distinctions to preserve
Sequence flow does not cross pools; message flow connects participating pools. A gateway does not represent the approval task itself. A timer boundary event and a timer in the normal task flow do different things. End event semantics must match the intended interruption or completion.

## Implemented BA XML handoff

For acyclic single-process models using start/end tasks and exclusive gateway branches, the BA extension provides a real BPMN XML+DI compiler at extensions/angent-ba/scripts/build_bpmn.py, with fixture extensions/angent-ba/examples/atlas-re/bpmn/claim-approval.ir.json. Treat this as a semantic file-generation stage, NOT as editable Figma canvas output. Require a live authorized Figma tool, native object creation, read-back, and layout inspection before claiming a Figma mutation. For collaboration, loops, parallelism or timers, the portable compiler intentionally fails; use a verified advanced renderer or report unsupported scope.

## Deliverables
One semantic BPMN IR, BPMN 2.0 XML with validation evidence when generated, editable Figma diagram when supported, and a source-to-node traceability table. Never claim executable process automation without verified engine/runtime behavior.

## Standard
OMG BPMN 2.0.2: https://www.omg.org/spec/BPMN/2.0.2/


## ANGENT authority

Root selects capabilities; BA owns source business decisions, Frontend supports art direction when necessary, Execution performs authorized Figma calls and read-back, Quality verifies semantics and rendering.
