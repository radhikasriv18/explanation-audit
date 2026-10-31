# Reference packet: GraphXAIN__Llama-8B__products__14760

- Method: GraphXAIN; configuration: Llama-8B; dataset: products; target node: 14760
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/products/graphxain_products_llama_narratives_fulleval.json` ([14760])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model confidently predicts that the product 'Lobo Spicy Tom Yum soup mix 30g X 5 pack' belongs to the 'Health & Personal Care' category with an accuracy of 98%. This prediction can be attributed to the top BOW features, where words like 'use', related to application instructions, and other descriptors like 'activ', 'brand', 'effect', and 'least' contribute positively. However, these words are strikingly absent in the product, yet their influence suggests they may have been used in similar products that fit within 'Health & Personal Care'. Moreover, a direct co-purchase neighbor, 'Namman Muay Thai Boxing Analgesic Balm Massage Relief Ache 100g', a product from the same health category, further supports this prediction. Interestingly, another direct neighbor does not conform to this pattern, indicating its relatively weaker impact. Two-step connections also exhibit a reinforcing trend towards health-related items, solidifying the prediction. Overall, it appears the model relied heavily on its understanding of product descriptions and co-purchasing behavior, identifying connections between health supplements, treatments, and care routines. This combined insight allows the model to accurately predict the target product's category as 'Health & Personal Care'.
~~~~~~

## 2. Prompt the method's model received

`prompt` field of the record (sent as the single user message).

**user:**

~~~~~~text
Your goal is to generate a textual narrative explaining why a GNN model made a certain prediction for a target product node, based on the output of a GNNExplainer.

### Machine Learning Task:
Multi-class node classification task that predicts the product category on Amazon. The model classifies each product into one of 47 top-level Amazon categories such as 'Health & Personal Care', 'Beauty', 'Sports & Outdoors', 'Tools & Home Improvement', etc.

### Dataset:
The Amazon Products co-purchase network contains 54,025 products. Each product (node) is represented as a bag-of-words feature vector of 2,000 words from the product title and description. Edges represent co-purchase relationships — two products are connected if customers frequently buy them together.

### Target Product (node 14760):
Product from Amazon platform with title and content: Title: Lobo Spicy Tom Yum soup mix 30g X 5 pack. Content: Shrimp Tom Yum or Tom Yum Goong must be one of the best know Thai dishes abroad. It's a subtle blend of hot and sour with citrus overtones derived from lime juice and kaffir lime peel. Be c

### Model Prediction:
{
  "Target Node": 14760,
  "Predicted Class": "Health & Personal Care",
  "Confidence": 0.9846
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='activ', importance=0.7385, present_in_product=0
  word='brand', importance=0.7381, present_in_product=0
  word='never', importance=0.7375, present_in_product=0
  word='use', importance=0.7333, present_in_product=1
  word='effect', importance=0.72, present_in_product=0
  word='least', importance=0.72, present_in_product=0
  word='use', importance=0.7183, present_in_product=1

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 1
Label distribution across all 1-hop neighbors (ground-truth category): Health & Personal Care=100.0%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 1974 | edge_importance=0.8068 | category=Health & Personal Care | Namman Muay Thai Boxing Analgesic Balm Massage Relief Ache 100g

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 165 | edge_importance=0.8105 | category=Clothing, Shoes & Jewelry | Revgear Muay Thai Shorts
  Product 14759 | edge_importance=0.8016 | category=Beauty | "POND'S Age Miracle Day Cream 50g
  Product 14758 | edge_importance=0.7892 | category=Grocery & Gourmet Food | Thai whole dried chile - 3
  Product 14762 | edge_importance=0.7628 | category=Beauty | 2x100 G
  Product 14761 | edge_importance=0.1415 | category=Health & Personal Care | Namman Muay Thai Boxing Liniment 120ml

Generate a fluent, cohesive narrative explaining the prediction. Rules:

**Format rules:**
1) Start the explanation immediately — no preamble.
2) Limit the entire answer to 8 sentences or fewer.
3) Do not use tables or bullet lists — write a single cohesive paragraph.

**Content rules:**
1) State clearly what category the model predicted and with what confidence.
2) Discuss how the top BOW features contributed — note whether each high-importance word is actually present or absent in the product.
3) Discuss how the most influential direct (1-hop) co-purchase neighbors shaped the prediction, describing them by product type or title.
4) Mention how 2-hop neighbors reinforce the pattern if relevant.
5) Interpret WHY a feature or connection pushed the prediction in a certain direction.
6) Do not quote raw importance numbers; use relative language (e.g., "most influential", "strongly associated").
7) Use clear language that a general audience can understand.

~~~~~~

## 3. Target node

- ID: 14760
- Title: Lobo Spicy Tom Yum soup mix 30g X 5 pack
- True class (canonical `y`): **Grocery & Gourmet Food**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Health & Personal Care**
- Prediction recorded by this method's pipeline: **Health & Personal Care**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Lobo Spicy Tom Yum soup mix 30g X 5 pack. Content: Shrimp Tom Yum or Tom Yum Goong must be one of the best know Thai dishes abroad. It's a subtle blend of hot and sour with citrus overtones derived from lime juice and kaffir lime peel. Be careful not to overcook the shrimps as they will become tough very easily.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 1974 | Health & Personal Care | Namman Muay Thai Boxing Analgesic Balm Massage Relief Ache 100g |

### 2-hop (shortest distance exactly 2): 5 nodes

| node id | true class | title |
|---|---|---|
| 165 | Clothing, Shoes & Jewelry | Revgear Muay Thai Shorts |
| 14758 | Grocery & Gourmet Food | Thai whole dried chile - 3.5 oz |
| 14759 | Beauty | "POND'S Age Miracle Day Cream 50g. Sale!!!" |
| 14761 | Health & Personal Care | Namman Muay Thai Boxing Liniment 120ml. (2 Bottles) |
| 14762 | Beauty | 2x100 G. Dentiste Plus White Vitamin C &amp; Xyitol Gum Toothpaste Made in Thailand |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=14760).
Recorded prediction: `{"Target Node": 14760, "Predicted Class": "Health & Personal Care", "Confidence": 0.9846}`
Recorded graph stats: `{"total_1hop_degree": 1, "neighbor_label_ratio": {"Health & Personal Care": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | activ | 0.7385 | 0 |
| 2 | brand | 0.7381 | 0 |
| 3 | never | 0.7375 | 0 |
| 4 | use | 0.7333 | 1 |
| 5 | effect | 0.72 | 0 |
| 6 | least | 0.72 | 0 |
| 7 | use | 0.7183 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
