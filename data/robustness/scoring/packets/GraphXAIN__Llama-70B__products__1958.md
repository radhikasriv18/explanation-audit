# Reference packet: GraphXAIN__Llama-70B__products__1958

- Method: GraphXAIN; configuration: Llama-70B; dataset: products; target node: 1958
- Explanation source: `./robustness_2026-10-30/llama70b/graphxain/products/1958.json` (response)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The GNN model predicted that the Hayabusa Chikara Fight Shorts belongs to the "Sports & Outdoors" category with a confidence of 58.29%. This prediction was largely driven by the presence of key words in the product description, particularly "use," which is strongly associated with sports equipment. Although the model also considered other important words like "tech," "help," and "one," these terms were absent from the product description, reducing their impact on the prediction.

In addition to these linguistic cues, the model drew heavily from co-purchasing patterns among similar products, such as the Muay Thai MMA Ankle Support Wraps and the Hayabusa Pro Training Series Kick Shield, both of which are commonly purchased alongside fight shorts and reinforced the "Sports & Outdoors" label. Among its direct co-purchase neighbors, products like hand wraps, kick shields, and mesh gear bags further supported this classification. 

Connections to second-degree neighbors, including various types of martial arts uniforms, gloves, and protective gear, likewise contribute to the model's conclusion, as they are commonly used in conjunction with fight shorts. Overall, the interplay between descriptive keywords, immediate co-purchasing relationships, and more extended connections within the product graph led the model to infer a strong association between the Hayabusa Chikara Fight Shorts and the world of competitive combat sports.
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

### Target Product (node 1958):
Product from Amazon platform with title and content: Title: Hayabusa Chikara Fight Shorts. Content: Designed with Mechanical PolyDirectional stretch fabric. Innovative tie system with indestructible webbing for a distinct customized fit. Pro Performance stretch panel and split side seams for unrestr

### Model Prediction:
{
  "Target Node": 1958,
  "Predicted Class": "Sports & Outdoors",
  "Confidence": 0.5829
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='use', importance=0.7596, present_in_product=1
  word='tech', importance=0.7515, present_in_product=0
  word='help', importance=0.745, present_in_product=0
  word='one', importance=0.7399, present_in_product=0
  word='authent', importance=0.7363, present_in_product=0
  word='hook', importance=0.7321, present_in_product=0
  word='mesh', importance=0.7319, present_in_product=0

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 5
Label distribution across all 1-hop neighbors (ground-truth category): Sports & Outdoors=60.0%, Clothing, Shoes & Jewelry=40.0%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 163 | edge_importance=0.8283 | category=Sports & Outdoors | Muay Thai MMA Ankle Support Wraps (Pair)
  Product 14712 | edge_importance=0.7862 | category=Sports & Outdoors | Hayabusa Pro Training Series Kick Shield
  Product 14711 | edge_importance=0.7355 | category=Clothing, Shoes & Jewelry | Hayabusa 70L Mesh Gear Bag, Black
  Product 164 | edge_importance=0.7311 | category=Sports & Outdoors | Hand Wrap Wash Bag w/ Bag Clip - Large
  Product 165 | edge_importance=0.6574 | category=Clothing, Shoes & Jewelry | Revgear Muay Thai Shorts

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 1962 | edge_importance=0.8309 | category=Sports & Outdoors | Titan Competition Headgear
  Product 169 | edge_importance=0.8232 | category=Clothing, Shoes & Jewelry | Muay Thai Shorts
  Product 1970 | edge_importance=0.8222 | category=Sports & Outdoors | Brazilian Jiu Jitsu Uniform or Gi Premium Black or Blue
  Product 1993 | edge_importance=0.8222 | category=Clothing, Shoes & Jewelry | Meister MMA Compression Rush Fight Shorts w/ Cup Pocket
  Product 1930 | edge_importance=0.8187 | category=Clothing, Shoes & Jewelry | "Title Boxing Title Mma 8 Limbs Thai Men's Tee, M, Black"
  Product 1976 | edge_importance=0.8166 | category=Sports & Outdoors | TITLE Classic MMA Protective Cup
  Product 1955 | edge_importance=0.8136 | category=Sports & Outdoors | Revgear Thai Style Boxing Gloves
  Product 1961 | edge_importance=0.8088 | category=Health & Personal Care | Clear Gear Sports Spray Bottle, 24-Ounce
  Product 1971 | edge_importance=0.8078 | category=Sports & Outdoors | Brazilian Jiu Jitsu Uniform or Gi Premium Black or Blue
  Product 1972 | edge_importance=0.8024 | category=Clothing, Shoes & Jewelry | Revgear Spartan MMA Fight Short
  Product 2002 | edge_importance=0.7994 | category=Clothing, Shoes & Jewelry | Lumpinee Muay Thai Kick Boxing Shorts : LUM-002
  Product 1947 | edge_importance=0.7964 | category=Sports & Outdoors | MMA Grappling Gloves Cage Fight Cowhide Leather, US Flag

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

- ID: 1958
- Title: Hayabusa Chikara Fight Shorts
- True class (canonical `y`): **Sports & Outdoors**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Sports & Outdoors**
- Prediction recorded by this method's pipeline: **Sports & Outdoors**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Hayabusa Chikara Fight Shorts. Content: Designed with Mechanical PolyDirectional stretch fabric. Innovative tie system with indestructible webbing for a distinct customized fit. Pro Performance stretch panel and split side seams for unrestricted range of motion. Contains Hayabusa's exclusive Guard lock inner grip waistband system. Reinforced T3 stitching for ultimate strength and durability. Extraordinary High-IQ odor inhibiting effects. Fiber-fused printing technology for lasting style.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 5 nodes

| node id | true class | title |
|---|---|---|
| 163 | Sports & Outdoors | Muay Thai MMA Ankle Support Wraps (Pair) |
| 164 | Sports & Outdoors | Hand Wrap Wash Bag w/ Bag Clip - Large |
| 165 | Clothing, Shoes & Jewelry | Revgear Muay Thai Shorts |
| 14711 | Clothing, Shoes & Jewelry | Hayabusa 70L Mesh Gear Bag, Black |
| 14712 | Sports & Outdoors | Hayabusa Pro Training Series Kick Shield |

### 2-hop (shortest distance exactly 2): 53 nodes

| node id | true class | title |
|---|---|---|
| 3 | Clothing, Shoes & Jewelry | Muay Thai Shorts-Black |
| 166 | Sports & Outdoors | "Revgear Women's Deluxe Muay Thai Short" |
| 168 | Clothing, Shoes & Jewelry | ARD xTreme MMA Fight Shorts UFC Cage Fight Grappling Muay Thai Boxing Black All Sizes |
| 169 | Clothing, Shoes & Jewelry | Muay Thai Shorts |
| 171 | Health & Personal Care | Namman Muay Thai Boxing Liniment 120ml |
| 1921 | Sports & Outdoors | TITLE Gel World Bag Gloves |
| 1930 | Clothing, Shoes & Jewelry | "Title Boxing Title Mma 8 Limbs Thai Men's Tee, M, Black" |
| 1940 | Sports & Outdoors | TapouT MMA Multipurpose Gloves (Small/Medium) |
| 1942 | Sports & Outdoors | Contender Fight Sports Knee Pads |
| 1947 | Sports & Outdoors | MMA Grappling Gloves Cage Fight Cowhide Leather, US Flag |
| 1948 | Sports & Outdoors | Junior 108&quot; Elastic Cotton MMA Hand Wraps (Pair) |
| 1949 | Sports & Outdoors | 4Q2 MMA Fight Socks |
| 1950 | Sports & Outdoors | Cloth Ankle Guard / Pads - Black - Piranha Gear |
| 1951 | Sports & Outdoors | Mrx MMA Fight Shorts Stretch Penals Black/Grey |
| 1952 | Sports & Outdoors | Piranha Gear Uniform Pants - Drawstring Waist |
| 1953 | Sports & Outdoors | Brute Torq Wrestling Knee Pad |
| 1954 | Clothing, Shoes & Jewelry | Hayabusa Mizuchi Short Sleeve Rashguard Shirt |
| 1955 | Sports & Outdoors | Revgear Thai Style Boxing Gloves |
| 1956 | Health & Personal Care | Compression Support Ankle Brace Size: Small, Color: Black |
| 1957 | Sports & Outdoors | "Muay Thai Men's Supporter with Steel Cup" |
| 1959 | Books | Boxing Mastery: Advanced Technique, Tactics, and Strategies from the Sweet Science |
| 1960 | Sports & Outdoors | Boon Sport Leather Training Gloves |
| 1961 | Health & Personal Care | Clear Gear Sports Spray Bottle, 24-Ounce |
| 1962 | Sports & Outdoors | Titan Competition Headgear |
| 1963 | Sports & Outdoors | Hayabusa Official MMA Shouri Bamboo Mizuchi T-Shirts/Tee |
| 1964 | Sports & Outdoors | Meister Mounted Metal Hand Wrap Roller |
| 1965 | Sports & Outdoors | TITLE Boxing 3/4 Length Stock Satin Robe |
| 1966 | Health & Personal Care | Authentic RDX Ankle Foot Support Anklet Pad MMA Brace Guard |
| 1967 | Sports & Outdoors | Hayabusa Logo T Shirt - White |
| 1968 | Clothing, Shoes & Jewelry | ARD Camo Pro MMA Fight Shorts Camouflage UFC Cage Fight Grappling Kickboxing |
| 1969 | Sports & Outdoors | Revgear Glove Dog Deodorizer |
| 1970 | Sports & Outdoors | Brazilian Jiu Jitsu Uniform or Gi Premium Black or Blue |
| 1971 | Sports & Outdoors | Brazilian Jiu Jitsu Uniform or Gi Premium Black or Blue |
| 1972 | Clothing, Shoes & Jewelry | Revgear Spartan MMA Fight Short |
| 1973 | Clothing, Shoes & Jewelry | "Shock Doctor Men's Power Supporter with BioFlex Cup" |
| 1974 | Health & Personal Care | Namman Muay Thai Boxing Analgesic Balm Massage Relief Ache 100g |
| 1975 | Clothing, Shoes & Jewelry | Muay Thai Shorts |
| 1976 | Sports & Outdoors | TITLE Classic MMA Protective Cup |
| 1986 | Clothing, Shoes & Jewelry | "Title Boxing Title Mma Submit Men's Tee, L, Yellow" |
| 1987 | Clothing, Shoes & Jewelry | Revgear Spartan MMA Fight Short |
| 1988 | Clothing, Shoes & Jewelry | Hayabusa Official MMA Champion Hoodie - Black |
| 1993 | Clothing, Shoes & Jewelry | Meister MMA Compression Rush Fight Shorts w/ Cup Pocket |
| 1994 | Sports & Outdoors | TITLE MMA Digital Interval Timer |
| 2000 | Clothing, Shoes & Jewelry | Hayabusa Flex Fight Shorts |
| 2001 | Sports & Outdoors | Muay Thai Shorts-Blue |
| 2002 | Clothing, Shoes & Jewelry | Lumpinee Muay Thai Kick Boxing Shorts : LUM-002 |
| 2003 | Clothing, Shoes & Jewelry | Revgear Deluxe Muay Thai Shorts |
| 2004 | Clothing, Shoes & Jewelry | New Winner Retro Muay Thai Shorts Kick Boxing K1 MMA Black Satin |
| 2009 | Sports & Outdoors | Muay Thai Shorts-Red |
| 2011 | Sports & Outdoors | Traditional Boxing Trunks, Blue or Red Color. Kids and Adult Sizes |
| 2016 | Sports & Outdoors | Rival d3o Intelli-Shock Pro Training Headgear |
| 2019 | Sports & Outdoors | Combat Sports Thai Style Jump Rope |
| 2021 | Sports & Outdoors | Fairtex Neoprene Shin Pads |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=1958).
Recorded prediction: `{"Target Node": 1958, "Predicted Class": "Sports & Outdoors", "Confidence": 0.5829}`
Recorded graph stats: `{"total_1hop_degree": 5, "neighbor_label_ratio": {"Sports & Outdoors": 0.6, "Clothing, Shoes & Jewelry": 0.4}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | use | 0.7596 | 1 |
| 2 | tech | 0.7515 | 0 |
| 3 | help | 0.745 | 0 |
| 4 | one | 0.7399 | 0 |
| 5 | authent | 0.7363 | 0 |
| 6 | hook | 0.7321 | 0 |
| 7 | mesh | 0.7319 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
