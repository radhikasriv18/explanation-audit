# Reference packet: CF-GNNExplainer__Llama-8B__products__30739

- Method: CF-GNNExplainer; configuration: Llama-8B; dataset: products; target node: 30739
- Explanation source: `./llm-graph-cf/data/results/cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_products_standard_Response.json` ([115][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, we can fill the dictionary as follows:

infos = {
    'Target_Node_ID': 30739,
    'Factual_Target_Node_Neighbors': [763, 30740, 30741, 30742],
    'Factual_Target_Node_Features': ['use', 'build', 'citi', 'new', 'print', 'state', 'york'],
    'Counterfactual_Target_Node_Neighbors': [30739],
    'Counterfactual_Target_Node_Features': ['use', 'build', 'citi', 'new', 'print', 'state', 'york'],
    'Factual_Target_Node_Class': 'Home & Kitchen',
    'Counterfactual_Target_Node_class': 'Toys & Games',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': ['Home & Kitchen', 'Toys & Games'],
    'Natural_Language_Explanation': 'The target node 30739 was classified as Home & Kitchen in the factual scenario but as Toys & Games in the counterfactual scenario. This change in classification can be attributed to the change in the classification of node 6577 from Home & Kitchen to Toys & Games in the counterfactual scenario. The neighbors of the target node, including 763, 30740, 30741, and 30742, did not change their classification, but their connections to the target node influenced the change in classification.'
}

The change in classification for the target node 30739 can be explained by the change in the classification of node 6577 from Home & Kitchen to Toys & Games in the counterfactual scenario. This change in classification is likely due to the influence of the neighbors of the target node, which remained the same in both scenarios.

In the factual scenario, the target node 30739 was classified as Home & Kitchen because it was connected to node 6577, which was also classified as Home & Kitchen. However, in the counterfactual scenario, node 6577 was classified as Toys & Games, which influenced the target node 30739 to be classified as Toys & Games as well.

The neighbors of the target node, including 763, 30740, 30741, and 30742, did not change their classification, but their connections to the target node influenced the change in classification. For example, node 763, which was connected to the target node in both scenarios, was classified as Home & Kitchen in the factual scenario but as Toys & Games in the counterfactual scenario. This suggests that the classification of node 763 was influenced by the change in classification of node 6577.

Overall, the change in classification for the target node 30739 can be attributed to the change in the classification of node 6577 and the influence of the neighbors of the target node.
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
given the factual graph: The node 763 is a product titled 'Times Square Metal Subway Sign , 17x11' with key attributes: use, enhanc, help, high, hundr, interior, item, like, match, metal, one, stori, manufactur, qualiti, squar, style, time, uniqu, wall and is connected with the node 6577 and it is classified as Home & Kitchen, it is not the target node. The node 6577 is a product titled 'DESIGN IDEAS New York Doodles Destinations City Map Beverage Napkins' with key attributes: year, use, citi, design, one, featur, idea, new, pack, sheet, plastic, qualiti, set, york and is connected with the nodes 763, 30739, 30740, 30741, 30742 and it is classified as Home & Kitchen, it is not the target node. The node 30739 is a product titled 'New York City Empire State Building (NYC) Decorative Photography Poster Print 12x36' with key attributes: use, build, citi, new, print, state, york and is connected with the node 6577 and it is classified as Home & Kitchen, it is the target node. The node 30740 is a product titled 'missing' with key attributes: use, button, diamet, inch, love, miss, new, pin, rare and is connected with the node 6577 and it is classified as Home & Kitchen, it is not the target node. The node 30741 is a product titled 'Paperproducts Design 20-Pack Wine Cellar Paper Cocktail Napkins' with key attributes: inch, year, per, accessori, addit, one, also, use, art, well, beauti, best, bring, busi, california, collect, creat, design, develop, entertain, fashion, featur, fun, gift, take, licens, line, offer, pack, sheet, perfect, plate, readi, set, sinc, style, tabl, togeth, top, truli, ultim, vivid, first and is connected with the node 6577 and it is classified as Home & Kitchen, it is not the target node. The node 30742 is a product titled 'True Wine Stain Cocktail Napkins' with key attributes: book, never, use, design, take, true, uniqu, make, worri and is connected with the node 6577 and it is classified as Toys & Games, it is not the target node. and given the counterfactual example: The node 763 is a product titled 'Times Square Metal Subway Sign , 17x11' with key attributes: use, enhanc, help, high, hundr, interior, item, like, match, metal, one, stori, manufactur, qualiti, squar, style, time, uniqu, wall and is connected with no other nodes and it is classified as Home & Kitchen, it is not the target node. The node 6577 is a product titled 'DESIGN IDEAS New York Doodles Destinations City Map Beverage Napkins' with key attributes: year, use, citi, design, one, featur, idea, new, pack, sheet, plastic, qualiti, set, york and is connected with the nodes 30739, 30740, 30741, 30742 and it is classified as Toys & Games, it is not the target node. The node 30739 is a product titled 'New York City Empire State Building (NYC) Decorative Photography Poster Print 12x36' with key attributes: use, build, citi, new, print, state, york and is connected with the node 6577 and it is classified as Toys & Games, it is the target node. The node 30740 is a product titled 'missing' with key attributes: use, button, diamet, inch, love, miss, new, pin, rare and is connected with the node 6577 and it is classified as Toys & Games, it is not the target node. The node 30741 is a product titled 'Paperproducts Design 20-Pack Wine Cellar Paper Cocktail Napkins' with key attributes: inch, year, per, accessori, addit, one, also, use, art, well, beauti, best, bring, busi, california, collect, creat, design, develop, entertain, fashion, featur, fun, gift, take, licens, line, offer, pack, sheet, perfect, plate, readi, set, sinc, style, tabl, togeth, top, truli, ultim, vivid, first and is connected with the node 6577 and it is classified as Toys & Games, it is not the target node. The node 30742 is a product titled 'True Wine Stain Cocktail Napkins' with key attributes: book, never, use, design, take, true, uniqu, make, worri and is connected with the node 6577 and it is classified as Toys & Games, it is not the target node.
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

- ID: 30739
- Title: New York City Empire State Building (NYC) Decorative Photography Poster Print 12x36
- True class (canonical `y`): **Home & Kitchen**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Home & Kitchen**
- Prediction recorded by this method's pipeline: **Home & Kitchen**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: New York City Empire State Building (NYC) Decorative Photography Poster Print 12x36. Content: Photography poster of The Empire State Building.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 6577 | Home & Kitchen | DESIGN IDEAS New York Doodles Destinations City Map Beverage Napkins |

### 2-hop (shortest distance exactly 2): 4 nodes

| node id | true class | title |
|---|---|---|
| 763 | Home & Kitchen | Times Square Metal Subway Sign , 17x11 |
| 30740 | label 25 | missing |
| 30741 | Health & Personal Care | Paperproducts Design 20-Pack Wine Cellar Paper Cocktail Napkins |
| 30742 | Home & Kitchen | True Wine Stain Cocktail Napkins |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/products/cf-gnnexplainer-canonical/random_seed_42_*` (key=115).

- Factual class: **Home & Kitchen**
- Counterfactual class: **Toys & Games**
- Removed edges (global ids, 1): (763, 6577)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 30739 |
| Factual_Target_Node_Neighbors | 6577 |
| Factual_Target_Node_Features | use, use, build, citi, use, use, new, use, use, print, use, state, use, use, use, york |
| Counterfactual_Target_Node_Neighbors | 6577 |
| Counterfactual_Target_Node_Features | use, use, build, citi, use, use, new, use, use, print, use, state, use, use, use, york |
| Factual_Target_Node_Class | Home & Kitchen |
| Counterfactual_Target_Node_class | Toys & Games |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 30739 |
| Factual_Target_Node_Neighbors | 6577 |
| Factual_Target_Node_Features | use, use, build, citi, use, use, new, use, use, print, use, state, use, use, use, york |
| Counterfactual_Target_Node_Neighbors | 6577 |
| Counterfactual_Target_Node_Features | use, use, build, citi, use, use, new, use, use, print, use, state, use, use, use, york |
| Factual_Target_Node_Class | Home & Kitchen |
| Counterfactual_Target_Node_class | Toys & Games |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |
