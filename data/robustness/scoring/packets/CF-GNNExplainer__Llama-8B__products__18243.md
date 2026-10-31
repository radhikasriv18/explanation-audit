# Reference packet: CF-GNNExplainer__Llama-8B__products__18243

- Method: CF-GNNExplainer; configuration: Llama-8B; dataset: products; target node: 18243
- Explanation source: `./llm-graph-cf/data/results/cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_products_standard_Response.json` ([61][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, we can fill the dictionary as follows:

infos = {
    'Target_Node_ID': 18243,
    'Factual_Target_Node_Neighbors': [2996],
    'Factual_Target_Node_Features': ['use', 'black', 'cartridg', 'color', 'combo', 'ink', 'pack'],
    'Counterfactual_Target_Node_Neighbors': [2996],
    'Counterfactual_Target_Node_Features': ['use', 'black', 'cartridg', 'color', 'combo', 'ink', 'pack'],
    'Factual_Target_Node_Class': 'Arts, Crafts & Sewing',
    'Counterfactual_Target_Node_class': 'Health & Personal Care',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': ['Arts, Crafts & Sewing' -> 'Health & Personal Care'],
    'Natural_Language_Explanation': 'The target node 18243, which is a Canon PG-210XL /CL-211XL Color Ink Cartridge Combo Pack-Black, was initially classified as Arts, Crafts & Sewing. However, after analyzing the graph structure and node features, we found that if the target node were connected to the node 2996, which is a GP Spectrum Multi-Use Paper, 8.5 x 11 Inches, 3-Ream Pack (1500 Sheets), it would be classified as Health & Personal Care. This change in classification is influenced by the presence of the node 2996, which has a strong connection to the target node and shares similar features such as "use" and "black".'
}

The change in classification for the target node 18243 from Arts, Crafts & Sewing to Health & Personal Care is primarily driven by the influence of the node 2996, which is a product in the Health & Personal Care category. The target node shares several features with node 2996, including "use" and "black", which suggests a strong connection between the two nodes. This connection is further reinforced by the fact that node 2996 is a co-purchased product with the target node, indicating a high likelihood of being classified under the same category.

The influence of the neighbors on the target node can be seen in the following:

* Node 2996 has a strong connection to the target node and shares similar features, which contributes to the change in classification.
* The other neighbors of the target node, such as 301, 309, 312, 2908, 2909, 2951, 2957, 3081, 4758, 7847, 18244, 18245, and 18247, do not have a significant impact on the classification change, as they belong to different categories and do not share similar features with the target node.

Overall, the analysis suggests that the change in classification for the target node 18243 is primarily driven by the influence of the node 2996, which is a product in the Health & Personal Care category and shares several features with the target node.
~~~~~~

## 2. Prompt the method's model received

Chat messages (system + user) built by llm-graph-cf's prompt code; identical for every CF configuration.

**system:**

~~~~~~text
You are a language model that generates responses in a coherent and well-structured discourse style. Avoid using bullet points, lists, or numerical outlines. Provide your responses in complete sentences and paragraphs, explaining concepts clearly and concisely in a continuous flow.You must take a factual example , a graph, and its counterfactual example, another graph, generated via adjacency matrix perturbation and you must explain the differences.Counterfactual Explanation: A counterfactual explanation refers to a type of explanation in machine learning and artificial intelligence that describes how altering certain input features can change the output of a model. It answers 'what if' scenarios by identifying minimal changes necessary to achieve a different desired outcome. Counterfactual explanations provide insights into the decision-making process of complex models, enhancing transparency and interpretability.For example, consider a credit scoring model that denies a loan application. A counterfactual explanation might be: 'If your annual income had been $50,000 instead of $45,000, your loan would have been approved.' This helps the applicant understand what specific change could lead to a different decision.Counterfactual Explanations in Graphs: Graphs are data structures consisting of nodes (vertices) and edges that represent relationships between entities. Graphs are prevalent in various domains such as social networks, biological networks, and knowledge graphs. When machine learning models, particularly Graph Neural Networks (GNNs), are applied to graph data, interpreting their predictions becomes challenging due to the complexity of the graph structure.Counterfactual explanations in graphs aim to provide insights into how changes in the graph's structure or node features can alter the model's predictions. This involves identifying minimal modifications to the graph that would change the outcome for a specific node or the entire graph.You MUST fill this dictionary taking into account that Node_Differences must contain JUST the nodes' id where the change happen, the Edge_Differences must contain a list of tuple representing the nodes involved in the edges:  infos={Target_Node_ID:'', Factual_Target_Node_Neighbors: [], Factual_Target_Node_Features: [], Counterfactual_Target_Node_Neighbors: [],
    Counterfactual_Target_Node_Features: [], Factual_Target_Node_Class: '', Counterfactual_Target_Node_class: '', Target_Node_Features_Changed_From_Factual_To_Counterfactual: [], Natural_Language_Explanation: ''}
~~~~~~

**user:**

~~~~~~text
given the factual graph: The node 301 is a product titled 'Inktoneram Remanufactured Ink Cartridges High CapacityReplacement for 127 (2xBlack, Cyan, Magenta, Yellow, 5-Pack)' with key attributes: use, black, capac, extra, high, ink, pack, total, yellow and is connected with the node 2996 and it is classified as Health & Personal Care, it is not the target node. The node 309 is a product titled 'Epson DURABrite T126120 Ultra 126 High-capacity Inkjet Cartridge-Black' with key attributes: use, black, capac, cartridg, high, ink, ultra and is connected with the node 2996 and it is classified as Health & Personal Care, it is not the target node. The node 312 is a product titled 'Inktoneram Remanufactured Ink Cartridges High Capacity Replacement for 126 (4x Black, 2x Cyan, 2x Magenta, 2x Yellow, 10' with key attributes: inch, use, black, capac, high, ink, pack, replac, set, total, yellow and is connected with the nodes 2996, 3081 and it is classified as Health & Personal Care, it is not the target node. The node 2908 is a product titled 'GE Lighting 24705 65-Watt 470/360-Lumen R30 Commercial Indoor Reflector Floodlight Bulb, Soft White, 6-Pack' with key attributes: xbox, dimens, one, use, applic, base, bulb, commerci, inch, indoor, light, medium, need, origin, pack, replac, screw, soft, spot, track, type, watt, white, wide, without and is connected with the node 2996 and it is classified as Tools & Home Improvement, it is not the target node. The node 2909 is a product titled 'Philips 406009 Landscape and Indoor Flood 50-Watt MR16 12-Volt Light Bulb, 6-pack' with key attributes: inch, per, one, use, applic, well, bright, bulb, display, gener, ideal, indoor, light, also, outdoor, pack, perfect, provid, read, make, track, varieti, watt, white and is connected with the node 2996 and it is classified as Industrial & Scientific, it is not the target node. The node 2951 is a product titled '(Pack of 10) 40-Watt G16.5 Decorative Globe E12 Candelabra Base Light Bulbs' with key attributes: inch, temperatur, use, base, clear, crystal, light, pack, watt and is connected with the nodes 2957, 2996 and it is classified as Health & Personal Care, it is not the target node. The node 2957 is a product titled 'GE Lighting 75368 Energy Smart 13-Watt Spiral Compact Fluorescent Bulb, Candelabra Base, 2-Pack' with key attributes: inch, dimens, year, capsul, use, base, believ, bulb, case, color, compact, cost, earth, energi, excel, extra, fan, get, high, includ, last, life, light, long, longer, mani, one, offer, output, pack, percent, perform, posit, provid, qualiti, rang, rare, replac, smart, may, standard, technolog, time, make, watt, also, award and is connected with the nodes 2951, 2996 and it is classified as Tools & Home Improvement, it is not the target node. The node 2996 is a product titled 'GP Spectrum Multi-Use Paper, 8.5 x 11 Inches, 3-Ream Pack (1500 Sheets) (998606)' with key attributes: inch, one, use, around, well, black, bright, choic, day, design, devic, equip, everyday, function, graphic, great, high, ideal, includ, laser, multi, pack, sheet, perform, qualiti, reliabl, solid, standard, text, varieti, volum, white, wide and is connected with the nodes 301, 309, 312, 2908, 2909, 2951, 2957, 3081, 4758, 7847, 18243, 18244, 18245, 18246, 18247 and it is classified as Health & Personal Care, it is not the target node. The node 3081 is a product titled 'Inktoneram Remanufactured Ink Cartridges Replacement for Epson 125 (2xBlack, Cyan, Magenta, Yellow , 5-Pack)' with key attributes: use, time, best, black, certifi, choic, clariti, compat, cost, deliv, design, detail, effect, ensur, get, great, high, ink, oem, origin, qualiti, pack, perform, price, provid, replac, set, stylu, test, thoroughli, make, work, yellow and is connected with the nodes 312, 2996 and it is classified as Health & Personal Care, it is not the target node. The node 4758 is a product titled 'Bosch DDB180-02 18-Volt Lithium-Ion 3/8-Inch Cordless Drill/Driver Kit with 2 Batteries, Charger and Case' with key attributes: inch, use, batteri, case, charger, ion, kit, none and is connected with the node 2996 and it is classified as Health & Personal Care, it is not the target node. The node 7847 is a product titled 'Flipside Science Fair Titles: Black' with key attributes: dimens, use, applic, time, avail, black, blue, coat, color, contain, data, one, green, high, home, includ, introduct, materi, packag, print, problem, project, purpos, qualiti, red, result, school, scienc, separ, sold, usborn, varieti, white, work and is connected with the node 2996 and it is classified as Office Products, it is not the target node. The node 18243 is a product titled 'Canon PG-210XL /CL-211XL Color Ink Cartridge Combo Pack-Black' with key attributes: use, black, cartridg, color, combo, ink, pack and is connected with the node 2996 and it is classified as Health & Personal Care, it is the target node. The node 18244 is a product titled '"Kimberly-Clark Kleenex 50606 Hard Roll Towel, 600' Length x 8&quot; Width, 1-3/4&quot; Core Diameter, White (Case of 6)' with key attributes: use, case, core, diamet, hard, length, none, quot, roll, white, width and is connected with the node 2996 and it is classified as Health & Personal Care, it is not the target node. The node 18245 is a product titled 'School Smart Trifold Presentation Board - 36 x 48 - Header Not Included' with key attributes: hour, handbookandth, pux, one, use, art, well, embroid, board, card, carri, dimens, easi, front, great, ideal, imag, inch, includ, item, lightweight, make, natur, offic, also, open, textbook, project, school, scienc, show, singl, smart, smooth, sold, surfac, type, unit, white and is connected with the node 2996 and it is classified as Office Products, it is not the target node. The node 18246 is a product titled '2 Pack Remanufactured HP 950 XL 950XL Black Ink Cartridges for HP OfficeJet Pro 276dw MFP, OfficeJet Pro 8600 e-All-In-O' with key attributes: one, use, black, compat, copi, follow, free, want, includ, ink, pack, plu, premium, pro, replac, ship, warranti, year and is connected with the node 2996 and it is classified as Health & Personal Care, it is not the target node. The node 18247 is a product titled 'Business Envelope, 4 1/8 x 9 1/2, 20 lb, White, 50/Box' with key attributes: year, per, use, box, busi, size, white and is connected with the node 2996 and it is classified as Health & Personal Care, it is not the target node. and given the counterfactual example: The node 301 is a product titled 'Inktoneram Remanufactured Ink Cartridges High CapacityReplacement for 127 (2xBlack, Cyan, Magenta, Yellow, 5-Pack)' with key attributes: use, black, capac, extra, high, ink, pack, total, yellow and is connected with the node 2996 and it is classified as Health & Personal Care, it is not the target node. The node 309 is a product titled 'Epson DURABrite T126120 Ultra 126 High-capacity Inkjet Cartridge-Black' with key attributes: use, black, capac, cartridg, high, ink, ultra and is connected with the node 2996 and it is classified as Health & Personal Care, it is not the target node. The node 312 is a product titled 'Inktoneram Remanufactured Ink Cartridges High Capacity Replacement for 126 (4x Black, 2x Cyan, 2x Magenta, 2x Yellow, 10' with key attributes: inch, use, black, capac, high, ink, pack, replac, set, total, yellow and is connected with the nodes 2996, 3081 and it is classified as Health & Personal Care, it is not the target node. The node 2908 is a product titled 'GE Lighting 24705 65-Watt 470/360-Lumen R30 Commercial Indoor Reflector Floodlight Bulb, Soft White, 6-Pack' with key attributes: xbox, dimens, one, use, applic, base, bulb, commerci, inch, indoor, light, medium, need, origin, pack, replac, screw, soft, spot, track, type, watt, white, wide, without and is connected with the node 2996 and it is classified as Tools & Home Improvement, it is not the target node. The node 2909 is a product titled 'Philips 406009 Landscape and Indoor Flood 50-Watt MR16 12-Volt Light Bulb, 6-pack' with key attributes: inch, per, one, use, applic, well, bright, bulb, display, gener, ideal, indoor, light, also, outdoor, pack, perfect, provid, read, make, track, varieti, watt, white and is connected with the node 2996 and it is classified as Tools & Home Improvement, it is not the target node. The node 2951 is a product titled '(Pack of 10) 40-Watt G16.5 Decorative Globe E12 Candelabra Base Light Bulbs' with key attributes: inch, temperatur, use, base, clear, crystal, light, pack, watt and is connected with the nodes 2957, 2996 and it is classified as Health & Personal Care, it is not the target node. The node 2957 is a product titled 'GE Lighting 75368 Energy Smart 13-Watt Spiral Compact Fluorescent Bulb, Candelabra Base, 2-Pack' with key attributes: inch, dimens, year, capsul, use, base, believ, bulb, case, color, compact, cost, earth, energi, excel, extra, fan, get, high, includ, last, life, light, long, longer, mani, one, offer, output, pack, percent, perform, posit, provid, qualiti, rang, rare, replac, smart, may, standard, technolog, time, make, watt, also, award and is connected with the nodes 2951, 2996 and it is classified as Tools & Home Improvement, it is not the target node. The node 2996 is a product titled 'GP Spectrum Multi-Use Paper, 8.5 x 11 Inches, 3-Ream Pack (1500 Sheets) (998606)' with key attributes: inch, one, use, around, well, black, bright, choic, day, design, devic, equip, everyday, function, graphic, great, high, ideal, includ, laser, multi, pack, sheet, perform, qualiti, reliabl, solid, standard, text, varieti, volum, white, wide and is connected with the nodes 301, 309, 312, 2908, 2909, 2951, 2957, 3081, 4758, 7847, 18244, 18245, 18246, 18247 and it is classified as Health & Personal Care, it is not the target node. The node 3081 is a product titled 'Inktoneram Remanufactured Ink Cartridges Replacement for Epson 125 (2xBlack, Cyan, Magenta, Yellow , 5-Pack)' with key attributes: use, time, best, black, certifi, choic, clariti, compat, cost, deliv, design, detail, effect, ensur, get, great, high, ink, oem, origin, qualiti, pack, perform, price, provid, replac, set, stylu, test, thoroughli, make, work, yellow and is connected with the nodes 312, 2996 and it is classified as Health & Personal Care, it is not the target node. The node 4758 is a product titled 'Bosch DDB180-02 18-Volt Lithium-Ion 3/8-Inch Cordless Drill/Driver Kit with 2 Batteries, Charger and Case' with key attributes: inch, use, batteri, case, charger, ion, kit, none and is connected with the node 2996 and it is classified as Health & Personal Care, it is not the target node. The node 7847 is a product titled 'Flipside Science Fair Titles: Black' with key attributes: dimens, use, applic, time, avail, black, blue, coat, color, contain, data, one, green, high, home, includ, introduct, materi, packag, print, problem, project, purpos, qualiti, red, result, school, scienc, separ, sold, usborn, varieti, white, work and is connected with the node 2996 and it is classified as Office Products, it is not the target node. The node 18243 is a product titled 'Canon PG-210XL /CL-211XL Color Ink Cartridge Combo Pack-Black' with key attributes: use, black, cartridg, color, combo, ink, pack and is connected with no other nodes and it is classified as Arts, Crafts & Sewing, it is the target node. The node 18244 is a product titled '"Kimberly-Clark Kleenex 50606 Hard Roll Towel, 600' Length x 8&quot; Width, 1-3/4&quot; Core Diameter, White (Case of 6)' with key attributes: use, case, core, diamet, hard, length, none, quot, roll, white, width and is connected with the node 2996 and it is classified as Health & Personal Care, it is not the target node. The node 18245 is a product titled 'School Smart Trifold Presentation Board - 36 x 48 - Header Not Included' with key attributes: hour, handbookandth, pux, one, use, art, well, embroid, board, card, carri, dimens, easi, front, great, ideal, imag, inch, includ, item, lightweight, make, natur, offic, also, open, textbook, project, school, scienc, show, singl, smart, smooth, sold, surfac, type, unit, white and is connected with the node 2996 and it is classified as Office Products, it is not the target node. The node 18246 is a product titled '2 Pack Remanufactured HP 950 XL 950XL Black Ink Cartridges for HP OfficeJet Pro 276dw MFP, OfficeJet Pro 8600 e-All-In-O' with key attributes: one, use, black, compat, copi, follow, free, want, includ, ink, pack, plu, premium, pro, replac, ship, warranti, year and is connected with the node 2996 and it is classified as Health & Personal Care, it is not the target node. The node 18247 is a product titled 'Business Envelope, 4 1/8 x 9 1/2, 20 lb, White, 50/Box' with key attributes: year, per, use, box, busi, size, white and is connected with the node 2996 and it is classified as Health & Personal Care, it is not the target node.
                    and given the knowledge base about the dataset: 
The Amazon Products dataset (ogbn-products) is a large-scale co-purchase graph of Amazon products. It is commonly used for node classification benchmarks in graph learning research.
Features:
Each node represents an Amazon product and is described by a 2,000-dimensional bag-of-words feature vector derived from the product's title and description text. A value of 1 at a given dimension indicates the presence of the corresponding word in the product text.
Graph Structure:
Edges connect products that are frequently co-purchased together on Amazon (i.e., customers who bought one product also bought the other). The graph is undirected.
Nodes: 54,025 products.
Edges: Co-purchase links between products.
Classes:
Products are categorized into one of 47 Amazon top-level product categories, including:
Home & Kitchen, Health & Personal Care, Beauty, Sports & Outdoors, Books, Patio Lawn & Garden, Toys & Games, CDs & Vinyl, Cell Phones & Accessories, Grocery & Gourmet Food, Arts Crafts & Sewing, Clothing Shoes & Jewelry, Electronics, Movies & TV, Software, Video Games, Automotive, Pet Supplies, Office Products, Industrial & Scientific, Musical Instruments, Tools & Home Improvement, Baby Products, and others.
, fill the dictionary!
                    and provide an explanation about the change in classification for the target node, please evaluate also the influences of neighbors nodes.
~~~~~~

## 3. Target node

- ID: 18243
- Title: Canon PG-210XL /CL-211XL Color Ink Cartridge Combo Pack-Black
- True class (canonical `y`): **Office Products**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Health & Personal Care**
- Prediction recorded by this method's pipeline: **Health & Personal Care**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Canon PG-210XL /CL-211XL Color Ink Cartridge Combo Pack-Black. Content: Canon PG-210XL /CL-211XL Color Ink Cartridge Combo Pack-Black
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 2996 | Office Products | GP Spectrum Multi-Use Paper, 8.5 x 11 Inches, 3-Ream Pack (1500 Sheets) (998606) |

### 2-hop (shortest distance exactly 2): 14 nodes

| node id | true class | title |
|---|---|---|
| 301 | Office Products | Inktoneram Remanufactured Ink Cartridges High CapacityReplacement for 127 (2xBlack, Cyan, Magenta, Yellow, 5-Pack) |
| 309 | Office Products | Epson DURABrite T126120 Ultra 126 High-capacity Inkjet Cartridge-Black |
| 312 | Office Products | Inktoneram Remanufactured Ink Cartridges High Capacity Replacement for 126 (4x Black, 2x Cyan, 2x Magenta, 2x Yellow, 10-Pack) |
| 2908 | Tools & Home Improvement | GE Lighting 24705 65-Watt 470/360-Lumen R30 Commercial Indoor Reflector Floodlight Bulb, Soft White, 6-Pack |
| 2909 | Tools & Home Improvement | Philips 406009 Landscape and Indoor Flood 50-Watt MR16 12-Volt Light Bulb, 6-pack |
| 2951 | Tools & Home Improvement | (Pack of 10) 40-Watt G16.5 Decorative Globe E12 Candelabra Base Light Bulbs |
| 2957 | Tools & Home Improvement | GE Lighting 75368 Energy Smart 13-Watt Spiral Compact Fluorescent Bulb, Candelabra Base, 2-Pack |
| 3081 | Office Products | Inktoneram Remanufactured Ink Cartridges Replacement for Epson 125 (2xBlack, Cyan, Magenta, Yellow , 5-Pack) |
| 4758 | Tools & Home Improvement | Bosch DDB180-02 18-Volt Lithium-Ion 3/8-Inch Cordless Drill/Driver Kit with 2 Batteries, Charger and Case |
| 7847 | Toys & Games | Flipside Science Fair Titles: Black |
| 18244 | Industrial & Scientific | "Kimberly-Clark Kleenex 50606 Hard Roll Towel, 600' Length x 8&quot; Width, 1-3/4&quot; Core Diameter, White (Case of 6)" |
| 18245 | Office Products | School Smart Trifold Presentation Board - 36 x 48 - Header Not Included |
| 18246 | Office Products | 2 Pack Remanufactured HP 950 XL 950XL Black Ink Cartridges for HP OfficeJet Pro 276dw MFP, OfficeJet Pro 8600 e-All-In-One - N911g, OfficeJet Pro 8600 Plus - N911n, OfficeJet Pro 8600 Premium - N911a OfficeJet Pro 251dw, OfficeJet Pro 8100 ePrinter - N811a &copy; YoYoInk |
| 18247 | Office Products | Business Envelope, 4 1/8 x 9 1/2, 20 lb, White, 50/Box |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/products/cf-gnnexplainer-canonical/random_seed_42_*` (key=61).

- Factual class: **Health & Personal Care**
- Counterfactual class: **Arts, Crafts & Sewing**
- Removed edges (global ids, 1): (2996, 18243)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 18243 |
| Factual_Target_Node_Neighbors | 2996 |
| Factual_Target_Node_Features | use, use, black, cartridg, color, combo, use, use, ink, pack, use, use, use, use |
| Counterfactual_Target_Node_Neighbors |  |
| Counterfactual_Target_Node_Features | use, use, black, cartridg, color, combo, use, use, ink, pack, use, use, use, use |
| Factual_Target_Node_Class | Health & Personal Care |
| Counterfactual_Target_Node_class | Arts, Crafts & Sewing |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 2996 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 18243 |
| Factual_Target_Node_Neighbors | 2996 |
| Factual_Target_Node_Features | use, use, black, cartridg, color, combo, use, use, ink, pack, use, use, use, use |
| Counterfactual_Target_Node_Neighbors |  |
| Counterfactual_Target_Node_Features | use, use, black, cartridg, color, combo, use, use, ink, pack, use, use, use, use |
| Factual_Target_Node_Class | Health & Personal Care |
| Counterfactual_Target_Node_class | Arts, Crafts & Sewing |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 2996 |
| Natural_Language_Explanation | None |
