# Reference packet: CF-GNNExplainer__Qwen-14B__products__23324

- Method: CF-GNNExplainer; configuration: Qwen-14B; dataset: products; target node: 23324
- Explanation source: `./robustness_2026-10-30/production_a100/qwen14b_gptq_int4_products_Response.json` ([83][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
To address the task, we need to compare the factual and counterfactual examples provided and identify the differences in the graph structure and node features that led to a change in the classification of the target node. Here’s the filled dictionary based on the provided information:

```python
infos = {
    'Target_Node_ID': '23324',
    'Factual_Target_Node_Neighbors': ['4435'],
    'Factual_Target_Node_Features': ['altern', 'use', 'book', 'avoid', 'base', 'best', 'contain', 'cream', 'design', 'feel', 'femal', 'moistur', 'formula', 'improv', 'includ', 'ingredi', 'like', 'look', 'natur', 'skin', 'perfect', 'power', 'success', 'read', 'varieti', 'women'],
    'Counterfactual_Target_Node_Neighbors': [],
    'Counterfactual_Target_Node_Features': ['altern', 'use', 'book', 'avoid', 'base', 'best', 'contain', 'cream', 'design', 'feel', 'femal', 'moistur', 'formula', 'improv', 'includ', 'ingredi', 'like', 'look', 'natur', 'skin', 'perfect', 'power', 'success', 'read', 'varieti', 'women'],
    'Factual_Target_Node_Class': 'Health & Personal Care',
    'Counterfactual_Target_Node_class': 'Beauty',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Natural_Language_Explanation': 'In the factual scenario, the target node (node 23324) was classified as "Health & Personal Care" and was connected to node 4435. In the counterfactual scenario, the same node is now classified as "Beauty" and has no connections to any other nodes. The change in classification is primarily due to the removal of all connections to neighboring nodes, which altered the context and influence of the target node.'
}
```

### Explanation of Changes

#### Target Node ID: 23324
- **Factual Scenario**: The target node (node 23324) is titled 'Breast Success Cream 2.0 Fl Oz Enhancement Bust Enlargement'. It is classified under "Health & Personal Care" and is connected to node 4435, which is a product titled 'Slim Green Reduce Cream 4 Oz'.
- **Counterfactual Scenario**: The same node retains its title but is now classified under "Beauty". It is disconnected from all other nodes.

#### Neighbors and Connections
- **Factual Scenario**: The only neighbor of the target node is node 4435, which is a product related to body slimming and reduction. This connection suggests that the target node is part of a network of health and personal care products.
- **Counterfactual Scenario**: The target node has no neighbors, indicating a complete isolation from other products.

#### Classification Change
- **Factual Classification**: "Health & Personal Care"
- **Counterfactual Classification**: "Beauty"

#### Influence of Neighbors
- **Factual Scenario**: The connection to node 4435, which is a slimming cream, likely influenced the classification of the target node towards "Health & Personal Care." The shared context of health and personal care products reinforced this classification.
- **Counterfactual Scenario**: Without any connections, the target node loses the contextual support from other health and personal care products. The absence of these connections shifts the classification towards "Beauty," as the product's attributes and title align more closely with beauty products rather than health and personal care products.

### Summary
The primary difference lies in the connectivity of the target node. In the factual scenario, the target node is embedded within a network of health and personal care products, leading to a classification of "Health & Personal Care." In the counterfactual scenario, the target node is isolated, leading to a reclassification as "Beauty." This demonstrates how the context provided by neighboring nodes significantly influences the classification of a node in a graph-based machine learning model.
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
given the factual graph: The node 491 is a product titled 'Yili Balo Hot Chili Body Slimming Gel 85ml' with key attributes: inch, twin, age, one, use, amp, appli, area, arm, time, year, never, bodi, bottl, children, condit, cool, cream, date, differ, take, want, doubl, dri, extract, feel, find, food, gel, good, heat, hot, ingredi, intend, keep, let, like, look, main, massag, medic, minut, make, natur, oil, text, per, place, prevent, manufactur, reach, result, see, sens, short, skin, slim, smooth, soft, storag, tight, much, treat, well, water and is connected with the node 4435 and it is classified as Health & Personal Care, it is not the target node. The node 492 is a product titled 'missing' with key attributes: use, bodi, cell, fat, gel, help, miss, natur, plu, reduc, way and is connected with the nodes 4435, 4444 and it is classified as Health & Personal Care, it is not the target node. The node 4344 is a product titled 'Hot Chili Balo Cream 85ml + Coffee Yili Balo Cream 85ml' with key attributes: inch, one, use, appli, area, arm, time, bodi, cream, differ, take, want, doubl, extract, feel, heat, hot, ingredi, let, like, look, main, massag, minut, make, natur, oil, year, per, result, see, sens, short, skin, slim, smooth, soft, tight, much, well, water and is connected with the node 4435 and it is classified as Health & Personal Care, it is not the target node. The node 4345 is a product titled 'Aokdis Plastic Weight Loss Weight Waist Leg Thigh Sauna Slimming Wrap Burn Cellulite Fat Belt Wrap' with key attributes: use, belt, fat, loss, packag, retail, plastic, weight, without, wrap and is connected with the node 4435 and it is classified as Health & Personal Care, it is not the target node. The node 4435 is a product titled 'Slim Green Reduce Cream 4 Oz' with key attributes: click, add, use, amount, appli, area, arm, around, never, blend, bodi, button, cover, cream, feel, food, gel, get, green, leg, manufactur, massag, may, natur, year, one, skin, sheet, plastic, reduc, right, simpli, slim, start, stori, usa, without, wrap and is connected with the nodes 491, 492, 4344, 4345, 4444, 23111, 23161, 23323, 23324, 23325 and it is classified as Health & Personal Care, it is not the target node. The node 4444 is a product titled '"L'eudine Redugel Excessive Body Fat Burner Reducer"' with key attributes: alwaysshowplaceholdertext, activ, year, use, anti, appli, approxim, area, well, bath, bodi, cell, clean, complet, compon, day, deep, take, dri, energi, exercis, extract, fat, gel, goe, help, hour, want, immedi, one, massag, oil, properti, recommend, reduc, releas, second, skin, stop, target, stori, work and is connected with the nodes 492, 4435 and it is classified as Health & Personal Care, it is not the target node. The node 23111 is a product titled 'Ultimate Body Wrap Lipo Applicator Wrap. 2 Wraps' with key attributes: amaz, use, applic, appli, bodi, diseas, either, function, intend, like, minut, make, one, also, prevent, process, program, result, simpl, structur, take, year, treat, tri, ultim, wrap, check and is connected with the node 4435 and it is classified as Health & Personal Care, it is not the target node. The node 23161 is a product titled 'PINALIM TEA/TE PINALIM - PINNEAPPLE, FLAX, GREEN TEA, RED TEA AND WHITE TEA' with key attributes: add, one, use, book, base, benefit, bring, buy, compani, design, diet, take, like, enhanc, even, exercis, famou, green, hard, help, lose, loss, year, origin, pound, red, right, start, success, supplement, tea, make, read, today, version, first, weight, know, white and is connected with the node 4435 and it is classified as Health & Personal Care, it is not the target node. The node 23323 is a product titled 'It Works! Defining Gel. Slimming Gel. Body Defining Gel by It Works! 0.5 oz sample size.' with key attributes: use, appear, area, arm, well, back, bodi, care, design, favorit, gel, great, help, leg, meet, neck, one, qualiti, skin, result, size, mani, ultim, provid, work and is connected with the node 4435 and it is classified as Health & Personal Care, it is not the target node. The node 23324 is a product titled 'Breast Success Cream 2.0 Fl Oz Enhancement Bust Enlargement' with key attributes: altern, use, book, avoid, base, best, contain, cream, design, feel, femal, moistur, formula, improv, includ, ingredi, like, look, natur, skin, perfect, power, success, read, varieti, women and is connected with the node 4435 and it is classified as Health & Personal Care, it is the target node. The node 23325 is a product titled '21st Century Slimming Tea, Green Tea, 24 Count (Pack of 3)' with key attributes: made, hour, achiev, use, blend, centuri, count, delici, green, help, light, loss, natur, pack, provid, result, tea, weight, also and is connected with the node 4435 and it is classified as Health & Personal Care, it is not the target node. and given the counterfactual example: The node 491 is a product titled 'Yili Balo Hot Chili Body Slimming Gel 85ml' with key attributes: inch, twin, age, one, use, amp, appli, area, arm, time, year, never, bodi, bottl, children, condit, cool, cream, date, differ, take, want, doubl, dri, extract, feel, find, food, gel, good, heat, hot, ingredi, intend, keep, let, like, look, main, massag, medic, minut, make, natur, oil, text, per, place, prevent, manufactur, reach, result, see, sens, short, skin, slim, smooth, soft, storag, tight, much, treat, well, water and is connected with the node 4435 and it is classified as Health & Personal Care, it is not the target node. The node 492 is a product titled 'missing' with key attributes: use, bodi, cell, fat, gel, help, miss, natur, plu, reduc, way and is connected with the nodes 4435, 4444 and it is classified as Health & Personal Care, it is not the target node. The node 4344 is a product titled 'Hot Chili Balo Cream 85ml + Coffee Yili Balo Cream 85ml' with key attributes: inch, one, use, appli, area, arm, time, bodi, cream, differ, take, want, doubl, extract, feel, heat, hot, ingredi, let, like, look, main, massag, minut, make, natur, oil, year, per, result, see, sens, short, skin, slim, smooth, soft, tight, much, well, water and is connected with the node 4435 and it is classified as Health & Personal Care, it is not the target node. The node 4345 is a product titled 'Aokdis Plastic Weight Loss Weight Waist Leg Thigh Sauna Slimming Wrap Burn Cellulite Fat Belt Wrap' with key attributes: use, belt, fat, loss, packag, retail, plastic, weight, without, wrap and is connected with the node 4435 and it is classified as Health & Personal Care, it is not the target node. The node 4435 is a product titled 'Slim Green Reduce Cream 4 Oz' with key attributes: click, add, use, amount, appli, area, arm, around, never, blend, bodi, button, cover, cream, feel, food, gel, get, green, leg, manufactur, massag, may, natur, year, one, skin, sheet, plastic, reduc, right, simpli, slim, start, stori, usa, without, wrap and is connected with the nodes 491, 492, 4344, 4345, 4444, 23111, 23161, 23323, 23325 and it is classified as Health & Personal Care, it is not the target node. The node 4444 is a product titled '"L'eudine Redugel Excessive Body Fat Burner Reducer"' with key attributes: alwaysshowplaceholdertext, activ, year, use, anti, appli, approxim, area, well, bath, bodi, cell, clean, complet, compon, day, deep, take, dri, energi, exercis, extract, fat, gel, goe, help, hour, want, immedi, one, massag, oil, properti, recommend, reduc, releas, second, skin, stop, target, stori, work and is connected with the nodes 492, 4435 and it is classified as Health & Personal Care, it is not the target node. The node 23111 is a product titled 'Ultimate Body Wrap Lipo Applicator Wrap. 2 Wraps' with key attributes: amaz, use, applic, appli, bodi, diseas, either, function, intend, like, minut, make, one, also, prevent, process, program, result, simpl, structur, take, year, treat, tri, ultim, wrap, check and is connected with the node 4435 and it is classified as Health & Personal Care, it is not the target node. The node 23161 is a product titled 'PINALIM TEA/TE PINALIM - PINNEAPPLE, FLAX, GREEN TEA, RED TEA AND WHITE TEA' with key attributes: add, one, use, book, base, benefit, bring, buy, compani, design, diet, take, like, enhanc, even, exercis, famou, green, hard, help, lose, loss, year, origin, pound, red, right, start, success, supplement, tea, make, read, today, version, first, weight, know, white and is connected with the node 4435 and it is classified as Health & Personal Care, it is not the target node. The node 23323 is a product titled 'It Works! Defining Gel. Slimming Gel. Body Defining Gel by It Works! 0.5 oz sample size.' with key attributes: use, appear, area, arm, well, back, bodi, care, design, favorit, gel, great, help, leg, meet, neck, one, qualiti, skin, result, size, mani, ultim, provid, work and is connected with the node 4435 and it is classified as Health & Personal Care, it is not the target node. The node 23324 is a product titled 'Breast Success Cream 2.0 Fl Oz Enhancement Bust Enlargement' with key attributes: altern, use, book, avoid, base, best, contain, cream, design, feel, femal, moistur, formula, improv, includ, ingredi, like, look, natur, skin, perfect, power, success, read, varieti, women and is connected with no other nodes and it is classified as Beauty, it is the target node. The node 23325 is a product titled '21st Century Slimming Tea, Green Tea, 24 Count (Pack of 3)' with key attributes: made, hour, achiev, use, blend, centuri, count, delici, green, help, light, loss, natur, pack, provid, result, tea, weight, also and is connected with the node 4435 and it is classified as Health & Personal Care, it is not the target node.
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

- ID: 23324
- Title: Breast Success Cream 2.0 Fl Oz Enhancement Bust Enlargement
- True class (canonical `y`): **Clothing, Shoes & Jewelry**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Health & Personal Care**
- Prediction recorded by this method's pipeline: **Health & Personal Care**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Breast Success Cream 2.0 Fl Oz Enhancement Bust Enlargement. Content: Breast Success Cream is a cream-based topical breast enhancement formula designed just for women. This product contains a variety of ingredients including Volufiline and Biobustyle designed for powerful female enhancement. Breast Success Cream is a perfect complement to Breast Success pills or can be used an alternative for those wanting to avoid expensive and dangerous surgery. Feel the sensuality of natural enhancement and improve your confidence by looking and feeling your best
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 4435 | Health & Personal Care | Slim Green Reduce Cream 4 Oz |

### 2-hop (shortest distance exactly 2): 9 nodes

| node id | true class | title |
|---|---|---|
| 491 | Beauty | Yili Balo Hot Chili Body Slimming Gel 85ml |
| 492 | label 25 | missing |
| 4344 | Beauty | Hot Chili Balo Cream 85ml + Coffee Yili Balo Cream 85ml |
| 4345 | Clothing, Shoes & Jewelry | Aokdis Plastic Weight Loss Weight Waist Leg Thigh Sauna Slimming Wrap Burn Cellulite Fat Belt Wrap |
| 4444 | Health & Personal Care | "L'eudine Redugel Excessive Body Fat Burner Reducer" |
| 23111 | Health & Personal Care | Ultimate Body Wrap Lipo Applicator Wrap. 2 Wraps |
| 23161 | Grocery & Gourmet Food | PINALIM TEA/TE PINALIM - PINNEAPPLE, FLAX, GREEN TEA, RED TEA AND WHITE TEA |
| 23323 | Health & Personal Care | It Works! Defining Gel. Slimming Gel. Body Defining Gel by It Works! 0.5 oz sample size. |
| 23325 | Health & Personal Care | 21st Century Slimming Tea, Green Tea, 24 Count (Pack of 3) |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/products/cf-gnnexplainer-canonical/random_seed_42_*` (key=83).

- Factual class: **Health & Personal Care**
- Counterfactual class: **Beauty**
- Removed edges (global ids, 1): (4435, 23324)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 23324 |
| Factual_Target_Node_Neighbors | 4435 |
| Factual_Target_Node_Features | altern, use, book, use, avoid, base, use, best, use, use, contain, use, cream, design, feel, feel, femal, moistur, use, formula, use, improv, includ, ingredi, use, like, look, natur, use, use, skin, perfect, use, power, use, success, use, use, read, use, use, use, varieti, use, women, use |
| Counterfactual_Target_Node_Neighbors |  |
| Counterfactual_Target_Node_Features | altern, use, book, use, avoid, base, use, best, use, use, contain, use, cream, design, feel, feel, femal, moistur, use, formula, use, improv, includ, ingredi, use, like, look, natur, use, use, skin, perfect, use, power, use, success, use, use, read, use, use, use, varieti, use, women, use |
| Factual_Target_Node_Class | Health & Personal Care |
| Counterfactual_Target_Node_class | Beauty |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 4435 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 23324 |
| Factual_Target_Node_Neighbors | 4435 |
| Factual_Target_Node_Features | altern, use, book, use, avoid, base, use, best, use, use, contain, use, cream, design, feel, feel, femal, moistur, use, formula, use, improv, includ, ingredi, use, like, look, natur, use, use, skin, perfect, use, power, use, success, use, use, read, use, use, use, varieti, use, women, use |
| Counterfactual_Target_Node_Neighbors |  |
| Counterfactual_Target_Node_Features | altern, use, book, use, avoid, base, use, best, use, use, contain, use, cream, design, feel, feel, femal, moistur, use, formula, use, improv, includ, ingredi, use, like, look, natur, use, use, skin, perfect, use, power, use, success, use, use, read, use, use, use, varieti, use, women, use |
| Factual_Target_Node_Class | Health & Personal Care |
| Counterfactual_Target_Node_class | Beauty |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 4435 |
| Natural_Language_Explanation | None |
