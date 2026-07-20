# Google Flow Limitations

The Google Flow package constrains a generated Tool's instructions, state model, and review process. It cannot guarantee that a generative edit preserves every product pixel or reproduces a reference background exactly.

## Generative fidelity

Product Lock and QA reduce risk but do not guarantee preservation. Fine stitching, fabric texture, pattern repeats, typography, jewelry findings, stones, transparency, metal color, highlights, reflections, and edges still require side-by-side human review.

Strict Match is a generative visual-matching mode, not a pixel-copying operation. It must disclose `Pixel-exact guarantee: NO — generative visual match`.

## Tool Builder and model capability

Generated code, image-editing actions, models, controls, quotas, and supported inputs can vary by Flow version, account, subscription, region, and rollout. Inspect both Preview and Code after the initial builder prompt and after every repair prompt. A polished interface does not prove that its underlying generation, isolation, retry, or download behavior works.

If the runtime cannot edit from the uploaded Product Source, the Tool must stop and disclose that limitation rather than silently recreating the product.

## Batch Experimental

`BATCH EXPERIMENTAL` requests one reference and 2–20 isolated product jobs. It does not guarantee that the current Tool runtime supports 20 simultaneous uploads, concurrent generation, uninterrupted queue processing, or perfect separation between visual inputs.

Start with three visibly different rights-cleared products. Confirm that every output comes from its matching original source before increasing the batch size. Single mode remains the production-oriented path.

## Credits and generated media

Tool analysis, image generation, retries, and separate `BOTH` outputs may consume Google Flow credits. Credit cost and availability can change by model, plan, and platform policy. Test with a small set before processing a commercial batch, and inspect the current credit indicator in Flow rather than relying on a fixed cost in this repository.

See Google's current [AI credits information](https://support.google.com/flow/answer/16526234?hl=en).

## Downloads and project storage

Do not assume `Download All`, ZIP creation, automatic local saving, a specific filename scheme, or a guaranteed retention period. A generated Tool should expose these controls only when they complete a real supported action.

After any download, verify that the expected file exists and opens correctly on the local machine. If batch export is unavailable, download completed outputs individually from the Tool or the Flow project.

## Shared snapshots and code visibility

A shared Tool snapshot can expose the Tool name, thumbnail, and generated code to anyone with its link. Later edits may not update an already shared snapshot; create and test a new shared snapshot after material changes.

Review Google's current [Create and manage Tools guidance](https://support.google.com/flow/answer/17104535?hl=en) before sharing.

## Privacy and image rights

Review current Google data controls, privacy settings, account or workspace policy, and image rights before uploading unreleased products, client work, people, personal data, or proprietary references. Do not enable optional data-sharing settings for confidential work unless the responsible organization has approved them.

See Google's current [Flow data and privacy guidance](https://support.google.com/flow/answer/17025472?hl=en).

## Commercial release

`PASS` is a workflow status at the available inspection resolution, not a legal, marketplace, color-calibration, or product-authenticity guarantee. A human remains responsible for approving commercial outputs and retaining the source, reference, generated candidate, QA evidence, Tool snapshot, and test date required by the organization.
