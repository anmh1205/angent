# ANGENT interfaces — minimal handoff contract

ANGENT skills share one working context. This is a semantic checklist for **real boundaries** (delegation, effect, long-lived task, accepted revision), not a mandatory set of YAML objects, a universal protocol or a sequence of owner invocations.

The receiving skill needs only the material fields it cannot safely reconstruct. Omitting irrelevant fields is correct.

## Core information carried across boundaries

| Concern | Minimum when material | Responsible skill |
| --- | --- | --- |
| TaskModel | Requested outcome, active constraints, current effect authority, completion evidence | Contract |
| CollaborationState / StateDelta | Relevant current instruction, baseline, provenance, history, uncertainty and applicable working mode | Context |
| Decision basis | Decisive premise/evidence, selected direction, dependency, reconsideration trigger | Reasoning |
| EvidenceQuery | Unresolved decision, plausible alternatives, evidence that would discriminate | Reasoning to Research |
| EvidenceDelta | What was observed or source-established, what was inferred, boundary and remaining unknowns | Research |
| ActionNode | Authorized operation and target, relevant preconditions, mutation basis if needed, success observation | Reasoning to Execution |
| ObservationDelta | Actual target/result/failure boundary, what changed, completeness, uncertainty and next useful action | Execution |
| SolutionModel | Established objects/relationships/mechanisms, reader job and evidence limits | Reasoning to Authoring |
| ArtifactCandidate | Content plus protected baseline, reader capability and coverage evidence if relevant | Authoring |
| QualityVerdict | PASS, FAIL or BLOCKED, supporting evidence, affected dependency, repair responsibility | Quality |
| PromotedMechanism | Failure/decision class, causal mechanism, applicability limit, supporting and disconfirming evidence | Learning |
| Frontier | Work identity, completed/unfinished branches, blockers/wait handles, source/baseline pointers, next safe work | Continuity |

Other fields are optional, never mandatory ceremony. Do not create records for owners that are not participating.

## Important exceptional cases

**Consequential effect:** The concrete operation, resolved target and material arguments must still match active authority at invocation. For an existing-state write, compare against the version or state on which the proposed delta depends. An ambiguous effect requires PREPARED / ATTEMPTED_UNKNOWN / reconciliation semantics; a write acknowledgement is not a verified endpoint.

**External operation still running:** Preserve branch ID, operation handle, WAITING_EXTERNAL status, dependencies and next informative observation condition. Reasoning chooses other runnable work before a similar status check. Do not model a background scheduler that the host does not provide.

**Revision / RepairModel:** Preserve the accepted baseline, observed failure, inferred generating mechanism, affected scope, protected properties and acceptance evidence. A repair may reopen upstream understanding rather than only change the quoted example.

**ReaderProgressDelta:** For a multi-unit teaching artifact, distinguish PREVIEWED, INTRODUCED, USABLE and FRAGILE concepts. An accepted capability needs supporting explanation/representative inference and, when required, Quality and destination evidence; topic mention and completed pages are insufficient.

**DelegationEnvelope / SpecialistReturn:** Bound the delegated question, access/effect scope and necessary context. On return, retain source/uncertainty and effects attempted; a specialist report is not independent confirmation.

**Resume binding:** Preserve only the identities, source/baseline versions, effect handles and dependency assumptions whose drift changes safe continuation. Classify COMPATIBLE, REVALIDATE, AMBIGUOUS or INCOMPATIBLE. Ambiguous/incompatible mappings block only dependent replay, not unrelated work.

**Quality verdict:** Evidence must support its scope and the evaluation must be valid. A required FAIL/BLOCKED prevents dependent acceptance; do not turn reviewer confidence or self-report into endpoint proof.

These checks are activated by the decision type, not by a fixed sequence of all skills. Deeper owner-specific procedures remain in their own references.
