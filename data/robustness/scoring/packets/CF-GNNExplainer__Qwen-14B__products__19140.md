# Reference packet: CF-GNNExplainer__Qwen-14B__products__19140

- Method: CF-GNNExplainer; configuration: Qwen-14B; dataset: products; target node: 19140
- Explanation source: `./robustness_2026-10-30/production_a100/qwen14b_gptq_int4_products_Response.json` ([65][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
To address the provided scenario, we will first fill the `infos` dictionary based on the given factual and counterfactual examples. Then, we will analyze the changes and their impact on the classification of the target node.

### Filling the Dictionary

Given the factual and counterfactual graphs, let's populate the `infos` dictionary:

```python
infos = {
    'Target_Node_ID': '19140',
    'Factual_Target_Node_Neighbors': ['3267'],
    'Factual_Target_Node_Features': ['use', 'avail', 'brown', 'clean', 'color', 'commerci', 'construct', 'custom', 'durabl', 'duti', 'easi', 'featur', 'feet', 'free', 'gener', 'great', 'hand', 'heavi', 'keep', 'kitchen', 'length', 'line', 'measur', 'offer', 'polyest', 'secur', 'twin', 'uniqu', 'work'],
    'Counterfactual_Target_Node_Neighbors': ['3267'],
    'Counterfactual_Target_Node_Features': ['use', 'avail', 'brown', 'clean', 'color', 'commerci', 'construct', 'custom', 'durabl', 'duti', 'easi', 'featur', 'feet', 'free', 'gener', 'great', 'hand', 'heavi', 'keep', 'kitchen', 'length', 'line', 'measur', 'offer', 'polyest', 'secur', 'twin', 'uniqu', 'work'],
    'Factual_Target_Node_Class': 'Arts, Crafts & Sewing',
    'Counterfactual_Target_Node_class': 'Home & Kitchen',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Natural_Language_Explanation': ''
}
```

### Explanation of Changes

In the factual graph, the target node (node 19140) is classified as "Arts, Crafts & Sewing." In the counterfactual graph, the same node is reclassified as "Home & Kitchen."

#### Key Differences

1. **Node Connections**:
   - In the factual graph, node 19140 (target node) is connected to node 3267.
   - In the counterfactual graph, node 19140 remains connected to node 3267 but loses connections to nodes 19139 and gains no new connections.

2. **Neighbor Classifications**:
   - In the factual graph, node 3267 is classified as "Arts, Crafts & Sewing."
   - In the counterfactual graph, node 3267 still retains the classification "Arts, Crafts & Sewing," but nodes 19138 and 19139 change their classifications. Specifically, node 19138 changes from "Arts, Crafts & Sewing" to "Sports & Outdoors," and node 19139 remains in "Arts, Crafts & Sewing."

3. **Impact on Classification**:
   - The change in classification of node 19138 from "Arts, Crafts & Sewing" to "Sports & Outdoors" likely influences the classification of node 19140. Since node 19140 was previously connected to node 19138, this connection contributed to its classification within "Arts, Crafts & Sewing." However, in the counterfactual graph, node 19138 is disconnected from node 19140 and reclassified, which may shift the influence towards a different category.
   - Additionally, node 19139, which was previously connected to node 3267, is now disconnected, further altering the local neighborhood context around node 19140.

### Natural Language Explanation

The natural language explanation for the change in classification of the target node (node 19140) from "Arts, Crafts & Sewing" to "Home & Kitchen" can be summarized as follows:

"In the factual graph, the target node (node 19140) is classified as 'Arts, Crafts & Sewing,' primarily influenced by its connections to nodes 3267 and 19139, both of which belong to the same category. However, in the counterfactual graph, the classification of node 19140 changes to 'Home & Kitchen.' This change is driven by the alteration in the neighborhood structure. Specifically, node 19138, which was previously classified as 'Arts, Crafts & Sewing,' is now reclassified as 'Sports & Outdoors' and disconnected from node 19140. Additionally, node 19139, which was previously connected to node 3267, is now disconnected. These changes in the neighborhood context shift the overall influence on node 19140, leading to its reclassification as 'Home & Kitchen.'"

This explanation highlights the importance of the local neighborhood structure in influencing the classification of nodes in graph-based machine learning models.
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
given the factual graph: The node 339 is a product titled 'Darice 0500-04 Wood Beads, Large, Assorted Color' with key attributes: alwaysshowplaceholdertext, use, assort, color, come, larg, packag, per, piec, round, size, like, wood and is connected with the node 3267 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 3267 is a product titled 'Darice 5-Ply Craft Designer Jute, Natural' with key attributes: use, well, chair, common, contain, craft, graphic, feet, fiber, ideal, item, make, natur, packag, plant, pound, project, mani, type and is connected with the nodes 339, 19137, 19138, 19139, 19140 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 19137 is a product titled 'Darice 135-Feet 4 Ply Jute, 1-Pound' with key attributes: use, craft, creat, feet, mani, pound, project and is connected with the node 3267 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 19138 is a product titled 'Hemtique Cord Spool 20-Pound, Dark Brown' with key attributes: year, per, one, altern, use, well, brown, certifi, cord, cotton, dark, feet, free, high, includ, make, non, perfect, pound, qualiti, six, smooth, synthet, toxic, weight and is connected with the node 3267 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 19139 is a product titled 'Surgical Steel Earring Earwires Hypoallergenic Shiny Silver Plated Fishhook with 10x3.5mm Ball and Coil with Open Loop, ' with key attributes: made, million, deflockedst, stereo, use, ball, gaug, loop, open, plate, silver, steel and is connected with the node 3267 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 19140 is a product titled 'Lehigh 540W 230-Feet Polypropylene Heavy Duty Twine, Brown' with key attributes: use, avail, brown, clean, color, commerci, construct, custom, durabl, duti, easi, featur, feet, free, gener, great, hand, heavi, keep, kitchen, length, line, measur, offer, polyest, secur, twin, uniqu, work and is connected with the node 3267 and it is classified as Arts, Crafts & Sewing, it is the target node. and given the counterfactual example: The node 339 is a product titled 'Darice 0500-04 Wood Beads, Large, Assorted Color' with key attributes: alwaysshowplaceholdertext, use, assort, color, come, larg, packag, per, piec, round, size, like, wood and is connected with the node 3267 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 3267 is a product titled 'Darice 5-Ply Craft Designer Jute, Natural' with key attributes: use, well, chair, common, contain, craft, graphic, feet, fiber, ideal, item, make, natur, packag, plant, pound, project, mani, type and is connected with the nodes 339, 19139, 19140 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 19137 is a product titled 'Darice 135-Feet 4 Ply Jute, 1-Pound' with key attributes: use, craft, creat, feet, mani, pound, project and is connected with no other nodes and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 19138 is a product titled 'Hemtique Cord Spool 20-Pound, Dark Brown' with key attributes: year, per, one, altern, use, well, brown, certifi, cord, cotton, dark, feet, free, high, includ, make, non, perfect, pound, qualiti, six, smooth, synthet, toxic, weight and is connected with no other nodes and it is classified as Sports & Outdoors, it is not the target node. The node 19139 is a product titled 'Surgical Steel Earring Earwires Hypoallergenic Shiny Silver Plated Fishhook with 10x3.5mm Ball and Coil with Open Loop, ' with key attributes: made, million, deflockedst, stereo, use, ball, gaug, loop, open, plate, silver, steel and is connected with the node 3267 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 19140 is a product titled 'Lehigh 540W 230-Feet Polypropylene Heavy Duty Twine, Brown' with key attributes: use, avail, brown, clean, color, commerci, construct, custom, durabl, duti, easi, featur, feet, free, gener, great, hand, heavi, keep, kitchen, length, line, measur, offer, polyest, secur, twin, uniqu, work and is connected with the node 3267 and it is classified as Home & Kitchen, it is the target node.
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

- ID: 19140
- Title: Lehigh 540W 230-Feet Polypropylene Heavy Duty Twine, Brown
- True class (canonical `y`): **Office Products**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Arts, Crafts & Sewing**
- Prediction recorded by this method's pipeline: **Arts, Crafts & Sewing**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Lehigh 540W 230-Feet Polypropylene Heavy Duty Twine, Brown. Content: Secure line by Lehigh twisted polypropylene twine. Great for hobbies, recycling, crafts, handyman work, kitchen, gardening, general household or commercial use. Durable sisal substitute. Polypropylene and polyester construction. Easy on the hands. Unique overwrap offers customers a dispensing feature that keeps twin clean and tangle free. Available in brown color. Measures 230-Feet length.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 3267 | Arts, Crafts & Sewing | Darice 5-Ply Craft Designer Jute, Natural |

### 2-hop (shortest distance exactly 2): 4 nodes

| node id | true class | title |
|---|---|---|
| 339 | Arts, Crafts & Sewing | Darice 0500-04 Wood Beads, Large, Assorted Color |
| 19137 | Office Products | Darice 135-Feet 4 Ply Jute, 1-Pound |
| 19138 | Arts, Crafts & Sewing | Hemtique Cord Spool 20-Pound, Dark Brown |
| 19139 | Arts, Crafts & Sewing | Surgical Steel Earring Earwires Hypoallergenic Shiny Silver Plated Fishhook with 10x3.5mm Ball and Coil with Open Loop, 21 Gauge. 100 Pairs. (200) |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/products/cf-gnnexplainer-canonical/random_seed_42_*` (key=65).

- Factual class: **Arts, Crafts & Sewing**
- Counterfactual class: **Home & Kitchen**
- Removed edges (global ids, 2): (3267, 19137), (3267, 19138)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 19140 |
| Factual_Target_Node_Neighbors | 3267 |
| Factual_Target_Node_Features | use, use, avail, brown, use, clean, color, commerci, construct, use, custom, durabl, duti, easi, featur, feet, use, free, use, gener, great, hand, heavi, use, keep, kitchen, length, line, measur, offer, use, use, use, polyest, use, secur, use, use, use, twin, uniqu, use, use, work |
| Counterfactual_Target_Node_Neighbors | 3267 |
| Counterfactual_Target_Node_Features | use, use, avail, brown, use, clean, color, commerci, construct, use, custom, durabl, duti, easi, featur, feet, use, free, use, gener, great, hand, heavi, use, keep, kitchen, length, line, measur, offer, use, use, use, polyest, use, secur, use, use, use, twin, uniqu, use, use, work |
| Factual_Target_Node_Class | Arts, Crafts & Sewing |
| Counterfactual_Target_Node_class | Home & Kitchen |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 19140 |
| Factual_Target_Node_Neighbors | 3267 |
| Factual_Target_Node_Features | use, use, avail, brown, use, clean, color, commerci, construct, use, custom, durabl, duti, easi, featur, feet, use, free, use, gener, great, hand, heavi, use, keep, kitchen, length, line, measur, offer, use, use, use, polyest, use, secur, use, use, use, twin, uniqu, use, use, work |
| Counterfactual_Target_Node_Neighbors | 3267 |
| Counterfactual_Target_Node_Features | use, use, avail, brown, use, clean, color, commerci, construct, use, custom, durabl, duti, easi, featur, feet, use, free, use, gener, great, hand, heavi, use, keep, kitchen, length, line, measur, offer, use, use, use, polyest, use, secur, use, use, use, twin, uniqu, use, use, work |
| Factual_Target_Node_Class | Arts, Crafts & Sewing |
| Counterfactual_Target_Node_class | Home & Kitchen |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |
