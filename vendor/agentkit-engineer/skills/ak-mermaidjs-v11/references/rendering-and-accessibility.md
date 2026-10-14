# Mermaid rendering, integration and accessibility

The stable Engineer 2.19.0 source covers Markdown embedding, Mermaid.js integration, Mermaid CLI export, themes, accessibility and rendering checks. Use these mechanisms only where the active runtime actually supports them.

## Markdown and inline rendering

A standard Mermaid-supporting Markdown surface recognizes:

~~~~markdown
~~~mermaid
flowchart LR
  Client --> API
  API --> Store
~~~
~~~~

The code block is **source**, not proof of successful rendering. Different destinations support different versions and diagram types. Preserve the source for future edits, and verify the target's actual preview if user-facing presentation quality matters.

## CLI export

The upstream tool is the separate npm package @mermaid-js/mermaid-cli (binary **mmdc**). Confirm it exists/has a compatible version and that export is authorized. Typical invocation:

~~~bash
mmdc -i diagram.mmd -o diagram.svg
mmdc -i diagram.mmd -o diagram.png -t dark -b transparent
mmdc -i diagram.mmd -o diagram.pdf
mmdc -i diagram.mmd -o diagram.svg --configFile mermaid-config.json
~~~

Use mmdc help for current supported flags and dependencies; installation or a Docker/browser invocation is an external effect and not automatic. Output extension selects SVG/PNG/PDF. A generated path is only delivered as an artifact after verifying the file is present and opens correctly.

For a CI pipeline, pin the Mermaid/CLI version where repeatability matters. Check source parsing, exported file integrity and, where possible, representative visual rendering—not just command exit status.

## Browser and application integration

Mermaid.js exposes initialization, parsing and rendering through the installed package. Example API operations:

~~~javascript
import mermaid from 'mermaid';
mermaid.initialize({ startOnLoad: false, securityLevel: 'strict' });
await mermaid.parse(diagramSource);
const { svg } = await mermaid.render('diagram-unique-id', diagramSource);
~~~

For React/Vue/SPAs, make render IDs unique, handle asynchronous render errors and stale component updates, avoid duplicate global initialization, and respect SSR/client-only boundaries. Treat DOM insertion of generated SVG as a security-sensitive operation if text or configuration comes from untrusted users. Use the platform's real diagram component/plugin when provided rather than injecting CDN scripts into user content.

## Appearance and accessibility

Common Mermaid themes include default, dark, forest, neutral and base. Different Mermaid versions may support classic/handDrawn looks, diagram-level frontmatter and layout algorithms (Dagre/ELK). Check compatibility and avoid relying on appearance directives to fix incorrect structure.

Add a concise accessible title/description when appropriate:

~~~mermaid
flowchart LR
  accTitle: Request validation flow
  accDescr: API rejects unauthorized requests; authorized calls reach storage.
  A[Request] --> B{Authorized?}
  B -->|No| C[Reject]
  B -->|Yes| D[Storage]
~~~

Retain a textual explanation for relationships the reader must understand without the image. Check text contrast, label legibility, screen-reader behavior and zoom/print scaling where the target requires accessibility.

## Trust and evidence

Keep Mermaid's **strict** security mode for untrusted diagram source unless the containing app deliberately establishes and tests a different trust model. Do not enable loose HTML, interactive links/click callbacks or arbitrary CSS from untrusted diagrams by default.

Report separately:
1. authored source and target Mermaid version;
2. actual parser validation (if run);
3. actual SVG/PNG/PDF export and artifact path (if created);
4. rendered-result review, accessibility and limitations.

Never claim all four solely from a valid Markdown fence.
