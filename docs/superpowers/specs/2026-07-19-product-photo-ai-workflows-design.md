# Product Photo AI Workflows — Design Specification

Date: 2026-07-19

Status: Approved design, pending written-spec review

Repository: `product-photo-ai-workflows`

License: MIT

## 1. Summary

`Product Photo AI Workflows` is an open-source, platform-native workflow kit for editing product photos inside consumer AI chat interfaces. Version 1 focuses on replacing product-photo backgrounds while preserving the real product as faithfully as possible.

Users do not need an API, a hosted application, local image models, or standardized filenames. They choose their preferred platform, install or paste the corresponding workflow, attach a style-reference image and one or more product images, and run a guided editing process.

The repository uses a shared core plus platform adapters, product modules, style cards, and output profiles. New templates can be added without modifying the core workflow.

## 2. Goals

- Preserve the real product's geometry, color, material, construction, text, logos, and identifying details.
- Let a user replace a background by supplying a visual reference rather than writing a long prompt.
- Work directly in ChatGPT, Gemini, or Claude without requiring the user to switch platforms mid-workflow.
- Support both careful `SAFE RUN` and low-friction `FAST RUN` operation.
- Make repeated work practical for users processing approximately 100 product photos per week.
- Make templates readable, copyable, versioned, and easy for non-developers to contribute.
- Publish English as the canonical language and provide a Vietnamese quickstart and key guidance.

## 3. Non-goals for Version 1

- API automation or unattended batch processing.
- A standalone web application, desktop application, or Python image-generation application.
- Cloud asset storage.
- Background removal as a standalone transparent-cutout product.
- Virtual try-on, model replacement, product redesign, colorway generation, video generation, or 3D generation.
- Guaranteed feature parity across AI platforms.
- Training, fine-tuning, or running local image models.

## 4. Audience

Primary users are product photographers, small shops, social-media teams, and independent sellers who already know how to arrange and photograph products but need a reliable workflow for AI-assisted background replacement.

Initial product categories are:

- garments;
- fabric and folded textiles;
- earrings;
- bracelets;
- reflective accessories, including metal, stones, glass, and polished surfaces.

## 5. Product Principles

### 5.1 Product fidelity outranks style fidelity

The source product image is authoritative. A style-reference image may influence only the background, surface, lighting, shadow character, palette, contrast, and overall mood. It must not introduce products, props, logos, labels, typography, or geometry into the edited result.

### 5.2 Source-first regeneration

Every ecommerce image, social image, and repair attempt starts from the original product source. A generated output is never used as the new product source. This prevents accumulated drift.

### 5.3 One product is one isolated editing unit

Multiple product images may be attached in a small-batch workflow, but each target must be analyzed, locked, edited, and evaluated independently. Details may not transfer between targets.

### 5.4 Minimal user ceremony

Users identify images by role in the chat, not by renaming files. The standard interaction is:

1. Attach a reference image with `Use this image as the style reference only.`
2. Attach a product image with `Edit this product image.`
3. Choose a run mode and output profile.

## 6. Repository Architecture

```text
product-photo-ai-workflows/
├── README.md
├── README.vi.md
├── QUICKSTART.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md
├── .github/
│   ├── pull_request_template.md
│   └── workflows/
│       └── validate.yml
│
├── core/
│   ├── product-lock.md
│   ├── workflow-protocol.md
│   ├── safe-run.md
│   ├── fast-run.md
│   ├── repair-loop.md
│   └── quality-check.md
│
├── platforms/
│   ├── chatgpt/
│   │   ├── setup.md
│   │   ├── instant-run.md
│   │   ├── installed-instructions.md
│   │   └── limitations.md
│   ├── gemini/
│   │   ├── setup.md
│   │   ├── instant-run.md
│   │   ├── installed-instructions.md
│   │   └── limitations.md
│   └── claude/
│       ├── setup.md
│       ├── instant-run.md
│       ├── installed-instructions.md
│       └── limitations.md
│
├── products/
│   ├── garments.md
│   ├── fabric.md
│   ├── earrings.md
│   ├── bracelets.md
│   ├── reflective-accessories.md
│   └── _template.md
│
├── styles/
│   ├── sage-minimal-flatlay.md
│   ├── clean-white-studio.md
│   ├── warm-beige-editorial.md
│   ├── dark-luxury-jewelry.md
│   └── _template.md
│
├── outputs/
│   ├── ecommerce.md
│   ├── social.md
│   └── _template.md
│
├── examples/
│   └── sage-minimal-flatlay/
│       ├── README.md
│       ├── assembled-prompt.md
│       ├── lock-sheet.md
│       └── qa-report.md
│
├── tests/
│   ├── manual-test-matrix.md
│   └── cases/
│       ├── garments.md
│       ├── fabric.md
│       ├── earrings.md
│       ├── bracelets.md
│       └── reflective-accessories.md
│
└── tools/
    └── validate_templates.py
```

## 7. Template Format

Templates are Markdown files with YAML front matter. This keeps them human-readable and copyable while allowing mechanical validation.

Required metadata:

```yaml
---
id: sage-minimal-flatlay
name: Sage Minimal Flat Lay
kind: style
version: 1.0.0
compatible_with:
  - chatgpt
  - gemini
  - claude
recommended_for:
  - garments
  - fabric
  - earrings
  - bracelets
outputs:
  - ecommerce
  - social
---
```

Rules:

- `id` uses lowercase kebab-case and is unique repository-wide within its kind.
- `kind` is one of `product`, `style`, or `output`.
- `version` uses semantic versioning.
- Platform IDs, product IDs, and output IDs must resolve to known entries.
- Template bodies use clear headings and imperative language.
- No `TODO`, `TBD`, or unfilled placeholder may remain in a publishable template.

## 8. Workflow Resolution and Precedence

The workflow assembles instructions in this order:

1. Product Lock core rules.
2. The original product source image.
3. The selected or automatically detected Product Module.
4. The selected Output Profile.
5. The Style Card and style-reference image.
6. Additional user requests that do not conflict with higher-priority constraints.

If instructions conflict, the earlier item wins. Style can never override product fidelity.

## 9. Runtime Pipeline

```text
INTAKE
  Identify reference and edit target roles
        ↓
PRODUCT ANALYSIS
  Detect category, shape, color, material, construction, and identity details
        ↓
PRODUCT LOCK
  Build the invariant list
        ↓
STYLE EXTRACTION
  Extract only background, surface, palette, lighting, shadows, contrast, and mood
        ↓
RENDER BRIEF
  Assemble Product Module + Style Card + Output Profile
        ↓
IMAGE EDIT
  Change only permitted regions and attributes
        ↓
FIDELITY CHECK
  Compare source, reference, and output
        ↓
PASS / WARN / FAIL
        ↓
REPAIR or NEXT PRODUCT
```

## 10. User Modes

### 10.1 Instant Run

The user opens a new conversation on the selected platform, pastes `platforms/<platform>/instant-run.md`, and attaches images. This path requires no saved assistant or project.

### 10.2 Install Once

The user installs platform-specific instructions once using the platform's supported persistent-instruction surface. Platform setup files explain how to place behavioral rules, reference knowledge, and image-generation capabilities where available.

### 10.3 Safe Run

Before editing, the assistant displays a compact lock sheet containing:

- detected product category;
- product invariants;
- extracted style attributes;
- elements explicitly excluded from the reference;
- detected risks.

The assistant waits for `CONTINUE` before generating or editing the image.

### 10.4 Fast Run

The assistant performs the same analysis internally and continues automatically when the input is unambiguous. It pauses when:

- image roles are unclear;
- the target contains multiple products that cannot be isolated confidently;
- important text, logos, stones, clasps, or patterns are too small or obscured;
- the requested style would require changing product geometry;
- the platform lacks an applicable image-editing capability.

## 11. Short Commands

The canonical command set is:

```text
SAFE RUN
FAST RUN
ECOMMERCE
SOCIAL
BOTH
CONTINUE
NEXT PRODUCT
REPAIR PRODUCT
REPAIR COLOR
REPAIR DETAILS
REPAIR EDGES
REPAIR BACKGROUND
REPAIR LIGHTING
REPAIR COMPOSITION
START OVER FROM SOURCE
```

`NEXT PRODUCT` retains the current reference, Style Card, and Output Profile while clearing the previous source, Product Lock, generated output, and QA state.

`BOTH` creates two independent outputs from the original product source. The ecommerce result is never used to derive the social result.

## 12. Output Profiles

### 12.1 Ecommerce

Priorities:

- faithful product representation;
- restrained background and props;
- clean silhouette and realistic grounding;
- consistent crop and adequate padding;
- no generated text or watermark;
- minimal creative reinterpretation.

### 12.2 Social

Priorities:

- faithful product representation remains mandatory;
- stronger mood and art direction are allowed in the background;
- composition may reserve negative space for later copy;
- no generated copy unless the user explicitly supplies exact text;
- props remain opt-in and may never be copied accidentally from the reference.

## 13. Product-Specific Locks

### 13.1 Garments and fabric

Lock silhouette, fold arrangement, seams, collar, sleeves, buttons, closures, pattern repetition, fabric thickness, weave, texture, labels, logos, and color.

### 13.2 Earrings

Lock item count, pairing, symmetry, hooks, posts, clasps, stone count, prongs, spacing, color, metal finish, and reflections.

### 13.3 Bracelets

Lock circumference, chain or band geometry, link count where visible, charms, spacing, clasp, stones, color, metal finish, and reflections.

### 13.4 Reflective accessories

Lock geometry, edge definition, highlights that describe the real surface, engravings, glass or stone transparency, metal color, and product-specific reflections. Background reflections may adapt only when required for physical plausibility.

## 14. Quality Assurance

Every output receives one status:

- `PASS`: suitable for use under the selected profile;
- `WARN`: visually usable but contains a detail the user should inspect;
- `FAIL`: should not be used.

The QA comparison covers:

- silhouette, scale, orientation, and fold arrangement;
- color and material fidelity;
- construction details, logos, text, patterns, stones, charms, links, and clasps;
- background style and absence of copied reference objects;
- edge quality, halos, missing material, or invented material;
- lighting direction, grounding, contact shadows, reflections, and floating artifacts;
- output aspect ratio, negative space, unwanted text, and watermarking.

The assistant must not report `PASS` when a critical detail is too small or obscured to verify. It reports `WARN` and names the uncertainty.

## 15. Repair Loop

Repair is single-purpose and source-first:

1. Return to the original product source.
2. Preserve all approved style and output-profile decisions.
3. Strengthen only one failed constraint group.
4. Generate a new output.
5. Re-run QA.

After the first failure, use the relevant repair command. After a second failure, switch to `SAFE RUN`. If the same critical issue remains, return `MANUAL REVIEW` instead of retrying indefinitely.

## 16. Error Handling

- **Missing reference:** ask whether to use a Style Card alone or wait for a reference image.
- **Missing target:** request the product image and do not generate.
- **Ambiguous image roles:** ask one short clarification question.
- **Multiple targets:** confirm that each will be processed independently; do not create a collage unless explicitly requested.
- **Multiple products in one target:** pause when a single product cannot be isolated confidently.
- **Unreadable critical detail:** use `WARN` in Safe Run or pause Fast Run.
- **Unsupported platform capability:** state the limitation and provide the best workflow available on that platform without silently moving the user elsewhere.
- **Generation refusal or policy block:** report the platform response plainly and do not weaken safety constraints.
- **Repeated fidelity failure:** stop after the defined repair limit and mark `MANUAL REVIEW`.

## 17. Initial Style Cards

Version 1 ships with:

- `sage-minimal-flatlay` — pale desaturated sage surface, subtle paper-like grain, soft upper-left light, short diffused contact shadows, restrained editorial mood;
- `clean-white-studio` — neutral commercial background, controlled soft light, clean grounding, minimal visual distraction;
- `warm-beige-editorial` — warm matte surface, soft directional light, gentle contrast, fashion-editorial mood;
- `dark-luxury-jewelry` — dark controlled surface, precise specular highlights, physically plausible reflections, luxury jewelry presentation.

## 18. Examples and Asset Rights

Public examples must use assets that the repository maintainers own, generated assets that are safe to redistribute, or assets with explicit compatible licenses. The user-provided inspiration image is not included in the public repository unless redistribution rights are confirmed.

Each complete example contains:

- source image;
- reference image;
- output image;
- lock sheet;
- assembled prompt;
- QA report;
- asset provenance and license note.

## 19. Validation Tool

`tools/validate_templates.py` performs read-only validation and exits nonzero on errors. It checks:

- required front-matter fields;
- valid kinds and semantic versions;
- unique IDs;
- valid platform, product, and output references;
- publishable templates with no placeholders;
- internal Markdown links;
- required headings per template kind.

Normal workflow users do not need Python. The validator is for maintainers, contributors, and continuous integration.

GitHub Actions runs the validator for every pull request and push to the default branch. Structural validation does not claim visual quality; it only prevents malformed or internally inconsistent repository content.

## 20. Manual Visual Testing

Image fidelity cannot be established by schema validation alone. `tests/manual-test-matrix.md` records the platform, plan or feature surface, date tested, source case, workflow mode, output profile, result status, and reviewer notes.

Each Product Module has a representative case description under `tests/cases/`. Test assets are referenced only when their redistribution rights are documented. A platform-specific workflow is considered tested only for capabilities actually available in that interface at the test date. Unsupported capabilities are recorded explicitly rather than counted as passes or silently redirected to another platform.

## 21. Documentation and Localization

- `README.md` is canonical English documentation.
- `README.vi.md` provides a complete Vietnamese introduction and usage path.
- `QUICKSTART.md` is concise English and links to platform-specific setup.
- Platform prompts and templates are authored canonically in English for portability.
- Vietnamese guidance may explain usage but must not silently diverge from canonical workflow behavior.

## 22. Contribution Model

Contributors copy the relevant `_template.md`, choose a unique ID, complete metadata and required sections, add a small reproducible test case where possible, run the validator, and open a pull request.

Changes to Product Lock or workflow precedence require broader review because they affect every platform and template. New style cards or product modules should not require core changes.

## 23. Version 1 Release Criteria

Version 1 is complete when:

- ChatGPT, Gemini, and Claude each have tested Instant Run and Install Once guidance for the capabilities available in that interface;
- Safe Run, Fast Run, repair, and reset behavior are documented and tested wherever the platform exposes the required image-editing capability;
- all five Product Modules pass at least one representative test case;
- both Output Profiles are tested from the same source without derivative chaining;
- all four initial Style Cards pass schema validation;
- the validator passes on the entire repository;
- English and Vietnamese documentation are consistent;
- example assets have documented redistribution rights;
- the manual test matrix records platform, date, capability, case, and outcome;
- GitHub Actions passes the repository validator;
- no critical placeholders, broken internal links, or contradictory instructions remain.

## 24. Future Expansion

Future versions may add Product Cleanup, Shadow Creation, Color Variations, Social Media Adaptation, API automation, or a local application. These are separate modules and must not weaken the Version 1 product-fidelity contract.
