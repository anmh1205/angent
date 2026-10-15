# Vibe delivery modes and permission boundaries

| Mode | Native intent | Portable host effect |
|---|---|---|
| default | Plan/implement/test/review then stable PR ready | Stop before merge unless independently authorized |
| `--beta` | Stage to beta/dev target | Confirm actual base, PR and release target |
| `--ship` | Merge PR then post-merge CI watch/repair | Must have current user authorization + branch policy; no implicit override |
| `--both` | Beta merge/CI convergence followed by stable stage | Never promote red/pending beta; ensure stable lineage; each actual merge needs authority |
| `--advice` | Independent Kongming supervision, including post-PR review | Only claim separate adviser if real runtime supports it |

The upstream Vibe pipeline involves worktree, plan, cook/fix, code-review, ship and review-pr in distinct ownership. Current authority and source-of-truth issue/repo state supersede stale handoffs or broad mode labels.

**Safety gates:** scope/issue acceptance, clean/isolated branch, source permissions, tests and review, PR base/head, CI status, user merge policy, deployment constraints and rollback. If an effect is ambiguous, read back provider state before retrying. Never force-push to 'complete' a stage.

**On interrupted runs:** preserve active stage, branch/ref, PR ID, last known CI run, accepted decisions, actual effects and first next action; don't replay a merge or publish on resume without observing its previous outcome.
