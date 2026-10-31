# Reference packet: GraphXAIN__GPT-4o__products__1852

- Method: GraphXAIN; configuration: GPT-4o; dataset: products; target node: 1852
- Explanation source: `./robustness_2026-10-30/graphxain_gpt4o/products/1852.json` (narrative)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model predicted that the target product, Pendaflex Essentials File Folders, belongs to the "Health & Personal Care" category with a confidence of 41.95%. Surprisingly, the top bag-of-words features influencing this prediction, such as "use," "card," "help," "white," "power," "condit," and "pre," are all absent from the product description. This indicates that the prediction was not strongly supported by the textual features of the product itself. Instead, the prediction was significantly shaped by its direct co-purchase neighbors, most of which are related to office supplies, such as time cards, toner cartridges, and steno books. These products predominantly belong to the "Office Products" category, which would typically suggest a similar classification. Additionally, the pattern is reinforced by the 2-hop neighbors, which include calculators and paper clips, also in the office supply realm. The presence of electronic-related 2-hop neighbors did not align with the "Health & Personal Care" prediction, suggesting that the model may have overly relied on weak or indirect associations, potentially misinterpreting office products as related to health care due to co-purchase behaviors not immediately obvious from the data.
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

### Target Product (node 1852):
Product from Amazon platform with title and content: Title: Pendaflex Essentials File Folders, 1/3 Cut, Top Tab, Letter, Manila, 100 Per Box, (752 1/3). Content: None

### Model Prediction:
{
  "Target Node": 1852,
  "Predicted Class": "Health & Personal Care",
  "Confidence": 0.4195
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='use', importance=0.7666, present_in_product=0
  word='card', importance=0.7511, present_in_product=0
  word='help', importance=0.7501, present_in_product=0
  word='white', importance=0.7486, present_in_product=0
  word='power', importance=0.7484, present_in_product=0
  word='condit', importance=0.7471, present_in_product=0
  word='pre', importance=0.7439, present_in_product=0

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 9
Label distribution across all 1-hop neighbors (ground-truth category): Office Products=77.8%, Electronics=22.2%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 14327 | edge_importance=0.8404 | category=Office Products | TOPS Weekly Time Cards, Green Ink Front, 3
  Product 14323 | edge_importance=0.7729 | category=Office Products | V4INK&#65533; New Compatible HP 131A Toner Cartridge-Black (CF210A) for Hp Laserjet Pro M251 M276 Toner Printers
  Product 1907 | edge_importance=0.7698 | category=Office Products | NEW Compatible Nukote BR80C Calculator Ribbon Black/Red (2-pack) For Canon MP-11 DX
  Product 14326 | edge_importance=0.7654 | category=Office Products | TOPS Spiral Steno Books, 6 x 9 Inches, Gregg Rule, White Paper, Assorted Covers, 80 Sheets per Book, 4 Books per Pack (8
  Product 1820 | edge_importance=0.7568 | category=Office Products | &quot;Package of Two&quot; Texas Instruments TI-5142, 5150, 5630, 8230 and 8630 Ink Roller, Compatible, Black
  Product 14325 | edge_importance=0.7529 | category=Office Products | Quartet Prestige Colored Cork Bulletin Board, 3 x 2 Feet, Graphite Finish Frame (B243G)
  Product 14324 | edge_importance=0.7487 | category=Office Products | Alliance Sterling Ergonomically Correct Rubber Bands, #105, 0

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 1904 | edge_importance=0.8279 | category=Office Products | Compatible Universal Calculator Spool EPC B / R Black and Red Ribbons, Works for Casio DR 210 HD, Casio DR 210 HT, Casio
  Product 1859 | edge_importance=0.8232 | category=Office Products | Swingline Deluxe Staple Remover, Extra Wide, Steel Jaws, Black (S7038101)
  Product 29326 | edge_importance=0.8133 | category=Electronics | Endust Multi-Surface Electronics Anti-Static Cleaner - 12 Pack (096000P12)
  Product 14255 | edge_importance=0.8108 | category=Office Products | ACCO Economy Jumbo Paper Clips, Smooth, Jumbo, 100/Box, 10 Boxes (72580)
  Product 1878 | edge_importance=0.8043 | category=Office Products | Calculator Plain Paper
  Product 14001 | edge_importance=0.2747 | category=Electronics | SanDisk Cruzer Blade 4GB (10 pack) USB 2
  Product 1856 | edge_importance=0.2428 | category=Arts, Crafts & Sewing | Fiskars Recycled 8 Inch Strait Scissors (01-004253J)
  Product 1857 | edge_importance=0.2395 | category=Office Products | Canon LS-82Z Calculator
  Product 156 | edge_importance=0.236 | category=Office & School Supplies | 6 PK Calculator Ink Rollers, IR-40T / Canon CP13 / NU-KOTE NR42 / NR422 for Various Sharp, VICTOR, ADLER-ROYAL, CANON, C
  Product 1853 | edge_importance=0.2312 | category=Industrial & Scientific | SmartSign Adhesive Vinyl Label, Legend &quot;No Smoking&quot; with Graphic, 10&quot; high x 7&quot; wide, Black/Red on W
  Product 1854 | edge_importance=0.2266 | category=Office Products | Easy-See Electronic Digital Calculator - Large Tilt Display - Big Buttons
  Product 1860 | edge_importance=0.2235 | category=label 25 | missing

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

- ID: 1852
- Title: Pendaflex Essentials File Folders, 1/3 Cut, Top Tab, Letter, Manila, 100 Per Box, (752 1/3)
- True class (canonical `y`): **Office Products**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Health & Personal Care**
- Prediction recorded by this method's pipeline: **Health & Personal Care**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Pendaflex Essentials File Folders, 1/3 Cut, Top Tab, Letter, Manila, 100 Per Box, (752 1/3). Content: None
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 9 nodes

| node id | true class | title |
|---|---|---|
| 151 | Electronics | Jumbo 12-Digit Desktop Calculator |
| 1820 | Office Products | &quot;Package of Two&quot; Texas Instruments TI-5142, 5150, 5630, 8230 and 8630 Ink Roller, Compatible, Black |
| 1907 | Office Products | NEW Compatible Nukote BR80C Calculator Ribbon Black/Red (2-pack) For Canon MP-11 DX |
| 6192 | Electronics | Centon DSP4GB10PK&nbsp;10 x 4GB Multi-pack Pro USB Flash Drive (Grey) |
| 14323 | Office Products | V4INK&#65533; New Compatible HP 131A Toner Cartridge-Black (CF210A) for Hp Laserjet Pro M251 M276 Toner Printers |
| 14324 | Office Products | Alliance Sterling Ergonomically Correct Rubber Bands, #105, 0.625 x 5 Inches, 70 per 1lb Box (25055) |
| 14325 | Office Products | Quartet Prestige Colored Cork Bulletin Board, 3 x 2 Feet, Graphite Finish Frame (B243G) |
| 14326 | Office Products | TOPS Spiral Steno Books, 6 x 9 Inches, Gregg Rule, White Paper, Assorted Covers, 80 Sheets per Book, 4 Books per Pack (80220) |
| 14327 | Office Products | TOPS Weekly Time Cards, Green Ink Front, 3.5 x 9 Inches, 500-Count, Manila (1256) |

### 2-hop (shortest distance exactly 2): 24 nodes

| node id | true class | title |
|---|---|---|
| 1 | Office Products | Casio DR-270TM 2-Color Professional Desktop Printing Calculator |
| 147 | Office Products | Casio Inc. HR-100TM Business Calculator |
| 150 | Office Products | Canon P23-DH V 2 color mini-Desktop Printing Calculator |
| 156 | Office & School Supplies | 6 PK Calculator Ink Rollers, IR-40T / Canon CP13 / NU-KOTE NR42 / NR422 for Various Sharp, VICTOR, ADLER-ROYAL, CANON, CASIO, AURORA, CITIZEN, OLIVETTI, TEXAS INSTRUMENTS Calculators |
| 713 | Electronics | Case Logic VNA-216 16-Inch Laptop Attache (Black) |
| 1851 | Home & Kitchen | 2-Pack Neiko Patented Heavy-Duty All-Angle Super-Power Plunger |
| 1853 | Industrial & Scientific | SmartSign Adhesive Vinyl Label, Legend &quot;No Smoking&quot; with Graphic, 10&quot; high x 7&quot; wide, Black/Red on White |
| 1854 | Office Products | Easy-See Electronic Digital Calculator - Large Tilt Display - Big Buttons |
| 1855 | Office Products | Columbian CO128 (#10) 4-1/8x9-1/2-Inch Security Tinted White Envelopes, 500 Count |
| 1856 | Arts, Crafts & Sewing | Fiskars Recycled 8 Inch Strait Scissors (01-004253J) |
| 1857 | Office Products | Canon LS-82Z Calculator |
| 1858 | Health & Personal Care | Long Reach Comfort Wipe (1) |
| 1859 | Office Products | Swingline Deluxe Staple Remover, Extra Wide, Steel Jaws, Black (S7038101) |
| 1860 | label 25 | missing |
| 1878 | Office Products | Calculator Plain Paper |
| 1904 | Office Products | Compatible Universal Calculator Spool EPC B / R Black and Red Ribbons, Works for Casio DR 210 HD, Casio DR 210 HT, Casio DR 210 TM, Casio DR 220 |
| 14001 | Electronics | SanDisk Cruzer Blade 4GB (10 pack) USB 2.0 Flash Drive Jump Drive Thumb Drive SDCZ50-004G-10PK w/ (5) Everything But Stromboli (TM) Lanyard |
| 14185 | Office Products | HP 05A Black Original LaserJet Toner Cartridge |
| 14186 | Office Products | PM Company Perfection POS/Calculator Rolls, 2.25 Inches x 150 Feet, White, 12/Pack (08835) |
| 14255 | Office Products | ACCO Economy Jumbo Paper Clips, Smooth, Jumbo, 100/Box, 10 Boxes (72580) |
| 14550 | Office Products | NEW Compatible Nukote BR80C Calculator Ribbon Black/Red (6-pack) For Canon MP-11 DX |
| 14551 | Office Products | Columbian CO790 9x12-Inch Clasp Brown Kraft Envelopes, 100 Count |
| 29325 | Electronics | Logitech MK710 Wireless Desktop Mouse and Keyboard Combo |
| 29326 | Electronics | Endust Multi-Surface Electronics Anti-Static Cleaner - 12 Pack (096000P12) |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=1852).
Recorded prediction: `{"Target Node": 1852, "Predicted Class": "Health & Personal Care", "Confidence": 0.4195}`
Recorded graph stats: `{"total_1hop_degree": 9, "neighbor_label_ratio": {"Office Products": 0.778, "Electronics": 0.222}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | use | 0.7666 | 0 |
| 2 | card | 0.7511 | 0 |
| 3 | help | 0.7501 | 0 |
| 4 | white | 0.7486 | 0 |
| 5 | power | 0.7484 | 0 |
| 6 | condit | 0.7471 | 0 |
| 7 | pre | 0.7439 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
