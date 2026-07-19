# Repair Loop

Repairs are source-first, targeted, and bounded. They correct one verified defect without compounding changes elsewhere.

## Source-first rule

Return to the original product source. Treat its product pixels and visible facts as authoritative for every correction. The binding rule is: never repair from a generated output. A generated output may be inspected to locate a defect but must not become the new product source.

Rebuild the requested region from the original product source, then reapply only the approved background or canvas treatment needed around it. Keep every unaffected region unchanged.

## Bounded sequence

1. Classify the defect as product, color, details, edges, background, lighting, or composition.
2. Apply one matching canonical repair command against the original source.
3. Run the complete quality check again, not only the repaired category.
4. If the same defect persists, run that product through Safe Run from the original source and require a new `CONTINUE` approval.
5. If the defect persists after the Safe Run attempt, stop automated repair and mark `MANUAL REVIEW` with the exact unresolved evidence.

Do not stack speculative fixes. Do not use a failed render as input for another render. `START OVER FROM SOURCE` is mandatory when product identity, geometry, count, or multiple locked details have drifted.
