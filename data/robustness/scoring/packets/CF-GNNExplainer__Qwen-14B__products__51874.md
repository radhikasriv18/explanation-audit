# Reference packet: CF-GNNExplainer__Qwen-14B__products__51874

- Method: CF-GNNExplainer; configuration: Qwen-14B; dataset: products; target node: 51874
- Explanation source: `./robustness_2026-10-30/production_a100/qwen14b_gptq_int4_products_Response.json` ([193][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
To address the provided scenario, we will fill the `infos` dictionary based on the differences observed between the factual and counterfactual graphs, and then provide a natural language explanation for the change in classification.

### Filling the Dictionary

```python
infos = {
    'Target_Node_ID': '51874',
    'Factual_Target_Node_Neighbors': ['12727'],
    'Factual_Target_Node_Features': ['use', 'miner', 'plu', 'pure', 'super', 'supplement'],
    'Counterfactual_Target_Node_Neighbors': ['12727'],
    'Counterfactual_Target_Node_Features': ['use', 'miner', 'plu', 'pure', 'super', 'supplement'],
    'Factual_Target_Node_Class': 'Books',
    'Counterfactual_Target_Node_class': 'Health & Personal Care',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Natural_Language_Explanation': ''
}
```

### Explanation of Changes

In the factual graph, the target node (node 51874) titled "Pure Essence Labs Ionic-Fizz Super D-K Calcium Plus Mineral Supplement" is classified as "Books". In the counterfactual graph, the same node is reclassified as "Health & Personal Care".

#### Key Differences:

1. **Node Connections**:
   - In the factual graph, node 51874 is connected only to node 12727 ("Staying Healthy With the Seasons").
   - In the counterfactual graph, node 51874 remains connected to node 12727 but loses connections to nodes 51875, 51876, and 51877. Node 12727 itself loses connections to nodes 51875, 51876, and 51877.

2. **Classification Change**:
   - The target node's classification shifts from "Books" to "Health & Personal Care".
   - This shift is likely influenced by the removal of connections to nodes that are classified as "Books", such as nodes 51875, 51876, and 51877.

3. **Neighbor Influence**:
   - In the factual graph, node 12727 ("Staying Healthy With the Seasons") is classified as "Books" and is connected to multiple other nodes classified as "Books".
   - In the counterfactual graph, node 12727 still retains its classification as "Books" but has fewer connections, which may indirectly influence the classification of node 51874.
   - The loss of connections to nodes 51875, 51876, and 51877, which are all classified as "Books," reduces the overall "Books" influence on node 51874.

### Natural Language Explanation

The target node (node 51874) titled "Pure Essence Labs Ionic-Fizz Super D-K Calcium Plus Mineral Supplement" was initially classified as "Books" in the factual graph. However, in the counterfactual graph, it is reclassified as "Health & Personal Care." This change is primarily due to the alteration in the graph structure, specifically the removal of connections to nodes 51875, 51876, and 51877, which were previously classified as "Books." These nodes were influencing the classification of node 51874 towards "Books." By removing these connections, the model now considers fewer "Books" nodes in its vicinity, leading to a more appropriate classification under "Health & Personal Care."

Thus, the natural language explanation for the dictionary is:

```python
infos['Natural_Language_Explanation'] = "The target node (node 51874) was initially classified as 'Books'. In the counterfactual graph, it is reclassified as 'Health & Personal Care' due to the removal of connections to nodes 51875, 51876, and 51877, which were previously classified as 'Books'. This change reflects a more accurate representation of the product's category."
```

This explanation captures the essence of how the graph structure influences the classification of the target node, highlighting the importance of neighboring nodes in determining the final classification.
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
given the factual graph: The node 1544 is a product titled 'The Encyclopedia of Natural Medicine Third Edition' with key attributes: publish, use, book, well, author, professor, edit, editor, food, founder, heal, health, industri, lead, live, medic, medicin, michael, make, natur, nutrit, presid, state, mani, teach, year, third, univers, washington, world and is connected with the node 12727 and it is classified as Books, it is not the target node. The node 12717 is a product titled 'Encyclopedia of Healing Foods' with key attributes: glock, also, use, book, well, time, author, professor, develop, director, editor, educ, experi, firm, first, food, heal, health, includ, industri, medic, medicin, michael, make, natur, serv, state, year, twenti, unit, univers, world, writer and is connected with the node 12727 and it is classified as Books, it is not the target node. The node 12727 is a product titled 'Staying Healthy With the Seasons' with key attributes: use, author, bodi, book, classic, professor, field, heal, health, healthi, help, instead, kind, medicin, michael, natur, offer, one, pleas, well, within and is connected with the nodes 1544, 12717, 51874, 51875, 51876, 51877 and it is classified as Books, it is not the target node. The node 51874 is a product titled 'Pure Essence Labs Ionic-Fizz Super D-K Calcium Plus Mineral Supplement, Raspberry, Lemonade, 420 Gram' with key attributes: use, miner, plu, pure, super, supplement and is connected with the node 12727 and it is classified as Books, it is the target node. The node 51875 is a product titled 'A Practical Guide to Acu-points' with key attributes: use, author, book, complet, guid, institut, live, medicin, point, practic, therapi and is connected with the node 12727 and it is classified as Books, it is not the target node. The node 51876 is a product titled '"The Herbalist's Way: The Art and Practice of Healing with Plant Medicines"' with key attributes: prais, never, use, art, becom, book, classic, creat, depth, peopl, field, friend, one, heal, much, inner, like, michael, old, also, plant, practic, rare, special, studi, mani, first, read, take, way, work and is connected with the node 12727 and it is classified as Books, it is not the target node. The node 51877 is a product titled 'Integrative Nutrition' with key attributes: access, one, use, book, approach, art, well, time, author, balanc, basic, career, comprehens, differ, eat, energi, engag, everyon, extrem, find, workout, food, good, growth, health, healthi, help, interest, look, love, make, mother, must, nutrit, peopl, person, popular, practic, textbook, read, recommend, scienc, sens, simpli, stori, mani, way, women and is connected with the node 12727 and it is classified as Books, it is not the target node. and given the counterfactual example: The node 1544 is a product titled 'The Encyclopedia of Natural Medicine Third Edition' with key attributes: publish, use, book, well, author, professor, edit, editor, food, founder, heal, health, industri, lead, live, medic, medicin, michael, make, natur, nutrit, presid, state, mani, teach, year, third, univers, washington, world and is connected with the node 12727 and it is classified as Books, it is not the target node. The node 12717 is a product titled 'Encyclopedia of Healing Foods' with key attributes: glock, also, use, book, well, time, author, professor, develop, director, editor, educ, experi, firm, first, food, heal, health, includ, industri, medic, medicin, michael, make, natur, serv, state, year, twenti, unit, univers, world, writer and is connected with no other nodes and it is classified as Books, it is not the target node. The node 12727 is a product titled 'Staying Healthy With the Seasons' with key attributes: use, author, bodi, book, classic, professor, field, heal, health, healthi, help, instead, kind, medicin, michael, natur, offer, one, pleas, well, within and is connected with the nodes 1544, 51874, 51875, 51876 and it is classified as Books, it is not the target node. The node 51874 is a product titled 'Pure Essence Labs Ionic-Fizz Super D-K Calcium Plus Mineral Supplement, Raspberry, Lemonade, 420 Gram' with key attributes: use, miner, plu, pure, super, supplement and is connected with the node 12727 and it is classified as Health & Personal Care, it is the target node. The node 51875 is a product titled 'A Practical Guide to Acu-points' with key attributes: use, author, book, complet, guid, institut, live, medicin, point, practic, therapi and is connected with the node 12727 and it is classified as Books, it is not the target node. The node 51876 is a product titled '"The Herbalist's Way: The Art and Practice of Healing with Plant Medicines"' with key attributes: prais, never, use, art, becom, book, classic, creat, depth, peopl, field, friend, one, heal, much, inner, like, michael, old, also, plant, practic, rare, special, studi, mani, first, read, take, way, work and is connected with the node 12727 and it is classified as Books, it is not the target node. The node 51877 is a product titled 'Integrative Nutrition' with key attributes: access, one, use, book, approach, art, well, time, author, balanc, basic, career, comprehens, differ, eat, energi, engag, everyon, extrem, find, workout, food, good, growth, health, healthi, help, interest, look, love, make, mother, must, nutrit, peopl, person, popular, practic, textbook, read, recommend, scienc, sens, simpli, stori, mani, way, women and is connected with no other nodes and it is classified as Books, it is not the target node.
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

- ID: 51874
- Title: Pure Essence Labs Ionic-Fizz Super D-K Calcium Plus Mineral Supplement, Raspberry, Lemonade, 420 Gram
- True class (canonical `y`): **Health & Personal Care**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Books**
- Prediction recorded by this method's pipeline: **Books**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Pure Essence Labs Ionic-Fizz Super D-K Calcium Plus Mineral Supplement, Raspberry, Lemonade, 420 Gram. Content: Ionic-Fizz Super D-K Calcium Plus - Raspberry Lemonade
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 12727 | Books | Staying Healthy With the Seasons |

### 2-hop (shortest distance exactly 2): 5 nodes

| node id | true class | title |
|---|---|---|
| 1544 | Books | The Encyclopedia of Natural Medicine Third Edition |
| 12717 | Books | Encyclopedia of Healing Foods |
| 51875 | Books | A Practical Guide to Acu-points |
| 51876 | Books | "The Herbalist's Way: The Art and Practice of Healing with Plant Medicines" |
| 51877 | Books | Integrative Nutrition |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/products/cf-gnnexplainer-canonical/random_seed_42_*` (key=193).

- Factual class: **Books**
- Counterfactual class: **Health & Personal Care**
- Removed edges (global ids, 2): (12717, 12727), (12727, 51877)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 51874 |
| Factual_Target_Node_Neighbors | 12727 |
| Factual_Target_Node_Features | use, use, use, use, miner, use, plu, use, pure, super, supplement, use, use |
| Counterfactual_Target_Node_Neighbors | 12727 |
| Counterfactual_Target_Node_Features | use, use, use, use, miner, use, plu, use, pure, super, supplement, use, use |
| Factual_Target_Node_Class | Books |
| Counterfactual_Target_Node_class | Health & Personal Care |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 51874 |
| Factual_Target_Node_Neighbors | 12727 |
| Factual_Target_Node_Features | use, use, use, use, miner, use, plu, use, pure, super, supplement, use, use |
| Counterfactual_Target_Node_Neighbors | 12727 |
| Counterfactual_Target_Node_Features | use, use, use, use, miner, use, plu, use, pure, super, supplement, use, use |
| Factual_Target_Node_Class | Books |
| Counterfactual_Target_Node_class | Health & Personal Care |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |
