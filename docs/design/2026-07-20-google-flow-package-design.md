# Google Flow Tool Package Design

**Date:** 2026-07-20  
**Status:** Approved design, pending implementation plan  
**Target:** Google Flow Tool Builder

## Purpose

Add a self-contained Google Flow package to Product Photo AI Workflows. Its primary artifact is a builder prompt that a non-technical user can paste into Google Flow Tool Builder to create a reusable product-background editing tool.

The Tool supports a stable single-product workflow and an explicitly experimental batch workflow for 2–20 products. Both use the repository's Product Lock, Reference-first, Strict Match, output, QA, and source-first repair contracts.

This package runs inside Google Flow. It does not add an API service, Python runner, cloud-storage layer, or external image host.

## Package Contents

Create the following platform package:

```text
platforms/google-flow/
├── builder-prompt.md
├── repair-prompts.md
├── acceptance-checklist.md
├── setup.md
├── setup.vi.md
└── limitations.md
```

- `builder-prompt.md` is the primary, copy-paste artifact. It contains all behavior required to build the Tool without Knowledge uploads.
- `repair-prompts.md` contains narrow follow-up prompts for correcting one Tool Builder defect without rebuilding unrelated behavior.
- `acceptance-checklist.md` defines observable PASS/FAIL checks before a Tool snapshot is shared.
- `setup.md` and `setup.vi.md` explain creation, testing, repair, sharing, and version updates.
- `limitations.md` documents generative fidelity, credit usage, experimental batch behavior, download capability, snapshot sharing, and privacy considerations.

## Data Boundaries

The generated Tool must maintain three separate domains:

1. **Product Source** supplies product identity and visible facts only.
2. **Style Reference** supplies transferable background treatment only.
3. **Generated Output** contains results and is never an authoritative input source.

Product and reference analysis must be independent:

```text
Product Source → Product Analysis → Product Lock ┐
                                                  ├→ Edit original Product → QA → Output
Style Reference → Reference Analysis → Style Profile ┘
```

`analyzeProduct(productImage)` must not describe or inherit reference-image attributes. `analyzeReference(referenceImage)` must extract only background surface, palette, texture, tonal variation, lighting, contact shadow, mood, negative space, and compatible composition. It must exclude products, props, people, packages, text, logos, labels, brand marks, and watermarks.

Only the edit-instruction assembly stage may combine a Product Lock with a Reference Style Profile. The final instruction follows this precedence:

1. Product Lock
2. Original Product Source
3. Product Module
4. Output Profile
5. Reference Style Profile
6. Non-conflicting user controls

## Tool Modes

### Single

Single mode accepts one Product Source and one Style Reference and produces one independently reviewable output per selected Output Profile. This is the default and production-oriented mode.

### Batch Experimental

Batch mode accepts one shared Style Reference and 2–20 Product Sources. It creates an isolated job for each product. Each job owns its Product Source, Product Lock, edit request, output, and QA result.

The Reference Style Profile and selected run/output settings may be shared. Product analysis, locks, generation context, retry context, output, and QA must not be shared between jobs. A failed item does not stop unrelated items. The Tool must not create a collage or use a previous product or generated output as context for another item.

The Tool may use sequential processing or bounded concurrency, depending on the runtime available. It must not claim parallel execution unless that behavior actually exists.

## User Interface

The sidebar exposes:

- Mode: `SINGLE` or `BATCH EXPERIMENTAL`
- Product input: one image in Single, 2–20 images in Batch
- Style Reference input: exactly one image
- Run Mode: `SAFE` or `FAST`
- Background Mode: `REFERENCE-FIRST` or `STRICT MATCH`
- Output: `ECOMMERCE`, `SOCIAL`, or `BOTH`
- Aspect Ratio: source, `1:1`, `4:5`, `3:4`, or `9:16`
- Product Scale
- Detail Recovery
- Run action

The main workspace displays three named areas: `PRODUCT SOURCE`, `STYLE REFERENCE`, and `GENERATED OUTPUT`. Product and reference analyses remain visibly separate.

Product Scale controls compatible canvas occupancy and spacing; it does not authorize distortion, disproportionate resizing, rearrangement, cropping, or reconstruction. Detail Recovery changes the strength of edge/detail preservation guidance; it does not relax Product Lock.

## Run Behavior

Safe Run analyzes inputs and pauses before generation. It displays:

- Product detected
- Product Lock
- Reference Style Profile
- Excluded from reference
- Background mode
- Risks
- `APPROVE & GENERATE`

Fast Run performs the same checks internally and proceeds unless image roles, critical product facts, geometry, exact color, separability, or model capability are ambiguous.

Reference-first is the default background mode. When a reference exists, the Tool builds a dynamic Reference Style Profile and must not select, name, or silently use a similar Style Card.

Strict Match requires a mapped reference and minimizes creative interpretation. It matches observable background color and tonal distribution, surface material and finish, texture scale/density, gradient or vignette, illumination falloff, light direction/softness, contrast, contact-shadow character, mood, and negative-space treatment. Product Lock remains higher priority. The UI and reports must state:

```text
Pixel-exact guarantee: NO — generative visual match
```

`BOTH` creates separate ecommerce and social outputs from the original Product Source. It must not transform one generated output into the other.

## Product Preservation

For every product, the Tool locks visible identity, count, geometry, silhouette, scale, orientation, perspective, arrangement, folds, construction, edges, text, logos, labels, patterns, observable color relationships, material, texture, transparency, components, highlights, and reflections.

The Tool must not invent, remove, duplicate, reshape, beautify, complete hidden details, or borrow products or props from the reference. Background treatment must not recolor or globally relight the product. Only the minimum compatible contact shadow may be generated to ground the locked product.

Exact Hex, RGB, or production-color accuracy must not be inferred from an ordinary uncalibrated photograph.

## State and Repair

Every generated image and every repair starts from its original Product Source. Generated output must never become the new source.

Retry actions are item-scoped in Batch mode. A retry clears that item's generated working result while retaining its original source, approved Product Lock, active Reference Style Profile, and compatible settings.

Changing the reference rebuilds the Reference Style Profile and invalidates prior unapproved outputs. Changing or removing one Batch product clears only that product's lock and outputs.

## QA and Status

Each output receives exactly one status:

- `PASS`: no material Product Lock or output-rule violation is observable at the available inspection resolution.
- `WARN`: a detail is unverifiable or the visual reference match is visibly approximate but no clear product violation is confirmed.
- `FAIL`: a visible Product Lock, background, composition, or output-rule violation exists.

Strict Match PASS never means pixel equality. A Product Lock violation is always FAIL, regardless of background quality.

Batch mode shows one queue row per product with its filename or visible identifier, processing state, QA status, View action, Retry from Source action, and Download action. `Download All` appears only if the generated runtime truly implements it. The Tool must not claim that a ZIP or local file was saved when no such action completed.

## Error Handling

- Missing Product or Reference disables generation and names the missing role.
- Suspected reversed roles require confirmation rather than automatic swapping.
- Unreadable critical product details pause the affected job rather than inventing them.
- Failure of one Batch item does not terminate unrelated items.
- Product Lock violations produce FAIL and an item-scoped retry from source.
- Material Strict Match differences produce WARN or FAIL with the differing attributes named.
- Unsupported generation, download, storage, concurrency, or model features are disclosed instead of simulated.

## Builder Prompt Contract

The builder prompt must:

1. Require stable business labels and forbid collapsing Product Source and Style Reference into one generic asset role.
2. Require separate state for original product sources, active reference, per-product locks, Reference Style Profile, outputs, and QA.
3. Require independent product and reference analysis before instruction assembly.
4. Encode Product Lock precedence and Reference-first behavior directly.
5. Include Strict Match and its non-pixel-exact disclosure.
6. Exclude reference products, props, people, packages, typography, logos, labels, and watermarks.
7. Prevent global product recoloring, relighting, redesign, distortion, and reconstruction.
8. Require one independent generation request and QA record per product.
9. Require source-first repair and item-scoped retries.
10. Forbid claims about ZIP, local storage, parallelism, or model/runtime capabilities that are not implemented.
11. Ask Tool Builder to preserve working behavior when applying later repair prompts.

The prompt is self-contained and does not require the four conversational Knowledge bundles.

## Repair Prompts

Repair prompts target one defect category at a time:

- role or state contamination;
- Product Lock omissions;
- Reference-first or Strict Match behavior;
- Safe/Fast run behavior;
- Single/Batch isolation;
- queue and per-item failure behavior;
- source-first retry;
- output/download claims;
- UI labels and analysis separation.

Every repair prompt instructs Tool Builder to preserve unrelated working features and rerun the relevant acceptance checks.

## Acceptance Tests

The acceptance checklist covers:

1. a patterned garment or fabric;
2. reflective jewelry;
3. a reference containing a different product;
4. a reference containing typography or a logo;
5. Reference-first without Style Card selection;
6. Strict Match with required disclosure;
7. a Batch run with at least three distinct products;
8. one failing Batch item while unrelated items continue;
9. reference replacement and profile invalidation;
10. `BOTH` producing independent outputs from the original source;
11. retry starting from the original Product Source;
12. download controls matching actual runtime behavior.

The Tool fails acceptance if Product Analysis contains attributes taken from the reference product, Reference Analysis contains transferable facts from the Product Source, jobs share product identity, generated results are reused as sources, or unsupported features are presented as completed.

## Repository Integration

Implementation updates English and Vietnamese README and Quickstart documents to list Google Flow as a fourth platform. The changelog records the new package. Platform-package tests gain Google Flow-specific required files and contract assertions without forcing the conversational package's five-file shape onto the Tool Builder adapter.

Automated tests verify required contract language and package links. They do not claim visual generation success. Visual fidelity and runtime behavior remain manual acceptance tests recorded honestly against a named Flow Tool snapshot and test date.

## Explicit Non-Goals

The first package does not include:

- a Google API integration;
- a Python batch runner;
- external file hosting or cloud storage;
- guaranteed ZIP or automatic local saving;
- guaranteed parallel generation;
- pixel-exact background reproduction;
- autonomous approval of commercial outputs;
- on-model or ghost-mannequin workflows.

## Completion Criteria

The package is ready for implementation completion when:

- all six package files exist and cross-link correctly;
- the builder prompt contains every contract above;
- bilingual setup instructions provide a complete paste, build, test, repair, and share workflow;
- automated repository tests pass;
- the validator passes;
- the manual checklist is usable without inventing unobserved PASS results;
- README, Quickstart, and changelog accurately describe Google Flow as a Tool Builder adapter with experimental batch behavior.
