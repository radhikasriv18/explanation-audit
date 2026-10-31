# Reference packet: GraphNarrator__Llama-8B__products__18243

- Method: GraphNarrator; configuration: Llama-8B; dataset: products; target node: 18243
- Explanation source: `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/61.json` (messages[assistant])
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

- ROOT (product)
  - Node-1 (product)
    - Node-1.1 (Epson ink cartridge)
    - Node-1.2 (GE energy-saving bulb)
    - Node-1.3 (remanufactured ink cartridges)
    - Node-1.4 (Bosch cordless drill driver kit)
    - Node-1.5 (science fair titles)

### Word-Level Evaluation:

Keywords with high saliency scores in ROOT — "product" (0.02), "title" (0.08), "content" (0.04) — are generic and do not strongly indicate a specific category. However, the presence of "canon" (0.03) and "pg-" (0.01) suggests a connection to printer-related products.

### Graph-Level Aggregation:

Node-1 (product) is a direct neighbor with moderate saliency, but its keywords — "amazon" (-0.03), "platform" (-0.09) — are not indicative of a specific category. However, Node-1.1 (Epson ink cartridge) and Node-1.3 (remanufactured ink cartridges) are both related to printer accessories, with Node-1.1 having a high saliency score for "ink" (0.04) and "cartridge" (0.05). Node-1.4 (Bosch cordless drill driver kit) is a power tool, which is a different category from the others. Node-1.5 (science fair titles) is a miscellaneous item.

### Free-Text Explanation
```markdown
The classification of ROOT into "Cell Phones & Accessories" is not strongly supported by its own keywords or the co-purchase neighborhood.

ROOT: Keywords like "product" (0.02), "title" (0.08), and "content" (0.04) are generic and do not strongly indicate a specific category.
  - Node-1: A product (keywords: "amazon" (-0.03), "platform" (-0.09)) is a generic term and does not provide strong evidence for a specific category.
    - Node-1.1: An Epson ink cartridge (keywords: "ink" (0.04), "cartridge" (0.05)) is a printer accessory, which is a different category from the classification label.
    - Node-1.2: A GE energy-saving bulb (keywords: "energy" (0.00), "bulb" (0.00)) is a household item and not related to cell phones or accessories.
    - Node-1.3: Remanufactured ink cartridges (keywords: "ink" (0.00), "cartridges" (0.00)) are also printer accessories, but the category is not strongly supported by the entire co-purchase neighborhood.
    - Node-1.4: A Bosch cordless drill driver kit (keywords: "cordless" (0.01), "drill" (0.00)) is a power tool, which is a different category from the others.
    - Node-1.5: Science fair titles (keywords: "science" (0.00), "titles" (0.00)) are miscellaneous items and do not support the classification label.

In summary, the classification of ROOT into "Cell Phones & Accessories" is not strongly supported by its own keywords or the co-purchase neighborhood, as the majority of the nodes are related to different categories.
```
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/61.json`).

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
<verbalized-graph>ROOT: product(0.02) amazon(-0.03) platform(-0.09) title(0.02) content(0.04) title(0.08) canon(0.03) pg-(-0.00) 210xl(-0.00) cl-(0.01) 211xl(0.00) color(0.02) ink(0.04) cartridge(0.05) combo(0.04) pack-(0.04) black.(0.05) content(0.00) canon(0.01) pg-(0.00) 210xl(0.01) cl-(0.03) 211xl(0.00) color(0.00) ink(0.02) cartridge(0.04) combo(0.04) pack-(0.03) black(-0.04) 
Node-1: product(-0.01) amazon(-0.00) platform(-0.00) title(0.01) content(0.01) title(0.05) gp(0.05) spectrum(0.02) multi-(0.06) use(0.02) paper,(0.02) 8.(0.03) 5(0.03) x(0.01) 11(0.03) inches,(0.01) 3-(0.03) ream(0.02) pack(0.03) 1500(0.06) sheets(0.03) 998606(0.02) ).(0.04) content(0.01) georgia-(0.02) pacific(0.05) spectrum(0.00) standard(0.01) 92(0.01) multipurpose(0.02) paper(0.02) designed(0.03) copying(0.04) printing(0.02) wide(0.03) variety(0.03) imaging(0.06) devices.(0.04) bright(-0.00) white(0.03) paper(0.05) great(0.02) around(0.01) performer,(0.02) ideal(-0.04) everyday(0.03) communications(0.04) include(0.03) black(0.03) white(0.03) text(-0.01) graphics.(-0.02) performs(0.09) well(0.03) copiers,(0.02) laser(0.02) multi-(0.05) function(0.03) printers,(-0.00) well(0.01) high-(0.03) volume(0.05) printing(0.03) equipment.(-0.06) quality,(0.04) consistency(0.03) reliable(-0.02) day-(0.03) to-(0.05) day(-0.00) performance,(0.03) spectrum(0.07) standard(0.07) 92(0.06) multipurpose(0.04) paper(0.09) solid(0.21) choice.(-0.03) 
Node-1.1: product(-0.00) amazon(0.01) platform(0.00) title(0.01) content(0.02) title(0.01) epson(-0.00) durabrite(0.00) t126120(0.00) ultra(0.02) 126(-0.00) high-(0.00) capacity(0.00) inkjet(0.00) cartridge-(0.01) black.(0.03) content(-0.01) epson(-0.00) durabrite(0.00) ultra(-0.00) ink,(0.01) black(0.00) t126120(0.01) 
Node-1.2: product(-0.00) amazon(0.00) platform(0.00) title(0.00) content(0.00) title(0.00) ge(0.00) lighting(0.00) 75368(0.00) energy(0.00) smart(-0.00) 13-(0.00) watt(0.00) spiral(0.00) compact(0.00) fluorescent(0.00) bulb,(0.00) candelabra(0.00) base,(0.00) 2-(0.00) pack.(0.00) content(0.00) ge(0.00) 75368(0.00) energy(0.00) smart(-0.00) 13(0.00) watt(0.00) spiral(0.00) cfl(0.00) ceiling(0.00) fan(0.00) candelabra(0.00) base(0.00) 60-(0.00) watt(0.00) replacement.(-0.00) ge(0.00) compact(0.00) fluorescent(0.00) lamps(0.00) cfl(-0.00) offer(0.00) many(0.00) advantages(-0.00) include(0.00) cost(0.00) savings,(0.00) extra(0.00) long(0.00) life,(0.00) light(0.00) output,(0.00) color(0.00) rendering.(0.00) cfl(0.00) get(0.00) dramatic(0.00) energy(0.00) cost(0.00) savings(0.00) 77(0.00) percent(0.00) vs.(0.00) incandescent(0.00) lamps(0.00) comparable(0.00) light(0.00) output.(-0.00) extra(0.00) long(0.00) life(-0.00) last(0.00) 8(0.00) 10(0.00) times(0.00) longer,(0.00) last(0.00) 20(0.00) times(0.00) longer,(0.00) standard(0.00) incandescent(0.00) lamps.(-0.00) high(0.00) light(0.00) output(0.00) comparable(0.00) to,(0.00) many(0.00) cases(0.00) exceeding(0.00) incandescent(0.00) lamps(0.00) replaced.(0.00) excellent(0.00) color(0.00) rendering(0.00) rare(0.00) earth(0.00) tri-(0.00) phosphor(0.00) provides(0.00) high-(0.00) quality(0.00) color(0.00) believe(0.00) fluorescent.(0.00) many(0.00) lamps(0.00) use(-0.00) amalgam(-0.00) technology(-0.00) provides(-0.00) stable(0.00) lumen(0.00) performance(0.00) operated(0.00) position,(0.00) wider,(0.00) range(0.00) ambient(0.00) temperatures.(0.00) 
Node-1.3: product(-0.00) amazon(-0.00) platform(-0.00) title(0.00) content(-0.00) title(-0.00) inktoneram(0.00) remanufactured(-0.00) ink(0.00) cartridges(-0.00) replacement(0.00) epson(-0.00) 125(-0.00) 2xblack,(0.00) cyan,(0.00) magenta,(-0.00) yellow,(0.00) 5-(0.00) pack(0.00) ).(0.00) content(0.00) 1(0.00) set(0.00) 1(0.00) black(0.00) remanufactured(-0.00) 125(0.00) ink(-0.00) cartridges(-0.00) t125120(0.00) black,(0.00) t125220(0.00) cyan,(0.00) t125320(0.00) magenta,(0.00) t125420(0.00) yellow(0.00) remanufactured(0.00) 125(0.00) t1251(0.00) t1252(0.00) t1253(0.00) t1254(0.00) ink(0.00) cartridges(0.00) replace(0.01) original(0.00) 125(0.00) cartridges.(-0.01) compatible(0.01) 125(0.00) ink(0.00) cartridges(0.00) deliver(0.00) documents(0.01) high(0.00) quality(0.00) details(0.00) clarity.(-0.00) getting(0.00) 125(-0.00) remanufactured(0.00) ink(0.00) cartridges(-0.00) cost-(0.00) effective(-0.00) choice(-0.00) provide(0.00) best(-0.00) quality(0.00) reliability(0.00) great(-0.00) discounted(0.00) price.(0.00) compatible(0.00) 125(0.01) iso9001(0.00) certified(0.00) ink(0.00) cartridges(-0.00) thoroughly(0.00) tested(0.00) inspected(0.00) ensure(-0.00) oem-(0.00) equivalent(0.00) yields(-0.00) performance.(0.00) 125(0.00) t1251(0.00) t1252(0.00) t1253(0.00) t1254(0.00) compatible(0.00) ink(0.00) cartridges(-0.00) designed(0.00) work(0.00) stylus(0.00) nx125(0.00) nx127(0.00) nx130(0.00) nx230(0.00) nx420(0.00) nx530(0.00) nx625,(0.00) workforce(-0.01) 320(0.00) 323(0.00) 325(0.00) 520(-0.02) 
Node-1.4: product(0.00) amazon(0.00) platform(0.00) title(0.01) content(0.01) title(0.01) bosch(0.01) ddb180-(0.01) 02(0.00) 18-(0.00) volt(0.00) lithium-(0.00) ion(0.00) 3(0.00) 8-(0.00) inch(0.01) cordless(0.01) drill(0.00) driver(0.01) kit(0.00) 2(0.01) batteries,(0.00) charger(0.01) case.(0.01) content(0.01) none(0.00) 
Node-1.5: product(0.00) amazon(0.00) platform(-0.00) title(-0.00) content(0.00) title(0.00) flipside(0.00) science(0.00) fair(-0.00) titles(0.00) black.(0.00) content(0.00) package(0.01) contains(-0.00) 13(0.00) 1-(0.00) 3(0.00) 8(0.00) x(0.00) 8-(0.00) 1(0.00) 2(0.00) titles(0.00) school(-0.00) projects,(0.00) science(0.00) fairs,(0.00) home,(0.00) work.(-0.00) titles(0.00) printed(0.00) high(0.00) quality(0.00) coated(0.00) cardstock(0.00) perforated.(0.00) titles(0.00) include(0.00) introduction,(0.00) procedure,(0.00) hypothesis,(0.00) problem,(0.00) data,(0.00) materials,(0.00) results,(0.00) application,(0.00) conclusion,(0.00) graph,(0.00) abstract,(0.00) purpose,(0.00) variables.(0.00) available(0.00) white(0.00) backgrounds(0.00) fonts(0.00) variety(0.00) colors(-0.00) r</verbalized-graph>

### Classification Label
Cell Phones & Accessories

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 18243
- Title: Canon PG-210XL /CL-211XL Color Ink Cartridge Combo Pack-Black
- True class (canonical `y`): **Office Products**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Health & Personal Care**
- Prediction recorded by this method's pipeline: **Cell Phones & Accessories**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Canon PG-210XL /CL-211XL Color Ink Cartridge Combo Pack-Black. Content: Canon PG-210XL /CL-211XL Color Ink Cartridge Combo Pack-Black
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 2996 | Office Products | GP Spectrum Multi-Use Paper, 8.5 x 11 Inches, 3-Ream Pack (1500 Sheets) (998606) |

### 2-hop (shortest distance exactly 2): 14 nodes

| node id | true class | title |
|---|---|---|
| 301 | Office Products | Inktoneram Remanufactured Ink Cartridges High CapacityReplacement for 127 (2xBlack, Cyan, Magenta, Yellow, 5-Pack) |
| 309 | Office Products | Epson DURABrite T126120 Ultra 126 High-capacity Inkjet Cartridge-Black |
| 312 | Office Products | Inktoneram Remanufactured Ink Cartridges High Capacity Replacement for 126 (4x Black, 2x Cyan, 2x Magenta, 2x Yellow, 10-Pack) |
| 2908 | Tools & Home Improvement | GE Lighting 24705 65-Watt 470/360-Lumen R30 Commercial Indoor Reflector Floodlight Bulb, Soft White, 6-Pack |
| 2909 | Tools & Home Improvement | Philips 406009 Landscape and Indoor Flood 50-Watt MR16 12-Volt Light Bulb, 6-pack |
| 2951 | Tools & Home Improvement | (Pack of 10) 40-Watt G16.5 Decorative Globe E12 Candelabra Base Light Bulbs |
| 2957 | Tools & Home Improvement | GE Lighting 75368 Energy Smart 13-Watt Spiral Compact Fluorescent Bulb, Candelabra Base, 2-Pack |
| 3081 | Office Products | Inktoneram Remanufactured Ink Cartridges Replacement for Epson 125 (2xBlack, Cyan, Magenta, Yellow , 5-Pack) |
| 4758 | Tools & Home Improvement | Bosch DDB180-02 18-Volt Lithium-Ion 3/8-Inch Cordless Drill/Driver Kit with 2 Batteries, Charger and Case |
| 7847 | Toys & Games | Flipside Science Fair Titles: Black |
| 18244 | Industrial & Scientific | "Kimberly-Clark Kleenex 50606 Hard Roll Towel, 600' Length x 8&quot; Width, 1-3/4&quot; Core Diameter, White (Case of 6)" |
| 18245 | Office Products | School Smart Trifold Presentation Board - 36 x 48 - Header Not Included |
| 18246 | Office Products | 2 Pack Remanufactured HP 950 XL 950XL Black Ink Cartridges for HP OfficeJet Pro 276dw MFP, OfficeJet Pro 8600 e-All-In-One - N911g, OfficeJet Pro 8600 Plus - N911n, OfficeJet Pro 8600 Premium - N911a OfficeJet Pro 251dw, OfficeJet Pro 8100 ePrinter - N811a &copy; YoYoInk |
| 18247 | Office Products | Business Envelope, 4 1/8 x 9 1/2, 20 lb, White, 50/Box |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/61.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Cell Phones & Accessories**, ground truth = **Office Products**.
The verbalized graph is 9713 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 18243 | 37 | 0.0815 | yes |
| Node-1 | 1 | 2996 | 109 | 0.2056 | yes |
| Node-1.1 | 2 | 309 | 31 | 0.0258 | yes |
| Node-1.2 | 3 | 2957 | 166 | 0.0054 | yes |
| Node-1.3 | 4 | 3081 | 150 | 0.0068 | yes |
| Node-1.4 | 5 | 4758 | 36 | 0.0138 | yes |
| Node-1.5 | 6 | 7847 | 94 | 0.0061 | yes |
| Node-1.6 | 7 | 301 | 54 | 0.0143 | no |
| Node-1.7 | 8 | 18244 | 47 | 0.0045 | no |
| Node-1.8 | 9 | 18245 | 115 | 0.0039 | no |
| Node-1.9 | 10 | 18246 | 143 | 0.0127 | no |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->Node-1.6, Node-1->Node-1.7, Node-1->Node-1.8, Node-1->Node-1.9, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, Node-1.6->Node-1, Node-1.7->Node-1, Node-1.8->Node-1, Node-1.9->Node-1, ROOT->Node-1

### Tokens and scores

**ROOT** (global 18243):

~~~~~~text
product (0.0161) from (0.0231) amazon (-0.0348) platform (-0.0949) with (-0.0186) title (0.0166) and (-0.0355) content (0.0409) : (-0.0186) title (0.0815) : (-0.0239) canon (0.0328) pg- (-0.0006) 210xl (-0.0009) / (0.0435) cl- (0.0147) 211xl (0.0015) color (0.0213) ink (0.0432) cartridge (0.0533) combo (0.0358) pack- (0.0439) black. (0.0540) content (0.0002) : (-0.0360) canon (0.0129) pg- (0.0036) 210xl (0.0126) / (0.0461) cl- (0.0278) 211xl (0.0031) color (0.0043) ink (0.0222) cartridge (0.0356) combo (0.0371) pack- (0.0265) black (-0.0430)
~~~~~~

**Node-1** (global 2996):

~~~~~~text
product (-0.0071) from (0.0261) amazon (-0.0016) platform (-0.0035) with (-0.0094) title (0.0148) and (0.0177) content (0.0145) : (0.0210) title (0.0488) : (0.0272) gp (0.0461) spectrum (0.0153) multi- (0.0576) use (0.0193) paper, (0.0160) 8. (0.0269) 5 (0.0300) x (0.0148) 11 (0.0305) inches, (0.0130) 3- (0.0338) ream (0.0250) pack (0.0322) ( (0.0430) 1500 (0.0581) sheets (0.0253) ) (-0.0064) ( (0.0404) 998606 (0.0187) ). (0.0383) content (0.0118) : (-0.0300) georgia- (0.0230) pacific (0.0484) spectrum (0.0048) standard (0.0149) 92 (0.0066) multipurpose (0.0247) paper (0.0238) is (0.0222) designed (0.0319) for (0.0277) copying (0.0368) and (0.0180) printing (0.0154) in (0.0002) a (-0.0277) wide (0.0335) variety (0.0286) of (0.0253) imaging (0.0633) devices. (0.0380) this (0.0210) bright (-0.0019) white (0.0293) paper (0.0531) is (0.0231) a (-0.0545) great (0.0210) all (0.0148) around (0.0055) performer, (0.0155) ideal (-0.0369) for (0.0316) everyday (0.0312) communications (0.0410) that (0.0032) include (0.0341) black (0.0317) and (0.0288) white (0.0304) text (-0.0086) and (0.0389) graphics. (-0.0181) performs (0.0914) well (0.0260) in (0.0219) copiers, (0.0183) laser (0.0227) and (0.0261) multi- (0.0485) function (0.0255) printers, (-0.0049) as (0.0252) well (0.0139) as (0.0310) high- (0.0255) volume (0.0498) printing (0.0290) equipment. (-0.0627) for (0.0641) quality, (0.0364) consistency (0.0323) and (0.0667) reliable (-0.0217) day- (0.0263) to- (0.0474) day (-0.0027) performance, (0.0272) spectrum (0.0683) standard (0.0729) 92 (0.0644) multipurpose (0.0353) paper (0.0864) is (-0.0473) a (-0.1510) solid (0.2056) choice. (-0.0288)
~~~~~~

**Node-1.1** (global 309):

~~~~~~text
product (-0.0014) from (0.0043) amazon (0.0145) platform (0.0048) with (-0.0009) title (0.0068) and (-0.0076) content (0.0198) : (-0.0038) title (0.0075) : (0.0042) epson (-0.0010) durabrite (0.0002) t126120 (0.0006) ultra (0.0169) 126 (-0.0046) high- (0.0022) capacity (0.0015) inkjet (0.0007) cartridge- (0.0106) black. (0.0258) content (-0.0072) : (-0.0003) epson (-0.0003) durabrite (0.0013) ultra (-0.0007) ink, (0.0073) black (0.0027) ( (0.0168) t126120 (0.0057) ) (0.0098)
~~~~~~

**Node-1.2** (global 2957):

~~~~~~text
product (-0.0000) from (0.0006) amazon (0.0011) platform (0.0009) with (0.0011) title (0.0007) and (0.0016) content (0.0011) : (0.0015) title (0.0008) : (0.0013) ge (0.0027) lighting (0.0025) 75368 (0.0009) energy (0.0019) smart (-0.0006) 13- (0.0014) watt (0.0012) spiral (0.0020) compact (0.0020) fluorescent (0.0017) bulb, (0.0012) candelabra (0.0007) base, (0.0012) 2- (0.0014) pack. (0.0015) content (0.0011) : (0.0016) ge (0.0025) 75368 (0.0012) energy (0.0022) smart (-0.0002) 13 (0.0016) watt (0.0016) spiral (0.0028) cfl (0.0019) ceiling (0.0035) fan (0.0022) candelabra (0.0010) base (0.0009) 60- (0.0021) watt (0.0010) replacement. (-0.0001) ge (0.0015) compact (0.0036) fluorescent (0.0033) lamps (0.0036) ( (0.0054) cfl (-0.0006) ) (-0.0006) offer (0.0048) many (0.0010) advantages (-0.0011) that (0.0021) include (0.0019) cost (0.0020) savings, (0.0014) extra (0.0007) long (0.0015) life, (0.0010) light (0.0023) output, (0.0007) and (0.0003) color (0.0021) rendering. (0.0023) with (0.0005) this (-0.0004) cfl (0.0006) you (-0.0034) ' (-0.0003) ll (0.0017) get (0.0009) dramatic (0.0014) energy (0.0023) cost (0.0017) savings (0.0010) up (0.0022) to (0.0011) 77 (0.0014) percent (0.0010) vs. (0.0023) incandescent (0.0005) lamps (0.0037) of (0.0006) comparable (0.0012) light (0.0023) output. (-0.0018) the (-0.0058) extra (0.0009) long (0.0023) life (-0.0007) most (0.0025) last (0.0006) 8 (0.0013) to (0.0007) 10 (0.0015) times (0.0007) longer, (0.0009) and (0.0011) some (0.0017) last (0.0001) up (0.0021) to (0.0012) 20 (0.0010) times (0.0006) longer, (0.0009) than (0.0017) standard (0.0007) incandescent (0.0005) lamps. (-0.0007) high (0.0032) light (0.0027) output (0.0010) comparable (0.0019) to, (0.0012) and (0.0007) in (0.0018) many (0.0008) cases (0.0020) exceeding (0.0016) incandescent (0.0016) lamps (0.0010) replaced. (0.0012) excellent (0.0022) color (0.0019) rendering (0.0021) rare (0.0009) earth (0.0043) tri- (0.0011) phosphor (0.0007) provides (0.0006) such (0.0014) high- (0.0016) quality (0.0019) color (0.0017) you (0.0011) won (0.0002) ' (-0.0005) t (0.0025) believe (0.0007) it (0.0007) ' (0.0003) s (0.0017) fluorescent. (0.0029) many (0.0002) lamps (0.0018) use (-0.0005) amalgam (-0.0003) technology (-0.0002) which (0.0014) provides (-0.0004) stable (0.0002) lumen (0.0015) performance (0.0004) when (0.0009) operated (0.0012) in (0.0007) any (0.0011) position, (0.0011) over (0.0015) a (-0.0037) wider, (0.0007) range (0.0018) of (0.0014) ambient (0.0016) temperatures. (0.0021)
~~~~~~

**Node-1.3** (global 3081):

~~~~~~text
product (-0.0024) from (-0.0036) amazon (-0.0009) platform (-0.0012) with (-0.0016) title (0.0008) and (0.0005) content (-0.0010) : (0.0009) title (-0.0015) : (0.0003) inktoneram (0.0017) remanufactured (-0.0027) ink (0.0002) cartridges (-0.0050) replacement (0.0006) for (0.0025) epson (-0.0004) 125 (-0.0028) ( (-0.0000) 2xblack, (0.0004) cyan, (0.0010) magenta, (-0.0005) yellow, (0.0004) 5- (0.0011) pack (0.0008) ). (0.0040) content (0.0003) : (-0.0033) ( (0.0022) 1 (0.0001) set (0.0020) + (0.0009) 1 (0.0014) black (0.0004) remanufactured (-0.0009) 125 (0.0022) ink (-0.0024) cartridges (-0.0019) t125120 (0.0015) black, (0.0018) t125220 (0.0015) cyan, (0.0009) t125320 (0.0036) magenta, (0.0012) t125420 (0.0028) yellow (0.0022) ) (-0.0033) the (0.0010) remanufactured (0.0004) 125 (0.0002) t1251 (0.0039) t1252 (0.0031) t1253 (0.0038) t1254 (0.0047) ink (0.0023) cartridges (0.0000) replace (0.0068) the (0.0023) original (0.0020) 125 (0.0044) cartridges. (-0.0073) our (-0.0015) compatible (0.0068) 125 (0.0047) ink (0.0044) cartridges (0.0013) deliver (0.0021) documents (0.0058) with (0.0000) high (0.0034) quality (0.0031) details (0.0034) and (0.0013) clarity. (-0.0033) getting (0.0016) the (0.0042) 125 (-0.0003) remanufactured (0.0004) ink (0.0017) cartridges (-0.0048) is (0.0015) a (0.0027) cost- (0.0021) effective (-0.0000) choice (-0.0000) that (0.0001) will (-0.0000) provide (0.0005) you (-0.0065) with (0.0021) best (-0.0004) quality (0.0008) and (0.0008) reliability (0.0025) at (0.0022) great (-0.0003) discounted (0.0017) price. (0.0031) our (0.0050) compatible (0.0034) 125 (0.0064) ( (0.0022) iso9001 (0.0008) certified (0.0018) ) (0.0017) ink (0.0016) cartridges (-0.0016) are (0.0058) thoroughly (0.0000) tested (0.0024) and (0.0002) inspected (0.0003) to (0.0027) ensure (-0.0000) oem- (0.0001) equivalent (0.0032) yields (-0.0002) and (0.0005) performance. (0.0048) the (0.0044) 125 (0.0035) t1251 (0.0025) t1252 (0.0019) t1253 (0.0011) t1254 (0.0008) compatible (0.0045) ink (0.0024) cartridges (-0.0014) are (0.0033) designed (0.0040) to (0.0010) work (0.0017) with (-0.0026) : (0.0025) stylus (0.0020) : (-0.0020) nx125 (0.0002) nx127 (0.0007) nx130 (0.0010) nx230 (0.0007) nx420 (0.0010) nx530 (0.0014) nx625, (0.0026) workforce (-0.0122) : (0.0042) 320 (0.0030) 323 (0.0004) 325 (0.0020) 520 (-0.0206)
~~~~~~

**Node-1.4** (global 4758):

~~~~~~text
product (0.0040) from (0.0015) amazon (0.0045) platform (0.0042) with (-0.0025) title (0.0138) and (-0.0007) content (0.0085) : (-0.0049) title (0.0074) : (0.0063) bosch (0.0080) ddb180- (0.0068) 02 (0.0040) 18- (0.0043) volt (0.0034) lithium- (0.0039) ion (0.0036) 3 (0.0036) / (0.0055) 8- (0.0046) inch (0.0076) cordless (0.0054) drill (0.0013) / (0.0081) driver (0.0077) kit (0.0038) with (0.0024) 2 (0.0067) batteries, (0.0037) charger (0.0053) and (0.0043) case. (0.0099) content (0.0080) : (0.0113) none (0.0025)
~~~~~~

**Node-1.5** (global 7847):

~~~~~~text
product (0.0000) from (-0.0025) amazon (0.0014) platform (-0.0005) with (-0.0019) title (-0.0004) and (-0.0004) content (0.0016) : (-0.0003) title (0.0001) : (0.0013) flipside (0.0026) science (0.0010) fair (-0.0000) titles (0.0005) : (-0.0027) black. (0.0010) content (0.0017) : (-0.0005) this (0.0037) package (0.0061) contains (-0.0007) ( (-0.0002) 13 (0.0012) ) (-0.0019) 1- (0.0003) 3 (0.0011) / (-0.0004) 8 (0.0010) " (0.0007) x (0.0006) 8- (0.0009) 1 (0.0013) / (0.0003) 2 (0.0015) " (-0.0006) titles (0.0014) for (0.0004) school (-0.0021) projects, (0.0015) science (0.0006) fairs, (0.0006) home, (0.0013) and (0.0016) at (0.0016) work. (-0.0017) titles (0.0011) are (0.0008) printed (0.0014) on (-0.0001) high (0.0021) quality (0.0018) coated (0.0005) cardstock (0.0012) and (0.0015) perforated. (0.0006) titles (0.0015) include (0.0001) : (0.0019) introduction, (0.0015) procedure, (0.0015) hypothesis, (0.0019) problem, (0.0012) data, (0.0012) materials, (0.0016) results, (0.0014) application, (0.0008) conclusion, (0.0019) graph, (0.0013) abstract, (0.0018) purpose, (0.0007) and (0.0044) variables. (0.0004) available (0.0017) with (0.0012) white (0.0035) backgrounds (0.0009) with (-0.0002) fonts (0.0023) in (0.0005) a (-0.0073) variety (0.0021) of (0.0011) colors (-0.0014) ( (0.0021) red, (0.0014) green, (0.0020) blue, (0.0016) and (0.0039) black (0.0022) ), (0.0016) each (0.0009) sold (0.0029) separately. (0.0030)
~~~~~~

**Node-1.6** (global 301):

~~~~~~text
product (0.0085) from (-0.0023) amazon (-0.0019) platform (-0.0035) with (-0.0039) title (0.0047) and (-0.0062) content (0.0026) : (-0.0014) title (0.0056) : (0.0005) inktoneram (0.0057) remanufactured (-0.0006) ink (0.0040) cartridges (-0.0088) high (0.0074) capacityreplacement (0.0008) for (0.0047) 127 (-0.0055) ( (0.0011) 2xblack, (0.0032) cyan, (0.0040) magenta, (0.0025) yellow, (0.0029) 5- (0.0051) pack (0.0043) ). (0.0143) content (-0.0032) : (-0.0020) 1 (0.0039) pack, (0.0034) 1 (0.0023) black (0.0031) of (-0.0001) total (0.0046) 5 (0.0022) remanufactured (0.0027) 127 (0.0011) ( (0.0040) extra (0.0042) high (0.0056) capacity (0.0084) ) (0.0001) ink (0.0013) cartridges (0.0042) 127 (0.0002) t127120 (0.0049) t127220 (0.0062) t127320 (0.0062) t127420 (0.0064) black (0.0023) cyan (0.0071) magenta (0.0088) yellow (0.0054)
~~~~~~

**Node-1.7** (global 18244):

~~~~~~text
product (0.0017) from (0.0012) amazon (-0.0026) platform (0.0033) with (0.0023) title (0.0035) and (0.0017) content (0.0032) : (-0.0009) title (0.0029) : (0.0005) " (-0.0010) kimberly- (0.0032) clark (-0.0023) kleenex (0.0007) 50606 (0.0012) hard (-0.0024) roll (0.0016) towel, (0.0014) 600 (0.0009) ' (0.0020) length (0.0018) x (-0.0006) 8 (0.0006) & (0.0004) quot (0.0003) ; (0.0021) width, (0.0013) 1- (0.0012) 3 (0.0011) / (0.0017) 4 (0.0020) & (0.0008) quot (0.0011) ; (0.0017) core (0.0020) diameter, (0.0008) white (0.0029) ( (0.0022) case (0.0034) of (0.0005) 6 (0.0026) ) (-0.0008) ". (0.0011) content (0.0010) : (0.0005) none (0.0045)
~~~~~~

**Node-1.8** (global 18245):

~~~~~~text
product (-0.0001) from (-0.0011) amazon (0.0017) platform (0.0009) with (-0.0006) title (0.0013) and (0.0004) content (-0.0006) : (0.0030) title (0.0004) : (0.0015) school (-0.0025) smart (-0.0004) trifold (0.0005) presentation (0.0012) board- (-0.0002) 36 (0.0004) x (-0.0002) 48- (0.0005) header (0.0004) not (-0.0001) included. (0.0011) content (0.0006) : (-0.0001) trifold, (0.0005) corrugated (0.0010) presentation (0.0011) boards (0.0009) are (0.0001) ideal (0.0006) for (0.0009) projects, (0.0002) booths, (0.0006) fairs, (0.0016) and (0.0008) all (0.0003) types (0.0002) of (0.0012) displays. (-0.0038) these (0.0039) boards (0.0007) are (0.0003) white (-0.0007) on (0.0003) the (-0.0021) front (-0.0009) with (0.0001) a (-0.0010) natural (0.0003) kraft (-0.0005) backing. (-0.0005) board (-0.0021) dimensions (-0.0010) are (-0.0000) 36 (-0.0003) x (0.0007) 48 (-0.0000) open, (0.0003) and (0.0004) 36 (-0.0004) x (0.0006) 24 (0.0004) inches (-0.0002) folded. (-0.0009) recyclable. (0.0005) image (-0.0004) shows (0.0022) board (-0.0005) with (0.0017) header (-0.0011) card. (-0.0009) this (0.0007) item (0.0001) is (0.0004) the (-0.0011) board (-0.0003) only. (-0.0009) sold (-0.0002) as (0.0001) single (0.0001) unit. (0.0024) great (-0.0009) for (-0.0015) science (0.0012) fairs, (0.0011) art (-0.0008) shows, (-0.0003) school (0.0001) and (0.0007) office (0.0006) presentations (0.0004) and (-0.0002) more. (-0.0012) trifold (0.0005) presentation (0.0006) board (0.0006) with (-0.0004) smooth (-0.0009) surface. (-0.0028) surface (0.0001) accepts (0.0026) all (-0.0010) types (-0.0004) of (0.0005) adhesives (-0.0005) markers, (-0.0014) paints,. (0.0022) rigid, (-0.0016) lightweight (-0.0014) and (0.0000) easy (-0.0002) to (0.0007) fold (0.0000) and (0.0006) carry. (0.0011)
~~~~~~

**Node-1.9** (global 18246):

~~~~~~text
product (-0.0019) from (-0.0010) amazon (0.0028) platform (-0.0027) with (-0.0010) title (0.0003) and (-0.0003) content (0.0028) : (0.0004) title (0.0024) : (0.0005) 2 (0.0026) pack (0.0006) remanufactured (0.0004) hp (-0.0008) 950 (0.0038) xl (-0.0012) 950xl (0.0011) black (0.0003) ink (0.0015) cartridges (-0.0024) for (0.0013) hp (-0.0012) officejet (0.0005) pro (0.0002) 276dw (0.0008) mfp, (0.0003) officejet (-0.0006) pro (-0.0004) 8600 (-0.0018) e- (0.0011) all- (0.0006) in- (-0.0015) one- (0.0014) n911g, (0.0009) officejet (-0.0001) pro (0.0007) 8600 (-0.0007) plus- (0.0006) n911n, (0.0008) officejet (-0.0003) pro (0.0013) 8600 (0.0007) premium- (0.0009) n911a (0.0011) officejet (0.0002) pro (-0.0001) 251dw, (0.0012) officejet (0.0009) pro (0.0006) 8100 (0.0011) eprinter- (0.0009) n811a (0.0010) & (-0.0017) copy (0.0002) ; (0.0060) yoyoink. (0.0004) content (0.0062) : (0.0048) yoyoink (0.0024) compatible (-0.0032) replacement (0.0018) for (0.0021) hp (0.0007) 950xldetails (0.0010) :- (0.0069) compatible (-0.0043) with (0.0029) the (-0.0095) following (0.0051) printers (-0.0037) : (0.0034) hp (-0.0004) all- (0.0021) in- (-0.0005) one (0.0019) printers (-0.0003) officejet (0.0004) pro (0.0019) 276dw (-0.0007) mfp, (0.0005) officejet (-0.0003) pro (0.0015) 8600 (-0.0008) e- (0.0004) all- (0.0001) in- (0.0003) one- (-0.0002) n911g, (0.0010) officejet (-0.0004) pro (0.0011) 8600 (-0.0005) plus- (0.0006) n911n, (0.0008) officejet (0.0004) pro (0.0015) 8600 (0.0007) premium- (0.0010) n911a (0.0018) hp (-0.0027) inkjet (0.0013) printers (-0.0005) officejet (0.0004) pro (0.0008) 251dw, (0.0008) officejet (0.0004) pro (0.0010) 8100 (0.0007) eprinter- (0.0010) n811a- (0.0006) listing (-0.0003) includes (0.0127) : (0.0003) 2 (-0.0021) of (-0.0021) hp (-0.0005) 950xlbk- (0.0005) one (0.0018) year (0.0012) warranty- (0.0015) free (0.0026) shipping (0.0011) for (-0.0030) orders (0.0028) fulfilled (0.0000) by (-0.0012) amazon (-0.0055) if (0.0003) you (0.0023) have (0.0005) prime- (0.0004) free (0.0014) shipping (0.0023) for (-0.0007) orders (0.0016) fulfilled (-0.0012) by (-0.0064) merchant- (0.0051) hassel- (0.0023) free (0.0016) returns (-0.0010) & (-0.0017) refunds (0.0013)
~~~~~~
