# Journal lifecycle without AgentKit

Native AgentKit 2.19.0 `ak journal create` writes a collision-safe dated Markdown file in the configured project plan/journals store; `list`, `show`, `validate` inspect that store. All four are **file/document workflows**, so use the actual project's connected file/editor capability and a suitable existing journal directory. There is no need for the `ak` binary.

## Author and persist

1. Resolve actual authorized project and existing journal location. Prefer the project's configured path; otherwise use `plans/journals/` under the approved project root. Do not infer a local path from a remote-only GitHub repo.
2. For `create`, form a date plus short safe slug and, on collision, choose a new suffix instead of overwriting. Use the user's time/date when specified, otherwise the active environment's current local date. Ensure body/frontmatter agree with the date and title.
3. A journal entry is a human-readable chronological account: context, work attempted, observed results (including failure), evidence links, important decisions and unfinished follow-up. Preserve source and version identity; redact secrets and third-party personal data.
4. Write once with a real tool, then **read back** the document/URL/path. If a provider write is ambiguous, reconcile before retrying or risk duplicate entries.
5. For `list` and `show`, inspect existing entries without creating anything; newest first only when dates are verified. For `validate`, check date/title/frontmatter and consistency of evidence, report defects without mutating entries.

## Ownership and policy

Journal ≠ Continuity frontier ≠ persistent memory ≠ promoted Learning. A log entry never updates active state or overrides current instructions by itself.

An explicit user request to write a journal authorizes that journal scope; automatic post-task journaling uses current project/user preferences when known, otherwise avoid generating irrelevant entries. Social publication needs a separately authorized account and provider and is **not** part of `create`. A local Markdown file is not a published post.

## Acceptance cases

- Multiple entries on the same day with the same title must retain both histories rather than silently overwrite.
- A history-only `show` or `list` request must not add new journal files, try to install `ak` or create a project registry.
- An entry after a failed deployment must describe the failure and rollback status from evidence, not call the attempt a success.
