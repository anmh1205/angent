# Git retrospective metrics and evidence gates

Adapted from stable Engineer 2.19.0 Retro metrics/reporting and the actual pitfalls visible in Git history.

## Collection and time

Specify repository/ref scope, resolved since/until instants with timezone, inclusion of merges, reachable history and whether Git was fetched. Time series must use consistent author-date vs commit-date semantics. A detached snapshot or shallow clone can omit legitimate history; disclose it.

Candidate measures:
- total commits, per-day commit count, distinct activity days;
- lines added/removed from `git log --numstat`, with binary/rename/generated-file caveats;
- hotspots by repeated path changes;
- conventional commit subject distribution when subject convention is actually used;
- number of distinct authors and optionally grouped author-identity statistics;
- test-file touches divided by all observed file touches (a **change ratio**, not executed test coverage);
- task/plan completion only from actual task mapping and acceptance evidence.

For any reported derived value give numerator, denominator, units and formula. Commit frequency = measured commits / actual period days; activity-day ratio = days with commits / period days. If added/removal sums or net LOC make a churn quotient unstable (net ~0 or negative), report raw adds/removes instead of an invalid 'churn rate'.

## Period and team comparisons

Use equal-length adjacent periods, disclose missing dates, author aliases, bots, squashes and bulk dependency updates. Highlight structural shifts rather than treating a numerical difference as causal progress. Per-author metrics are optional descriptive data; do not score people from commit counts or LOC.

## Plans and CI

Read actual plan files and provider tasks where available. A checkbox alone may be unverified; map acceptance evidence. Git changes to tests do not establish test execution/passing. State CI status only from observed results.

## Reporting

Return period, source/provenance/limitations, measured data, notable change clusters, outcome/rework narrative, real incidents/blockers, actions and next-observation criteria. When requested, format Markdown or a self-contained HTML export with no external dependencies. If the report is not saved, output a draft and say so.

Do not alter source files, commits, branches or task state as part of the retrospective.
