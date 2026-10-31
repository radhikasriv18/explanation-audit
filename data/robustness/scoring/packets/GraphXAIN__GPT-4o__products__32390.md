# Reference packet: GraphXAIN__GPT-4o__products__32390

- Method: GraphXAIN; configuration: GPT-4o; dataset: products; target node: 32390
- Explanation source: `./robustness_2026-10-30/graphxain_gpt4o/products/32390.json` (narrative)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model predicted that the Gerber Paraframe Mini Knife belongs to the "Sports & Outdoors" category with a high confidence of 99.43%. This prediction is influenced by certain key features in the product description, such as the word "use," which appears multiple times and is strongly associated with products that are versatile and functional, traits often linked to outdoor gear. The word "dimens" also contributes significantly, indicating relevance to product specifications, which is common in sporting equipment descriptions. Interestingly, the absence of the word "year" suggests the product's timeless utility, aligning with outdoor products' enduring appeal. The model also considered the direct co-purchase relationship with the Gerber LST Folding Knife, which belongs to the "Tools & Home Improvement" category; however, this connection was less persuasive for the prediction due to its contrasting category. More compellingly, several influential 2-hop neighbors, such as the Buck 55 Folding Hunter and Case Cutlery 004, are categorized under "Sports & Outdoors." These connections reinforce the model's decision as they reflect a pattern of co-purchase behavior strongly tied to outdoor activities and gear, aligning with the overall prediction.
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

### Target Product (node 32390):
Product from Amazon platform with title and content: Title: Gerber Paraframe Mini Knife. Content: Don't let the 3-inch folded size of the Mini fool you; Gerber gives this little guy the same attention to detail that has won the larger Paraframe models a dedicated following. You'll notice the same er

### Model Prediction:
{
  "Target Node": 32390,
  "Predicted Class": "Sports & Outdoors",
  "Confidence": 0.9943
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='use', importance=0.6959, present_in_product=1
  word='use', importance=0.6853, present_in_product=1
  word='use', importance=0.6845, present_in_product=1
  word='dimens', importance=0.6841, present_in_product=1
  word='use', importance=0.6746, present_in_product=1
  word='use', importance=0.6716, present_in_product=1
  word='year', importance=0.6715, present_in_product=0

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 1
Label distribution across all 1-hop neighbors (ground-truth category): Tools & Home Improvement=100.0%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 7041 | edge_importance=0.7485 | category=Tools & Home Improvement | Gerber LST Folding Knife 22-06009

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 32391 | edge_importance=0.8271 | category=Sports & Outdoors | Buck 55 Folding Hunter
  Product 32389 | edge_importance=0.817 | category=Sports & Outdoors | Case Cutlery 004 Case Executive Lockback Pocket Knife With Stainless Steel Blade   Metal
  Product 32392 | edge_importance=0.7791 | category=Sports & Outdoors | Bantam BBW
  Product 32393 | edge_importance=0.7464 | category=Sports & Outdoors | Gerber 31-001088 Myth Pocket Folder, Fine Edge Folding Lock-Back Clip Knife
  Product 822 | edge_importance=0.1347 | category=Tools & Home Improvement | Gerber 31-001709 Swagger Assisted Opening Clip Knife

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

- ID: 32390
- Title: Gerber Paraframe Mini Knife
- True class (canonical `y`): **Sports & Outdoors**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Sports & Outdoors**
- Prediction recorded by this method's pipeline: **Sports & Outdoors**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Gerber Paraframe Mini Knife. Content: Don't let the 3-inch folded size of the Mini fool you; Gerber gives this little guy the same attention to detail that has won the larger Paraframe models a dedicated following. You'll notice the same ergonomic metal handle and frame lock design, and it delivers the same positive blade engagement and balanced feel, even at this size. Features: - Tanto-style blade - Black titanium nitride-coated blade - Full fine edge blade is easy to sharpen - Frame lock - Pocket clip - Small size disappears in your pocket Specifications: - Overall Length: 5.25" (13.34 cm) - Blade Length: 2.13" (5.41 cm) - Closed Length: 3.13" (7.95 cm) - Weight: 1.5 oz. (43 g) - Steel Type: 7Cr17MoV - Handle Material: 3Cr13.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 7041 | Tools & Home Improvement | Gerber LST Folding Knife 22-06009 |

### 2-hop (shortest distance exactly 2): 5 nodes

| node id | true class | title |
|---|---|---|
| 822 | Tools & Home Improvement | Gerber 31-001709 Swagger Assisted Opening Clip Knife |
| 32389 | Sports & Outdoors | Case Cutlery 004 Case Executive Lockback Pocket Knife With Stainless Steel Blade   Metal |
| 32391 | Sports & Outdoors | Buck 55 Folding Hunter |
| 32392 | Sports & Outdoors | Bantam BBW |
| 32393 | Sports & Outdoors | Gerber 31-001088 Myth Pocket Folder, Fine Edge Folding Lock-Back Clip Knife |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=32390).
Recorded prediction: `{"Target Node": 32390, "Predicted Class": "Sports & Outdoors", "Confidence": 0.9943}`
Recorded graph stats: `{"total_1hop_degree": 1, "neighbor_label_ratio": {"Tools & Home Improvement": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | use | 0.6959 | 1 |
| 2 | use | 0.6853 | 1 |
| 3 | use | 0.6845 | 1 |
| 4 | dimens | 0.6841 | 1 |
| 5 | use | 0.6746 | 1 |
| 6 | use | 0.6716 | 1 |
| 7 | year | 0.6715 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
