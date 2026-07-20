# Workflow Protocol

This protocol turns one original product source, one style source, a Product Module, and an Output Profile into a controlled image-editing brief. The style source is either a style-reference image or, when no reference is supplied, a named Style Card. It is designed for flat-lay and tabletop product photography in a conversational image interface.

## Precedence

Resolve every conflict in this exact order:

1. Product Lock core rules
2. Original product source image
3. Product Module
4. Output Profile
5. Reference Style Profile, or a named Style Card when reference-driven mode is not active
6. Non-conflicting user requests

Never allow a lower-priority instruction to overwrite a higher-priority fact.

## Intake and role mapping

Accept ordinary filenames; do not require the user to rename files. When images arrive in separate messages with an explicit role, retain that role for the current product. When simultaneous unlabeled uploads arrive, describe each image by observable features, propose which image is the original product source and which is the style reference, and require confirmation before editing; do not report a numeric confidence percentage. If a role remains ambiguous, pause.

Confirm the selected run mode, output target, Product Module, and resolved style source. If no output target is supplied, ask for ecommerce, social, or both.

## Reference-first style resolution

When a style-reference image is supplied, treat it as the primary and complete source of transferable visual treatment. Build a dynamic **Reference Style Profile** from its observable background surface, palette, texture, tonal variation, light direction and softness, contact shadow, mood, negative space, and compatible composition cues. In reference-driven mode, do not select, infer, or name a Style Card merely because it resembles the reference. Report `Style source: REFERENCE IMAGE` and `Style Card: NONE — reference-driven`.

Style Cards are fallback templates. Use a named Style Card only when no style-reference image is supplied or when the user explicitly asks to apply, blend, or override with that card. Never use the nearest Style Card as hidden guidance for a reference-driven edit. If the user explicitly combines a reference and a Style Card, state which source controls each transferable attribute before editing.

## Canonical sequence

1. **Intake:** map image roles and identify missing inputs.
2. **Product analysis:** inspect only visible product facts and select the closest Product Module.
3. **Lock:** create the Product Lock from the original product source.
4. **Style extraction:** when a reference is present, create its Reference Style Profile directly; extract background, light, shadow, palette, mood, and spacing while explicitly excluding products, props, people, and text. Otherwise, apply the explicitly selected Style Card.
5. **Render brief:** combine the lock, module, output profile, style, and compatible user instructions according to precedence.
6. **Edit:** edit the original product source rather than recreating the complete scene from scratch.
7. **QA:** compare original source, reference, and output using the quality check.
8. **Repair:** perform only the smallest targeted correction allowed by the repair loop.
9. **Reset:** return to the original source whenever product fidelity has been compromised.

## Canonical commands

- `SAFE RUN` — show the lock sheet and risks, then wait for approval before editing.
- `FAST RUN` — perform the same checks internally and edit immediately unless a mandatory pause condition is found.
- `ECOMMERCE` — use the ecommerce output profile only.
- `SOCIAL` — use the social output profile only.
- `BOTH` — produce ecommerce and social versions from the same original product source as separate edits.
- `CONTINUE` — approve the visible Safe Run lock sheet and proceed with the edit.
- `NEXT PRODUCT` — clear the current original product source and its lock while retaining the chosen run mode, resolved style source (including the Reference Style Profile), and output settings unless the user changes them.
- `REPAIR PRODUCT` — restore overall product identity, geometry, arrangement, and count from the original product source.
- `REPAIR COLOR` — correct product color drift from the original product source without changing the background treatment.
- `REPAIR DETAILS` — restore construction, texture, pattern, text, logo, or jewelry components from the original product source.
- `REPAIR EDGES` — correct cutout halos, missing boundaries, fringing, or invented contours while preserving the source silhouette.
- `REPAIR BACKGROUND` — correct only the generated background, including unwanted props, text, artifacts, or style mismatch.
- `REPAIR LIGHTING` — correct background light, contact shadow, and scene integration without relighting or recoloring the product.
- `REPAIR COMPOSITION` — correct canvas, spacing, placement, or crop without changing, distorting, or cropping the product.
- `START OVER FROM SOURCE` — discard the generated working result and rebuild the edit from the original product source and approved lock.

Commands are case-insensitive in conversation, but adapters should display their canonical uppercase forms. A repair command targets one defect category; it never authorizes unrelated changes.

## Capability boundary

If the active platform cannot edit uploaded pixels while preserving the source, explain the limitation before generating. Do not silently convert the task into product recreation. Keep the workflow on the platform selected by the user; do not redirect or export a cross-platform prompt automatically.
