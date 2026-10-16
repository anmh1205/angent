# BA/Figma specialist scenario evaluations (67/67 planned, not run)

This suite is a **manual/agent acceptance corpus**, not an autonomous executor and not a test-passing certificate. It supplements source code/unit tests by checking business sense, source handling, output quality and provider truth in **13 realistic workflows that collectively exercise all 67 specialist skills exactly once**.

The exact cases, expected behaviors and falsifiable failure conditions are in \`scenarios.json\`. Each case has:
- \`input\`: the user's concrete problem and missing evidence;
- \`must\`: observable deliverables and source/semantic decisions;
- \`reject\`: negative controls that should invalidate a convincing-looking response;
- \`scope\`: bounded allowed effects;
- \`execution_status: not-run\`: never promoted by checking in this file.

## Execution and scoring protocol

1. Freeze actual source revisions, host, runtime tools, prompt, source corpus and supported evidence. Inspect ANGENT Root dispatch; a matching installed kit does not imply it should run autonomously.
2. Run the case using the current build and record the **actual response/artifact and run transcript** separately, with accurate source links and provider receipts. Do not edit \`scenarios.json\` to change expected criteria after inspecting failures.
3. Have an independent human or authorized reviewer check **every must and reject condition**, plus whether optional providers were actually available. Missing runs or live read-back are \`NOT_VERIFIED\`, not \`PASS\`.
4. Distinguish requirements **verification** (quality of definition), **validation** (value/scope supported by stakeholders), and **solution testing** (implementation under a real runtime). Following IIBA's definitions, these are distinct evidentiary claims.
5. Fix systemic causes in ANGENT Core/Hub or the relevant specialist; keep specific example tweaks only when they generalize. Re-run other cases in the same cluster to detect regressions.
6. Do not merge based on this document alone. Full branch release decisions require code checks, package extraction/smokes, actual behavior tests and appropriate provider testing. Do not use fake reviews to promote a kit's evidence tier.

**Grounding:** IIBA BA Standards and BABOK concepts for validation/verification/traceability; public MIT Dev BA Kit source; public Reqwise Figma MCP six-kind OSS API; current ANGENT 2.0 Hub and Core contracts. No commercial prompts or protected Pro source were copied.
