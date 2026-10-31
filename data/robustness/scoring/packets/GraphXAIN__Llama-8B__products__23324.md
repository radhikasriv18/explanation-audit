# Reference packet: GraphXAIN__Llama-8B__products__23324

- Method: GraphXAIN; configuration: Llama-8B; dataset: products; target node: 23324
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/products/graphxain_products_llama_narratives_fulleval.json` ([23324])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model predicted the product category as "Health & Personal Care" with high confidence (0.9439). The model drew upon the presence of key words from the product's bag-of-words feature vector, where words such as "use," "get," and "used" contributed strongly, even though they were absent in the product. However, the word "used" was found in the product's text, supporting its relevance. In addition, the model considered the local graph structure, where the majority of the product's 1-hop co-purchase neighbors belonged to the "Health & Personal Care" category, with the Strongly associated neighbor being the "Slim Green Reduce Cream 4 Oz". Furthermore, among the more distant connections, some 2-hop co-purchase neighbors also reinforced this pattern, suggesting a broader context of slimming and body-shaping creams within the health category. Overall, the combination of these factors propelled the prediction towards the "Health & Personal Care" category, highlighting an apparent association between the product and similar items in this category. The absence of key words like "simpli" and "year" might have played a negligible role in diverting the prediction away from other categories, reinforcing the dominance of the "Health & Personal Care" prediction.
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

### Target Product (node 23324):
Product from Amazon platform with title and content: Title: Breast Success Cream 2.0 Fl Oz Enhancement Bust Enlargement. Content: Breast Success Cream is a cream-based topical breast enhancement formula designed just for women. This product contains a variety of ingredients including Volufiline and 

### Model Prediction:
{
  "Target Node": 23324,
  "Predicted Class": "Health & Personal Care",
  "Confidence": 0.9439
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='use', importance=0.7376, present_in_product=0
  word='get', importance=0.733, present_in_product=0
  word='simpli', importance=0.7226, present_in_product=0
  word='year', importance=0.7219, present_in_product=0
  word='use', importance=0.7209, present_in_product=0
  word='one', importance=0.7181, present_in_product=0
  word='used', importance=0.7167, present_in_product=1

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 1
Label distribution across all 1-hop neighbors (ground-truth category): Health & Personal Care=100.0%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 4435 | edge_importance=0.5853 | category=Health & Personal Care | Slim Green Reduce Cream 4 Oz

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 23161 | edge_importance=0.8327 | category=Grocery & Gourmet Food | PINALIM TEA/TE PINALIM - PINNEAPPLE, FLAX, GREEN TEA, RED TEA AND WHITE TEA
  Product 492 | edge_importance=0.7951 | category=label 25 | missing
  Product 4345 | edge_importance=0.7846 | category=Clothing, Shoes & Jewelry | Aokdis Plastic Weight Loss Weight Waist Leg Thigh Sauna Slimming Wrap Burn Cellulite Fat Belt Wrap
  Product 491 | edge_importance=0.7661 | category=Beauty | Yili Balo Hot Chili Body Slimming Gel 85ml
  Product 23325 | edge_importance=0.7553 | category=Health & Personal Care | 21st Century Slimming Tea, Green Tea, 24 Count (Pack of 3)
  Product 23111 | edge_importance=0.2898 | category=Health & Personal Care | Ultimate Body Wrap Lipo Applicator Wrap
  Product 4444 | edge_importance=0.1876 | category=Health & Personal Care | "L'eudine Redugel Excessive Body Fat Burner Reducer"
  Product 23323 | edge_importance=0.1794 | category=Health & Personal Care | It Works! Defining Gel
  Product 4344 | edge_importance=0.1665 | category=Beauty | Hot Chili Balo Cream 85ml + Coffee Yili Balo Cream 85ml

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

- ID: 23324
- Title: Breast Success Cream 2.0 Fl Oz Enhancement Bust Enlargement
- True class (canonical `y`): **Clothing, Shoes & Jewelry**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Health & Personal Care**
- Prediction recorded by this method's pipeline: **Health & Personal Care**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Breast Success Cream 2.0 Fl Oz Enhancement Bust Enlargement. Content: Breast Success Cream is a cream-based topical breast enhancement formula designed just for women. This product contains a variety of ingredients including Volufiline and Biobustyle designed for powerful female enhancement. Breast Success Cream is a perfect complement to Breast Success pills or can be used an alternative for those wanting to avoid expensive and dangerous surgery. Feel the sensuality of natural enhancement and improve your confidence by looking and feeling your best
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 4435 | Health & Personal Care | Slim Green Reduce Cream 4 Oz |

### 2-hop (shortest distance exactly 2): 9 nodes

| node id | true class | title |
|---|---|---|
| 491 | Beauty | Yili Balo Hot Chili Body Slimming Gel 85ml |
| 492 | label 25 | missing |
| 4344 | Beauty | Hot Chili Balo Cream 85ml + Coffee Yili Balo Cream 85ml |
| 4345 | Clothing, Shoes & Jewelry | Aokdis Plastic Weight Loss Weight Waist Leg Thigh Sauna Slimming Wrap Burn Cellulite Fat Belt Wrap |
| 4444 | Health & Personal Care | "L'eudine Redugel Excessive Body Fat Burner Reducer" |
| 23111 | Health & Personal Care | Ultimate Body Wrap Lipo Applicator Wrap. 2 Wraps |
| 23161 | Grocery & Gourmet Food | PINALIM TEA/TE PINALIM - PINNEAPPLE, FLAX, GREEN TEA, RED TEA AND WHITE TEA |
| 23323 | Health & Personal Care | It Works! Defining Gel. Slimming Gel. Body Defining Gel by It Works! 0.5 oz sample size. |
| 23325 | Health & Personal Care | 21st Century Slimming Tea, Green Tea, 24 Count (Pack of 3) |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=23324).
Recorded prediction: `{"Target Node": 23324, "Predicted Class": "Health & Personal Care", "Confidence": 0.9439}`
Recorded graph stats: `{"total_1hop_degree": 1, "neighbor_label_ratio": {"Health & Personal Care": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | use | 0.7376 | 0 |
| 2 | get | 0.733 | 0 |
| 3 | simpli | 0.7226 | 0 |
| 4 | year | 0.7219 | 0 |
| 5 | use | 0.7209 | 0 |
| 6 | one | 0.7181 | 0 |
| 7 | used | 0.7167 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
