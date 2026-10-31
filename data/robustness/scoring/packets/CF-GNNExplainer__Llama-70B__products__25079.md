# Reference packet: CF-GNNExplainer__Llama-70B__products__25079

- Method: CF-GNNExplainer; configuration: Llama-70B; dataset: products; target node: 25079
- Explanation source: `./robustness_2026-10-30/llama70b/cf/products/25079.json` (response)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, we can fill the dictionary as follows:

infos = {
    'Target_Node_ID': 25079,
    'Factual_Target_Node_Neighbors': [4884],
    'Factual_Target_Node_Features': ['book', 'allow', 'also', 'use', 'well', 'away', 'better', 'one', 'dog', 'featur', 'full', 'function', 'half', 'year', 'man', 'humor', 'littl', 'lo', 'movi', 'text', 'race', 'romant', 'see', 'set', 'sexi', 'live', 'team', 'tough', 'travel', 'know', 'whole', 'make', 'young'],
    'Counterfactual_Target_Node_Neighbors': [],
    'Counterfactual_Target_Node_Features': ['book', 'allow', 'also', 'use', 'well', 'away', 'better', 'one', 'dog', 'featur', 'full', 'function', 'half', 'year', 'man', 'humor', 'littl', 'lo', 'movi', 'text', 'race', 'romant', 'see', 'set', 'sexi', 'live', 'team', 'tough', 'travel', 'know', 'whole', 'make', 'young'],
    'Factual_Target_Node_Class': 'Movies & TV',
    'Counterfactual_Target_Node_class': 'Books',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Node_Differences': [25079],
    'Edge_Differences': [(25079, 4884)],
    'Natural_Language_Explanation': 'The product "Chilly Dogs" was initially classified as "Movies & TV" but was reclassified as "Books" after removing its connection with the node "Snow Dogs" (4884). This change suggests that the co-purchase relationship with "Snow Dogs" was influencing the classification of "Chilly Dogs" towards "Movies & TV". Without this connection, the features of "Chilly Dogs" are more aligned with the "Books" category.'
}

Explanation:

The target node 25079, "Chilly Dogs", was initially classified as "Movies & TV" due to its connection with node 4884, "Snow Dogs". However, after removing this connection, the node was reclassified as "Books". This change suggests that the co-purchase relationship with "Snow Dogs" was influencing the classification of "Chilly Dogs" towards "Movies & TV".

The features of "Chilly Dogs" remain the same in both the factual and counterfactual scenarios, indicating that the change in classification is primarily due to the removal of the edge with "Snow Dogs". This highlights the importance of considering the graph structure and co-purchase relationships when classifying products.

In the counterfactual scenario, the node "Chilly Dogs" is no longer connected to any other nodes, which allows its features to be evaluated independently. In this case, the features of "Chilly Dogs" are more aligned with the "Books" category, leading to the reclassification.

The influence of neighboring nodes, particularly "Snow Dogs", played a significant role in the initial classification of "Chilly Dogs" as "Movies & TV". The removal of this connection allowed the true characteristics of "Chilly Dogs" to be revealed, leading to a more accurate classification as "Books".
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
given the factual graph: The node 545 is a product titled 'missing' with key attributes: action, adventur, air, use, anoth, appear, well, back, year, never, one, disney, dog, enjoy, everyon, famili, favorit, fill, find, fun, golden, book, howev, late, lead, made, major, miss, natur, new, take, text, player, play, plenti, point, pro, real, season, serv, show, make, special, sport, stop, stori, sun, sure, like, time, much, condit and is connected with the nodes 551, 4884 and it is classified as Movies & TV, it is not the target node. The node 550 is a product titled 'Inspector Gadget' with key attributes: use and is connected with the node 4884 and it is classified as Movies & TV, it is not the target node. The node 551 is a product titled 'Air Bud Spikes Back' with key attributes: action, adventur, air, one, use, book, appear, well, back, year, disney, everyon, famili, favorit, fill, fun, golden, lead, new, take, play, pleas, plenti, point, pro, real, serv, make, special, sport, stori, sun, sure, like, time, condit and is connected with the nodes 545, 4884 and it is classified as Movies & TV, it is not the target node. The node 4820 is a product titled 'missing' with key attributes: book, adult, age, one, also, alway, use, well, year, brother, charg, close, compel, cours, cute, disney, take, dog, done, easi, end, enough, famili, famou, father, film, find, first, forc, four, get, head, help, histor, home, want, import, includ, involv, like, later, learn, left, life, littl, look, love, make, miss, mission, month, new, often, older, stori, parent, particularli, plan, popular, power, collagen, proud, research, see, seem, show, shown, may, someth, star, style, mani, time, tough, travel, two, upon, virtual, know, provid, whose, winner, young and is connected with the node 4884 and it is classified as Movies & TV, it is not the target node. The node 4884 is a product titled 'Snow Dogs' with key attributes: book, action, use, well, away, best, one, challeng, death, discov, disney, dog, eight, famili, fish, fun, get, goe, good, human, ice, jack, jame, learn, leav, life, love, make, man, name, never, noth, old, also, text, pack, practic, race, rescu, seven, success, like, thin, two, water, whole and is connected with the nodes 545, 550, 551, 4820, 4915, 25078, 25079, 25080, 25081 and it is classified as Movies & TV, it is not the target node. The node 4915 is a product titled 'missing' with key attributes: book, action, adult, age, alik, one, along, also, use, anim, well, becam, best, big, bonu, children, christma, citi, dark, dog, done, especi, everyth, featur, film, find, first, found, friend, girl, give, year, import, includ, inspir, life, live, longer, miss, music, name, new, north, number, older, particularli, play, pop, power, collagen, get, richard, scene, search, may, someth, song, spirit, stori, style, make, read, togeth, work, york, young and is connected with the node 4884 and it is classified as Movies & TV, it is not the target node. The node 25078 is a product titled 'My Favorite Martian' with key attributes: use, favorit, read and is connected with the node 4884 and it is classified as Movies & TV, it is not the target node. The node 25079 is a product titled 'Chilly Dogs' with key attributes: book, allow, also, use, well, away, better, one, dog, featur, full, function, half, year, man, humor, littl, lo, movi, text, race, romant, see, set, sexi, live, team, tough, travel, know, whole, make, young and is connected with the node 4884 and it is classified as Movies & TV, it is the target node. The node 25080 is a product titled 'missing' with key attributes: year, use, anoth, audio, best, bonu, busi, care, cast, children, david, deal, director, dog, take, famili, featur, fill, friend, funni, green, one, heart, import, includ, john, lead, life, live, minut, miss, old, produc, get, realli, scene, seven, may, star, book, make, turn, two, understand, know, provid, writer and is connected with the node 4884 and it is classified as Movies & TV, it is not the target node. The node 25081 is a product titled 'Eight Below (Widescreen Edition)' with key attributes: action, adventur, amaz, use, book, anoth, time, stori, disney, dog, war, edit, eight, famili, guid, incred, journey, learn, make, one, must, noth, paul, pictur, planet, exampl, stop, tale, togeth, whole and is connected with the node 4884 and it is classified as Movies & TV, it is not the target node. and given the counterfactual example: The node 545 is a product titled 'missing' with key attributes: action, adventur, air, use, anoth, appear, well, back, year, never, one, disney, dog, enjoy, everyon, famili, favorit, fill, find, fun, golden, book, howev, late, lead, made, major, miss, natur, new, take, text, player, play, plenti, point, pro, real, season, serv, show, make, special, sport, stop, stori, sun, sure, like, time, much, condit and is connected with the nodes 551, 4884 and it is classified as Movies & TV, it is not the target node. The node 550 is a product titled 'Inspector Gadget' with key attributes: use and is connected with the node 4884 and it is classified as Movies & TV, it is not the target node. The node 551 is a product titled 'Air Bud Spikes Back' with key attributes: action, adventur, air, one, use, book, appear, well, back, year, disney, everyon, famili, favorit, fill, fun, golden, lead, new, take, play, pleas, plenti, point, pro, real, serv, make, special, sport, stori, sun, sure, like, time, condit and is connected with the nodes 545, 4884 and it is classified as Movies & TV, it is not the target node. The node 4820 is a product titled 'missing' with key attributes: book, adult, age, one, also, alway, use, well, year, brother, charg, close, compel, cours, cute, disney, take, dog, done, easi, end, enough, famili, famou, father, film, find, first, forc, four, get, head, help, histor, home, want, import, includ, involv, like, later, learn, left, life, littl, look, love, make, miss, mission, month, new, often, older, stori, parent, particularli, plan, popular, power, collagen, proud, research, see, seem, show, shown, may, someth, star, style, mani, time, tough, travel, two, upon, virtual, know, provid, whose, winner, young and is connected with the node 4884 and it is classified as Movies & TV, it is not the target node. The node 4884 is a product titled 'Snow Dogs' with key attributes: book, action, use, well, away, best, one, challeng, death, discov, disney, dog, eight, famili, fish, fun, get, goe, good, human, ice, jack, jame, learn, leav, life, love, make, man, name, never, noth, old, also, text, pack, practic, race, rescu, seven, success, like, thin, two, water, whole and is connected with the nodes 545, 550, 551, 4820, 4915, 25078, 25080, 25081 and it is classified as Movies & TV, it is not the target node. The node 4915 is a product titled 'missing' with key attributes: book, action, adult, age, alik, one, along, also, use, anim, well, becam, best, big, bonu, children, christma, citi, dark, dog, done, especi, everyth, featur, film, find, first, found, friend, girl, give, year, import, includ, inspir, life, live, longer, miss, music, name, new, north, number, older, particularli, play, pop, power, collagen, get, richard, scene, search, may, someth, song, spirit, stori, style, make, read, togeth, work, york, young and is connected with the node 4884 and it is classified as Movies & TV, it is not the target node. The node 25078 is a product titled 'My Favorite Martian' with key attributes: use, favorit, read and is connected with the node 4884 and it is classified as Movies & TV, it is not the target node. The node 25079 is a product titled 'Chilly Dogs' with key attributes: book, allow, also, use, well, away, better, one, dog, featur, full, function, half, year, man, humor, littl, lo, movi, text, race, romant, see, set, sexi, live, team, tough, travel, know, whole, make, young and is connected with no other nodes and it is classified as Books, it is the target node. The node 25080 is a product titled 'missing' with key attributes: year, use, anoth, audio, best, bonu, busi, care, cast, children, david, deal, director, dog, take, famili, featur, fill, friend, funni, green, one, heart, import, includ, john, lead, life, live, minut, miss, old, produc, get, realli, scene, seven, may, star, book, make, turn, two, understand, know, provid, writer and is connected with the node 4884 and it is classified as Movies & TV, it is not the target node. The node 25081 is a product titled 'Eight Below (Widescreen Edition)' with key attributes: action, adventur, amaz, use, book, anoth, time, stori, disney, dog, war, edit, eight, famili, guid, incred, journey, learn, make, one, must, noth, paul, pictur, planet, exampl, stop, tale, togeth, whole and is connected with the node 4884 and it is classified as Movies & TV, it is not the target node.
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

- ID: 25079
- Title: Chilly Dogs
- True class (canonical `y`): **Movies & TV**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Movies & TV**
- Prediction recorded by this method's pipeline: **Movies & TV**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Chilly Dogs. Content: The lovely snowy expanses of Alaska are the setting forChilly Dogs, a goofy comedy about a travel agency clerk (Skeet Ulrich,Scream,The Newton Boys) from Los Angeles who has to prove his mettle by racing a team of mismatched sled dogs from Anchorage to Nome. Only this will allow him to claim his grandfather's inheritance--and a wily lawyer (Leslie Nielsen, mugging shamelessly as usual) intends to claim that inheritance for himself by knocking the clerk out of the race. It's not surprising to see Ulrich in a movie full of clumsy, half-baked slapstick and bodily function humor, but why is Natasha Henstridge (Species,The Whole Nine Yards) thrown away as a bland romantic foil? Her intelligence and sexy/tough persona deserve better--she providesChilly Dogswith what little momentum it has. Also featuring Rik Mayall (The Young Ones).--Bret Fetzer
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 4884 | Movies & TV | Snow Dogs |

### 2-hop (shortest distance exactly 2): 8 nodes

| node id | true class | title |
|---|---|---|
| 545 | Movies & TV | missing |
| 550 | Movies & TV | Inspector Gadget |
| 551 | Movies & TV | Air Bud Spikes Back |
| 4820 | Movies & TV | missing |
| 4915 | Movies & TV | missing |
| 25078 | Movies & TV | My Favorite Martian |
| 25080 | Movies & TV | missing |
| 25081 | Movies & TV | Eight Below (Widescreen Edition) |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/products/cf-gnnexplainer-canonical/random_seed_42_*` (key=93).

- Factual class: **Movies & TV**
- Counterfactual class: **Books**
- Removed edges (global ids, 1): (4884, 25079)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 25079 |
| Factual_Target_Node_Neighbors | 4884 |
| Factual_Target_Node_Features | book, allow, also, use, use, use, well, away, better, one, use, use, dog, featur, use, use, full, function, half, year, book, man, man, book, humor, use, use, use, littl, lo, movi, use, use, littl, also, text, use, use, race, romant, see, set, sexi, live, team, use, use, use, use, use, tough, travel, know, book, whole, know, make, use, young |
| Counterfactual_Target_Node_Neighbors |  |
| Counterfactual_Target_Node_Features | book, allow, also, use, use, use, well, away, better, one, use, use, dog, featur, use, use, full, function, half, year, book, man, man, book, humor, use, use, use, littl, lo, movi, use, use, littl, also, text, use, use, race, romant, see, set, sexi, live, team, use, use, use, use, use, tough, travel, know, book, whole, know, make, use, young |
| Factual_Target_Node_Class | Movies & TV |
| Counterfactual_Target_Node_class | Books |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 4884 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 25079 |
| Factual_Target_Node_Neighbors | 4884 |
| Factual_Target_Node_Features | book, allow, also, use, use, use, well, away, better, one, use, use, dog, featur, use, use, full, function, half, year, book, man, man, book, humor, use, use, use, littl, lo, movi, use, use, littl, also, text, use, use, race, romant, see, set, sexi, live, team, use, use, use, use, use, tough, travel, know, book, whole, know, make, use, young |
| Counterfactual_Target_Node_Neighbors |  |
| Counterfactual_Target_Node_Features | book, allow, also, use, use, use, well, away, better, one, use, use, dog, featur, use, use, full, function, half, year, book, man, man, book, humor, use, use, use, littl, lo, movi, use, use, littl, also, text, use, use, race, romant, see, set, sexi, live, team, use, use, use, use, use, tough, travel, know, book, whole, know, make, use, young |
| Factual_Target_Node_Class | Movies & TV |
| Counterfactual_Target_Node_class | Books |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 4884 |
| Natural_Language_Explanation | None |
