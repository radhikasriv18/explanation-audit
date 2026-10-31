# Reference packet: CF-GNNExplainer__Llama-8B__products__32390

- Method: CF-GNNExplainer; configuration: Llama-8B; dataset: products; target node: 32390
- Explanation source: `./llm-graph-cf/data/results/cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_products_standard_Response.json` ([117][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, we can fill the dictionary as follows:

infos = {
    'Target_Node_ID': 32390,
    'Factual_Target_Node_Neighbors': [7041],
    'Factual_Target_Node_Features': ['dimens', 'inch', 'album', 'use', 'time', 'attent', 'balanc', 'black', 'blade', 'clip', 'close', 'coat', 'dedic', 'deliv', 'design', 'detail', 'want', 'easi', 'edg', 'even', 'featur', 'feel', 'fine', 'follow', 'frame', 'full', 'give', 'handl', 'year', 'knife', 'larger', 'length', 'let', 'littl', 'get', 'lock', 'materi', 'metal', 'mini', 'model', 'overal', 'skin', 'pocket', 'posit', 'size', 'small', 'specif', 'steel', 'style', 'type', 'weight', 'award'],
    'Counterfactual_Target_Node_Neighbors': [],
    'Counterfactual_Target_Node_Features': ['dimens', 'inch', 'album', 'use', 'time', 'attent', 'balanc', 'black', 'blade', 'clip', 'close', 'coat', 'dedic', 'deliv', 'design', 'detail', 'want', 'easi', 'edg', 'even', 'featur', 'feel', 'fine', 'follow', 'frame', 'full', 'give', 'handl', 'year', 'knife', 'larger', 'length', 'let', 'littl', 'get', 'lock', 'materi', 'metal', 'mini', 'model', 'overal', 'skin', 'pocket', 'posit', 'size', 'small', 'specif', 'steel', 'style', 'type', 'weight', 'award'],
    'Factual_Target_Node_Class': 'Home & Kitchen',
    'Counterfactual_Target_Node_class': 'Sports & Outdoors',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Natural_Language_Explanation': ''
}

The target node 32390 is initially classified as 'Home & Kitchen' in the factual graph, but in the counterfactual graph, it is classified as 'Sports & Outdoors'. This change in classification can be attributed to the removal of edges connecting the target node to other nodes in the 'Home & Kitchen' category.

Upon analyzing the neighbors of the target node in the factual graph, we see that it is only connected to node 7041, which is also classified as 'Sports & Outdoors'. However, in the counterfactual graph, the target node has no connections to any other nodes. This suggests that the removal of these connections has led to a change in the target node's classification.

In terms of feature differences, both the factual and counterfactual graphs have the same set of features for the target node. However, the absence of connections to other nodes in the counterfactual graph may have contributed to the change in classification.

To provide a more detailed explanation, we can analyze the influence of neighboring nodes on the target node's classification. In the factual graph, the connection to node 7041 may have reinforced the target node's classification as 'Home & Kitchen', as both nodes share similar characteristics. In contrast, the removal of this connection in the counterfactual graph may have allowed the target node to be influenced by other nodes in the graph, leading to a change in classification.

However, without further analysis of the graph structure and node features, it is difficult to pinpoint the exact reason for the change in classification. A more thorough investigation would require examining the graph's topology and the relationships between nodes to identify the underlying factors contributing to the change.

As for the natural language explanation, it can be generated based on the changes in the graph structure and node features. For instance, "The target node 32390 was initially classified as 'Home & Kitchen' due to its connection to node 7041, which shares similar characteristics. However, in the counterfactual graph, the removal of this connection led to a change in classification to 'Sports & Outdoors', suggesting that the target node's features were influenced by other nodes in the graph."
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
given the factual graph: The node 822 is a product titled 'Gerber 31-001709 Swagger Assisted Opening Clip Knife' with key attributes: inch, use, book, black, blade, carri, clip, coat, day, drop, everi, excel, featur, great, grip, handl, knife, make, new, offer, open, origin, point, provid, quick, surfac, tactic, ultra, version, also and is connected with the node 7041 and it is classified as Sports & Outdoors, it is not the target node. The node 7041 is a product titled 'Gerber LST Folding Knife 22-06009' with key attributes: calib, one, use, back, year, never, deliv, graphic, first, fold, goe, would, handl, book, much, knife, last, lightweight, man, market, materi, name, none, qualiti, text, perform, manufactur, rug, seen, may, synthet, whose and is connected with the nodes 822, 32389, 32390, 32391, 32392, 32393 and it is classified as Sports & Outdoors, it is not the target node. The node 32389 is a product titled 'Case Cutlery 004 Case Executive Lockback Pocket Knife With Stainless Steel Blade   Metal' with key attributes: book, ad, use, american, well, time, warranti, year, blade, brand, case, centuri, choic, close, professor, companion, compani, craft, design, drop, edg, execut, featur, finest, gift, hand, handl, one, hunt, ideal, war, like, key, knife, lead, length, lifetim, limit, lock, make, manufactur, materi, measur, metal, skin, pattern, perfect, pocket, point, premium, rich, ring, sharp, slim, specif, stainless, steel, still, techniqu, tool, weight, world, redistribut, reader, chapter and is connected with the node 7041 and it is classified as Sports & Outdoors, it is not the target node. The node 32390 is a product titled 'Gerber Paraframe Mini Knife' with key attributes: dimens, inch, album, use, time, attent, balanc, black, blade, clip, close, coat, dedic, deliv, design, detail, want, easi, edg, even, featur, feel, fine, follow, frame, full, give, handl, year, knife, larger, length, let, littl, get, lock, materi, metal, mini, model, overal, skin, pocket, posit, size, small, specif, steel, style, type, weight, award and is connected with the node 7041 and it is classified as Sports & Outdoors, it is the target node. The node 32391 is a product titled 'Buck 55 Folding Hunter' with key attributes: use, fold, none and is connected with the node 7041 and it is classified as Sports & Outdoors, it is not the target node. The node 32392 is a product titled 'Bantam BBW' with key attributes: one, use, american, book, anyth, around, back, best, classic, cold, com, cool, custom, day, know, direct, end, featur, fine, fold, good, grip, hand, high, hole, hunt, knife, lightweight, lock, made, need, old, open, text, pocket, realli, repair, rescu, review, size, small, make, steel, style, surviv, think, usa, warranti, live and is connected with the node 7041 and it is classified as Sports & Outdoors, it is not the target node. The node 32393 is a product titled 'Gerber 31-001088 Myth Pocket Folder, Fine Edge Folding Lock-Back Clip Knife' with key attributes: use, back, blade, bulk, carri, clip, compact, durabl, edg, everyday, field, fine, fold, game, grip, handl, year, high, insid, knife, lightweight, lock, make, modern, one, qualiti, pocket, pro, provid, quick, rubber, secur, slim, soft, stainless, weather, work and is connected with the node 7041 and it is classified as Sports & Outdoors, it is not the target node. and given the counterfactual example: The node 822 is a product titled 'Gerber 31-001709 Swagger Assisted Opening Clip Knife' with key attributes: inch, use, book, black, blade, carri, clip, coat, day, drop, everi, excel, featur, great, grip, handl, knife, make, new, offer, open, origin, point, provid, quick, surfac, tactic, ultra, version, also and is connected with the node 7041 and it is classified as Sports & Outdoors, it is not the target node. The node 7041 is a product titled 'Gerber LST Folding Knife 22-06009' with key attributes: calib, one, use, back, year, never, deliv, graphic, first, fold, goe, would, handl, book, much, knife, last, lightweight, man, market, materi, name, none, qualiti, text, perform, manufactur, rug, seen, may, synthet, whose and is connected with the nodes 822, 32389, 32391, 32392, 32393 and it is classified as Sports & Outdoors, it is not the target node. The node 32389 is a product titled 'Case Cutlery 004 Case Executive Lockback Pocket Knife With Stainless Steel Blade   Metal' with key attributes: book, ad, use, american, well, time, warranti, year, blade, brand, case, centuri, choic, close, professor, companion, compani, craft, design, drop, edg, execut, featur, finest, gift, hand, handl, one, hunt, ideal, war, like, key, knife, lead, length, lifetim, limit, lock, make, manufactur, materi, measur, metal, skin, pattern, perfect, pocket, point, premium, rich, ring, sharp, slim, specif, stainless, steel, still, techniqu, tool, weight, world, redistribut, reader, chapter and is connected with the node 7041 and it is classified as Sports & Outdoors, it is not the target node. The node 32390 is a product titled 'Gerber Paraframe Mini Knife' with key attributes: dimens, inch, album, use, time, attent, balanc, black, blade, clip, close, coat, dedic, deliv, design, detail, want, easi, edg, even, featur, feel, fine, follow, frame, full, give, handl, year, knife, larger, length, let, littl, get, lock, materi, metal, mini, model, overal, skin, pocket, posit, size, small, specif, steel, style, type, weight, award and is connected with no other nodes and it is classified as Home & Kitchen, it is the target node. The node 32391 is a product titled 'Buck 55 Folding Hunter' with key attributes: use, fold, none and is connected with the node 7041 and it is classified as Sports & Outdoors, it is not the target node. The node 32392 is a product titled 'Bantam BBW' with key attributes: one, use, american, book, anyth, around, back, best, classic, cold, com, cool, custom, day, know, direct, end, featur, fine, fold, good, grip, hand, high, hole, hunt, knife, lightweight, lock, made, need, old, open, text, pocket, realli, repair, rescu, review, size, small, make, steel, style, surviv, think, usa, warranti, live and is connected with the node 7041 and it is classified as Sports & Outdoors, it is not the target node. The node 32393 is a product titled 'Gerber 31-001088 Myth Pocket Folder, Fine Edge Folding Lock-Back Clip Knife' with key attributes: use, back, blade, bulk, carri, clip, compact, durabl, edg, everyday, field, fine, fold, game, grip, handl, year, high, insid, knife, lightweight, lock, make, modern, one, qualiti, pocket, pro, provid, quick, rubber, secur, slim, soft, stainless, weather, work and is connected with the node 7041 and it is classified as Sports & Outdoors, it is not the target node.
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

- ID: 32390
- Title: Gerber Paraframe Mini Knife
- True class (canonical `y`): **Sports & Outdoors**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Sports & Outdoors**
- Prediction recorded by this method's pipeline: **Sports & Outdoors**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Gerber Paraframe Mini Knife. Content: Don't let the 3-inch folded size of the Mini fool you; Gerber gives this little guy the same attention to detail that has won the larger Paraframe models a dedicated following. You'll notice the same ergonomic metal handle and frame lock design, and it delivers the same positive blade engagement and balanced feel, even at this size. Features: - Tanto-style blade - Black titanium nitride-coated blade - Full fine edge blade is easy to sharpen - Frame lock - Pocket clip - Small size disappears in your pocket Specifications: - Overall Length: 5.25" (13.34 cm) - Blade Length: 2.13" (5.41 cm) - Closed Length: 3.13" (7.95 cm) - Weight: 1.5 oz. (43 g) - Steel Type: 7Cr17MoV - Handle Material: 3Cr13.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 7041 | Tools & Home Improvement | Gerber LST Folding Knife 22-06009 |

### 2-hop (shortest distance exactly 2): 5 nodes

| node id | true class | title |
|---|---|---|
| 822 | Tools & Home Improvement | Gerber 31-001709 Swagger Assisted Opening Clip Knife |
| 32389 | Sports & Outdoors | Case Cutlery 004 Case Executive Lockback Pocket Knife With Stainless Steel Blade   Metal |
| 32391 | Sports & Outdoors | Buck 55 Folding Hunter |
| 32392 | Sports & Outdoors | Bantam BBW |
| 32393 | Sports & Outdoors | Gerber 31-001088 Myth Pocket Folder, Fine Edge Folding Lock-Back Clip Knife |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/products/cf-gnnexplainer-canonical/random_seed_42_*` (key=117).

- Factual class: **Sports & Outdoors**
- Counterfactual class: **Home & Kitchen**
- Removed edges (global ids, 1): (7041, 32390)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 32390 |
| Factual_Target_Node_Neighbors | 7041 |
| Factual_Target_Node_Features | dimens, inch, album, use, use, time, attent, balanc, black, blade, clip, close, coat, use, dedic, deliv, design, detail, want, easi, edg, even, featur, feel, fine, follow, frame, use, full, give, handl, year, use, inch, use, use, knife, larger, length, let, littl, get, lock, materi, metal, mini, model, use, overal, skin, use, pocket, posit, use, time, size, small, specif, steel, style, use, use, use, use, use, type, weight, use, award, use, use |
| Counterfactual_Target_Node_Neighbors |  |
| Counterfactual_Target_Node_Features | dimens, inch, album, use, use, time, attent, balanc, black, blade, clip, close, coat, use, dedic, deliv, design, detail, want, easi, edg, even, featur, feel, fine, follow, frame, use, full, give, handl, year, use, inch, use, use, knife, larger, length, let, littl, get, lock, materi, metal, mini, model, use, overal, skin, use, pocket, posit, use, time, size, small, specif, steel, style, use, use, use, use, use, type, weight, use, award, use, use |
| Factual_Target_Node_Class | Sports & Outdoors |
| Counterfactual_Target_Node_class | Home & Kitchen |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 7041 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 32390 |
| Factual_Target_Node_Neighbors | 7041 |
| Factual_Target_Node_Features | dimens, inch, album, use, use, time, attent, balanc, black, blade, clip, close, coat, use, dedic, deliv, design, detail, want, easi, edg, even, featur, feel, fine, follow, frame, use, full, give, handl, year, use, inch, use, use, knife, larger, length, let, littl, get, lock, materi, metal, mini, model, use, overal, skin, use, pocket, posit, use, time, size, small, specif, steel, style, use, use, use, use, use, type, weight, use, award, use, use |
| Counterfactual_Target_Node_Neighbors |  |
| Counterfactual_Target_Node_Features | dimens, inch, album, use, use, time, attent, balanc, black, blade, clip, close, coat, use, dedic, deliv, design, detail, want, easi, edg, even, featur, feel, fine, follow, frame, use, full, give, handl, year, use, inch, use, use, knife, larger, length, let, littl, get, lock, materi, metal, mini, model, use, overal, skin, use, pocket, posit, use, time, size, small, specif, steel, style, use, use, use, use, use, type, weight, use, award, use, use |
| Factual_Target_Node_Class | Sports & Outdoors |
| Counterfactual_Target_Node_class | Home & Kitchen |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 7041 |
| Natural_Language_Explanation | None |
