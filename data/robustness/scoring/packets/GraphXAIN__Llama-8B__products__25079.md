# Reference packet: GraphXAIN__Llama-8B__products__25079

- Method: GraphXAIN; configuration: Llama-8B; dataset: products; target node: 25079
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/products/graphxain_products_llama_narratives_fulleval.json` ([25079])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model accurately predicted the product category of "Chilly Dogs" as "Movies & TV" with 99.65% confidence. This prediction is largely driven by the presence of certain key words in the product title and description, such as "use," which strongly suggests an entertainment-related product. Another crucial aspect contributing to this prediction is the product's co-purchasing behavior - specifically, its frequent pairing with other movies like "Snow Dogs." Direct co-purchase neighbors, including "Snow Dogs," played a significant role in shaping this prediction, indicating a strong association between these products. Additionally, reinforcing this pattern are the 2-hop co-purchase neighbors, such as "My Favorite Martian" and "Eight Below," which were likely purchased together with the target product due to shared themes and customer interests. Overall, the model's prediction leverages both contextual cues (BOW features) and behavioral patterns (co-purchase networks) to effectively categorize "Chilly Dogs" within the movies & TV domain. By considering multiple lines of evidence, the model confidently placed this product within the correct category.
~~~~~~

## 2. Prompt the method's model received

`prompt` field of the record (sent as the single user message).

**user:**

~~~~~~text
Your goal is to generate a textual narrative explaining why a GNN model made a certain prediction for a target product node, based on the output of a GNNExplainer.

### Machine Learning Task:
Multi-class node classification task that predicts the product category on Amazon. The model classifies each product into one of 47 top-level Amazon categories such as 'Health & Personal Care', 'Beauty', 'Sports & Outdoors', 'Tools & Home Improvement', etc.

### Dataset:
The Amazon Products co-purchase network contains 54,025 products. Each product (node) is represented as a bag-of-words feature vector of 2,000 words from the product title and description. Edges represent co-purchase relationships — two products are connected if customers frequently buy them together.

### Target Product (node 25079):
Product from Amazon platform with title and content: Title: Chilly Dogs. Content: The lovely snowy expanses of Alaska are the setting forChilly Dogs, a goofy comedy about a travel agency clerk (Skeet Ulrich,Scream,The Newton Boys) from Los Angeles who has to prove his mettle by racing a team of mism

### Model Prediction:
{
  "Target Node": 25079,
  "Predicted Class": "Movies & TV",
  "Confidence": 0.9965
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='use', importance=0.7107, present_in_product=1
  word='use', importance=0.7076, present_in_product=1
  word='use', importance=0.7055, present_in_product=1
  word='use', importance=0.6942, present_in_product=1
  word='pack', importance=0.6902, present_in_product=0
  word='use', importance=0.6819, present_in_product=1
  word='man', importance=0.6792, present_in_product=1

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 1
Label distribution across all 1-hop neighbors (ground-truth category): Movies & TV=100.0%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 4884 | edge_importance=0.7772 | category=Movies & TV | Snow Dogs

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 25078 | edge_importance=0.8784 | category=Movies & TV | My Favorite Martian
  Product 25081 | edge_importance=0.8672 | category=Movies & TV | Eight Below (Widescreen Edition)
  Product 550 | edge_importance=0.8371 | category=Movies & TV | Inspector Gadget
  Product 545 | edge_importance=0.7714 | category=Movies & TV | missing
  Product 4820 | edge_importance=0.7529 | category=Movies & TV | missing
  Product 25080 | edge_importance=0.7452 | category=Movies & TV | missing
  Product 4915 | edge_importance=0.7258 | category=Movies & TV | missing
  Product 551 | edge_importance=0.2183 | category=Movies & TV | Air Bud Spikes Back

Generate a fluent, cohesive narrative explaining the prediction. Rules:

**Format rules:**
1) Start the explanation immediately — no preamble.
2) Limit the entire answer to 8 sentences or fewer.
3) Do not use tables or bullet lists — write a single cohesive paragraph.

**Content rules:**
1) State clearly what category the model predicted and with what confidence.
2) Discuss how the top BOW features contributed — note whether each high-importance word is actually present or absent in the product.
3) Discuss how the most influential direct (1-hop) co-purchase neighbors shaped the prediction, describing them by product type or title.
4) Mention how 2-hop neighbors reinforce the pattern if relevant.
5) Interpret WHY a feature or connection pushed the prediction in a certain direction.
6) Do not quote raw importance numbers; use relative language (e.g., "most influential", "strongly associated").
7) Use clear language that a general audience can understand.

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

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=25079).
Recorded prediction: `{"Target Node": 25079, "Predicted Class": "Movies & TV", "Confidence": 0.9965}`
Recorded graph stats: `{"total_1hop_degree": 1, "neighbor_label_ratio": {"Movies & TV": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | use | 0.7107 | 1 |
| 2 | use | 0.7076 | 1 |
| 3 | use | 0.7055 | 1 |
| 4 | use | 0.6942 | 1 |
| 5 | pack | 0.6902 | 0 |
| 6 | use | 0.6819 | 1 |
| 7 | man | 0.6792 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
