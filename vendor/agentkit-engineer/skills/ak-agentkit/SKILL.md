---
name: ak-agentkit
description: Route a multi-step or ambiguous engineering request to the smallest useful combination of Engineer Skills and Agents.
metadata: {port: angent-fallback, mode: adapted}
---

# Engineer Router — Portable Fallback

This Skill provides Engineer routing when native AgentKit is unavailable.

It does not replace ANGENT Root or Reasoning.

Read `references/routing-protocol.md` for the full selection/delegation policy.

## Core rule

Use the **smallest workflow that preserves quality**.

Do not build a chain merely because several Skills exist.

## Typical routes

- unclear ownership → Scout → Plan or Debug;
- bug → Scout if needed → Debug → Fix/Cook → Test → Code Review;
- feature → Research/Brainstorm if needed → Plan → Cook → Test → Code Review;
- PR → Review PR / Code Review;
- long continuation → Continuity/Handoff;
- independent parallel jobs → Orchestrate or Team only when parallelism/isolation is worth its coordination cost.

## Native boundary

If native AgentKit Engineer is actually usable in the active environment, prefer it instead of loading the fallback library.

## Output

Return the selected route only when route visibility helps the user or downstream workflow. Do not add routing narration to trivial tasks.
