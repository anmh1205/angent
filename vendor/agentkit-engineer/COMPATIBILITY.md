# Engineer fallback compatibility routes

This file preserves migration guidance for upstream Engineer identities that remain discoverable in old conversations/bookmarks but are **not current packaged public Skills**.

Canonical fallback target inventory is `STABLE_CATALOG.json`. It represents the documented stable public workflow contract, not an exact mirror of the current registry portable export.

## Retired routes

| Retired identity | Current route |
|---|---|
| `ak-security-scan` | `ak-security` with the appropriate scan/audit mode |
| `ak-use-mcp` | Use the active harness's connected MCP discovery/invocation for existing tools; use `ak-mcp-builder` for MCP servers, `ak-webmcp` for page tools, or `ak-agent-browser` for browser automation |
| `ak-handover` | `ak-handoff` for continuation state; `ak-orchestrate` or `ak-team` only when actual coordination is required |
| `ak-html-video` | `ak-hyperframes`, `ak-media-processing`, or `ak-remotion` according to the artifact/toolchain |
| `ak-sequential-thinking` | `ak-fable-thinking` for the packaged reasoning workflow; ANGENT Reasoning remains strategic owner |
| `ak-web-design-guidelines` | `ak-ui-ux-pro-max` or `ak-frontend-design` according to review vs implementation intent |

Do not keep these retired names under the public `skills/` discovery root merely to preserve old invocations. The documented stable contract treats them as retired routes rather than current public workflows.

## Upstream drift and documentation inconsistency

Stable documentation marks `ak-use-mcp` retired, while some current individual Skill guides still mention it as a route for running existing MCP tools. The current stable CLI 2.19.0 portable export also still contains the legacy 102-identity set, including retired names.

ANGENT therefore separates two facts:

- the **documented public workflow contract** is the fallback semantic target;
- the **observed registry portable export** is provenance about upstream delivery state, not the fallback's identity authority.

Do not expose `ak-use-mcp` as a fallback public Skill. Existing connected MCP tools belong to the active harness/provider surface and should be discovered live rather than reconstructed from a retired workflow identity.

## Internal support

`ak-common` was never a user workflow. Its shared fallback conventions now live under `internal/common-conventions.md` so public Skill counts/identities are not distorted.
