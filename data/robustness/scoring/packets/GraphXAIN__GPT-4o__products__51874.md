# Reference packet: GraphXAIN__GPT-4o__products__51874

- Method: GraphXAIN; configuration: GPT-4o; dataset: products; target node: 51874
- Explanation source: `./robustness_2026-10-30/graphxain_gpt4o/products/51874.json` (narrative)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The GNN model predicted that the target product, Pure Essence Labs Ionic-Fizz Super D-K Calcium Plus Mineral Supplement, belongs to the 'Books' category, with a confidence level of 50.55%. Despite the model's decision, none of the top bag-of-words (BOW) features such as 'editor', 'heal', 'washington', and 'classic' are present in the product's description, although they carry strong associations typically relevant to books or literature. The prediction was significantly influenced by its direct co-purchase neighbor, 'Staying Healthy With the Seasons', which is categorized under 'Books'. This co-purchase relationship likely created an impression that the target product shares characteristics with book products. Additionally, 2-hop neighbors, including titles such as 'The Encyclopedia of Natural Medicine Third Edition' and 'Integrative Nutrition', all classified as 'Books', reinforced this categorization. These connections suggest that customers purchasing the supplement may have interests aligning with health-related literature. Consequently, both the strong book-related network connections and the absence of specific health or supplement-related vocabulary in the BOW features directed the model towards categorizing the supplement under 'Books'.
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

### Target Product (node 51874):
Product from Amazon platform with title and content: Title: Pure Essence Labs Ionic-Fizz Super D-K Calcium Plus Mineral Supplement, Raspberry, Lemonade, 420 Gram. Content: Ionic-Fizz Super D-K Calcium Plus - Raspberry Lemonade

### Model Prediction:
{
  "Target Node": 51874,
  "Predicted Class": "Books",
  "Confidence": 0.5055
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='editor', importance=0.7893, present_in_product=0
  word='heal', importance=0.7698, present_in_product=0
  word='washington', importance=0.7629, present_in_product=0
  word='classic', importance=0.7613, present_in_product=0
  word='health', importance=0.7565, present_in_product=0
  word='live', importance=0.7542, present_in_product=0
  word='use', importance=0.7534, present_in_product=0

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 1
Label distribution across all 1-hop neighbors (ground-truth category): Books=100.0%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 12727 | edge_importance=0.9027 | category=Books | Staying Healthy With the Seasons

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 1544 | edge_importance=0.8613 | category=Books | The Encyclopedia of Natural Medicine Third Edition
  Product 51876 | edge_importance=0.7921 | category=Books | "The Herbalist's Way: The Art and Practice of Healing with Plant Medicines"
  Product 51877 | edge_importance=0.7788 | category=Books | Integrative Nutrition
  Product 12717 | edge_importance=0.6389 | category=Books | Encyclopedia of Healing Foods
  Product 51875 | edge_importance=0.1147 | category=Books | A Practical Guide to Acu-points

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

- ID: 51874
- Title: Pure Essence Labs Ionic-Fizz Super D-K Calcium Plus Mineral Supplement, Raspberry, Lemonade, 420 Gram
- True class (canonical `y`): **Health & Personal Care**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Books**
- Prediction recorded by this method's pipeline: **Books**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Pure Essence Labs Ionic-Fizz Super D-K Calcium Plus Mineral Supplement, Raspberry, Lemonade, 420 Gram. Content: Ionic-Fizz Super D-K Calcium Plus - Raspberry Lemonade
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 12727 | Books | Staying Healthy With the Seasons |

### 2-hop (shortest distance exactly 2): 5 nodes

| node id | true class | title |
|---|---|---|
| 1544 | Books | The Encyclopedia of Natural Medicine Third Edition |
| 12717 | Books | Encyclopedia of Healing Foods |
| 51875 | Books | A Practical Guide to Acu-points |
| 51876 | Books | "The Herbalist's Way: The Art and Practice of Healing with Plant Medicines" |
| 51877 | Books | Integrative Nutrition |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=51874).
Recorded prediction: `{"Target Node": 51874, "Predicted Class": "Books", "Confidence": 0.5055}`
Recorded graph stats: `{"total_1hop_degree": 1, "neighbor_label_ratio": {"Books": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | editor | 0.7893 | 0 |
| 2 | heal | 0.7698 | 0 |
| 3 | washington | 0.7629 | 0 |
| 4 | classic | 0.7613 | 0 |
| 5 | health | 0.7565 | 0 |
| 6 | live | 0.7542 | 0 |
| 7 | use | 0.7534 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
