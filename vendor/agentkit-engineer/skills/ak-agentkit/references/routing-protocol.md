# Engineer routing protocol

## 1. Proportionality

Before routing:

- user named a Skill → use it unless impossible/unsafe;
- one obvious single-domain operation → use one Skill;
- factual/conversational request → no engineering chain;
- multi-step, ambiguous, cross-domain, high-risk, or capability-unclear task → route deliberately.

Routing overhead is itself a cost.

## 2. Inventory actual capability

Do not route from memory alone.

Check what is really available now:
- native AgentKit Engineer, if usable;
- ANGENT fallback Skills/Agents;
- harness-native tools/agents;
- connected provider/plugin capabilities.

A cached file or remembered tool name is not proof the capability is callable. Conversely, a missing `ak` executable is not evidence that an Engineer **working method** is unavailable: Skills teach the agent to inspect, plan, analyze, review and coordinate using whatever real tools the current harness offers.

When a user mentions an `ak` verb, extract the intended outcome and its reasoning obligations rather than dispatching one-to-one to a simulated CLI. Load `outcome-routing.md` for task-level decisions. `ak-ak` is reserved for actual AgentKit product administration.

If a needed capability is absent:
- choose a semantically adequate replacement when the owning workflow allows degradation;
- execute inline/sequentially if safe and semantically equivalent enough;
- otherwise report the exact gap.

Do not degrade a workflow past its load-bearing capability boundary. In particular, `ak-team` requires a live team lifecycle; ordinary subagents/sequential roles belong to Orchestrate/Cook rather than being mislabeled as Team.

## 3. Skill chaining

Prefer domain-specific Skill for domain knowledge and workflow Skill for execution structure.

Each link should have:
- a real prerequisite relationship;
- a clear output consumed by the next link;
- an exit condition.

Collapse adjacent links that add no independent evidence or capability.

## 4. Delegation

Delegate only when one of these is useful:
- fresh context isolation;
- specialist instruction;
- parallel wall-clock reduction;
- independent review;
- tool/permission boundary.

Good triggers include:
- broad investigation with separable areas;
- material implementation needing independent test/review;
- distinct disjoint work units;
- repeated failure that benefits from a fresh debugger view.

Do not spawn an agent for trivial edits or when the full current context is essential.

Choose the workflow by collaboration semantics:
- persistent teammates/shared messaging → Team, only if lifecycle is actually available;
- independent jobs/headless CLIs/one-shot workers → Orchestrate;
- one coherent implementation owner → Cook.

## 5. Risk-based verification

Verification scales with consequence:

- low/reversible → owning Skill checks may be enough;
- user-visible/cross-module → targeted test + review of changed behavior;
- security/data/money/public contract/destructive → stronger independent review and explicit authority before irreversible effects.

Do not convert these into rigid ceremony when the actual consequence is low.

## 6. Failure handling

A failed link does not advance the chain.

After failure:
1. preserve the observation;
2. determine whether input/context, capability, or model/plan was wrong;
3. reroute only when new evidence justifies it;
4. do not resend the same failing request unchanged;
5. return to Reasoning when the failure invalidates the plan.

Do not stop merely because one specialist failed if a safe semantically valid alternate route exists.
