# Reference packet: GraphNarrator__Llama-8B__products__21445

- Method: GraphNarrator; configuration: Llama-8B; dataset: products; target node: 21445
- Explanation source: `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/73.json` (messages[assistant])
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

- ROOT (product)
  - Node-1 (Mosin-Nagant rifle book)
    - Node-1.1 (missing item)
    - Node-1.2 (Mosin-Nagant stripper clips)
    - Node-1.3 (Mauser stripper clips)
    - Node-1.4 (Lee-Enfield rifle book)
    - Node-1.5 (Promag Archangel forend rail)
    - Node-1.6 (Mosin-Nagant front sight adjustment tool)

### Word-Level Evaluation

Keywords with high saliency scores in ROOT — "product" (0.02), "amazon" (0.02), "title" (-0.02), "content" (0.00), and "rifle" (-0.05) — are strongly associated with books and firearms. However, the negative scores for "rifle" and "title" indicate a lack of relevance to the product itself. More generic terms like "product" (0.02) and "amazon" (0.02) carry moderate saliency and contribute moderately.

### Graph-Level Aggregation

Node-1 (Mosin-Nagant rifle book, keywords: "book" (not explicitly mentioned, but implied), "Mosin-Nagant" (0.03), "rifle" (-0.04)) is a direct neighbor with moderate saliency, identifying a specific type of book related to firearms. Indirect neighbors — Node-1.1 (missing item), Node-1.2 (stripper clips), Node-1.3 (Mauser stripper clips), Node-1.4 (Lee-Enfield rifle book), Node-1.5 (Promag Archangel forend rail), and Node-1.6 (Mosin-Nagant front sight adjustment tool) — are all related to firearms or accessories, collectively confirming a context related to books about firearms.

### Free-Text Explanation

The classification of ROOT into "Books" is supported by its own keywords and the co-purchase neighborhood.

ROOT: Keywords like "product" (0.02), "amazon" (0.02), and "content" (0.00) clearly identify this as a product description, and the presence of "title" (-0.02) and "rifle" (-0.05) suggests a book about firearms.
  - Node-1: A Mosin-Nagant rifle book (keywords: "Mosin-Nagant" (0.03), "rifle" (-0.04)) is a direct book related to firearms, reinforcing the Books category.
    - Node-1.1 ~ Node-1.6: Various firearm-related items, including stripper clips, a forend rail, and a front sight adjustment tool, are all related to the Mosin-Nagant rifle, supporting the book category.

In summary, ROOT's own keywords moderately signal a product description, and the entire co-purchase neighborhood consists of firearm-related items, providing evidence for the "Books" category.
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/73.json`).

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
<verbalized-graph>ROOT: product(0.02) amazon(0.02) platform(-0.04) title(-0.02) content(0.00) title(-0.01) evans(-0.02) sports(-0.02) standing(0.01) rifle(-0.05) rack.(0.02) content(0.05) evans(-0.02) standing(0.02) rifle(-0.02) rack(0.01) measuring(0.04) 31(-0.01) x(0.02) 10(0.00) x(0.01) 35(-0.00) 1(0.02) 2(-0.01) made(0.04) solid(-0.01) native(-0.01) pine.(-0.01) holds(0.02) seven(-0.00) long(0.05) guns.(-0.04) assembly(-0.01) required(0.03) assembly(-0.04) hardware(0.06) included.(0.02) recommended(-0.01) indoor(0.01) use(0.03) only.(0.04) made(0.02) usa.(-0.01) 
Node-1: product(-0.06) amazon(-0.04) platform(-0.04) title(-0.00) content(-0.02) title(0.01) mosin-(-0.01) nagant(0.03) rifle,(-0.03) 6th(-0.02) edition(0.02) collectors(-0.07) ).(-0.04) content(0.01) mosin-(0.01) nagant(-0.04) rifle(-0.04) first(0.04) book(0.02) ever(0.02) published(0.01) english(0.02) mosin-(-0.02) nagant(-0.05) rifle(-0.08) breadth(0.06) depth(0.02) information(0.00) presentation(0.00) set(0.01) standard(0.03) authors(-0.02) find(0.00) extremely(-0.03) difficult(0.00) meet(-0.01) future.(0.08) provides(-0.01) history(0.03) rifle(-0.02) development(0.07) use(0.01) late(0.02) 1880s(-0.01) 1970s,(0.01) provides(0.05) part-(0.02) by-(0.03) part(0.02) description(0.04) differences(0.05) models(0.09) changes(0.08) made(-0.01) long(0.01) production(0.03) life(0.03) countries(-0.01) around(0.02) world,(0.02) including(0.01) united(0.02) states.(-0.03) long(-0.00) list(0.03) codes,(-0.03) markings(-0.01) stamps(-0.05) also(0.03) provided(-0.00) top(0.01) aid(0.02) identifying(0.02) rifle(-0.01) made(0.02) used.(-0.06) 
Node-1.1: product(0.00) amazon(0.01) platform(-0.00) title(0.00) content(0.00) title(0.00) missing.(0.00) content(0.01) new(-0.00) made(0.00) item(0.00) new(0.00) made(0.00) example(-0.00) quality(0.00) brown(0.00) leather(0.00) classic(0.00) enfield(-0.00) smle(0.00) series(0.00) rifle(0.00) slings(-0.00) use(0.00) 1900(0.01) superseded(-0.00) web(0.01) slings(0.00) latter(0.00) part(0.00) ww2.(0.00) complete(0.00) running(0.00) leather(0.00) keeper(0.00) loop(0.00) thronged(0.00) butt(0.00) attachment(0.00) standard(0.00) british(0.01) military(0.00) issue(0.01) sling(-0.01) almost(0.00) fifty(0.00) years.(0.00) replicated(-0.00) markings!(0.01) length(0.00) 46(0.00) 1(0.01) 2(0.02) width(-0.00) 1(0.01) 3(-0.00) 16(-0.01) 
Node-1.2: product(-0.00) amazon(0.01) platform(0.00) title(-0.00) content(0.01) title(0.00) set(0.00) 40(-0.00) brand(0.00) new(-0.01) stripper(-0.00) clips(-0.00) mosin(0.00) nagant(-0.01) 1891(0.01) 30(0.00) 91(0.00) 30(0.00) m38(0.00) m39(0.01) m44(0.00) 7.(0.00) 62x54r(0.00) rifles.(0.01) content(-0.01) set(0.00) 40(-0.00) brand(-0.00) new(-0.00) stripper(0.00) clips(-0.00) 
Node-1.3: product(0.00) amazon(0.01) platform(0.00) title(-0.00) content(-0.00) title(0.00) mauser(-0.00) stripper(-0.00) clips(0.00) 40ct(-0.00) 6.(-0.00) 5x55mm(0.00) 38,(0.00) 94,(0.00) 96(-0.00) amp(0.01) 30-(-0.00) 06,(0.00) 1903,(0.00) 1917.(0.01) content(-0.00) 40x(0.00) 6.(0.00) 5x55(0.00) mm(0.00) stripper(0.00) clips(0.00) unopened(0.00) box(-0.00) new(0.00) stripper(-0.00) clips(0.00) work(-0.00) many(0.00) firearms(-0.00) including(0.00) swedish(0.00) mauser(-0.00) 38,(0.00) 94,(0.00) 96,(0.00) 1903(0.00) springfield,(0.01) 1917(0.01) enfield(-0.00) told(0.00) 6.(0.00) 5mm(0.00) arisaka(0.00) rifles(-0.01) receive(0.00) 40(0.00) new(0.00) stripper(0.00) clips(0.00) order(-0.00) 
Node-1.4: product(-0.00) amazon(0.00) platform(-0.00) title(0.00) content(0.00) title(0.00) lee-(0.00) enfield(0.00) rifle(0.00) weapon(0.00) ).(-0.00) content(-0.00) martin(0.00) pegler(-0.00) ba(0.00) hons(0.00) medieval(0.00) modern(0.00) history(0.00) museum(0.00) studies,(0.00) university(0.00) college,(0.00) london,(0.00) many(0.00) years(0.00) senior(0.00) curator(0.00) firearms(0.00) royal(0.00) armouries(0.00) museum,(0.00) leeds.(0.00) lives(-0.00) somme,(0.00) france,(0.00) wife(-0.00) run(-0.00) small(-0.00) bed(-0.00) breakfast,(0.00) situated(0.00) top(-0.00) old(0.00) german(0.00) front(-0.00) line!(-0.00) martin(-0.00) established(-0.00) somme(-0.00) historical(0.00) centre(-0.00) www.(0.00) martinpegler.(-0.00) com(0.00) ),(-0.00) visitors(0.00) see(0.00) technology(0.00) used(0.00) 1914-(-0.00) 18(0.00) trench(0.00) warfare.(0.00) spare(-0.00) time(-0.00) martin(-0.00) runs(0.00) motorcycle(0.00) tours(-0.00) battlefield.(0.00) author(-0.00) number(-0.00) books(0.00) including(0.00) military(0.00) sniper(0.00) since(0.00) 1914(0.00) osprey,(0.00) 2001(0.00) ),(0.00) firearms(0.00) american(0.00) west(0.00) 1700-(0.00) 1900(0.00) crowood(-0.00) press,(0.00) 2002(0.00) ),(0.00) highly(-0.00) acclaimed(0.00) nowhere(0.00) history(0.00) military(0.00) sniper(0.00) osprey,(0.00) 2004(0.00) ),(0.00) also(0.00) contributed(0.00) number(0.00) magazines.(0.00) 1980s(0.00) privilege(0.00) interviewing(0.00) many(0.00) world(0.00) war(0.00) veterans(0.00) wartime(0.00) experiences,(0.00) recordings(0.00) part(0.00) sound(0.00) archives(0.00) imperial(0.00) war(0.00) museum,(0.00) london.(-0.00) martin(0.00) series(0.00) editor(-0.00) osprey(0.00) weapon(0.00) series.(0.00) 
Node-1.5: product(0.01) amazon(0.01) platform(-0.00) title(0.01) content(-0.00) title(0.00) promag(0.01) archangel(-0.00) opfor(0.00) aa9130(0.00) forend(0.01) rail,(0.00) black.(0.00) content(0.00) promag(0.00) picatinny(0.00) rail(0.01) accessory(0.01) end(0.00) mosin-(0.00) nagant(0.01) precision(0.00) rifle(0.00) stock(0.00) made(0.01) proprietary(0.01) polymer(0.00) compound(0.00) stock.(0.00) color(0.01) black.(-0.01) 
Node-1.6: product(0.00) amazon(0.00) platform(0.00) title(0.00) content(0.00) title(0.00) mosin(-0.00) nagant(-0.00) 91(0.00) 30(-0.00) quot(-0.00) range(0.00) buddy(-0.00) quot(-0.00) front(-0.00) sight(0.01) adjustment(0.01) tool.(-0.01) content(0.01) mosin(-0.00) nagant(0.00) great(0.00) military(0.00) surplus(0.00) rifle(0.00) blast(-0.00) shoot,(0.00) know(0.00) front(0.00) sight(0.00) difficult(0.00) fine(0.00) tune(0.00) optimal(0.</verbalized-graph>

### Classification Label
Books

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 21445
- Title: Evans Sports Standing Rifle Rack
- True class (canonical `y`): **Sports & Outdoors**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Sports & Outdoors**
- Prediction recorded by this method's pipeline: **Books**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Evans Sports Standing Rifle Rack. Content: The Evans Standing Rifle Rack measuring 31"x 10"x 35 1/2" is made of solid native pine. It holds up to seven long guns. Assembly Required with all assembly hardware included. Recommended for indoor use only. Made in the USA.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 3893 | Books | The Mosin-Nagant Rifle, 6th Edition (For collectors only) |

### 2-hop (shortest distance exactly 2): 7 nodes

| node id | true class | title |
|---|---|---|
| 422 | label 25 | missing |
| 3827 | Sports & Outdoors | Set of 40 BRAND NEW Stripper Clips For Mosin Nagant 1891/30 91/30 M38 M39 M44 7.62X54r Rifles |
| 3846 | Sports & Outdoors | Mauser Stripper Clips 40CT 6.5x55mm 38,94,96 &amp; 30-06, 1903, 1917 |
| 21214 | Books | The Lee-Enfield Rifle (Weapon) |
| 21233 | Sports & Outdoors | ProMag Archangel Opfor AA9130 Forend Rail, Black |
| 21443 | Sports & Outdoors | Mosin Nagant 91/30 &quot;Range Buddy&quot; Front Sight Adjustment Tool |
| 21444 | Sports & Outdoors | Pachmayr Decelerator Slip On Recoil Pad |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/73.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Books**, ground truth = **Sports & Outdoors**.
The verbalized graph is 7638 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 21445 | 64 | 0.0596 | yes |
| Node-1 | 1 | 3893 | 145 | 0.0930 | yes |
| Node-1.1 | 2 | 422 | 90 | 0.0293 | yes |
| Node-1.2 | 3 | 3827 | 42 | 0.0124 | yes |
| Node-1.3 | 4 | 3846 | 80 | 0.0061 | yes |
| Node-1.4 | 5 | 21214 | 234 | 0.0036 | yes |
| Node-1.5 | 6 | 21233 | 52 | 0.0089 | yes |
| Node-1.6 | 7 | 21443 | 118 | 0.0072 | yes |
| Node-1.7 | 8 | 21444 | 167 | 0.0085 | no |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->Node-1.6, Node-1->Node-1.7, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, Node-1.6->Node-1, Node-1.7->Node-1, ROOT->Node-1

### Tokens and scores

**ROOT** (global 21445):

~~~~~~text
product (0.0225) from (0.0110) amazon (0.0177) platform (-0.0383) with (0.0484) title (-0.0228) and (0.0350) content (0.0036) : (0.0058) title (-0.0059) : (-0.0062) evans (-0.0206) sports (-0.0231) standing (0.0079) rifle (-0.0517) rack. (0.0175) content (0.0451) : (0.0405) the (0.0019) evans (-0.0188) standing (0.0223) rifle (-0.0195) rack (0.0130) measuring (0.0358) 31 (-0.0133) " (-0.0160) x (0.0171) 10 (0.0001) " (-0.0009) x (0.0067) 35 (-0.0024) 1 (0.0151) / (0.0152) 2 (-0.0111) " (-0.0081) is (0.0385) made (0.0438) of (0.0303) solid (-0.0051) native (-0.0065) pine. (-0.0068) it (0.0101) holds (0.0197) up (0.0175) to (0.0067) seven (-0.0036) long (0.0463) guns. (-0.0400) assembly (-0.0126) required (0.0273) with (0.0288) all (0.0102) assembly (-0.0433) hardware (0.0596) included. (0.0197) recommended (-0.0058) for (0.0204) indoor (0.0100) use (0.0260) only. (0.0400) made (0.0237) in (0.0166) the (-0.0036) usa. (-0.0084)
~~~~~~

**Node-1** (global 3893):

~~~~~~text
product (-0.0558) from (-0.0177) amazon (-0.0436) platform (-0.0427) with (0.0064) title (-0.0045) and (0.0066) content (-0.0209) : (-0.0020) title (0.0093) : (-0.0019) the (-0.0260) mosin- (-0.0100) nagant (0.0304) rifle, (-0.0335) 6th (-0.0191) edition (0.0224) ( (0.0129) for (0.0317) collectors (-0.0698) only (-0.0049) ). (-0.0449) content (0.0127) : (0.0368) the (0.0182) mosin- (0.0067) nagant (-0.0385) rifle (-0.0385) is (-0.0176) the (-0.0040) first (0.0425) book (0.0231) ever (0.0218) published (0.0089) in (0.0337) english (0.0199) about (0.0416) the (0.0086) mosin- (-0.0159) nagant (-0.0465) rifle (-0.0751) and (0.0063) the (0.0290) breadth (0.0553) and (-0.0004) depth (0.0173) of (0.0355) its (-0.0108) information (0.0033) and (0.0733) its (0.0177) presentation (0.0011) has (-0.0022) set (0.0115) a (-0.0066) standard (0.0305) that (0.0026) other (0.0074) authors (-0.0236) will (0.0073) find (0.0043) extremely (-0.0303) difficult (0.0015) to (0.0271) meet (-0.0139) in (-0.0231) the (-0.0675) future. (0.0752) it (0.0051) not (-0.0016) only (-0.0197) provides (-0.0077) a (-0.0037) history (0.0291) of (0.0148) the (0.0085) rifle (-0.0225) ' (0.0003) s (0.0560) development (0.0726) and (0.0146) use (0.0144) from (0.0324) the (-0.0107) late (0.0225) 1880s (-0.0128) to (0.0317) the (-0.0090) 1970s, (0.0130) but (0.0417) provides (0.0507) a (-0.0161) part- (0.0245) by- (0.0251) part (0.0162) description (0.0389) of (-0.0277) differences (0.0460) between (-0.0121) models (0.0930) and (0.0459) changes (0.0766) made (-0.0129) during (-0.0019) its (0.0143) long (0.0134) production (0.0257) life (0.0270) in (0.0113) countries (-0.0089) around (0.0227) the (0.0088) world, (0.0224) including (0.0141) the (0.0086) united (0.0216) states. (-0.0286) a (-0.0002) long (-0.0035) list (0.0251) of (-0.0093) codes, (-0.0326) markings (-0.0120) and (0.0472) other (-0.0006) stamps (-0.0501) are (0.0920) also (0.0283) provided (-0.0009) top (0.0126) aid (0.0171) in (-0.0195) identifying (0.0165) when (-0.0044) the (0.0017) rifle (-0.0144) was (0.0234) made (0.0184) and (0.0382) when (0.0124) and (0.0342) where (0.0131) it (0.0042) was (-0.0196) used. (-0.0558)
~~~~~~

**Node-1.1** (global 422):

~~~~~~text
product (0.0001) from (-0.0012) amazon (0.0084) platform (-0.0007) with (-0.0008) title (0.0016) and (0.0017) content (0.0016) : (0.0054) title (0.0029) : (0.0034) missing. (0.0040) content (0.0051) : (0.0028) new (-0.0000) made (0.0019) item (0.0016) : (0.0023) this (0.0018) a (0.0022) new (0.0007) made (0.0010) example (-0.0007) of (-0.0007) quality (0.0027) brown (0.0014) leather (0.0047) of (-0.0004) the (0.0008) classic (0.0002) enfield (-0.0006) smle (0.0013) series (0.0017) rifle (0.0024) slings (-0.0019) in (0.0022) use (0.0022) from (0.0013) about (0.0005) 1900 (0.0054) until (0.0025) superseded (-0.0008) by (0.0006) web (0.0081) slings (0.0009) in (0.0020) the (0.0006) latter (0.0020) part (0.0019) of (0.0024) ww2. (0.0008) complete (0.0018) with (0.0004) running (0.0039) leather (0.0015) keeper (0.0030) loop (0.0010) and (0.0049) thronged (0.0020) for (0.0029) butt (0.0001) attachment (0.0011) this (0.0052) was (0.0009) the (-0.0037) standard (0.0043) british (0.0063) military (0.0014) issue (0.0053) sling (-0.0051) for (0.0003) almost (0.0029) fifty (0.0039) years. (0.0009) replicated (-0.0012) markings! (0.0075) length (0.0007) : (0.0036) 46 (0.0020) 1 (0.0065) / (0.0003) 2 (0.0244) " (-0.0188) width (-0.0021) : (-0.0028) 1 (0.0053) 3 (-0.0005) / (0.0092) 16 (-0.0126) " (0.0293)
~~~~~~

**Node-1.2** (global 3827):

~~~~~~text
product (-0.0024) from (0.0036) amazon (0.0089) platform (0.0002) with (0.0074) title (-0.0018) and (0.0010) content (0.0062) : (0.0025) title (0.0026) : (-0.0011) set (0.0008) of (0.0041) 40 (-0.0004) brand (0.0012) new (-0.0080) stripper (-0.0010) clips (-0.0032) for (0.0011) mosin (0.0016) nagant (-0.0071) 1891 (0.0115) / (0.0050) 30 (0.0002) 91 (0.0005) / (0.0040) 30 (0.0035) m38 (0.0034) m39 (0.0063) m44 (0.0049) 7. (0.0049) 62x54r (0.0030) rifles. (0.0124) content (-0.0080) : (0.0050) set (0.0009) of (0.0040) 40 (-0.0017) brand (-0.0044) new (-0.0015) stripper (0.0027) clips (-0.0017)
~~~~~~

**Node-1.3** (global 3846):

~~~~~~text
product (0.0010) from (-0.0038) amazon (0.0055) platform (0.0024) with (-0.0008) title (-0.0022) and (0.0016) content (-0.0007) : (-0.0050) title (0.0013) : (-0.0029) mauser (-0.0018) stripper (-0.0007) clips (0.0000) 40ct (-0.0012) 6. (-0.0005) 5x55mm (0.0005) 38, (0.0003) 94, (0.0003) 96 (-0.0015) & (-0.0024) amp (0.0058) ; (0.0061) 30- (-0.0006) 06, (0.0012) 1903, (0.0038) 1917. (0.0053) content (-0.0023) : (0.0014) 40x (0.0008) 6. (0.0017) 5x55 (0.0013) mm (0.0020) stripper (0.0009) clips (0.0013) in (0.0005) a (-0.0019) unopened (0.0002) box (-0.0011) these (0.0036) are (-0.0000) new (0.0010) stripper (-0.0002) clips (0.0027) that (0.0007) will (-0.0025) work (-0.0007) on (0.0005) many (0.0034) firearms (-0.0023) including (0.0044) the (-0.0061) swedish (0.0033) mauser (-0.0014) 38, (0.0023) 94, (0.0019) 96, (0.0020) 1903 (0.0048) springfield, (0.0054) 1917 (0.0059) enfield (-0.0017) and (0.0002) i (0.0018) have (-0.0037) been (-0.0027) told (0.0023) 6. (0.0038) 5mm (0.0003) arisaka (0.0043) rifles (-0.0068) you (-0.0083) will (0.0022) receive (0.0002) 40 (0.0013) new (0.0041) stripper (0.0029) clips (0.0037) with (0.0005) each (-0.0020) order (-0.0000)
~~~~~~

**Node-1.4** (global 21214):

~~~~~~text
product (-0.0011) from (-0.0006) amazon (0.0000) platform (-0.0003) with (0.0001) title (0.0009) and (0.0002) content (0.0006) : (0.0009) title (0.0003) : (0.0005) the (0.0004) lee- (0.0006) enfield (0.0021) rifle (0.0008) ( (0.0006) weapon (0.0011) ). (-0.0001) content (-0.0007) : (-0.0015) martin (0.0010) pegler (-0.0019) has (0.0002) a (0.0004) ba (0.0004) hons (0.0009) in (0.0005) medieval (0.0015) and (0.0000) modern (0.0003) history (0.0009) and (0.0007) an (0.0001) ma (-0.0009) in (0.0003) museum (0.0021) studies, (0.0004) both (0.0005) from (0.0001) university (0.0011) college, (0.0009) london, (0.0015) and (0.0005) was (0.0001) for (0.0002) many (0.0012) years (0.0004) the (0.0008) senior (0.0007) curator (0.0015) of (0.0005) firearms (0.0007) at (0.0008) the (0.0002) royal (0.0021) armouries (0.0014) museum, (0.0015) leeds. (0.0030) he (0.0008) now (0.0006) lives (-0.0005) in (0.0020) the (0.0011) somme, (0.0017) france, (0.0011) where (-0.0001) he (0.0010) and (0.0024) his (0.0002) wife (-0.0002) run (-0.0003) a (0.0005) small (-0.0001) bed (-0.0006) and (0.0006) breakfast, (0.0009) which (0.0002) is (0.0008) situated (0.0007) on (0.0002) top (-0.0001) of (0.0001) the (0.0001) old (0.0007) german (0.0021) front (-0.0000) line! (-0.0007) martin (-0.0011) has (0.0022) established (-0.0009) the (0.0022) somme (-0.0002) historical (0.0012) centre (-0.0003) ( (0.0004) www. (0.0006) martinpegler. (-0.0005) com (0.0001) ), (-0.0003) where (-0.0011) visitors (0.0005) can (-0.0002) see (0.0005) the (-0.0000) technology (0.0004) used (0.0006) in (-0.0002) the (0.0001) 1914- (-0.0000) 18 (0.0004) trench (0.0023) warfare. (0.0014) in (-0.0008) his (-0.0021) spare (-0.0008) time (-0.0010) martin (-0.0015) runs (0.0007) motorcycle (0.0000) tours (-0.0010) of (0.0007) the (0.0009) battlefield. (0.0010) he (0.0002) is (0.0004) the (-0.0001) author (-0.0003) of (-0.0002) a (-0.0009) number (-0.0001) of (-0.0001) books (0.0002) including (0.0007) ' (0.0004) the (0.0001) military (0.0006) sniper (0.0016) since (0.0009) 1914 (0.0009) ' (0.0008) ( (0.0004) osprey, (0.0000) 2001 (0.0003) ), (0.0013) ' (0.0006) firearms (0.0011) in (0.0009) the (0.0001) american (0.0023) west (0.0008) 1700- (0.0008) 1900 (0.0021) ' (0.0010) ( (0.0007) the (0.0001) crowood (-0.0007) press, (0.0002) 2002 (0.0012) ), (0.0004) and (0.0004) the (0.0004) highly (-0.0003) acclaimed (0.0002) ' (0.0003) out (0.0004) of (-0.0000) nowhere (0.0012) : (0.0007) a (0.0003) history (0.0007) of (0.0003) the (0.0005) military (0.0010) sniper (0.0009) ' (0.0004) ( (-0.0005) osprey, (0.0001) 2004 (0.0004) ), (0.0002) and (0.0004) he (0.0004) has (0.0008) also (0.0007) contributed (0.0004) to (0.0002) a (-0.0001) number (0.0004) of (0.0009) magazines. (0.0009) in (0.0008) the (-0.0002) 1980s (0.0005) he (0.0001) had (-0.0002) the (-0.0009) privilege (0.0018) of (0.0007) interviewing (0.0036) many (0.0007) world (0.0010) war (0.0008) i (0.0007) veterans (0.0004) about (0.0002) their (0.0006) wartime (0.0010) experiences, (0.0008) and (0.0013) the (-0.0009) recordings (0.0006) are (0.0008) now (0.0009) part (0.0005) of (0.0003) the (0.0002) sound (0.0000) archives (0.0010) of (-0.0000) the (-0.0004) imperial (0.0009) war (0.0006) museum, (0.0001) london. (-0.0007) martin (0.0030) is (-0.0015) the (0.0005) series (0.0022) editor (-0.0020) for (-0.0003) osprey (0.0005) ' (0.0003) s (-0.0008) weapon (0.0014) series. (0.0008)
~~~~~~

**Node-1.5** (global 21233):

~~~~~~text
product (0.0055) from (-0.0020) amazon (0.0089) platform (-0.0032) with (0.0038) title (0.0061) and (0.0044) content (-0.0008) : (0.0054) title (0.0041) : (0.0024) promag (0.0056) archangel (-0.0021) opfor (0.0044) aa9130 (0.0048) forend (0.0062) rail, (0.0020) black. (0.0007) content (0.0019) : (0.0021) promag (0.0045) picatinny (0.0050) rail (0.0085) is (0.0043) an (0.0048) accessory (0.0064) for (0.0035) the (0.0031) for (0.0032) end (0.0027) of (0.0032) the (0.0006) mosin- (0.0040) nagant (0.0058) precision (0.0050) rifle (0.0023) stock (0.0041) and (0.0057) is (0.0051) made (0.0050) from (0.0044) the (0.0031) same (0.0073) proprietary (0.0075) polymer (0.0027) compound (0.0039) as (0.0066) the (0.0034) stock. (0.0020) color (0.0089) : (0.0050) black. (-0.0059)
~~~~~~

**Node-1.6** (global 21443):

~~~~~~text
product (0.0030) from (-0.0005) amazon (0.0024) platform (0.0003) with (0.0026) title (0.0036) and (0.0011) content (0.0016) : (0.0010) title (0.0038) : (0.0006) mosin (-0.0011) nagant (-0.0012) 91 (0.0016) / (0.0022) 30 (-0.0011) & (0.0033) quot (-0.0010) ; (0.0041) range (0.0018) buddy (-0.0001) & (0.0019) quot (-0.0015) ; (0.0046) front (-0.0008) sight (0.0068) adjustment (0.0059) tool. (-0.0059) content (0.0072) : (0.0055) the (0.0002) mosin (-0.0002) nagant (0.0011) is (0.0013) a (0.0003) great (0.0002) military (0.0046) surplus (0.0007) rifle (0.0013) that (0.0011) is (0.0030) a (0.0008) blast (-0.0003) to (0.0033) shoot, (0.0011) but (0.0027) we (-0.0005) all (0.0023) know (0.0016) that (0.0022) the (-0.0016) front (0.0025) sight (0.0013) is (0.0033) very (0.0025) difficult (0.0023) to (0.0018) fine (0.0027) tune (0.0030) for (0.0025) optimal (0.0027) accuracy. (0.0027) with (0.0015) this (0.0002) sight (0.0018) pusher, (0.0016) you (0.0033) ' (0.0007) ll (0.0028) be (0.0015) amazed (0.0054) how (0.0032) effortlessly (0.0032) and (0.0037) precise (0.0030) you (0.0022) will (0.0037) be (0.0016) able (0.0016) to (0.0022) remove, (0.0036) install, (0.0040) and (0.0042) adjust (0.0034) the (0.0006) front (0.0042) sight (0.0030) windage (0.0028) of (0.0016) your (0.0041) 91 (0.0062) / (0.0014) 30 (-0.0000) mosin. (0.0012) stop (0.0021) damaging (0.0047) your (-0.0011) rifle (0.0022) by (0.0050) blindly (0.0045) banging (0.0042) on (0.0040) it (0.0026) with (0.0024) a (-0.0001) hammer (0.0051) and (0.0015) get (0.0063) a (0.0016) tool (0.0042) that (0.0038) is (0.0030) specifically (0.0026) designed (0.0053) for (0.0024) the (-0.0021) job (0.0062) today! (0.0049)
~~~~~~

**Node-1.7** (global 21444):

~~~~~~text
product (-0.0029) from (-0.0027) amazon (-0.0001) platform (-0.0016) with (-0.0010) title (0.0015) and (0.0004) content (0.0002) : (0.0023) title (0.0013) : (0.0016) pachmayr (0.0005) decelerator (-0.0004) slip (0.0026) on (0.0006) recoil (-0.0013) pad. (0.0008) content (0.0018) : (0.0006) no (0.0020) gunsmithing (-0.0007) required! (0.0013) pachmayr (0.0022) & (0.0003) # (0.0005) x2019 (0.0013) ; (-0.0001) s (0.0013) decelerator (0.0011) recoil (0.0028) pads (0.0003) provide (0.0027) the (-0.0051) ultimate (0.0019) in (0.0014) recoil (0.0010) control (0.0001) and (0.0021) appearance (0.0007) and (0.0008) now (0.0019) you (0.0015) can (0.0017) install (0.0022) them (0.0015) on (0.0015) all (0.0009) your (0.0026) long (0.0019) guns. (-0.0015) designed (0.0050) to (0.0021) fit (0.0007) within. (0.0017) 050 (0.0008) inch (-0.0001) tolerance (-0.0002) on (0.0010) factory (0.0012) stocks, (-0.0022) these (0.0023) pads (0.0071) will (0.0042) enhance (0.0027) the (-0.0041) look (0.0004) and (0.0025) feel (0.0015) of (0.0021) the (-0.0051) gun, (-0.0007) improve (0.0021) your (0.0020) shooting (0.0002) experience, (-0.0007) and (0.0025) maybe (0.0036) help (-0.0008) you (0.0036) bag (0.0051) more (0.0030) game. (0.0019) features (0.0061) :- (0.0009) easy (0.0034) & (0.0017) # (0.0020) x201c (0.0021) ; (0.0040) do- (0.0013) it- (0.0025) yourself (0.0011) & (0.0034) # (0.0028) x201d (0.0022) ; (0.0085) installation- (0.0035) replaces (0.0073) hard (0.0039) factory (-0.0017) pads- (0.0017) custom (0.0012) & (0.0017) # (0.0008) x201c (-0.0001) ; (0.0032) pre- (0.0030) ground (-0.0008) & (0.0015) # (0.0018) x201d (0.0005) ; (0.0075) fit (-0.0001) size (0.0031) large (0.0010) fits (0.0038) : (0.0021) stock (-0.0000) dimensions (0.0011) of (0.0006) 1- (0.0021) 3 (0.0038) / (0.0023) 4 (0.0006) " (-0.0010) to (0.0013) 1- (0.0020) 7 (0.0011) / (0.0014) 8 (0.0005) " (-0.0000) wide (0.0015) x (0.0025) 5- (0.0012) 3 (0.0015) / (0.0007) 16 (-0.0000) " (-0.0003) to (0.0012) 5- (0.0007) 7 (0.0006) / (0.0012) 16 (-0.0006) " (0.0030) long, (0.0010) or (0.0014) will (0.0037) fit (0.0015) the (-0.0024) following (-0.0012) : (0.0017) beretaa (0.0025) : (-0.0017) 686, (0.0020) 687 (0.0016) field (0.0022) models, (0.0007) 302, (0.0030) 303 (0.0015) semi- (0.0017) auto (0.0020) browning (-0.0039) : (-0.0063) citori (0.0043) with (0.0014) english (0.0037) stock (0.0006)
~~~~~~
