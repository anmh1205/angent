---
name: ba-d2-architect
description: Business analysis d2-architect specialist.
---

# ANGENT BA: d2-architect

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/d2-architect/SKILL.md

## Portability and authority

Use domain-specific steps below as methodology, not as authority or proof of tool execution. Original Claude-specific scripts, hooks, subagents, filesystem paths and approval levels are illustrative until verified in the current environment. ANGENT Root owns intent and routing; Execution owns writes and read-back; Quality verifies outcomes. Honor project naming and do not invent decisions.


# /d2-architect — System / Architecture Diagram (D2, nested container + ELK)


## Goal

Draw the **system architecture picture** at the business level: blocks (client, backend, external services) nesting sub-components (service, DB, gateway), with business-labeled call flows between them. Use [D2](https://d2lang.com) nested containers — something **Mermaid cannot draw nicely**. Output in `docs/{feature}/d2-architect/`:

1. `{slug}.d2` — D2 source (text, git-tracked). Edit when calling the skill again (auto update mode).
2. `{slug}.svg` — pre-rendered (open in browser/IDE/Obsidian).

Plus `d2-architect/{feature-or-shared}-d2-architect-index.md` (metadata + block table). If drawing the whole-system architecture (not belonging to a single feature) → save under `docs/_shared/d2-architect/`.

## Architecture = business level, NOT a deployment diagram

A skill for **devs acting as BAs** — draw at the **logical architecture** level, NOT a solution architect's deployment diagram. Draw at the level of **"what blocks the system has, which external services it calls, the main data flows"** — enough for stakeholders + devs to understand the context. Do NOT draw: pods/replicas, load balancer config, VPC/subnet, port numbers, container images. If the user needs that level → that is the architect's job, out of scope.

**ALLOWED to draw:** logical blocks (Client/Backend/Mobile), services by business function (Auth, SRS Engine, Import), the database (1 block), external services by name + purpose (Google OAuth, Stripe, SendGrid), business-labeled call flows.

## Constraints

- **Fixed output** `docs/{feature}/d2-architect/{slug}.d2` + `.svg` (or `docs/_shared/d2-architect/` if cross-feature).
- **`--feature` optional** — auto-detect from context; no `--feature` but a WHOLE-system architecture description → draw into `_shared/d2-architect/` (escape hatch, KEEP as is). File already exists → enter update mode automatically, no flag needed. **Want to attach to a specific feature that doesn't exist yet → auto-derive slug + create feature** (entry point, see `feature-bootstrap.md` group A); a whole-system architecture still goes into `_shared/` as before.
- **AI writes the source, NO coordinates** — ELK handles the layout.
- **Compile must PASS** before reporting done.
- **Review the image yourself** (accuracy): if Chrome is available, render `--png` then Read the image to inspect overlaps/overlapping edges/wrong labels before reporting; without Chrome, inspect the source + `.svg` carefully.
- **L1 approval** before Write — BA-friendly prose (blocks + external services + main flows), do NOT dump the source.
- **NO L3 iterate** — review from the .svg.
- **Do NOT ask about/draw infra details** (port, replica, VPC) — see the "business level" section above.
- **Per `diagram-selection.md`** — `/d2-architect` for the system picture; a multi-branch business flow → `/d2-activity`; a data model → `/d2-erd`.
- **Idempotent** — 1 slug = 1 file; rerun → enter update mode automatically (L2 diff), no refusal.

## Inputs

```
/d2-architect --feature <slug>              # architecture in the context of one feature
/d2-architect "<system description>"            # whole-system architecture → docs/_shared/d2-architect/
/d2-architect "<description>" --feature <new-slug>  # feature doesn't exist → derive/use slug + interview + create (entry point)
```

Slug already exists → the skill recognizes it and enters update mode (L2 diff), no extra typing needed.

## Flow runtime

```
User calls /d2-architect [--feature X | "<description>"]
   │  d2 not installed? → stop, give install instructions
   │  ┌─ Resolve the write target (feature-bootstrap.md group A + _shared escape hatch):
   │  │  • WHOLE-system architecture (whole-system description, no --feature) → docs/_shared/d2-architect/
   │  │    (KEEP this path — the "no feature yet" state is valid, no need to derive).
   │  │  • Want to attach to a specific feature that matches no docs/{feature}/ → entry point:
   │  │    derive/use slug (kebab-case, ASCII, ≤50 chars), confirm at L1 (user can override),
   │  │    create docs/{feature}/d2-architect/ on Write. Do NOT require running /brainstorm first.
   │  │  • ambiguous 1-word unknown slug → ask "new feature, typo, or whole-system architecture?" (list features).
   │  ▼
1. Read the architecture source by priority:
   docs/_shared/system-overview.md (if present — the best source) →
   docs/X/srs/{feature}-spec.md + flows.md (external service mentions, components) →
   NO source yet (new feature / whole-system architecture lacking system-overview): interview EXACTLY the
   scope the architecture needs (feature-bootstrap.md group A step 3), gather 1 business-language batch (do NOT ask
   about port/replica/VPC): logical blocks (Client/Backend/...) · services by function · external
   services (name + purpose) · main call flows. No-re-ask what the source already has.
   Ambiguous description even with a source (system-overview.md only lists block names, call flows unclear) →
   MUST ask clarifying questions before generating, do NOT fabricate call flows/external services.
   ▼
2. Break down: logical blocks (containers) → sub-components → external services → call flows + labels
   ▼
3. Write the .d2 source (formula below) — nested containers
   ▼
4. L1 plan preview (prose: K blocks, N services, M external services). User Y → continue
   ▼
5. Write {slug}.d2 → render.sh → {slug}.svg (compile fail → fix, up to 2 times)
   ▼
6. Update {feature-or-shared}-d2-architect-index.md (env note → activity.log). Tell the user to open the .svg.
```

## How to build (build step-by-step)

### Step 1 — Skeleton d2-architect/ if it doesn't exist

`{feature-or-shared}-d2-architect-index.md` (type `d2-architect-index`): standard frontmatter + diagram table (slug / blocks / external services / updated). Lifecycle inherited from `srs/{feature}-spec.md` (or standalone if `_shared/`).

### Step 2 — Formula for writing the .d2 source (architecture)

```
direction: right       # horizontal architecture reads more easily

# User actor:
Learner: Learner { shape: person; style.fill: "#E8F0FE" }

# Logical block = a container nesting sub-components:
Client: Client (Web / Mobile) {
  UI: Interface
  SW: Service Worker
}

Backend: Backend {
  API: API Gateway { shape: hexagon; style.fill: "#E0E7FF" }    # gateway/proxy/LB = hexagon
  Auth: Auth Service { style.fill: "#E6F4EA" }                 # service = rectangle (default) + green
  Core: Core Engine { style.fill: "#FFF4E5" }                  # highlight the main component
  Cache: Redis cache { shape: stored_data; style.fill: "#CCFBF1" }  # cache = stored_data
  DB: Database { shape: cylinder; style.fill: "#F1EAFB" }      # DB/store = cylinder
}

# External services = dashed-border container:
External: External services {
  style.stroke-dash: 3
  Google: Google OAuth
  Pay: Payment Gateway
}

# Call flows = edges, business label, reference children via a dot:
Learner -> Client.UI: uses
Client.UI -> Backend.API: HTTPS / REST
Backend.API -> Backend.Auth: log in
Backend.Core -> Backend.DB: read/write
Backend.Auth -> External.Google: OAuth callback
```

**Rules:**
- Nested container: `Backend: { API: ...; DB: {shape: cylinder} }`. Reference children: `Backend.API`.
- External services: wrap in a `style.stroke-dash: 3` container (dashed border) — to distinguish "outside our control".
- Highlight the main component with `style.fill`. Don't color everything — 1-2 accent colors is enough.
- **QUOTE labels/names with special characters** `() / | :` — e.g. `Client (Web / Mobile)` is OK (not merely for spaces), but `"API v2 / gateway"` needs quoting.
- NO coordinates — ELK handles it. NO infra detail (port/replica).

### Step 3 — Render + verify

```bash
# compile fail → usually a missing quote on a label with special characters → fix, re-render.
```

## Gotchas

- **d2 not installed** → stop, print 1 install line.
- **QUOTE labels with special characters** (gotcha #1) — `/ | ( ) :` in a name/label must be wrapped in `"..."`. Forget → compile fail.
- **Don't draw infra** — port, replica, load balancer, VPC are the deployment level, out of IT-BA scope. Keep at the logical-block + external-service level.
- **The best source is system-overview.md** — if it doesn't exist, suggest the user run `/update-overview system` first to get a proper source.
- **Containers too deep** (nested >3 levels) → hard to read; merge some or split into 2 diagrams (e.g. 1 overview + 1 backend zoom).
- **External services** always in a dashed-border wrapper + real name + a short purpose phrase (Google OAuth, not "IdP #1").
- **Cross-feature** (whole-app architecture) → save under `docs/_shared/d2-architect/`, do NOT stuff into one feature folder.
- **Update mode (slug exists)** → Read the old source, L2 diff, re-render after user Y.
