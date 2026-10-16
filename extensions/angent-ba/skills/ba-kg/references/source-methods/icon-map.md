# Icons in technical diagrams: opt-in and source-safe

**Provenance:** Adapted from MIT Dev BA Kit / rules/icon-map.md (Edward Ngo, 2026), https://github.com/nv-minh/dev-ba-kit. The original shell icon resolver and automatic CDN fallback are not part of the portable ANGENT kit.

## When an icon helps

An icon may clarify a **verified technology-specific** node (PostgreSQL, MQTT broker, an actual service provider). Do not assign vendor logos to generic business actors, abstract capabilities or inferred implementation components. A wrong icon is worse than no icon.

Node type and connections carry the meaning first. In a logical architecture, a database cylinder, queue shape and clear protocol label are normally sufficient.

## Safe source and licensing

Prefer local, reviewed icon resources with known license and correct attribution if needed. Never pull arbitrary assets from a remote CDN during rendering without explicit permission—business diagrams may contain confidential identities and external dependencies.

Do not promise the ANGENT D2 generator automatically embeds technology icons: its current executable subset represents typed nodes and labels without a general icon-path resolver.

## Accessibility and maintenance

Icons must not replace readable text labels; use consistent size and meaningful alternative descriptions for exported documents. Update/retire an icon when the source technology changes rather than trusting an outdated dependency scan.

## Fallback

If the appropriate licensed icon is missing, render the diagram without it. This is an acceptable, truthful output. Do not block a functional process or data diagram for decoration.

## Review

Check technology matches source evidence, visual layout, label readability and whether the assets are embedded safely for offline distribution. A generated SVG is not a license grant to redistribute the icons it might reference.
