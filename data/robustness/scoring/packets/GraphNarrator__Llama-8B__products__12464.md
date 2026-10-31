# Reference packet: GraphNarrator__Llama-8B__products__12464

- Method: GraphNarrator; configuration: Llama-8B; dataset: products; target node: 12464
- Explanation source: `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/42.json` (messages[assistant])
- Scored scope (what the claims were extracted from): ### Free-Text Explanation section
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

Claims were extracted from the `### Free-Text Explanation` section only; the full assistant message is shown here.

~~~~~~text
### Graph Structure Reconstruction:

In the provided verbalized graph, the ROOT node (first line) is the target for classification.
Single-digit indexed nodes are direct neighbors of ROOT.
Double-digit indexed nodes are:
  - Two hops away from ROOT
  - Direct children of their parent node

Thus, the graph structure of this verbalized graph is:

- ROOT (scarf)
  - Node-1 (authentic keffiyeh)
    - Node-1.1 (tactical scarf)
    - Node-1.2 (kufi hat)
    - Node-1.3 (desert shemagh)
    - Node-1.4 (traditional shemagh)

### Word-Level Evaluation:

Keywords with high saliency scores in ROOT — "shemagh" (0.04), "scarf" (0.04), "head" (0.03), "neck" (0.03), "scarves" (0.01) — are strongly associated with headwear or clothing items. However, the presence of "amazon" (-0.00) and "product" (-0.04) carries negligible saliency and contributes little.

### Graph-Level Aggregation:

Node-1 (authentic keffiyeh, keywords: "keffiyeh" (0.00), "kafiya" (0.00), "shemagh" (0.00)) is a direct neighbor with moderate saliency, identifying a specific type of headwear. Indirect neighbors — Node-1.1 (tactical scarf), Node-1.2 (kufi hat), Node-1.3 (desert shemagh), Node-1.4 (traditional shemagh) — are all types of scarves or headwear, collectively confirming a clothing context across both hops.

### Free-Text Explanation
```markdown
The classification of ROOT into "Cell Phones & Accessories" is not strongly supported by its own keywords and the co-purchase neighborhood.

ROOT: Keywords like "shemagh" (0.04), "scarf" (0.04), and "head" (0.03) clearly identify this as a headwear item, but the classification label is unexpected.
  - Node-1: An authentic keffiyeh (keywords: "keffiyeh" (0.00), "kafiya" (0.00), "shemagh" (0.00)) is a direct neighbor, reinforcing the clothing context.
    - Node-1.1 ~ Node-1.4: Tactical scarves, kufi hats, desert shemaghs, and traditional shemaghs are all types of scarves or headwear, supporting the clothing category.
      - Node-1.1: A tactical scarf is a specific type of headwear, further confirming the clothing context.
      - Node-1.2: A kufi hat is a traditional headwear item, supporting the clothing category.
      - Node-1.3: A desert shemagh is a type of scarf, further confirming the clothing context.
      - Node-1.4: A traditional shemagh is a type of headwear, supporting the clothing category.

In summary, ROOT's own high-saliency keywords strongly signal clothing items, and the entire co-purchase neighborhood consists of headwear and clothing items, providing some evidence for the "Clothing" category. However, the classification label "Cell Phones & Accessories" is not strongly supported by the graph structure and keywords.
```
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/42.json`).

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
<verbalized-graph>ROOT: product(-0.04) amazon(-0.00) platform(-0.00) title(0.02) content(0.01) title(0.01) missing.(0.02) content(0.02) brand(0.01) new(0.01) arabic(0.02) shemagh(0.02) head(0.03) neck(0.03) scarf.(-0.03) great(0.02) value(0.06) shemagh.(0.01) plain(0.04) dull(0.02) white(0.01) bright(0.02) white(0.02) middle(0.02) eastern(0.04) head(0.01) neck(0.03) scarf.(0.04) scarves(0.01) come(0.02) dye(-0.01) scent,(0.02) simple(0.03) hand(0.02) wash(0.03) soft(0.02) detergent(0.02) take(0.01) care(0.01) scent.(-0.01) measures(0.02) 40(0.04) x(-0.00) 40(-0.02) inches(-0.04) 103(0.04) x(-0.02) 103(0.04) cm(0.03) ).(0.01) shemagh(0.04) made(-0.01) india(0.01) reliable.(0.04) type(0.04) shemagh(0.04) comes(0.04) hadab(0.04) two(0.03) sides(0.05) ends(0.02) scarf(0.02) tassel(0.01) surrounding(0.04) ).(0.00) brand(-0.02) new.(0.04) 
Node-1: product(-0.00) amazon(0.00) platform(0.00) title(0.00) content(0.01) title(0.00) authentic(0.01) black(-0.00) amp(-0.00) white(0.00) middle(-0.00) eastern(0.00) arab(0.00) kafiya(-0.00) keffiyeh(0.00) aqel(-0.00) rope.(0.01) content(0.00) authentic(0.00) middle(-0.00) eastern(0.00) black(0.00) white(0.00) kafiya(0.00) black(0.00) aqel-(0.00) black(0.00) rope(0.01) tighten(0.00) kafiya(0.00) head.(0.00) worn(0.01) millions(0.00) millions(0.00) middle(0.00) east.(0.00) material(0.00) 60(-0.00) cotton(0.01) 40(0.00) polyester(0.00) unisex(-0.00) style(0.01) size(0.00) 45(-0.00) x(0.01) 45(0.00) 110cm(0.01) x(0.01) 110cm(0.01) 
Node-1.1: product(0.00) amazon(-0.00) platform(0.00) title(0.00) content(-0.00) title(0.00) km(0.00) outfitters(0.00) reg(-0.00) pakistan(0.00) shemagh(-0.00) keffiyeh-(-0.00) choose(0.00) color!.(0.00) content(-0.00) made(0.00) 100(-0.00) heavy(0.00) weight(0.00) cotton.(0.00) high(0.00) quality(0.00) stitched(0.00) material.(0.00) arabian(-0.00) pattern(0.00) design.(0.00) designed(0.00) protect(0.00) head(0.00) neck(0.00) sun,(0.00) sand(0.00) wind.(0.00) tassles(-0.00) attached(-0.00) ends(0.00) shemagh(-0.00) scarf.(-0.00) folded(0.00) wrapped(-0.00) various(0.00) styles(-0.00) around(-0.00) head.(0.00) dries(-0.00) quickly(0.00) keep(-0.00) head(-0.00) warm.(-0.00) worn(-0.00) across(0.00) forehead(-0.00) neck.(-0.00) used(-0.00) military(-0.00) soldiers(0.00) afghanistan,(-0.00) iraq(-0.00) worldwide.(0.00) also(-0.00) used(0.00) neck(0.00) warmer(0.00) hand(0.00) towel.(-0.00) extremely(0.00) fashionable(0.00) popular.(-0.00) keffiyeh(0.00) also(0.00) known(0.00) shmagh,(0.00) shemagh(0.00) yashmag,(0.00) ghutra(0.00) hatta,(0.00) traditional(0.00) headdress(0.00) arab(0.00) men,(0.00) made(0.00) square(0.00) cloth(0.00) scarf(0.00) ),(0.00) folded(0.00) wrapped(-0.00) various(0.00) styles(0.00) around(-0.00) head.(0.00) works(-0.00) well(0.00) alternative(0.00) winter(0.00) headwear,(0.00) particularly(0.00) areas(0.00) snow(0.00) strong(0.00) winds.(0.00) shemagh,(0.00) also(0.00) known(-0.00) keffiyeh(0.00) arab(0.00) scarf,(0.00) simple(0.00) yet(0.00) efficient(0.00) way(0.00) protect(0.00) face(-0.00) neck(0.00) sun,(-0.00) wind(-0.00) sand.(0.00) also(0.00) works(0.00) well(-0.00) alternative(-0.00) winter(0.00) headwear,(-0.00) particularly(-0.00) areas(-0.00) snow(0.00) strong(-0.00) winds.(0.00) although(0.00) cotton,(0.00) warmer,(0.00) faster-(-0.00) drying(-0.00) cotton-(0.00) wool(0.00) blends(-0.00) also(0.00) available.(0.00) styles(-0.00) wearing(-0.00) shemagh(0.00) vary,(-0.00) wrapping(-0.00) scarf(-0.00) around(-0.00) head(-0.00) face(-0.00) provides(0.00) optimal(-0.00) protection(-0.00) elements.(-0.00) shemaghs(0.00) made(0.00) 100(-0.00) cotton(0.00) shrink(-0.00) washed(0.00) properly.(0.00) import.(-0.00) dimensions(-0.00) 42(0.00) x42(0.00) 
Node-1.2: product(0.00) amazon(0.00) platform(0.00) title(0.00) content(0.00) title(0.00) ultimate(0.00) arms(0.00) gear(0.00) tactical(0.00) scarf-(0.00) shemagh-(0.00) kafiya-(0.00) keffiyeh(-0.00) head(0.00) wrap(0.00) od(0.00) olive(-0.00) drab(0.00) green(0.00) black(0.00) 100(0.00) cotton.(0.00) content(0.00) ultimate(0.00) arms(0.00) gear(0.00) tactical(0.00) scarf-(0.00) shemagh-(0.00) kafiya-(0.00) keffiyeh(0.00) head(0.00) wrap(0.00) od(0.00) olive(0.00) drab(0.00) green(0.00) black(0.00) 100(0.00) cottonbrand(0.00) new-(0.00) 100(0.00) cotton-(0.00) 44(0.00) x(0.00) 44(0.00) essential(0.00) protecting(0.00) eyes,(0.00) nose,(0.00) mouth,(0.00) neck(0.00) sand.(0.00) also(-0.00) used(-0.00) neck(0.00) warmer(0.00) hand(0.00) towel(0.00) currently(0.00) used(0.00) usa,(0.00) british,(0.00) coalition(0.00) forces(0.00) iraq(0.00) afghanistan(0.00) woven(0.00) od(0.00) green(0.00) black(-0.00) color(0.00) pattern(0.00) 
Node-1.3: product(0.00) amazon(0.00) platform(-0.00) title(0.00) content(0.00) title(0.00) missing.(0.00) content(0.00) soft(0.00) comfortable(0.00) kufi(-0.00) hat.(0.00) hand-(0.00) crocheted(0.00) care.(0.00) stretches(0.00) fit(0.00) comfortable(0.00) small(0.00) medium(0.00) heads(0.00) 21-(-0.00) 22.(0.00) 5(-0.00) inches(0.00) us(-0.00) hat(-0.00) size(-0.00) 6(-0.00) 3(-0.00) 4(-0.00) 7(-0.00) 1(0.00) 4(0.00) ).(-0.00) large(0.00) xl(0.00) head(0.00) sizes.(0.00) 
Node-1.4: product(0.00) amazon(-0.00) platform(0.00) title(0.00) content(0.00) title(0.00) desert(-0.00) sand(-0.00) yellow(-0.00) amp(-0.00) black(0.00) shemagh(-0.00) arab(0.00) keffiyeh(-0.00) neck(0.00) scarf.(-0.00) content(0.00) yellow(-0.00) sand(0.00) black(0.00) shemagh(0.00) arab(0.00) keffiyeh(0.00) neck(-0.00) scarf-(0.00) 100(0.00) cotton(0.00) material.(-0.00) desert(-0.00) sand(-0.00) yellow(0.00) black.(0.00) size(0.00) 42(-0.00) x(-0.00) 42(0.00) inches(0.00) ).(0.00) traditional(0.00) desert(0.00) arab(0.00) head(0.00) dress,(0.00) evolved(-0.00) turbans(0.00) ancient(0.00) times.(-0.00) essential(0.00) protecting(0.00) eyes,(-0.00) nose,(0.00) mouth,(0.00) ears(0.00) face(0.00) sand.(-0.00) also(0.00) used(0.00) neck(0.00) warmer(0.00) hand(0.00) towel.(-0.00) scarf(0.00) high(0.00) quality(0.00) stitch.(0.00) worn(0.00) soldiers(0.00) iraq(0.00) afghanistan(0.00) ab</verbalized-graph>

### Classification Label
Cell Phones & Accessories

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 12464
- Title: missing
- True class (canonical `y`): **label 25**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Sports & Outdoors**
- Prediction recorded by this method's pipeline: **Cell Phones & Accessories**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: missing. Content: brand new Arabic Shemagh Head/Neck Scarf. This is a great value shemagh. plain dull white (not a bright white) middle eastern head & neck scarf. All these scarves come with a dye scent, a simple hand wash with a soft detergent should take care of the scent. It measures 40" X 40" inches (103 X 103 cm). This Shemagh is made in India by Reliable. This type of Shemagh comes with Hadab on two sides at the ends of the scarf (tassel on the surrounding). This is brand new.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 8 nodes

| node id | true class | title |
|---|---|---|
| 1509 | Sports & Outdoors | AUTHENTIC Black &amp; White Middle Eastern Arab Kafiya Keffiyeh with Aqel Rope |
| 1510 | label 25 | missing |
| 12449 | label 25 | missing |
| 12463 | label 25 | missing |
| 12467 | Sports & Outdoors | Authentic and NEW Head Shemagh Arab Kafiya Keffiyeh Kufiya with Agal Red &amp; White the Same Israel, Palestine and British SAS Military USE Unique and Retro Look, Soft and Lightweight Great and Cool Unisex Accessory |
| 51060 | Sports & Outdoors | Proforce Shemagh Scarf Sand Solid |
| 51061 | label 25 | missing |
| 51062 | label 25 | missing |

### 2-hop (shortest distance exactly 2): 28 nodes

| node id | true class | title |
|---|---|---|
| 119 | Sports & Outdoors | Desert Sand/Yellow &amp; Black Shemagh Arab Keffiyeh Neck Scarf |
| 1501 | Sports & Outdoors | KM Outfitters&reg; Pakistan Shemagh Keffiyeh - Choose Color! |
| 1507 | Arts, Crafts & Sewing | 40&quot;x40&quot;Grey Lightweight Shemagh Arab Tactical Desert Scarf Keffiyeh |
| 10233 | Tools & Home Improvement | Damascus DNKPB Imperial Neoprene Knee Pads with Reinforced Non-slip Trion-X Caps, Black |
| 12444 | Clothing, Shoes & Jewelry | Desert Military Tactial Keffiyeh Shemagh White &amp; Black |
| 12450 | Sports & Outdoors | Condor Tactical Cap - BLACK |
| 12460 | Sports & Outdoors | Ultimate Arms Gear Tactical Scarf - Shemagh - Kafiya - Keffiyeh Head Wrap : OD Olive Drab Green / Black 100% Cotton |
| 12461 | label 25 | missing |
| 12462 | label 25 | missing |
| 12465 | label 25 | missing |
| 12466 | All Beauty | White &amp; Black Shemagh Heavyweight Arab Tactical Desert Keffiyeh Scarf |
| 12468 | Tools & Home Improvement | Mechanix Wear MP3-05-010 Mpact3 Knuckle Protection Glove, Black, Large |
| 12469 | label 25 | missing |
| 12470 | label 25 | missing |
| 12471 | Beauty | Change 1PC Unisex Fashion Women Men Arab Shemagh Keffiyeh Palestine Scarf Shawl Wrap (Purple) |
| 12472 | Sports & Outdoors | Century&reg; hand forearm armor |
| 12473 | Tools & Home Improvement | Damascus DNKPB Imperial Neoprene Knee Pads with Reinforced Non-slip Trion-X Caps, Black |
| 12474 | label 25 | missing |
| 12475 | Sports & Outdoors | Matrix Iron Face Carbon Steel &quot;Striker&quot; Metal Mesh Lower Half Mask (Black) |
| 12476 | Beauty | Change 1PC Unisex Fashion Women Men Arab Shemagh Keffiyeh Palestine Scarf Shawl Wrap (Red) |
| 50828 | Sports & Outdoors | KM Outfitters&reg; Pakistan Shemagh Keffiyeh - Choose Color! |
| 51010 | Sports & Outdoors | Dark Blue Arab Shemagh Head/neck Scarf Authentic Quality Desert Wear Wrap Arafat Palestine |
| 51011 | label 25 | missing |
| 51012 | label 25 | missing |
| 51050 | label 25 | missing |
| 51053 | label 25 | missing |
| 51059 | label 25 | missing |
| 51064 | Sports & Outdoors | KM Outfitters&reg; Pakistan Shemagh Keffiyeh - Choose Color! |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/42.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Cell Phones & Accessories**, ground truth = **label 25**.
The verbalized graph is 30648 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 12464 | 113 | 0.0586 | yes |
| Node-1 | 1 | 1509 | 80 | 0.0137 | yes |
| Node-1.1 | 9 | 1501 | 257 | 0.0009 | yes |
| Node-1.2 | 10 | 12460 | 102 | 0.0040 | yes |
| Node-1.3 | 11 | 12461 | 57 | 0.0037 | yes |
| Node-1.4 | 12 | 119 | 195 | 0.0005 | yes |
| Node-1.5 | 13 | 12465 | 94 | 0.0079 | no |
| Node-1.6 | 14 | 12466 | 170 | 0.0041 | no |
| Node-2 | 2 | 1510 | 84 | 0.0149 | no |
| Node-2.1 | 15 | 1507 | 48 | 0.0010 | no |
| Node-2.2 | 16 | 12450 | 43 | 0.0019 | no |
| Node-2.3 | 17 | 12469 | 40 | 0.0014 | no |
| Node-2.4 | 18 | 12471 | 103 | 0.0009 | no |
| Node-2.5 | 19 | 12472 | 37 | 0.0008 | no |
| Node-2.6 | 20 | 12468 | 85 | 0.0005 | no |
| Node-2.7 | 21 | 12473 | 197 | 0.0004 | no |
| Node-2.8 | 22 | 12475 | 82 | 0.0005 | no |
| Node-2.9 | 23 | 12476 | 103 | 0.0005 | no |
| Node-3 | 3 | 12449 | 122 | 0.0031 | no |
| Node-3.1 | 24 | 12444 | 180 | 0.0011 | no |
| Node-3.2 | 25 | 51010 | 133 | 0.0015 | no |
| Node-3.3 | 26 | 51011 | 99 | 0.0013 | no |
| Node-3.4 | 27 | 51012 | 105 | 0.0010 | no |
| Node-4 | 4 | 12463 | 34 | 0.0199 | no |
| Node-4.1 | 28 | 51050 | 22 | 0.0033 | no |
| Node-4.2 | 29 | 51053 | 62 | 0.0012 | no |
| Node-4.3 | 30 | 51059 | 29 | 0.0009 | no |
| Node-5 | 5 | 12467 | 75 | 0.0103 | no |
| Node-5.1 | 31 | 50828 | 257 | 0.0016 | no |
| Node-5.2 | 32 | 51064 | 257 | 0.0016 | no |
| Node-6 | 6 | 51060 | 65 | 0.0080 | no |
| Node-7 | 7 | 51061 | 140 | 0.0068 | no |
| Node-8 | 8 | 51062 | 110 | 0.0046 | no |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->Node-1.6, Node-1->Node-3, Node-1->Node-4, Node-1->Node-5, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.3->Node-4, Node-1.4->Node-1, Node-1.5->Node-1, Node-1.5->Node-8, Node-1.6->Node-1, Node-1.6->Node-5, Node-1.6->Node-6, Node-2->Node-2.1, Node-2->Node-2.2, Node-2->Node-2.3, Node-2->Node-2.4, Node-2->Node-2.5, Node-2->Node-2.6, Node-2->Node-2.7, Node-2->Node-2.8, Node-2->Node-2.9, Node-2->ROOT, Node-2.1->Node-2, Node-2.1->Node-3, Node-2.2->Node-2, Node-2.3->Node-2, Node-2.4->Node-2, Node-2.5->Node-2, Node-2.6->Node-2, Node-2.7->Node-2, Node-2.8->Node-2, Node-2.9->Node-2, Node-3->Node-1, Node-3->Node-2.1, Node-3->Node-3.1, Node-3->Node-3.2, Node-3->Node-3.3, Node-3->Node-3.4, Node-3->Node-5, Node-3->ROOT, Node-3.1->Node-3, Node-3.2->Node-3, Node-3.2->Node-5, Node-3.3->Node-3, Node-3.4->Node-3, Node-4->Node-1, Node-4->Node-1.3, Node-4->Node-4.1, Node-4->Node-4.2, Node-4->Node-4.3, Node-4->ROOT, Node-4.1->Node-4, Node-4.2->Node-4, Node-4.3->Node-4, Node-5->Node-1, Node-5->Node-1.6, Node-5->Node-3, Node-5->Node-3.2, Node-5->Node-5.1, Node-5->Node-5.2, Node-5->ROOT, Node-5.1->Node-5, Node-5.2->Node-5, Node-6->Node-1.6, Node-6->ROOT, Node-7->ROOT, Node-8->Node-1.5, Node-8->ROOT, ROOT->Node-1, ROOT->Node-2, ROOT->Node-3, ROOT->Node-4, ROOT->Node-5, ROOT->Node-6, ROOT->Node-7, ROOT->Node-8

### Tokens and scores

**ROOT** (global 12464):

~~~~~~text
product (-0.0359) from (0.0035) amazon (-0.0028) platform (-0.0022) with (0.0108) title (0.0207) and (0.0238) content (0.0139) : (0.0314) title (0.0086) : (0.0237) missing. (0.0247) content (0.0216) : (0.0140) brand (0.0052) new (0.0089) arabic (0.0166) shemagh (0.0232) head (0.0261) / (0.0208) neck (0.0264) scarf. (-0.0260) this (0.0311) is (0.0230) a (0.0144) great (0.0218) value (0.0582) shemagh. (0.0059) plain (0.0366) dull (0.0246) white (0.0052) ( (0.0292) not (0.0361) a (0.0177) bright (0.0197) white (0.0217) ) (0.0226) middle (0.0185) eastern (0.0376) head (0.0055) & (0.0395) neck (0.0278) scarf. (0.0354) all (0.0336) these (0.0501) scarves (0.0135) come (0.0236) with (0.0393) a (0.0233) dye (-0.0057) scent, (0.0174) a (0.0147) simple (0.0344) hand (0.0178) wash (0.0316) with (0.0285) a (0.0098) soft (0.0155) detergent (0.0202) should (0.0368) take (0.0055) care (0.0124) of (0.0185) the (0.0116) scent. (-0.0119) it (0.0340) measures (0.0234) 40 (0.0437) " (-0.0037) x (-0.0024) 40 (-0.0230) " (0.0168) inches (-0.0420) ( (0.0197) 103 (0.0379) x (-0.0151) 103 (0.0425) cm (0.0301) ). (0.0063) this (-0.0103) shemagh (0.0363) is (0.0586) made (-0.0061) in (0.0153) india (0.0150) by (0.0108) reliable. (0.0396) this (0.0140) type (0.0449) of (0.0051) shemagh (0.0356) comes (0.0444) with (0.0167) hadab (0.0379) on (0.0110) two (0.0257) sides (0.0474) at (0.0212) the (-0.0013) ends (0.0233) of (0.0214) the (0.0236) scarf (0.0174) ( (0.0182) tassel (0.0142) on (0.0392) the (0.0259) surrounding (0.0358) ). (0.0017) this (0.0408) is (0.0378) brand (-0.0230) new. (0.0371)
~~~~~~

**Node-1** (global 1509):

~~~~~~text
product (-0.0041) from (-0.0054) amazon (0.0026) platform (0.0014) with (-0.0015) title (0.0037) and (-0.0077) content (0.0079) : (-0.0036) title (0.0036) : (-0.0018) authentic (0.0069) black (-0.0004) & (0.0013) amp (-0.0002) ; (0.0084) white (0.0005) middle (-0.0006) eastern (0.0003) arab (0.0007) kafiya (-0.0006) keffiyeh (0.0005) with (0.0029) aqel (-0.0013) rope. (0.0106) content (0.0027) : (-0.0022) authentic (0.0036) middle (-0.0009) eastern (0.0037) black (0.0012) & (0.0016) white (0.0013) kafiya (0.0009) with (0.0001) a (0.0020) black (0.0019) aqel- (0.0010) the (0.0029) black (0.0040) rope (0.0093) to (-0.0014) tighten (0.0036) the (0.0016) kafiya (0.0007) on (0.0003) the (0.0002) head. (0.0021) worn (0.0081) by (0.0023) millions (0.0022) in (0.0024) the (0.0028) millions (0.0038) in (-0.0022) the (0.0018) middle (0.0010) east. (0.0044) material (0.0024) : (-0.0042) 60 (-0.0019) % (0.0009) cotton (0.0054) / (0.0000) 40 (0.0011) % (0.0028) polyester (0.0027) unisex (-0.0010) style (0.0137) size (0.0032) : (-0.0010) 45 (-0.0006) " (0.0045) x (0.0050) 45 (0.0012) " (0.0004) / (0.0042) 110cm (0.0051) x (0.0057) 110cm (0.0053)
~~~~~~

**Node-1.1** (global 1501):

~~~~~~text
product (0.0001) from (0.0002) amazon (-0.0000) platform (0.0005) with (0.0001) title (0.0001) and (0.0002) content (-0.0002) : (0.0002) title (0.0001) : (0.0001) km (0.0001) outfitters (0.0003) & (0.0002) reg (-0.0001) ; (0.0002) pakistan (0.0002) shemagh (-0.0004) keffiyeh- (-0.0001) choose (0.0002) color!. (0.0002) content (-0.0000) : (-0.0001) made (0.0000) from (0.0002) 100 (-0.0001) % (-0.0001) heavy (0.0003) weight (0.0002) cotton. (0.0008) high (0.0002) quality (0.0002) stitched (0.0001) material. (0.0009) arabian (-0.0004) pattern (0.0001) design. (0.0004) designed (0.0000) to (-0.0000) protect (0.0000) head (0.0000) & (0.0003) neck (0.0001) from (-0.0000) sun, (0.0001) sand (0.0002) & (0.0002) wind. (0.0001) tassles (-0.0000) attached (-0.0000) to (-0.0000) ends (0.0000) of (-0.0001) shemagh (-0.0002) scarf. (-0.0005) folded (0.0002) & (-0.0000) wrapped (-0.0001) in (0.0001) various (0.0000) styles (-0.0001) around (-0.0001) the (0.0001) head. (0.0000) dries (-0.0002) quickly (0.0002) & (0.0001) keep (-0.0000) the (0.0001) head (-0.0001) warm. (-0.0002) worn (-0.0001) across (0.0001) the (0.0000) forehead (-0.0000) or (0.0001) neck. (-0.0002) used (-0.0000) by (-0.0002) military (-0.0003) soldiers (0.0000) in (0.0001) afghanistan, (-0.0001) iraq (-0.0001) & (-0.0000) worldwide. (0.0000) can (0.0000) also (-0.0000) be (0.0002) used (0.0001) as (-0.0000) a (0.0000) neck (0.0001) warmer (0.0002) or (0.0001) hand (0.0001) towel. (-0.0004) extremely (0.0003) fashionable (0.0001) & (-0.0002) popular. (-0.0001) a (0.0006) keffiyeh (0.0001) is (0.0002) also (0.0001) known (0.0004) as (0.0004) a (0.0001) shmagh, (0.0000) shemagh (0.0001) or (0.0002) yashmag, (0.0002) a (0.0001) ghutra (0.0000) or (0.0002) a (0.0000) hatta, (0.0000) and (0.0000) is (0.0005) a (0.0002) traditional (0.0002) headdress (0.0001) of (0.0001) arab (0.0004) men, (0.0002) made (0.0001) of (0.0000) a (0.0001) square (0.0002) of (0.0000) cloth (0.0001) ( (-0.0002) " (0.0002) scarf (0.0003) " (0.0003) ), (0.0001) folded (0.0003) and (0.0002) wrapped (-0.0000) in (0.0002) various (0.0002) styles (0.0002) around (-0.0001) the (0.0002) head. (0.0001) works (-0.0000) well (0.0001) as (0.0000) alternative (0.0000) winter (0.0001) headwear, (0.0000) particularly (0.0000) in (0.0000) areas (0.0001) with (-0.0001) snow (0.0003) and (-0.0000) strong (0.0001) winds. (0.0001) the (-0.0000) shemagh, (0.0002) also (0.0001) known (-0.0000) as (0.0001) the (0.0001) keffiyeh (0.0001) or (0.0002) arab (0.0004) scarf, (0.0001) is (0.0001) a (0.0001) simple (0.0001) yet (0.0000) efficient (0.0001) way (0.0000) to (0.0001) protect (0.0001) your (0.0001) face (-0.0000) and (0.0000) neck (0.0000) from (-0.0000) sun, (-0.0000) wind (-0.0001) and (0.0000) sand. (0.0000) it (0.0002) also (0.0001) works (0.0000) well (-0.0000) as (0.0001) alternative (-0.0000) winter (0.0002) headwear, (-0.0001) particularly (-0.0000) in (-0.0000) areas (-0.0000) with (-0.0001) snow (0.0002) and (0.0001) strong (-0.0001) winds. (0.0000) although (0.0002) most (0.0002) are (0.0001) cotton, (0.0002) warmer, (0.0002) faster- (-0.0000) drying (-0.0000) cotton- (0.0002) wool (0.0003) blends (-0.0001) are (0.0001) also (0.0000) available. (0.0000) styles (-0.0001) of (-0.0001) wearing (-0.0000) the (0.0003) shemagh (0.0001) vary, (-0.0001) but (-0.0000) wrapping (-0.0002) the (-0.0000) scarf (-0.0001) around (-0.0002) the (0.0002) head (-0.0001) and (0.0000) face (-0.0001) provides (0.0001) optimal (-0.0001) protection (-0.0001) from (0.0000) the (0.0001) elements. (-0.0001) shemaghs (0.0004) are (-0.0002) made (0.0000) from (0.0001) 100 (-0.0001) % (-0.0005) cotton (0.0001) and (0.0000) will (0.0001) shrink (-0.0002) if (0.0000) not (-0.0000) washed (0.0001) properly. (0.0003) import. (-0.0001) dimensions (-0.0002) : (0.0007) 42 (0.0001) " (-0.0005) x42 (0.0001) " (0.0001)
~~~~~~

**Node-1.2** (global 12460):

~~~~~~text
product (0.0009) from (-0.0003) amazon (0.0019) platform (0.0010) with (0.0001) title (0.0010) and (-0.0001) content (0.0010) : (0.0003) title (0.0004) : (0.0000) ultimate (0.0009) arms (0.0005) gear (0.0017) tactical (0.0010) scarf- (0.0005) shemagh- (0.0006) kafiya- (0.0004) keffiyeh (-0.0001) head (0.0007) wrap (0.0006) : (-0.0001) od (0.0001) olive (-0.0005) drab (0.0008) green (0.0007) / (0.0006) black (0.0005) 100 (0.0003) % (0.0007) cotton. (0.0007) content (0.0005) : (0.0007) ultimate (0.0013) arms (0.0005) gear (0.0013) tactical (0.0013) scarf- (0.0007) shemagh- (0.0007) kafiya- (0.0006) keffiyeh (0.0007) head (0.0003) wrap (0.0011) : (0.0003) od (0.0005) olive (0.0003) drab (0.0010) green (0.0013) / (0.0009) black (0.0007) 100 (0.0007) % (0.0007) cottonbrand (0.0022) new- (0.0001) 100 (0.0003) % (0.0006) cotton- (0.0014) 44 (0.0002) " (0.0012) x (0.0010) 44 (0.0001) " (0.0008) essential (0.0009) for (0.0000) protecting (0.0007) eyes, (0.0005) nose, (0.0005) mouth, (0.0002) and (0.0009) neck (0.0007) from (0.0005) sand. (0.0006) can (0.0002) also (-0.0002) be (0.0004) used (-0.0000) as (0.0001) a (-0.0015) neck (0.0013) warmer (0.0008) or (0.0004) hand (0.0012) towel (0.0025) currently (0.0006) used (0.0009) by (0.0004) usa, (0.0013) british, (0.0013) and (0.0008) coalition (0.0014) forces (0.0010) in (0.0007) iraq (0.0013) and (0.0010) afghanistan (0.0016) woven (0.0040) od (0.0007) green (0.0002) and (0.0005) black (-0.0013) color (0.0035) pattern (0.0024)
~~~~~~

**Node-1.3** (global 12461):

~~~~~~text
product (0.0037) from (-0.0002) amazon (0.0022) platform (-0.0009) with (0.0003) title (0.0019) and (0.0010) content (0.0011) : (0.0019) title (0.0022) : (0.0017) missing. (0.0009) content (0.0013) : (0.0006) soft (0.0009) comfortable (0.0011) kufi (-0.0006) hat. (0.0005) hand- (0.0005) crocheted (0.0002) with (0.0002) care. (0.0000) stretches (0.0015) to (0.0001) fit (0.0003) comfortable (0.0002) on (0.0005) small (0.0010) to (0.0004) medium (0.0017) heads (0.0003) 21- (-0.0000) 22. (0.0004) 5 (-0.0001) inches (0.0009) ( (0.0016) us (-0.0018) hat (-0.0011) size (-0.0003) : (0.0011) 6 (-0.0004) 3 (-0.0000) / (-0.0002) 4 (-0.0004) to (0.0009) 7 (-0.0001) 1 (0.0006) / (-0.0003) 4 (0.0005) ). (-0.0010) not (0.0006) for (0.0001) large (0.0007) or (0.0001) xl (0.0004) head (0.0006) sizes. (0.0008)
~~~~~~

**Node-1.4** (global 119):

~~~~~~text
product (0.0003) from (-0.0000) amazon (-0.0001) platform (0.0004) with (0.0001) title (0.0002) and (-0.0000) content (0.0001) : (-0.0000) title (0.0002) : (0.0002) desert (-0.0001) sand (-0.0000) / (-0.0000) yellow (-0.0000) & (0.0001) amp (-0.0001) ; (0.0000) black (0.0000) shemagh (-0.0000) arab (0.0001) keffiyeh (-0.0003) neck (0.0000) scarf. (-0.0006) content (0.0002) : (0.0001) yellow (-0.0000) sand (0.0000) / (0.0001) black (0.0001) shemagh (0.0001) arab (0.0001) keffiyeh (0.0001) neck (-0.0001) scarf- (0.0002) 100 (0.0002) % (0.0002) cotton (0.0003) material. (-0.0001) desert (-0.0000) sand (-0.0001) / (0.0001) yellow (0.0000) & (0.0003) black. (0.0003) size (0.0003) 42 (-0.0000) " (0.0001) x (-0.0000) 42 (0.0000) " (0.0001) ( (0.0001) inches (0.0002) ). (0.0001) traditional (0.0001) desert (0.0000) arab (0.0002) head (0.0001) dress, (0.0002) which (0.0001) evolved (-0.0001) from (-0.0001) turbans (0.0001) in (0.0000) ancient (0.0004) times. (-0.0001) essential (0.0005) for (0.0001) protecting (0.0002) the (-0.0001) eyes, (-0.0000) nose, (0.0001) mouth, (0.0001) ears (0.0002) and (0.0001) face (0.0001) from (0.0002) sand. (-0.0000) can (0.0003) also (0.0002) be (0.0003) used (0.0002) as (0.0001) a (0.0002) neck (0.0003) warmer (0.0003) or (0.0001) hand (0.0001) towel. (-0.0001) scarf (0.0002) is (0.0001) high (0.0002) quality (0.0002) stitch. (0.0002) worn (0.0001) by (-0.0000) soldiers (0.0001) in (0.0003) iraq (0.0004) and (0.0002) afghanistan (0.0003) and (0.0003) abroad. (0.0004) retains (0.0004) heat (0.0002) and (0.0001) absorbs (0.0001) sweat (-0.0001) in (0.0000) warm (0.0001) / (0.0000) hot (0.0001) conditions. (0.0001) imported. (0.0002) the (0.0003) keffiyeh (-0.0001) is (0.0002) also (0.0002) known (0.0002) as (0.0002) a (-0.0001) shmagh, (0.0001) shemagh (0.0001) or (0.0001) yashmag, (0.0002) a (0.0001) ghutra (0.0001) or (0.0003) a (0.0002) hatta, (0.0000) and (-0.0002) is (0.0005) a (0.0002) traditional (0.0003) headdress (-0.0002) of (0.0000) arab (0.0002) men, (0.0002) made (0.0002) of (0.0001) a (0.0001) square (0.0002) of (0.0001) cloth (0.0000) ( (0.0000) " (-0.0000) scarf (0.0003) " (0.0001) ), (0.0003) folded (0.0002) and (0.0001) wrapped (0.0001) in (0.0001) various (0.0002) styles (0.0001) around (0.0002) the (0.0000) head. (0.0001) it (0.0001) is (0.0000) commonly (0.0001) found (0.0001) in (0.0001) arid (0.0000) climate (0.0002) areas (0.0002) to (0.0001) provide (0.0001) protection (0.0002) from (0.0001) direct (0.0001) sun (0.0002) exposure, (0.0000) as (0.0002) well (0.0001) as (0.0001) for (0.0001) occasional (0.0001) use (0.0001) in (-0.0000) protecting (0.0002) the (-0.0000) mouth (0.0001) and (0.0001) eyes (0.0001) from (0.0001) blown (0.0001) dust (0.0001) and (0.0002) sand. (0.0002) worn (0.0000) and (0.0004) known (-0.0004) by (-0.0001) palestinians. (0.0005)
~~~~~~

**Node-1.5** (global 12465):

~~~~~~text
product (0.0013) from (0.0005) amazon (-0.0002) platform (0.0014) with (0.0012) title (0.0017) and (0.0015) content (0.0005) : (0.0012) title (0.0006) : (0.0013) missing. (-0.0007) content (0.0035) : (0.0017) this (0.0006) is (-0.0001) the (-0.0002) headband (0.0014) which (0.0009) is (0.0012) placed (0.0010) on (0.0005) top (0.0022) of (0.0005) the (0.0012) arab (-0.0010) scarf, (0.0001) known (0.0006) as (0.0013) agel. (0.0002) the (0.0005) agel (0.0006) is (0.0015) one (0.0015) size (0.0010) and (0.0015) is (0.0021) adaptable, (0.0013) by (0.0013) pulling (0.0008) the (-0.0001) string (0.0011) you (0.0013) would (0.0004) be (0.0008) able (0.0007) to (0.0007) change (0.0011) the (0.0002) size (0.0018) to (0.0008) make (0.0011) it (0.0014) fit (0.0017) your (0.0006) head (0.0008) size. (0.0000) the (-0.0002) ribbon (0.0011) will (0.0013) fit (0.0014) on (0.0012) any (0.0025) scarf, (-0.0013) the (-0.0006) traditional (0.0001) arab (-0.0006) scarves (0.0015) or (0.0009) the (-0.0002) modern (0.0002) colorful (0.0014) ones (0.0001) we (0.0004) have. (-0.0017) this (0.0014) is (0.0019) the (-0.0012) genuine (0.0000) agel (0.0005) arab (-0.0002) scarf! (0.0033) * (-0.0015) sunglasses (0.0010) are (0.0003) not (0.0023) included (0.0021) * (0.0041) * (0.0079) scarf (0.0015) is (0.0009) not (-0.0017) included (-0.0000) * (-0.0006)
~~~~~~

**Node-1.6** (global 12466):

~~~~~~text
product (0.0011) from (0.0031) amazon (0.0006) platform (0.0005) with (0.0011) title (-0.0001) and (0.0016) content (0.0004) : (0.0026) title (-0.0003) : (0.0013) white (0.0003) & (0.0012) amp (0.0026) ; (-0.0012) black (0.0004) shemagh (0.0005) heavyweight (-0.0020) arab (0.0020) tactical (0.0004) desert (-0.0002) keffiyeh (0.0004) scarf. (-0.0018) content (0.0018) : (0.0015) white (-0.0014) & (0.0004) black (0.0001) shemagh (0.0005) heavyweight (-0.0022) arab (0.0028) tactical (-0.0004) military (-0.0006) desert (-0.0010) keffiyeh (0.0003) scarf- (0.0008) made (0.0007) from (0.0010) 100 (0.0002) % (0.0000) heavy (0.0021) weight (-0.0005) cotton. (0.0013) high (0.0014) quality (0.0007) stitched (0.0010) material. (-0.0003) arabian (0.0012) pattern (0.0008) design. (-0.0010) designed (0.0005) to (0.0012) protect (0.0010) head (0.0010) & (-0.0008) neck (0.0011) from (0.0014) sun, (0.0005) sand (-0.0003) & (0.0012) wind. (-0.0004) tassles (0.0001) attached (0.0012) to (0.0002) ends (-0.0006) of (0.0010) shemagh (-0.0002) scarf. (0.0041) folded (-0.0010) & (0.0017) wrapped (0.0015) in (0.0008) various (0.0005) styles (0.0013) around (0.0007) the (-0.0007) head. (0.0007) dries (0.0009) quickly (0.0002) & (0.0010) keep (-0.0005) the (-0.0022) head (0.0003) warm. (0.0011) worn (-0.0013) across (-0.0003) the (-0.0020) forehead (0.0001) or (0.0005) neck. (-0.0008) used (0.0002) by (0.0013) military (-0.0002) soldiers (-0.0002) in (0.0001) afghanistan, (0.0011) iraq (-0.0001) & (0.0021) worldwide. (-0.0019) can (-0.0002) also (0.0005) be (0.0002) used (0.0010) as (0.0020) a (-0.0001) neck (0.0007) warmer (0.0003) or (0.0014) hand (0.0003) towel. (0.0006) extremely (-0.0003) fashionable (0.0009) & (0.0023) popular. (-0.0013) a (-0.0015) keffiyeh (0.0009) is (0.0015) also (0.0013) known (0.0006) as (0.0006) a (-0.0004) shmagh, (-0.0001) shemagh (-0.0001) or (0.0016) yashmag, (0.0005) a (-0.0000) ghutra (0.0006) or (-0.0002) a (-0.0005) hatta, (0.0007) and (0.0016) is (0.0005) a (0.0006) traditional (-0.0010) headdress (0.0001) of (0.0016) arab (-0.0004) men, (0.0008) made (0.0002) of (0.0003) a (-0.0011) square (0.0002) of (0.0002) cloth (-0.0006) ( (0.0001) " (0.0001) scarf (-0.0005) " (-0.0002) ), (-0.0001) folded (-0.0008) and (-0.0001) wrapped (-0.0008) in (0.0009) various (-0.0010) styles (-0.0012) around (0.0007) the (0.0001) head. (0.0002) color (0.0002) : (0.0017) white (0.0005) & (0.0004) black. (-0.0011) dimensions (-0.0001) : (0.0022) 42 (-0.0015) " (-0.0014) x (0.0007) 42 (0.0002) ". (0.0002)
~~~~~~

**Node-2** (global 1510):

~~~~~~text
product (-0.0131) from (0.0018) amazon (0.0003) platform (0.0046) with (-0.0001) title (0.0062) and (0.0016) content (0.0024) : (0.0083) title (-0.0007) : (0.0045) missing. (0.0025) content (0.0035) : (0.0113) brand (-0.0008) new (0.0027) arabic (-0.0005) shemagh (0.0036) head (0.0029) / (0.0033) neck (0.0011) scarf. (0.0011) this (0.0010) is (0.0033) a (0.0014) great (0.0026) value (0.0079) shemagh. (0.0036) plain (0.0000) black (0.0025) middle (0.0005) eastern (0.0066) head (0.0011) & (0.0051) neck (0.0019) scarf. (0.0049) it (0.0049) measures (0.0054) 39 (0.0026) " (0.0016) x (0.0036) 39 (-0.0033) " (0.0050) inches (-0.0033) ( (0.0037) 100 (0.0010) x (0.0019) 100 (0.0017) cm (0.0062) ). (0.0041) this (-0.0043) shemagh (0.0046) is (0.0034) made (0.0039) in (0.0013) india (0.0099) by (-0.0016) reliable. (0.0056) this (0.0012) type (0.0067) of (-0.0005) shemagh (0.0015) comes (0.0055) with (0.0028) hadab (0.0042) on (0.0010) two (0.0014) sides (0.0066) at (0.0040) the (-0.0027) ends (0.0047) of (0.0001) the (-0.0008) scarf (0.0101) ( (0.0002) tassel (0.0020) on (0.0038) the (0.0007) surrounding (0.0065) ). (-0.0024) this (0.0149) is (-0.0003) brand (0.0047) new. (0.0068)
~~~~~~

**Node-2.1** (global 1507):

~~~~~~text
product (-0.0006) from (0.0005) amazon (0.0004) platform (0.0010) with (-0.0002) title (0.0004) and (0.0004) content (0.0003) : (-0.0004) title (0.0006) : (0.0004) 40 (0.0007) & (0.0003) quot (-0.0000) ; (0.0002) x40 (0.0003) & (-0.0002) quot (0.0000) ; (0.0004) grey (-0.0002) lightweight (0.0004) shemagh (0.0006) arab (0.0003) tactical (0.0003) desert (0.0002) scarf (0.0008) keffiyeh. (0.0001) content (0.0002) : (-0.0001) color- (0.0001) gray (-0.0001) design- (0.0002) tassels (0.0001) around (0.0006) size- (0.0009) 40 (0.0003) " (-0.0004) by40 (0.0008) "- (0.0003) 101. (0.0003) 5cm (0.0007) by (-0.0002) 101. (-0.0001) 5cm. (0.0006) weight- (-0.0005) 3. (0.0004) 77 (0.0003) oz. (-0.0006)
~~~~~~

**Node-2.2** (global 12450):

~~~~~~text
product (0.0019) from (0.0004) amazon (0.0006) platform (0.0006) with (0.0010) title (0.0010) and (0.0006) content (0.0003) : (0.0013) title (0.0012) : (0.0004) condor (0.0006) tactical (-0.0002) cap- (0.0015) black. (0.0006) content (0.0014) : (0.0011) hat (-0.0002) with (0.0011) velcro (0.0002) for (0.0004) patch (0.0016) 1000 (0.0009) denier (0.0005) cordura (0.0010) nylon (0.0013) authentic (0.0003) crye (0.0009) precision (0.0008) fabric (0.0010) one (0.0006) size (0.0007) fits (0.0010) all (0.0003) ( (0.0009) adjustable (0.0010) ) (0.0002) with (0.0006) velcro (0.0005) for (0.0001) patch (0.0007) color (0.0014) black. (0.0000)
~~~~~~

**Node-2.3** (global 12469):

~~~~~~text
product (0.0006) from (0.0008) amazon (0.0005) platform (0.0002) with (0.0003) title (0.0010) and (0.0005) content (0.0002) : (0.0010) title (0.0006) : (0.0002) missing. (0.0002) content (0.0001) : (0.0001) our (0.0001) punisher (0.0007) tactical (0.0007) patches (0.0000) are (0.0003) 100 (0.0014) % (0.0012) embroidered (-0.0011) with (0.0005) velcro (0.0002) loop (0.0003) backing. (-0.0003) the (-0.0009) 2 (0.0008) " (0.0007) x3 (0.0008) " (0.0009) size (0.0012) is (0.0012) specifically (0.0008) desinged (0.0007) for (0.0006) use (0.0008) with (0.0003) tactical (0.0009) caps. (-0.0009)
~~~~~~

**Node-2.4** (global 12471):

~~~~~~text
product (0.0001) from (0.0000) amazon (0.0002) platform (-0.0001) with (-0.0001) title (0.0006) and (-0.0003) content (-0.0003) : (0.0003) title (0.0004) : (0.0002) change (0.0001) 1pc (0.0003) unisex (0.0001) fashion (0.0002) women (-0.0001) men (-0.0000) arab (0.0001) shemagh (0.0002) keffiyeh (-0.0001) palestine (-0.0000) scarf (-0.0004) shawl (0.0003) wrap (0.0002) ( (0.0003) purple (0.0003) ). (0.0005) content (0.0002) : (-0.0002) this (0.0007) trendy (0.0002) shaped (0.0005) scarf (0.0003) is (0.0001) a (0.0001) great (0.0001) addition (0.0001) to (0.0001) your (0.0006) collection (0.0003) of (0.0001) fashion (0.0004) accessories. (0.0001) high (0.0004) quality (0.0005) & (-0.0001) versatile. (0.0002) the (0.0004) most (0.0005) popular (0.0003) accessory (-0.0002) of (0.0001) this (-0.0003) season. (-0.0000) perfect (0.0005) for (0.0000) wearing (0.0003) around (0.0001) neck (0.0003) or (-0.0001) as (0.0001) a (0.0001) shoulder (0.0003) wrap. (0.0003) brings (0.0004) you (0.0003) simple (0.0003) & (-0.0000) effortless (0.0002) style (0.0002) along (0.0001) with (0.0003) warmth (0.0003) & (-0.0000) comfort. (0.0004) this (0.0004) makes (0.0005) an (-0.0000) excellent (0.0003) gift (0.0003) on (0.0003) any (0.0003) occasion. (0.0003) package (0.0004) include (-0.0000) : (0.0004) 1pc (0.0001) unisex (0.0002) fashion (0.0003) women (0.0001) men (0.0003) arab (0.0004) shemagh (0.0007) keffiyeh (0.0003) palestine (0.0007) scarf (0.0005) shawl (0.0003) wrap (0.0006) ( (-0.0002) without (0.0002) retail (0.0009) package (0.0008) ) (0.0006)
~~~~~~

**Node-2.5** (global 12472):

~~~~~~text
product (-0.0001) from (0.0004) amazon (0.0008) platform (0.0002) with (0.0004) title (0.0002) and (0.0003) content (-0.0000) : (0.0002) title (0.0001) : (0.0003) century (0.0004) & (0.0006) reg (0.0007) ; (0.0008) hand (0.0002) forearm (0.0003) armor. (0.0003) content (0.0002) : (0.0007) revolutionary (-0.0002) design- (0.0004) you (0.0000) ' (-0.0002) ve (-0.0001) never (0.0001) experienced (0.0003) sparring (0.0004) gear (0.0004) like (-0.0000) this (0.0000) before! (-0.0001) high- (0.0004) density. (0.0007) sold (0.0002) in (0.0002) pairs. (0.0000)
~~~~~~

**Node-2.6** (global 12468):

~~~~~~text
product (-0.0006) from (-0.0009) amazon (-0.0000) platform (0.0003) with (-0.0004) title (-0.0001) and (-0.0006) content (-0.0002) : (-0.0003) title (0.0005) : (-0.0001) mechanix (-0.0002) wear (-0.0004) mp3- (-0.0002) 05- (-0.0002) 010 (-0.0001) mpact3 (0.0000) knuckle (-0.0002) protection (0.0000) glove, (-0.0002) black, (-0.0001) large. (0.0004) content (-0.0002) : (-0.0002) the (-0.0001) m- (-0.0002) pact3 (-0.0001) glove (-0.0007) is (-0.0001) designed (-0.0005) to (-0.0004) deliver (-0.0004) under (-0.0005) the (-0.0002) toughest (-0.0004) conditions. (0.0001) we (-0.0001) ' (-0.0003) ve (-0.0003) started (-0.0002) with (-0.0003) the (-0.0002) components (0.0001) of (-0.0001) the (0.0000) heavy- (-0.0003) duty (-0.0001) mpact- (-0.0002) 2 (-0.0000) palm (-0.0003) and (-0.0002) then (-0.0002) fused (-0.0002) them (-0.0001) to (-0.0003) a (-0.0000) molded (-0.0000) kevlar (-0.0001) knuckle (-0.0002) shell. (0.0004) a (-0.0003) unique (-0.0004) top (-0.0003) stretch (-0.0001) panel (-0.0000) and (-0.0001) molded (0.0003) rubber (-0.0001) finger (-0.0005) ribbing (-0.0002) were (-0.0000) added (-0.0002) to (-0.0002) give (-0.0004) this (-0.0003) glove (-0.0004) maximum (-0.0002) flex (-0.0002) for (-0.0003) optimum (-0.0002) response (0.0001) to (-0.0002) your (-0.0007) every (-0.0003) move (-0.0003)
~~~~~~

**Node-2.7** (global 12473):

~~~~~~text
product (0.0001) from (-0.0000) amazon (0.0001) platform (0.0001) with (0.0000) title (0.0001) and (-0.0000) content (-0.0001) : (0.0000) title (0.0000) : (-0.0000) damascus (0.0000) dnkpb (0.0000) imperial (0.0000) neoprene (0.0000) knee (0.0001) pads (-0.0001) with (-0.0001) reinforced (0.0000) non- (0.0000) slip (0.0000) trion- (0.0001) x (0.0002) caps, (-0.0001) black. (-0.0002) content (0.0003) : (0.0000) created (0.0001) by (0.0001) damascus (-0.0000) protective (0.0001) gear, (0.0000) leaders (0.0001) in (0.0000) full (0.0001) body (0.0001) protective (-0.0000) gear (0.0001) for (0.0001) law (0.0000) enforcement, (0.0001) military, (-0.0000) etc. (0.0001) the (0.0001) imperial (0.0000) neoprene (0.0000) knee (0.0001) pads (0.0000) provide (0.0000) a (-0.0000) unique (0.0001) adjustment (0.0000) system (0.0001) allowing (-0.0000) for (0.0000) a (0.0000) very (0.0000) secure (0.0000) fit. (0.0000) high- (0.0000) density (-0.0001) closed- (0.0000) cell (0.0001) foam (0.0000) with (-0.0000) the (-0.0000) neoprene (-0.0000) outer (-0.0001) shell (0.0000) provides (-0.0000) for (-0.0000) its (0.0001) extremely (0.0000) comfortable (-0.0001) and (-0.0000) silent (-0.0001) design. (-0.0001) the (-0.0000) increased (-0.0000) grip (-0.0000) and (-0.0000) durability (0.0000) of (-0.0000) these (0.0002) pads (0.0001) is (0.0001) provided (-0.0000) by (-0.0000) the (0.0000) damascus (0.0002) trion- (0.0002) x (0.0001) textured (0.0001) non- (0.0001) slip (-0.0000) grip (0.0000) surface (0.0001) technology. (0.0004) matching (0.0000) elbow (0.0000) pads (-0.0001) available. (0.0002) sold (0.0001) as (0.0001) a (0.0000) pair. (0.0001) available (0.0002) colors (0.0002) and (0.0001) camouflage (0.0002) prints (0.0002) include (0.0000) : (0.0000) black, (0.0000) od (0.0000) green, (0.0000) tan, (0.0000) mullticam (0.0000) camo, (0.0001) digital (0.0001) woodland (0.0001) camo (0.0000) and (0.0000) acu (0.0000) digital (0.0001) camo. (0.0000) damascus (0.0002) is (0.0002) a (-0.0001) legacy (0.0002) brand (0.0001) with (-0.0001) well (-0.0001) over (-0.0000) 50 (0.0000) years (0.0000) of (0.0000) experience (0.0001) in (0.0000) glove (0.0000) and (0.0001) protective (-0.0000) gear (0.0000) design. (0.0000) the (0.0000) damascus (-0.0000) brand (0.0001) product (0.0003) line (-0.0000) focuses (0.0001) on (0.0001) head (0.0000) to (0.0001) toe (0.0000) non- (0.0001) ballistic (0.0001) protection. (-0.0000) damascus (0.0003) creates (0.0001) the (0.0000) latest (0.0001) in (0.0000) personal (0.0001) protection, (0.0000) from (0.0001) functionally (0.0001) superior (0.0001) cut- (0.0001) resistant (0.0001) gloves (0.0000) to (0.0000) cutting- (0.0001) edge, (0.0001) form- (0.0000) fitting (0.0001) duty (0.0001) gloves-- (0.0001) as (0.0001) well (0.0001) as (0.0001) unmatched (0.0001) full- (0.0000) body (0.0000) riot (0.0001) control (-0.0000) and (0.0001) tactical (-0.0000) gear. (-0.0001) our (0.0000) products (-0.0000) are (0.0001) worn (0.0001) with (-0.0001) confidence (0.0002) by (0.0001) departments (0.0000) worldwide. (0.0000)
~~~~~~

**Node-2.8** (global 12475):

~~~~~~text
product (0.0005) from (0.0001) amazon (-0.0000) platform (0.0000) with (0.0000) title (0.0002) and (0.0001) content (-0.0002) : (0.0004) title (0.0001) : (0.0003) matrix (0.0003) iron (-0.0000) face (-0.0001) carbon (0.0001) steel (0.0001) & (0.0000) quot (0.0001) ; (-0.0001) striker (0.0004) & (0.0001) quot (0.0000) ; (0.0003) metal (0.0001) mesh (0.0000) lower (0.0000) half (0.0001) mask (0.0001) ( (0.0004) black (0.0001) ). (0.0002) content (0.0002) : (-0.0001) there (0.0000) are (-0.0001) many (-0.0001) similar (0.0001) products (0.0003) in (0.0000) the (0.0001) market (0.0002) and (0.0002) we (0.0003) have (0.0001) carried (-0.0000) the (0.0001) highest (0.0000) quality (0.0000) version (0.0002) at (0.0002) factory (0.0001) direct (0.0001) pricing (0.0003) just (-0.0001) for (0.0001) you! (0.0001) applications (0.0002) : (0.0001) achieve (0.0001) full (0.0001) face (0.0001) protection (0.0003) with (0.0001) most (-0.0000) full (-0.0000) seal (0.0000) goggles (0.0000) and (0.0002) other (0.0001) similar (0.0002) size (0.0001) eye (0.0002) goggles. (0.0000) provides (0.0001) cheek, (0.0002) nose (0.0001) and (0.0003) mouth (-0.0001) lower (0.0000) face (0.0001) protection. (0.0001) adjustable. (0.0001)
~~~~~~

**Node-2.9** (global 12476):

~~~~~~text
product (-0.0003) from (-0.0001) amazon (0.0000) platform (0.0000) with (-0.0000) title (-0.0001) and (-0.0001) content (-0.0000) : (-0.0002) title (0.0001) : (-0.0000) change (-0.0001) 1pc (0.0000) unisex (-0.0000) fashion (-0.0001) women (-0.0001) men (0.0000) arab (0.0002) shemagh (-0.0000) keffiyeh (0.0000) palestine (-0.0001) scarf (0.0001) shawl (0.0000) wrap (0.0000) ( (0.0002) red (0.0001) ). (0.0003) content (0.0001) : (-0.0001) this (-0.0001) trendy (-0.0000) shaped (0.0000) scarf (0.0002) is (0.0001) a (-0.0001) great (-0.0000) addition (-0.0000) to (-0.0000) your (0.0002) collection (-0.0001) of (-0.0000) fashion (-0.0003) accessories. (0.0001) high (0.0000) quality (-0.0000) & (-0.0001) versatile. (0.0003) the (-0.0003) most (-0.0001) popular (-0.0002) accessory (-0.0002) of (-0.0002) this (0.0000) season. (0.0002) perfect (-0.0000) for (-0.0001) wearing (0.0001) around (0.0000) neck (0.0000) or (-0.0000) as (-0.0000) a (-0.0002) shoulder (0.0001) wrap. (-0.0000) brings (0.0001) you (-0.0001) simple (0.0001) & (-0.0001) effortless (0.0000) style (-0.0000) along (-0.0001) with (0.0001) warmth (0.0002) & (-0.0000) comfort. (0.0002) this (0.0001) makes (0.0001) an (-0.0002) excellent (-0.0001) gift (0.0001) on (-0.0001) any (-0.0000) occasion. (0.0000) package (0.0001) include (0.0005) : (0.0002) 1pc (-0.0000) unisex (0.0001) fashion (0.0001) women (0.0000) men (0.0001) arab (0.0003) shemagh (-0.0001) keffiyeh (0.0001) palestine (-0.0002) scarf (0.0003) shawl (-0.0000) wrap (0.0001) ( (-0.0002) without (-0.0001) retail (0.0002) package (0.0000) ) (-0.0000)
~~~~~~

**Node-3** (global 12449):

~~~~~~text
product (-0.0027) from (-0.0014) amazon (-0.0016) platform (-0.0017) with (-0.0010) title (-0.0024) and (-0.0007) content (-0.0026) : (-0.0026) title (-0.0031) : (-0.0016) missing. (-0.0014) content (-0.0012) : (-0.0016) up (-0.0019) for (-0.0003) sale (-0.0022) is (-0.0006) this (0.0025) brand (-0.0023) new (0.0002) black (-0.0011) arabic (0.0001) shemagh (-0.0000) head (-0.0006) scarf (0.0012) neck (-0.0002) wrap. (-0.0019) this (0.0011) is (0.0005) an (0.0010) authentic (0.0008) embroidered (0.0021) ( (0.0006) one (-0.0002) one (0.0003) side (-0.0007) ) (0.0020) shemagh (0.0006) top (0.0009) quality (-0.0002) black (0.0009) & (-0.0001) white (0.0013) middle (0.0003) eastern (0.0005) head (0.0003) cotton (0.0027) scarf. (0.0007) it (0.0021) measures (0.0010) 47 (0.0022) " (-0.0023) x (-0.0012) 47 (-0.0007) " (-0.0009) inches (-0.0015) ( (0.0003) 120 (0.0003) x (0.0005) 120 (-0.0001) cm (0.0003) ). (0.0009) this (-0.0007) shemagh (0.0008) is (0.0019) made (0.0006) by (-0.0009) relaible (-0.0007) which (0.0008) is (-0.0003) the (0.0006) finest (0.0006) quality (0.0025) in (-0.0019) india. (0.0018) this (-0.0009) one (-0.0008) of (-0.0037) our (-0.0030) top (0.0004) selling, (-0.0016) best (-0.0008) quality (0.0008) and (-0.0002) the (0.0002) softest (-0.0007) cotton (-0.0015) we (0.0026) carry. (-0.0000) this (0.0009) type (0.0004) of (0.0004) shemagh (0.0017) comes (0.0005) with (0.0014) white (0.0011) hadab (0.0016) on (0.0014) the (0.0010) ends (0.0004) of (0.0009) the (0.0015) scarf (0.0014) ( (0.0001) tassel (0.0006) on (0.0013) the (0.0003) surrounding (0.0006) ). (0.0002) this (-0.0016) is (-0.0009) brand (-0.0013) new. (-0.0007) the (0.0008) back (-0.0006) of (0.0012) the (0.0031) scarf (-0.0003) is (-0.0007) not (0.0001) embroidered (-0.0055)
~~~~~~

**Node-3.1** (global 12444):

~~~~~~text
product (-0.0001) from (0.0000) amazon (0.0002) platform (0.0003) with (0.0001) title (0.0002) and (0.0001) content (0.0005) : (-0.0003) title (0.0003) : (0.0003) desert (-0.0001) military (0.0001) tactial (0.0000) keffiyeh (-0.0003) shemagh (0.0000) white (0.0001) & (0.0005) amp (-0.0000) ; (0.0002) black. (0.0003) content (0.0002) : (0.0001) 100 (0.0002) % (0.0004) cotton (0.0002) material. (0.0010) black (0.0002) and (0.0003) white. (0.0006) size (0.0000) 42 (0.0007) " (-0.0005) x (-0.0001) 42 (0.0007) " (0.0001) ( (0.0000) inches (0.0005) ). (-0.0006) traditional (-0.0005) desert (-0.0000) arab (0.0003) head (0.0000) dress, (0.0001) which (0.0003) evolved (0.0001) from (0.0001) turbans (0.0002) in (0.0002) ancient (0.0006) times. (0.0003) essential (0.0002) for (0.0001) protecting (0.0000) the (-0.0001) eyes, (0.0001) nose, (0.0000) mouth, (0.0001) ears (0.0002) and (0.0001) face (0.0002) from (0.0002) sand. (-0.0000) can (0.0001) also (0.0002) be (0.0004) used (0.0004) as (0.0001) a (-0.0001) neck (0.0005) warmer (0.0005) or (0.0003) hand (0.0005) towel. (-0.0001) scarf (-0.0011) is (0.0005) high (0.0003) quality (0.0008) stitch. (0.0004) worn (0.0008) by (-0.0001) soldiers (0.0011) in (0.0002) iraq (0.0002) and (0.0001) afghanistan (0.0005) and (0.0004) abroad. (0.0003) retains (0.0005) heat (0.0002) and (0.0004) absorbs (0.0004) sweat (0.0005) in (0.0004) warm (0.0007) / (0.0004) hot (0.0002) conditions. (-0.0002) imported. (0.0002) the (0.0007) keffiyeh (0.0007) is (0.0004) also (0.0006) known (0.0004) as (0.0003) a (-0.0002) shmagh, (0.0003) shemagh (0.0000) or (0.0004) yashmag, (0.0003) a (-0.0000) ghutra (0.0000) or (0.0005) a (-0.0002) hatta, (-0.0001) and (-0.0008) is (0.0009) a (0.0005) traditional (0.0006) headdress (-0.0003) of (0.0004) arab (0.0001) men, (-0.0001) made (0.0000) of (0.0002) a (0.0001) square (0.0003) of (0.0003) cloth (-0.0002) ( (0.0004) " (0.0000) scarf (-0.0002) " (0.0003) ), (0.0002) folded (0.0004) and (0.0001) wrapped (0.0004) in (0.0004) various (0.0007) styles (0.0005) around (0.0004) the (0.0002) head. (0.0001) it (0.0003) is (0.0002) commonly (0.0002) found (0.0002) in (0.0003) arid (0.0001) climate (0.0002) areas (0.0002) to (0.0003) provide (0.0001) protection (0.0001) from (-0.0001) direct (0.0002) sun (0.0003) exposure, (0.0001) as (0.0001) well (0.0001) as (0.0001) for (0.0000) occasional (0.0002) use (0.0001) in (0.0003) protecting (0.0001) the (0.0001) mouth (0.0003) and (0.0002) eyes (0.0005) from (0.0001) blown (0.0003) dust (0.0004) and (0.0003) sand. (0.0003) worn (0.0001) and (0.0009) known (0.0001) by (0.0003) palestinians. (0.0002)
~~~~~~

**Node-3.2** (global 51010):

~~~~~~text
product (-0.0007) from (0.0002) amazon (-0.0001) platform (0.0001) with (0.0005) title (0.0002) and (0.0002) content (0.0001) : (0.0005) title (0.0003) : (0.0003) dark (0.0006) blue (-0.0004) arab (0.0004) shemagh (0.0004) head (0.0001) / (0.0003) neck (-0.0004) scarf (-0.0004) authentic (0.0003) quality (-0.0005) desert (0.0007) wear (-0.0002) wrap (0.0000) arafat (0.0003) palestine. (0.0007) content (-0.0001) : (0.0001) brand (0.0003) new (0.0002) dark (0.0004) navy (0.0006) blue (0.0002) arabic (-0.0011) shemagh (0.0007) head (0.0000) scarf (0.0001) neck (-0.0001) wrap. (-0.0001) this (0.0000) is (0.0000) an (0.0001) authentic (0.0005) embroidered (0.0004) ( (-0.0000) one (0.0004) one (0.0005) side (0.0002) ) (0.0002) shemagh (0.0003) top (0.0004) quality (-0.0001) dark (0.0007) blue (0.0001) & (-0.0002) white (0.0003) middle (0.0004) eastern (0.0005) 100 (0.0000) % (0.0004) cotton (0.0004) scarf. (0.0000) it (0.0006) measures (0.0002) 45 (-0.0001) " (0.0002) x (0.0002) 45 (-0.0005) " (0.0001) inches (-0.0003) ( (0.0008) 115 (-0.0003) x (-0.0005) 115 (0.0005) cm (0.0002) ). (-0.0003) this (-0.0005) shemagh (0.0005) is (0.0006) made (0.0004) by (-0.0000) relaible (0.0002) which (0.0000) is (0.0004) the (-0.0001) finest (0.0000) quality (0.0006) in (-0.0002) india. (-0.0014) this (0.0001) one (0.0004) of (-0.0005) our (0.0002) top (0.0004) selling, (-0.0003) best (-0.0001) quality (0.0001) and (-0.0000) the (0.0000) softest (0.0003) 100 (0.0004) % (-0.0000) cotton (-0.0001) we (0.0003) carry. (-0.0005) this (0.0004) type (0.0008) of (-0.0001) shemagh (0.0005) comes (-0.0002) with (0.0002) white (-0.0003) hadab (0.0002) on (0.0001) the (-0.0002) ends (0.0002) of (0.0004) the (0.0003) scarf (0.0003) ( (0.0004) tassel (0.0001) on (0.0004) the (-0.0000) surrounding (0.0008) ). (0.0001) the (0.0000) back (0.0003) of (0.0006) the (0.0002) scarf (0.0001) is (-0.0001) not (0.0004) embroidered (0.0015)
~~~~~~

**Node-3.3** (global 51011):

~~~~~~text
product (0.0001) from (0.0001) amazon (0.0005) platform (-0.0001) with (0.0002) title (0.0004) and (0.0003) content (-0.0002) : (0.0004) title (0.0003) : (0.0000) missing. (0.0001) content (0.0001) : (0.0004) brand (0.0002) new (0.0002) arabic (-0.0003) shemagh (0.0003) head (0.0002) scarf. (0.0000) this (0.0004) is (0.0003) an (0.0005) authentic (0.0004) embroidered (0.0003) black (0.0000) & (0.0003) white (0.0002) shemagh (0.0002) top (0.0001) quality (0.0003) middle (-0.0001) eastern (0.0002) head (0.0001) scarf. (0.0000) it (0.0002) measures (0.0001) 47 (0.0004) " (0.0001) x (0.0002) 47 (0.0001) " (0.0001) inches (-0.0001) ( (0.0003) 120 (0.0000) x (0.0002) 120 (0.0001) cm (-0.0001) ). (0.0002) this (-0.0000) shemagh (0.0002) is (0.0004) made (-0.0001) in (0.0002) syria. (0.0003) this (0.0002) type (0.0003) of (0.0001) shemagh (0.0002) comes (0.0003) with (0.0002) very (0.0003) light (0.0002) hadab (0.0001) on (0.0001) the (-0.0000) ends (0.0002) of (0.0001) the (0.0000) scarf (0.0002) ( (0.0002) tassel (0.0001) on (0.0003) the (0.0000) surrounding (0.0003) ). (-0.0001) this (0.0005) is (0.0000) brand (0.0003) new (-0.0002) and (0.0002) each (0.0001) comes (0.0001) in (0.0001) its (0.0003) own (0.0001) packaging. (-0.0004) the (0.0004) back (0.0003) of (-0.0000) this (0.0006) scarf (-0.0000) is (0.0005) plain (0.0003) just (0.0000) like (0.0004) the (-0.0002) last (0.0013) picture (0.0010)
~~~~~~

**Node-3.4** (global 51012):

~~~~~~text
product (-0.0006) from (-0.0003) amazon (0.0006) platform (-0.0001) with (-0.0004) title (0.0003) and (0.0000) content (-0.0002) : (0.0006) title (0.0005) : (0.0003) missing. (0.0002) content (0.0002) : (0.0006) brand (-0.0004) new (-0.0002) red (0.0006) arabic (-0.0002) shemagh (0.0003) head (0.0004) scarf (-0.0000) neck (0.0001) wrap. (0.0003) this (0.0001) is (0.0005) an (0.0005) authentic (0.0005) embroidered (0.0003) ( (-0.0001) one (0.0002) one (0.0001) side (0.0002) ) (0.0003) shemagh (0.0004) top (0.0002) quality (0.0001) red (0.0000) & (0.0001) white (0.0003) middle (-0.0001) eastern (0.0007) head (0.0002) cotton (0.0002) scarf. (-0.0012) it (0.0009) measures (0.0007) 47 (0.0002) " (-0.0003) x (0.0001) 47 (0.0002) " (0.0003) inches (-0.0004) ( (0.0002) 120 (0.0001) x (0.0002) 120 (-0.0000) cm (-0.0001) ). (-0.0000) this (0.0002) shemagh (0.0003) is (0.0004) made (0.0000) by (-0.0001) relaible (0.0001) which (0.0001) is (0.0002) the (0.0001) finest (0.0001) quality (0.0004) in (0.0001) india. (-0.0005) this (0.0003) one (0.0001) of (-0.0001) our (0.0000) top (0.0005) selling, (-0.0001) best (0.0004) quality (0.0002) and (0.0000) the (0.0003) softest (0.0004) cotton (0.0003) we (0.0000) carry. (-0.0001) this (0.0003) type (0.0007) of (-0.0002) shemagh (0.0005) comes (0.0002) with (0.0001) white (0.0006) hadab (0.0003) on (0.0002) the (0.0002) ends (0.0004) of (0.0003) the (0.0004) scarf (0.0010) ( (-0.0000) tassel (0.0002) on (0.0004) the (0.0001) surrounding (0.0005) ). (-0.0002)
~~~~~~

**Node-4** (global 12463):

~~~~~~text
product (-0.0090) from (0.0029) amazon (-0.0036) platform (-0.0037) with (0.0035) title (0.0093) and (0.0036) content (0.0045) : (0.0093) title (-0.0031) : (0.0047) missing. (-0.0048) content (0.0017) : (0.0022) soft (-0.0054) comfortable (0.0079) kufi (0.0061) hat. (0.0032) high (0.0057) quality (0.0087) machine (0.0021) knit. (0.0176) stretches (0.0079) to (-0.0044) fit (-0.0019) comfortable (0.0048) on (0.0078) almost (0.0029) any (-0.0080) head (0.0037) size. (0.0139) imported (-0.0097) from (0.0199) turkey. (0.0134)
~~~~~~

**Node-4.1** (global 51050):

~~~~~~text
product (0.0024) from (0.0009) amazon (0.0002) platform (-0.0001) with (0.0008) title (0.0033) and (0.0002) content (0.0003) : (0.0021) title (0.0019) : (0.0019) missing. (0.0014) content (-0.0001) : (0.0015) kufi (0.0007) hat (0.0006) crochet (0.0020) cap (0.0017) beanie- (0.0009) dark (0.0009) gray (-0.0002) grey (-0.0009)
~~~~~~

**Node-4.2** (global 51053):

~~~~~~text
product (-0.0002) from (0.0002) amazon (0.0004) platform (-0.0003) with (-0.0001) title (0.0004) and (-0.0000) content (0.0005) : (0.0004) title (0.0001) : (0.0004) missing. (0.0001) content (0.0007) : (0.0006) soft (0.0001) comfortable (0.0002) quality (0.0004) machine- (0.0002) knit (0.0004) open- (0.0004) work (-0.0002) design (0.0003) kufi (0.0000) hat. (0.0006) stretches (0.0012) to (0.0000) fit (0.0002) comfortably (0.0001) small (0.0002) to (0.0001) medium (0.0000) head (-0.0000) sizes (0.0002) ( (0.0003) not (0.0001) large (0.0001) ). (0.0003) imported (0.0006) from (0.0004) turkey. (0.0006) note (0.0002) : (0.0008) this (-0.0004) kufi (0.0007) is (0.0004) not (0.0001) designed (0.0005) for (0.0004) individuals (0.0004) with (0.0001) long (0.0004) hair. (-0.0000) it (-0.0001) is (0.0002) made (0.0002) to (-0.0001) be (0.0003) somewhat (-0.0000) snug (0.0002) on (0.0002) the (-0.0008) skull. (-0.0001)
~~~~~~

**Node-4.3** (global 51059):

~~~~~~text
product (0.0009) from (0.0007) amazon (0.0008) platform (-0.0003) with (0.0000) title (0.0002) and (0.0002) content (0.0008) : (0.0001) title (-0.0003) : (0.0004) missing. (0.0006) content (0.0008) : (0.0007) soft (0.0000) comfortable (-0.0007) kufi (-0.0007) hat. (0.0004) hand- (0.0001) crocheted. (0.0002) stretches (0.0006) to (0.0006) fit (0.0005) comfortable (-0.0003) on (-0.0002) almost (0.0006) any (0.0006) head (0.0004) size. (-0.0002)
~~~~~~

**Node-5** (global 12467):

~~~~~~text
product (-0.0025) from (0.0016) amazon (-0.0016) platform (0.0009) with (0.0020) title (0.0081) and (0.0036) content (0.0011) : (0.0044) title (0.0051) : (0.0019) authentic (0.0059) and (0.0042) new (0.0035) head (-0.0004) shemagh (0.0041) arab (0.0048) kafiya (0.0012) keffiyeh (0.0019) kufiya (0.0041) with (0.0029) agal (0.0033) red (0.0012) & (0.0088) amp (0.0021) ; (0.0079) white (-0.0032) the (-0.0025) same (0.0055) israel, (0.0010) palestine (0.0023) and (0.0039) british (0.0027) sas (0.0009) military (0.0002) use (0.0017) unique (0.0021) and (0.0052) retro (0.0014) look, (0.0047) soft (0.0030) and (0.0029) lightweight (-0.0035) great (0.0019) and (0.0035) cool (0.0017) unisex (0.0035) accessory. (0.0067) content (0.0007) : (-0.0005) authentic (-0.0034) arab (0.0013) middle (-0.0038) eastern (0.0041) red (0.0032) & (0.0029) kafiya (0.0023) with (0.0061) agal. (0.0054) also (0.0074) ideal (0.0022) for (0.0030) sun (0.0009) and (0.0037) desert (0.0070) gear. (0.0060) identical (-0.0047) to (0.0036) the (-0.0034) one (0.0008) king (-0.0016) hussein (0.0103) use (0.0026) to (0.0015) wear. (0.0035)
~~~~~~

**Node-5.1** (global 50828):

~~~~~~text
product (0.0002) from (0.0003) amazon (-0.0000) platform (0.0010) with (0.0001) title (0.0004) and (0.0004) content (-0.0003) : (0.0005) title (0.0003) : (0.0002) km (0.0003) outfitters (0.0006) & (0.0005) reg (-0.0002) ; (0.0003) pakistan (0.0004) shemagh (-0.0008) keffiyeh- (-0.0002) choose (0.0005) color!. (0.0005) content (0.0000) : (-0.0003) made (0.0000) from (0.0003) 100 (0.0000) % (-0.0002) heavy (0.0006) weight (0.0004) cotton. (0.0015) high (0.0003) quality (0.0005) stitched (0.0002) material. (0.0016) arabian (-0.0007) pattern (0.0001) design. (0.0007) designed (0.0001) to (-0.0000) protect (0.0001) head (0.0000) & (0.0005) neck (0.0001) from (-0.0001) sun, (0.0001) sand (0.0004) & (0.0005) wind. (0.0003) tassles (-0.0001) attached (-0.0000) to (-0.0000) ends (0.0000) of (-0.0002) shemagh (-0.0004) scarf. (-0.0010) folded (0.0004) & (0.0001) wrapped (-0.0001) in (0.0001) various (0.0001) styles (-0.0001) around (-0.0002) the (0.0001) head. (0.0001) dries (-0.0003) quickly (0.0004) & (0.0003) keep (0.0000) the (0.0001) head (-0.0001) warm. (-0.0003) worn (-0.0002) across (0.0001) the (0.0001) forehead (0.0001) or (0.0002) neck. (-0.0004) used (0.0000) by (-0.0004) military (-0.0004) soldiers (0.0001) in (0.0002) afghanistan, (-0.0004) iraq (-0.0003) & (-0.0001) worldwide. (0.0001) can (0.0000) also (-0.0000) be (0.0003) used (0.0001) as (0.0000) a (-0.0000) neck (0.0003) warmer (0.0004) or (0.0002) hand (0.0003) towel. (-0.0008) extremely (0.0006) fashionable (0.0003) & (-0.0003) popular. (-0.0001) a (0.0009) keffiyeh (0.0002) is (0.0003) also (0.0001) known (0.0007) as (0.0005) a (0.0002) shmagh, (0.0001) shemagh (0.0002) or (0.0002) yashmag, (0.0003) a (0.0002) ghutra (0.0001) or (0.0003) a (0.0001) hatta, (0.0001) and (0.0001) is (0.0009) a (0.0002) traditional (0.0004) headdress (0.0003) of (0.0001) arab (0.0008) men, (0.0003) made (0.0003) of (-0.0000) a (0.0002) square (0.0004) of (0.0001) cloth (0.0002) ( (-0.0003) " (0.0004) scarf (0.0006) " (0.0006) ), (0.0001) folded (0.0006) and (0.0004) wrapped (-0.0000) in (0.0004) various (0.0004) styles (0.0003) around (-0.0002) the (0.0004) head. (0.0003) works (0.0000) well (0.0003) as (0.0001) alternative (0.0000) winter (0.0002) headwear, (0.0001) particularly (0.0000) in (0.0001) areas (0.0002) with (-0.0002) snow (0.0004) and (-0.0000) strong (0.0002) winds. (0.0001) the (-0.0001) shemagh, (0.0004) also (0.0002) known (-0.0001) as (0.0003) the (0.0002) keffiyeh (0.0003) or (0.0003) arab (0.0007) scarf, (0.0001) is (0.0002) a (0.0002) simple (0.0002) yet (0.0001) efficient (0.0002) way (0.0001) to (0.0002) protect (0.0001) your (0.0002) face (-0.0001) and (0.0001) neck (0.0001) from (-0.0001) sun, (-0.0000) wind (-0.0001) and (-0.0000) sand. (0.0000) it (0.0004) also (0.0001) works (0.0001) well (-0.0000) as (0.0001) alternative (0.0000) winter (0.0004) headwear, (-0.0001) particularly (-0.0001) in (-0.0001) areas (-0.0000) with (-0.0002) snow (0.0003) and (0.0001) strong (-0.0001) winds. (0.0001) although (0.0004) most (0.0003) are (0.0003) cotton, (0.0003) warmer, (0.0004) faster- (-0.0000) drying (-0.0001) cotton- (0.0003) wool (0.0007) blends (-0.0000) are (0.0002) also (0.0000) available. (-0.0000) styles (-0.0002) of (-0.0003) wearing (0.0001) the (0.0006) shemagh (0.0002) vary, (-0.0003) but (-0.0000) wrapping (-0.0003) the (0.0000) scarf (-0.0001) around (-0.0003) the (0.0003) head (-0.0002) and (-0.0000) face (-0.0002) provides (0.0002) optimal (-0.0001) protection (-0.0001) from (0.0001) the (0.0002) elements. (-0.0002) shemaghs (0.0008) are (-0.0003) made (0.0000) from (0.0002) 100 (-0.0001) % (-0.0009) cotton (0.0002) and (0.0000) will (0.0002) shrink (-0.0004) if (0.0001) not (0.0000) washed (0.0003) properly. (0.0005) import. (0.0004) dimensions (-0.0005) : (0.0008) 42 (0.0004) " (-0.0002) x42 (0.0004) " (-0.0000)
~~~~~~

**Node-5.2** (global 51064):

~~~~~~text
product (0.0002) from (0.0003) amazon (-0.0000) platform (0.0010) with (0.0001) title (0.0004) and (0.0004) content (-0.0003) : (0.0005) title (0.0003) : (0.0002) km (0.0003) outfitters (0.0006) & (0.0005) reg (-0.0002) ; (0.0003) pakistan (0.0004) shemagh (-0.0008) keffiyeh- (-0.0002) choose (0.0005) color!. (0.0005) content (0.0000) : (-0.0003) made (0.0000) from (0.0003) 100 (0.0000) % (-0.0002) heavy (0.0006) weight (0.0004) cotton. (0.0015) high (0.0003) quality (0.0005) stitched (0.0002) material. (0.0016) arabian (-0.0007) pattern (0.0001) design. (0.0007) designed (0.0001) to (-0.0000) protect (0.0001) head (0.0000) & (0.0005) neck (0.0001) from (-0.0001) sun, (0.0001) sand (0.0004) & (0.0005) wind. (0.0003) tassles (-0.0001) attached (-0.0000) to (-0.0000) ends (0.0000) of (-0.0002) shemagh (-0.0004) scarf. (-0.0010) folded (0.0004) & (0.0001) wrapped (-0.0001) in (0.0001) various (0.0001) styles (-0.0001) around (-0.0002) the (0.0001) head. (0.0001) dries (-0.0003) quickly (0.0004) & (0.0003) keep (0.0000) the (0.0001) head (-0.0001) warm. (-0.0003) worn (-0.0002) across (0.0001) the (0.0001) forehead (0.0001) or (0.0002) neck. (-0.0004) used (0.0000) by (-0.0004) military (-0.0004) soldiers (0.0001) in (0.0002) afghanistan, (-0.0004) iraq (-0.0003) & (-0.0001) worldwide. (0.0001) can (0.0000) also (-0.0000) be (0.0003) used (0.0001) as (0.0000) a (-0.0000) neck (0.0003) warmer (0.0004) or (0.0002) hand (0.0003) towel. (-0.0008) extremely (0.0006) fashionable (0.0003) & (-0.0003) popular. (-0.0001) a (0.0009) keffiyeh (0.0002) is (0.0003) also (0.0001) known (0.0007) as (0.0005) a (0.0002) shmagh, (0.0001) shemagh (0.0002) or (0.0002) yashmag, (0.0003) a (0.0002) ghutra (0.0001) or (0.0003) a (0.0001) hatta, (0.0001) and (0.0001) is (0.0009) a (0.0002) traditional (0.0004) headdress (0.0003) of (0.0001) arab (0.0008) men, (0.0003) made (0.0003) of (-0.0000) a (0.0002) square (0.0004) of (0.0001) cloth (0.0002) ( (-0.0003) " (0.0004) scarf (0.0006) " (0.0006) ), (0.0001) folded (0.0006) and (0.0004) wrapped (-0.0000) in (0.0004) various (0.0004) styles (0.0003) around (-0.0002) the (0.0004) head. (0.0003) works (0.0000) well (0.0003) as (0.0001) alternative (0.0000) winter (0.0002) headwear, (0.0001) particularly (0.0000) in (0.0001) areas (0.0002) with (-0.0002) snow (0.0004) and (-0.0000) strong (0.0002) winds. (0.0001) the (-0.0001) shemagh, (0.0004) also (0.0002) known (-0.0001) as (0.0003) the (0.0002) keffiyeh (0.0003) or (0.0003) arab (0.0007) scarf, (0.0001) is (0.0002) a (0.0002) simple (0.0002) yet (0.0001) efficient (0.0002) way (0.0001) to (0.0002) protect (0.0001) your (0.0002) face (-0.0001) and (0.0001) neck (0.0001) from (-0.0001) sun, (-0.0000) wind (-0.0001) and (-0.0000) sand. (0.0000) it (0.0004) also (0.0001) works (0.0001) well (-0.0000) as (0.0001) alternative (0.0000) winter (0.0004) headwear, (-0.0001) particularly (-0.0001) in (-0.0001) areas (-0.0000) with (-0.0002) snow (0.0003) and (0.0001) strong (-0.0001) winds. (0.0001) although (0.0004) most (0.0003) are (0.0003) cotton, (0.0003) warmer, (0.0004) faster- (-0.0000) drying (-0.0001) cotton- (0.0003) wool (0.0007) blends (-0.0000) are (0.0002) also (0.0000) available. (-0.0000) styles (-0.0002) of (-0.0003) wearing (0.0001) the (0.0006) shemagh (0.0002) vary, (-0.0003) but (-0.0000) wrapping (-0.0003) the (0.0000) scarf (-0.0001) around (-0.0003) the (0.0003) head (-0.0002) and (-0.0000) face (-0.0002) provides (0.0002) optimal (-0.0001) protection (-0.0001) from (0.0001) the (0.0002) elements. (-0.0002) shemaghs (0.0008) are (-0.0003) made (0.0000) from (0.0002) 100 (-0.0001) % (-0.0009) cotton (0.0002) and (0.0000) will (0.0002) shrink (-0.0004) if (0.0001) not (0.0000) washed (0.0003) properly. (0.0005) import. (0.0004) dimensions (-0.0005) : (0.0008) 42 (0.0004) " (-0.0002) x42 (0.0004) " (-0.0000)
~~~~~~

**Node-6** (global 51060):

~~~~~~text
product (0.0011) from (0.0023) amazon (-0.0050) platform (-0.0068) with (0.0028) title (0.0071) and (0.0008) content (0.0012) : (0.0080) title (-0.0001) : (0.0008) proforce (0.0009) shemagh (0.0019) scarf (-0.0003) sand (-0.0027) solid. (0.0064) content (-0.0016) : (0.0035) traditional (-0.0014) desert (0.0019) head (-0.0003) wear, (0.0019) essential (0.0010) for (0.0007) protecting (0.0041) eyes, (0.0031) nose, (0.0026) mouth (0.0014) and (0.0050) neck (0.0018) from (0.0028) sand. (0.0063) can (0.0002) also (0.0033) be (0.0030) used (0.0035) as (0.0030) a (-0.0077) neck (0.0009) warmer (0.0047) and (0.0044) or (0.0050) hand (0.0033) towel. (0.0070) currently (0.0036) used (0.0036) by (0.0044) us (0.0018) and (0.0030) british (-0.0010) forces (0.0030) in (0.0054) iraq (0.0021) and (0.0053) afghanistan. (0.0029) 100 (-0.0066) % (0.0061) cotton, (0.0021) 44 (-0.0026) in. (0.0016) x (0.0040) 44 (-0.0032) in. (-0.0018) opened (0.0071) out. (0.0012)
~~~~~~

**Node-7** (global 51061):

~~~~~~text
product (-0.0009) from (0.0008) amazon (-0.0020) platform (-0.0002) with (0.0003) title (0.0009) and (0.0016) content (-0.0020) : (0.0001) title (0.0009) : (-0.0005) missing. (-0.0023) content (0.0032) : (0.0009) brand (-0.0006) new (-0.0005) all (0.0019) black (0.0018) with (0.0014) black (0.0017) trim (0.0010) arabic (-0.0053) shemagh (0.0021) head (0.0024) scarf (-0.0038) neck (0.0053) wrap. (0.0007) this (0.0016) is (0.0034) an (0.0008) authentic (0.0053) embroidered (0.0004) ( (0.0016) one (0.0016) one (0.0015) side (0.0016) ) (0.0031) shemagh (0.0023) top (0.0013) quality (-0.0007) black (0.0002) on (0.0031) black (0.0001) middle (0.0022) eastern (0.0023) head (0.0026) cotton (0.0039) scarf. (0.0007) it (0.0031) measures (-0.0004) 47 (0.0010) " (-0.0018) x (0.0033) 47 (-0.0016) " (0.0009) inches (-0.0019) ( (0.0021) 120 (0.0022) x (0.0007) 120 (0.0011) cm (0.0024) ). (0.0024) this (0.0014) shemagh (0.0040) is (0.0026) made (0.0029) by (-0.0003) relaible (0.0004) which (0.0003) is (0.0011) the (-0.0015) finest (0.0005) quality (0.0068) in (0.0014) india. (-0.0063) this (0.0018) one (0.0002) of (-0.0020) our (-0.0063) top (0.0031) selling, (0.0001) best (0.0007) quality (0.0012) and (0.0018) the (-0.0010) softest (0.0020) cotton (0.0032) we (-0.0034) carry. (-0.0016) this (0.0028) type (0.0043) of (-0.0023) shemagh (0.0036) comes (0.0043) with (0.0006) black (0.0013) hadab (0.0041) on (0.0011) the (-0.0013) ends (0.0024) of (0.0018) the (0.0018) scarf (0.0028) ( (0.0011) tassel (0.0010) on (0.0034) the (0.0007) surrounding (0.0022) ). (0.0004) this (0.0024) is (0.0020) brand (-0.0025) new. (0.0005) the (0.0001) back (-0.0002) of (0.0022) the (0.0031) scarf (-0.0031) is (0.0023) not (0.0035) embroidered (-0.0064) just (-0.0002) like (-0.0006) it (-0.0002) showes (0.0010) in (0.0001) the (-0.0030) last (0.0015) picture (-0.0012) on (0.0003) top! (0.0009) this (-0.0025) head (-0.0014) scarf (0.0003) is (-0.0001) worn (-0.0006) by (0.0015) everyone (-0.0004) world- (0.0035) wide. (0.0029)
~~~~~~

**Node-8** (global 51062):

~~~~~~text
product (-0.0065) from (-0.0020) amazon (-0.0015) platform (-0.0011) with (-0.0007) title (0.0021) and (0.0010) content (-0.0014) : (0.0016) title (0.0004) : (0.0016) missing. (-0.0007) content (-0.0006) : (0.0019) brand (-0.0016) new (-0.0003) light (0.0000) black (0.0011) arabic (-0.0003) shemagh (0.0011) head (0.0007) scarf (-0.0009) neck (0.0021) wrap. (0.0020) this (0.0013) is (0.0032) an (0.0010) authentic (0.0046) embroidered (0.0020) ( (-0.0009) one (0.0015) one (0.0009) side (0.0018) ) (0.0028) shemagh (0.0015) top (0.0020) quality (0.0005) light (0.0011) black (0.0016) & (0.0013) white (0.0017) middle (0.0000) eastern (0.0029) 100 (0.0005) % (0.0024) cotton (0.0014) scarf. (0.0021) it (0.0029) measures (0.0008) 47 (-0.0002) " (-0.0008) x (0.0030) 47 (-0.0007) " (0.0004) inches (0.0006) ( (0.0014) 120 (0.0010) x (0.0003) 120 (0.0001) cm (0.0012) ). (0.0030) this (0.0018) shemagh (0.0014) is (0.0035) made (0.0011) by (-0.0003) relaible (-0.0001) which (0.0009) is (0.0016) the (-0.0013) finest (0.0008) quality (0.0029) in (-0.0027) india. (-0.0005) this (0.0007) one (-0.0006) of (-0.0024) our (-0.0027) top (0.0018) selling, (-0.0012) best (-0.0001) quality (0.0007) and (0.0006) the (-0.0005) softest (0.0008) 100 (0.0010) % (0.0001) cotton (-0.0021) we (-0.0015) carry. (-0.0018) this (0.0000) type (0.0029) of (-0.0024) shemagh (0.0025) comes (0.0038) with (0.0018) white (0.0026) hadab (0.0015) on (0.0006) the (-0.0006) ends (0.0014) of (0.0006) the (0.0007) scarf (0.0023) ( (0.0004) tassel (0.0012) on (0.0017) the (-0.0007) surrounding (0.0032) ). (0.0035)
~~~~~~
