# Reference packet: CF-GNNExplainer__Llama-70B__products__15065

- Method: CF-GNNExplainer; configuration: Llama-70B; dataset: products; target node: 15065
- Explanation source: `./robustness_2026-10-30/llama70b/cf/products/15065.json` (response)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, we can fill the dictionary as follows:

infos = {
    'Target_Node_ID': 15065,
    'Factual_Target_Node_Neighbors': [2082],
    'Factual_Target_Node_Features': ['adapt', 'adjust', 'one', 'also', 'use', 'anywher', 'arm', 'time', 'better', 'camera', 'carri', 'compact', 'conveni', 'degre', 'design', 'durabl', 'easi', 'experi', 'fast', 'featur', 'feel', 'fit', 'gopro', 'handl', 'hero', 'holder', 'length', 'lightweight', 'make', 'metal', 'mount', 'non', 'packag', 'photo', 'portabl', 'provid', 'quick', 'slip', 'taken', 'take', 'touch', 'univers', 'user', 'video', 'wonder', 'check'],
    'Counterfactual_Target_Node_Neighbors': [2082],
    'Counterfactual_Target_Node_Features': ['adapt', 'adjust', 'one', 'also', 'use', 'anywher', 'arm', 'time', 'better', 'camera', 'carri', 'compact', 'conveni', 'degre', 'design', 'durabl', 'easi', 'experi', 'fast', 'featur', 'feel', 'fit', 'gopro', 'handl', 'hero', 'holder', 'length', 'lightweight', 'make', 'metal', 'mount', 'non', 'packag', 'photo', 'portabl', 'provid', 'quick', 'slip', 'taken', 'take', 'touch', 'univers', 'user', 'video', 'wonder', 'check'],
    'Factual_Target_Node_Class': 'Sports & Outdoors',
    'Counterfactual_Target_Node_class': 'Electronics',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Node_Differences': [2109],
    'Edge_Differences': [(2109, 2082)],
    'Natural_Language_Explanation': 'The target node 15065, which represents the product "Camera Extender Handheld Telescopic Monopod +Tripod Mount Adapter for Gopro Hero 1/ 2/ 3 Camera Monopod", was initially classified as "Sports & Outdoors" but changed to "Electronics" in the counterfactual scenario. This change can be attributed to the fact that the node 2109, which was previously connected to node 2082, is now disconnected from it. Node 2109 represents the product "POV Dive Buoy Floating Camera Handle - GoPro Edition", which is more closely related to sports and outdoors activities. The disconnection of node 2109 from node 2082 may have caused the model to reclassify node 15065 as "Electronics", possibly due to the loss of contextual information provided by the connection to node 2109.'
}

Explanation:

The change in classification for the target node 15065 from "Sports & Outdoors" to "Electronics" can be attributed to the disconnection of node 2109 from node 2082. Node 2109 represents a product that is more closely related to sports and outdoors activities, and its connection to node 2082 may have provided contextual information that influenced the initial classification of node 15065 as "Sports & Outdoors". The loss of this connection may have caused the model to reclassify node 15065 as "Electronics", possibly due to the presence of other features or connections that are more indicative of electronics products.

It's worth noting that the features of the target node 15065 remain unchanged between the factual and counterfactual scenarios, suggesting that the change in classification is primarily driven by the changes in the graph structure rather than the node's attributes.
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
given the factual graph: The node 178 is a product titled 'Hitcase ChestR Mount' with key attributes: xbox, abl, adjust, one, use, attach, avoid, back, bag, board, built, captur, carri, comfort, durabl, easili, easi, enough, even, featur, fit, get, great, high, includ, let, lightweight, low, made, make, mount, text, pocket, possibl, put, quick, specif, super, system, much, versatil, want, waterproof, way and is connected with the node 2082 and it is classified as Sports & Outdoors, it is not the target node. The node 2069 is a product titled 'Jmt Sports Camera Handlebar Seatpost Rack Mount Compatible Gopro Hd Hero 2 3' with key attributes: use, arm, bag, black, box, brand, camera, color, compat, diamet, easi, featur, gopro, hero, high, includ, instal, light, materi, metal, mount, new, one, packag, pack, plastic, portabl, qualiti, remov, retail, safe, size, sport, suitabl, way, without and is connected with the node 2082 and it is classified as Sports & Outdoors, it is not the target node. The node 2082 is a product titled 'Adjustable Chest Mount Harness for Gopro Hd Hero 2 Hero 3 Camera - Black' with key attributes: action, activ, adjust, one, use, arm, well, black, camera, captur, design, digit, easi, film, fit, frame, friend, fulli, get, gopro, hero, includ, larg, let, lower, make, mount, year, perfect, photo, quick, recommend, releas, see, shape, share, size, sport, video, view, want, way, wear, live, provid, wrist and is connected with the nodes 178, 2069, 2109, 14980, 15063, 15064, 15065 and it is classified as Sports & Outdoors, it is not the target node. The node 2109 is a product titled 'POV Dive Buoy Floating Camera Handle - GoPro Edition' with key attributes: use, camera, comfort, direct, edit, gopro, grip, handl, head, lightweight, pocket, size, super, tight, water and is connected with the node 2082 and it is classified as Sports & Outdoors, it is not the target node. The node 14980 is a product titled 'VicTsing Suction Cup Mount for GoPro HD HERO HERO2 HERO3 Camera (Tripod Mount and Handle Screw)' with key attributes: one, use, book, time, bodi, camera, compat, cup, enough, featur, fit, gopro, handl, hero, hous, includ, line, mount, power, profession, screw, standard, stay, univers, vehicl, also, wide, window and is connected with the node 2082 and it is classified as Sports & Outdoors, it is not the target node. The node 15063 is a product titled 'WoCase&reg; Adjustable (Anti-Slippery) Head Strap Mount and Quick Clip Mount for GoPro HERO3+ 3 2 1 Cameras' with key attributes: accessori, adjust, one, use, anti, attach, better, camera, cap, captur, clip, compact, directli, even, fit, fulli, gopro, head, includ, like, low, manufactur, mount, also, origin, year, perspect, pictur, profil, purpos, qualiti, quick, reg, shown, size, strap, thick, ultra and is connected with the node 2082 and it is classified as Sports & Outdoors, it is not the target node. The node 15064 is a product titled 'WoCase&reg; Wrist Strap Mount for GoPro HD HERO3+ 3 2 1 Cameras (Compatible with Housing and Frame)' with key attributes: access, adapt, protect, use, book, camera, compat, easi, fit, flat, fli, frame, full, gear, gopro, hand, one, hous, includ, let, like, get, make, mount, origin, year, perfect, photo, plu, quickli, rang, reg, shoot, strap, video, watch, wear, wide, wrist, yet and is connected with the node 2082 and it is classified as Sports & Outdoors, it is not the target node. The node 15065 is a product titled 'Camera Extender Handheld Telescopic Monopod +Tripod Mount Adapter for Gopro Hero 1/ 2/ 3 Camera Monopod' with key attributes: adapt, adjust, one, also, use, anywher, arm, time, better, camera, carri, compact, conveni, degre, design, durabl, easi, experi, fast, featur, feel, fit, gopro, handl, hero, holder, length, lightweight, make, metal, mount, non, packag, photo, portabl, provid, quick, slip, taken, take, touch, univers, user, video, wonder, check and is connected with the node 2082 and it is classified as Sports & Outdoors, it is the target node. and given the counterfactual example: The node 178 is a product titled 'Hitcase ChestR Mount' with key attributes: xbox, abl, adjust, one, use, attach, avoid, back, bag, board, built, captur, carri, comfort, durabl, easili, easi, enough, even, featur, fit, get, great, high, includ, let, lightweight, low, made, make, mount, text, pocket, possibl, put, quick, specif, super, system, much, versatil, want, waterproof, way and is connected with the node 2082 and it is classified as Sports & Outdoors, it is not the target node. The node 2069 is a product titled 'Jmt Sports Camera Handlebar Seatpost Rack Mount Compatible Gopro Hd Hero 2 3' with key attributes: use, arm, bag, black, box, brand, camera, color, compat, diamet, easi, featur, gopro, hero, high, includ, instal, light, materi, metal, mount, new, one, packag, pack, plastic, portabl, qualiti, remov, retail, safe, size, sport, suitabl, way, without and is connected with the node 2082 and it is classified as Electronics, it is not the target node. The node 2082 is a product titled 'Adjustable Chest Mount Harness for Gopro Hd Hero 2 Hero 3 Camera - Black' with key attributes: action, activ, adjust, one, use, arm, well, black, camera, captur, design, digit, easi, film, fit, frame, friend, fulli, get, gopro, hero, includ, larg, let, lower, make, mount, year, perfect, photo, quick, recommend, releas, see, shape, share, size, sport, video, view, want, way, wear, live, provid, wrist and is connected with the nodes 178, 2069, 14980, 15063, 15064, 15065 and it is classified as Sports & Outdoors, it is not the target node. The node 2109 is a product titled 'POV Dive Buoy Floating Camera Handle - GoPro Edition' with key attributes: use, camera, comfort, direct, edit, gopro, grip, handl, head, lightweight, pocket, size, super, tight, water and is connected with no other nodes and it is classified as Sports & Outdoors, it is not the target node. The node 14980 is a product titled 'VicTsing Suction Cup Mount for GoPro HD HERO HERO2 HERO3 Camera (Tripod Mount and Handle Screw)' with key attributes: one, use, book, time, bodi, camera, compat, cup, enough, featur, fit, gopro, handl, hero, hous, includ, line, mount, power, profession, screw, standard, stay, univers, vehicl, also, wide, window and is connected with the node 2082 and it is classified as Electronics, it is not the target node. The node 15063 is a product titled 'WoCase&reg; Adjustable (Anti-Slippery) Head Strap Mount and Quick Clip Mount for GoPro HERO3+ 3 2 1 Cameras' with key attributes: accessori, adjust, one, use, anti, attach, better, camera, cap, captur, clip, compact, directli, even, fit, fulli, gopro, head, includ, like, low, manufactur, mount, also, origin, year, perspect, pictur, profil, purpos, qualiti, quick, reg, shown, size, strap, thick, ultra and is connected with the node 2082 and it is classified as Sports & Outdoors, it is not the target node. The node 15064 is a product titled 'WoCase&reg; Wrist Strap Mount for GoPro HD HERO3+ 3 2 1 Cameras (Compatible with Housing and Frame)' with key attributes: access, adapt, protect, use, book, camera, compat, easi, fit, flat, fli, frame, full, gear, gopro, hand, one, hous, includ, let, like, get, make, mount, origin, year, perfect, photo, plu, quickli, rang, reg, shoot, strap, video, watch, wear, wide, wrist, yet and is connected with the node 2082 and it is classified as Sports & Outdoors, it is not the target node. The node 15065 is a product titled 'Camera Extender Handheld Telescopic Monopod +Tripod Mount Adapter for Gopro Hero 1/ 2/ 3 Camera Monopod' with key attributes: adapt, adjust, one, also, use, anywher, arm, time, better, camera, carri, compact, conveni, degre, design, durabl, easi, experi, fast, featur, feel, fit, gopro, handl, hero, holder, length, lightweight, make, metal, mount, non, packag, photo, portabl, provid, quick, slip, taken, take, touch, univers, user, video, wonder, check and is connected with the node 2082 and it is classified as Electronics, it is the target node.
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

- ID: 15065
- Title: Camera Extender Handheld Telescopic Monopod +Tripod Mount Adapter for Gopro Hero 1/ 2/ 3 Camera Monopod
- True class (canonical `y`): **Electronics**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Sports & Outdoors**
- Prediction recorded by this method's pipeline: **Sports & Outdoors**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Camera Extender Handheld Telescopic Monopod +Tripod Mount Adapter for Gopro Hero 1/ 2/ 3 Camera Monopod. Content: This monopod is a universal camera holder, easy to carry, and fits all compact cameras. With it, you can photograph and video by yourself anywhere! Product Feature: -Durable metal shaft, lightweight, usable and easy to carry with -Fit most of compact cameras, connecting to the tripod mount of cameras -Considerate design of the quick spin knob for fast and convenient mounting -Non-slip handle for better using experience and wonderful touch feeling -180-degree rotation, providing convenience for the users while they are taking photos -Adjustable design not only makes it portable but also eliminates awkward photos taken at arms length Package Content: -1 x Monopod -1 x Tripod adapter
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 2082 | Sports & Outdoors | Adjustable Chest Mount Harness for Gopro Hd Hero 2 Hero 3 Camera - Black |

### 2-hop (shortest distance exactly 2): 6 nodes

| node id | true class | title |
|---|---|---|
| 178 | Cell Phones & Accessories | Hitcase ChestR Mount |
| 2069 | Sports & Outdoors | Jmt Sports Camera Handlebar Seatpost Rack Mount Compatible Gopro Hd Hero 2 3 |
| 2109 | Electronics | POV Dive Buoy Floating Camera Handle - GoPro Edition |
| 14980 | Cell Phones & Accessories | VicTsing Suction Cup Mount for GoPro HD HERO HERO2 HERO3 Camera (Tripod Mount and Handle Screw) |
| 15063 | Electronics | WoCase&reg; Adjustable (Anti-Slippery) Head Strap Mount and Quick Clip Mount for GoPro HERO3+ 3 2 1 Cameras |
| 15064 | Electronics | WoCase&reg; Wrist Strap Mount for GoPro HD HERO3+ 3 2 1 Cameras (Compatible with Housing and Frame) |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/products/cf-gnnexplainer-canonical/random_seed_42_*` (key=50).

- Factual class: **Sports & Outdoors**
- Counterfactual class: **Electronics**
- Removed edges (global ids, 1): (2082, 2109)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 15065 |
| Factual_Target_Node_Neighbors | 2082 |
| Factual_Target_Node_Features | adapt, adjust, one, also, use, use, anywher, use, arm, time, better, one, use, camera, use, carri, compact, use, conveni, conveni, degre, design, durabl, easi, experi, fast, featur, feel, fit, fit, use, use, gopro, handl, hero, holder, use, use, length, lightweight, make, metal, one, mount, mount, non, use, use, also, packag, photo, use, portabl, use, provid, quick, slip, taken, take, use, make, use, use, use, touch, univers, user, use, video, provid, use, wonder, use, check |
| Counterfactual_Target_Node_Neighbors | 2082 |
| Counterfactual_Target_Node_Features | adapt, adjust, one, also, use, use, anywher, use, arm, time, better, one, use, camera, use, carri, compact, use, conveni, conveni, degre, design, durabl, easi, experi, fast, featur, feel, fit, fit, use, use, gopro, handl, hero, holder, use, use, length, lightweight, make, metal, one, mount, mount, non, use, use, also, packag, photo, use, portabl, use, provid, quick, slip, taken, take, use, make, use, use, use, touch, univers, user, use, video, provid, use, wonder, use, check |
| Factual_Target_Node_Class | Sports & Outdoors |
| Counterfactual_Target_Node_class | Electronics |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 15065 |
| Factual_Target_Node_Neighbors | 2082 |
| Factual_Target_Node_Features | adapt, adjust, one, also, use, use, anywher, use, arm, time, better, one, use, camera, use, carri, compact, use, conveni, conveni, degre, design, durabl, easi, experi, fast, featur, feel, fit, fit, use, use, gopro, handl, hero, holder, use, use, length, lightweight, make, metal, one, mount, mount, non, use, use, also, packag, photo, use, portabl, use, provid, quick, slip, taken, take, use, make, use, use, use, touch, univers, user, use, video, provid, use, wonder, use, check |
| Counterfactual_Target_Node_Neighbors | 2082 |
| Counterfactual_Target_Node_Features | adapt, adjust, one, also, use, use, anywher, use, arm, time, better, one, use, camera, use, carri, compact, use, conveni, conveni, degre, design, durabl, easi, experi, fast, featur, feel, fit, fit, use, use, gopro, handl, hero, holder, use, use, length, lightweight, make, metal, one, mount, mount, non, use, use, also, packag, photo, use, portabl, use, provid, quick, slip, taken, take, use, make, use, use, use, touch, univers, user, use, video, provid, use, wonder, use, check |
| Factual_Target_Node_Class | Sports & Outdoors |
| Counterfactual_Target_Node_class | Electronics |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |
