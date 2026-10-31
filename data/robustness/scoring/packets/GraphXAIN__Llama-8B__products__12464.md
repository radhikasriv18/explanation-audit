# Reference packet: GraphXAIN__Llama-8B__products__12464

- Method: GraphXAIN; configuration: Llama-8B; dataset: products; target node: 12464
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/products/graphxain_products_llama_narratives_fulleval.json` ([12464])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model predicted the target product to belong to the "Sports & Outdoors" category with moderate confidence of 42.26%. Notably, despite the product's actual category being mentioned in its content ("brand new Arabic Shemagh..."), the absence of related words like "shemagh" or "Arabic" does not seem to have influenced the decision significantly. Instead, certain top BOW features strongly associated with outdoor activities, such as "head," "scarf," "sand," and "desert," appear to be driving the prediction, likely due to their presence in neighboring product titles. In fact, most of the top 1-hop co-purchase neighbors, such as "Proforce Shemagh Scarf Sand Solid" and "Ultimate Arms Gear Tactical Scarf - Shemagh - Kafiya - Keffiyeh Head Wrap," explicitly categorize under "Sports & Outdoors." These neighbors seem to push the prediction further in that direction. Furthermore, some distant connections, like the "Century&reg; hand forearm armor" at 2 hops away, continue to reinforce the idea of the product being part of an outdoor or protective gear category.
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

### Target Product (node 12464):
Product from Amazon platform with title and content: Title: missing. Content: brand new Arabic Shemagh Head/Neck Scarf. This is a great value shemagh. plain dull white (not a bright white) middle eastern head & neck scarf. All these scarves come with a dye scent, a simple hand wash with a soft deter

### Model Prediction:
{
  "Target Node": 12464,
  "Predicted Class": "Sports & Outdoors",
  "Confidence": 0.4226
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='known', importance=0.7656, present_in_product=0
  word='use', importance=0.7592, present_in_product=0
  word='side', importance=0.7554, present_in_product=0
  word='tactic', importance=0.7514, present_in_product=0
  word='wrap', importance=0.7504, present_in_product=0
  word='dimens', importance=0.7459, present_in_product=0
  word='one', importance=0.7407, present_in_product=0

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 8
Label distribution across all 1-hop neighbors (ground-truth category): label 25=62.5%, Sports & Outdoors=37.5%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 1510 | edge_importance=0.8393 | category=label 25 | missing
  Product 12449 | edge_importance=0.8009 | category=label 25 | missing
  Product 51061 | edge_importance=0.7981 | category=label 25 | missing
  Product 1509 | edge_importance=0.7516 | category=Sports & Outdoors | AUTHENTIC Black &amp; White Middle Eastern Arab Kafiya Keffiyeh with Aqel Rope
  Product 51062 | edge_importance=0.7373 | category=label 25 | missing
  Product 51060 | edge_importance=0.7281 | category=Sports & Outdoors | Proforce Shemagh Scarf Sand Solid
  Product 12467 | edge_importance=0.7248 | category=Sports & Outdoors | Authentic and NEW Head Shemagh Arab Kafiya Keffiyeh Kufiya with Agal Red &amp; White the Same Israel, Palestine and Brit

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 12472 | edge_importance=0.8275 | category=Sports & Outdoors | Century&reg; hand forearm armor
  Product 1507 | edge_importance=0.8158 | category=Arts, Crafts & Sewing | 40&quot;x40&quot;Grey Lightweight Shemagh Arab Tactical Desert Scarf Keffiyeh
  Product 12465 | edge_importance=0.8157 | category=label 25 | missing
  Product 51012 | edge_importance=0.8086 | category=label 25 | missing
  Product 12444 | edge_importance=0.8085 | category=Clothing, Shoes & Jewelry | Desert Military Tactial Keffiyeh Shemagh White &amp; Black
  Product 12460 | edge_importance=0.8025 | category=Sports & Outdoors | Ultimate Arms Gear Tactical Scarf - Shemagh - Kafiya - Keffiyeh Head Wrap : OD Olive Drab Green / Black 100% Cotton
  Product 12466 | edge_importance=0.7986 | category=All Beauty | White &amp; Black Shemagh Heavyweight Arab Tactical Desert Keffiyeh Scarf
  Product 1501 | edge_importance=0.7977 | category=Sports & Outdoors | KM Outfitters&reg; Pakistan Shemagh Keffiyeh - Choose Color!
  Product 51064 | edge_importance=0.7938 | category=Sports & Outdoors | KM Outfitters&reg; Pakistan Shemagh Keffiyeh - Choose Color!
  Product 12473 | edge_importance=0.7917 | category=Tools & Home Improvement | Damascus DNKPB Imperial Neoprene Knee Pads with Reinforced Non-slip Trion-X Caps, Black
  Product 50828 | edge_importance=0.7866 | category=Sports & Outdoors | KM Outfitters&reg; Pakistan Shemagh Keffiyeh - Choose Color!
  Product 51010 | edge_importance=0.7838 | category=Sports & Outdoors | Dark Blue Arab Shemagh Head/neck Scarf Authentic Quality Desert Wear Wrap Arafat Palestine

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

- ID: 12464
- Title: missing
- True class (canonical `y`): **label 25**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Sports & Outdoors**
- Prediction recorded by this method's pipeline: **Sports & Outdoors**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: missing. Content: brand new Arabic Shemagh Head/Neck Scarf. This is a great value shemagh. plain dull white (not a bright white) middle eastern head & neck scarf. All these scarves come with a dye scent, a simple hand wash with a soft detergent should take care of the scent. It measures 40" X 40" inches (103 X 103 cm). This Shemagh is made in India by Reliable. This type of Shemagh comes with Hadab on two sides at the ends of the scarf (tassel on the surrounding). This is brand new.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 8 nodes

| node id | true class | title |
|---|---|---|
| 1509 | Sports & Outdoors | AUTHENTIC Black &amp; White Middle Eastern Arab Kafiya Keffiyeh with Aqel Rope |
| 1510 | label 25 | missing |
| 12449 | label 25 | missing |
| 12463 | label 25 | missing |
| 12467 | Sports & Outdoors | Authentic and NEW Head Shemagh Arab Kafiya Keffiyeh Kufiya with Agal Red &amp; White the Same Israel, Palestine and British SAS Military USE Unique and Retro Look, Soft and Lightweight Great and Cool Unisex Accessory |
| 51060 | Sports & Outdoors | Proforce Shemagh Scarf Sand Solid |
| 51061 | label 25 | missing |
| 51062 | label 25 | missing |

### 2-hop (shortest distance exactly 2): 28 nodes

| node id | true class | title |
|---|---|---|
| 119 | Sports & Outdoors | Desert Sand/Yellow &amp; Black Shemagh Arab Keffiyeh Neck Scarf |
| 1501 | Sports & Outdoors | KM Outfitters&reg; Pakistan Shemagh Keffiyeh - Choose Color! |
| 1507 | Arts, Crafts & Sewing | 40&quot;x40&quot;Grey Lightweight Shemagh Arab Tactical Desert Scarf Keffiyeh |
| 10233 | Tools & Home Improvement | Damascus DNKPB Imperial Neoprene Knee Pads with Reinforced Non-slip Trion-X Caps, Black |
| 12444 | Clothing, Shoes & Jewelry | Desert Military Tactial Keffiyeh Shemagh White &amp; Black |
| 12450 | Sports & Outdoors | Condor Tactical Cap - BLACK |
| 12460 | Sports & Outdoors | Ultimate Arms Gear Tactical Scarf - Shemagh - Kafiya - Keffiyeh Head Wrap : OD Olive Drab Green / Black 100% Cotton |
| 12461 | label 25 | missing |
| 12462 | label 25 | missing |
| 12465 | label 25 | missing |
| 12466 | All Beauty | White &amp; Black Shemagh Heavyweight Arab Tactical Desert Keffiyeh Scarf |
| 12468 | Tools & Home Improvement | Mechanix Wear MP3-05-010 Mpact3 Knuckle Protection Glove, Black, Large |
| 12469 | label 25 | missing |
| 12470 | label 25 | missing |
| 12471 | Beauty | Change 1PC Unisex Fashion Women Men Arab Shemagh Keffiyeh Palestine Scarf Shawl Wrap (Purple) |
| 12472 | Sports & Outdoors | Century&reg; hand forearm armor |
| 12473 | Tools & Home Improvement | Damascus DNKPB Imperial Neoprene Knee Pads with Reinforced Non-slip Trion-X Caps, Black |
| 12474 | label 25 | missing |
| 12475 | Sports & Outdoors | Matrix Iron Face Carbon Steel &quot;Striker&quot; Metal Mesh Lower Half Mask (Black) |
| 12476 | Beauty | Change 1PC Unisex Fashion Women Men Arab Shemagh Keffiyeh Palestine Scarf Shawl Wrap (Red) |
| 50828 | Sports & Outdoors | KM Outfitters&reg; Pakistan Shemagh Keffiyeh - Choose Color! |
| 51010 | Sports & Outdoors | Dark Blue Arab Shemagh Head/neck Scarf Authentic Quality Desert Wear Wrap Arafat Palestine |
| 51011 | label 25 | missing |
| 51012 | label 25 | missing |
| 51050 | label 25 | missing |
| 51053 | label 25 | missing |
| 51059 | label 25 | missing |
| 51064 | Sports & Outdoors | KM Outfitters&reg; Pakistan Shemagh Keffiyeh - Choose Color! |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=12464).
Recorded prediction: `{"Target Node": 12464, "Predicted Class": "Sports & Outdoors", "Confidence": 0.4226}`
Recorded graph stats: `{"total_1hop_degree": 8, "neighbor_label_ratio": {"label 25": 0.625, "Sports & Outdoors": 0.375}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | known | 0.7656 | 0 |
| 2 | use | 0.7592 | 0 |
| 3 | side | 0.7554 | 0 |
| 4 | tactic | 0.7514 | 0 |
| 5 | wrap | 0.7504 | 0 |
| 6 | dimens | 0.7459 | 0 |
| 7 | one | 0.7407 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
