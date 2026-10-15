---
name: ak-predict
description: Pre-analyze risky changes through five separated expert lenses, reconcile worst-case conflicts and issue a GO/CAUTION/STOP advisory verdict with optional reason/probe follow-up.
metadata: {port: angent-fallback, mode: adapted}
---

# Predict — Portable Fallback

Use before major features, architecture shifts, difficult refactors and high-impact security/performance/product decisions where a cheap pre-mortem can prevent expensive implementation errors. Not for trivial changes or stable work with no open decision. Stable Engineer 2.19.0 includes **five named perspectives**, explicit consensus/debate and two chained modes; losing those would change the workflow.

## Five perspectives

1. **Architect** — interfaces, coupling, system constraints, scale, migration and failure domains.
2. **Security** — abuse, authorization, privacy/data exposure, secrets, trust boundaries.
3. **Performance** — latency, memory, N+1 queries, throughput, resource/cost growth.
4. **UX** — human workflow, accessibility, errors, state feedback, device and recovery experience.
5. **Devil's Advocate** — whether to do nothing, simpler alternatives, which load-bearing assumption could collapse the proposal, and cost of reversing it.

Present only applicable details within each lens, but evaluate all five explicitly when the user invokes the stable Predict workflow. If the host supports actual independent delegated evaluations, use the appropriate real runtime; if one model evaluates lenses sequentially, say so and **do not pretend they independently debated**.

## Procedure

1. Establish the exact proposal, current code/system state, user outcome, constraints and the stage of approval. Read affected paths/tests when supplied; verify load-bearing facts against source.
2. Develop initial lens findings independently where host capabilities permit; otherwise keep provisional lens-specific notes before synthesizing to reduce premature consensus.
3. Separate points of genuine agreement from material conflicts. Look at **worst plausible consequences** (authorization bypass, data loss, irreversible migration, unacceptable load), not only average-case optimization.
4. Resolve each conflict by evidence, harm severity, reversibility, cost and mitigations. Do not average a critical security concern into four low-risk votes.
5. Produce actionable mitigations, probes/early signals, owners and an advisory verdict:
   - **GO** — no material unresolved blocker; adequate evidence.
   - **CAUTION** — specific manageable risks remain with required gates.
   - **STOP** — a credible unresolved critical defect, design incompatibility or false central assumption invalidates proceeding safely.
6. Make assumptions and unknown evidence explicit. A STOP finding prevents a **dependent risk acceptance** in this advisory model, not arbitrary user authority. ANGENT Reasoning/authorized owner decides next action.

## Chained modes

- **--chain reason**: when subjective architectural/design trade-offs still make CAUTION plausible, generate alternatives, critique separately, synthesize, re-evaluate and converge only with a defendable criterion. No endless 'more thinking' loop.
- **--chain probe**: when missing requirements/constraints explain CAUTION or STOP, formulate the minimum high-value questions or low-cost observations, gather/confirm user-owned answers through real available interaction, then re-evaluate. Do not assume AskUserQuestion/agent relay exists.

These are follow-ons to Predict, not independent installed skills in the pinned package. Chain only when invoked/requested and the active runtime can support the required interactions.

## Output

Return proposal/scope; overall verdict; five lens findings; agreements; conflicts and resolution evidence; risks with impact/severity, early observable signals and mitigations; ranked actions; unresolved assumptions and confidence; any chain result. For serious choices, pass material risks to Plan or Scenario as acceptance constraints.

Do not implement changes or manufacture independent subagent votes. A polished table is not evidence that a risk was tested.
