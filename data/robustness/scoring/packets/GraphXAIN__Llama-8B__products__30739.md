# Reference packet: GraphXAIN__Llama-8B__products__30739

- Method: GraphXAIN; configuration: Llama-8B; dataset: products; target node: 30739
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/products/graphxain_products_llama_narratives_fulleval.json` ([30739])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model predicts that the target product, a decorative photography poster print, falls under the category "Home & Kitchen" with a moderate confidence level of 30%. This categorization can be attributed to the presence of certain key features, including the word "print", which is indeed present in the product title and strongly suggests an item suitable for home decoration. However, the absence of words like "like", "inch", and "design", which are often associated with design ideas and measurements, hints at a more functional product rather than something purely aesthetic. Moreover, the lack of words like "uniqu" and "item" implies a commercial or generic product rather than a unique or specialized item. In terms of local graph structure, all direct neighbors of the target product fall under the category "Home & Kitchen". More specifically, the product is often bought together with items such as beverage napkins and cocktail napkins, further reinforcing its association with the kitchen and home decoration. Additionally, some 2-hop neighbors also share this pattern, lending credibility to the model's prediction. Overall, the combination of these factors pushes the model to predict that the target product belongs to the "Home & Kitchen" category.
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

### Target Product (node 30739):
Product from Amazon platform with title and content: Title: New York City Empire State Building (NYC) Decorative Photography Poster Print 12x36. Content: Photography poster of The Empire State Building.

### Model Prediction:
{
  "Target Node": 30739,
  "Predicted Class": "Home & Kitchen",
  "Confidence": 0.3043
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='like', importance=0.7606, present_in_product=0
  word='inch', importance=0.7586, present_in_product=0
  word='design', importance=0.7581, present_in_product=0
  word='uniqu', importance=0.7533, present_in_product=0
  word='print', importance=0.7458, present_in_product=1
  word='wall', importance=0.7442, present_in_product=0
  word='item', importance=0.7418, present_in_product=0

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 1
Label distribution across all 1-hop neighbors (ground-truth category): Home & Kitchen=100.0%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 6577 | edge_importance=0.8512 | category=Home & Kitchen | DESIGN IDEAS New York Doodles Destinations City Map Beverage Napkins

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 30740 | edge_importance=0.7746 | category=label 25 | missing
  Product 30742 | edge_importance=0.7745 | category=Home & Kitchen | True Wine Stain Cocktail Napkins
  Product 763 | edge_importance=0.7376 | category=Home & Kitchen | Times Square Metal Subway Sign , 17x11
  Product 30741 | edge_importance=0.1415 | category=Health & Personal Care | Paperproducts Design 20-Pack Wine Cellar Paper Cocktail Napkins

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

- ID: 30739
- Title: New York City Empire State Building (NYC) Decorative Photography Poster Print 12x36
- True class (canonical `y`): **Home & Kitchen**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Home & Kitchen**
- Prediction recorded by this method's pipeline: **Home & Kitchen**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: New York City Empire State Building (NYC) Decorative Photography Poster Print 12x36. Content: Photography poster of The Empire State Building.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 6577 | Home & Kitchen | DESIGN IDEAS New York Doodles Destinations City Map Beverage Napkins |

### 2-hop (shortest distance exactly 2): 4 nodes

| node id | true class | title |
|---|---|---|
| 763 | Home & Kitchen | Times Square Metal Subway Sign , 17x11 |
| 30740 | label 25 | missing |
| 30741 | Health & Personal Care | Paperproducts Design 20-Pack Wine Cellar Paper Cocktail Napkins |
| 30742 | Home & Kitchen | True Wine Stain Cocktail Napkins |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=30739).
Recorded prediction: `{"Target Node": 30739, "Predicted Class": "Home & Kitchen", "Confidence": 0.3043}`
Recorded graph stats: `{"total_1hop_degree": 1, "neighbor_label_ratio": {"Home & Kitchen": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | like | 0.7606 | 0 |
| 2 | inch | 0.7586 | 0 |
| 3 | design | 0.7581 | 0 |
| 4 | uniqu | 0.7533 | 0 |
| 5 | print | 0.7458 | 1 |
| 6 | wall | 0.7442 | 0 |
| 7 | item | 0.7418 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
