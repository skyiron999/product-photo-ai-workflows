# Synthetic Test Cases

Synthetic transparent cutouts are a supplemental control for isolating edge integration, contact-shadow construction, safe padding, canvas expansion, and background-light harmonization. They make certain defects easier to attribute because the source has a known transparent boundary.

These cases do not replace real photographed-source tests. Real sources remain mandatory for evaluating extraction edges, embedded lighting, occlusion, product-background color interaction, fine texture, reflections, and the generative model's tendency to reinterpret photographed detail.

## Admission rule

Do not add an image until every field in the manifest is complete and verifiable. The repository must have the right to redistribute both the cutout and any paired reference. Generated assets require the tool or model, date, prompt or generation record, human editor if applicable, and a license or terms basis that permits redistribution.

## Intended controls

- one-pixel and semi-transparent edge retention;
- light and dark halo detection;
- preservation of holes and negative spaces;
- contact-shadow direction, softness, and product grounding;
- background-only color harmonization;
- ratio change through canvas expansion rather than product distortion;
- ecommerce safe-padding measurements.

Record synthetic and real test results in separate matrix rows. A synthetic PASS cannot satisfy a real-source release requirement.
