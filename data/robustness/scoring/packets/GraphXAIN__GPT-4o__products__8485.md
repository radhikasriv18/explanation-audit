# Reference packet: GraphXAIN__GPT-4o__products__8485

- Method: GraphXAIN; configuration: GPT-4o; dataset: products; target node: 8485
- Explanation source: `./robustness_2026-10-30/graphxain_gpt4o/products/8485.json` (narrative)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The GNN model predicted that the product "Wright & McGill Magnetic Net Release" falls under the "Sports & Outdoors" category with a confidence of 67.86%. The top bag-of-words features identified as influential were notably absent from the product, which suggests that their absence helped steer the prediction towards "Sports & Outdoors" rather than diverting it. For instance, words like "fish" and "spring," which are relevant to fishing gear, were not present, potentially indicating that this particular type of product is more niche or specialized within the broader sports category. The most influential direct co-purchase neighbors, such as the "Greys GS Large Fly Box" and "RIO Powerflex Trout Leader," predominantly belonged to "Sports & Outdoors," highlighting a strong association with fishing-related products that further reinforced this classification. Additionally, the presence of a related "Sports & Outdoors" item like the "Scientific Anglers Fluorocarbon Tippet" among neighbors helped consolidate this prediction. The pattern is echoed by 2-hop neighbors like the "20/20 Magnetic Tippet Threader," underscoring an ecosystem of fishing accessories that supports the categorization. These connections suggest that the context provided by co-purchase patterns strongly points to "Sports & Outdoors" as the target product's natural category, aligning with a community of similar products frequently bought together.
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

### Target Product (node 8485):
Product from Amazon platform with title and content: Title: Wright &amp; McGill Magnetic Net Release. Content: W&M; WMEMNR Magnetic Net Release

### Model Prediction:
{
  "Target Node": 8485,
  "Predicted Class": "Sports & Outdoors",
  "Confidence": 0.6786
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='reduc', importance=0.7759, present_in_product=0
  word='without', importance=0.7758, present_in_product=0
  word='spring', importance=0.771, present_in_product=0
  word='fish', importance=0.7694, present_in_product=0
  word='stock', importance=0.7675, present_in_product=0
  word='year', importance=0.7585, present_in_product=0
  word='shoot', importance=0.7581, present_in_product=0

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 12
Label distribution across all 1-hop neighbors (ground-truth category): Sports & Outdoors=75.0%, Books=16.7%, Tools & Home Improvement=8.3%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 37293 | edge_importance=0.8093 | category=Sports & Outdoors | Greys GS Large Fly Box
  Product 37294 | edge_importance=0.8001 | category=Sports & Outdoors | RIO Powerflex Trout Leader
  Product 998 | edge_importance=0.7901 | category=Books | The Orvis Fly-Fishing Guide, Completely Revised and Updated with Over 400 New Color Photos and Illustrations
  Product 37291 | edge_importance=0.7872 | category=Sports & Outdoors | Fly Box + 100 Assorted Fly Fishing Fly Package
  Product 8548 | edge_importance=0.7679 | category=Sports & Outdoors | Scientific Anglers Fluorocarbon II Leader
  Product 37292 | edge_importance=0.7669 | category=Sports & Outdoors | Mojo Outdoors Wading Pole
  Product 37290 | edge_importance=0.7319 | category=Sports & Outdoors | Scientific Anglers Fluorocarbon Tippet with Cutter 30-meters

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 8575 | edge_importance=0.8422 | category=Sports & Outdoors | 20/20 Magnetic Tippet Threader
  Product 8492 | edge_importance=0.8268 | category=Sports & Outdoors | Loon Outdoors Aquel Floatant
  Product 8515 | edge_importance=0.8152 | category=Sports & Outdoors | Bill Dance Hook Remover
  Product 37247 | edge_importance=0.8144 | category=Books | Simple Fly Fishing: Techniques for Tenkara and Rod and Reel
  Product 8493 | edge_importance=0.8112 | category=Books | "Trout Streams of Wisconsin and Minnesota: An Angler's Guide to More Than 120 Rivers and Streams, Second Edition"
  Product 8579 | edge_importance=0.8075 | category=Sports & Outdoors | Magnetic Net Release
  Product 8491 | edge_importance=0.8042 | category=Sports & Outdoors | Loon Outdoors Top Ride Floatant and Desiccant
  Product 8479 | edge_importance=0.8035 | category=Books | "Colorado's Best Fly Fishing: Flies, Access, and Guide's Advice for the State's Premier Rivers (Headwater Guides)"
  Product 8576 | edge_importance=0.7983 | category=Sports & Outdoors | "Loon Outdoors Nip 'N Sip Fishing Nippers and Bottle Opener"
  Product 1006 | edge_importance=0.7953 | category=Sports & Outdoors | Hammers Collapsible Wading Staff Fishing Stick
  Product 37505 | edge_importance=0.7892 | category=Health & Personal Care | C&amp;F Design CFA-40 3-IN-1 Fly Fishing Tweezers New
  Product 8517 | edge_importance=0.7881 | category=Sports & Outdoors | "Caddis Men's Northern Guide Lightweight Taupe and Green Ecosmart Grip Sole Wading Shoe"

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

- ID: 8485
- Title: Wright &amp; McGill Magnetic Net Release
- True class (canonical `y`): **Sports & Outdoors**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Sports & Outdoors**
- Prediction recorded by this method's pipeline: **Sports & Outdoors**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Wright &amp; McGill Magnetic Net Release. Content: W&M; WMEMNR Magnetic Net Release
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 12 nodes

| node id | true class | title |
|---|---|---|
| 998 | Books | The Orvis Fly-Fishing Guide, Completely Revised and Updated with Over 400 New Color Photos and Illustrations |
| 1001 | Tools & Home Improvement | Rapala Fishing Forceps 7 1/2 Inch |
| 1008 | Sports & Outdoors | Eagle Claw W&amp;M Streamside Lanyard |
| 8490 | Sports & Outdoors | Rio Perception Fly Line Floating Accurate Angling Freshwater Fishing |
| 8548 | Sports & Outdoors | Scientific Anglers Fluorocarbon II Leader |
| 8555 | Books | "Trout Streams of Southern New England: An Angler's Guide to the Watersheds of Connecticut, Rhode Island, and Massachusetts (Trout Streams)" |
| 8588 | Sports & Outdoors | Hardy Stainless Twin Retractor |
| 37290 | Sports & Outdoors | Scientific Anglers Fluorocarbon Tippet with Cutter 30-meters |
| 37291 | Sports & Outdoors | Fly Box + 100 Assorted Fly Fishing Fly Package |
| 37292 | Sports & Outdoors | Mojo Outdoors Wading Pole |
| 37293 | Sports & Outdoors | Greys GS Large Fly Box |
| 37294 | Sports & Outdoors | RIO Powerflex Trout Leader |

### 2-hop (shortest distance exactly 2): 46 nodes

| node id | true class | title |
|---|---|---|
| 76 | Sports & Outdoors | Dr. Slick Standard Clamps |
| 996 | Sports & Outdoors | Crystal River Live Release Net |
| 1002 | Sports & Outdoors | Eagle Claw Forceps Hook Remover |
| 1005 | Sports & Outdoors | Berkley 6-Inch Softouch Hemostat Pliers |
| 1006 | Sports & Outdoors | Hammers Collapsible Wading Staff Fishing Stick |
| 1010 | Sports & Outdoors | Frogs Fanny Fly Treatment |
| 6080 | Sports & Outdoors | Nite Ize C9S-03-TP01 Small Figure 9 Carabiner with Rope, Black, Two-Pack |
| 8479 | Books | "Colorado's Best Fly Fishing: Flies, Access, and Guide's Advice for the State's Premier Rivers (Headwater Guides)" |
| 8484 | Sports & Outdoors | Glacier Glove Alaska River Fleece Fingerless Fishing Glove |
| 8486 | Books | "The Orvis Guide to Prospecting for Trout: How to Catch Fish When There's No Hatch to Match, Revised Edition" |
| 8487 | Sports & Outdoors | Loon Outdoors Hydrostop Dry Fly and Indicator Treatment |
| 8488 | Movies & TV | missing |
| 8489 | Sports & Outdoors | Orvis Tie-fast Knot-tying Tool |
| 8491 | Sports & Outdoors | Loon Outdoors Top Ride Floatant and Desiccant |
| 8492 | Sports & Outdoors | Loon Outdoors Aquel Floatant |
| 8493 | Books | "Trout Streams of Wisconsin and Minnesota: An Angler's Guide to More Than 120 Rivers and Streams, Second Edition" |
| 8514 | Sports & Outdoors | Rapala Fishing Clipper |
| 8515 | Sports & Outdoors | Bill Dance Hook Remover |
| 8516 | Sports & Outdoors | Berkley 8-Inch Precision Grip Pliers |
| 8517 | Sports & Outdoors | "Caddis Men's Northern Guide Lightweight Taupe and Green Ecosmart Grip Sole Wading Shoe" |
| 8518 | Sports & Outdoors | Dr. Slick Scissor Clamps |
| 8561 | Sports & Outdoors | New Zealand Strike Indicator Tool |
| 8568 | Sports & Outdoors | Tooltron 6-Inch Locking Clamp Curved Tip Fish Hook Remover |
| 8570 | Sports & Outdoors | Chums Fly Fishing Lanyard |
| 8571 | Sports & Outdoors | Allen Company Black River Fishing Chest Pack/Fanny Pack |
| 8572 | Sports & Outdoors | ECO Dr. Slick Retractable Reel ::: Zinger Pin on Reel - Package of Five (5) |
| 8573 | Sports & Outdoors | TyRite Hook Holder |
| 8574 | Sports & Outdoors | Anglers Accessories Lightweight Rubber Tippet/Floatant Holder |
| 8575 | Sports & Outdoors | 20/20 Magnetic Tippet Threader |
| 8576 | Sports & Outdoors | "Loon Outdoors Nip 'N Sip Fishing Nippers and Bottle Opener" |
| 8577 | Sports & Outdoors | Allen Company Fox River Fishing Chest Pack, Twin Double Compartment |
| 8578 | Sports & Outdoors | Standard Fly Tying Kit with wooden box |
| 8579 | Sports & Outdoors | Magnetic Net Release |
| 8593 | Sports & Outdoors | Allen Company Fly Rod Case (For Up To 9-Feet Four Piece Rod with Reel Attached) |
| 37219 | Sports & Outdoors | Okuma Crisium Graphite 2-Piece Fly Rod |
| 37247 | Books | Simple Fly Fishing: Techniques for Tenkara and Rod and Reel |
| 37251 | Sports & Outdoors | Flies Direct Adams Assortment Trout Fishing Flies (1-Dozen) |
| 37308 | Sports & Outdoors | Scientific Anglers Supra Floating Fly Fly Line |
| 37309 | Sports & Outdoors | Scientific Anglers Sharkskin Ultimate Trout Fly Line |
| 37388 | Sports & Outdoors | Plastic Waterproof Fly Box - White |
| 37505 | Health & Personal Care | C&amp;F Design CFA-40 3-IN-1 Fly Fishing Tweezers New |
| 37506 | Sports & Outdoors | Gone Fishing Freshwater Flies, Pack of 55 |
| 37525 | Books | Trout Streams of Northern New England: A Guide to the Best Fly-Fishing in Vermont, New Hampshire, and Maine, First Edition |
| 37526 | Books | "White Mountain Guide, 29th: AMC's Comprehensive Guide to Hiking Trails in the White Mountain National Forest (Appalachian Mountain Club White Mountain Guide)" |
| 37527 | Books | Maine Atlas &amp; Gazetteer |
| 37579 | Sports & Outdoors | Tie-Fast Knot Tyer #1 Nail&euro;&#157; Knot Tool- Black |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=8485).
Recorded prediction: `{"Target Node": 8485, "Predicted Class": "Sports & Outdoors", "Confidence": 0.6786}`
Recorded graph stats: `{"total_1hop_degree": 12, "neighbor_label_ratio": {"Sports & Outdoors": 0.75, "Books": 0.167, "Tools & Home Improvement": 0.083}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | reduc | 0.7759 | 0 |
| 2 | without | 0.7758 | 0 |
| 3 | spring | 0.771 | 0 |
| 4 | fish | 0.7694 | 0 |
| 5 | stock | 0.7675 | 0 |
| 6 | year | 0.7585 | 0 |
| 7 | shoot | 0.7581 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
