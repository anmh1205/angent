---
name: ak-preview
description: View existing artifacts or generate visual explanations, diagrams and lightweight presentation views using the most appropriate render/browser/document capability.
metadata: {port: angent-fallback, mode: adapted}
---

# Preview — Portable Fallback

Read `references/preview-routing.md`.

## Resolve the intent first

### View mode

The user already has an artifact and wants to inspect it.

Open/render the artifact in its natural viewer when possible.

Do not create a new deck/diagram just to “preview” something that can be rendered directly.

### Generate mode

The user asks for a visual explanation of code/system/content rather than merely viewing an existing file.

Choose the lightest representation that explains the requested relation:
- annotated HTML/Markdown;
- Mermaid/Excalidraw/Tech Graph diagram;
- small slide-like HTML presentation;
- another destination explicitly requested by the user.

## Workflow

1. Identify view vs generate mode.
2. Select destination-specific tool/renderer.
3. Preserve source semantics and user-provided styling/preferences.
4. Render/open the result.
5. Inspect the visible output.
6. Fix clipping, broken links, unreadable diagrams or failed media before reporting success.

Preview is a visual understanding surface, not a reason to mutate the source artifact unnecessarily.
