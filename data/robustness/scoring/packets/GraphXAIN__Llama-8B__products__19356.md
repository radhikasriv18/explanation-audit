# Reference packet: GraphXAIN__Llama-8B__products__19356

- Method: GraphXAIN; configuration: Llama-8B; dataset: products; target node: 19356
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/products/graphxain_products_llama_narratives_fulleval.json` ([19356])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model predicted that the target product, which consists of a set of balsa sheets, falls under the category "Arts, Crafts & Sewing" with a moderate level of confidence at 41.63%. This prediction is heavily influenced by the presence of specific words in its product title and description, including words like "piece," "water," and "wood," all strongly associated with the crafting process. Furthermore, the model took into account the direct co-purchase relationships between this product and other items, such as the Balsa Sheets 1/16 x 6 x 36, also categorized under "Toys & Games." However, it appears that the presence of these toys-based items in the customer's basket may be a result of customers intending to use them in conjunction with balsa wood sheets for craft projects, thereby reinforcing the prediction. Interestingly, while the label distribution among the 1-hop neighbors overwhelmingly indicates "Toys & Games," the model's prediction follows the trend observed among 2-hop neighbors, where products like Loew Cornell Woodsies Spring Clothespins - a tool typically used in arts and crafts - are more aligned with the prediction. Additionally, two other 2-hop neighbors, categorized under "Arts, Crafts & Sewing" and "Arts Supplies" respectively, further support this classification. By considering both the product's inherent characteristics and its relationships within the network, the model has come up with this well-supported prediction.
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

### Target Product (node 19356):
Product from Amazon platform with title and content: Title: Balsa Sheets 3/32 x 4 x 36 (15). Content: Midwest Wood offers premium quality wood for the construction of models, doll houses, bazaar crafts and so much more! All sheets and strips are bundled and shrink-wrapped. Each individual piece is U

### Model Prediction:
{
  "Target Node": 19356,
  "Predicted Class": "Arts, Crafts & Sewing",
  "Confidence": 0.4163
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='piece', importance=0.7551, present_in_product=1
  word='water', importance=0.7532, present_in_product=1
  word='wood', importance=0.7352, present_in_product=1
  word='individual', importance=0.7346, present_in_product=1
  word='use', importance=0.7345, present_in_product=1
  word='cuts', importance=0.7341, present_in_product=1
  word='use', importance=0.734, present_in_product=1

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 1
Label distribution across all 1-hop neighbors (ground-truth category): Toys & Games=100.0%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 3315 | edge_importance=0.659 | category=Toys & Games | Balsa Sheets 1/16 x 6 x 36 (10)

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 19357 | edge_importance=0.8556 | category=Toys & Games | Balsa Strips 1/8 x 1/8 x 36 (36)
  Product 344 | edge_importance=0.8139 | category=Arts, Crafts & Sewing | Loew Cornell 1021178 Woodsies Spring Clothespins, 40 count
  Product 19355 | edge_importance=0.7587 | category=Toys & Games | Wood Cement Extra Fast,5/8 oz
  Product 19359 | edge_importance=0.6714 | category=Arts, Crafts & Sewing | Midwest Products Project Woods Balsa &amp; Basswood Strip Economy Bag
  Product 19358 | edge_importance=0.171 | category=Office Products | Pitsco Heavy Density Balsa Wood Strips (Pack of 100)

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

- ID: 19356
- Title: Balsa Sheets 3/32 x 4 x 36 (15)
- True class (canonical `y`): **Arts, Crafts & Sewing**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Arts, Crafts & Sewing**
- Prediction recorded by this method's pipeline: **Arts, Crafts & Sewing**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Balsa Sheets 3/32 x 4 x 36 (15). Content: Midwest Wood offers premium quality wood for the construction of models, doll houses, bazaar crafts and so much more! All sheets and strips are bundled and shrink-wrapped. Each individual piece is UPC coded. Balsa wood is carefully dried in special kilns, reducing the water content to leave a light wood with a high strength to weight ratio. The premier wood for all types of modeling projects, Balsa cuts easily with a hobby knife and may be stained or painted to represent any wood type.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 3315 | Toys & Games | Balsa Sheets 1/16 x 6 x 36 (10) |

### 2-hop (shortest distance exactly 2): 5 nodes

| node id | true class | title |
|---|---|---|
| 344 | Arts, Crafts & Sewing | Loew Cornell 1021178 Woodsies Spring Clothespins, 40 count |
| 19355 | Toys & Games | Wood Cement Extra Fast,5/8 oz |
| 19357 | Toys & Games | Balsa Strips 1/8 x 1/8 x 36 (36) |
| 19358 | Office Products | Pitsco Heavy Density Balsa Wood Strips (Pack of 100) |
| 19359 | Arts, Crafts & Sewing | Midwest Products Project Woods Balsa &amp; Basswood Strip Economy Bag |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=19356).
Recorded prediction: `{"Target Node": 19356, "Predicted Class": "Arts, Crafts & Sewing", "Confidence": 0.4163}`
Recorded graph stats: `{"total_1hop_degree": 1, "neighbor_label_ratio": {"Toys & Games": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | piece | 0.7551 | 1 |
| 2 | water | 0.7532 | 1 |
| 3 | wood | 0.7352 | 1 |
| 4 | individual | 0.7346 | 1 |
| 5 | use | 0.7345 | 1 |
| 6 | cuts | 0.7341 | 1 |
| 7 | use | 0.734 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
