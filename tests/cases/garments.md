# Manual Case — Garments

## Objective

Verify background replacement on a folded or flat-laid garment without changing its phom, folds, construction, pattern, or observable color.

## Minimum source-image characteristics

Use an owned or redistributable real photograph with a complete garment boundary, at least one natural fold, visible seams, collar or closure detail, fine textile texture, and a neutral color patch vulnerable to background spill.

## Critical invariants

Product count, silhouette, collar, sleeves, fold junctions, seams, closures, pattern registration, labels or logos, fabric texture, and color relationships.

## Reference-style requirements

Include a clearly different product plus at least one excluded element such as typography, a watermark, or prop. The desired surface and lighting must still be readable.

## Safe Run checks

Confirm all lock-sheet sections, correct role mapping, explicit excluded elements, color risk, and no render before `CONTINUE`.

## Fast Run checks

Confirm the same locks were enforced without leaking the prior product after `NEXT PRODUCT`. Ambiguous layers or unreadable labels must trigger a pause.

## Ecommerce checks

Check source ratio, alternate ratio via background expansion, no product crop or distortion, realistic contact shadow, restrained background, and approximately 15% safe padding where feasible.

## Social checks

Check intentional negative space, no invented copy, no props unless requested, and no stronger grade crossing the garment.

## Failure conditions

Any changed outline, fold, seam, closure, pattern, label, texture, product color, reference contamination, generated typography, or unverifiable detail marked PASS.

## Asset-rights requirement

Record owner or creator, source record, consent where relevant, and redistribution license before adding assets to the repository.
