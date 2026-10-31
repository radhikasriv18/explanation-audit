# Reference packet: GraphXAIN__GPT-4o__products__30322

- Method: GraphXAIN; configuration: GPT-4o; dataset: products; target node: 30322
- Explanation source: `./robustness_2026-10-30/graphxain_gpt4o/products/30322.json` (narrative)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model predicted that the target product, "Ahi Viene Martin Corona" (described simply as a DVD), belongs to the "CDs & Vinyl" category with a confidence of 90.67%. Among the top words influencing this prediction were "use" and "miss", which are generally important but not present in the product's description, potentially indicating the model's reliance on other factors due to their absence. The direct co-purchase neighbor, "Carmen la de Ronda", is from the "Movies & TV" category, which initially seems counterintuitive, but the notable association with audio content might blur the line between media types. Additionally, 2-hop neighbors show a mix, with products under "CDs & Vinyl" like those connected through co-purchases, reinforcing the possibility of audio-related categorization. This pattern suggests that while the direct neighbor leans heavily towards "Movies & TV", the model captured broader relationships within the network that align more closely with audio media, contributing to the "CDs & Vinyl" classification. Despite the prominent influence of "Movies & TV" connections, the sparse yet specific 2-hop relations pulled the prediction toward "CDs & Vinyl", possibly due to overlapping consumer interests in audio content shared between DVDs and CDs.
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

### Target Product (node 30322):
Product from Amazon platform with title and content: Title: Ahi Viene Martin Corona. Content: dvd

### Model Prediction:
{
  "Target Node": 30322,
  "Predicted Class": "CDs & Vinyl",
  "Confidence": 0.9067
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='use', importance=0.7396, present_in_product=0
  word='miss', importance=0.7277, present_in_product=0
  word='polici', importance=0.7258, present_in_product=0
  word='use', importance=0.7228, present_in_product=1
  word='would', importance=0.7201, present_in_product=0
  word='along', importance=0.7142, present_in_product=0
  word='love', importance=0.7132, present_in_product=0

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 1
Label distribution across all 1-hop neighbors (ground-truth category): Movies & TV=100.0%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 6463 | edge_importance=0.7388 | category=Movies & TV | Carmen la de Ronda (1959) [audio in Spanish only]

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 30318 | edge_importance=0.9033 | category=Movies & TV | missing
  Product 30319 | edge_importance=0.7955 | category=Movies & TV | missing
  Product 751 | edge_importance=0.7692 | category=CDs & Vinyl | missing
  Product 743 | edge_importance=0.7407 | category=CDs & Vinyl | missing
  Product 30321 | edge_importance=0.7309 | category=Movies & TV | Vera Cruz
  Product 30320 | edge_importance=0.1714 | category=Movies & TV | Samba (NO ENGLISH) [Import]

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

- ID: 30322
- Title: Ahi Viene Martin Corona
- True class (canonical `y`): **Movies & TV**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **CDs & Vinyl**
- Prediction recorded by this method's pipeline: **CDs & Vinyl**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Ahi Viene Martin Corona. Content: dvd
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 6463 | Movies & TV | Carmen la de Ronda (1959) [audio in Spanish only] |

### 2-hop (shortest distance exactly 2): 6 nodes

| node id | true class | title |
|---|---|---|
| 743 | CDs & Vinyl | missing |
| 751 | CDs & Vinyl | missing |
| 30318 | Movies & TV | missing |
| 30319 | Movies & TV | missing |
| 30320 | Movies & TV | Samba (NO ENGLISH) [Import] |
| 30321 | Movies & TV | Vera Cruz |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=30322).
Recorded prediction: `{"Target Node": 30322, "Predicted Class": "CDs & Vinyl", "Confidence": 0.9067}`
Recorded graph stats: `{"total_1hop_degree": 1, "neighbor_label_ratio": {"Movies & TV": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | use | 0.7396 | 0 |
| 2 | miss | 0.7277 | 0 |
| 3 | polici | 0.7258 | 0 |
| 4 | use | 0.7228 | 1 |
| 5 | would | 0.7201 | 0 |
| 6 | along | 0.7142 | 0 |
| 7 | love | 0.7132 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
