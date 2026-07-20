# ChatGPT Setup

**English** · [Tiếng Việt](setup.vi.md)

Choose the path that matches how often you use the workflow. No API key is required; both paths run in the ChatGPT interface.

## Path 1 — Instant Run

1. Open a new ChatGPT conversation that supports image uploads and image generation.
2. Copy the complete runtime block from `instant-run.md` and paste it as the first message.
3. Upload or paste the style-reference image and identify it in your message.
4. Upload one or more original product photos and identify them as product sources.
5. Send `SAFE RUN ECOMMERCE`, `FAST RUN SOCIAL`, or another supported command combination.

With a reference attached, confirm that the lock sheet says `Style source: REFERENCE IMAGE` and `Style Card: NONE — reference-driven`. A named Style Card is only a fallback when no reference is active or you explicitly request one.

For maximum visual adherence, send `SAFE RUN STRICT MATCH ECOMMERCE`. Confirm that ChatGPT reports the match target, reconstructed regions, and `Pixel-exact guarantee: NO — generative visual match` before you continue.

Use this path to test the kit or handle occasional work. Begin a fresh chat if context becomes confused between products.

## Path 2 — Install Once as a Custom GPT

Creating or editing a GPT currently requires an eligible paid ChatGPT plan and is performed on the web; availability and permissions can also depend on workspace policy. A shared GPT may be usable under different plan or workspace conditions.

1. Open the [GPT editor](https://chatgpt.com/gpts/editor) and create a new GPT.
2. Give it a clear name such as **Product Photo Background Studio**.
3. Paste the full content of `installed-instructions.md` into **Instructions**.
4. Enable **Image Generation** under capabilities.
5. Upload these four generated files as **Knowledge**:
   - [Core workflow](../../bundles/knowledge-core.md)
   - [Product Modules](../../bundles/knowledge-products.md)
   - [Style Cards](../../bundles/knowledge-styles.md)
   - [Output Profiles](../../bundles/knowledge-outputs.md)
   Put workflow behavior in Instructions; Knowledge supplies the modular reference content. The Style Cards bundle remains a no-reference fallback and does not override an uploaded reference. Do not upload both the bundles and their individual source files.
6. Add conversation starters such as `SAFE RUN ECOMMERCE` and `FAST RUN BOTH`.
7. Test with a non-critical product first, inspect the source and output side by side, then save or share the GPT according to your workspace policy.

OpenAI's current guides explain [creating and editing GPTs](https://help.openai.com/en/articles/8554397-creating-a-gpt) and [creating or editing uploaded images in ChatGPT](https://help.openai.com/en/articles/11084440-images-in-chatgpt). Controls and plan availability can change, so treat those official pages as authoritative.

## Updating the installation

When the repository changes, download and replace the affected generated bundles. Update Instructions if `installed-instructions.md` changed. Do not upload `_template.md` contributor templates unless you want the GPT to help author new modules.
