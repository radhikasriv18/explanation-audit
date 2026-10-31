# Reference packet: GraphXAIN__Llama-8B__products__38815

- Method: GraphXAIN; configuration: Llama-8B; dataset: products; target node: 38815
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/products/graphxain_products_llama_narratives_fulleval.json` ([38815])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
For node 38815, the GNN model predicted a classification of "Tools & Home Improvement" with a confidence level of 0.5342. This categorization was influenced by several key features, including high-importance words that were notably absent in the product's title and description, such as "technolog," "year," and "use." However, it's the presence of related terms like these, rather than their absence, which drives this trend - highlighting a nuanced association with technical features and applicability. Furthermore, the model strongly took into account direct co-purchase neighbors that also belonged to the Tools & Home Improvement category, especially notable influences like the Streamlight 73001 Nano Light Miniature Keychain LED Flashlight, which shares similarities in functionality and intended use with our target product. As additional contextual support, secondary connections through 2-hop co-purchase relationships involving items like flashlights further reinforce the classification, solidifying its placement within the Tools & Home Improvement category. These patterns collectively pointed the model towards its eventual prediction, taking into account a combination of explicit attributes and implicit connections. Overall, the model's confident decision reflects a weighted consideration of both technical features and collaborative purchasing behavior among Amazon customers. In summary, multiple pieces of evidence contribute to this specific prediction of "Tools & Home Improvement" for product 38815.
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

### Target Product (node 38815):
Product from Amazon platform with title and content: Title: FOURSEVENS Quark AA&sup2;/ Pro QP2A-X Black Finish / Cool White LED; 2XAA; 280 Lumens. Content: The Quark series offers a staggering array of options, accessories and interchangeability. With a wide range of LED, battery and clip choices, y

### Model Prediction:
{
  "Target Node": 38815,
  "Predicted Class": "Tools & Home Improvement",
  "Confidence": 0.5342
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='technolog', importance=0.76, present_in_product=0
  word='year', importance=0.759, present_in_product=0
  word='hour', importance=0.7516, present_in_product=0
  word='one', importance=0.7516, present_in_product=0
  word='provid', importance=0.7475, present_in_product=0
  word='use', importance=0.7466, present_in_product=0
  word='know', importance=0.746, present_in_product=0

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 1
Label distribution across all 1-hop neighbors (ground-truth category): Tools & Home Improvement=100.0%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 8935 | edge_importance=0.8555 | category=Tools & Home Improvement | Streamlight 73001 Nano Light Miniature Keychain LED Flashlight, Black

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 1053 | edge_importance=0.8163 | category=Arts, Crafts & Sewing | Singer Sewing Kit in Egg Shaped Storage Case
  Product 38813 | edge_importance=0.7766 | category=Sports & Outdoors | Cold Steel Inferno
  Product 38816 | edge_importance=0.194 | category=Tools & Home Improvement | MECO(TM) Mini CREE Led Flashlight Torch Adjustable Zoom Light Lamp
  Product 38817 | edge_importance=0.1762 | category=Sports & Outdoors | Light My Fire Swedish Firesteel Mini 1,500 Strike Ultralight Fire Starter
  Product 38814 | edge_importance=0.1596 | category=Sports & Outdoors | Kelty Redwing 50 Internal Frame Pack (Black, Small/Medium -14

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

- ID: 38815
- Title: FOURSEVENS Quark AA&sup2;/ Pro QP2A-X Black Finish / Cool White LED; 2XAA; 280 Lumens
- True class (canonical `y`): **Tools & Home Improvement**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Tools & Home Improvement**
- Prediction recorded by this method's pipeline: **Tools & Home Improvement**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: FOURSEVENS Quark AA&sup2;/ Pro QP2A-X Black Finish / Cool White LED; 2XAA; 280 Lumens. Content: The Quark series offers a staggering array of options, accessories and interchangeability. With a wide range of LED, battery and clip choices, you get the features you want without compromise. Waterproof and constructed with aircraft-grade aluminum and impact-resistant lenses, Quark lights are tough enough to meet any challenge.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 8935 | Tools & Home Improvement | Streamlight 73001 Nano Light Miniature Keychain LED Flashlight, Black |

### 2-hop (shortest distance exactly 2): 5 nodes

| node id | true class | title |
|---|---|---|
| 1053 | Arts, Crafts & Sewing | Singer Sewing Kit in Egg Shaped Storage Case |
| 38813 | Sports & Outdoors | Cold Steel Inferno .38 oz. Keyring Hardcase Unit Pepper Spray |
| 38814 | Sports & Outdoors | Kelty Redwing 50 Internal Frame Pack (Black, Small/Medium -14.5 - 18.5-Inch Torso) |
| 38816 | Tools & Home Improvement | MECO(TM) Mini CREE Led Flashlight Torch Adjustable Zoom Light Lamp |
| 38817 | Sports & Outdoors | Light My Fire Swedish Firesteel Mini 1,500 Strike Ultralight Fire Starter |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=38815).
Recorded prediction: `{"Target Node": 38815, "Predicted Class": "Tools & Home Improvement", "Confidence": 0.5342}`
Recorded graph stats: `{"total_1hop_degree": 1, "neighbor_label_ratio": {"Tools & Home Improvement": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | technolog | 0.76 | 0 |
| 2 | year | 0.759 | 0 |
| 3 | hour | 0.7516 | 0 |
| 4 | one | 0.7516 | 0 |
| 5 | provid | 0.7475 | 0 |
| 6 | use | 0.7466 | 0 |
| 7 | know | 0.746 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
