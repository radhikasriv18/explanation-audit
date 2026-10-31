# Reference packet: CF-GNNExplainer__Llama-8B__products__33376

- Method: CF-GNNExplainer; configuration: Llama-8B; dataset: products; target node: 33376
- Explanation source: `./llm-graph-cf/data/results/cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_products_standard_Response.json` ([118][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, we can fill in the dictionary as follows:

infos = {
    'Target_Node_ID': 33376,
    'Factual_Target_Node_Neighbors': [7314],
    'Factual_Target_Node_Features': ['adhes', 'also', 'use', 'anyth', 'book', 'clean', 'disney', 'easi', 'els', 'kit', 'maintain', 'perfect', 'remov', 'reusabl', 'self', 'stick', 'sticker', 'surfac', 'make', 'toy', 'wall', 'window'],
    'Counterfactual_Target_Node_Neighbors': [7314],
    'Counterfactual_Target_Node_Features': ['adhes', 'also', 'use', 'anyth', 'book', 'clean', 'disney', 'easi', 'els', 'kit', 'maintain', 'perfect', 'remov', 'reusabl', 'self', 'stick', 'sticker', 'surfac', 'make', 'toy', 'wall', 'window'],
    'Factual_Target_Node_Class': 'Home & Kitchen',
    'Counterfactual_Target_Node_class': 'Toys & Games',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Natural_Language_Explanation': ''
}

The target node is 33376, which is the Disney Fairies (Tinkerbell) Wall Sticker Kit. In the factual graph, it is classified as Home & Kitchen, but in the counterfactual graph, it is classified as Toys & Games.

Upon analyzing the changes in the graph, we notice that the only difference between the factual and counterfactual graphs is the classification of the target node. The neighbors of the target node remain the same in both graphs. However, the classification of the target node has changed from Home & Kitchen to Toys & Games.

This change in classification can be attributed to the fact that the target node's features have not changed, but its classification has been altered. This suggests that the model's decision to classify the target node as Toys & Games is based on factors other than the node's features, such as the influence of its neighbors or the overall structure of the graph.

In terms of the influences of neighboring nodes, we can see that the target node is connected to node 7314, which is a Disney - Tinkerbell Fairies Room-in-a-Box Bundle. This node is classified as Home & Kitchen in both graphs, suggesting that it does not contribute to the change in classification of the target node.

However, the classification of the target node has changed from Home & Kitchen to Toys & Games, which implies that the model has taken into account the influence of other nodes in the graph. One possible explanation is that the model has considered the relationships between the target node and other nodes in the Toys & Games category, leading to a change in classification.

To provide a more detailed explanation, we can analyze the features of the target node and its neighbors. The target node has features such as 'adhes', 'also', 'use', 'anyth', 'book', 'clean', 'disney', 'easi', 'els', 'kit', 'maintain', 'perfect', 'remov', 'reusabl', 'self', 'stick', 'sticker', 'surfac', 'make', 'toy', 'wall', and 'window'. These features suggest that the target node is related to toys and games, which is consistent with its new classification as Toys & Games.

In contrast, the features of the target node in the factual graph are similar to those in the counterfactual graph, but its classification has changed. This suggests that the model's decision to classify the target node as Home & Kitchen was incorrect, and the correct classification is Toys & Games.

Overall, the change in classification of the target node can be attributed to the influence of other nodes in the graph, particularly those in the Toys & Games category. The model has taken into account the relationships between the target node and other nodes, leading to a change in classification.
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
given the factual graph: The node 854 is a product titled 'Nickelodeon Sponge Bob Toddler Bed' with key attributes: access, also, use, well, bed, built, charact, child, come, dream, easi, favorit, featur, frame, ground, kid, let, low, metal, year, plastic, safe, secur, side, sleep, standard, stori, book, make, hope and is connected with the node 7314 and it is classified as Home & Kitchen, it is not the target node. The node 7314 is a product titled 'Disney - Tinkerbell Fairies Room-in-a-Box Bundle' with key attributes: use, bed, box, disney, room and is connected with the nodes 854, 33375, 33376, 33377, 33378, 33379 and it is classified as Home & Kitchen, it is not the target node. The node 33375 is a product titled 'Disney 4 Piece Toddler Set, Tinkerbell' with key attributes: temperatur, capsul, across, use, bed, case, cold, collect, cotton, disney, take, dri, pillowcas, fli, four, fun, includ, one, iron, kid, land, let, littl, low, machin, made, piec, polyest, room, set, sheet, top, wash and is connected with the node 7314 and it is classified as Home & Kitchen, it is not the target node. The node 33376 is a product titled 'Disney Fairies (Tinkerbell) Wall Sticker Kit' with key attributes: adhes, also, use, anyth, book, clean, disney, easi, els, kit, maintain, perfect, remov, reusabl, self, stick, sticker, surfac, make, toy, wall, window and is connected with the node 7314 and it is classified as Home & Kitchen, it is the target node. The node 33377 is a product titled 'Disney Fairies Toddler Bed' with key attributes: access, use, bed, big, built, charact, child, color, come, design, disney, durabl, easi, favorit, featur, frame, girl, ground, one, high, inspir, last, lightweight, littl, low, make, metal, must, perfect, plastic, qualiti, safe, secur, side, strength, sturdi, yet and is connected with the node 7314 and it is classified as Home & Kitchen, it is not the target node. The node 33378 is a product titled 'Disney Princess 3-in-1 Dream Canopy Bed - Convertible Doll Bed' with key attributes: inch, use, back, bed, disney, dream, fabric, favorit, featur, fit, girl, book, includ, littl, love, make, perfect, play, live, way and is connected with the node 7314 and it is classified as Home & Kitchen, it is not the target node. The node 33379 is a product titled '"Disney 4 Piece Minnie's Fluttery Friends Toddler Bedding Set, Lavender"' with key attributes: made, across, use, bed, bottom, cold, disney, dri, fill, pillowcas, flat, friend, gentl, heat, book, includ, one, iron, littl, love, low, machin, microfib, need, non, also, piec, polyest, room, set, sheet, standard, sweet, top, make, wash, water and is connected with the node 7314 and it is classified as Home & Kitchen, it is not the target node. and given the counterfactual example: The node 854 is a product titled 'Nickelodeon Sponge Bob Toddler Bed' with key attributes: access, also, use, well, bed, built, charact, child, come, dream, easi, favorit, featur, frame, ground, kid, let, low, metal, year, plastic, safe, secur, side, sleep, standard, stori, book, make, hope and is connected with the node 7314 and it is classified as Home & Kitchen, it is not the target node. The node 7314 is a product titled 'Disney - Tinkerbell Fairies Room-in-a-Box Bundle' with key attributes: use, bed, box, disney, room and is connected with the nodes 854, 33375, 33376, 33378 and it is classified as Home & Kitchen, it is not the target node. The node 33375 is a product titled 'Disney 4 Piece Toddler Set, Tinkerbell' with key attributes: temperatur, capsul, across, use, bed, case, cold, collect, cotton, disney, take, dri, pillowcas, fli, four, fun, includ, one, iron, kid, land, let, littl, low, machin, made, piec, polyest, room, set, sheet, top, wash and is connected with the node 7314 and it is classified as Home & Kitchen, it is not the target node. The node 33376 is a product titled 'Disney Fairies (Tinkerbell) Wall Sticker Kit' with key attributes: adhes, also, use, anyth, book, clean, disney, easi, els, kit, maintain, perfect, remov, reusabl, self, stick, sticker, surfac, make, toy, wall, window and is connected with the node 7314 and it is classified as Toys & Games, it is the target node. The node 33377 is a product titled 'Disney Fairies Toddler Bed' with key attributes: access, use, bed, big, built, charact, child, color, come, design, disney, durabl, easi, favorit, featur, frame, girl, ground, one, high, inspir, last, lightweight, littl, low, make, metal, must, perfect, plastic, qualiti, safe, secur, side, strength, sturdi, yet and is connected with no other nodes and it is classified as Toys & Games, it is not the target node. The node 33378 is a product titled 'Disney Princess 3-in-1 Dream Canopy Bed - Convertible Doll Bed' with key attributes: inch, use, back, bed, disney, dream, fabric, favorit, featur, fit, girl, book, includ, littl, love, make, perfect, play, live, way and is connected with the node 7314 and it is classified as Home & Kitchen, it is not the target node. The node 33379 is a product titled '"Disney 4 Piece Minnie's Fluttery Friends Toddler Bedding Set, Lavender"' with key attributes: made, across, use, bed, bottom, cold, disney, dri, fill, pillowcas, flat, friend, gentl, heat, book, includ, one, iron, littl, love, low, machin, microfib, need, non, also, piec, polyest, room, set, sheet, standard, sweet, top, make, wash, water and is connected with no other nodes and it is classified as Home & Kitchen, it is not the target node.
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

- ID: 33376
- Title: Disney Fairies (Tinkerbell) Wall Sticker Kit
- True class (canonical `y`): **Toys & Games**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Home & Kitchen**
- Prediction recorded by this method's pipeline: **Home & Kitchen**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Disney Fairies (Tinkerbell) Wall Sticker Kit. Content: Disney Fairies (Tinkerbell) Wall Sticker Kit is perfect to decorate a themed bedroom, they can also be used to stick on Windows, Mirrors, Toy Boxes, Books and anything else you can imagine. With a wipe clean surface they are easy to maintain. Self adhesive. Removable and Reusable.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 7314 | Baby | Disney - Tinkerbell Fairies Room-in-a-Box Bundle |

### 2-hop (shortest distance exactly 2): 5 nodes

| node id | true class | title |
|---|---|---|
| 854 | Home & Kitchen | Nickelodeon Sponge Bob Toddler Bed |
| 33375 | Baby | Disney 4 Piece Toddler Set, Tinkerbell |
| 33377 | Home & Kitchen | Disney Fairies Toddler Bed |
| 33378 | Toys & Games | Disney Princess 3-in-1 Dream Canopy Bed - Convertible Doll Bed |
| 33379 | Baby | "Disney 4 Piece Minnie's Fluttery Friends Toddler Bedding Set, Lavender" |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/products/cf-gnnexplainer-canonical/random_seed_42_*` (key=118).

- Factual class: **Home & Kitchen**
- Counterfactual class: **Toys & Games**
- Removed edges (global ids, 2): (7314, 33377), (7314, 33379)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 33376 |
| Factual_Target_Node_Neighbors | 7314 |
| Factual_Target_Node_Features | adhes, also, use, use, anyth, use, use, book, use, clean, use, disney, easi, els, use, use, kit, maintain, use, perfect, use, use, remov, reusabl, self, stick, sticker, surfac, make, use, use, toy, use, wall, window, use, use |
| Counterfactual_Target_Node_Neighbors | 7314 |
| Counterfactual_Target_Node_Features | adhes, also, use, use, anyth, use, use, book, use, clean, use, disney, easi, els, use, use, kit, maintain, use, perfect, use, use, remov, reusabl, self, stick, sticker, surfac, make, use, use, toy, use, wall, window, use, use |
| Factual_Target_Node_Class | Home & Kitchen |
| Counterfactual_Target_Node_class | Toys & Games |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 33376 |
| Factual_Target_Node_Neighbors | 7314 |
| Factual_Target_Node_Features | adhes, also, use, use, anyth, use, use, book, use, clean, use, disney, easi, els, use, use, kit, maintain, use, perfect, use, use, remov, reusabl, self, stick, sticker, surfac, make, use, use, toy, use, wall, window, use, use |
| Counterfactual_Target_Node_Neighbors | 7314 |
| Counterfactual_Target_Node_Features | adhes, also, use, use, anyth, use, use, book, use, clean, use, disney, easi, els, use, use, kit, maintain, use, perfect, use, use, remov, reusabl, self, stick, sticker, surfac, make, use, use, toy, use, wall, window, use, use |
| Factual_Target_Node_Class | Home & Kitchen |
| Counterfactual_Target_Node_class | Toys & Games |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |
