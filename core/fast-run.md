# Fast Run

Fast Run is the high-throughput mode for a repeated, already-understood setup. It uses the same Product Lock, precedence, render brief, QA, and repair rules as Safe Run, but performs the lock analysis internally and proceeds without a visible approval gate.

## Required behavior

For every product, map roles, rebuild the lock from the original product source, extract only allowed style attributes, apply the selected modules, edit, and run QA. When a reference is present, retain its dynamic Reference Style Profile as the batch style source and do not auto-select a Style Card; its status is `Style source: REFERENCE IMAGE` and `Style Card: NONE — reference-driven`. Do not reuse the previous product's identity details. The command `NEXT PRODUCT` clears the previous source and lock while retaining the Reference Style Profile, run mode, and output settings.

Return a short result note containing the output target and `PASS`, `WARN`, `FAIL`, or `MANUAL REVIEW`. Surface any warning that could affect commercial use.

## Mandatory pause conditions

Stop before editing and ask for the minimum clarification when any of these occurs:

- source and reference roles are ambiguous;
- multiple products cannot be separated into a reliable lock;
- critical text, construction, pattern, or component details are unreadable;
- the requested crop, spacing, or style conflicts with locked geometry;
- exact product color is requested without calibrated user input;
- the platform cannot perform a source-preserving image edit;
- the reference demands a product, prop, logo, or typography that the user did not supply.

Once clarified, continue in Fast Run unless the risk remains; then switch that product to Safe Run.
