# Commit boundaries

A good commit usually represents one coherent reason for change.

Split when changes:
- serve unrelated outcomes;
- can be reviewed/reverted independently;
- mix formatting/refactor with behavior in a way that hides the behavior.

Keep together when splitting would create a broken intermediate state or obscure one atomic migration.

Review staged diff, not only working-tree diff.
