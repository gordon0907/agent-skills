---
name: hk-credit-cards-kb
description: Use as a Hong Kong credit card knowledge base by reading all references/*.yaml files sequentially.
---

# Purpose
This skill answers Hong Kong credit card questions using per-card YAML files in `references/`.
Use full card data reading and card-by-card reasoning, not tag indexing.

# Retrieval Strategy
1. Read all files under `references/*.yaml`.
2. Read files one by one, fully.
3. Do not use keyword-only filtering as the primary retrieval method.
4. Do not skip files just because quick keyword matches look weak.

# Matching Strategy
1. Compare each card against the user query one by one.
2. Evaluate merchant, category, payment method, conditions, validity, and exclusions from the card's `promotions` text.
3. Handle bilingual mismatch robustly: user queries can be English or Chinese, and stored content can use mixed naming.
4. Use semantic matching for merchant aliases and common naming variants instead of exact keyword dependence.
5. Use incremental elimination while reading sequentially; avoid large batch analysis that risks context overflow.

# When To Fetch More Information
1. If local YAML data is insufficient, stale, or ambiguous, fetch supporting details from promotion `tc_url` when available.
2. If `tc_url` is missing or insufficient, perform limited targeted web lookup for the specific gap only.
3. Prefer official terms pages when resolving conflicts.

# References
Read all card files from `references/*.yaml`.
