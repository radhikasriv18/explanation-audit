# Reference packet: GraphNarrator__gpt-4o-mini__products__23324

- Method: GraphNarrator; configuration: gpt-4o-mini; dataset: products; target node: 23324
- Explanation source: `./robustness_2026-10-30/graphnarrator_gpt4omini/generated_expls-601/83.json` (messages[assistant])
- Scored scope (what the claims were extracted from): ### Free-Text Explanation section
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

Claims were extracted from the `### Free-Text Explanation` section only; the full assistant message is shown here.

~~~~~~text
### Reasoning

0. **Graph Structure Reconstruction:**

In the provided verbalized graph, the ROOT node (first line) is the target for classification. Single-digit indexed nodes are direct neighbors of ROOT. Double-digit indexed nodes are:
  - Two hops away from ROOT
  - Direct children of their parent node

Thus, the graph structure of this verbalized graph is:

- ROOT (breast enhancement cream)
  - Node-1 (slimming cream)
    - Node-1.1 (body slimming gel)
    - Node-1.2 (redugel)
    - Node-1.3 (hot chili cream)
    - Node-1.4 (sauna slimming wrap)
    - Node-1.5 (eudine redugel)

1. **Word-Level Evaluation:**

The ROOT node contains keywords such as "breast" (0.05), "enhancement" (0.06), "cream" (0.05), and "success" (0.04), which are strongly associated with beauty and cosmetic products aimed at body enhancement. The presence of terms like "topical" (0.04) and "formula" (0.03) further emphasizes its classification within the beauty category. Less relevant terms like "product" (-0.03) and "amazon" (0.13) do not significantly influence the classification.

2. **Graph-Level Aggregation:**

Node-1 (slimming cream) contains keywords such as "slim" (0.02), "reduce" (0.03), and "cream" (0.02), which indicate body contouring and enhancement products, reinforcing the beauty context. The direct neighbors of Node-1 include various creams and gels (Node-1.1 to Node-1.5), all of which focus on body slimming and enhancement, further solidifying the classification. These products collectively highlight a focus on beauty and body aesthetics, which is consistent across the entire co-purchase neighborhood.

### Free-Text Explanation
```markdown
The classification of ROOT into "Beauty" is supported by its own keywords and the co-purchase neighborhood.

ROOT: Keywords like "breast" (0.05), "enhancement" (0.06), and "cream" (0.05) clearly identify this as a breast enhancement cream — a product that falls squarely within the beauty category.
  - Node-1: A slimming cream (keywords: "slim" (0.02), "reduce" (0.03), "cream" (0.02)) is directly related to body enhancement, reinforcing the beauty context.
    - Node-1.1: A body slimming gel (keywords: "slimming" (0.00), "cream" (0.00)) supports the classification by focusing on body aesthetics.
    - Node-1.2: Redugel is another product aimed at fat reduction, further emphasizing the beauty theme.
    - Node-1.3: A hot chili cream, which is also a body slimming product, aligns with the beauty category.
    - Node-1.4: A sauna slimming wrap (keywords: "slimming" (0.01), "wrap" (0.01)) is designed for body contouring, adding to the beauty product ecosystem.
    - Node-1.5: Eudine redugel, aimed at reducing body fat, continues to affirm the focus on beauty and body enhancement.

In summary, ROOT's own high-saliency keywords strongly signal a beauty product, and the entire co-purchase neighborhood consists of body enhancement creams and gels, providing robust evidence for the "Beauty" classification.
```
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/83.json`).

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
<verbalized-graph>ROOT: product(-0.03) amazon(0.13) platform(-0.03) title(0.07) content(0.02) title(0.07) breast(-0.01) success(0.03) cream(0.02) 2.(-0.01) 0(0.05) fl(-0.00) oz(0.02) enhancement(0.06) bust(0.04) enlargement.(0.03) content(0.09) breast(0.05) success(0.04) cream(0.05) cream-(0.04) based(0.05) topical(0.04) breast(0.02) enhancement(0.03) formula(0.03) designed(0.04) women.(0.01) product(0.05) contains(0.04) variety(0.05) ingredients(0.07) including(0.04) volufiline(0.01) biobustyle(0.02) designed(0.06) powerful(0.04) female(0.03) enhancement.(0.04) breast(-0.02) success(0.03) cream(0.05) perfect(0.03) complement(0.03) breast(0.02) success(0.06) pills(0.05) used(0.03) alternative(0.02) wanting(0.04) avoid(0.02) expensive(0.04) dangerous(0.03) surgery.(-0.06) feel(0.10) sensuality(0.03) natural(0.06) enhancement(0.02) improve(0.00) confidence(0.06) looking(0.10) feeling(0.15) best(0.10) 
Node-1: product(-0.02) amazon(0.06) platform(0.04) title(0.04) content(0.01) title(0.04) slim(0.02) green(0.01) reduce(0.03) cream(0.02) 4(0.02) oz.(0.01) content(0.04) slim(0.00) green(0.01) reduce(0.02) cream(0.02) blend(0.03) exotic(0.05) herbal(0.06) extracts(0.04) naturally(0.03) sculpt(0.01) body.(0.04) apply(0.02) generous(0.02) amount(0.02) areas(0.03) legs,(0.01) thighs,(0.01) stomach,(0.02) arms,(0.02) buttocks,(0.02) hips.(0.03) massage(0.05) vigorously(0.03) gel(0.03) disappears.(0.01) wrap(0.05) around(0.03) plastic(0.05) paper(0.04) one(0.03) used(0.01) cover(0.02) food(0.03) ),(-0.01) use(0.03) without(0.04) plastic,(0.04) preferably(0.05) workouts.(0.03) may(0.02) feel(0.09) sensation(0.04) freshness(0.03) skin.(0.08) manufactured(0.04) usa(0.05) alfa(0.08) vitaminsto(0.04) get(0.06) started(0.05) right(0.03) simply(0.08) click(0.11) add(0.06) cart(0.10) button(0.05) above.(0.05) 
Node-1.1: product(0.00) amazon(0.00) platform(0.00) title(0.00) content(-0.00) title(0.00) yili(-0.00) balo(-0.00) hot(-0.00) chili(-0.00) body(-0.00) slimming(0.00) gel(0.00) 85ml.(-0.00) content(0.00) yili(-0.00) balo(0.00) cafe(-0.00) body(0.00) slimming(0.00) cream(0.00) 85ml(0.00) apply(-0.00) cream(0.00) areas(0.00) wish(0.00) slim(0.00) like(0.00) arms,(0.00) waist,(0.00) abdomen,(0.00) buttocks(0.00) thighs.(0.00) massage(-0.00) well(0.00) over.(0.00) metabolism(-0.00) go(0.00) see(0.00) results(-0.00) short(0.00) time.(0.00) skin(-0.00) fee(-0.00) look(0.00) tight,(0.00) smooth(-0.00) soft.(0.00) main(0.00) ingredients(-0.00) coffee(-0.00) factors(0.00) double(-0.00) caffeine(0.00) ),(0.00) natural(0.00) hot(0.00) pepper(0.00) oil,(0.00) ivy,(0.00) seaweed(0.00) extract,(0.00) exceparl-(0.00) ho(0.00) excel(0.00) t-(0.00) 95,(0.00) 1805-(-0.00) t,(0.00) kalcol-(0.00) 8670,(0.00) glycerin,(0.00) water,(-0.00) mp,(-0.00) ppprecautions(-0.00) use(0.00) 15(0.00) minutes(0.00) time.(0.00) feel(-0.00) sense(0.00) heat(-0.00) skin.(0.00) 39(0.00) hot(0.00) use(-0.00) alcohol(-0.00) soothe(-0.00) heat.(0.00) skins(-0.00) different(-0.00) careful(-0.00) 39(-0.00) let(0.00) skin(0.00) overheat.(0.00) use(0.00) 3(0.00) times(0.00) per(0.00) week.(0.00) storage(-0.00) keep(-0.00) airtight(-0.00) cool(-0.00) dry(-0.00) place.(0.00) good(0.00) 3(0.00) year(0.00) date(0.00) manufacture(0.00) find(0.00) bottle.(0.00) take(-0.00) product(-0.01) pregnant(-0.00) nursing,(-0.00) age(-0.00) 18.(0.00) consult(-0.00) physician(-0.00) using(-0.00) products(-0.00) take(-0.00) medicines(-0.00) medical(0.00) conditions.(0.00) keep(-0.00) reach(-0.00) children.(0.00) approved(-0.00) food(-0.01) amp(0.00) drug(0.00) administration.(-0.01) product(-0.00) intended(-0.00) diagnose,(0.00) treat,(-0.00) cure(-0.00) prevent(0.01) diseases.(-0.00) 
Node-1.2: product(-0.00) amazon(-0.00) platform(0.00) title(0.00) content(-0.00) title(0.00) missing.(0.00) content(0.00) redugel(0.00) plus(0.00) body(-0.00) gel,(0.00) helps(-0.00) reduce(-0.00) fat(-0.00) cells(-0.00) natural(0.00) way.(0.00) 
Node-1.3: product(0.00) amazon(-0.00) platform(0.00) title(-0.00) content(-0.00) title(-0.00) hot(-0.00) chili(0.00) balo(-0.00) cream(-0.00) 85ml(-0.00) coffee(0.00) yili(-0.00) balo(-0.00) cream(-0.00) 85ml.(0.00) content(0.00) yili(-0.00) balo(-0.00) cafe(0.00) body(-0.00) slimming(-0.00) cream(0.00) 85ml(-0.00) apply(0.00) cream(-0.00) areas(0.00) wish(-0.00) slim(-0.00) like(-0.00) arms,(0.00) waist,(0.00) abdomen,(-0.00) buttocks(-0.00) thighs.(0.00) massage(0.00) well(-0.00) over.(0.00) metabolism(0.00) go(0.00) see(0.00) results(-0.00) short(0.00) time.(0.00) skin(-0.00) feel(-0.00) look(-0.00) tight,(0.00) smooth(0.00) soft.(0.00) main(-0.00) ingredients(0.00) coffee(-0.00) factors(-0.00) double(0.00) caffeine(0.00) ),(0.00) natural(-0.00) hot(-0.00) pepper(0.00) oil,(-0.00) ivy,(-0.00) seaweed(0.00) extract,(-0.00) exceparl-(0.00) ho(0.00) excel(0.00) t-(0.00) 95,(0.00) 1805-(-0.00) t,(0.00) kalcol-(0.00) 8670,(0.00) glycerin,(0.00) water,(0.00) mp,(0.00) precautions(-0.00) use(-0.00) 15(-0.00) minutes(-0.00) time.(-0.00) feel(0.00) sense(0.00) heat(-0.00) skin.(-0.00) hot(0.00) use(-0.00) alcohol(0.00) soothe(0.00) heat.(0.00) skins(0.00) different(-0.00) careful(0.00) let(-0.00) skin(-0.00) overheat.(-0.00) use(0.00) 3(0.00) times(-0.00) per(0.00) week.(0.00) 
Node-1.4: product(0.01) amazon(-0.00) platform(0.00) title(0.00) content(0.01) title(0.01) aokdis(0.00) plastic(0.01) weight(0.01) loss(0.01) weight(0.01) waist(0.01) leg(0.00) thigh(0.00) sauna(0.00) slimming(0.01) wrap(0.01) burn(0.01) cellulite(0.00) fat(0.01) belt(0.00) wrap.(-0.00) content(0.00) package(0.00) content(0.00) 1pc(0.01) sauna(0.00) slimming(0.01) wrap(0.01) burn(0.01) cellulite(0.00) fat(0.01) weight(0.01) loss(0.01) waist(0.01) leg(0.01) thigh(0.01) without(0.01) retail(0.01) packaging(0.01) 
Node-1.5: product(-0.00) amazon(0.00) platform(-0.00) title(0.00) content(-0.00) title(0.00) l(0.00) eudine(-0.00) redugel(0.00) excessive(-0.00) body(-0.00) fat(-0.00) burner(-0.00) reducer(-0.00) ".(0.00) content(-0.00) l(-0.00) eudine(0.00) redugel(-0.00) excessive(0.00) body(0.00</verbalized-graph>

### Classification Label
Beauty

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 23324
- Title: Breast Success Cream 2.0 Fl Oz Enhancement Bust Enlargement
- True class (canonical `y`): **Clothing, Shoes & Jewelry**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Health & Personal Care**
- Prediction recorded by this method's pipeline: **Beauty**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Breast Success Cream 2.0 Fl Oz Enhancement Bust Enlargement. Content: Breast Success Cream is a cream-based topical breast enhancement formula designed just for women. This product contains a variety of ingredients including Volufiline and Biobustyle designed for powerful female enhancement. Breast Success Cream is a perfect complement to Breast Success pills or can be used an alternative for those wanting to avoid expensive and dangerous surgery. Feel the sensuality of natural enhancement and improve your confidence by looking and feeling your best
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 4435 | Health & Personal Care | Slim Green Reduce Cream 4 Oz |

### 2-hop (shortest distance exactly 2): 9 nodes

| node id | true class | title |
|---|---|---|
| 491 | Beauty | Yili Balo Hot Chili Body Slimming Gel 85ml |
| 492 | label 25 | missing |
| 4344 | Beauty | Hot Chili Balo Cream 85ml + Coffee Yili Balo Cream 85ml |
| 4345 | Clothing, Shoes & Jewelry | Aokdis Plastic Weight Loss Weight Waist Leg Thigh Sauna Slimming Wrap Burn Cellulite Fat Belt Wrap |
| 4444 | Health & Personal Care | "L'eudine Redugel Excessive Body Fat Burner Reducer" |
| 23111 | Health & Personal Care | Ultimate Body Wrap Lipo Applicator Wrap. 2 Wraps |
| 23161 | Grocery & Gourmet Food | PINALIM TEA/TE PINALIM - PINNEAPPLE, FLAX, GREEN TEA, RED TEA AND WHITE TEA |
| 23323 | Health & Personal Care | It Works! Defining Gel. Slimming Gel. Body Defining Gel by It Works! 0.5 oz sample size. |
| 23325 | Health & Personal Care | 21st Century Slimming Tea, Green Tea, 24 Count (Pack of 3) |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/83.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Beauty**, ground truth = **Clothing, Shoes & Jewelry**.
The verbalized graph is 10479 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 23324 | 96 | 0.1539 | yes |
| Node-1 | 1 | 4435 | 108 | 0.1078 | yes |
| Node-1.1 | 2 | 491 | 268 | 0.0070 | yes |
| Node-1.2 | 3 | 492 | 26 | 0.0035 | yes |
| Node-1.3 | 4 | 4344 | 172 | 0.0019 | yes |
| Node-1.4 | 5 | 4345 | 49 | 0.0096 | yes |
| Node-1.5 | 6 | 4444 | 155 | 0.0035 | yes |
| Node-1.6 | 7 | 23111 | 97 | 0.0068 | no |
| Node-1.7 | 8 | 23161 | 122 | 0.0053 | no |
| Node-1.8 | 9 | 23323 | 109 | 0.0043 | no |
| Node-1.9 | 10 | 23325 | 59 | 0.0042 | no |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->Node-1.6, Node-1->Node-1.7, Node-1->Node-1.8, Node-1->Node-1.9, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, Node-1.6->Node-1, Node-1.7->Node-1, Node-1.8->Node-1, Node-1.9->Node-1, ROOT->Node-1

### Tokens and scores

**ROOT** (global 23324):

~~~~~~text
product (-0.0340) from (-0.0172) amazon (0.1254) platform (-0.0297) with (-0.0236) title (0.0681) and (-0.0130) content (0.0200) : (-0.0097) title (0.0662) : (0.0293) breast (-0.0073) success (0.0319) cream (0.0235) 2. (-0.0055) 0 (0.0504) fl (-0.0028) oz (0.0202) enhancement (0.0608) bust (0.0365) enlargement. (0.0286) content (0.0881) : (-0.0188) breast (0.0492) success (0.0383) cream (0.0507) is (-0.0212) a (-0.0393) cream- (0.0408) based (0.0488) topical (0.0357) breast (0.0168) enhancement (0.0324) formula (0.0349) designed (0.0360) just (-0.0047) for (0.0353) women. (0.0087) this (0.0195) product (0.0473) contains (0.0380) a (0.0156) variety (0.0493) of (0.0341) ingredients (0.0716) including (0.0391) volufiline (0.0116) and (0.0215) biobustyle (0.0218) designed (0.0578) for (0.0303) powerful (0.0396) female (0.0254) enhancement. (0.0425) breast (-0.0187) success (0.0262) cream (0.0481) is (0.0425) a (-0.0032) perfect (0.0349) complement (0.0283) to (0.0278) breast (0.0173) success (0.0584) pills (0.0529) or (0.0636) can (0.0217) be (0.0310) used (0.0290) an (0.0084) alternative (0.0167) for (0.0084) those (0.0219) wanting (0.0365) to (0.0185) avoid (0.0232) expensive (0.0363) and (0.0176) dangerous (0.0295) surgery. (-0.0617) feel (0.0972) the (0.0439) sensuality (0.0279) of (0.0083) natural (0.0644) enhancement (0.0247) and (0.0117) improve (0.0050) your (0.0111) confidence (0.0557) by (0.0343) looking (0.1034) and (-0.0267) feeling (0.1539) your (0.0819) best (0.0985)
~~~~~~

**Node-1** (global 4435):

~~~~~~text
product (-0.0191) from (-0.0194) amazon (0.0640) platform (0.0403) with (-0.0103) title (0.0373) and (-0.0138) content (0.0131) : (0.0465) title (0.0440) : (0.0291) slim (0.0203) green (0.0144) reduce (0.0262) cream (0.0184) 4 (0.0158) oz. (0.0116) content (0.0396) : (0.0203) slim (0.0040) green (0.0136) reduce (0.0195) cream (0.0183) is (-0.0000) a (-0.0017) blend (0.0289) of (-0.0128) exotic (0.0497) herbal (0.0613) extracts (0.0413) to (0.0071) naturally (0.0252) sculpt (0.0106) your (-0.0079) body. (0.0368) apply (0.0243) a (-0.0004) generous (0.0246) amount (0.0231) in (0.0138) the (-0.0100) areas (0.0280) of (0.0047) the (-0.0030) legs, (0.0115) thighs, (0.0147) stomach, (0.0229) arms, (0.0195) buttocks, (0.0249) hips. (0.0345) massage (0.0451) vigorously (0.0320) until (0.0400) gel (0.0266) disappears. (0.0105) wrap (0.0519) around (0.0294) with (0.0286) plastic (0.0517) paper (0.0424) ( (0.0179) the (-0.0314) one (0.0279) that (0.0172) is (0.0170) used (0.0133) to (0.0171) cover (0.0214) food (0.0304) ), (-0.0056) or (0.0082) use (0.0294) it (0.0185) without (0.0448) the (-0.0090) plastic, (0.0359) preferably (0.0507) before (0.0254) workouts. (0.0272) you (0.0686) may (0.0200) feel (0.0869) a (-0.0065) sensation (0.0371) of (0.0107) freshness (0.0316) on (0.0217) your (0.0069) skin. (0.0833) manufactured (0.0439) in (0.0209) the (0.0156) usa (0.0509) by (0.0048) alfa (0.0765) vitaminsto (0.0411) get (0.0581) started (0.0492) right (0.0317) now (0.0925) simply (0.0846) click (0.1078) the (0.0548) add (0.0585) to (0.0511) cart (0.1018) button (0.0504) above. (0.0475)
~~~~~~

**Node-1.1** (global 491):

~~~~~~text
product (0.0004) from (-0.0006) amazon (0.0042) platform (0.0011) with (-0.0001) title (0.0011) and (0.0015) content (-0.0012) : (0.0022) title (0.0015) : (0.0010) yili (-0.0004) balo (-0.0008) hot (-0.0007) chili (-0.0014) body (-0.0001) slimming (0.0002) gel (0.0010) 85ml. (-0.0002) content (0.0008) : (0.0002) yili (-0.0005) balo (0.0003) cafe (-0.0026) body (0.0007) slimming (0.0004) cream (0.0008) 85ml (0.0006) apply (-0.0006) cream (0.0003) on (0.0003) all (0.0002) areas (0.0009) that (0.0013) you (0.0005) wish (0.0015) to (0.0013) slim (0.0009) down (0.0005) like (0.0009) arms, (0.0008) waist, (0.0007) abdomen, (0.0008) buttocks (0.0006) and (0.0016) thighs. (0.0012) massage (-0.0025) well (0.0001) all (0.0010) over. (0.0015) your (0.0008) metabolism (-0.0007) will (-0.0002) go (0.0000) up (0.0004) and (0.0022) you (-0.0000) will (-0.0008) see (0.0008) the (0.0016) results (-0.0008) in (0.0011) a (0.0012) very (0.0010) short (0.0000) time. (0.0004) your (-0.0001) skin (-0.0015) will (-0.0014) fee (-0.0003) and (0.0020) look (0.0004) tight, (0.0008) smooth (-0.0001) and (0.0009) soft. (0.0011) main (0.0025) ingredients (-0.0002) : (0.0014) coffee (-0.0017) factors (0.0008) ( (0.0025) double (-0.0003) caffeine (0.0003) ), (0.0028) natural (0.0010) hot (0.0014) pepper (0.0003) oil, (0.0024) ivy, (0.0024) seaweed (0.0003) extract, (0.0031) exceparl- (0.0008) ho (0.0026) excel (0.0018) t- (0.0013) 95, (0.0029) 1805- (-0.0017) t, (0.0010) kalcol- (0.0003) 8670, (0.0010) glycerin, (0.0007) water, (-0.0001) mp, (-0.0000) ppprecautions (-0.0002) : (0.0014) do (-0.0010) not (-0.0006) use (0.0012) it (-0.0007) for (0.0000) more (0.0003) than (0.0001) 15 (0.0006) minutes (0.0001) at (0.0005) a (0.0001) time. (0.0006) you (-0.0019) will (-0.0021) feel (-0.0005) a (-0.0004) sense (0.0000) of (0.0015) heat (-0.0010) in (-0.0010) the (0.0007) skin. (0.0002) if (0.0013) it (0.0013) & (0.0006) # (0.0013) 39 (0.0016) ; (-0.0012) s (-0.0017) too (0.0003) hot (0.0012) you (-0.0004) can (-0.0014) use (-0.0001) alcohol (-0.0023) to (-0.0001) soothe (-0.0006) the (0.0010) heat. (0.0014) all (-0.0002) skins (-0.0001) are (-0.0000) different (-0.0006) so (0.0005) you (-0.0005) have (0.0001) to (0.0001) be (-0.0004) careful (-0.0001) and (0.0005) don (0.0009) & (0.0025) # (-0.0008) 39 (-0.0006) ; (-0.0002) t (0.0030) let (0.0010) your (0.0008) skin (0.0003) overheat. (0.0006) do (-0.0004) not (0.0002) use (0.0000) more (0.0003) than (-0.0005) 3 (0.0016) times (0.0006) per (0.0008) week. (0.0010) storage (-0.0020) : (0.0001) keep (-0.0029) airtight (-0.0009) in (-0.0013) a (0.0005) cool (-0.0004) and (0.0005) dry (-0.0008) place. (0.0002) it (0.0008) is (-0.0009) good (0.0004) for (0.0003) 3 (0.0006) year (0.0003) from (-0.0019) the (-0.0006) date (0.0005) of (0.0001) manufacture (0.0017) that (0.0007) you (0.0000) can (0.0006) find (0.0001) on (-0.0010) the (0.0004) bottle. (0.0003) do (-0.0017) not (0.0002) take (-0.0011) this (-0.0002) product (-0.0052) if (-0.0010) you (-0.0014) are (-0.0004) pregnant (-0.0018) or (-0.0003) nursing, (-0.0003) or (-0.0006) under (-0.0011) the (0.0008) age (-0.0025) of (-0.0009) 18. (0.0008) consult (-0.0008) your (-0.0019) physician (-0.0027) before (0.0003) using (-0.0005) this (-0.0012) products (-0.0005) if (-0.0006) you (-0.0028) take (-0.0019) medicines (-0.0005) or (-0.0007) have (0.0015) medical (0.0001) conditions. (0.0012) keep (-0.0034) out (-0.0024) of (-0.0016) the (-0.0007) reach (-0.0016) of (-0.0005) children. (0.0008) it (0.0005) has (0.0001) not (0.0004) been (-0.0002) approved (-0.0013) by (-0.0015) the (-0.0005) food (-0.0053) & (0.0015) amp (0.0010) ; (0.0027) drug (0.0013) administration. (-0.0079) this (-0.0043) product (-0.0031) is (-0.0039) not (0.0069) intended (-0.0003) to (0.0025) diagnose, (0.0024) treat, (-0.0002) cure (-0.0030) or (-0.0000) prevent (0.0070) any (-0.0018) diseases. (-0.0049)
~~~~~~

**Node-1.2** (global 492):

~~~~~~text
product (-0.0008) from (0.0016) amazon (-0.0034) platform (0.0016) with (0.0019) title (0.0035) and (-0.0011) content (-0.0008) : (-0.0003) title (0.0033) : (0.0010) missing. (0.0001) content (0.0016) : (-0.0018) redugel (0.0001) plus (0.0015) body (-0.0017) gel, (0.0001) helps (-0.0037) to (-0.0024) reduce (-0.0006) fat (-0.0021) cells (-0.0001) in (0.0003) natural (0.0018) way. (0.0013)
~~~~~~

**Node-1.3** (global 4344):

~~~~~~text
product (0.0003) from (-0.0001) amazon (-0.0000) platform (0.0013) with (0.0001) title (-0.0008) and (0.0001) content (-0.0001) : (-0.0000) title (-0.0004) : (0.0001) hot (-0.0002) chili (0.0010) balo (-0.0005) cream (-0.0003) 85ml (-0.0001) + (0.0002) coffee (0.0011) yili (-0.0001) balo (-0.0004) cream (-0.0000) 85ml. (0.0002) content (0.0007) : (0.0001) yili (-0.0002) balo (-0.0003) cafe (0.0005) body (-0.0003) slimming (-0.0000) cream (0.0002) 85ml (-0.0001) apply (0.0005) cream (-0.0002) on (-0.0002) all (-0.0002) areas (0.0000) that (-0.0002) you (-0.0002) wish (-0.0001) to (-0.0001) slim (-0.0000) down (-0.0001) like (-0.0001) arms, (0.0000) waist, (0.0002) abdomen, (-0.0001) buttocks (-0.0001) and (-0.0001) thighs. (0.0003) massage (0.0019) well (-0.0000) all (0.0001) over. (0.0007) your (-0.0004) metabolism (0.0004) will (-0.0000) go (0.0003) up (0.0000) and (0.0003) you (0.0005) will (-0.0003) see (0.0005) the (0.0005) results (-0.0003) in (0.0003) a (-0.0001) very (-0.0002) short (0.0000) time. (0.0005) your (-0.0006) skin (-0.0000) will (-0.0004) feel (-0.0003) and (0.0000) look (-0.0000) tight, (0.0005) smooth (0.0004) and (0.0001) soft. (0.0008) main (-0.0027) ingredients (0.0000) : (-0.0003) coffee (-0.0002) factors (-0.0011) ( (0.0003) double (0.0003) caffeine (0.0002) ), (0.0002) natural (-0.0005) hot (-0.0005) pepper (0.0002) oil, (-0.0004) ivy, (-0.0001) seaweed (0.0000) extract, (-0.0006) exceparl- (0.0003) ho (0.0002) excel (0.0004) t- (0.0000) 95, (0.0002) 1805- (-0.0001) t, (0.0003) kalcol- (0.0003) 8670, (0.0001) glycerin, (0.0001) water, (0.0004) mp, (0.0000) precautions (-0.0000) : (-0.0002) do (-0.0004) not (-0.0004) use (-0.0004) it (0.0000) for (-0.0000) more (-0.0003) than (-0.0003) 15 (-0.0007) minutes (-0.0007) at (-0.0003) a (-0.0003) time. (-0.0002) you (0.0005) will (0.0001) feel (0.0002) a (-0.0004) sense (0.0004) of (0.0004) heat (-0.0002) in (-0.0002) the (0.0002) skin. (-0.0000) if (-0.0002) it (-0.0006) ` (0.0011) s (-0.0018) too (-0.0001) hot (0.0002) you (-0.0001) can (-0.0001) use (-0.0002) alcohol (0.0001) to (-0.0003) soothe (0.0005) the (-0.0006) heat. (0.0002) all (0.0001) skins (0.0003) are (-0.0000) different (-0.0004) so (-0.0001) you (-0.0002) have (-0.0001) to (-0.0000) be (-0.0003) careful (0.0003) and (0.0000) don (-0.0005) ` (0.0000) t (0.0010) let (-0.0007) your (-0.0004) skin (-0.0001) overheat. (-0.0001) do (0.0001) not (-0.0007) use (0.0001) more (-0.0002) than (-0.0001) 3 (0.0000) times (-0.0001) per (0.0005) week. (0.0007)
~~~~~~

**Node-1.4** (global 4345):

~~~~~~text
product (0.0067) from (0.0051) amazon (-0.0006) platform (0.0007) with (0.0065) title (0.0032) and (0.0029) content (0.0083) : (0.0036) title (0.0084) : (0.0052) aokdis (0.0028) plastic (0.0083) weight (0.0067) loss (0.0057) weight (0.0055) waist (0.0059) leg (0.0005) thigh (0.0015) sauna (0.0022) slimming (0.0062) wrap (0.0079) burn (0.0053) cellulite (0.0038) fat (0.0059) belt (0.0040) wrap. (-0.0028) content (0.0048) : (0.0010) package (0.0049) content (0.0037) : (0.0037) 1pc (0.0071) sauna (0.0017) slimming (0.0059) wrap (0.0073) burn (0.0052) cellulite (0.0039) fat (0.0062) weight (0.0079) loss (0.0063) waist (0.0051) leg (0.0060) thigh (0.0064) ( (0.0037) without (0.0093) retail (0.0080) packaging (0.0096) ) (0.0070)
~~~~~~

**Node-1.5** (global 4444):

~~~~~~text
product (-0.0022) from (-0.0013) amazon (0.0005) platform (-0.0016) with (-0.0010) title (0.0001) and (-0.0001) content (-0.0004) : (0.0001) title (0.0002) : (0.0001) " (-0.0001) l (0.0008) ' (0.0004) eudine (-0.0003) redugel (0.0000) excessive (-0.0000) body (-0.0002) fat (-0.0005) burner (-0.0006) reducer (-0.0013) ". (0.0002) content (-0.0001) : (-0.0014) l (-0.0002) ' (0.0003) eudine (0.0003) redugel (-0.0002) excessive (0.0010) body (0.0002) fat (-0.0002) burner (-0.0001) reducer (-0.0001) l (-0.0001) ' (0.0003) eudine (-0.0002) t (0.0002) redugel (-0.0005) penetrates (-0.0001) deep (-0.0001) into (-0.0002) the (-0.0001) skin (-0.0001) to (-0.0008) help (0.0004) mobilize (-0.0001) stored (0.0001) fat. (0.0011) this (0.0000) product (-0.0002) with (-0.0002) anti- (-0.0003) inflammatory (0.0008) and (-0.0004) slimming (-0.0001) properties, (-0.0012) immediately (0.0026) goes (0.0002) to (0.0015) work (0.0001) by (-0.0001) forcing (0.0010) over (-0.0000) bloated (-0.0002) fat (-0.0002) cells (-0.0008) to (0.0004) release (0.0006) trapped (0.0006) fat (-0.0000) into (0.0003) the (0.0017) bloodstream (-0.0002) to (0.0004) be (0.0001) burned (0.0003) as (-0.0000) energy. (-0.0009) directions (0.0004) : (-0.0012) apply (0.0009) on (0.0012) clean, (-0.0000) dry (-0.0001) skin (0.0010) twice (-0.0005) a (0.0014) day. (0.0002) vigorously (-0.0060) massage (0.0035) on (0.0022) target (-0.0008) area (-0.0000) ( (0.0002) abs, (0.0005) thights, (-0.0001) hips (-0.0012) or (-0.0008) buttocks (-0.0005) ) (-0.0000) for (0.0001) approximately (0.0004) 45 (-0.0002) seconds (0.0004) until (0.0017) is (0.0008) completely (0.0002) absorbed. (-0.0002) do (0.0012) not (-0.0008) bath (-0.0002) for (0.0009) 2 (0.0008) hours (0.0011) after (0.0005) applying (0.0017) this (0.0010) gel. (0.0007) it (0.0018) is (0.0003) recommended (0.0002) to (-0.0001) reduce (-0.0000) the (0.0021) calorie (0.0000) intake (-0.0000) and (-0.0004) exercise (-0.0003) frequently. (0.0000) warning (-0.0002) : (0.0010) if (0.0011) irritation (0.0015) occurs, (-0.0004) stop (-0.0007) use. (-0.0012) active (0.0015) components (0.0026) : (-0.0009) peppermint (0.0001) oil, (-0.0005) camphor, (0.0002) carbomer, (-0.0000) menthol, (-0.0001) horse (-0.0007) chestnut, (-0.0005) centella (-0.0004) asiatica, (0.0001) horse (-0.0015) tail (-0.0014) extract, (-0.0013) algae, (-0.0023) ivy, (-0.0013) mate (-0.0019) extract (0.0010)
~~~~~~

**Node-1.6** (global 23111):

~~~~~~text
product (0.0024) from (0.0007) amazon (0.0007) platform (-0.0001) with (0.0053) title (0.0034) and (0.0052) content (-0.0040) : (0.0029) title (0.0016) : (-0.0017) ultimate (0.0007) body (0.0019) wrap (-0.0000) lipo (0.0013) applicator (0.0021) wrap. (0.0035) 2 (-0.0002) wraps. (0.0003) content (-0.0033) : (0.0013) wrap (-0.0022) body (-0.0041) wrap (-0.0045) program (0.0004) is (0.0003) amazing. (0.0003) there (0.0044) is (0.0010) no (0.0036) soaking (0.0008) towels (0.0007) or (0.0023) bands.. (0.0005) or (-0.0029) trying (-0.0017) to (0.0026) wrap (0.0005) yourself (0.0016) up (0.0013) like (0.0017) a (0.0032) cocoon. (0.0016) lipowrap (-0.0008) body (-0.0023) wrap (0.0003) and (0.0015) belly (-0.0018) wrap- (0.0004) amazing (-0.0005) results (-0.0002) wrap (-0.0022) program (-0.0048) is (0.0014) a (0.0003) simple (0.0013) application (0.0013) process (0.0027) that (0.0031) takes (0.0007) no (0.0021) more (0.0040) than (0.0021) 5 (0.0006) minutes (0.0002) to (-0.0024) apply (0.0053) this (-0.0049) product (-0.0042) is (0.0015) for (-0.0015) cosmetic (-0.0044) use (0.0014) only. (0.0022) this (-0.0036) product (-0.0008) is (-0.0043) not (0.0050) intended (-0.0016) to (0.0040) either (0.0005) affect (-0.0012) the (-0.0000) structure (-0.0000) or (0.0011) function (-0.0001) of (0.0022) the (0.0020) body (-0.0031) or (0.0068) to (0.0029) cure, (0.0005) mitigate, (0.0024) treat, (0.0000) or (0.0034) prevent (0.0009) disease. (0.0050)
~~~~~~

**Node-1.7** (global 23161):

~~~~~~text
product (-0.0038) from (-0.0008) amazon (0.0002) platform (0.0002) with (-0.0004) title (0.0014) and (-0.0004) content (-0.0022) : (0.0010) title (0.0016) : (0.0004) pinalim (0.0006) tea (0.0036) / (0.0047) te (0.0025) pinalim- (0.0011) pinneapple, (0.0009) flax, (0.0004) green (0.0007) tea, (0.0015) red (0.0019) tea (0.0028) and (0.0002) white (0.0008) tea. (0.0029) content (-0.0005) : (0.0027) this (0.0006) is (0.0005) the (-0.0009) original (-0.0009) gn (0.0016) + (0.0011) vida (0.0008) weight (-0.0008) loss (-0.0025) tea, (0.0013) add (0.0014) this (0.0017) to (-0.0014) you (-0.0001) diet (0.0018) and (-0.0005) exercise (0.0020) regimen (0.0005) and (-0.0005) lose (0.0007) those (0.0008) hard (0.0020) to (0.0008) lose (0.0003) pounds. (0.0008) this (0.0005) product (0.0031) does (0.0008) what (-0.0003) it (0.0001) was (0.0001) designed (0.0026) to (-0.0002) do.... (-0.0011) help (-0.0006) you (0.0008) lose (0.0027) weight. (0.0019) the (-0.0022) pineapple (0.0015) tea, (0.0044) pinalim, (0.0022) is (0.0006) the (-0.0035) strongest (0.0015) enhanced (0.0026) pineapple (0.0029) tea (0.0053) from (0.0029) gn (0.0010) + (0.0031) vida, (0.0028) company (0.0020) that (0.0004) is (0.0020) most (0.0013) famous (0.0007) for (-0.0005) its (0.0018) wildly (0.0007) successful (0.0005) weight- (0.0027) loss (0.0018) supplement, (0.0015) the (0.0001) artichoke (0.0016) vials. (0.0013) now (0.0005) they (0.0027) bring (-0.0013) you (-0.0043) an (-0.0017) even (0.0010) stronger (-0.0005) version (0.0001) of (-0.0006) their (0.0016) famous (-0.0001) tea, (-0.0017) based (0.0008) on (0.0013) pineapple (0.0020) and (-0.0007) all (0.0010) its (0.0012) benefits. (0.0013) buy (0.0031) today (-0.0007) and (0.0025) start (0.0028) your (0.0019) weight (0.0007) loss (-0.0039) off (0.0009) right (-0.0019)
~~~~~~

**Node-1.8** (global 23323):

~~~~~~text
product (-0.0013) from (-0.0024) amazon (0.0012) platform (-0.0011) with (-0.0023) title (0.0014) and (-0.0014) content (-0.0012) : (0.0002) title (0.0028) : (0.0001) it (-0.0003) works! (0.0009) defining (0.0024) gel. (-0.0007) slimming (0.0017) gel. (-0.0005) body (0.0024) defining (0.0017) gel (-0.0010) by (-0.0013) it (-0.0001) works! (-0.0005) 0. (-0.0004) 5 (0.0021) oz (0.0007) sample (0.0012) size.. (-0.0006) content (0.0016) : (-0.0009) it (-0.0011) works! (0.0010) defining (-0.0003) gel. (0.0013) 0. (0.0014) 5 (0.0007) oz (0.0002) size (-0.0000) of (0.0007) slimming (0.0021) gel. (0.0028) luxurious (-0.0006) hydration (0.0006) meets (0.0010) contouring (0.0008) results (-0.0009) with (0.0001) this (0.0010) favorite (0.0023) it (-0.0005) works (-0.0003) product! (0.0014) intensive (0.0017) skin (0.0013) care (-0.0007) gel (0.0013) deeply (0.0015) hydrates (0.0009) while (0.0003) firming (0.0011) areas (0.0021) such (0.0008) as (0.0009) the (0.0003) legs, (-0.0003) back, (0.0004) abdomen, (-0.0016) and (0.0005) upper (0.0011) arms. (0.0021) helps (0.0024) minimize (0.0011) the (0.0002) appearance (0.0015) of (0.0004) cellulite (0.0004) and (0.0010) varicose (0.0013) veins. (0.0035) designed (0.0011) to (0.0023) maximize (0.0017) results (0.0039) when (0.0003) paired (0.0029) with (0.0020) one (0.0009) of (0.0007) our (0.0043) body (0.0010) contouring (0.0013) applicators. (0.0012) works (0.0035) great (0.0004) with (0.0006) the (0.0035) it (0.0032) works! (0.0008) ultimate (0.0009) body (-0.0015) applicator (-0.0005) and (0.0006) the (-0.0003) it (0.0007) works! (0.0001) chin (0.0009) and (-0.0002) neck (-0.0005) applicator. (0.0002)
~~~~~~

**Node-1.9** (global 23325):

~~~~~~text
product (0.0002) from (0.0033) amazon (-0.0010) platform (-0.0009) with (0.0023) title (0.0025) and (0.0017) content (0.0029) : (0.0004) title (0.0037) : (0.0018) 21st (-0.0002) century (0.0004) slimming (0.0002) tea, (0.0014) green (0.0011) tea, (0.0006) 24 (0.0008) count (0.0004) ( (0.0023) pack (0.0006) of (0.0008) 3 (0.0022) ). (-0.0000) content (0.0042) : (0.0009) 21st (-0.0003) century (-0.0013) ' (0.0004) s (0.0010) herbal (0.0002) slimming (0.0006) tea (0.0006) is (0.0018) a (0.0004) blend (0.0004) of (0.0010) 100 (0.0012) % (0.0021) natural (0.0014) herbs (0.0025) which (0.0006) provides (0.0033) a (-0.0001) light, (0.0008) delicious (-0.0005) beverage (0.0004) that (0.0007) helps (0.0021) achieve (0.0015) results (0.0012) in (0.0007) aiding (0.0010) digestion (0.0011) and (0.0014) contributing (0.0024) to (0.0007) weight (0.0019) loss. (-0.0013)
~~~~~~
