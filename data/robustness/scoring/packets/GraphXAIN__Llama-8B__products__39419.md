# Reference packet: GraphXAIN__Llama-8B__products__39419

- Method: GraphXAIN; configuration: Llama-8B; dataset: products; target node: 39419
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/products/graphxain_products_llama_narratives_fulleval.json` ([39419])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Given the title and description of the product 'Badger Basket Doll Bunk Beds With Ladder - Pink/White,' our model confidently predicted it belongs to the category 'Toys & Games' with a probability of about 56%. Key factors driving this prediction include the presence of significant Bag Of Words (BOW) features such as 'use' and 'includes', which are highly indicative of toys that encourage imaginative play. Notably, though related terms like 'accessori' are absent, their close association suggests they may have played a role in reinforcing this categorization. Furthermore, the model considered the strongly associated direct co-purchase neighbor, which is the 'American Girl Starry 2 Doll Tote Bag', indicating the model connects the product with another closely related toy item commonly purchased together. This connection significantly supports its inclusion within the 'Toys & Games' category. Although some distant co-purchase neighbors from different categories like 'Movies & TV' exist, they seem to be less influential. In summary, our model effectively identifies the product's category as 'Toys & Games', given its reliance on prominent BOW characteristics and notable co-purchase patterns among similar toys.
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

### Target Product (node 39419):
Product from Amazon platform with title and content: Title: Badger Basket Doll Bunk Beds With Ladder - Pink/White. Content: Just right when doll friends come to visit. Our Doll Bunk Beds are built for two dolls to rest in style. Includes a ladder for extra fun and realism. Pretty pink gingham comple

### Model Prediction:
{
  "Target Node": 39419,
  "Predicted Class": "Toys & Games",
  "Confidence": 0.5584
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='use', importance=0.7002, present_in_product=1
  word='bag', importance=0.6901, present_in_product=0
  word='includes', importance=0.6887, present_in_product=1
  word='accessori', importance=0.6882, present_in_product=0
  word='use', importance=0.6863, present_in_product=1
  word='take', importance=0.686, present_in_product=0
  word='girl', importance=0.6835, present_in_product=0

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 1
Label distribution across all 1-hop neighbors (ground-truth category): Toys & Games=100.0%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 9135 | edge_importance=0.8013 | category=Toys & Games | American Girl Starry 2 Doll Tote Bag

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 1089 | edge_importance=0.8436 | category=Toys & Games | 18 Inch Doll Backpack, Doll Size for 18&quot; Doll Accessories and American Girl Dolls in Purple Nylon, Zippered Opening
  Product 39417 | edge_importance=0.7775 | category=Movies & TV | missing
  Product 39346 | edge_importance=0.6999 | category=Toys & Games | 3 PC
  Product 39418 | edge_importance=0.666 | category=Toys & Games | Doll Bicycle Seat - &quot;Ride Along Dolly&quot; Bike Seat with Decorate Yourself Decals (Fits 18&quot; American Girl an
  Product 39420 | edge_importance=0.134 | category=Toys & Games | Red and Yellow Roses Dress &amp; Sandals ~ Fits 18&quot; American Girl Dolls

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

- ID: 39419
- Title: Badger Basket Doll Bunk Beds With Ladder - Pink/White
- True class (canonical `y`): **Toys & Games**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Toys & Games**
- Prediction recorded by this method's pipeline: **Toys & Games**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Badger Basket Doll Bunk Beds With Ladder - Pink/White. Content: Just right when doll friends come to visit. Our Doll Bunk Beds are built for two dolls to rest in style. Includes a ladder for extra fun and realism. Pretty pink gingham complements the attractive white finish. For Dolls up to 20" . Overall size of 11.5" x 22.25" x 15" . There is 6.75" clearance between the top and bottom bunks and 3.5" distance between the bottom bunk and the floor. Includes two removable mattresses (21.25" x 10" ) with attached pillows and eyelet trim. Pillow area of the mattress is approximately 3.5" x 10" . Ladder measures approximately 15" x 5" x 3/8" D. Can be enjoyed by children from three years old and up. All paints and finishes are non-toxic. Some adult assembly required. Illustrated instructions included. Made with wood and wood composites. Fabric parts are poly/cotton and stuffed with polyfill. Wipe wood parts clean with a damp cloth and mild detergent as needed. For longevity of the product, spot cleaning or hand washing recommended for the fabric parts (but you can machine wash gentle and air dry if desired). This item is a toy for use with dolls only. It is never to be used with real infants or pets. This item ships in its original carton which may include a photo of the product.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 9135 | Toys & Games | American Girl Starry 2 Doll Tote Bag |

### 2-hop (shortest distance exactly 2): 5 nodes

| node id | true class | title |
|---|---|---|
| 1089 | Toys & Games | 18 Inch Doll Backpack, Doll Size for 18&quot; Doll Accessories and American Girl Dolls in Purple Nylon, Zippered Opening and Pocket in Purple |
| 39346 | Toys & Games | 3 PC. Gymnastics Leotard, Jacket, and Bag, Doll Gymnastics Outfit Fits 18&quot; Dolls Like American Girl |
| 39417 | Movies & TV | missing |
| 39418 | Toys & Games | Doll Bicycle Seat - &quot;Ride Along Dolly&quot; Bike Seat with Decorate Yourself Decals (Fits 18&quot; American Girl and Standard Sized Dolls and Stuffed Animals) |
| 39420 | Toys & Games | Red and Yellow Roses Dress &amp; Sandals ~ Fits 18&quot; American Girl Dolls |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=39419).
Recorded prediction: `{"Target Node": 39419, "Predicted Class": "Toys & Games", "Confidence": 0.5584}`
Recorded graph stats: `{"total_1hop_degree": 1, "neighbor_label_ratio": {"Toys & Games": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | use | 0.7002 | 1 |
| 2 | bag | 0.6901 | 0 |
| 3 | includes | 0.6887 | 1 |
| 4 | accessori | 0.6882 | 0 |
| 5 | use | 0.6863 | 1 |
| 6 | take | 0.686 | 0 |
| 7 | girl | 0.6835 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
