# Google ADK runtime contracts (pinned 2.19.0 semantics)

These are workflow/architecture invariants, not copy-paste API signatures for newer releases.

- **Entrypoint:** package imports agent module and exposes `root_agent` or `app` according to installed ADK discovery rules.
- **Model-driven:** LlmAgent/Agent selects tools/subagents under explicit instruction and permission boundaries.
- **Ordered:** SequentialAgent passes correct completed state to the next step; a failed prerequisite must stop or use a specified recovery.
- **Concurrent:** ParallelAgent needs independent state ownership or a deterministic conflict resolution boundary.
- **Loop:** LoopAgent must have termination, iteration budget and recovery.
- **Remote:** RemoteA2aAgent introduces identity, authentication, transport, version and network-failure constraints.
- **State:** per-session ToolContext state is distinct from persisted memory, shared cache and artifacts. Specify tenant keys, lifecycle and cleanup.
- **Tools:** MCP connection, typed arguments, retry/idempotency, user approval, timeout/cancellation and consistent result types.
- **App and plugin:** plugin/event compaction/callbacks are lifecycle extension surfaces; verify observability without leaking raw private prompts or credentials.
- **Evaluation:** user goal success, tool arguments/routing, errors, denial, session/tenant separation, artifact persistence and measured latency/cost where relevant.
- **Deployment:** after approved rollout check real serving endpoint, logs, environment permissions, health and rollback path.
