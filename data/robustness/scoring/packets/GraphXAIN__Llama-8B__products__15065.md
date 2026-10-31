# Reference packet: GraphXAIN__Llama-8B__products__15065

- Method: GraphXAIN; configuration: Llama-8B; dataset: products; target node: 15065
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/products/graphxain_products_llama_narratives_fulleval.json` ([15065])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The machine learning model predicted the target product node, with the title "Camera Extender Handheld Telescopic Monopod" belonging to the "Sports & Outdoors" category with a confidence level of 52%. The top BOW features revealed that words like "universal", "using", and "quick" had strong associations with the model's decision, and interestingly, these words were indeed present in the product's title and description. Furthermore, the model considered the strongly co-purchased product "Adjustable Chest Mount Harness for Gopro Hd Hero 2 Hero 3 Camera" that shares similar characteristics with the target product, heavily influencing the prediction. While analyzing the product's connections, we observed that its 1-hop neighbors were overwhelmingly classified under the "Sports & Outdoors" category, supporting the model's conclusion. Additionally, the presence of electronics-related products among the 2-hop neighbors didn't significantly shift the model's stance, indicating that it stayed focused on the strong sports-related signals. Overall, the combination of indicative product attributes and patterns derived from local graph structure led to the prediction. This outcome showcases the model's ability to identify connections between product descriptions and related items, making accurate category predictions.
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

### Target Product (node 15065):
Product from Amazon platform with title and content: Title: Camera Extender Handheld Telescopic Monopod +Tripod Mount Adapter for Gopro Hero 1/ 2/ 3 Camera Monopod. Content: This monopod is a universal camera holder, easy to carry, and fits all compact cameras. With it, you can photograph and video 

### Model Prediction:
{
  "Target Node": 15065,
  "Predicted Class": "Sports & Outdoors",
  "Confidence": 0.5209
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='universal', importance=0.7252, present_in_product=1
  word='using', importance=0.7199, present_in_product=1
  word='activ', importance=0.7171, present_in_product=0
  word='using', importance=0.7146, present_in_product=1
  word='quick', importance=0.7075, present_in_product=1
  word='one', importance=0.7047, present_in_product=1
  word='using', importance=0.7037, present_in_product=1

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 1
Label distribution across all 1-hop neighbors (ground-truth category): Sports & Outdoors=100.0%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 2082 | edge_importance=0.639 | category=Sports & Outdoors | Adjustable Chest Mount Harness for Gopro Hd Hero 2 Hero 3 Camera - Black

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 15064 | edge_importance=0.8647 | category=Electronics | WoCase&reg; Wrist Strap Mount for GoPro HD HERO3+ 3 2 1 Cameras (Compatible with Housing and Frame)
  Product 14980 | edge_importance=0.8131 | category=Cell Phones & Accessories | VicTsing Suction Cup Mount for GoPro HD HERO HERO2 HERO3 Camera (Tripod Mount and Handle Screw)
  Product 178 | edge_importance=0.7727 | category=Cell Phones & Accessories | Hitcase ChestR Mount
  Product 2069 | edge_importance=0.1898 | category=Sports & Outdoors | Jmt Sports Camera Handlebar Seatpost Rack Mount Compatible Gopro Hd Hero 2 3
  Product 2109 | edge_importance=0.1581 | category=Electronics | POV Dive Buoy Floating Camera Handle - GoPro Edition
  Product 15063 | edge_importance=0.1509 | category=Electronics | WoCase&reg; Adjustable (Anti-Slippery) Head Strap Mount and Quick Clip Mount for GoPro HERO3+ 3 2 1 Cameras

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

- ID: 15065
- Title: Camera Extender Handheld Telescopic Monopod +Tripod Mount Adapter for Gopro Hero 1/ 2/ 3 Camera Monopod
- True class (canonical `y`): **Electronics**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Sports & Outdoors**
- Prediction recorded by this method's pipeline: **Sports & Outdoors**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Camera Extender Handheld Telescopic Monopod +Tripod Mount Adapter for Gopro Hero 1/ 2/ 3 Camera Monopod. Content: This monopod is a universal camera holder, easy to carry, and fits all compact cameras. With it, you can photograph and video by yourself anywhere! Product Feature: -Durable metal shaft, lightweight, usable and easy to carry with -Fit most of compact cameras, connecting to the tripod mount of cameras -Considerate design of the quick spin knob for fast and convenient mounting -Non-slip handle for better using experience and wonderful touch feeling -180-degree rotation, providing convenience for the users while they are taking photos -Adjustable design not only makes it portable but also eliminates awkward photos taken at arms length Package Content: -1 x Monopod -1 x Tripod adapter
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 2082 | Sports & Outdoors | Adjustable Chest Mount Harness for Gopro Hd Hero 2 Hero 3 Camera - Black |

### 2-hop (shortest distance exactly 2): 6 nodes

| node id | true class | title |
|---|---|---|
| 178 | Cell Phones & Accessories | Hitcase ChestR Mount |
| 2069 | Sports & Outdoors | Jmt Sports Camera Handlebar Seatpost Rack Mount Compatible Gopro Hd Hero 2 3 |
| 2109 | Electronics | POV Dive Buoy Floating Camera Handle - GoPro Edition |
| 14980 | Cell Phones & Accessories | VicTsing Suction Cup Mount for GoPro HD HERO HERO2 HERO3 Camera (Tripod Mount and Handle Screw) |
| 15063 | Electronics | WoCase&reg; Adjustable (Anti-Slippery) Head Strap Mount and Quick Clip Mount for GoPro HERO3+ 3 2 1 Cameras |
| 15064 | Electronics | WoCase&reg; Wrist Strap Mount for GoPro HD HERO3+ 3 2 1 Cameras (Compatible with Housing and Frame) |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=15065).
Recorded prediction: `{"Target Node": 15065, "Predicted Class": "Sports & Outdoors", "Confidence": 0.5209}`
Recorded graph stats: `{"total_1hop_degree": 1, "neighbor_label_ratio": {"Sports & Outdoors": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | universal | 0.7252 | 1 |
| 2 | using | 0.7199 | 1 |
| 3 | activ | 0.7171 | 0 |
| 4 | using | 0.7146 | 1 |
| 5 | quick | 0.7075 | 1 |
| 6 | one | 0.7047 | 1 |
| 7 | using | 0.7037 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
