# Reference packet: GraphXAIN__GPT-4o__products__47510

- Method: GraphXAIN; configuration: GPT-4o; dataset: products; target node: 47510
- Explanation source: `./robustness_2026-10-30/graphxain_gpt4o/products/47510.json` (narrative)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model predicted that the target product, a PlayStation 3 Slim Console skin, belongs to the "Video Games" category with a confidence of 24.52%. Among the top Bag-of-Words features influencing this prediction, words like "use" appear frequently and are present in the product, suggesting a functionality often associated with video game accessories. Although words such as "access," "bold," and "play" were important, their absence in the product points towards indirect associations with gaming, such as accessory design or packaging descriptions. The primary influence in the model's decision stems from the product's direct 1-hop co-purchase neighbor, another item categorized under "Video Games," highlighting a strong co-purchase trend within gaming products. This connection suggests that consumers who purchase the skin are also interested in other video game-related items. Moreover, examining the 2-hop neighbors further solidifies this classification, as the majority fall under the "Video Games" category, indicating a broader community of related purchases reinforcing the target product's categorization. Overall, the combination of present key terms and a robust network of co-purchase relationships supports the model's prediction.
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

### Target Product (node 47510):
Product from Amazon platform with title and content: Title: missing. Content: This listing is for one (1) PlayStation 3 Slim Console skin and (2) Constoller Skins displayed above. Actual controller not included. All our skins are made from the highest quality 3M material. Proudly made from 100% recy

### Model Prediction:
{
  "Target Node": 47510,
  "Predicted Class": "Video Games",
  "Confidence": 0.2452
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='use', importance=0.7841, present_in_product=1
  word='use', importance=0.7696, present_in_product=1
  word='access', importance=0.765, present_in_product=0
  word='use', importance=0.7639, present_in_product=1
  word='bold', importance=0.7627, present_in_product=0
  word='play', importance=0.7519, present_in_product=0
  word='system', importance=0.7514, present_in_product=0

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 1
Label distribution across all 1-hop neighbors (ground-truth category): Video Games=100.0%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 11442 | edge_importance=0.7565 | category=Video Games | missing

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 11417 | edge_importance=0.849 | category=Video Games | missing
  Product 47509 | edge_importance=0.8404 | category=Video Games | missing
  Product 47508 | edge_importance=0.8336 | category=Video Games | missing
  Product 11393 | edge_importance=0.7601 | category=Video Games | missing
  Product 47507 | edge_importance=0.7385 | category=Toys & Games | missing
  Product 1381 | edge_importance=0.7096 | category=Video Games | missing
  Product 1376 | edge_importance=0.1504 | category=Video Games | missing

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

- ID: 47510
- Title: missing
- True class (canonical `y`): **label 25**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Video Games**
- Prediction recorded by this method's pipeline: **Video Games**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: missing. Content: This listing is for one (1) PlayStation 3 Slim Console skin and (2) Constoller Skins displayed above. Actual controller not included. All our skins are made from the highest quality 3M material. Proudly made from 100% recycled materials here in the USA! These are Vinyl skins "Sticker" ONLY. Not a hard plastic cover or case! Sony Corporation is not affiliated with, nor does it authorize or sponsor the products being sold by 247Skins.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 11442 | Video Games | missing |

### 2-hop (shortest distance exactly 2): 7 nodes

| node id | true class | title |
|---|---|---|
| 1376 | Video Games | missing |
| 1381 | Video Games | missing |
| 11393 | Video Games | missing |
| 11417 | Video Games | missing |
| 47507 | Toys & Games | missing |
| 47508 | Video Games | missing |
| 47509 | Video Games | missing |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=47510).
Recorded prediction: `{"Target Node": 47510, "Predicted Class": "Video Games", "Confidence": 0.2452}`
Recorded graph stats: `{"total_1hop_degree": 1, "neighbor_label_ratio": {"Video Games": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | use | 0.7841 | 1 |
| 2 | use | 0.7696 | 1 |
| 3 | access | 0.765 | 0 |
| 4 | use | 0.7639 | 1 |
| 5 | bold | 0.7627 | 0 |
| 6 | play | 0.7519 | 0 |
| 7 | system | 0.7514 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
