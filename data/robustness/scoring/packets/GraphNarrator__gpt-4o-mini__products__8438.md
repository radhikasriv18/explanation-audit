# Reference packet: GraphNarrator__gpt-4o-mini__products__8438

- Method: GraphNarrator; configuration: gpt-4o-mini; dataset: products; target node: 8438
- Explanation source: `./robustness_2026-10-30/graphnarrator_gpt4omini/generated_expls-601/29.json` (messages[assistant])
- Scored scope (what the claims were extracted from): ### Free-Text Explanation section
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

Claims were extracted from the `### Free-Text Explanation` section only; the full assistant message is shown here.

~~~~~~text
### Reasoning

0. **Graph Structure Reconstruction:**

In the provided verbalized graph, the ROOT node (first line) is the target for classification. The single-digit indexed nodes are direct neighbors of ROOT, while the double-digit indexed nodes are:
  - Two hops away from ROOT
  - Direct children of their parent node

Thus, the graph structure of this verbalized graph is:

- ROOT (bottle with active venting technology)
  - Node-1 (children's probiotic chewables)
    - Node-1.1 (acidophilus wafers)
    - Node-1.2 (children's probiotic capsules)
    - Node-1.3 (ultimate flora kids probiotic)
    - Node-1.4 (dino dophilus chewables)
    - Node-1.5 (children's focus chewable tablets)

1. **Word-Level Evaluation:**

The ROOT node contains keywords such as "bottle," "activeflow," "venting technology," and "high heat resistant," which suggest it is a specialized bottle designed for health-related purposes, likely for hydration or nutrition. These terms indicate a focus on health and personal care products. The presence of "bpa-free" also emphasizes safety and health-consciousness, which are critical factors in the Health & Personal Care category.

2. **Graph-Level Aggregation:**

Node-1, which focuses on children's probiotic chewables, contains keywords like "probiotic," "kids," and "natural defense systems." These terms highlight the health aspect, particularly in supporting children's digestive health. The proximity of Node-1 to the ROOT node reinforces the classification as both nodes relate to health and wellness.

The child nodes of Node-1 (Node-1.1 to Node-1.5) further emphasize the health theme, with keywords related to digestive health, immune support, and children's well-being. This collective focus on health-related products across the entire co-purchase neighborhood strengthens the classification of the ROOT node into the Health & Personal Care category.

### Free-Text Explanation
```markdown
The classification of ROOT into "Health & Personal Care" is supported by its own keywords and the co-purchase neighborhood.

ROOT: Keywords like "bottle," "activeflow," and "venting technology" indicate that this is a specialized bottle designed for health-related purposes, emphasizing hydration or nutrition. The mention of "bpa-free" further highlights the product's safety and health-conscious attributes, aligning it with the Health & Personal Care category.
  - Node-1: This node focuses on children's probiotic chewables, with keywords such as "probiotic," "kids," and "natural defense systems," reinforcing the health aspect aimed at supporting children's digestive health.
    - Node-1.1: Acidophilus wafers support digestive health, indicating a focus on beneficial bacteria for children's well-being.
    - Node-1.2: Children's probiotic capsules are formulated to meet the digestive needs of kids, further emphasizing health support.
    - Node-1.3: The ultimate flora kids probiotic provides a gentle way to replenish balance in children's digestive systems.
    - Node-1.4: Dino dophilus chewables offer nutritive support for children's delicate digestive systems.
    - Node-1.5: Children's focus chewable tablets indicate a focus on overall health and wellness for kids.

In summary, ROOT's keywords strongly signal a health-oriented product, and the entire co-purchase neighborhood consists of items that support children's health and wellness, providing robust evidence for the "Health & Personal Care" classification.
```
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/29.json`).

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
<verbalized-graph>ROOT: product(0.02) amazon(0.02) platform(-0.01) title(0.02) content(-0.00) title(0.03) born(0.03) free(-0.02) 9(-0.00) oz.(-0.01) bpa-(-0.01) free(-0.01) high-(-0.00) heat(0.00) resistant(0.02) classic(0.01) bottle(-0.01) activeflow(0.02) venting(0.02) technology,(0.02) 3-(0.01) pack.(0.01) content(0.04) none(-0.02) 
Node-1: product(0.00) amazon(-0.00) platform(-0.00) title(0.00) content(0.00) title(0.00) culturelle(-0.00) kids!(0.00) chewables(0.00) probiotic,(0.00) kids(-0.00) 50-(-0.00) 100lbs,(-0.00) tablets,(-0.00) 30(0.00) ea(0.00) pack(-0.00) 2(-0.00) ).(-0.00) content(0.00) supporting(0.00) kids(0.00) natural(0.00) defense(0.00) systems(0.00) important(-0.00) promoting(0.00) overall(-0.00) health(0.00) well(0.00) helping(-0.00) alleviate(0.00) occasional(-0.00) digestive(0.00) distress.(-0.00) culturelle(0.00) kids!(0.00) chewables(0.00) support(0.00) child(-0.00) health(0.01) fostering(0.00) proper(0.00) balance(-0.00) good(0.00) bacteria(0.00) non-(0.00) benefical(0.00) bacteria(0.00) resides(0.00) gastrointestinal(-0.00) tract.(0.01) culturelle(-0.00) kids!(0.00) chewables(-0.00) contain(-0.00) lactobacillus(0.00) gg,(0.00) one(0.00) widely(0.00) studied(0.01) probiotic(0.00) strains.(0.00) demonstrated(0.00) survive(0.00) harsh(0.00) stomach(-0.00) acids(0.00) get(0.00) needed(-0.00) intestines(0.00) recognized(0.00) safe(0.00) regular(0.00) use.(0.01) research(-0.01) shown(-0.00) lactobacillus(0.00) gg(0.00) alleviates(-0.00) occasional(-0.00) digestive(-0.00) distress(-0.00) supporting(0.00) child(-0.00) natural(0.00) defenses.(-0.00) 
Node-1.1: product(-0.00) amazon(0.00) platform(-0.00) title(0.00) content(0.00) title(0.00) american(0.00) health(-0.00) acidophilus(0.00) bifidus(0.00) fruit--(-0.00) 100(-0.00) wafers.(-0.00) content(0.00) maintain(0.00) daily(-0.00) digestive(0.00) health,(-0.00) natural(0.00) regularity(0.00) optimal(0.00) intestinal(0.00) balance(0.00) milk-(0.00) free(0.00) chewable(-0.00) acidophilus.(0.00) acidophilus(0.00) helps(0.00) stimulate(0.00) growth(0.00) beneficial(0.00) bacteria(0.00) digestive(0.00) intestinal(0.00) tracts,(0.00) encourages(0.00) proper(0.00) nutrient(0.00) absorption(0.00) promotes(0.00) immune(0.00) health.(0.00) acidophilus(0.00) ideal(0.00) way(-0.00) enhance(0.00) positive(0.00) flora.(-0.00) 100(0.00) naturally(0.00) delicious(0.00) assorted(-0.00) fruit(-0.00) flavored(0.00) chewable(0.00) acidophilus(0.00) ideal(0.00) lactose-(0.00) intolerant.(0.00) wafer(-0.00) contains(-0.00) mix(-0.00) two(0.00) classic(0.00) latobacilli-(0.00) acidophilus(0.00) bifidum-(-0.00) guaranteed(-0.00) deliver(0.00) 1(-0.00) billion(0.00) microorganisms(0.00) per(0.00) serving.(0.00) addition,(0.00) chewable(0.00) acidophilus(0.00) wafers(0.00) easy,(0.00) convenient(0.00) great(0.00) tasting(0.00) way(-0.00) receive(-0.00) digestive(0.00) health(0.00) benefits.(0.00) acidophilus(0.00) bifidum,(-0.00) support(-0.00) digestive(-0.00) health(0.00) feel(0.00) good(0.00) day,(-0.00) everyday.(0.00) 
Node-1.2: product(-0.00) amazon(-0.00) platform(-0.00) title(0.00) content(-0.00) title(0.00) udo(0.00) choice(0.00) children(0.00) blend(0.00) probiotic(-0.00) 60(-0.00) capsules(-0.00) ".(-0.00) content(0.00) udo(0.00) x2019(0.00) choice(0.00) children(0.00) x2019(0.00) probiotic(-0.00) formulated(0.00) meet(0.00) digestive(0.00) needs(-0.00) children(-0.00) ages(0.00) 5-(0.00) 15(-0.00) years.(0.00) contains(-0.00) 8(0.00) strains(0.00) friendly(0.00) bacteria(0.00) 4(0.00) billion(0.00) viable(0.00) cells(0.00) per(-0.00) capsule(-0.00) date(-0.00) manufacture(0.00) designed(0.00) reflect(0.00) normal(0.00) healthy(0.00) childhood(0.00) microflora.(0.00) supports(0.00) development(0.00) flora(0.00) small(0.00) large(0.00) intestines.(0.00) udo(0.00) x2019(0.00) choice(0.00) children(-0.00) x2019(0.00) probiotic(-0.00) helps(-0.00) maintain(0.00) proper(0.00) digestion(-0.00) strengthen(0.00) immune(-0.00) system.(0.00) use(-0.00) extra(-0.00) strength(-0.00) amount(0.00) relieve(0.00) symptoms(0.00) associated(0.00) intestinal(0.00) discomfort.(0.00) unique(0.00) company(-0.00) features(0.00) flora,(0.00) manufacturing(0.00) supplying(0.00) quality(-0.00) herbal(0.00) remedies(0.00) distribution(0.00) united(0.00) states(0.00) since(0.00) 1988,(0.00) roots(0.00) stretch(0.00) back(0.00) germany(0.00) early(0.00) 1900(0.00) s,(0.00) dr.(0.00) otto(-0.00) greither,(0.00) grandfather(0.00) current(0.00) owner(0.00) thomas(0.00) greither,(0.00) dedicated(-0.00) life(0.00) discovery,(0.00) production(0.00) distribution(-0.00) natural(0.00) health(-0.00) care(-0.00) products.(0.00) preserved(-0.00) original(0.00) dedication(-0.00) perfect(-0.00) european(0.00) herbal(-0.00) remedies(-0.00) ensure(-0.00) maximum(0.00) purity,(0.00) quality(-0.00) potency.(0.00) product(-0.00) specifications(-0.00) 60(-0.00) caps.(0.00) 
Node-1.3: product(-0.00) amazon(0.00) platform(0.00) title(0.00) content(0.00) title(0.00) renew(0.00) life-(0.00) ultimate(0.00) flora(0.00) kids(0.00) probiotic-(0.00) 30(0.00) chewable(0.00) tablets.(-0.00) content(0.00) ultimate(0.00) flora(0.00) kids(0.00) probiotic(0.00) great-(0.00) tasting,(0.00) safe(0.00) gentle(0.00) way(0.00) help(0.00) replenish(0.00) balance(-0.00) 
Node-1.4: product(-0.00) amazon(-0.00) platform(-0.00) title(0.00) content(-0.00) title(0.00) kal(0.00) dino-(0.00) dophilus(0.00) probiotic(0.00) 2(0.00) billion(0.00) chewables,(0.00) black(0.00) cherry,(0.00) 60(-0.00) count.(0.00) content(0.00) dinodophilus(0.00) probiotic(-0.00) blend(-0.00) combination(0.00) important(0.00) intestinal(0.00) flora(0.00) intended(-0.00) provide(-0.00) nutritive(0.00) support(0.00) child(0.00) delicate(0.00) digestive(0.00) system.(-0.00) 
Node-1.5: product(-0.00) amazon(0.00) platform(0.00) title(0.00) content(0.00) title(-0.00) focus(0.00) children(0.00) solaray(0.00) 60(0.00) chewable(0.00) tablet.(0.00) content(-0.00) focus(-0.00) children(0.00) solaray(-0.00) 60(0.00) chewable(0.00) tablet(0.00) chewable(0.00) sm</verbalized-graph>

### Classification Label
Health & Personal Care

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 8438
- Title: Born Free 9 oz. BPA-Free High-Heat Resistant Classic Bottle with ActiveFlow Venting Technology, 3-Pack
- True class (canonical `y`): **Baby**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Health & Personal Care**
- Prediction recorded by this method's pipeline: **Health & Personal Care**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Born Free 9 oz. BPA-Free High-Heat Resistant Classic Bottle with ActiveFlow Venting Technology, 3-Pack. Content: None
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 6 nodes

| node id | true class | title |
|---|---|---|
| 992 | Health & Personal Care | Culturelle Kids! Chewables Probiotic, for kids 50-100lbs, Tablets, 30 ea(Pack of 2) |
| 37121 | Baby | Kidco F710 Baby Food Mill |
| 37122 | Baby | Zo-Li Two Baby Wide Neck Baby Bottles (10 Oz) |
| 37123 | Baby | Beaba Bib Expresso 3 in 1 Baby Bottle &amp; Food Warmer |
| 37124 | Health & Personal Care | Braun Thermoscan Ear Thermometer-irt4520 |
| 37125 | Baby | Born Free Silicone Teether |

### 2-hop (shortest distance exactly 2): 12 nodes

| node id | true class | title |
|---|---|---|
| 75 | Health & Personal Care | KAL Dino-Dophilus Probiotic 2 Billion Chewables, Black Cherry, 60 Count |
| 984 | Health & Personal Care | Power Probiotic ENT Kids - Strawberry Blast 30 Chewable Tablets \| Supports the Natural Immune Defenses of the Ears, Nose/Nasopharynx, and Throat \| Promotes Oral Health and Fresh Breath \| Individually Sealed in Nitrogen-Purged Aluminum Blister Packs to Insure Freshness |
| 987 | Health & Personal Care | ReNew Life - Buddy Bear Probiotic for Kids Orange - 60 Chewable Tablets |
| 991 | Health & Personal Care | American Health Acidophilus with Bifidus Fruit -- 100 Wafers |
| 995 | Health & Personal Care | "Udo's Choice Children's Blend Probiotic 60 Capsules" |
| 8340 | Health & Personal Care | ReNew Life - Ultimate Flora Kids Probiotic - 30 Chewable Tablets |
| 8389 | Health & Personal Care | Amerifit Culturelle Probiotics for Kids, 30 Count |
| 8433 | Health & Personal Care | Focus for Children Solaray 60 Chewable Tablet |
| 8434 | Beauty | BIOGAIA PROBIOTIC CHEWABLE TABLETS 60 TABS |
| 8435 | Baby | green sprouts Warming Plate, Sage |
| 8436 | Baby | Medela Swing Breastpump |
| 8437 | Health & Personal Care | Culturelle Probiotics for Kids 30 Ct (2 Pack) |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/29.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Health & Personal Care**, ground truth = **Baby**.
The verbalized graph is 21955 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 8438 | 31 | 0.0350 | yes |
| Node-1 | 1 | 992 | 141 | 0.0303 | yes |
| Node-1.1 | 7 | 991 | 145 | 0.0003 | yes |
| Node-1.2 | 8 | 995 | 213 | 0.0004 | yes |
| Node-1.3 | 9 | 8340 | 40 | 0.0020 | yes |
| Node-1.4 | 10 | 75 | 47 | 0.0020 | yes |
| Node-1.5 | 11 | 8433 | 182 | 0.0003 | yes |
| Node-1.6 | 12 | 987 | 288 | 0.0018 | no |
| Node-1.7 | 13 | 8435 | 44 | 0.0012 | no |
| Node-1.8 | 14 | 8436 | 289 | 0.0005 | no |
| Node-1.9 | 15 | 984 | 151 | 0.0010 | no |
| Node-1.10 | 16 | 8434 | 173 | 0.0015 | no |
| Node-2 | 2 | 37121 | 86 | 0.0154 | no |
| Node-3 | 3 | 37122 | 80 | 0.0278 | no |
| Node-4 | 4 | 37123 | 226 | 0.0058 | no |
| Node-5 | 5 | 37124 | 252 | 0.0085 | no |
| Node-6 | 6 | 37125 | 34 | 0.0482 | no |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.10, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->Node-1.6, Node-1->Node-1.7, Node-1->Node-1.8, Node-1->Node-1.9, Node-1->ROOT, Node-1.1->Node-1, Node-1.10->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, Node-1.6->Node-1, Node-1.7->Node-1, Node-1.8->Node-1, Node-1.9->Node-1, Node-2->ROOT, Node-3->ROOT, Node-4->ROOT, Node-5->ROOT, Node-6->ROOT, ROOT->Node-1, ROOT->Node-2, ROOT->Node-3, ROOT->Node-4, ROOT->Node-5, ROOT->Node-6

### Tokens and scores

**ROOT** (global 8438):

~~~~~~text
product (0.0187) from (-0.0160) amazon (0.0157) platform (-0.0132) with (-0.0097) title (0.0200) and (0.0019) content (-0.0011) : (-0.0044) title (0.0282) : (0.0063) born (0.0338) free (-0.0156) 9 (-0.0050) oz. (-0.0066) bpa- (-0.0056) free (-0.0119) high- (-0.0022) heat (0.0006) resistant (0.0243) classic (0.0145) bottle (-0.0107) with (0.0013) activeflow (0.0181) venting (0.0182) technology, (0.0226) 3- (0.0064) pack. (0.0133) content (0.0350) : (-0.0195) none (-0.0243)
~~~~~~

**Node-1** (global 992):

~~~~~~text
product (0.0014) from (-0.0030) amazon (-0.0038) platform (-0.0049) with (-0.0005) title (0.0022) and (-0.0008) content (0.0016) : (-0.0005) title (0.0040) : (0.0002) culturelle (-0.0003) kids! (0.0012) chewables (0.0017) probiotic, (0.0000) for (0.0004) kids (-0.0003) 50- (-0.0011) 100lbs, (-0.0001) tablets, (-0.0017) 30 (0.0022) ea (0.0013) ( (-0.0026) pack (-0.0017) of (-0.0006) 2 (-0.0007) ). (-0.0002) content (0.0038) : (0.0032) supporting (0.0021) kids (0.0027) ' (-0.0021) natural (0.0029) defense (0.0018) systems (0.0009) is (0.0018) important (-0.0002) to (-0.0001) promoting (0.0012) their (0.0024) overall (-0.0000) health (0.0023) as (-0.0005) well (0.0007) as (-0.0010) helping (-0.0003) to (0.0004) alleviate (0.0014) occasional (-0.0007) digestive (0.0031) distress. (-0.0012) * (0.0026) culturelle (0.0038) kids! (0.0034) chewables (0.0006) support (0.0042) a (0.0023) child (-0.0007) ' (0.0000) s (0.0011) health (0.0056) by (-0.0008) fostering (0.0003) the (-0.0039) proper (0.0019) balance (-0.0001) between (0.0015) good (0.0005) bacteria (0.0004) and (-0.0015) the (0.0008) non- (0.0013) benefical (0.0007) bacteria (0.0030) that (0.0021) resides (0.0005) in (0.0007) the (0.0018) gastrointestinal (-0.0001) tract. (0.0056) culturelle (-0.0016) kids! (0.0010) chewables (-0.0016) contain (-0.0023) lactobacillus (0.0012) gg, (0.0014) one (0.0040) of (0.0011) the (0.0045) most (0.0034) widely (0.0048) studied (0.0071) probiotic (0.0027) strains. (0.0040) it (0.0021) is (0.0039) demonstrated (0.0009) to (-0.0007) survive (0.0007) harsh (0.0009) stomach (-0.0018) acids (0.0043) to (0.0009) get (0.0011) where (0.0002) it (-0.0006) ' (-0.0013) s (0.0016) needed (-0.0010) most (0.0001) in (0.0001) the (-0.0018) intestines (0.0010) and (-0.0011) is (0.0041) recognized (0.0045) as (0.0027) safe (0.0026) for (0.0002) regular (0.0018) use. (0.0142) * (0.0157) research (-0.0078) has (0.0010) shown (-0.0034) that (0.0037) lactobacillus (0.0010) gg (0.0007) alleviates (-0.0036) occasional (-0.0020) digestive (-0.0011) distress (-0.0002) while (-0.0025) supporting (0.0030) a (0.0021) child (-0.0030) ' (-0.0015) s (-0.0012) natural (0.0031) defenses. (-0.0036) * (0.0303)
~~~~~~

**Node-1.1** (global 991):

~~~~~~text
product (-0.0000) from (-0.0002) amazon (0.0001) platform (-0.0002) with (-0.0001) title (0.0002) and (0.0001) content (0.0001) : (0.0002) title (0.0003) : (0.0001) american (0.0001) health (-0.0000) acidophilus (0.0000) with (-0.0001) bifidus (0.0001) fruit-- (-0.0000) 100 (-0.0001) wafers. (-0.0001) content (0.0002) : (-0.0003) maintain (0.0000) your (-0.0000) daily (-0.0001) digestive (0.0001) health, (-0.0001) natural (0.0001) regularity (0.0001) and (-0.0001) optimal (0.0001) intestinal (0.0000) balance (0.0000) with (-0.0001) milk- (0.0001) free (0.0001) chewable (-0.0000) acidophilus. (0.0001) acidophilus (0.0000) helps (0.0001) to (0.0000) stimulate (0.0001) the (0.0000) growth (0.0001) of (-0.0000) beneficial (0.0000) bacteria (0.0002) in (-0.0000) the (0.0000) digestive (0.0001) and (-0.0000) intestinal (0.0000) tracts, (0.0001) encourages (0.0001) proper (0.0000) nutrient (0.0000) absorption (0.0001) and (0.0000) promotes (0.0001) immune (0.0001) health. (0.0001) acidophilus (0.0000) is (0.0002) the (-0.0002) ideal (0.0002) way (-0.0001) to (0.0000) enhance (0.0001) our (-0.0001) positive (0.0001) flora. (-0.0000) this (0.0001) 100 (0.0000) % (0.0001) naturally (0.0001) delicious (0.0001) assorted (-0.0000) fruit (-0.0001) flavored (0.0002) chewable (0.0001) acidophilus (0.0000) is (0.0002) ideal (0.0001) for (-0.0000) those (0.0001) who (0.0001) are (0.0001) lactose- (0.0001) intolerant. (0.0001) each (-0.0000) wafer (-0.0001) contains (-0.0000) a (0.0001) mix (-0.0000) of (-0.0000) two (0.0001) classic (0.0002) latobacilli- (0.0000) acidophilus (0.0000) and (-0.0001) bifidum- (-0.0000) and (0.0000) is (0.0002) guaranteed (-0.0000) to (-0.0000) deliver (0.0001) 1 (-0.0000) billion (0.0001) microorganisms (0.0000) per (0.0001) serving. (0.0001) in (-0.0000) addition, (0.0000) these (0.0001) chewable (0.0000) acidophilus (0.0000) wafers (0.0000) are (0.0001) an (0.0001) easy, (0.0000) convenient (0.0001) and (-0.0001) great (0.0000) tasting (0.0000) way (-0.0001) to (-0.0000) receive (-0.0000) digestive (0.0000) health (0.0001) benefits. (0.0002) with (-0.0000) acidophilus (0.0000) and (-0.0000) bifidum, (-0.0000) you (-0.0000) can (0.0002) support (-0.0000) your (0.0002) digestive (-0.0000) health (0.0000) and (-0.0001) feel (0.0000) good (0.0000) all (0.0000) day, (-0.0001) everyday. (0.0001)
~~~~~~

**Node-1.2** (global 995):

~~~~~~text
product (-0.0000) from (-0.0001) amazon (-0.0001) platform (-0.0001) with (0.0000) title (0.0001) and (0.0002) content (-0.0000) : (0.0001) title (0.0001) : (0.0001) " (-0.0004) udo (0.0001) ' (0.0001) s (0.0000) choice (0.0001) children (0.0001) ' (0.0000) s (0.0001) blend (0.0002) probiotic (-0.0000) 60 (-0.0002) capsules (-0.0002) ". (-0.0000) content (0.0001) : (-0.0001) udo (0.0000) & (0.0001) # (0.0001) x2019 (0.0001) ; (0.0001) s (-0.0000) choice (0.0002) children (0.0000) & (0.0002) # (0.0000) x2019 (0.0001) ; (-0.0001) s (-0.0002) probiotic (-0.0000) was (0.0001) formulated (0.0002) to (-0.0000) meet (0.0000) the (-0.0000) digestive (0.0000) needs (-0.0001) of (0.0001) children (-0.0000) ages (0.0000) 5- (0.0001) 15 (-0.0000) years. (0.0003) it (-0.0003) contains (-0.0001) 8 (0.0001) strains (0.0001) of (0.0002) friendly (0.0002) bacteria (0.0001) with (0.0001) 4 (0.0000) billion (0.0000) viable (0.0000) cells (0.0001) per (-0.0000) capsule (-0.0001) ( (-0.0000) at (0.0000) date (-0.0000) of (0.0000) manufacture (0.0002) ) (-0.0000) designed (0.0002) to (-0.0001) reflect (0.0001) normal (0.0001) healthy (0.0001) childhood (0.0001) microflora. (0.0003) it (-0.0003) supports (0.0003) the (-0.0001) development (0.0003) of (-0.0001) flora (0.0002) in (-0.0000) the (0.0000) small (0.0001) and (-0.0000) large (0.0001) intestines. (0.0001) * (-0.0000) udo (0.0001) & (0.0000) # (0.0001) x2019 (0.0002) ; (0.0000) s (-0.0000) choice (0.0001) children (-0.0001) & (0.0002) # (-0.0001) x2019 (0.0002) ; (0.0004) s (0.0002) probiotic (-0.0002) helps (-0.0000) maintain (0.0001) proper (0.0000) digestion (-0.0000) and (0.0000) strengthen (0.0000) the (0.0000) immune (-0.0000) system. (0.0002) * (0.0002) use (-0.0000) extra (-0.0002) strength (-0.0001) amount (0.0000) to (0.0002) relieve (0.0001) symptoms (0.0001) associated (0.0001) with (0.0000) intestinal (0.0002) discomfort. (0.0004) * (0.0001) unique (0.0003) company (-0.0003) features (0.0001) : (-0.0002) at (0.0003) flora, (0.0001) we (0.0002) have (0.0000) been (0.0000) manufacturing (0.0001) and (0.0001) supplying (0.0002) quality (-0.0000) herbal (0.0000) remedies (0.0001) for (-0.0000) distribution (0.0001) in (0.0000) the (-0.0001) united (0.0000) states (0.0001) since (0.0000) 1988, (0.0001) but (0.0002) our (-0.0002) roots (0.0002) stretch (0.0002) back (0.0001) to (0.0001) germany (0.0000) in (-0.0000) the (0.0001) early (0.0000) 1900 (0.0001) ' (0.0000) s, (0.0001) where (0.0000) dr. (0.0000) otto (-0.0000) greither, (0.0001) grandfather (0.0002) of (-0.0001) the (0.0000) current (0.0001) owner (0.0000) thomas (0.0001) greither, (0.0002) dedicated (-0.0000) his (0.0001) life (0.0001) to (0.0000) the (-0.0001) discovery, (0.0001) production (0.0000) and (0.0001) distribution (-0.0000) of (0.0000) natural (0.0001) health (-0.0000) care (-0.0001) products. (0.0003) we (-0.0001) have (0.0002) preserved (-0.0002) his (-0.0001) original (0.0000) dedication (-0.0001) to (0.0001) perfect (-0.0001) european (0.0002) herbal (-0.0002) remedies (-0.0000) that (0.0001) ensure (-0.0002) maximum (0.0000) purity, (0.0002) quality (-0.0003) and (-0.0001) potency. (0.0002) product (-0.0006) specifications (-0.0000) : (-0.0003) 60 (-0.0003) caps. (0.0001)
~~~~~~

**Node-1.3** (global 8340):

~~~~~~text
product (-0.0000) from (0.0012) amazon (0.0003) platform (0.0004) with (0.0007) title (0.0004) and (0.0003) content (0.0014) : (-0.0008) title (0.0008) : (0.0011) renew (0.0007) life- (0.0007) ultimate (0.0007) flora (0.0003) kids (0.0011) probiotic- (0.0009) 30 (0.0010) chewable (0.0010) tablets. (-0.0016) content (0.0020) : (0.0008) ultimate (0.0002) flora (0.0011) kids (0.0006) probiotic (0.0008) is (0.0002) a (0.0000) great- (0.0018) tasting, (0.0006) safe (0.0007) and (0.0016) gentle (0.0007) way (0.0005) to (0.0015) help (0.0006) replenish (0.0007) the (-0.0013) balance (-0.0005) of (0.0009)
~~~~~~

**Node-1.4** (global 75):

~~~~~~text
product (-0.0004) from (0.0007) amazon (-0.0005) platform (-0.0012) with (-0.0000) title (0.0014) and (-0.0002) content (-0.0003) : (0.0010) title (0.0005) : (0.0010) kal (0.0001) dino- (0.0001) dophilus (0.0003) probiotic (0.0000) 2 (0.0009) billion (0.0001) chewables, (0.0006) black (0.0013) cherry, (0.0012) 60 (-0.0018) count. (0.0002) content (0.0010) : (0.0003) dinodophilus (0.0004) probiotic (-0.0001) blend (-0.0000) is (0.0005) a (0.0003) combination (0.0002) of (0.0004) important (0.0007) intestinal (0.0020) flora (0.0009) intended (-0.0001) to (0.0001) provide (-0.0000) nutritive (0.0005) support (0.0002) for (0.0006) a (0.0010) child (0.0006) ' (0.0005) s (0.0004) delicate (0.0003) digestive (0.0003) system. (-0.0002)
~~~~~~

**Node-1.5** (global 8433):

~~~~~~text
product (-0.0000) from (0.0001) amazon (0.0000) platform (0.0000) with (0.0001) title (0.0000) and (0.0001) content (0.0000) : (0.0001) title (-0.0000) : (0.0000) focus (0.0000) for (0.0000) children (0.0000) solaray (0.0000) 60 (0.0000) chewable (0.0000) tablet. (0.0000) content (-0.0001) : (0.0001) focus (-0.0000) for (0.0000) children (0.0000) by (0.0001) solaray (-0.0000) 60 (0.0001) chewable (0.0000) tablet (0.0000) chewable (0.0000) smartbite (0.0000) wafers (0.0000) in (0.0000) tart (0.0000) grape (-0.0000) flavor. (-0.0001) size (-0.0000) 60ct (0.0000) directions (0.0000) as (0.0000) a (-0.0002) dietary (0.0002) supplement (-0.0001) take (-0.0000) one (0.0000) chewable (0.0000) smartbite (0.0000) wafer (0.0000) 1- (0.0001) 2 (0.0001) times (0.0001) daily (0.0000) with (0.0000) a (-0.0002) meal. (0.0000) serving (0.0001) size (0.0000) 1 (-0.0001) tablet (-0.0000) 60 (-0.0000) servings (-0.0000) per (-0.0000) container (0.0000) ingredients (-0.0002) amount (-0.0001) per (0.0000) serving (0.0000) daily (0.0001) value (0.0000) + (0.0000) calories (0.0001) 5 (0.0001) guaranteed (0.0001) potency (0.0000) grape (-0.0000) seed (0.0000) extract (0.0002) supplying (0.0000) 9. (0.0002) 5mg (0.0002) ( (0.0003) 95 (0.0001) ) (0.0000) opc (-0.0000) 10 (0.0001) mg (-0.0002) leci- (0.0000) ps (-0.0000) phosphatidylserine (-0.0000) concentrate (-0.0000) ( (0.0001) lecithin (-0.0000) ) (-0.0001) supplying (-0.0004) 10mg (-0.0000) phosphatidylserine (-0.0000) 25 (-0.0000) mg (-0.0001) l- (0.0000) tyrosine (0.0001) 25 (0.0000) mg (-0.0001) dmae (0.0000) ( (0.0001) as (0.0000) dimethylaminoethanol (0.0000) bitartrate (0.0000) ) (0.0001) 25 (0.0001) mg (-0.0001) stevia (-0.0001) ( (0.0002) leaf (0.0001) extract (0.0001) ) (0.0000) 3 (-0.0000) mg (-0.0001) griffonia (0.0000) simplicifolia (0.0001) ( (0.0002) bean (-0.0000) ) (0.0000) 50 (0.0000) mg (-0.0001) total (-0.0000) carbohydrate (0.0000) 1 (-0.0000) g (-0.0001) 1 (-0.0001) key (-0.0000) to (-0.0000) ingredients (-0.0001) daily (0.0000) value (-0.0001) not (-0.0000) established. (-0.0001) + (0.0001) percent (-0.0001) daily (0.0000) value (-0.0001) is (0.0001) based (0.0000) on (0.0001) a (-0.0002) 2 (0.0001) 000 (0.0000) calorie (-0.0000) diet. (-0.0000) values (-0.0002) differ (0.0001) depending (0.0002) on (0.0001) age (0.0001) values (-0.0001) differ (0.0000) depending (0.0000) on (0.0001) age (0.0000) other (-0.0000) ingredients (-0.0001) sorbitol (0.0000) xylitol (-0.0000) blueberry (-0.0000) ( (0.0001) fruit (0.0000) ) (0.0000) natural (0.0000) flavors (-0.0002) guar (-0.0001) gum (-0.0001) stearic (-0.0000) acid (-0.0000) silica (-0.0000) and (0.0001) citric (0.0000) acid (-0.0000) other (-0.0000) see (0.0001) product (0.0003) label (0.0000) for (0.0001) more (-0.0001) information. (0.0000)
~~~~~~

**Node-1.6** (global 987):

~~~~~~text
product (-0.0001) from (-0.0003) amazon (0.0005) platform (0.0001) with (-0.0002) title (0.0001) and (-0.0001) content (0.0001) : (0.0002) title (0.0003) : (0.0002) renew (0.0000) life- (0.0002) buddy (-0.0000) bear (-0.0000) probiotic (0.0002) for (-0.0002) kids (0.0001) orange- (0.0002) 60 (-0.0001) chewable (-0.0000) tablets. (0.0002) content (-0.0001) : (0.0002) renew (0.0001) life (0.0001) buddy (0.0001) bear (0.0001) chewable (0.0000) probiotic (0.0001) for (-0.0001) children (0.0002) orange (-0.0003) flavor- (0.0002) 60 (0.0002) tablets (0.0001) renew (0.0001) life (0.0000) buddy (0.0001) bear (0.0001) chewable (-0.0000) probiotic (0.0002) for (-0.0001) children (0.0007) orange (0.0003) flavor (-0.0001) is (-0.0002) a (0.0002) natural (-0.0001) probiotic (0.0000) supplement (-0.0001) formulated (0.0006) for (-0.0000) children (0.0004) age (0.0001) 2 (0.0003) and (0.0002) older (-0.0001) who (0.0000) are (0.0002) capable (0.0001) of (-0.0001) chewing. (0.0001) each (0.0003) easy- (0.0003) to (0.0001) chew (0.0000) bear (0.0001) tablet (-0.0001) contains (0.0003) acidophilus, (0.0002) bifidus (0.0002) and (0.0001) other (0.0003) active (0.0002) cultures (0.0001) help (0.0002) support (0.0002) digestive (-0.0001) and (-0.0000) immune (0.0001) health. (-0.0001) fructooligosaccharide (0.0001) ( (0.0003) fos (0.0001) ) (0.0002) helps (0.0002) nourish (0.0001) the (0.0007) beneficial (0.0003) flora (-0.0000) and (0.0002) maximize (-0.0001) bioavailability. (0.0001) natural (0.0002) ingredients (0.0002) 1 (0.0003) billion (-0.0000) active (0.0000) bifidobacteria (0.0000) and (-0.0000) lactobacillus (0.0000) cultures (-0.0001) supports (0.0001) digestive (0.0001) and (-0.0000) immune (0.0002) health (0.0001) fos (0.0003) to (-0.0002) nourish (0.0001) beneficial (0.0001) bacteria (0.0001) delicious, (0.0001) natural (0.0000) sun- (0.0000) kissed (0.0002) orange (-0.0001) flavor (0.0005) frequently (-0.0001) asked (0.0006) questions (-0.0002) what (-0.0004) are (0.0001) probiotics? (0.0001) there (-0.0001) are (0.0001) literally (0.0004) trillions (0.0002) of (-0.0002) microorganisms (0.0001) in (-0.0001) the (0.0001) human (-0.0002) digestive (0.0000) tract. (0.0004) some (-0.0000) are (0.0001) beneficial, (0.0002) some (-0.0000) are (0.0000) harmful, (0.0002) and (-0.0001) some (0.0001) are (-0.0000) neutral. (0.0002) probiotics (0.0001) are (0.0001) the (0.0001) good (0.0001) type (0.0002) of (-0.0001) bacteria (0.0001) that (0.0001) help (0.0000) crowd (0.0000) out (0.0001) the (0.0000) harmful (-0.0000) bacteria (0.0001) in (-0.0000) order (0.0001) to (-0.0000) keep (0.0000) you (-0.0001) healthy. (0.0001) this (0.0000) is (0.0001) important (0.0002) because (0.0003) more (0.0001) than (-0.0000) 70 (0.0001) percent (-0.0000) of (-0.0002) your (-0.0001) immune (0.0000) defenses (0.0002) can (0.0000) be (0.0001) found (0.0002) in (-0.0001) your (-0.0001) digestive (0.0002) tract. (0.0002) ideally, (0.0002) there (0.0005) should (0.0001) be (0.0002) about (0.0001) 80 (0.0001) percent (0.0003) good (0.0000) / (0.0004) neutral (0.0001) bacteria (0.0001) to (0.0000) about (0.0000) 20 (0.0001) percent (0.0002) harmful (0.0001) bacteria (0.0000) in (-0.0001) your (-0.0002) gut. (0.0003) however, (0.0001) everyday (0.0001) factors (0.0002) such (0.0001) as (0.0001) diet, (0.0001) stress, (0.0003) travel, (0.0001) exposure (0.0001) to (-0.0000) illness (0.0000) and (0.0002) even (0.0002) the (0.0002) use (0.0001) of (-0.0001) certain (0.0003) medications (-0.0002) can (0.0002) diminish (0.0002) the (0.0001) number (0.0001) of (-0.0000) healthy (-0.0001) bacteria (-0.0000) in (-0.0001) the (0.0001) digestive (0.0000) tract (0.0000) and (-0.0001) upset (-0.0001) an (0.0001) otherwise (0.0001) balanced (0.0001) intestinal (0.0001) environment. (0.0001) this (0.0002) allows (0.0002) unhealthy (0.0001) microbes (0.0004) to (0.0000) flourish (0.0001) and (0.0001) may (0.0002) lead (0.0001) to (0.0000) intestinal (0.0001) issues (0.0001) such (0.0001) as (-0.0001) diarrhea (0.0001) and (-0.0001) constipation, (0.0001) as (0.0000) well (-0.0000) as (0.0000) a (0.0001) decline (0.0001) in (-0.0001) healthy (-0.0001) immune (0.0000) function. (0.0001) taking (0.0000) a (0.0001) daily (-0.0000) probiotic (-0.0002) supplement (0.0001) can (-0.0000) help (-0.0001) replenish (0.0000) good (0.0001) bacteria (-0.0001) and (0.0002) restore (0.0001) a (-0.0004) healthy (0.0001) bacterial (0.0001) balance. (-0.0007) what (0.0002) are (-0.0013) the (-0.0005) benefits (0.0018) of (-0.0022)
~~~~~~

**Node-1.7** (global 8435):

~~~~~~text
product (0.0012) from (0.0001) amazon (0.0007) platform (0.0007) with (0.0001) title (0.0007) and (0.0003) content (0.0011) : (0.0011) title (0.0008) : (0.0006) green (0.0001) sprouts (0.0004) warming (-0.0002) plate, (0.0003) sage. (0.0006) content (0.0007) : (0.0001) new. (0.0002) bpa, (0.0003) pvc (0.0001) and (0.0003) phthalate (0.0001) free. (0.0008) keep (0.0000) food (0.0004) warm (0.0003) when (-0.0001) base (-0.0000) is (0.0004) filled (0.0003) with (0.0002) warm (0.0000) water. (0.0005) divided (0.0002) compartments (0.0005) and (0.0003) non- (0.0002) slip (0.0001) suction (0.0004) on (0.0002) bottom. (0.0000) dishwasher (0.0002) safe. (0.0005)
~~~~~~

**Node-1.8** (global 8436):

~~~~~~text
product (0.0001) from (0.0002) amazon (-0.0000) platform (-0.0001) with (0.0001) title (0.0000) and (0.0000) content (0.0001) : (0.0002) title (0.0001) : (0.0002) medela (0.0001) swing (-0.0002) breastpump. (-0.0000) content (0.0000) : (-0.0000) so, (0.0000) you (0.0000) want (0.0001) a (-0.0000) medela (0.0000) electric (0.0001) breast (0.0000) pump- (0.0001) after (0.0000) all, (0.0001) it (0.0000) is (0.0000) the (-0.0000) gold (0.0001) standard- (-0.0000) but (-0.0001) you (-0.0000) ' (0.0001) re (0.0000) watching (0.0000) your (-0.0001) budget? (-0.0000) you (0.0000) ' (0.0001) ll (-0.0001) love (-0.0000) the (-0.0000) swing (-0.0000) & (-0.0001) trade (0.0001) ; (-0.0000) breastpump, (-0.0000) medela (-0.0000) ' (-0.0000) s (-0.0001) smallest, (0.0000) lightest, (-0.0000) most- (-0.0000) affordable (0.0000) electric (0.0000) breast (-0.0001) pump! (0.0003) this (-0.0000) single (-0.0001) breast (-0.0000) pump (0.0001) features (-0.0002) medela (0.0000) ' (-0.0001) s (-0.0001) exclusive (0.0001) 2- (0.0001) phase (0.0001) expression (-0.0003) ( (0.0003) r (-0.0002) ) (0.0001) technology (-0.0004) for (0.0002) efficient (-0.0002) pumping. (0.0000) and (0.0001) it (0.0000) ' (-0.0001) s (-0.0000) so (0.0000) compact (0.0000) and (0.0000) portable, (0.0001) you (0.0000) can (-0.0000) clip (-0.0000) it (-0.0001) to (-0.0000) your (-0.0001) belt, (-0.0000) or (0.0001) even (-0.0000) hang (-0.0001) it (-0.0001) off (-0.0001) your (-0.0003) shoulder. (0.0002) swing (-0.0001) includes (-0.0001) all (-0.0001) the (-0.0002) accessories (0.0001) you (-0.0000) need (0.0000) to (-0.0000) get (-0.0000) started (-0.0000) ( (-0.0000) including (0.0001) a (0.0000) bottle (-0.0000) stand (0.0000) and (0.0000) two (-0.0000) breastmilk (0.0000) bottles (-0.0001) ). (0.0000) all (0.0000) housed (-0.0001) in (0.0000) a (-0.0000) portable (0.0000) drawstring (0.0000) bag. (-0.0001) ac (0.0001) adaptor (-0.0000) included, (0.0001) or (-0.0001) takes (-0.0000) 4 (-0.0000) " (-0.0002) aa (-0.0000) " (0.0001) batteries (0.0001) ( (-0.0001) sold (-0.0000) separately (0.0001) ) (0.0000) for (0.0000) pumping (0.0000) on (0.0000) the (-0.0001) go. (-0.0003) the (-0.0001) swing (-0.0000) breast (0.0001) pump (0.0001) features (0.0001) medela (0.0001) ' (-0.0001) s (-0.0001) 2- (-0.0001) phase (0.0001) expression (0.0002) ( (-0.0004) r (0.0000) ) (-0.0000) technology (-0.0000) which (-0.0001) mimics (0.0000) a (-0.0001) baby (0.0001) ' (-0.0000) s (0.0000) natural (0.0001) nursing (0.0000) patterns. (0.0000) a (-0.0001) light, (-0.0001) fast (-0.0000) stimulation (0.0001) phase (-0.0000) is (0.0000) followed (-0.0002) by (0.0000) a (0.0000) deeper, (-0.0000) slower (0.0000) expression (0.0001) phase. (-0.0001) pump (0.0001) weighs (-0.0001) less (-0.0001) than (0.0000) 1 (0.0001) lb. (0.0000) ( (-0.0001) about (-0.0000) 10 (-0.0000) 1 (-0.0001) / (-0.0000) 2 (-0.0001) oz. (0.0000) ) (-0.0000) and (-0.0000) is (-0.0002) just (-0.0003) 5 (0.0004) " (0.0005) in (-0.0003) diameter (-0.0001) swing (0.0001) accessories (0.0003) include (0.0002) : (-0.0002) 24 (0.0000) mm (-0.0000) personalfit (0.0000) & (-0.0000) trade (-0.0001) ; (-0.0001) breastshield, (0.0000) valve, (0.0001) 2 (0.0002) membranes, (0.0002) tubing, (-0.0000) and (-0.0000) optional- (-0.0001) use (0.0001) neck (-0.0001) / (-0.0001) shoulder (-0.0001) strap (0.0000) includes (0.0003) these (-0.0002) breastmilk (-0.0001) storage (0.0003) supplies (0.0001) : (-0.0005) 1- (0.0000) motor (-0.0002) unit (-0.0001) 1- (-0.0000) personalfit (0.0000) 24 (0.0001) mm (-0.0001) ( (-0.0000) medium (-0.0000) ) (-0.0001) breastshield (0.0000) 1- (0.0000) breastshield (-0.0001) connector (-0.0000) ( (-0.0002) pump (0.0003) body (0.0000) ) (-0.0001) 1- (0.0001) valve (0.0002) 2- (-0.0000) membranes (-0.0007) 1- (-0.0001) tubing (0.0001) 2- (-0.0003) 5 (-0.0002) oz (-0.0001) ( (-0.0003) 150 (-0.0002) ml (-0.0001) ) (0.0001) breastmilk (0.0001) bottles (0.0000) 2- (-0.0001) bottle (0.0001) lids (0.0001) 1- (0.0000) bottle (0.0001) stand (0.0000) 1- (0.0000) shoulder (0.0001) / (-0.0001) neck (0.0000) strap (-0.0002) 1- (0.0001) ac (-0.0000) adapter (-0.0000) 1- (0.0000) drawstring (0.0000) bag (-0.0003) 1- (0.0001) breastfeeding (0.0000) information (-0.0000) guide (-0.0002) 1- (-0.0001) instructions (0.0001) for (-0.0001) use (0.0001)
~~~~~~

**Node-1.9** (global 984):

~~~~~~text
product (-0.0007) from (0.0001) amazon (0.0002) platform (-0.0002) with (0.0002) title (0.0000) and (0.0004) content (-0.0001) : (0.0006) title (0.0003) : (0.0007) power (-0.0000) probiotic (0.0002) ent (0.0001) kids- (-0.0002) strawberry (0.0003) blast (0.0002) 30 (-0.0003) chewable (-0.0001) tablets (0.0004) | (-0.0002) supports (-0.0003) the (-0.0003) natural (0.0003) immune (0.0003) defenses (0.0001) of (0.0001) the (-0.0003) ears, (0.0002) nose (0.0002) / (-0.0000) nasopharynx, (0.0001) and (0.0002) throat (0.0002) | (-0.0005) promotes (-0.0000) oral (0.0004) health (0.0001) and (0.0003) fresh (-0.0001) breath (0.0001) | (0.0000) individually (-0.0001) sealed (-0.0000) in (0.0001) nitrogen- (-0.0002) purged (0.0001) aluminum (0.0002) blister (0.0001) packs (0.0003) to (-0.0000) insure (0.0002) freshness. (0.0002) content (0.0000) : (0.0002) power (0.0002) probiotic (0.0002) ent (0.0001) ( (-0.0001) strawberry (0.0003) blast (0.0002) ) (-0.0007) are (0.0005) chewable, (-0.0001) strawberry- (0.0003) flavored (-0.0001) probiotic (0.0001) formulas (0.0003) that (0.0001) activate (-0.0001) in (0.0000) the (-0.0004) oral (0.0002) cavity (-0.0002) for (0.0000) support (-0.0000) of (0.0001) ear, (-0.0002) nose, (-0.0001) and (-0.0003) throat (0.0003) health (0.0002) and (-0.0003) to (-0.0001) naturally (0.0001) promote (-0.0002) fresh (0.0003) breath. (-0.0003) as (0.0004) you (-0.0005) chew, (-0.0005) each (-0.0004) tablet (-0.0001) releases (0.0003) the (-0.0001) dsm (-0.0000) 13084 (0.0003) strain (0.0006) of (-0.0008) streptococcus (0.0000) salivarius, (0.0004) a (-0.0002) beneficial (-0.0002) bacterium (0.0002) that (-0.0001) normally (-0.0001) occurs (0.0000) in (0.0002) a (-0.0001) healthy (0.0002) oral (0.0002) cavity. (-0.0001) s (0.0001) salivarius (-0.0003) adheres (0.0002) to (0.0000) cells (-0.0001) in (0.0001) the (0.0001) cavity (-0.0001) and (0.0004) positively (0.0003) affects (-0.0001) the (-0.0001) bacterial (-0.0000) population (-0.0001) and (0.0001) natural (0.0000) immune (0.0002) defenses (-0.0001) therein. (0.0004) once (0.0003) established, (0.0003) s (0.0010) salivarius (0.0002) dsm (-0.0003) 13084 (0.0004) also (0.0007) naturally (-0.0002) counteracts (-0.0005) the (0.0002) production (0.0000) of (0.0002) volatile (-0.0004) sulfur (-0.0000) compounds (0.0003) that (0.0001) can (0.0001) cause (0.0001) bad (0.0002) breath. (-0.0002)
~~~~~~

**Node-1.10** (global 8434):

~~~~~~text
product (0.0015) from (0.0009) amazon (-0.0009) platform (0.0003) with (0.0007) title (0.0002) and (-0.0002) content (0.0003) : (0.0002) title (-0.0000) : (-0.0000) biogaia (0.0006) probiotic (-0.0003) chewable (0.0005) tablets (0.0001) 60 (-0.0007) tabs. (-0.0003) content (0.0003) : (0.0003) biogaia (0.0003) probiotics (-0.0000) are (-0.0006) clinically (-0.0001) proven, (-0.0001) health (-0.0002) fortifying, (-0.0000) natural (0.0000) active (0.0000) cultures. (-0.0015) the (-0.0004) word (0.0001) probiotic (-0.0002) means (0.0000) " (-0.0001) for (-0.0001) life. (-0.0001) " (0.0006) there (0.0001) is (-0.0002) a (0.0001) constant (0.0001) battle (-0.0000) going (-0.0002) on (0.0003) in (0.0006) your (0.0004) gut (0.0007) between (0.0000) good (-0.0001) and (0.0001) bad (-0.0001) bacteria. (0.0005) unfortunately, (-0.0002) our (0.0006) modern (-0.0001) lifestyle (-0.0002) favors (-0.0001) the (-0.0003) bad (0.0001) ones (-0.0000) which (-0.0001) may (-0.0003) cause (-0.0001) diseases. (-0.0012) the (0.0002) good (0.0003) bacteria (0.0001) that (-0.0006) are (-0.0002) natural (-0.0005) to (-0.0001) the (0.0004) body (-0.0004) need (-0.0011) reinforcements. (0.0007) biogaia (-0.0001) probiotic (-0.0003) chewable (0.0001) tablets (0.0008) contain (-0.0006) lactobacillus (-0.0001) reuteri (0.0002) protectis, (-0.0006) a (-0.0003) natural (-0.0004) lactobacillus (-0.0003) that (-0.0007) helps (-0.0002) the (-0.0004) good (0.0006) guys (0.0009) restore (-0.0001) a (-0.0002) natural (-0.0002) balance (-0.0002) in (0.0001) your (0.0012) gut. (0.0008) biogaia (-0.0009) ' (0.0007) s (-0.0005) l. (-0.0007) reuteri (-0.0005) is (-0.0010) unique (-0.0006) in (-0.0001) that (-0.0001) it (0.0003) is (-0.0002) an (0.0002) indigenous (-0.0003) probiotic, (0.0002) meaning (-0.0003) l. (-0.0012) reuteri (-0.0008) ' (0.0004) s (-0.0004) natural (0.0004) habitat (-0.0004) is (-0.0002) the (-0.0004) human (-0.0003) body. (-0.0005) scientists (-0.0002) feel (0.0007) that (0.0002) biogaia (-0.0001) ' (0.0009) s (0.0002) l. (-0.0001) reuteri (-0.0009) ' (0.0005) s (-0.0003) indigenous (0.0004) status (0.0002) is (-0.0000) a (-0.0002) major (-0.0003) contributing (0.0001) factor (-0.0003) to (-0.0002) its (-0.0005) health- (-0.0001) enhancing (0.0001) effects (0.0002) and (-0.0000) exceptional (0.0004) safety (0.0008) record. (0.0003) l. (0.0004) reuteri (-0.0008) protectis (-0.0004) has (-0.0003) been (-0.0004) tested (-0.0002) in (0.0000) a (0.0006) number (-0.0000) of (0.0002) clinical (0.0003) studies (-0.0006) and (-0.0000) proven (0.0004) effective (0.0003) as (-0.0001) well (0.0001) as (0.0000) safe (0.0002) for (-0.0000) both (-0.0001) adults (-0.0001) and (-0.0004) children. (-0.0006)
~~~~~~

**Node-2** (global 37121):

~~~~~~text
product (0.0034) from (0.0005) amazon (0.0022) platform (0.0013) with (0.0012) title (0.0067) and (0.0036) content (0.0023) : (0.0125) title (0.0046) : (0.0031) kidco (0.0012) f710 (0.0007) baby (0.0005) food (0.0090) mill. (0.0136) content (-0.0034) : (0.0017) give (0.0071) your (0.0057) baby (0.0022) all (0.0021) the (0.0096) advantages (0.0019) of (0.0004) wholesome, (0.0039) home- (0.0039) cooked (0.0005) meats, (0.0023) fresh (0.0018) fruits (0.0046) and (0.0042) vegetables. (0.0011) this (0.0044) lightweight, (-0.0005) travel- (0.0034) anywhere (0.0021) food (0.0047) grinder (0.0060) makes (0.0081) it (0.0044) easy! (0.0022) medical- (0.0038) grade, (0.0037) stainless- (-0.0004) steel (0.0015) components (0.0035) and (0.0027) precision- (0.0018) sharpened (0.0019) blade (0.0029) lets (0.0065) you (0.0004) quickly (0.0064) hand- (0.0024) grind (-0.0014) fruits (0.0030) and (0.0023) vegetables (0.0034) into (0.0030) a (-0.0004) smooth (0.0020) puree (0.0012) for (0.0020) easy (0.0034) digestion. (0.0013) food (-0.0019) strains (0.0008) automatically (-0.0008) into (0.0028) a (-0.0037) 4 (-0.0004) oz. (0.0075) feeding (0.0011) dish. (0.0102) this (0.0009) item (0.0026) does (0.0008) not (0.0011) come (0.0042) with (0.0071) a (-0.0004) carrying (-0.0056) case. (0.0077) dishwasher (-0.0043) safe. (0.0154)
~~~~~~

**Node-3** (global 37122):

~~~~~~text
product (0.0057) from (0.0080) amazon (0.0119) platform (-0.0052) with (0.0120) title (0.0108) and (0.0084) content (0.0061) : (0.0278) title (0.0186) : (0.0103) zo- (0.0116) li (-0.0013) two (0.0150) baby (0.0066) wide (0.0209) neck (0.0112) baby (-0.0156) bottles (-0.0065) ( (0.0248) 10 (0.0124) oz (0.0106) ). (-0.0004) content (0.0151) : (0.0149) zoli (0.0032) bottles (-0.0071) are (0.0101) made (0.0056) from (0.0045) polyethersulfone (0.0043) ( (0.0135) pes (0.0080) ) (0.0055) plastic (0.0072) which (0.0073) is (0.0080) free (0.0084) of (0.0051) harmful (-0.0009) chemicals (0.0074) such (0.0088) as (0.0055) bisphenol- (0.0068) a. (-0.0060) these (0.0181) bottles (0.0078) feature (0.0136) an (0.0092) integrated (0.0154) valve (0.0127) on (0.0074) the (0.0058) nipple (0.0065) that (0.0137) reduces (0.0145) air (0.0106) intake (0.0159) and (0.0122) nipple (0.0032) collapse. (-0.0038) the (0.0098) unique (0.0197) valve (0.0116) works (0.0090) the (-0.0008) same (0.0094) as (0.0081) other (0.0158) anti- (0.0137) colic (0.0086) bottles (0.0158) without (0.0074) the (-0.0046) extra (0.0104) parts (0.0149) to (0.0090) wash (0.0153) and (0.0145) assemble. (0.0023)
~~~~~~

**Node-4** (global 37123):

~~~~~~text
product (-0.0010) from (-0.0008) amazon (0.0028) platform (0.0037) with (-0.0023) title (0.0018) and (0.0026) content (-0.0016) : (0.0014) title (0.0051) : (0.0008) beaba (0.0018) bib (0.0020) expresso (0.0030) 3 (0.0034) in (0.0013) 1 (0.0014) baby (-0.0000) bottle (0.0037) & (0.0038) amp (0.0009) ; (0.0046) food (-0.0004) warmer. (0.0023) content (0.0006) : (0.0022) this (-0.0043) ingeneous (-0.0006) little (0.0022) machine (0.0001) does (0.0001) it (-0.0003) all! (0.0035) prepare (-0.0014) formula (0.0031) bottles (0.0029) in (0.0010) 60 (0.0048) seconds (-0.0020) with (0.0010) one (0.0020) hand, (0.0013) warm (-0.0022) pre- (0.0003) mixed (-0.0022) or (-0.0008) breast (0.0026) milk (-0.0036) bottles, (-0.0015) warm (-0.0010) food (-0.0016) jars, (0.0008) make (-0.0010) hot (-0.0001) water (-0.0020) for (-0.0001) tea (0.0003) / (0.0048) coffee, (-0.0009) sanitize (0.0009) bottles, (0.0011) store (-0.0001) bottles, (-0.0001) and (0.0005) it (0.0022) ' (-0.0023) s (-0.0009) self (0.0010) cleaning! (0.0018) did (-0.0024) we (0.0031) mention (0.0011) that (0.0001) it (0.0021) ' (-0.0016) s (0.0011) bpa- (-0.0000) free? (0.0019) how (-0.0042) easy (-0.0023) is (0.0026) it? (0.0003) fill (-0.0003) the (0.0006) bottle (-0.0004) with (0.0023) as (0.0008) much (0.0004) water (-0.0020) as (0.0029) you (0.0003) need (-0.0003) ( (0.0004) 2, (0.0010) 4, (0.0024) etc (-0.0004) ozs (0.0016) ), (0.0047) pour (0.0009) the (0.0034) water (0.0011) into (0.0017) the (0.0020) machine, (0.0012) press (0.0021) the (0.0010) heat (0.0004) button (0.0021) and (0.0003) while (0.0026) you (-0.0000) wait (0.0010) you (0.0025) can (0.0002) scoop (0.0000) the (0.0021) amount (0.0040) of (0.0018) formula (-0.0098) needed (0.0017) into (-0.0000) the (0.0029) bottle. (0.0005) once (0.0007) the (0.0004) machine (-0.0029) beeps (-0.0011) you (0.0022) simply (0.0005) press (-0.0021) the (0.0025) orange (0.0001) button (-0.0011) and (0.0013) it (0.0021) dispenses (0.0006) the (0.0033) perfect (0.0007) temp (0.0003) water (-0.0006) into (0.0001) the (0.0011) bottle, (0.0017) put (0.0007) the (0.0014) lid (-0.0006) on (0.0012) and (0.0024) shake. (0.0005) much (-0.0009) faster (0.0002) and (0.0026) safer (-0.0014) than (-0.0010) boiling (-0.0007) water (0.0005) or (0.0034) using (0.0019) a (0.0016) kettle. (0.0012) how (-0.0011) do (-0.0000) i (0.0058) warm (0.0030) other (-0.0006) things? (0.0028) you (0.0014) can (0.0012) warm (0.0013) your (0.0022) jars (0.0020) of (0.0022) baby (0.0020) food (0.0057) up (0.0004) in (0.0005) the (0.0005) bib (0.0021) ' (-0.0000) expresso (0.0030) as (0.0004) well (0.0009) with (-0.0018) the (-0.0021) bain- (0.0041) marie (0.0006) mode. (0.0027) you (0.0000) simply (0.0002) fill (-0.0012) the (0.0008) water (-0.0055) reservoir (0.0006) to (0.0002) the (0.0021) max (-0.0016) line (0.0000) indicated, (0.0004) place (0.0013) the (0.0011) jar (-0.0002) of (-0.0010) food (-0.0023) into (-0.0009) the (0.0005) reservoir (-0.0055) and (0.0003) then (0.0015) you (-0.0012) choose (-0.0015) one (0.0014) of (-0.0007) the (-0.0000) two (0.0013) warm (0.0010) buttons. (0.0014) this (-0.0055) also (0.0054) works (0.0017) for (0.0005) pre- (-0.0012) mixed (0.0016) bottles (-0.0080) and (-0.0007) breast (-0.0000) milk. (0.0055)
~~~~~~

**Node-5** (global 37124):

~~~~~~text
product (-0.0015) from (-0.0011) amazon (0.0024) platform (0.0032) with (-0.0007) title (0.0004) and (0.0004) content (0.0010) : (0.0016) title (0.0015) : (-0.0003) braun (0.0038) thermoscan (0.0004) ear (0.0004) thermometer- (0.0001) irt4520. (0.0010) content (0.0022) : (-0.0006) the (0.0007) most (0.0024) accurate (-0.0005) ear (-0.0009) thermometer (0.0002) from (0.0016) braun (0.0000) due (-0.0004) to (-0.0003) unique (0.0035) pre- (0.0012) warmed (0.0027) tipsmarter- (0.0006) guidance (-0.0015) system (0.0007) confirms (0.0010) secure (0.0010) position (0.0008) and (0.0004) accurate (0.0004) resultmemory (0.0014) function (0.0026) ( (0.0012) 8x (-0.0001) ) (-0.0000) measurement (0.0002) in (0.0012) just (0.0009) secondseasy (0.0005) lens (-0.0021) filter (-0.0013) removal2 (0.0019) year (0.0011) guaranteethermoscan (0.0002) 5 (0.0014) ear (0.0001) thermometerfor (-0.0002) infants, (-0.0011) children (0.0005) and (-0.0015) adultswhy (0.0017) measuring (0.0023) in (-0.0003) the (-0.0012) ear? (-0.0001) the (0.0001) ear (-0.0002) is (0.0032) an (0.0009) excellent (0.0007) site (0.0020) to (-0.0000) measure (0.0025) temperature. (-0.0047) braun (0.0023) thermoscan (0.0002) measures (0.0016) the (-0.0003) infrared (0.0001) heat (0.0011) generated (0.0014) by (0.0005) the (-0.0002) eardrum (0.0002) and (0.0003) the (-0.0004) surrounding (0.0019) tissues. (0.0027) the (0.0026) eardrum (0.0006) shares (0.0012) blood (0.0002) supply (0.0012) with (0.0004) the (0.0006) temperature (0.0014) control (0.0001) center (0.0008) in (0.0010) the (0.0008) brain. (-0.0003) therefore (0.0001) temperature (0.0017) changes (0.0017) are (0.0009) reflected (0.0009) more (0.0011) quickly (0.0005) and (0.0008) accurately (0.0008) than (0.0004) at (0.0011) other (0.0006) sites. (0.0012) unlike (0.0005) other (0.0009) ear (-0.0030) thermometers, (0.0006) braun (-0.0015) thermoscan (0.0004) features (0.0011) a (0.0015) pre- (0.0015) warmed (-0.0041) tip (0.0029) that (0.0011) minimizes (0.0016) the (0.0004) cooling (0.0010) effect (0.0004) that (0.0004) could (-0.0003) result (0.0008) from (0.0006) the (0.0018) introduction (0.0019) of (0.0004) a (0.0015) cool (0.0016) probe (0.0028) tip. (0.0027) the (0.0015) pre- (0.0015) warmed (0.0008) tip (0.0015) helps (0.0015) ensure (0.0023) accuracy (0.0023) measurement (0.0009) after (-0.0032) measurement. (0.0020) the (0.0007) # (0.0006) 1 (0.0004) brand (-0.0027) most (-0.0018) used (0.0014) by (0.0013) doctors (-0.0006) * (0.0051) * (0.0034) based (0.0002) on (0.0006) survey (0.0033) of (0.0004) pediatricians (-0.0010) and (0.0011) general (-0.0000) practitioners (0.0018) in (0.0007) uk, (0.0030) france, (0.0013) germany. (-0.0000) gfk (0.0004) custom (0.0014) research (0.0029) france. (0.0014) 2009proven (0.0010) more (0.0033) accurate (0.0009) than (0.0014) rectal (0.0026) or (0.0039) temple (-0.0013) * (0.0026) * (0.0062) * (0.0065) * (0.0041) nimah (0.0022) mm, (0.0017) bshesh (0.0007) k, (0.0019) callahan (0.0039) jd, (0.0017) jacobs (0.0029) br. (0.0013) infrared (-0.0018) tympanic (0.0010) thermometry (0.0008) in (-0.0009) comparison (0.0011) with (-0.0011) other (-0.0017) temperature (0.0017) measurement (0.0011) techniques (0.0028) in (0.0009) febrile (0.0010) children. (-0.0001) pediatr (0.0018) crit (0.0022) care (0.0024) med. (0.0010) 2006 (-0.0010) ; (0.0013) 7 (-0.0027) ( (0.0054) 1 (-0.0017) ) (-0.0018) : (0.0025) 48- (0.0009) 55. (0.0019) includes1x (0.0017) braun (-0.0019) thermoscan (0.0020) ear (-0.0032) thermometer1x (-0.0009) protective (0.0009) case (-0.0013) with (0.0000) lens (0.0041) filter (0.0008) storage21x (0.0021) lens (0.0040) filters2 (0.0010) x (0.0034) aa (0.0035) duracell (0.0009) batteries (0.0011) total (0.0013) weight (-0.0011) for (-0.0016) the (0.0017) two (0.0018) is (0.0028) 46 (0.0018) grams (-0.0049) ( (0.0022) 23g (-0.0007) each (0.0026) ) (0.0034) designed (0.0085) in (-0.0011) germany (0.0037)
~~~~~~

**Node-6** (global 37125):

~~~~~~text
product (0.0134) from (0.0124) amazon (-0.0286) platform (-0.0268) with (0.0005) title (0.0350) and (-0.0073) content (-0.0402) : (0.0340) title (0.0234) : (0.0139) born (0.0402) free (-0.0143) silicone (0.0009) teether. (0.0137) content (-0.0218) : (0.0273) born (0.0482) free (-0.0225) ' (0.0364) s (0.0132) calm (0.0371) & (0.0149) # (0.0095) x2018 (0.0110) ; (-0.0032) n (0.0071) soothe (0.0256) teether (0.0171) soothes (0.0095) and (0.0129) stimulates (0.0059) sore (0.0052) gums. (0.0039)
~~~~~~
