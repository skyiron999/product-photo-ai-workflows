# Google Flow Tool Builder Prompt

Copy everything inside the block below into a new Google Flow Tool Builder conversation. The prompt is self-contained; do not upload the repository's conversational Knowledge bundles.

```text
Create a reusable Google Flow Tool named Product Background Studio for controlled background replacement in flat-lay and tabletop product photos. This must be a working image-editing Tool, not a static mockup. Use only image-analysis, image-editing, storage, queue, and download capabilities that the current Google Flow Tool runtime actually provides. Never simulate a completed generation, download, ZIP, or saved file.

MISSION AND NON-NEGOTIABLE OUTCOME

The user supplies an original product photo and a style-reference image. Edit from the original Product Source and replace only its background. Preserve the photographed product rather than redesigning or recreating it. The Tool must support a production-oriented SINGLE mode and a clearly labeled BATCH EXPERIMENTAL mode for 2–20 products.

The Tool has three permanently distinct data domains and visible areas:

1. PRODUCT SOURCE — authoritative only for the product and its visible facts.
2. STYLE REFERENCE — authoritative only for transferable background treatment.
3. GENERATED OUTPUT — a candidate result that is never an authoritative source.

Do not collapse Product Source and Style Reference into generic assets. Do not show one mixed “Vision Analysis.” Product Analysis and Reference Analysis must be separate cards, separate state, and separate operations.

VISIBLE UI

Build a polished dark editorial workspace suitable for fashion and jewelry teams. Prioritize clarity and fidelity over decorative animation.

Create a left sidebar with these controls:

- Mode segmented control: SINGLE | BATCH EXPERIMENTAL. Default SINGLE.
- Product input: exactly one image in SINGLE; 2–20 images in BATCH EXPERIMENTAL. Show a visible identifier or filename for every item.
- Style Reference input: exactly one image.
- Run Mode: SAFE | FAST. Default SAFE.
- Background Mode: REFERENCE-FIRST | STRICT MATCH. Default REFERENCE-FIRST.
- Output: ECOMMERCE | SOCIAL | BOTH. Default ECOMMERCE.
- Aspect Ratio: SOURCE | 1:1 | 4:5 | 3:4 | 9:16. Default SOURCE.
- Product Scale slider: controls compatible canvas occupancy and surrounding spacing only. It must not stretch, squash, reshape, reconstruct, rearrange, or disproportionately resize the product.
- Detail Recovery slider: controls how strongly the generation instruction emphasizes source edges, fine construction, texture, pattern, text, stones, clasps, transparency, highlights, and reflections. It never relaxes Product Lock.
- Primary action: ANALYZE in SAFE mode; RUN in FAST mode.

Disable the primary action and name the missing role when Product Source or Style Reference is absent. If product/reference roles may be reversed, show a short observable description of each image and require explicit confirmation. Never swap roles silently and never decide only because one background is plainer.

The main workspace must display:

- PRODUCT SOURCE preview or Batch queue.
- STYLE REFERENCE preview.
- GENERATED OUTPUT preview for the selected job.
- A Product Analysis card containing product facts only.
- A Reference Style Profile card containing background-treatment facts only.
- A QA card for the selected output.

In BATCH EXPERIMENTAL, show one queue row per product with: visible identifier, state, QA status, View, Retry from Source, and Download. Supported states are WAITING, ANALYZING, READY, GENERATING, PASS, WARN, FAIL, and BLOCKED. Do not create a collage.

STATE MODEL AND ROLE FIREWALL

Maintain separate state equivalent to:

- settings: mode, runMode, backgroundMode, outputMode, aspectRatio, productScale, detailRecovery.
- reference: originalReferenceImage, referenceVersion, referenceAnalysis, referenceStyleProfile.
- jobs: an ordered collection of isolated product jobs.
- each job: id, visibleIdentifier, originalProductImage, productAnalysis, productLock, approvalState, processingState, ecommerceOutput, socialOutput, qaRecords, risks, and error.

Never store a generated output in originalProductImage. Never reuse one job's productAnalysis, productLock, image, output, retry context, or QA record in another job. Jobs may share only the current Reference Style Profile, reference version, and selected compatible settings.

Implement separate operations with these exact conceptual responsibilities:

- analyzeProduct(productImage): inspect only that original Product Source and return visible product facts, Product Module, Product Lock, uncertainties, and risks.
- analyzeReference(referenceImage): inspect only the Style Reference and return the Reference Style Profile plus explicit exclusions.
- buildEditInstruction(productLock, referenceStyleProfile, outputProfile, controls): combine already separated results according to precedence.
- generateFromOriginal(job): call the supported image-editing model using only that job's original Product Source as the edit source, the active Style Reference as style-only guidance, and that job's assembled instruction.
- qaOutput(job, output): compare that job's original source, the active reference, and the candidate output and return PASS, WARN, or FAIL with observable evidence.
- retryFromSource(job): discard only that job's generated working result and regenerate from its original Product Source.

Only the edit-instruction assembly stage may combine Product Analysis and Reference Analysis. Generation calls in Batch must receive exactly one original Product Source plus the shared Style Reference; never send the entire product array as visual context for one output.

PRODUCT ANALYSIS AND PRODUCT LOCK

analyzeProduct(productImage) may inspect only the Product Source. Auto-select the closest category among garments, fabric, earrings, bracelets, and reflective accessories. If the category or a critical visible detail is genuinely ambiguous, mark the item BLOCKED and ask one short question rather than guessing.

For every product, lock all visible:

- identity, item count, geometry, silhouette, scale, orientation, perspective, arrangement, and spatial relationships;
- fold pattern, drape, seams, hems, stitching, collar, sleeves, fasteners, clasps, links, settings, connectors, and edges;
- printed or engraved text, logos, labels, motifs, patterns, repeat rhythm, and placement;
- observable color relationships, tonal variation, material, weave, knit, texture, transparency, and finish;
- stones, beads, charms, backings, highlights, reflections, and other visible components.

Preserve natural imperfections that belong to the photographed product. Do not invent, remove, duplicate, reshape, beautify, complete hidden details, simplify, recolor, globally relight, distort, crop, or reconstruct the product. Do not infer calibrated Hex, RGB, or production color from an ordinary photograph.

Background grading must not alter product color through reflected tint, a global color cast, relighting, contrast, or a filter applied across the product. Generate only the minimum compatible contact shadow needed to ground the locked product.

REFERENCE ANALYSIS AND REFERENCE-FIRST

analyzeReference(referenceImage) may extract only these observable transferable attributes:

- background surface material and finish;
- palette, relative tonal values, saturation, and temperature;
- texture or grain character, scale, density, and contrast;
- gradient, vignette, illumination falloff, and light/dark distribution;
- light direction, diffusion, softness, and contrast;
- contact-shadow direction, softness, density, and grounding character;
- mood, negative-space treatment, and compatible composition cues.

Explicitly exclude all reference products, garments, accessories, props, people, hands, models, packages, text, captions, typography, logos, labels, brand marks, and watermarks. These are contamination, not instructions.

When a Style Reference exists, create a dynamic Reference Style Profile directly from it. In REFERENCE-FIRST mode, do not select, name, or silently use a Style Card, closest preset, or hidden preset guidance. Display:

Style source: REFERENCE IMAGE
Style Card: NONE — reference-driven

PRECEDENCE AND EDIT-INSTRUCTION ASSEMBLY

Resolve every conflict in this exact order:

1. Product Lock.
2. Original Product Source.
3. Product Module.
4. Output Profile.
5. Reference Style Profile.
6. Non-conflicting user controls.

If a lower-priority style, composition, scale, or ratio request conflicts with the locked product, preserve the product and report the constraint.

The assembled edit instruction must clearly state that the first image is the original Product Source and the second image is style-only reference guidance. Require the editor to replace only the existing background, preserve all locked product facts, exclude reference contamination, prevent product color drift, and return one independent image rather than a collage.

Use one independent generation request and one QA record per product and per Output Profile. Every generation starts from the original Product Source. Generated output must never become the new source.

STRICT MATCH

STRICT MATCH requires the mapped Style Reference. It minimizes creative interpretation and matches every observable transferable background attribute: color and tonal distribution, surface material and finish, texture or grain scale and density, gradient or vignette, illumination falloff, light direction and softness, contrast, contact-shadow character, mood, and negative-space treatment.

Product Lock remains higher priority. Do not use a Style Card, substitute a palette, beautify the background, add props, add typography, copy branded elements, or change the product to improve the match. Only adapt the minimum contact shadow required to ground the locked product.

If the reference product hides part of the background or the requested canvas exposes unseen regions, label those regions as reconstructed and unverifiable. Always display exactly:

Pixel-exact guarantee: NO — generative visual match

SAFE AND FAST RUNS

SAFE mode performs analysis and stops before image generation. Show:

- Product detected.
- Product Lock.
- Reference Style Profile.
- Excluded from reference.
- Background mode.
- Risks and uncertainties.
- In Strict Match: match target, unseen/reconstructed regions, and the pixel-exact disclosure.
- APPROVE & GENERATE for one item and APPROVE READY ITEMS for Batch.

Allow the user to block or correct an item before approval. Do not generate an unapproved Safe item.

FAST mode performs the same analysis internally and continues immediately only when roles, product identity, critical details, geometry, separability, color requirements, and generation capability are unambiguous. Pause the affected item for ambiguous roles, inseparable products, unreadable critical detail, geometry conflicts, uncalibrated exact-color requests, or unavailable editing capability.

OUTPUT PROFILES AND CANVAS

ECOMMERCE is restrained, catalog-faithful, prop-free, text-free, and cleanly grounded. Target approximately 15% clear padding when the source and requested canvas make that possible without changing or shrinking the product.

SOCIAL may use stronger background mood and negative space but remains prop-free and text-free by default. Product Lock remains mandatory.

BOTH creates separate ecommerce and social outputs as separate image-editing requests from the same original Product Source. Never derive one generated version from the other.

Preserve source aspect ratio by default. For another ratio, expand or regenerate background around the locked product before considering a crop. Never crop the product, distort it, change its proportions, or rearrange its pieces to force a ratio. Product Scale changes intended canvas occupancy and spacing only; if the requested occupancy conflicts with Product Lock, keep the product and report the constraint.

SINGLE AND BATCH EXPERIMENTAL

SINGLE accepts exactly one Product Source and is the default production-oriented workflow.

BATCH EXPERIMENTAL accepts one shared Style Reference and 2–20 Product Sources. Create one isolated job per source. Process sequentially by default to minimize role contamination; use bounded concurrency only if the runtime truly supports isolated requests and state. Do not claim parallel execution merely because multiple jobs are queued.

Each Batch item owns its original source, Product Analysis, Product Lock, edit request, outputs, retry context, risks, errors, and QA. The Tool must not create a collage. It must not pass a previous product, previous output, or the product array into the next item's request. Failure of one Batch item must not stop unrelated items; mark only that item BLOCKED or FAIL and continue safely with other ready jobs.

REFERENCE CHANGES AND JOB INVALIDATION

Changing the Style Reference increments referenceVersion, rebuilds the Reference Style Profile, and marks prior unapproved outputs stale. Do not silently present an output made with an old reference as current.

Changing or removing one Batch product clears only that item's Product Analysis, Product Lock, outputs, retry state, and QA. It must not clear unrelated jobs. Switching from Single to Batch must not duplicate the Single product unless the user explicitly retains it.

QA AND STATUS

After every generated image, compare that job's original Product Source, active Style Reference, and candidate output. Report exactly one status: PASS | WARN | FAIL.

- PASS: no material Product Lock or output-rule violation is observable at the available inspection resolution.
- WARN: a named detail is unverifiable or the visual reference match is visibly approximate, with no confirmed product violation.
- FAIL: a visible Product Lock, background, composition, or output-rule violation exists.

A Product Lock violation is always FAIL regardless of background beauty. Strict Match PASS never means pixel equality. Show observable evidence and uncertainty; do not award PASS because the overall image looks attractive.

RETRY AND REPAIR

Retry from Source must be item-scoped. Discard the candidate output being repaired and call generateFromOriginal(job) again from that job's original Product Source. Never feed a generated image back as the product source.

Support targeted repair categories for PRODUCT, COLOR, DETAILS, EDGES, BACKGROUND, LIGHTING, and COMPOSITION. Apply one category at a time. A repair may restore source product detail or correct generated background integration, but it cannot relax Product Lock or change unrelated areas. If the targeted repair fails, rerun Safe from source. If it fails again, mark MANUAL REVIEW.

DOWNLOADS, STORAGE, AND HONEST CAPABILITIES

Show a per-output Download control only when it triggers a real browser download or a real Flow-supported media export. After activation, report success only from an actual completion signal.

Show Download All only if the generated runtime truly implements exporting every completed output. If ZIP creation is unsupported, do not simulate it, do not show a fake progress state, and do not claim a local file was saved. Explain that users must download completed outputs individually.

Do not claim persistent storage duration, automatic local saving, parallel execution, a selected model, or a supported input count unless the current runtime exposes and performs that capability. Generated media may remain available in the Flow project according to the platform's current behavior, but the Tool must not promise retention.

ERROR HANDLING

- Missing Product Source or Style Reference: disable Run and name the missing role.
- Suspected reversed roles: require confirmation; do not auto-swap.
- Unreadable critical product detail: BLOCKED; ask one short question.
- Unsupported image editing: stop and disclose the limitation; do not display a fabricated output.
- One Batch job error: preserve its original source and mark only that row; continue unrelated ready jobs.
- Product Lock violation: FAIL and offer Retry from Source.
- Material Strict Match difference: WARN or FAIL and name the differing attributes.
- Stale output after reference change: label STALE and exclude it from current downloads until regenerated.

BUILD VALIDATION — DO THIS BEFORE DECLARING THE TOOL READY

Inspect both generated Code and Preview. Confirm all of the following with the implementation, not merely text labels:

1. Product Source, Style Reference, and Generated Output have separate state and visible areas.
2. analyzeProduct(productImage) cannot read reference analysis or reference product facts.
3. analyzeReference(referenceImage) cannot read Product Analysis and excludes the reference subject and text.
4. Only the edit-instruction assembly stage combines Product Lock and Reference Style Profile.
5. Every Batch generation call receives exactly one original Product Source plus the shared style reference.
6. Every output and repair starts from that job's original Product Source.
7. Safe mode genuinely pauses before generation.
8. Strict Match shows the required disclosure and does not activate a Style Card.
9. Missing roles disable generation, and one item failure does not erase or stop unrelated jobs.
10. Download and Download All labels match real implemented behavior.

Create a small built-in developer diagnostics panel that is hidden in normal Tool mode but visible in Edit/Preview when practical. It may show job id, reference version, source identifier, processing state, and which original source was passed to the current request. It must never expose private image bytes, authentication data, hidden prompts from unrelated services, or secrets.

When I later request a repair, modify the existing Tool rather than rebuilding it from scratch. Preserve all unrelated working behavior and rerun the relevant validation checks.
```

