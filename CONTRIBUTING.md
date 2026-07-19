# Contributing

Thank you for helping make AI-assisted product photography more faithful, reviewable, and useful to commercial image teams. Contributions from photographers, retouchers, fashion and jewelry specialists, ecommerce operators, translators, prompt designers, and developers are welcome.

By participating, follow the project's `CODE_OF_CONDUCT.md` and submit only work you have the right to share.

## Choose the right contribution

- **Product Module:** category-specific detection, locked details, failure risks, and QA.
- **Style Card:** a reusable surface, lighting, mood, preservation, and exclusion treatment.
- **Output Profile:** composition and release constraints for a channel or business use.
- **Platform Package:** interface-specific setup, runtime behavior, and honest limitations.
- **Core workflow:** shared precedence, commands, Product Lock, QA, or repair semantics.
- **Test or example:** reproducible visual evaluation, documentation, or a rights-cleared asset.

Core and platform changes affect every user and require stricter evidence and backward-compatibility review than adding a scoped Style Card.

## Create a template

1. Copy the matching contributor file: `products/_template.md`, `styles/_template.md`, or `outputs/_template.md`.
2. Rename it to a descriptive lowercase kebab-case filename.
3. Replace contributor tokens and complete the YAML front matter:
   - `id`: unique lowercase kebab-case identifier;
   - `name`: human-readable title;
   - `kind`: `product`, `style`, or `output`;
   - `version`: semantic version such as `1.0.0`;
   - `compatible_with`: supported platforms from `chatgpt`, `gemini`, and `claude`;
   - `recommended_for`: valid Product Module IDs;
   - `outputs`: valid Output Profile IDs.
4. Keep all required headings:
   - product: `Detect`, `Lock`, `Risks`, `QA`;
   - style: `Visual intent`, `Background`, `Lighting`, `Preserve`, `Avoid`;
   - output: `Purpose`, `Composition`, `Constraints`, `QA`.
5. Write observable, testable rules. Do not claim exact color values from an ordinary photograph, perfect fidelity, or platform parity.
6. Increment the semantic version when changing the behavior of an existing published module.

Never allow a style or output contribution to override Product Lock. Never import products, props, text, logos, brand marks, labels, captions, or watermarks from a style reference by default.

## Validate locally

Use Python 3.11 or newer, install the development dependencies, and run:

```bash
python -m pip install -e '.[dev]'
python -m pytest -v
python tools/validate_templates.py .
git diff --check
```

The test suite checks schema, IDs, references, required headings, links, package contracts, public documentation, and governance. The validator must print `Validation passed.` before review.

## Record visual evidence honestly

Automated tests cannot prove product fidelity. Add or update the manual test matrix only after a real run in the named platform and interface surface.

- Record platform, surface, date, source type, case, run mode, output, status, and reviewer notes.
- Keep failed evidence; add a new row for a repair instead of rewriting history.
- Use only `PASS`, `WARN`, `FAIL`, `MANUAL REVIEW`, or the documented not-run/unsupported state.
- Do not convert an analysis-only run into an image-editing PASS.
- Test real photographed sources and supplemental synthetic cutouts separately.
- Include ratio change, ecommerce padding, reference typography contamination, and product color drift when relevant.
- Do not invent results for a platform you did not test.

## Images, privacy, and redistribution rights

Every committed image needs documented asset provenance and redistribution rights. Record the creator, owner or permission basis, source URL or durable generation record, applicable license, material edits, and intended test use. Generated assets must also record the generating tool/model and date.

Do not commit:

- client or unreleased product images without explicit authorization;
- images copied from a marketplace, social post, portfolio, or reference board without a compatible license;
- personal data or identifiable people without the required consent;
- an asset whose license is unknown, incompatible, or missing required attribution.

An MIT license on the repository does not erase a separate asset license. Keep required notices with the asset and describe the exception clearly.

## Documentation and language

English is the canonical repository language for commands, IDs, schemas, and shared technical behavior. Keep the Vietnamese README faithful in meaning whenever public positioning or user steps change. Use the established Vietnamese glossary; do not translate canonical uppercase commands.

Write for commercial image makers first. Explain the business impact of a rule and avoid promising guaranteed results.

## Pull request scope

Keep one logical change per pull request. Describe affected IDs and platforms, validation output, visual evidence, limitations, asset provenance, documentation changes, and compatibility impact. If no raster run was possible, say so directly.

Do not bundle Version 1 roadmap work—on-model, ghost mannequin, or automatic prompt export—into an unrelated contribution. Those features need a separate specification.
