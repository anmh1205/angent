# Starting work when the feature or source artifact does not exist

**Provenance:** Adapted from MIT Dev BA Kit / rules/feature-bootstrap.md (Edward Ngo, 2026), https://github.com/nv-minh/dev-ba-kit. ANGENT does not require an existing feature directory or a new one for every user request.

## Decide whether a durable artifact is warranted

For a research question or an uncertain idea, conduct evidence collection and give findings before creating a project folder. For a requested accepted feature specification, identify actual product namespace, owner, intended output and source-of-truth location. Read any existing project conventions first.

If the requested skill needs an upstream acceptance decision (for example a UI prototype with undecided business permissions), produce a qualified draft or ask the one blocking question. Do not fabricate BR/FR/AC or create empty upstream files for the appearance of completeness.

## Establish a safe identity

Use existing feature identifiers where present. If none exist and a durable file is authorized, propose an unambiguous project-local slug; check for collisions, retired features and already accepted aliases. Stable IDs should not be silently renumbered on a rerun.

A named feature is not necessarily a directory, and a feature directory does not confer permission to rewrite everything within it. Never impose an inherited fixed docs layout on a different project.

## Minimum useful initial evidence

For opportunity work: buyer/users, the actual job, existing alternatives, evidence ledger, material constraints and next experiment. For requirement work: source need, actor, scope, accepted or proposed behavior, consequential open decisions and owning stakeholder.

For reverse engineering: pin code/document revision and distinguish observed behavior from proposed intent. An absent legacy document does not mean the user authorized reconstituting every architecture layer.

## Re-run and failure behavior

On a repeated request, inspect what already exists, compare source/target revisions and prefer updating only affected accepted sections. Where missing source blocks correctness, report exactly what evidence is required and what can still be produced safely. Never silently soften an error into a fictitious success.

## Example

A new vehicle-rental “remote control” feature requires legal/safety policy before a live immobilization command; research and draft diagrams can progress with that capability clearly marked unapproved. There is no need to create a dozen placeholder specs merely to start the work.
