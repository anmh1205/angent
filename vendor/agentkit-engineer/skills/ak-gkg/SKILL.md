---
name: ak-gkg
description: Use a verified GitLab Knowledge Graph index for definition, reference and impact queries, with explicit limitations and source-backed fallback search.
metadata: {port: angent-fallback, mode: degraded}
---

# GitLab Knowledge Graph (GKG) — Portable Fallback

Stable Engineer 2.19.0 routes semantic code navigation to GitLab Knowledge Graph (GKG), a separate beta AST/index/graph runtime. It is distinct from Graphify's broader multimodal/concept graph and from a plain repository snapshot. Select GKG for **definition, usage and impact analysis** in code before refactors or architecture changes.

## Native runtime decision

Confirm an actual Git repository, installed GKG binary and current help/version. The stable package documents **gkg --version**, **gkg index** and **gkg server start/stop**; its persisted data was under ~/.gkg/ and its HTTP/MCP endpoint used port 27495. Do not presume these commands/endpoints still apply to a different installed release.

Indexing, deleting an index, starting an API/MCP server, downloading an installer or exposing source through a service are **real effects** requiring authorization and privacy consideration. Do not execute upstream curl/PowerShell installer scripts merely because the stable Skill lists them. Upstream specifically requires stopping the server before reindexing; verify the actual installed runtime's concurrency behavior.

### Semantic queries

1. Select repository/revision, language and target symbol or code interaction.
2. Index or refresh the authorized project with actual native GKG tools, if installed and approved.
3. Locate symbol definition (including fully qualified name and source location).
4. Ask for all usages/references across relevant files and, when the runtime supports it, across indexed projects.
5. For impact analysis, classify direct callers, transitive consumers, write/state effects and external contracts; verify the relevant call sites in source.
6. Re-query after code changes to detect stale graph information. Report actual index freshness and language capabilities.

Stable upstream MCP exposes roles equivalent to **list_projects**, **search_codebase_definitions**, **index_project**, **get_references**, **read_definitions**, **get_definition** and **repo_map**. Do not advertise these as live tools until the server and actual connector report them. HTTP search and MCP calls are runtime-specific; discover the real schema before invocation.

## Support limitations

The pinned stable package gives stronger cross-file reference support for Ruby, Java and Kotlin; it describes Python, TypeScript and JavaScript cross-file resolution as incomplete. Current installed GKG may differ. Verify supported languages, symbol kinds, dynamic dispatch, generated code and cross-repository edges before claiming complete usages. Absence from a partial index is **not proof** of no callers.

## Portable fallback

Without native GKG:
- Prefer actual language-server/indexer go-to-definition/reference APIs when available.
- Then use parser/AST/symbol-aware tools for imports, definitions and callers.
- Use bounded text search with manual source/control-flow tracing only as a lower-confidence fallback.

For each consequential conclusion include path, symbol, source line and search boundary, plus what may be missed (runtime reflection, dynamic dispatch, vendor/generated code, unsupported languages). When changes affect public APIs, trace tests and runtime consumers as well as internal references.

## Output

Return the question, repository/ref and index/search method; definitions and observed usages; likely impact set; links to source; language/index freshness limitations; follow-up probes. Do not claim a semantic graph or full-repository completeness from grep output. For a simple repo snapshot or remote code context, Repomix/search may be more economical.

The lack of native GKG is a real capability degradation, not an excuse to fabricate semantic-index results.
