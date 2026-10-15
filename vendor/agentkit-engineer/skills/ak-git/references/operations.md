# Git operation semantics

## Commit

- inspect current/staged diff;
- stage only the intended coherent unit;
- scan for secrets/sensitive artifacts;
- follow repository commit conventions;
- verify resulting commit content.

## Commit + push

After commit:
- resolve intended remote/upstream;
- fetch/inspect divergence when it can change safety;
- push normally;
- on rejection, diagnose divergence instead of blindly rebasing/forcing.

## Pull request

Resolve:
- canonical provider/repository;
- source/base;
- complete remote diff;
- linked issue/spec when relevant;
- provider template/required metadata.

Create/update the PR through the available provider capability and read it back when the PR itself is the requested endpoint.

## Branch merge

Before merge:
- confirm target/source and authority;
- fetch current refs;
- inspect divergence/conflicts;
- run required verification where merge-readiness depends on it.

Do not rewrite shared history merely to make the merge prettier.

## Merge PR

Use provider state for:
- mergeability/conflicts;
- required checks;
- required reviews;
- branch protection/queue.

If checks are pending, follow the repository/provider's allowed merge/queue behavior. Do not claim completion until the requested merge/post-merge endpoint is actually observed.

## Stacked PRs

A stack is an ordered dependency graph of branches/PRs.

Operations can include init/add/submit/sync/rebase/merge when supported.

History rewriting and multi-PR merge are consequential: preserve explicit authority and provider safety gates. Do not carry commands/flags from one stacked-PR implementation into another without live capability evidence.
