---
id: ecommerce
name: Ecommerce Catalog
kind: output
version: 1.0.0
compatible_with: [chatgpt, gemini, claude]
recommended_for: [garments, fabric, earrings, bracelets, reflective-accessories]
outputs: [ecommerce]
---
# Ecommerce Catalog

## Purpose

Create a faithful, commercially usable product image with restrained styling and minimal reinterpretation. Product recognition, accurate comparison, and a clean catalog presentation take priority over drama.

## Composition

Preserve the source canvas ratio and product scale by default. Center or balance the locked arrangement without rotating or rearranging it. Target at least 15% safe padding from the product's outermost edge when possible without altering product geometry. Use a clean silhouette, restrained background, and realistic contact shadow.

## Constraints

When another ratio is requested, expand only the background before considering a crop; never rescale, distort, or crop the product. Do not generate text, captions, labels, logos, decorative typography, or watermarks. Do not add props. Keep background treatment from recoloring or relighting the product.

## QA

Require Product Lock `PASS`, clean edges, realistic grounding, consistent clear space, and no reference contamination. Treat insufficient canvas, unverifiable critical details, or uncalibrated exact-color requirements as a warning or manual review rather than changing the product.
