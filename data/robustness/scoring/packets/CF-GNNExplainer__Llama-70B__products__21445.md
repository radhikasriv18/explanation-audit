# Reference packet: CF-GNNExplainer__Llama-70B__products__21445

- Method: CF-GNNExplainer; configuration: Llama-70B; dataset: products; target node: 21445
- Explanation source: `./robustness_2026-10-30/llama70b/cf/products/21445.json` (response)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, we can fill the dictionary as follows:

infos = {
    'Target_Node_ID': 21445,
    'Factual_Target_Node_Neighbors': [3893],
    'Factual_Target_Node_Features': ['inch', 'deflockedst', 'one', 'use', 'assembl', 'hardwar', 'hold', 'includ', 'indoor', 'long', 'made', 'also', 'recommend', 'requir', 'rifl', 'seven', 'solid', 'sport', 'make', 'usa'],
    'Counterfactual_Target_Node_Neighbors': [],
    'Counterfactual_Target_Node_Features': ['inch', 'deflockedst', 'one', 'use', 'assembl', 'hardwar', 'hold', 'includ', 'indoor', 'long', 'made', 'also', 'recommend', 'requir', 'rifl', 'seven', 'solid', 'sport', 'make', 'usa'],
    'Factual_Target_Node_Class': 'Sports & Outdoors',
    'Counterfactual_Target_Node_class': 'Industrial & Scientific',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Node_Differences': [21445],
    'Edge_Differences': [(21445, 3893)],
    'Natural_Language_Explanation': 'The product "Evans Sports Standing Rifle Rack" was initially classified as Sports & Outdoors, but after removing its connection with node 3893, which is a book about the Mosin-Nagant rifle, it got reclassified as Industrial & Scientific. This change suggests that the connection with the book was influencing the product's classification towards Sports & Outdoors, possibly due to the book's content being related to rifles and sports. Without this connection, the product's features, such as being a standing rifle rack, became more prominent, leading to its reclassification as Industrial & Scientific.'
}

Explanation:
The target node, "Evans Sports Standing Rifle Rack", was initially classified as Sports & Outdoors, likely due to its connection with node 3893, which is a book about the Mosin-Nagant rifle. This connection may have influenced the product's classification towards Sports & Outdoors, as the book's content is related to rifles and sports.

However, when the connection between the two nodes was removed, the product's features, such as being a standing rifle rack, became more prominent, leading to its reclassification as Industrial & Scientific. This change suggests that the connection with the book was a significant factor in the product's initial classification, and that the product's inherent features are more closely related to the Industrial & Scientific category.

The influence of neighboring nodes can be seen in this case, as the removal of the connection with node 3893 had a significant impact on the product's classification. This highlights the importance of considering the graph structure and node connections when analyzing and interpreting the results of node classification models.
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
given the factual graph: The node 422 is a product titled 'missing' with key attributes: inch, book, almost, use, brown, classic, complet, exampl, item, leather, length, loop, made, militari, miss, new, part, qualiti, rifl, run, seri, standard, stori, first, web, width, year and is connected with the node 3893 and it is classified as Sports & Outdoors, it is not the target node. The node 3827 is a product titled 'Set of 40 BRAND NEW Stripper Clips For Mosin Nagant 1891/30 91/30 M38 M39 M44 7.62X54r Rifles' with key attributes: day, temperatur, use, brand, new, set and is connected with the node 3893 and it is classified as Sports & Outdoors, it is not the target node. The node 3846 is a product titled 'Mauser Stripper Clips 40CT 6.5x55mm 38,94,96 &amp; 30-06, 1903, 1917' with key attributes: day, temperatur, stereo, use, amp, year, box, one, includ, mani, reticl, new, order, receiv, make, work and is connected with the node 3893 and it is classified as Sports & Outdoors, it is not the target node. The node 3893 is a product titled 'The Mosin-Nagant Rifle, 6th Edition (For collectors only)' with key attributes: book, aid, also, use, around, author, stori, one, chang, depth, descript, develop, difficult, war, edit, english, ever, extrem, find, first, futur, year, histori, includ, inform, late, life, list, long, made, meet, model, part, textbook, collagen, provid, publish, rifl, set, standard, state, top, unit, live, make, world and is connected with the nodes 422, 3827, 3846, 21214, 21233, 21443, 21444, 21445 and it is classified as Books, it is not the target node. The node 21214 is a product titled 'The Lee-Enfield Rifle (Weapon)' with key attributes: inch, book, also, use, american, time, author, bed, colleg, com, editor, front, would, year, highli, histor, histori, includ, line, live, london, mani, militari, modern, number, old, text, part, press, rifl, run, see, seri, sinc, small, sound, studi, technolog, top, univers, war, first, west, wife, world, www and is connected with the node 3893 and it is classified as Books, it is not the target node. The node 21233 is a product titled 'ProMag Archangel Opfor AA9130 Forend Rail, Black' with key attributes: accessori, use, book, well, black, color, end, made, precis, rail, rifl, time, stock and is connected with the node 3893 and it is classified as Sports & Outdoors, it is not the target node. The node 21443 is a product titled 'Mosin Nagant 91/30 &quot;Range Buddy&quot; Front Sight Adjustment Tool' with key attributes: day, abl, accuraci, one, use, design, difficult, fine, front, get, great, book, instal, job, know, militari, optim, precis, quot, rang, remov, rifl, sight, specif, stop, today, tool, well, make and is connected with the node 3893 and it is classified as Sports & Outdoors, it is not the target node. The node 21444 is a product titled 'Pachmayr Decelerator Slip On Recoil Pad' with key attributes: inch, one, use, appear, auto, bag, control, custom, design, dimens, take, easi, english, enhanc, experi, factori, featur, feel, field, fit, follow, game, ground, gun, hard, help, improv, instal, larg, long, look, model, make, year, pad, pre, provid, requir, shoot, size, slip, stock, ultim, wide, within, reader, chapter, check and is connected with the node 3893 and it is classified as Sports & Outdoors, it is not the target node. The node 21445 is a product titled 'Evans Sports Standing Rifle Rack' with key attributes: inch, deflockedst, one, use, assembl, hardwar, hold, includ, indoor, long, made, also, recommend, requir, rifl, seven, solid, sport, make, usa and is connected with the node 3893 and it is classified as Sports & Outdoors, it is the target node. and given the counterfactual example: The node 422 is a product titled 'missing' with key attributes: inch, book, almost, use, brown, classic, complet, exampl, item, leather, length, loop, made, militari, miss, new, part, qualiti, rifl, run, seri, standard, stori, first, web, width, year and is connected with the node 3893 and it is classified as Sports & Outdoors, it is not the target node. The node 3827 is a product titled 'Set of 40 BRAND NEW Stripper Clips For Mosin Nagant 1891/30 91/30 M38 M39 M44 7.62X54r Rifles' with key attributes: day, temperatur, use, brand, new, set and is connected with the node 3893 and it is classified as Sports & Outdoors, it is not the target node. The node 3846 is a product titled 'Mauser Stripper Clips 40CT 6.5x55mm 38,94,96 &amp; 30-06, 1903, 1917' with key attributes: day, temperatur, stereo, use, amp, year, box, one, includ, mani, reticl, new, order, receiv, make, work and is connected with the node 3893 and it is classified as Sports & Outdoors, it is not the target node. The node 3893 is a product titled 'The Mosin-Nagant Rifle, 6th Edition (For collectors only)' with key attributes: book, aid, also, use, around, author, stori, one, chang, depth, descript, develop, difficult, war, edit, english, ever, extrem, find, first, futur, year, histori, includ, inform, late, life, list, long, made, meet, model, part, textbook, collagen, provid, publish, rifl, set, standard, state, top, unit, live, make, world and is connected with the nodes 422, 3827, 3846, 21214, 21233, 21443, 21444 and it is classified as Books, it is not the target node. The node 21214 is a product titled 'The Lee-Enfield Rifle (Weapon)' with key attributes: inch, book, also, use, american, time, author, bed, colleg, com, editor, front, would, year, highli, histor, histori, includ, line, live, london, mani, militari, modern, number, old, text, part, press, rifl, run, see, seri, sinc, small, sound, studi, technolog, top, univers, war, first, west, wife, world, www and is connected with the node 3893 and it is classified as Books, it is not the target node. The node 21233 is a product titled 'ProMag Archangel Opfor AA9130 Forend Rail, Black' with key attributes: accessori, use, book, well, black, color, end, made, precis, rail, rifl, time, stock and is connected with the node 3893 and it is classified as Sports & Outdoors, it is not the target node. The node 21443 is a product titled 'Mosin Nagant 91/30 &quot;Range Buddy&quot; Front Sight Adjustment Tool' with key attributes: day, abl, accuraci, one, use, design, difficult, fine, front, get, great, book, instal, job, know, militari, optim, precis, quot, rang, remov, rifl, sight, specif, stop, today, tool, well, make and is connected with the node 3893 and it is classified as Sports & Outdoors, it is not the target node. The node 21444 is a product titled 'Pachmayr Decelerator Slip On Recoil Pad' with key attributes: inch, one, use, appear, auto, bag, control, custom, design, dimens, take, easi, english, enhanc, experi, factori, featur, feel, field, fit, follow, game, ground, gun, hard, help, improv, instal, larg, long, look, model, make, year, pad, pre, provid, requir, shoot, size, slip, stock, ultim, wide, within, reader, chapter, check and is connected with the node 3893 and it is classified as Sports & Outdoors, it is not the target node. The node 21445 is a product titled 'Evans Sports Standing Rifle Rack' with key attributes: inch, deflockedst, one, use, assembl, hardwar, hold, includ, indoor, long, made, also, recommend, requir, rifl, seven, solid, sport, make, usa and is connected with no other nodes and it is classified as Industrial & Scientific, it is the target node.
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

- ID: 21445
- Title: Evans Sports Standing Rifle Rack
- True class (canonical `y`): **Sports & Outdoors**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Sports & Outdoors**
- Prediction recorded by this method's pipeline: **Sports & Outdoors**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Evans Sports Standing Rifle Rack. Content: The Evans Standing Rifle Rack measuring 31"x 10"x 35 1/2" is made of solid native pine. It holds up to seven long guns. Assembly Required with all assembly hardware included. Recommended for indoor use only. Made in the USA.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 3893 | Books | The Mosin-Nagant Rifle, 6th Edition (For collectors only) |

### 2-hop (shortest distance exactly 2): 7 nodes

| node id | true class | title |
|---|---|---|
| 422 | label 25 | missing |
| 3827 | Sports & Outdoors | Set of 40 BRAND NEW Stripper Clips For Mosin Nagant 1891/30 91/30 M38 M39 M44 7.62X54r Rifles |
| 3846 | Sports & Outdoors | Mauser Stripper Clips 40CT 6.5x55mm 38,94,96 &amp; 30-06, 1903, 1917 |
| 21214 | Books | The Lee-Enfield Rifle (Weapon) |
| 21233 | Sports & Outdoors | ProMag Archangel Opfor AA9130 Forend Rail, Black |
| 21443 | Sports & Outdoors | Mosin Nagant 91/30 &quot;Range Buddy&quot; Front Sight Adjustment Tool |
| 21444 | Sports & Outdoors | Pachmayr Decelerator Slip On Recoil Pad |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/products/cf-gnnexplainer-canonical/random_seed_42_*` (key=73).

- Factual class: **Sports & Outdoors**
- Counterfactual class: **Industrial & Scientific**
- Removed edges (global ids, 1): (3893, 21445)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 21445 |
| Factual_Target_Node_Neighbors | 3893 |
| Factual_Target_Node_Features | inch, deflockedst, one, use, use, assembl, use, use, use, hardwar, hold, use, includ, indoor, use, use, long, made, use, also, use, use, recommend, requir, rifl, seven, solid, sport, use, use, use, make, usa, use, use |
| Counterfactual_Target_Node_Neighbors |  |
| Counterfactual_Target_Node_Features | inch, deflockedst, one, use, use, assembl, use, use, use, hardwar, hold, use, includ, indoor, use, use, long, made, use, also, use, use, recommend, requir, rifl, seven, solid, sport, use, use, use, make, usa, use, use |
| Factual_Target_Node_Class | Sports & Outdoors |
| Counterfactual_Target_Node_class | Industrial & Scientific |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 3893 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 21445 |
| Factual_Target_Node_Neighbors | 3893 |
| Factual_Target_Node_Features | inch, deflockedst, one, use, use, assembl, use, use, use, hardwar, hold, use, includ, indoor, use, use, long, made, use, also, use, use, recommend, requir, rifl, seven, solid, sport, use, use, use, make, usa, use, use |
| Counterfactual_Target_Node_Neighbors |  |
| Counterfactual_Target_Node_Features | inch, deflockedst, one, use, use, assembl, use, use, use, hardwar, hold, use, includ, indoor, use, use, long, made, use, also, use, use, recommend, requir, rifl, seven, solid, sport, use, use, use, make, usa, use, use |
| Factual_Target_Node_Class | Sports & Outdoors |
| Counterfactual_Target_Node_class | Industrial & Scientific |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 3893 |
| Natural_Language_Explanation | None |
