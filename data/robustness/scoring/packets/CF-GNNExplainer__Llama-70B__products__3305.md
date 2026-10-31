# Reference packet: CF-GNNExplainer__Llama-70B__products__3305

- Method: CF-GNNExplainer; configuration: Llama-70B; dataset: products; target node: 3305
- Explanation source: `./robustness_2026-10-30/llama70b/cf/products/3305.json` (response)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, we can fill the dictionary as follows:

infos = {
    "Target_Node_ID": 3305,
    "Factual_Target_Node_Neighbors": [343, 19311, 19312, 19313, 19314, 19315],
    "Factual_Target_Node_Features": ["made", "use", "bag", "inch", "per"],
    "Counterfactual_Target_Node_Neighbors": [343, 19313, 19314, 19315],
    "Counterfactual_Target_Node_Features": ["made", "use", "bag", "inch", "per"],
    "Factual_Target_Node_Class": "Arts, Crafts & Sewing",
    "Counterfactual_Target_Node_class": "Health & Personal Care",
    "Target_Node_Features_Changed_From_Factual_To_Counterfactual": [],
    "Node_Differences": [19312],
    "Edge_Differences": [(19312, 3305)],
    "Natural_Language_Explanation": "The product 'Winco Bamboo Skewer, 6 inch' has changed its classification from 'Arts, Crafts & Sewing' to 'Health & Personal Care'. This change is likely due to the removal of the edge connecting it to the node 'Surebonder DT-25 All Temperature Mini Glue Sticks, 4-Inch', which is classified as 'Arts, Crafts & Sewing'. The remaining neighbors of the target node, such as 'Northwest Enterprises Hard Plastic 2-Ounce Shot Glasses, Clear, 50 Count' and 'Cindus Cellophane Wrap, 30-Inch Wide, 5-Feet Roll, Purple', are more closely related to the 'Health & Personal Care' category."
}

Explanation:
The target node 3305, representing the product 'Winco Bamboo Skewer, 6 inch', has changed its classification from 'Arts, Crafts & Sewing' to 'Health & Personal Care'. This change is likely due to the removal of the edge connecting it to the node 19312, 'Surebonder DT-25 All Temperature Mini Glue Sticks, 4-Inch', which is classified as 'Arts, Crafts & Sewing'. The remaining neighbors of the target node, such as 'Northwest Enterprises Hard Plastic 2-Ounce Shot Glasses, Clear, 50 Count' and 'Cindus Cellophane Wrap, 30-Inch Wide, 5-Feet Roll, Purple', are more closely related to the 'Health & Personal Care' category.

In the factual graph, the target node 3305 is connected to node 19312, which is classified as 'Arts, Crafts & Sewing'. This connection likely influenced the classification of the target node to 'Arts, Crafts & Sewing'. However, in the counterfactual graph, this edge is removed, and the target node is no longer connected to node 19312. As a result, the classification of the target node changes to 'Health & Personal Care', which is more consistent with the categories of its remaining neighbors.
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
given the factual graph: The node 17 is a product titled 'Fiber Craft 72-Pack Jingle Bells, 6mm-16mm, Gold' with key attributes: also, use, christma, craft, creativ, thing, fiber, fun, gold, great, holiday, look, make, pack, packag, per, perfect, piec, project, put, variou, way, one and is connected with the node 343 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 343 is a product titled 'Loew Cornell 1021254 Woodsies Craft Sticks, 1000-Piece' with key attributes: use, classroom, count, craft, food, great, ideal, inch, made, measur, natur, non, parti, piec, project, safe, student, teacher, wood and is connected with the nodes 17, 1840, 3249, 3301, 3302, 3303, 3304, 3305, 3306, 3307, 3308, 3309 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 1840 is a product titled 'Duck Brand 1302209 Duck 3/4 Inch by 500 Inch Invisible Tape, 3-Pack' with key attributes: per, acid, use, applic, ball, brand, come, one, featur, finish, free, gift, handi, year, inch, includ, long, matt, pack, sheet, pen, photo, premium, project, qualiti, surfac, tape, wide, make and is connected with the node 343 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 3249 is a product titled 'Darice 10843-99 350-Pack Chenille/Tinsel and Bump Chenille Stems, 12-Inch, Assorted' with key attributes: inch, use, book, assort, color, craft, group, includ, kid, length, measur, pack, packag, parti, per, perfect, size and is connected with the node 343 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 3301 is a product titled 'BAZIC Natural Craft Sticks, Wood, 100 Per Pack' with key attributes: made, ldquo, use, craft, natur, pack, per, wood and is connected with the node 343 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 3302 is a product titled 'Graham Spa Essentials 3.5 inch Make-up and Waxing Applicators 100pk' with key attributes: also, use, condit, eye, face, ideal, inch, make, perfect, user and is connected with the node 343 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 3303 is a product titled 'Blumenthal Lansing Company Favorite Findings 3-1/2-Ounce Big Bag of Buttons, Flowers' with key attributes: made, add, one, use, well, attach, bag, year, big, button, chang, color, compani, facepl, especi, everi, favorit, great, may, make, much, nylon, ounc, packag, sheet, percent, person, project, say, shape, size, special, subject, touch, way, wood and is connected with the node 343 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 3304 is a product titled 'Sargent Art 22-1205 1-Gallon Washable School Glue' with key attributes: calib, adult, advanc, almost, use, book, art, time, buy, certifi, children, classroom, formula, great, home, ideal, one, non, offic, safe, school, student, surfac, toxic, washabl, young and is connected with the node 343 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 3305 is a product titled 'Winco Bamboo Skewer, 6 inch' with key attributes: made, use, bag, inch, per and is connected with the nodes 343, 19311, 19312, 19313, 19314, 19315 and it is classified as Arts, Crafts & Sewing, it is the target node. The node 3306 is a product titled 'Darice Victoria Lynn Chenille Stems 6mm 12&quot; 100/Pkg-White' with key attributes: made, inch, use, time, avail, color, contain, one, flexibl, fun, great, home, kid, make, packag, quot, school, separ, soft, sold, varieti, white and is connected with the node 343 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 3307 is a product titled 'Poptails: 60 Boozy Treats Served on a Stick' with key attributes: capsul, use, none, serv, stick and is connected with the node 343 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 3308 is a product titled 'Geographics Gold Foil Seals, Pack of 200 (44461)' with key attributes: million, use, gold, pack and is connected with the node 343 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 3309 is a product titled 'Loew Cornell 1021201 Woodsies Alphabet Value Pack, 250 Piece' with key attributes: kenwood, use, classroom, count, food, great, height, ideal, inch, made, measur, natur, non, pack, parti, piec, project, safe, student, teacher, valu, wood and is connected with the node 343 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 19311 is a product titled 'Wilton Mini Muffin Cups, 100 Count' with key attributes: made, use, count, ideal, mini, much and is connected with the node 3305 and it is classified as Home & Kitchen, it is not the target node. The node 19312 is a product titled 'Surebonder DT-25 All Temperature Mini Glue Sticks, 4-Inch' with key attributes: inch, capsul, adhes, one, use, book, well, time, bag, children, clear, color, degre, diamet, either, everyday, fabric, glass, gun, high, hot, length, low, materi, metal, mini, sheet, per, plastic, project, second, mani, temperatur, wood, work and is connected with the node 3305 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 19313 is a product titled 'Northwest Enterprises Hard Plastic 2-Ounce Shot Glasses, Clear, 50 Count' with key attributes: inch, per, use, well, time, bit, clear, compani, contain, continu, count, creat, crystal, custom, take, one, easi, event, everyday, experi, famili, food, friend, get, hard, help, high, ideal, industri, leader, littl, make, ounc, packag, parti, perfect, plastic, price, manufactur, qualiti, servic, simpl, start, super, suppli, year, book, togeth, tradit, live, whether and is connected with the node 3305 and it is classified as Health & Personal Care, it is not the target node. The node 19314 is a product titled 'Cindus Cellophane Wrap, 30-Inch Wide, 5-Feet Roll, Purple' with key attributes: day, use, avail, bag, brightli, color, contain, one, feet, gift, inch, make, packag, perfect, purpl, roll, separ, sold, varieti, wide, wrap and is connected with the node 3305 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 19315 is a product titled 'On a Stick!: 80 Party-Perfect Recipes' with key attributes: ldquo, bed, across, use, anoth, area, time, busi, collect, color, com, come, comprehens, creativ, enough, ever, fill, food, full, group, keep, kind, least, mdash, one, news, parti, perfect, photo, profession, weekli, rdquo, recip, rsquo, state, stick, street, take, make, got, provid and is connected with the node 3305 and it is classified as Books, it is not the target node. and given the counterfactual example: The node 17 is a product titled 'Fiber Craft 72-Pack Jingle Bells, 6mm-16mm, Gold' with key attributes: also, use, christma, craft, creativ, thing, fiber, fun, gold, great, holiday, look, make, pack, packag, per, perfect, piec, project, put, variou, way, one and is connected with the node 343 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 343 is a product titled 'Loew Cornell 1021254 Woodsies Craft Sticks, 1000-Piece' with key attributes: use, classroom, count, craft, food, great, ideal, inch, made, measur, natur, non, parti, piec, project, safe, student, teacher, wood and is connected with the nodes 17, 1840, 3249, 3301, 3302, 3303, 3304, 3305, 3306, 3307, 3308, 3309 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 1840 is a product titled 'Duck Brand 1302209 Duck 3/4 Inch by 500 Inch Invisible Tape, 3-Pack' with key attributes: per, acid, use, applic, ball, brand, come, one, featur, finish, free, gift, handi, year, inch, includ, long, matt, pack, sheet, pen, photo, premium, project, qualiti, surfac, tape, wide, make and is connected with the node 343 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 3249 is a product titled 'Darice 10843-99 350-Pack Chenille/Tinsel and Bump Chenille Stems, 12-Inch, Assorted' with key attributes: inch, use, book, assort, color, craft, group, includ, kid, length, measur, pack, packag, parti, per, perfect, size and is connected with the node 343 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 3301 is a product titled 'BAZIC Natural Craft Sticks, Wood, 100 Per Pack' with key attributes: made, ldquo, use, craft, natur, pack, per, wood and is connected with the node 343 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 3302 is a product titled 'Graham Spa Essentials 3.5 inch Make-up and Waxing Applicators 100pk' with key attributes: also, use, condit, eye, face, ideal, inch, make, perfect, user and is connected with the node 343 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 3303 is a product titled 'Blumenthal Lansing Company Favorite Findings 3-1/2-Ounce Big Bag of Buttons, Flowers' with key attributes: made, add, one, use, well, attach, bag, year, big, button, chang, color, compani, facepl, especi, everi, favorit, great, may, make, much, nylon, ounc, packag, sheet, percent, person, project, say, shape, size, special, subject, touch, way, wood and is connected with the node 343 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 3304 is a product titled 'Sargent Art 22-1205 1-Gallon Washable School Glue' with key attributes: calib, adult, advanc, almost, use, book, art, time, buy, certifi, children, classroom, formula, great, home, ideal, one, non, offic, safe, school, student, surfac, toxic, washabl, young and is connected with the node 343 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 3305 is a product titled 'Winco Bamboo Skewer, 6 inch' with key attributes: made, use, bag, inch, per and is connected with the nodes 343, 19311, 19313, 19314, 19315 and it is classified as Health & Personal Care, it is the target node. The node 3306 is a product titled 'Darice Victoria Lynn Chenille Stems 6mm 12&quot; 100/Pkg-White' with key attributes: made, inch, use, time, avail, color, contain, one, flexibl, fun, great, home, kid, make, packag, quot, school, separ, soft, sold, varieti, white and is connected with the node 343 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 3307 is a product titled 'Poptails: 60 Boozy Treats Served on a Stick' with key attributes: capsul, use, none, serv, stick and is connected with the node 343 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 3308 is a product titled 'Geographics Gold Foil Seals, Pack of 200 (44461)' with key attributes: million, use, gold, pack and is connected with the node 343 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 3309 is a product titled 'Loew Cornell 1021201 Woodsies Alphabet Value Pack, 250 Piece' with key attributes: kenwood, use, classroom, count, food, great, height, ideal, inch, made, measur, natur, non, pack, parti, piec, project, safe, student, teacher, valu, wood and is connected with the node 343 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 19311 is a product titled 'Wilton Mini Muffin Cups, 100 Count' with key attributes: made, use, count, ideal, mini, much and is connected with the node 3305 and it is classified as Health & Personal Care, it is not the target node. The node 19312 is a product titled 'Surebonder DT-25 All Temperature Mini Glue Sticks, 4-Inch' with key attributes: inch, capsul, adhes, one, use, book, well, time, bag, children, clear, color, degre, diamet, either, everyday, fabric, glass, gun, high, hot, length, low, materi, metal, mini, sheet, per, plastic, project, second, mani, temperatur, wood, work and is connected with no other nodes and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 19313 is a product titled 'Northwest Enterprises Hard Plastic 2-Ounce Shot Glasses, Clear, 50 Count' with key attributes: inch, per, use, well, time, bit, clear, compani, contain, continu, count, creat, crystal, custom, take, one, easi, event, everyday, experi, famili, food, friend, get, hard, help, high, ideal, industri, leader, littl, make, ounc, packag, parti, perfect, plastic, price, manufactur, qualiti, servic, simpl, start, super, suppli, year, book, togeth, tradit, live, whether and is connected with the node 3305 and it is classified as Health & Personal Care, it is not the target node. The node 19314 is a product titled 'Cindus Cellophane Wrap, 30-Inch Wide, 5-Feet Roll, Purple' with key attributes: day, use, avail, bag, brightli, color, contain, one, feet, gift, inch, make, packag, perfect, purpl, roll, separ, sold, varieti, wide, wrap and is connected with the node 3305 and it is classified as Arts, Crafts & Sewing, it is not the target node. The node 19315 is a product titled 'On a Stick!: 80 Party-Perfect Recipes' with key attributes: ldquo, bed, across, use, anoth, area, time, busi, collect, color, com, come, comprehens, creativ, enough, ever, fill, food, full, group, keep, kind, least, mdash, one, news, parti, perfect, photo, profession, weekli, rdquo, recip, rsquo, state, stick, street, take, make, got, provid and is connected with the node 3305 and it is classified as Books, it is not the target node.
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

- ID: 3305
- Title: Winco Bamboo Skewer, 6 inch
- True class (canonical `y`): **Patio, Lawn & Garden**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Arts, Crafts & Sewing**
- Prediction recorded by this method's pipeline: **Arts, Crafts & Sewing**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Winco Bamboo Skewer, 6 inch. Content: Bamboo Skewer, 100 per Bag, 6".
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 6 nodes

| node id | true class | title |
|---|---|---|
| 343 | Arts, Crafts & Sewing | Loew Cornell 1021254 Woodsies Craft Sticks, 1000-Piece |
| 19311 | Home & Kitchen | Wilton Mini Muffin Cups, 100 Count |
| 19312 | Arts, Crafts & Sewing | Surebonder DT-25 All Temperature Mini Glue Sticks, 4-Inch |
| 19313 | Health & Personal Care | Northwest Enterprises Hard Plastic 2-Ounce Shot Glasses, Clear, 50 Count |
| 19314 | Health & Personal Care | Cindus Cellophane Wrap, 30-Inch Wide, 5-Feet Roll, Purple |
| 19315 | Books | On a Stick!: 80 Party-Perfect Recipes |

### 2-hop (shortest distance exactly 2): 11 nodes

| node id | true class | title |
|---|---|---|
| 17 | Arts, Crafts & Sewing | Fiber Craft 72-Pack Jingle Bells, 6mm-16mm, Gold |
| 1840 | Office Products | Duck Brand 1302209 Duck 3/4 Inch by 500 Inch Invisible Tape, 3-Pack |
| 3249 | Arts, Crafts & Sewing | Darice 10843-99 350-Pack Chenille/Tinsel and Bump Chenille Stems, 12-Inch, Assorted |
| 3301 | Arts, Crafts & Sewing | BAZIC Natural Craft Sticks, Wood, 100 Per Pack |
| 3302 | Health & Personal Care | Graham Spa Essentials 3.5 inch Make-up and Waxing Applicators 100pk |
| 3303 | Arts, Crafts & Sewing | Blumenthal Lansing Company Favorite Findings 3-1/2-Ounce Big Bag of Buttons, Flowers |
| 3304 | Arts, Crafts & Sewing | Sargent Art 22-1205 1-Gallon Washable School Glue |
| 3306 | Arts, Crafts & Sewing | Darice Victoria Lynn Chenille Stems 6mm 12&quot; 100/Pkg-White |
| 3307 | Books | Poptails: 60 Boozy Treats Served on a Stick |
| 3308 | Office Products | Geographics Gold Foil Seals, Pack of 200 (44461) |
| 3309 | Arts, Crafts & Sewing | Loew Cornell 1021201 Woodsies Alphabet Value Pack, 250 Piece |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/products/cf-gnnexplainer-canonical/random_seed_42_*` (key=7).

- Factual class: **Arts, Crafts & Sewing**
- Counterfactual class: **Health & Personal Care**
- Removed edges (global ids, 1): (3305, 19312)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 3305 |
| Factual_Target_Node_Neighbors | 343, 19311, 19312, 19313, 19314, 19315 |
| Factual_Target_Node_Features | made, use, use, bag, use, use, inch, per, use, use, use, use |
| Counterfactual_Target_Node_Neighbors | 343, 19311, 19313, 19314, 19315 |
| Counterfactual_Target_Node_Features | made, use, use, bag, use, use, inch, per, use, use, use, use |
| Factual_Target_Node_Class | Arts, Crafts & Sewing |
| Counterfactual_Target_Node_class | Health & Personal Care |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 19312 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 3305 |
| Factual_Target_Node_Neighbors | 343, 19311, 19312, 19313, 19314, 19315 |
| Factual_Target_Node_Features | made, use, use, bag, use, use, inch, per, use, use, use, use |
| Counterfactual_Target_Node_Neighbors | 343, 19311, 19313, 19314, 19315 |
| Counterfactual_Target_Node_Features | made, use, use, bag, use, use, inch, per, use, use, use, use |
| Factual_Target_Node_Class | Arts, Crafts & Sewing |
| Counterfactual_Target_Node_class | Health & Personal Care |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 19312 |
| Natural_Language_Explanation | None |
