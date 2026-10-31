# Reference packet: GraphNarrator__Llama-8B__products__47510

- Method: GraphNarrator; configuration: Llama-8B; dataset: products; target node: 47510
- Explanation source: `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/182.json` (messages[assistant])
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

- ROOT (console skin)
  - Node-1 (PlayStation 3 console skin)
    - Node-1.1 (3rd party controller)
    - Node-1.2 (accessory with adjustable settings)
    - Node-1.3 (PlayStation 3 controller charging dock)
    - Node-1.4 (Venezuela-related text)
    - Node-1.5 (Mortal Kombat game)
    - Node-1.6 (Need for Speed game)
    - Node-1.7 (PlayStation 3 bundle)

### Word-Level Evaluation

Keywords with high saliency scores in ROOT — "platform" (0.02), "title" (0.02), "content" (-0.00), "playstation" (0.01), "slim" (0.02), "console" (0.01) — are associated with gaming consoles. However, the presence of "amazon" (0.04) suggests an online marketplace context. The negative saliency scores for "product" (-0.01) and "content" (-0.00) indicate a lack of relevance to the product description.

### Graph-Level Aggregation

Node-1 (PlayStation 3 console skin, keywords: "playstation" (0.01), "slim" (0.02), "console" (0.01)) is a direct neighbor with moderate saliency, identifying a gaming console skin. Indirect neighbors — Node-1.1 (3rd party controller), Node-1.2 (accessory with adjustable settings), Node-1.3 (PlayStation 3 controller charging dock), Node-1.4 (Venezuela-related text), Node-1.5 (Mortal Kombat game), Node-1.6 (Need for Speed game), Node-1.7 (PlayStation 3 bundle) — are all related to gaming accessories or games, collectively confirming a gaming context across both hops.

### Free-Text Explanation

The classification of ROOT into "Books" is not strongly supported by its own keywords and the co-purchase neighborhood.

ROOT: Keywords like "platform" (0.02), "title" (0.02), and "console" (0.01) clearly identify this as a product related to gaming consoles, not books.
  - Node-1: A PlayStation 3 console skin (keywords: "playstation" (0.01), "slim" (0.02), "console" (0.01)) is a direct gaming console accessory, reinforcing the gaming context.
    - Node-1.1 ~ Node-1.7: A 3rd party controller, an accessory with adjustable settings, a PlayStation 3 controller charging dock, a Venezuela-related text, a Mortal Kombat game, a Need for Speed game, and a PlayStation 3 bundle are all related to gaming accessories or games, supporting the gaming category.

In summary, ROOT's own keywords strongly signal a gaming product, and the entire co-purchase neighborhood consists of gaming accessories or games, providing robust evidence for the "Electronics" or "Gaming" category, not "Books".
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/182.json`).

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
<verbalized-graph>ROOT: product(-0.01) amazon(0.04) platform(0.02) title(0.02) content(-0.00) title(0.01) missing.(0.01) content(0.01) listing(0.01) one(0.01) 1(0.01) playstation(0.01) 3(0.00) slim(0.02) console(0.01) skin(0.00) 2(0.01) constoller(0.02) skins(-0.01) displayed(0.02) above.(0.01) actual(0.03) controller(-0.01) included.(-0.00) skins(0.01) made(0.00) highest(0.01) quality(0.02) 3m(0.01) material.(0.02) proudly(0.01) made(0.01) 100(0.01) recycled(0.02) materials(0.02) usa!(0.01) vinyl(-0.00) skins(-0.00) sticker(-0.00) only.(0.01) hard(0.02) plastic(-0.00) cover(0.01) case!(0.04) sony(0.03) corporation(0.02) affiliated(0.04) with,(0.02) authorize(0.01) sponsor(0.02) products(0.02) sold(0.03) 247skins.(0.01) 
Node-1: product(0.09) amazon(0.02) platform(-0.04) title(0.09) content(0.03) title(0.06) missing.(0.11) content(0.04) mortal(-0.21) kombat(0.04) komplete(0.03) ps3(0.16) 
Node-1.1: product(-0.00) amazon(0.00) platform(-0.00) title(0.00) content(-0.00) title(0.00) missing.(0.00) content(0.00) 3rd(0.01) party,(0.00) good(-0.00) quality(-0.01) 
Node-1.2: product(-0.00) amazon(0.01) platform(-0.00) title(0.00) content(0.00) title(0.00) missing.(0.00) content(0.00) features(0.00) wide(0.01) range(0.00) adjustable(0.00) settings(0.00) various(0.00) flat-(0.00) panel(0.00) hdtv(0.00) shapesnote(0.00) accessory(0.00) only,(0.00) camera(-0.00) includedmaterial(0.00) plasticcolor(-0.00) blackpackage(0.01) included(-0.00) 1(0.00) x(0.01) mounting(0.01) bracket(0.01) ps-(0.00) eye(0.01) camera(0.02) ps3(-0.02) move(-0.02) 
Node-1.3: product(-0.00) amazon(0.00) platform(-0.00) title(0.00) content(-0.00) title(-0.00) missing.(0.00) content(-0.00) charges(0.00) stores(0.00) 4(0.00) original(0.00) sony(0.00) playstation(-0.00) 3(0.00) controllers(0.00) time.(0.00) features(0.01) custom(0.01) illumination(0.00) charging(0.00) includes(0.00) 110(0.00) 240(0.00) volt(0.00) ac(0.00) adapter.(0.00) 
Node-1.4: product(-0.00) amazon(-0.00) platform(0.00) title(0.00) content(-0.00) title(0.00) missing.(-0.00) content(0.00) venezuela(0.00) left(-0.00) state(0.00) civil(0.00) war(0.00) government(-0.00) brutally(0.00) overthrown(0.00) military(0.00) coup.(-0.00) factions(-0.00) fighting(0.00) reinstate(0.00) democracy,(-0.00) u.(0.01) s.(-0.00) government(0.00) offered(0.00) assistance,(0.00) though(0.00) new(0.00) government(0.00) regime(-0.00) threatened(0.00) deploy(0.00) nuclear(0.00) weapons(0.00) u.(0.00) s.(0.00) meddles(0.00) venezuelan(-0.00) affairs.(0.00) threat(-0.00) needs(0.00) neutralized,(0.00) u.(0.00) xbf(0.00) risk(0.00) nuclear(0.00) war.(0.00) cia(0.00) special(0.00) activities(-0.00) division(-0.00) operates(0.00) isolation(0.00) secrecy.(-0.00) captured,(0.00) link(0.00) u.(0.00) s.(0.00) government(-0.00) denied.(-0.00) conflict(-0.00) denied(0.00) ops(0.00) highly(0.00) accessible(-0.00) co-(-0.00) op(-0.00) fps(0.00) featuring(0.00) massive,(0.00) extremely(-0.00) explosive(-0.00) firefights(0.00) across(0.00) destructible(-0.00) environments.(-0.00) work(0.00) team(0.00) utilize(0.00) specific(0.00) skills(0.00) operative(0.00) experience(0.00) ultimate(0.00) destructive(0.00) satisfaction(-0.00) tons(0.00) exploding(-0.00) objects(0.00) endless(0.00) barrage(0.00) terrorists(0.00) begging(-0.00) blown(0.00) hell.(0.00) 
Node-1.5: product(0.00) amazon(-0.00) platform(-0.00) title(0.00) content(-0.00) title(0.01) missing.(-0.00) content(0.01) takes(0.01) netherrealm(0.00) studios(-0.00) bold(0.00) new(0.01) fighting(-0.00) game(0.00) enhances(0.00) 60(0.00) new(0.00) content(0.00) including(0.00) 6(0.00) new(0.00) characters,(-0.00) 30(0.00) new(-0.00) skins(-0.00) 60(-0.00) new(0.00) s.(0.00) t.(-0.00) a.(-0.00) r.(-0.00) labs(0.01) missions.(0.00) addition(0.00) new(0.00) characters(-0.00) brings(0.00) roster(0.00) 30(-0.00) fan(0.00) favorite(0.00) dc(-0.00) icons,(-0.01) including(0.00) batman,(-0.00) joker,(0.00) green(0.00) lantern,(-0.00) flash,(0.00) superman(-0.01) wonder(0.00) woman.(-0.01) heroes(-0.00) villains(-0.02) engage(0.00) epic(0.00) battles(-0.00) massive(0.00) scale(0.00) world(0.00) line(0.00) good(0.00) evil(-0.00) blurred.(0.00) 
Node-1.6: product(-0.00) amazon(-0.00) platform(-0.00) title(0.00) content(-0.00) title(0.00) missing.(-0.00) content(-0.00) need(-0.00) speed(-0.00) hot(0.00) pursuit(-0.00) players(0.00) experience(-0.00) thrill(0.00) chase(-0.00) rush(-0.00) escape(0.00) play(0.00) full(0.00) careers(0.00) cop(0.00) racer(0.00) 8211(-0.00) solo(0.00) connected.(0.00) blistering(0.00) speeds,(-0.00) brutal(0.00) busts(-0.00) heart-(0.00) stopping(0.00) getaways(0.00) connected(0.00) via(0.00) need(0.00) speed(-0.00) autolog.(0.00) network(0.00) connects(0.00) friends(0.00) epic(0.00) head-(0.00) head(-0.00) pursuits(0.00) races,(0.00) also(0.00) enables(0.00) players(0.00) compare(0.00) performances(0.01) stats,(0.00) thereby(-0.00) setting(0.00) stage(0.00) ultimate(0.01) friendly(0.01) competition.(0.00) 
Node-1.7: product(-0.00) amazon(-0.00) platform(-0.00) title(-0.00) content(-0.00) title(-0.00) missing.(0.00) content(-0.00) package(0.00) includes(-0.00) x2022(0.00) slim(0.00) 250gb(0.00) ps3(0.00) system(0.00) x1(0.00) x2022(0.00) playstation(-0.00) move(-0.00) controller(0.00) x1(0.00) x2022(0.00) playstation(-0.00) eye(-0.00) camera(0.00) x1(0.00) x2022(0.00) games(-0.00) eyepet(0.00) x1(0.00) sports(-0.00) champion(-0.00) x1(0.00) ps3(-0.00) move(-0.00) sports(-0.00) champions(-0.00) bundle(0.00) cech-(0.00) 4001b(0.00) eye(-0.00) pet(0.00) ps3(0.00) includes(0.00) slim(0.00) 250gb(0.00) ps3(0.00) game(0.00) system,(0.00) playstation(-0.00) move(0.00) controller,(0.00) playstation(0.00) eye(0.00) camera,(0.00) eyepet(0.00) sports(-0.00) champions(0.00) game.(-0.00) sports(-0.00) champions(0.00) game(0.00) makes(-0.00) actively(-0.00) competing(0.00) friends(-0.00) family(-0.00) fun.(0.00) play(-0.00) six(0.00) different(0.00) events,(-0.00) special(0.00) control(0.00) system.(0.00) ps3(0.00) move(-0.00) game(0.00) bundle(0.00) offers(0.00) 250</verbalized-graph>

### Classification Label
Books

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 47510
- Title: missing
- True class (canonical `y`): **label 25**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Video Games**
- Prediction recorded by this method's pipeline: **Books**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: missing. Content: This listing is for one (1) PlayStation 3 Slim Console skin and (2) Constoller Skins displayed above. Actual controller not included. All our skins are made from the highest quality 3M material. Proudly made from 100% recycled materials here in the USA! These are Vinyl skins "Sticker" ONLY. Not a hard plastic cover or case! Sony Corporation is not affiliated with, nor does it authorize or sponsor the products being sold by 247Skins.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 11442 | Video Games | missing |

### 2-hop (shortest distance exactly 2): 7 nodes

| node id | true class | title |
|---|---|---|
| 1376 | Video Games | missing |
| 1381 | Video Games | missing |
| 11393 | Video Games | missing |
| 11417 | Video Games | missing |
| 47507 | Toys & Games | missing |
| 47508 | Video Games | missing |
| 47509 | Video Games | missing |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/182.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Books**, ground truth = **label 25**.
The verbalized graph is 6482 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 47510 | 94 | 0.0449 | yes |
| Node-1 | 1 | 11442 | 18 | 0.1583 | yes |
| Node-1.1 | 2 | 1376 | 18 | 0.0084 | yes |
| Node-1.2 | 3 | 1381 | 49 | 0.0184 | yes |
| Node-1.3 | 4 | 11393 | 44 | 0.0059 | yes |
| Node-1.4 | 5 | 11417 | 164 | 0.0051 | yes |
| Node-1.5 | 6 | 47507 | 101 | 0.0106 | yes |
| Node-1.6 | 7 | 47508 | 103 | 0.0073 | yes |
| Node-1.7 | 8 | 47509 | 179 | 0.0026 | yes |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->Node-1.6, Node-1->Node-1.7, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, Node-1.6->Node-1, Node-1.7->Node-1, ROOT->Node-1

### Tokens and scores

**ROOT** (global 47510):

~~~~~~text
product (-0.0071) from (0.0005) amazon (0.0360) platform (0.0163) with (-0.0003) title (0.0213) and (0.0162) content (-0.0031) : (0.0078) title (0.0122) : (-0.0025) missing. (0.0093) content (0.0083) : (0.0138) this (0.0046) listing (0.0134) is (0.0156) for (0.0012) one (0.0091) ( (0.0084) 1 (0.0141) ) (0.0083) playstation (0.0090) 3 (0.0019) slim (0.0162) console (0.0148) skin (0.0046) and (0.0020) ( (0.0129) 2 (0.0108) ) (-0.0036) constoller (0.0204) skins (-0.0086) displayed (0.0218) above. (0.0086) actual (0.0284) controller (-0.0093) not (0.0070) included. (-0.0001) all (0.0143) our (-0.0113) skins (0.0131) are (0.0047) made (0.0045) from (0.0009) the (0.0008) highest (0.0108) quality (0.0161) 3m (0.0078) material. (0.0216) proudly (0.0107) made (0.0063) from (0.0038) 100 (0.0090) % (0.0253) recycled (0.0165) materials (0.0184) here (0.0109) in (0.0133) the (0.0042) usa! (0.0112) these (0.0146) are (0.0152) vinyl (-0.0042) skins (-0.0005) " (0.0199) sticker (-0.0012) " (0.0091) only. (0.0064) not (0.0082) a (-0.0011) hard (0.0200) plastic (-0.0020) cover (0.0111) or (-0.0112) case! (0.0396) sony (0.0321) corporation (0.0190) is (0.0085) not (-0.0043) affiliated (0.0449) with, (0.0215) nor (0.0212) does (0.0170) it (0.0124) authorize (0.0053) or (0.0011) sponsor (0.0178) the (-0.0019) products (0.0165) being (-0.0044) sold (0.0270) by (0.0039) 247skins. (0.0094)
~~~~~~

**Node-1** (global 11442):

~~~~~~text
product (0.0893) from (0.0884) amazon (0.0186) platform (-0.0361) with (0.0468) title (0.0853) and (0.0541) content (0.0302) : (0.0325) title (0.0576) : (0.1070) missing. (0.1070) content (0.0381) : (0.0880) mortal (-0.2060) kombat (0.0384) komplete (0.0266) ps3 (0.1583)
~~~~~~

**Node-1.1** (global 1376):

~~~~~~text
product (-0.0020) from (-0.0013) amazon (0.0040) platform (-0.0005) with (0.0010) title (0.0030) and (-0.0010) content (-0.0006) : (-0.0014) title (0.0006) : (0.0013) missing. (0.0032) content (0.0009) : (0.0009) 3rd (0.0084) party, (0.0001) good (-0.0027) quality (-0.0071)
~~~~~~

**Node-1.2** (global 1381):

~~~~~~text
product (-0.0003) from (0.0037) amazon (0.0132) platform (-0.0042) with (0.0035) title (0.0006) and (0.0030) content (0.0004) : (0.0058) title (0.0013) : (0.0049) missing. (0.0046) content (0.0017) : (0.0043) features (0.0011) a (0.0028) wide (0.0054) range (0.0047) of (0.0019) adjustable (0.0049) settings (0.0026) for (0.0036) various (0.0027) flat- (0.0026) panel (0.0043) hdtv (0.0042) shapesnote (0.0045) : (-0.0007) accessory (0.0028) only, (0.0041) camera (-0.0018) not (0.0035) includedmaterial (0.0010) : (0.0058) plasticcolor (-0.0018) : (0.0013) blackpackage (0.0055) included (-0.0046) : (-0.0041) 1 (0.0050) x (0.0059) mounting (0.0063) bracket (0.0110) for (-0.0032) ps- (0.0010) eye (0.0069) camera (0.0184) ps3 (-0.0165) move (-0.0194)
~~~~~~

**Node-1.3** (global 11393):

~~~~~~text
product (-0.0043) from (0.0028) amazon (0.0024) platform (-0.0006) with (0.0015) title (0.0040) and (0.0015) content (-0.0014) : (0.0020) title (-0.0024) : (0.0015) missing. (0.0044) content (-0.0008) : (0.0054) charges (0.0007) and (0.0000) stores (0.0020) up (0.0015) to (0.0017) 4 (0.0018) original (0.0008) sony (0.0008) playstation (-0.0030) 3 (0.0039) controllers (0.0002) at (0.0004) the (-0.0012) same (0.0012) time. (0.0026) features (0.0059) a (-0.0002) custom (0.0051) illumination (0.0015) while (0.0018) charging (0.0038) and (0.0032) includes (0.0010) a (0.0012) 110 (0.0006) / (0.0042) 240 (0.0006) volt (0.0010) ac (0.0039) adapter. (0.0006)
~~~~~~

**Node-1.4** (global 11417):

~~~~~~text
product (-0.0001) from (0.0013) amazon (-0.0024) platform (0.0026) with (0.0019) title (0.0029) and (0.0041) content (-0.0006) : (0.0003) title (0.0027) : (0.0019) missing. (-0.0038) content (0.0045) : (-0.0036) venezuela (0.0010) is (0.0001) left (-0.0013) in (0.0013) a (0.0001) state (0.0008) of (0.0013) civil (0.0013) war (0.0011) after (0.0011) the (-0.0005) government (-0.0003) was (0.0013) brutally (0.0002) overthrown (0.0003) by (0.0016) a (0.0003) military (0.0011) coup. (-0.0006) with (0.0008) factions (-0.0012) fighting (0.0007) to (0.0012) reinstate (0.0007) democracy, (-0.0003) the (-0.0021) u. (0.0051) s. (-0.0039) government (0.0022) has (0.0011) offered (0.0050) their (0.0007) assistance, (0.0001) though (0.0029) the (-0.0007) new (0.0021) government (0.0000) regime (-0.0005) has (0.0009) threatened (0.0010) to (0.0020) deploy (0.0008) nuclear (0.0008) weapons (0.0006) if (0.0014) the (-0.0015) u. (0.0008) s. (0.0013) meddles (0.0022) in (0.0013) venezuelan (-0.0021) affairs. (0.0007) the (-0.0015) threat (-0.0008) needs (0.0003) to (0.0030) be (0.0008) neutralized, (0.0016) and (0.0024) the (-0.0010) u. (0.0005) s (0.0019) can (0.0005) & (0.0048) # (0.0028) xbf (0.0017) ; (0.0038) t (0.0012) risk (0.0015) nuclear (0.0009) war. (0.0036) the (0.0000) cia (0.0022) special (0.0008) activities (-0.0016) division (-0.0009) operates (0.0023) in (0.0003) isolation (0.0007) and (0.0034) secrecy. (-0.0007) if (0.0010) captured, (0.0015) any (0.0023) link (0.0021) with (0.0019) the (-0.0005) u. (0.0007) s. (0.0010) government (-0.0007) will (0.0007) be (0.0042) denied. (-0.0016) conflict (-0.0042) : (-0.0046) denied (0.0019) ops (0.0022) is (-0.0018) a (-0.0032) highly (0.0026) accessible (-0.0006) co- (-0.0004) op (-0.0021) fps (0.0019) featuring (0.0030) massive, (0.0012) extremely (-0.0016) explosive (-0.0004) firefights (0.0010) across (0.0020) destructible (-0.0001) environments. (-0.0026) work (0.0006) as (0.0020) a (0.0007) team (0.0035) to (0.0014) utilize (0.0003) the (-0.0014) specific (0.0025) skills (0.0019) of (0.0007) each (0.0025) operative (0.0008) and (0.0017) experience (0.0018) the (0.0003) ultimate (0.0018) in (-0.0009) destructive (0.0022) satisfaction (-0.0014) with (0.0009) tons (0.0013) of (0.0022) exploding (-0.0028) objects (0.0003) and (0.0023) an (0.0002) endless (0.0010) barrage (0.0003) of (0.0009) terrorists (0.0008) who (0.0021) are (0.0004) begging (-0.0008) to (0.0024) be (0.0007) blown (0.0012) to (0.0017) hell. (0.0045)
~~~~~~

**Node-1.5** (global 47507):

~~~~~~text
product (0.0039) from (0.0010) amazon (-0.0021) platform (-0.0019) with (0.0084) title (0.0034) and (0.0031) content (-0.0013) : (0.0020) title (0.0064) : (0.0077) missing. (-0.0047) content (0.0086) : (0.0106) takes (0.0053) netherrealm (0.0023) studios (-0.0019) ' (0.0031) bold (0.0003) new (0.0065) fighting (-0.0009) game (0.0041) and (0.0054) enhances (0.0001) it (0.0013) with (0.0028) over (0.0041) $ (0.0009) 60 (0.0021) of (0.0029) new (0.0005) content (0.0024) including (0.0005) 6 (0.0010) new (0.0008) characters, (-0.0005) over (0.0023) 30 (0.0016) new (-0.0008) skins (-0.0022) and (0.0025) 60 (-0.0019) new (0.0025) s. (0.0007) t. (-0.0000) a. (-0.0002) r. (-0.0010) labs (0.0053) missions. (0.0005) the (-0.0029) addition (0.0003) of (0.0017) the (0.0005) new (0.0009) characters (-0.0012) brings (0.0015) the (-0.0052) roster (0.0033) to (0.0011) 30 (-0.0003) fan (0.0041) favorite (0.0005) dc (-0.0012) icons, (-0.0055) including (0.0035) batman, (-0.0022) the (0.0014) joker, (0.0012) green (0.0045) lantern, (-0.0007) the (-0.0002) flash, (0.0017) superman (-0.0087) and (0.0055) wonder (0.0046) woman. (-0.0061) heroes (-0.0030) and (0.0106) villains (-0.0165) will (0.0009) engage (0.0017) in (0.0037) epic (0.0032) battles (-0.0026) on (0.0074) a (0.0033) massive (0.0031) scale (0.0037) in (0.0049) a (0.0036) world (0.0003) where (0.0076) the (-0.0033) line (0.0017) between (0.0044) good (0.0019) and (0.0008) evil (-0.0025) has (-0.0005) been (0.0020) blurred. (0.0019)
~~~~~~

**Node-1.6** (global 47508):

~~~~~~text
product (-0.0039) from (-0.0025) amazon (-0.0005) platform (-0.0011) with (-0.0002) title (0.0037) and (0.0018) content (-0.0015) : (0.0004) title (0.0024) : (0.0026) missing. (-0.0004) content (-0.0008) : (0.0024) need (-0.0017) for (-0.0008) speed (-0.0001) hot (0.0023) pursuit (-0.0002) players (0.0019) will (-0.0004) experience (-0.0003) the (-0.0008) thrill (0.0002) of (0.0006) the (-0.0014) chase (-0.0002) and (0.0013) the (-0.0006) rush (-0.0001) of (0.0007) the (0.0004) escape (0.0006) as (0.0013) they (-0.0005) play (0.0005) through (-0.0005) full (0.0005) careers (0.0015) as (0.0009) both (0.0000) a (-0.0000) cop (0.0023) and (0.0013) a (0.0009) racer (0.0032) & (-0.0014) # (0.0015) 8211 (-0.0016) ; (0.0018) solo (0.0017) or (0.0031) connected. (0.0022) the (-0.0041) blistering (0.0006) speeds, (-0.0002) brutal (0.0024) busts (-0.0001) and (0.0000) heart- (0.0005) stopping (0.0002) getaways (0.0004) are (0.0019) all (-0.0003) connected (0.0009) via (0.0004) need (0.0005) for (0.0005) speed (-0.0012) autolog. (0.0009) this (0.0009) network (0.0038) not (-0.0011) only (-0.0023) connects (0.0049) friends (0.0020) for (0.0014) epic (0.0034) head- (0.0002) to (0.0022) head (-0.0005) pursuits (0.0003) and (0.0010) races, (0.0011) but (0.0037) also (0.0028) enables (0.0014) players (0.0046) to (0.0015) compare (0.0015) performances (0.0051) and (0.0005) stats, (0.0032) thereby (-0.0047) setting (0.0029) the (0.0000) stage (0.0037) for (0.0017) the (-0.0010) ultimate (0.0063) in (0.0063) friendly (0.0073) competition. (0.0036)
~~~~~~

**Node-1.7** (global 47509):

~~~~~~text
product (-0.0006) from (-0.0004) amazon (-0.0001) platform (-0.0017) with (-0.0005) title (-0.0003) and (-0.0001) content (-0.0008) : (0.0004) title (-0.0002) : (0.0004) missing. (0.0009) content (-0.0011) : (0.0002) package (0.0002) includes (-0.0001) : (-0.0001) & (-0.0001) # (-0.0002) x2022 (0.0004) ; (0.0008) slim (0.0004) 250gb (0.0004) ps3 (0.0004) system (0.0005) x1 (0.0002) & (-0.0005) # (0.0000) x2022 (0.0005) ; (-0.0000) playstation (-0.0015) move (-0.0007) controller (0.0000) x1 (0.0002) & (-0.0007) # (0.0000) x2022 (0.0002) ; (0.0002) playstation (-0.0016) eye (-0.0006) camera (0.0000) x1 (0.0000) & (-0.0006) # (0.0003) x2022 (0.0003) ; (0.0003) games (-0.0009) : (-0.0007) eyepet (0.0000) x1 (0.0003) and (0.0000) sports (-0.0005) champion (-0.0000) x1 (0.0002) the (-0.0004) ps3 (-0.0001) move (-0.0009) sports (-0.0003) champions (-0.0022) bundle (0.0014) ( (-0.0023) cech- (0.0003) 4001b (0.0003) ) (0.0001) with (-0.0002) eye (-0.0004) pet (0.0004) ( (0.0008) ps3 (0.0008) ) (0.0008) includes (0.0012) the (0.0014) slim (0.0018) 250gb (0.0011) ps3 (0.0007) game (0.0017) system, (0.0003) a (0.0010) playstation (-0.0001) move (0.0014) controller, (0.0004) a (0.0011) playstation (0.0001) eye (0.0011) camera, (0.0006) an (0.0005) eyepet (0.0004) and (0.0013) the (0.0016) sports (-0.0001) champions (0.0023) game. (-0.0016) the (0.0012) sports (-0.0003) champions (0.0020) game (0.0021) makes (-0.0006) actively (-0.0011) competing (0.0020) with (-0.0003) your (-0.0004) friends (-0.0016) or (0.0008) family (-0.0014) fun. (0.0016) play (-0.0006) through (-0.0004) six (0.0002) different (0.0009) events, (-0.0000) each (-0.0001) with (0.0003) its (0.0003) own (-0.0001) special (0.0001) control (0.0001) system. (0.0011) the (0.0014) ps3 (0.0010) move (-0.0003) game (0.0008) bundle (0.0016) offers (0.0007) 250 (-0.0003) gb (-0.0001) of (-0.0003) hard (0.0005) drive (0.0001) space (0.0011) to (-0.0001) save (0.0001) your (-0.0008) favorite (0.0004) gaming (-0.0004) moments, (0.0003) along (0.0004) with (-0.0001) movies (-0.0002) and (-0.0004) music. (-0.0001) with (-0.0005) the (0.0009) included (-0.0004) eyepet, (0.0005) you (-0.0004) can (-0.0000) use (0.0010) the (0.0005) playstation (-0.0006) eye (0.0016) camera (-0.0002) and (0.0005) ps3 (0.0003) move (0.0013) console (0.0007) to (0.0004) project (0.0009) your (0.0009) own (0.0000) eyepet (0.0011) for (-0.0002) interactive (-0.0002) game (0.0003) play. (-0.0010) the (-0.0002) ps3 (-0.0001) move (0.0004) sports (0.0010) champions (0.0005) bundle (0.0003) will (0.0026) provide (0.0014) hours (-0.0004) of (-0.0008) game (0.0006) play (0.0013) and (-0.0006) physical (0.0015) activity. (-0.0005)
~~~~~~
