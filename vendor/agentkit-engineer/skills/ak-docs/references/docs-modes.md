# Project documentation modes

## Init

Inspect instructions, README, existing docs/navigation, relevant source and tests. Discover missing information ownership rather than filling a preset template. Keep the smallest useful document set; confirm any material replacement of existing authority before writing. Do not create empty scaffolds or inventory snapshots.

## Reader-facing explanation

The reader needs a model of the system, not merely a list of authoritative filenames. When a topic is unfamiliar, introduce the components and their roles, follow a meaningful input/state through the relevant mechanisms, and explain the observable result and failure boundaries. Prefer cohesive cause-and-effect prose and carefully chosen code/diagram examples over one-line bullet inventories. A documentation update should preserve previously accepted conceptual depth; converting an explanatory answer into a doc or Notion page does not justify reducing it to a skeleton.

The code remains authority for executable behavior. For example, an embedded device's decode → transport → cloud-processing path can be explained in a trace with validated interface names and appropriately scoped code excerpts. That explanatory trace does not assert the docs are an independently maintained API specification, and every version-sensitive claim must still be checked against source.

## Update

Establish which public contract, environment rule or accepted decision changed. Find its canonical owner and linked consumers. Remove obsolete paraphrase; preserve non-derivable rationale. Update only impacted documents; verify links and claims, and run existing docs checks or owning generators where relevant.

## Summarize

Bound inspection by requested topic. Distinguish current code behavior, planned direction and unverified research. Provide evidence pointers. Do not silently create a generic codebase-summary file.

## Cross-skill impact

A change to setup, public API, architecture, security, data flow, operations, recovery or accepted maintainer decisions may require docs updates. An internal refactor with no observable changed contract normally does not. Follow repository-specific authority rather than enforcing universal filenames.

## Shared deletion test

If source/tests/schema/generator already describe a mutable fact, point there instead of paraphrasing it. Keep WHY that the executable owner cannot reveal: reasons, rejected alternatives, terminology and constraints. A path/command/reference must be checked against its actual owner; chronological records are not evergreen product truth.
