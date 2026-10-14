# ANGENT architecture

ANGENT is a compact cognitive layer for agents. It helps retain the user's objective and constraints, reason from evidence, perform authorized work, verify the outcome, recover unfinished work and learn from meaningful feedback.

## One context, optional skills

The agent does not need to instantiate a new worker, workflow or persistent object for each skill. Root selects a responsibility only when the current decision benefits from it:

- **Understand:** Contract captures outcome/authority; Context retrieves only relevant history, project state and obligations.
- **Decide:** Reasoning integrates evidence and dependencies; Research resolves unknown facts or mechanisms when necessary.
- **Act or explain:** Execution performs and observes tool actions; Authoring writes for the reader; Format preserves the destination's actual representation.
- **Check:** Quality evaluates material outcomes and revisions against evidence and accepted properties.
- **Resume or improve:** Continuity preserves only unreconstructable unfinished work; Learning saves reusable, conditional causes and working methods.

A straightforward question may use one skill. Complex work can revisit a skill when observations change the model. This is not a mandatory phase order or a multi-agent orchestration service.

## Boundaries that protect correctness

**Authority:** Saved plans, memory and provider content never grant permission. For material external effects, confirm current authorization against the actual operation, target and arguments immediately before calling the tool.

**Evidence:** Distinguish directly observed state from inference, uncertainty, stale context and failures of the tool path. A citation, search miss, truncated result or agent self-report supports only the claim its observation boundary permits.

**Existing state:** Read a relevant live baseline before changing it. A concurrent change may require revising the affected delta. Do not overwrite unrelated work from an obsolete read.

**Pending work:** A running external call is one waiting branch. Keep its operation identity and next meaningful observation condition, then choose independent useful work before polling again. This is a planning rule; the host remains responsible for actually executing calls.

**Revision:** Preserve accepted strengths, infer the shared cause of repeated failures and repair the affected dependency closure. A user example is not automatically the whole defect or a mandate to optimize its opposite.

**Teaching:** Preserve established causal and dependency relationships across Research, Reasoning and Authoring. Choose depth from the reader's current capability and desired next inference. Explain naturally; do not dump a fact inventory into a document.

**Acceptance:** Quality is independent judgment when warranted by consequence, recurrence, propagation or accepted baselines. A valid PASS relies on evidence at the right scope; blocked dependent transitions do not prevent independent work.

## Storage

Durable task state, memory and Learning are separate semantic classes:

- Project instructions: applicable AGENTS.md files.
- Active constraints: the current task's Contract.
- Current model, decisions and evidence: working context.
- Long-lived facts: scoped Memory.
- Conditional causal lessons: Learning.
- Unfinished tasks and uncertain effects: Continuity.
- Reader/curriculum progress: the artifact's own state.

These classes need not become separate services. A harness may use native facilities or the small local storage scripts. Store dynamic work state outside tracked source files. At resume, reconcile affected saved facts with current authority and provider state before dependent actions.

## Harness contract

ANGENT defines what a correct decision requires, not a scheduler, storage service, transaction engine, evaluator platform or second agent runtime.

The harness provides the capabilities actually available: tools, provider observations, skill loading, history retrieval, durable storage and optional delegated work. Missing capabilities are reported honestly, not simulated. The same core skill files should remain usable across chat and local agents.

See skills/angent/references/harness-contract.md for conditional adapter details and skills/angent/references/interface-contracts.md for the minimal handoff vocabulary. Specialized decision rules stay with their owning skill.

## Package identity

Plugin manifests hold package metadata. The Git repository holds source history. Runtime provider identifiers and live task checkpoints are obtained from the relevant runtime/store when needed, not copied into documentation or committed source.
