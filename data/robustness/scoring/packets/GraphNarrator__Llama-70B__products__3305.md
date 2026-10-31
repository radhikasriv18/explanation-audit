# Reference packet: GraphNarrator__Llama-70B__products__3305

- Method: GraphNarrator; configuration: Llama-70B; dataset: products; target node: 3305
- Explanation source: `./robustness_2026-10-30/llama70b/graphnarrator/products/3305.json` (response)
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

- ROOT (bamboo skewer)
  - Node-1 (craft sticks)
    - Node-1.1 (chenille stems)
    - Node-1.2 (invisible tape)
    - Node-1.3 (waxing applicators)
    - Node-1.4 (buttons)
    - Node-1.5 (jingle bells)
    - Node-1.6 (chenille stems)
    - Node-1.7 (boozy treats)
    - Node-1.8 (washable school glue)

1. Word-Level Evaluation:

Keywords with high saliency scores in ROOT — "platform" (0.18), "bamboo" (0.13), "skewer" (0.01), "6 inch" (0.13, 0.10) — are moderately associated with craft supplies. However, these words alone do not strongly indicate a specific category.

2. Graph-Level Aggregation:

Node-1 (craft sticks, keywords: "craft" (0.00), "sticks" (0.00)) is a direct neighbor with low saliency, but its children provide more insight. Node-1.1 (chenille stems), Node-1.5 (jingle bells), and Node-1.6 (chenille stems) are all craft supplies, while Node-1.2 (invisible tape) and Node-1.8 (washable school glue) are also related to crafting or DIY projects. Node-1.3 (waxing applicators) and Node-1.4 (buttons) are less directly related to crafting, but still relevant to the broader category of Health & Personal Care.

### Free-Text Explanation
```markdown
The classification of ROOT into "Health & Personal Care" is supported by its own keywords and the co-purchase neighborhood.

ROOT: Keywords like "platform" (0.18), "bamboo" (0.13), and "skewer" (0.01) are moderately associated with craft supplies, but do not strongly indicate a specific category.
  - Node-1: Craft sticks are a direct neighbor, and while not strongly indicative of Health & Personal Care, their children provide more insight.
    - Node-1.1 ~ Node-1.5 ~ Node-1.6: Chenille stems, jingle bells, and other craft supplies are related to crafting or DIY projects, but not directly to Health & Personal Care.
    - Node-1.2 ~ Node-1.8: Invisible tape and washable school glue are also related to crafting or DIY projects, but not directly to Health & Personal Care.
    - Node-1.3: Waxing applicators are a key indicator of the Health & Personal Care category, as they are used for hair removal and personal grooming.
    - Node-1.4: Buttons are less directly related to Health & Personal Care, but can be used in craft projects related to personal care or beauty.

In summary, while the ROOT node's keywords do not strongly indicate Health & Personal Care, the co-purchase neighborhood, particularly Node-1.3 (waxing applicators), provides robust evidence for the classification.
```
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/7.json`).

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
<verbalized-graph>ROOT: product(-0.29) amazon(0.14) platform(0.18) title(0.08) content(0.23) title(0.00) winco(-0.03) bamboo(0.13) skewer,(0.01) 6(0.13) inch.(0.10) content(-0.04) bamboo(0.09) skewer,(0.03) 100(-0.11) per(0.06) bag,(0.06) 6(-0.07) ".(0.04) 
Node-1: product(-0.00) amazon(0.00) platform(0.00) title(0.00) content(0.00) title(0.00) loew(0.00) cornell(0.01) 1021254(-0.00) woodsies(0.00) craft(-0.00) sticks,(-0.00) 1000-(-0.00) piece.(0.00) content(-0.00) woodsies(-0.00) 1000-(0.00) count(0.00) natural(0.00) craft(0.00) sticks(-0.00) great(-0.00) use(-0.00) classroom(0.00) projects,(0.00) party(0.00) crafts,(0.00) camp(-0.00) crafts.(0.00) craft(-0.00) sticks(0.00) measure(-0.00) 4-(-0.00) 1(-0.00) 2(0.00) 3(-0.00) 8(0.00) inches(0.00) natural(-0.00) raw(0.00) wood.(0.01) ideal(0.00) crafters,(0.00) teachers,(0.00) students.(0.00) made(0.00) birch(0.00) wood,(0.00) non(0.00) food(-0.00) safe.(0.01) 
Node-1.1: product(0.00) amazon(-0.00) platform(-0.00) title(0.00) content(0.00) title(0.00) darice(0.00) 10843-(0.00) 99(0.00) 350-(0.00) pack(0.00) chenille(0.00) tinsel(-0.00) bump(0.00) chenille(0.00) stems,(0.00) 12-(0.00) inch,(-0.00) assorted.(0.00) content(0.00) craft(0.00) pack(0.00) includes(0.00) chenille(0.00) stems,(0.00) tinsel(-0.00) stems(0.00) bump(0.00) chenille(0.00) stems(0.00) assortment(0.00) sizes(0.00) colors.(0.00) perfect(0.00) group(0.00) crafting(0.00) kids(0.00) party(-0.00) crafts.(0.00) includes(0.00) 350(0.00) stems(0.00) per(-0.00) package.(0.00) measures(0.00) 12-(0.00) inch(-0.00) length.(0.00) 
Node-1.2: product(-0.00) amazon(0.00) platform(0.00) title(-0.00) content(0.00) title(-0.00) duck(0.00) brand(-0.00) 1302209(0.00) duck(0.00) 3(-0.00) 4(0.00) inch(0.00) 500(-0.00) inch(0.00) invisible(0.00) tape,(0.00) 3-(0.00) pack.(0.00) content(0.00) henkel(0.00) duck(0.00) invisible(-0.00) tape(-0.00) premium(0.00) quality(-0.00) acetate(-0.00) tape,(-0.00) featuring(-0.00) quality(0.00) matte(0.00) finish(-0.00) invisible(0.00) paper(0.00) mending,(0.00) sealing,(-0.00) gift(0.00) wrapping.(0.00) acid(0.00) free(-0.00) archival(0.00) applications(0.00) ckok(0.00) approved(-0.00) photo(-0.00) scrapbooking(0.00) projects.(0.00) 3(-0.00) 4-(-0.00) by-(0.00) 650-(-0.00) inch(-0.00) tape(-0.00) writable(-0.00) surface(0.00) accept(-0.00) ball(-0.00) pen,(0.00) pencil,(0.00) marker.(0.00) refill(-0.00) rolls(-0.00) come(0.00) 3(-0.00) pack(-0.00) 3(-0.00) 4(-0.00) inch(-0.00) wide(0.00) 500(-0.00) inches(0.00) long.(0.00) handy,(0.00) disposable(0.00) dispenser(0.00) included.(-0.00) 
Node-1.3: product(-0.00) amazon(0.00) platform(-0.00) title(0.00) content(-0.00) title(0.00) graham(-0.00) spa(0.00) essentials(0.00) 3.(-0.00) 5(0.00) inch(-0.00) make-(-0.00) waxing(0.00) applicators(-0.00) 100pk.(0.00) content(0.00) graham(0.00) spa(-0.00) essentials(0.00) 3.(0.00) 5(0.00) inch(-0.00) make-(-0.00) waxing(-0.00) applicators(-0.00) 100pk(-0.00) spa(0.00) essentials(0.00) eye(-0.00) lip(0.00) applicators(0.00) perfect(0.00) applying(0.00) face(0.00) eye(0.00) make-(0.00) up.(0.00) applicators(-0.00) also(-0.00) ideal(0.00) eyebrow(0.00) waxing.(0.00) thesedisposableapplicators(0.00) offersafe(0.00) sanitary(0.00) conditions(0.00) clients(0.00) users.(0.00) 
Node-1.4: product(0.00) amazon(-0.00) platform(0.00) title(0.00) content(0.00) title(0.00) blumenthal(0.00) lansing(0.00) company(0.00) favorite(0.00) findings(0.00) 3-(-0.00) 1(0.00) 2-(-0.00) ounce(0.00) big(-0.00) bag(0.00) buttons,(0.00) flowers.(0.00) content(0.00) oodles(-0.00) buttons(0.00) every(-0.00) crafter(0.00) treasure(0.00) chest.(-0.00) favorite(0.00) findings(0.00) big(-0.00) bags(0.00) buttons(0.00) colorful(-0.00) assortment(0.00) sizes(0.00) shapes(-0.00) add(0.00) special(-0.00) touch(0.00) projects.(-0.00) stack(-0.00) em,(-0.00) sew(-0.00) em,(0.00) glue(-0.00) em(0.00) add(0.00) personal(-0.00) touch(0.00) great(0.00) way(0.00) say(0.00) made(0.00) especially(0.00) you.(-0.00) package(0.00) 3-(0.00) 1(0.00) 2-(0.00) ounces(0.00) 100-(0.00) percent(0.00) nylon(0.00) buttons(0.00) color(0.00) themed(0.00) attached(0.00) wood,(0.00) paper,(0.00) styrofoam(-0.00) much,(-0.00) much(0.00) more.(0.00) contents(0.00) package(0.00) subject(0.00) change(-0.00) may(-0.00) exactly(0.00) pictured.(0.00) 
Node-1.5: product(-0.00) amazon(0.00) platform(0.00) title(0.00) content(-0.00) title(0.00) fiber(-0.00) craft(-0.00) 72-(0.00) pack(-0.00) jingle(0.00) bells,(0.00) 6mm-(0.00) 16mm,(-0.00) gold.(0.00) content(-0.00) fibre(-0.00) craft-(-0.00) jingle(0.00) bells.(0.00) 6mm(-0.00) 16mm(-0.00) 72(-0.00) pieces(0.00) per(0.00) package.(-0.00) gold.(0.00) jingle(-0.00) bell(-0.00) perfect(-0.00) various(0.00) crafts.(-0.00) looks(-0.00) great(-0.00) put(0.00) holiday(-0.00) wreath(0.00) flower(0.00) arrangement(0.00) creative(0.00) way.(0.00) bell(0.00) also(0.00) great(-0.00) making(0.00) halloween(-0.00) costumes(-0.00) making(0.00) christmas(0.00) ornaments(0.00) fun(0.00) holiday(0.00) projects.(-0.00) 
Node-1.6: product(-0.00) amazon(-0.00) platform(-0.00) title(0.00) content(-0.00) title(0.00) darice(0.00) victoria(0.00) lynn(0.00) chenille(0.00) stems(0.00) 6mm(0.00) 12(0.00) quot(-0.00) 100(0.00) pkg-(0.00) white.(0.00) content(0.00) chenille(-0.00) stems.(0.00) soft(-0.00) flexible(0.00) chenille(0.00) stems(0.00) fun(0.00) kids(-0.00) great(0.00) use(0.00) school,(0.00) home,(0.00) camp(0.00) more.(0.00) package(-0.00) contains(0.00) 100(0.00) 6mm(-0.00) x(0.00) 12(0.00) stems.(0.00) available(0.00) variety(-0.00) colors,(-0.00) sold(0.00) separately.(0.00) 
Node-1.7: product(-0.00) amazon(-0.00) platform(-0.00) title(-0.00) content(0.00) title(0.00) poptails(0.00) 60(-0.00) boozy(0.00) treats(-0.00) served(-0.00) stick.(-0.00) content(0.00) none(-0.00) 
Node-1.8: product(-0.00) amazon(0.00) platform(0.00) title(0.00) content(0.00) title(0.00) sargent(0.00) art(0.00) 22-(-0.00) 1205(0.00) 1-(-0.00) gallon(-0.00) washable(-0.00) school(-0.00) glue.(0.00) content(0.00) sargent(0.00) art(-0.00) school(-0.00) gl</verbalized-graph>

### Classification Label
Health & Personal Care

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 3305
- Title: Winco Bamboo Skewer, 6 inch
- True class (canonical `y`): **Patio, Lawn & Garden**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Arts, Crafts & Sewing**
- Prediction recorded by this method's pipeline: **Health & Personal Care**

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

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/7.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Health & Personal Care**, ground truth = **Patio, Lawn & Garden**.
The verbalized graph is 11614 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 3305 | 25 | 0.2339 | yes |
| Node-1 | 1 | 343 | 69 | 0.0081 | yes |
| Node-1.1 | 7 | 3249 | 64 | 0.0011 | yes |
| Node-1.2 | 8 | 1840 | 114 | 0.0005 | yes |
| Node-1.3 | 9 | 3302 | 69 | 0.0022 | yes |
| Node-1.4 | 10 | 3303 | 138 | 0.0010 | yes |
| Node-1.5 | 11 | 17 | 82 | 0.0012 | yes |
| Node-1.6 | 12 | 3306 | 66 | 0.0015 | yes |
| Node-1.7 | 13 | 3307 | 23 | 0.0012 | yes |
| Node-1.8 | 14 | 3304 | 82 | 0.0009 | yes |
| Node-1.9 | 15 | 3301 | 28 | 0.0053 | no |
| Node-2 | 2 | 19311 | 30 | 0.0158 | no |
| Node-3 | 3 | 19312 | 129 | 0.0159 | no |
| Node-4 | 4 | 19313 | 158 | 0.0108 | no |
| Node-5 | 5 | 19314 | 60 | 0.0405 | no |
| Node-6 | 6 | 19315 | 172 | 0.0289 | no |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->Node-1.6, Node-1->Node-1.7, Node-1->Node-1.8, Node-1->Node-1.9, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, Node-1.6->Node-1, Node-1.7->Node-1, Node-1.8->Node-1, Node-1.9->Node-1, Node-2->ROOT, Node-3->ROOT, Node-4->ROOT, Node-5->ROOT, Node-6->ROOT, ROOT->Node-1, ROOT->Node-2, ROOT->Node-3, ROOT->Node-4, ROOT->Node-5, ROOT->Node-6

### Tokens and scores

**ROOT** (global 3305):

~~~~~~text
product (-0.2873) from (0.0936) amazon (0.1428) platform (0.1828) with (0.0141) title (0.0787) and (-0.0965) content (0.2339) : (-0.0452) title (0.0041) : (-0.0427) winco (-0.0344) bamboo (0.1308) skewer, (0.0123) 6 (0.1346) inch. (0.0994) content (-0.0443) : (0.0122) bamboo (0.0942) skewer, (0.0291) 100 (-0.1112) per (0.0611) bag, (0.0577) 6 (-0.0740) ". (0.0425)
~~~~~~

**Node-1** (global 343):

~~~~~~text
product (-0.0040) from (0.0002) amazon (0.0039) platform (0.0027) with (-0.0011) title (0.0023) and (-0.0032) content (0.0016) : (0.0018) title (0.0014) : (0.0009) loew (0.0041) cornell (0.0081) 1021254 (-0.0010) woodsies (0.0004) craft (-0.0018) sticks, (-0.0027) 1000- (-0.0011) piece. (0.0030) content (-0.0007) : (0.0009) woodsies (-0.0030) 1000- (0.0014) count (0.0019) natural (0.0001) craft (0.0009) sticks (-0.0017) are (0.0002) great (-0.0009) for (0.0021) use (-0.0007) in (0.0018) classroom (0.0025) projects, (0.0002) party (0.0006) crafts, (0.0007) and (-0.0003) camp (-0.0024) crafts. (0.0015) craft (-0.0012) sticks (0.0022) measure (-0.0006) 4- (-0.0011) 1 (-0.0011) / (0.0015) 2 (0.0007) by (0.0016) 3 (-0.0009) / (0.0023) 8 (0.0001) inches (0.0013) and (-0.0017) are (0.0020) natural (-0.0014) raw (0.0005) wood. (0.0051) ideal (0.0002) for (-0.0000) crafters, (0.0009) teachers, (0.0004) and (0.0003) students. (0.0024) made (0.0013) of (0.0018) birch (0.0030) wood, (0.0000) non (0.0032) food (-0.0033) safe. (0.0052)
~~~~~~

**Node-1.1** (global 3249):

~~~~~~text
product (0.0004) from (0.0000) amazon (-0.0005) platform (-0.0001) with (0.0000) title (0.0011) and (-0.0002) content (0.0005) : (0.0004) title (0.0007) : (0.0005) darice (0.0004) 10843- (0.0004) 99 (0.0005) 350- (0.0005) pack (0.0001) chenille (0.0002) / (0.0005) tinsel (-0.0003) and (0.0001) bump (0.0005) chenille (0.0002) stems, (0.0004) 12- (0.0002) inch, (-0.0000) assorted. (0.0007) content (0.0000) : (0.0005) this (0.0007) craft (0.0004) pack (0.0009) includes (0.0005) chenille (0.0000) stems, (0.0002) tinsel (-0.0001) stems (0.0007) and (0.0002) bump (0.0003) chenille (0.0001) stems (0.0008) in (0.0002) an (-0.0009) assortment (0.0006) of (0.0002) sizes (0.0007) and (0.0005) colors. (0.0004) perfect (0.0005) for (0.0006) group (0.0005) crafting (0.0005) and (0.0002) kids (0.0005) party (-0.0000) crafts. (0.0004) includes (0.0010) 350 (0.0006) stems (0.0004) per (-0.0002) package. (0.0002) measures (0.0007) 12- (0.0005) inch (-0.0004) length. (0.0005)
~~~~~~

**Node-1.2** (global 1840):

~~~~~~text
product (-0.0001) from (-0.0001) amazon (0.0005) platform (0.0000) with (-0.0001) title (-0.0000) and (0.0001) content (0.0001) : (0.0003) title (-0.0000) : (0.0000) duck (0.0001) brand (-0.0001) 1302209 (0.0000) duck (0.0001) 3 (-0.0001) / (0.0000) 4 (0.0001) inch (0.0000) by (0.0000) 500 (-0.0001) inch (0.0000) invisible (0.0000) tape, (0.0000) 3- (0.0000) pack. (0.0000) content (0.0002) : (-0.0002) the (0.0001) henkel (0.0001) duck (0.0003) invisible (-0.0002) tape (-0.0000) is (-0.0001) a (-0.0000) premium (0.0003) quality (-0.0001) acetate (-0.0000) tape, (-0.0000) featuring (-0.0001) a (-0.0001) quality (0.0000) matte (0.0000) finish (-0.0001) for (-0.0001) invisible (0.0002) paper (0.0000) mending, (0.0000) sealing, (-0.0000) and (-0.0000) gift (0.0001) wrapping. (0.0000) it (-0.0001) is (0.0000) acid (0.0003) free (-0.0001) for (-0.0002) archival (0.0001) applications (0.0001) and (-0.0000) is (-0.0001) ckok (0.0001) approved (-0.0001) for (-0.0000) photo (-0.0000) and (-0.0002) scrapbooking (0.0000) projects. (0.0001) the (-0.0001) 3 (-0.0000) / (0.0000) 4- (-0.0000) by- (0.0000) 650- (-0.0000) inch (-0.0002) tape (-0.0001) has (-0.0002) a (-0.0000) writable (-0.0001) surface (0.0000) that (-0.0002) will (0.0001) accept (-0.0002) ball (-0.0002) pen, (0.0000) pencil, (0.0001) or (-0.0001) marker. (0.0002) these (0.0001) refill (-0.0000) rolls (-0.0001) come (0.0000) 3 (-0.0001) to (-0.0001) a (-0.0000) pack (-0.0000) and (-0.0001) are (0.0000) each (-0.0001) 3 (-0.0001) / (0.0000) 4 (-0.0001) inch (-0.0001) wide (0.0001) and (-0.0000) 500 (-0.0000) inches (0.0001) long. (0.0001) a (-0.0001) handy, (0.0002) disposable (0.0002) dispenser (0.0001) is (0.0000) included. (-0.0000)
~~~~~~

**Node-1.3** (global 3302):

~~~~~~text
product (-0.0009) from (0.0005) amazon (0.0013) platform (-0.0007) with (0.0000) title (0.0004) and (-0.0007) content (-0.0002) : (0.0006) title (0.0011) : (0.0003) graham (-0.0000) spa (0.0002) essentials (0.0002) 3. (-0.0001) 5 (0.0003) inch (-0.0002) make- (-0.0000) up (-0.0002) and (-0.0002) waxing (0.0000) applicators (-0.0007) 100pk. (0.0000) content (0.0003) : (-0.0000) graham (0.0003) spa (-0.0001) essentials (0.0002) 3. (0.0001) 5 (0.0002) inch (-0.0001) make- (-0.0000) up (-0.0001) and (-0.0003) waxing (-0.0000) applicators (-0.0002) 100pk (-0.0002) spa (0.0000) essentials (0.0000) eye (-0.0000) / (-0.0001) lip (0.0005) applicators (0.0000) are (0.0003) perfect (0.0005) for (0.0004) applying (0.0003) face (0.0003) and (-0.0003) eye (0.0004) make- (0.0001) up. (0.0007) these (-0.0005) applicators (-0.0001) are (0.0006) also (-0.0001) ideal (0.0009) for (-0.0003) eyebrow (0.0000) waxing. (0.0002) thesedisposableapplicators (0.0006) offersafe (0.0003) and (0.0002) sanitary (0.0006) conditions (0.0002) for (-0.0001) clients (0.0022) and (0.0003) users. (0.0007)
~~~~~~

**Node-1.4** (global 3303):

~~~~~~text
product (0.0001) from (-0.0002) amazon (-0.0005) platform (0.0001) with (0.0001) title (0.0001) and (0.0000) content (0.0002) : (0.0001) title (0.0001) : (-0.0001) blumenthal (0.0002) lansing (0.0002) company (0.0003) favorite (0.0005) findings (0.0009) 3- (-0.0000) 1 (0.0001) / (0.0001) 2- (-0.0001) ounce (0.0002) big (-0.0000) bag (0.0001) of (-0.0001) buttons, (0.0001) flowers. (0.0002) content (0.0001) : (-0.0004) oodles (-0.0000) of (-0.0000) buttons (0.0004) for (0.0001) every (-0.0001) crafter (0.0001) ' (-0.0001) s (-0.0000) treasure (0.0001) chest. (-0.0002) favorite (0.0001) findings (0.0010) big (-0.0002) bags (0.0003) of (-0.0001) buttons (0.0005) are (0.0001) a (-0.0002) colorful (-0.0001) assortment (0.0003) of (-0.0000) sizes (0.0003) and (0.0001) shapes (-0.0000) to (-0.0000) add (0.0000) a (-0.0001) special (-0.0000) touch (0.0000) to (0.0000) all (-0.0001) of (0.0001) your (-0.0006) projects. (-0.0002) stack (-0.0002) ' (-0.0000) em, (-0.0000) sew (-0.0000) ' (-0.0001) em, (0.0000) or (0.0002) glue (-0.0001) ' (-0.0001) em (0.0000) ; (0.0004) they (0.0000) add (0.0001) a (-0.0000) personal (-0.0000) touch (0.0000) that (0.0001) is (0.0002) a (0.0001) great (0.0001) way (0.0001) to (-0.0000) say (0.0003) " (-0.0002) i (0.0002) made (0.0001) this (0.0001) especially (0.0001) for (0.0000) you. (-0.0002) " (0.0000) each (0.0003) package (0.0003) is (0.0001) 3- (0.0001) 1 (0.0001) / (0.0003) 2- (0.0001) ounces (0.0004) of (-0.0001) 100- (0.0000) percent (0.0006) nylon (0.0005) buttons (0.0002) that (0.0004) have (-0.0000) been (-0.0001) color (0.0001) themed (0.0004) and (-0.0000) can (0.0001) be (-0.0000) attached (0.0001) to (-0.0001) wood, (0.0000) paper, (0.0001) styrofoam (-0.0000) and (-0.0001) much, (-0.0001) much (0.0002) more. (0.0001) contents (0.0001) of (-0.0003) each (0.0002) package (0.0001) are (0.0002) subject (0.0002) to (-0.0001) change (-0.0001) and (-0.0001) may (-0.0001) not (0.0005) be (0.0004) exactly (0.0004) as (-0.0002) pictured. (0.0003)
~~~~~~

**Node-1.5** (global 17):

~~~~~~text
product (-0.0006) from (0.0002) amazon (0.0009) platform (0.0002) with (-0.0004) title (0.0002) and (-0.0001) content (-0.0002) : (-0.0001) title (0.0001) : (-0.0000) fiber (-0.0002) craft (-0.0004) 72- (0.0000) pack (-0.0005) jingle (0.0004) bells, (0.0002) 6mm- (0.0001) 16mm, (-0.0002) gold. (0.0009) content (-0.0001) : (0.0002) fibre (-0.0003) craft- (-0.0000) jingle (0.0004) bells. (0.0006) 6mm (-0.0001) to (0.0000) 16mm (-0.0000) in (0.0002) 72 (-0.0001) pieces (0.0001) per (0.0007) package. (-0.0002) gold. (0.0012) the (-0.0009) jingle (-0.0005) bell (-0.0001) is (0.0000) perfect (-0.0000) for (-0.0002) doing (0.0002) various (0.0001) crafts. (-0.0000) it (0.0000) looks (-0.0001) great (-0.0002) when (0.0002) it (0.0001) is (0.0004) put (0.0001) on (0.0002) a (-0.0001) holiday (-0.0002) wreath (0.0003) or (0.0001) in (0.0002) a (-0.0002) flower (0.0004) arrangement (0.0001) in (0.0002) a (-0.0001) creative (0.0004) way. (0.0001) this (-0.0001) bell (0.0003) is (0.0004) also (0.0002) great (-0.0003) for (0.0001) making (0.0001) halloween (-0.0002) costumes (-0.0004) and (0.0001) making (0.0000) christmas (0.0002) ornaments (0.0001) or (0.0001) other (0.0001) fun (0.0004) holiday (0.0004) projects. (-0.0000)
~~~~~~

**Node-1.6** (global 3306):

~~~~~~text
product (-0.0003) from (0.0001) amazon (-0.0001) platform (-0.0000) with (0.0000) title (0.0008) and (0.0002) content (-0.0000) : (0.0006) title (0.0002) : (0.0003) darice (0.0003) victoria (0.0002) lynn (0.0001) chenille (0.0002) stems (0.0002) 6mm (0.0001) 12 (0.0005) & (0.0001) quot (-0.0004) ; (0.0004) 100 (0.0004) / (0.0002) pkg- (0.0004) white. (0.0005) content (0.0001) : (0.0003) chenille (-0.0002) stems. (0.0006) these (0.0000) soft (-0.0000) flexible (0.0004) chenille (0.0002) stems (0.0005) are (-0.0000) fun (0.0004) for (0.0001) kids (-0.0000) and (0.0003) great (0.0001) to (0.0000) use (0.0003) at (0.0001) school, (0.0002) home, (0.0001) camp (0.0003) and (0.0004) more. (0.0003) this (0.0015) package (-0.0001) contains (0.0000) 100 (0.0001) 6mm (-0.0000) x (0.0002) 12 (0.0001) " (-0.0004) stems. (0.0001) available (0.0005) in (0.0004) a (-0.0009) variety (-0.0000) of (0.0003) colors, (-0.0002) each (-0.0001) sold (0.0002) separately. (0.0005)
~~~~~~

**Node-1.7** (global 3307):

~~~~~~text
product (-0.0001) from (0.0001) amazon (-0.0005) platform (-0.0002) with (0.0003) title (-0.0004) and (0.0001) content (0.0005) : (0.0002) title (0.0002) : (0.0006) poptails (0.0001) : (0.0001) 60 (-0.0003) boozy (0.0005) treats (-0.0011) served (-0.0001) on (-0.0006) a (0.0001) stick. (-0.0004) content (0.0012) : (-0.0000) none (-0.0020)
~~~~~~

**Node-1.8** (global 3304):

~~~~~~text
product (-0.0003) from (-0.0001) amazon (0.0005) platform (0.0000) with (-0.0002) title (0.0002) and (0.0000) content (0.0002) : (0.0009) title (0.0000) : (0.0000) sargent (0.0007) art (0.0002) 22- (-0.0002) 1205 (0.0001) 1- (-0.0002) gallon (-0.0002) washable (-0.0002) school (-0.0000) glue. (0.0001) content (0.0001) : (0.0002) sargent (0.0002) art (-0.0002) school (-0.0002) glue (-0.0002) gallon (0.0001) is (0.0003) an (-0.0001) economical (0.0001) buy (-0.0000) for (-0.0001) the (-0.0000) classroom (0.0002) on (-0.0000) a (0.0002) budget. (-0.0002) it (-0.0001) ' (0.0001) s (-0.0002) washable (-0.0001) and (0.0001) ideal (-0.0000) for (-0.0001) young (-0.0001) students. (0.0001) ap (0.0001) certified (0.0001) ; (-0.0004) non- (0.0000) toxic (0.0001) and (-0.0000) safe. (0.0003) advanced (0.0001) formula (-0.0001) washes (-0.0001) from (-0.0001) most (-0.0001) surfaces. (0.0002) bonds (-0.0004) to (-0.0000) almost (0.0001) any (0.0001) porous (0.0000) surface. (0.0004) great (0.0002) for (-0.0000) both (-0.0001) children (0.0003) and (0.0000) adult (0.0001) crafters. (0.0002) use (-0.0003) at (0.0002) home, (-0.0001) in (-0.0001) the (0.0004) office (0.0003) or (-0.0001) in (0.0001) the (0.0006) classroom. (0.0002)
~~~~~~

**Node-1.9** (global 3301):

~~~~~~text
product (0.0053) from (0.0007) amazon (0.0027) platform (0.0004) with (0.0017) title (0.0038) and (0.0015) content (-0.0014) : (0.0007) title (0.0022) : (0.0016) bazic (-0.0012) natural (0.0011) craft (0.0034) sticks, (0.0027) wood, (-0.0001) 100 (0.0026) per (0.0028) pack. (0.0020) content (-0.0002) : (-0.0007) bazic (-0.0008) natural (0.0018) craft (0.0042) sticks (-0.0004) 160 (0.0006) per (-0.0008) pack (0.0035)
~~~~~~

**Node-2** (global 19311):

~~~~~~text
product (-0.0032) from (0.0153) amazon (0.0008) platform (-0.0167) with (0.0042) title (0.0109) and (-0.0041) content (-0.0027) : (0.0110) title (0.0125) : (0.0116) wilton (0.0027) mini (0.0039) muffin (0.0001) cups, (0.0052) 100 (0.0058) count. (0.0071) content (0.0035) : (-0.0006) wilton (-0.0041) baking (-0.0023) cups (0.0024) are (0.0158) ideal (-0.0024) for (0.0041) holding (0.0015) candy (-0.0084) and (-0.0048) nuts, (0.0032) too. (-0.0038)
~~~~~~

**Node-3** (global 19312):

~~~~~~text
product (0.0047) from (-0.0011) amazon (0.0076) platform (-0.0039) with (-0.0019) title (0.0073) and (0.0005) content (-0.0018) : (0.0001) title (0.0047) : (-0.0018) surebonder (-0.0002) dt- (0.0015) 25 (-0.0009) all (-0.0026) temperature (0.0011) mini (-0.0013) glue (-0.0053) sticks, (-0.0007) 4- (0.0003) inch. (-0.0025) content (-0.0025) : (-0.0055) surebonder (-0.0022) dt- (0.0036) 25 (0.0011) all (-0.0025) temperature (0.0022) mini (0.0005) glue (-0.0025) sticks (-0.0003) is (0.0080) an (-0.0013) all- (0.0014) temperature (0.0053) hot (0.0014) melt (-0.0015) adhesive (0.0025) that (0.0024) works (-0.0001) at (0.0030) either (0.0021) low (0.0022) temperature (0.0010) ( (0.0012) 230 (-0.0027) degrees (0.0065) f (-0.0096) ) (-0.0048) or (-0.0081) high (0.0016) temperature (0.0109) ( (0.0012) 380 (0.0019) degrees (0.0023) f (-0.0003) ) (0.0006) for (-0.0004) everyday (0.0016) gluing (0.0001) projects. (0.0001) use (0.0025) with (0.0081) high (-0.0017) or (0.0019) low (-0.0003) temperature (0.0038) glue (0.0060) guns. (0.0050) bonds (0.0075) to (0.0159) metal, (0.0009) wood, (0.0005) paper, (0.0015) fabric, (0.0020) magnets, (0.0008) ceramics, (-0.0011) floral (0.0044) arrangements, (0.0017) glass (0.0061) and (0.0016) plastic (0.0072) using (0.0032) a (0.0039) high (0.0046) temperature (0.0071) glue (0.0083) gun. (0.0063) bonds (0.0039) to (0.0114) delicate (0.0088) materials (0.0061) such (0.0034) as (0.0084) balloons, (0.0043) ribbon, (0.0021) lace (0.0036) and (0.0050) children (0.0017) ' (0.0016) s (0.0054) crafts (0.0066) using (0.0013) a (0.0019) low (-0.0012) temperature (0.0034) glue (-0.0050) gun. (-0.0003) clear (-0.0008) color (0.0036) with (0.0018) 60- (-0.0017) 65 (-0.0009) second (-0.0038) working (0.0017) time. (-0.0008) 5 (-0.0008) / (-0.0002) 16- (-0.0018) inch (-0.0034) diameter (0.0026) by (-0.0007) 4- (-0.0015) inch (-0.0018) length. (-0.0013) 25 (-0.0030) sticks (-0.0014) per (0.0008) bag. (0.0008)
~~~~~~

**Node-4** (global 19313):

~~~~~~text
product (0.0044) from (0.0011) amazon (-0.0030) platform (0.0011) with (0.0046) title (0.0021) and (-0.0000) content (0.0065) : (0.0035) title (0.0053) : (0.0037) northwest (-0.0066) enterprises (0.0055) hard (0.0000) plastic (0.0010) 2- (0.0032) ounce (-0.0011) shot (-0.0003) glasses, (0.0014) clear, (0.0012) 50 (0.0045) count. (-0.0120) content (0.0100) : (0.0000) get (0.0034) the (0.0018) party (0.0009) started (0.0066) with (0.0024) northwest (-0.0145) enterprises (0.0079) super (-0.0024) little (0.0054) 2- (0.0035) ounce (0.0016) shot (0.0008) glasses. (-0.0004) each (-0.0009) package (-0.0009) contains (0.0024) 50 (0.0026) crystal (0.0022) clear (0.0022) quality (0.0019) hard (0.0019) plastic (0.0018) glasses (0.0015) ideal (0.0025) for (0.0007) events, (0.0011) wine (-0.0001) tasting (-0.0006) parties, (0.0008) bachelorette (0.0015) parties (0.0003) or (0.0031) any (0.0023) occasion (0.0012) where (0.0047) friends (0.0027) gather (0.0001) to (0.0016) do (0.0020) a (-0.0005) wee (0.0048) bit (0.0018) of (0.0007) " (-0.0003) sipping. (-0.0001) " (-0.0013) so, (0.0012) whether (0.0036) it (0.0025) ' (0.0007) s (0.0041) a (-0.0002) wedding, (-0.0006) family (0.0014) picnic, (0.0009) simple (0.0068) neighborhood (0.0022) get (0.0064) together (0.0021) or (0.0043) easy- (0.0053) cleanup (0.0055) everyday (0.0064) use, (0.0032) choosing (0.0075) northwest (-0.0016) enterprises (0.0065) will (0.0032) help (0.0091) you (0.0075) to (0.0030) create (0.0059) the (-0.0002) perfect (0.0032) party (0.0023) at (0.0050) the (-0.0017) perfect (0.0055) price. (-0.0037) northwest (-0.0107) enterprises (0.0108) is (0.0063) a (0.0019) traditional (0.0094) family (0.0035) company (0.0056) with (0.0104) more (0.0056) than (0.0033) 25 (0.0007) years (0.0014) of (-0.0001) experience (0.0036) in (0.0020) party (-0.0030) supplies (0.0021) and (0.0034) food (0.0000) service (0.0038) disposables. (0.0010) through (0.0010) their (0.0028) dedication (0.0019) to (0.0004) the (0.0013) high (0.0011) quality (0.0069) of (0.0017) their (-0.0040) products (0.0037) and (0.0078) services, (0.0022) northwest (-0.0078) enterprises (0.0064) continues (0.0028) to (-0.0007) earn (0.0031) a (-0.0008) reputation (0.0072) as (0.0031) a (0.0028) leader (0.0013) in (0.0014) the (0.0015) party (0.0049) industry (0.0010) and (0.0025) the (-0.0013) trust (0.0011) and (0.0025) loyalty (0.0006) of (-0.0005) their (-0.0011) customers. (-0.0010)
~~~~~~

**Node-5** (global 19314):

~~~~~~text
product (-0.0028) from (0.0029) amazon (0.0156) platform (0.0042) with (-0.0017) title (0.0007) and (-0.0015) content (0.0100) : (-0.0002) title (-0.0018) : (0.0025) cindus (0.0009) cellophane (0.0044) wrap, (0.0012) 30- (0.0025) inch (0.0010) wide, (0.0017) 5- (0.0022) feet (-0.0027) roll, (0.0025) purple. (0.0079) content (0.0074) : (0.0007) cindus- (0.0029) cello (0.0078) wrap. (0.0067) transparent (0.0028) colored (0.0039) cello (0.0112) wrap (0.0069) perfect (0.0025) for (-0.0028) gift (0.0061) baskets (-0.0055) ; (-0.0012) gift (0.0063) bag (-0.0007) filler (0.0015) and (0.0011) more. (0.0008) this (0.0055) package (-0.0054) contains (-0.0076) one (-0.0028) 5ft (-0.0001) roll (0.0003) of (-0.0002) 30in (-0.0019) wrap. (0.0092) available (-0.0000) in (0.0041) a (-0.0201) variety (-0.0048) of (0.0024) colors (0.0012) : (-0.0053) each (-0.0022) sold (0.0024) separately. (-0.0055) imported. (0.0405)
~~~~~~

**Node-6** (global 19315):

~~~~~~text
product (0.0013) from (-0.0022) amazon (0.0022) platform (-0.0001) with (-0.0002) title (-0.0018) and (-0.0025) content (-0.0005) : (-0.0028) title (-0.0035) : (-0.0020) on (-0.0023) a (-0.0010) stick! (-0.0014) : (-0.0019) 80 (-0.0041) party- (-0.0011) perfect (-0.0031) recipes. (-0.0003) content (-0.0043) : (-0.0025) & (-0.0014) ldquo (-0.0002) ; (-0.0024) creative, (-0.0005) comprehensive, (0.0007) and (-0.0024) crammed (0.0003) with (-0.0015) full- (-0.0010) color (-0.0022) photos, (-0.0017) & (0.0001) # (0.0000) 160 (-0.0011) ; (0.0042) on (-0.0017) a (0.0022) stick!, (0.0020) by (-0.0016) matt (0.0000) armendariz, (-0.0015) is, (-0.0012) frankly, (-0.0012) the (-0.0011) most (-0.0019) awesome (-0.0034) cookbook (-0.0026) concept (-0.0009) we (-0.0013) & (0.0015) rsquo (-0.0015) ; (0.0023) ve (-0.0027) come (-0.0033) across (-0.0018) in (-0.0031) a (-0.0022) while (-0.0021) ( (-0.0021) and (-0.0035) maybe (-0.0028) ever (-0.0016) ). (0.0010) & (0.0010) rdquo (-0.0018) ; (0.0041) & (-0.0021) mdash (-0.0016) ; (0.0073) grandparents. (-0.0033) com (-0.0003) & (0.0020) ldquo (-0.0016) ; (0.0052) food (0.0010) blogger (-0.0032) and (-0.0060) professional (-0.0003) photographer (-0.0043) armendiaz (-0.0013) & (0.0004) rsquo (-0.0052) ; (0.0289) s (-0.0168) impressive (-0.0009) collection (-0.0002) of (-0.0027) stick- (-0.0014) mounted (0.0001) recipes (-0.0019) is (-0.0000) enough (0.0006) to (-0.0036) keep (-0.0038) county (-0.0060) fair (-0.0012) vendors (0.0010) in (-0.0011) business (-0.0024) for (-0.0015) at (-0.0005) least (-0.0008) another (-0.0025) decade. (0.0015) & (0.0030) rdquo (0.0006) ; (0.0019) & (-0.0008) mdash (0.0000) ; (0.0054) publishers (0.0017) weekly (0.0003) & (-0.0003) ldquo (-0.0009) ;... (-0.0010) a (-0.0012) wildly (-0.0026) inventive (-0.0014) take (-0.0001) on (-0.0022) finger (-0.0041) food. (-0.0015) & (0.0010) rdquo (-0.0007) ; (-0.0005) & (-0.0023) mdash (-0.0019) ; (0.0033) bay (0.0018) area (-0.0046) news (-0.0025) group (-0.0013) & (-0.0003) ldquo (-0.0014) ; (-0.0024) on (-0.0004) a (-0.0027) stick! (-0.0029) is (-0.0040) filled (-0.0036) with (-0.0015) surprising (-0.0040) and (-0.0026) exotic (-0.0035) nibbles (-0.0014) & (0.0013) mdash (-0.0023) ; (0.0015) kind (-0.0043) of (-0.0022) a (-0.0006) mash- (-0.0007) up (-0.0011) of (-0.0003) asian (-0.0034) street (-0.0015) food (-0.0011) and (-0.0020) state (-0.0017) fair (-0.0009) fare. (0.0011) & (-0.0007) rdquo (-0.0015) ; (0.0029) & (-0.0008) mdash (-0.0025) ; (0.0001) katherine (-0.0047) miller, (-0.0039) the (0.0115) oregonian (-0.0030)
~~~~~~
