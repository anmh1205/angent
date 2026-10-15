# Failure routing

## Quick/direct

Appropriate when:
- defect mechanism is deterministic and established;
- owner is known;
- change is local/low-risk;
- verification is straightforward.

Quick still performs a bounded scout and diagnosis. It removes ceremony, not causality.

## Standard

Use when:
- repair spans multiple files/consumers;
- blast radius needs explicit verification;
- one cause/direction is established.

Keep one repair contract, implement the causal scope, then verify affected consumers.

## Debug first

Required when:
- several causes remain plausible;
- failure is intermittent/environment-specific;
- state crosses layers;
- previous fixes failed;
- the suspected fix does not explain the symptom.

## Deep / Reasoning / Plan

Required when the "fix" is actually:
- an architecture/public-contract/product decision;
- a migration requiring staged compatibility;
- a repair with several materially different valid approaches;
- a recurrent failure indicating the controlling model is wrong.

Do not let Fix make a hidden design decision just to keep the workflow moving.

## Parallel

Use only for:
- several independent failures;
- disjoint repair branches/evidence sources;
- ownership that can be isolated.

Do not parallelize competing fixes for one unresolved causal mechanism and then choose by whichever finishes first.

## Advisory mode

An advisor can pressure-test diagnosis/repair at high-risk or stuck points.

Advice is evidence/proposal. The Fix owner remains responsible for decisions, edits and verification.

## Non-convergence

Repeated failed attempts trigger re-diagnosis/re-modeling.

The pinned upstream uses a three-attempt stop gate. Portable ANGENT preserves the **non-convergence invariant** rather than using a blind counter when attempts are not equivalent. If multiple cause-aligned attempts fail without improving the causal model, stop local patching and escalate.
