# Reference packet: CF-GNNExplainer__Llama-8B__products__47510

- Method: CF-GNNExplainer; configuration: Llama-8B; dataset: products; target node: 47510
- Explanation source: `./llm-graph-cf/data/results/cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_products_standard_Response.json` ([182][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, we can fill the dictionary as follows:

infos = {
    Target_Node_ID: 47510,
    Factual_Target_Node_Neighbors: [11442],
    Factual_Target_Node_Features: ['made', 'click', 'actual', 'one', 'use', 'well', 'case', 'cover', 'like', 'hard', 'much', 'highest', 'includ', 'materi', 'miss', 'also', 'qualiti', 'plastic', 'manufactur', 'skin', 'slim', 'sold', 'sticker', 'usa', 'vinyl'],
    Counterfactual_Target_Node_Neighbors: [11442],
    Counterfactual_Target_Node_Features: ['made', 'click', 'actual', 'one', 'use', 'well', 'case', 'cover', 'like', 'hard', 'much', 'highest', 'includ', 'materi', 'miss', 'also', 'qualiti', 'plastic', 'manufactur', 'skin', 'slim', 'sold', 'sticker', 'usa', 'vinyl],
    Factual_Target_Node_Class: 'Video Games',
    Counterfactual_Target_Node_class: 'Electronics',
    Target_Node_Features_Changed_From_Factual_To_Counterfactual: [],
    Natural_Language_Explanation: ''
}

However, there is a discrepancy in the classification of the target node between the factual and counterfactual examples. In the factual example, the target node 47510 is classified as 'Video Games', while in the counterfactual example, it is classified as 'Electronics'. To fill the dictionary correctly, we should note that the classification change is due to the change in the classification of the target node itself, rather than any changes in its neighbors or features.

To provide a more detailed explanation, let's analyze the changes in the graph structure and node features. The target node 47510 remains connected to the same set of neighbors in both the factual and counterfactual examples, which are all connected to the node 11442. However, the classification of the target node changes from 'Video Games' to 'Electronics'.

This change in classification may be attributed to the fact that the target node's features do not change significantly between the two examples. The features of the target node remain the same, indicating that the change in classification is not due to any changes in the node's characteristics.

The influence of the neighbor nodes on the target node's classification is also worth considering. The neighbors of the target node are all connected to the node 11442, which is classified as 'Video Games' in the factual example but remains unchanged in the counterfactual example. This suggests that the neighbors of the target node do not significantly influence its classification, as the classification change occurs despite the neighbors remaining the same.

In conclusion, the change in classification of the target node 47510 from 'Video Games' to 'Electronics' in the counterfactual example is primarily due to the change in the target node's classification itself, rather than any changes in its neighbors or features. The neighbors of the target node do not appear to significantly influence its classification, suggesting that the classification change is driven by the target node's intrinsic characteristics.
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
given the factual graph: The node 1376 is a product titled 'missing' with key attributes: use, good, miss, parti, qualiti and is connected with the node 11442 and it is classified as Video Games, it is not the target node. The node 1381 is a product titled 'missing' with key attributes: accessori, adjust, use, camera, eye, featur, flat, includ, miss, mount, move, also, panel, rang, viewer, variou, wide and is connected with the node 11442 and it is classified as Video Games, it is not the target node. The node 11393 is a product titled 'missing' with key attributes: charger, adapt, use, time, charg, custom, featur, includ, miss, origin, make, provid and is connected with the node 11442 and it is classified as Video Games, it is not the target node. The node 11417 is a product titled 'missing' with key attributes: access, across, activ, year, use, book, well, professor, divis, one, experi, extrem, featur, fight, govern, highli, want, left, militari, miss, need, new, risk, satisfact, skill, special, specif, state, team, though, ultim, war, first, make, work and is connected with the node 11442 and it is classified as Video Games, it is not the target node. The node 11442 is a product titled 'missing' with key attributes: use, miss and is connected with the nodes 1376, 1381, 11393, 11417, 47507, 47508, 47509, 47510 and it is classified as Video Games, it is not the target node. The node 47507 is a product titled 'missing' with key attributes: day, capsul, addit, use, year, stori, bold, bring, charact, voltag, evil, fan, favorit, fight, flash, game, good, green, includ, line, miss, new, take, live, make, woman, world and is connected with the node 11442 and it is classified as Toys & Games, it is not the target node. The node 47508 is a product titled 'missing' with key attributes: one, also, use, well, book, experi, friendli, friend, full, head, heart, hot, miss, need, play, player, set, speed, stage, make, take, ultim, via and is connected with the node 11442 and it is classified as Video Games, it is not the target node. The node 47509 is a product titled 'missing' with key attributes: kenwood, activ, along, use, book, camera, control, differ, drive, one, event, eye, famili, favorit, friend, fun, game, hard, hour, includ, make, miss, move, music, offer, stori, packag, pet, physic, play, project, provid, save, six, slim, space, special, sport, system, take and is connected with the node 11442 and it is classified as Video Games, it is not the target node. The node 47510 is a product titled 'missing' with key attributes: made, click, actual, one, use, well, case, cover, like, hard, much, highest, includ, materi, miss, also, qualiti, plastic, manufactur, skin, slim, sold, sticker, usa, vinyl and is connected with the node 11442 and it is classified as Video Games, it is the target node. and given the counterfactual example: The node 1376 is a product titled 'missing' with key attributes: use, good, miss, parti, qualiti and is connected with the node 11442 and it is classified as Video Games, it is not the target node. The node 1381 is a product titled 'missing' with key attributes: accessori, adjust, use, camera, eye, featur, flat, includ, miss, mount, move, also, panel, rang, viewer, variou, wide and is connected with the node 11442 and it is classified as Video Games, it is not the target node. The node 11393 is a product titled 'missing' with key attributes: charger, adapt, use, time, charg, custom, featur, includ, miss, origin, make, provid and is connected with the node 11442 and it is classified as Video Games, it is not the target node. The node 11417 is a product titled 'missing' with key attributes: access, across, activ, year, use, book, well, professor, divis, one, experi, extrem, featur, fight, govern, highli, want, left, militari, miss, need, new, risk, satisfact, skill, special, specif, state, team, though, ultim, war, first, make, work and is connected with the node 11442 and it is classified as Video Games, it is not the target node. The node 11442 is a product titled 'missing' with key attributes: use, miss and is connected with the nodes 1376, 1381, 11393, 11417, 47507, 47508, 47510 and it is classified as Video Games, it is not the target node. The node 47507 is a product titled 'missing' with key attributes: day, capsul, addit, use, year, stori, bold, bring, charact, voltag, evil, fan, favorit, fight, flash, game, good, green, includ, line, miss, new, take, live, make, woman, world and is connected with the node 11442 and it is classified as Toys & Games, it is not the target node. The node 47508 is a product titled 'missing' with key attributes: one, also, use, well, book, experi, friendli, friend, full, head, heart, hot, miss, need, play, player, set, speed, stage, make, take, ultim, via and is connected with the node 11442 and it is classified as Video Games, it is not the target node. The node 47509 is a product titled 'missing' with key attributes: kenwood, activ, along, use, book, camera, control, differ, drive, one, event, eye, famili, favorit, friend, fun, game, hard, hour, includ, make, miss, move, music, offer, stori, packag, pet, physic, play, project, provid, save, six, slim, space, special, sport, system, take and is connected with no other nodes and it is classified as Video Games, it is not the target node. The node 47510 is a product titled 'missing' with key attributes: made, click, actual, one, use, well, case, cover, like, hard, much, highest, includ, materi, miss, also, qualiti, plastic, manufactur, skin, slim, sold, sticker, usa, vinyl and is connected with the node 11442 and it is classified as Electronics, it is the target node.
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

- ID: 47510
- Title: missing
- True class (canonical `y`): **label 25**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Video Games**
- Prediction recorded by this method's pipeline: **Video Games**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: missing. Content: This listing is for one (1) PlayStation 3 Slim Console skin and (2) Constoller Skins displayed above. Actual controller not included. All our skins are made from the highest quality 3M material. Proudly made from 100% recycled materials here in the USA! These are Vinyl skins "Sticker" ONLY. Not a hard plastic cover or case! Sony Corporation is not affiliated with, nor does it authorize or sponsor the products being sold by 247Skins.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 11442 | Video Games | missing |

### 2-hop (shortest distance exactly 2): 7 nodes

| node id | true class | title |
|---|---|---|
| 1376 | Video Games | missing |
| 1381 | Video Games | missing |
| 11393 | Video Games | missing |
| 11417 | Video Games | missing |
| 47507 | Toys & Games | missing |
| 47508 | Video Games | missing |
| 47509 | Video Games | missing |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/products/cf-gnnexplainer-canonical/random_seed_42_*` (key=182).

- Factual class: **Video Games**
- Counterfactual class: **Electronics**
- Removed edges (global ids, 1): (11442, 47509)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 47510 |
| Factual_Target_Node_Neighbors | 11442 |
| Factual_Target_Node_Features | made, click, actual, one, use, use, use, well, use, case, use, cover, like, use, use, hard, much, highest, use, includ, use, use, made, materi, materi, miss, use, one, also, use, qualiti, plastic, use, use, manufactur, qualiti, skin, slim, sold, sticker, use, use, use, use, usa, vinyl, use |
| Counterfactual_Target_Node_Neighbors | 11442 |
| Counterfactual_Target_Node_Features | made, click, actual, one, use, use, use, well, use, case, use, cover, like, use, use, hard, much, highest, use, includ, use, use, made, materi, materi, miss, use, one, also, use, qualiti, plastic, use, use, manufactur, qualiti, skin, slim, sold, sticker, use, use, use, use, usa, vinyl, use |
| Factual_Target_Node_Class | Video Games |
| Counterfactual_Target_Node_class | Electronics |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 47510 |
| Factual_Target_Node_Neighbors | 11442 |
| Factual_Target_Node_Features | made, click, actual, one, use, use, use, well, use, case, use, cover, like, use, use, hard, much, highest, use, includ, use, use, made, materi, materi, miss, use, one, also, use, qualiti, plastic, use, use, manufactur, qualiti, skin, slim, sold, sticker, use, use, use, use, usa, vinyl, use |
| Counterfactual_Target_Node_Neighbors | 11442 |
| Counterfactual_Target_Node_Features | made, click, actual, one, use, use, use, well, use, case, use, cover, like, use, use, hard, much, highest, use, includ, use, use, made, materi, materi, miss, use, one, also, use, qualiti, plastic, use, use, manufactur, qualiti, skin, slim, sold, sticker, use, use, use, use, usa, vinyl, use |
| Factual_Target_Node_Class | Video Games |
| Counterfactual_Target_Node_class | Electronics |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |
