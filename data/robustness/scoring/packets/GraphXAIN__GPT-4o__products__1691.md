# Reference packet: GraphXAIN__GPT-4o__products__1691

- Method: GraphXAIN; configuration: GPT-4o; dataset: products; target node: 1691
- Explanation source: `./robustness_2026-10-30/graphxain_gpt4o/products/1691.json` (narrative)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The GNN model predicts the product "Johnson's Contour Nursing Pads - 36 ct" belongs to the "Beauty" category with a confidence of 61.32%. Among the top words influencing this prediction, "care," "using," and "protected" are present in the product description, suggesting attributes of personal attention and protection that align with beauty-related products, while absent words like "want" and "washable" still shape the model's interpretation by highlighting contrasting elements. This prediction is further influenced by the product's co-purchase network; significant direct neighbors include "Lansinoh Soothies Gel Pads" and "Charlie Banana Nursing Pads," both falling under "Baby," which might suggest caregiving but overlap with beauty due to their focus on comfort and personal care. The "Health & Personal Care" neighbors such as "Tucks Medicated Cooling Pads" contribute health-focused elements, potentially blurring category lines toward personal care. Although these neighbors predominantly belong to the "Baby" and "Health & Personal Care" categories, the shared attributes of absorbency and protection across these products steer the model toward a "Beauty" classification. Additionally, 2-hop connections, especially those linked to health treatments and postpartum care, emphasize the nurturing and restorative aspects, reinforcing the beauty prediction as they resonate with personal well-being and grooming. These factors, combined with the context of how such products often serve dual purposes in hygiene and appearance, guide the model to view the nursing pads as fitting within the beauty sphere.
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

### Target Product (node 1691):
Product from Amazon platform with title and content: Title: "Johnson's Contour Nursing Pads - 36 ct". Content: Exclusive Contour Shape 50% More Absorbent than the Leading Brand Nursing your little one and spending time together creates a special bond. While enjoying this time with your baby, you can

### Model Prediction:
{
  "Target Node": 1691,
  "Predicted Class": "Beauty",
  "Confidence": 0.6132
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Amazon Products BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word | importance score | whether the word is present in the product (1=yes, 0=no).
  word='want', importance=0.7099, present_in_product=0
  word='washabl', importance=0.7043, present_in_product=0
  word='care', importance=0.7016, present_in_product=1
  word='using', importance=0.7003, present_in_product=1
  word='fast', importance=0.6983, present_in_product=0
  word='using', importance=0.6962, present_in_product=1
  word='protected', importance=0.6959, present_in_product=1

### Target Node's Local Graph Structure:
Total 1-hop co-purchase degree (all direct neighbors, not just those listed below): 6
Label distribution across all 1-hop neighbors (ground-truth category): Baby=66.7%, Health & Personal Care=33.3%

### Direct Co-purchase Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are products customers frequently buy together with the target product.
  Product 13353 | edge_importance=0.7969 | category=Baby | Lansinoh Soothies Gel Pads, 2 Count
  Product 13618 | edge_importance=0.7949 | category=Baby | Charlie Banana Nursing Pads, White
  Product 13621 | edge_importance=0.775 | category=Baby | Philips AVENT Day Disposable Breast Pads, 60-Count
  Product 13619 | edge_importance=0.7694 | category=Baby | Waterproof Crib Mattress Pad - Soft Fitted Quilted Cover Pads for Baby - Best Protectors Liner Sheet Toppers Helps Infan
  Product 13620 | edge_importance=0.7653 | category=Health & Personal Care | Lansinoh Breastmilk Storage Bags, 25-Count Boxes (Pack of 3)
  Product 134 | edge_importance=0.6935 | category=Health & Personal Care | Tucks Medicated Cooling Pads 100 Pads Per Pack (Pack of 2)

### 2-hop Co-purchase Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-12 shown):
These products are not directly co-purchased with the target but are connected through shared co-purchase partners.
  Product 5164 | edge_importance=0.8136 | category=Health & Personal Care | Nelsons Bach Hemorrhoid Cream 1 oz
  Product 1686 | edge_importance=0.808 | category=Health & Personal Care | Anusol Haemorrhoids (Piles) Treatment Cream - 23g
  Product 1692 | edge_importance=0.8044 | category=Health & Personal Care | Tucks Hemorrhoid Ointment
  Product 1646 | edge_importance=0.8016 | category=Health & Personal Care | "T
  Product 1685 | edge_importance=0.7917 | category=Beauty | Earth Mama Angel Baby Postpartum Bath Herbs, 6 Count
  Product 1627 | edge_importance=0.7675 | category=Baby | Sugar Booger &quot;Numbers&quot; Closet Dividers Set of 5
  Product 1688 | edge_importance=0.2205 | category=Baby | Fisher-Price My Little Snugakitty Bouncer
  Product 1684 | edge_importance=0.2138 | category=Health & Personal Care | Puffs Plus Lotion With The Scent Of Vicks Facial Tissues; 88 Count; 1 Family Box (88 Tissues Per Box) (Pack of 24)
  Product 1690 | edge_importance=0.2095 | category=Health & Personal Care | Tucks Witch Hazel Hemorrhoidal Pads, 40 ea
  Product 0 | edge_importance=0.2085 | category=Clothing, Shoes & Jewelry | Aimee Gowns Original Bra-less Nursing Gown (X-Large, Fuchsia)
  Product 1680 | edge_importance=0.1911 | category=Baby Products | Pampers Swaddlers Diapers Size 1 Economy Pack Plus 216 Count
  Product 1687 | edge_importance=0.189 | category=Health & Personal Care | Always Maxi Overnight Extra Heavy Flow Pads With Wings, 40 Count

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

- ID: 1691
- Title: "Johnson's Contour Nursing Pads - 36 ct"
- True class (canonical `y`): **Baby Products**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Beauty**
- Prediction recorded by this method's pipeline: **Beauty**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: "Johnson's Contour Nursing Pads - 36 ct". Content: Exclusive Contour Shape 50% More Absorbent than the Leading Brand Nursing your little one and spending time together creates a special bond. While enjoying this time with your baby, you can continue to look and feel your best by using Johnson's(R) Nursing Pads. They are designed for superior absorbency, comfort, and complete discretion. Johnson's(R) Nursing Pads help you feel confident that you are protected while you are on the go. We know babies have unique skin needs. That's why we've created a full range of mild and gentle products especially for babies to be cleanse, moisturize and protect their delicate skin. Held to our high standard of safety, our unique No more Tears(R) Formula Wash is the #1 choice of hospitals and our Clinically Proven Mildness(TM) lotion is gentle enough to use both morning and night. Dermatologist tested and hypoallergenic. Also look for the other members of the Johnson's(R) family, such as Johnson's(R) Natural(R), the line of baby skincare products that are made with naturally derived ingredients and over 100 years of baby care expertise.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 6 nodes

| node id | true class | title |
|---|---|---|
| 134 | Health & Personal Care | Tucks Medicated Cooling Pads 100 Pads Per Pack (Pack of 2) |
| 13353 | Baby | Lansinoh Soothies Gel Pads, 2 Count |
| 13618 | Baby | Charlie Banana Nursing Pads, White |
| 13619 | Baby | Waterproof Crib Mattress Pad - Soft Fitted Quilted Cover Pads for Baby - Best Protectors Liner Sheet Toppers Helps Infants From Bed Bugs, Allergies - Long Lasting Size Fits All Cribs Breathable and Absorbent - Extremely Healthy Choice for You Toddler |
| 13620 | Health & Personal Care | Lansinoh Breastmilk Storage Bags, 25-Count Boxes (Pack of 3) |
| 13621 | Baby | Philips AVENT Day Disposable Breast Pads, 60-Count |

### 2-hop (shortest distance exactly 2): 13 nodes

| node id | true class | title |
|---|---|---|
| 0 | Clothing, Shoes & Jewelry | Aimee Gowns Original Bra-less Nursing Gown (X-Large, Fuchsia) |
| 1627 | Baby | Sugar Booger &quot;Numbers&quot; Closet Dividers Set of 5 |
| 1646 | Health & Personal Care | "T.N. Dickinson's Hemorrhoidal Pads, Witch Hazel with Aloe, 100-Count Packages (Pack of 2)" |
| 1680 | Baby Products | Pampers Swaddlers Diapers Size 1 Economy Pack Plus 216 Count |
| 1684 | Health & Personal Care | Puffs Plus Lotion With The Scent Of Vicks Facial Tissues; 88 Count; 1 Family Box (88 Tissues Per Box) (Pack of 24) |
| 1685 | Beauty | Earth Mama Angel Baby Postpartum Bath Herbs, 6 Count |
| 1686 | Health & Personal Care | Anusol Haemorrhoids (Piles) Treatment Cream - 23g |
| 1687 | Health & Personal Care | Always Maxi Overnight Extra Heavy Flow Pads With Wings, 40 Count |
| 1688 | Baby | Fisher-Price My Little Snugakitty Bouncer |
| 1689 | Baby Products | Lansinoh 20265 Disposable Nursing Pads, 60-Count |
| 1690 | Health & Personal Care | Tucks Witch Hazel Hemorrhoidal Pads, 40 ea |
| 1692 | Health & Personal Care | Tucks Hemorrhoid Ointment |
| 5164 | Health & Personal Care | Nelsons Bach Hemorrhoid Cream 1 oz. |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/products/prompts_dump.jsonl`, target_node=1691).
Recorded prediction: `{"Target Node": 1691, "Predicted Class": "Beauty", "Confidence": 0.6132}`
Recorded graph stats: `{"total_1hop_degree": 6, "neighbor_label_ratio": {"Baby": 0.667, "Health & Personal Care": 0.333}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | want | 0.7099 | 0 |
| 2 | washabl | 0.7043 | 0 |
| 3 | care | 0.7016 | 1 |
| 4 | using | 0.7003 | 1 |
| 5 | fast | 0.6983 | 0 |
| 6 | using | 0.6962 | 1 |
| 7 | protected | 0.6959 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
