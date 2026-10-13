# Browser profile safety

Treat real browser profile state as sensitive.

Do not:
- print/export cookies;
- read saved passwords;
- copy local-storage/session tokens into reports;
- automate unrelated personal tabs/accounts;
- persist private session state into ANGENT memory/handoff.

Before a write/purchase/admin action, verify the active account/tenant and current authorization.
