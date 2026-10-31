# Reference packet: CF-GNNExplainer__Qwen-14B__products__30322

- Method: CF-GNNExplainer; configuration: Qwen-14B; dataset: products; target node: 30322
- Explanation source: `./robustness_2026-10-30/production_a100/qwen14b_gptq_int4_products_Response.json` ([112][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
To address the provided scenario, we need to analyze the differences between the factual and counterfactual graphs and fill the `infos` dictionary accordingly. Let's break down the changes and their implications.

### Factual Graph Analysis

In the factual graph, the target node (node 30322) titled "Ahi Viene Martin Corona" is classified as CDs & Vinyl and is connected to node 6463, which is titled "Carmen la de Ronda (1959) [audio in Spanish only]". This connection suggests that the target node shares some common attributes with node 6463, leading to its classification as CDs & Vinyl.

### Counterfactual Graph Analysis

In the counterfactual graph, the same target node (node 30322) is still titled "Ahi Viene Martin Corona" but is now disconnected from node 6463. Additionally, it remains classified as Movies & TV, which is different from the original classification of CDs & Vinyl.

### Differences Identified

- **Node Differences**: The only difference lies in the connections of node 30322. In the factual graph, it is connected to node 6463, while in the counterfactual graph, it is not.
  
- **Edge Differences**: The edge between node 30322 and node 6463 is removed in the counterfactual graph. Therefore, the edge difference is represented as `[(30322, 6463)]`.

### Filling the Dictionary

Based on the analysis, we can fill the `infos` dictionary as follows:

```python
infos = {
    'Target_Node_ID': 30322,
    'Factual_Target_Node_Neighbors': [6463],
    'Factual_Target_Node_Features': ['use', 'dvd'],
    'Counterfactual_Target_Node_Neighbors': [],
    'Counterfactual_Target_Node_Features': ['use', 'dvd'],
    'Factual_Target_Node_Class': 'CDs & Vinyl',
    'Counterfactual_Target_Node_class': 'Movies & TV',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Natural_Language_Explanation': 'In the factual graph, node 30322 titled "Ahi Viene Martin Corona" was classified as CDs & Vinyl and was connected to node 6463. In the counterfactual graph, the connection to node 6463 is removed, leading to a reclassification as Movies & TV.'
}
```

### Explanation of Changes

The removal of the edge between node 30322 and node 6463 significantly alters the classification of node 30322. In the factual graph, the connection to node 6463, which is a CD, influenced the classification of node 30322 as CDs & Vinyl. However, in the counterfactual graph, the absence of this connection disrupts the influence of node 6463, leading to a reclassification as Movies & TV. This demonstrates how the structural context of a node within a graph can heavily impact its classification, highlighting the importance of neighboring nodes in determining the overall classification of a node in a graph-based machine learning model.

This counterfactual explanation provides insight into how minimal changes in the graph structure can lead to significant shifts in the predicted class of a node, thereby enhancing our understanding of the model's decision-making process.
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
given the factual graph: The node 743 is a product titled 'missing' with key attributes: use, appli, record, com, que, demand, manufactur, media, miss, polici, return, standard, make and is connected with the nodes 751, 6463 and it is classified as CDs & Vinyl, it is not the target node. The node 751 is a product titled 'missing' with key attributes: use, appli, record, com, demand, que, manufactur, media, miss, polici, return, standard, make and is connected with the nodes 743, 6463 and it is classified as CDs & Vinyl, it is not the target node. The node 6463 is a product titled 'Carmen la de Ronda (1959) [audio in Spanish only]' with key attributes: along, use, well, attent, audio, becam, began, better, career, que, war, earli, english, first, would, book, known, lead, movi, multi, music, one, also, popular, releas, singer, star, provid, work, world and is connected with the nodes 743, 751, 30318, 30319, 30320, 30321, 30322 and it is classified as CDs & Vinyl, it is not the target node. The node 30318 is a product titled 'missing' with key attributes: one, also, although, use, among, art, time, audio, away, beauti, dvd, english, enjoy, ever, everyth, eye, film, final, format, greater, greatest, heart, book, que, love, low, may, miss, make, movement, movi, much, read, note, year, qualiti, outstand, pictur, play, player, pleas, plot, quit, real, sea, live, sold, take, well, voic, watch, woman, world, worldwid and is connected with the node 6463 and it is classified as Movies & TV, it is not the target node. The node 30319 is a product titled 'missing' with key attributes: use, factori, miss, new and is connected with the node 6463 and it is classified as CDs & Vinyl, it is not the target node. The node 30320 is a product titled 'Samba (NO ENGLISH) [Import]' with key attributes: one, also, use, audio, que, dead, take, dvd, english, forc, format, goe, book, man, live, play, player, presid, real, room, school, see, singer, sold, make, two, pleas, first, worldwid and is connected with the node 6463 and it is classified as Movies & TV, it is not the target node. The node 30321 is a product titled 'Vera Cruz' with key attributes: use, anoth, anyon, well, bit, cast, charact, charl, countri, cute, director, discov, doubl, one, even, ever, featur, first, friend, game, get, gold, would, year, book, highest, jack, last, look, magic, may, love, meet, men, old, text, pair, real, revolutionari, robert, time, secret, sell, serv, south, take, tale, team, hope, make, way, work and is connected with the node 6463 and it is classified as Movies & TV, it is not the target node. The node 30322 is a product titled 'Ahi Viene Martin Corona' with key attributes: use, dvd and is connected with the node 6463 and it is classified as CDs & Vinyl, it is the target node. and given the counterfactual example: The node 743 is a product titled 'missing' with key attributes: use, appli, record, com, que, demand, manufactur, media, miss, polici, return, standard, make and is connected with the nodes 751, 6463 and it is classified as CDs & Vinyl, it is not the target node. The node 751 is a product titled 'missing' with key attributes: use, appli, record, com, demand, que, manufactur, media, miss, polici, return, standard, make and is connected with the nodes 743, 6463 and it is classified as CDs & Vinyl, it is not the target node. The node 6463 is a product titled 'Carmen la de Ronda (1959) [audio in Spanish only]' with key attributes: along, use, well, attent, audio, becam, began, better, career, que, war, earli, english, first, would, book, known, lead, movi, multi, music, one, also, popular, releas, singer, star, provid, work, world and is connected with the nodes 743, 751, 30318, 30319, 30320, 30321 and it is classified as CDs & Vinyl, it is not the target node. The node 30318 is a product titled 'missing' with key attributes: one, also, although, use, among, art, time, audio, away, beauti, dvd, english, enjoy, ever, everyth, eye, film, final, format, greater, greatest, heart, book, que, love, low, may, miss, make, movement, movi, much, read, note, year, qualiti, outstand, pictur, play, player, pleas, plot, quit, real, sea, live, sold, take, well, voic, watch, woman, world, worldwid and is connected with the node 6463 and it is classified as Movies & TV, it is not the target node. The node 30319 is a product titled 'missing' with key attributes: use, factori, miss, new and is connected with the node 6463 and it is classified as CDs & Vinyl, it is not the target node. The node 30320 is a product titled 'Samba (NO ENGLISH) [Import]' with key attributes: one, also, use, audio, que, dead, take, dvd, english, forc, format, goe, book, man, live, play, player, presid, real, room, school, see, singer, sold, make, two, pleas, first, worldwid and is connected with the node 6463 and it is classified as Movies & TV, it is not the target node. The node 30321 is a product titled 'Vera Cruz' with key attributes: use, anoth, anyon, well, bit, cast, charact, charl, countri, cute, director, discov, doubl, one, even, ever, featur, first, friend, game, get, gold, would, year, book, highest, jack, last, look, magic, may, love, meet, men, old, text, pair, real, revolutionari, robert, time, secret, sell, serv, south, take, tale, team, hope, make, way, work and is connected with the node 6463 and it is classified as Movies & TV, it is not the target node. The node 30322 is a product titled 'Ahi Viene Martin Corona' with key attributes: use, dvd and is connected with no other nodes and it is classified as Movies & TV, it is the target node.
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

- ID: 30322
- Title: Ahi Viene Martin Corona
- True class (canonical `y`): **Movies & TV**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **CDs & Vinyl**
- Prediction recorded by this method's pipeline: **CDs & Vinyl**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Ahi Viene Martin Corona. Content: dvd
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 6463 | Movies & TV | Carmen la de Ronda (1959) [audio in Spanish only] |

### 2-hop (shortest distance exactly 2): 6 nodes

| node id | true class | title |
|---|---|---|
| 743 | CDs & Vinyl | missing |
| 751 | CDs & Vinyl | missing |
| 30318 | Movies & TV | missing |
| 30319 | Movies & TV | missing |
| 30320 | Movies & TV | Samba (NO ENGLISH) [Import] |
| 30321 | Movies & TV | Vera Cruz |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/products/cf-gnnexplainer-canonical/random_seed_42_*` (key=112).

- Factual class: **CDs & Vinyl**
- Counterfactual class: **Movies & TV**
- Removed edges (global ids, 1): (6463, 30322)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 30322 |
| Factual_Target_Node_Neighbors | 6463 |
| Factual_Target_Node_Features | use, use, use, dvd, use, use, use, use, use |
| Counterfactual_Target_Node_Neighbors |  |
| Counterfactual_Target_Node_Features | use, use, use, dvd, use, use, use, use, use |
| Factual_Target_Node_Class | CDs & Vinyl |
| Counterfactual_Target_Node_class | Movies & TV |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 6463 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 30322 |
| Factual_Target_Node_Neighbors | 6463 |
| Factual_Target_Node_Features | use, use, use, dvd, use, use, use, use, use |
| Counterfactual_Target_Node_Neighbors |  |
| Counterfactual_Target_Node_Features | use, use, use, dvd, use, use, use, use, use |
| Factual_Target_Node_Class | CDs & Vinyl |
| Counterfactual_Target_Node_class | Movies & TV |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 6463 |
| Natural_Language_Explanation | None |
