# Optional Reqwise schema-level integration test

This test checks the exact compiled argument structures against the **actual MIT Reqwise server validators**, not ANGENT's own test doubles. It is read-only and never connects to Figma or triggers figma_diagram.

Validated on 2026-10-16 with Reqwise OSS 0.3.0 at commit 4ee65b7a037578690cfcd4006257c4f25e458eea: **six of six shapes accepted**.

## Reproduce (in a controlled development/test environment)

1. Clone https://github.com/hoangpm96/reqwise-figma-mcp to a separate folder and inspect its MIT license; check out the commit above.
2. Install its dependencies with npm ci --ignore-scripts.
3. From the ANGENT repo, generate payloads:

       python tests/integration/export_reqwise_payloads.py /tmp/reqwise-payloads.json

4. Check via a TypeScript runner such as tsx (which may need installation or the local package dependency):

       npx tsx tests/integration/check_reqwise_schema.ts /tmp/reqwise-payloads.json /path/to/reqwise-figma-mcp

A schema success does not prove the plugin is connected, the canvas was modified, drawing is visually legible, or Pro-only methods exist. In a real environment, these are separate acceptance gates. If the upstream schema changes, rerun this test before shipping.

## D2 rendering (actual CLI, optional)

D2 is not bundled with ANGENT. Review/install the official D2 CLI independently (tested with v0.9.0), then run:

    python tests/integration/check_d2_cli.py --d2 PATH_TO_D2

The test compiles three synthetic source models and checks D2 process exit status, SVG root/viewBox, real node labels and unexpected active elements. The SVG and PNG were also visually inspected in a separate test session. This cannot certify production architecture or an unreviewed business data model.

Source: https://d2lang.com/tour/man/ and https://d2lang.com/tour/sql-tables/.
