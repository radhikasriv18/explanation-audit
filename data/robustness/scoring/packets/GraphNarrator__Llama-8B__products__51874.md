# Reference packet: GraphNarrator__Llama-8B__products__51874

- Method: GraphNarrator; configuration: Llama-8B; dataset: products; target node: 51874
- Explanation source: `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/193.json` (messages[assistant])
- Scored scope (what the claims were extracted from): ### Free-Text Explanation section
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

Claims were extracted from the `### Free-Text Explanation` section only; the full assistant message is shown here.

~~~~~~text
### Graph Structure Reconstruction

In the provided verbalized graph, the ROOT node (first line) is the target for classification.
Single-digit indexed nodes are direct neighbors of ROOT.
Double-digit indexed nodes are:
  - Two hops away from ROOT
  - Direct children of their parent node

Thus, the graph structure of this verbalized graph is:

- ROOT (health supplement)
  - Node-1 (health book)
    - Node-1.1 (natural medicine encyclopedia)
    - Node-1.2 (healing foods)
    - Node-1.3 (practical guide to acu-points)
    - Node-1.4 (herbalist way to healing)
    - Node-1.5 (integrative nutrition)

### Word-Level Evaluation

Keywords with high saliency scores in ROOT — "mineral" (0.08), "supplement" (0.02), "ionic" (0.05), "fizz" (0.05), "gram" (0.05) — are strongly associated with health products. These directly indicate the product belongs to "Books" (health-related literature).

### Graph-Level Aggregation

Node-1 (health book, keywords: "healthy" (0.01), "medicine" (0.10), "optimum" (0.04), "health" (0.04), "kind" (0.14)) is a direct neighbor with high saliency, identifying a health-related book. Indirect neighbors — Node-1.1 (natural medicine encyclopedia), Node-1.2 (healing foods), Node-1.3 (practical guide to acu-points), Node-1.4 (herbalist way to healing), Node-1.5 (integrative nutrition) — are all health-related books, collectively confirming a health context across both hops.

### Free-Text Explanation

The classification of ROOT into "Books" is supported by its own keywords and the co-purchase neighborhood.

ROOT: Keywords like "mineral" (0.08), "supplement" (0.02), and "ionic" (0.05) clearly identify this as a health supplement product — quintessentially a health-related product.
  - Node-1: A health book (keywords: "healthy" (0.01), "medicine" (0.10), "optimum" (0.04), "health" (0.04), "kind" (0.14)) is a direct health-related book, reinforcing the Books category.
    - Node-1.1 ~ Node-1.5: Natural medicine encyclopedia, healing foods, practical guide to acu-points, herbalist way to healing, and integrative nutrition are all health-related books, supporting the Books category.

In summary, ROOT's own high-saliency keywords strongly signal health-related products, and the entire co-purchase neighborhood consists of health-related books, providing robust evidence for the "Books" category.
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/193.json`).

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
<verbalized-graph>ROOT: product(-0.06) amazon(-0.00) platform(0.03) title(0.03) content(0.11) title(0.09) pure(0.03) essence(0.11) labs(0.02) ionic-(0.05) fizz(-0.00) super(-0.03) d-(0.00) k(0.01) calcium(-0.05) plus(0.05) mineral(0.08) supplement,(0.02) raspberry,(-0.01) lemonade,(0.03) 420(-0.01) gram.(0.05) content(0.06) ionic-(0.01) fizz(-0.01) super(-0.02) d-(0.00) k(0.01) calcium(-0.05) plus-(0.01) raspberry(-0.00) lemonade(-0.00) 
Node-1: product(-0.03) amazon(-0.01) platform(-0.03) title(0.07) content(-0.05) title(0.02) staying(0.03) healthy(0.01) seasons.(0.02) content(0.07) one(0.07) classics(0.06) field(0.01) integrative(0.10) medicine.-(-0.02) dr.(0.02) andrew(0.06) weil,(0.03) author(0.09) of8(0.03) weeks(0.09) optimum(0.04) health(0.04) kind(0.14) book(-0.03) helps(0.01) redefine(0.04) healing.(-0.01) instead(0.08) offering(0.06) drugs(0.06) surgery,(0.03) advocates(0.02) natural(0.03) path(0.06) helps(0.07) us(0.03) heal(0.07) within.(0.06) "-(-0.09) michael(0.05) samuels,(-0.04) author(0.13) ofthe(-0.00) well(-0.40) body(0.13) book(0.11) 
Node-1.1: product(-0.00) amazon(0.00) platform(0.00) title(-0.00) content(0.00) title(0.00) encyclopedia(0.00) natural(0.00) medicine(-0.00) third(0.00) edition.(0.00) content(0.00) dr.(0.00) michael(-0.00) t.(0.00) murrayis(0.00) regarded(-0.00) world(0.00) authority(0.00) natural(0.00) medicine.(0.00) educator,(0.00) lecturer,(0.00) researcher,(0.00) health(0.00) food(0.00) industry(0.00) consultant,(0.00) author(0.00) thirty(0.00) books(0.00) health(0.00) healing.(-0.00) lives(0.00) arizona.(0.00) dr.(0.00) joseph(-0.00) pizzornois(0.00) co-(-0.00) founder(-0.00) president(-0.00) emeritus(0.00) bastyr(0.00) university,(0.00) leading(0.00) institution(0.00) teaching(0.00) naturopathic(0.00) medicine.(-0.00) medical(0.00) editor(-0.00) ofintegrative(0.00) medicine(0.00) clinician(0.00) 8217(-0.00) journaland(0.00) ongoing(0.00) contributor(-0.00) magazines,(0.00) asnatural(0.00) healthandbetter(-0.00) nutrition.(-0.00) lives(0.00) washington(-0.00) state.(0.00) 
Node-1.2: product(0.00) amazon(0.00) platform(0.00) title(-0.00) content(0.00) title(-0.00) encyclopedia(0.00) healing(0.00) foods.(-0.00) content(0.00) author(-0.00) 23(-0.00) books,(-0.00) including(0.00) acclaimed(-0.00) bestellerthe(0.00) encyclopedia(-0.00) natural(-0.00) foods(0.00) co-(0.00) authored(-0.00) dr.(-0.00) joseph(-0.00) pizzorno(-0.00) ),(0.00) dr.(-0.00) michael(-0.00) t.(0.00) murrayis(-0.00) regarded(0.00) world(-0.00) authority(0.00) natural(-0.00) medicine.(0.00) educator,(0.00) lecturer,(-0.00) researcher(0.00) health(0.00) food(0.00) industry(0.00) consultant,(-0.00) michael(-0.00) also(-0.00) serves(0.00) director(0.00) product(-0.00) development(-0.00) education(-0.00) natural(-0.00) factors,(-0.00) health(0.00) product(0.00) firm.(0.00) dr.(0.00) joseph(-0.00) pizzornois(0.00) cofounder(0.00) bastyr(-0.00) university,(0.00) first(-0.00) accredited(-0.00) multidisciplinary(-0.00) university(-0.00) natural(-0.00) medicine(-0.00) united(-0.00) states.(-0.00) lara(0.00) pizzorno,(-0.00) m.(-0.00) a.,(-0.00) l.(-0.00) m.(-0.00) t.,(-0.00) health(-0.00) writer(0.00) medical(0.00) editor(-0.00) twenty(-0.00) years(-0.00) experience.(0.00) 
Node-1.3: product(-0.00) amazon(0.00) platform(-0.00) title(0.00) content(-0.00) title(-0.00) practical(-0.00) guide(-0.00) acu-(0.00) points.(0.00) content(-0.01) chris(0.00) jarmey,(0.00) mcsp,(0.00) ds,(0.00) mrss,(0.00) teaches(0.00) shiatsu,(-0.00) qigong,(0.00) bodywork(0.00) therapy,(-0.00) anatomy.(-0.01) author(-0.00) ofthe(0.00) concise(0.00) book(-0.00) muscles,(0.00) shiatsu(-0.00) complete(0.00) guide,(-0.00) books,(-0.00) lives(-0.00) marlborough,(-0.00) uk.(-0.00) ilaira(0.00) bouratinos,(0.00) dipac,(0.00) ds,(-0.01) founded(0.00) european(-0.00) institute(-0.00) oriental(-0.00) medicine(-0.00) 1998.(0.00) lives(0.01) athens,(-0.01) greece.(-0.00) 
Node-1.4: product(-0.00) amazon(-0.00) platform(-0.00) title(0.00) content(-0.00) title(0.00) herbalist(0.00) way(0.00) art(0.00) practice(-0.00) healing(-0.00) plant(0.01) medicines(-0.00) ".(-0.00) content(0.00) 8212(0.00) few,(0.00) rare(0.00) book(0.00) 8212(-0.00) destined(-0.00) become(0.00) herbal(0.00) classics,(0.00) treasured(0.00) like(0.00) old(0.00) friends,(0.00) thumbed(0.00) depth(0.00) herbal(-0.00) wisdom,(-0.00) teachings,(-0.00) inner(0.01) brilliance(0.01) illuminates(0.00) ancient(-0.00) field(0.00) plant(0.00) study.(-0.00) michael(0.00) nancy(0.00) phillips(-0.00) created(0.01) special(0.00) inspirational(0.01) work.(0.00) "--(0.01) rosemary(-0.00) gladstar,(0.01) foreword(0.02) 
Node-1.5: product(0.00) amazon(0.00) platform(0.00) title(0.00) content(0.00) title(0.00) integrative(0.00) nutrition.(-0.00) content(0.00) balanced(0.00) comprehensive(0.00) book(0.00) nutrition...(-0.00) presented(0.00) accessible(0.00) engaging(0.00) way.(-0.00) joshua(-0.00) rosenthal(0.00) discusses(0.00) fad(-0.00) extreme(0.00) diets(0.00) popular,(-0.00) looks(0.00) politics(0.00) food,(-0.00) afraid(-0.00) look(-0.00) esoteric(0.00) subjects,(-0.00) energy(0.00) different(-0.00) foods(0.00) eating(0.00) spiritual(0.00) practice.(-0.01) recommend(0.00) integrative(-0.00) nutrition(-0.00) must-(0.00) read(-0.00) everyone(-0.00) interested(-0.00) basic(-0.00) component(-0.00) good(-0.00) health.--(0.00) andrew(-0.00) weil,(-0.00) md,(-0.00) author(-0.00) 8(-0.00) weeks(0.00) optimum(-0.00) health(-0.00) healthy(-0.00) agingintegrative(-0.00) nutrition(0.00) brilliantly(0.00) blends(-0.00) art(0.00) science(-0.00) nutrition(0.00) personal(0.00) growth(0.00) aspects(0.00) love,(-0.00) relationship,(0.00) fitness,(-0.00) career,(0.00) spiritual(0.00) practice(0.00) help(0.00) people(0.00) find(0.00) path(0.00) toward(0.00) health(0.00) happiness.--(-0.00) deepak(0.00) chopra,(-0.00) author(0.00) buddha(-0.00) story(0.00) enlightenmentintegrative(-0.00) nutrition(-0.00) comprehensive,(-0.00) practical(-0.00) approach(0.00) nutrition(-0.00) simply(0.00) makes(-0.01) sense.--(0.00</verbalized-graph>

### Classification Label
Books

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 51874
- Title: Pure Essence Labs Ionic-Fizz Super D-K Calcium Plus Mineral Supplement, Raspberry, Lemonade, 420 Gram
- True class (canonical `y`): **Health & Personal Care**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Books**
- Prediction recorded by this method's pipeline: **Books**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Pure Essence Labs Ionic-Fizz Super D-K Calcium Plus Mineral Supplement, Raspberry, Lemonade, 420 Gram. Content: Ionic-Fizz Super D-K Calcium Plus - Raspberry Lemonade
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 12727 | Books | Staying Healthy With the Seasons |

### 2-hop (shortest distance exactly 2): 5 nodes

| node id | true class | title |
|---|---|---|
| 1544 | Books | The Encyclopedia of Natural Medicine Third Edition |
| 12717 | Books | Encyclopedia of Healing Foods |
| 51875 | Books | A Practical Guide to Acu-points |
| 51876 | Books | "The Herbalist's Way: The Art and Practice of Healing with Plant Medicines" |
| 51877 | Books | Integrative Nutrition |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/193.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Books**, ground truth = **Health & Personal Care**.
The verbalized graph is 6156 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 51874 | 38 | 0.1115 | yes |
| Node-1 | 1 | 12727 | 75 | 0.1447 | yes |
| Node-1.1 | 2 | 1544 | 106 | 0.0050 | yes |
| Node-1.2 | 3 | 12717 | 116 | 0.0027 | yes |
| Node-1.3 | 4 | 51875 | 69 | 0.0063 | yes |
| Node-1.4 | 5 | 51876 | 109 | 0.0195 | yes |
| Node-1.5 | 6 | 51877 | 176 | 0.0048 | yes |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, ROOT->Node-1

### Tokens and scores

**ROOT** (global 51874):

~~~~~~text
product (-0.0615) from (-0.0639) amazon (-0.0047) platform (0.0273) with (-0.0529) title (0.0309) and (-0.0904) content (0.1115) : (-0.0249) title (0.0874) : (-0.0382) pure (0.0283) essence (0.1053) labs (0.0163) ionic- (0.0453) fizz (-0.0005) super (-0.0270) d- (0.0024) k (0.0126) calcium (-0.0527) plus (0.0482) mineral (0.0795) supplement, (0.0189) raspberry, (-0.0103) lemonade, (0.0258) 420 (-0.0129) gram. (0.0465) content (0.0617) : (-0.0097) ionic- (0.0057) fizz (-0.0103) super (-0.0161) d- (0.0001) k (0.0139) calcium (-0.0459) plus- (0.0081) raspberry (-0.0046) lemonade (-0.0001)
~~~~~~

**Node-1** (global 12727):

~~~~~~text
product (-0.0341) from (0.0553) amazon (-0.0150) platform (-0.0282) with (-0.0143) title (0.0705) and (0.0612) content (-0.0490) : (0.0645) title (0.0226) : (0.0430) staying (0.0272) healthy (0.0079) with (0.0771) the (0.1075) seasons. (0.0235) content (0.0704) : (0.0567) one (0.0729) of (0.0414) the (0.0546) classics (0.0648) in (0.0266) the (0.0867) field (0.0138) of (0.0270) integrative (0.1047) medicine.- (-0.0243) dr. (0.0169) andrew (0.0618) weil, (0.0305) author (0.0851) of8 (0.0345) weeks (0.0907) to (0.0221) optimum (0.0417) health (0.0418) " (-0.0490) this (0.0633) is (0.0320) the (0.0312) kind (0.1447) of (0.0169) book (-0.0315) that (0.0511) helps (0.0125) to (0.0449) redefine (0.0366) healing. (-0.0086) instead (0.0751) of (0.0382) offering (0.0596) drugs (0.0564) and (0.0670) surgery, (0.0333) it (0.1040) advocates (0.0249) a (0.0364) natural (0.0292) path (0.0552) that (0.0541) helps (0.0743) us (0.0342) to (0.0461) heal (0.0682) from (0.0303) within. (0.0584) "- (-0.0917) michael (0.0513) samuels, (-0.0450) author (0.1314) ofthe (-0.0026) well (-0.4044) body (0.1263) book (0.1094)
~~~~~~

**Node-1.1** (global 1544):

~~~~~~text
product (-0.0001) from (0.0005) amazon (0.0006) platform (0.0006) with (0.0002) title (-0.0006) and (0.0011) content (0.0001) : (0.0012) title (0.0010) : (0.0006) the (-0.0017) encyclopedia (0.0003) of (0.0010) natural (0.0005) medicine (-0.0020) third (0.0026) edition. (0.0023) content (0.0005) : (-0.0003) dr. (0.0016) michael (-0.0021) t. (0.0009) murrayis (0.0013) regarded (-0.0006) as (0.0014) the (-0.0003) world (0.0013) authority (0.0002) on (0.0004) natural (0.0009) medicine. (0.0003) an (0.0005) educator, (0.0022) lecturer, (0.0022) researcher, (0.0012) and (0.0007) health (0.0021) food (0.0012) industry (0.0017) consultant, (0.0004) he (0.0024) is (0.0003) the (-0.0004) author (0.0032) of (0.0004) more (0.0010) than (-0.0000) thirty (0.0011) books (0.0013) on (0.0002) health (0.0021) and (0.0028) healing. (-0.0006) he (0.0034) lives (0.0015) in (-0.0016) arizona. (0.0028) dr. (0.0010) joseph (-0.0006) pizzornois (0.0015) the (-0.0019) co- (-0.0004) founder (-0.0021) and (0.0011) president (-0.0016) emeritus (0.0028) of (-0.0003) bastyr (0.0019) university, (0.0004) the (-0.0015) leading (0.0008) institution (0.0020) teaching (0.0004) naturopathic (0.0018) medicine. (-0.0013) he (0.0048) is (-0.0017) the (-0.0008) medical (0.0045) editor (-0.0008) ofintegrative (0.0000) medicine (0.0005) : (0.0006) a (0.0023) clinician (0.0012) & (0.0023) # (0.0012) 8217 (-0.0012) ; (0.0034) s (0.0004) journaland (0.0040) an (-0.0030) ongoing (0.0032) contributor (-0.0006) to (0.0018) magazines, (0.0003) such (-0.0024) asnatural (0.0001) healthandbetter (-0.0000) nutrition. (-0.0003) he (0.0050) lives (0.0033) in (-0.0012) washington (-0.0006) state. (0.0036)
~~~~~~

**Node-1.2** (global 12717):

~~~~~~text
product (0.0005) from (0.0017) amazon (0.0027) platform (0.0009) with (0.0011) title (-0.0013) and (0.0004) content (0.0002) : (0.0008) title (-0.0001) : (0.0004) encyclopedia (0.0009) of (-0.0002) healing (0.0009) foods. (-0.0021) content (0.0016) : (0.0027) author (-0.0003) of (-0.0005) 23 (-0.0000) books, (-0.0008) including (0.0017) the (-0.0001) acclaimed (-0.0005) bestellerthe (0.0003) encyclopedia (-0.0001) of (0.0002) natural (-0.0001) foods (0.0008) ( (-0.0004) co- (0.0000) authored (-0.0008) with (-0.0003) dr. (-0.0000) joseph (-0.0001) pizzorno (-0.0002) ), (0.0009) dr. (-0.0000) michael (-0.0011) t. (0.0000) murrayis (-0.0006) regarded (0.0003) as (-0.0006) the (0.0002) world (-0.0011) authority (0.0007) on (0.0005) natural (-0.0001) medicine. (0.0001) an (0.0006) educator, (0.0001) lecturer, (-0.0002) researcher (0.0010) and (-0.0001) health (0.0008) food (0.0014) industry (0.0011) consultant, (-0.0002) michael (-0.0006) also (-0.0002) serves (0.0007) as (-0.0002) the (-0.0003) director (0.0001) of (0.0004) product (-0.0004) development (-0.0002) and (-0.0002) education (-0.0000) at (0.0007) natural (-0.0001) factors, (-0.0009) a (-0.0004) health (0.0007) product (0.0016) firm. (0.0001) dr. (0.0000) joseph (-0.0001) pizzornois (0.0003) cofounder (0.0009) of (0.0010) bastyr (-0.0007) university, (0.0002) the (-0.0010) first (-0.0000) accredited (-0.0010) multidisciplinary (-0.0002) university (-0.0009) of (-0.0008) natural (-0.0007) medicine (-0.0010) in (-0.0008) the (-0.0005) united (-0.0010) states. (-0.0004) lara (0.0027) pizzorno, (-0.0008) m. (-0.0008) a., (-0.0007) l. (-0.0005) m. (-0.0000) t., (-0.0003) is (-0.0029) a (0.0011) health (-0.0001) writer (0.0005) and (-0.0011) medical (0.0010) editor (-0.0007) with (0.0004) more (0.0004) than (0.0002) twenty (-0.0012) years (-0.0006) of (0.0008) experience. (0.0011)
~~~~~~

**Node-1.3** (global 51875):

~~~~~~text
product (-0.0027) from (0.0063) amazon (0.0044) platform (-0.0016) with (0.0020) title (0.0005) and (0.0033) content (-0.0011) : (0.0045) title (-0.0034) : (0.0027) a (0.0009) practical (-0.0006) guide (-0.0001) to (0.0030) acu- (0.0022) points. (0.0046) content (-0.0061) : (-0.0042) chris (0.0026) jarmey, (0.0016) mcsp, (0.0023) ds, (0.0010) mrss, (0.0012) teaches (0.0003) shiatsu, (-0.0010) qigong, (0.0013) bodywork (0.0004) therapy, (-0.0010) and (0.0004) anatomy. (-0.0053) the (-0.0019) author (-0.0043) ofthe (0.0015) concise (0.0023) book (-0.0033) of (0.0001) muscles, (0.0020) shiatsu (-0.0043) : (0.0003) the (-0.0025) complete (0.0002) guide, (-0.0015) and (0.0009) other (0.0011) books, (-0.0013) he (0.0039) lives (-0.0022) in (0.0028) marlborough, (-0.0004) uk. (-0.0004) ilaira (0.0014) bouratinos, (0.0001) dipac, (0.0006) ds, (-0.0050) founded (0.0006) the (-0.0009) european (-0.0005) institute (-0.0004) of (0.0019) oriental (-0.0014) medicine (-0.0031) in (0.0000) 1998. (0.0017) she (0.0019) lives (0.0056) in (0.0009) athens, (-0.0054) greece. (-0.0008)
~~~~~~

**Node-1.4** (global 51876):

~~~~~~text
product (-0.0004) from (0.0039) amazon (-0.0026) platform (-0.0038) with (0.0005) title (0.0005) and (0.0031) content (-0.0021) : (0.0004) title (0.0022) : (-0.0002) " (-0.0017) the (-0.0039) herbalist (0.0033) ' (-0.0019) s (-0.0001) way (0.0009) : (0.0006) the (-0.0064) art (0.0029) and (0.0029) practice (-0.0000) of (0.0011) healing (-0.0015) with (0.0040) plant (0.0060) medicines (-0.0030) ". (-0.0009) content (0.0020) : (-0.0064) " (-0.0048) and (-0.0007) then (0.0028) there (-0.0009) are (0.0027) those (0.0027) & (-0.0008) # (0.0003) 8212 (0.0016) ; (0.0034) only (0.0017) a (-0.0015) few, (0.0005) a (-0.0012) rare (0.0003) book (0.0032) here (0.0013) and (0.0023) there (0.0010) & (0.0022) # (0.0037) 8212 (-0.0004) ; (0.0060) that (0.0004) are (0.0011) destined (-0.0013) to (0.0028) become (0.0024) herbal (0.0047) classics, (0.0032) treasured (0.0022) like (0.0004) old (0.0017) friends, (0.0004) thumbed (0.0004) through (-0.0010) again (0.0023) and (0.0003) again (0.0032) for (-0.0005) their (0.0007) depth (0.0041) of (0.0033) herbal (-0.0023) wisdom, (-0.0001) for (0.0003) their (0.0017) teachings, (-0.0022) and (0.0002) for (0.0013) their (0.0007) inner (0.0052) brilliance (0.0073) that (-0.0011) illuminates (0.0031) this (-0.0016) ancient (-0.0006) field (0.0003) of (0.0017) plant (0.0041) study. (-0.0007) michael (0.0041) and (0.0038) nancy (0.0016) phillips (-0.0021) have (0.0031) created (0.0078) such (0.0056) a (-0.0047) special (0.0008) and (0.0038) inspirational (0.0071) work. (0.0046) "-- (0.0097) rosemary (-0.0049) gladstar, (0.0057) from (0.0113) the (0.0074) foreword (0.0195)
~~~~~~

**Node-1.5** (global 51877):

~~~~~~text
product (0.0005) from (-0.0026) amazon (0.0007) platform (0.0000) with (0.0004) title (0.0020) and (0.0001) content (0.0003) : (0.0016) title (0.0044) : (-0.0001) integrative (0.0017) nutrition. (-0.0016) content (0.0015) : (0.0010) this (0.0011) is (0.0009) a (0.0002) balanced (0.0015) and (0.0003) comprehensive (0.0019) book (0.0023) on (0.0032) nutrition... (-0.0044) presented (0.0048) in (-0.0006) an (0.0000) accessible (0.0003) and (0.0004) engaging (0.0020) way. (-0.0026) joshua (-0.0008) rosenthal (0.0017) discusses (0.0010) all (0.0007) the (-0.0024) fad (-0.0005) and (0.0000) extreme (0.0014) diets (0.0008) that (0.0011) are (0.0009) so (0.0007) popular, (-0.0017) looks (0.0006) at (0.0004) the (-0.0022) politics (0.0011) of (-0.0006) food, (-0.0013) and (-0.0014) is (0.0009) not (0.0011) afraid (-0.0010) to (0.0005) look (-0.0001) at (0.0011) more (0.0001) esoteric (0.0008) subjects, (-0.0001) such (-0.0021) as (0.0003) the (-0.0020) energy (0.0018) of (0.0004) different (-0.0012) foods (0.0029) and (-0.0004) eating (0.0014) as (0.0003) a (-0.0025) spiritual (0.0042) practice. (-0.0065) i (-0.0016) recommend (0.0024) integrative (-0.0001) nutrition (-0.0022) as (0.0014) a (0.0010) must- (0.0006) read (-0.0008) for (0.0012) everyone (-0.0033) interested (-0.0016) in (-0.0009) this (-0.0006) most (-0.0032) basic (-0.0014) component (-0.0018) of (0.0003) good (-0.0006) health.-- (0.0011) andrew (-0.0024) weil, (-0.0002) md, (-0.0002) author (-0.0003) of (-0.0041) 8 (-0.0017) weeks (0.0002) to (-0.0010) optimum (-0.0015) health (-0.0013) and (-0.0008) healthy (-0.0005) agingintegrative (-0.0004) nutrition (0.0011) brilliantly (0.0014) blends (-0.0001) the (-0.0011) art (0.0002) and (-0.0002) science (-0.0002) of (0.0005) nutrition (0.0001) with (0.0021) the (-0.0014) personal (0.0003) growth (0.0011) aspects (0.0006) of (0.0013) love, (-0.0001) relationship, (0.0001) fitness, (-0.0009) career, (0.0010) and (0.0001) spiritual (0.0024) practice (0.0010) to (0.0003) help (0.0004) people (0.0009) find (0.0008) their (0.0007) path (0.0001) toward (0.0008) health (0.0012) and (-0.0002) happiness.-- (-0.0003) deepak (0.0012) chopra, (-0.0025) author (0.0030) of (0.0040) buddha (-0.0012) : (-0.0007) a (-0.0011) story (0.0013) of (0.0013) enlightenmentintegrative (-0.0017) nutrition (-0.0019) is (-0.0019) a (-0.0005) comprehensive, (-0.0014) practical (-0.0015) approach (0.0010) to (-0.0002) nutrition (-0.0005) that (-0.0008) simply (0.0008) makes (-0.0056) sense.-- (0.0014) christiane (0.0012) northrup, (-0.0009) md, (-0.0009) author (0.0011) of (-0.0001) mother- (0.0012) daughter (0.0002) wisdom (-0.0023) and (-0.0012) women (0.0005) ' (-0.0005) s (0.0011) bodies, (-0.0005) women (0.0003) ' (-0.0008) s (0.0022) wisdom (0.0001)
~~~~~~
