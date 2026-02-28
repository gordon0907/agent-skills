---
name: hk-credit-cards-kb-updater
description: Use when updating the hk-credit-cards-kb card database and regenerating its reference index.
---

# Purpose
This skill maintains `hk-credit-cards-kb`, a static knowledge base for Hong Kong credit cards.
The knowledge base focuses on promotions and offers, and also includes key card attributes such as fees and other notable features.

# Workflow
1. Read [`references/cards.yaml`](references/cards.yaml) for the card list to maintain.
2. Create or update per-card YAML files under `hk-credit-cards-kb/references/`.
3. For each card, prioritize official issuer sources. You may also use trusted aggregator sites to cross-check offers:
   - https://hkcashrebate.com/
   - https://www.hongkongcard.com/
   - https://www.moneysmart.hk/
   - https://flyformiles.hk/
4. Update the `# References` section in `hk-credit-cards-kb/SKILL.md` as a concise index of cards and tags.

# Per-Card YAML Schema
Each card file should follow this structure:
```
id:
  Stable identifier for the card. Must be unique and match the ID in references/cards.yaml.

name_en / name_zh:
  Conventional card names.

issuer:
  Bank/institution name (or key).

payment_network:
  International payment network / scheme.
  Allowed examples: Visa, Mastercard, UnionPay, JCB.

official_url:
  Issuer-owned product page for the card.

annual_fee_hkd:
  Annual fee in HKD (number). Use 0 if waived as standard.
  If fee varies by variant, omit and use annual_fee_notes.

annual_fee_notes:
  Free text notes when fee is conditional or variant-based.

offers:
  List of current/curated offers.
  Each offer:
    - title: short label
    - description: what the offer is
    - restrictions: key conditions / exclusions
    - tc_url: terms link for the offer
    - validity: ISO 8601 interval string:
        "YYYY-MM-DD/YYYY-MM-DD" or "YYYY-MM-DD/PnD" etc.

as_of:
  Last verified date (string, YYYY-MM-DD).

sources:
  List of URLs used to populate/verify fields (official preferred).
```

# Reference Index Format
In `hk-credit-cards-kb/SKILL.md`, keep one entry per card file with short, high-signal tags for retrieval.

Tag examples:
- `Apple Pay`: card has Apple Pay-related offers
- `Online`: card has online spending offers
- `Sushiro HK`: card has merchant-specific offers (for example, Sushiro HK)

Example:
```
# References
Use this section as an index of per-card files in `references/*.yaml`.
Each entry should point to one card YAML file and list concise retrieval tags.

## references/card_id1.yaml
- tag1
- tag2
- tag3

## references/card_id2.yaml
- tag1
- tag2
```

# Rules
1. If a card appears outdated, unavailable, or discontinued, report it to the user.
2. Keep the `# References` index in `hk-credit-cards-kb/SKILL.md` concise; do not include full card details there.

# References
- [`references/cards.yaml`](references/cards.yaml): list of cards to maintain
- [`hk-credit-cards-kb/SKILL.md`](hk-credit-cards-kb/SKILL.md): index file to refresh
