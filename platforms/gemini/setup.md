# Gemini Setup

Choose Instant Run for occasional work or install a custom Gem for repeated batches. Both paths run in the Gemini interface and require no API key.

## Path 1 — Instant Run

1. Open a new conversation at [Gemini](https://gemini.google.com/).
2. Paste the complete runtime block from `instant-run.md` as the first message.
3. Upload the style reference and identify its role in your message.
4. Upload one or more original product photos and identify them as product sources.
5. Send a command such as `SAFE RUN ECOMMERCE` or `FAST RUN BOTH`.

## Path 2 — Install Once as a Gem

Custom Gems are created and edited in the Gemini web app; the resulting Gem can be available in other supported Gemini surfaces.

1. Open Gemini on the web, open **Gems**, and choose **New Gem**.
2. Name it **Product Photo Background Studio** or another recognizable name.
3. Paste the complete content of `installed-instructions.md` into the Gem instructions.
4. Under **Knowledge**, add the Markdown files from `core/`, `products/`, `styles/`, and `outputs/`.
5. Preview with a non-critical product. Verify that the Gem asks for role confirmation when uploads are unlabeled and does not borrow reference objects.
6. Save the Gem. When this repository changes, replace affected Knowledge files and update the instructions.

Google's current help covers [creating and managing Gems](https://support.google.com/gemini/answer/15146780?hl=en) and [generating or editing uploaded images](https://support.google.com/gemini/answer/14286560?hl=en). Feature placement and account eligibility can change, so use those official pages as the current authority.

Do not add contributor `_template.md` files to Knowledge unless the Gem will also help author new modules.
