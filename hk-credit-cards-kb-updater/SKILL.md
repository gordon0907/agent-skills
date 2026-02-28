---
name: hk-credit-cards-kb-updater
description: Use when updating hk-credit-cards-kb with detailed, source-backed card offers and high-recall retrieval tags.
---

# Purpose
This skill maintains `hk-credit-cards-kb`, a static knowledge base for Hong Kong credit cards.
The knowledge base focuses on promotions and offers, and also includes key card attributes such as fees and other notable features.

# Scope Priority
Prioritize offers in this order:
1. Ongoing spending promotions (`消費` promotions): merchant/channel/payment-method/category based rebates, cashback, points, miles, or discounts.
2. Recurring card benefits that are useful for regular spend decisions.
3. Welcome offers (include them, but place them after ongoing spending promotions).

The goal is card recommendation quality for real spending scenarios (for example, "Which card for TamJai?"), not only onboarding offers.

# Workflow
1. Read [`references/cards.yaml`](references/cards.yaml) for the card list to maintain.
2. Create or update per-card YAML files under `hk-credit-cards-kb/references/`.
3. For each card, prioritize official issuer pages and official terms PDFs. You may also use trusted aggregator sites for discovery/cross-checking:
   - https://hkcashrebate.com/
   - https://www.hongkongcard.com/
   - https://www.moneysmart.hk/
   - https://flyformiles.hk/
4. If the user directly provides source URL(s) and/or a promotion/offer terms PDF, treat them as primary sources: parse them as deeply as possible and write all extractable details into the card YAML.
5. For each offer, extract concrete values from sources (rates, caps, min spend, period, eligible merchants/channels/methods, exclusions, registration requirements).
6. Update the `# References` section in `hk-credit-cards-kb/SKILL.md` as a concise but high-recall index of cards and tags.

# Data Quality Requirements
1. Do not write vague placeholders when exact values are available.
   - Bad: "monthly caps apply"
   - Good: "monthly spend cap HKD 3,571; monthly cashback cap HKD 250"
2. If a key value is not found from available sources, use `null` for the field and explain briefly in `restrictions`.
3. Keep monetary values as numbers in HKD where possible (for example `3571`, not `"HK$3,571"` in numeric fields).
4. Every non-trivial claim should be source-backed via `tc_url` and/or `sources`.
5. Examples in this skill are format examples only. They are not limits on number of offers, fields, or tags.
6. Offer coverage is open-ended: keep adding active, material offers until sources are exhausted.
7. When user-provided URL(s) and/or terms PDF(s) are available, parse them thoroughly and prefer structured extraction (numeric caps, thresholds, dates, merchant/channel lists, exclusions, registration rules) over generic summaries.

# Per-Card YAML Schema
Each card file should follow this structure. Add more fields if they improve precision/searchability.
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
  List of current/curated offers. No fixed length limit.
  Put ongoing spending promotions first, then welcome offers.
  Each offer:
    - title: short label
    - offer_type: one of [spending, recurring-benefit, welcome, installment, points]
    - description: include concrete value(s), not generic wording
    - reward_type: cashback | points | miles | discount | mixed
    - reward_rate_percent: number or null
    - reward_cap_hkd: number or null
    - min_spend_hkd: number or null
    - spend_cap_hkd: number or null
    - spend_cap_period: monthly | campaign | transaction | null
    - payment_methods: list (e.g. ["Apple Pay", "Card Present"]) or []
    - eligible_merchants: list of merchant names or []
    - eligible_categories: list (e.g. ["Dining", "Online"]) or []
    - excluded_merchants: list or []
    - excluded_categories: list or []
    - registration_required: true | false | null
    - restrictions: key conditions, with exact values if available
    - keywords: query-oriented tokens (EN/ZH, aliases, merchant variants)
    - tc_url: terms link for the offer
    - validity: ISO 8601 interval string:
        "YYYY-MM-DD/YYYY-MM-DD" or "YYYY-MM-DD/PnD" etc.

as_of:
  Last verified date (string, YYYY-MM-DD).

sources:
  List of URLs used to populate/verify fields (official preferred).
```

# Reference Index Format
In `hk-credit-cards-kb/SKILL.md`, keep one entry per card file with high-recall tags for retrieval.
Do not cap tag count artificially. Include all useful keywords likely to appear in user queries.

Tag selection rules:
1. Include issuer and network tags (for example `HSBC`, `Mastercard`).
2. Include reward-type and mechanism tags (for example `Cashback`, `RewardCash`, `Miles`, `Installment`).
3. Include payment method tags (for example `Apple Pay`, `Google Pay`, `UnionPay QR`).
4. Include channel/category tags (for example `Online`, `Dining`, `Supermarket`, `Overseas`, `Japan`).
5. Include merchant tags where applicable (for example `TamJai`, `譚仔`, `Sushiro`).
6. Include EN/ZH and common alias variants when they are realistic query terms.
7. Prefer specific tags over vague tags. `TamJai` is better than only `Dining`.

Example:
```
# References
Use this section as an index of per-card files in `references/*.yaml`.
Each entry should point to one card YAML file and list concise retrieval tags.

## references/card_id1.yaml
- network
- reward-type
- payment-method
- category
- merchant-en
- merchant-zh

## references/card_id2.yaml
- network
- category
- merchant
- keyword-variant
```

# Rules
1. If a card appears outdated, unavailable, or discontinued, report it to the user.
2. Keep the `# References` index in `hk-credit-cards-kb/SKILL.md` concise; do not include full card details there.
3. Do not assume "2-3 offers" or "4 tags" is sufficient. Coverage should match source reality.
4. If an offer exists but lacks enough structured details, keep it and mark missing numeric fields as `null` with explanation in `restrictions`.

# References
- [`references/cards.yaml`](references/cards.yaml): list of cards to maintain
- [`hk-credit-cards-kb/SKILL.md`](hk-credit-cards-kb/SKILL.md): index file to refresh
