# Skill validation and calibration

Structural validity is necessary but not evidence of behavioral quality.

## Structural checks

Verify:
- valid frontmatter/name/description for the target Skill standard;
- no duplicate/broken metadata;
- resource links resolve;
- no placeholder/example cruft remains;
- scripts have documented dependencies and deterministic behavior where claimed;
- generated/package artifacts exclude secrets and irrelevant build environments.

Use the actual target runtime/spec limits rather than copying stale universal numeric limits.

## Behavioral cases

At minimum cover the distinct risks that matter:

1. **positive trigger** — should activate;
2. **negative/counter trigger** — nearby task should not;
3. **normal path** — representative workflow outcome;
4. **hard branch** — reference/fallback/gate matters;
5. **capability absence** — degraded behavior;
6. **regression case** — accepted previous behavior stays good.

For broad Skills, sample different project/domain conditions rather than many paraphrases of one prompt.

## Baseline comparison

For create, compare against no Skill when that answers whether the Skill adds value.

For update/optimize, compare against the accepted original behavior.

Judge:
- outcome quality;
- activation precision;
- preserved safety/authority;
- unnecessary ceremony/cost;
- artifact/provider evidence;
- regressions.

A blocked/ungraded evaluation is not a pass.

## Human/Quality review

Where semantic quality is load-bearing, include substantive review rather than relying only on deterministic scripts or an automated grader.

Record enough model/runtime/source version to know what the evaluation actually established.

## Iteration

Generalize from failure mechanism, not literal test wording.

If an eval exposes an ambiguous task or bad criterion, repair the eval/criterion rather than distorting the Skill.

Scale the case set only when additional cases cover a new failure class.
