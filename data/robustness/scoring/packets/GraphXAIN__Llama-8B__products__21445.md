# Reference packet: GraphXAIN__Llama-8B__products__21445

- Method: GraphXAIN; configuration: Llama-8B; dataset: products; target node: 21445
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/products/graphxain_products_llama_narratives_fulleval.json` ([21445])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The GNN model predicted that the Evans Sports Standing Rifle Rack would belong to the 'Sports & Outdoors' category with an impressive confidence level of 90.48%. This prediction was significantly influenced by several key features extracted from the product's Bag-of-Words representation, including strong associations with the words 'rifle' and 'use', despite neither being explicitly present in the product title and description. Additionally, the local graph structure showed a stark absence of any neighboring products belonging to the same category, except for mostly books among the 1-hop co-purchase neighbors - a striking exception being "The Mosin-Nagant Rifle, 6th Edition" which has some relevance due to its categorization under Books yet has the word rifle - hinting at co-purchase patterns between rifles and literature about these items. Moreover, further reinforcing the sports and outdoors prediction were the strongly-associated direct co-purchase neighbors, primarily comprised of other firearm accessories and equipment. Interestingly, many of the 2-hop co-purchase neighbors also fell into the 'Sports & Outdoors' category, highlighting a larger trend where the target product tends to be bought along with similar items. Overall, it appears that the model accurately identified the product's place within this broader category by recognizing both explicit features as well as implicit connections to related items, making a compelling case for why this prediction emerged. By analyzing various layers of data, we gain insight into how the model drew conclusions about this specific product's likely classification.
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

### Target Product (node 21445):
Product from Amazon platform with title and content: Title: Evans Sports Standing Rifle Rack. Content: The Evans Standing Rifle Rack measuring 31"x 10"x 35 1/2" is made of solid native pine. It holds up to seven long guns. Assembly Required with all assembly hardware included. Recommended for indoor

### Model Prediction:
{
  "Target Node": 21445,
  "Predicted Class": "Sports & Outdoors",
  "Confidence": 0.9048
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='precis', importance=0.7439, present_in_product=0
  word='english', importance=0.7386, present_in_product=0
  word='use', importance=0.7345, present_in_product=1
  word='provid', importance=0.7331, present_in_product=0
  word='depth', importance=0.7323, present_in_product=0
  word='rifle', importance=0.73, present_in_product=1
  word='use', importance=0.7222, present_in_product=0

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 1
Label distribution across all 1-hop neighbors (ground-truth category): Books=100.0%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 3893 | edge_importance=0.7757 | category=Books | The Mosin-Nagant Rifle, 6th Edition (For collectors only)

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 21214 | edge_importance=0.8511 | category=Books | The Lee-Enfield Rifle (Weapon)
  Product 21233 | edge_importance=0.8305 | category=Sports & Outdoors | ProMag Archangel Opfor AA9130 Forend Rail, Black
  Product 21443 | edge_importance=0.8132 | category=Sports & Outdoors | Mosin Nagant 91/30 &quot;Range Buddy&quot; Front Sight Adjustment Tool
  Product 3827 | edge_importance=0.7955 | category=Sports & Outdoors | Set of 40 BRAND NEW Stripper Clips For Mosin Nagant 1891/30 91/30 M38 M39 M44 7
  Product 3846 | edge_importance=0.2052 | category=Sports & Outdoors | Mauser Stripper Clips 40CT 6
  Product 422 | edge_importance=0.1269 | category=label 25 | missing
  Product 21444 | edge_importance=0.1003 | category=Sports & Outdoors | Pachmayr Decelerator Slip On Recoil Pad

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

- ID: 21445
- Title: Evans Sports Standing Rifle Rack
- True class (canonical `y`): **Sports & Outdoors**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Sports & Outdoors**
- Prediction recorded by this method's pipeline: **Sports & Outdoors**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Evans Sports Standing Rifle Rack. Content: The Evans Standing Rifle Rack measuring 31"x 10"x 35 1/2" is made of solid native pine. It holds up to seven long guns. Assembly Required with all assembly hardware included. Recommended for indoor use only. Made in the USA.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 3893 | Books | The Mosin-Nagant Rifle, 6th Edition (For collectors only) |

### 2-hop (shortest distance exactly 2): 7 nodes

| node id | true class | title |
|---|---|---|
| 422 | label 25 | missing |
| 3827 | Sports & Outdoors | Set of 40 BRAND NEW Stripper Clips For Mosin Nagant 1891/30 91/30 M38 M39 M44 7.62X54r Rifles |
| 3846 | Sports & Outdoors | Mauser Stripper Clips 40CT 6.5x55mm 38,94,96 &amp; 30-06, 1903, 1917 |
| 21214 | Books | The Lee-Enfield Rifle (Weapon) |
| 21233 | Sports & Outdoors | ProMag Archangel Opfor AA9130 Forend Rail, Black |
| 21443 | Sports & Outdoors | Mosin Nagant 91/30 &quot;Range Buddy&quot; Front Sight Adjustment Tool |
| 21444 | Sports & Outdoors | Pachmayr Decelerator Slip On Recoil Pad |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=21445).
Recorded prediction: `{"Target Node": 21445, "Predicted Class": "Sports & Outdoors", "Confidence": 0.9048}`
Recorded graph stats: `{"total_1hop_degree": 1, "neighbor_label_ratio": {"Books": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | precis | 0.7439 | 0 |
| 2 | english | 0.7386 | 0 |
| 3 | use | 0.7345 | 1 |
| 4 | provid | 0.7331 | 0 |
| 5 | depth | 0.7323 | 0 |
| 6 | rifle | 0.73 | 1 |
| 7 | use | 0.7222 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
