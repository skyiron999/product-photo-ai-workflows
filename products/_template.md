---
id: product-template
name: Product Module Template
kind: product
version: 1.0.0
compatible_with: [chatgpt, gemini, claude]
recommended_for: [product-template]
outputs: [ecommerce, social]
---
# YOUR PRODUCT NAME

Explain what products and photographic setups this module covers.

## Detect

YOUR TEXT: list the observable features the assistant must identify before editing.

## Lock

YOUR TEXT: define geometry, count, material, construction, color, texture, and identity details that cannot change. Add product-specific invariants beyond the shared Product Lock.

## Risks

YOUR TEXT: name likely generative failures, ambiguities, and conditions that require a pause or warning.

## QA

YOUR TEXT: provide a practical source-to-output inspection order and product-specific checks.
