## Summary

Describe the user or contributor problem, the chosen scope, and affected module IDs or platforms.

## Validation

- [ ] `python -m pytest -v` passes.
- [ ] `python tools/validate_templates.py .` prints `Validation passed.`
- [ ] `git diff --check` reports no whitespace errors.

Paste concise command results or link the CI run:

## Visual test evidence

- [ ] I updated the manual test matrix for every platform/surface I actually ran.
- [ ] I kept real photographed-source and supplemental synthetic results separate.
- [ ] I did not claim PASS for an unrun, analysis-only, or unsupported capability.

List test case, platform, surface, date, mode, output, status, and observable evidence. If no visual test applies, explain why.

## Asset provenance

- [ ] Every added image records creator, source or generation record, and redistribution license.
- [ ] Client, unreleased, personal, or third-party material has documented authorization.
- [ ] Required attribution or separate asset notices are included.

List each asset and its rights record. If no assets were added, state that.

## Platform limitations

- [ ] Instructions do not imply parity across image models.
- [ ] Unsupported capabilities are stated plainly.
- [ ] Provider-specific availability or interface assumptions are documented.

## Documentation

- [ ] Public usage or behavior changes are documented.
- [ ] English canonical content and Vietnamese meaning remain consistent where applicable.
- [ ] New IDs and commands are discoverable from the appropriate quickstart or catalog.

## Backward compatibility

- [ ] Existing canonical commands and template IDs remain compatible, or the breaking change and migration path are documented.
- [ ] Core changes received broader cross-platform review than a scoped style addition.

## Reviewer notes

Call out remaining uncertainty, follow-up work, or areas needing a domain expert.
