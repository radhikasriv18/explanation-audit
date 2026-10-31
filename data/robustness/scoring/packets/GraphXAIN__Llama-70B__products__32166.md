# Reference packet: GraphXAIN__Llama-70B__products__32166

- Method: GraphXAIN; configuration: Llama-70B; dataset: products; target node: 32166
- Explanation source: `./robustness_2026-10-30/llama70b/graphxain/products/32166.json` (response)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model predicted that the product "RAM Mounts 1\" Diameter Ball with Custom GoPro Hero Adapter RAP-B-202U-GOP1" belongs to the category "Sports & Outdoors" with a confidence of 35.88%. Although none of the top BOW features were strongly indicative of sports equipment, the frequent appearance of "use" in the product description suggests adaptability and versatility, which are often valued in outdoor gear. However, it was the local graph structure and co-purchase patterns that heavily influenced the model's decision. The product's sole 1-hop neighbor, Cortech Super 2, an automotive part, initially seemed contradictory, yet its strong association likely arose due to the adapter's compatibility with various mounts, rather than an inherent link between cameras and cars. In contrast, the 2-hop neighbors revealed a different trend – numerous automotive-related products emerged as secondary connections, suggesting that mount compatibility extends beyond sports applications. Ultimately, the model found an affinity between the product's adaptability and the Sports & Outdoors realm, overriding potential hints from direct and indirect co-purchases related to automobiles.
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

### Target Product (node 32166):
Product from Amazon platform with title and content: Title: RAM Mounts 1&quot; Diameter Ball with Custom GoPro Hero Adapter RAP-B-202U-GOP1. Content: Consists of a 1" diameter ball, connected to a custom Go Pro adapterAdapter attaches directly to the under side of the camera, replacing the factory m

### Model Prediction:
{
  "Target Node": 32166,
  "Predicted Class": "Sports & Outdoors",
  "Confidence": 0.3588
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='base', importance=0.7605, present_in_product=0
  word='snap', importance=0.7448, present_in_product=0
  word='use', importance=0.7404, present_in_product=1
  word='use', importance=0.736, present_in_product=1
  word='use', importance=0.7342, present_in_product=0
  word='factory', importance=0.7331, present_in_product=1
  word='glock', importance=0.7304, present_in_product=0

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 1
Label distribution across all 1-hop neighbors (ground-truth category): Automotive=100.0%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 6986 | edge_importance=0.7672 | category=Automotive | "Cortech Super 2

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 32164 | edge_importance=0.8507 | category=Automotive | Classic Accessories 73807 MotoGear Motorcycle Indoor Dust Cover, Sport
  Product 6990 | edge_importance=0.8264 | category=Automotive | missing
  Product 6902 | edge_importance=0.7967 | category=Automotive | Battery Tender 081-0069-8 Female Cigarette Adaptor for Quick Disconnect
  Product 6903 | edge_importance=0.736 | category=Automotive | Super Strong Stretch Heavy-duty 15&quot; Cargo Net for Motorcycle ATV - Stretches to 45&quot;
  Product 32165 | edge_importance=0.6537 | category=Automotive | MotoCentric Mototrek Sport Tail Bag - Black
  Product 6969 | edge_importance=0.1686 | category=Automotive | OGIO Saddlebag 110093
  Product 815 | edge_importance=0.1472 | category=Automotive | Bestem LGKA-NOMAD-SDL-R Black Regular Saddlebag Liner for Kawasaki Vulcan Nomad
  Product 6981 | edge_importance=0.1395 | category=Automotive | Dowco 50144-00 Fastrax Elite Series Black Sport and Adventure Tour Luggage Tail Bag

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

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=32166).
Recorded prediction: `{"Target Node": 32166, "Predicted Class": "Sports & Outdoors", "Confidence": 0.3588}`
Recorded graph stats: `{"total_1hop_degree": 1, "neighbor_label_ratio": {"Automotive": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | base | 0.7605 | 0 |
| 2 | snap | 0.7448 | 0 |
| 3 | use | 0.7404 | 1 |
| 4 | use | 0.736 | 1 |
| 5 | use | 0.7342 | 0 |
| 6 | factory | 0.7331 | 1 |
| 7 | glock | 0.7304 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
