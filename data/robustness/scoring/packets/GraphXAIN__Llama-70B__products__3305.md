# Reference packet: GraphXAIN__Llama-70B__products__3305

- Method: GraphXAIN; configuration: Llama-70B; dataset: products; target node: 3305
- Explanation source: `./robustness_2026-10-30/llama70b/graphxain/products/3305.json` (response)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The GNN model predicted that the Winco Bamboo Skewer, 6 inch belongs to the "Arts, Crafts & Sewing" category with a confidence of 27.48%. This prediction was largely driven by the presence of the word "use" in the product title, which is strongly associated with the craft category. Although other highly weighted words like "enough" and "purpl" were absent in the product description, their influence suggests that the model was drawn to words commonly used in arts and crafts supplies. Notably, many of the product's direct co-purchase neighbors, including Loew Cornell 1021254 Woodsies Craft Sticks and Surebonder DT-25 All Temperature Mini Glue Sticks, are also craft-related items, reinforcing this categorization. Furthermore, several second-degree co-purchase neighbors, such as BAZIC Natural Craft Sticks and Fiber Craft Jingle Bells, further solidify the connection to the craft community. These patterns suggest that the model was able to identify both linguistic cues and contextual associations indicative of an arts and crafts supply. As a result, it leaned toward the "Arts, Crafts & Sewing" category despite competing influences from health and personal care products among its co-purchase neighbors. Ultimately, the combination of linguistic analysis and network-based inference led the model to make this informed prediction.
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

### Target Product (node 3305):
Product from Amazon platform with title and content: Title: Winco Bamboo Skewer, 6 inch. Content: Bamboo Skewer, 100 per Bag, 6".

### Model Prediction:
{
  "Target Node": 3305,
  "Predicted Class": "Arts, Crafts & Sewing",
  "Confidence": 0.2748
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='use', importance=0.7712, present_in_product=1
  word='enough', importance=0.7603, present_in_product=0
  word='suppli', importance=0.7596, present_in_product=0
  word='use', importance=0.7594, present_in_product=1
  word='purpl', importance=0.7585, present_in_product=0
  word='color', importance=0.7513, present_in_product=0
  word='use', importance=0.7501, present_in_product=0

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 6
Label distribution across all 1-hop neighbors (ground-truth category): Arts, Crafts & Sewing=33.3%, Health & Personal Care=33.3%, Home & Kitchen=16.7%, Books=16.7%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 343 | edge_importance=0.8214 | category=Arts, Crafts & Sewing | Loew Cornell 1021254 Woodsies Craft Sticks, 1000-Piece
  Product 19313 | edge_importance=0.7954 | category=Health & Personal Care | Northwest Enterprises Hard Plastic 2-Ounce Shot Glasses, Clear, 50 Count
  Product 19312 | edge_importance=0.7918 | category=Arts, Crafts & Sewing | Surebonder DT-25 All Temperature Mini Glue Sticks, 4-Inch
  Product 19315 | edge_importance=0.7801 | category=Books | On a Stick!: 80 Party-Perfect Recipes
  Product 19314 | edge_importance=0.6973 | category=Health & Personal Care | Cindus Cellophane Wrap, 30-Inch Wide, 5-Feet Roll, Purple
  Product 19311 | edge_importance=0.3177 | category=Home & Kitchen | Wilton Mini Muffin Cups, 100 Count

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 3302 | edge_importance=0.8567 | category=Health & Personal Care | Graham Spa Essentials 3
  Product 1840 | edge_importance=0.8279 | category=Office Products | Duck Brand 1302209 Duck 3/4 Inch by 500 Inch Invisible Tape, 3-Pack
  Product 3301 | edge_importance=0.8137 | category=Arts, Crafts & Sewing | BAZIC Natural Craft Sticks, Wood, 100 Per Pack
  Product 3306 | edge_importance=0.8085 | category=Arts, Crafts & Sewing | Darice Victoria Lynn Chenille Stems 6mm 12&quot; 100/Pkg-White
  Product 17 | edge_importance=0.7858 | category=Arts, Crafts & Sewing | Fiber Craft 72-Pack Jingle Bells, 6mm-16mm, Gold
  Product 3307 | edge_importance=0.2221 | category=Books | Poptails: 60 Boozy Treats Served on a Stick
  Product 3308 | edge_importance=0.2171 | category=Office Products | Geographics Gold Foil Seals, Pack of 200 (44461)
  Product 3309 | edge_importance=0.2064 | category=Arts, Crafts & Sewing | Loew Cornell 1021201 Woodsies Alphabet Value Pack, 250 Piece
  Product 3304 | edge_importance=0.2017 | category=Arts, Crafts & Sewing | Sargent Art 22-1205 1-Gallon Washable School Glue
  Product 3249 | edge_importance=0.1715 | category=Arts, Crafts & Sewing | Darice 10843-99 350-Pack Chenille/Tinsel and Bump Chenille Stems, 12-Inch, Assorted
  Product 3303 | edge_importance=0.1647 | category=Arts, Crafts & Sewing | Blumenthal Lansing Company Favorite Findings 3-1/2-Ounce Big Bag of Buttons, Flowers

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

- ID: 3305
- Title: Winco Bamboo Skewer, 6 inch
- True class (canonical `y`): **Patio, Lawn & Garden**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Arts, Crafts & Sewing**
- Prediction recorded by this method's pipeline: **Arts, Crafts & Sewing**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Winco Bamboo Skewer, 6 inch. Content: Bamboo Skewer, 100 per Bag, 6".
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 6 nodes

| node id | true class | title |
|---|---|---|
| 343 | Arts, Crafts & Sewing | Loew Cornell 1021254 Woodsies Craft Sticks, 1000-Piece |
| 19311 | Home & Kitchen | Wilton Mini Muffin Cups, 100 Count |
| 19312 | Arts, Crafts & Sewing | Surebonder DT-25 All Temperature Mini Glue Sticks, 4-Inch |
| 19313 | Health & Personal Care | Northwest Enterprises Hard Plastic 2-Ounce Shot Glasses, Clear, 50 Count |
| 19314 | Health & Personal Care | Cindus Cellophane Wrap, 30-Inch Wide, 5-Feet Roll, Purple |
| 19315 | Books | On a Stick!: 80 Party-Perfect Recipes |

### 2-hop (shortest distance exactly 2): 11 nodes

| node id | true class | title |
|---|---|---|
| 17 | Arts, Crafts & Sewing | Fiber Craft 72-Pack Jingle Bells, 6mm-16mm, Gold |
| 1840 | Office Products | Duck Brand 1302209 Duck 3/4 Inch by 500 Inch Invisible Tape, 3-Pack |
| 3249 | Arts, Crafts & Sewing | Darice 10843-99 350-Pack Chenille/Tinsel and Bump Chenille Stems, 12-Inch, Assorted |
| 3301 | Arts, Crafts & Sewing | BAZIC Natural Craft Sticks, Wood, 100 Per Pack |
| 3302 | Health & Personal Care | Graham Spa Essentials 3.5 inch Make-up and Waxing Applicators 100pk |
| 3303 | Arts, Crafts & Sewing | Blumenthal Lansing Company Favorite Findings 3-1/2-Ounce Big Bag of Buttons, Flowers |
| 3304 | Arts, Crafts & Sewing | Sargent Art 22-1205 1-Gallon Washable School Glue |
| 3306 | Arts, Crafts & Sewing | Darice Victoria Lynn Chenille Stems 6mm 12&quot; 100/Pkg-White |
| 3307 | Books | Poptails: 60 Boozy Treats Served on a Stick |
| 3308 | Office Products | Geographics Gold Foil Seals, Pack of 200 (44461) |
| 3309 | Arts, Crafts & Sewing | Loew Cornell 1021201 Woodsies Alphabet Value Pack, 250 Piece |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=3305).
Recorded prediction: `{"Target Node": 3305, "Predicted Class": "Arts, Crafts & Sewing", "Confidence": 0.2748}`
Recorded graph stats: `{"total_1hop_degree": 6, "neighbor_label_ratio": {"Arts, Crafts & Sewing": 0.333, "Health & Personal Care": 0.333, "Home & Kitchen": 0.167, "Books": 0.167}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | use | 0.7712 | 1 |
| 2 | enough | 0.7603 | 0 |
| 3 | suppli | 0.7596 | 0 |
| 4 | use | 0.7594 | 1 |
| 5 | purpl | 0.7585 | 0 |
| 6 | color | 0.7513 | 0 |
| 7 | use | 0.7501 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
