# Reference packet: GraphNarrator__Llama-70B__products__32390

- Method: GraphNarrator; configuration: Llama-70B; dataset: products; target node: 32390
- Explanation source: `./robustness_2026-10-30/llama70b/graphnarrator/products/32390.json` (response)
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

- ROOT (mini knife)
  - Node-1 (folding knife)
    - Node-1.1 (assisted opening clip knife)
    - Node-1.2 (lockback pocket knife)
    - Node-1.3 (folding hunter)
    - Node-1.4 (mid lock back style knife)

1. Word-Level Evaluation:

Keywords with high saliency scores in ROOT — "knife" (-0.01), "mini" (0.01), "gerber" (0.00), "paraframe" (0.00), "blade" (0.00) — are strongly associated with knives. However, the classification label is "Beauty", which seems unrelated to knives. Upon closer inspection, the importance scores of these keywords are relatively low, indicating that they may not be the primary drivers of the classification.

2. Graph-Level Aggregation:

Node-1 (folding knife, keywords: "knife" (-0.00), "gerber" (-0.00), "lst" (-0.01)) and its children (Node-1.1, Node-1.2, Node-1.3, Node-1.4) are all related to knives, but none of them have keywords that are strongly associated with beauty. However, the lack of strong keywords in the ROOT node and the presence of a large number of nodes related to knives may indicate that the classification label is not driven by the content of the nodes, but rather by some other factor.

### Free-Text Explanation
```markdown
The classification of ROOT into "Beauty" is not immediately clear from the keywords and co-purchase neighborhood.

ROOT: Keywords like "knife" (-0.01), "mini" (0.01), and "gerber" (0.00) are associated with knives, but their low importance scores suggest that they may not be the primary drivers of the classification.
  - Node-1: A folding knife (keywords: "knife" (-0.00), "gerber" (-0.00), "lst" (-0.01)) is a direct neighbor, but its keywords do not provide any insight into the "Beauty" classification.
    - Node-1.1: An assisted opening clip knife (keywords: "swagger" (0.01), "assisted" (0.00), "opening" (0.01)) is a child of Node-1, but its keywords are also unrelated to beauty.
    - Node-1.2: A lockback pocket knife (keywords: "case" (0.00), "cutlery" (-0.00), "executive" (0.01)) is another child of Node-1, but its keywords do not provide any insight into the "Beauty" classification.
    - Node-1.3: A folding hunter (keywords: "buck" (0.01), "55" (0.01), "folding" (0.01)) is a child of Node-1, but its keywords are also unrelated to beauty.
    - Node-1.4: A mid lock back style knife (keywords: "bantam" (-0.00), "bbw" (-0.00), "buck" (0.00)) is a child of Node-1, but its keywords do not provide any insight into the "Beauty" classification.

In summary, the classification of ROOT into "Beauty" is not supported by the keywords and co-purchase neighborhood. It is possible that the classification is driven by some other factor, such as the product's packaging or marketing, that is not reflected in the verbalized graph.
```
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/117.json`).

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
<verbalized-graph>ROOT: product(-0.00) amazon(0.00) platform(0.01) title(0.01) content(0.01) title(0.00) gerber(-0.00) paraframe(0.00) mini(0.01) knife.(-0.01) content(0.01) let(0.01) 3-(-0.00) inch(-0.00) folded(0.00) size(0.01) mini(-0.00) fool(0.00) gerber(0.00) gives(-0.01) little(0.01) guy(-0.00) attention(0.00) detail(0.01) larger(0.01) paraframe(0.01) models(0.00) dedicated(0.00) following.(-0.00) notice(0.01) ergonomic(0.00) metal(0.00) handle(0.00) frame(0.00) lock(-0.00) design,(0.01) delivers(0.01) positive(0.02) blade(-0.00) engagement(0.01) balanced(0.00) feel,(0.00) even(0.01) size.(0.02) features(0.02) :-(-0.00) tanto-(0.01) style(-0.01) blade-(0.00) black(-0.00) titanium(-0.00) nitride-(0.00) coated(0.01) blade-(0.01) full(0.00) fine(0.01) edge(0.02) blade(0.00) easy(0.01) sharpen-(0.01) frame(0.01) lock-(0.01) pocket(0.02) clip-(0.00) small(0.02) size(0.01) disappears(0.00) pocket(-0.00) specifications(0.05) :-(-0.00) overall(0.01) length(0.00) 5.(0.01) 25(0.01) 13.(0.00) 34(0.00) cm(0.00) )-(-0.00) blade(-0.01) length(0.00) 2.(0.00) 13(0.01) 5.(-0.00) 41(0.00) cm(0.00) )-(-0.01) closed(0.01) length(0.01) 3.(0.00) 13(0.00) 7.(0.00) 95(-0.00) cm(0.00) )-(-0.00) weight(0.01) 1.(0.00) 5(0.01) oz.(0.01) 43(-0.00) g(0.00) )-(-0.00) steel(0.01) type(0.00) 7cr17mov-(-0.00) handle(0.02) material(0.01) 3cr13.(-0.00) 
Node-1: product(0.00) amazon(0.01) platform(-0.00) title(-0.00) content(-0.01) title(-0.01) gerber(-0.00) lst(-0.01) folding(-0.02) knife(-0.00) 22-(-0.01) 06009.(0.00) content(-0.00) knife(-0.00) mighty(-0.01) impressive(-0.02) roots.(-0.01) brought(-0.02) market(0.01) back(-0.02) 1980(0.01) none(-0.02) man(-0.01) whose(-0.02) last(-0.00) name(-0.02) goes(-0.01) products.(-0.01) pete(0.01) gerber(-0.01) first(-0.00) knife(-0.01) creator(-0.03) envision(-0.01) merits(-0.02) using(-0.01) all-(-0.01) synthetic(-0.02) materials(-0.01) handle.(-0.01) knife(0.01) designer(-0.06) blackie(0.01) collins(0.00) aimed(-0.01) deliver(-0.00) lightweight(-0.02) performance(-0.04) seen(-0.01) knife(-0.00) all-(-0.00) rugged.(0.00) 
Node-1.1: product(0.01) amazon(0.02) platform(0.00) title(0.00) content(0.01) title(0.01) gerber(0.00) 31-(0.00) 001709(0.00) swagger(0.01) assisted(0.00) opening(0.01) clip(-0.00) knife.(0.00) content(0.01) updated(0.00) version(0.00) original(0.00) swagger,(0.00) swagger(0.00) ao(0.00) features(0.00) gerber(-0.00) new(0.00) assisted(0.00) opening(0.00) 2.(0.00) 0(0.01) mechanism,(-0.00) provides(0.01) ultra-(0.00) quick(0.00) blade(0.00) deployment.(0.00) g-(0.01) 10(0.01) handle(0.01) sc(0.00) ales(0.00) offer(0.01) excellent(0.01) grip(0.01) surface.(-0.01) black(0.01) coated(0.01) drop-(0.01) point(0.01) blade(0.00) features(-0.00) partial(0.00) serrations,(0.01) making(0.01) swagger(0.01) ao(0.01) great(0.01) every-(0.01) day-(0.01) carry(0.00) tactical(0.01) knife.(-0.00) 
Node-1.2: product(0.00) amazon(0.00) platform(0.00) title(0.00) content(-0.00) title(0.00) case(0.00) cutlery(-0.00) 004(0.00) case(0.00) executive(0.01) lockback(0.00) pocket(0.00) knife(-0.00) stainless(-0.00) steel(0.00) blade(0.00) metal.(0.00) content(0.00) 004(0.00) case(-0.00) executive(0.00) lockback(0.00) features(0.00) brushed(-0.00) stainless(-0.00) steel(0.00) handle(0.00) tru-(0.00) sharp(0.00) surgical(-0.00) steel(0.00) drop(0.00) point(0.00) blade.(-0.00) 3(0.00) 1(0.00) 8(0.00) closed,(0.00) weighing(-0.00) 1.(0.00) 0(-0.00) oz.,(0.00) slim(0.00) design(0.00) perfect(0.00) suit-(0.00) pocket,(0.00) purse(-0.00) key(0.00) ring.(0.00) blade(0.00) skillfully(0.00) honed(0.00) polished(-0.00) razor(0.00) x2019(0.00) edge,(0.00) measures(0.00) 2(0.00) xbc(0.00) x201d(0.00) locks(0.00) added(0.00) confidence.(0.00) backed(0.00) case(-0.00) x2019(0.00) limited(0.00) lifetime(0.00) warranty,(0.00) executive(-0.01) lockback(-0.00) makes(-0.00) ideal(-0.00) gift.(0.00) specifications(-0.00) x2022(0.00) pattern(0.00) m1059l(0.00) ss(0.00) x2022(0.00) handle(-0.00) material(0.00) brushed(-0.00) stainless(-0.00) steel(0.00) x2022(0.00) blade(-0.00) locking(0.00) drop(0.00) point(0.00) x2022(0.00) blade(0.00) material(0.00) tru-(0.00) sharp(0.00) surgical(-0.00) steel(0.00) x2022(0.00) length(0.00) closed(0.00) 3(0.00) 1(0.00) 8(-0.00) x201d(0.00) x2022(0.00) weight(0.00) 1.(0.00) 0(0.00) oz.(-0.00) w.(0.00) r.(0.00) case(0.00) sons(-0.00) cutlery(-0.00) co.(0.00) w.(0.00) r.(0.00) case(-0.00) sons(0.00) cutlery(-0.00) company(0.00) leading(0.00) american(-0.00) manufacturer(0.00) premium,(0.00) hand-(0.00) crafted(0.00) knives(-0.00) century.(-0.00) still(-0.00) manufactured(0.00) bradford,(0.00) pennsylvania(0.00) skilled(0.00) artisans(0.00) using(0.00) finest(-0.00) materials(0.00) time-(0.00) honored(-0.00) techniques(0.00) x2013(0.00) rich(-0.00) heritage(-0.00) makes(-0.00) case(0.00) knives(-0.01) brand(-0.00) choice(0.00) sportsmen(0.00) knife(-0.00) enthusiasts,(0.00) well(0.00) collected(0.01) knives(-0.00) world.(0.00) hunting(0.00) pocket(-0.00) knives(-0.00) v-(0.00) 42(0.00) stiletto(0.00) carried(0.00) u.(0.00) s.(-0.00) army(0.00) soldiers(0.00) world(0.00) war(0.00) ii,(-0.00) m-(0.00) 1(0.00) astronauts(-0.00) knife(-0.00) carried(-0.00) gemini(0.00) apollo(-0.00) missions,(-0.00) case(0.00) knives(-0.00) trusted(0.00) 
Node-1.3: product(0.01) amazon(0.02) platform(-0.00) title(0.01) content(0.01) title(0.01) buck(0.01) 55(0.01) folding(0.01) hunter.(0.01) content(0.02) none(-0.01) 
Node-1.4: product(-0.00) amazon(-0.00) platform(0.00) title(0.00) content(-0.00) title(-0.00) bantam(-0.00) bbw.(0.00) content(-0.00) really(-0.00) need(-0.00) anything(0.00) bew(0.00) bantam(0.00) bbw(-0.00) buck(0.00) knives?(-0.00) think(-0.00) so.(0.00) lightweight,(0.00) mid(0.00) lock(0.00) back(0.00) style,(0.00) knife(0.00) pocket(0.00) day(0.00) day(0.00) out.(-0.00) bantam(0.00) around(-0.00) american(-0.00) need.(-0.00) product(-0.00) features(0.00) small(0.00) size,(0.00) lightweight,(0.00) mid-(0.00) lockback(0.00) knife(0.00) 1-(0.00) hand(0.00) open(0.00) contoured(0.00) finger(0.0</verbalized-graph>

### Classification Label
Beauty

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 32390
- Title: Gerber Paraframe Mini Knife
- True class (canonical `y`): **Sports & Outdoors**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Sports & Outdoors**
- Prediction recorded by this method's pipeline: **Beauty**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Gerber Paraframe Mini Knife. Content: Don't let the 3-inch folded size of the Mini fool you; Gerber gives this little guy the same attention to detail that has won the larger Paraframe models a dedicated following. You'll notice the same ergonomic metal handle and frame lock design, and it delivers the same positive blade engagement and balanced feel, even at this size. Features: - Tanto-style blade - Black titanium nitride-coated blade - Full fine edge blade is easy to sharpen - Frame lock - Pocket clip - Small size disappears in your pocket Specifications: - Overall Length: 5.25" (13.34 cm) - Blade Length: 2.13" (5.41 cm) - Closed Length: 3.13" (7.95 cm) - Weight: 1.5 oz. (43 g) - Steel Type: 7Cr17MoV - Handle Material: 3Cr13.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 7041 | Tools & Home Improvement | Gerber LST Folding Knife 22-06009 |

### 2-hop (shortest distance exactly 2): 5 nodes

| node id | true class | title |
|---|---|---|
| 822 | Tools & Home Improvement | Gerber 31-001709 Swagger Assisted Opening Clip Knife |
| 32389 | Sports & Outdoors | Case Cutlery 004 Case Executive Lockback Pocket Knife With Stainless Steel Blade   Metal |
| 32391 | Sports & Outdoors | Buck 55 Folding Hunter |
| 32392 | Sports & Outdoors | Bantam BBW |
| 32393 | Sports & Outdoors | Gerber 31-001088 Myth Pocket Folder, Fine Edge Folding Lock-Back Clip Knife |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/117.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Beauty**, ground truth = **Sports & Outdoors**.
The verbalized graph is 9069 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 32390 | 160 | 0.0468 | yes |
| Node-1 | 1 | 7041 | 96 | 0.0259 | yes |
| Node-1.1 | 2 | 822 | 78 | 0.0165 | yes |
| Node-1.2 | 3 | 32389 | 304 | 0.0084 | yes |
| Node-1.3 | 4 | 32391 | 18 | 0.0246 | yes |
| Node-1.4 | 5 | 32392 | 256 | 0.0047 | yes |
| Node-1.5 | 6 | 32393 | 99 | 0.0300 | no |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, ROOT->Node-1

### Tokens and scores

**ROOT** (global 32390):

~~~~~~text
product (-0.0050) from (-0.0060) amazon (0.0049) platform (0.0103) with (-0.0093) title (0.0065) and (0.0026) content (0.0054) : (0.0052) title (0.0050) : (0.0028) gerber (-0.0027) paraframe (0.0033) mini (0.0094) knife. (-0.0119) content (0.0086) : (0.0000) don (-0.0035) ' (-0.0006) t (0.0028) let (0.0054) the (0.0056) 3- (-0.0001) inch (-0.0023) folded (0.0002) size (0.0064) of (0.0015) the (0.0060) mini (-0.0012) fool (0.0044) you (0.0029) ; (0.0391) gerber (0.0040) gives (-0.0085) this (-0.0003) little (0.0052) guy (-0.0004) the (0.0003) same (-0.0018) attention (0.0039) to (0.0042) detail (0.0087) that (0.0056) has (0.0055) won (-0.0046) the (0.0083) larger (0.0116) paraframe (0.0061) models (0.0041) a (0.0058) dedicated (0.0047) following. (-0.0047) you (0.0078) ' (-0.0013) ll (0.0046) notice (0.0078) the (0.0069) same (0.0021) ergonomic (0.0022) metal (0.0024) handle (0.0013) and (0.0010) frame (0.0038) lock (-0.0005) design, (0.0074) and (0.0029) it (0.0045) delivers (0.0079) the (0.0003) same (0.0036) positive (0.0167) blade (-0.0049) engagement (0.0122) and (0.0054) balanced (0.0049) feel, (0.0039) even (0.0094) at (0.0103) this (0.0006) size. (0.0176) features (0.0165) :- (-0.0013) tanto- (0.0094) style (-0.0104) blade- (0.0013) black (-0.0001) titanium (-0.0003) nitride- (0.0025) coated (0.0137) blade- (0.0070) full (0.0040) fine (0.0088) edge (0.0196) blade (0.0034) is (0.0056) easy (0.0097) to (-0.0002) sharpen- (0.0065) frame (0.0081) lock- (0.0089) pocket (0.0157) clip- (0.0011) small (0.0169) size (0.0056) disappears (0.0027) in (0.0041) your (0.0017) pocket (-0.0025) specifications (0.0468) :- (-0.0013) overall (0.0097) length (0.0010) : (0.0052) 5. (0.0082) 25 (0.0073) " (-0.0132) ( (-0.0016) 13. (0.0003) 34 (0.0023) cm (0.0016) )- (-0.0005) blade (-0.0069) length (0.0025) : (0.0039) 2. (0.0045) 13 (0.0074) " (-0.0057) ( (0.0020) 5. (-0.0020) 41 (0.0021) cm (0.0009) )- (-0.0061) closed (0.0090) length (0.0110) : (-0.0023) 3. (0.0045) 13 (0.0021) " (-0.0015) ( (-0.0020) 7. (0.0005) 95 (-0.0007) cm (0.0003) )- (-0.0020) weight (0.0082) : (0.0015) 1. (0.0042) 5 (0.0068) oz. (0.0062) ( (-0.0051) 43 (-0.0001) g (0.0034) )- (-0.0049) steel (0.0087) type (0.0029) : (-0.0031) 7cr17mov- (-0.0005) handle (0.0226) material (0.0094) : (0.0060) 3cr13. (-0.0026)
~~~~~~

**Node-1** (global 7041):

~~~~~~text
product (0.0043) from (-0.0165) amazon (0.0074) platform (-0.0025) with (-0.0033) title (-0.0044) and (-0.0129) content (-0.0085) : (-0.0012) title (-0.0065) : (0.0002) gerber (-0.0014) lst (-0.0100) folding (-0.0211) knife (-0.0042) 22- (-0.0085) 06009. (0.0018) content (-0.0018) : (-0.0218) now (-0.0108) here (-0.0108) ' (-0.0129) s (0.0006) a (-0.0036) knife (-0.0003) with (-0.0192) some (-0.0072) mighty (-0.0140) impressive (-0.0236) roots. (-0.0057) it (-0.0176) was (-0.0145) brought (-0.0218) to (-0.0135) market (0.0074) back (-0.0172) in (-0.0055) 1980 (0.0145) by (-0.0143) none (-0.0212) other (-0.0064) than (-0.0100) the (-0.0173) man (-0.0124) whose (-0.0156) last (-0.0001) name (-0.0223) goes (-0.0123) on (-0.0174) each (-0.0081) of (-0.0034) our (-0.0169) products. (-0.0051) pete (0.0051) gerber (-0.0061) was (-0.0194) the (-0.0007) first (-0.0031) knife (-0.0121) creator (-0.0316) to (0.0043) envision (-0.0119) the (0.0079) merits (-0.0177) of (-0.0079) using (-0.0099) all- (-0.0077) synthetic (-0.0187) materials (-0.0073) in (-0.0107) the (0.0259) handle. (-0.0143) he (0.0092) and (0.0113) knife (0.0148) designer (-0.0639) blackie (0.0066) collins (0.0015) aimed (-0.0059) to (0.0037) deliver (-0.0035) lightweight (-0.0185) performance (-0.0380) that (-0.0008) had (-0.0077) not (-0.0031) been (0.0032) seen (-0.0126) before (-0.0000) in (-0.0184) a (-0.0042) knife (-0.0041) this (-0.0274) all- (-0.0023) out (-0.0140) rugged. (0.0012)
~~~~~~

**Node-1.1** (global 822):

~~~~~~text
product (0.0061) from (-0.0019) amazon (0.0165) platform (0.0021) with (-0.0021) title (0.0028) and (0.0011) content (0.0096) : (-0.0010) title (0.0082) : (0.0051) gerber (0.0031) 31- (0.0028) 001709 (0.0037) swagger (0.0088) assisted (0.0012) opening (0.0054) clip (-0.0036) knife. (0.0024) content (0.0089) : (0.0036) an (-0.0002) updated (0.0020) version (0.0050) of (-0.0016) the (-0.0020) original (0.0030) swagger, (0.0021) the (0.0015) swagger (0.0015) ao (0.0021) features (0.0020) gerber (-0.0003) ' (-0.0001) s (0.0012) new (0.0008) assisted (0.0044) opening (0.0029) 2. (0.0027) 0 (0.0061) mechanism, (-0.0008) which (0.0031) provides (0.0060) ultra- (0.0041) quick (0.0033) blade (0.0033) deployment. (0.0020) the (0.0005) g- (0.0071) 10 (0.0062) handle (0.0050) sc (0.0000) ales (0.0048) offer (0.0072) an (0.0025) excellent (0.0060) grip (0.0059) surface. (-0.0127) the (0.0062) black (0.0053) coated (0.0056) drop- (0.0062) point (0.0056) blade (0.0026) features (-0.0002) partial (0.0041) serrations, (0.0061) making (0.0067) the (0.0052) swagger (0.0125) ao (0.0077) a (-0.0052) great (0.0072) every- (0.0098) day- (0.0051) carry (0.0025) tactical (0.0133) knife. (-0.0005)
~~~~~~

**Node-1.2** (global 32389):

~~~~~~text
product (0.0023) from (-0.0001) amazon (0.0001) platform (0.0011) with (-0.0012) title (0.0039) and (-0.0018) content (-0.0018) : (0.0018) title (0.0020) : (0.0003) case (0.0036) cutlery (-0.0006) 004 (0.0008) case (0.0007) executive (0.0084) lockback (0.0019) pocket (0.0028) knife (-0.0026) with (-0.0015) stainless (-0.0024) steel (0.0011) blade (0.0012) metal. (0.0008) content (0.0005) : (-0.0030) the (-0.0002) # (-0.0002) 004 (0.0003) case (-0.0009) executive (0.0017) lockback (0.0013) features (0.0014) a (-0.0005) brushed (-0.0001) stainless (-0.0022) steel (0.0019) handle (0.0005) and (-0.0009) tru- (0.0003) sharp (0.0012) surgical (-0.0004) steel (0.0007) drop (0.0028) point (0.0018) blade. (-0.0013) at (0.0024) 3 (0.0005) 1 (0.0003) / (0.0012) 8 (0.0013) " (-0.0002) closed, (0.0014) and (0.0006) weighing (-0.0014) just (0.0009) 1. (0.0020) 0 (-0.0009) oz., (0.0010) the (0.0012) slim (0.0005) design (0.0025) is (0.0014) perfect (0.0000) for (0.0003) a (0.0028) suit- (0.0010) pocket, (0.0007) purse (-0.0007) or (0.0008) on (0.0005) a (0.0005) key (0.0001) ring. (0.0022) the (0.0012) blade (0.0002) is (0.0017) skillfully (0.0009) honed (0.0005) and (0.0007) polished (-0.0006) to (0.0008) a (0.0012) razor (0.0023) & (-0.0005) # (-0.0005) x2019 (0.0011) ; (-0.0003) s (0.0025) edge, (0.0001) measures (0.0029) 2 (0.0007) & (0.0013) # (0.0020) xbc (0.0019) ; (0.0023) & (0.0020) # (0.0016) x201d (0.0014) ; (0.0049) and (0.0020) locks (0.0019) for (0.0023) added (0.0029) confidence. (0.0016) backed (0.0015) by (0.0034) case (-0.0004) & (-0.0012) # (0.0007) x2019 (0.0004) ; (0.0021) s (0.0007) limited (0.0025) lifetime (0.0033) warranty, (0.0005) the (0.0027) executive (-0.0084) lockback (-0.0001) makes (-0.0016) an (0.0003) ideal (-0.0010) gift. (0.0025) specifications (-0.0014) & (0.0007) # (0.0009) x2022 (0.0004) ; (0.0022) pattern (0.0023) : (0.0003) m1059l (0.0004) ss (0.0018) & (0.0001) # (0.0006) x2022 (0.0000) ; (0.0030) handle (-0.0007) material (0.0021) : (0.0021) brushed (-0.0041) stainless (-0.0017) steel (0.0022) & (0.0004) # (0.0017) x2022 (0.0006) ; (0.0001) blade (-0.0004) ( (0.0013) s (0.0024) ) (0.0005) : (0.0008) locking (0.0005) drop (0.0012) point (0.0000) & (0.0011) # (0.0008) x2022 (0.0003) ; (0.0011) blade (0.0003) material (0.0010) : (0.0010) tru- (0.0010) sharp (0.0010) surgical (-0.0008) steel (0.0009) & (0.0001) # (0.0004) x2022 (0.0006) ; (0.0025) length (0.0027) closed (0.0015) : (0.0010) 3 (0.0004) 1 (0.0011) / (0.0014) 8 (-0.0008) & (0.0012) # (0.0012) x201d (0.0011) ; (0.0008) & (0.0005) # (0.0008) x2022 (0.0009) ; (0.0011) weight (0.0004) : (0.0007) 1. (0.0007) 0 (0.0006) oz. (-0.0005) about (-0.0009) w. (0.0005) r. (0.0002) case (0.0013) & (0.0004) sons (-0.0021) cutlery (-0.0014) co. (0.0007) w. (0.0010) r. (0.0014) case (-0.0005) & (-0.0023) sons (0.0024) cutlery (-0.0005) company (0.0009) has (0.0011) been (-0.0006) a (0.0004) leading (0.0005) american (-0.0001) manufacturer (0.0012) of (-0.0006) premium, (0.0002) hand- (0.0007) crafted (0.0010) knives (-0.0011) for (-0.0003) more (0.0009) than (0.0011) a (0.0006) century. (-0.0010) still (-0.0004) manufactured (0.0005) in (-0.0007) bradford, (0.0005) pennsylvania (0.0026) by (0.0009) skilled (0.0002) artisans (0.0011) using (0.0003) the (-0.0003) finest (-0.0007) materials (0.0017) and (-0.0004) time- (0.0010) honored (-0.0003) techniques (0.0008) & (0.0000) # (-0.0000) x2013 (0.0015) ; (0.0029) this (0.0023) rich (-0.0015) heritage (-0.0046) makes (-0.0034) case (0.0004) knives (-0.0050) the (0.0025) brand (-0.0021) of (-0.0020) choice (0.0006) for (-0.0003) sportsmen (0.0003) and (0.0001) knife (-0.0011) enthusiasts, (0.0006) as (0.0010) well (0.0009) as (-0.0002) the (-0.0003) most (0.0016) collected (0.0051) knives (-0.0013) in (0.0003) the (0.0002) world. (0.0021) from (0.0001) hunting (0.0013) and (0.0003) pocket (-0.0039) knives (-0.0015) to (0.0007) the (-0.0017) v- (0.0013) 42 (0.0015) stiletto (0.0004) carried (0.0011) by (0.0002) u. (0.0008) s. (-0.0001) army (0.0005) soldiers (0.0005) in (0.0001) world (0.0001) war (0.0015) ii, (-0.0012) to (0.0028) the (0.0019) m- (0.0001) 1 (0.0016) astronauts (-0.0048) knife (-0.0014) carried (-0.0001) on (-0.0009) the (0.0003) gemini (0.0018) and (0.0003) apollo (-0.0027) missions, (-0.0002) case (0.0040) knives (-0.0028) have (-0.0020) been (0.0000) a (0.0025) trusted (0.0005)
~~~~~~

**Node-1.3** (global 32391):

~~~~~~text
product (0.0104) from (0.0089) amazon (0.0189) platform (-0.0036) with (0.0054) title (0.0060) and (0.0057) content (0.0113) : (0.0143) title (0.0052) : (0.0130) buck (0.0150) 55 (0.0105) folding (0.0079) hunter. (0.0115) content (0.0246) : (0.0131) none (-0.0058)
~~~~~~

**Node-1.4** (global 32392):

~~~~~~text
product (-0.0033) from (-0.0031) amazon (-0.0009) platform (0.0047) with (-0.0014) title (0.0001) and (0.0014) content (-0.0019) : (0.0001) title (-0.0025) : (-0.0001) bantam (-0.0002) bbw. (0.0019) content (-0.0007) : (0.0006) did (0.0014) you (-0.0002) really (-0.0012) need (-0.0006) anything (0.0002) but (0.0002) the (-0.0109) bew (0.0014) bantam (0.0007) bbw (-0.0001) from (0.0007) buck (0.0006) knives? (-0.0025) i (-0.0009) didn (0.0007) ' (-0.0006) t (-0.0004) think (-0.0007) so. (0.0024) with (0.0014) it (0.0007) ' (0.0001) s (0.0008) lightweight, (0.0002) mid (0.0014) lock (0.0014) back (0.0002) style, (0.0004) this (0.0025) knife (0.0020) will (-0.0009) be (0.0003) in (-0.0002) your (-0.0014) pocket (0.0015) day (0.0010) in (0.0007) and (0.0001) day (0.0008) out. (-0.0013) the (-0.0051) bantam (0.0011) is (0.0025) an (-0.0001) all (0.0018) around (-0.0003) american (-0.0042) need. (-0.0041) product (-0.0032) features (0.0038) : (0.0024) small (0.0020) size, (0.0017) lightweight, (0.0001) mid- (0.0006) lockback (0.0015) knife (0.0015) with (0.0018) 1- (0.0013) hand (0.0004) open (0.0021) contoured (0.0006) with (0.0008) finger (0.0010) groove, (0.0005) grip (0.0003) ridges, (0.0028) lanyard (0.0009) hole (0.0017) 0284bks- (0.0007) b, (0.0020) buck (0.0000) knives (-0.0001) bantam (0.0019) bbw, (0.0008) buck (0.0010) knives (-0.0002) bantam, (0.0004) buck (0.0015) knives (0.0008) bbw, (0.0004) buck (0.0019) bantam (0.0022) bbw, (0.0007) buck (0.0016) bbw, (0.0008) buck (0.0010) bantam, (0.0006) buck (0.0009) knives, (-0.0001) buck (0.0018) knives (-0.0001) warranty, (0.0007) buck (0.0015) folding (0.0011) knives, (-0.0004) buck (0.0006) knives (-0.0000) for (0.0007) sale, (0.0009) buck (0.0011) knives (0.0008) pocket (0.0009) knives, (0.0008) pocket (0.0017) knives, (0.0008) buck (0.0014) pocket (0.0023) knives, (0.0004) buck (0.0014) survival (0.0027) knives, (-0.0001) buck (0.0011) knives (-0.0002) review, (0.0021) buck (0.0006) knifes, (0.0006) best (0.0011) pocket (0.0012) knife, (-0.0000) where (0.0012) are (0.0022) buck (0.0011) knives (0.0014) made, (0.0019) buck (0.0008) knife, (0.0001) pocket (0.0014) knives (0.0014) for (0.0005) sale, (-0.0001) buck (0.0018) knives (0.0009) usa, (0.0007) vintage (0.0011) buck (0.0007) knives, (0.0000) buck (0.0010) knives (0.0012) direct, (-0.0005) buck (0.0005) knives (0.0008) made (0.0011) in (0.0005) usa, (-0.0011) buckknives, (-0.0000) rescue (0.0010) knives, (0.0003) buck (0.0002) knives (0.0006) wiki, (0.0007) buck (0.0009) knives (0.0012) catalog, (-0.0009) buck (0.0003) knives (0.0004) hunting (0.0007) knives, (0.0004) personalized (0.0004) buck (0.0003) knives, (0.0002) buck (0.0005) hunting (0.0005) knives, (0.0002) cheap (0.0030) buck (-0.0004) knives, (-0.0003) custom (0.0003) buck (-0.0001) knives, (0.0005) cold (0.0014) steel, (0.0005) buckknives. (0.0000) com, (-0.0004) buck (0.0006) knives (-0.0001) repair, (0.0008) buck (-0.0011) knives (0.0009) website, (0.0013) buck (0.0010) knives (0.0009) hunting (0.0007) knife, (0.0015) buck (-0.0006) knives (-0.0007) idaho, (0.0029) buck (-0.0004) knives (0.0005) sharpening, (0.0008) pocket (0.0009) knives, (0.0009) buck (0.0006) pocket (0.0003) knives, (0.0008) pocket (0.0006) knives (0.0004) for (0.0017) sale, (0.0011) old (0.0005) timer (0.0008) pocket (0.0007) knives, (0.0018) best (0.0023) pocket (0.0006) knives, (0.0012) good (0.0005) pocket (0.0015) knives, (0.0013) classic (0.0003) pocket (0.0013) knives, (0.0006) buck (0.0008) knives, (0.0006) buck (0.0014) knife, (-0.0001) fine (0.0018) pocket (0.0004) knives, (0.0009) high (-0.0014) end (-0.0015) pocket (0.0012) knives, (0.0001) custom (0.0022) made (0.0002) pocket (0.0013) knives, (0.0002) folding (0.0009) pocket (0.0010) knives, (0.0003) cool (0.0006) pocket (0.0003) knives, (0.0007) pocket (0.0010) knifes, (0.0010) small (0.0010) pocket (0.0005) knives, (0.0013) buck, (0.0005) buck (0.0014) knives (0.0012)
~~~~~~

**Node-1.5** (global 32393):

~~~~~~text
product (-0.0067) from (-0.0050) amazon (-0.0021) platform (-0.0031) with (-0.0015) title (-0.0008) and (-0.0019) content (0.0059) : (0.0026) title (0.0076) : (0.0039) gerber (0.0047) 31- (-0.0005) 001088 (-0.0007) myth (0.0159) pocket (0.0012) folder, (0.0010) fine (0.0047) edge (0.0020) folding (0.0057) lock- (0.0021) back (0.0037) clip (0.0020) knife. (0.0063) content (0.0067) : (0.0093) the (0.0032) myth (0.0038) pocket (-0.0060) folder (0.0132) is (-0.0034) the (-0.0006) compact, (0.0023) everyday (0.0072) carry, (0.0001) counterpart (0.0116) to (-0.0018) the (-0.0110) myth (0.0300) fixed (-0.0013) blade (-0.0041) pro. (-0.0002) it (0.0006) has (0.0003) a (0.0013) durable, (0.0018) soft (0.0029) rubberized (0.0025) handle (0.0043) that (-0.0025) provides (0.0029) a (-0.0008) secure (0.0028) grip (0.0050) in (0.0017) any (0.0026) climate (0.0019) or (0.0013) weather. (0.0004) the (-0.0009) high (0.0028) carbon (0.0018) stainless (0.0004) blade (0.0045) is (0.0020) durable (-0.0009) and (0.0024) lightweight, (0.0008) making (-0.0025) quick (0.0092) work (0.0082) of (0.0041) game (0.0038) dressing (0.0097) in (0.0028) the (0.0042) field. (0.0064) slim (0.0032) and (0.0052) minimal, (0.0032) it (0.0040) slides (0.0108) comfortably (0.0062) inside (0.0107) pockets (0.0055) and (0.0036) backpacks. (-0.0038) it (0.0040) ' (0.0077) s (-0.0004) our (0.0293) no (0.0165) bulk (0.0029) folder (-0.0053) for (0.0070) the (0.0070) modern (0.0009) athlete (0.0085) hunter. (0.0087)
~~~~~~
