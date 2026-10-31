# Reference packet: GraphNarrator__gpt-4o-mini__products__14760

- Method: GraphNarrator; configuration: gpt-4o-mini; dataset: products; target node: 14760
- Explanation source: `./robustness_2026-10-30/graphnarrator_gpt4omini/generated_expls-601/49.json` (messages[assistant])
- Scored scope (what the claims were extracted from): ### Free-Text Explanation section
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

Claims were extracted from the `### Free-Text Explanation` section only; the full assistant message is shown here.

~~~~~~text
### Reasoning

0. **Graph Structure Reconstruction:**

In the provided verbalized graph, the ROOT node (first line) is the target for classification. The structure of the graph is as follows:

- **ROOT** (Tom Yum Soup)
  - **Node-1** (Muay Thai Analgesic Balm)
    - **Node-1.1** (Muay Thai Shorts)
    - **Node-1.2** (Whole Dried Chile)
    - **Node-1.3** (Pond's Age Miracle Day Cream)
    - **Node-1.4** (Namman Muay Thai Boxing Liniment)
    - **Node-1.5** (Dentiste Plus White Toothpaste)

1. **Word-Level Evaluation:**

The ROOT node contains keywords like "soup," "spicy," "shrimp," and "Thai," which are highly relevant to food products, particularly Asian cuisine. However, the presence of "content" (0.07) and "mix" (0.02) suggests a focus on a product that combines various ingredients, which can also indicate a culinary context. The keywords "best" (0.01) and "dishes" (0.03) further emphasize the quality and culinary aspect of the product.

2. **Graph-Level Aggregation:**

Node-1 (Muay Thai Analgesic Balm) contains keywords such as "analgesic" (0.00), "massage" (0.00), and "pain" (0.00), which indicate a product used for relief and wellness, aligning with beauty and personal care. The presence of Node-1.3 (Pond's Age Miracle Day Cream) is particularly significant, as it directly relates to skincare, reinforcing the classification towards beauty products. Other nodes like Node-1.4 (Namman Muay Thai Boxing Liniment) and Node-1.5 (Dentiste Plus White Toothpaste) also contribute to the beauty and personal care context through their focus on skin and oral care.

### Free-Text Explanation
```markdown
The classification of ROOT into "Beauty" is supported by its own keywords and the co-purchase neighborhood.

**ROOT:** The keywords "soup," "spicy," and "Thai" suggest a culinary product, specifically Tom Yum Soup, which is popular in beauty and wellness contexts for its health benefits.
  - **Node-1:** The Muay Thai Analgesic Balm (keywords: "analgesic," "massage," "pain") indicates a product aimed at relief and wellness, aligning with beauty and personal care.
    - **Node-1.1:** Muay Thai Shorts are related to the sport but do not contribute directly to the beauty classification.
    - **Node-1.2:** Whole Dried Chile is more culinary-focused and less relevant to beauty.
    - **Node-1.3:** Pond's Age Miracle Day Cream is a skincare product, reinforcing the beauty classification significantly.
    - **Node-1.4:** Namman Muay Thai Boxing Liniment is another wellness product that supports skin health, contributing to the beauty context.
    - **Node-1.5:** Dentiste Plus White Toothpaste is directly related to oral care, further affirming the beauty category.

In summary, while ROOT suggests a culinary product, the surrounding nodes, particularly the skincare and oral care products, strongly support the classification into the "Beauty" category, highlighting the intersection of wellness and beauty in the graph.
```
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/49.json`).

**system:**

~~~~~~text
You are a helpful, reliable and responsible AI assistant.
~~~~~~

**user:**

~~~~~~text
The following verbalized graph contains important words in the text of each nodes. These words (each with corresponding importance score in the bracket) contribute to the classification of Node 0 into one of the Amazon product categories. Edges represent co-purchase relationships between products.
Generate a concise, human-readable explanation that justifies the classification result of Node 0 by identifying and explaining the relevant inner-node features (i.e., keywords) and inter-node relationships (i.e., graph structure). The explanation should focus on how these factors contribute to the classification label.

## Example

### Verbalized Graph
<verbalized-graph>ROOT: product(0.02) amazon(0.01) title(0.06) content(0.05) vibrelli(0.05) performance(0.04) bike(0.07) pump(0.08) bicycle(0.06) gauge(0.06) content(0.05) high(0.04) pressure(0.06) bike(0.05) pump(0.07) fits(0.04) presta(0.05) schrader(0.05) valve.(0.04) 160(0.03) psi(0.06) aluminum(0.03) alloy(0.03) barrel.(0.04)
Node-1: product(0.01) amazon(0.01) title(0.03) content(0.03) continental(0.03) race(0.03) tire(0.04) inner(0.04) tube(0.05) road(0.04) bike(0.04) bicycle(0.03)
Node-1.1: product(0.00) amazon(0.00) title(0.01) content(0.01) pedro's(0.00) tire(0.01) lever(0.01) bicycle(0.00) removal(0.00)
Node-1.2: product(0.00) amazon(0.00) title(0.00) content(0.00) park(0.00) tool(0.00) gp-2(0.00) patch(0.00) kit(0.00) tube(0.00)
Node-2: product(0.01) amazon(0.01) title(0.02) content(0.02) vittoria(0.02) zaffiro(0.02) road(0.02) bike(0.02) tire(0.03) 700c(0.02) cycling(0.02) bicycle(0.02) durable(0.01) puncture(0.02) resistant(0.01)
Node-2.1: product(0.00) amazon(0.00) title(0.00) content(0.00) kmc(0.00) x9(0.00) 9(0.00) speed(0.00) chain(0.00) bicycle(0.00)
Node-2.2: product(0.00) amazon(0.00) title(0.00) content(0.00) bontrager(0.00) race(0.00) lite(0.00) saddle(0.00) road(0.00) bike(0.00)
</verbalized-graph>

### Classification Label
Sports & Outdoors

### Reasoning

0. Graph Structure Reconstruction:

In the provided verbalized graph, the ROOT node (first line) is the target for classification.
Single-digit indexed nodes are direct neighbors of ROOT.
Double-digit indexed nodes are:
  - Two hops away from ROOT
  - Direct children of their parent node

Thus, the graph structure of this verbalized graph is:

- ROOT (bicycle pump)
  - Node-1 (inner tube)
    - Node-1.1 (tire lever)
    - Node-1.2 (patch kit)
  - Node-2 (road tire)
    - Node-2.1 (bike chain)
    - Node-2.2 (saddle)

1. Word-Level Evaluation:

Keywords with high saliency scores in ROOT — "pump" (0.08), "bike" (0.07), "bicycle" (0.06), "psi" (0.06), "pressure" (0.06), "presta" (0.05), "schrader" (0.05) — are strongly associated with cycling equipment. These directly indicate the product belongs to "Sports & Outdoors" (cycling accessories). More generic terms like "product" (0.02) and "amazon" (0.01) carry negligible saliency and contribute little.

2. Graph-Level Aggregation:

Node-1 (inner tube, keywords: "tube" (0.05), "road" (0.04), "bike" (0.04)) and Node-2 (road tire, keywords: "tire" (0.03), "cycling" (0.02)) are direct neighbors with moderate saliency, identifying cycling-specific accessories whose close proximity to ROOT reinforces the classification. Indirect neighbors — Node-1.1 (tire lever), Node-1.2 (patch kit), Node-2.1 (chain), Node-2.2 (saddle) — are all bicycle components, collectively confirming a cycling context across both hops.

### Free-Text Explanation
```markdown
The classification of ROOT into "Sports & Outdoors" is supported by its own keywords and the co-purchase neighborhood.

ROOT: Keywords like "pump" (0.08), "bike" (0.07), and "psi" (0.06) clearly identify this as a high-pressure bicycle pump — quintessentially a sports accessory.
  - Node-1: An inner tube (keywords: "tube" (0.05), "road" (0.04), "bike" (0.04)) is a direct cycling component, reinforcing the Sports & Outdoors context.
    - Node-1.1 ~ Node-1.2: Tire levers and patch kits are bicycle repair tools, supporting the cycling category.
  - Node-2: A road bike tire (keywords: "tire" (0.03), "cycling" (0.02)) further confirms the cycling product ecosystem.
    - Node-2.1 ~ Node-2.2: A chain and a saddle are additional cycling components, collectively affirming the Sports & Outdoors classification.

In summary, ROOT's own high-saliency keywords strongly signal cycling use, and the entire co-purchase neighborhood consists of bicycle components and accessories, providing robust evidence for the "Sports & Outdoors" category.
```

## Task

### Verbalized Graph
<verbalized-graph>ROOT: product(-0.03) amazon(0.02) platform(-0.00) title(0.01) content(0.07) title(0.04) lobo(0.01) spicy(0.01) tom(-0.00) yum(0.01) soup(0.02) mix(0.02) 30g(0.01) x(0.02) 5(0.02) pack.(0.05) content(0.02) shrimp(-0.03) tom(0.00) yum(0.01) tom(0.02) yum(0.00) goong(-0.00) must(-0.01) one(0.01) best(0.01) know(0.02) thai(0.01) dishes(0.03) abroad.(-0.01) subtle(0.02) blend(0.00) hot(-0.00) sour(0.02) citrus(0.00) overtones(0.02) derived(0.01) lime(0.01) juice(0.01) kaffir(0.00) lime(-0.01) peel.(0.01) careful(0.03) overcook(-0.00) shrimps(0.02) become(0.03) tough(0.01) easily.(-0.01) 
Node-1: product(0.00) amazon(-0.01) platform(0.01) title(0.01) content(0.02) title(0.00) namman(0.00) muay(-0.00) thai(-0.01) boxing(0.02) analgesic(-0.00) balm(0.01) massage(0.00) relief(0.00) ache(0.01) 100g.(-0.00) content(-0.00) description(0.01) muay(-0.01) thai(-0.00) boxing(0.02) cream(0.01) pain(-0.00) reliever(0.00) condition(-0.00) brand(-0.00) new,(0.01) sealed,(0.00) never(0.01) open(0.00) size(0.00) sizes(0.01) 100(0.00) grams(-0.01) muay(-0.01) thai(0.00) boxing(0.02) cream(0.00) thai(0.00) nam(0.00) man(0.00) muay(0.00) imuay(-0.00) thai(-0.01) boxing(0.00) cream(-0.00) well(0.02) known(0.00) popular(-0.01) analgesic(0.00) cream(-0.01) brand(0.00) nam(0.01) man(-0.00) muay(-0.00) thailand.(0.03) unique(0.02) massage(-0.01) cream(-0.01) used(0.00) thai(-0.01) boxers,(0.02) kick(0.01) boxers(0.01) athletes(-0.00) around(0.00) world.(0.02) must(0.03) training(0.01) session(0.01) competition(0.01) providing(0.01) warmth(-0.01) relax(-0.00) muscles(-0.01) strenuous(0.00) exercise.(0.01) many(-0.01) practioners(0.00) currently(-0.00) use(-0.00) product(-0.01) know(0.00) necessity(0.01) serious(0.01) fight.(-0.00) simply(0.01) rub(0.01) massage(-0.00) muscles(0.01) long(0.01) warm(0.00) muscles(0.01) open(0.00) nostrils(0.01) distinct(0.00) odour,(0.01) ready(0.01) action.(-0.00) product(-0.02) used(0.00) warm(0.00) tool(0.00) simply(0.01) apply(0.00) tired,(0.01) aching(0.01) mildly(0.01) injured(0.01) muscles.(-0.00) indicated(-0.00) relief(0.00) muscular(0.00) aches(-0.01) arthritic(-0.00) rheumatic(-0.00) pain(-0.01) strains(0.00) sprain(-0.00) directions(0.02) apply(-0.02) boxing(0.02) cream(0.00) body(-0.00) pre-(0.02) sport(-0.00) warm(0.00) gently(0.01) massage,(-0.00) re-(0.01) apply(0.00) sport(-0.01) strenuous(0.01) activity(-0.01) loosen(-0.01) tight(0.01) muscles(0.00) pain(-0.00) relief.(0.00) apply(0.00) boxing(0.01) cream(-0.01) injury(0.00) treatment(-0.00) least(0.02) 3-(0.02) 4(-0.00) times(-0.00) day(0.01) stiff(0.00) painful(0.00) areas(0.01) gently(0.00) massage.(0.02) contra-(0.01) indications(-0.07) used(-0.00) infected(0.01) injured(0.01) areas(0.01) skin.(0.01) active-(-0.01) ingredients(-0.05) methyl(-0.02) salicylate(-0.01) 10.(-0.00) 2(-0.01) menthol(0.00) 5.(0.00) 44(0.00) eugenol(-0.00) 1.(-0.01) 36(0.01) side-(-0.01) effect(-0.01) known(0.02) side-(-0.01) effects.(-0.01) 
Node-1.1: product(0.00) amazon(0.00) platform(0.00) title(0.00) content(0.00) title(0.00) revgear(0.00) muay(0.00) thai(0.00) shorts.(-0.00) content(0.00) revgear(0.00) professional(-0.00) satin(0.00) muay(0.00) thai(0.00) shorts.(-0.00) 4(0.00) muay(0.00) thai(0.00) elastic(0.00) drawstring(0.00) waistband(-0.00) 7(0.00) rows(0.00) stitching.(0.00) cut(0.00) extra(-0.00) wide(0.00) short(0.00) freedom(0.00) movement(0.00) ease(0.00) kicking.(0.00) authentic(-0.00) thai(-0.00) appliqu(0.00) xe9(-0.00) lettering(-0.00) across(0.00) front(0.00) means(0.00) muay(-0.00) thai(0.00) thai(-0.00) revgear(0.00) woven(0.00) waist(0.00) patch.(0.00) available(-0.00) colors(0.00) black,(0.00) red,(0.00) blue.(0.00) available(-0.00) sizes(0.01) s,(0.00) m,(0.00) l,(0.00) xl,(0.00) xxl.(0.01) 
Node-1.2: product(-0.00) amazon(-0.00) platform(0.01) title(0.01) content(0.02) title(0.02) thai(0.02) whole(0.00) dried(0.02) chile-(0.02) 3.(0.00) 5(0.01) oz.(0.02) content(0.02) thai(0.03) whole(-0.00) dried(0.01) chile-(0.01) 3.(-0.00) 5(0.00) oz(-0.00) bag(0.02) 
Node-1.3: product(-0.01) amazon(0.01) platform(0.00) title(0.01) content(-0.01) title(0.00) pond(-0.01) age(0.00) miracle(-0.00) day(-0.00) cream(0.00) 50g.(-0.00) sale!!!(-0.00) ".(-0.00) content(-0.01) pond(0.00) age(0.00) miracle(0.01) sensitive(-0.01) daily(-0.00) resurfacing(-0.00) day(0.00) cream(-0.01) advanced(0.00) cla4(0.00) complex(0.00) pond(-0.00) best(-0.00) age-(-0.00) fighting(0.00) technology.(-0.00) smooth(-0.00) day(0.01) cream(-0.00) specially(0.00) developed(-0.01) fight(0.01) fine(-0.00) lines(-0.00) wrinkles(-0.00) diminish(0.01) age(-0.01) spots.(-0.00) 50(0.01) grams(-0.03) 
Node-1.4: product(-0.00) amazon(0.00) platform(0.00) title(0.00) content(0.00) title(0.00) namman(-0.00) muay(0.00) thai(0.00) boxing(0.00) liniment(0.00) 120ml.(0.00) 2(0.00) bottles(0.00) ).(0.00) content(0.00) namman(-0.00) muay(0.00) muay(0.00) thai(0.00) boxing(-0.00) liniment(0.00) oil(0.00) herbal(0.00) liniment(0.00) made(0.00) quality(0.00) regional(0.01) botanicals.(0.00) main(0.00) active(0.00) ingredients(0.00) derived(0.00) plants(0.00) region(-0.00) known(0.00) reduce(0.00) inflammation(0.01) aid(0.00) blood(0.00) circulation.(0.01) special(-0.00) formulation(0.00) produces(0.00) product,(0.00) light,(0.00) smooth(0.00) glide(0.00) upon(0.00) application(0.01) formulated(0.01) fast(0.00) absorbing.(0.00) unlike(0.00) products,(0.00) namman(0.00) muay(0.00) penetrates(0.00) body(0.00) quickly(0.00) leave(0.00) greasy(0.01) sticky(-0.00) feeling.(0.00) products(-0.00) leave(0.00) pasty(0.00) hours.(0.00) side(-0.00) benefit(-0.00) scent(-0.00) believed(0.00) open(0.00) nasal(0.00) passages(0.00) helping(0.00) improve(-0.00) oxygen(-0.00) intake(0.00) increasing(-0.00) alertness.(0.00) 
Node-1.5: product(-0.00) amazon(-0.00) platform(0.00) title(0.00) content(0.00) title(-0.00) 2x100(0.00) g.(-0.00) dentiste(0.00) plus(0.00) white(0.00) vitamin(0.00) c(-0.00) amp(-0.00) xyitol(-0.00) gum(-0.00) toothpaste(0.00) made(-0.00) thailand.(0.00) content(0.00) bran</verbalized-graph>

### Classification Label
Beauty

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 14760
- Title: Lobo Spicy Tom Yum soup mix 30g X 5 pack
- True class (canonical `y`): **Grocery & Gourmet Food**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Health & Personal Care**
- Prediction recorded by this method's pipeline: **Beauty**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Lobo Spicy Tom Yum soup mix 30g X 5 pack. Content: Shrimp Tom Yum or Tom Yum Goong must be one of the best know Thai dishes abroad. It's a subtle blend of hot and sour with citrus overtones derived from lime juice and kaffir lime peel. Be careful not to overcook the shrimps as they will become tough very easily.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 1974 | Health & Personal Care | Namman Muay Thai Boxing Analgesic Balm Massage Relief Ache 100g |

### 2-hop (shortest distance exactly 2): 5 nodes

| node id | true class | title |
|---|---|---|
| 165 | Clothing, Shoes & Jewelry | Revgear Muay Thai Shorts |
| 14758 | Grocery & Gourmet Food | Thai whole dried chile - 3.5 oz |
| 14759 | Beauty | "POND'S Age Miracle Day Cream 50g. Sale!!!" |
| 14761 | Health & Personal Care | Namman Muay Thai Boxing Liniment 120ml. (2 Bottles) |
| 14762 | Beauty | 2x100 G. Dentiste Plus White Vitamin C &amp; Xyitol Gum Toothpaste Made in Thailand |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/49.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Beauty**, ground truth = **Grocery & Gourmet Food**.
The verbalized graph is 6867 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 14760 | 75 | 0.0671 | yes |
| Node-1 | 1 | 1974 | 300 | 0.0604 | yes |
| Node-1.1 | 2 | 165 | 88 | 0.0093 | yes |
| Node-1.2 | 3 | 14758 | 29 | 0.0326 | yes |
| Node-1.3 | 4 | 14759 | 65 | 0.0168 | yes |
| Node-1.4 | 5 | 14761 | 136 | 0.0083 | yes |
| Node-1.5 | 6 | 14762 | 101 | 0.0027 | yes |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, ROOT->Node-1

### Tokens and scores

**ROOT** (global 14760):

~~~~~~text
product (-0.0279) from (0.0160) amazon (0.0177) platform (-0.0035) with (0.0102) title (0.0097) and (-0.0025) content (0.0671) : (-0.0064) title (0.0440) : (0.0346) lobo (0.0124) spicy (0.0129) tom (-0.0032) yum (0.0062) soup (0.0245) mix (0.0161) 30g (0.0062) x (0.0242) 5 (0.0229) pack. (0.0455) content (0.0225) : (0.0341) shrimp (-0.0260) tom (0.0029) yum (0.0068) or (0.0206) tom (0.0247) yum (0.0021) goong (-0.0048) must (-0.0096) be (-0.0089) one (0.0126) of (0.0114) the (-0.0237) best (0.0108) know (0.0238) thai (0.0095) dishes (0.0337) abroad. (-0.0144) it (-0.0034) ' (-0.0230) s (0.0073) a (0.0128) subtle (0.0163) blend (0.0030) of (0.0039) hot (-0.0040) and (0.0135) sour (0.0208) with (0.0092) citrus (0.0039) overtones (0.0199) derived (0.0132) from (0.0105) lime (0.0135) juice (0.0075) and (0.0082) kaffir (0.0026) lime (-0.0092) peel. (0.0062) be (0.0147) careful (0.0252) not (-0.0101) to (-0.0055) overcook (-0.0005) the (-0.0049) shrimps (0.0155) as (0.0160) they (0.0082) will (0.0253) become (0.0330) tough (0.0070) very (-0.0084) easily. (-0.0090)
~~~~~~

**Node-1** (global 1974):

~~~~~~text
product (0.0042) from (0.0207) amazon (-0.0107) platform (0.0083) with (0.0150) title (0.0136) and (0.0127) content (0.0159) : (0.0262) title (0.0030) : (0.0122) namman (0.0023) muay (-0.0042) thai (-0.0085) boxing (0.0248) analgesic (-0.0006) balm (0.0103) massage (0.0006) relief (0.0038) ache (0.0072) 100g. (-0.0042) content (-0.0003) : (0.0223) description (0.0069) : (0.0054) muay (-0.0089) thai (-0.0037) boxing (0.0179) cream (0.0144) pain (-0.0031) reliever (0.0038) condition (-0.0021) : (0.0129) brand (-0.0046) new, (0.0079) sealed, (0.0004) never (0.0148) open (0.0043) size (0.0033) : (0.0182) sizes (0.0108) 100 (0.0023) grams (-0.0053) muay (-0.0063) thai (0.0033) boxing (0.0159) cream (0.0019) ( (0.0051) in (0.0027) thai (0.0005) : (0.0104) nam (0.0005) man (0.0048) muay (0.0032) ) (-0.0058) imuay (-0.0006) thai (-0.0065) boxing (0.0030) cream (-0.0045) is (-0.0161) the (0.0251) well (0.0201) known (0.0006) very (0.0030) popular (-0.0066) analgesic (0.0039) cream (-0.0095) brand (0.0021) " (0.0100) nam (0.0133) man (-0.0020) muay (-0.0013) " (0.0038) from (-0.0063) thailand. (0.0290) this (0.0039) unique (0.0159) massage (-0.0060) cream (-0.0105) is (0.0035) used (0.0045) by (0.0072) thai (-0.0149) boxers, (0.0174) kick (0.0149) boxers (0.0132) and (0.0276) athletes (-0.0016) around (0.0036) world. (0.0221) it (0.0043) ' (0.0144) s (-0.0161) a (-0.0143) must (0.0260) for (0.0109) any (0.0128) training (0.0123) session (0.0091) or (0.0168) competition (0.0091) providing (0.0134) that (0.0127) warmth (-0.0092) to (0.0111) relax (-0.0026) the (-0.0034) muscles (-0.0054) before (0.0020) or (0.0107) after (0.0133) any (0.0118) strenuous (0.0025) exercise. (0.0087) many (-0.0052) practioners (0.0019) that (0.0031) currently (-0.0013) use (-0.0024) this (-0.0160) product (-0.0055) all (-0.0035) know (0.0022) that (0.0067) it (0.0046) is (-0.0010) a (-0.0125) necessity (0.0097) before (0.0097) any (0.0119) serious (0.0077) fight. (-0.0043) you (-0.0052) just (0.0113) simply (0.0086) rub (0.0056) / (-0.0117) massage (-0.0013) it (0.0040) into (0.0007) your (-0.0089) muscles (0.0061) and (0.0117) before (0.0097) long (0.0087) you (0.0002) ' (0.0008) ll (0.0127) warm (0.0017) up (0.0077) those (0.0093) muscles (0.0084) and (0.0165) open (0.0031) up (0.0045) your (0.0008) nostrils (0.0063) with (0.0145) that (0.0128) distinct (0.0049) odour, (0.0071) and (0.0235) you (0.0056) ' (0.0006) ll (0.0072) be (0.0058) ready (0.0129) for (0.0114) action. (-0.0002) this (-0.0038) product (-0.0231) can (0.0031) be (0.0042) used (0.0003) as (0.0068) a (-0.0020) warm (0.0007) up (0.0042) tool (0.0009) or (0.0079) simply (0.0074) apply (0.0020) to (0.0078) those (0.0106) tired, (0.0104) aching (0.0108) or (0.0080) mildly (0.0093) injured (0.0085) muscles. (-0.0013) indicated (-0.0031) for (-0.0101) relief (0.0036) of (-0.0055) : (0.0171) muscular (0.0005) aches (-0.0053) arthritic (-0.0002) rheumatic (-0.0024) pain (-0.0100) strains (0.0011) sprain (-0.0005) directions (0.0185) : (-0.0167) apply (-0.0194) boxing (0.0193) cream (0.0047) all (0.0031) over (0.0000) the (-0.0178) body (-0.0016) as (-0.0072) a (-0.0165) pre- (0.0151) sport (-0.0047) warm (0.0046) up (0.0071) and (0.0071) gently (0.0052) massage, (-0.0014) then (0.0040) re- (0.0066) apply (0.0000) after (0.0085) sport (-0.0070) or (0.0110) strenuous (0.0096) activity (-0.0090) to (-0.0030) loosen (-0.0058) tight (0.0085) muscles (0.0005) or (0.0103) for (-0.0074) pain (-0.0045) relief. (0.0004) apply (0.0013) boxing (0.0096) cream (-0.0053) as (-0.0081) an (0.0017) injury (0.0006) treatment (-0.0019) at (0.0052) least (0.0241) 3- (0.0168) 4 (-0.0013) times (-0.0018) a (-0.0452) day (0.0081) to (0.0019) the (-0.0189) stiff (0.0025) or (0.0005) painful (0.0027) areas (0.0100) and (0.0117) gently (0.0046) massage. (0.0178) contra- (0.0112) indications (-0.0714) : (-0.0673) not (0.0132) to (-0.0137) be (0.0604) used (-0.0002) on (0.0280) infected (0.0056) and (0.0196) / (0.0058) or (0.0059) injured (0.0076) areas (0.0132) of (-0.0070) skin. (0.0055) active- (-0.0069) ingredients (-0.0537) : (-0.0428) methyl (-0.0161) salicylate (-0.0088) 10. (-0.0012) 2 (-0.0101) % (0.0107) menthol (0.0011) 5. (0.0017) 44 (0.0037) % (-0.0039) eugenol (-0.0008) 1. (-0.0093) 36 (0.0057) % (0.0100) side- (-0.0055) effect (-0.0060) : (0.0384) there (0.0014) are (-0.0112) no (-0.0210) known (0.0244) side- (-0.0076) effects. (-0.0088)
~~~~~~

**Node-1.1** (global 165):

~~~~~~text
product (0.0007) from (0.0004) amazon (0.0011) platform (0.0016) with (0.0039) title (0.0017) and (0.0021) content (0.0019) : (0.0068) title (0.0025) : (0.0032) revgear (0.0010) muay (0.0021) thai (0.0019) shorts. (-0.0018) content (0.0046) : (0.0010) revgear (0.0001) professional (-0.0003) satin (0.0010) muay (0.0037) thai (0.0013) shorts. (-0.0034) 4 (0.0038) " (-0.0043) muay (0.0021) thai (0.0004) elastic (0.0016) and (0.0019) drawstring (0.0019) waistband (-0.0002) with (0.0019) 7 (0.0005) rows (0.0019) of (0.0025) stitching. (0.0029) cut (0.0006) extra (-0.0020) wide (0.0015) and (0.0019) short (0.0018) for (0.0017) freedom (0.0027) of (0.0008) movement (0.0018) and (0.0027) ease (0.0037) in (0.0024) kicking. (0.0045) authentic (-0.0016) thai (-0.0034) appliqu (0.0017) & (-0.0002) # (-0.0016) xe9 (-0.0006) ; (0.0093) lettering (-0.0003) across (0.0020) the (-0.0056) front (0.0015) ( (0.0036) means (0.0010) " (-0.0009) muay (-0.0009) thai (0.0017) " (0.0007) in (0.0039) thai (-0.0022) ) (0.0031) and (0.0035) revgear (0.0001) woven (0.0031) waist (0.0003) patch. (0.0024) available (-0.0019) colors (0.0010) : (0.0026) black, (0.0014) red, (0.0011) blue. (0.0050) available (-0.0021) sizes (0.0051) : (0.0076) s, (0.0028) m, (0.0014) l, (0.0032) xl, (0.0029) xxl. (0.0080)
~~~~~~

**Node-1.2** (global 14758):

~~~~~~text
product (-0.0007) from (0.0088) amazon (-0.0022) platform (0.0125) with (0.0063) title (0.0073) and (-0.0202) content (0.0200) : (0.0011) title (0.0165) : (-0.0007) thai (0.0207) whole (0.0012) dried (0.0230) chile- (0.0210) 3. (0.0028) 5 (0.0090) oz. (0.0202) content (0.0177) : (-0.0114) thai (0.0262) whole (-0.0046) dried (0.0108) chile- (0.0107) 3. (-0.0008) 5 (0.0004) oz (-0.0047) / (0.0326) bag (0.0224)
~~~~~~

**Node-1.3** (global 14759):

~~~~~~text
product (-0.0088) from (0.0092) amazon (0.0067) platform (0.0025) with (0.0042) title (0.0051) and (0.0024) content (-0.0088) : (-0.0055) title (0.0044) : (-0.0006) " (-0.0016) pond (-0.0051) ' (0.0020) s (-0.0005) age (0.0024) miracle (-0.0010) day (-0.0009) cream (0.0004) 50g. (-0.0039) sale!!! (-0.0009) ". (-0.0005) content (-0.0059) : (-0.0109) pond (0.0004) ' (-0.0007) s (0.0017) age (0.0001) miracle (0.0077) sensitive (-0.0070) daily (-0.0002) resurfacing (-0.0013) day (0.0002) cream (-0.0065) with (0.0018) advanced (0.0001) cla4 (0.0010) complex (0.0013) is (-0.0041) pond (-0.0039) ' (0.0051) s (0.0030) best (-0.0046) age- (-0.0017) fighting (0.0042) technology. (-0.0037) this (0.0110) smooth (-0.0019) day (0.0089) cream (-0.0017) is (0.0055) specially (0.0041) developed (-0.0074) to (0.0125) fight (0.0083) fine (-0.0029) lines (-0.0014) and (0.0168) wrinkles (-0.0035) and (0.0156) diminish (0.0087) age (-0.0093) spots. (-0.0014) 50 (0.0095) grams (-0.0267)
~~~~~~

**Node-1.4** (global 14761):

~~~~~~text
product (-0.0006) from (0.0003) amazon (0.0009) platform (0.0013) with (0.0015) title (0.0022) and (0.0009) content (0.0021) : (0.0004) title (0.0043) : (-0.0004) namman (-0.0025) muay (0.0009) thai (0.0030) boxing (0.0035) liniment (0.0015) 120ml. (0.0030) ( (0.0011) 2 (0.0018) bottles (0.0032) ). (0.0003) content (0.0045) : (-0.0028) namman (-0.0022) muay (0.0001) ( (0.0016) or (-0.0010) ' (-0.0007) muay (0.0007) thai (0.0040) boxing (-0.0024) liniment (0.0009) or (0.0005) oil (0.0015) ' (-0.0000) ) (-0.0160) is (0.0073) an (0.0044) herbal (0.0004) liniment (0.0004) made (0.0028) from (0.0019) quality (0.0006) regional (0.0083) botanicals. (0.0025) its (0.0005) main (0.0016) active (0.0014) ingredients (0.0021) are (0.0008) derived (0.0011) from (0.0018) plants (0.0003) of (0.0016) the (0.0012) region (-0.0015) and (0.0046) are (0.0006) known (0.0005) to (-0.0002) reduce (0.0004) inflammation (0.0079) and (0.0035) aid (0.0013) in (0.0026) blood (0.0009) circulation. (0.0070) the (-0.0030) special (-0.0003) formulation (0.0013) produces (0.0036) a (-0.0041) product, (0.0030) which (0.0035) has (0.0025) a (0.0013) light, (0.0032) smooth (0.0038) glide (0.0017) upon (0.0005) application (0.0054) ; (0.0035) it (0.0034) is (0.0013) formulated (0.0082) to (0.0045) be (0.0021) fast (0.0038) absorbing. (0.0022) unlike (0.0008) other (0.0014) products, (0.0016) namman (0.0044) muay (0.0037) penetrates (0.0014) the (-0.0002) body (0.0001) quickly (0.0021) and (0.0026) does (0.0023) not (0.0050) leave (0.0023) a (0.0023) greasy (0.0056) nor (0.0025) sticky (-0.0010) feeling. (0.0004) some (0.0000) products (-0.0012) can (-0.0014) leave (0.0005) you (-0.0023) pasty (0.0004) for (-0.0017) hours. (0.0016) a (-0.0016) side (-0.0028) benefit (-0.0023) is (-0.0021) that (0.0000) the (-0.0015) scent (-0.0008) is (0.0025) believed (0.0007) to (0.0010) open (0.0024) nasal (0.0013) passages (0.0036) helping (0.0013) to (-0.0003) improve (-0.0022) oxygen (-0.0004) intake (0.0035) while (0.0025) increasing (-0.0000) alertness. (0.0034)
~~~~~~

**Node-1.5** (global 14762):

~~~~~~text
product (-0.0003) from (-0.0006) amazon (-0.0023) platform (0.0007) with (-0.0006) title (0.0002) and (-0.0015) content (0.0017) : (0.0006) title (-0.0007) : (-0.0007) 2x100 (0.0005) g. (-0.0015) dentiste (0.0003) plus (0.0004) white (0.0000) vitamin (0.0010) c (-0.0001) & (-0.0001) amp (-0.0003) ; (0.0010) xyitol (-0.0002) gum (-0.0006) toothpaste (0.0003) made (-0.0012) in (0.0006) thailand. (0.0004) content (0.0008) : (-0.0013) brand (0.0018) : (0.0002) dentiste (-0.0007) product (0.0009) size (-0.0011) : (-0.0019) 100 (-0.0013) g. (0.0015) condition (-0.0011) : (-0.0007) brand (0.0012) new (-0.0003) & (0.0002) never (0.0002) used (-0.0012) description (-0.0017) : (-0.0005) hygienic (0.0001) & (0.0006) herbapeutic (0.0001) toothpaste (0.0003) natural (-0.0002) therapeutic (0.0006) extraces (-0.0004) freshen (0.0007) moring (0.0002) breath (0.0001) gentle (0.0011) on (0.0003) tooth (-0.0009) enamel, (-0.0011) safely (0.0009) clean (0.0010) inhibits (0.0001) nighttime (0.0005) bacteria (0.0006) reduces (0.0015) plaque (-0.0003) helps (0.0001) promote (0.0014) strong (-0.0009) and (-0.0003) healthy (0.0006) gum (0.0025) direction (-0.0000) : (0.0025) use (0.0008) with (0.0006) tooh (-0.0007) brush (0.0006) ingredients (0.0003) : (0.0000) eucalyptus, (0.0003) clove, (-0.0000) fennel, (-0.0001) anise, (-0.0006) salvia, (-0.0003) catechu, (-0.0003) commiphora, (0.0001) cinnamon, (-0.0002) myrrhis, (-0.0001) chamomila, (0.0001) ratanhia, (0.0000) mint, (0.0002) glycyrrhiza, (0.0001) echinacea, (0.0001) vitamin (0.0027) c, (0.0000) xylitol, (0.0002) silica (-0.0001) complex, (0.0004) cdx (0.0002)
~~~~~~
