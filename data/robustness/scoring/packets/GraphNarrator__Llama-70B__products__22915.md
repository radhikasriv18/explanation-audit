# Reference packet: GraphNarrator__Llama-70B__products__22915

- Method: GraphNarrator; configuration: Llama-70B; dataset: products; target node: 22915
- Explanation source: `./robustness_2026-10-30/llama70b/graphnarrator/products/22915.json` (response)
- Scored scope (what the claims were extracted from): ### Free-Text Explanation section
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

Claims were extracted from the `### Free-Text Explanation` section only; the full assistant message is shown here.

~~~~~~text
### Reasoning

0. Graph Structure Reconstruction:

In the provided verbalized graph, the ROOT node (first line) is the target for classification.
Single-digit indexed nodes are direct neighbors of ROOT.
Double-digit indexed nodes are:
  - Two hops away from ROOT
  - Direct children of their parent node

Thus, the graph structure of this verbalized graph is:

- ROOT (organic wheat grass powder)
  - Node-1 (pain relief roll-on)
    - Node-1.1 (soap saver)
    - Node-1.2 (probiotics for kids)
    - Node-1.3 (goat milk soap)
    - Node-1.4 (stretch marks therapy)
    - Node-1.5 (body shaper)

1. Word-Level Evaluation:

Keywords with high saliency scores in ROOT — "organic" (0.01), "wheat" (-0.02), "grass" (-0.02), "powder" (0.03), "amazing" (0.05), "excellent" (0.04), "concentrated" (0.00), "food" (0.02), "source" (-0.01), "beta-carotene" (0.03), "calcium" (0.01), "chlorophyll" (0.01), "fiber" (0.02), "iron" (0.02), "vitamin" (-0.04) — are strongly associated with health supplements and organic products. These directly indicate the product belongs to the "Beauty" or "Health" category. More generic terms like "product" (0.02) and "amazon" (0.12) carry negligible saliency and contribute little.

2. Graph-Level Aggregation:

Node-1 (pain relief roll-on, keywords: "pain" (-0.02), "relief" (0.04), "roll-on" (0.00)) is a direct neighbor with moderate saliency, identifying a health-related product whose close proximity to ROOT reinforces the classification. Indirect neighbors — Node-1.1 (soap saver), Node-1.2 (probiotics for kids), Node-1.3 (goat milk soap), Node-1.4 (stretch marks therapy), Node-1.5 (body shaper) — are all personal care or beauty products, collectively confirming a beauty or health context across both hops.

### Free-Text Explanation
```markdown
The classification of ROOT into "Beauty" is supported by its own keywords and the co-purchase neighborhood.

ROOT: Keywords like "organic" (0.01), "amazing" (0.05), and "excellent" (0.04) clearly identify this as a high-quality organic product — quintessentially a beauty or health supplement.
  - Node-1: A pain relief roll-on (keywords: "pain" (-0.02), "relief" (0.04)) is a direct health-related product, reinforcing the Beauty or Health context.
    - Node-1.1: A soap saver is a bathroom accessory, supporting the personal care category.
    - Node-1.2: Probiotics for kids are a health supplement, further confirming the health context.
    - Node-1.3: Goat milk soap is a natural beauty product, affirming the Beauty category.
    - Node-1.4: Stretch marks therapy is a beauty treatment, providing robust evidence for the Beauty classification.
    - Node-1.5: A body shaper is a beauty or fitness product, collectively affirming the Beauty category.

In summary, ROOT's own high-saliency keywords strongly signal a health or beauty product, and the entire co-purchase neighborhood consists of personal care or beauty products, providing robust evidence for the "Beauty" category.
```
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/78.json`).

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
<verbalized-graph>ROOT: product(0.02) amazon(0.12) platform(0.07) title(0.05) content(0.03) title(0.06) amazing(0.05) grass(-0.02) organic(0.01) wheat(-0.02) grass(-0.02) powder,(0.03) 60(0.01) servings,(0.01) 17-(-0.00) ounce(0.02) container.(0.05) content(0.06) amazing(0.03) grass(-0.01) wheat(-0.01) grass(0.02) powder(0.01) excellent(0.04) concentrated(0.00) food(0.02) source(-0.01) beta-(0.03) carotene,(0.02) calcium,(0.01) chlorophyll,(0.01) fiber,(0.02) iron(0.02) vitamin(-0.04) k.(0.02) also(-0.01) good(-0.00) source(-0.01) protein,(0.03) vitamin(-0.05) c,(0.03) vitamin(-0.03) b-(0.02) 12,(0.00) folic(0.01) acid,(0.01) vitamin(-0.01) b-(0.03) 6,(-0.01) trace(-0.01) minerals(0.00) contains(0.02) essential(0.02) amino(0.04) acids.(-0.02) mix(0.02) tablespoon(0.00) green(0.01) superfood(0.01) juice,(-0.01) milk,(0.01) smoothie(0.03) favorite(0.01) beverage.(-0.02) natural(0.05) organic(0.01) ingredients.(0.02) 
Node-1: product(-0.02) amazon(0.15) platform(0.00) title(0.08) content(0.04) title(0.06) stopain(0.05) extra(-0.02) strength(0.03) pain(-0.02) relief(0.04) roll-(0.00) on,(0.01) 3(-0.00) ounce.(-0.00) content(0.07) penetrates(-0.03) deep(0.03) provide(-0.01) proven(0.01) pain-(0.02) relieving(0.01) benefits(0.01) menthol(0.00) non-(0.01) greasy,(0.01) non-(0.02) staining(0.00) formula.(-0.00) roll-(0.03) formula(0.03) also(0.02) contains(0.02) glucosamine(0.02) msm.(0.01) light,(0.03) pleasant(0.04) scent,(0.06) stopain(0.03) provides(0.04) extra(-0.03) strength(0.01) pain(-0.02) relief(0.03) featuring(0.07) easy-(0.01) to-(0.01) use,(0.03) hands(-0.00) free(0.01) applicator.(0.03) temporary(0.00) relief(-0.00) minor(0.04) aches(0.02) pains(0.01) muscles(0.07) joints(0.04) associated(0.03) with,(0.02) simple(0.03) backache,(0.02) arthritis,(0.02) strains,(0.04) bruises(0.05) sprains.(0.04) 
Node-1.1: product(-0.01) amazon(-0.01) platform(0.00) title(0.01) content(0.01) title(0.02) idea(0.01) works(0.01) waterfall(0.01) soap(0.01) saver.(0.00) content(-0.00) handy(0.03) slanted(0.00) soap(0.01) dish(0.01) drains(0.00) excess(0.00) water(0.00) away(0.00) soap(0.01) sink(0.01) shower,(0.01) keeping(0.01) soap(0.01) dry(0.00) making(0.00) last(0.00) longer.(0.00) built(0.01) plastic(0.01) prongs(0.01) hold(0.00) soap(0.01) place.(0.00) 
Node-1.2: product(0.00) amazon(-0.00) platform(-0.00) title(0.00) content(0.00) title(0.00) amerifit(0.00) culturelle(0.00) probiotics(0.00) kids,(0.00) 30(0.00) count.(0.00) content(0.00) developed(-0.00) science,(0.00) trusted(0.00) momsthe(0.00) ingredient(0.00) culturelle(-0.00) kids(0.00) probiotics(-0.00) clinically(0.00) proven(0.00) help(0.00) reduce(-0.00) occasional(-0.00) tummy(0.00) troubles(0.00) like(0.00) gas,(0.00) bloating,(0.00) diarrhea(-0.00) helping(-0.00) restore(-0.00) balance(0.00) good(0.00) not-(0.00) so-(0.00) good(0.00) bacteria(-0.00) digestive(0.00) systems.(0.00) taken(-0.00) regularly,(0.00) actually(-0.00) helps(-0.00) child(0.00) rsquo(0.00) digestive(0.00) immune(-0.00) systems(0.00) work(0.00) better.(0.01) happy(-0.00) tummies,(0.00) healthy(0.00) kids,(0.00) relaxed(0.00) parents.(0.01) support(-0.00) kids(-0.00) rsquo(0.00) natural(-0.00) defenses(0.00) keep(0.00) digestive(0.00) system(0.00) happy(0.00) culturelle(0.00) probiotics.(0.00) benefits(-0.01) culturelle(-0.00) kids(-0.00) packets(-0.00) lactobacillus(0.00) ggcontains(0.00) 100(0.00) naturally(0.00) sourced(0.00) lactobacillus(0.00) gg(0.00) ndash(0.00) 1(0.00) clinically(0.00) studied(0.00) probiotic.(0.01) dagger(0.00) dagger(-0.01) helps(0.00) support(-0.00) kids(0.00) rsquo(0.00) natural(0.00) defense(0.00) systems(0.00) helps(0.00) reduce(0.00) occasional(0.00) digestive(0.00) upset(0.00) easy(0.00) take(0.00) especially(-0.00) little(0.00) ones(0.00) flavorless,(0.00) add(0.00) cool(0.00) liquid(0.00) fooddairy(0.00) gluten(-0.00) free(0.00) 
Node-1.3: product(0.01) amazon(-0.01) platform(0.01) title(0.00) content(0.01) title(0.00) goat(0.00) milk(0.00) soap-(0.00) original(0.00) 3(0.00) pack(0.00) canus(0.00) vermont(-0.00) 3(0.00) bar(0.00) soap.(0.00) content(0.00) combine(0.00) natural(0.00) soap(0.00) base(-0.00) fresh(0.00) goat(0.00) milk(0.00) original(0.00) fragrance(0.01) essential(0.00) oils(0.00) leave(0.00) skin(0.00) feeling(-0.00) soft(0.00) rejuvenated.(0.00) value(0.00) 3(-0.00) pack(0.01) bars(0.00) 
Node-1.4: product(0.00) amazon(0.00) platform(0.00) title(0.00) content(0.01) title(0.00) mederma(0.00) stretch(0.00) marks(0.00) therapy,(0.00) 5.(0.00) 29(-0.00) oz(-0.00) box.(0.00) content(0.00) mederma(0.00) stretch(0.00) marks(0.00) therapy(0.00) 5.(0.00) 29(0.00) oz.(-0.00) combines(-0.00) botanical(0.00) ingredients(0.00) premium(0.00) skin(0.00) hydrator(0.00) nourishing(0.00) formula(-0.00) clinically(0.00) shown(-0.00) improve(0.00) appearance(-0.00) stretch(0.00) marks.(0.00) noticeable(0.00) improvement(0.00) 4(0.00) weeks.(-0.00) paraben(-0.00) free,(0.00) dermatologist(0.00) tested.(-0.00) reduces(0.01) discoloration,(0.00) improves(0.00) texture(0.00) enhances(-0.00) softness(0.02) 
Node-1.5: product(0.00) amazon(-0.01) platform(0.00) title(0.01) content(0.00) title(0.01) mama(0.00) mio(-0.00) get(0.01) waisted(0.00) body(0.00) shaper,(0.01) 3.(-0.00) 4(0.00) ounce.(-0.00) content(0.01) holy(-0.00) grail(0.00) slimming(0.01) potions(0.00) packed(0.00) nine(0.01) well(0.00) proven(-0.00) ingredients(0.00) designed(0.01) help(0.00) combat(0.00) fat(0.00) deposits,(0.00) tighten(-0.00) tum,(0.00) reduce(0.00) puffiness,(0.00) x2013(0.00) importantly(0.00) x2013(0.00) maximise(0.01) lipolysis.(0.01) lipolysis(0.01) way(0.00) body(0.00) breaks(0.01) fat(0.00) stored(0.01) fat(0.00) cells(0.01) giving(0.00) slim(0.01) fat(0.01) cells(0.01) slimmer(0.01) silhouette.(0.01) get(-0.00) waisted(-0.01) x2019(0.01) ingredients(-0.00) well(0.01) proven(0.01) lab(0.02) tests(0.01) dramatically(0.00) increase(0.00) destruction(0.00) fat(0.01) 
</verbalized-graph>

### Classification Label
Beauty

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 22915
- Title: Amazing Grass Organic Wheat Grass Powder, 60 Servings, 17-Ounce Container
- True class (canonical `y`): **Health & Personal Care**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Health & Personal Care**
- Prediction recorded by this method's pipeline: **Beauty**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Amazing Grass Organic Wheat Grass Powder, 60 Servings, 17-Ounce Container. Content: Amazing Grass wheat grass powder is an excellent concentrated food source of beta-carotene, calcium, chlorophyll, fiber, iron and vitamin K. It is also a very good source of protein, vitamin C, vitamin B-12, folic acid, vitamin B-6, trace minerals and contains all essential amino acids. Mix a tablespoon of Green SuperFood with juice, milk, a smoothie or your favorite beverage. All natural and organic ingredients.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 4305 | Health & Personal Care | Stopain Extra Strength Pain Relief Roll-On, 3 Ounce |

### 2-hop (shortest distance exactly 2): 5 nodes

| node id | true class | title |
|---|---|---|
| 475 | Home & Kitchen | Idea Works Waterfall Soap Saver |
| 8389 | Health & Personal Care | Amerifit Culturelle Probiotics for Kids, 30 Count |
| 22916 | Beauty | Goat Milk Soap - Original (3 Pack) Canus Vermont 3 Bar Soap |
| 22917 | Beauty | Mederma Stretch Marks Therapy, 5.29 Oz Box |
| 22918 | Beauty | Mama Mio Get Waisted Body Shaper, 3.4 Ounce |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/78.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Beauty**, ground truth = **Health & Personal Care**.
The verbalized graph is 5895 characters; the model saw the first 6000 (the whole graph).
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 22915 | 92 | 0.1173 | yes |
| Node-1 | 1 | 4305 | 91 | 0.1502 | yes |
| Node-1.1 | 2 | 475 | 52 | 0.0255 | yes |
| Node-1.2 | 3 | 8389 | 174 | 0.0066 | yes |
| Node-1.3 | 4 | 22916 | 59 | 0.0110 | yes |
| Node-1.4 | 5 | 22917 | 68 | 0.0212 | yes |
| Node-1.5 | 6 | 22918 | 106 | 0.0184 | yes |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, ROOT->Node-1

### Tokens and scores

**ROOT** (global 22915):

~~~~~~text
product (0.0158) from (-0.0494) amazon (0.1173) platform (0.0684) with (-0.0023) title (0.0544) and (0.0130) content (0.0262) : (0.0214) title (0.0626) : (0.0169) amazing (0.0468) grass (-0.0232) organic (0.0084) wheat (-0.0179) grass (-0.0178) powder, (0.0307) 60 (0.0122) servings, (0.0128) 17- (-0.0034) ounce (0.0227) container. (0.0496) content (0.0585) : (0.0446) amazing (0.0272) grass (-0.0064) wheat (-0.0073) grass (0.0198) powder (0.0089) is (0.0210) an (0.0037) excellent (0.0396) concentrated (0.0021) food (0.0163) source (-0.0119) of (0.0029) beta- (0.0270) carotene, (0.0184) calcium, (0.0115) chlorophyll, (0.0143) fiber, (0.0213) iron (0.0176) and (0.0463) vitamin (-0.0366) k. (0.0165) it (0.0128) is (0.0231) also (-0.0083) a (-0.0115) very (0.0289) good (-0.0003) source (-0.0076) of (0.0356) protein, (0.0280) vitamin (-0.0475) c, (0.0270) vitamin (-0.0335) b- (0.0215) 12, (0.0014) folic (0.0117) acid, (0.0080) vitamin (-0.0147) b- (0.0282) 6, (-0.0062) trace (-0.0051) minerals (0.0000) and (0.0220) contains (0.0169) all (-0.0046) essential (0.0163) amino (0.0408) acids. (-0.0238) mix (0.0248) a (-0.0018) tablespoon (0.0009) of (0.0152) green (0.0052) superfood (0.0072) with (0.0487) juice, (-0.0097) milk, (0.0094) a (-0.0382) smoothie (0.0262) or (-0.0471) your (0.0273) favorite (0.0072) beverage. (-0.0245) all (0.0353) natural (0.0546) and (-0.0035) organic (0.0122) ingredients. (0.0186)
~~~~~~

**Node-1** (global 4305):

~~~~~~text
product (-0.0215) from (-0.0095) amazon (0.1502) platform (0.0046) with (-0.0361) title (0.0819) and (0.0022) content (0.0415) : (0.0236) title (0.0640) : (-0.0097) stopain (0.0476) extra (-0.0206) strength (0.0309) pain (-0.0197) relief (0.0424) roll- (0.0018) on, (0.0069) 3 (-0.0038) ounce. (-0.0011) content (0.0681) : (-0.0070) it (0.0376) penetrates (-0.0301) deep (0.0332) to (0.0052) provide (-0.0110) the (-0.0013) proven (0.0103) pain- (0.0167) relieving (0.0097) benefits (0.0052) of (0.0167) menthol (0.0004) in (0.0302) a (0.0232) non- (0.0101) greasy, (0.0128) non- (0.0223) staining (0.0030) formula. (-0.0050) the (0.0339) roll- (0.0307) on (0.0272) formula (0.0271) also (0.0152) contains (0.0227) glucosamine (0.0180) and (0.0108) msm. (0.0139) with (0.0250) a (0.0418) light, (0.0261) pleasant (0.0439) scent, (0.0618) stopain (0.0276) provides (0.0414) extra (-0.0345) strength (0.0147) pain (-0.0174) relief (0.0315) featuring (0.0668) an (0.0148) easy- (0.0116) to- (0.0074) use, (0.0335) hands (-0.0032) free (0.0051) applicator. (0.0298) for (0.0439) the (0.0136) temporary (0.0032) relief (-0.0015) of (0.0134) minor (0.0361) aches (0.0242) and (0.0204) pains (0.0060) of (0.0121) muscles (0.0702) and (0.0174) joints (0.0392) associated (0.0331) with, (0.0151) simple (0.0338) backache, (0.0157) arthritis, (0.0170) strains, (0.0418) bruises (0.0450) and (0.0260) sprains. (0.0426)
~~~~~~

**Node-1.1** (global 475):

~~~~~~text
product (-0.0061) from (0.0062) amazon (-0.0078) platform (0.0046) with (0.0006) title (0.0074) and (-0.0045) content (0.0087) : (-0.0054) title (0.0193) : (-0.0025) idea (0.0129) works (0.0090) waterfall (0.0132) soap (0.0087) saver. (0.0024) content (-0.0040) : (0.0009) this (0.0055) handy (0.0255) slanted (0.0043) soap (0.0142) dish (0.0085) drains (0.0024) excess (0.0017) water (0.0014) away (0.0018) from (0.0092) your (0.0093) soap (0.0053) and (-0.0009) into (0.0023) your (0.0048) sink (0.0062) or (0.0071) shower, (0.0056) keeping (0.0061) soap (0.0066) dry (0.0038) and (0.0012) making (0.0028) it (0.0041) last (0.0049) longer. (0.0008) built (0.0059) in (0.0070) plastic (0.0100) prongs (0.0092) hold (0.0003) soap (0.0061) in (-0.0042) place. (0.0022)
~~~~~~

**Node-1.2** (global 8389):

~~~~~~text
product (0.0002) from (-0.0001) amazon (-0.0012) platform (-0.0002) with (-0.0015) title (0.0019) and (0.0002) content (0.0004) : (0.0013) title (0.0003) : (0.0019) amerifit (0.0009) culturelle (0.0008) probiotics (0.0019) for (0.0007) kids, (0.0009) 30 (0.0007) count. (0.0049) content (0.0004) : (0.0024) developed (-0.0003) with (-0.0024) science, (0.0032) trusted (0.0007) by (0.0006) momsthe (0.0006) ingredient (0.0003) in (0.0012) culturelle (-0.0010) kids (0.0005) probiotics (-0.0000) is (0.0006) clinically (0.0010) proven (0.0002) to (-0.0009) help (0.0001) reduce (-0.0003) occasional (-0.0004) tummy (0.0004) troubles (0.0007) like (0.0014) gas, (0.0031) bloating, (0.0010) and (0.0001) diarrhea (-0.0003) by (0.0004) helping (-0.0007) to (-0.0003) restore (-0.0006) the (-0.0036) balance (0.0006) of (0.0008) good (0.0002) and (-0.0000) not- (0.0006) so- (0.0008) good (0.0006) bacteria (-0.0012) in (0.0003) their (0.0009) digestive (0.0001) systems. (0.0046) * (-0.0054) taken (-0.0003) regularly, (0.0001) it (0.0027) actually (-0.0005) helps (-0.0014) your (0.0037) child (0.0001) & (0.0014) rsquo (0.0008) ; (0.0066) s (-0.0006) digestive (0.0001) and (0.0001) immune (-0.0022) systems (0.0018) to (-0.0029) work (0.0006) better. (0.0066) * (-0.0033) happy (-0.0004) tummies, (0.0012) healthy (0.0008) kids, (0.0035) relaxed (0.0018) parents. (0.0061) support (-0.0025) your (0.0047) kids (-0.0032) & (0.0030) rsquo (0.0008) ; (0.0044) natural (-0.0009) defenses (0.0011) and (-0.0001) keep (0.0022) their (0.0032) digestive (0.0008) system (0.0024) happy (0.0004) with (0.0020) culturelle (0.0008) probiotics. (0.0025) benefits (-0.0067) of (-0.0047) culturelle (-0.0023) kids (-0.0017) packets (-0.0025) with (-0.0018) lactobacillus (0.0004) ggcontains (0.0014) 100 (0.0006) % (0.0005) naturally (0.0002) sourced (0.0009) lactobacillus (0.0003) gg (0.0006) & (0.0004) ndash (0.0001) ; (0.0014) the (-0.0053) # (0.0020) 1 (0.0008) most (0.0008) clinically (0.0012) studied (0.0015) probiotic. (0.0057) & (0.0040) dagger (0.0035) ; (0.0031) & (0.0014) dagger (-0.0089) ; (0.0038) helps (0.0017) support (-0.0002) kids (0.0002) & (0.0000) rsquo (0.0004) ; (0.0021) natural (0.0008) defense (0.0006) systems (0.0011) * (0.0032) helps (0.0033) reduce (0.0014) occasional (0.0001) digestive (0.0008) upset (0.0019) * (-0.0015) easy (0.0001) to (0.0009) take (0.0002) ( (0.0004) especially (-0.0007) for (-0.0001) little (0.0010) ones (0.0004) ) (0.0000) flavorless, (0.0011) so (0.0008) you (0.0013) can (0.0002) add (0.0010) to (0.0005) any (0.0002) cool (0.0000) liquid (0.0003) or (0.0015) fooddairy (0.0002) and (0.0004) gluten (-0.0004) free (0.0023)
~~~~~~

**Node-1.3** (global 22916):

~~~~~~text
product (0.0053) from (0.0022) amazon (-0.0065) platform (0.0056) with (0.0068) title (0.0021) and (0.0014) content (0.0110) : (0.0011) title (0.0043) : (0.0012) goat (0.0022) milk (0.0050) soap- (0.0042) original (0.0021) ( (0.0091) 3 (0.0026) pack (0.0024) ) (-0.0003) canus (0.0017) vermont (-0.0017) 3 (0.0042) bar (0.0002) soap. (0.0047) content (0.0039) : (-0.0032) we (0.0030) combine (0.0020) an (-0.0065) all (0.0003) natural (0.0019) soap (0.0009) base (-0.0007) with (0.0009) fresh (0.0043) goat (0.0018) ' (0.0016) s (0.0001) milk (0.0043) and (0.0034) our (0.0023) original (0.0002) fragrance (0.0071) of (0.0001) essential (0.0029) oils (0.0036) which (0.0012) will (0.0020) leave (0.0019) your (-0.0022) skin (0.0015) feeling (-0.0003) soft (0.0029) and (0.0018) rejuvenated. (0.0021) value (0.0021) 3 (-0.0019) pack (0.0050) bars (0.0031)
~~~~~~

**Node-1.4** (global 22917):

~~~~~~text
product (0.0010) from (0.0009) amazon (0.0046) platform (0.0014) with (-0.0001) title (0.0022) and (-0.0011) content (0.0055) : (-0.0014) title (0.0027) : (0.0019) mederma (0.0012) stretch (0.0022) marks (0.0006) therapy, (0.0019) 5. (0.0002) 29 (-0.0017) oz (-0.0018) box. (0.0025) content (0.0018) : (0.0005) mederma (0.0004) stretch (0.0028) marks (0.0007) therapy (0.0030) 5. (0.0005) 29 (0.0008) oz. (-0.0007) combines (-0.0019) botanical (0.0025) ingredients (0.0017) and (-0.0004) a (-0.0016) premium (0.0044) skin (0.0002) hydrator (0.0007) in (0.0001) a (-0.0003) nourishing (0.0010) formula (-0.0001) that (0.0017) is (0.0023) clinically (0.0002) shown (-0.0011) to (0.0015) improve (0.0009) the (-0.0037) appearance (-0.0001) of (0.0015) stretch (0.0024) marks. (0.0023) noticeable (0.0005) improvement (0.0005) in (0.0004) just (0.0009) 4 (0.0032) weeks. (-0.0000) paraben (-0.0022) free, (0.0016) dermatologist (0.0027) tested. (-0.0016) reduces (0.0051) discoloration, (0.0012) improves (0.0017) texture (0.0038) and (0.0045) enhances (-0.0021) softness (0.0212)
~~~~~~

**Node-1.5** (global 22918):

~~~~~~text
product (0.0021) from (0.0031) amazon (-0.0073) platform (0.0012) with (0.0056) title (0.0100) and (0.0076) content (0.0002) : (0.0121) title (0.0108) : (0.0054) mama (0.0043) mio (-0.0042) get (0.0052) waisted (0.0027) body (0.0017) shaper, (0.0052) 3. (-0.0032) 4 (0.0007) ounce. (-0.0015) content (0.0119) : (-0.0081) this (0.0026) is (0.0026) the (-0.0010) holy (-0.0018) grail (0.0025) of (0.0044) slimming (0.0079) potions (0.0048) ; (-0.0008) packed (0.0026) with (0.0100) nine (0.0050) well (0.0044) proven (-0.0014) ingredients (0.0002) designed (0.0082) to (0.0068) help (0.0023) combat (0.0044) fat (0.0018) deposits, (0.0048) tighten (-0.0014) your (0.0079) tum, (0.0042) reduce (0.0041) puffiness, (0.0040) and (0.0104) & (0.0000) # (0.0007) x2013 (0.0029) ; (0.0051) most (0.0077) importantly (0.0030) & (0.0049) # (0.0028) x2013 (0.0033) ; (0.0093) maximise (0.0061) lipolysis. (0.0070) lipolysis (0.0058) is (0.0090) the (-0.0123) way (0.0013) your (0.0005) body (0.0046) breaks (0.0052) down (0.0044) the (-0.0021) fat (0.0025) stored (0.0074) in (-0.0008) fat (0.0048) cells (0.0096) ; (0.0086) giving (0.0042) you (-0.0010) slim (0.0082) fat (0.0080) cells (0.0051) and (0.0071) a (0.0025) slimmer (0.0073) silhouette. (0.0081) get (-0.0040) waisted (-0.0061) & (0.0100) # (0.0004) x2019 (0.0056) ; (0.0039) s (0.0136) ingredients (-0.0015) are (0.0087) well (0.0083) proven (0.0069) in (0.0118) lab (0.0184) tests (0.0136) to (0.0083) dramatically (0.0048) increase (0.0037) the (-0.0088) destruction (0.0023) of (0.0024) fat (0.0091)
~~~~~~
