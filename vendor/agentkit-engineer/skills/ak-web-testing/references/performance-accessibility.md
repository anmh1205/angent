# Performance and accessibility testing

## Performance

Use representative workloads.

Separate:
- server latency;
- browser main-thread/render;
- network transfer;
- asset loading;
- memory/resource leak;
- concurrency/throughput.

Compare before/after with the same method.

## Accessibility

Check relevant WCAG-aligned behaviors:
- semantic names/roles;
- keyboard/focus;
- labels/errors;
- contrast;
- heading/landmark structure;
- reduced motion;
- zoom/reflow when required.

Automated scans find classes of issues; they do not replace keyboard/screen-reader-oriented reasoning for critical flows.
