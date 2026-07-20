# Ready-to-upload Knowledge Bundles

[Tiếng Việt](README.vi.md)

These four generated files combine the 17 publishable workflow sources into a compact Knowledge package:

1. [Core workflow](knowledge-core.md)
2. [Product Modules](knowledge-products.md)
3. [Style Cards](knowledge-styles.md)
4. [Output Profiles](knowledge-outputs.md)

The Style Cards bundle is a fallback library. When the user supplies a style-reference image, the workflow builds a dynamic Reference Style Profile from that image and does not auto-select a named card.

Upload all four files to the Knowledge area of your Custom GPT, Gemini Gem, or Claude Project. Do not upload this README, contributor `_template.md` files, or the individual source modules at the same time.

## Why four files

The source library remains modular for contributors, while the generated package stays comfortably below Gemini's 10-attachment upload batch limit. Grouping by responsibility also makes individual bundle replacement easier than maintaining one monolithic file.

## Source of truth

Files in `core/`, `products/`, `styles/`, and `outputs/` remain canonical. The four Knowledge bundles are generated artifacts and must not be edited by hand.

After changing a canonical source, rebuild and verify:

```bash
python tools/build_bundles.py
python tools/build_bundles.py --check
```

CI fails when a committed bundle is missing or stale.
