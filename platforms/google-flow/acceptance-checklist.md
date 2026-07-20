# Google Flow Tool Acceptance Checklist

Use this checklist after creating or materially repairing a Google Flow Tool. Record only behavior you actually observe. Leave every case `NOT RUN` until it has been executed against the named Tool snapshot.

## Test record

- Tool name:
- Shared snapshot URL:
- Flow plan/account context:
- Tool Builder/model information shown by Flow:
- Test date:
- Tester:
- Overall status: **NOT RUN** | PASS | WARN | FAIL

## Status rules

- `PASS` — every expected result in that case was observed and evidence was recorded.
- `WARN` — no confirmed release-blocking violation was observed, but a named result could not be verified.
- `FAIL` — an expected result was visibly violated or the Tool claimed an action it did not complete.
- `NOT RUN` — the case has not been executed against the recorded snapshot.

Do not infer a visual PASS from automated repository tests. The repository tests verify prompt and documentation contracts, not Google Flow runtime behavior.

## 1. Product Lock — patterned garment or fabric

**Inputs:** One rights-cleared patterned garment or fabric photo with visible folds, edges, construction, texture, color relationships, and motif repeat; one style reference whose subject and palette differ visibly.

**Actions:** Run `SINGLE`, `SAFE`, `REFERENCE-FIRST`, and `ECOMMERCE`. Inspect Product Analysis and Product Lock before approval, then generate.

**Expected result:** Product Analysis contains facts only from the Product Source. Output preserves silhouette, folds, edges, seams or hems, texture, motif geometry/repeat, placement, labels, and product color. No reference subject, prop, text, or logo appears.

**Evidence:** Record source/output filenames, screenshots of the two analysis cards and QA, and every inspected detail.

**Status:** **NOT RUN** | PASS | WARN | FAIL

## 2. Product Lock — reflective jewelry

**Inputs:** One rights-cleared reflective jewelry product with visible stones, settings, clasp or backing, highlights, reflections, and fine edges; one contrasting background reference.

**Actions:** Run Safe ECOMMERCE with high Detail Recovery, then inspect at a useful zoom.

**Expected result:** Count, geometry, stone count/placement, prongs, clasp/backing, metal color, transparency, highlights, reflections, engraving/text, and edges match the original Product Source. Background color does not tint the product.

**Evidence:** Record side-by-side crops and the QA evidence for each critical component.

**Status:** **NOT RUN** | PASS | WARN | FAIL

## 3. Reference contains a different product

**Inputs:** Target Product Source A and a Style Reference containing a clearly different product B.

**Actions:** Run Safe Reference-first and inspect analysis before generation.

**Expected result:** Product Analysis describes only A. Reference Style Profile describes background treatment and explicitly excludes B. The generated output contains A only and borrows no geometry, construction, pattern, accessory, or prop from B.

**Evidence:** Record both analysis cards and the output region where contamination would be most visible.

**Status:** **NOT RUN** | PASS | WARN | FAIL

## 4. Reference contains typography or logo

**Inputs:** A Product Source without requested output text and a Style Reference containing visible typography or logo content.

**Actions:** Run Single Safe Reference-first.

**Expected result:** Reference analysis lists typography and logo as excluded contamination. Output contains no copied, approximated, or invented reference text, logo, caption, label, watermark, or brand mark.

**Evidence:** Record the exclusion list and a full output screenshot.

**Status:** **NOT RUN** | PASS | WARN | FAIL

## 5. Reference-first does not select a Style Card

**Inputs:** One Product Source and one distinctive Style Reference.

**Actions:** Select `REFERENCE-FIRST`, analyze, and inspect all visible style labels and any developer diagnostics.

**Expected result:** Tool displays `Style source: REFERENCE IMAGE` and `Style Card: NONE — reference-driven`. No named preset, closest Style Card, or hidden preset selection is visible in Code or diagnostics.

**Evidence:** Record analysis panel and the relevant generated-code location or diagnostic.

**Status:** **NOT RUN** | PASS | WARN | FAIL

## 6. Strict Match disclosure and priority

**Inputs:** One Product Source and a reference with observable surface texture, tonal distribution, gradient, lighting, and contact shadow.

**Actions:** Select `STRICT MATCH` and Safe. Inspect the pre-generation report, then generate and inspect QA.

**Expected result:** Safe report names the match target and unseen/reconstructed regions, does not use a Style Card, and displays `Pixel-exact guarantee: NO — generative visual match`. Product Lock remains higher priority. QA includes Match assessment and never equates PASS with pixel equality.

**Evidence:** Record pre-generation and post-generation panels.

**Status:** **NOT RUN** | PASS | WARN | FAIL

## 7. Batch isolation with at least three distinct products

**Inputs:** One shared Style Reference and at least three distinct products whose color, shape, category, or construction makes cross-contamination easy to see.

**Actions:** Run `BATCH EXPERIMENTAL`, Safe, and ECOMMERCE. Review each lock, approve ready items, and inspect every result and job diagnostic.

**Expected result:** There is one queue row, original source, Product Lock, independent generation request, output, and QA record per product. Every generation request receives only its matching original Product Source plus the shared reference. No collage, product merge, or prior-output context appears.

**Evidence:** Record the queue, source-to-output mapping, job identifiers, and diagnostics.

**Status:** **NOT RUN** | PASS | WARN | FAIL

## 8. Failure of one item does not stop the Batch

**Inputs:** A Batch with at least three products, including one input that is intentionally unsupported, unreadable, or missing a critical separable product boundary.

**Actions:** Start the Batch and observe job-state changes without correcting the failing item.

**Expected result:** The affected row becomes BLOCKED or FAIL with a specific reason. Unrelated ready items continue safely and retain their source, locks, outputs, and QA. The queue is not globally erased or marked successful.

**Evidence:** Record the queue before, during, and after the item failure.

**Status:** **NOT RUN** | PASS | WARN | FAIL

## 9. Reference replacement invalidates stale results

**Inputs:** One Product Source, Reference A, and visibly different Reference B.

**Actions:** Analyze or generate with A, then replace it with B without replacing the Product Source.

**Expected result:** The Tool increments or changes reference version, rebuilds the Reference Style Profile, and labels prior unapproved outputs STALE. Regeneration uses B. It does not silently present the output from A as current.

**Evidence:** Record both reference profiles, versions, stale state, and regenerated output.

**Status:** **NOT RUN** | PASS | WARN | FAIL

## 10. BOTH creates independent outputs from source

**Inputs:** One Product Source and one Style Reference.

**Actions:** Select `BOTH` and generate.

**Expected result:** Ecommerce and Social are separate requests that both start from the same original Product Source. Neither generated version is used as the source for the other. Both receive separate QA records and are not combined into a collage.

**Evidence:** Record request diagnostics, both outputs, and both QA records.

**Status:** **NOT RUN** | PASS | WARN | FAIL

## 11. Retry from Source is truly source-first

**Inputs:** One generated result with a clearly identified repair category.

**Actions:** Record the immutable source identifier, choose `Retry from Source`, and compare the initial and retry diagnostics.

**Expected result:** Both generation attempts use the identical original Product Source identifier. The failed generated candidate is discarded rather than reused as source. Only the targeted repair category changes; unrelated Product Lock facts remain binding.

**Evidence:** Record source identifiers, output identifiers, repair category, and before/after QA.

**Status:** **NOT RUN** | PASS | WARN | FAIL

## 12. Download controls match real behavior

**Inputs:** One completed Single output and, if supported, at least two completed Batch outputs.

**Actions:** Trigger every visible Download control and any visible Download All control. Inspect the browser completion signal and local files.

**Expected result:** Every displayed success corresponds to a file that exists and opens locally. Download All appears only if all completed outputs are actually exported. Unsupported ZIP or multi-download behavior is absent or clearly disabled; no fake local path or automatic-save claim appears.

**Evidence:** Record control state, completion signal, received filenames, file count, and file-open verification.

**Status:** **NOT RUN** | PASS | WARN | FAIL

## Release gate

The shared snapshot is **FAIL** and must not be presented as production-ready if any of these are observed:

- Product Analysis contains attributes from the reference subject.
- Reference Analysis contains Product Source facts instead of only background treatment.
- A product, prop, person, package, typography, logo, label, brand mark, or watermark is copied from the reference.
- Product identity, count, geometry, construction, color relationships, material, pattern, text, components, highlights, reflections, or edges change materially.
- Batch jobs share product identity, images, locks, outputs, retry state, or QA.
- A generated output is reused as Product Source.
- Safe mode generates before approval.
- Reference-first silently selects a Style Card.
- Strict Match claims pixel equality or omits its disclosure.
- A Download, Download All, ZIP, local-save, parallel-processing, or storage claim is displayed without implemented observable behavior.
- A case is marked PASS without recorded evidence.

## Final decision

- Release decision: **NOT RUN** | APPROVE FOR PILOT | APPROVE WITH WARNINGS | REJECT
- Approved modes:
- Maximum observed Batch size:
- Known warnings:
- Required manual review:
- Next snapshot/version action:
