# SVG and raster output

## SVG

Produce valid XML/SVG with:
- explicit viewBox;
- predictable dimensions;
- escaped text;
- stable IDs when elements are referenced;
- no external font/image dependency unless intentionally packaged;
- text large enough for the final destination.

Prefer vector shapes/text over embedding a flattened screenshot.

## Validation

Check:
- XML parses;
- no element extends outside the intended canvas;
- arrowheads/connectors render correctly;
- text does not overlap shapes;
- clipping/masks work in the target renderer;
- links/embedded resources are valid when used.

## PNG export

Rasterize from the verified SVG rather than maintaining a separate hand-authored PNG.

Use sufficient resolution for the destination and inspect the raster output after conversion.

If a renderer substitutes fonts or changes geometry, fix the SVG or renderer choice before acceptance.
