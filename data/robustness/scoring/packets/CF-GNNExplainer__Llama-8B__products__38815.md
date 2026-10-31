# Reference packet: CF-GNNExplainer__Llama-8B__products__38815

- Method: CF-GNNExplainer; configuration: Llama-8B; dataset: products; target node: 38815
- Explanation source: `./llm-graph-cf/data/results/cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_products_standard_Response.json` ([145][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, we can fill the dictionary as follows:

infos = {
    'Target_Node_ID': 38815,
    'Factual_Target_Node_Neighbors': [8935, 38813, 38814],
    'Factual_Target_Node_Features': ['accessori', 'aluminum', 'use', 'batteri', 'black', 'challeng', 'clip', 'construct', 'cool', 'enough', 'featur', 'finish', 'get', 'grade', 'impact', 'led', 'light', 'meet', 'offer', 'option', 'pro', 'rang', 'resist', 'seri', 'tough', 'want', 'waterproof', 'white', 'wide', 'without'],
    'Counterfactual_Target_Node_Neighbors': [],
    'Counterfactual_Target_Node_Features': ['adjust', 'amp', 'blue', 'color', 'contain', 'design', 'extern', 'featur', 'includ', 'led', 'light', 'mini', 'mode', 'model', 'take', 'text', 'requir', 'switch', 'regist'],
    'Factual_Target_Node_Class': 'Sports & Outdoors',
    'Counterfactual_Target_Node_class': 'Health & Personal Care',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': ['accessori', 'aluminum', 'use', 'batteri', 'black', 'challeng', 'clip', 'construct', 'cool', 'enough', 'featur', 'finish', 'get', 'grade', 'impact', 'led', 'light', 'meet', 'offer', 'option', 'pro', 'rang', 'resist', 'seri', 'tough', 'want', 'waterproof', 'white', 'wide', 'without'],
    'Natural_Language_Explanation': 'The target node 38815, which is a product titled "FOURSEVENS Quark AA&sup2;/ Pro QP2A-X Black Finish / Cool White LED; 2XAA; 280 Lumens", was initially classified as "Sports & Outdoors". However, in the counterfactual scenario, it is classified as "Health & Personal Care" because its features changed to include words related to health and personal care, such as "adjust", "amp", "blue", "color", "contain", "design", "extern", "featur", "includ", "led", "light", "mini", "mode", "model", "take", "text", "requir", "switch", and "regist". This change in classification is influenced by the absence of its original neighbors, 8935, 38813, and 38814, which were all classified as "Tools & Home Improvement" and "Sports & Outdoors".'
}

The change in classification for the target node 38815 from "Sports & Outdoors" to "Health & Personal Care" is primarily due to the removal of its original neighbors, 8935, 38813, and 38814, which were all classified as "Tools & Home Improvement" and "Sports & Outdoors". The absence of these neighbors leads to a shift in the target node's features towards health and personal care-related words.

The influence of the neighbors can be seen in the following ways:

* The original neighbors 8935, 38813, and 38814 were all classified as "Tools & Home Improvement" and "Sports & Outdoors", which suggests that they were influencing the target node 38815 to be classified as "Sports & Outdoors".
* In the counterfactual scenario, the absence of these neighbors leads to a change in the target node's features, causing it to be classified as "Health & Personal Care".
* The new features of the target node in the counterfactual scenario, such as "adjust", "amp", "blue", "color", "contain", "design", "extern", "featur", "includ", "led", "light", "mini", "mode", "model", "take", "text", "requir", "switch", and "regist", are more relevant to health and personal care than sports and outdoors.

Overall, the change in classification for the target node 38815 is a result of the removal of its original neighbors, which led to a shift in its features towards health and personal care-related words.
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
given the factual graph: The node 1053 is a product titled 'Singer Sewing Kit in Egg Shaped Storage Case' with key attributes: inch, use, assort, box, button, case, color, one, easili, easi, everyth, fit, great, help, includ, keep, kit, measur, need, plastic, polyest, quick, reusabl, safeti, sew, shape, singer, small, storag, straight, stylish, tape, thread, travel and is connected with the node 8935 and it is classified as Tools & Home Improvement, it is not the target node. The node 8935 is a product titled 'Streamlight 73001 Nano Light Miniature Keychain LED Flashlight, Black' with key attributes: hour, inch, made, year, handbookandth, capsul, book, access, never, allow, also, aluminum, use, applic, approxim, area, well, time, back, warranti, bag, batteri, need, belt, black, blue, bright, bulb, button, carri, cell, coat, construct, want, durabl, easili, easi, eight, everyday, extend, extrem, featur, finish, fire, five, four, gift, give, glass, goe, grade, great, greater, hand, handi, hardwar, one, head, high, home, hook, ideal, includ, innov, like, key, larger, last, law, led, length, less, life, lifetim, light, lightweight, limit, get, long, longer, make, manufactur, micro, money, much, non, take, often, oper, ounc, outdoor, output, perform, period, person, pocket, posit, power, produc, provid, quickli, red, regular, replac, rescu, ring, run, save, shape, shock, sinc, singl, size, small, snap, solid, standard, store, super, switch, system, technolog, though, tool, turn, view, know, white, work, worri and is connected with the nodes 1053, 38813, 38814, 38815, 38816, 38817 and it is classified as Tools & Home Improvement, it is not the target node. The node 38813 is a product titled 'Cold Steel Inferno .38 oz. Keyring Hardcase Unit Pepper Spray' with key attributes: inch, book, one, use, time, black, cold, contact, contain, deep, due, effect, extract, eye, face, feet, foam, give, good, ground, highli, hot, import, leav, life, like, liquid, make, may, new, skin, period, possibl, prevent, short, sinc, spray, steel, super, support, turn, unit, unlik and is connected with the node 8935 and it is classified as Sports & Outdoors, it is not the target node. The node 38814 is a product titled 'Kelty Redwing 50 Internal Frame Pack (Black, Small/Medium -14.5 - 18.5-Inch Torso)' with key attributes: inch, per, use, black, classic, comfort, conveni, design, frame, got, war, intern, one, like, main, medium, pack, pocket, popular, proven, small, stay, sturdi, system, top, also, reader and is connected with the node 8935 and it is classified as Sports & Outdoors, it is not the target node. The node 38815 is a product titled 'FOURSEVENS Quark AA&sup2;/ Pro QP2A-X Black Finish / Cool White LED; 2XAA; 280 Lumens' with key attributes: accessori, aluminum, use, batteri, black, challeng, clip, construct, cool, enough, featur, finish, get, grade, impact, led, light, meet, offer, option, pro, rang, resist, seri, tough, want, waterproof, white, wide, without and is connected with the node 8935 and it is classified as Tools & Home Improvement, it is the target node. The node 38816 is a product titled 'MECO(TM) Mini CREE Led Flashlight Torch Adjustable Zoom Light Lamp' with key attributes: adjust, aluminum, use, amp, batteri, blue, color, contain, design, extern, featur, includ, led, light, mini, mode, model, take, text, requir, switch, regist and is connected with the node 8935 and it is classified as Tools & Home Improvement, it is not the target node. The node 38817 is a product titled 'Light My Fire Swedish Firesteel Mini 1,500 Strike Ultralight Fire Starter' with key attributes: hour, inch, per, alreadi, also, use, around, well, time, build, degre, depart, develop, easi, essenti, everi, favorit, fire, flash, found, ga, year, one, kit, light, made, make, mini, read, number, ounc, proof, steel, surviv, way, weather, world and is connected with the node 8935 and it is classified as Tools & Home Improvement, it is not the target node. and given the counterfactual example: The node 1053 is a product titled 'Singer Sewing Kit in Egg Shaped Storage Case' with key attributes: inch, use, assort, box, button, case, color, one, easili, easi, everyth, fit, great, help, includ, keep, kit, measur, need, plastic, polyest, quick, reusabl, safeti, sew, shape, singer, small, storag, straight, stylish, tape, thread, travel and is connected with no other nodes and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 8935 is a product titled 'Streamlight 73001 Nano Light Miniature Keychain LED Flashlight, Black' with key attributes: hour, inch, made, year, handbookandth, capsul, book, access, never, allow, also, aluminum, use, applic, approxim, area, well, time, back, warranti, bag, batteri, need, belt, black, blue, bright, bulb, button, carri, cell, coat, construct, want, durabl, easili, easi, eight, everyday, extend, extrem, featur, finish, fire, five, four, gift, give, glass, goe, grade, great, greater, hand, handi, hardwar, one, head, high, home, hook, ideal, includ, innov, like, key, larger, last, law, led, length, less, life, lifetim, light, lightweight, limit, get, long, longer, make, manufactur, micro, money, much, non, take, often, oper, ounc, outdoor, output, perform, period, person, pocket, posit, power, produc, provid, quickli, red, regular, replac, rescu, ring, run, save, shape, shock, sinc, singl, size, small, snap, solid, standard, store, super, switch, system, technolog, though, tool, turn, view, know, white, work, worri and is connected with the nodes 38813, 38814, 38815 and it is classified as Tools & Home Improvement, it is not the target node. The node 38813 is a product titled 'Cold Steel Inferno .38 oz. Keyring Hardcase Unit Pepper Spray' with key attributes: inch, book, one, use, time, black, cold, contact, contain, deep, due, effect, extract, eye, face, feet, foam, give, good, ground, highli, hot, import, leav, life, like, liquid, make, may, new, skin, period, possibl, prevent, short, sinc, spray, steel, super, support, turn, unit, unlik and is connected with the node 8935 and it is classified as Sports & Outdoors, it is not the target node. The node 38814 is a product titled 'Kelty Redwing 50 Internal Frame Pack (Black, Small/Medium -14.5 - 18.5-Inch Torso)' with key attributes: inch, per, use, black, classic, comfort, conveni, design, frame, got, war, intern, one, like, main, medium, pack, pocket, popular, proven, small, stay, sturdi, system, top, also, reader and is connected with the node 8935 and it is classified as Sports & Outdoors, it is not the target node. The node 38815 is a product titled 'FOURSEVENS Quark AA&sup2;/ Pro QP2A-X Black Finish / Cool White LED; 2XAA; 280 Lumens' with key attributes: accessori, aluminum, use, batteri, black, challeng, clip, construct, cool, enough, featur, finish, get, grade, impact, led, light, meet, offer, option, pro, rang, resist, seri, tough, want, waterproof, white, wide, without and is connected with the node 8935 and it is classified as Sports & Outdoors, it is the target node. The node 38816 is a product titled 'MECO(TM) Mini CREE Led Flashlight Torch Adjustable Zoom Light Lamp' with key attributes: adjust, aluminum, use, amp, batteri, blue, color, contain, design, extern, featur, includ, led, light, mini, mode, model, take, text, requir, switch, regist and is connected with no other nodes and it is classified as Health & Personal Care, it is not the target node. The node 38817 is a product titled 'Light My Fire Swedish Firesteel Mini 1,500 Strike Ultralight Fire Starter' with key attributes: hour, inch, per, alreadi, also, use, around, well, time, build, degre, depart, develop, easi, essenti, everi, favorit, fire, flash, found, ga, year, one, kit, light, made, make, mini, read, number, ounc, proof, steel, surviv, way, weather, world and is connected with no other nodes and it is classified as Toys & Games, it is not the target node.
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

- ID: 38815
- Title: FOURSEVENS Quark AA&sup2;/ Pro QP2A-X Black Finish / Cool White LED; 2XAA; 280 Lumens
- True class (canonical `y`): **Tools & Home Improvement**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Tools & Home Improvement**
- Prediction recorded by this method's pipeline: **Tools & Home Improvement**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: FOURSEVENS Quark AA&sup2;/ Pro QP2A-X Black Finish / Cool White LED; 2XAA; 280 Lumens. Content: The Quark series offers a staggering array of options, accessories and interchangeability. With a wide range of LED, battery and clip choices, you get the features you want without compromise. Waterproof and constructed with aircraft-grade aluminum and impact-resistant lenses, Quark lights are tough enough to meet any challenge.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 8935 | Tools & Home Improvement | Streamlight 73001 Nano Light Miniature Keychain LED Flashlight, Black |

### 2-hop (shortest distance exactly 2): 5 nodes

| node id | true class | title |
|---|---|---|
| 1053 | Arts, Crafts & Sewing | Singer Sewing Kit in Egg Shaped Storage Case |
| 38813 | Sports & Outdoors | Cold Steel Inferno .38 oz. Keyring Hardcase Unit Pepper Spray |
| 38814 | Sports & Outdoors | Kelty Redwing 50 Internal Frame Pack (Black, Small/Medium -14.5 - 18.5-Inch Torso) |
| 38816 | Tools & Home Improvement | MECO(TM) Mini CREE Led Flashlight Torch Adjustable Zoom Light Lamp |
| 38817 | Sports & Outdoors | Light My Fire Swedish Firesteel Mini 1,500 Strike Ultralight Fire Starter |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/products/cf-gnnexplainer-canonical/random_seed_42_*` (key=145).

- Factual class: **Tools & Home Improvement**
- Counterfactual class: **Sports & Outdoors**
- Removed edges (global ids, 3): (1053, 8935), (8935, 38816), (8935, 38817)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 38815 |
| Factual_Target_Node_Neighbors | 8935 |
| Factual_Target_Node_Features | accessori, aluminum, use, use, use, use, batteri, black, challeng, clip, construct, use, cool, enough, featur, finish, use, get, grade, impact, led, light, meet, use, offer, option, use, pro, use, rang, resist, seri, use, use, use, tough, want, waterproof, white, wide, use, without, use |
| Counterfactual_Target_Node_Neighbors | 8935 |
| Counterfactual_Target_Node_Features | accessori, aluminum, use, use, use, use, batteri, black, challeng, clip, construct, use, cool, enough, featur, finish, use, get, grade, impact, led, light, meet, use, offer, option, use, pro, use, rang, resist, seri, use, use, use, tough, want, waterproof, white, wide, use, without, use |
| Factual_Target_Node_Class | Tools & Home Improvement |
| Counterfactual_Target_Node_class | Sports & Outdoors |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 38815 |
| Factual_Target_Node_Neighbors | 8935 |
| Factual_Target_Node_Features | accessori, aluminum, use, use, use, use, batteri, black, challeng, clip, construct, use, cool, enough, featur, finish, use, get, grade, impact, led, light, meet, use, offer, option, use, pro, use, rang, resist, seri, use, use, use, tough, want, waterproof, white, wide, use, without, use |
| Counterfactual_Target_Node_Neighbors | 8935 |
| Counterfactual_Target_Node_Features | accessori, aluminum, use, use, use, use, batteri, black, challeng, clip, construct, use, cool, enough, featur, finish, use, get, grade, impact, led, light, meet, use, offer, option, use, pro, use, rang, resist, seri, use, use, use, tough, want, waterproof, white, wide, use, without, use |
| Factual_Target_Node_Class | Tools & Home Improvement |
| Counterfactual_Target_Node_class | Sports & Outdoors |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |
