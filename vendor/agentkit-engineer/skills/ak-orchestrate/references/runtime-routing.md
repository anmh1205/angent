# Orchestration runtime routing

Build a live inventory before dispatch.

For each candidate runtime/agent, verify only what matters for the job:
- callable/available now;
- authentication/session usable where required;
- read/write/tool capability;
- cwd/worktree support;
- timeout/cancellation behavior;
- isolation/permission controls;
- model/agent identity when materially relevant.

Do not route to a remembered runtime or carry flags/model names from another runtime.

If a candidate is missing, unauthenticated or too weak for the risk/capability requirement, try a qualified fallback.

If no route meets the requirement, block that job rather than silently weakening the requirement.

## Selection

Choose based on:
- task capability;
- risk/effect boundary;
- context needs;
- isolation needs;
- latency/cost only after capability and safety floors are met.

Metrics can inform future choices but do not automatically rewrite routing policy.
