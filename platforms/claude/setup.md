# Claude Setup

**English** · [Tiếng Việt](setup.vi.md)

Claude can always perform the visual analysis and workflow assembly stages when it can read the uploads. Raster editing depends on the tools exposed in the user's current Claude interface, so verify capability at runtime.

## Path 1 — Instant Run

1. Open a new Claude conversation.
2. Paste the complete runtime block from `instant-run.md` as the first message.
3. Upload or paste the style reference and identify it in your message.
4. Upload one or more original product sources and identify their roles.
5. Send `SAFE RUN ECOMMERCE`, `FAST RUN SOCIAL`, or another supported command combination.
6. Read Claude's capability statement before expecting a raster output. If editing is unavailable, use the resulting lock sheet and render brief as analysis—not as proof an image was changed.

## Path 2 — Install Once as a Claude Project

1. Open [Claude Projects](https://claude.ai/projects) and create a new project.
2. Name it **Product Photo Background Studio**.
3. Choose **Set project instructions**, paste all content from `installed-instructions.md`, and save.
4. Add the Markdown files from `core/`, `products/`, `styles/`, and `outputs/` to Project Knowledge.
5. Start a project chat and test a non-critical source. Confirm that Claude states whether an image-editing tool is actually available.
6. Replace affected Knowledge and instruction files whenever the repository is updated.

Anthropic's current guides explain [creating and managing Projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) and [uploading supported image files](https://support.claude.com/en/articles/8241126-upload-files-to-claude). Account and workspace availability may change; those official pages are authoritative.

Do not upload contributor `_template.md` files unless the Project will also be used to create modules.
