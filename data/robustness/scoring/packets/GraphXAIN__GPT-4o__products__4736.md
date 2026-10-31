# Reference packet: GraphXAIN__GPT-4o__products__4736

- Method: GraphXAIN; configuration: GPT-4o; dataset: products; target node: 4736
- Explanation source: `./robustness_2026-10-30/graphxain_gpt4o/products/4736.json` (narrative)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The GNN model predicted that the target product, Freud D0756N Diablo 7-1/4 56 Tooth TCG Non-Ferrous Metal and Plastic Cutting Saw Blade, belongs to the "Industrial & Scientific" category with a confidence of 33.16%. The model was influenced by several words in the product's description. Words such as "lasting" and "use," which were present, contributed significantly to the model's decision, emphasizing durability and functionality, typical attributes valued in industrial products. Conversely, despite their high importance scores, absent words like "well" and "need" did not directly sway the prediction. The direct co-purchase network further shaped this prediction, with significant influence from similar cutting tools such as the Freud LU94M010 Plexiglass and Plastic Cutting Saw Blade, labeled under "Tools & Home Improvement," indicating a strong connection between tools used in specialized industrial applications. Another important neighbor, IPS AAB4 Weld-On 1, directly associated with "Industrial & Scientific," solidified the category linkage, supporting the model's classification. While the majority of immediate neighbors were in "Tools & Home Improvement," the influence of similar tools in the 2-hop neighborhood suggested a substantial overlap with industrial applications, reinforcing the industrial categorization. This pattern suggests that despite the mixed neighbor categories, the emphasis on specialized, durable tools in co-purchase behavior aligned well with industrial and scientific uses, driving the prediction.
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

### Target Product (node 4736):
Product from Amazon platform with title and content: Title: Freud D0756N Diablo 7-1/4 56 Tooth TCG Non-Ferrous Metal and Plastic Cutting Saw Blade with 5/8-Inch Arbor, Diamond Knockout, and PermaShield Coating. Content: For a high-impact blade that makes clean cuts in plastics and non-ferrous metals

### Model Prediction:
{
  "Target Node": 4736,
  "Predicted Class": "Industrial & Scientific",
  "Confidence": 0.3316
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='well', importance=0.7539, present_in_product=0
  word='need', importance=0.7498, present_in_product=0
  word='lasting', importance=0.7443, present_in_product=1
  word='use', importance=0.7388, present_in_product=1
  word='brass', importance=0.7384, present_in_product=1
  word='formul', importance=0.7327, present_in_product=0
  word='use', importance=0.7311, present_in_product=1

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 6
Label distribution across all 1-hop neighbors (ground-truth category): Tools & Home Improvement=66.7%, Automotive=16.7%, Industrial & Scientific=16.7%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 24539 | edge_importance=0.8142 | category=Tools & Home Improvement | Freud LU94M010 10-Inch 80 Tooth MTCG Plexiglass and Plastic Cutting Saw Blade with 5/8-Inch Arbor
  Product 526 | edge_importance=0.8011 | category=Tools & Home Improvement | DEWALT D26960K Heavy Duty Heat Gun with LCD Display
  Product 24543 | edge_importance=0.7449 | category=Industrial & Scientific | IPS AAB4 Weld-On 1
  Product 24541 | edge_importance=0.7373 | category=Tools & Home Improvement | DEWALT DWE575SB 7-1/4-Inch Lightweight Circular Saw with Electric Brake
  Product 24542 | edge_importance=0.7203 | category=Automotive | "Extra-Large 72&quot; x 96&quot; Cargo Net with 28 Hooks - Stretches to 10' x 14'!"
  Product 24540 | edge_importance=0.7184 | category=Tools & Home Improvement | Freud D1084L 10-Inch Diameter 84t TCG Saw Blade with 5/8-Inch Arbor

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 4738 | edge_importance=0.8357 | category=Tools & Home Improvement | MICRO MESH 5&quot; - 8-HOLE 9 PC SANDING DISC ASSORTMENT PACK
  Product 4732 | edge_importance=0.8135 | category=Tools & Home Improvement | DEWALT DCB090 12V/20V Max USB Power Source
  Product 4731 | edge_importance=0.8127 | category=Automotive | CPS Products QC14SET Conversion Style Coupler Set R-12 to R-134A
  Product 4739 | edge_importance=0.8114 | category=Patio, Lawn & Garden | King Canopy HC1020PC 10-Feet by 20-Feet Hercules 8-Leg Canopy, White
  Product 4734 | edge_importance=0.2248 | category=Home & Kitchen | Bench Dog Tools 10-054 Cookie Cone
  Product 4737 | edge_importance=0.2208 | category=Tools & Home Improvement | DEWALT DCD740C1 20-Volt MAX Li-Ion Compact Right Angle 1
  Product 4733 | edge_importance=0.2194 | category=Automotive | ATD Tools 393 Heat Shrink Tube Assortment
  Product 4730 | edge_importance=0.2102 | category=Tools & Home Improvement | DEWALT DWS520K 6-1/2-Inch TrackSaw Kit
  Product 33 | edge_importance=0.1847 | category=Automotive | Bosch Bosch L-RACK Complete Kit with (1) i-boxx53, (2) LST72-OD, (3) L-RACK-S, and (1) L-RACK-T
  Product 4735 | edge_importance=0.1522 | category=Tools & Home Improvement | DEWALT DWHT62512 4 Piece Screwdriver Set

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

- ID: 4736
- Title: Freud D0756N Diablo 7-1/4 56 Tooth TCG Non-Ferrous Metal and Plastic Cutting Saw Blade with 5/8-Inch Arbor, Diamond Knockout, and PermaShield Coating
- True class (canonical `y`): **Tools & Home Improvement**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Industrial & Scientific**
- Prediction recorded by this method's pipeline: **Industrial & Scientific**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Freud D0756N Diablo 7-1/4 56 Tooth TCG Non-Ferrous Metal and Plastic Cutting Saw Blade with 5/8-Inch Arbor, Diamond Knockout, and PermaShield Coating. Content: For a high-impact blade that makes clean cuts in plastics and non-ferrous metals, look no further than the Freud D0756N Diablo 7.25-Inch Non-Ferrous Metal and Plastics Saw Blade. Thanks to its proprietary TCG (triple-chip grind) teeth, this is your go-to blade for slicing through plastic structures and non-ferrous metals such as copper pipes, aluminum extrusions, and brass plates.Model #D0756NDiameter7-1/4"Machine UseCircular SawApplicationNon-Ferrous Metals/PlasticsTeeth56 TCG(Triple-Chip Grind)Arbor5/8"(Diamond knockout arbor)Kerf.106"Hook Angle-6&deg;Makes Clean, Razor-Sharp Cuts in Plastic and Non-Ferrous MetalsAchieving premium results when working with plastics and non-ferrous metals is all about clean, accurate cuts. The Freud D0756N makes this process easy, fast, and precise. For making flawless crosscuts, this blade's proprietary TCG (triple-chip grind) teeth leave a clean, burr-free finish.Contractors, construction workers, and avid do-it-yourselfers will want to keep this blade on hand for jobs that call for slicing through plastic structures and non-ferrous metal pipes, extrusions, and plates. Appropriate application materials include copper, aluminum, brass, and plastic.Produces Smooth, Quiet Cuts with Laser-Cut KerfThe Freud D0756N's clean-cutting design means that you can enjoy the comfort of smooth performance. The thin 0.106-inch kerf between the blade's 56 TCG (triple-chip grind) teeth is laser cut to provide ease of feed, so you have more control over the blade's position. This helps maximize both the accuracy of the cut and the efficiency of your work, so you enjoy a job well done and the ability to complete more tasks in less time.An added bonus, the blade's laser-cut stabilizer vents reduce noise and vibration during operation, keeping your work environment more relaxed and your hands more in control. This feature also reduces friction and warping, helping to extend the blade's cutting life.Features Shock-Resistant Carbide for Long-Lasting PrecisionSo you can count on it over the long term, the Freud D0756N is designed for durability. The blade's hardy teeth are protected by Freud's exclusive shock-resistant TiCo Hi-Density Carbide formula, which helps fight wear and tear and maintains blade sharpness up to four times longer than standard carbide. And protecting the blade is Perma-Shield Non-Stick Coating that provides resistance to heat and corrosion.Fits Circular SawsThe Freud D0756N is a great addition to your workshop because it's designed with the versatility to fit a variety of circular saws.This product is covered by Freud's Limited Lifetime Warranty.What's in the BoxFreud D0756N Diablo 7.25-Inch Non-Ferrous Metal and Plastic Saw Blade.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 6 nodes

| node id | true class | title |
|---|---|---|
| 526 | Tools & Home Improvement | DEWALT D26960K Heavy Duty Heat Gun with LCD Display |
| 24539 | Tools & Home Improvement | Freud LU94M010 10-Inch 80 Tooth MTCG Plexiglass and Plastic Cutting Saw Blade with 5/8-Inch Arbor |
| 24540 | Tools & Home Improvement | Freud D1084L 10-Inch Diameter 84t TCG Saw Blade with 5/8-Inch Arbor |
| 24541 | Tools & Home Improvement | DEWALT DWE575SB 7-1/4-Inch Lightweight Circular Saw with Electric Brake |
| 24542 | Automotive | "Extra-Large 72&quot; x 96&quot; Cargo Net with 28 Hooks - Stretches to 10' x 14'!" |
| 24543 | Industrial & Scientific | IPS AAB4 Weld-On 1.25 oz Applicator Bottle with Needle |

### 2-hop (shortest distance exactly 2): 10 nodes

| node id | true class | title |
|---|---|---|
| 33 | Automotive | Bosch Bosch L-RACK Complete Kit with (1) i-boxx53, (2) LST72-OD, (3) L-RACK-S, and (1) L-RACK-T |
| 4730 | Tools & Home Improvement | DEWALT DWS520K 6-1/2-Inch TrackSaw Kit |
| 4731 | Automotive | CPS Products QC14SET Conversion Style Coupler Set R-12 to R-134A |
| 4732 | Tools & Home Improvement | DEWALT DCB090 12V/20V Max USB Power Source |
| 4733 | Automotive | ATD Tools 393 Heat Shrink Tube Assortment |
| 4734 | Home & Kitchen | Bench Dog Tools 10-054 Cookie Cone |
| 4735 | Tools & Home Improvement | DEWALT DWHT62512 4 Piece Screwdriver Set |
| 4737 | Tools & Home Improvement | DEWALT DCD740C1 20-Volt MAX Li-Ion Compact Right Angle 1.5 Ah Drill Kit |
| 4738 | Tools & Home Improvement | MICRO MESH 5&quot; - 8-HOLE 9 PC SANDING DISC ASSORTMENT PACK |
| 4739 | Patio, Lawn & Garden | King Canopy HC1020PC 10-Feet by 20-Feet Hercules 8-Leg Canopy, White |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=4736).
Recorded prediction: `{"Target Node": 4736, "Predicted Class": "Industrial & Scientific", "Confidence": 0.3316}`
Recorded graph stats: `{"total_1hop_degree": 6, "neighbor_label_ratio": {"Tools & Home Improvement": 0.667, "Automotive": 0.167, "Industrial & Scientific": 0.167}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | well | 0.7539 | 0 |
| 2 | need | 0.7498 | 0 |
| 3 | lasting | 0.7443 | 1 |
| 4 | use | 0.7388 | 1 |
| 5 | brass | 0.7384 | 1 |
| 6 | formul | 0.7327 | 0 |
| 7 | use | 0.7311 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
