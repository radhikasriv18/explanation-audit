# Reference packet: GraphXAIN__GPT-4o__products__19140

- Method: GraphXAIN; configuration: GPT-4o; dataset: products; target node: 19140
- Explanation source: `./robustness_2026-10-30/graphxain_gpt4o/products/19140.json` (narrative)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The GNN model predicted that the product "Lehigh 540W 230-Feet Polypropylene Heavy Duty Twine, Brown" belongs to the "Arts, Crafts & Sewing" category with a confidence of 49.76%. The presence of the word "heavy" and "line" in the product description significantly contributed to this prediction, aligning well with items used in crafting and sewing activities, although other top words like "project" and "round" were absent. The model also considered the direct co-purchase relationship with another "Arts, Crafts & Sewing" product, the "Darice 5-Ply Craft Designer Jute, Natural," indicating a strong association with crafting materials. Furthermore, the 2-hop neighbors, such as "Surgical Steel Earring Earwires Hypoallergenic Shiny Silver Plated Fishhook," often purchased with craft supplies, support this categorization. The absence of some words like "project" and "stereo" did not deter the model’s confidence, as the co-purchase pattern predominantly ties the twine to arts and crafts uses. Overall, the influential product connections, alongside specific relevant vocabulary, lead the model to classify the twine within the crafting category.
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

### Target Product (node 19140):
Product from Amazon platform with title and content: Title: Lehigh 540W 230-Feet Polypropylene Heavy Duty Twine, Brown. Content: Secure line by Lehigh twisted polypropylene twine. Great for hobbies, recycling, crafts, handyman work, kitchen, gardening, general household or commercial use. Durable si

### Model Prediction:
{
  "Target Node": 19140,
  "Predicted Class": "Arts, Crafts & Sewing",
  "Confidence": 0.4976
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='project', importance=0.7448, present_in_product=0
  word='round', importance=0.744, present_in_product=0
  word='heavy', importance=0.7392, present_in_product=1
  word='packag', importance=0.738, present_in_product=0
  word='stereo', importance=0.7379, present_in_product=0
  word='line', importance=0.7353, present_in_product=1
  word='use', importance=0.7316, present_in_product=0

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 1
Label distribution across all 1-hop neighbors (ground-truth category): Arts, Crafts & Sewing=100.0%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 3267 | edge_importance=0.646 | category=Arts, Crafts & Sewing | Darice 5-Ply Craft Designer Jute, Natural

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 19139 | edge_importance=0.8089 | category=Arts, Crafts & Sewing | Surgical Steel Earring Earwires Hypoallergenic Shiny Silver Plated Fishhook with 10x3
  Product 19137 | edge_importance=0.7775 | category=Office Products | Darice 135-Feet 4 Ply Jute, 1-Pound
  Product 339 | edge_importance=0.7375 | category=Arts, Crafts & Sewing | Darice 0500-04 Wood Beads, Large, Assorted Color
  Product 19138 | edge_importance=0.1721 | category=Arts, Crafts & Sewing | Hemtique Cord Spool 20-Pound, Dark Brown

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

- ID: 19140
- Title: Lehigh 540W 230-Feet Polypropylene Heavy Duty Twine, Brown
- True class (canonical `y`): **Office Products**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Arts, Crafts & Sewing**
- Prediction recorded by this method's pipeline: **Arts, Crafts & Sewing**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Lehigh 540W 230-Feet Polypropylene Heavy Duty Twine, Brown. Content: Secure line by Lehigh twisted polypropylene twine. Great for hobbies, recycling, crafts, handyman work, kitchen, gardening, general household or commercial use. Durable sisal substitute. Polypropylene and polyester construction. Easy on the hands. Unique overwrap offers customers a dispensing feature that keeps twin clean and tangle free. Available in brown color. Measures 230-Feet length.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 3267 | Arts, Crafts & Sewing | Darice 5-Ply Craft Designer Jute, Natural |

### 2-hop (shortest distance exactly 2): 4 nodes

| node id | true class | title |
|---|---|---|
| 339 | Arts, Crafts & Sewing | Darice 0500-04 Wood Beads, Large, Assorted Color |
| 19137 | Office Products | Darice 135-Feet 4 Ply Jute, 1-Pound |
| 19138 | Arts, Crafts & Sewing | Hemtique Cord Spool 20-Pound, Dark Brown |
| 19139 | Arts, Crafts & Sewing | Surgical Steel Earring Earwires Hypoallergenic Shiny Silver Plated Fishhook with 10x3.5mm Ball and Coil with Open Loop, 21 Gauge. 100 Pairs. (200) |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=19140).
Recorded prediction: `{"Target Node": 19140, "Predicted Class": "Arts, Crafts & Sewing", "Confidence": 0.4976}`
Recorded graph stats: `{"total_1hop_degree": 1, "neighbor_label_ratio": {"Arts, Crafts & Sewing": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | project | 0.7448 | 0 |
| 2 | round | 0.744 | 0 |
| 3 | heavy | 0.7392 | 1 |
| 4 | packag | 0.738 | 0 |
| 5 | stereo | 0.7379 | 0 |
| 6 | line | 0.7353 | 1 |
| 7 | use | 0.7316 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
