# Reference packet: GraphNarrator__Llama-8B__products__15065

- Method: GraphNarrator; configuration: Llama-8B; dataset: products; target node: 15065
- Explanation source: `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/50.json` (messages[assistant])
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

- ROOT (camera equipment)
  - Node-1 (camera accessories)
    - Node-1.1 (chest mount)
    - Node-1.2 (handlebar mount)
    - Node-1.3 (diving camera)
    - Node-1.4 (tripod mount)

### Word-Level Evaluation

Keywords with high saliency scores in ROOT — "camera" (-0.01), "extender" (0.02), "handheld" (0.03), "monopod" (0.04), "tripod" (0.01), "adapter" (0.03) — are strongly associated with camera equipment. These directly indicate the product belongs to "Cell Phones & Accessories" (camera accessories). More generic terms like "product" (-0.02) and "amazon" (0.04) carry negligible saliency and contribute little.

### Graph-Level Aggregation

Node-1 (camera accessories, keywords: "adjustable" (0.06), "mount" (0.02), "harness" (0.02), "gopro" (0.05)) and its children are direct neighbors with moderate to high saliency, identifying camera accessories whose close proximity to ROOT reinforces the classification. Indirect neighbors — Node-1.1 (chest mount), Node-1.2 (handlebar mount), Node-1.3 (diving camera), Node-1.4 (tripod mount) — are all camera-related accessories, collectively confirming a camera context across both hops.

### Free-Text Explanation

The classification of ROOT into "Cell Phones & Accessories" is supported by its own keywords and the co-purchase neighborhood.

ROOT: Keywords like "camera" (-0.01), "extender" (0.02), and "handheld" (0.03) clearly identify this as camera equipment — quintessentially a cell phone accessory.
  - Node-1: Camera accessories (keywords: "adjustable" (0.06), "mount" (0.02), "harness" (0.02), "gopro" (0.05)) are direct camera-related components, reinforcing the Cell Phones & Accessories context.
    - Node-1.1: A chest mount is a camera accessory, supporting the camera category.
    - Node-1.2: A handlebar mount is another camera accessory, further confirming the camera product ecosystem.
    - Node-1.3: A diving camera is a specialized camera type, also fitting the camera category.
    - Node-1.4: A tripod mount is a camera accessory, providing additional evidence for the Cell Phones & Accessories classification.

In summary, ROOT's own high-saliency keywords strongly signal camera equipment, and the entire co-purchase neighborhood consists of camera accessories, providing robust evidence for the "Cell Phones & Accessories" category.
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/50.json`).

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
<verbalized-graph>ROOT: product(-0.02) amazon(0.04) platform(-0.02) title(0.03) content(0.04) title(0.00) camera(-0.01) extender(0.02) handheld(0.03) telescopic(0.00) monopod(0.04) tripod(0.01) mount(-0.01) adapter(0.03) gopro(0.01) hero(0.00) 1(0.01) 2(0.02) 3(0.01) camera(-0.02) monopod.(0.00) content(0.02) monopod(0.01) universal(0.02) camera(0.02) holder,(-0.00) easy(0.02) carry,(-0.00) fits(0.04) compact(0.03) cameras.(-0.00) it,(0.00) photograph(-0.00) video(0.01) anywhere!(0.03) product(0.06) feature(0.02) :-(0.03) durable(0.03) metal(0.03) shaft,(0.01) lightweight,(0.01) usable(0.02) easy(0.03) carry(0.01) with-(-0.00) fit(0.02) compact(0.03) cameras,(0.00) connecting(0.03) tripod(0.01) mount(0.02) cameras-(0.02) considerate(0.02) design(0.02) quick(0.04) spin(0.03) knob(0.03) fast(0.03) convenient(0.06) mounting-(0.02) non-(0.03) slip(0.02) handle(0.03) better(0.03) using(0.02) experience(0.01) wonderful(0.10) touch(0.01) feeling-(0.03) 180-(0.02) degree(0.02) rotation,(0.01) providing(-0.01) convenience(-0.00) users(0.02) taking(0.01) photos-(0.01) adjustable(0.07) design(-0.01) makes(0.01) portable(0.00) also(0.01) eliminates(0.02) awkward(0.00) photos(0.01) taken(-0.00) arms(0.02) length(0.01) package(0.02) content(0.03) :-(0.00) 1(0.02) x(0.02) monopod-(0.01) 1(0.01) x(0.03) tripod(0.02) adapter(0.00) 
Node-1: product(-0.04) amazon(-0.05) platform(-0.04) title(0.00) content(0.01) title(0.01) adjustable(0.06) chest(0.05) mount(0.02) harness(0.02) gopro(0.05) hd(-0.04) hero(-0.04) 2(-0.00) hero(-0.07) 3(0.02) camera-(0.01) black.(-0.02) content(0.05) chest(-0.01) harness(-0.03) quick-(0.01) release(0.01) hero(-0.01) camera.(-0.01) makes(0.04) easy(-0.00) capture(-0.01) immersive(0.03) video(0.03) photo(0.05) footage(0.00) from,(0.00) well(0.03) chest.(-0.04) perfect(0.01) skiing,(-0.03) mountain(0.00) biking,(-0.02) motocross,(0.01) paddle(0.01) sports,(-0.00) activity(0.04) want(0.03) get(0.01) lower(0.05) helmet(0.02) view(0.03) action.(-0.00) see(0.03) arms,(0.02) knees(0.03) poles,(0.03) skis(0.04) skiing(-0.03) arms(0.02) handlebars(0.03) biking(-0.02) riding(0.00) motorcycle.(0.07) recommended(0.03) immersive(0.03) way(0.01) film(0.03) helmet.(0.01) lets(0.11) wear(-0.00) gopro(0.00) cameras(0.03) except(0.02) digital(0.06) hero(-0.03) 5(-0.00) wrist(-0.02) camera(0.00) chestcomfortable,(0.02) fully-(0.02) adjustable(0.08) design(0.04) fits(-0.01) shapes(0.02) sizes,(0.02) including(0.02) large(0.06) jacketsperfect(0.03) mount(0.02) skiing,(0.02) kayaking,(0.03) biking,(0.00) motocross,(0.03) equestrian(0.04) action(0.03) sportslets(0.03) capture(0.04) knees(0.01) skis(0.04) slopes,(0.04) bike(0.02) frame(0.02) handlebarseasy(0.01) way(0.02) share(0.01) filming(0.03) friends(-0.00) 
Node-1.1: product(-0.00) amazon(-0.00) platform(-0.00) title(-0.00) content(0.01) title(0.01) hitcase(-0.00) chestr(-0.00) mount.(-0.01) content(-0.00) features(0.00) hitcase(-0.00) chestr(-0.00) mount(0.00) great(0.00) helmet(-0.00) mount(-0.00) high,(-0.00) handlebar(0.00) board(0.00) mount(0.00) low(0.00) lightweight(0.00) neoprene(0.00) chest(0.00) harness(0.00) comfortable(0.00) fit(0.00) easily(0.00) adjustable,(-0.00) letting(-0.00) avoid(0.00) getting(-0.00) tangled(0.00) railslide(0.00) quick(-0.00) mount(0.00) system(0.00) lets(0.00) easily(0.00) put(0.00) hitcase(-0.00) out,(0.00) even(0.00) rotate(0.00) smartphone(0.00) 360(-0.00) deg(0.00) pivot(0.00) 180(0.00) deg(-0.00) railslide(0.01) quick(-0.00) mount(0.00) let(0.00) get(0.00) possible(0.00) angles,(0.00) making(0.00) shots(0.01) want(0.00) super(0.01) easy(0.00) capture(0.00) built(0.01) stow(0.00) pocket(0.01) able(0.01) attach(0.00) mount(0.00) back,(-0.00) versatile(0.01) enough(0.00) use(0.00) ways(0.00) specifications(0.00) hitcase(-0.00) chestr(-0.00) mount(-0.00) made(0.00) super(-0.00) durable(-0.00) waterproof(0.00) neoprene(0.00) included(0.00) hitcase(0.00) chestr(-0.00) mount(0.00) chestr(-0.00) mount(-0.00) railslide(0.00) carry(-0.00) bag(0.00) made(0.00) neoprene(0.00) 
Node-1.2: product(-0.00) amazon(0.01) platform(-0.00) title(0.00) content(-0.00) title(0.00) jmt(0.00) sports(0.00) camera(-0.00) handlebar(0.00) seatpost(0.00) rack(0.00) mount(0.00) compatible(-0.00) gopro(0.01) hd(-0.00) hero(0.00) 2(0.00) 3.(0.00) content(0.00) features(0.00) brand(-0.00) new(0.00) high(0.00) quality.(0.00) easy(0.00) install(-0.00) remove.(-0.00) light(0.00) weighted(0.01) portable.(0.00) material(0.00) plastic,(0.00) metal.(0.00) color(0.00) black.(0.01) compatible(-0.01) gopro(0.00) hero(0.00) 3(0.00) 2(0.00) 1.(0.00) suitable(-0.00) tubes(0.00) diameter(0.00) 1.(0.00) 9cm-(0.00) 3.(0.00) 5cm.(0.00) size(0.00) 8cm(0.00) x(0.00) 8cm(0.00) x(0.00) 2cm.(0.00) package(0.00) included(0.00) 1(0.00) x(0.00) handlebar(0.00) seatpost(0.00) mount(0.00) without(0.00) 3-(0.00) way(0.00) pivot(0.00) arm(0.00) retail(0.00) box.(0.01) packed(0.00) safely(0.00) bubble(0.01) bag.(0.01) 
Node-1.3: product(0.01) amazon(0.01) platform(0.00) title(0.01) content(0.00) title(0.01) pov(0.01) dive(0.01) buoy(0.01) floating(0.01) camera(0.01) handle-(0.01) gopro(0.01) edition.(-0.02) content(-0.00) floats(0.01) camera(0.00) bacpac(0.01) screwable(0.00) water-(0.01) tight(0.01) endcap(0.01) direct(0.01) 180(0.01) swivel(0.01) head(0.00) gopro(0.01) camera(0.01) attachment(0.01) super-(0.01) comfortable(-0.00) eva(0.02) grip(-0.00) pocket(0.00) sized(0.01) lightweight(-0.01) 
Node-1.4: product(-0.00) amazon(0.00) platform(-0.01) title(-0.00) content(-0.00) title(-0.00) victsing(0.00) suction(-0.00) cup(0.00) mount(0.00) gopro(0.00) hd(-0.00) hero(-0.00) hero2(0.00) hero3(0.00) camera(-0.00) tripod(-0.00) mount(-0.00) handle(-0.00) screw(0.00) ).(-0.00) content(0.01) features(-0.00) compatible(-0.01) hd(-0.00) hero,(0.00) hd(-0.00) hero2(0.00) hd(-0.00) hero3(-0.00) professional(-0.00) cameras(0.00) cameras(0.00) fit(-0.00) universal(0.00) 1(0.00) 4?(0.01) screwsecurely(0.00) attaches(0.00) camera(0.00) housing(0.00) vehicle(0.00) body,(0.00) window,(0.00) fuel(0.00</verbalized-graph>

### Classification Label
Cell Phones & Accessories

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 15065
- Title: Camera Extender Handheld Telescopic Monopod +Tripod Mount Adapter for Gopro Hero 1/ 2/ 3 Camera Monopod
- True class (canonical `y`): **Electronics**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Sports & Outdoors**
- Prediction recorded by this method's pipeline: **Cell Phones & Accessories**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Camera Extender Handheld Telescopic Monopod +Tripod Mount Adapter for Gopro Hero 1/ 2/ 3 Camera Monopod. Content: This monopod is a universal camera holder, easy to carry, and fits all compact cameras. With it, you can photograph and video by yourself anywhere! Product Feature: -Durable metal shaft, lightweight, usable and easy to carry with -Fit most of compact cameras, connecting to the tripod mount of cameras -Considerate design of the quick spin knob for fast and convenient mounting -Non-slip handle for better using experience and wonderful touch feeling -180-degree rotation, providing convenience for the users while they are taking photos -Adjustable design not only makes it portable but also eliminates awkward photos taken at arms length Package Content: -1 x Monopod -1 x Tripod adapter
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 2082 | Sports & Outdoors | Adjustable Chest Mount Harness for Gopro Hd Hero 2 Hero 3 Camera - Black |

### 2-hop (shortest distance exactly 2): 6 nodes

| node id | true class | title |
|---|---|---|
| 178 | Cell Phones & Accessories | Hitcase ChestR Mount |
| 2069 | Sports & Outdoors | Jmt Sports Camera Handlebar Seatpost Rack Mount Compatible Gopro Hd Hero 2 3 |
| 2109 | Electronics | POV Dive Buoy Floating Camera Handle - GoPro Edition |
| 14980 | Cell Phones & Accessories | VicTsing Suction Cup Mount for GoPro HD HERO HERO2 HERO3 Camera (Tripod Mount and Handle Screw) |
| 15063 | Electronics | WoCase&reg; Adjustable (Anti-Slippery) Head Strap Mount and Quick Clip Mount for GoPro HERO3+ 3 2 1 Cameras |
| 15064 | Electronics | WoCase&reg; Wrist Strap Mount for GoPro HD HERO3+ 3 2 1 Cameras (Compatible with Housing and Frame) |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/50.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Cell Phones & Accessories**, ground truth = **Electronics**.
The verbalized graph is 8746 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 15065 | 144 | 0.0979 | yes |
| Node-1 | 1 | 2082 | 172 | 0.1054 | yes |
| Node-1.1 | 2 | 178 | 150 | 0.0116 | yes |
| Node-1.2 | 3 | 2069 | 97 | 0.0083 | yes |
| Node-1.3 | 4 | 2109 | 44 | 0.0182 | yes |
| Node-1.4 | 5 | 14980 | 126 | 0.0198 | yes |
| Node-1.5 | 6 | 15063 | 143 | 0.0079 | no |
| Node-1.6 | 7 | 15064 | 126 | 0.0060 | no |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->Node-1.6, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, Node-1.6->Node-1, ROOT->Node-1

### Tokens and scores

**ROOT** (global 15065):

~~~~~~text
product (-0.0164) from (-0.0336) amazon (0.0402) platform (-0.0203) with (-0.0263) title (0.0254) and (-0.0124) content (0.0382) : (-0.0066) title (0.0040) : (0.0098) camera (-0.0051) extender (0.0170) handheld (0.0257) telescopic (0.0039) monopod (0.0351) + (-0.0073) tripod (0.0119) mount (-0.0107) adapter (0.0308) for (-0.0007) gopro (0.0115) hero (0.0031) 1 (0.0119) / (-0.0116) 2 (0.0205) / (0.0057) 3 (0.0142) camera (-0.0170) monopod. (0.0008) content (0.0207) : (-0.0000) this (0.0054) monopod (0.0140) is (0.0122) a (-0.0106) universal (0.0212) camera (0.0167) holder, (-0.0014) easy (0.0163) to (0.0040) carry, (-0.0035) and (-0.0071) fits (0.0360) all (0.0078) compact (0.0299) cameras. (-0.0022) with (0.0021) it, (0.0040) you (0.0011) can (0.0147) photograph (-0.0020) and (0.0092) video (0.0093) by (0.0175) yourself (0.0152) anywhere! (0.0282) product (0.0557) feature (0.0232) :- (0.0277) durable (0.0280) metal (0.0271) shaft, (0.0059) lightweight, (0.0124) usable (0.0192) and (0.0123) easy (0.0274) to (0.0139) carry (0.0127) with- (-0.0025) fit (0.0189) most (0.0229) of (0.0063) compact (0.0286) cameras, (0.0005) connecting (0.0344) to (0.0054) the (-0.0036) tripod (0.0137) mount (0.0181) of (0.0098) cameras- (0.0176) considerate (0.0240) design (0.0165) of (0.0051) the (0.0164) quick (0.0443) spin (0.0319) knob (0.0328) for (0.0119) fast (0.0271) and (0.0119) convenient (0.0565) mounting- (0.0249) non- (0.0277) slip (0.0166) handle (0.0328) for (0.0262) better (0.0304) using (0.0203) experience (0.0143) and (0.0069) wonderful (0.0979) touch (0.0118) feeling- (0.0299) 180- (0.0210) degree (0.0191) rotation, (0.0100) providing (-0.0148) convenience (-0.0011) for (0.0057) the (-0.0181) users (0.0169) while (0.0014) they (0.0101) are (0.0167) taking (0.0057) photos- (0.0124) adjustable (0.0718) design (-0.0051) not (-0.0047) only (0.0134) makes (0.0109) it (0.0235) portable (0.0028) but (0.0170) also (0.0124) eliminates (0.0158) awkward (0.0021) photos (0.0058) taken (-0.0010) at (0.0108) arms (0.0175) length (0.0075) package (0.0216) content (0.0252) :- (0.0029) 1 (0.0160) x (0.0151) monopod- (0.0102) 1 (0.0097) x (0.0317) tripod (0.0163) adapter (0.0011)
~~~~~~

**Node-1** (global 2082):

~~~~~~text
product (-0.0358) from (-0.0563) amazon (-0.0485) platform (-0.0439) with (-0.0121) title (0.0012) and (-0.0023) content (0.0086) : (0.0077) title (0.0056) : (-0.0189) adjustable (0.0583) chest (0.0521) mount (0.0188) harness (0.0156) for (-0.1390) gopro (0.0453) hd (-0.0395) hero (-0.0394) 2 (-0.0013) hero (-0.0711) 3 (0.0188) camera- (0.0097) black. (-0.0174) content (0.0499) : (0.0358) chest (-0.0107) harness (-0.0325) for (-0.0199) your (-0.0022) quick- (0.0060) release (0.0109) hero (-0.0121) camera. (-0.0110) makes (0.0381) it (0.0166) easy (-0.0041) to (0.0146) capture (-0.0076) immersive (0.0252) video (0.0300) and (0.0150) photo (0.0467) footage (0.0032) from, (0.0027) well (0.0255) your (-0.0192) chest. (-0.0380) perfect (0.0065) for (-0.0219) skiing, (-0.0270) mountain (0.0033) biking, (-0.0189) motocross, (0.0054) paddle (0.0140) sports, (-0.0007) or (-0.0078) any (0.0376) activity (0.0374) where (0.0146) you (-0.0035) want (0.0262) to (0.0208) get (0.0134) a (0.0286) " (0.0002) lower (0.0477) than (-0.0107) the (-0.0514) helmet (0.0190) " (-0.0429) view (0.0257) of (0.0205) the (0.0045) action. (-0.0034) see (0.0290) more (0.0615) of (0.0203) your (0.0091) arms, (0.0232) knees (0.0255) poles, (0.0298) and (0.0409) skis (0.0379) while (0.0180) skiing (-0.0295) or (0.0422) your (0.0296) arms (0.0168) and (0.0410) handlebars (0.0274) while (0.0490) biking (-0.0248) or (0.0580) riding (0.0035) your (0.0387) motorcycle. (0.0708) recommended (0.0256) as (0.0427) a (0.0474) more (0.0355) immersive (0.0348) way (0.0062) to (0.0259) film (0.0308) than (0.0132) on (-0.0191) the (0.0055) helmet. (0.0141) lets (0.1054) you (-0.0531) wear (-0.0018) all (0.0034) gopro (0.0035) cameras (0.0259) ( (0.0284) except (0.0234) digital (0.0611) hero (-0.0306) 5 (-0.0004) wrist (-0.0230) camera (0.0011) ) (0.0264) on (0.0138) your (-0.0038) chestcomfortable, (0.0158) fully- (0.0162) adjustable (0.0783) design (0.0381) fits (-0.0104) all (-0.0256) shapes (0.0208) and (0.0043) sizes, (0.0174) including (0.0230) over (-0.0037) large (0.0564) jacketsperfect (0.0298) mount (0.0231) for (-0.0062) skiing, (0.0152) kayaking, (0.0264) biking, (0.0041) motocross, (0.0301) equestrian (0.0393) and (0.0317) other (0.0235) action (0.0292) sportslets (0.0257) you (-0.0037) capture (0.0417) your (0.0023) knees (0.0146) & (0.0165) skis (0.0367) on (0.0006) the (0.0185) slopes, (0.0384) or (0.0160) your (-0.0136) bike (0.0210) frame (0.0157) & (0.0144) handlebarseasy (0.0122) way (0.0172) to (0.0155) share (0.0112) the (-0.0134) filming (0.0337) with (0.0146) your (-0.0191) friends (-0.0016)
~~~~~~

**Node-1.1** (global 178):

~~~~~~text
product (-0.0002) from (0.0013) amazon (-0.0017) platform (-0.0007) with (0.0032) title (-0.0021) and (0.0025) content (0.0081) : (-0.0038) title (0.0058) : (0.0116) hitcase (-0.0011) chestr (-0.0023) mount. (-0.0132) content (-0.0028) : (-0.0011) features (0.0030) of (0.0012) the (-0.0032) hitcase (-0.0022) chestr (-0.0003) mount (0.0005) great (0.0017) for (0.0011) when (0.0012) a (0.0021) helmet (-0.0004) mount (-0.0002) is (0.0023) too (0.0019) high, (-0.0003) and (0.0019) a (0.0007) handlebar (0.0015) or (0.0021) board (0.0032) mount (0.0020) is (0.0002) too (0.0027) low (0.0043) lightweight (0.0012) neoprene (0.0012) chest (0.0001) harness (0.0006) with (0.0013) a (-0.0006) comfortable (0.0008) fit (0.0004) easily (0.0012) adjustable, (-0.0017) letting (-0.0021) you (-0.0011) avoid (0.0002) getting (-0.0009) tangled (0.0019) railslide (0.0031) quick (-0.0006) mount (0.0018) system (0.0021) lets (0.0012) you (-0.0007) easily (0.0022) put (0.0008) your (0.0014) hitcase (-0.0001) in (-0.0006) or (0.0024) out, (0.0005) even (0.0016) rotate (0.0017) your (-0.0013) smartphone (0.0023) 360 (-0.0008) & (0.0005) deg (0.0001) ; (-0.0003) and (0.0034) pivot (0.0017) it (0.0013) 180 (0.0018) & (0.0038) deg (-0.0002) ; (-0.0002) the (-0.0006) railslide (0.0062) quick (-0.0007) mount (0.0005) let (0.0013) you (-0.0009) get (0.0027) all (0.0010) possible (0.0010) angles, (0.0041) making (0.0020) the (0.0014) shots (0.0055) you (0.0006) want (0.0017) super (0.0059) easy (0.0047) to (0.0049) capture (0.0025) built (0.0057) with (0.0068) a (0.0015) stow (0.0026) pocket (0.0067) able (0.0052) to (0.0055) attach (0.0037) mount (0.0010) to (0.0015) back, (-0.0011) and (0.0011) versatile (0.0056) enough (0.0024) to (-0.0001) use (0.0020) other (0.0001) ways (0.0011) too (0.0017) specifications (0.0033) of (0.0000) the (-0.0026) hitcase (-0.0005) chestr (-0.0017) mount (-0.0008) made (0.0002) with (0.0025) super (-0.0009) durable (-0.0016) and (0.0012) waterproof (0.0000) neoprene (0.0019) included (0.0018) with (0.0018) the (-0.0006) hitcase (0.0003) chestr (-0.0008) mount (0.0000) chestr (-0.0012) mount (-0.0002) with (0.0016) railslide (0.0025) carry (-0.0009) bag (0.0007) made (0.0025) out (-0.0006) of (-0.0005) neoprene (0.0014)
~~~~~~

**Node-1.2** (global 2069):

~~~~~~text
product (-0.0015) from (-0.0050) amazon (0.0083) platform (-0.0037) with (-0.0045) title (0.0019) and (-0.0023) content (-0.0006) : (-0.0016) title (0.0006) : (0.0006) jmt (0.0018) sports (0.0032) camera (-0.0023) handlebar (0.0007) seatpost (0.0026) rack (0.0011) mount (0.0036) compatible (-0.0014) gopro (0.0052) hd (-0.0000) hero (0.0004) 2 (0.0018) 3. (0.0006) content (0.0023) : (0.0006) features (0.0004) : (-0.0005) brand (-0.0000) new (0.0014) and (0.0018) high (0.0021) quality. (0.0024) easy (0.0028) to (0.0012) install (-0.0006) & (0.0035) remove. (-0.0002) light (0.0038) weighted (0.0079) and (0.0012) portable. (0.0047) material (0.0027) : (-0.0000) plastic, (0.0019) metal. (0.0030) color (0.0021) : (0.0015) black. (0.0059) compatible (-0.0057) with (0.0040) gopro (0.0030) hero (0.0013) 3 (0.0005) / (0.0011) 2 (0.0006) / (0.0028) 1. (0.0020) suitable (-0.0014) for (0.0005) tubes (0.0033) diameter (0.0004) of (0.0018) 1. (0.0025) 9cm- (0.0011) 3. (0.0021) 5cm. (0.0017) size (0.0009) : (0.0003) 8cm (0.0017) x (0.0021) 8cm (0.0040) x (0.0036) 2cm. (0.0048) package (0.0049) included (0.0030) : (0.0052) 1 (0.0013) x (0.0007) handlebar (0.0035) seatpost (0.0046) mount (0.0038) ( (0.0032) without (0.0020) 3- (0.0026) way (0.0013) pivot (0.0041) arm (0.0026) ) (0.0013) no (0.0002) retail (0.0038) box. (0.0059) packed (0.0044) safely (0.0029) in (0.0008) bubble (0.0075) bag. (0.0056)
~~~~~~

**Node-1.3** (global 2109):

~~~~~~text
product (0.0106) from (0.0044) amazon (0.0099) platform (0.0049) with (0.0090) title (0.0085) and (0.0086) content (0.0027) : (0.0171) title (0.0073) : (0.0152) pov (0.0053) dive (0.0127) buoy (0.0122) floating (0.0141) camera (0.0066) handle- (0.0073) gopro (0.0066) edition. (-0.0192) content (-0.0018) : (0.0128) floats (0.0137) camera (0.0030) + (0.0083) bacpac (0.0056) screwable (0.0032) water- (0.0100) tight (0.0059) endcap (0.0070) direct (0.0069) 180 (0.0079) swivel (0.0089) head (0.0025) gopro (0.0069) camera (0.0082) attachment (0.0070) super- (0.0084) comfortable (-0.0006) eva (0.0182) grip (-0.0002) pocket (0.0028) sized (0.0118) & (0.0030) lightweight (-0.0149)
~~~~~~

**Node-1.4** (global 14980):

~~~~~~text
product (-0.0017) from (-0.0014) amazon (0.0042) platform (-0.0072) with (-0.0044) title (-0.0024) and (-0.0004) content (-0.0009) : (-0.0023) title (-0.0004) : (-0.0017) victsing (0.0002) suction (-0.0020) cup (0.0043) mount (0.0011) for (-0.0080) gopro (0.0014) hd (-0.0048) hero (-0.0003) hero2 (0.0024) hero3 (0.0001) camera (-0.0018) ( (0.0014) tripod (-0.0037) mount (-0.0034) and (-0.0000) handle (-0.0022) screw (0.0036) ). (-0.0015) content (0.0050) : (0.0023) features (-0.0002) : (0.0022) compatible (-0.0065) with (-0.0024) : (0.0016) all (0.0003) hd (-0.0010) hero, (0.0009) hd (-0.0012) hero2 (0.0009) and (0.0011) hd (-0.0009) hero3 (-0.0006) professional (-0.0021) cameras (0.0002) all (-0.0002) cameras (0.0019) which (0.0010) can (0.0003) fit (-0.0017) with (-0.0018) universal (0.0018) 1 (0.0013) / (-0.0028) 4? (0.0061) screwsecurely (0.0022) attaches (0.0035) camera (0.0001) housing (0.0032) to (0.0022) vehicle (0.0014) body, (0.0038) window, (0.0023) fuel (0.0008) tank, (0.0015) boats, (0.0020) kayaktop- (0.0013) of- (0.0017) the- (-0.0043) line (0.0048) mount (0.0025) with (-0.0010) enough (0.0044) holding (0.0027) power (0.0064) to (0.0012) stay (0.0042) on (0.0020) an (0.0017) airplane (0.0115) at (0.0060) 150mphcomes (0.0042) standard (0.0033) with (-0.0002) hd (0.0033) motorsports (0.0198) hero, (0.0018) motorsports (0.0172) hero (-0.0012) wide, (0.0030) and (-0.0015) motorsports (0.0190) hero (0.0057) cameraspackage (0.0120) included (-0.0080) : (-0.0034) 1 (-0.0016) x (0.0008) suction (0.0038) cup (-0.0006) mount (0.0012) for (0.0004) camera (-0.0009) with (-0.0004) universal (-0.0005) 1 (0.0011) / (-0.0005) 4 (-0.0005) " (-0.0004) screw, (0.0002) 1 (-0.0000) x (0.0015) tripod (0.0019) mount (-0.0001) for (0.0021) gopro (0.0006) camera, (-0.0002) 1 (0.0011) x (0.0006) screw (0.0012) and (-0.0021) nut, (-0.0017) 1 (0.0005) x (-0.0004) handle. (0.0047)
~~~~~~

**Node-1.5** (global 15063):

~~~~~~text
product (-0.0013) from (-0.0004) amazon (-0.0006) platform (-0.0035) with (-0.0021) title (0.0016) and (0.0023) content (0.0016) : (-0.0025) title (0.0030) : (0.0010) wocase (0.0011) & (0.0003) reg (0.0015) ; (0.0014) adjustable (0.0023) ( (0.0014) anti- (0.0008) slippery (0.0034) ) (0.0009) head (0.0018) strap (-0.0022) mount (0.0002) and (0.0006) quick (0.0026) clip (0.0004) mount (0.0040) for (-0.0119) gopro (0.0050) hero3 (0.0005) + (0.0013) 3 (0.0018) 2 (0.0021) 1 (0.0017) cameras. (-0.0008) content (0.0018) : (0.0027) this (0.0013) product (0.0016) is (0.0022) manufactured (0.0008) by (0.0005) wocase, (0.0015) with (0.0015) equivalent (0.0001) or (0.0009) even (0.0012) better (0.0010) quality (0.0021) when (0.0008) compared (-0.0029) to (0.0036) gopro (0.0031) original (0.0037) head (0.0021) strap (0.0004) mount. (0.0011) only (0.0010) the (0.0010) head (0.0010) strap (0.0002) mount (0.0020) is (0.0031) included. (0.0005) camera (0.0004) and (0.0024) tripod (0.0017) and (0.0022) other (0.0022) accessories (0.0011) shown (0.0012) in (0.0037) the (0.0001) pictures (0.0031) are (0.0033) for (0.0009) exhibition (0.0021) purpose (0.0015) only (0.0012) and (0.0022) are (0.0026) not (0.0028) included. (-0.0015) the (0.0004) head (0.0027) strap (0.0014) is (0.0028) fully (0.0027) adjustable (0.0026) to (0.0022) fit (0.0033) all (0.0022) sizes, (0.0021) the (0.0010) head (0.0027) strap (0.0005) can (0.0027) be (0.0027) worn (0.0045) over (0.0033) a (0.0026) helmet (0.0023) or (0.0030) directly (0.0020) on (0.0037) your (0.0001) head (0.0028) to (0.0022) capture (0.0028) footage (0.0036) from (0.0036) a (0.0026) headlamp- (0.0033) like (0.0014) perspective. (-0.0017) the (0.0043) quickclip (0.0012) enables (0.0005) ultra- (0.0020) compact, (0.0018) low- (0.0024) profile (0.0023) mounting, (-0.0004) and (0.0006) can (0.0025) be (0.0008) used (0.0036) to (0.0026) attach (0.0079) your (0.0043) gopro (0.0032) to (0.0055) a (0.0002) backwards (-0.0011) baseball (0.0008) cap (0.0012) or (0.0016) other (0.0012) 3mm (0.0014) to (0.0015) 10mm (0.0014) thick (0.0022) object. (0.0011)
~~~~~~

**Node-1.6** (global 15064):

~~~~~~text
product (0.0003) from (-0.0053) amazon (0.0004) platform (-0.0035) with (-0.0018) title (0.0006) and (-0.0011) content (-0.0014) : (-0.0041) title (-0.0012) : (-0.0039) wocase (0.0019) & (0.0010) reg (-0.0035) ; (0.0022) wrist (-0.0016) strap (-0.0008) mount (-0.0016) for (-0.0051) gopro (0.0014) hd (-0.0006) hero3 (0.0003) + (-0.0014) 3 (0.0009) 2 (0.0013) 1 (-0.0007) cameras (0.0019) ( (0.0040) compatible (-0.0041) with (0.0024) housing (0.0008) and (0.0002) frame (0.0022) ). (-0.0044) content (0.0060) : (-0.0005) original (-0.0022) product (-0.0002) by (-0.0006) wocase. (0.0003) wear (-0.0014) your (0.0033) gopro (0.0031) like (-0.0035) a (0.0011) watch (-0.0026) for (0.0014) easy (-0.0009) access (-0.0007) when (0.0014) capturing (0.0014) footage (-0.0024) on (-0.0008) the (0.0043) fly. (-0.0056) the (0.0032) wrist (0.0009) housing (0.0037) secures (-0.0016) your (0.0012) gopro (0.0034) flat (-0.0027) against (0.0007) your (-0.0014) wrist, (0.0004) yet (-0.0010) lets (-0.0017) you (-0.0011) quickly (-0.0002) pivot (-0.0003) the (-0.0005) camera (0.0000) upright (0.0017) to (-0.0017) shoot (-0.0003) photos (-0.0009) or (0.0001) video. (0.0003) when (0.0025) not (-0.0011) recording, (-0.0004) you (-0.0027) ' (-0.0010) ll (0.0013) have (-0.0009) full (-0.0009) use (-0.0011) of (0.0013) both (0.0005) hands, (-0.0012) making (-0.0001) it (0.0011) perfect (-0.0002) for (0.0018) surfing, (-0.0004) snorkeling, (0.0002) climbing (0.0012) and (-0.0007) skiing. (-0.0047) fits (0.0021) over (-0.0013) ski (-0.0019) gloves (-0.0021) or (-0.0002) jackets (-0.0053) with (-0.0004) the (-0.0005) included (-0.0020) adapter, (-0.0004) plus (-0.0014) straps (0.0046) to (-0.0041) kayak (-0.0004) paddles, (-0.0007) kitesurfing (0.0003) kites (-0.0037) and (-0.0007) other (-0.0016) gear (-0.0014) for (-0.0016) a (0.0036) wide (-0.0020) range (-0.0015) of (0.0014) shooting (-0.0014) possibilities. (0.0014)
~~~~~~
