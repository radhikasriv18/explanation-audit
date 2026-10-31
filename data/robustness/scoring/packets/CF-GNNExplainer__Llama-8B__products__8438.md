# Reference packet: CF-GNNExplainer__Llama-8B__products__8438

- Method: CF-GNNExplainer; configuration: Llama-8B; dataset: products; target node: 8438
- Explanation source: `./llm-graph-cf/data/results/cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_products_standard_Response.json` ([29][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, we will fill the dictionary with the required information.

The target node is 8438, which is a product titled 'Born Free 9 oz. BPA-Free High-Heat Resistant Classic Bottle with ActiveFlow Venting Technology, 3-Pack'. 

The factual graph has the following information:

- Target_Node_ID: 8438
- Factual_Target_Node_Neighbors: [37121, 37122, 37123, 37124, 37125]
- Factual_Target_Node_Features: ['use', 'born', 'bottl', 'classic', 'free', 'heat', 'high', 'none', 'skin', 'pack', 'resist', 'technolog']
- Counterfactual_Target_Node_Neighbors: [37121, 37122, 37123, 37124, 37125]
- Counterfactual_Target_Node_Features: ['use', 'born', 'bottl', 'classic', 'free', 'heat', 'high', 'none', 'skin', 'pack', 'resist', 'technolog']
- Factual_Target_Node_Class: Home & Kitchen
- Counterfactual_Target_Node_class: Home & Kitchen
- Target_Node_Features_Changed_From_Factual_To_Counterfactual: []
- Natural_Language_Explanation: The target node remains classified as Home & Kitchen in both the factual and counterfactual examples.

However, upon closer inspection, we notice that the factual and counterfactual examples have the same neighbors and features. This suggests that there are no changes in the graph structure or node features that would affect the classification of the target node.

To generate a counterfactual explanation, we need to introduce some changes to the graph structure or node features. Let's assume we introduce a new edge between the target node 8438 and a node from a different category, say 37124, which is a product titled 'Braun Thermoscan Ear Thermometer-irt4520' from the Health & Personal Care category.

Here's the updated dictionary:

- Target_Node_ID: 8438
- Factual_Target_Node_Neighbors: [37121, 37122, 37123, 37124, 37125]
- Factual_Target_Node_Features: ['use', 'born', 'bottl', 'classic', 'free', 'heat', 'high', 'none', 'skin', 'pack', 'resist', 'technolog']
- Counterfactual_Target_Node_Neighbors: [37121, 37122, 37123, 37124, 37125, 37124] # New edge added
- Counterfactual_Target_Node_Features: ['use', 'born', 'bottl', 'classic', 'free', 'heat', 'high', 'none', 'skin', 'pack', 'resist', 'technolog']
- Factual_Target_Node_Class: Home & Kitchen
- Counterfactual_Target_Node_class: Health & Personal Care
- Target_Node_Features_Changed_From_Factual_To_Counterfactual: []
- Natural_Language_Explanation: The addition of the new edge between the target node 8438 and node 37124, which is from a different category, causes the target node to be reclassified as Health & Personal Care in the counterfactual example.

This change in classification is influenced by the neighbors of the target node, specifically the new edge added to node 37124, which is from a different category. This highlights the importance of considering the graph structure and node features when generating counterfactual explanations.

In terms of the influences of neighbor nodes, we can see that the addition of the new edge to node 37124 has a significant impact on the classification of the target node. This suggests that the neighbors of the target node play a crucial role in determining its classification, especially when the graph structure is modified.

Overall, the counterfactual explanation provides valuable insights into how changes in the graph structure or node features can affect the classification of the target node, highlighting the importance of considering the complex interactions between nodes in the graph.
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
given the factual graph: The node 75 is a product titled 'KAL Dino-Dophilus Probiotic 2 Billion Chewables, Black Cherry, 60 Count' with key attributes: capsul, use, black, blend, child, combin, count, import, intend, provid, support, system and is connected with the nodes 984, 987, 991, 992, 995 and it is classified as Health & Personal Care, it is not the target node. The node 984 is a product titled 'Power Probiotic ENT Kids - Strawberry Blast 30 Chewable Tablets | Supports the Natural Immune Defenses of the Ears, Nose' with key attributes: day, also, aluminum, use, well, bad, caus, cell, one, fresh, health, healthi, kid, natur, never, pack, power, collagen, promot, seal, support, tablet and is connected with the nodes 75, 992, 8340 and it is classified as Health & Personal Care, it is not the target node. The node 987 is a product titled 'ReNew Life - Buddy Bear Probiotic for Kids Orange - 60 Chewable Tablets' with key attributes: year, capsul, deflockedst, bed, book, activ, age, allow, use, well, bacteria, balanc, need, benefit, bodi, certain, children, contain, daili, delici, diet, one, easi, enhanc, environ, even, everyday, flavor, formul, found, function, good, health, healthi, help, howev, human, import, ingredi, issu, keep, kid, lead, life, maintain, may, make, natur, number, older, orang, order, text, percent, prevent, provid, question, read, stress, mani, sun, supplement, support, tablet, take, like, travel, type, know, whole and is connected with the nodes 75, 991, 992 and it is classified as Health & Personal Care, it is not the target node. The node 991 is a product titled 'American Health Acidophilus with Bifidus Fruit -- 100 Wafers' with key attributes: made, addit, one, use, american, book, assort, bacteria, balanc, benefit, classic, contain, conveni, daili, day, delici, deliv, easi, enhanc, everyday, feel, free, good, great, growth, guarante, health, help, ideal, maintain, mix, natur, optim, qualiti, per, posit, proper, receiv, serv, support, read, two, way and is connected with the nodes 75, 987, 992 and it is classified as Health & Personal Care, it is not the target node. The node 992 is a product titled 'Culturelle Kids! Chewables Probiotic, for kids 50-100lbs, Tablets, 30 ea(Pack of 2)' with key attributes: day, per, use, well, bacteria, balanc, stori, child, contain, get, good, year, health, help, import, kid, one, natur, need, non, overal, pack, proper, regular, research, safe, shown, support, system, tablet, book, live, provid and is connected with the nodes 75, 984, 987, 991, 995, 8340, 8389, 8433, 8434, 8435, 8436, 8437, 8438 and it is classified as Health & Personal Care, it is not the target node. The node 995 is a product titled '"Udo's Choice Children's Blend Probiotic 60 Capsules"' with key attributes: inch, capsul, age, use, amount, time, back, bacteria, year, blend, one, care, cell, children, choic, compani, contain, current, date, dedic, design, develop, professor, earli, ensur, extra, featur, formul, friendli, health, healthi, help, book, larg, life, maintain, manufactur, maximum, meet, natur, need, normal, origin, qualiti, per, perfect, collagen, proper, sinc, small, specif, state, strength, stretch, support, system, uniqu, unit, first, make, live, reader and is connected with the nodes 75, 992 and it is classified as Health & Personal Care, it is not the target node. The node 8340 is a product titled 'ReNew Life - Ultimate Flora Kids Probiotic - 30 Chewable Tablets' with key attributes: day, use, balanc, gentl, great, help, kid, life, safe, tablet, ultim, way and is connected with the nodes 984, 992 and it is classified as Health & Personal Care, it is not the target node. The node 8389 is a product titled 'Amerifit Culturelle Probiotics for Kids, 30 Count' with key attributes: made, day, actual, add, use, bacteria, balanc, benefit, better, child, cool, count, develop, easi, especi, free, ga, good, happi, healthi, help, keep, kid, like, liquid, littl, one, natur, ndash, parent, proven, reduc, rsquo, scienc, make, support, system, take, taken, book, work and is connected with the node 992 and it is classified as Health & Personal Care, it is not the target node. The node 8433 is a product titled 'Focus for Children Solaray 60 Chewable Tablet' with key attributes: hour, inch, per, capsul, acid, age, use, amount, well, base, children, daili, diet, extract, flavor, focu, guarante, inform, ingredi, key, label, make, natur, one, percent, see, serv, size, supplement, tablet, take, time, total, valu and is connected with the node 992 and it is classified as Health & Personal Care, it is not the target node. The node 8434 is a product titled 'BIOGAIA PROBIOTIC CHEWABLE TABLETS 60 TABS' with key attributes: capsul, activ, adult, use, book, well, bacteria, bad, balanc, battl, year, stori, bodi, caus, children, clinic, contain, effect, except, feel, go, good, health, help, human, one, life, major, may, mean, modern, natur, need, number, littl, qualiti, proven, record, safe, safeti, studi, tablet, test, like, uniqu, also, word and is connected with the node 992 and it is classified as Health & Personal Care, it is not the target node. The node 8435 is a product titled 'green sprouts Warming Plate, Sage' with key attributes: use, base, bottom, dishwash, fill, food, free, green, keep, new, non, plate, safe, slip, warm, water, one and is connected with the node 992 and it is classified as Health & Personal Care, it is not the target node. The node 8436 is a product titled 'Medela Swing Breastpump' with key attributes: inch, rm, hour, book, charger, accessori, adapt, afford, year, one, use, babi, bag, batteri, belt, bodi, bottl, clip, compact, connector, diamet, effici, electr, even, exclus, fast, featur, get, take, gold, guid, includ, inform, instruct, like, less, light, love, medium, reticl, motor, natur, neck, need, skin, pattern, portabl, separ, shoulder, singl, make, sold, stand, standard, start, storag, strap, suppli, technolog, trade, two, unit, want, also and is connected with the node 992 and it is classified as Health & Personal Care, it is not the target node. The node 8437 is a product titled 'Culturelle Probiotics for Kids 30 Ct (2 Pack)' with key attributes: day, use, kid, pack and is connected with the node 992 and it is classified as Health & Personal Care, it is not the target node. The node 8438 is a product titled 'Born Free 9 oz. BPA-Free High-Heat Resistant Classic Bottle with ActiveFlow Venting Technology, 3-Pack' with key attributes: use, born, bottl, classic, free, heat, high, none, skin, pack, resist, technolog and is connected with the nodes 992, 37121, 37122, 37123, 37124, 37125 and it is classified as Health & Personal Care, it is the target node. The node 37121 is a product titled 'Kidco F710 Baby Food Mill' with key attributes: one, use, anywher, babi, blade, carri, case, come, compon, dishwash, like, easi, food, fresh, give, grade, hand, home, item, let, lightweight, make, medic, skin, precis, quickli, safe, smooth, stainless, steel, travel and is connected with the node 8438 and it is classified as Health & Personal Care, it is not the target node. The node 37122 is a product titled 'Zo-Li Two Baby Wide Neck Baby Bottles (10 Oz)' with key attributes: inch, air, use, book, anti, well, babi, bottl, extra, featur, free, integr, made, neck, skin, part, plastic, reduc, time, mani, two, uniqu, wash, also, wide, without, work and is connected with the node 8438 and it is classified as Home & Kitchen, it is not the target node. The node 37123 is a product titled 'Beaba Bib Expresso 3 in 1 Baby Bottle &amp; Food Warmer' with key attributes: capsul, one, also, use, amount, amp, well, babi, bottl, button, choos, clean, know, take, like, easi, etc, faster, fill, food, formula, free, hand, heat, hot, book, lid, line, littl, machin, make, max, mode, much, need, never, orang, perfect, place, pre, press, put, second, self, simpli, store, tea, year, first, thing, two, warm, water, provid, work and is connected with the node 8438 and it is classified as Home & Kitchen, it is not the target node. The node 37124 is a product titled 'Braun Thermoscan Ear Thermometer-irt4520' with key attributes: pux, accuraci, accur, year, use, book, time, base, batteri, blood, brand, care, case, center, chang, children, control, cool, could, custom, design, due, one, effect, ensur, excel, featur, filter, function, gener, heat, help, introduct, like, len, measur, reticl, make, posit, pre, protect, quickli, research, result, secur, suppli, system, techniqu, temperatur, tip, total, two, uniqu, unlik, weight and is connected with the node 8438 and it is classified as Health & Personal Care, it is not the target node. The node 37125 is a product titled 'Born Free Silicone Teether' with key attributes: use, born, free, silicon and is connected with the node 8438 and it is classified as Health & Personal Care, it is not the target node. and given the counterfactual example: The node 75 is a product titled 'KAL Dino-Dophilus Probiotic 2 Billion Chewables, Black Cherry, 60 Count' with key attributes: capsul, use, black, blend, child, combin, count, import, intend, provid, support, system and is connected with the nodes 984, 987, 991, 992, 995 and it is classified as Health & Personal Care, it is not the target node. The node 984 is a product titled 'Power Probiotic ENT Kids - Strawberry Blast 30 Chewable Tablets | Supports the Natural Immune Defenses of the Ears, Nose' with key attributes: day, also, aluminum, use, well, bad, caus, cell, one, fresh, health, healthi, kid, natur, never, pack, power, collagen, promot, seal, support, tablet and is connected with the nodes 75, 992, 8340 and it is classified as Health & Personal Care, it is not the target node. The node 987 is a product titled 'ReNew Life - Buddy Bear Probiotic for Kids Orange - 60 Chewable Tablets' with key attributes: year, capsul, deflockedst, bed, book, activ, age, allow, use, well, bacteria, balanc, need, benefit, bodi, certain, children, contain, daili, delici, diet, one, easi, enhanc, environ, even, everyday, flavor, formul, found, function, good, health, healthi, help, howev, human, import, ingredi, issu, keep, kid, lead, life, maintain, may, make, natur, number, older, orang, order, text, percent, prevent, provid, question, read, stress, mani, sun, supplement, support, tablet, take, like, travel, type, know, whole and is connected with the nodes 75, 991, 992 and it is classified as Health & Personal Care, it is not the target node. The node 991 is a product titled 'American Health Acidophilus with Bifidus Fruit -- 100 Wafers' with key attributes: made, addit, one, use, american, book, assort, bacteria, balanc, benefit, classic, contain, conveni, daili, day, delici, deliv, easi, enhanc, everyday, feel, free, good, great, growth, guarante, health, help, ideal, maintain, mix, natur, optim, qualiti, per, posit, proper, receiv, serv, support, read, two, way and is connected with the nodes 75, 987, 992 and it is classified as Health & Personal Care, it is not the target node. The node 992 is a product titled 'Culturelle Kids! Chewables Probiotic, for kids 50-100lbs, Tablets, 30 ea(Pack of 2)' with key attributes: day, per, use, well, bacteria, balanc, stori, child, contain, get, good, year, health, help, import, kid, one, natur, need, non, overal, pack, proper, regular, research, safe, shown, support, system, tablet, book, live, provid and is connected with the nodes 75, 984, 987, 991, 995, 8340, 8389, 8433, 8434, 8435, 8436, 8437 and it is classified as Health & Personal Care, it is not the target node. The node 995 is a product titled '"Udo's Choice Children's Blend Probiotic 60 Capsules"' with key attributes: inch, capsul, age, use, amount, time, back, bacteria, year, blend, one, care, cell, children, choic, compani, contain, current, date, dedic, design, develop, professor, earli, ensur, extra, featur, formul, friendli, health, healthi, help, book, larg, life, maintain, manufactur, maximum, meet, natur, need, normal, origin, qualiti, per, perfect, collagen, proper, sinc, small, specif, state, strength, stretch, support, system, uniqu, unit, first, make, live, reader and is connected with the nodes 75, 992 and it is classified as Health & Personal Care, it is not the target node. The node 8340 is a product titled 'ReNew Life - Ultimate Flora Kids Probiotic - 30 Chewable Tablets' with key attributes: day, use, balanc, gentl, great, help, kid, life, safe, tablet, ultim, way and is connected with the nodes 984, 992 and it is classified as Health & Personal Care, it is not the target node. The node 8389 is a product titled 'Amerifit Culturelle Probiotics for Kids, 30 Count' with key attributes: made, day, actual, add, use, bacteria, balanc, benefit, better, child, cool, count, develop, easi, especi, free, ga, good, happi, healthi, help, keep, kid, like, liquid, littl, one, natur, ndash, parent, proven, reduc, rsquo, scienc, make, support, system, take, taken, book, work and is connected with the node 992 and it is classified as Health & Personal Care, it is not the target node. The node 8433 is a product titled 'Focus for Children Solaray 60 Chewable Tablet' with key attributes: hour, inch, per, capsul, acid, age, use, amount, well, base, children, daili, diet, extract, flavor, focu, guarante, inform, ingredi, key, label, make, natur, one, percent, see, serv, size, supplement, tablet, take, time, total, valu and is connected with the node 992 and it is classified as Health & Personal Care, it is not the target node. The node 8434 is a product titled 'BIOGAIA PROBIOTIC CHEWABLE TABLETS 60 TABS' with key attributes: capsul, activ, adult, use, book, well, bacteria, bad, balanc, battl, year, stori, bodi, caus, children, clinic, contain, effect, except, feel, go, good, health, help, human, one, life, major, may, mean, modern, natur, need, number, littl, qualiti, proven, record, safe, safeti, studi, tablet, test, like, uniqu, also, word and is connected with the node 992 and it is classified as Health & Personal Care, it is not the target node. The node 8435 is a product titled 'green sprouts Warming Plate, Sage' with key attributes: use, base, bottom, dishwash, fill, food, free, green, keep, new, non, plate, safe, slip, warm, water, one and is connected with the node 992 and it is classified as Health & Personal Care, it is not the target node. The node 8436 is a product titled 'Medela Swing Breastpump' with key attributes: inch, rm, hour, book, charger, accessori, adapt, afford, year, one, use, babi, bag, batteri, belt, bodi, bottl, clip, compact, connector, diamet, effici, electr, even, exclus, fast, featur, get, take, gold, guid, includ, inform, instruct, like, less, light, love, medium, reticl, motor, natur, neck, need, skin, pattern, portabl, separ, shoulder, singl, make, sold, stand, standard, start, storag, strap, suppli, technolog, trade, two, unit, want, also and is connected with the node 992 and it is classified as Health & Personal Care, it is not the target node. The node 8437 is a product titled 'Culturelle Probiotics for Kids 30 Ct (2 Pack)' with key attributes: day, use, kid, pack and is connected with the node 992 and it is classified as Health & Personal Care, it is not the target node. The node 8438 is a product titled 'Born Free 9 oz. BPA-Free High-Heat Resistant Classic Bottle with ActiveFlow Venting Technology, 3-Pack' with key attributes: use, born, bottl, classic, free, heat, high, none, skin, pack, resist, technolog and is connected with the nodes 37121, 37122, 37125 and it is classified as Home & Kitchen, it is the target node. The node 37121 is a product titled 'Kidco F710 Baby Food Mill' with key attributes: one, use, anywher, babi, blade, carri, case, come, compon, dishwash, like, easi, food, fresh, give, grade, hand, home, item, let, lightweight, make, medic, skin, precis, quickli, safe, smooth, stainless, steel, travel and is connected with the node 8438 and it is classified as Home & Kitchen, it is not the target node. The node 37122 is a product titled 'Zo-Li Two Baby Wide Neck Baby Bottles (10 Oz)' with key attributes: inch, air, use, book, anti, well, babi, bottl, extra, featur, free, integr, made, neck, skin, part, plastic, reduc, time, mani, two, uniqu, wash, also, wide, without, work and is connected with the node 8438 and it is classified as Beauty, it is not the target node. The node 37123 is a product titled 'Beaba Bib Expresso 3 in 1 Baby Bottle &amp; Food Warmer' with key attributes: capsul, one, also, use, amount, amp, well, babi, bottl, button, choos, clean, know, take, like, easi, etc, faster, fill, food, formula, free, hand, heat, hot, book, lid, line, littl, machin, make, max, mode, much, need, never, orang, perfect, place, pre, press, put, second, self, simpli, store, tea, year, first, thing, two, warm, water, provid, work and is connected with no other nodes and it is classified as Home & Kitchen, it is not the target node. The node 37124 is a product titled 'Braun Thermoscan Ear Thermometer-irt4520' with key attributes: pux, accuraci, accur, year, use, book, time, base, batteri, blood, brand, care, case, center, chang, children, control, cool, could, custom, design, due, one, effect, ensur, excel, featur, filter, function, gener, heat, help, introduct, like, len, measur, reticl, make, posit, pre, protect, quickli, research, result, secur, suppli, system, techniqu, temperatur, tip, total, two, uniqu, unlik, weight and is connected with no other nodes and it is classified as Health & Personal Care, it is not the target node. The node 37125 is a product titled 'Born Free Silicone Teether' with key attributes: use, born, free, silicon and is connected with the node 8438 and it is classified as Home & Kitchen, it is not the target node.
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

- ID: 8438
- Title: Born Free 9 oz. BPA-Free High-Heat Resistant Classic Bottle with ActiveFlow Venting Technology, 3-Pack
- True class (canonical `y`): **Baby**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Health & Personal Care**
- Prediction recorded by this method's pipeline: **Health & Personal Care**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Born Free 9 oz. BPA-Free High-Heat Resistant Classic Bottle with ActiveFlow Venting Technology, 3-Pack. Content: None
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 6 nodes

| node id | true class | title |
|---|---|---|
| 992 | Health & Personal Care | Culturelle Kids! Chewables Probiotic, for kids 50-100lbs, Tablets, 30 ea(Pack of 2) |
| 37121 | Baby | Kidco F710 Baby Food Mill |
| 37122 | Baby | Zo-Li Two Baby Wide Neck Baby Bottles (10 Oz) |
| 37123 | Baby | Beaba Bib Expresso 3 in 1 Baby Bottle &amp; Food Warmer |
| 37124 | Health & Personal Care | Braun Thermoscan Ear Thermometer-irt4520 |
| 37125 | Baby | Born Free Silicone Teether |

### 2-hop (shortest distance exactly 2): 12 nodes

| node id | true class | title |
|---|---|---|
| 75 | Health & Personal Care | KAL Dino-Dophilus Probiotic 2 Billion Chewables, Black Cherry, 60 Count |
| 984 | Health & Personal Care | Power Probiotic ENT Kids - Strawberry Blast 30 Chewable Tablets \| Supports the Natural Immune Defenses of the Ears, Nose/Nasopharynx, and Throat \| Promotes Oral Health and Fresh Breath \| Individually Sealed in Nitrogen-Purged Aluminum Blister Packs to Insure Freshness |
| 987 | Health & Personal Care | ReNew Life - Buddy Bear Probiotic for Kids Orange - 60 Chewable Tablets |
| 991 | Health & Personal Care | American Health Acidophilus with Bifidus Fruit -- 100 Wafers |
| 995 | Health & Personal Care | "Udo's Choice Children's Blend Probiotic 60 Capsules" |
| 8340 | Health & Personal Care | ReNew Life - Ultimate Flora Kids Probiotic - 30 Chewable Tablets |
| 8389 | Health & Personal Care | Amerifit Culturelle Probiotics for Kids, 30 Count |
| 8433 | Health & Personal Care | Focus for Children Solaray 60 Chewable Tablet |
| 8434 | Beauty | BIOGAIA PROBIOTIC CHEWABLE TABLETS 60 TABS |
| 8435 | Baby | green sprouts Warming Plate, Sage |
| 8436 | Baby | Medela Swing Breastpump |
| 8437 | Health & Personal Care | Culturelle Probiotics for Kids 30 Ct (2 Pack) |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/products/cf-gnnexplainer-canonical/random_seed_42_*` (key=29).

- Factual class: **Health & Personal Care**
- Counterfactual class: **Home & Kitchen**
- Removed edges (global ids, 3): (992, 8438), (8438, 37123), (8438, 37124)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 8438 |
| Factual_Target_Node_Neighbors | 992, 37121, 37122, 37123, 37124, 37125 |
| Factual_Target_Node_Features | use, use, born, bottl, classic, use, free, use, heat, high, none, skin, pack, use, use, resist, technolog, use, use |
| Counterfactual_Target_Node_Neighbors | 37121, 37122, 37125 |
| Counterfactual_Target_Node_Features | use, use, born, bottl, classic, use, free, use, heat, high, none, skin, pack, use, use, resist, technolog, use, use |
| Factual_Target_Node_Class | Health & Personal Care |
| Counterfactual_Target_Node_class | Home & Kitchen |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 992, 37123, 37124 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 8438 |
| Factual_Target_Node_Neighbors | 992, 37121, 37122, 37123, 37124, 37125 |
| Factual_Target_Node_Features | use, use, born, bottl, classic, use, free, use, heat, high, none, skin, pack, use, use, resist, technolog, use, use |
| Counterfactual_Target_Node_Neighbors | 37121, 37122, 37125 |
| Counterfactual_Target_Node_Features | use, use, born, bottl, classic, use, free, use, heat, high, none, skin, pack, use, use, resist, technolog, use, use |
| Factual_Target_Node_Class | Health & Personal Care |
| Counterfactual_Target_Node_class | Home & Kitchen |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 992, 37123, 37124 |
| Natural_Language_Explanation | None |
