---
id: reflective-accessories
name: Reflective Accessories
kind: product
version: 1.0.0
compatible_with: [chatgpt, gemini, claude]
recommended_for: [reflective-accessories]
outputs: [ecommerce, social]
---
# Reflective Accessories

Use for polished metal, glass, crystal, mirrored, lacquered, and mixed reflective accessories not covered by a more specific module.

## Detect

Identify product count, geometry, bevels, polished edges, engravings, transparent or translucent regions, stones or glass, metal parts, surface finish, highlight paths, and visible environment reflections.

## Lock

Preserve geometry, proportions, openings, engravings, polished edges, glass or stone transparency, refraction cues, metal color, surface finish, highlights, and all identity details. Background reflections may change only where physically required by the new scene and must remain plausible; they must not repaint the base material or conceal construction.

## Risks

Reflection replacement can bend geometry, erase engravings, introduce impossible light sources, shift metal color, make glass opaque, or create false components. Separate a reflected background tint from the object's intrinsic color before judging drift.

## QA

Compare hard contours and engraved landmarks first. Verify that highlight shapes follow the locked surface, transparent areas retain depth, metal color remains stable, and new background reflections are coherent with the requested light and contact plane.
