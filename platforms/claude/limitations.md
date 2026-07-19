# Claude Limitations

Claude's image understanding and file-upload capability do not by themselves prove that the current interface can edit and return a source-preserving raster image.

- Check the active chat's tools before the edit stage. Capability can vary by interface, account, plan, workspace policy, connected tools, and product updates.
- When raster editing is unavailable, Claude can still map image roles, analyze the product and reference, create Product Lock, assemble a render brief, and inspect a user-supplied result. It cannot truthfully report a completed image edit.
- Image analysis can miss small text, stitching, pattern changes, earring findings, stones, prongs, chain links, clasps, transparency, product color drift, and reflection errors. Human review remains required.
- Ordinary product photos are not calibrated color measurements. Exact Hex, RGB, or production-color claims require calibrated user input.
- Any available editing integration may reinterpret more than the intended background and cannot guarantee fidelity.
- A repair must return to the original product source. If one targeted repair and one Safe Run attempt fail, mark `MANUAL REVIEW`.

Version 1 has no automatic Prompt Exporter, one-click redirect, or silent handoff to another model. Claude must not move the user to a different platform automatically. A future export feature, if added, must be user-triggered and disclose that prompts are not behaviorally portable between image models.
