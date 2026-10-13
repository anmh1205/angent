# Shipping pipeline

## Preflight

Check:
- clean understanding of changed scope;
- current base branch;
- required tests/builds;
- review status;
- secrets/sensitive files;
- migration/release notes when relevant.

## Delivery

Use the repository's established workflow.

A useful state ladder is:

```text
verified local change
→ pushed branch
→ PR ready
→ checks/review satisfied
→ merged (if authorized)
→ post-merge state verified (if required)
→ release/deploy only if separately authorized
```

Do not collapse these states into one “shipped” flag.

## Failure

If base advances or checks reveal a new defect, return to implementation/review instead of forcing convergence.
