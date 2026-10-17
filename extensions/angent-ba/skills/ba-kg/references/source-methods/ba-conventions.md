# Common business-analysis content conventions

**Provenance:** Adapted from MIT Dev BA Kit / rules/ba-conventions.md (Edward Ngo, 2026), https://github.com/nv-minh/dev-ba-kit. Methods are portable; no host-specific hooks or runtime variables are required.

## Write for the reader and the business decision

A user need states an observed or accepted problem in its working context. A business objective states the result sought. A capability describes product support for that objective. An FR states a testable behavior; an NFR gives an observable quality threshold, workload and measuring method; a BR describes an enforceable policy with owner, scope and exceptions.

Avoid conversational notes, explanatory filler and template instructions in the final accepted artifact. Preserve enough why/source context to explain a decision, but do not fill every optional template field merely because it exists.

## Evidence types

Keep accepted stakeholder decision, proposal, direct code observation, runtime observation and inference distinct. A vendor page does not establish a customer's need; a source-code branch does not establish deployed behavior; a passed mock test does not establish production compliance.

Use exact source paths, IDs, timestamps or provider revisions for important claims. If a rule threshold is unsettled, mark it open rather than invent a default. Compare current sources before asking the user something already answered.

## IDs, scope and updates

Retain existing project IDs and naming conventions. Introduce only the next needed IDs from accepted sources. Relationships between UN, BO, CAP, FR, AC, CHK and TC must point to real inspected artifacts; never create evidence nodes to improve structural coverage.

When updating, inspect the current file and propose changes to affected sections. Preserve glossary, human decisions, citations and unrelated content. A neat rewrite that loses business constraints is a regression.

## Language and detail

Follow the user's requested language and the accepted document's terminology. Keep technical identifiers exactly as used by code/API; explain jargon when needed for the intended audience. Use code-level detail when it is necessary for testability or implementation, not to turn a business requirement into an unrelated architecture proposal.

## Completion

Check semantic contradictions, actor ownership, failure paths, security/privacy obligations, source linkage and reader usability. Validation tools can report structural errors, but only actual stakeholders and verified behavior can confirm business correctness.
