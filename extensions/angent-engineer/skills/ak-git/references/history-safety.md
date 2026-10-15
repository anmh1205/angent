# Git history safety

Before rebase/reset/force-push/delete:
- identify whether the branch is shared;
- check uncommitted work;
- know the remote tracking state;
- understand whether commits are referenced by open PRs/releases.

Prefer `--force-with-lease` semantics over blind force where rewriting is explicitly authorized.

Do not rewrite protected/shared history for cosmetic reasons.
