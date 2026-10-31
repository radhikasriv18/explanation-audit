# Reference packet: CF-GNNExplainer__Llama-8B__products__36811

- Method: CF-GNNExplainer; configuration: Llama-8B; dataset: products; target node: 36811
- Explanation source: `./llm-graph-cf/data/results/cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_products_standard_Response.json` ([138][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, we can fill in the dictionary as follows:

infos={
'Target_Node_ID': 36811,
'Factual_Target_Node_Neighbors': [8361],
'Factual_Target_Node_Features': ['use', 'never', 'choic', 'comfort', 'cotton', 'cover', 'design', 'dust', 'ever', 'finest', 'first', 'year', 'healthi', 'high', 'like', 'keep', 'life', 'made', 'mask', 'materi', 'maximum', 'microfib', 'modern', 'one', 'organ', 'text', 'pink', 'protect', 'provid', 'relief', 'reusabl', 'stay', 'style', 'stylish', 'tech', 'want', 'whether', 'world'],
'Counterfactual_Target_Node_Neighbors': [8361],
'Counterfactual_Target_Node_Features': ['use', 'never', 'choic', 'comfort', 'cotton', 'cover', 'design', 'dust', 'ever', 'finest', 'first', 'year', 'healthi', 'high', 'like', 'keep', 'life', 'made', 'mask', 'materi', 'maximum', 'microfib', 'modern', 'one', 'organ', 'text', 'pink', 'protect', 'provid', 'relief', 'reusabl', 'stay', 'style', 'stylish', 'tech', 'want', 'whether', 'world'],
'Factual_Target_Node_Class': 'Health & Personal Care',
'Counterfactual_Target_Node_class': 'Sports & Outdoors',
'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
'Natural_Language_Explanation': 'The target node 36811, which is a Vogmask Microfiber Filtering Mask: Pink Roses, was initially classified as Health & Personal Care but changed to Sports & Outdoors in the counterfactual scenario. This change is likely due to the removal or addition of certain keywords in the product title or description that influenced the model\'s classification decision.'
}

The target node 36811, which is a Vogmask Microfiber Filtering Mask: Pink Roses, was initially classified as Health & Personal Care but changed to Sports & Outdoors in the counterfactual scenario. This change is likely due to the removal or addition of certain keywords in the product title or description that influenced the model's classification decision.

Upon analyzing the neighbors of the target node, we can see that the only neighbor in both the factual and counterfactual scenarios is node 8361, which is a Child Life Liquid Calcium/Magnesium product. However, the classification of node 8361 remains unchanged in both scenarios, indicating that the influence of node 8361 on the target node's classification is minimal.

The change in classification of the target node is more likely due to the changes in its own features rather than the changes in its neighbors. In the counterfactual scenario, the target node's features remain the same as in the factual scenario, indicating that there were no changes made to the target node's features that would have influenced the model's classification decision.

However, upon closer inspection, we can see that the target node's category changed from Health & Personal Care to Sports & Outdoors in the counterfactual scenario. This suggests that the model's classification decision was influenced by the removal or addition of certain keywords in the product title or description that are more relevant to the Sports & Outdoors category.

To further investigate this, we can analyze the features of the target node in both scenarios. In the factual scenario, the target node has features such as 'use', 'never', 'choic', 'comfort', 'cotton', 'cover', 'design', 'dust', 'ever', 'finest', 'first', 'year', 'healthi', 'high', 'like', 'keep', 'life', 'made', 'mask', 'materi', 'maximum', 'microfib', 'modern', 'one', 'organ', 'text', 'pink', 'protect', 'provid', 'relief', 'reusabl', 'stay', 'style', 'stylish', 'tech', 'want', 'whether', 'world'. These features are more relevant to the Sports & Outdoors category.

In contrast, the counterfactual scenario has the same features as the factual scenario, indicating that there were no changes made to the target node's features that would have influenced the model's classification decision.

Therefore, the change in classification of the target node is likely due to the removal or addition of certain keywords in the product title or description that are more relevant to the Sports & Outdoors category.
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
given the factual graph: The node 983 is a product titled 'Child Life Probiotics Plus Colostrum Chewable Tablets, Mixed Berry Flavor, 90 Count' with key attributes: capsul, use, child, contain, count, flavor, health, includ, life, one, plu, support, system, tablet, also and is connected with the node 8361 and it is classified as Health & Personal Care, it is not the target node. The node 8361 is a product titled 'Child Life Liquid Calcium/Magnesium,Natural Orange Flavor Plastic Bottle, 16-Fl. Oz.' with key attributes: inch, use, well, balanc, bodi, bone, bottl, child, combin, develop, essenti, moistur, flavor, formula, found, foundat, great, growth, healthi, help, life, liquid, miner, one, natur, orang, skin, plastic, primari, provid, requir, read, support, teeth, book, total, two, vitamin, weight and is connected with the nodes 983, 8389, 36810, 36811, 36812, 36813, 36814 and it is classified as Health & Personal Care, it is not the target node. The node 8389 is a product titled 'Amerifit Culturelle Probiotics for Kids, 30 Count' with key attributes: made, day, actual, add, use, bacteria, balanc, benefit, better, child, cool, count, develop, easi, especi, free, ga, good, happi, healthi, help, keep, kid, like, liquid, littl, one, natur, ndash, parent, proven, reduc, rsquo, scienc, make, support, system, take, taken, book, work and is connected with the node 8361 and it is classified as Health & Personal Care, it is not the target node. The node 36810 is a product titled 'thinkbaby BPA Free Cereal Bowl, Orange' with key attributes: adult, year, also, use, well, begin, design, easi, food, free, grade, interior, item, one, lead, lid, made, orang, perfect, exampl, set, slightli, make, solid, stainless, steel, mani, first, toxic and is connected with the node 8361 and it is classified as Health & Personal Care, it is not the target node. The node 36811 is a product titled 'Vogmask Microfiber Filtering Mask: Pink Roses' with key attributes: use, never, choic, comfort, cotton, cover, design, dust, ever, finest, first, year, healthi, high, like, keep, life, made, mask, materi, maximum, microfib, modern, one, organ, text, pink, protect, provid, relief, reusabl, stay, style, stylish, tech, want, whether, world and is connected with the node 8361 and it is classified as Health & Personal Care, it is the target node. The node 36812 is a product titled 'La Mer The Eye Concentrate 3ml x 5 = 15ml' with key attributes: use, book, appear, dark, eye, que, line, treatment, wrinkl and is connected with the node 8361 and it is classified as Beauty, it is not the target node. The node 36813 is a product titled 'Thermos FUNtainer Stainless Steel 10 oz Leak-Proof Straw Bottle - Mickey Mouse' with key attributes: inch, use, bottl, skin, proof, stainless, steel and is connected with the node 8361 and it is classified as Health & Personal Care, it is not the target node. The node 36814 is a product titled 'Aveeno Eczema Therapy  Bath Treatment, 3 Count (Pack of 2)' with key attributes: made, capsul, activ, also, use, well, bath, beauti, count, discov, dri, effect, essenti, formul, gentli, health, long, natur, year, pack, pure, recommend, sensit, skin, smooth, soft, may, sooth, mani, therapi, treat, treatment, unlik and is connected with the node 8361 and it is classified as Beauty, it is not the target node. and given the counterfactual example: The node 983 is a product titled 'Child Life Probiotics Plus Colostrum Chewable Tablets, Mixed Berry Flavor, 90 Count' with key attributes: capsul, use, child, contain, count, flavor, health, includ, life, one, plu, support, system, tablet, also and is connected with the node 8361 and it is classified as Health & Personal Care, it is not the target node. The node 8361 is a product titled 'Child Life Liquid Calcium/Magnesium,Natural Orange Flavor Plastic Bottle, 16-Fl. Oz.' with key attributes: inch, use, well, balanc, bodi, bone, bottl, child, combin, develop, essenti, moistur, flavor, formula, found, foundat, great, growth, healthi, help, life, liquid, miner, one, natur, orang, skin, plastic, primari, provid, requir, read, support, teeth, book, total, two, vitamin, weight and is connected with the nodes 983, 8389, 36810, 36812, 36813, 36814 and it is classified as Health & Personal Care, it is not the target node. The node 8389 is a product titled 'Amerifit Culturelle Probiotics for Kids, 30 Count' with key attributes: made, day, actual, add, use, bacteria, balanc, benefit, better, child, cool, count, develop, easi, especi, free, ga, good, happi, healthi, help, keep, kid, like, liquid, littl, one, natur, ndash, parent, proven, reduc, rsquo, scienc, make, support, system, take, taken, book, work and is connected with the node 8361 and it is classified as Health & Personal Care, it is not the target node. The node 36810 is a product titled 'thinkbaby BPA Free Cereal Bowl, Orange' with key attributes: adult, year, also, use, well, begin, design, easi, food, free, grade, interior, item, one, lead, lid, made, orang, perfect, exampl, set, slightli, make, solid, stainless, steel, mani, first, toxic and is connected with the node 8361 and it is classified as Health & Personal Care, it is not the target node. The node 36811 is a product titled 'Vogmask Microfiber Filtering Mask: Pink Roses' with key attributes: use, never, choic, comfort, cotton, cover, design, dust, ever, finest, first, year, healthi, high, like, keep, life, made, mask, materi, maximum, microfib, modern, one, organ, text, pink, protect, provid, relief, reusabl, stay, style, stylish, tech, want, whether, world and is connected with no other nodes and it is classified as Sports & Outdoors, it is the target node. The node 36812 is a product titled 'La Mer The Eye Concentrate 3ml x 5 = 15ml' with key attributes: use, book, appear, dark, eye, que, line, treatment, wrinkl and is connected with the node 8361 and it is classified as Beauty, it is not the target node. The node 36813 is a product titled 'Thermos FUNtainer Stainless Steel 10 oz Leak-Proof Straw Bottle - Mickey Mouse' with key attributes: inch, use, bottl, skin, proof, stainless, steel and is connected with the node 8361 and it is classified as Health & Personal Care, it is not the target node. The node 36814 is a product titled 'Aveeno Eczema Therapy  Bath Treatment, 3 Count (Pack of 2)' with key attributes: made, capsul, activ, also, use, well, bath, beauti, count, discov, dri, effect, essenti, formul, gentli, health, long, natur, year, pack, pure, recommend, sensit, skin, smooth, soft, may, sooth, mani, therapi, treat, treatment, unlik and is connected with the node 8361 and it is classified as Beauty, it is not the target node.
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

- ID: 36811
- Title: Vogmask Microfiber Filtering Mask: Pink Roses
- True class (canonical `y`): **Beauty**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Health & Personal Care**
- Prediction recorded by this method's pipeline: **Health & Personal Care**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Vogmask Microfiber Filtering Mask: Pink Roses. Content: Stay healthy and keep airborne particles out of your lungs with Vogmask, the first dust masks designed to be stylish, comfortable and reusable. With the choice of high-tech microfiber or organic cotton, these comfortable, reusable masks combine protection and style like never before. Whether you seek shelter from the perils of modern life or just want relief from allergies, Vogmask has you covered. Vogmask is the world's first stylish filtering dust mask, made from the finest materials and designed to be the most comfortable dust mask ever while providing maximum protection from airborne particles.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 8361 | Health & Personal Care | Child Life Liquid Calcium/Magnesium,Natural Orange Flavor Plastic Bottle, 16-Fl. Oz. |

### 2-hop (shortest distance exactly 2): 6 nodes

| node id | true class | title |
|---|---|---|
| 983 | Health & Personal Care | Child Life Probiotics Plus Colostrum Chewable Tablets, Mixed Berry Flavor, 90 Count |
| 8389 | Health & Personal Care | Amerifit Culturelle Probiotics for Kids, 30 Count |
| 36810 | Baby | thinkbaby BPA Free Cereal Bowl, Orange |
| 36812 | Beauty | La Mer The Eye Concentrate 3ml x 5 = 15ml |
| 36813 | Baby | Thermos FUNtainer Stainless Steel 10 oz Leak-Proof Straw Bottle - Mickey Mouse |
| 36814 | Beauty | Aveeno Eczema Therapy  Bath Treatment, 3 Count (Pack of 2) |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/products/cf-gnnexplainer-canonical/random_seed_42_*` (key=138).

- Factual class: **Health & Personal Care**
- Counterfactual class: **Sports & Outdoors**
- Removed edges (global ids, 1): (8361, 36811)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 36811 |
| Factual_Target_Node_Neighbors | 8361 |
| Factual_Target_Node_Features | use, use, use, never, choic, comfort, use, cotton, cover, design, dust, ever, finest, first, use, year, healthi, high, use, like, keep, life, like, made, mask, materi, maximum, microfib, modern, one, never, use, use, organ, text, pink, use, use, protect, provid, relief, reusabl, stay, style, stylish, tech, use, use, use, use, want, whether, provid, use, world, use, use |
| Counterfactual_Target_Node_Neighbors |  |
| Counterfactual_Target_Node_Features | use, use, use, never, choic, comfort, use, cotton, cover, design, dust, ever, finest, first, use, year, healthi, high, use, like, keep, life, like, made, mask, materi, maximum, microfib, modern, one, never, use, use, organ, text, pink, use, use, protect, provid, relief, reusabl, stay, style, stylish, tech, use, use, use, use, want, whether, provid, use, world, use, use |
| Factual_Target_Node_Class | Health & Personal Care |
| Counterfactual_Target_Node_class | Sports & Outdoors |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 8361 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 36811 |
| Factual_Target_Node_Neighbors | 8361 |
| Factual_Target_Node_Features | use, use, use, never, choic, comfort, use, cotton, cover, design, dust, ever, finest, first, use, year, healthi, high, use, like, keep, life, like, made, mask, materi, maximum, microfib, modern, one, never, use, use, organ, text, pink, use, use, protect, provid, relief, reusabl, stay, style, stylish, tech, use, use, use, use, want, whether, provid, use, world, use, use |
| Counterfactual_Target_Node_Neighbors |  |
| Counterfactual_Target_Node_Features | use, use, use, never, choic, comfort, use, cotton, cover, design, dust, ever, finest, first, use, year, healthi, high, use, like, keep, life, like, made, mask, materi, maximum, microfib, modern, one, never, use, use, organ, text, pink, use, use, protect, provid, relief, reusabl, stay, style, stylish, tech, use, use, use, use, want, whether, provid, use, world, use, use |
| Factual_Target_Node_Class | Health & Personal Care |
| Counterfactual_Target_Node_class | Sports & Outdoors |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 8361 |
| Natural_Language_Explanation | None |
