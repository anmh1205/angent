# Component system styling

Prefer:
- primitive components with clear ownership;
- variants for real semantic differences;
- composition over giant prop matrices;
- consistent spacing/size tokens.

Avoid:
- copying component markup between pages;
- page-specific overrides that fight the design system;
- styling by DOM position when component state/variant is the real concept.

When using shadcn/Radix-like primitives, keep accessibility semantics from the underlying primitive intact.
