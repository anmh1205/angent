# Curriculum progression and reader capability transitions

Use when a teaching artifact contains multiple units whose knowledge depends on earlier units. A simple explanation, reference page, or overview does not need this ledger.

## Separate knowledge, admission and demonstrated affordance

The complete technical model may be rich. The current unit has a narrower capability obligation, but its selected mechanism must be explained fully enough for the promised inference. Classify each concept at the **precision relevant to that obligation**:

- **PREVIEWED** — the name/purpose is recognizable; no downstream technical inference is licensed.
- **INTRODUCED** — the object and immediate role are defined; interactions requiring an unstated mechanism are not yet licensed.
- **USABLE** — the artifact gives the necessary mechanism and at least one inspectable inference, trace, application, contrast or diagnosis at the promised level.
- **FRAGILE** — earlier exposure is insufficient for a new context; repair the missing relation before depending on it.
- **UNKNOWN** — canonical accepted material cannot establish the state.

These are artifact-supported reader capability *affordances*, not measurements of actual individual learning. Do not turn a self-reported chapter status, word count, a glossary mention, or diagram presence into USABLE.

## Before composing a unit

Recover the last accepted reader state and the next target capability. Identify the single dominant mechanism/interaction that lets the reader perform the new inference. Derive its true prerequisite relations from the evidence-grounded subject model. Choose explicitly:

1. what prerequisite is already USABLE at sufficient precision;
2. which FRAGILE or INTRODUCED relation must be repaired or established now;
3. which advanced branch can be deferred without hiding the active mechanism;
4. which deeper precision a later unit will need, and which downstream unit depends on it.

A recurring project/example is an observation surface, not a replacement for the general object/interface model. Keep the same referent through the active trace, then generalize its boundary. If explaining the current mechanism would require simultaneous introduction of several independent expert graphs, adjust the unit boundary/curriculum allocation instead of merely shortening sentences or adding a giant diagram.

## After composing

Propose a small ReaderProgressDelta: capability before/target, active mechanism, concept transitions, evidence/probe within the artifact, unmet prerequisite debt, deferred depth and dependent units. Quality checks whether the provided explanation actually makes the claimed inference possible using established prerequisites. Only then may required accepted state advance; external rendering is checked independently by Format/Execution.

When a prior concept is revised, invalidate only the later capability claims that consume the changed relation. A local wording change that does not change that relation should not invalidate the whole book.

## Failure and counter-cases

Failure: an early chapter defines "process", a later chapter presumes address-space scheduling and synchronization internals were already learned, and Quality passes because both headings exist. Repair the prerequisite allocation and affected dependencies, not the document's tone alone.

Counter-case: a chapter introducing the Linux userspace/kernel boundary may legitimately preview scheduler details while fully explaining what a system call changes. Do not force it to teach scheduling internals before the first usable system-call inference.

Another counter-case: a dense advanced unit can assume earlier verified prerequisites and be compact, provided it still explains the *new* mechanism at the level promised. More length is not inherently better.

Use Root `references/core-fixtures.md` for the paired MCP2515 and unseen-transfer calibration; do not memorize those examples as templates.
