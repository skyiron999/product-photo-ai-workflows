# Google Flow Tool Repair Prompts

Use these only after the initial Tool has been created with [`builder-prompt.md`](builder-prompt.md). Choose the single prompt matching the observed defect. Do not paste all repairs at once: broad rewrites make it harder to know which change fixed or broke the Tool.

After a repair, inspect both Code and Preview and rerun the named checks in [`acceptance-checklist.md`](acceptance-checklist.md).

## Repair role contamination

Use when Product Analysis contains facts from the reference subject, Reference Analysis contains facts from the target product, or the generated output borrows the reference product.

```text
Modify the existing Tool; do not rebuild it from scratch. Preserve all unrelated working behavior, labels, controls, and verified tests.

Repair role and state contamination only.

Keep PRODUCT SOURCE, STYLE REFERENCE, and GENERATED OUTPUT in separate state objects and visible areas. Make analyzeProduct(productImage) receive only the selected job's original Product Source and return product facts, Product Lock, uncertainties, and risks. It must not read referenceAnalysis, referenceStyleProfile, the reference subject, another job, or any generated output.

Make analyzeReference(referenceImage) receive only the active Style Reference and return transferable background surface, palette, texture, tonal variation, light, contact shadow, mood, negative space, compatible composition, and an exclusion list. It must not read Product Analysis or describe the Product Source. Explicitly exclude reference products, props, people, packages, text, logos, labels, brand marks, and watermarks.

Only buildEditInstruction may combine an already completed Product Lock with an already completed Reference Style Profile. In every generation request, label the first image as original Product Source and the second as style-only reference. Do not allow the reference subject or text to enter the product description or output.

Add a development-only diagnostic showing which source identifier and reference version were passed to each analysis and generation operation, without exposing image bytes or secrets.

Verify with a target product and a reference containing a visibly different garment: Product Analysis must describe only the target, Reference Analysis must describe only the background treatment, and the output must not borrow the reference garment.
```

## Repair Product Lock

Use when the output changes shape, folds, construction, pattern, color, jewelry components, text, or other product identity details.

```text
Modify the existing Tool; do not rebuild it from scratch. Preserve all unrelated working behavior, labels, controls, and verified tests.

Repair Product Lock construction and enforcement only.

Expand analyzeProduct(productImage) so each job records visible identity, count, geometry, silhouette, scale, orientation, perspective, arrangement, folds, construction, edges, text, logos, labels, patterns and repeat rhythm, observable color relationships, material, texture, transparency, components, highlights, and reflections. Apply category-specific scrutiny for garments, fabric, earrings, bracelets, and reflective accessories.

Place the complete Product Lock before all style and composition instructions in buildEditInstruction. State that the editor must replace only the existing background; it must not invent, remove, duplicate, reshape, beautify, complete hidden details, recolor, globally relight, distort, crop, or reconstruct the product. Background grading must not tint or recolor the product.

Make qaOutput compare the original Product Source and candidate output for every locked attribute. Any observable Product Lock violation must be FAIL regardless of background quality, with Retry from Source offered for that job.

Verify with one patterned garment or fabric and one reflective jewelry item. Confirm that a visually attractive output cannot receive PASS when a fold, motif, seam, stone, clasp, metal color, highlight, reflection, text, or edge changed.
```

## Repair Reference-first and Strict Match

Use when the Tool selects a named style preset despite having a reference, creatively reinterprets the background in Strict Match, or claims exact equality.

```text
Modify the existing Tool; do not rebuild it from scratch. Preserve all unrelated working behavior, labels, controls, and verified tests.

Repair Reference-first and STRICT MATCH behavior only.

When a Style Reference exists, create its dynamic Reference Style Profile directly from observable background surface, palette, tonal distribution, texture or grain, gradient or vignette, illumination falloff, light direction and softness, contrast, contact-shadow character, mood, negative space, and compatible composition. Display “Style source: REFERENCE IMAGE” and “Style Card: NONE — reference-driven”. Do not select, name, or silently use a Style Card, nearest preset, or hidden preset.

STRICT MATCH must require the mapped reference and minimize creative interpretation across every transferable background attribute. Product Lock remains higher priority. Do not substitute a palette, beautify the background, add props or typography, copy a reference subject, or change the product to improve the match. Label hidden or newly expanded regions as reconstructed and unverifiable.

Always display exactly: Pixel-exact guarantee: NO — generative visual match. Strict Match PASS means no material mismatch is observable at the inspection resolution; it never means pixel equality.

Verify one REFERENCE-FIRST run contains no named Style Card and one STRICT MATCH Safe analysis shows the match target, reconstructed regions, disclosure, and Product Lock precedence before generation.
```

## Repair Single/Batch isolation

Use when products are merged, a prior item affects the next output, the Tool creates a collage, or one failure stops the whole queue.

```text
Modify the existing Tool; do not rebuild it from scratch. Preserve all unrelated working behavior, labels, controls, and verified tests.

Repair SINGLE and BATCH EXPERIMENTAL job isolation only.

SINGLE owns one original Product Source and one job. BATCH EXPERIMENTAL accepts one Style Reference and 2–20 Product Sources, then creates one isolated job per source. Each job must own its originalProductImage, Product Analysis, Product Lock, generation request, ecommerce/social outputs, retry context, risks, error, and QA records.

Jobs may share only the active Reference Style Profile, reference version, and selected compatible settings. For every Batch generation, pass exactly one job's original Product Source plus the shared style reference. Never pass the full product array, another product, another output, or another job's Product Lock as visual or text context.

Process sequentially by default. Use bounded concurrency only if isolation is real in the current runtime. Failure of one item must mark only that row BLOCKED or FAIL and continue unrelated ready jobs. Never create a collage.

Add or correct queue rows with visible identifier, state, QA status, View, Retry from Source, and Download. Verify with at least three visibly different products that every output maps to exactly one source and that forcing one item to fail does not erase or stop the others.
```

## Repair source-first retry

Use when a repair edits the generated candidate repeatedly or when Product Lock drift accumulates after retries.

```text
Modify the existing Tool; do not rebuild it from scratch. Preserve all unrelated working behavior, labels, controls, and verified tests.

Repair source-first retry behavior only.

Keep originalProductImage immutable for the life of each job. Generated candidates must be stored only in ecommerceOutput or socialOutput and must never be assigned to originalProductImage.

Implement retryFromSource(job) so it discards only the affected generated working result and calls generateFromOriginal(job) using that job's immutable original Product Source, approved Product Lock, active Reference Style Profile, current reference version, Output Profile, and compatible controls. Never pass the failed generated image as the product source.

Repairs may target PRODUCT, COLOR, DETAILS, EDGES, BACKGROUND, LIGHTING, or COMPOSITION one category at a time. If the targeted repair fails, rerun Safe from the original source. If it fails again, mark MANUAL REVIEW.

Expose a development diagnostic containing the immutable source identifier used for the initial generation and retry. Verify both identifiers match while the generated output identifier changes.
```

## Repair download claims

Use when Download does nothing, Download All shows false success, a ZIP is promised but absent, or the Tool claims files were saved locally without evidence.

```text
Modify the existing Tool; do not rebuild it from scratch. Preserve all unrelated working behavior, labels, controls, and verified tests.

Repair download and storage claims only.

Keep a per-output Download control only when it invokes a real Flow-supported export or browser download and receives a real completion signal. Report success only after that signal. If the action is unavailable, disable or hide the control and explain that the output remains in the Flow project according to current platform behavior.

Show Download All only when the generated runtime truly exports every completed output. If ZIP creation or multi-file export is unsupported, remove Download All. Do not simulate progress, fabricate a ZIP, display a false saved path, or claim automatic local saving.

Do not promise retention duration. Tell the user to verify downloaded files on the local machine. Test one single output and a three-item Batch; record the filenames actually received. The repair passes only when every displayed success corresponds to an observable completed download.
```

## Repair UI separation

Use when the interface has one mixed analysis panel, unclear image roles, controls with misleading effects, or no per-item QA.

```text
Modify the existing Tool; do not rebuild it from scratch. Preserve all unrelated working behavior, labels, controls, and verified tests.

Repair visible UI separation and control semantics only; do not alter already verified generation behavior.

Create distinct, persistent areas labeled PRODUCT SOURCE, STYLE REFERENCE, and GENERATED OUTPUT. Replace any mixed “Vision Analysis” with a Product Analysis card containing product facts only and a Reference Style Profile card containing background-treatment facts and exclusions only. Show a separate QA card for the selected output.

Keep sidebar controls named SINGLE / BATCH EXPERIMENTAL, SAFE / FAST, REFERENCE-FIRST / STRICT MATCH, ECOMMERCE / SOCIAL / BOTH, Aspect Ratio, Product Scale, and Detail Recovery. Product Scale must say that it changes compatible canvas occupancy and spacing only. Detail Recovery must say that it strengthens preservation guidance and never relaxes Product Lock.

Disable Run when a role is missing. In Safe mode, display Product detected, Product Lock, Reference Style Profile, Excluded from reference, Background mode, Risks, and APPROVE & GENERATE before generation. In Batch, show one independent row and QA status per product.

Verify from Preview that a user can identify the authoritative Product Source, the style-only reference, the selected job, the active background mode, whether generation is approved, and the result's PASS/WARN/FAIL state without opening Code.
```

