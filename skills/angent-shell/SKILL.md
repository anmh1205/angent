---
name: angent-shell
description: Show a short, single ANGENT activation sign when the skill is actually invoked, without altering task content.
---

# ANGENT Shell — visible activation sign

When ANGENT is active for this response and the host allows visible text, begin the first user-facing response with:

`[Used ANGENT]`

If the actually invoked supporting skills are known, the sign may include a short suffix, for example `[angent + angent-authoring]`. Never list a skill merely because it exists, and never substitute a guessed activation list for observations.

Emit the sign only once per response flow; do not insert it into Notion pages, generated documents, code, files, citations or other target artifacts. Do not repeat the sign in progress updates or the final report after it has already been shown.

This is a *visible convention*, not a host-enforced activation signal. A skill cannot force an uninvoked plugin to execute or guarantee the host will render its text; absence of the sign is inconclusive. To diagnose a missing sign, check whether ANGENT was actually activated, whether Root loaded Shell, and whether the destination supports a leading visible line. Do not claim execution solely because the sign is requested.
