---
name: ak-problem-solving
description: Apply targeted problem-solving techniques when ordinary reasoning is stuck, overcomplicated or constrained by a bad assumption.
metadata: {port: angent-fallback, mode: portable}
---

# Problem Solving — Portable Fallback

Read `references/technique-selection.md`.

This is a toolbox, not a mandatory sequence.

## Trigger

Use only when ordinary Reasoning shows a specific failure pattern such as:
- growing special cases;
- repeated local fixes with no system improvement;
- one untested assumption constraining all options;
- uncertainty about extreme scale or boundary behavior;
- a claim that needs a counterexample;
- a problem decomposed by the wrong ownership/state boundary.

## Workflow

1. Name the stuckness.
2. Choose one technique whose mechanism fits it.
3. Reframe or probe the model.
4. Compare the new model with the previous one.
5. Return only changes that improve explanatory or decision power.

Do not create a separate agent for every thinking method.

If normal Reasoning is making progress, do not invoke this Skill ceremonially.
