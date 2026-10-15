# Product interface design as causal decision-making

The point of a UX review is not to score typography, spacing or color independently. It is to explain how an observable UI condition changes a user's ability to complete a real task, and how a proposed design would change that mechanism.

## Reconstruct the task before judging pixels

Identify who the user is, the information they need to decide, the action they can take, the relevant constraints and what "success" looks like. Follow the task through the actual navigation and system states. A screen may be visually balanced yet cause error because the primary action is unreachable during a permission failure, or because similar controls have incompatible meanings.

Treat user-supplied screenshots/templates and established product UI rules as a **positive baseline** where accepted. Investigate whether a difference is required by the target task or merely an accidental deviation. An existing good component should be reused before creating a parallel variant that fragments the system.

## Diagnose and choose

Describe a problem as **observation → plausible mechanism → consequence**, not as a styling dislike.

For example, "the rental fleet overview feels confusing" could come from excessive equal-priority cards, stale live statuses, inconsistent vehicle identifiers or missing warning severity. A new color palette will not fix every cause. Inspect realistic content and error/empty/loading states, then choose a discriminator: can the operator locate the at-risk vehicle and understand the next action with the existing information? If the failure is freshness rather than hierarchy, the remedy belongs in data/state semantics before visual styling.

Compare candidate fixes by task outcome, impact on other screens, accessibility, responsive behavior, implementation cost and maintainable design-system fit. Avoid majority voting across references. A frequent pattern in popular apps may be inappropriate when the product's actual data density or failure consequence differs.

## Preserve the accepted baseline

On a redesign, identify which existing behavior and visual qualities are already good (e.g., compact expert table, keyboard navigation, reliable color semantics, template login/reauth flow). A local complaint is not authority to replace the entire product grammar. Change the smallest affected dependency closure, and inspect adjacent views/states for regressions.

Differentiate levels:
- **systemic**: semantic color meaning, navigation, typography scale, reusable component behavior;
- **flow-specific**: missing decision step, order, permission state, validation feedback;
- **page-local**: one content imbalance or clipping defect;
- **production-only**: missing font glyph, vector stroke imbalance, export scaling or unverified browser render.

The earliest actual cause should own the correction. A global token change should not be the default remedy for one unusual page.

## Verification

State the expected behavior before changing the UI: what the user can now locate, decide or do, in which state and device context. Render and exercise the representative flow with real-length content, correct language/fonts, permissions, errors and loading states. When a user study is unavailable, code/browser inspection can substantiate implementation and interaction properties, **not** measured improvement in user success. Report that distinction.

## Contrasting cases

- **Systemic issue:** every dialog loses focus on dismissal. Repair the shared dialog/focus behavior, then check consumers; styling each screen individually misses the mechanism.
- **Local issue:** one dashboard row clips a long Vietnamese asset name. Verify actual font/width and repair that component without globally shrinking type.
- **Wrong proposed fix:** warnings are hard to notice because the server marks stale data as current. Stronger red is not an integrity fix; investigate the freshness contract.
- **Protected strength:** a user-provided approved admin template already has effective table density and authentication flows. Reuse them while changing only the new product-specific state, then compare rendered behavior.
