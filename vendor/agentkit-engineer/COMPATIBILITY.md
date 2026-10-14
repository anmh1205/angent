# Engineer fallback compatibility routes

This file preserves migration guidance for upstream Engineer identities that remain discoverable in old conversations/bookmarks but are **not current packaged public Skills**.

Canonical current inventory is `STABLE_CATALOG.json`.

## Retired routes

| Retired identity | Current route |
|---|---|
| `ak-security-scan` | `ak-security` with the appropriate scan/audit mode |
| `ak-use-mcp` | Use the active harness's connected MCP discovery/invocation for existing tools; use `ak-mcp-builder` for MCP servers, `ak-webmcp` for page tools, or `ak-agent-browser` for browser automation |
| `ak-handover` | `ak-handoff` for continuation state; `ak-orchestrate` or `ak-team` only when actual coordination is required |
| `ak-html-video` | `ak-hyperframes`, `ak-media-processing`, or `ak-remotion` according to the artifact/toolchain |
| `ak-sequential-thinking` | `ak-fable-thinking` for the packaged reasoning workflow; ANGENT Reasoning remains strategic owner |
| `ak-web-design-guidelines` | `ak-ui-ux-pro-max` or `ak-frontend-design` according to review vs implementation intent |

Do not keep these retired names under the public `skills/` discovery root merely to preserve old invocations. That would make the fallback catalog differ from the current stable package.

## Upstream documentation inconsistency

The current stable Engineer catalog marks `ak-use-mcp` retired, while some individual Skill pages may still mention it as a route for running existing MCP tools.

For fallback parity, package composition wins: do not expose `ak-use-mcp` as a public Skill. Existing connected MCP tools belong to the active harness/provider surface and should be discovered live rather than reconstructed from a retired Skill identity.

## Internal support

`ak-common` was never a user workflow. Its shared fallback conventions now live under `internal/common-conventions.md` so public Skill counts/identities are not distorted.
