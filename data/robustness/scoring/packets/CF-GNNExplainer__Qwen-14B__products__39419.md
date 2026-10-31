# Reference packet: CF-GNNExplainer__Qwen-14B__products__39419

- Method: CF-GNNExplainer; configuration: Qwen-14B; dataset: products; target node: 39419
- Explanation source: `./robustness_2026-10-30/production_a100/qwen14b_gptq_int4_products_Response.json` ([147][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
To address the task, we will fill the `infos` dictionary based on the provided factual and counterfactual examples, and then provide a natural language explanation for the change in classification.

### Filling the Dictionary

```python
infos = {
    'Target_Node_ID': '39419',
    'Factual_Target_Node_Neighbors': ['9135'],
    'Factual_Target_Node_Features': ['inch', 'year', 'deflockedst', 'calib', 'dimens', 'adult', 'air', 'one', 'use', 'approxim', 'area', 'well', 'assembl', 'attach', 'attract', 'stori', 'bottom', 'built', 'children', 'clean', 'cloth', 'come', 'cotton', 'dri', 'extra', 'fabric', 'finish', 'floor', 'friend', 'fun', 'gentl', 'hand', 'want', 'illustr', 'includ', 'instruct', 'item', 'like', 'machin', 'made', 'may', 'measur', 'need', 'never', 'non', 'old', 'also', 'origin', 'qualiti', 'overal', 'part', 'pet', 'photo', 'pink', 'real', 'recommend', 'remov', 'requir', 'rest', 'right', 'size', 'spot', 'style', 'three', 'top', 'toxic', 'toy', 'two', 'make', 'visit', 'wash', 'white', 'wood'],
    'Counterfactual_Target_Node_Neighbors': ['9135'],
    'Counterfactual_Target_Node_Features': ['inch', 'year', 'deflockedst', 'calib', 'dimens', 'adult', 'air', 'one', 'use', 'approxim', 'area', 'well', 'assembl', 'attach', 'attract', 'stori', 'bottom', 'built', 'children', 'clean', 'cloth', 'come', 'cotton', 'dri', 'extra', 'fabric', 'finish', 'floor', 'friend', 'fun', 'gentl', 'hand', 'want', 'illustr', 'includ', 'instruct', 'item', 'like', 'machin', 'made', 'may', 'measur', 'need', 'never', 'non', 'old', 'also', 'origin', 'qualiti', 'overal', 'part', 'pet', 'photo', 'pink', 'real', 'recommend', 'remov', 'requir', 'rest', 'right', 'size', 'spot', 'style', 'three', 'top', 'toxic', 'toy', 'two', 'make', 'visit', 'wash', 'white', 'wood'],
    'Factual_Target_Node_Class': 'Toys & Games',
    'Counterfactual_Target_Node_class': 'Arts, Crafts & Sewing',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Natural_Language_Explanation': ''
}
```

### Explanation of Changes

In the factual scenario, the target node (node 39419) is classified as "Toys & Games." In the counterfactual scenario, the same node is reclassified as "Arts, Crafts & Sewing."

#### Key Differences:

1. **Node Connections**:
   - In the factual graph, node 39419 is connected only to node 9135.
   - In the counterfactual graph, node 39419 remains connected only to node 9135.

2. **Node Features**:
   - The features of node 39419 remain unchanged between the factual and counterfactual scenarios.

3. **Classification Change**:
   - Despite the unchanged connections and features, the classification of node 39419 shifts from "Toys & Games" to "Arts, Crafts & Sewing."

#### Influence of Neighbors:

- **Node 9135**: This node is a product titled 'American Girl Starry 2 Doll Tote Bag' and is classified as "Toys & Games." It is connected to multiple nodes, including the target node 39419. However, the classification of node 9135 does not change across the factual and counterfactual scenarios.

Given these observations, the change in classification appears to be driven by factors beyond just the direct connections and features of the target node itself. Possible reasons include:

- **Contextual Influence**: The overall context of the graph might influence the classification. For instance, if there are other nodes in the vicinity that are more closely associated with "Arts, Crafts & Sewing," the model might infer that the target node should belong to this category.
  
- **Model Interpretation**: The machine learning model might weigh the importance of certain features differently in the counterfactual scenario, leading to a different prediction despite identical features and connections.

### Natural Language Explanation

The target node (node 39419) was originally classified as "Toys & Games" in the factual scenario. In the counterfactual scenario, the same node is reclassified as "Arts, Crafts & Sewing." Notably, the features and connections of the target node did not change. The shift in classification suggests that the model's decision-making process is influenced by broader contextual factors within the graph. Specifically, the model might be considering the overall context of the graph, where nodes connected to the target node or nearby nodes might have a stronger association with "Arts, Crafts & Sewing," leading to a reclassification of the target node. This highlights the importance of understanding the broader context and dependencies within the graph when interpreting model predictions.
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
given the factual graph: The node 1089 is a product titled '18 Inch Doll Backpack, Doll Size for 18&quot; Doll Accessories and American Girl Dolls in Purple Nylon, Zippered Opening' with key attributes: inch, llc, accessori, one, allow, use, american, girl, take, book, nylon, open, stori, plush, pocket, purpl, quot, reserv, size, toy and is connected with the node 9135 and it is classified as Toys & Games, it is not the target node. The node 9135 is a product titled 'American Girl Starry 2 Doll Tote Bag' with key attributes: inch, accessori, use, american, bag, exterior, extra, fabric, girl, take, year, hold, nylon, perfect, plenti, pocket, room, two and is connected with the nodes 1089, 39346, 39417, 39418, 39419, 39420 and it is classified as Toys & Games, it is not the target node. The node 39346 is a product titled '3 PC. Gymnastics Leotard, Jacket, and Bag, Doll Gymnastics Outfit Fits 18&quot; Dolls Like American Girl' with key attributes: inch, llc, one, use, american, time, bag, easi, fit, girl, hook, includ, like, usb, piec, quot, reserv, set, stylish, top and is connected with the node 9135 and it is classified as Toys & Games, it is not the target node. The node 39417 is a product titled 'missing' with key attributes: book, action, age, also, although, alway, use, art, artist, well, time, away, year, believ, best, one, chanc, chang, charact, complet, cut, like, due, even, everyon, fact, film, find, friend, good, import, job, learn, local, made, middl, miss, music, new, older, plot, point, program, save, school, live, may, take, make, first, know, provid and is connected with the node 9135 and it is classified as Movies & TV, it is not the target node. The node 39418 is a product titled 'Doll Bicycle Seat - &quot;Ride Along Dolly&quot; Bike Seat with Decorate Yourself Decals (Fits 18&quot; American Girl an' with key attributes: inch, ad, one, along, also, use, american, anim, around, well, time, attach, bar, belt, brightli, come, compani, design, take, like, easi, fill, fit, found, fun, gift, girl, good, book, hole, home, want, includ, lb, leav, longer, love, matter, name, note, perfect, perform, pink, quot, rear, safe, show, size, make, standard, mani, super, year, uniqu, virtual, way, without, work, young, check and is connected with the node 9135 and it is classified as Toys & Games, it is not the target node. The node 39419 is a product titled 'Badger Basket Doll Bunk Beds With Ladder - Pink/White' with key attributes: inch, year, deflockedst, calib, dimens, adult, air, one, use, approxim, area, well, assembl, attach, attract, stori, bottom, built, children, clean, cloth, come, cotton, dri, extra, fabric, finish, floor, friend, fun, gentl, hand, want, illustr, includ, instruct, item, like, machin, made, may, measur, need, never, non, old, also, origin, qualiti, overal, part, pet, photo, pink, real, recommend, remov, requir, rest, right, size, spot, style, three, top, toxic, toy, two, make, visit, wash, white, wood and is connected with the node 9135 and it is classified as Toys & Games, it is the target node. The node 39420 is a product titled 'Red and Yellow Roses Dress &amp; Sandals ~ Fits 18&quot; American Girl Dolls' with key attributes: inch, accessori, use, american, amp, book, time, eleg, fit, floor, girl, match, pair, perfect, quot, red, yellow and is connected with the node 9135 and it is classified as Toys & Games, it is not the target node. and given the counterfactual example: The node 1089 is a product titled '18 Inch Doll Backpack, Doll Size for 18&quot; Doll Accessories and American Girl Dolls in Purple Nylon, Zippered Opening' with key attributes: inch, llc, accessori, one, allow, use, american, girl, take, book, nylon, open, stori, plush, pocket, purpl, quot, reserv, size, toy and is connected with the node 9135 and it is classified as Toys & Games, it is not the target node. The node 9135 is a product titled 'American Girl Starry 2 Doll Tote Bag' with key attributes: inch, accessori, use, american, bag, exterior, extra, fabric, girl, take, year, hold, nylon, perfect, plenti, pocket, room, two and is connected with the nodes 1089, 39419 and it is classified as Toys & Games, it is not the target node. The node 39346 is a product titled '3 PC. Gymnastics Leotard, Jacket, and Bag, Doll Gymnastics Outfit Fits 18&quot; Dolls Like American Girl' with key attributes: inch, llc, one, use, american, time, bag, easi, fit, girl, hook, includ, like, usb, piec, quot, reserv, set, stylish, top and is connected with no other nodes and it is classified as Toys & Games, it is not the target node. The node 39417 is a product titled 'missing' with key attributes: book, action, age, also, although, alway, use, art, artist, well, time, away, year, believ, best, one, chanc, chang, charact, complet, cut, like, due, even, everyon, fact, film, find, friend, good, import, job, learn, local, made, middl, miss, music, new, older, plot, point, program, save, school, live, may, take, make, first, know, provid and is connected with no other nodes and it is classified as Movies & TV, it is not the target node. The node 39418 is a product titled 'Doll Bicycle Seat - &quot;Ride Along Dolly&quot; Bike Seat with Decorate Yourself Decals (Fits 18&quot; American Girl an' with key attributes: inch, ad, one, along, also, use, american, anim, around, well, time, attach, bar, belt, brightli, come, compani, design, take, like, easi, fill, fit, found, fun, gift, girl, good, book, hole, home, want, includ, lb, leav, longer, love, matter, name, note, perfect, perform, pink, quot, rear, safe, show, size, make, standard, mani, super, year, uniqu, virtual, way, without, work, young, check and is connected with no other nodes and it is classified as Toys & Games, it is not the target node. The node 39419 is a product titled 'Badger Basket Doll Bunk Beds With Ladder - Pink/White' with key attributes: inch, year, deflockedst, calib, dimens, adult, air, one, use, approxim, area, well, assembl, attach, attract, stori, bottom, built, children, clean, cloth, come, cotton, dri, extra, fabric, finish, floor, friend, fun, gentl, hand, want, illustr, includ, instruct, item, like, machin, made, may, measur, need, never, non, old, also, origin, qualiti, overal, part, pet, photo, pink, real, recommend, remov, requir, rest, right, size, spot, style, three, top, toxic, toy, two, make, visit, wash, white, wood and is connected with the node 9135 and it is classified as Arts, Crafts & Sewing, it is the target node. The node 39420 is a product titled 'Red and Yellow Roses Dress &amp; Sandals ~ Fits 18&quot; American Girl Dolls' with key attributes: inch, accessori, use, american, amp, book, time, eleg, fit, floor, girl, match, pair, perfect, quot, red, yellow and is connected with no other nodes and it is classified as Toys & Games, it is not the target node.
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

- ID: 39419
- Title: Badger Basket Doll Bunk Beds With Ladder - Pink/White
- True class (canonical `y`): **Toys & Games**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Toys & Games**
- Prediction recorded by this method's pipeline: **Toys & Games**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Badger Basket Doll Bunk Beds With Ladder - Pink/White. Content: Just right when doll friends come to visit. Our Doll Bunk Beds are built for two dolls to rest in style. Includes a ladder for extra fun and realism. Pretty pink gingham complements the attractive white finish. For Dolls up to 20" . Overall size of 11.5" x 22.25" x 15" . There is 6.75" clearance between the top and bottom bunks and 3.5" distance between the bottom bunk and the floor. Includes two removable mattresses (21.25" x 10" ) with attached pillows and eyelet trim. Pillow area of the mattress is approximately 3.5" x 10" . Ladder measures approximately 15" x 5" x 3/8" D. Can be enjoyed by children from three years old and up. All paints and finishes are non-toxic. Some adult assembly required. Illustrated instructions included. Made with wood and wood composites. Fabric parts are poly/cotton and stuffed with polyfill. Wipe wood parts clean with a damp cloth and mild detergent as needed. For longevity of the product, spot cleaning or hand washing recommended for the fabric parts (but you can machine wash gentle and air dry if desired). This item is a toy for use with dolls only. It is never to be used with real infants or pets. This item ships in its original carton which may include a photo of the product.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 9135 | Toys & Games | American Girl Starry 2 Doll Tote Bag |

### 2-hop (shortest distance exactly 2): 5 nodes

| node id | true class | title |
|---|---|---|
| 1089 | Toys & Games | 18 Inch Doll Backpack, Doll Size for 18&quot; Doll Accessories and American Girl Dolls in Purple Nylon, Zippered Opening and Pocket in Purple |
| 39346 | Toys & Games | 3 PC. Gymnastics Leotard, Jacket, and Bag, Doll Gymnastics Outfit Fits 18&quot; Dolls Like American Girl |
| 39417 | Movies & TV | missing |
| 39418 | Toys & Games | Doll Bicycle Seat - &quot;Ride Along Dolly&quot; Bike Seat with Decorate Yourself Decals (Fits 18&quot; American Girl and Standard Sized Dolls and Stuffed Animals) |
| 39420 | Toys & Games | Red and Yellow Roses Dress &amp; Sandals ~ Fits 18&quot; American Girl Dolls |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/products/cf-gnnexplainer-canonical/random_seed_42_*` (key=147).

- Factual class: **Toys & Games**
- Counterfactual class: **Arts, Crafts & Sewing**
- Removed edges (global ids, 4): (9135, 39346), (9135, 39417), (9135, 39418), (9135, 39420)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 39419 |
| Factual_Target_Node_Neighbors | 9135 |
| Factual_Target_Node_Features | inch, inch, inch, year, deflockedst, calib, inch, dimens, adult, air, one, use, use, approxim, use, area, well, assembl, attach, attract, use, stori, bottom, built, one, use, use, children, clean, clean, cloth, come, use, cotton, dri, extra, fabric, finish, floor, use, friend, use, fun, gentl, hand, want, illustr, use, includ, includ, includ, instruct, use, use, item, one, like, machin, made, may, measur, need, never, non, use, old, also, use, origin, qualiti, overal, part, pet, photo, pink, use, use, real, recommend, remov, requir, rest, right, size, may, spot, style, use, like, use, three, use, use, top, toxic, toy, two, make, use, use, visit, wash, one, also, white, use, wood, year, use |
| Counterfactual_Target_Node_Neighbors | 9135 |
| Counterfactual_Target_Node_Features | inch, inch, inch, year, deflockedst, calib, inch, dimens, adult, air, one, use, use, approxim, use, area, well, assembl, attach, attract, use, stori, bottom, built, one, use, use, children, clean, clean, cloth, come, use, cotton, dri, extra, fabric, finish, floor, use, friend, use, fun, gentl, hand, want, illustr, use, includ, includ, includ, instruct, use, use, item, one, like, machin, made, may, measur, need, never, non, use, old, also, use, origin, qualiti, overal, part, pet, photo, pink, use, use, real, recommend, remov, requir, rest, right, size, may, spot, style, use, like, use, three, use, use, top, toxic, toy, two, make, use, use, visit, wash, one, also, white, use, wood, year, use |
| Factual_Target_Node_Class | Toys & Games |
| Counterfactual_Target_Node_class | Arts, Crafts & Sewing |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 39419 |
| Factual_Target_Node_Neighbors | 9135 |
| Factual_Target_Node_Features | inch, inch, inch, year, deflockedst, calib, inch, dimens, adult, air, one, use, use, approxim, use, area, well, assembl, attach, attract, use, stori, bottom, built, one, use, use, children, clean, clean, cloth, come, use, cotton, dri, extra, fabric, finish, floor, use, friend, use, fun, gentl, hand, want, illustr, use, includ, includ, includ, instruct, use, use, item, one, like, machin, made, may, measur, need, never, non, use, old, also, use, origin, qualiti, overal, part, pet, photo, pink, use, use, real, recommend, remov, requir, rest, right, size, may, spot, style, use, like, use, three, use, use, top, toxic, toy, two, make, use, use, visit, wash, one, also, white, use, wood, year, use |
| Counterfactual_Target_Node_Neighbors | 9135 |
| Counterfactual_Target_Node_Features | inch, inch, inch, year, deflockedst, calib, inch, dimens, adult, air, one, use, use, approxim, use, area, well, assembl, attach, attract, use, stori, bottom, built, one, use, use, children, clean, clean, cloth, come, use, cotton, dri, extra, fabric, finish, floor, use, friend, use, fun, gentl, hand, want, illustr, use, includ, includ, includ, instruct, use, use, item, one, like, machin, made, may, measur, need, never, non, use, old, also, use, origin, qualiti, overal, part, pet, photo, pink, use, use, real, recommend, remov, requir, rest, right, size, may, spot, style, use, like, use, three, use, use, top, toxic, toy, two, make, use, use, visit, wash, one, also, white, use, wood, year, use |
| Factual_Target_Node_Class | Toys & Games |
| Counterfactual_Target_Node_class | Arts, Crafts & Sewing |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |
