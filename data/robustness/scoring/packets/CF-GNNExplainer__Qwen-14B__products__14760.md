# Reference packet: CF-GNNExplainer__Qwen-14B__products__14760

- Method: CF-GNNExplainer; configuration: Qwen-14B; dataset: products; target node: 14760
- Explanation source: `./robustness_2026-10-30/production_a100/qwen14b_gptq_int4_products_Response.json` ([49][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
To address the provided scenario, we need to analyze the differences between the factual and counterfactual graphs and fill the `infos` dictionary accordingly. Let's break down the changes and their implications.

### Factual Graph Analysis

In the factual graph, the target node (node 14760) is titled "Lobo Spicy Tom Yum soup mix 30g X 5 pack" and is classified under "Health & Personal Care." It is connected to node 1974, which is a product titled "Namman Muay Thai Boxing Analgesic Balm Massage Relief Ache 100g," and several other nodes related to health and personal care products.

### Counterfactual Graph Analysis

In the counterfactual graph, the same target node (node 14760) is still titled "Lobo Spicy Tom Yum soup mix 30g X 5 pack," but its classification has changed to "Beauty." Additionally, it is no longer connected to node 1974, indicating a structural change in the graph.

### Differences Identified

1. **Node Connections**: In the factual graph, node 14760 is connected to node 1974. In the counterfactual graph, node 14760 is disconnected from node 1974.
2. **Classification Change**: The target node's classification changes from "Health & Personal Care" to "Beauty."

### Filling the Dictionary

Based on the analysis, we can fill the `infos` dictionary as follows:

```python
infos = {
    'Target_Node_ID': 14760,
    'Factual_Target_Node_Neighbors': [1974],
    'Factual_Target_Node_Features': ['use', 'well', 'becom', 'best', 'blend', 'easili', 'hot', 'know', 'mix', 'must', 'one', 'pack', 'peel', 'make', 'tough'],
    'Counterfactual_Target_Node_Neighbors': [],
    'Counterfactual_Target_Node_Features': ['use', 'well', 'becom', 'best', 'blend', 'easili', 'hot', 'know', 'mix', 'must', 'one', 'pack', 'peel', 'make', 'tough'],
    'Factual_Target_Node_Class': 'Health & Personal Care',
    'Counterfactual_Target_Node_class': 'Beauty',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Natural_Language_Explanation': 'In the factual graph, the target node (node 14760) was classified as "Health & Personal Care" and was connected to node 1974. In the counterfactual graph, the target node is disconnected from node 1974 and reclassified as "Beauty". The removal of the connection to node 1974 likely influenced the change in classification.'
}
```

### Explanation of Changes

The primary difference lies in the connectivity and classification of the target node. In the factual graph, the target node is part of a network primarily associated with health and personal care products. By removing the connection to node 1974, the target node loses its association with health-related products, leading to a reclassification under "Beauty." 

This change highlights the importance of the graph structure in influencing node classifications. The removal of a single edge can significantly alter the context and classification of a node, demonstrating the interconnected nature of nodes in a graph and the impact of their neighborhood on their classification.

In summary, the counterfactual scenario illustrates how altering the graph structure can lead to a different classification for the target node, emphasizing the role of neighboring nodes in determining node classifications within graph-based machine learning models.
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
given the factual graph: The node 165 is a product titled 'Revgear Muay Thai Shorts' with key attributes: across, use, authent, avail, black, blue, color, cut, eas, elast, extra, front, mean, movement, profession, red, short, size, wide and is connected with the node 1974 and it is classified as Health & Personal Care, it is not the target node. The node 1974 is a product titled 'Namman Muay Thai Boxing Analgesic Balm Massage Relief Ache 100g' with key attributes: inch, made, handbookandth, action, activ, year, one, use, book, appli, area, around, well, time, never, bodi, brand, condit, cream, current, day, descript, effect, exercis, fight, gentli, ingredi, like, know, known, least, get, long, man, mani, massag, must, new, open, pain, popular, pre, provid, readi, relief, seal, seriou, side, simpli, size, skin, sport, first, read, tight, tool, train, treatment, uniqu, make, warm, world and is connected with the nodes 165, 14758, 14759, 14760, 14761, 14762 and it is classified as Health & Personal Care, it is not the target node. The node 14758 is a product titled 'Thai whole dried chile - 3.5 oz' with key attributes: use, bag, skin, whole and is connected with the node 1974 and it is classified as Health & Personal Care, it is not the target node. The node 14759 is a product titled '"POND'S Age Miracle Day Cream 50g. Sale!!!"' with key attributes: per, advanc, age, use, best, complex, cream, daili, day, develop, fight, fine, line, sensit, smooth, special, technolog, wrinkl and is connected with the node 1974 and it is classified as Health & Personal Care, it is not the target node. The node 14760 is a product titled 'Lobo Spicy Tom Yum soup mix 30g X 5 pack' with key attributes: use, well, becom, best, blend, easili, hot, know, mix, must, one, pack, peel, make, tough and is connected with the node 1974 and it is classified as Health & Personal Care, it is the target node. The node 14761 is a product titled 'Namman Muay Thai Boxing Liniment 120ml. (2 Bottles)' with key attributes: activ, aid, use, book, applic, benefit, blood, bodi, bottl, like, fast, feel, formul, year, help, hour, improv, ingredi, one, known, leav, light, made, main, oil, open, manufactur, qualiti, quickli, reduc, scent, side, smooth, may, special, unlik, upon, also, provid and is connected with the node 1974 and it is classified as Health & Personal Care, it is not the target node. The node 14762 is a product titled '2x100 G. Dentiste Plus White Vitamin C &amp; Xyitol Gum Toothpaste Made in Thailand' with key attributes: made, use, amp, bacteria, brand, brush, clean, complex, condit, descript, gentl, healthi, help, ingredi, natur, never, new, plu, promot, reduc, safe, size, strong, vitamin, white and is connected with the node 1974 and it is classified as Health & Personal Care, it is not the target node. and given the counterfactual example: The node 165 is a product titled 'Revgear Muay Thai Shorts' with key attributes: across, use, authent, avail, black, blue, color, cut, eas, elast, extra, front, mean, movement, profession, red, short, size, wide and is connected with the node 1974 and it is classified as Health & Personal Care, it is not the target node. The node 1974 is a product titled 'Namman Muay Thai Boxing Analgesic Balm Massage Relief Ache 100g' with key attributes: inch, made, handbookandth, action, activ, year, one, use, book, appli, area, around, well, time, never, bodi, brand, condit, cream, current, day, descript, effect, exercis, fight, gentli, ingredi, like, know, known, least, get, long, man, mani, massag, must, new, open, pain, popular, pre, provid, readi, relief, seal, seriou, side, simpli, size, skin, sport, first, read, tight, tool, train, treatment, uniqu, make, warm, world and is connected with the nodes 165, 14758, 14759, 14761, 14762 and it is classified as Health & Personal Care, it is not the target node. The node 14758 is a product titled 'Thai whole dried chile - 3.5 oz' with key attributes: use, bag, skin, whole and is connected with the node 1974 and it is classified as Health & Personal Care, it is not the target node. The node 14759 is a product titled '"POND'S Age Miracle Day Cream 50g. Sale!!!"' with key attributes: per, advanc, age, use, best, complex, cream, daili, day, develop, fight, fine, line, sensit, smooth, special, technolog, wrinkl and is connected with the node 1974 and it is classified as Health & Personal Care, it is not the target node. The node 14760 is a product titled 'Lobo Spicy Tom Yum soup mix 30g X 5 pack' with key attributes: use, well, becom, best, blend, easili, hot, know, mix, must, one, pack, peel, make, tough and is connected with no other nodes and it is classified as Beauty, it is the target node. The node 14761 is a product titled 'Namman Muay Thai Boxing Liniment 120ml. (2 Bottles)' with key attributes: activ, aid, use, book, applic, benefit, blood, bodi, bottl, like, fast, feel, formul, year, help, hour, improv, ingredi, one, known, leav, light, made, main, oil, open, manufactur, qualiti, quickli, reduc, scent, side, smooth, may, special, unlik, upon, also, provid and is connected with the node 1974 and it is classified as Health & Personal Care, it is not the target node. The node 14762 is a product titled '2x100 G. Dentiste Plus White Vitamin C &amp; Xyitol Gum Toothpaste Made in Thailand' with key attributes: made, use, amp, bacteria, brand, brush, clean, complex, condit, descript, gentl, healthi, help, ingredi, natur, never, new, plu, promot, reduc, safe, size, strong, vitamin, white and is connected with the node 1974 and it is classified as Health & Personal Care, it is not the target node.
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

- ID: 14760
- Title: Lobo Spicy Tom Yum soup mix 30g X 5 pack
- True class (canonical `y`): **Grocery & Gourmet Food**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Health & Personal Care**
- Prediction recorded by this method's pipeline: **Health & Personal Care**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Lobo Spicy Tom Yum soup mix 30g X 5 pack. Content: Shrimp Tom Yum or Tom Yum Goong must be one of the best know Thai dishes abroad. It's a subtle blend of hot and sour with citrus overtones derived from lime juice and kaffir lime peel. Be careful not to overcook the shrimps as they will become tough very easily.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 1974 | Health & Personal Care | Namman Muay Thai Boxing Analgesic Balm Massage Relief Ache 100g |

### 2-hop (shortest distance exactly 2): 5 nodes

| node id | true class | title |
|---|---|---|
| 165 | Clothing, Shoes & Jewelry | Revgear Muay Thai Shorts |
| 14758 | Grocery & Gourmet Food | Thai whole dried chile - 3.5 oz |
| 14759 | Beauty | "POND'S Age Miracle Day Cream 50g. Sale!!!" |
| 14761 | Health & Personal Care | Namman Muay Thai Boxing Liniment 120ml. (2 Bottles) |
| 14762 | Beauty | 2x100 G. Dentiste Plus White Vitamin C &amp; Xyitol Gum Toothpaste Made in Thailand |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/products/cf-gnnexplainer-canonical/random_seed_42_*` (key=49).

- Factual class: **Health & Personal Care**
- Counterfactual class: **Beauty**
- Removed edges (global ids, 1): (1974, 14760)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 14760 |
| Factual_Target_Node_Neighbors | 1974 |
| Factual_Target_Node_Features | use, use, well, use, becom, best, blend, use, easili, use, hot, use, know, mix, must, use, use, one, use, pack, peel, use, use, use, make, use, use, tough, well, make, use |
| Counterfactual_Target_Node_Neighbors |  |
| Counterfactual_Target_Node_Features | use, use, well, use, becom, best, blend, use, easili, use, hot, use, know, mix, must, use, use, one, use, pack, peel, use, use, use, make, use, use, tough, well, make, use |
| Factual_Target_Node_Class | Health & Personal Care |
| Counterfactual_Target_Node_class | Beauty |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 1974 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 14760 |
| Factual_Target_Node_Neighbors | 1974 |
| Factual_Target_Node_Features | use, use, well, use, becom, best, blend, use, easili, use, hot, use, know, mix, must, use, use, one, use, pack, peel, use, use, use, make, use, use, tough, well, make, use |
| Counterfactual_Target_Node_Neighbors |  |
| Counterfactual_Target_Node_Features | use, use, well, use, becom, best, blend, use, easili, use, hot, use, know, mix, must, use, use, one, use, pack, peel, use, use, use, make, use, use, tough, well, make, use |
| Factual_Target_Node_Class | Health & Personal Care |
| Counterfactual_Target_Node_class | Beauty |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 1974 |
| Natural_Language_Explanation | None |
