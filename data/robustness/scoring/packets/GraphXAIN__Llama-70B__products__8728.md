# Reference packet: GraphXAIN__Llama-70B__products__8728

- Method: GraphXAIN; configuration: Llama-70B; dataset: products; target node: 8728
- Explanation source: `./robustness_2026-10-30/llama70b/graphxain/products/8728.json` (response)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The GNN model predicted that the target product belongs to the "Beauty" category with a confidence of 57.83%. This prediction was largely driven by the presence of strongly associated words in the product's content, particularly "skin" which suggests a cosmetic product, although its overall impact was tempered by words like "touch", "profession", and "brush" being less relevant due to their absence. Furthermore, the product's co-purchase connections played a key role, especially those with "Mehron Barrier Spray" from the Beauty category, highlighting the influence of products frequently bought together with the target item. Similarly, neighboring products such as face paints and makeup tools indirectly reinforced the beauty association through their strong ties with other directly linked products like "Snazaroo Face Paint". These findings indicate that both the target product's individual attributes and the broader context within which it's purchased have aligned to strongly suggest a classification in the Beauty domain. Specifically, these influences likely steered the prediction because they imply uses related to personal appearance and aesthetics commonly found in beauty products. Despite having competing signals from Toys & Games and Arts, Crafts & Sewing in the product's neighborhood, the cumulative effect of these factors ultimately led the model towards predicting a Beauty classification for the target product. Overall, the combination of highly relevant content, closely related co-purchasing patterns, and reinforcing signals from neighboring items led to the confident prediction of the target product belonging to the Beauty category.
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

### Target Product (node 8728):
Product from Amazon platform with title and content: Title: missing. Content: Paradise Makeup AQ is a semi-soft, water activated, moist cake makeup. Our unique blend of ingredients includes aloe and chamomile to help make Paradise Makeup AQ safe and gentle to the skin. Glycerin, avocado oil and coco

### Model Prediction:
{
  "Target Node": 8728,
  "Predicted Class": "Beauty",
  "Confidence": 0.5783
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='touch', importance=0.7276, present_in_product=0
  word='use', importance=0.7244, present_in_product=1
  word='profession', importance=0.7163, present_in_product=0
  word='use', importance=0.7138, present_in_product=1
  word='brush', importance=0.7138, present_in_product=0
  word='use', importance=0.7115, present_in_product=1
  word='skin', importance=0.7068, present_in_product=1

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 6
Label distribution across all 1-hop neighbors (ground-truth category): label 25=33.3%, Toys & Games=33.3%, Beauty=16.7%, Arts, Crafts & Sewing=16.7%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 38136 | edge_importance=0.8276 | category=Toys & Games | Mehron Liquid Face Paints - Glow In The Dark GL (1 oz)
  Product 8776 | edge_importance=0.8012 | category=label 25 | missing
  Product 38123 | edge_importance=0.7927 | category=Arts, Crafts & Sewing | Snazaroo Face Paint 12ml Face - Body Glitter Gel, Silver
  Product 38135 | edge_importance=0.79 | category=Toys & Games | Snazaroo High Density Face Painting Sponge (10 Pack)
  Product 38134 | edge_importance=0.6828 | category=label 25 | missing
  Product 1027 | edge_importance=0.6619 | category=Beauty | Mehron Barrier Spray (2 oz pump)

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 8727 | edge_importance=0.8249 | category=All Beauty | Mehron Ultrafine Setting Powder 2 oz (Neutral/Translucent)
  Product 8733 | edge_importance=0.8244 | category=Arts, Crafts & Sewing | Paradise Palette Basic
  Product 8726 | edge_importance=0.8219 | category=Beauty | Mehron Barrier Spray 9 oz Refill Bottle
  Product 78 | edge_importance=0.8179 | category=Beauty | Mehron CreamBlend Stick Makeup
  Product 8719 | edge_importance=0.8163 | category=Beauty | Mehron Slim Pro-Pencil Makeup - Black
  Product 8734 | edge_importance=0.813 | category=Clothing, Shoes & Jewelry | Ben Nye Clown White Makeup (2
  Product 8818 | edge_importance=0.7998 | category=Beauty | Mehron CreamBlend Stick Makeup - Black (0
  Product 8723 | edge_importance=0.7499 | category=Toys & Games | 18ML DARK GREY Classic Snazaroo Classic Face Paint
  Product 38288 | edge_importance=0.2355 | category=Arts, Crafts & Sewing | TAG Split Cakes - Berry Wine and Pink (50 gm)
  Product 8730 | edge_importance=0.2271 | category=Arts, Crafts & Sewing | Pro Arte Scholar Multi Purpose Brush Set
  Product 8731 | edge_importance=0.2222 | category=Toys & Games | Mehron Liquid Face Paints - Red R (1 oz)
  Product 8735 | edge_importance=0.218 | category=Arts, Crafts & Sewing | Snazaroo Face Paint Stipple Sponge, 2 Pack

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

- ID: 8728
- Title: missing
- True class (canonical `y`): **label 25**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Beauty**
- Prediction recorded by this method's pipeline: **Beauty**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: missing. Content: Paradise Makeup AQ is a semi-soft, water activated, moist cake makeup. Our unique blend of ingredients includes aloe and chamomile to help make Paradise Makeup AQ safe and gentle to the skin. Glycerin, avocado oil and cocoa butter provide rich, vibrant, color-saturated coverage. It requires no special removers and washes off easily with just soap and water.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 6 nodes

| node id | true class | title |
|---|---|---|
| 1027 | Beauty | Mehron Barrier Spray (2 oz pump) |
| 8776 | label 25 | missing |
| 38123 | Arts, Crafts & Sewing | Snazaroo Face Paint 12ml Face - Body Glitter Gel, Silver |
| 38134 | label 25 | missing |
| 38135 | Toys & Games | Snazaroo High Density Face Painting Sponge (10 Pack) |
| 38136 | Toys & Games | Mehron Liquid Face Paints - Glow In The Dark GL (1 oz) |

### 2-hop (shortest distance exactly 2): 20 nodes

| node id | true class | title |
|---|---|---|
| 78 | Beauty | Mehron CreamBlend Stick Makeup .75 oz (Light Buff) |
| 1032 | Beauty | Mehron Ultrafine Makeup Setting Powder - Neutral/Translucent (0.6 Oz) |
| 8717 | Toys & Games | Mehron Liquid Face Paints - White W (4.5 oz) |
| 8719 | Beauty | Mehron Slim Pro-Pencil Makeup - Black |
| 8723 | Toys & Games | 18ML DARK GREY Classic Snazaroo Classic Face Paint |
| 8726 | Beauty | Mehron Barrier Spray 9 oz Refill Bottle |
| 8727 | All Beauty | Mehron Ultrafine Setting Powder 2 oz (Neutral/Translucent) |
| 8729 | Beauty | Ben Nye Final Seal Matte Makeup Sealer 2oz Spray |
| 8730 | Arts, Crafts & Sewing | Pro Arte Scholar Multi Purpose Brush Set |
| 8731 | Toys & Games | Mehron Liquid Face Paints - Red R (1 oz) |
| 8732 | Health & Personal Care | Maxim Antiperspirant Towelette Antiperspirant Deodorant - Clinical Strength Wipes |
| 8733 | Arts, Crafts & Sewing | Paradise Palette Basic |
| 8734 | Clothing, Shoes & Jewelry | Ben Nye Clown White Makeup (2.25 oz) |
| 8735 | Arts, Crafts & Sewing | Snazaroo Face Paint Stipple Sponge, 2 Pack |
| 8818 | Beauty | Mehron CreamBlend Stick Makeup - Black (0.75 oz) |
| 38287 | Arts, Crafts & Sewing | Petal Sponge 8 PACK Snazaroo Face Painting Sponge |
| 38288 | Arts, Crafts & Sewing | TAG Split Cakes - Berry Wine and Pink (50 gm) |
| 38289 | Books | Fun Face Painting Ideas for Kids: 40 Step-by-Step Demos |
| 38290 | label 25 | missing |
| 38291 | Toys & Games | Mehron Paradise AQ Pro Face Paint Palettes (30 Colors) |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=8728).
Recorded prediction: `{"Target Node": 8728, "Predicted Class": "Beauty", "Confidence": 0.5783}`
Recorded graph stats: `{"total_1hop_degree": 6, "neighbor_label_ratio": {"label 25": 0.333, "Toys & Games": 0.333, "Beauty": 0.167, "Arts, Crafts & Sewing": 0.167}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | touch | 0.7276 | 0 |
| 2 | use | 0.7244 | 1 |
| 3 | profession | 0.7163 | 0 |
| 4 | use | 0.7138 | 1 |
| 5 | brush | 0.7138 | 0 |
| 6 | use | 0.7115 | 1 |
| 7 | skin | 0.7068 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
