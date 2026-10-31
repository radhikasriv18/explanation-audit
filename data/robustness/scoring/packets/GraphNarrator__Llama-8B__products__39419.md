# Reference packet: GraphNarrator__Llama-8B__products__39419

- Method: GraphNarrator; configuration: Llama-8B; dataset: products; target node: 39419
- Explanation source: `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/147.json` (messages[assistant])
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
  - Node-1 (tote bag)
    - Node-1.1 (18-inch doll backpack)
    - Node-1.2 (3-piece gymnastics outfit)
    - Node-1.3 (paints)
    - Node-1.4 (bicycle seat for doll)

### Word-Level Evaluation

Keywords with high saliency scores in ROOT — "product" (-0.01), "amazon" (0.01), "title" (0.01), "content" (-0.00) — are not strongly associated with a specific product category. However, the presence of "product" (-0.01) indicates a commercial item, which is a good starting point.

### Graph-Level Aggregation

Node-1 (tote bag, keywords: "bag" (0.07), "tote" (0.05), "nylon" (0.10), "imported" (0.05)) is a direct neighbor with high saliency, identifying a product related to storage or carrying. This is reinforced by its own keywords, which indicate a product designed for carrying multiple items, such as dolls and accessories.

Indirect neighbors — Node-1.1 (18-inch doll backpack), Node-1.2 (3-piece gymnastics outfit), Node-1.3 (paints), Node-1.4 (bicycle seat for doll) — are all related to dolls or doll accessories, collectively confirming a context of doll-related products.

### Free-Text Explanation

The classification of ROOT into "Cell Phones & Accessories" is not strongly supported by its own keywords or the co-purchase neighborhood.

ROOT: Keywords like "product" (-0.01) and "amazon" (0.01) are generic and do not indicate a specific product category.

- Node-1: A tote bag (keywords: "bag" (0.07), "tote" (0.05), "nylon" (0.10)) is a direct neighbor with high saliency, identifying a product related to storage or carrying.
  - Node-1.1 ~ Node-1.4: Doll-related products (18-inch doll backpack, 3-piece gymnastics outfit, paints, bicycle seat for doll) collectively confirm a context of doll-related products.

However, the classification label "Cell Phones & Accessories" does not align with the identified keywords and co-purchase neighborhood. A more suitable classification would be "Toys & Games" or "Dolls & Accessories," as the graph structure and keywords strongly suggest a context of doll-related products.
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/147.json`).

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
<verbalized-graph>ROOT: product(-0.01) amazon(0.01) platform(0.00) title(0.01) content(-0.00) title(-0.01) badger(0.01) basket(0.01) doll(-0.01) bunk(-0.02) beds(-0.01) ladder-(0.00) pink(-0.01) white.(0.01) content(-0.00) right(-0.00) doll(-0.00) friends(0.00) come(0.01) visit.(-0.03) doll(-0.01) bunk(-0.01) beds(-0.01) built(0.00) two(0.00) dolls(-0.00) rest(0.00) style.(-0.01) includes(-0.02) ladder(0.04) extra(0.01) fun(0.01) realism.(0.02) pretty(0.00) pink(-0.00) gingham(0.01) complements(0.01) attractive(0.01) white(0.01) finish.(-0.04) dolls(-0.04) 20(-0.01) ".(0.01) overall(0.01) size(-0.01) 11.(0.01) 5(-0.01) x(-0.02) 22.(0.00) 25(-0.01) x(-0.01) 15(-0.01) ".(0.02) 6.(0.01) 75(0.00) clearance(0.01) top(0.01) bottom(0.03) bunks(-0.00) 3.(0.01) 5(0.00) distance(0.01) bottom(0.03) bunk(-0.02) floor.(-0.00) includes(-0.00) two(0.01) removable(0.01) mattresses(0.01) 21.(0.01) 25(-0.00) x(-0.00) 10(-0.01) attached(-0.00) pillows(0.00) eyelet(0.00) trim.(0.01) pillow(-0.00) area(-0.01) mattress(-0.01) approximately(-0.00) 3.(0.01) 5(0.01) x(0.01) 10(-0.00) ".(0.01) ladder(-0.02) measures(0.02) approximately(0.00) 15(0.00) x(0.00) 5(-0.00) x(0.00) 3(0.00) 8(0.00) d.(0.00) enjoyed(0.03) children(0.03) three(0.02) years(0.01) old(0.00) up.(0.01) paints(0.02) finishes(0.02) non-(0.01) toxic.(0.00) adult(-0.00) assembly(-0.00) required.(0.01) illustrated(0.03) instructions(0.02) included.(0.01) made(-0.00) wood(0.00) wood(0.01) composites.(0.01) fabric(0.00) parts(0.00) poly(0.01) cotton(0.01) stuffed(0.01) polyfill.(0.00) wipe(0.01) wood(0.01) parts(0.01) clean(0.01) damp(0.01) cloth(0.01) mild(0.00) detergent(0.00) needed.(0.01) longevity(0.01) product,(0.00) spot(0.01) cleaning(0.01) hand(0.00) washing(-0.00) recommended(0.01) fabric(0.01) parts(0.01) machine(0.01) wash(0.00) gentle(0.01) air(-0.00) dry(0.00) desired(0.01) ).(0.03) item(-0.01) toy(0.01) use(-0.01) dolls(-0.01) only.(0.02) never(0.02) used(-0.01) real(0.01) infants(-0.01) pets.(0.02) item(0.01) ships(-0.02) original(-0.00) carton(0.01) may(0.01) include(0.01) photo(0.02) product.(0.03) 
Node-1: product(-0.06) amazon(0.03) platform(0.03) title(0.07) content(0.02) title(0.02) american(0.01) girl(-0.02) starry(0.02) 2(0.03) doll(-0.01) tote(0.01) bag.(0.07) content(0.05) perfect(0.01) girls(-0.06) go!(-0.02) fabric(0.02) tote(0.03) plenty(0.08) room(0.03) hold(0.01) two(0.03) american(0.02) girl(-0.01) dolls,(0.02) exterior(0.05) pockets(0.02) holding(0.04) extra(0.02) outfits,(0.04) shoes,(0.05) accessories.(0.09) nylon.(0.10) imported.(0.05) raspberry.(0.06) w(0.07) 6(0.04) 1(0.03) 2(0.01) x(0.07) l(0.04) 16(0.03) 1(0.02) 2(-0.00) x(0.05) h(0.05) 8(0.01) 1(0.06) 2(0.06) 
Node-1.1: product(0.00) amazon(0.00) platform(0.00) title(0.00) content(0.00) title(0.00) 18(-0.00) inch(0.00) doll(0.00) backpack,(0.00) doll(0.00) size(0.00) 18(0.00) quot(0.00) doll(0.00) accessories(0.00) american(0.00) girl(0.00) dolls(0.01) purple(0.00) nylon,(0.00) zippered(0.00) opening(0.00) pocket(0.00) purple.(0.00) content(0.00) doll(0.00) plush(0.00) toy(0.00) sized(0.00) backpack!(0.00) backpack(0.00) sized(0.00) allow(0.00) take(0.00) accessories(0.00) go(0.00) doll(0.00) sized(0.00) backpack.(-0.00) 2013(0.00) sophia(0.00) s-(0.00) rights(-0.02) reserved(-0.01) 
Node-1.2: product(0.00) amazon(-0.00) platform(-0.00) title(-0.00) content(0.00) title(0.00) 3(0.01) pc.(0.01) gymnastics(-0.01) leotard,(0.00) jacket,(0.00) bag,(0.00) doll(-0.00) gymnastics(0.00) outfit(0.00) fits(0.00) 18(0.01) quot(-0.00) dolls(0.00) like(-0.00) american(-0.01) girl.(0.00) content(0.01) adorable(0.01) 3(0.00) piece(0.00) set(0.00) consists(0.00) stylish(0.00) aqua(0.01) gymnastics(0.00) leotard,(0.00) jacket,(0.00) coordinating(0.00) gym(0.00) bag!(0.00) doll(0.00) included.(0.01) hook(-0.00) loops(-0.00) top(-0.00) leotard(0.00) easy(0.00) dressing.(0.01) 2013(0.03) sophia(0.01) s-(0.02) rights(-0.01) reserved(-0.05) 
Node-1.3: product(-0.00) amazon(-0.00) platform(0.00) title(0.00) content(-0.00) title(0.00) missing.(0.00) content(0.01) saige(0.00) paints(-0.01) skyis(0.00) film(0.01) difficulties(0.00) change(0.00) speaking(0.00) believe(0.00) in.(-0.01) fourth-(0.00) grader(-0.00) saige(0.00) sidney(0.00) fullmer(0.00) crushed(-0.00) art(0.00) program(0.00) school(0.00) canceled(0.00) year(0.00) due(0.00) budget(0.01) cuts.(0.00) also(-0.00) upsetting(-0.00) fact(0.00) best(-0.00) friend(-0.00) tessa(0.01) alex(0.00) peters(0.01) made(0.00) new(0.00) best(0.00) friend(0.00) away(0.00) music(0.01) camp.(-0.00) saige(0.00) grandmother(-0.00) mimi(0.00) jane(0.01) seymour(0.01) ),(0.00) local(0.01) artist(0.01) horsewoman(0.00) always(0.00) saige(0.00) confidant,(0.00) encourages(0.01) saige(0.00) take(0.00) action(0.00) save(0.00) school(0.00) art(-0.00) program(0.00) friendship(0.01) tessa,(0.00) chance(0.00) accident(-0.00) threatens(-0.00) everyone(-0.00) resolve--(0.00) even(0.00) mimi(-0.01) s.(0.00) saige(0.00) fights(-0.00) preserve(-0.00) programs(0.00) relationships(-0.00) important(-0.00) her,(0.00) struggles(0.00) find(0.00) courage(0.00) act(0.00) learning(0.00) embrace(0.00) change.(-0.00) although(0.00) characters(0.00) seem(0.00) significantly(0.00) older(-0.00) fourth(0.00) graders(0.00) plot(0.00) points(0.00) completely(-0.00) believable,(-0.00) film(0.01) good(-0.00) job(0.00) portraying(-0.00) uncertainties(0.00) elementary(-0.00) middle(0.00) school(0.00) friendships(0.01) difficulty(0.00) standing(0.00) one(-0.00) believes(0.00) in.(0.00) ages(-0.00) 7(-0.00) older(0.01) )--(-0.00) tami(0.01) horiuchi(0.00) 
Node-1.4: product(-0.00) amazon(-0.00) platform(-0.00) title(-0.00) content(-0.00) title(-0.00) doll(-0.00) bicycle(-0.00) seat-(-0.00) quot(-0.00) ride(-0.00) along(0.00) dolly(0.00) quot(0.00) bike(-0.00) seat(-0.00) decorate(0.00) decals(-0.00) fits(0.00) 18(-0.00) quot(0.00) american(0.00) girl(-0.00) standard(-0.00) sized(-0.00) dolls(-0.00) stuffed(0.00) animals(0.00) ).(-0.00) content(0.00) doll(-0.00) bicycle(-0.00) seat-(-0.00) ride(0.00) alo</verbalized-graph>

### Classification Label
Cell Phones & Accessories

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 39419
- Title: Badger Basket Doll Bunk Beds With Ladder - Pink/White
- True class (canonical `y`): **Toys & Games**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Toys & Games**
- Prediction recorded by this method's pipeline: **Cell Phones & Accessories**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Badger Basket Doll Bunk Beds With Ladder - Pink/White. Content: Just right when doll friends come to visit. Our Doll Bunk Beds are built for two dolls to rest in style. Includes a ladder for extra fun and realism. Pretty pink gingham complements the attractive white finish. For Dolls up to 20" . Overall size of 11.5" x 22.25" x 15" . There is 6.75" clearance between the top and bottom bunks and 3.5" distance between the bottom bunk and the floor. Includes two removable mattresses (21.25" x 10" ) with attached pillows and eyelet trim. Pillow area of the mattress is approximately 3.5" x 10" . Ladder measures approximately 15" x 5" x 3/8" D. Can be enjoyed by children from three years old and up. All paints and finishes are non-toxic. Some adult assembly required. Illustrated instructions included. Made with wood and wood composites. Fabric parts are poly/cotton and stuffed with polyfill. Wipe wood parts clean with a damp cloth and mild detergent as needed. For longevity of the product, spot cleaning or hand washing recommended for the fabric parts (but you can machine wash gentle and air dry if desired). This item is a toy for use with dolls only. It is never to be used with real infants or pets. This item ships in its original carton which may include a photo of the product.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 9135 | Toys & Games | American Girl Starry 2 Doll Tote Bag |

### 2-hop (shortest distance exactly 2): 5 nodes

| node id | true class | title |
|---|---|---|
| 1089 | Toys & Games | 18 Inch Doll Backpack, Doll Size for 18&quot; Doll Accessories and American Girl Dolls in Purple Nylon, Zippered Opening and Pocket in Purple |
| 39346 | Toys & Games | 3 PC. Gymnastics Leotard, Jacket, and Bag, Doll Gymnastics Outfit Fits 18&quot; Dolls Like American Girl |
| 39417 | Movies & TV | missing |
| 39418 | Toys & Games | Doll Bicycle Seat - &quot;Ride Along Dolly&quot; Bike Seat with Decorate Yourself Decals (Fits 18&quot; American Girl and Standard Sized Dolls and Stuffed Animals) |
| 39420 | Toys & Games | Red and Yellow Roses Dress &amp; Sandals ~ Fits 18&quot; American Girl Dolls |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/147.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Cell Phones & Accessories**, ground truth = **Toys & Games**.
The verbalized graph is 8228 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 39419 | 266 | 0.0441 | yes |
| Node-1 | 1 | 9135 | 75 | 0.1037 | yes |
| Node-1.1 | 2 | 1089 | 72 | 0.0070 | yes |
| Node-1.2 | 3 | 39346 | 70 | 0.0308 | yes |
| Node-1.3 | 4 | 39417 | 222 | 0.0108 | yes |
| Node-1.4 | 5 | 39418 | 258 | 0.0068 | yes |
| Node-1.5 | 6 | 39420 | 64 | 0.0310 | no |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, ROOT->Node-1

### Tokens and scores

**ROOT** (global 39419):

~~~~~~text
product (-0.0092) from (0.0011) amazon (0.0114) platform (0.0019) with (-0.0130) title (0.0104) and (-0.0035) content (-0.0001) : (0.0084) title (-0.0111) : (0.0049) badger (0.0146) basket (0.0054) doll (-0.0124) bunk (-0.0244) beds (-0.0085) with (0.0154) ladder- (0.0021) pink (-0.0124) / (0.0031) white. (0.0081) content (-0.0011) : (-0.0028) just (0.0030) right (-0.0020) when (-0.0019) doll (-0.0006) friends (0.0018) come (0.0133) to (0.0142) visit. (-0.0288) our (0.0239) doll (-0.0097) bunk (-0.0129) beds (-0.0110) are (0.0094) built (0.0005) for (-0.0017) two (0.0021) dolls (-0.0048) to (0.0073) rest (0.0003) in (0.0015) style. (-0.0148) includes (-0.0238) a (-0.0100) ladder (0.0441) for (0.0049) extra (0.0069) fun (0.0136) and (0.0001) realism. (0.0182) pretty (0.0031) pink (-0.0008) gingham (0.0079) complements (0.0090) the (-0.0213) attractive (0.0084) white (0.0093) finish. (-0.0359) for (-0.0142) dolls (-0.0435) up (0.0173) to (0.0040) 20 (-0.0133) ". (0.0142) overall (0.0065) size (-0.0120) of (-0.0081) 11. (0.0138) 5 (-0.0127) " (-0.0097) x (-0.0212) 22. (0.0046) 25 (-0.0091) " (-0.0135) x (-0.0068) 15 (-0.0063) ". (0.0179) there (0.0017) is (0.0084) 6. (0.0126) 75 (0.0047) " (-0.0082) clearance (0.0066) between (-0.0021) the (-0.0106) top (0.0114) and (0.0023) bottom (0.0251) bunks (-0.0028) and (0.0070) 3. (0.0052) 5 (0.0018) " (-0.0122) distance (0.0103) between (0.0017) the (0.0036) bottom (0.0322) bunk (-0.0229) and (0.0123) the (-0.0065) floor. (-0.0036) includes (-0.0037) two (0.0055) removable (0.0142) mattresses (0.0129) ( (0.0089) 21. (0.0120) 25 (-0.0034) " (-0.0059) x (-0.0006) 10 (-0.0111) " (-0.0101) ) (-0.0024) with (-0.0040) attached (-0.0048) pillows (0.0047) and (-0.0002) eyelet (0.0024) trim. (0.0086) pillow (-0.0034) area (-0.0075) of (0.0002) the (-0.0026) mattress (-0.0105) is (0.0013) approximately (-0.0022) 3. (0.0101) 5 (0.0113) " (-0.0090) x (0.0058) 10 (-0.0000) ". (0.0125) ladder (-0.0192) measures (0.0183) approximately (0.0014) 15 (0.0032) " (-0.0022) x (0.0046) 5 (-0.0005) " (-0.0052) x (0.0001) 3 (0.0029) / (0.0067) 8 (0.0025) " (-0.0040) d. (0.0015) can (0.0092) be (0.0303) enjoyed (0.0291) by (-0.0040) children (0.0268) from (-0.0018) three (0.0154) years (0.0147) old (0.0031) and (0.0048) up. (0.0124) all (0.0089) paints (0.0186) and (0.0072) finishes (0.0248) are (0.0071) non- (0.0128) toxic. (0.0042) some (0.0123) adult (-0.0003) assembly (-0.0005) required. (0.0108) illustrated (0.0251) instructions (0.0206) included. (0.0095) made (-0.0037) with (0.0114) wood (0.0047) and (0.0084) wood (0.0075) composites. (0.0078) fabric (0.0047) parts (0.0039) are (0.0072) poly (0.0053) / (0.0062) cotton (0.0082) and (0.0071) stuffed (0.0131) with (0.0036) polyfill. (0.0039) wipe (0.0060) wood (0.0073) parts (0.0094) clean (0.0121) with (-0.0040) a (0.0031) damp (0.0137) cloth (0.0132) and (-0.0002) mild (0.0049) detergent (0.0036) as (0.0031) needed. (0.0091) for (-0.0072) longevity (0.0109) of (0.0018) the (-0.0098) product, (0.0013) spot (0.0120) cleaning (0.0125) or (0.0076) hand (0.0016) washing (-0.0005) recommended (0.0080) for (-0.0025) the (0.0006) fabric (0.0080) parts (0.0058) ( (0.0080) but (0.0219) you (0.0090) can (-0.0001) machine (0.0053) wash (0.0033) gentle (0.0134) and (0.0018) air (-0.0008) dry (0.0003) if (0.0064) desired (0.0097) ). (0.0291) this (-0.0010) item (-0.0101) is (0.0316) a (0.0303) toy (0.0141) for (0.0151) use (-0.0068) with (-0.0163) dolls (-0.0077) only. (0.0247) it (0.0245) is (0.0187) never (0.0190) to (0.0051) be (0.0060) used (-0.0062) with (-0.0131) real (0.0103) infants (-0.0143) or (-0.0090) pets. (0.0190) this (0.0340) item (0.0106) ships (-0.0217) in (0.0136) its (0.0215) original (-0.0018) carton (0.0093) which (0.0054) may (0.0092) include (0.0101) a (-0.0031) photo (0.0211) of (-0.0002) the (-0.0029) product. (0.0278)
~~~~~~

**Node-1** (global 9135):

~~~~~~text
product (-0.0552) from (0.0414) amazon (0.0338) platform (0.0267) with (0.0425) title (0.0660) and (0.0245) content (0.0244) : (0.0715) title (0.0153) : (-0.0098) american (0.0110) girl (-0.0168) starry (0.0184) 2 (0.0284) doll (-0.0073) tote (0.0119) bag. (0.0726) content (0.0538) : (0.0333) perfect (0.0123) for (0.0199) girls (-0.0598) on (0.0417) the (0.0275) go! (-0.0211) this (0.0496) fabric (0.0163) tote (0.0255) has (0.0240) plenty (0.0761) of (0.0509) room (0.0284) to (0.0528) hold (0.0095) two (0.0334) american (0.0158) girl (-0.0060) dolls, (0.0249) with (0.0586) exterior (0.0541) pockets (0.0186) for (0.0375) holding (0.0377) extra (0.0248) outfits, (0.0411) shoes, (0.0464) and (0.0781) accessories. (0.0928) nylon. (0.1037) imported. (0.0542) raspberry. (0.0579) w (0.0662) : (0.0549) 6 (0.0364) 1 (0.0343) / (0.0484) 2 (0.0144) " (0.0746) x (0.0733) l (0.0449) : (0.0667) 16 (0.0259) 1 (0.0241) / (0.0355) 2 (-0.0025) " (-0.0048) x (0.0525) h (0.0458) : (0.0814) 8 (0.0075) 1 (0.0625) / (0.0330) 2 (0.0633) " (-0.0474)
~~~~~~

**Node-1.1** (global 1089):

~~~~~~text
product (0.0029) from (0.0037) amazon (0.0034) platform (0.0007) with (0.0024) title (0.0022) and (0.0031) content (0.0036) : (0.0017) title (0.0038) : (0.0044) 18 (-0.0003) inch (0.0018) doll (0.0008) backpack, (0.0016) doll (0.0007) size (0.0026) for (0.0025) 18 (0.0019) & (0.0027) quot (0.0011) ; (-0.0000) doll (0.0010) accessories (0.0018) and (0.0036) american (0.0010) girl (0.0031) dolls (0.0051) in (0.0012) purple (0.0036) nylon, (0.0029) zippered (0.0033) opening (0.0028) and (0.0044) pocket (0.0040) in (0.0011) purple. (0.0005) content (0.0050) : (0.0040) doll (0.0014) or (0.0030) plush (0.0040) toy (0.0015) sized (0.0043) backpack! (0.0021) this (0.0011) backpack (0.0025) is (0.0042) sized (0.0025) to (0.0029) allow (0.0033) her (0.0047) to (0.0036) take (0.0030) her (0.0033) accessories (0.0010) on (0.0038) the (-0.0002) go (0.0041) in (0.0032) her (0.0021) own (0.0034) doll (0.0032) sized (0.0028) backpack. (-0.0035) 2013 (0.0028) sophia (0.0033) ' (0.0070) s- (0.0031) all (0.0003) rights (-0.0159) reserved (-0.0088)
~~~~~~

**Node-1.2** (global 39346):

~~~~~~text
product (0.0045) from (-0.0039) amazon (-0.0044) platform (-0.0015) with (-0.0013) title (-0.0013) and (-0.0015) content (0.0022) : (0.0014) title (0.0037) : (0.0028) 3 (0.0081) pc. (0.0058) gymnastics (-0.0084) leotard, (0.0009) jacket, (0.0020) and (0.0026) bag, (0.0025) doll (-0.0012) gymnastics (0.0014) outfit (0.0018) fits (0.0017) 18 (0.0058) & (0.0035) quot (-0.0025) ; (0.0088) dolls (0.0018) like (-0.0013) american (-0.0057) girl. (0.0029) content (0.0067) : (0.0057) this (0.0007) adorable (0.0064) 3 (0.0034) piece (0.0017) set (0.0025) consists (0.0021) of (-0.0010) a (-0.0044) stylish (0.0012) aqua (0.0061) gymnastics (0.0019) leotard, (0.0032) a (-0.0065) jacket, (0.0031) and (0.0028) coordinating (0.0041) gym (0.0011) bag! (0.0043) doll (0.0022) not (0.0012) included. (0.0099) hook (-0.0044) & (0.0098) loops (-0.0041) at (0.0010) top (-0.0024) of (-0.0011) leotard (0.0021) for (0.0065) easy (0.0044) dressing. (0.0092) 2013 (0.0295) sophia (0.0057) ' (0.0154) s- (0.0248) all (0.0308) rights (-0.0060) reserved (-0.0518)
~~~~~~

**Node-1.3** (global 39417):

~~~~~~text
product (-0.0009) from (-0.0008) amazon (-0.0045) platform (0.0019) with (-0.0011) title (0.0022) and (-0.0004) content (-0.0013) : (-0.0007) title (0.0013) : (0.0006) missing. (0.0010) content (0.0052) : (0.0027) saige (0.0017) paints (-0.0085) the (-0.0024) skyis (0.0026) a (0.0027) film (0.0063) about (-0.0040) the (-0.0015) difficulties (0.0005) of (-0.0031) change (0.0003) and (-0.0023) speaking (0.0008) up (-0.0003) for (0.0003) what (-0.0005) you (0.0015) believe (0.0001) in. (-0.0051) fourth- (0.0017) grader (-0.0019) saige (0.0024) ( (0.0010) sidney (0.0027) fullmer (0.0040) ) (0.0069) is (-0.0009) crushed (-0.0041) when (-0.0049) the (-0.0035) art (0.0010) program (0.0020) at (-0.0030) her (-0.0007) school (0.0002) is (-0.0003) canceled (0.0027) for (0.0014) the (-0.0012) year (0.0043) due (0.0011) to (-0.0005) budget (0.0056) cuts. (0.0003) also (-0.0011) upsetting (-0.0014) is (-0.0004) the (-0.0018) fact (0.0012) that (0.0003) her (0.0024) best (-0.0003) friend (-0.0017) tessa (0.0089) ( (0.0108) alex (0.0046) peters (0.0069) ) (-0.0015) made (0.0028) a (0.0015) new (0.0021) best (0.0024) friend (0.0040) while (0.0022) she (0.0040) was (0.0033) away (0.0025) at (0.0019) music (0.0090) camp. (-0.0034) saige (0.0024) ' (0.0018) s (0.0070) grandmother (-0.0016) mimi (0.0045) ( (0.0061) jane (0.0090) seymour (0.0062) ), (0.0008) who (0.0029) is (0.0042) a (0.0018) local (0.0072) artist (0.0071) and (0.0026) horsewoman (0.0043) and (0.0032) has (0.0045) always (0.0040) been (0.0015) saige (0.0043) ' (0.0038) s (0.0044) confidant, (0.0018) encourages (0.0053) saige (0.0025) to (-0.0008) take (0.0001) action (0.0017) to (-0.0006) save (0.0015) her (0.0015) school (0.0005) ' (-0.0007) s (0.0017) art (-0.0019) program (0.0004) and (0.0009) her (0.0039) friendship (0.0055) with (0.0015) tessa, (0.0036) but (-0.0006) a (0.0045) chance (0.0020) accident (-0.0010) threatens (-0.0043) everyone (-0.0004) ' (-0.0014) s (0.0004) resolve-- (0.0016) even (0.0020) mimi (-0.0058) ' (0.0005) s. (0.0011) as (-0.0015) saige (0.0031) fights (-0.0011) to (-0.0003) preserve (-0.0007) the (-0.0021) programs (0.0024) and (-0.0006) relationships (-0.0004) that (0.0006) are (-0.0001) most (0.0007) important (-0.0004) to (0.0006) her, (0.0013) she (0.0037) struggles (0.0012) to (0.0015) find (0.0010) the (-0.0010) courage (0.0019) to (0.0015) act (0.0022) while (-0.0002) learning (0.0023) to (0.0010) embrace (0.0005) change. (-0.0025) although (0.0007) the (-0.0009) characters (0.0040) seem (0.0028) significantly (0.0013) older (-0.0006) than (-0.0019) fourth (0.0037) graders (0.0010) and (-0.0018) some (-0.0001) of (-0.0015) the (-0.0023) plot (0.0019) points (0.0021) aren (-0.0010) ' (-0.0019) t (0.0021) completely (-0.0006) believable, (-0.0025) the (-0.0032) film (0.0094) does (0.0014) a (-0.0022) good (-0.0009) job (0.0027) of (0.0003) portraying (-0.0036) the (-0.0034) uncertainties (0.0027) of (0.0018) elementary (-0.0032) and (0.0013) middle (0.0006) school (0.0024) friendships (0.0059) and (-0.0013) the (-0.0005) difficulty (0.0001) of (-0.0007) standing (0.0013) up (0.0018) for (-0.0021) what (-0.0008) one (-0.0003) believes (0.0032) in. (0.0004) ( (-0.0117) ages (-0.0001) 7 (-0.0019) and (0.0024) older (0.0056) )-- (-0.0021) tami (0.0054) horiuchi (0.0034)
~~~~~~

**Node-1.4** (global 39418):

~~~~~~text
product (-0.0018) from (-0.0001) amazon (-0.0009) platform (-0.0017) with (-0.0022) title (-0.0018) and (-0.0022) content (-0.0001) : (-0.0002) title (-0.0025) : (0.0002) doll (-0.0019) bicycle (-0.0002) seat- (-0.0003) & (-0.0019) quot (-0.0001) ; (-0.0010) ride (-0.0013) along (0.0006) dolly (0.0014) & (0.0007) quot (0.0003) ; (0.0005) bike (-0.0043) seat (-0.0020) with (-0.0023) decorate (0.0023) yourself (-0.0028) decals (-0.0020) ( (-0.0019) fits (0.0004) 18 (-0.0007) & (0.0011) quot (0.0008) ; (-0.0021) american (0.0002) girl (-0.0017) and (-0.0022) standard (-0.0002) sized (-0.0003) dolls (-0.0020) and (-0.0016) stuffed (0.0013) animals (0.0006) ). (-0.0006) content (0.0015) : (-0.0015) doll (-0.0011) bicycle (-0.0004) seat- (-0.0002) " (-0.0003) ride (0.0002) along (0.0009) dolly (-0.0004) " (-0.0008) is (-0.0009) the (0.0007) perfect (-0.0008) way (-0.0008) to (-0.0003) show (0.0002) your (0.0001) loved (0.0002) doll (-0.0017) a (0.0011) good (0.0002) time. (0.0020) no (-0.0005) longer (0.0003) do (-0.0000) you (0.0010) have (-0.0008) to (-0.0011) leave (0.0007) your (0.0003) doll (0.0001) at (0.0000) home. (-0.0032) take (0.0001) your (0.0028) doll (-0.0020) along (0.0031) on (-0.0013) a (0.0011) fun- (-0.0010) filled (-0.0000) afternoon (-0.0016) bike (-0.0021) ride (-0.0009) around (0.0017) the (0.0024) neighborhood. (-0.0009) super (0.0009) easy (0.0005) to (-0.0005) attach (0.0014) to (0.0005) any (-0.0004) bicycle, (-0.0004) and (0.0017) sturdier (-0.0003) than (-0.0009) other (0.0000) seats (0.0007) with (-0.0003) a (0.0017) unique (0.0009) bar (0.0006) attachment (0.0009) and (0.0000) bolt (0.0004) included. (0.0021) also (-0.0008) includes (0.0001) seat (-0.0007) belt (0.0000) so (0.0005) your (0.0003) doll (-0.0004) can (-0.0003) be (-0.0008) just (-0.0009) as (-0.0005) safe (0.0000) as (-0.0009) you. (-0.0001) fun (0.0009) girl- (0.0011) themed (-0.0005) decals (-0.0002) adorn (-0.0013) his (0.0068) pink- (0.0008) a- (0.0006) licious (0.0009) colored (-0.0014) doll (0.0020) bike (0.0002) seat (-0.0020) for (-0.0011) added (-0.0005) fun. (-0.0005) affordably (0.0009) priced (0.0002) versus (0.0021) other (-0.0013) name (0.0015) brands (-0.0002) like (-0.0015) dolly (0.0000) come (0.0013) ride (-0.0013) with (-0.0009) me, (0.0000) ride (-0.0015) along (0.0013) dolly (0.0028) is (-0.0013) the (0.0035) perfect (0.0009) gift (-0.0016) for (0.0013) any (0.0001) doll (0.0026) enthused (0.0001) young (0.0003) girl. (0.0023) fits (0.0026) virtually (-0.0002) all (-0.0024) standard (0.0017) sized (0.0001) dolls (-0.0012) up (-0.0009) to (-0.0006) 3 (-0.0000) lbs, (0.0004) including (-0.0002) american (0.0003) girl (0.0019) dolls, (-0.0005) corolle (0.0002) dolls, (-0.0004) and (-0.0013) stuffed (-0.0003) animals. (-0.0003) note (-0.0015) : (-0.0017) ride (-0.0001) along (0.0023) dolly (0.0028) will (-0.0013) fit (-0.0001) on (0.0000) any (-0.0023) bike (0.0035) with (-0.0010) the (-0.0006) standard (0.0007) rear (0.0004) crossbar (-0.0003) with (-0.0006) a (-0.0000) hole, (0.0000) found (0.0011) on (0.0010) any (-0.0006) bikes. (-0.0001) it (0.0002) does (0.0005) not (-0.0001) matter (0.0005) if (-0.0013) you (-0.0010) have (-0.0006) a (0.0008) rear (-0.0015) brake (-0.0007) or (-0.0011) not. (0.0008) the (-0.0007) seat (0.0002) is (0.0001) designed (0.0005) to (-0.0005) work (0.0005) around (0.0006) such (-0.0015) brake (-0.0010) cords (0.0005) without (-0.0009) compromising (-0.0000) bike (-0.0006) or (-0.0005) seat (-0.0003) performance. (0.0018) ride (0.0000) along (-0.0049) dolly (0.0042) is (0.0020) not (0.0013) affiliate (0.0068) with (0.0027) or (0.0005) endorsed (0.0016) by (0.0015) american (0.0014) girl (0.0015) llc (0.0012) and (-0.0001) references (-0.0000) their (-0.0039) company (-0.0003) purely (0.0005) for (-0.0006) illustrative (-0.0010) purposes (-0.0001) only. (-0.0010)
~~~~~~

**Node-1.5** (global 39420):

~~~~~~text
product (-0.0050) from (0.0004) amazon (-0.0165) platform (-0.0181) with (0.0071) title (-0.0055) and (0.0027) content (0.0082) : (-0.0037) title (0.0161) : (0.0100) red (-0.0044) and (0.0116) yellow (0.0074) roses (0.0027) dress (0.0124) & (0.0110) amp (0.0100) ; (0.0082) sandals (0.0129) ~ (0.0061) fits (0.0160) 18 (0.0062) & (0.0156) quot (0.0017) ; (0.0023) american (0.0136) girl (0.0065) dolls. (0.0310) content (-0.0023) : (0.0126) yellow (0.0047) dress (0.0117) of (-0.0078) embroidered (0.0167) yellow (0.0115) organza (0.0055) trimmed (0.0090) at (0.0019) the (-0.0084) waist (0.0024) with (0.0047) layered (-0.0015) organza. (0.0037) the (-0.0028) silk (0.0031) lined (0.0052) gown (0.0123) cascades (0.0049) to (-0.0036) the (-0.0062) floor. (0.0005) an (0.0041) elegant (0.0167) pair (0.0102) of (-0.0005) sandals (0.0194) in (0.0155) matching (0.0057) yellow (0.0057) are (0.0150) the (-0.0070) perfect (0.0014) accessories. (-0.0202)
~~~~~~
