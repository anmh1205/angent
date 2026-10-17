---
name: figma-activity
description: Domain-specific activity diagram design and real Figma MCP delivery, if available.
---

# ANGENT Figma specialist: activity

Maintained adaptation of the MIT Reqwise Figma MCP method, copyright and attribution in extensions/angent-figma/THIRD_PARTY_NOTICES.md. Original: https://github.com/hoangpm96/reqwise-figma-mcp/blob/main/.claude/skills/figma-activity/SKILL.md

## ANGENT adaptation rules

ANGENT Root keeps reasoning and permission decisions. The original role/tool list and slash-command lifecycle are source examples, not evidence that the current host has the Reqwise MCP installed. Check figma_status, active file, target and permissions before invoking a native write; verify results by figma_read/get_diagram_spec and layout_audit. An unavailable native tool permits only a draft model; never claim a Figma write. Read the shared OSS diagram rules from ../figma-activity/references/oss-diagram-rules.md when useful. Keep the user's existing design system and BA business semantics.


## ANGENT runnable adapter and evidence boundary

The corresponding **real, local model fixture** is `extensions/angent-figma/examples/rental-fleet-activity.json`. Derive any new model from inspected requirements before running this tool; the fixture is illustrative only.

```sh
python extensions/angent-figma/scripts/to_reqwise_payload.py extensions/angent-figma/examples/rental-fleet-activity.json
```

The script validates this activity model and outputs the actual Reqwise OSS `figma_diagram` candidate arguments, `dry_run=true` and `writes_performed=false`. For an approved project, pass `--evidence-graph PATH_TO_BA_GRAPH` to check cited requirement IDs **if every reference is defined in that graph**. If a source is missing, stop and report the gap; never remove or invent an ID to make the check pass. The printed JSON does not call MCP and never creates Figma nodes.

When the Reqwise MCP and its companion Figma plugin **actually exist in the host**, consult `figma_status` and `figma_docs`, verify the selected file/page and permission, then only invoke an authorized `figma_diagram`. After execution, read back `figma_read` with `get_diagram_spec` and `layout_audit`, compare node/edge inventory and inspect a real image. Record tool errors and divergences, not just a success-looking response. If the MCP is unavailable, deliver the checked semantic payload labeled **not written to Figma**.

**Additional activity semantic acceptance:** Check each task has a responsible lane when lanes are enabled, each decision has grounded guards, and every inter-lane transition represents a real handoff.

**Upstream scope:** MIT Reqwise OSS implements this diagram type, but the source-local payload generator alone proves neither upstream server compatibility for every version nor canvas fidelity. Pro-only functionality cannot be substituted silently.


# /figma-activity — Who does what, and what gets handed over

findings loop, frame placement, verification. This file carries only what is specific to an
activity diagram.

## Goal

Draw a process that crosses people. Approval, onboarding, fulfilment, escalation — anywhere
the interesting failures are **handoffs**: the step that sits in someone's inbox, the rejection
that goes back to the wrong person, the parallel work nobody waits for.

Output: one Figma frame `Activity · <title>`, plus the process questions the diagram exposed.

## Constraints

### Hard rules — never violate

- **ASK which way it runs before drawing.** `rankdir: "LR"` gives horizontal lanes — the
  classic swimlane, reading left→right. `"TB"` gives vertical lanes, reading top→bottom. It
  changes how the whole thing reads and it costs one question. Do not guess.
- **With lanes, EVERY node needs a `lane`.** A step nobody owns is exactly the bug this diagram
  exists to expose; it is drawn in a visible "(no lane)" band rather than quietly filed under
  the first lane.
- **Drop `lanes` entirely for a single-owner process.** Same notation, no bands. Do not invent
  a second lane to make it look like a swimlane.
- **Label a lane-crossing edge with WHAT is handed over** — "hồ sơ đã duyệt", "lý do từ chối" —
  not "next", not "tiếp theo", not nothing.
- **A `decision` needs at least two ways out, each with a condition on the edge.**
- **Never invent a step.** If the source stops at "rồi duyệt", that is the finding.

### Write it in the compact form

`text` is one line per thing. The `<lane>:` prefix is the field this diagram exists for — who
performs the step — and here it is two characters at the front of the line rather than a
property buried in an object, so a missing owner is visible at a glance.

```
rankdir LR                                  # ask the user first — see Phase 2
lane cus "Khách hàng"
lane cvkh "CVKH" / chi nhánh
lane los "LOS" / external
cus:  s start "Nộp hồ sơ vay"
cvkh: check "Kiểm tra giấy tờ"
cvkh: enough ? "Đủ hồ sơ?"                  # ? = a decision
los:  score "Chấm điểm tín dụng"
cvkh: reject err "Từ chối | và nêu lý do"   # err = the failure path, | splits a detail line
cus:  done end "Nhận kết quả"
s > check "hồ sơ + giấy tờ"
check > enough
enough > score "đủ"                          # a decision branch MUST carry its condition
enough > reject "thiếu"
score > done "hồ sơ đã duyệt"                # a lane-crossing edge says WHAT crossed
reject ~> check "bổ sung giấy tờ"            # ~> = rework, routed outside the lanes
```

Kinds on the node line: `start` · `end` · `?` (decision) · `fork` · `join` · `event` ·
`external`. Classes: `ok` · `err` · `edge`. Drop every `lane` line and the `<lane>:` prefixes
for a single-owner process — same notation, no bands.

### The node table — read this before writing a single node

| Want to say | Write | NOT |
|---|---|---|
| Somebody performs a step | `cvkh: check "Kiểm tra giấy tờ"` | leaving the `<lane>:` off when the diagram has lanes |
| The process begins / ends | `cus: s start "…"` / `cus: done end "…"` | leaving them out — "no trigger" and "no outcome" are reported |
| A question with branches | `cvkh: enough ? "Đủ hồ sơ?"` + ≥2 labelled edges out | one arrow out, or unlabelled branches |
| Something happens TO the process | `sys: t event "Hết 30 ngày"` | an `action`, which implies somebody chose to do it |
| Split into parallel work | `sys: f fork` … `sys: j join` | a decision, which is a choice, not concurrency |
| A step outside our boundary | `los: pull external "…"` | pretending we control it |
| It goes back for rework | `reject ~> check "bổ sung"` | `>`, which draws it as ordinary forward flow |

`fork` without `join` means the process never waits for the parallel work. The tool reports
it; that is almost always a real hole, not a drawing shortcut.

### Pitfalls — easy to get wrong

- **A lane is an OWNER, not a system layer.** "Khách hàng", "CVKH", "Hệ thống LOS" — roles and
  systems that *do* something. Not "Frontend / Backend / Database".
- **Do not model the UI.** "Bấm nút Gửi" is a screen interaction; the step is "Gửi hồ sơ". If
  the diagram is turning into screens, you want `/figma-userflow`.
- **One decision, one question.** "Đủ hồ sơ và đủ hạn mức?" with two outcomes hides two rules.
  Split it.
- **The unhappy path is not optional.** A process with only the approval branch is half a
  process. Ask what happens on rejection, on timeout, on missing documents.
- **`cls: "error"`** on the rejection path and `"edge"` on the rare one makes a long diagram
  readable at a glance. Use them.
- **A step dragged into another lane is REPORTED, not applied.** Whether the process changed
  hands is the spec author's call — if it really did, re-run with the corrected `lane`.

## Inputs

```
/figma-activity "Duyệt hồ sơ vay"                        # interview from scratch
/figma-activity "Onboarding" @docs/srs/spec.md           # derive from a source
/figma-activity                                           # asks which process
```

## Approach

### Phase 0 — Connection

Per shared rules §5.

### Phase 1 — Derive the model, and name the gaps

Build the **fact-list**:

1. **What starts the process**, and what ends it — every ending, not just the good one.
2. **The owners**: who or what performs a step. This becomes the lane list.
3. **The steps in order**, each with its owner.
4. **The decisions**, each with its question and every outcome.
5. **The handoffs**: at each lane change, what is passed across.
6. **The rework paths**: what goes back, to whom, and why.
7. **Parallel work**: what runs at the same time, and where it rejoins.

Anything the source does not say, **ask**, in business language: *who actually presses that?*
· *what happens if they reject it?* · *does anything wait for both of those to finish?*

### Phase 2 — Ask the one question that changes the drawing

**Horizontal lanes (LR) or vertical lanes (TB)?** Show what each means in one line and let
them pick. A process with many steps per role reads better LR; one with many roles and few
steps each reads better TB.

While you are asking, confirm the lane list itself — the reader's mental model of "who is
involved" is the thing most likely to be wrong, and it is cheapest to fix now.

### Phase 3 — Check, then draw, in one call

Call `figma_diagram` with `type: "activity"` and `options: { checkFirst: true }`: it checks the model and
**draws only if there are no findings**. Dirty → `checkedOnly: true` + the findings and nothing
is drawn; clean → it draws and returns `audit` in the same call. (`options: { dryRun: true }`
is still there for iterating on a model you expect to be wrong.)

Read every warning. The ones specific to this kind:

| Warning | What it usually means |
|---|---|
| Unlabelled handoff between lanes | say what crossed — this is the finding this diagram exists for |
| Step with no lane / lane that does not exist | somebody owns it; find out who |
| No start / no end | what triggers it, and what is the outcome including the bad one |
| Decision with fewer than two ways out | a question with one answer is not a question |
| Fork that never joins | nobody waits for the parallel work |
| Dead end that is not `end`/`external` | the process stops there and nobody said so |
| End step with a way out / arrow INTO a start step | the terminal is not really one: a step was marked `end`/`start` by mistake, or the arrow belongs elsewhere |
| Lane with no steps | the role does not belong on this diagram |

Fix the model, re-dry-run, then draw.

### Phase 4 — Draw, verify, report

1. Place the frame clear of what is on the page (shared rules §7).
2. Draw.
3. Read `audit` from the same result — it is the render-side check (overflow, clipping,
   truncation). Fix anything it reports. No second call for it.
4. One `screenshot` per SET of diagrams at the end, not one per frame — skip it when
   `audit` is clean and the human is watching Figma live.
5. Report per shared rules §11.

## What the machine does NOT check

- whether these are the steps people actually perform, as opposed to the ones in the SOP;
- whether the owner named is the owner in practice;
- whether a decision's outcomes are exhaustive (the checker counts branches, it cannot know
  the third case exists);
- how long anything takes, or where the process actually gets stuck.

The last one is worth saying out loud: an activity diagram shows structure, not queueing. If
the real problem is that step 4 waits three days, that fact belongs beside the diagram.
