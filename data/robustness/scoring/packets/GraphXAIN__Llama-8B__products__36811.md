# Reference packet: GraphXAIN__Llama-8B__products__36811

- Method: GraphXAIN; configuration: Llama-8B; dataset: products; target node: 36811
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/products/graphxain_products_llama_narratives_fulleval.json` ([36811])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The GNN model predicted the Vogmask Microfiber Filtering Mask: Pink Roses product, which is related to "Health & Personal Care" with a high confidence of 88.57%. This prediction was largely influenced by key categorical features extracted from the product's title and description, including words such as "microfiber", "support", and "reusable", which are strongly associated with health-related products. Furthermore, the model relied heavily on the local graph structure surrounding the product, particularly its direct 1-hop co-purchase neighbors, many of which were categorized under "Health & Personal Care", reinforcing the prediction. Notably, neighboring products like the Child Life Liquid Calcium/Magnesium supplement also support this association, suggesting a link between co-purchase behaviors and shared themes of health and wellness. While less prominent, the influence of 2-hop neighbors in related areas like "Beauty" further reinforced the dominant signal, validating the model's final classification. Overall, these observations indicate that the model effectively captured patterns of co-purchasing behavior around the target product, ultimately yielding a strong prediction within the expected category. This outcome showcases the success of the GNN architecture in uncovering meaningful connections among related nodes within the network.
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

### Target Product (node 36811):
Product from Amazon platform with title and content: Title: Vogmask Microfiber Filtering Mask: Pink Roses. Content: Stay healthy and keep airborne particles out of your lungs with Vogmask, the first dust masks designed to be stylish, comfortable and reusable. With the choice of high-tech microfiber 

### Model Prediction:
{
  "Target Node": 36811,
  "Predicted Class": "Health & Personal Care",
  "Confidence": 0.8857
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='microfiber', importance=0.708, present_in_product=1
  word='support', importance=0.7018, present_in_product=0
  word='like', importance=0.7006, present_in_product=1
  word='reusable', importance=0.6988, present_in_product=1
  word='essenti', importance=0.6971, present_in_product=0
  word='designed', importance=0.6939, present_in_product=1
  word='first', importance=0.6912, present_in_product=1

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 1
Label distribution across all 1-hop neighbors (ground-truth category): Health & Personal Care=100.0%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 8361 | edge_importance=0.8626 | category=Health & Personal Care | Child Life Liquid Calcium/Magnesium,Natural Orange Flavor Plastic Bottle, 16-Fl

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 36814 | edge_importance=0.8079 | category=Beauty | Aveeno Eczema Therapy  Bath Treatment, 3 Count (Pack of 2)
  Product 36813 | edge_importance=0.803 | category=Baby | Thermos FUNtainer Stainless Steel 10 oz Leak-Proof Straw Bottle - Mickey Mouse
  Product 8389 | edge_importance=0.7811 | category=Health & Personal Care | Amerifit Culturelle Probiotics for Kids, 30 Count
  Product 983 | edge_importance=0.7567 | category=Health & Personal Care | Child Life Probiotics Plus Colostrum Chewable Tablets, Mixed Berry Flavor, 90 Count
  Product 36810 | edge_importance=0.1715 | category=Baby | thinkbaby BPA Free Cereal Bowl, Orange
  Product 36812 | edge_importance=0.151 | category=Beauty | La Mer The Eye Concentrate 3ml x 5 = 15ml

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

- ID: 36811
- Title: Vogmask Microfiber Filtering Mask: Pink Roses
- True class (canonical `y`): **Beauty**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Health & Personal Care**
- Prediction recorded by this method's pipeline: **Health & Personal Care**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Vogmask Microfiber Filtering Mask: Pink Roses. Content: Stay healthy and keep airborne particles out of your lungs with Vogmask, the first dust masks designed to be stylish, comfortable and reusable. With the choice of high-tech microfiber or organic cotton, these comfortable, reusable masks combine protection and style like never before. Whether you seek shelter from the perils of modern life or just want relief from allergies, Vogmask has you covered. Vogmask is the world's first stylish filtering dust mask, made from the finest materials and designed to be the most comfortable dust mask ever while providing maximum protection from airborne particles.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 8361 | Health & Personal Care | Child Life Liquid Calcium/Magnesium,Natural Orange Flavor Plastic Bottle, 16-Fl. Oz. |

### 2-hop (shortest distance exactly 2): 6 nodes

| node id | true class | title |
|---|---|---|
| 983 | Health & Personal Care | Child Life Probiotics Plus Colostrum Chewable Tablets, Mixed Berry Flavor, 90 Count |
| 8389 | Health & Personal Care | Amerifit Culturelle Probiotics for Kids, 30 Count |
| 36810 | Baby | thinkbaby BPA Free Cereal Bowl, Orange |
| 36812 | Beauty | La Mer The Eye Concentrate 3ml x 5 = 15ml |
| 36813 | Baby | Thermos FUNtainer Stainless Steel 10 oz Leak-Proof Straw Bottle - Mickey Mouse |
| 36814 | Beauty | Aveeno Eczema Therapy  Bath Treatment, 3 Count (Pack of 2) |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=36811).
Recorded prediction: `{"Target Node": 36811, "Predicted Class": "Health & Personal Care", "Confidence": 0.8857}`
Recorded graph stats: `{"total_1hop_degree": 1, "neighbor_label_ratio": {"Health & Personal Care": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | microfiber | 0.708 | 1 |
| 2 | support | 0.7018 | 0 |
| 3 | like | 0.7006 | 1 |
| 4 | reusable | 0.6988 | 1 |
| 5 | essenti | 0.6971 | 0 |
| 6 | designed | 0.6939 | 1 |
| 7 | first | 0.6912 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
