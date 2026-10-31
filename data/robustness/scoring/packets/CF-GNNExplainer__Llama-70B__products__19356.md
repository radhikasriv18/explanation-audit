# Reference packet: CF-GNNExplainer__Llama-70B__products__19356

- Method: CF-GNNExplainer; configuration: Llama-70B; dataset: products; target node: 19356
- Explanation source: `./robustness_2026-10-30/llama70b/cf/products/19356.json` (response)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, we can fill the dictionary as follows:

infos = {
    'Target_Node_ID': 19356,
    'Factual_Target_Node_Neighbors': [3315],
    'Factual_Target_Node_Features': ['inch', 'commerci', 'handbookandth', 'one', 'use', 'care', 'construct', 'cut', 'easili', 'high', 'individu', 'knife', 'leav', 'light', 'may', 'model', 'make', 'much', 'offer', 'piec', 'premium', 'project', 'qualiti', 'sheet', 'special', 'strength', 'type', 'water', 'weight', 'wood'],
    'Counterfactual_Target_Node_Neighbors': [3315],
    'Counterfactual_Target_Node_Features': ['inch', 'commerci', 'handbookandth', 'one', 'use', 'care', 'construct', 'cut', 'easili', 'high', 'individu', 'knife', 'leav', 'light', 'may', 'model', 'make', 'much', 'offer', 'piec', 'premium', 'project', 'qualiti', 'sheet', 'special', 'strength', 'type', 'water', 'weight', 'wood'],
    'Factual_Target_Node_Class': 'Arts, Crafts & Sewing',
    'Counterfactual_Target_Node_class': 'Toys & Games',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Node_Differences': [19355, 19357, 19358, 19359],
    'Edge_Differences': [(19355, 3315), (19357, 3315), (19358, 3315), (19359, 3315)],
    'Natural_Language_Explanation': 'The classification of the target node 19356 changed from Arts, Crafts & Sewing to Toys & Games. This change is likely due to the changes in the neighborhood of the node 3315, which is connected to the target node. In the counterfactual example, the nodes 19355, 19357, 19358, and 19359 are no longer connected to the node 3315, which may have influenced the classification of the target node. Additionally, the features of the target node remain the same, suggesting that the change in classification is primarily due to the changes in the graph structure.'
}

Explanation:

The classification of the target node 19356 changed from Arts, Crafts & Sewing to Toys & Games. This change is likely due to the changes in the neighborhood of the node 3315, which is connected to the target node. In the counterfactual example, the nodes 19355, 19357, 19358, and 19359 are no longer connected to the node 3315, which may have influenced the classification of the target node.

The node 19355, which was previously connected to the node 3315, is now disconnected and has a different classification (Beauty). This change may have affected the classification of the target node, as the node 19355 is no longer contributing to the Arts, Crafts & Sewing category.

Similarly, the nodes 19357, 19358, and 19359, which were previously connected to the node 3315, are now disconnected and have different classifications (Arts, Crafts & Sewing, Health & Personal Care, and Arts, Crafts & Sewing, respectively). These changes may have also contributed to the change in classification of the target node.

The features of the target node remain the same, suggesting that the change in classification is primarily due to the changes in the graph structure. The target node's features are still related to balsa sheets and woodworking, but the changes in the neighborhood of the node 3315 have led to a reclassification of the target node into the Toys & Games category.
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
given the factual graph: The node 344 is a product titled 'Loew Cornell 1021178 Woodsies Spring Clothespins, 40 count' with key attributes: temperatur, use, classroom, count, food, great, height, ideal, inch, made, measur, natur, non, parti, project, safe, spring, student, teacher, wood and is connected with the node 3315 and it is classified as Toys & Games, it is not the target node. The node 3315 is a product titled 'Balsa Sheets 1/16 x 6 x 36 (10)' with key attributes: inch, handbookandth, one, use, care, construct, cut, easili, high, individu, knife, leav, light, may, model, make, much, offer, piec, premium, project, qualiti, sheet, special, strength, type, water, weight, wood and is connected with the nodes 344, 19355, 19356, 19357, 19358, 19359 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 19355 is a product titled 'Wood Cement Extra Fast,5/8 oz' with key attributes: one, allow, use, never, book, cut, dri, extra, fast, peopl, formula, formul, half, hot, hour, instruct, maximum, model, ounc, skin, pleas, press, proof, read, second, six, special, strength, strong, surfac, time, togeth, tube, wood and is connected with the node 3315 and it is classified as Toys & Games, it is not the target node. The node 19356 is a product titled 'Balsa Sheets 3/32 x 4 x 36 (15)' with key attributes: inch, commerci, handbookandth, one, use, care, construct, cut, easili, high, individu, knife, leav, light, may, model, make, much, offer, piec, premium, project, qualiti, sheet, special, strength, type, water, weight, wood and is connected with the node 3315 and it is classified as Arts, Crafts & Sewing, it is the target node. The node 19357 is a product titled 'Balsa Strips 1/8 x 1/8 x 36 (36)' with key attributes: handbookandth, one, also, use, america, avail, year, care, cut, easili, even, finest, high, leav, light, perfect, project, sheet, south, special, strength, type, warm, water, weight, wood and is connected with the node 3315 and it is classified as Toys & Games, it is not the target node. The node 19358 is a product titled 'Pitsco Heavy Density Balsa Wood Strips (Pack of 100)' with key attributes: made, use, heavi, none, pack, wood and is connected with the node 3315 and it is classified as Toys & Games, it is not the target node. The node 19359 is a product titled 'Midwest Products Project Woods Balsa &amp; Basswood Strip Economy Bag' with key attributes: handbookandth, one, use, american, amp, art, bag, board, close, craft, cut, foot, high, inch, includ, light, produc, manufactur, project, school, shape, size, south, strength, structur, tight, type, variou, weight, wood and is connected with the node 3315 and it is classified as Arts, Crafts & Sewing, it is not the target node. and given the counterfactual example: The node 344 is a product titled 'Loew Cornell 1021178 Woodsies Spring Clothespins, 40 count' with key attributes: temperatur, use, classroom, count, food, great, height, ideal, inch, made, measur, natur, non, parti, project, safe, spring, student, teacher, wood and is connected with the node 3315 and it is classified as Toys & Games, it is not the target node. The node 3315 is a product titled 'Balsa Sheets 1/16 x 6 x 36 (10)' with key attributes: inch, handbookandth, one, use, care, construct, cut, easili, high, individu, knife, leav, light, may, model, make, much, offer, piec, premium, project, qualiti, sheet, special, strength, type, water, weight, wood and is connected with the nodes 344, 19356 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 19355 is a product titled 'Wood Cement Extra Fast,5/8 oz' with key attributes: one, allow, use, never, book, cut, dri, extra, fast, peopl, formula, formul, half, hot, hour, instruct, maximum, model, ounc, skin, pleas, press, proof, read, second, six, special, strength, strong, surfac, time, togeth, tube, wood and is connected with no other nodes and it is classified as Beauty, it is not the target node. The node 19356 is a product titled 'Balsa Sheets 3/32 x 4 x 36 (15)' with key attributes: inch, commerci, handbookandth, one, use, care, construct, cut, easili, high, individu, knife, leav, light, may, model, make, much, offer, piec, premium, project, qualiti, sheet, special, strength, type, water, weight, wood and is connected with the node 3315 and it is classified as Toys & Games, it is the target node. The node 19357 is a product titled 'Balsa Strips 1/8 x 1/8 x 36 (36)' with key attributes: handbookandth, one, also, use, america, avail, year, care, cut, easili, even, finest, high, leav, light, perfect, project, sheet, south, special, strength, type, warm, water, weight, wood and is connected with no other nodes and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 19358 is a product titled 'Pitsco Heavy Density Balsa Wood Strips (Pack of 100)' with key attributes: made, use, heavi, none, pack, wood and is connected with no other nodes and it is classified as Health & Personal Care, it is not the target node. The node 19359 is a product titled 'Midwest Products Project Woods Balsa &amp; Basswood Strip Economy Bag' with key attributes: handbookandth, one, use, american, amp, art, bag, board, close, craft, cut, foot, high, inch, includ, light, produc, manufactur, project, school, shape, size, south, strength, structur, tight, type, variou, weight, wood and is connected with no other nodes and it is classified as Arts, Crafts & Sewing, it is not the target node.
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

- ID: 19356
- Title: Balsa Sheets 3/32 x 4 x 36 (15)
- True class (canonical `y`): **Arts, Crafts & Sewing**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Arts, Crafts & Sewing**
- Prediction recorded by this method's pipeline: **Arts, Crafts & Sewing**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Balsa Sheets 3/32 x 4 x 36 (15). Content: Midwest Wood offers premium quality wood for the construction of models, doll houses, bazaar crafts and so much more! All sheets and strips are bundled and shrink-wrapped. Each individual piece is UPC coded. Balsa wood is carefully dried in special kilns, reducing the water content to leave a light wood with a high strength to weight ratio. The premier wood for all types of modeling projects, Balsa cuts easily with a hobby knife and may be stained or painted to represent any wood type.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 3315 | Toys & Games | Balsa Sheets 1/16 x 6 x 36 (10) |

### 2-hop (shortest distance exactly 2): 5 nodes

| node id | true class | title |
|---|---|---|
| 344 | Arts, Crafts & Sewing | Loew Cornell 1021178 Woodsies Spring Clothespins, 40 count |
| 19355 | Toys & Games | Wood Cement Extra Fast,5/8 oz |
| 19357 | Toys & Games | Balsa Strips 1/8 x 1/8 x 36 (36) |
| 19358 | Office Products | Pitsco Heavy Density Balsa Wood Strips (Pack of 100) |
| 19359 | Arts, Crafts & Sewing | Midwest Products Project Woods Balsa &amp; Basswood Strip Economy Bag |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/products/cf-gnnexplainer-canonical/random_seed_42_*` (key=66).

- Factual class: **Arts, Crafts & Sewing**
- Counterfactual class: **Toys & Games**
- Removed edges (global ids, 4): (3315, 19355), (3315, 19357), (3315, 19358), (3315, 19359)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 19356 |
| Factual_Target_Node_Neighbors | 3315 |
| Factual_Target_Node_Features | inch, commerci, handbookandth, one, use, use, use, use, use, care, construct, use, cut, one, easili, use, use, high, use, individu, use, knife, leav, light, may, model, make, much, use, offer, use, piec, use, premium, use, project, qualiti, sheet, make, special, strength, use, use, use, type, type, water, weight, use, wood |
| Counterfactual_Target_Node_Neighbors | 3315 |
| Counterfactual_Target_Node_Features | inch, commerci, handbookandth, one, use, use, use, use, use, care, construct, use, cut, one, easili, use, use, high, use, individu, use, knife, leav, light, may, model, make, much, use, offer, use, piec, use, premium, use, project, qualiti, sheet, make, special, strength, use, use, use, type, type, water, weight, use, wood |
| Factual_Target_Node_Class | Arts, Crafts & Sewing |
| Counterfactual_Target_Node_class | Toys & Games |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 19356 |
| Factual_Target_Node_Neighbors | 3315 |
| Factual_Target_Node_Features | inch, commerci, handbookandth, one, use, use, use, use, use, care, construct, use, cut, one, easili, use, use, high, use, individu, use, knife, leav, light, may, model, make, much, use, offer, use, piec, use, premium, use, project, qualiti, sheet, make, special, strength, use, use, use, type, type, water, weight, use, wood |
| Counterfactual_Target_Node_Neighbors | 3315 |
| Counterfactual_Target_Node_Features | inch, commerci, handbookandth, one, use, use, use, use, use, care, construct, use, cut, one, easili, use, use, high, use, individu, use, knife, leav, light, may, model, make, much, use, offer, use, piec, use, premium, use, project, qualiti, sheet, make, special, strength, use, use, use, type, type, water, weight, use, wood |
| Factual_Target_Node_Class | Arts, Crafts & Sewing |
| Counterfactual_Target_Node_class | Toys & Games |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |
