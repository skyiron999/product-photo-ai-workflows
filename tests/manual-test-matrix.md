# Manual Test Matrix

Use this matrix for real runs in the named consumer interface. Never record a pass from prompt review alone. Duplicate a row for every retry rather than overwriting failure evidence.

Allowed status values are `NOT RUN`, `PASS`, `WARN`, `FAIL`, `MANUAL REVIEW`, and `UNSUPPORTED`. Use `UNSUPPORTED` when a tested interface lacks the required raster-editing capability; describe the observed capability boundary in Reviewer notes. Use `NOT RUN` only when no platform attempt occurred.

| Platform | Surface | Test date | Source type | Case | Mode | Output | Aspect / canvas check | Padding check | Typography contamination | Color drift | Status | Reviewer notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ChatGPT | Web chat | — | Real photographed source | Garments | Safe Run | Ecommerce | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | — |
| ChatGPT | Web chat | — | Real photographed source | Fabric | Fast Run | Social | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | — |
| ChatGPT | Web chat | — | Real photographed source | Earrings | Safe Run | Both | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | — |
| ChatGPT | Web chat | — | Real photographed source | Bracelets | Fast Run | Ecommerce | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | — |
| ChatGPT | Web chat | — | Real photographed source | Reflective accessories | Safe Run | Social | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | — |
| Gemini | Web app | — | Real photographed source | Garments | Fast Run | Social | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | — |
| Gemini | Web app | — | Real photographed source | Fabric | Safe Run | Ecommerce | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | — |
| Gemini | Web app | — | Real photographed source | Earrings | Fast Run | Both | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | — |
| Gemini | Web app | — | Real photographed source | Bracelets | Safe Run | Social | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | — |
| Gemini | Web app | — | Real photographed source | Reflective accessories | Fast Run | Ecommerce | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | — |
| Claude | Web project | — | Real photographed source | Garments | Safe Run | Ecommerce | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | Record available capability first. |
| Claude | Web project | — | Real photographed source | Fabric | Fast Run | Social | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | Record available capability first. |
| Claude | Web project | — | Real photographed source | Earrings | Safe Run | Both | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | Record available capability first. |
| Claude | Web project | — | Real photographed source | Bracelets | Fast Run | Ecommerce | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | Record available capability first. |
| Claude | Web project | — | Real photographed source | Reflective accessories | Safe Run | Social | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | Record available capability first. |
| ChatGPT | Web chat | — | Synthetic transparent cutout | Bracelet edge control | Safe Run | Ecommerce | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | Supplemental control only. |
| Gemini | Web app | — | Synthetic transparent cutout | Bracelet edge control | Fast Run | Social | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | Supplemental control only. |
| Claude | Web project | — | Synthetic transparent cutout | Bracelet edge control | Safe Run | Ecommerce | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | Supplemental; capability required. |

## Release coverage rules

- Every platform must be checked separately; never transfer a status between platforms or interface surfaces.
- Every product case must include at least one Safe Run and one Fast Run over the release cycle.
- Ecommerce checks include source ratio, requested alternate ratio, background-first expansion, product crop, and approximately 15% safe padding where feasible.
- Social checks include negative space, opt-in props, product crop, and invented copy.
- At least one style reference must contain visible typography, a logo, a prop, and a different product to test contamination rejection.
- Inspect color drift on the product independently of whether the new background palette looks attractive.
- Record real photographed-source evidence and synthetic transparent-cutout evidence separately. Synthetic controls are supplemental.
