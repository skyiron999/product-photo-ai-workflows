# Strict Match

`STRICT MATCH` is an optional reference-adherence mode. The mode must minimize creative interpretation and reproduce the active style reference's transferable background treatment as closely as the current generative interface allows. It is not a pixel-copying mode. `STRICT MATCH OFF` returns to normal Reference-first behavior without discarding the active reference.

## Preconditions

Strict Match requires an explicitly mapped style-reference image. If none exists, pause and request one before editing. Build or refresh the Reference Style Profile from that image. In this mode, do not use a Style Card, nearest preset, or hidden preset guidance.

## Matching target

Match every observable and transferable background attribute:

- color family, relative tonal values, saturation, and color temperature;
- surface material and finish;
- texture or grain character, scale, density, and contrast;
- gradient, vignette, illumination falloff, and light/dark distribution;
- light direction, diffusion, softness, and contrast;
- contact-shadow direction, softness, density, and grounding character;
- overall background mood and negative-space treatment.

Minimize creative interpretation. Do not reinterpret, beautify, substitute the palette, add props or typography, or introduce decorative elements. Only the minimum contact-shadow adaptation required to ground the locked product is allowed.

## Safety and unavailable pixels

Product Lock remains higher priority than Strict Match. Never recolor, relight, reshape, crop, distort, or rebuild the product to improve the background match. Exclude reference products, props, people, packages, text, logos, and watermarks.

When objects hide part of the reference background or a new aspect ratio exposes unseen canvas, reconstruct those regions and disclose them as unverifiable rather than claiming equality.

## Run and batch state

Safe Run reports the match target and reconstructed regions before `CONTINUE`. Fast Run performs the same analysis internally. `NEXT PRODUCT` clears the previous product source and Product Lock while retaining Strict Match and the Reference Style Profile unless the user changes them.

## Required reporting

Before editing in Safe Run:

```text
Background mode: STRICT MATCH
Match target: <concise observable background profile>
Unseen/reconstructed regions: NONE | <named regions>
Pixel-exact guarantee: NO — generative visual match
```

After editing:

```text
Background mode: STRICT MATCH
Match assessment: PASS | WARN | FAIL
Pixel-exact guarantee: NO — generative visual match
```

`PASS` means no material visual mismatch is observable at the available inspection resolution; it never means pixel equality. `WARN` names an unverifiable or visibly approximate attribute. `FAIL` names a material background mismatch or Product Lock violation.
