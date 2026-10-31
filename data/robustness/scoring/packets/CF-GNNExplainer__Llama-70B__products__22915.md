# Reference packet: CF-GNNExplainer__Llama-70B__products__22915

- Method: CF-GNNExplainer; configuration: Llama-70B; dataset: products; target node: 22915
- Explanation source: `./robustness_2026-10-30/llama70b/cf/products/22915.json` (response)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, we can fill the dictionary as follows:

infos = {
    'Target_Node_ID': 22915,
    'Factual_Target_Node_Neighbors': [4305],
    'Factual_Target_Node_Features': ['inch', 'dimens', 'capsul', 'acid', 'one', 'also', 'amaz', 'use', 'book', 'contain', 'essenti', 'excel', 'favorit', 'fiber', 'food', 'good', 'green', 'ingredi', 'iron', 'miner', 'mix', 'natur', 'organ', 'ounc', 'powder', 'protein', 'sourc', 'well', 'vitamin'],
    'Counterfactual_Target_Node_Neighbors': [4305],
    'Counterfactual_Target_Node_Features': ['inch', 'dimens', 'capsul', 'acid', 'one', 'also', 'amaz', 'use', 'book', 'contain', 'essenti', 'excel', 'favorit', 'fiber', 'food', 'good', 'green', 'ingredi', 'iron', 'miner', 'mix', 'natur', 'organ', 'ounc', 'powder', 'protein', 'sourc', 'well', 'vitamin'],
    'Factual_Target_Node_Class': 'Health & Personal Care',
    'Counterfactual_Target_Node_class': 'Grocery & Gourmet Food',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Node_Differences': [22916, 22917],
    'Edge_Differences': [(22916, 4305), (22917, 4305)],
    'Natural_Language_Explanation': 'The classification of the target node 22915 changed from Health & Personal Care to Grocery & Gourmet Food. This change is likely due to the fact that the node 22915 is still connected to the same node 4305, but the nodes 22916 and 22917 are no longer connected to 4305 in the counterfactual graph. The features of the target node 22915 remain the same, suggesting that the change in classification is not due to any changes in the node's attributes, but rather due to changes in the graph structure.'
}

Explanation:

The classification of the target node 22915 changed from Health & Personal Care to Grocery & Gourmet Food. This change is likely due to the fact that the node 22915 is still connected to the same node 4305, which is classified as Health & Personal Care. However, in the counterfactual graph, the nodes 22916 and 22917, which were previously connected to 4305, are no longer connected to it. These nodes are classified as Beauty, which may have influenced the classification of the target node 22915 in the factual graph.

In the counterfactual graph, the absence of connections between 22916, 22917, and 4305 may have reduced the influence of the Beauty category on the target node 22915, allowing it to be classified as Grocery & Gourmet Food. This suggests that the graph structure plays a significant role in determining the classification of nodes, and changes in the graph structure can lead to changes in node classification even if the node's attributes remain the same.

It's worth noting that the features of the target node 22915 remain the same in both the factual and counterfactual graphs, which suggests that the change in classification is not due to any changes in the node's attributes, but rather due to changes in the graph structure.
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
given the factual graph: The node 475 is a product titled 'Idea Works Waterfall Soap Saver' with key attributes: use, away, built, dri, excess, handi, hold, idea, one, keep, last, longer, make, place, plastic, soap, water, work and is connected with the node 4305 and it is classified as Beauty, it is not the target node. The node 4305 is a product titled 'Stopain Extra Strength Pain Relief Roll-On, 3 Ounce' with key attributes: also, use, book, benefit, contain, deep, easi, extra, featur, formula, free, hand, light, non, ounc, pain, proven, provid, relief, roll, scent, simpl, strength and is connected with the nodes 475, 8389, 22915, 22916, 22917, 22918 and it is classified as Health & Personal Care, it is not the target node. The node 8389 is a product titled 'Amerifit Culturelle Probiotics for Kids, 30 Count' with key attributes: made, day, actual, add, use, bacteria, balanc, benefit, better, child, cool, count, develop, easi, especi, free, ga, good, happi, healthi, help, keep, kid, like, liquid, littl, one, natur, ndash, parent, proven, reduc, rsquo, scienc, make, support, system, take, taken, book, work and is connected with the node 4305 and it is classified as Health & Personal Care, it is not the target node. The node 22915 is a product titled 'Amazing Grass Organic Wheat Grass Powder, 60 Servings, 17-Ounce Container' with key attributes: inch, dimens, capsul, acid, one, also, amaz, use, book, contain, essenti, excel, favorit, fiber, food, good, green, ingredi, iron, miner, mix, natur, organ, ounc, powder, protein, sourc, well, vitamin and is connected with the node 4305 and it is classified as Health & Personal Care, it is the target node. The node 22916 is a product titled 'Goat Milk Soap - Original (3 Pack) Canus Vermont 3 Bar Soap' with key attributes: one, use, book, bar, base, essenti, feel, fragranc, fresh, leav, natur, oil, origin, qualiti, pack, skin, soap, soft, valu, make, also and is connected with the node 4305 and it is classified as Beauty, it is not the target node. The node 22917 is a product titled 'Mederma Stretch Marks Therapy, 5.29 Oz Box' with key attributes: use, appear, box, combin, formula, free, improv, ingredi, like, skin, premium, reduc, shown, stretch, test, textur, therapi and is connected with the node 4305 and it is classified as Beauty, it is not the target node. The node 22918 is a product titled 'Mama Mio Get Waisted Body Shaper, 3.4 Ounce' with key attributes: use, bodi, cell, combat, design, take, fat, get, give, help, increas, ingredi, one, ounc, pack, proven, reduc, slim, way, well, redistribut, reader and is connected with the node 4305 and it is classified as Beauty, it is not the target node. and given the counterfactual example: The node 475 is a product titled 'Idea Works Waterfall Soap Saver' with key attributes: use, away, built, dri, excess, handi, hold, idea, one, keep, last, longer, make, place, plastic, soap, water, work and is connected with the node 4305 and it is classified as Health & Personal Care, it is not the target node. The node 4305 is a product titled 'Stopain Extra Strength Pain Relief Roll-On, 3 Ounce' with key attributes: also, use, book, benefit, contain, deep, easi, extra, featur, formula, free, hand, light, non, ounc, pain, proven, provid, relief, roll, scent, simpl, strength and is connected with the nodes 475, 8389, 22915, 22918 and it is classified as Health & Personal Care, it is not the target node. The node 8389 is a product titled 'Amerifit Culturelle Probiotics for Kids, 30 Count' with key attributes: made, day, actual, add, use, bacteria, balanc, benefit, better, child, cool, count, develop, easi, especi, free, ga, good, happi, healthi, help, keep, kid, like, liquid, littl, one, natur, ndash, parent, proven, reduc, rsquo, scienc, make, support, system, take, taken, book, work and is connected with the node 4305 and it is classified as Health & Personal Care, it is not the target node. The node 22915 is a product titled 'Amazing Grass Organic Wheat Grass Powder, 60 Servings, 17-Ounce Container' with key attributes: inch, dimens, capsul, acid, one, also, amaz, use, book, contain, essenti, excel, favorit, fiber, food, good, green, ingredi, iron, miner, mix, natur, organ, ounc, powder, protein, sourc, well, vitamin and is connected with the node 4305 and it is classified as Grocery & Gourmet Food, it is the target node. The node 22916 is a product titled 'Goat Milk Soap - Original (3 Pack) Canus Vermont 3 Bar Soap' with key attributes: one, use, book, bar, base, essenti, feel, fragranc, fresh, leav, natur, oil, origin, qualiti, pack, skin, soap, soft, valu, make, also and is connected with no other nodes and it is classified as Beauty, it is not the target node. The node 22917 is a product titled 'Mederma Stretch Marks Therapy, 5.29 Oz Box' with key attributes: use, appear, box, combin, formula, free, improv, ingredi, like, skin, premium, reduc, shown, stretch, test, textur, therapi and is connected with no other nodes and it is classified as Beauty, it is not the target node. The node 22918 is a product titled 'Mama Mio Get Waisted Body Shaper, 3.4 Ounce' with key attributes: use, bodi, cell, combat, design, take, fat, get, give, help, increas, ingredi, one, ounc, pack, proven, reduc, slim, way, well, redistribut, reader and is connected with the node 4305 and it is classified as Beauty, it is not the target node.
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

- ID: 22915
- Title: Amazing Grass Organic Wheat Grass Powder, 60 Servings, 17-Ounce Container
- True class (canonical `y`): **Health & Personal Care**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Health & Personal Care**
- Prediction recorded by this method's pipeline: **Health & Personal Care**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Amazing Grass Organic Wheat Grass Powder, 60 Servings, 17-Ounce Container. Content: Amazing Grass wheat grass powder is an excellent concentrated food source of beta-carotene, calcium, chlorophyll, fiber, iron and vitamin K. It is also a very good source of protein, vitamin C, vitamin B-12, folic acid, vitamin B-6, trace minerals and contains all essential amino acids. Mix a tablespoon of Green SuperFood with juice, milk, a smoothie or your favorite beverage. All natural and organic ingredients.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 4305 | Health & Personal Care | Stopain Extra Strength Pain Relief Roll-On, 3 Ounce |

### 2-hop (shortest distance exactly 2): 5 nodes

| node id | true class | title |
|---|---|---|
| 475 | Home & Kitchen | Idea Works Waterfall Soap Saver |
| 8389 | Health & Personal Care | Amerifit Culturelle Probiotics for Kids, 30 Count |
| 22916 | Beauty | Goat Milk Soap - Original (3 Pack) Canus Vermont 3 Bar Soap |
| 22917 | Beauty | Mederma Stretch Marks Therapy, 5.29 Oz Box |
| 22918 | Beauty | Mama Mio Get Waisted Body Shaper, 3.4 Ounce |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/products/cf-gnnexplainer-canonical/random_seed_42_*` (key=78).

- Factual class: **Health & Personal Care**
- Counterfactual class: **Grocery & Gourmet Food**
- Removed edges (global ids, 2): (4305, 22916), (4305, 22917)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 22915 |
| Factual_Target_Node_Neighbors | 4305 |
| Factual_Target_Node_Features | inch, dimens, capsul, acid, one, also, amaz, use, book, use, contain, use, essenti, excel, favorit, fiber, food, use, good, green, ingredi, iron, use, use, miner, mix, natur, use, use, organ, ounc, use, powder, use, protein, sourc, use, well, vitamin, use, use |
| Counterfactual_Target_Node_Neighbors | 4305 |
| Counterfactual_Target_Node_Features | inch, dimens, capsul, acid, one, also, amaz, use, book, use, contain, use, essenti, excel, favorit, fiber, food, use, good, green, ingredi, iron, use, use, miner, mix, natur, use, use, organ, ounc, use, powder, use, protein, sourc, use, well, vitamin, use, use |
| Factual_Target_Node_Class | Health & Personal Care |
| Counterfactual_Target_Node_class | Grocery & Gourmet Food |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 22915 |
| Factual_Target_Node_Neighbors | 4305 |
| Factual_Target_Node_Features | inch, dimens, capsul, acid, one, also, amaz, use, book, use, contain, use, essenti, excel, favorit, fiber, food, use, good, green, ingredi, iron, use, use, miner, mix, natur, use, use, organ, ounc, use, powder, use, protein, sourc, use, well, vitamin, use, use |
| Counterfactual_Target_Node_Neighbors | 4305 |
| Counterfactual_Target_Node_Features | inch, dimens, capsul, acid, one, also, amaz, use, book, use, contain, use, essenti, excel, favorit, fiber, food, use, good, green, ingredi, iron, use, use, miner, mix, natur, use, use, organ, ounc, use, powder, use, protein, sourc, use, well, vitamin, use, use |
| Factual_Target_Node_Class | Health & Personal Care |
| Counterfactual_Target_Node_class | Grocery & Gourmet Food |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |
