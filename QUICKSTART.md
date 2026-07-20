# Quickstart

**English** · [Tiếng Việt](QUICKSTART.vi.md)

Your first controlled product-background edit takes seven decisions, not a custom technical setup.

## 1. Choose a platform

- [ChatGPT setup](platforms/chatgpt/setup.md)
- [Gemini setup](platforms/gemini/setup.md)
- [Claude setup](platforms/claude/setup.md)

Use the interface you already have. Platform packages share workflow rules but do not promise identical model behavior.

## 2. Choose Instant Run or Install Once

- **Instant Run:** paste the platform's `instant-run.md` into a new conversation. Best for evaluation and occasional work.
- **Install Once:** follow `setup.md` to create a Custom GPT, Gem, or Claude Project and upload the four ready-made files in [`bundles/`](bundles/README.md) as Knowledge. Best for repeated batches.

Claude must confirm that the current interface has a real image-editing tool. Without one, it produces analysis and a render brief—not a raster edit.

## 3. Attach the style reference

Send the reference with this role sentence:

> Use this image as the style reference only. Extract the background, lighting, contact shadow, palette, mood, and spacing. Do not copy its product, props, text, logos, or watermark.

The workflow must create a dynamic Reference Style Profile from this image and report `Style source: REFERENCE IMAGE` plus `Style Card: NONE — reference-driven`. It must not map the reference to the nearest named preset. Style Cards are used only when no reference exists or you explicitly request one.

## 4. Attach the product target

Send the photo to edit with:

> This is the original product source. Replace only its background. Preserve the complete product and use this image as the source for every edit or repair.

Repeat that message for each target. Ordinary filenames are fine. When several unlabeled images arrive together, confirm the proposed role mapping before continuing.

## 5. Choose mode and output

For the first product, send:

```text
SAFE RUN ECOMMERCE
```

Review Product detected, Locked, Style extracted, Excluded from reference, and Risks. Correct anything wrong, then send `CONTINUE`.

For a familiar setup, use `FAST RUN`. Choose `ECOMMERCE`, `SOCIAL`, or `BOTH`. Both means separate outputs, not a collage.

## 6. Review QA

Place source and output side by side. Inspect geometry, silhouette, folds, seams, texture, product color, pattern, text, stones, clasps, edges, transparency, highlights, reflections, padding, crop, and reference contamination.

- `PASS`: inspectable locks and output rules are satisfied.
- `WARN`: no verified violation is visible, but named details cannot be confirmed.
- `FAIL`: a visible defect needs one targeted repair.
- `MANUAL REVIEW`: automated repair is exhausted or capability is insufficient.

## 7. Repair or continue the batch

Use one matching command: `REPAIR PRODUCT`, `REPAIR COLOR`, `REPAIR DETAILS`, `REPAIR EDGES`, `REPAIR BACKGROUND`, `REPAIR LIGHTING`, or `REPAIR COMPOSITION`.

The repair must return to the original product source. If it fails, run Safe Run again from source. If that also fails, stop at `MANUAL REVIEW`.

When the image is accepted, send `NEXT PRODUCT`. The workflow retains the Reference Style Profile, mode, and output settings but clears the prior source and Product Lock.
