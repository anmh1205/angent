# Generated-design normalization

When importing generated HTML/Tailwind/design output:

1. extract layout/component/state intent;
2. map colors/type/spacing to project tokens;
3. replace duplicated primitives with project components;
4. preserve accessibility/semantic structure;
5. remove demo-only content/inline hacks;
6. implement real loading/error/empty/auth states;
7. compare rendered result with the intended design.

Treat generated code as a reference implementation, not authority.
