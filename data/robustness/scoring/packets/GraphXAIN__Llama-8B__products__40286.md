# Reference packet: GraphXAIN__Llama-8B__products__40286

- Method: GraphXAIN; configuration: Llama-8B; dataset: products; target node: 40286
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/products/graphxain_products_llama_narratives_fulleval.json` ([40286])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model predicted that the target product "Schleich Giganotosaurus" belongs to the category "Toys & Games" with high confidence (0.8705). This prediction is supported by several key features. Notably, the top Bag-of-Words (BOW) features include words like "game," "time," and "play," which although absent in the product description, strongly associate with toys and games in the training data. Additionally, many high-importance words related to dinosaurs, such as "size," "lower," and "front," suggest a product fitting within the toy category. Furthermore, the model took cues from the product's direct co-purchase neighbors, including other dinosaur figures like "Tyrannosaurus Rex" and "Brachiosaurus," which solidified the prediction of "Toys & Games." Importantly, these highly-influential neighbors further reinforced the association between the target product and dinosaur toys. Overall, the combination of BOW features and co-purchase patterns led the model to confidently predict that "Schleich Giganotosaurus" falls under "Toys & Games".
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

### Target Product (node 40286):
Product from Amazon platform with title and content: Title: Schleich Giganotosaurus. Content: Schleich's Giganotosaurus is the perfect size for playing, has movable lower jaw. With small quills and large spots on its back, this dinosaur was quite a sight. The Gigantosaurus had three claws on each of

### Model Prediction:
{
  "Target Node": 40286,
  "Predicted Class": "Toys & Games",
  "Confidence": 0.8705
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='game', importance=0.7503, present_in_product=0
  word='time', importance=0.7393, present_in_product=0
  word='size', importance=0.7358, present_in_product=1
  word='front', importance=0.7326, present_in_product=1
  word='lower', importance=0.7316, present_in_product=1
  word='fantasi', importance=0.7265, present_in_product=0
  word='play', importance=0.7247, present_in_product=0

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 4
Label distribution across all 1-hop neighbors (ground-truth category): Toys & Games=50.0%, Books=25.0%, Home & Kitchen=25.0%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 9387 | edge_importance=0.7799 | category=Toys & Games | Tyrannosaurus Rex Soft Plastic Dinosaur (Large)
  Product 9357 | edge_importance=0.7557 | category=Toys & Games | Schleich Brachiosaurus
  Product 9392 | edge_importance=0.7545 | category=Home & Kitchen | (24x36) Dinosaur Evolution Educational Science Chart Poster
  Product 9365 | edge_importance=0.7536 | category=Books | Walking With Dinosaurs: A Reusable Sticker Book (Walking With Dinosaurs the 3d Movie)

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 40407 | edge_importance=0.8524 | category=Toys & Games | Realistic Triceratops 12&quot; by Wild Republic
  Product 40426 | edge_importance=0.8119 | category=Books | Dinosaurs and Other Prehistoric Animals (Smithsonian Handbooks)
  Product 40308 | edge_importance=0.8115 | category=Toys & Games | Spinosaurus
  Product 1119 | edge_importance=0.8094 | category=Toys & Games | "Hatch'em (Growing Pet Dinosaur)"
  Product 40408 | edge_importance=0.8066 | category=Toys & Games | Schleich Velociraptor
  Product 9385 | edge_importance=0.7885 | category=Books | How Do Dinosaurs Play with Their Friends?
  Product 40284 | edge_importance=0.7841 | category=Toys & Games | Schleich Triceratops Figure
  Product 10599 | edge_importance=0.7791 | category=Toys & Games | Safari Ltd  Wild Safari Liopleurodon
  Product 40288 | edge_importance=0.7738 | category=Toys & Games | CollectA Diplodocus Dinosaur Toy
  Product 40409 | edge_importance=0.7602 | category=Toys & Games | 12 foam dinosaur masks
  Product 40287 | edge_importance=0.7498 | category=Toys & Games | Papo Plesiosaurus
  Product 40427 | edge_importance=0.7303 | category=Toys & Games | Dinosaurs Match Me Game

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

- ID: 40286
- Title: Schleich Giganotosaurus
- True class (canonical `y`): **Toys & Games**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Toys & Games**
- Prediction recorded by this method's pipeline: **Toys & Games**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Schleich Giganotosaurus. Content: Schleich's Giganotosaurus is the perfect size for playing, has movable lower jaw. With small quills and large spots on its back, this dinosaur was quite a sight. The Gigantosaurus had three claws on each of its short front legs and fed on herbivores. Scientists suspect that the Gigantosaurus was able to run very fast thanks to its thin tail which it held upright.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 4 nodes

| node id | true class | title |
|---|---|---|
| 9357 | Toys & Games | Schleich Brachiosaurus |
| 9365 | Books | Walking With Dinosaurs: A Reusable Sticker Book (Walking With Dinosaurs the 3d Movie) |
| 9387 | Toys & Games | Tyrannosaurus Rex Soft Plastic Dinosaur (Large) |
| 9392 | Home & Kitchen | (24x36) Dinosaur Evolution Educational Science Chart Poster |

### 2-hop (shortest distance exactly 2): 20 nodes

| node id | true class | title |
|---|---|---|
| 1118 | Toys & Games | Schleich Tyrannosaurus Rex |
| 1119 | Toys & Games | "Hatch'em (Growing Pet Dinosaur)" |
| 1121 | Books | My Big Dinosaur Book |
| 9385 | Books | How Do Dinosaurs Play with Their Friends? |
| 10599 | Toys & Games | Safari Ltd  Wild Safari Liopleurodon |
| 40284 | Toys & Games | Schleich Triceratops Figure |
| 40285 | Toys & Games | Safari LTD Carnegie Brachiosaurus |
| 40287 | Toys & Games | Papo Plesiosaurus |
| 40288 | Toys & Games | CollectA Diplodocus Dinosaur Toy |
| 40308 | Toys & Games | Spinosaurus |
| 40320 | Toys & Games | Walking With Dinosaurs (Pack of 3) |
| 40321 | Toys & Games | Schleich Triceratops |
| 40322 | Toys & Games | Papo Pachyrhinosaurus |
| 40407 | Toys & Games | Realistic Triceratops 12&quot; by Wild Republic |
| 40408 | Toys & Games | Schleich Velociraptor |
| 40409 | Toys & Games | 12 foam dinosaur masks |
| 40425 | Tools & Home Improvement | Dinosaur Volcano Decorative Outlet Cover |
| 40426 | Books | Dinosaurs and Other Prehistoric Animals (Smithsonian Handbooks) |
| 40427 | Toys & Games | Dinosaurs Match Me Game |
| 40428 | Home & Kitchen | Famous Scientists Poster Print, 24x36 Poster Print, 24x36 |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=40286).
Recorded prediction: `{"Target Node": 40286, "Predicted Class": "Toys & Games", "Confidence": 0.8705}`
Recorded graph stats: `{"total_1hop_degree": 4, "neighbor_label_ratio": {"Toys & Games": 0.5, "Books": 0.25, "Home & Kitchen": 0.25}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | game | 0.7503 | 0 |
| 2 | time | 0.7393 | 0 |
| 3 | size | 0.7358 | 1 |
| 4 | front | 0.7326 | 1 |
| 5 | lower | 0.7316 | 1 |
| 6 | fantasi | 0.7265 | 0 |
| 7 | play | 0.7247 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
