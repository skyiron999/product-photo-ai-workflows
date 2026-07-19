# Quality Check

Quality assurance compares three roles side by side: the original product source for fidelity, the style reference or Style Card for visual treatment, and the output for both. Never judge the output from memory alone.

## Product checks against source

- same product identity, count, geometry, silhouette, orientation, perspective, folds, and arrangement;
- same observable product colors and internal tonal relationships, without background color spill;
- same materials, textures, transparency, reflection behavior, and specular highlights;
- same construction, seams, edges, fasteners, jewelry components, text, logos, labels, and patterns;
- no missing, invented, duplicated, beautified, or simplified detail;
- no cutout halos, clipped edges, artificial outlines, or lost fine structure.

## Treatment checks against style

- background material, color family, texture, mood, lighting direction, softness, and contact shadow are coherent;
- composition and spacing fit the selected Output Profile;
- no reference product, prop, person, package, text, logo, or watermark has leaked into the output;
- the product remains visually grounded without being relit, recolored, distorted, or cropped.

## Result semantics

- `PASS` — every locked product fact that can be inspected matches the source, the requested output constraints are met, and no reference contamination is visible.
- `WARN` — no verified Product Lock violation is visible, but one or more details cannot be confirmed because of resolution, occlusion, reflection, color calibration, or platform limitations. State each uncertainty explicitly.
- `FAIL` — a visible Product Lock violation, reference contamination, output-constraint violation, or material artifact exists. Name the defect category and use the matching repair command.
- `MANUAL REVIEW` — the bounded repair loop has been exhausted, exact commercial accuracy cannot be established, or the platform cannot preserve the source reliably enough for release.

Never convert an unverifiable detail into `PASS`. If color is commercially critical and the input is not calibrated, report that exact color accuracy cannot be verified even when the visual match appears close.
