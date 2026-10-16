# BPMN process model — ANGENT portable input and verification

This is a **bounded BPMN 2.0** source model for an observed or accepted business process, not a general-purpose workflow engine. The ANGENT compiler implements one **non-executable acyclic process**, task nodes, start/end events, exclusive split/join gateways and optional lanes. Loops, parallel forks, timers, compensations, subprocesses and cross-pool messages are not currently supported.

## Evidence prerequisites

- Accepted SRS/BRD or use-case source/revision: {{actual_source}}
- Actors and business owners: {{source_backed_actors}}
- Complete decision table, including guards and alternatives: {{accepted_decisions}}
- Required exception, cancellation or retry semantics: {{required_behavior_or_explicitly_unmodeled}}

If a required behavior needs unsupported BPMN semantics, stop and report the gap; do not substitute a superficially similar shape and claim the process is equivalent.

## Source IR

Use the compiler's existing input structure with process (id/title), optional lanes (id/name), nodes (id/kind/name/optional lane) and flows (id/src/tgt/optional name). Node kinds: start, end, task and gateway. For diverging exclusive gateways, every outgoing branch needs a **distinct nonempty name**.

Reference a complete, compiled fixture rather than an incomplete JSON-with-comments snippet:

    extensions/angent-ba/examples/atlas-re/bpmn/claim-approval.ir.json

Make a reviewed copy with stable process, lane, node and flow IDs and actual source-backed transitions. The compiler validates one start, reachable termination, branch guards, globally unique identifiers and no cycles.

## Executable verification

Check the concrete IR without writing a BPMN file:

    python extensions/angent-ba/scripts/build_bpmn.py INPUT.ir.json --check

Generate BPMN XML and basic diagram interchange:

    python extensions/angent-ba/scripts/build_bpmn.py INPUT.ir.json --output OUTPUT.bpmn

For a test environment containing **original OMG normative XSD files**, check true BPMN schema compliance:

    python tests/integration/check_bpmn_official_xsd.py --schema-dir PATH_TO_OFFICIAL_XSD

The last integration test validates the included Atlas fixture; it does not automatically validate arbitrary OUTPUT.bpmn. Validate each project result separately against the normative schema when required.

## Acceptance

Record the inspected IR, accepted process revision, actual compiler exit status, evidence for each branch, generated XML file, rendered image/modeler inspection if available and unsupported behavior. XML parsing or XSD validation alone is not proof that the process can be imported, executed or faithfully rendered in a particular BPMN product.

No Claude-specific scripts, auto-generation of viewer.html, hidden semcheck or fixed .claude paths are available or required.
