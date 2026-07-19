---
id: garments
name: Garments
kind: product
version: 1.0.0
compatible_with: [chatgpt, gemini, claude]
recommended_for: [garments]
outputs: [ecommerce, social]
---
# Garments

Use for flat-lay clothing, folded apparel, and garment sets photographed on a horizontal surface.

## Detect

Identify garment count and type, front or back orientation, overlap order, folding method, visible panels, and any separate pieces. Describe only what the source shows; do not assume hidden construction.

## Lock

Preserve the exact silhouette, proportions, fold paths, overlap, seams, darts, hems, collar shape, cuffs, sleeves, buttons, closures, pockets, labels, logos, and visible hardware. Lock pattern scale and repetition, fabric thickness, texture, drape, color relationships, and natural wrinkles. Keep every piece in the same position and orientation unless the user explicitly supplies a different source arrangement.

## Risks

Watch for AI-symmetrized folds, changed collar openings, invented buttons, lost seams, duplicated sleeves, smoothed texture, shifted prints, unreadable labels, altered whites, and background color spill. Occluded or very dark details remain uncertain and must not be invented.

## QA

Compare source and output at the outer silhouette, all openings and fold junctions, then inspect construction details, pattern registration, texture, and product color. Confirm that contact shadow grounds the original shape without redrawing it.
