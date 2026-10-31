# Reference packet: CF-GNNExplainer__Qwen-14B__products__32166

- Method: CF-GNNExplainer; configuration: Qwen-14B; dataset: products; target node: 32166
- Explanation source: `./robustness_2026-10-30/production_a100/qwen14b_gptq_int4_products_Response.json` ([116][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
To address the task, we will first populate the `infos` dictionary based on the provided factual and counterfactual examples. Then, we will analyze the changes and provide a natural language explanation.

### Populating the Dictionary

Given the factual and counterfactual graphs, we can extract the relevant information for the target node (node 32166) and its neighbors:

```python
infos = {
    'Target_Node_ID': '32166',
    'Factual_Target_Node_Neighbors': ['6986'],
    'Factual_Target_Node_Features': ['adapt', 'use', 'ball', 'camera', 'custom', 'descript', 'diamet', 'directli', 'factori', 'take', 'gopro', 'hero', 'item', 'mount', 'pro', 'quot', 'side', 'sold', 'specif', 'condit'],
    'Counterfactual_Target_Node_Neighbors': ['6986'],
    'Counterfactual_Target_Node_Features': ['adapt', 'use', 'ball', 'camera', 'custom', 'descript', 'diamet', 'directli', 'factori', 'take', 'gopro', 'hero', 'item', 'mount', 'pro', 'quot', 'side', 'sold', 'specif', 'condit'],
    'Factual_Target_Node_Class': 'Sports & Outdoors',
    'Counterfactual_Target_Node_class': 'Electronics',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Natural_Language_Explanation': ''
}
```

### Analyzing the Changes

In the factual graph, the target node (node 32166) is classified as "Sports & Outdoors." In the counterfactual graph, the same node is reclassified as "Electronics."

#### Key Observations:
1. **Node Features**: The features of the target node remain unchanged between the factual and counterfactual graphs. The node retains attributes related to a camera mount and adapter, which are consistent with both "Sports & Outdoors" and "Electronics" categories.
   
2. **Neighbor Nodes**: The only neighbor of the target node in both graphs is node 6986. However, the classification of node 6986 changes from "Sports & Outdoors" to "Electronics" in the counterfactual graph. This shift in the classification of node 6986 likely influences the reclassification of node 32166.

3. **Graph Structure**: The adjacency matrix perturbation likely altered the influence of node 6986 on node 32166. Since node 6986 is now classified as "Electronics," the model interprets node 32166 as more aligned with the "Electronics" category rather than "Sports & Outdoors."

### Natural Language Explanation

The target node (node 32166) was initially classified as "Sports & Outdoors" in the factual graph. However, in the counterfactual graph, it is reclassified as "Electronics." Despite the features of node 32166 remaining unchanged, the reclassification is influenced by the change in the classification of its neighbor node 6986. In the factual graph, node 6986 was classified as "Sports & Outdoors," but in the counterfactual graph, it is reclassified as "Electronics." This change in the classification of node 6986 alters the overall context and influences the model to classify node 32166 as "Electronics" in the counterfactual scenario.

Thus, the natural language explanation for the change in classification is:

**Natural_Language_Explanation**: "The target node (node 32166) was initially classified as 'Sports & Outdoors' because it was connected to a neighbor node (node 6986) that was also classified as 'Sports & Outdoors'. However, in the counterfactual scenario, the neighbor node (node 6986) is reclassified as 'Electronics', leading the model to reclassify the target node as 'Electronics' as well, reflecting the changed context provided by the neighbor node's new classification."

This explanation highlights the importance of neighbor nodes in influencing the classification of a target node within a graph-based machine learning model.
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
given the factual graph: The node 815 is a product titled 'Bestem LGKA-NOMAD-SDL-R Black Regular Saddlebag Liner for Kawasaki Vulcan Nomad' with key attributes: one, use, well, bag, black, carri, construct, custom, duti, easi, edg, even, featur, fit, handl, heavi, high, like, made, mani, multipl, never, nylon, plastic, pocket, proof, qualiti, regular, resist, shape, shoulder, make, stay, strap, system, water, weather and is connected with the nodes 6986, 6990 and it is classified as Sports & Outdoors, it is not the target node. The node 6902 is a product titled 'Battery Tender 081-0069-8 Female Cigarette Adaptor for Quick Disconnect' with key attributes: inch, accessori, use, time, batteri, cell, charg, devic, directli, featur, femal, help, phone, quick, rest, make, vehicl, one, provid and is connected with the node 6986 and it is classified as Sports & Outdoors, it is not the target node. The node 6903 is a product titled 'Super Strong Stretch Heavy-duty 15&quot; Cargo Net for Motorcycle ATV - Stretches to 45&quot;' with key attributes: inch, alwaysshowplaceholdertext, book, use, well, come, cool, duti, gener, heavi, materi, make, much, quot, rubber, see, stretch, strong, super, year and is connected with the node 6986 and it is classified as Sports & Outdoors, it is not the target node. The node 6969 is a product titled 'OGIO Saddlebag 110093.36' with key attributes: handbookandth, use, attach, one, heat, inch, lb, mold, mount, nylon, pad, paint, resist, side, silicon, volum, web, weight, wide and is connected with the nodes 6986, 6990 and it is classified as Sports & Outdoors, it is not the target node. The node 6981 is a product titled 'Dowco 50144-00 Fastrax Elite Series Black Sport and Adventure Tour Luggage Tail Bag' with key attributes: adventur, use, bag, black, none, seri, sport and is connected with the node 6986 and it is classified as Sports & Outdoors, it is not the target node. The node 6986 is a product titled '"Cortech Super 2.0 24-Liter Motorcycle Tail Bag - Black / Size 13.4'' L x 14.2'' W x 7.5'' D"' with key attributes: dimens, inch, hour, access, use, bag, black, carri, cover, interior, intern, lock, main, mount, pocket, polyest, red, releas, rubber, shoulder, side, size, snap, soft, sport, storag, strap, super, system, three, tone, top, way, one and is connected with the nodes 815, 6902, 6903, 6969, 6981, 6990, 32164, 32165, 32166 and it is classified as Sports & Outdoors, it is not the target node. The node 6990 is a product titled 'missing' with key attributes: book, also, use, avoid, bag, base, choos, critic, design, easi, ensur, featur, firm, fit, gear, indoor, like, metal, method, miss, one, mount, multi, must, need, non, option, outdoor, posit, resist, secur, seri, store, strap, system, think, valu, water, waterproof and is connected with the nodes 815, 6969, 6986, 32165 and it is classified as Sports & Outdoors, it is not the target node. The node 32164 is a product titled 'Classic Accessories 73807 MotoGear Motorcycle Indoor Dust Cover, Sport' with key attributes: accessori, use, classic, cover, dust, indoor, none, sport and is connected with the node 6986 and it is classified as Sports & Outdoors, it is not the target node. The node 32165 is a product titled 'MotoCentric Mototrek Sport Tail Bag - Black' with key attributes: dimens, inch, calib, glock, accessori, ad, one, also, use, attach, away, bag, base, black, built, capac, carri, come, construct, cord, cover, creat, detail, durabl, fit, four, full, handl, highest, hold, includ, interior, lifetim, light, made, match, materi, piec, protect, qualiti, quick, releas, remov, set, shoulder, side, soft, sport, strap, strength, like, warranti and is connected with the nodes 6986, 6990 and it is classified as Sports & Outdoors, it is not the target node. The node 32166 is a product titled 'RAM Mounts 1&quot; Diameter Ball with Custom GoPro Hero Adapter RAP-B-202U-GOP1' with key attributes: adapt, use, ball, camera, custom, descript, diamet, directli, factori, take, gopro, hero, item, mount, pro, quot, side, sold, specif, condit and is connected with the node 6986 and it is classified as Sports & Outdoors, it is the target node. and given the counterfactual example: The node 815 is a product titled 'Bestem LGKA-NOMAD-SDL-R Black Regular Saddlebag Liner for Kawasaki Vulcan Nomad' with key attributes: one, use, well, bag, black, carri, construct, custom, duti, easi, edg, even, featur, fit, handl, heavi, high, like, made, mani, multipl, never, nylon, plastic, pocket, proof, qualiti, regular, resist, shape, shoulder, make, stay, strap, system, water, weather and is connected with the nodes 6986, 6990 and it is classified as Sports & Outdoors, it is not the target node. The node 6902 is a product titled 'Battery Tender 081-0069-8 Female Cigarette Adaptor for Quick Disconnect' with key attributes: inch, accessori, use, time, batteri, cell, charg, devic, directli, featur, femal, help, phone, quick, rest, make, vehicl, one, provid and is connected with the node 6986 and it is classified as Sports & Outdoors, it is not the target node. The node 6903 is a product titled 'Super Strong Stretch Heavy-duty 15&quot; Cargo Net for Motorcycle ATV - Stretches to 45&quot;' with key attributes: inch, alwaysshowplaceholdertext, book, use, well, come, cool, duti, gener, heavi, materi, make, much, quot, rubber, see, stretch, strong, super, year and is connected with the node 6986 and it is classified as Sports & Outdoors, it is not the target node. The node 6969 is a product titled 'OGIO Saddlebag 110093.36' with key attributes: handbookandth, use, attach, one, heat, inch, lb, mold, mount, nylon, pad, paint, resist, side, silicon, volum, web, weight, wide and is connected with the nodes 6986, 6990 and it is classified as Sports & Outdoors, it is not the target node. The node 6981 is a product titled 'Dowco 50144-00 Fastrax Elite Series Black Sport and Adventure Tour Luggage Tail Bag' with key attributes: adventur, use, bag, black, none, seri, sport and is connected with the node 6986 and it is classified as Sports & Outdoors, it is not the target node. The node 6986 is a product titled '"Cortech Super 2.0 24-Liter Motorcycle Tail Bag - Black / Size 13.4'' L x 14.2'' W x 7.5'' D"' with key attributes: dimens, inch, hour, access, use, bag, black, carri, cover, interior, intern, lock, main, mount, pocket, polyest, red, releas, rubber, shoulder, side, size, snap, soft, sport, storag, strap, super, system, three, tone, top, way, one and is connected with the nodes 815, 6902, 6903, 6969, 6981, 32164, 32166 and it is classified as Sports & Outdoors, it is not the target node. The node 6990 is a product titled 'missing' with key attributes: book, also, use, avoid, bag, base, choos, critic, design, easi, ensur, featur, firm, fit, gear, indoor, like, metal, method, miss, one, mount, multi, must, need, non, option, outdoor, posit, resist, secur, seri, store, strap, system, think, valu, water, waterproof and is connected with the nodes 815, 6969, 32165 and it is classified as Sports & Outdoors, it is not the target node. The node 32164 is a product titled 'Classic Accessories 73807 MotoGear Motorcycle Indoor Dust Cover, Sport' with key attributes: accessori, use, classic, cover, dust, indoor, none, sport and is connected with the node 6986 and it is classified as Sports & Outdoors, it is not the target node. The node 32165 is a product titled 'MotoCentric Mototrek Sport Tail Bag - Black' with key attributes: dimens, inch, calib, glock, accessori, ad, one, also, use, attach, away, bag, base, black, built, capac, carri, come, construct, cord, cover, creat, detail, durabl, fit, four, full, handl, highest, hold, includ, interior, lifetim, light, made, match, materi, piec, protect, qualiti, quick, releas, remov, set, shoulder, side, soft, sport, strap, strength, like, warranti and is connected with the node 6990 and it is classified as Sports & Outdoors, it is not the target node. The node 32166 is a product titled 'RAM Mounts 1&quot; Diameter Ball with Custom GoPro Hero Adapter RAP-B-202U-GOP1' with key attributes: adapt, use, ball, camera, custom, descript, diamet, directli, factori, take, gopro, hero, item, mount, pro, quot, side, sold, specif, condit and is connected with the node 6986 and it is classified as Electronics, it is the target node.
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

- ID: 32166
- Title: RAM Mounts 1&quot; Diameter Ball with Custom GoPro Hero Adapter RAP-B-202U-GOP1
- True class (canonical `y`): **Electronics**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Sports & Outdoors**
- Prediction recorded by this method's pipeline: **Sports & Outdoors**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: RAM Mounts 1&quot; Diameter Ball with Custom GoPro Hero Adapter RAP-B-202U-GOP1. Content: Consists of a 1" diameter ball, connected to a custom Go Pro adapterAdapter attaches directly to the under side of the camera, replacing the factory mounting bracketAll items are sold individually unless specifically described otherwise in the product description
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 6986 | Automotive | "Cortech Super 2.0 24-Liter Motorcycle Tail Bag - Black / Size 13.4'' L x 14.2'' W x 7.5'' D" |

### 2-hop (shortest distance exactly 2): 8 nodes

| node id | true class | title |
|---|---|---|
| 815 | Automotive | Bestem LGKA-NOMAD-SDL-R Black Regular Saddlebag Liner for Kawasaki Vulcan Nomad |
| 6902 | Automotive | Battery Tender 081-0069-8 Female Cigarette Adaptor for Quick Disconnect |
| 6903 | Automotive | Super Strong Stretch Heavy-duty 15&quot; Cargo Net for Motorcycle ATV - Stretches to 45&quot; |
| 6969 | Automotive | OGIO Saddlebag 110093.36 |
| 6981 | Automotive | Dowco 50144-00 Fastrax Elite Series Black Sport and Adventure Tour Luggage Tail Bag |
| 6990 | Automotive | missing |
| 32164 | Automotive | Classic Accessories 73807 MotoGear Motorcycle Indoor Dust Cover, Sport |
| 32165 | Automotive | MotoCentric Mototrek Sport Tail Bag - Black |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/products/cf-gnnexplainer-canonical/random_seed_42_*` (key=116).

- Factual class: **Sports & Outdoors**
- Counterfactual class: **Electronics**
- Removed edges (global ids, 2): (6986, 6990), (6986, 32165)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 32166 |
| Factual_Target_Node_Neighbors | 6986 |
| Factual_Target_Node_Features | adapt, use, use, use, ball, camera, use, custom, descript, diamet, directli, factori, use, take, gopro, hero, use, item, mount, use, use, pro, use, quot, side, sold, specif, use, use, use, condit, use |
| Counterfactual_Target_Node_Neighbors | 6986 |
| Counterfactual_Target_Node_Features | adapt, use, use, use, ball, camera, use, custom, descript, diamet, directli, factori, use, take, gopro, hero, use, item, mount, use, use, pro, use, quot, side, sold, specif, use, use, use, condit, use |
| Factual_Target_Node_Class | Sports & Outdoors |
| Counterfactual_Target_Node_class | Electronics |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 32166 |
| Factual_Target_Node_Neighbors | 6986 |
| Factual_Target_Node_Features | adapt, use, use, use, ball, camera, use, custom, descript, diamet, directli, factori, use, take, gopro, hero, use, item, mount, use, use, pro, use, quot, side, sold, specif, use, use, use, condit, use |
| Counterfactual_Target_Node_Neighbors | 6986 |
| Counterfactual_Target_Node_Features | adapt, use, use, use, ball, camera, use, custom, descript, diamet, directli, factori, use, take, gopro, hero, use, item, mount, use, use, pro, use, quot, side, sold, specif, use, use, use, condit, use |
| Factual_Target_Node_Class | Sports & Outdoors |
| Counterfactual_Target_Node_class | Electronics |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |
