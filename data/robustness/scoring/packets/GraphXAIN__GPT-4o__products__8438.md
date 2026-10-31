# Reference packet: GraphXAIN__GPT-4o__products__8438

- Method: GraphXAIN; configuration: GPT-4o; dataset: products; target node: 8438
- Explanation source: `./robustness_2026-10-30/graphxain_gpt4o/products/8438.json` (narrative)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The GNN model predicted that the product "Born Free 9 oz. BPA-Free High-Heat Resistant Classic Bottle with ActiveFlow Venting Technology, 3-Pack" belongs to the "Health & Personal Care" category with a confidence of 65.43%. Among the top words influencing this prediction, the word "use" is present in the product description and carries significant weight, suggesting a practical application associated with health and personal care products. Though other important words like "import", "inch", and "base" are absent, their high importance indicates that similar products in the dataset often contain these features, which might typically relate to product specifications and quality, indirectly aligning with personal care attributes. The direct co-purchase neighbors, such as the "Culturelle Kids! Chewables Probiotic" and the "Braun Thermoscan Ear Thermometer", both categorized under "Health & Personal Care", further solidify this classification by highlighting a tendency for co-purchased health-related items. Additionally, the neighboring "Baby" products like "Zo-Li Two Baby Wide Neck Baby Bottles" suggest a dual association with personal care for babies. The influence extends to 2-hop neighbors like "American Health Acidophilus with Bifidus Fruit", which are also health-focused, strengthening the link to the "Health & Personal Care" category. Overall, the interplay of product word features and the buying patterns associated with health-centric items collectively steer the model toward this confident prediction.
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

### Target Product (node 8438):
Product from Amazon platform with title and content: Title: Born Free 9 oz. BPA-Free High-Heat Resistant Classic Bottle with ActiveFlow Venting Technology, 3-Pack. Content: None

### Model Prediction:
{
  "Target Node": 8438,
  "Predicted Class": "Health & Personal Care",
  "Confidence": 0.6543
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='import', importance=0.771, present_in_product=0
  word='inch', importance=0.7545, present_in_product=0
  word='base', importance=0.7545, present_in_product=0
  word='cool', importance=0.7535, present_in_product=0
  word='accuraci', importance=0.7519, present_in_product=0
  word='use', importance=0.7516, present_in_product=1
  word='control', importance=0.7455, present_in_product=0

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 6
Label distribution across all 1-hop neighbors (ground-truth category): Baby=66.7%, Health & Personal Care=33.3%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 37122 | edge_importance=0.8363 | category=Baby | Zo-Li Two Baby Wide Neck Baby Bottles (10 Oz)
  Product 992 | edge_importance=0.8113 | category=Health & Personal Care | Culturelle Kids! Chewables Probiotic, for kids 50-100lbs, Tablets, 30 ea(Pack of 2)
  Product 37121 | edge_importance=0.7882 | category=Baby | Kidco F710 Baby Food Mill
  Product 37124 | edge_importance=0.7854 | category=Health & Personal Care | Braun Thermoscan Ear Thermometer-irt4520
  Product 37123 | edge_importance=0.7431 | category=Baby | Beaba Bib Expresso 3 in 1 Baby Bottle &amp; Food Warmer
  Product 37125 | edge_importance=0.7371 | category=Baby | Born Free Silicone Teether

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 991 | edge_importance=0.8248 | category=Health & Personal Care | American Health Acidophilus with Bifidus Fruit -- 100 Wafers
  Product 984 | edge_importance=0.8148 | category=Health & Personal Care | Power Probiotic ENT Kids - Strawberry Blast 30 Chewable Tablets | Supports the Natural Immune Defenses of the Ears, Nose
  Product 8434 | edge_importance=0.8054 | category=Beauty | BIOGAIA PROBIOTIC CHEWABLE TABLETS 60 TABS
  Product 8389 | edge_importance=0.7999 | category=Health & Personal Care | Amerifit Culturelle Probiotics for Kids, 30 Count
  Product 987 | edge_importance=0.77 | category=Health & Personal Care | ReNew Life - Buddy Bear Probiotic for Kids Orange - 60 Chewable Tablets
  Product 8436 | edge_importance=0.2145 | category=Baby | Medela Swing Breastpump
  Product 8435 | edge_importance=0.2104 | category=Baby | green sprouts Warming Plate, Sage
  Product 8437 | edge_importance=0.2018 | category=Health & Personal Care | Culturelle Probiotics for Kids 30 Ct (2 Pack)
  Product 75 | edge_importance=0.2017 | category=Health & Personal Care | KAL Dino-Dophilus Probiotic 2 Billion Chewables, Black Cherry, 60 Count
  Product 995 | edge_importance=0.1793 | category=Health & Personal Care | "Udo's Choice Children's Blend Probiotic 60 Capsules"
  Product 8433 | edge_importance=0.1715 | category=Health & Personal Care | Focus for Children Solaray 60 Chewable Tablet
  Product 8340 | edge_importance=0.1602 | category=Health & Personal Care | ReNew Life - Ultimate Flora Kids Probiotic - 30 Chewable Tablets

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

- ID: 8438
- Title: Born Free 9 oz. BPA-Free High-Heat Resistant Classic Bottle with ActiveFlow Venting Technology, 3-Pack
- True class (canonical `y`): **Baby**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Health & Personal Care**
- Prediction recorded by this method's pipeline: **Health & Personal Care**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Born Free 9 oz. BPA-Free High-Heat Resistant Classic Bottle with ActiveFlow Venting Technology, 3-Pack. Content: None
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 6 nodes

| node id | true class | title |
|---|---|---|
| 992 | Health & Personal Care | Culturelle Kids! Chewables Probiotic, for kids 50-100lbs, Tablets, 30 ea(Pack of 2) |
| 37121 | Baby | Kidco F710 Baby Food Mill |
| 37122 | Baby | Zo-Li Two Baby Wide Neck Baby Bottles (10 Oz) |
| 37123 | Baby | Beaba Bib Expresso 3 in 1 Baby Bottle &amp; Food Warmer |
| 37124 | Health & Personal Care | Braun Thermoscan Ear Thermometer-irt4520 |
| 37125 | Baby | Born Free Silicone Teether |

### 2-hop (shortest distance exactly 2): 12 nodes

| node id | true class | title |
|---|---|---|
| 75 | Health & Personal Care | KAL Dino-Dophilus Probiotic 2 Billion Chewables, Black Cherry, 60 Count |
| 984 | Health & Personal Care | Power Probiotic ENT Kids - Strawberry Blast 30 Chewable Tablets \| Supports the Natural Immune Defenses of the Ears, Nose/Nasopharynx, and Throat \| Promotes Oral Health and Fresh Breath \| Individually Sealed in Nitrogen-Purged Aluminum Blister Packs to Insure Freshness |
| 987 | Health & Personal Care | ReNew Life - Buddy Bear Probiotic for Kids Orange - 60 Chewable Tablets |
| 991 | Health & Personal Care | American Health Acidophilus with Bifidus Fruit -- 100 Wafers |
| 995 | Health & Personal Care | "Udo's Choice Children's Blend Probiotic 60 Capsules" |
| 8340 | Health & Personal Care | ReNew Life - Ultimate Flora Kids Probiotic - 30 Chewable Tablets |
| 8389 | Health & Personal Care | Amerifit Culturelle Probiotics for Kids, 30 Count |
| 8433 | Health & Personal Care | Focus for Children Solaray 60 Chewable Tablet |
| 8434 | Beauty | BIOGAIA PROBIOTIC CHEWABLE TABLETS 60 TABS |
| 8435 | Baby | green sprouts Warming Plate, Sage |
| 8436 | Baby | Medela Swing Breastpump |
| 8437 | Health & Personal Care | Culturelle Probiotics for Kids 30 Ct (2 Pack) |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=8438).
Recorded prediction: `{"Target Node": 8438, "Predicted Class": "Health & Personal Care", "Confidence": 0.6543}`
Recorded graph stats: `{"total_1hop_degree": 6, "neighbor_label_ratio": {"Baby": 0.667, "Health & Personal Care": 0.333}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | import | 0.771 | 0 |
| 2 | inch | 0.7545 | 0 |
| 3 | base | 0.7545 | 0 |
| 4 | cool | 0.7535 | 0 |
| 5 | accuraci | 0.7519 | 0 |
| 6 | use | 0.7516 | 1 |
| 7 | control | 0.7455 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
