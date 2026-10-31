# Reference packet: GraphXAIN__Llama-8B__products__22915

- Method: GraphXAIN; configuration: Llama-8B; dataset: products; target node: 22915
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/products/graphxain_products_llama_narratives_fulleval.json` ([22915])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model predicted the target product, Amazing Grass Organic Wheat Grass Powder, falls under the category of "Health & Personal Care" with a confidence level of about 49%. This prediction was heavily influenced by the top Bag-of-Words (BOW) features, where words like "use" and "acid" were strongly associated with the product, despite some being absent ("roll" was not present). Moreover, the most influential direct neighbor - Stopain Extra Strength Pain Relief Roll-On, was categorized under "Health & Personal Care", reinforcing the initial prediction. The presence of multiple occurrences of "use" among the top BOW features further emphasized the product's likely category. While the co-purchase pattern may seem unrelated at first glance, it makes sense given that nutritional powders are often used alongside pain relief products. Notably, the absence of certain words, such as "relief", suggests the product focuses more on nutritional benefits rather than pain management. Overall, these linguistic patterns and local structure interactions supported the model's determination that the product belongs to the "Health & Personal Care" category.
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

### Target Product (node 22915):
Product from Amazon platform with title and content: Title: Amazing Grass Organic Wheat Grass Powder, 60 Servings, 17-Ounce Container. Content: Amazing Grass wheat grass powder is an excellent concentrated food source of beta-carotene, calcium, chlorophyll, fiber, iron and vitamin K. It is also a ve

### Model Prediction:
{
  "Target Node": 22915,
  "Predicted Class": "Health & Personal Care",
  "Confidence": 0.4927
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='roll', importance=0.7528, present_in_product=0
  word='use', importance=0.7507, present_in_product=1
  word='relief', importance=0.7487, present_in_product=0
  word='use', importance=0.7401, present_in_product=1
  word='acid', importance=0.7372, present_in_product=1
  word='use', importance=0.7325, present_in_product=1
  word='use', importance=0.7305, present_in_product=0

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 1
Label distribution across all 1-hop neighbors (ground-truth category): Health & Personal Care=100.0%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 4305 | edge_importance=0.8326 | category=Health & Personal Care | Stopain Extra Strength Pain Relief Roll-On, 3 Ounce

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 22917 | edge_importance=0.8157 | category=Beauty | Mederma Stretch Marks Therapy, 5
  Product 22918 | edge_importance=0.8065 | category=Beauty | Mama Mio Get Waisted Body Shaper, 3
  Product 475 | edge_importance=0.2061 | category=Home & Kitchen | Idea Works Waterfall Soap Saver
  Product 8389 | edge_importance=0.1916 | category=Health & Personal Care | Amerifit Culturelle Probiotics for Kids, 30 Count
  Product 22916 | edge_importance=0.1746 | category=Beauty | Goat Milk Soap - Original (3 Pack) Canus Vermont 3 Bar Soap

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

- ID: 22915
- Title: Amazing Grass Organic Wheat Grass Powder, 60 Servings, 17-Ounce Container
- True class (canonical `y`): **Health & Personal Care**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Health & Personal Care**
- Prediction recorded by this method's pipeline: **Health & Personal Care**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Amazing Grass Organic Wheat Grass Powder, 60 Servings, 17-Ounce Container. Content: Amazing Grass wheat grass powder is an excellent concentrated food source of beta-carotene, calcium, chlorophyll, fiber, iron and vitamin K. It is also a very good source of protein, vitamin C, vitamin B-12, folic acid, vitamin B-6, trace minerals and contains all essential amino acids. Mix a tablespoon of Green SuperFood with juice, milk, a smoothie or your favorite beverage. All natural and organic ingredients.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 4305 | Health & Personal Care | Stopain Extra Strength Pain Relief Roll-On, 3 Ounce |

### 2-hop (shortest distance exactly 2): 5 nodes

| node id | true class | title |
|---|---|---|
| 475 | Home & Kitchen | Idea Works Waterfall Soap Saver |
| 8389 | Health & Personal Care | Amerifit Culturelle Probiotics for Kids, 30 Count |
| 22916 | Beauty | Goat Milk Soap - Original (3 Pack) Canus Vermont 3 Bar Soap |
| 22917 | Beauty | Mederma Stretch Marks Therapy, 5.29 Oz Box |
| 22918 | Beauty | Mama Mio Get Waisted Body Shaper, 3.4 Ounce |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=22915).
Recorded prediction: `{"Target Node": 22915, "Predicted Class": "Health & Personal Care", "Confidence": 0.4927}`
Recorded graph stats: `{"total_1hop_degree": 1, "neighbor_label_ratio": {"Health & Personal Care": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | roll | 0.7528 | 0 |
| 2 | use | 0.7507 | 1 |
| 3 | relief | 0.7487 | 0 |
| 4 | use | 0.7401 | 1 |
| 5 | acid | 0.7372 | 1 |
| 6 | use | 0.7325 | 1 |
| 7 | use | 0.7305 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
