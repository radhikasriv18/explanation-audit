# Reference packet: GraphNarrator__Llama-70B__products__8485

- Method: GraphNarrator; configuration: Llama-70B; dataset: products; target node: 8485
- Explanation source: `./robustness_2026-10-30/llama70b/graphnarrator/products/8485.json` (response)
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

- ROOT (magnetic net release)
  - Node-1 (fly fishing guide)
    - Node-1.1 (fly fishing clamps)
    - Node-1.2 (fly floatant treatment)
    - Node-1.3 (fly casting workshop)

1. Word-Level Evaluation:

Keywords with high saliency scores in ROOT — "mcgill" (0.20), "net" (0.06), "release" (0.08), "magnetic" (0.05) — are strongly associated with fishing equipment. However, these words alone do not directly indicate a book. More generic terms like "product" (0.01) and "amazon" (0.07) carry negligible saliency and contribute little.

2. Graph-Level Aggregation:

Node-1 (fly fishing guide, keywords: "guide" (0.00), "fishing" (0.00), "revised" (0.00), "updated" (0.00)) is a direct neighbor with moderate saliency, identifying a fishing-related book whose close proximity to ROOT reinforces the classification. Indirect neighbors — Node-1.1 (fly fishing clamps), Node-1.2 (fly floatant treatment), Node-1.3 (fly casting workshop) — are all fishing accessories or related content, collectively confirming a fishing context across both hops.

### Free-Text Explanation
```markdown
The classification of ROOT into "Books" is supported by its own keywords and the co-purchase neighborhood.

ROOT: Although keywords like "mcgill" (0.20), "net" (0.06), and "release" (0.08) are associated with fishing equipment, they do not directly indicate a book. However, the context provided by neighboring nodes clarifies the classification.
  - Node-1: A fly fishing guide (keywords: "guide", "fishing", "revised", "updated") is a direct neighbor, strongly indicating a book. This node reinforces the "Books" context.
    - Node-1.1: Fly fishing clamps are a fishing accessory, supporting the fishing context.
    - Node-1.2: Fly floatant treatment is another fishing-related product, further confirming the fishing context.
    - Node-1.3: A fly casting workshop is a related content, collectively affirming the fishing context and, by extension, the "Books" classification.

In summary, ROOT's own keywords do not directly signal a book, but the entire co-purchase neighborhood consists of fishing-related content and accessories, providing robust evidence for the "Books" category, specifically a book about fishing.
```
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/30.json`).

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
<verbalized-graph>ROOT: product(0.01) amazon(0.07) platform(-0.06) title(0.04) content(0.02) title(0.05) wright(-0.05) amp(0.03) mcgill(0.20) magnetic(0.02) net(0.06) release.(0.08) content(0.03) w(-0.04) wmemnr(0.07) magnetic(0.05) net(-0.00) release(0.01) 
Node-1: product(0.00) amazon(-0.00) platform(0.00) title(0.00) content(0.00) title(0.00) orvis(0.00) fly-(-0.00) fishing(-0.00) guide,(0.00) completely(0.00) revised(0.00) updated(0.00) 400(0.00) new(-0.00) color(0.01) photos(0.01) illustrations.(0.00) content(0.01) guide(-0.00) may(0.00) single(0.00) valuable(0.00) item(0.00) novice(0.01) angler(-0.00) buy...(0.00) us(0.01) would(0.00) well(0.00) re-(0.00) read(0.01) sections(0.01) flies,(0.00) fly(0.00) selection,(0.00) stream(0.00) tactics(0.01) every(0.01) spring(0.00) pulling(0.01) waders(0.00) first(0.00) time.(-0.00) "--(0.01) rod(0.01) amp(0.01) reel(-0.00) 
Node-1.1: product(0.00) amazon(0.00) platform(-0.00) title(0.00) content(-0.00) title(0.00) dr.(0.00) slick(-0.00) standard(-0.00) clamps.(0.00) content(-0.00) clamps(-0.00) designed(0.00) myriad(-0.00) tasks(-0.00) like(-0.00) crushing(0.00) barbs,(0.00) removing(-0.00) hooks(-0.00) fish(-0.00) yourself!(0.00) ),(0.00) opening(-0.00) closing(-0.00) split(-0.00) shot,(0.00) knot-(0.00) tying,(0.00) cutting(-0.00) tippet,(0.00) etc.(0.00) knowing(0.00) tasks(-0.00) regularly(-0.00) perform(0.00) stream-(0.00) side(0.00) help(-0.00) select(0.00) clamp(-0.00) best(-0.00) suit(0.00) angling(-0.00) needs.(0.00) clamps(-0.00) tend(-0.00) personal(-0.00) item,(0.00) like(0.00) favorite(-0.00) rod(0.00) reel,(0.00) people(0.00) preferences(0.00) clamps.(-0.00) anglers(-0.00) like(-0.00) short(0.00) clamps(-0.00) others(0.00) prefer(0.00) long.(-0.00) like(-0.00) straight(-0.00) jaws(-0.00) others(0.00) prefer(0.00) curved.(0.00) many(0.00) like(-0.00) gold(-0.00) loops(-0.00) handles(-0.00) others(0.00) prefer(-0.00) stealth-(0.00) mode(-0.00) black.(0.00) so,(0.00) lose(-0.00) buddy(0.00) 5(-0.00) curved(-0.00) black(-0.00) clamp,(0.00) assume(-0.00) 4(-0.00) gold(-0.00) loop(-0.00) straight(-0.00) model(0.00) gave(-0.00) vest(0.00) clear(0.00) air.(0.00) salt(0.00) waterif(0.00) angling(-0.00) salt(-0.00) water,(0.00) consider(0.00) using(0.00) black(0.00) oxidized(-0.00) prism(0.00) finished(0.00) clamps(0.00) provide(-0.00) extra(-0.00) layer(-0.00) protection.(0.00) clamp(0.00) longevity(-0.00) salt(-0.00) water,(0.00) rinse(-0.00) clamps(-0.00) fresh(-0.00) water(0.00) apply(-0.00) little(-0.00) oil.(0.00) clamp(0.00) sizingmatch(-0.00) clamp(0.00) size(0.00) flies(0.00) using.(0.00) generally,(0.00) shorter(-0.00) clamp(0.00) smaller(-0.00) lighter(-0.00) jaws,(-0.00) longer(0.00) clamp(0.00) larger(0.00) heavier(-0.00) jaws.(0.00) 4-(-0.00) inch(-0.00) clamp(0.00) struggle(0.00) crushing(-0.00) barb(0.00) 4(0.00) streamer(0.00) 6-(-0.00) inch(-0.00) clamp(0.00) large(0.00) removing(0.00) 22(0.00) midge(-0.00) cluster(-0.00) fish.(-0.00) metalall(0.00) clamps(-0.00) made(0.00) 410(0.00) japanese(0.00) stainless(-0.00) steel(0.00) rockwell(0.00) hardness(0.00) 42.(0.00) dr.(0.00) slick(0.00) standard(-0.00) clamps(-0.00) popular(0.00) sizes(-0.00) 4(0.00) 6(-0.00) ".(0.00) designed(-0.00) handle(-0.00) streamside(-0.00) tasks(-0.00) like(0.00) hook(-0.00) removal,(0.00) barb(-0.00) crushing(0.00) 
Node-1.2: product(0.00) amazon(0.00) platform(-0.00) title(0.00) content(0.00) title(-0.00) loon(0.00) outdoors(0.00) hydrostop(-0.00) dry(-0.00) fly(0.00) indicator(-0.00) treatment.(-0.00) content(0.00) permanent(0.00) fly(0.00) floatant(0.00) treating(0.00) new(-0.00) flies(0.00) yarn(0.00) strike(-0.00) indicators.(-0.00) large(0.00) jar(0.00) treats(-0.00) hundreds(-0.00) flies,(-0.00) dozens(0.00) time,(0.00) giving(0.00) time(-0.00) water.(-0.00) outstanding(-0.00) treating(0.00) yarn-(0.00) type(0.00) indicators,(-0.00) pre-(0.00) treating(0.00) dubbing(0.00) even(0.00) waterproofing(0.00) tent(0.00) seams(0.00) similar(-0.00) gear.(0.00) use,(-0.00) simply(0.00) soak(0.00) fly(0.00) indicator(0.00) 5(-0.00) minutes(-0.00) let(0.00) dry(-0.00) overnight.(0.00) 2(-0.00) oz.(0.00) bottle(-0.00) treats(-0.00) hundreds(-0.00) flies.(0.00) 
Node-1.3: product(-0.00) amazon(-0.00) platform(-0.00) title(-0.00) content(-0.00) title(0.00) missing.(0.00) content(-0.00) learn(0.00) top(-0.00) fly(0.00) fishing(-0.00) presentation(0.00) casts(0.00) really(-0.00) catch(-0.00) fish.(0.00) intensive(-0.00) one(-0.00) one(-0.00) fly(-0.00) casting(-0.00) workshop(0.00) master(-0.00) fly(0.00) casting(-0.00) instructor(-0.00) carl(0.00) mcneil.(-0.00) indispensable(0.00) reference(0.00) years(-0.00) come(-0.00) never(-0.00) seen(-0.00) excellent(0.00) flycasting(0.00) footage-(-0.00) fly(-0.00) fisher(-0.00) journal(-0.00) casts(-0.00) catch(0.00) fish,(0.00) dvd(-0.00) brings(-0.00) gorgeous(-0.00) cinematography(-0.00) how-(-0.00) genre.(0.00) existing(-0.00) combination(0.00) visuals(0.00) enthralling,(-0.00) actually(-0.00) feel(-0.00) like(-0.00) going(0.00) school(-0.00) yet(0.00) video(-0.00) packed(-0.00) great(-0.00) casting(0.00) instruction(0.00) carl(-0.00) mcneil,(-0.00) federation(-0.00) fly(-0.00) fishers(-0.00) master(0.00) casting(-0.00) instructor(-0.00) "-(-0.00) american(-0.00) angler(0.00) magazine.(-0.00) filming(-0.00) exquisite.(0.00) settings(0.00) well(-0.00) chosen(0.00) purpose(-0.00) backdrop(-0.00) make(0.00) line(0.00) easy(0.00) see,(0.00) also(0.00) beautiful.(0.00) hurt(0.00) filming(0.00) flawless(0.00) too,(0.00) love(0.00) camera(0.00) following(0.00) wiggle(-0.00) casts(-0.00) towards(0.00) surface(-0.00) seen(-0.00) caster(0.00) perspective(-0.00) fly(0.00) going(-0.00) land.(0.00) "-(0.00) global(0.00) fly(-0.00) fishertake(-0.00) one(0.00) one(-0.00) fly(0.00) casting(-0.00) workshop(-0.00) federation(0.00) fly(0.00) fishers(-0.00) master(0.00) casting(-0.00) instructor(-0.00) carl(-0.00) mcneil(-0.00) demonstrates(0.00) essential(0.00) presentation(0.00) casts.(0.00) cast(0.00) explained(0.00) step(0.00) step(0.00) p</verbalized-graph>

### Classification Label
Books

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 8485
- Title: Wright &amp; McGill Magnetic Net Release
- True class (canonical `y`): **Sports & Outdoors**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Sports & Outdoors**
- Prediction recorded by this method's pipeline: **Books**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Wright &amp; McGill Magnetic Net Release. Content: W&M; WMEMNR Magnetic Net Release
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 12 nodes

| node id | true class | title |
|---|---|---|
| 998 | Books | The Orvis Fly-Fishing Guide, Completely Revised and Updated with Over 400 New Color Photos and Illustrations |
| 1001 | Tools & Home Improvement | Rapala Fishing Forceps 7 1/2 Inch |
| 1008 | Sports & Outdoors | Eagle Claw W&amp;M Streamside Lanyard |
| 8490 | Sports & Outdoors | Rio Perception Fly Line Floating Accurate Angling Freshwater Fishing |
| 8548 | Sports & Outdoors | Scientific Anglers Fluorocarbon II Leader |
| 8555 | Books | "Trout Streams of Southern New England: An Angler's Guide to the Watersheds of Connecticut, Rhode Island, and Massachusetts (Trout Streams)" |
| 8588 | Sports & Outdoors | Hardy Stainless Twin Retractor |
| 37290 | Sports & Outdoors | Scientific Anglers Fluorocarbon Tippet with Cutter 30-meters |
| 37291 | Sports & Outdoors | Fly Box + 100 Assorted Fly Fishing Fly Package |
| 37292 | Sports & Outdoors | Mojo Outdoors Wading Pole |
| 37293 | Sports & Outdoors | Greys GS Large Fly Box |
| 37294 | Sports & Outdoors | RIO Powerflex Trout Leader |

### 2-hop (shortest distance exactly 2): 46 nodes

| node id | true class | title |
|---|---|---|
| 76 | Sports & Outdoors | Dr. Slick Standard Clamps |
| 996 | Sports & Outdoors | Crystal River Live Release Net |
| 1002 | Sports & Outdoors | Eagle Claw Forceps Hook Remover |
| 1005 | Sports & Outdoors | Berkley 6-Inch Softouch Hemostat Pliers |
| 1006 | Sports & Outdoors | Hammers Collapsible Wading Staff Fishing Stick |
| 1010 | Sports & Outdoors | Frogs Fanny Fly Treatment |
| 6080 | Sports & Outdoors | Nite Ize C9S-03-TP01 Small Figure 9 Carabiner with Rope, Black, Two-Pack |
| 8479 | Books | "Colorado's Best Fly Fishing: Flies, Access, and Guide's Advice for the State's Premier Rivers (Headwater Guides)" |
| 8484 | Sports & Outdoors | Glacier Glove Alaska River Fleece Fingerless Fishing Glove |
| 8486 | Books | "The Orvis Guide to Prospecting for Trout: How to Catch Fish When There's No Hatch to Match, Revised Edition" |
| 8487 | Sports & Outdoors | Loon Outdoors Hydrostop Dry Fly and Indicator Treatment |
| 8488 | Movies & TV | missing |
| 8489 | Sports & Outdoors | Orvis Tie-fast Knot-tying Tool |
| 8491 | Sports & Outdoors | Loon Outdoors Top Ride Floatant and Desiccant |
| 8492 | Sports & Outdoors | Loon Outdoors Aquel Floatant |
| 8493 | Books | "Trout Streams of Wisconsin and Minnesota: An Angler's Guide to More Than 120 Rivers and Streams, Second Edition" |
| 8514 | Sports & Outdoors | Rapala Fishing Clipper |
| 8515 | Sports & Outdoors | Bill Dance Hook Remover |
| 8516 | Sports & Outdoors | Berkley 8-Inch Precision Grip Pliers |
| 8517 | Sports & Outdoors | "Caddis Men's Northern Guide Lightweight Taupe and Green Ecosmart Grip Sole Wading Shoe" |
| 8518 | Sports & Outdoors | Dr. Slick Scissor Clamps |
| 8561 | Sports & Outdoors | New Zealand Strike Indicator Tool |
| 8568 | Sports & Outdoors | Tooltron 6-Inch Locking Clamp Curved Tip Fish Hook Remover |
| 8570 | Sports & Outdoors | Chums Fly Fishing Lanyard |
| 8571 | Sports & Outdoors | Allen Company Black River Fishing Chest Pack/Fanny Pack |
| 8572 | Sports & Outdoors | ECO Dr. Slick Retractable Reel ::: Zinger Pin on Reel - Package of Five (5) |
| 8573 | Sports & Outdoors | TyRite Hook Holder |
| 8574 | Sports & Outdoors | Anglers Accessories Lightweight Rubber Tippet/Floatant Holder |
| 8575 | Sports & Outdoors | 20/20 Magnetic Tippet Threader |
| 8576 | Sports & Outdoors | "Loon Outdoors Nip 'N Sip Fishing Nippers and Bottle Opener" |
| 8577 | Sports & Outdoors | Allen Company Fox River Fishing Chest Pack, Twin Double Compartment |
| 8578 | Sports & Outdoors | Standard Fly Tying Kit with wooden box |
| 8579 | Sports & Outdoors | Magnetic Net Release |
| 8593 | Sports & Outdoors | Allen Company Fly Rod Case (For Up To 9-Feet Four Piece Rod with Reel Attached) |
| 37219 | Sports & Outdoors | Okuma Crisium Graphite 2-Piece Fly Rod |
| 37247 | Books | Simple Fly Fishing: Techniques for Tenkara and Rod and Reel |
| 37251 | Sports & Outdoors | Flies Direct Adams Assortment Trout Fishing Flies (1-Dozen) |
| 37308 | Sports & Outdoors | Scientific Anglers Supra Floating Fly Fly Line |
| 37309 | Sports & Outdoors | Scientific Anglers Sharkskin Ultimate Trout Fly Line |
| 37388 | Sports & Outdoors | Plastic Waterproof Fly Box - White |
| 37505 | Health & Personal Care | C&amp;F Design CFA-40 3-IN-1 Fly Fishing Tweezers New |
| 37506 | Sports & Outdoors | Gone Fishing Freshwater Flies, Pack of 55 |
| 37525 | Books | Trout Streams of Northern New England: A Guide to the Best Fly-Fishing in Vermont, New Hampshire, and Maine, First Edition |
| 37526 | Books | "White Mountain Guide, 29th: AMC's Comprehensive Guide to Hiking Trails in the White Mountain National Forest (Appalachian Mountain Club White Mountain Guide)" |
| 37527 | Books | Maine Atlas &amp; Gazetteer |
| 37579 | Sports & Outdoors | Tie-Fast Knot Tyer #1 Nail&euro;&#157; Knot Tool- Black |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/30.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Books**, ground truth = **Sports & Outdoors**.
The verbalized graph is 34582 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 8485 | 29 | 0.2029 | yes |
| Node-1 | 1 | 998 | 81 | 0.0110 | yes |
| Node-1.1 | 11 | 76 | 309 | 0.0031 | yes |
| Node-1.2 | 12 | 8487 | 90 | 0.0008 | yes |
| Node-1.3 | 13 | 8488 | 317 | 0.0011 | yes |
| Node-1.4 | 14 | 8486 | 141 | 0.0004 | no |
| Node-1.5 | 15 | 8484 | 75 | 0.0009 | no |
| Node-1.6 | 16 | 8491 | 142 | 0.0004 | no |
| Node-1.7 | 17 | 8492 | 129 | 0.0004 | no |
| Node-1.8 | 18 | 8493 | 58 | 0.0009 | no |
| Node-1.9 | 19 | 8489 | 79 | 0.0006 | no |
| Node-2 | 2 | 8490 | 159 | 0.0068 | no |
| Node-2.1 | 20 | 8579 | 140 | 0.0012 | no |
| Node-2.2 | 21 | 37219 | 101 | 0.0016 | no |
| Node-2.3 | 22 | 37309 | 34 | 0.0020 | no |
| Node-3 | 3 | 1001 | 53 | 0.0096 | no |
| Node-3.1 | 23 | 1006 | 136 | 0.0013 | no |
| Node-3.2 | 24 | 6080 | 47 | 0.0007 | no |
| Node-3.3 | 25 | 996 | 50 | 0.0007 | no |
| Node-3.4 | 26 | 8515 | 45 | 0.0018 | no |
| Node-3.5 | 27 | 8516 | 24 | 0.0010 | no |
| Node-3.6 | 28 | 8517 | 83 | 0.0011 | no |
| Node-3.7 | 29 | 8518 | 304 | 0.0005 | no |
| Node-3.8 | 30 | 8568 | 60 | 0.0004 | no |
| Node-4 | 4 | 8555 | 106 | 0.0141 | no |
| Node-4.1 | 31 | 37247 | 25 | 0.0011 | no |
| Node-4.2 | 32 | 37525 | 78 | 0.0008 | no |
| Node-4.3 | 33 | 37526 | 102 | 0.0010 | no |
| Node-4.4 | 34 | 37527 | 41 | 0.0007 | no |
| Node-5 | 5 | 8548 | 69 | 0.0053 | no |
| Node-5.1 | 35 | 1005 | 24 | 0.0022 | no |
| Node-5.2 | 36 | 8575 | 28 | 0.0027 | no |
| Node-5.3 | 37 | 37251 | 52 | 0.0011 | no |
| Node-5.4 | 38 | 37505 | 84 | 0.0005 | no |
| Node-5.5 | 39 | 37506 | 77 | 0.0011 | no |
| Node-6 | 6 | 37290 | 94 | 0.0141 | no |
| Node-7 | 7 | 37291 | 105 | 0.0315 | no |
| Node-8 | 8 | 37292 | 122 | 0.0132 | no |
| Node-8.1 | 40 | 8561 | 225 | 0.0014 | no |
| Node-9 | 9 | 37293 | 57 | 0.0127 | no |
| Node-10 | 10 | 37294 | 115 | 0.0064 | no |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->Node-1.6, Node-1->Node-1.7, Node-1->Node-1.8, Node-1->Node-1.9, Node-1->Node-2, Node-1->ROOT, Node-1.1->Node-1, Node-1.1->Node-3, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, Node-1.6->Node-1, Node-1.7->Node-1, Node-1.8->Node-1, Node-1.9->Node-1, Node-10->ROOT, Node-2->Node-1, Node-2->Node-2.1, Node-2->Node-2.2, Node-2->Node-2.3, Node-2->ROOT, Node-2.1->Node-2, Node-2.2->Node-2, Node-2.3->Node-2, Node-3->Node-1.1, Node-3->Node-3.1, Node-3->Node-3.2, Node-3->Node-3.3, Node-3->Node-3.4, Node-3->Node-3.5, Node-3->Node-3.6, Node-3->Node-3.7, Node-3->Node-3.8, Node-3->ROOT, Node-3.1->Node-3, Node-3.1->Node-4, Node-3.2->Node-3, Node-3.3->Node-3, Node-3.4->Node-3, Node-3.5->Node-3, Node-3.6->Node-3, Node-3.7->Node-3, Node-3.8->Node-3, Node-4->Node-3.1, Node-4->Node-4.1, Node-4->Node-4.2, Node-4->Node-4.3, Node-4->Node-4.4, Node-4->ROOT, Node-4.1->Node-4, Node-4.2->Node-4, Node-4.3->Node-4, Node-4.4->Node-4, Node-5->Node-5.1, Node-5->Node-5.2, Node-5->Node-5.3, Node-5->Node-5.4, Node-5->Node-5.5, Node-5->ROOT, Node-5.1->Node-5, Node-5.2->Node-5, Node-5.3->Node-5, Node-5.4->Node-5, Node-5.5->Node-5, Node-6->ROOT, Node-7->ROOT, Node-8->Node-8.1, Node-8->ROOT, Node-8.1->Node-8, Node-9->ROOT, ROOT->Node-1, ROOT->Node-10, ROOT->Node-2, ROOT->Node-3, ROOT->Node-4, ROOT->Node-5, ROOT->Node-6, ROOT->Node-7, ROOT->Node-8, ROOT->Node-9

### Tokens and scores

**ROOT** (global 8485):

~~~~~~text
product (0.0123) from (-0.0051) amazon (0.0716) platform (-0.0576) with (0.0195) title (0.0364) and (0.0109) content (0.0245) : (0.0298) title (0.0498) : (0.0793) wright (-0.0482) & (0.0870) amp (0.0313) ; (0.1292) mcgill (0.2029) magnetic (0.0238) net (0.0610) release. (0.0785) content (0.0278) : (0.0431) w (-0.0415) & (0.0993) m (0.0252) ; (0.0558) wmemnr (0.0672) magnetic (0.0496) net (-0.0043) release (0.0076)
~~~~~~

**Node-1** (global 998):

~~~~~~text
product (0.0016) from (0.0026) amazon (-0.0041) platform (0.0026) with (-0.0004) title (0.0022) and (0.0005) content (0.0047) : (0.0015) title (0.0040) : (0.0022) the (0.0038) orvis (0.0032) fly- (-0.0027) fishing (-0.0021) guide, (0.0005) completely (0.0035) revised (0.0041) and (0.0016) updated (0.0049) with (0.0010) over (0.0014) 400 (0.0009) new (-0.0008) color (0.0063) photos (0.0094) and (0.0012) illustrations. (0.0001) content (0.0074) : (0.0011) " (-0.0037) this (0.0044) guide (-0.0010) may (0.0013) be (0.0014) the (0.0034) single (0.0045) most (0.0035) valuable (0.0024) item (0.0041) a (0.0009) novice (0.0051) angler (-0.0001) can (0.0026) buy... (0.0003) and (0.0028) most (0.0032) of (0.0020) us (0.0056) would (0.0018) do (0.0022) well (0.0046) to (0.0008) re- (0.0008) read (0.0060) the (0.0024) sections (0.0051) on (0.0015) flies, (0.0023) fly (0.0021) selection, (0.0044) and (0.0015) stream (0.0037) tactics (0.0062) every (0.0057) spring (0.0037) before (0.0005) pulling (0.0062) on (0.0010) our (0.0070) waders (0.0037) for (0.0037) the (0.0046) first (0.0015) time. (-0.0042) "-- (0.0110) rod (0.0058) & (-0.0002) amp (0.0101) ; (-0.0049) reel (-0.0028)
~~~~~~

**Node-1.1** (global 76):

~~~~~~text
product (0.0000) from (0.0001) amazon (0.0001) platform (-0.0002) with (-0.0001) title (0.0002) and (0.0000) content (-0.0003) : (0.0002) title (0.0000) : (-0.0003) dr. (0.0001) slick (-0.0005) standard (-0.0003) clamps. (0.0001) content (-0.0000) : (-0.0002) clamps (-0.0002) are (0.0001) designed (0.0001) for (0.0001) a (0.0002) myriad (-0.0002) of (-0.0001) tasks (-0.0002) like (-0.0009) crushing (0.0007) barbs, (0.0002) removing (-0.0003) hooks (-0.0001) from (-0.0000) fish (-0.0004) ( (-0.0001) or (0.0000) yourself! (0.0001) ), (0.0001) opening (-0.0001) / (0.0001) closing (-0.0000) split (-0.0001) shot, (0.0002) knot- (0.0000) tying, (0.0002) cutting (-0.0000) tippet, (0.0001) etc. (0.0002) knowing (0.0000) what (-0.0001) tasks (-0.0001) you (0.0000) regularly (-0.0002) perform (0.0001) stream- (0.0000) side (0.0000) will (-0.0000) help (-0.0000) you (-0.0000) select (0.0001) the (-0.0000) clamp (-0.0000) ( (0.0000) s (0.0002) ) (0.0001) that (0.0000) best (-0.0000) suit (0.0000) your (0.0001) angling (-0.0000) needs. (0.0003) clamps (-0.0001) tend (-0.0000) to (-0.0000) be (0.0000) a (0.0001) very (0.0001) personal (-0.0001) item, (0.0000) and (-0.0001) like (0.0000) a (0.0001) favorite (-0.0000) rod (0.0000) or (-0.0001) reel, (0.0000) people (0.0000) have (-0.0001) preferences (0.0002) for (-0.0001) their (0.0000) clamps. (-0.0001) some (-0.0000) anglers (-0.0000) like (-0.0003) short (0.0001) clamps (-0.0002) and (-0.0000) others (0.0001) prefer (0.0001) long. (-0.0002) some (0.0001) like (-0.0001) straight (-0.0001) jaws (-0.0003) while (-0.0000) others (0.0002) prefer (0.0000) curved. (0.0001) many (0.0002) like (-0.0001) the (0.0001) gold (-0.0000) loops (-0.0001) / (0.0001) handles (-0.0001) and (0.0000) others (0.0001) prefer (-0.0001) the (0.0001) stealth- (0.0001) mode (-0.0001) black. (0.0001) so, (0.0001) if (0.0000) you (-0.0001) lose (-0.0001) your (0.0001) buddy (0.0003) ' (0.0001) s (0.0002) 5 (-0.0001) " (-0.0000) curved (-0.0001) black (-0.0001) clamp, (0.0001) don (0.0001) ' (-0.0000) t (0.0001) assume (-0.0002) the (0.0002) 4 (-0.0001) " (-0.0001) gold (-0.0001) loop (-0.0002) straight (-0.0001) model (0.0001) you (-0.0002) gave (-0.0000) him (0.0003) off (0.0001) your (0.0002) vest (0.0001) will (0.0001) clear (0.0001) the (0.0001) air. (0.0002) salt (0.0001) waterif (0.0001) you (0.0001) ' (0.0000) re (0.0002) angling (-0.0000) in (0.0001) salt (-0.0001) water, (0.0004) consider (0.0000) using (0.0000) the (0.0002) black (0.0002) oxidized (-0.0000) or (-0.0000) prism (0.0001) finished (0.0001) clamps (0.0001) which (0.0000) provide (-0.0001) an (-0.0000) extra (-0.0001) layer (-0.0001) of (-0.0001) protection. (0.0001) for (0.0000) clamp (0.0001) longevity (-0.0001) in (0.0001) salt (-0.0001) water, (0.0002) rinse (-0.0001) your (-0.0002) clamps (-0.0000) in (0.0001) fresh (-0.0001) water (0.0002) and (-0.0002) apply (-0.0002) a (0.0000) little (-0.0000) oil. (0.0003) clamp (0.0001) sizingmatch (-0.0000) the (0.0002) clamp (0.0001) to (0.0000) the (0.0002) size (0.0000) of (0.0000) the (0.0001) flies (0.0000) you (-0.0000) ' (-0.0001) re (-0.0000) using. (0.0001) generally, (0.0001) the (0.0000) shorter (-0.0000) the (0.0000) clamp (0.0001) the (0.0000) smaller (-0.0000) and (-0.0002) lighter (-0.0002) the (-0.0001) jaws, (-0.0000) and (-0.0002) the (0.0001) longer (0.0001) the (0.0001) clamp (0.0000) the (0.0000) larger (0.0000) and (-0.0002) heavier (-0.0001) the (0.0000) jaws. (0.0000) a (-0.0000) 4- (-0.0000) inch (-0.0003) clamp (0.0001) will (0.0002) struggle (0.0000) crushing (-0.0007) a (0.0003) barb (0.0000) on (0.0000) a (0.0001) # (-0.0001) 4 (0.0002) streamer (0.0002) and (0.0000) a (0.0002) 6- (-0.0000) inch (-0.0002) clamp (0.0001) will (0.0000) be (-0.0001) too (0.0000) large (0.0000) for (0.0001) removing (0.0001) a (0.0001) # (-0.0003) 22 (0.0002) midge (-0.0001) cluster (-0.0002) from (0.0000) a (0.0001) fish. (-0.0002) metalall (0.0000) clamps (-0.0001) are (0.0001) made (0.0001) from (-0.0000) 410 (0.0003) japanese (0.0004) stainless (-0.0001) steel (0.0002) with (-0.0000) a (0.0001) rockwell (0.0001) hardness (0.0003) of (-0.0000) 42. (0.0001) dr. (0.0004) slick (0.0009) standard (-0.0002) clamps (-0.0001) : (0.0004) all (-0.0002) the (-0.0001) most (-0.0003) popular (0.0003) sizes (-0.0002) from (0.0001) 4 (0.0004) " (-0.0006) to (-0.0010) 6 (-0.0003) ". (0.0004) designed (-0.0002) to (-0.0002) handle (-0.0002) all (-0.0001) your (0.0001) streamside (-0.0001) tasks (-0.0006) like (0.0002) hook (-0.0001) removal, (0.0001) barb (-0.0001) crushing (0.0031)
~~~~~~

**Node-1.2** (global 8487):

~~~~~~text
product (0.0001) from (0.0002) amazon (0.0000) platform (-0.0001) with (-0.0000) title (0.0000) and (-0.0001) content (0.0002) : (0.0001) title (-0.0003) : (0.0000) loon (0.0001) outdoors (0.0001) hydrostop (-0.0000) dry (-0.0000) fly (0.0001) and (-0.0000) indicator (-0.0001) treatment. (-0.0004) content (0.0004) : (-0.0001) permanent (0.0000) fly (0.0001) floatant (0.0001) for (0.0001) treating (0.0000) new (-0.0001) flies (0.0000) and (0.0000) yarn (0.0003) strike (-0.0002) indicators. (-0.0000) large (0.0001) jar (0.0000) treats (-0.0000) hundreds (-0.0002) of (0.0000) flies, (-0.0001) dozens (0.0001) at (-0.0000) a (0.0000) time, (0.0000) giving (0.0000) you (-0.0002) more (0.0001) time (-0.0000) on (-0.0001) the (0.0001) water. (-0.0000) outstanding (-0.0001) for (-0.0001) treating (0.0000) yarn- (0.0001) type (0.0001) indicators, (-0.0002) for (0.0000) pre- (0.0001) treating (0.0000) dubbing (0.0000) and (0.0001) even (0.0000) for (-0.0000) waterproofing (0.0000) tent (0.0002) seams (0.0000) and (-0.0000) similar (-0.0002) gear. (0.0001) to (-0.0003) use, (-0.0001) simply (0.0000) soak (0.0000) your (0.0001) fly (0.0001) or (-0.0001) indicator (0.0000) for (0.0000) 5 (-0.0002) minutes (-0.0003) and (0.0002) let (0.0001) dry (-0.0001) overnight. (0.0001) 2 (-0.0002) oz. (0.0003) bottle (-0.0005) treats (-0.0001) hundreds (-0.0005) of (-0.0002) flies. (0.0008)
~~~~~~

**Node-1.3** (global 8488):

~~~~~~text
product (-0.0000) from (-0.0000) amazon (-0.0001) platform (-0.0001) with (-0.0001) title (-0.0000) and (-0.0000) content (-0.0001) : (0.0001) title (0.0000) : (0.0001) missing. (0.0001) content (-0.0001) : (-0.0001) learn (0.0001) the (0.0001) top (-0.0000) fly (0.0001) fishing (-0.0002) presentation (0.0000) casts (0.0001) that (-0.0000) really (-0.0001) do (0.0001) catch (-0.0001) more (0.0000) fish. (0.0001) an (-0.0001) intensive (-0.0001) one (-0.0000) on (-0.0000) one (-0.0000) fly (-0.0000) casting (-0.0000) workshop (0.0000) with (-0.0002) master (-0.0001) fly (0.0000) casting (-0.0001) instructor (-0.0003) carl (0.0001) mcneil. (-0.0003) " (-0.0000) an (-0.0000) indispensable (0.0000) reference (0.0001) for (-0.0000) years (-0.0001) to (0.0000) come (-0.0001) " (-0.0000) never (-0.0000) have (0.0000) i (0.0000) seen (-0.0000) such (0.0000) excellent (0.0000) flycasting (0.0000) footage- (-0.0000) the (0.0001) fly (-0.0001) fisher (-0.0000) journal (-0.0001) " (-0.0001) casts (-0.0000) that (-0.0000) catch (0.0000) fish, (0.0000) a (0.0002) dvd (-0.0001) that (-0.0000) brings (-0.0001) gorgeous (-0.0001) cinematography (-0.0001) to (-0.0002) the (-0.0001) how- (-0.0000) to (0.0000) genre. (0.0002) it (0.0000) ' (0.0000) s (0.0001) a (0.0001) very (0.0000) existing (-0.0000) combination (0.0000) because (-0.0001) the (-0.0001) visuals (0.0002) are (-0.0000) so (-0.0000) enthralling, (-0.0000) you (0.0001) don (-0.0000) ' (-0.0000) t (0.0001) actually (-0.0001) feel (-0.0000) like (-0.0000) you (0.0000) ' (-0.0001) re (0.0001) going (0.0000) to (-0.0001) school (-0.0000) yet (0.0001) the (0.0000) video (-0.0000) is (0.0002) packed (-0.0000) with (-0.0001) great (-0.0000) casting (0.0000) instruction (0.0001) from (0.0000) carl (-0.0002) mcneil, (-0.0001) a (0.0001) federation (-0.0000) of (0.0001) fly (-0.0001) fishers (-0.0002) master (0.0000) casting (-0.0000) instructor (-0.0002) "- (-0.0000) american (-0.0001) angler (0.0001) magazine. (-0.0000) " (0.0000) the (0.0000) filming (-0.0000) is (0.0001) exquisite. (0.0002) the (-0.0000) settings (0.0001) are (0.0001) well (-0.0000) chosen (0.0001) for (-0.0001) the (0.0000) purpose (-0.0000) and (-0.0001) not (0.0000) only (-0.0000) does (0.0001) the (0.0000) backdrop (-0.0000) make (0.0001) the (0.0000) line (0.0001) very (0.0000) easy (0.0001) to (0.0000) see, (0.0001) but (0.0001) it (0.0000) ' (-0.0000) s (0.0001) also (0.0000) beautiful. (0.0001) it (0.0000) doesn (0.0001) ' (-0.0000) t (0.0000) hurt (0.0000) that (0.0000) the (-0.0000) filming (0.0001) is (0.0000) flawless (0.0001) too, (0.0000) and (-0.0001) i (0.0000) love (0.0000) the (0.0001) camera (0.0002) following (0.0000) the (0.0002) wiggle (-0.0000) casts (-0.0000) down (0.0001) towards (0.0000) the (0.0000) surface (-0.0000) seen (-0.0000) from (0.0000) both (-0.0000) the (0.0000) caster (0.0001) ' (0.0000) s (0.0000) perspective (-0.0000) and (-0.0000) from (0.0000) where (-0.0001) the (-0.0000) fly (0.0000) is (0.0000) going (-0.0000) to (-0.0000) land. (0.0001) "- (0.0000) global (0.0001) fly (-0.0000) fishertake (-0.0000) a (0.0001) one (0.0000) on (-0.0001) one (-0.0000) fly (0.0000) casting (-0.0000) workshop (-0.0001) with (-0.0000) federation (0.0000) of (0.0000) fly (0.0001) fishers (-0.0001) master (0.0000) casting (-0.0001) instructor (-0.0000) carl (-0.0001) mcneil (-0.0000) as (-0.0000) he (-0.0000) demonstrates (0.0001) the (0.0000) essential (0.0002) presentation (0.0001) casts. (0.0002) each (0.0000) cast (0.0000) is (0.0001) explained (0.0000) step (0.0000) by (-0.0001) step (0.0000) in (-0.0001) plain (0.0001) simple (0.0001) language (0.0001) with (-0.0001) the (0.0000) assistance (0.0001) of (-0.0001) slow (0.0001) motion (0.0001) and (-0.0000) graphical (-0.0002) overlays. (0.0001) these (-0.0001) casts (0.0000) should (-0.0002) be (0.0001) considered (-0.0001) vital (-0.0001) ammunition (-0.0001) in (-0.0001) the (0.0000) arsenal (-0.0001) of (-0.0001) all (-0.0002) fly (-0.0001) anglers (0.0002) of (-0.0000) both (0.0000) fresh (-0.0000) and (-0.0000) salt (-0.0001) water. (-0.0000) in (-0.0001) addition (-0.0001) to (0.0002) the (-0.0000) slack (0.0004) line (0.0001) presentation (0.0002) casts (0.0001) mcneil (-0.0002) covers (0.0002) the (0.0003) roll (-0.0000) cast, (0.0000) bill (0.0000) gammel (-0.0001) ' (0.0000) s (0.0001) five (0.0000) essentials (0.0001) of (-0.0001) good (-0.0001) fly (0.0000) casting (0.0001) and (0.0001) dealing (0.0003) with (-0.0000) windy (0.0005) conditions. (0.0001) featuring (-0.0002) : (0.0002) the (-0.0000) five (0.0001) essentials (0.0001) of (0.0001) good (-0.0000) fly (0.0000) castingroll (0.0001) castreach (0.0000) mendpile (0.0000) castwiggle (0.0000) castaerial (-0.0000) mendbucket (0.0000) mendtuck (-0.0000) castcurve (0.0001) castsdealing (-0.0000) with (0.0011) the (0.0000)
~~~~~~

**Node-1.4** (global 8486):

~~~~~~text
product (-0.0001) from (-0.0001) amazon (0.0001) platform (0.0000) with (-0.0001) title (-0.0001) and (-0.0000) content (-0.0001) : (-0.0000) title (-0.0000) : (0.0000) " (-0.0000) the (0.0000) orvis (0.0000) guide (-0.0000) to (0.0002) prospecting (0.0000) for (0.0000) trout (-0.0000) : (-0.0001) how (-0.0000) to (0.0001) catch (-0.0000) fish (0.0000) when (0.0000) there (-0.0000) ' (-0.0001) s (-0.0001) no (0.0001) hatch (0.0000) to (0.0002) match, (-0.0000) revised (0.0001) edition (-0.0000) ". (0.0001) content (-0.0000) : (-0.0000) in (0.0000) this (0.0000) comprehensive (-0.0000) and (0.0001) readable (0.0000) guide, (-0.0000) tom (-0.0001) rosenbauer (0.0000) shares (-0.0000) his (-0.0001) vast (0.0001) knowledge (-0.0000) of (-0.0000) fly (-0.0001) fishing (-0.0001) when (0.0000) there (0.0000) is (0.0000) no (-0.0000) hatch. (0.0001) written (-0.0000) for (0.0000) both (0.0000) the (-0.0000) novice (-0.0000) and (0.0000) the (-0.0001) seasoned (0.0001) angler, (0.0000) the (0.0001) orvis (0.0000) guide (-0.0000) to (0.0000) prospecting (-0.0001) for (-0.0002) trout, (-0.0001) new (0.0001) and (0.0003) revised (-0.0003) explores (0.0001) how (-0.0001) trout (0.0001) live (-0.0001) and (-0.0000) feed, (0.0000) and (0.0001) how (-0.0001) to (0.0000) make (-0.0000) them (0.0000) strike, (0.0000) with (0.0000) a (-0.0001) thoroughly (-0.0002) updated (0.0001) text (-0.0001) that (-0.0001) addresses (-0.0000) state- (0.0000) of- (0.0000) the- (0.0000) art (-0.0000) approaches, (-0.0000) and (0.0001) all (0.0001) new (0.0001) color (0.0001) photography. (-0.0001) there (0.0001) is (0.0002) expert (-0.0001) advice (0.0002) on (0.0002) how (0.0000) to (0.0000) fish (0.0000) with (0.0000) dry (0.0000) flies, (0.0000) wet (0.0001) flies, (-0.0000) nymphs, (0.0001) and (0.0001) streamers (-0.0000) & (-0.0001) mdash (-0.0000) ; (0.0004) supported (0.0001) by (-0.0001) many (0.0001) detailed (0.0001) illustrations (0.0002) and (0.0001) photos. (-0.0001) this (-0.0001) is (0.0000) the (-0.0000) guide (-0.0000) no (0.0001) trout (0.0001) fisherman (-0.0001) should (0.0000) be (0.0001) without. (0.0001)
~~~~~~

**Node-1.5** (global 8484):

~~~~~~text
product (-0.0001) from (0.0001) amazon (0.0006) platform (0.0003) with (0.0001) title (0.0006) and (0.0001) content (0.0005) : (0.0004) title (0.0007) : (0.0004) glacier (0.0006) glove (0.0007) alaska (-0.0002) river (-0.0002) fleece (0.0001) fingerless (-0.0001) fishing (0.0000) glove. (0.0008) content (0.0006) : (0.0009) the (-0.0001) glacier (0.0003) glove (0.0007) alaska (0.0001) river (-0.0003) series (0.0003) was (0.0000) designed (0.0005) for (0.0001) the (-0.0000) unpredictable (0.0000) weather (0.0005) that (0.0003) alaska (0.0003) is (0.0004) known (0.0003) for. (-0.0001) it (0.0003) features (0.0002) a (0.0003) g- (0.0003) tek (0.0002) 2mm (0.0002) fleece (0.0003) lined (0.0002) neoprene (0.0003) palm (-0.0001) for (0.0001) grip (0.0006) and (0.0003) a (0.0002) windproof (0.0003) fleece (0.0003) back. (0.0001) the (0.0004) fingerless (0.0004) design (0.0008) allows (0.0003) you (0.0002) maintain (0.0002) the (0.0000) dexterity (0.0003) you (0.0003) need (0.0004) for (0.0003) the (0.0001) complicated (0.0005) tasks (0.0009) you (0.0001) experience (0.0004) while (0.0001) enjoying (0.0005) the (0.0002) outdoors (0.0007)
~~~~~~

**Node-1.6** (global 8491):

~~~~~~text
product (0.0002) from (0.0002) amazon (0.0001) platform (0.0002) with (0.0002) title (-0.0001) and (0.0003) content (0.0002) : (0.0000) title (-0.0001) : (0.0001) loon (0.0000) outdoors (0.0003) top (0.0002) ride (0.0002) floatant (0.0001) and (0.0002) desiccant. (0.0000) content (0.0002) : (0.0001) known (0.0000) as (0.0000) " (0.0000) shake (0.0001) and (0.0003) bake (0.0001) " (-0.0001) by (0.0002) world (-0.0000) class (0.0002) guides, (0.0000) this (0.0002) desiccant (0.0001) ( (0.0001) drying (0.0002) agent (0.0001) ) (-0.0001) and (0.0001) powder (0.0002) floatant (0.0001) is (0.0001) fast (0.0002) and (0.0002) easy (0.0001) to (0.0001) use. (-0.0000) a (-0.0001) fly (0.0001) ( (0.0002) still (0.0001) attached (0.0002) to (0.0001) the (-0.0001) leader (0.0002) ) (-0.0001) goes (0.0001) in (0.0001) wet, (0.0001) and (0.0002) a (0.0000) few (0.0000) shakes (0.0003) later (-0.0000) comes (0.0001) out (0.0000) dry (0.0001) and (0.0002) coated (0.0002) with (0.0002) a (-0.0001) powder (0.0002) floatant. (0.0002) open (-0.0000) flip (0.0000) lid (0.0002) and (0.0001) drop (0.0002) fly (0.0001) attached (0.0000) to (0.0001) leader (0.0001) into (0.0002) container. (0.0002) hold (0.0000) lid (0.0002) closed (0.0002) without (0.0001) snapping (0.0002) shut, (0.0001) and (0.0001) shake (0.0001) a (-0.0000) few (-0.0000) times. (0.0000) false (0.0004) cast (0.0002) or (0.0001) blow (0.0001) on (0.0001) fly (0.0002) to (0.0002) remove (0.0000) excess (0.0002) powder. (0.0003) for (0.0001) best (0.0002) results, (0.0001) coat (0.0000) fly (-0.0000) with (0.0001) aquel (0.0001) or (0.0000) royal (-0.0001) gel (0.0003) prior (-0.0002) to (0.0000) applying (-0.0000) top (0.0002) ride. (-0.0001) powder (0.0001) floatant (0.0001) and (0.0003) drying (0.0001) agent (0.0001) in (0.0002) oneeasy (0.0001) to (0.0003) use (0.0001) shake (0.0001) applicationlarge (0.0001) cap (0.0000) opening (0.0001) for (0.0002) any (0.0002) size (0.0002) flyquick (0.0000) dry (0.0000) powderperfect (0.0001) for (0.0000) dry (-0.0000) fly (-0.0001) fishing (-0.0001)
~~~~~~

**Node-1.7** (global 8492):

~~~~~~text
product (0.0002) from (0.0002) amazon (0.0002) platform (0.0001) with (0.0003) title (0.0001) and (0.0002) content (0.0002) : (0.0001) title (0.0001) : (0.0001) loon (0.0001) outdoors (0.0003) aquel (0.0001) floatant. (0.0001) content (0.0002) : (0.0001) this (0.0004) premium (0.0000) gel (0.0003) floatant (0.0001) is (0.0000) the (-0.0000) world (0.0001) ' (0.0000) s (-0.0001) best (0.0000) fly (0.0001) floatant. (0.0001) aquel (-0.0000) is (0.0001) long (0.0001) lasting, (0.0000) silicon (0.0002) based (0.0000) and (0.0001) won (0.0000) ' (-0.0000) t (0.0000) melt (0.0001) when (0.0000) it (0.0001) ' (-0.0000) s (0.0000) hot (0.0000) or (0.0001) harden (0.0001) when (-0.0002) it (-0.0006) ' (-0.0000) s (-0.0003) cold. (-0.0002) furthermore, (0.0002) it (-0.0000) masks (0.0001) human (0.0000) odor (0.0002) and (0.0000) won (0.0001) ' (-0.0000) t (0.0001) leave (0.0000) any (-0.0000) slick (0.0001) on (0.0001) even (0.0001) the (-0.0000) calmest (0.0000) water. (0.0000) ( (0.0000) pronounced (0.0003) " (-0.0000) ahh (0.0001) kwel (-0.0000) " (-0.0000) ). (0.0002) prior (-0.0002) to (0.0001) first (0.0002) cast, (0.0000) apply (0.0002) desired (0.0002) amount (-0.0000) of (-0.0001) aquel (-0.0001) to (0.0000) fly. (0.0001) use (0.0002) fingers (0.0000) to (0.0002) work (0.0000) aquel (0.0000) into (0.0001) hair (0.0001) and (0.0001) hackle. (0.0000) if (0.0000) fly (0.0001) becomes (0.0001) water (0.0001) logged, (0.0000) use (0.0002) powder (0.0000) desiccant (0.0001) to (0.0000) dry, (0.0001) then (0.0001) reapply. (-0.0000) premium (-0.0000) dry (-0.0000) fly (0.0001) gel (0.0000) floatanttemperature (0.0000) stablesilicon (0.0002) basedwill (-0.0002) not (0.0000) leave (0.0000) oil (-0.0001) slick (-0.0000) on (0.0001) waterofficial (0.0001) floatant (0.0000) of (0.0004) fly (0.0001) fishing (0.0001) team (0.0002) usamasks (0.0001) human (0.0000) scent (0.0003)
~~~~~~

**Node-1.8** (global 8493):

~~~~~~text
product (0.0003) from (0.0000) amazon (0.0003) platform (0.0004) with (0.0000) title (-0.0001) and (0.0000) content (0.0003) : (-0.0002) title (0.0001) : (0.0000) " (0.0001) trout (-0.0005) streams (0.0002) of (-0.0000) wisconsin (-0.0001) and (-0.0001) minnesota (0.0002) : (0.0001) an (0.0000) angler (0.0000) ' (-0.0001) s (-0.0001) guide (-0.0000) to (-0.0001) more (-0.0002) than (-0.0001) 120 (0.0000) rivers (-0.0000) and (0.0001) streams, (0.0000) second (0.0000) edition (0.0003) ". (0.0002) content (0.0001) : (0.0002) fly- (-0.0001) fishing (0.0001) is (0.0001) about (-0.0003) discovery. (0.0007) have (0.0001) an (-0.0002) itch (0.0000) to (-0.0000) discover (0.0000) a (0.0002) stream? (0.0000) this (0.0001) book (-0.0003) will (-0.0000) scratch (0.0000) it.-- (0.0001) craig (0.0002) lincoln, (-0.0001) duluth (0.0006) news- (0.0001) tribune (0.0009)
~~~~~~

**Node-1.9** (global 8489):

~~~~~~text
product (-0.0003) from (0.0002) amazon (0.0003) platform (-0.0000) with (-0.0006) title (0.0006) and (-0.0001) content (-0.0002) : (0.0005) title (0.0001) : (0.0002) orvis (-0.0001) tie- (-0.0001) fast (-0.0001) knot- (-0.0002) tying (-0.0002) tool. (0.0000) content (0.0000) : (0.0002) found (-0.0001) hanging (-0.0000) from (-0.0000) lanyards (0.0001) and (0.0002) in (0.0002) drift (0.0001) boats (0.0001) all (0.0002) across (0.0001) the (-0.0000) world, (0.0000) the (-0.0001) tie- (0.0001) fast (0.0000) knot- (0.0000) tying (-0.0001) tool (-0.0002) will (0.0002) have (0.0002) you (0.0001) tying (-0.0000) nail (-0.0003) knots (-0.0002) in (0.0000) seconds. (0.0003) from (0.0001) seasoned (-0.0001) guides (0.0002) to (0.0002) first- (0.0001) time (0.0002) anglers, (0.0001) nail (-0.0001) knots (-0.0003) will (0.0001) become (0.0000) an (-0.0000) afterthought (0.0002) with (0.0000) this (0.0002) perfectly (-0.0002) designed (0.0003) and (0.0002) extremely (0.0002) handy (0.0002) stainless (0.0006) steel (0.0006) nail (0.0004) knot (0.0000) tyer (-0.0000) tool. (0.0003) step- (0.0002) by- (0.0001) step (-0.0000) instructions (0.0002) included. (0.0001) made (-0.0000) in (-0.0000) usa. (0.0000)
~~~~~~

**Node-2** (global 8490):

~~~~~~text
product (-0.0015) from (-0.0003) amazon (0.0015) platform (-0.0009) with (0.0017) title (0.0010) and (0.0006) content (0.0026) : (0.0023) title (0.0022) : (0.0026) rio (-0.0015) perception (0.0016) fly (0.0015) line (-0.0003) floating (0.0021) accurate (0.0025) angling (0.0011) freshwater (0.0007) fishing. (-0.0012) content (0.0018) : (0.0012) our (-0.0006) revolutionary (0.0038) rio (-0.0025) perception (0.0027) floating (0.0023) trout (0.0025) line (0.0010) helps (0.0015) anglers (0.0009) connect (0.0009) with (0.0016) more (0.0019) fish (0.0007) than (0.0013) ever (0.0021) before. (0.0002) built (0.0010) with (0.0016) ultra- (0.0014) low (0.0017) stretch (0.0029) connectcore (0.0018) technology, (0.0007) perception (-0.0002) lines (-0.0002) provide (0.0005) groundbreaking (0.0028) levels (0.0007) of (0.0003) sensitivity (0.0011) for (0.0012) intuitively (0.0011) better (0.0015) cast (0.0024) timing, (0.0017) easier (0.0019) line (0.0011) lift (0.0022) and (0.0017) sharp, (0.0013) precise (0.0012) mends. (0.0010) lack (0.0029) of (0.0009) stretch (0.0023) also (0.0013) means (0.0011) enhanced (0.0016) detection (0.0046) of (0.0054) subtle (0.0064) takes (-0.0009) and (0.0051) faster (0.0068) reaction (0.0006) time (0.0056) when (0.0035) setting (0.0025) the (-0.0053) hook. (0.0009) our (0.0033) exclusive (0.0039) surefire (0.0032) color (0.0030) system (0.0030) ( (0.0036) rios (0.0024) uniquetri- (0.0018) color (0.0031) distance (0.0039) measure (0.0027) ) (0.0011) improves (0.0007) casting (0.0033) accuracy (0.0039) by (0.0023) making (0.0021) it (0.0020) easy (0.0028) to (0.0024) gauge (0.0038) exact (0.0019) distances (0.0035) with (0.0021) a (-0.0019) quick (0.0043) glance. (0.0008) unique (0.0039) three- (0.0021) color (0.0031) surefire (0.0029) system (0.0012) ensures (-0.0005) deadly (0.0020) accurate (0.0018) distance (0.0017) controlconnectcore (0.0009) improves (-0.0006) casting (0.0016) timing, (0.0001) hook (0.0008) set (0.0015) and (0.0008) mendingeasyid (0.0001) tag (0.0030) to (0.0013) quickly (0.0016) identify (-0.0001) fly (0.0015) linewinner (0.0006) of (0.0006) best (0.0004) new (-0.0003) fly (0.0022) line (-0.0006) for (0.0011) 2014 (-0.0001) at (0.0015) efttex (0.0003) and (0.0024) iftd (0.0005) showsrios (0.0013) maxfloat (0.0005) tips (0.0004) float (0.0005) more (0.0019) than (0.0008) twice (0.0018) as (0.0015) high (0.0007) as (0.0017) regular (0.0007) line (0.0019) tips, (0.0009) without (0.0031) more (0.0006) diameter (-0.0119)
~~~~~~

**Node-2.1** (global 8579):

~~~~~~text
product (0.0002) from (0.0001) amazon (-0.0004) platform (-0.0001) with (0.0002) title (0.0000) and (0.0006) content (0.0003) : (0.0000) title (0.0003) : (-0.0001) magnetic (-0.0002) net (0.0002) release. (0.0005) content (0.0005) : (-0.0001) this (0.0005) device (0.0010) holds (0.0004) your (0.0000) net (0.0001) securely (0.0006) when (0.0001) not (0.0001) being (0.0004) used. (0.0002) one (-0.0000) hand (0.0004) operation (0.0004) allows (0.0003) you (0.0007) to (0.0000) release (-0.0001) your (-0.0000) net (-0.0000) when (0.0001) needed (0.0005) by (-0.0001) simply (0.0003) grasping (0.0002) the (0.0006) handle (0.0006) and (0.0005) giving (0.0005) it (0.0004) a (0.0005) tug. (-0.0003) strong (-0.0001) nickel (0.0003) plated (0.0001) magnets (0.0002) provide (0.0003) 7 (0.0004) + (0.0001) pounds (0.0005) of (-0.0003) pull (0.0003) to (0.0002) hold (0.0001) your (-0.0002) net (-0.0000) safely (-0.0001) out (0.0002) of (-0.0001) the (0.0002) way (0.0001) until (0.0002) you (0.0004) need (0.0002) it (0.0003) just (0.0002) get (0.0003) the (0.0003) magnets (0.0002) close (-0.0001) and (-0.0001) they (0.0008) " (-0.0017) jump (-0.0003) " (-0.0008) back (0.0003) together. (0.0005) equipped (-0.0008) with (-0.0004) 2 (-0.0001) brass (0.0001) split (0.0001) rings (0.0004) to (0.0001) attach (-0.0001) each (-0.0001) end (0.0000) to (0.0000) your (-0.0002) net, (0.0001) vest, (0.0001) pack, (0.0001) belt, (0.0003) etc. (-0.0004) or (0.0002) use (0.0001) the (-0.0000) holder (0.0001) of (-0.0001) your (0.0002) choice (0.0001) such (-0.0001) as (0.0001) cords (-0.0001) catle- (0.0001) ties, (0.0004) or (0.0003) clips. (0.0005) the (0.0006) units (0.0005) are (0.0004) molded (0.0004) from (0.0000) durable (0.0001) yet (0.0007) lightweight (-0.0002) uv (-0.0002) rated (-0.0002) vinyl (0.0000) that (-0.0002) prevents (-0.0001) sun (-0.0002) damage. (-0.0003) a (0.0001) convenient (0.0008) out- (0.0000) of- (-0.0003) the- (0.0000) way (0.0001) solution (-0.0000) for (-0.0002) carring (0.0001) your (-0.0066) net (0.0004) " (0.0012)
~~~~~~

**Node-2.2** (global 37219):

~~~~~~text
product (-0.0004) from (-0.0001) amazon (0.0010) platform (-0.0006) with (0.0003) title (0.0004) and (0.0002) content (0.0004) : (0.0008) title (0.0002) : (0.0004) okuma (-0.0001) crisium (0.0001) graphite (0.0006) 2- (0.0005) piece (0.0001) fly (0.0003) rod. (-0.0003) content (0.0008) : (0.0002) with (0.0006) a (0.0004) traditional (0.0006) build (0.0005) that (0.0003) includes (0.0002) a (0.0002) half (0.0003) wells (0.0006) grip, (0.0003) rosewood (0.0007) reel (0.0003) seat (0.0004) and (0.0006) stainless (-0.0001) steel (0.0007) snake (0.0007) guides, (0.0004) crisium (0.0006) fly (0.0005) rods (0.0003) are (0.0003) constructed (0.0004) for (0.0001) those (0.0005) who (0.0001) cast (0.0001) with (0.0003) a (0.0000) smooth (0.0005) and (0.0004) patient (0.0007) stroke. (-0.0001) as (0.0004) reward (0.0005) for (0.0004) their (0.0003) patience, (0.0004) casters (0.0001) receive (0.0004) nearly (0.0004) effortless (0.0001) casting (0.0000) and (0.0006) exceptional (0.0009) protection (-0.0002) of (0.0000) light (0.0003) tippets. (0.0005) built (0.0001) in (0.0005) two- (0.0004) piece (0.0002) models (0.0005) from (0.0002) 7- (0.0006) to (0.0004) 9- (0.0005) feet (0.0001) in (0.0005) length, (0.0002) crisium (0.0004) fly (0.0007) rods (0.0003) are (0.0003) exceptional (0.0006) on (0.0009) smaller (0.0002) waters (0.0004) where (0.0006) the (-0.0004) quality (0.0010) of (0.0001) the (-0.0003) presentation (0.0016) reaps (0.0004) greater (0.0003) rewards (0.0012) than (0.0006) casting (0.0007) distance. (0.0005)
~~~~~~

**Node-2.3** (global 37309):

~~~~~~text
product (0.0016) from (0.0012) amazon (0.0011) platform (-0.0003) with (0.0009) title (0.0005) and (0.0011) content (0.0003) : (0.0016) title (0.0003) : (0.0007) scientific (0.0010) anglers (0.0013) sharkskin (-0.0000) ultimate (0.0004) trout (0.0016) fly (0.0012) line. (0.0014) content (0.0012) : (0.0008) sharkskin (0.0005) ' (0.0000) s (0.0001) ultimate (0.0015) trout (0.0002) fuses (0.0012) our (0.0020) best (0.0002) taper (-0.0003) features (0.0002) in (0.0019) one (0.0014) single (0.0001) line (0.0009)
~~~~~~

**Node-3** (global 1001):

~~~~~~text
product (0.0053) from (0.0067) amazon (0.0009) platform (0.0015) with (0.0064) title (0.0060) and (0.0063) content (-0.0013) : (0.0054) title (0.0060) : (0.0034) rapala (0.0021) fishing (0.0036) forceps (0.0045) 7 (0.0045) 1 (0.0038) / (0.0044) 2 (0.0019) inch. (0.0011) content (0.0029) : (0.0037) the (-0.0007) rapala (0.0018) 7 (0.0034) 1 (0.0064) / (-0.0013) 2 (0.0010) " (0.0056) stainless (-0.0021) steel (0.0038) fishing (-0.0018) forceps (0.0008) are (0.0082) a (-0.0014) must- (0.0096) have (0.0061) tool (0.0019) for (0.0073) removing (0.0074) hooks, (0.0046) rigging (0.0037) and (0.0059) knot (0.0005) tying. (0.0006) built- (0.0057) in (0.0036) scissors, (0.0038) oversize (0.0044) thumb (0.0058) holes (0.0056) and (0.0069) hand (0.0047) lanyard. (0.0052)
~~~~~~

**Node-3.1** (global 1006):

~~~~~~text
product (0.0001) from (-0.0004) amazon (0.0004) platform (-0.0001) with (0.0002) title (0.0004) and (0.0005) content (-0.0002) : (0.0007) title (-0.0002) : (0.0006) hammers (-0.0001) collapsible (0.0002) wading (0.0001) staff (-0.0002) fishing (0.0003) stick. (-0.0006) content (0.0002) : (0.0004) a (-0.0002) great (0.0004) stick (-0.0004) for (-0.0001) added (0.0005) stability (0.0005) when (0.0002) wading (-0.0000) in (0.0002) swift (0.0001) water, (0.0002) climbing (0.0005) river (0.0002) banks (-0.0001) or (-0.0000) walking (-0.0000) on (0.0002) land. (-0.0007) made (0.0006) of (0.0002) lightweight, (0.0001) yet (0.0002) strong (0.0004) aluminum (-0.0000) alloy (0.0003) tubing (0.0002) of (0.0000) 3 (0.0001) / (-0.0000) 4inch (0.0001) in (0.0002) anodized (0.0000) matte (0.0001) black (0.0004) finish, (0.0002) it (0.0002) folds (0.0003) easily (0.0004) to (0.0002) 12 (0.0001) " (-0.0007) and (0.0004) fits (0.0004) into (0.0006) the (-0.0004) included (0.0000) nylon (0.0005) belt (0.0005) pouch. (0.0001) its (0.0004) double (0.0003) shock (0.0004) corded (0.0003) spring (0.0006) action (-0.0001) design (0.0005) allows (0.0006) one- (0.0003) hand (0.0004) operation (0.0005) to (0.0000) have (0.0001) the (0.0003) staff (0.0000) instantly (0.0002) ready (0.0002) for (0.0002) use. (-0.0003) nylon (0.0006) lanyard (0.0000) with (0.0004) easy (0.0006) carabineer (0.0001) link (0.0004) keeps (0.0005) the (-0.0003) staff (0.0005) close (0.0004) to (0.0003) you (0.0009) when (0.0004) not (0.0007) needed. (-0.0002) long (0.0004) eva (0.0009) handle (0.0006) has (0.0013) nylon (-0.0002) band (0.0002) strap. (0.0009) durable (-0.0009) carbide (0.0002) steel (0.0002) end (0.0001) tip (0.0006) gives (0.0000) sure (-0.0001) grip (0.0002) on (0.0004) slippery (-0.0002) rocks. (0.0002) length (-0.0011) : (0.0000) 52 (0.0001) 1 (0.0003) / (-0.0000) 2 (0.0013) " (-0.0017) fully (-0.0001) extended (0.0002) ; (0.0006) 12 (0.0008) " (-0.0003) folded. (0.0001) weight (0.0002) : (0.0001) 11ozs. (0.0001)
~~~~~~

**Node-3.2** (global 6080):

~~~~~~text
product (-0.0004) from (-0.0004) amazon (-0.0000) platform (0.0003) with (-0.0001) title (0.0000) and (-0.0001) content (0.0004) : (-0.0001) title (0.0001) : (-0.0002) nite (-0.0000) ize (-0.0000) c9s- (-0.0002) 03- (-0.0001) tp01 (-0.0002) small (-0.0002) figure (0.0001) 9 (-0.0001) carabiner (0.0001) with (-0.0003) rope, (0.0001) black, (-0.0001) two- (-0.0002) pack. (0.0006) content (0.0002) : (0.0001) carbiner (-0.0001) rope (-0.0004) tightener (0.0000) for (-0.0001) easy (-0.0003) attachment (-0.0000) to (-0.0001) fixed (-0.0002) points. (0.0005) easily (-0.0003) secure (-0.0000) loads, (0.0004) achieve (-0.0002) maximum (-0.0000) tension. (0.0007) load (0.0005) rated- (-0.0001) not (0.0000) for (0.0006) climbing (-0.0002)
~~~~~~

**Node-3.3** (global 996):

~~~~~~text
product (-0.0004) from (-0.0001) amazon (0.0004) platform (0.0002) with (0.0001) title (0.0003) and (0.0003) content (0.0002) : (0.0000) title (0.0004) : (0.0001) crystal (0.0003) river (-0.0000) live (-0.0000) release (-0.0000) net. (0.0004) content (0.0000) : (0.0001) unique (-0.0000) bow (0.0002) shape, (-0.0000) shallow (-0.0001) bag (0.0002) design, (0.0001) minimizes (0.0000) the (-0.0005) risk (0.0001) of (0.0002) injury (0.0001) to (0.0003) fish (0.0003) prior (0.0002) to (0.0001) release. (-0.0000) high (0.0004) quality (0.0004) laminated (0.0004) hardwood (0.0007) bow (0.0000) measures (0.0004) 14 (0.0002) " (0.0003) x (0.0000) 7 (0.0000) " (0.0002) and (0.0002) includes (0.0002) removable (0.0001) elastic (0.0002) lanyard. (0.0002)
~~~~~~

**Node-3.4** (global 8515):

~~~~~~text
product (-0.0014) from (0.0010) amazon (0.0017) platform (0.0006) with (0.0004) title (0.0017) and (0.0010) content (0.0003) : (0.0012) title (0.0012) : (0.0011) bill (0.0009) dance (0.0000) hook (0.0011) remover. (0.0006) content (0.0001) : (0.0015) the (0.0003) bill (0.0006) dance (-0.0003) hook (0.0008) remover (0.0003) features (0.0005) an (0.0006) ergonomic (0.0008) design (0.0007) for (0.0009) better (0.0001) hand (0.0005) control. (0.0002) additional (0.0000) features (0.0004) are (0.0018) the (0.0006) soft (0.0011) touch (0.0007) handle, (0.0012) steel (0.0010) frame (0.0010) construction (0.0012) and (0.0011) build (0.0009) in (0.0007) line (0.0013) cutter. (0.0005)
~~~~~~

**Node-3.5** (global 8516):

~~~~~~text
product (0.0002) from (0.0001) amazon (-0.0004) platform (0.0003) with (0.0000) title (0.0010) and (-0.0001) content (-0.0004) : (-0.0000) title (0.0007) : (0.0001) berkley (0.0002) 8- (-0.0001) inch (-0.0004) precision (0.0007) grip (0.0003) pliers. (0.0003) content (0.0006) : (0.0001) 8 (0.0003) " (0.0002) precision (0.0001) grip (-0.0001) pliers (0.0001)
~~~~~~

**Node-3.6** (global 8517):

~~~~~~text
product (0.0006) from (0.0008) amazon (0.0001) platform (0.0004) with (0.0006) title (0.0009) and (0.0005) content (-0.0002) : (0.0008) title (0.0005) : (0.0002) " (0.0002) caddis (-0.0001) men (0.0002) ' (0.0004) s (0.0004) northern (-0.0001) guide (0.0011) lightweight (0.0007) taupe (0.0004) and (0.0005) green (0.0004) ecosmart (0.0002) grip (0.0004) sole (0.0007) wading (0.0003) shoe (-0.0005) ". (0.0004) content (0.0004) : (0.0010) the (-0.0000) caddis (0.0001) brand (0.0003) has (0.0002) stood (0.0004) for (0.0003) quality (-0.0000) for (0.0000) many (0.0003) years. (-0.0004) all (0.0002) of (0.0001) our (-0.0004) products (0.0002) are (0.0001) on (-0.0001) the (0.0001) cutting (0.0008) edge (0.0003) of (-0.0000) available (0.0003) technology (0.0002) and (0.0003) every (0.0008) wader (-0.0001) is (0.0003) water (0.0002) tested (0.0005) before (0.0001) the (0.0001) brand (0.0001) ever (0.0005) goes (0.0002) on (0.0003) the (-0.0004) product. (0.0002) all (0.0003) caddis (-0.0000) waders, (0.0004) wading (0.0002) shoes, (0.0003) jackets, (0.0005) vests (0.0007) and (0.0007) accessory (0.0002) products (0.0005) come (-0.0005) with (-0.0000) a (-0.0006) one (-0.0001) year (0.0004) manufacturers (0.0006) warranty. (0.0001)
~~~~~~

**Node-3.7** (global 8518):

~~~~~~text
product (-0.0001) from (-0.0000) amazon (0.0001) platform (0.0001) with (0.0000) title (-0.0000) and (0.0001) content (-0.0000) : (0.0000) title (-0.0000) : (-0.0003) dr. (0.0001) slick (0.0002) scissor (0.0001) clamps. (0.0001) content (-0.0000) : (-0.0002) clamps (-0.0001) are (0.0001) designed (0.0001) for (0.0000) a (0.0000) myriad (-0.0000) of (0.0001) tasks (0.0001) like (-0.0002) crushing (0.0000) barbs, (0.0001) removing (0.0001) hooks (0.0000) from (0.0000) fish (0.0000) ( (0.0000) or (0.0000) yourself! (0.0001) ), (0.0000) opening (0.0000) / (0.0000) closing (0.0000) split (0.0000) shot, (0.0000) knot- (0.0000) tying, (0.0001) cutting (-0.0000) tippet, (0.0001) etc. (0.0001) knowing (0.0000) what (0.0000) tasks (0.0002) you (0.0000) regularly (-0.0000) perform (0.0001) stream- (-0.0001) side (0.0000) will (0.0000) help (0.0001) you (0.0000) select (0.0000) the (-0.0000) clamp (-0.0000) ( (0.0000) s (-0.0000) ) (-0.0000) that (0.0001) best (-0.0001) suit (0.0000) your (-0.0001) angling (0.0001) needs. (-0.0000) clamps (0.0000) tend (-0.0000) to (0.0001) be (0.0000) a (-0.0000) very (0.0000) personal (-0.0001) item, (0.0000) and (0.0001) like (0.0000) a (-0.0000) favorite (-0.0000) rod (-0.0000) or (0.0002) reel, (0.0001) people (0.0000) have (0.0001) preferences (-0.0000) for (0.0000) their (-0.0000) clamps. (0.0001) some (-0.0000) anglers (0.0000) like (-0.0000) short (-0.0000) clamps (0.0000) and (0.0002) others (0.0000) prefer (0.0001) long. (0.0001) some (0.0000) like (0.0000) straight (0.0000) jaws (-0.0000) while (0.0000) others (0.0000) prefer (0.0001) curved. (0.0001) many (0.0001) like (-0.0001) the (-0.0000) gold (0.0001) loops (-0.0000) / (0.0001) handles (0.0000) and (0.0000) others (0.0000) prefer (-0.0000) the (-0.0001) stealth- (0.0001) mode (0.0001) black. (0.0000) so, (0.0000) if (0.0001) you (0.0000) lose (0.0000) your (-0.0000) buddy (-0.0001) ' (-0.0000) s (0.0000) 5 (0.0001) " (0.0000) curved (-0.0000) black (0.0001) clamp, (0.0001) don (0.0000) ' (0.0000) t (0.0000) assume (0.0000) the (-0.0000) 4 (0.0000) " (-0.0000) gold (0.0001) loop (0.0000) straight (0.0001) model (0.0000) you (-0.0001) gave (0.0000) him (0.0001) off (0.0001) your (0.0000) vest (0.0000) will (0.0001) clear (0.0000) the (-0.0001) air. (0.0001) salt (-0.0001) waterif (0.0000) you (-0.0002) ' (0.0000) re (-0.0000) angling (0.0001) in (0.0000) salt (-0.0000) water, (0.0001) consider (-0.0000) using (0.0001) the (-0.0000) black (0.0000) oxidized (0.0000) or (0.0000) prism (0.0000) finished (-0.0000) clamps (0.0000) which (0.0000) provide (0.0000) an (0.0000) extra (0.0000) layer (-0.0000) of (-0.0000) protection. (0.0001) for (-0.0000) clamp (0.0000) longevity (0.0000) in (0.0000) salt (-0.0000) water, (0.0000) rinse (-0.0000) your (-0.0001) clamps (0.0000) in (0.0000) fresh (0.0000) water (0.0001) and (-0.0000) apply (-0.0000) a (0.0000) little (0.0000) oil. (0.0000) clamp (-0.0000) sizingmatch (0.0000) the (0.0000) clamp (0.0000) to (0.0001) the (-0.0001) size (-0.0000) of (-0.0001) the (-0.0002) flies (0.0002) you (-0.0001) ' (-0.0000) re (-0.0000) using. (0.0001) generally, (-0.0001) the (-0.0001) shorter (-0.0001) the (-0.0001) clamp (-0.0000) the (-0.0001) smaller (-0.0001) and (-0.0000) lighter (-0.0001) the (-0.0001) jaws, (-0.0000) and (0.0000) the (-0.0002) longer (-0.0001) the (-0.0001) clamp (0.0000) the (-0.0001) larger (0.0000) and (0.0001) heavier (-0.0001) the (-0.0000) jaws. (0.0001) a (-0.0001) 4- (-0.0001) inch (-0.0001) clamp (-0.0001) will (0.0001) struggle (0.0001) crushing (0.0001) a (-0.0000) barb (-0.0000) on (0.0001) a (0.0000) # (0.0001) 4 (-0.0000) streamer (0.0001) and (0.0002) a (0.0001) 6- (-0.0000) inch (0.0001) clamp (0.0001) will (-0.0001) be (0.0000) too (0.0000) large (0.0000) for (-0.0001) removing (-0.0001) a (0.0002) # (-0.0002) 22 (-0.0002) midge (0.0001) cluster (0.0001) from (0.0001) a (-0.0001) fish. (0.0000) metalall (0.0000) clamps (-0.0000) are (-0.0001) made (-0.0001) from (0.0000) 410 (0.0000) japanese (0.0001) stainless (-0.0000) steel (0.0001) with (-0.0000) a (-0.0001) rockwell (0.0002) hardness (0.0005) of (-0.0001) 42. (0.0002) dr. (0.0000) slick (0.0000) scissor (-0.0001) clamps (0.0000) : (-0.0001) the (0.0001) most (0.0005) versatile (-0.0002) series (0.0003) we (-0.0003) make (0.0003) and (0.0003) able (0.0001) to (0.0001) handle (0.0003) all (0.0000) streamside (-0.0002) tasks. (-0.0000) serrated (-0.0000) scissor (0.0001) for (0.0001) cutting (0.0001) tip (-0.0000)
~~~~~~

**Node-3.8** (global 8568):

~~~~~~text
product (-0.0000) from (0.0002) amazon (0.0003) platform (-0.0003) with (-0.0000) title (0.0000) and (0.0001) content (0.0002) : (0.0002) title (0.0000) : (0.0000) tooltron (-0.0001) 6- (0.0000) inch (-0.0001) locking (-0.0000) clamp (-0.0000) curved (0.0000) tip (0.0001) fish (0.0001) hook (0.0000) remover. (0.0001) content (0.0001) : (-0.0001) forceps (-0.0000) make (-0.0003) a (0.0002) great (0.0000) multi- (-0.0000) purpose (-0.0000) clamping (0.0001) tool (-0.0001) for (0.0000) hook (-0.0000) removal. (0.0000) 3- (0.0000) stage (0.0000) locking (-0.0001) jaw (0.0001) varies (0.0002) grip (0.0001) tightness, (-0.0000) quick (-0.0002) release (0.0001) ; (0.0001) serrated (0.0000) teeth (0.0000) for (0.0000) non- (0.0001) slip (0.0001) hold. (-0.0001) mirror- (-0.0000) polished (-0.0001) stainless (0.0001) steel (0.0001) has (-0.0001) superior (0.0004) rust (0.0001) and (-0.0000) corrosion (-0.0000) resistance. (0.0001)
~~~~~~

**Node-4** (global 8555):

~~~~~~text
product (0.0030) from (0.0025) amazon (0.0043) platform (0.0046) with (0.0049) title (0.0029) and (0.0058) content (0.0030) : (0.0070) title (0.0016) : (0.0079) " (-0.0027) trout (0.0009) streams (0.0104) of (0.0058) southern (0.0002) new (0.0043) england (0.0022) : (0.0073) an (0.0048) angler (0.0064) ' (0.0033) s (0.0032) guide (0.0064) to (0.0041) the (0.0021) watersheds (0.0069) of (0.0053) connecticut, (0.0020) rhode (0.0055) island, (0.0028) and (0.0057) massachusetts (0.0081) ( (0.0072) trout (-0.0032) streams (0.0051) ) (0.0087) ". (-0.0000) content (-0.0012) : (0.0056) tom (0.0028) fuller (0.0003) has (-0.0000) spilled (0.0007) the (0.0013) beans (0.0025) on (0.0027) everything (0.0030) from (0.0027) access (0.0032) points (0.0019) and (0.0034) the (-0.0027) best (0.0009) holding (-0.0002) water (0.0015) to (0.0025) the (-0.0025) intricacies (0.0036) of (0.0032) matching (0.0043) hatches.... (-0.0001) more (0.0068) than (0.0039) just (0.0040) a (0.0016) talented (0.0007) fly- (0.0028) fisherman, (0.0008) he (0.0053) is (0.0055) a (0.0005) devoted (0.0034) conservationist, (0.0029) an (0.0030) inquisitive (0.0034) naturalist, (0.0019) and (0.0046) a (0.0037) gifted (-0.0029) writer (0.0037) with (0.0023) a (0.0009) deep- (0.0034) rooted (0.0058) understanding (0.0038) of (0.0038) and (0.0047) appreciation (0.0014) for (0.0045) the (-0.0007) trout (0.0010) waters (0.0019) of (0.0040) southern (0.0001) new (-0.0008) england.-- (0.0020) james (0.0036) r. (-0.0047) babb, (0.0050) editor, (-0.0006) gray (0.0027) ' (0.0030) s (0.0080) sporting (0.0068) journal (0.0141)
~~~~~~

**Node-4.1** (global 37247):

~~~~~~text
product (0.0000) from (-0.0001) amazon (0.0002) platform (0.0011) with (0.0001) title (-0.0000) and (0.0004) content (0.0003) : (0.0002) title (0.0001) : (-0.0000) simple (0.0003) fly (0.0003) fishing (0.0006) : (-0.0000) techniques (0.0008) for (-0.0002) tenkara (-0.0002) and (-0.0001) rod (0.0002) and (-0.0001) reel. (0.0006) content (0.0006) : (-0.0003) none (0.0002)
~~~~~~

**Node-4.2** (global 37525):

~~~~~~text
product (0.0000) from (0.0002) amazon (0.0001) platform (0.0003) with (0.0004) title (0.0000) and (0.0002) content (0.0002) : (0.0002) title (0.0003) : (0.0003) trout (-0.0004) streams (0.0003) of (0.0001) northern (0.0001) new (0.0002) england (0.0001) : (0.0005) a (-0.0003) guide (0.0002) to (0.0003) the (0.0000) best (0.0000) fly- (0.0002) fishing (0.0007) in (0.0003) vermont, (0.0002) new (0.0001) hampshire, (0.0002) and (0.0006) maine, (0.0002) first (0.0000) edition. (-0.0001) content (0.0002) : (0.0001) david (0.0005) klausmeyer (0.0000) has (0.0003) been (0.0002) the (-0.0004) editor (-0.0001) in (0.0002) chief (0.0001) of (0.0003) fly (-0.0003) tyer (-0.0001) magazine (-0.0003) for (0.0000) fifteen (0.0002) years. (-0.0002) he (0.0006) has (0.0002) written (0.0001) numerous (0.0001) books (0.0003) and (0.0003) articles (0.0003) about (0.0002) fly (-0.0001) tying, (0.0000) and (0.0005) now (0.0002) does (0.0001) blogs (0.0002) and (0.0005) webcasts (0.0002) about (0.0000) them (0.0002) as (0.0002) well. (0.0002) his (0.0008) tying (-0.0002) techniques (-0.0003) are (-0.0001) well (0.0004) known (0.0003) among (0.0008) tiers. (0.0004)
~~~~~~

**Node-4.3** (global 37526):

~~~~~~text
product (-0.0004) from (0.0000) amazon (0.0002) platform (-0.0002) with (0.0002) title (-0.0000) and (0.0003) content (-0.0002) : (0.0004) title (0.0001) : (0.0002) " (-0.0003) white (0.0002) mountain (0.0002) guide, (0.0003) 29th (0.0005) : (0.0007) amc (-0.0000) ' (0.0001) s (0.0004) comprehensive (0.0008) guide (0.0002) to (0.0003) hiking (-0.0004) trails (-0.0001) in (-0.0002) the (0.0003) white (0.0001) mountain (-0.0001) national (0.0004) forest (-0.0000) ( (0.0004) appalachian (-0.0000) mountain (0.0002) club (-0.0001) white (0.0002) mountain (0.0003) guide (0.0001) ) (0.0004) ". (0.0004) content (0.0003) : (0.0004) & (-0.0002) # (0.0004) 8220 (0.0004) ; (-0.0004) for (0.0005) hikers (-0.0001) in (0.0002) the (0.0001) northeast, (0.0003) the (-0.0004) amcwhite (0.0002) mountain (0.0003) guideis (0.0000) like (0.0001) the (-0.0002) bible (0.0001) & (0.0000) # (0.0002) 8212 (0.0004) ; (0.0003) we (0.0002) read (0.0003) it (0.0004) religiously (0.0001) when (0.0004) scouting (-0.0002) trips (-0.0000) and (0.0004) trust (0.0001) it (0.0004) completely (0.0002) for (0.0005) useful (0.0002) trail (-0.0002) information. (0.0004) this (0.0004) book (0.0007) belongs (-0.0004) on (0.0004) every (-0.0001) backpacker (-0.0004) & (0.0001) # (0.0004) 8217 (0.0006) ; (-0.0002) s (0.0005) bookshelf. (0.0004) & (0.0004) # (0.0005) 8221 (0.0004) ; (0.0010) & (0.0004) # (0.0006) 8212 (0.0004) ; (0.0008) jonathan (0.0008) dorn, (0.0002) executive (0.0001) editor, (0.0006) backpacker (0.0002)
~~~~~~

**Node-4.4** (global 37527):

~~~~~~text
product (0.0002) from (-0.0000) amazon (0.0007) platform (-0.0000) with (0.0001) title (0.0004) and (-0.0003) content (0.0003) : (-0.0004) title (0.0007) : (0.0001) maine (-0.0004) atlas (-0.0002) & (-0.0001) amp (0.0003) ; (0.0002) gazetteer. (-0.0002) content (0.0005) : (0.0001) delorme (0.0000) has (-0.0001) been (0.0006) directly (0.0002) responsible (0.0001) for (0.0001) many (0.0000) of (0.0003) the (-0.0003) major (0.0002) technological (0.0006) advances (0.0002) made (-0.0001) in (0.0001) the (0.0001) mapping (-0.0006) industry (-0.0001) over (0.0003) the (0.0002) past (-0.0001) 30 (0.0002) years. (-0.0001)
~~~~~~

**Node-5** (global 8548):

~~~~~~text
product (0.0010) from (0.0031) amazon (0.0053) platform (-0.0012) with (-0.0010) title (0.0009) and (0.0036) content (0.0001) : (-0.0017) title (0.0028) : (0.0002) scientific (0.0035) anglers (0.0020) fluorocarbon (0.0014) ii (0.0032) leader. (0.0016) content (0.0008) : (-0.0002) dang, (-0.0004) those (0.0019) fish (-0.0008) are (-0.0008) picky. (0.0003) instead (0.0007) of (0.0001) sulking, (0.0006) switch (-0.0007) out (-0.0011) your (-0.0055) leader (-0.0027) for (0.0004) the (-0.0009) scientific (0.0017) anglers (0.0018) fluorocarbon (0.0014) ii (0.0025) leader. (0.0028) thanks (-0.0003) to (0.0010) its (0.0011) ultra- (0.0003) low (0.0004) visibility, (0.0007) the (0.0003) fish (-0.0013) have (0.0002) a (-0.0022) hard (-0.0000) time (0.0000) seeing (0.0000) your (-0.0028) line (-0.0003) and (0.0008) you (-0.0012) ' (-0.0006) re (-0.0014) able (0.0002) to (0.0002) fool (-0.0014) them (-0.0006) more (0.0010) easily (0.0007) with (0.0019) a (-0.0024) life- (0.0004) like (0.0001) fly (0.0012) or (0.0013) nymph. (0.0011)
~~~~~~

**Node-5.1** (global 1005):

~~~~~~text
product (-0.0006) from (0.0007) amazon (0.0005) platform (0.0014) with (0.0001) title (0.0012) and (-0.0001) content (0.0022) : (-0.0004) title (0.0009) : (0.0003) berkley (0.0006) 6- (0.0009) inch (0.0009) softouch (0.0001) hemostat (0.0005) pliers. (0.0007) content (0.0011) : (0.0002) 6 (0.0009) " (0.0000) softouch (0.0008) hemostat (0.0006) pliers (0.0004)
~~~~~~

**Node-5.2** (global 8575):

~~~~~~text
product (0.0013) from (0.0013) amazon (0.0018) platform (-0.0007) with (0.0016) title (0.0005) and (0.0003) content (0.0004) : (0.0015) title (0.0009) : (0.0016) 20 (0.0002) / (0.0014) 20 (0.0003) magnetic (-0.0002) tippet (0.0009) threader. (0.0001) content (0.0012) : (0.0002) this (-0.0003) handy (0.0020) device (-0.0010) aligns (0.0012) the (0.0010) tippet (0.0010) and (-0.0002) fly (0.0027) to (0.0021)
~~~~~~

**Node-5.3** (global 37251):

~~~~~~text
product (-0.0002) from (0.0004) amazon (-0.0003) platform (0.0000) with (-0.0002) title (-0.0002) and (-0.0002) content (0.0002) : (-0.0002) title (-0.0004) : (-0.0000) flies (-0.0004) direct (-0.0000) adams (0.0002) assortment (0.0011) trout (-0.0010) fishing (-0.0002) flies (-0.0002) ( (-0.0006) 1- (-0.0001) dozen (-0.0007) ). (0.0003) content (-0.0007) : (0.0003) this (-0.0006) item (0.0002) is (-0.0001) an (-0.0006) assortment (0.0005) of (-0.0002) adams (-0.0006) flies. (0.0005) & (-0.0001) # (-0.0002) xa0 (-0.0002) ; (-0.0004) this (-0.0004) item (-0.0001) consists (-0.0004) of (0.0000) 12 (-0.0001) flies (-0.0008) ; (0.0001) 3 (-0.0001) each (-0.0000) of (-0.0000) hook (-0.0006) size (-0.0003) 12, (0.0000) 14, (-0.0001) 16, (-0.0003) 18. (-0.0006)
~~~~~~

**Node-5.4** (global 37505):

~~~~~~text
product (0.0004) from (0.0002) amazon (0.0000) platform (-0.0000) with (0.0003) title (0.0002) and (0.0003) content (0.0000) : (0.0003) title (0.0001) : (0.0003) c (0.0002) & (0.0003) amp (0.0001) ; (0.0002) f (0.0002) design (0.0003) cfa- (-0.0000) 40 (0.0003) 3- (0.0002) in- (0.0002) 1 (0.0001) fly (-0.0001) fishing (0.0003) tweezers (0.0003) new. (0.0001) content (0.0002) : (0.0002) the (0.0001) c (0.0002) & (0.0004) f (0.0002) ; (0.0005) design (0.0004) cfa- (-0.0000) 40 (0.0002) 3- (0.0002) in- (0.0002) 1 (0.0002) tweezers, (0.0002) you (0.0001) ' (0.0001) ve (0.0001) got (0.0002) the (0.0002) fly (-0.0001) box (0.0002) now (0.0001) step (0.0003) it (0.0001) up (0.0004) with (0.0003) the (0.0002) accessories. (0.0002) combines (-0.0005) fly (-0.0000) handling (0.0002) tweezers, (0.0002) a (0.0002) hook (-0.0000) eye (0.0002) cleaner (0.0004) and (0.0002) three (-0.0000) different (0.0001) sized (0.0004) threaders, (0.0002) one (0.0000) of (-0.0001) which (0.0002) clips (0.0001) between (-0.0001) the (0.0000) tweezers (0.0001) for (0.0002) a (-0.0002) very (0.0002) handy (0.0001) tool. (0.0004) highlights (-0.0002) of (0.0003) this (-0.0005) item (-0.0001) : (-0.0002)
~~~~~~

**Node-5.5** (global 37506):

~~~~~~text
product (-0.0001) from (0.0000) amazon (-0.0001) platform (-0.0004) with (0.0000) title (0.0004) and (0.0001) content (-0.0003) : (0.0006) title (0.0005) : (0.0001) gone (0.0006) fishing (-0.0000) freshwater (-0.0010) flies, (0.0002) pack (0.0004) of (-0.0003) 55. (0.0009) content (0.0003) : (0.0003) you (0.0004) ' (0.0000) ll (0.0001) be (0.0002) pulling (0.0004) fish (-0.0002) from (0.0007) water (0.0002) in (0.0002) no (0.0002) time (0.0002) with (0.0001) this (0.0002) excellent (0.0008) assorted (0.0004) set (0.0002) of (0.0001) hand (-0.0000) tied (0.0006) flies (0.0001) and (-0.0002) streamers. (-0.0001) with (0.0005) 55 (-0.0002) of (0.0004) today (0.0003) ' (0.0002) s (0.0002) most (0.0005) popular (0.0011) patterns (0.0002) and (0.0001) styles (0.0008) you (0.0009) ' (0.0001) re (0.0002) sure (0.0006) to (0.0002) find (0.0004) one (0.0003) that (0.0002) works (0.0004) for (0.0003) any (0.0004) given (0.0005) situation. (0.0004) expand (-0.0008) your (0.0007) fly (0.0004) and (0.0005) streamer (0.0002) collection (0.0003) exponentially (0.0002) with (0.0002) this (0.0008) great (0.0004) set. (0.0001)
~~~~~~

**Node-6** (global 37290):

~~~~~~text
product (-0.0024) from (-0.0060) amazon (0.0039) platform (-0.0041) with (-0.0046) title (0.0088) and (0.0002) content (0.0014) : (-0.0005) title (0.0062) : (-0.0041) scientific (0.0065) anglers (0.0028) fluorocarbon (-0.0000) tippet (-0.0043) with (0.0030) cutter (0.0009) 30- (-0.0025) meters. (-0.0033) content (0.0038) : (-0.0009) scientific (0.0000) anglers (-0.0008) fluorocarbon (-0.0008) tippet (-0.0031) with (0.0028) cutter (-0.0005) gives (0.0026) you (0.0043) more (0.0035) for (0.0028) your (0.0036) money! (0.0023) more (0.0041) is (0.0052) better! (0.0026) scientific (0.0028) anglers (0.0030) fluorocarbon (0.0011) tippet (0.0018) with (0.0035) cutter (0.0017) includes (0.0052) 30 (0.0043) meters (0.0025) of (0.0032) line... (-0.0034) that (0.0051) ' (-0.0013) s (0.0023) 9 (0.0014) % (-0.0007) more (0.0034) than (0.0058) the (-0.0131) competition. (-0.0040) patented (0.0052) fluorocarbon (0.0045) resins (0.0017) are (0.0068) combined (0.0017) to (0.0073) form (0.0029) a (0.0000) tough, (0.0006) abrasion (-0.0005) resistant, (0.0021) virtually (-0.0001) invisible (0.0092) line (0.0023) with (0.0064) a (0.0033) softer (0.0016) core. (0.0053) includes (0.0090) built- (0.0016) in (0.0028) razor (0.0114) cutter. (0.0010) stock (-0.0011) up! (0.0077) state (0.0039) line (-0.0045) weight. (0.0017) order (-0.0001) today! (0.0088) scientific (0.0023) anglers (0.0109) fluorocarbon (0.0081) tippet (0.0141) with (0.0117) cutter, (0.0003) 30- (0.0111) meters (-0.0038)
~~~~~~

**Node-7** (global 37291):

~~~~~~text
product (0.0001) from (0.0007) amazon (-0.0013) platform (-0.0064) with (0.0043) title (0.0000) and (0.0044) content (-0.0004) : (0.0023) title (0.0024) : (-0.0025) fly (-0.0010) box (0.0055) + (0.0066) 100 (0.0042) assorted (0.0014) fly (0.0017) fishing (-0.0049) fly (-0.0007) package. (0.0003) content (0.0061) : (0.0018) the (0.0047) essential (0.0026) selection (-0.0001) of (0.0009) fly (0.0018) box (0.0020) and (0.0039) fly (-0.0014) fishing (-0.0040) flies (0.0013) if (0.0058) you (-0.0018) ' (-0.0012) re (-0.0002) fishing (-0.0045) for (0.0031) trout, (0.0023) steelhead, (0.0020) or (0.0073) salmon. (0.0017) there (0.0049) are (0.0040) enough (0.0025) assorted (0.0021) flies (0.0048) in (0.0018) this (0.0007) package (0.0024) to (-0.0002) allow (0.0032) you (-0.0007) to (0.0006) fly (0.0024) fish (0.0039) just (0.0052) about (0.0033) any (0.0043) freshwater (0.0055) river (0.0038) or (0.0058) stream (0.0035) all (0.0020) year (0.0061) round. (0.0055) the (-0.0092) fly (0.0011) patterns (0.0052) and (0.0076) sizes (0.0009) chosen (0.0051) in (0.0042) this (-0.0005) set (0.0006) are (0.0001) the (0.0019) most (0.0023) effective (0.0067) patterns (0.0047) and (0.0047) are (0.0070) a (-0.0063) must (0.0021) have (0.0031) in (0.0022) every (0.0022) fly (0.0021) fisherman (0.0181) ' (0.0068) s (0.0053) fly (0.0141) box. (-0.0245) please (0.0315) see (0.0112) pictures (0.0129) on (0.0087) fly (0.0133) patterns (0.0052) and (0.0099) sizes (0.0063) included (0.0100) in (0.0033) this (0.0094) set. (-0.0085)
~~~~~~

**Node-8** (global 37292):

~~~~~~text
product (-0.0051) from (-0.0024) amazon (0.0020) platform (-0.0065) with (-0.0004) title (0.0076) and (0.0013) content (-0.0006) : (0.0053) title (0.0005) : (0.0015) mojo (0.0021) outdoors (0.0073) wading (-0.0009) pole. (-0.0011) content (0.0042) : (0.0034) tired (0.0048) of (-0.0044) stumbling (0.0063) on (-0.0020) unseen (0.0053) objects (0.0011) in (0.0017) the (-0.0028) water? (0.0030) finally (-0.0047) an (0.0002) aid (-0.0050) to (-0.0019) hunters (-0.0121) wading (0.0033) in (0.0014) the (-0.0017) mud (-0.0008) and (-0.0025) water! (0.0069) wading (0.0032) support (0.0065) pole (0.0026) with (0.0016) a (-0.0002) specially (0.0025) designed (0.0057) tip (0.0014) & (-0.0009) # (0.0018) x2013 (0.0017) ; (0.0029) the (0.0015) knot (0.0018) & (0.0018) # (0.0052) x2013 (0.0053) ; (0.0033) to (0.0040) give (0.0037) waders (0.0021) support (0.0044) without (0.0028) the (-0.0009) tip (0.0012) sticking (-0.0001) in (0.0061) the (0.0000) mud. (0.0015) light (0.0017) weight (0.0039) and (0.0029) handy, (0.0028) it (-0.0004) has (0.0038) a (-0.0031) comfortable (0.0051) handle (0.0045) with (0.0068) carry (0.0059) strap, (0.0053) adjustable (0.0036) from (0.0022) 42 (0.0088) & (0.0082) # (0.0047) x201d (0.0053) ; (0.0020) to (0.0030) 60 (0.0027) & (0.0126) # (0.0053) x201d (0.0051) ; (0.0080) for (0.0075) comfort (0.0132) for (0.0071) persons (0.0022) of (0.0066) any (0.0067) height. (0.0096) designed (0.0065) to (0.0054) float (0.0015) in (0.0058) the (0.0032) water, (0.0022) so (0.0071) not (0.0048) to (0.0041) lose. (0.0030) a (-0.0026) must (0.0034) for (0.0052) waterfowlers (-0.0001) and (0.0073) other (0.0082) hunters (0.0002) who (-0.0006) wade (-0.0045) in (0.0030) the (-0.0007) mud (-0.0034) and (0.0026) water. (-0.0021)
~~~~~~

**Node-8.1** (global 8561):

~~~~~~text
product (-0.0001) from (-0.0005) amazon (-0.0008) platform (-0.0007) with (-0.0002) title (0.0005) and (-0.0000) content (-0.0004) : (0.0010) title (0.0004) : (0.0001) new (0.0007) zealand (-0.0005) strike (0.0004) indicator (0.0005) tool. (0.0000) content (0.0002) : (0.0002) top (0.0000) benefits (0.0002) of (-0.0002) the (-0.0001) new (0.0004) zealand (-0.0002) strike (0.0006) indicator. (-0.0004) guide (0.0003) endorsed. (0.0003) enables (0.0002) the (-0.0004) perfect (0.0003) presentation. (-0.0010) we (-0.0004) recommend (0.0009) purchasing (0.0004) a (-0.0003) pack (0.0003) of (0.0002) the (-0.0004) new (0.0000) zealand (-0.0004) strike (0.0004) indicator (0.0008) mixed (-0.0006) wool (-0.0007) colors (-0.0005) with (0.0000) your (0.0001) indicator (0.0005) tool. (0.0004) 10 (0.0002) percent (0.0003) of (0.0001) the (-0.0003) fisherman (-0.0006) catch (0.0001) 90 (0.0003) percent (0.0001) of (-0.0001) the (-0.0001) fish. (0.0001) presentation (0.0007) is (0.0002) the (-0.0004) difference. (-0.0000) totally (0.0005) adjustable. (0.0013) places (0.0002) nymph (0.0002) in (-0.0000) the (-0.0005) strike (0.0009) zone. (-0.0007) no (0.0004) damage (0.0001) to (0.0006) leader (0.0004) so (0.0000) significant (0.0002) savings (0.0007) in (0.0001) dollars (0.0002) and (0.0001) re- (0.0003) rigging. (0.0004) knotless (0.0002) so (0.0006) it (0.0004) doesn (0.0002) ' (-0.0000) t (0.0004) weaken (0.0006) the (-0.0000) line. (0.0006) pleasure (0.0008) to (-0.0001) cast (0.0005) its (0.0003) so (0.0003) light (0.0004) and (0.0003) natural (0.0000) it (0.0003) casts (0.0005) like (0.0002) a (-0.0002) dry (0.0005) fly. (0.0011) floats (0.0005) high (0.0004) so (-0.0001) easy (0.0004) to (-0.0001) see. (0.0003) lands (0.0008) gently (-0.0004) and (0.0002) makes (0.0010) a (0.0003) delicate (0.0001) presentation (-0.0003) that (-0.0001) doesn (-0.0002) ' (-0.0001) t (0.0002) spook (0.0004) fish. (0.0010) wool (-0.0023) indicator (-0.0006) is (0.0002) extremely (0.0002) sensitive (0.0001) to (0.0002) strikes. (0.0004) many (0.0003) takes (0.0002) are (0.0004) currently (0.0007) undetectable (0.0000) with (0.0000) hard (-0.0000) plastic (0.0007) type (0.0003) indicators (-0.0000) as (0.0003) fish (0.0006) spits (0.0002) out (0.0003) nymph. (0.0003) trim (0.0004) to (0.0003) exact (0.0005) size (0.0006) required. (0.0008) wool (0.0007) indicator (0.0001) floats (0.0001) a (0.0002) size (0.0001) 14 (0.0001) tungsten (0.0001) nymph (0.0001) or (0.0004) can (0.0004) be (0.0002) trimmed (0.0005) small (0.0004) and (-0.0002) stealthy (0.0001) for (0.0007) fishing (0.0006) size (0.0005) 22 (0.0004) midges (0.0003) easy (0.0002) to (0.0001) make (0.0001) and (0.0001) just (0.0001) takes (0.0000) a (-0.0000) few (0.0001) seconds. (0.0005) quick (0.0001) and (0.0002) easy (0.0000) to (0.0001) remove (0.0001) so (0.0001) you (-0.0000) can (0.0001) catch (0.0001) that (0.0002) rising (0.0005) rainbow. (0.0007) be (0.0001) sure (0.0006) to (0.0000) also (0.0002) see (0.0001) our (0.0006) new (0.0004) zealand (-0.0000) strike (0.0006) indicator (0.0007) wool (0.0003) listing (0.0004) on (0.0007) amazon. (-0.0004) also (0.0003) we (0.0005) recommend (0.0004) you (0.0006) view (-0.0001) our (0.0012) instructional (-0.0011) videos (0.0014) available (-0.0001) at (0.0006) our (0.0007) web (0.0005) site- (0.0003) www. (0.0004) strikeindicator. (0.0001) com (0.0004)
~~~~~~

**Node-9** (global 37293):

~~~~~~text
product (-0.0004) from (-0.0046) amazon (-0.0062) platform (0.0002) with (0.0031) title (0.0041) and (0.0059) content (0.0024) : (-0.0064) title (0.0088) : (0.0057) greys (0.0000) gs (0.0127) large (0.0111) fly (0.0044) box. (0.0034) content (0.0035) : (-0.0036) our (0.0107) original (0.0016) fly (0.0034) box (-0.0022) is (0.0063) strong (0.0040) and (0.0065) lightweight. (0.0029) this (0.0083) large (0.0086) six (0.0029) box (0.0063) will (0.0098) fit (0.0042) in (0.0037) the (-0.0037) vest (-0.0056) pocket. (0.0041) weight (0.0065) : (0.0034) 6. (0.0055) 42- (0.0062) inch- (0.0078) ounce (0.0008) length (0.0056) : (0.0071) 7. (0.0054) 68- (0.0053) inch (0.0064) width (0.0049) : (0.0038) 4. (0.0052) 33- (0.0046) inch (0.0106) height (0.0109) : (0.0115) 1. (0.0052) 77- (0.0067) inch. (0.0078)
~~~~~~

**Node-10** (global 37294):

~~~~~~text
product (0.0031) from (-0.0007) amazon (-0.0005) platform (-0.0024) with (0.0019) title (0.0018) and (0.0031) content (0.0015) : (0.0046) title (0.0033) : (-0.0014) rio (0.0015) powerflex (0.0002) trout (0.0028) leader. (-0.0003) content (0.0030) : (-0.0023) rio (0.0020) ' (0.0017) s (0.0031) new (0.0018) powerflex (0.0004) trout (0.0016) leaders (0.0033) are (0.0013) designed (0.0026) to (0.0012) turnover (0.0036) with (0.0010) ease, (0.0025) whether (0.0017) casting (0.0044) dry (0.0033) flies, (-0.0010) streamers (0.0018) or (0.0009) an (0.0019) indicator (0.0026) with (0.0027) weighted (0.0013) nymphs. (0.0000) powerflex (0.0022) leaders (0.0017) are (0.0009) manufactured (0.0030) to (0.0018) exacting (0.0013) tolerances (0.0024) using (0.0037) the (0.0006) latest (0.0026) technology (0.0037) and (0.0034) materials (0.0025) to (0.0021) ensure (0.0038) the (0.0021) leaders (0.0024) are (0.0012) the (0.0003) strongest (0.0017) possible, (0.0003) and (0.0035) turnover (0.0032) under (0.0012) the (-0.0001) most (0.0017) demanding (0.0018) conditions. (-0.0003) designed (0.0045) to (0.0026) turnover (0.0005) with (0.0017) ease (0.0011) under (0.0028) a (0.0006) variety (0.0025) of (0.0009) conditionsmanufactured (0.0017) to (0.0029) exacting (0.0017) tolerances (0.0028) using (0.0041) the (0.0011) latested (0.0026) technology (0.0059) and (0.0023) materialsthese (0.0021) leaders (0.0041) are (0.0012) the (0.0008) strongest (0.0034) possible (0.0006) and (0.0020) turnover (0.0050) under (0.0026) the (0.0013) most (0.0016) demanding (0.0039) conditions, (0.0026) whether (0.0064) casting (0.0040) dry (0.0001) flies, (0.0018) streamers (0.0017) or (0.0035) an (0.0038) indicator (0.0046) with (-0.0004) weighted (-0.0007) nymphshigh (0.0006) strengthperfection (0.0019) loop (0.0021) built (-0.0111) in (0.0017)
~~~~~~
