# Google Flow Tool Setup

**English** · [Tiếng Việt](setup.vi.md)

This package builds a reusable product-background editing Tool inside Google Flow. Its primary artifact is [`builder-prompt.md`](builder-prompt.md), not an Instant Run conversation prompt.

The builder prompt is self-contained. Do **not** upload the four conversational Knowledge bundles: they duplicate instructions and can make Tool Builder mix roles or generate an unnecessarily complicated app.

## What you need

- A Google account that can open Google Flow on the web and create Tools.
- Enough current Flow credits for a small test. Analysis, generation, retries, and `BOTH` may each consume credits.
- One rights-cleared Product Source and one rights-cleared Style Reference for the first test.
- Three visibly different rights-cleared products for the Batch test.
- Permission to upload the product and reference images under your organization or client's privacy policy.

Tool creation, availability, credits, models, and controls can vary by account, subscription, region, and rollout. Read [`limitations.md`](limitations.md) before generating commercial work. Also review Google's current [Tools guidance](https://support.google.com/flow/answer/17104535?hl=en), [AI credits information](https://support.google.com/flow/answer/16526234?hl=en), and [Flow data guidance](https://support.google.com/flow/answer/17025472?hl=en).

## 1. Create the Tool

1. Open [Google Flow](https://labs.google/fx/tools/flow) in a desktop browser and sign in.
2. Open **Tools** and start a new custom Tool.
3. Give it a temporary name such as **Product Background Studio — Draft**.
4. Open [`builder-prompt.md`](builder-prompt.md).
5. Copy everything inside its single fenced `text` block. Do not copy only selected sections.
6. Paste it into Tool Builder and let Flow create or update the Tool.
7. Do not run image generation yet.

The first build may not implement every requested capability correctly. Natural-language confirmation in the Tool Builder chat is not proof; inspect the generated Tool.

## 2. Inspect Preview and Code

Before spending credits, confirm in Preview:

- three separate areas labeled `PRODUCT SOURCE`, `STYLE REFERENCE`, and `GENERATED OUTPUT`;
- separate Product Analysis and Reference Style Profile cards rather than one mixed Vision Analysis;
- `SINGLE` and `BATCH EXPERIMENTAL` modes;
- `SAFE` / `FAST`, `REFERENCE-FIRST` / `STRICT MATCH`, and `ECOMMERCE` / `SOCIAL` / `BOTH` controls;
- Aspect Ratio, Product Scale, and Detail Recovery controls;
- the Run action is disabled when Product Source or Style Reference is missing;
- Batch rows have independent status, View, Retry from Source, and truthful Download controls.

Then inspect Code or the development diagnostics and confirm:

- original product images, active reference, Product Locks, Reference Style Profile, outputs, and QA records use separate state;
- product and reference analysis are separate operations;
- each Batch generation uses one original Product Source plus the shared style reference, not the whole product list;
- retries use the immutable original Product Source;
- Download All exists only if it performs a real supported export.

If a contract is missing, use one matching prompt from [`repair-prompts.md`](repair-prompts.md). Do not paste every repair prompt and do not ask Tool Builder to rebuild everything unless the Tool is irrecoverably broken.

## 3. Run the Single smoke test

1. Select `SINGLE`, `SAFE`, `REFERENCE-FIRST`, and `ECOMMERCE`.
2. Add one Product Source with visible identity details such as folds, seams, weave, pattern, text, stones, clasp, or reflections.
3. Add a Style Reference whose subject differs visibly from the target product.
4. Select `ANALYZE`.
5. Confirm Product Analysis describes only the target product.
6. Confirm the Reference Style Profile describes only surface, palette, texture, light, contact shadow, mood, negative space, and compatible composition.
7. Confirm reference products, props, people, packages, typography, logos, labels, brand marks, and watermarks are listed as exclusions.
8. Confirm the Tool displays `Style source: REFERENCE IMAGE` and `Style Card: NONE — reference-driven`.
9. Approve generation only after Product Lock is accurate.
10. Compare the original Product Source and output side by side before accepting QA.

If Product Analysis mentions the reference product, stop. Apply **Repair role contamination** before testing again.

## 4. Test Strict Match

Keep the same inputs, choose `STRICT MATCH`, and run Safe again.

Before generation, verify:

- match target covers background color and tonal distribution, surface and finish, texture scale/density, gradient or vignette, illumination falloff, light direction/softness, contrast, contact shadow, mood, and negative space;
- hidden or expanded background regions are identified as reconstructed;
- Product Lock remains higher priority;
- no Style Card is selected;
- `Pixel-exact guarantee: NO — generative visual match` is visible.

After generation, Strict Match may receive PASS only when no material mismatch is observable at the available resolution. PASS never means pixel equality.

## 5. Test Batch Experimental

Do not start with 20 commercial products. First verify isolation with three visibly different rights-cleared products.

1. Select `BATCH EXPERIMENTAL`, `SAFE`, `REFERENCE-FIRST`, and `ECOMMERCE`.
2. Keep one shared Style Reference and add three Product Sources.
3. Analyze the Batch and review a separate Product Lock for every row.
4. Approve only ready items.
5. Observe the queue until every item reaches PASS, WARN, FAIL, or BLOCKED.
6. Confirm every output maps to one source and is not a collage.
7. Confirm one failed or blocked item does not erase or stop unrelated items.
8. Inspect diagnostics: each request must contain only that row's original Product Source plus the shared reference.
9. Use `Retry from Source` on one item and confirm its original source identifier is unchanged.
10. Increase the Batch size only after the three-item test passes with evidence.

Treat the largest Batch you actually observed working as the practical limit for that Tool snapshot. The requested 2–20 range is not a guarantee that every account/runtime will process 20 items reliably.

## 6. Repair one defect at a time

Open [`repair-prompts.md`](repair-prompts.md) and choose only the observed category:

- role contamination;
- Product Lock;
- Reference-first or Strict Match;
- Single/Batch isolation;
- source-first retry;
- download claims;
- UI separation.

Paste that block into the existing Tool Builder chat. After Flow updates the Tool, inspect the changed Code and Preview, rerun the matching acceptance case, and also rerun one previously passing smoke test to detect regression.

## 7. Complete acceptance before sharing

Copy [`acceptance-checklist.md`](acceptance-checklist.md) into your test record or fill it directly in a working branch. Record:

- Tool name and shared snapshot URL;
- account/plan context, visible model information, test date, and tester;
- inputs, actions, observable evidence, and status for every executed case;
- maximum Batch size actually observed;
- known warnings and required human review.

Leave unexecuted cases `NOT RUN`. Repository tests do not turn visual cases into PASS.

## 8. Download and verify outputs

A success message is not enough. For every download:

1. trigger the visible Download control;
2. wait for a real browser or Flow completion signal;
3. confirm the expected file exists on the local machine;
4. open it and verify it is the selected product/output;
5. record its filename if the image enters a commercial workflow.

If Download All or ZIP is unavailable, download outputs individually. Do not rely on a fake path, simulated progress, or an unverified automatic-save claim.

## 9. Share and update the Tool

Share only a snapshot that has passed the checks needed for its approved modes. Anyone with a shared Tool link may be able to see its name, thumbnail, and generated code. Do not include secrets, private instructions, confidential filenames, or client data in the Tool source.

A shared snapshot may not change when you later edit the original Tool. After a material builder or repair change:

1. rerun affected acceptance cases;
2. update the test date and evidence;
3. create a new shared snapshot/link when Flow requires it;
4. retire the old link in your team's documentation.

## Recommended production rollout

Use `SINGLE` Safe mode for the first high-risk products, then pilot a three-item Batch. Require side-by-side human review for all commercial images. Promote Batch size gradually and keep a conventional retouch path for FAIL, repeated repair failure, exact-color work, unreadable detail, and products whose boundaries cannot be separated reliably.

