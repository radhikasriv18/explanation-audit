# Reference packet: CF-GNNExplainer__Qwen-14B__products__33376

- Method: CF-GNNExplainer; configuration: Qwen-14B; dataset: products; target node: 33376
- Explanation source: `./robustness_2026-10-30/production_a100/qwen14b_gptq_int4_products_Response.json` ([118][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
To address the provided scenario, we will first fill the `infos` dictionary based on the factual and counterfactual examples, then analyze the changes and their implications.

### Filling the Dictionary

Given the factual and counterfactual graphs, we can populate the `infos` dictionary as follows:

```python
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
```

### Explanation of Changes

In the factual graph, the target node (node 33376) is classified as "Home & Kitchen." In the counterfactual graph, the same node is reclassified as "Toys & Games."

#### Key Observations:

1. **Node Features**: The features of the target node remain unchanged between the factual and counterfactual graphs. The node still retains attributes like "adhes," "disney," "easi," "stick," and "sticker," which are consistent with both classifications.

2. **Classification Change**: Despite the unchanged features, the classification shifts from "Home & Kitchen" to "Toys & Games." This suggests that the classification is influenced by factors beyond just the node's direct attributes.

3. **Neighbor Nodes**: The neighbor nodes of the target node also show some changes. Specifically, in the counterfactual graph:
   - Node 33377 (a product titled "Disney Fairies Toddler Bed") is now classified as "Toys & Games."
   - Node 33379 (a product titled "Disney 4 Piece Minnie's Fluttery Friends Toddler Bedding Set, Lavender") is disconnected from the target node and is also classified as "Home & Kitchen."

These changes in the neighbor nodes likely contribute to the shift in classification for the target node. 

### Influence of Neighbor Nodes

The classification of the target node is influenced by the context provided by its neighboring nodes. In the factual graph, the target node is connected to multiple products classified under "Home & Kitchen," reinforcing its classification in the same category. However, in the counterfactual graph, the target node loses connections to some "Home & Kitchen" products and gains a connection to a product classified as "Toys & Games" (node 33377).

This shift in the neighborhood context alters the overall classification of the target node. The removal of connections to "Home & Kitchen" products and the addition of a "Toys & Games" product neighbor likely triggers the reclassification of the target node to "Toys & Games."

### Natural Language Explanation

The natural language explanation for the change in classification can be summarized as follows:

"The target node, 'Disney Fairies (Tinkerbell) Wall Sticker Kit,' was initially classified as 'Home & Kitchen' due to its connections with other 'Home & Kitchen' products. In the counterfactual scenario, the target node's classification changes to 'Toys & Games' because it loses connections to 'Home & Kitchen' products and gains a connection to a 'Toys & Games' product. This shift in the neighborhood context influences the model to reclassify the target node accordingly."

Thus, the `Natural_Language_Explanation` field in the dictionary can be filled as:

```python
'Natural_Language_Explanation': "The target node's classification changed from 'Home & Kitchen' to 'Toys & Games' due to alterations in its neighborhood context. The target node lost connections to 'Home & Kitchen' products and gained a connection to a 'Toys & Games' product, leading to a reclassification."
```

This completes the detailed analysis and explanation of the changes observed in the factual and counterfactual graphs.
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
