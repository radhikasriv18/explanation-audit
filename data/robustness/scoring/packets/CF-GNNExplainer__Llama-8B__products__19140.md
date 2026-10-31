# Reference packet: CF-GNNExplainer__Llama-8B__products__19140

- Method: CF-GNNExplainer; configuration: Llama-8B; dataset: products; target node: 19140
- Explanation source: `./llm-graph-cf/data/results/cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_products_standard_Response.json` ([65][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, we can fill in the dictionary as follows:

infos = {
    'Target_Node_ID': '19140',
    'Factual_Target_Node_Neighbors': ['339', '3267'],
    'Factual_Target_Node_Features': ['use', 'avail', 'brown', 'clean', 'color', 'commerci', 'construct', 'custom', 'durabl', 'duti', 'easi', 'featur', 'feet', 'free', 'gener', 'great', 'hand', 'heavi', 'keep', 'kitchen', 'length', 'line', 'measur', 'offer', 'polyest', 'secur', 'twin', 'uniqu', 'work'],
    'Counterfactual_Target_Node_Neighbors': ['339', '3267', '19139'],
    'Counterfactual_Target_Node_Features': ['use', 'avail', 'brown', 'clean', 'color', 'commerci', 'construct', 'custom', 'durabl', 'duti', 'easi', 'featur', 'feet', 'free', 'gener', 'great', 'hand', 'heavi', 'keep', 'kitchen', 'length', 'line', 'measur', 'offer', 'polyest', 'secur', 'twin', 'uniqu', 'work'],
    'Factual_Target_Node_Class': 'Arts, Crafts & Sewing',
    'Counterfactual_Target_Node_class': 'Home & Kitchen',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': ['kitchen'],
    'Natural_Language_Explanation': 'The target node 19140 was classified as Arts, Crafts & Sewing in the factual scenario but as Home & Kitchen in the counterfactual scenario. This change in classification can be attributed to the addition of the neighbor node 19139, which is a product related to Home & Kitchen. The presence of this node in the counterfactual scenario influenced the classification of the target node, shifting it from Arts, Crafts & Sewing to Home & Kitchen.'
}

The change in classification for the target node 19140 can be explained by the influence of the neighbor node 19139, which is a product related to Home & Kitchen. In the counterfactual scenario, the addition of this node to the neighborhood of the target node led to a change in its classification from Arts, Crafts & Sewing to Home & Kitchen. This suggests that the model is sensitive to the local structure of the graph and can be influenced by the presence or absence of specific nodes in the neighborhood.

The features that changed from the factual to the counterfactual scenario are 'kitchen', which is a key attribute related to the Home & Kitchen category. This change in features contributed to the shift in classification, highlighting the importance of considering the local graph structure and node features when interpreting the behavior of graph neural networks.

In terms of the influences of neighbor nodes, the addition of node 19139 to the neighborhood of the target node 19140 had a significant impact on its classification. This suggests that the model is using the local structure of the graph to inform its predictions, and that the presence or absence of specific nodes can influence the outcome.
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
