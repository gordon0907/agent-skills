---
name: hk-credit-cards-kb-updater
description: Use when updating hk-credit-cards-kb by dumping promo_guide_url HTML and writing simplified per-card promotion YAML files.
---

# Purpose
This skill updates `hk-credit-cards-kb` by extracting promotion details from source pages and writing per-card YAML files under `hk-credit-cards-kb/references/`.

# Inputs
1. `references/cards.yaml` is the source of card metadata and target card list.
2. For each card, `promo_guide_url` is the default primary source.
3. User-provided URL(s), PDF(s), or other source files are allowed as additional priority sources.

# Required Tool Invocation
Use this exact command format:
```bash
.venv/bin/python <SCRIPT_PATH> <URL>
```

Use this script path from the updater skill root:
```bash
SCRIPT_PATH=./scripts/dump_html.py
```

Always use `.venv/bin/python` because `dump_html.py` depends on Playwright in that environment.

# Update Workflow
Process cards strictly one by one.

For each card in `references/cards.yaml`:
1. Read card metadata and target output path `hk-credit-cards-kb/references/<id>.yaml`.
2. Run the dump script with the card's `promo_guide_url`.
3. Parse the returned raw HTML and extract all promotion details.
4. Merge details from user-provided sources if available (URL/PDF/etc.), prioritizing newer and more explicit terms.
5. Write or update exactly one per-card YAML file.
6. Move to the next card only after finishing the current card.

Do not batch multiple cards in a single extraction pass.

# HTML Parsing And Information Preservation
1. Preserve promotion information as losslessly as possible in plain text.
2. Include all meaningful terms: conditions, thresholds, caps, exclusions, registration requirements, payment methods, merchant scope, category scope, and validity cues.
3. Ignore irrelevant site metadata (UI boilerplate, tracking, layout-only fragments).
4. Treat `del` / strikethrough content as obsolete or inactive terms unless the page explicitly states otherwise.
5. If HTML comments or nearby context clarify a promotion term, use that context when writing the description.

# YAML Output Schema
Write per-card YAML using this simplified schema:

```yaml
id: string
name_en: string
name_zh: string
issuer: string
payment_network: string
official_url: string
promo_guide_url: string
promotions:
  - description: string
    tc_url: string | null
    validity: string | null
as_of: YYYY-MM-DD
```

Rules:
1. `promotions` is the canonical list key.
2. `tc_url` must be `null` if no terms URL is found.
3. `validity` must be `null` if no reliable date range can be inferred.
4. Keep base fields aligned with `references/cards.yaml`.

# Language Rules
1. Write promotion descriptions in English.
2. Keep proper nouns and merchant/program names in their original form when translation would reduce precision.
3. Keep card metadata fields from `references/cards.yaml` as-is, including `name_zh`.

# Quality Bar
1. Prefer precise and complete wording over short summaries.
2. Avoid generic statements if concrete terms are present in sources.
3. If source terms conflict, prefer official terms pages or the latest effective source and reflect uncertainty in the description.
4. If a card appears discontinued or source content looks stale, report it to the user.

# References
- [`references/cards.yaml`](references/cards.yaml): list of cards to maintain
- [`scripts/dump_html.py`](scripts/dump_html.py): HTML dump script
- `hk-credit-cards-kb/references/*.yaml`: output files
