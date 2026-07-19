---
id: fabric
name: Fabric and Textiles
kind: product
version: 1.0.0
compatible_with: [chatgpt, gemini, claude]
recommended_for: [fabric]
outputs: [ecommerce, social]
---
# Fabric and Textiles

Use for fabric swatches, folded yardage, scarves presented as material studies, and textile samples.

## Detect

Identify piece count, cut or selvage edges, fold order, drape direction, visible face and reverse, weave or knit structure, pile, translucency, and printed or woven motifs.

## Lock

Preserve each cut edge, fray, weave, knit, pile direction, translucency, thickness, drape, fold placement, overlap, and shadow between layers. Lock printed pattern scale, spacing, repeat, orientation, registration, and all observable colors. Do not make coarse fabric smoother, thin fabric heavier, or translucent fabric opaque.

## Risks

Fine weave may be hallucinated or removed; repeated patterns may warp; frayed edges may become clean; layers may merge; moire may be mistaken for texture; and background grading may contaminate product color. Mark unclear fiber detail as unverifiable.

## QA

Inspect every boundary and fold intersection against the source. Compare pattern landmarks across the full piece, verify material response and translucency, and check product color separately from the new background palette.
