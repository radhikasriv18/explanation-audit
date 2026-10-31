# Reference packet: GraphNarrator__Llama-8B__products__33376

- Method: GraphNarrator; configuration: Llama-8B; dataset: products; target node: 33376
- Explanation source: `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/118.json` (messages[assistant])
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

- ROOT (Disney-themed bedding)
  - Node-1 (Disney-themed toddler bed)
    - Node-1.1 (SpongeBob-themed toddler bed)
    - Node-1.2 (Disney Princess-themed toddler bed)
    - Node-1.3 (Disney Fairies-themed toddler bed)
    - Node-1.4 (Disney Princess-themed convertible doll bed)
    - Node-1.5 (Minnie Mouse-themed toddler bedding set)

### Word-Level Evaluation:

Keywords with high saliency scores in ROOT — "disney" (-0.04), "fairies" (-0.01), "tinkerbell" (0.01), "wall" (0.02), "sticker" (-0.00), "kit" (0.03) — are strongly associated with Disney-themed products. These directly indicate the product belongs to "Cell Phones & Accessories" is incorrect, but the keywords are more likely to be associated with a toy or a product related to Disney. More generic terms like "product" (-0.04) and "amazon" (0.01) carry negligible saliency and contribute little.

### Graph-Level Aggregation:

Node-1 (Disney-themed toddler bed, keywords: "tinkerbell" (0.04), "fairies" (0.13), "room" (0.03), "box" (0.04)) and its children — Node-1.1 (SpongeBob-themed toddler bed), Node-1.2 (Disney Princess-themed toddler bed), Node-1.3 (Disney Fairies-themed toddler bed), Node-1.4 (Disney Princess-themed convertible doll bed), Node-1.5 (Minnie Mouse-themed toddler bedding set) — are direct neighbors with moderate to high saliency, identifying Disney-themed products whose close proximity to ROOT reinforces the classification. Indirect neighbors — Node-1.1, Node-1.2, Node-1.3, Node-1.4, Node-1.5 — are all Disney-themed products, collectively confirming a Disney-themed context across both hops.

### Free-Text Explanation

The classification of ROOT into "Cell Phones & Accessories" is not supported by the provided graph. However, the correct classification is likely to be "Toys & Games" or "Home & Kitchen" given the keywords and the co-purchase neighborhood.

ROOT: Keywords like "disney" (-0.04), "fairies" (-0.01), and "tinkerbell" (0.01) clearly identify this as a Disney-themed product — quintessentially a toy or a product related to Disney.
  - Node-1: A Disney-themed toddler bed (keywords: "tinkerbell" (0.04), "fairies" (0.13), "room" (0.03), "box" (0.04)) is a direct Disney product, reinforcing the Disney-themed context.
    - Node-1.1 ~ Node-1.5: Disney-themed toddler beds and bedding sets are all toys or products related to Disney, supporting the classification.

In summary, ROOT's own high-saliency keywords strongly signal Disney-themed products, and the entire co-purchase neighborhood consists of Disney-themed products, providing robust evidence for the "Toys & Games" or "Home & Kitchen" category.
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/118.json`).

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
<verbalized-graph>ROOT: product(-0.04) amazon(0.01) platform(-0.03) title(0.00) content(0.02) title(0.01) disney(-0.04) fairies(-0.01) tinkerbell(0.01) wall(0.02) sticker(-0.00) kit.(0.03) content(-0.01) disney(-0.03) fairies(-0.04) tinkerbell(0.01) wall(0.01) sticker(-0.01) kit(-0.02) perfect(0.01) decorate(-0.01) themed(0.00) bedroom,(0.00) also(0.00) used(0.01) stick(0.01) windows,(0.02) mirrors,(0.02) toy(-0.02) boxes,(-0.00) books(-0.01) anything(0.00) else(0.01) imagine.(0.01) wipe(0.00) clean(0.01) surface(0.03) easy(0.02) maintain.(0.04) self(-0.02) adhesive.(0.04) removable(-0.03) reusable.(0.03) 
Node-1: product(-0.03) amazon(0.03) platform(-0.05) title(0.02) content(0.00) title(0.03) disney-(0.01) tinkerbell(0.04) fairies(0.13) room-(0.03) in-(0.01) a-(0.01) box(0.04) bundle.(0.02) content(-0.03) x2022(0.04) disney(-0.01) tinkerbell(0.04) fairies(0.06) toddler(0.02) bed(-0.01) canopy(0.09) 
Node-1.1: product(-0.01) amazon(0.00) platform(-0.00) title(0.00) content(0.00) title(0.01) nickelodeon(-0.02) sponge(0.00) bob(-0.00) toddler(-0.00) bed.(0.00) content(-0.00) kids(-0.01) literally(0.01) immerse(0.00) stories(0.01) favorite(0.00) fictional(0.00) characters,(0.00) spongebob(0.00) squarepants(0.00) toddler(0.00) bed(-0.00) lets(0.01) sleep(0.00) dream(0.00) spongebob(0.00) universe.(-0.00) featuring(0.00) plastic(0.01) metal(0.01) frame,(0.00) bed(0.00) built(0.01) low(0.00) ground(0.01) easy(0.00) child(0.00) access(0.01) comes(0.00) side(0.00) rails(0.01) safe(0.00) secure(0.01) sleeping.(-0.00) decal(0.01) character(0.01) appears(0.00) headboard(0.00) footboard.(0.00) bed(0.01) also(0.01) uses(0.01) standard(0.01) crib(0.01) mattress.(-0.01) 
Node-1.2: product(-0.00) amazon(0.00) platform(-0.00) title(0.00) content(-0.00) title(0.00) disney(-0.00) 4(-0.00) piece(0.00) toddler(-0.00) set,(0.00) tinkerbell.(0.00) content(0.00) let(-0.00) kids(0.00) fly(0.00) land(0.00) fairies(-0.00) disney(0.00) tinkerbell(0.00) garden(0.00) treasures(0.00) toddler(-0.00) set.(0.00) tinker(0.00) bell(0.00) floats(0.00) across(0.00) fun(-0.00) bed(-0.00) set.(0.01) x2018(0.00) made(0.00) 60(0.00) cotton(0.00) 40(0.00) polyester.(0.00) decorate(0.00) little(0.00) one(-0.00) room(0.00) adorable(-0.00) disney(-0.00) tinkerbell(-0.00) collection.(0.01) four-(-0.00) piece(0.00) toddler(0.00) set(0.00) includes(0.00) comforter,(0.00) top(0.00) sheet,(0.00) fitted(0.00) sheet(0.00) pillow(-0.00) case.(0.00) iron,(0.00) tumble(0.00) dry(0.00) low,(0.00) machine(0.00) wash(-0.00) cold.(0.01) 
Node-1.3: product(-0.00) amazon(0.00) platform(-0.00) title(0.01) content(-0.00) title(0.01) disney(-0.00) fairies(-0.00) toddler(0.00) bed.(0.00) content(0.00) disney(0.00) fairies(0.00) toddler(0.00) bed(-0.00) perfect(-0.00) transitioning(0.00) little(0.01) angel(0.01) crib(0.00) big(0.00) girl(0.00) bed.(0.00) features(0.00) high(0.00) quality(0.00) plastic(0.00) metal(0.00) frame(0.00) making(0.00) lightweight(0.00) yet(0.00) sturdy(0.01) strength(0.00) durability(0.00) last.(-0.00) bed(0.00) built(0.01) low(0.00) ground(0.00) easy(0.00) child(0.00) access(0.00) comes(0.00) side(0.00) rails(0.01) safe(0.00) secure(0.00) sleeping.(-0.00) colorful(0.01) fairies(0.00) inspired(0.01) design(0.01) theme(0.00) featuring(0.01) child(0.00) favorite(0.01) fairies(0.00) characters(-0.00) headboard(0.00) footboard(0.01) making(0.00) must(0.01) have.(-0.00) 
Node-1.4: product(-0.01) amazon(0.00) platform(-0.00) title(0.00) content(-0.00) title(0.00) disney(-0.00) princess(-0.01) 3-(0.00) in-(0.00) 1(0.00) dream(0.00) canopy(0.00) bed-(-0.00) convertible(0.00) doll(-0.00) bed.(0.01) content(-0.00) little(-0.00) girl(0.00) love(0.00) disney(-0.00) princess(-0.01) 4-(0.00) in-(-0.00) 1(0.00) princess(-0.00) bed.(0.00) 4(0.00) ways(0.00) play,(0.00) make(0.00) perfect(0.00) bed(-0.00) favorite(0.00) princess!(-0.00) features(0.01) ruffled(0.00) skirt(0.00) fabric(0.00) canopy(0.00) tied(0.00) back(0.00) bows.(0.01) transformations(-0.03) include(0.02) canopy(0.01) bed,(0.00) daybed,(0.00) crib(0.00) canopy(0.00) crib.(0.00) fits(0.00) dolls(0.01) 16(0.00) inches.(0.00) doll(0.01) included.(0.01) 
Node-1.5: product(-0.01) amazon(0.00) platform(0.01) title(0.00) content(0.00) title(-0.00) disney(0.01) 4(0.00) piece(0.00) minnie(0.00) fluttery(0.00) friends(0.00) toddler(0.00) bedding(0.00) set,(0.00) lavender(0.00) ".(0.00) content(-0.01) minnie(0.01) fluttery(0.00) friends(0.01) float(0.00) across(0.00) sweet(0.01) toddler(0.00) bedding(0.00) set(0.00) filled(0.01) flowers.(0.00) little(0.00) one(0.00) love(0.01) climbing(0.00) bed(0.00) minnie(0.00) friends.(-0.00) adorable(0.01) bedding(0.01) set(0.00) surely(0.01) brighten(0.00) childs(0.00) room.(-0.01) set(0.00) includes(0.01) comforter,(0.00) standard(0.00) pillowcase,(0.00) flat(0.00) top(0.00) sheet(0.01) fitted(0.01) bottom(0.00) sheet.(0.01) 100(-0.00) polyester(0.01) microfiber.(0.01) machine(0.01) wash(-0.00) seperately(0.01) cold(0.00) water,(0.01) gentle(0.02) cycle.(0.01) use(0.00) non-(0.00) chlorine(0.00) bleach(0.01) needed.(0.01) tumble(0.01) dry(-0.01) low(-0.00) heat.(0.01) iron(0.01) low(-0.00) heat(0.00) needed.(0.00) 
</verbalized-graph>

### Classification Label
Cell Phones & Accessories

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 33376
- Title: Disney Fairies (Tinkerbell) Wall Sticker Kit
- True class (canonical `y`): **Toys & Games**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Home & Kitchen**
- Prediction recorded by this method's pipeline: **Cell Phones & Accessories**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Disney Fairies (Tinkerbell) Wall Sticker Kit. Content: Disney Fairies (Tinkerbell) Wall Sticker Kit is perfect to decorate a themed bedroom, they can also be used to stick on Windows, Mirrors, Toy Boxes, Books and anything else you can imagine. With a wipe clean surface they are easy to maintain. Self adhesive. Removable and Reusable.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 7314 | Baby | Disney - Tinkerbell Fairies Room-in-a-Box Bundle |

### 2-hop (shortest distance exactly 2): 5 nodes

| node id | true class | title |
|---|---|---|
| 854 | Home & Kitchen | Nickelodeon Sponge Bob Toddler Bed |
| 33375 | Baby | Disney 4 Piece Toddler Set, Tinkerbell |
| 33377 | Home & Kitchen | Disney Fairies Toddler Bed |
| 33378 | Toys & Games | Disney Princess 3-in-1 Dream Canopy Bed - Convertible Doll Bed |
| 33379 | Baby | "Disney 4 Piece Minnie's Fluttery Friends Toddler Bedding Set, Lavender" |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/118.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Cell Phones & Accessories**, ground truth = **Toys & Games**.
The verbalized graph is 5134 characters; the model saw the first 6000 (the whole graph).
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 33376 | 70 | 0.0425 | yes |
| Node-1 | 1 | 7314 | 32 | 0.1349 | yes |
| Node-1.1 | 2 | 854 | 94 | 0.0116 | yes |
| Node-1.2 | 3 | 33375 | 95 | 0.0087 | yes |
| Node-1.3 | 4 | 33377 | 101 | 0.0112 | yes |
| Node-1.4 | 5 | 33378 | 86 | 0.0238 | yes |
| Node-1.5 | 6 | 33379 | 108 | 0.0163 | yes |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, ROOT->Node-1

### Tokens and scores

**ROOT** (global 33376):

~~~~~~text
product (-0.0411) from (0.0055) amazon (0.0064) platform (-0.0275) with (-0.0106) title (0.0006) and (0.0236) content (0.0163) : (0.0295) title (0.0127) : (0.0252) disney (-0.0399) fairies (-0.0113) ( (0.0234) tinkerbell (0.0141) ) (-0.0108) wall (0.0244) sticker (-0.0049) kit. (0.0262) content (-0.0051) : (0.0425) disney (-0.0261) fairies (-0.0373) ( (0.0124) tinkerbell (0.0060) ) (0.0086) wall (0.0120) sticker (-0.0081) kit (-0.0215) is (0.0343) perfect (0.0149) to (0.0122) decorate (-0.0135) a (0.0387) themed (0.0001) bedroom, (0.0007) they (0.0324) can (0.0186) also (0.0012) be (0.0223) used (0.0111) to (-0.0075) stick (0.0117) on (0.0123) windows, (0.0186) mirrors, (0.0154) toy (-0.0201) boxes, (-0.0000) books (-0.0076) and (0.0026) anything (0.0040) else (0.0063) you (-0.0170) can (-0.0099) imagine. (0.0118) with (-0.0108) a (0.0189) wipe (0.0013) clean (0.0089) surface (0.0318) they (-0.0244) are (0.0105) easy (0.0181) to (-0.0135) maintain. (0.0422) self (-0.0193) adhesive. (0.0365) removable (-0.0281) and (-0.0018) reusable. (0.0274)
~~~~~~

**Node-1** (global 7314):

~~~~~~text
product (-0.0303) from (0.0370) amazon (0.0301) platform (-0.0460) with (0.0119) title (0.0191) and (0.0046) content (0.0014) : (0.0042) title (0.0319) : (0.0175) disney- (0.0127) tinkerbell (0.0371) fairies (0.1349) room- (0.0326) in- (0.0143) a- (0.0073) box (0.0440) bundle. (0.0171) content (-0.0297) : (-0.0034) & (0.0887) # (0.1154) x2022 (0.0394) ; (0.0555) disney (-0.0074) tinkerbell (0.0423) fairies (0.0642) toddler (0.0202) bed (-0.0145) with (0.0047) canopy (0.0893)
~~~~~~

**Node-1.1** (global 854):

~~~~~~text
product (-0.0072) from (-0.0052) amazon (0.0038) platform (-0.0048) with (-0.0014) title (0.0046) and (-0.0001) content (0.0025) : (0.0098) title (0.0057) : (0.0088) nickelodeon (-0.0157) sponge (0.0024) bob (-0.0005) toddler (-0.0006) bed. (0.0044) content (-0.0002) : (-0.0025) kids (-0.0058) can (0.0015) now (0.0013) literally (0.0058) immerse (0.0030) themselves (0.0034) in (0.0031) the (-0.0012) stories (0.0078) of (0.0030) their (0.0023) favorite (0.0011) fictional (0.0020) characters, (0.0025) as (0.0048) the (0.0008) spongebob (0.0019) squarepants (0.0015) toddler (0.0023) bed (-0.0021) lets (0.0078) them (0.0052) sleep (0.0041) and (0.0032) dream (0.0040) in (0.0041) the (0.0006) spongebob (0.0004) universe. (-0.0032) featuring (0.0034) a (0.0016) plastic (0.0053) and (0.0045) metal (0.0063) frame, (0.0035) the (-0.0020) bed (0.0032) is (0.0044) built (0.0068) low (0.0048) to (0.0026) the (-0.0032) ground (0.0072) for (0.0022) easy (0.0032) child (0.0006) access (0.0060) and (0.0056) comes (0.0000) with (-0.0012) side (0.0041) rails (0.0116) for (0.0024) safe (0.0048) and (0.0045) secure (0.0065) sleeping. (-0.0016) a (-0.0007) decal (0.0064) of (0.0014) the (0.0046) character (0.0066) appears (0.0049) on (0.0014) the (0.0014) headboard (0.0048) and (0.0055) footboard. (0.0010) the (0.0033) bed (0.0060) also (0.0082) uses (0.0069) a (0.0032) standard (0.0066) crib (0.0089) mattress. (-0.0141)
~~~~~~

**Node-1.2** (global 33375):

~~~~~~text
product (-0.0027) from (0.0019) amazon (0.0009) platform (-0.0009) with (-0.0002) title (0.0020) and (0.0015) content (-0.0033) : (0.0011) title (0.0013) : (0.0001) disney (-0.0005) 4 (-0.0000) piece (0.0010) toddler (-0.0005) set, (0.0005) tinkerbell. (0.0007) content (0.0014) : (-0.0019) let (-0.0013) kids (0.0001) fly (0.0004) into (-0.0005) the (-0.0002) land (0.0005) of (0.0015) fairies (-0.0007) with (-0.0009) disney (0.0006) tinkerbell (0.0014) garden (0.0013) treasures (0.0002) toddler (-0.0009) set. (0.0016) tinker (0.0008) bell (0.0005) floats (0.0025) across (0.0011) this (0.0002) fun (-0.0000) bed (-0.0008) set. (0.0054) it (-0.0001) & (0.0016) # (0.0030) x2018 (0.0014) ; (0.0057) s (0.0012) made (0.0025) of (0.0007) 60 (0.0022) % (0.0017) cotton (0.0015) and (0.0008) 40 (0.0006) % (-0.0006) polyester. (0.0023) decorate (0.0002) your (-0.0032) little (0.0006) one (-0.0001) ' (0.0008) s (0.0000) room (0.0020) with (0.0021) this (0.0006) adorable (-0.0029) disney (-0.0005) tinkerbell (-0.0006) collection. (0.0087) the (-0.0041) four- (-0.0006) piece (0.0010) toddler (0.0008) set (0.0020) includes (0.0001) a (0.0003) comforter, (0.0010) top (0.0027) sheet, (0.0022) fitted (0.0038) sheet (0.0017) and (-0.0010) a (-0.0018) pillow (-0.0002) case. (0.0005) do (-0.0005) not (0.0002) iron, (0.0023) tumble (0.0004) dry (0.0019) low, (0.0037) machine (0.0038) wash (-0.0006) cold. (0.0065)
~~~~~~

**Node-1.3** (global 33377):

~~~~~~text
product (-0.0021) from (0.0021) amazon (0.0026) platform (-0.0007) with (0.0014) title (0.0063) and (0.0027) content (-0.0043) : (0.0112) title (0.0101) : (0.0078) disney (-0.0027) fairies (-0.0009) toddler (0.0014) bed. (0.0029) content (0.0038) : (0.0037) the (-0.0004) disney (0.0048) fairies (0.0006) toddler (0.0011) bed (-0.0024) is (0.0062) perfect (-0.0011) for (0.0055) transitioning (0.0032) your (0.0035) little (0.0067) angel (0.0052) from (0.0028) crib (0.0021) to (0.0018) big (0.0022) girl (0.0039) bed. (0.0034) features (0.0030) a (-0.0007) high (0.0024) quality (0.0038) plastic (0.0019) and (0.0042) metal (0.0043) frame (0.0030) making (0.0011) it (0.0050) lightweight (0.0019) yet (0.0034) sturdy (0.0062) for (0.0015) strength (0.0019) and (0.0031) durability (0.0015) that (0.0037) will (0.0016) last. (-0.0002) the (0.0002) bed (0.0015) is (0.0091) built (0.0061) low (0.0042) to (0.0008) the (-0.0044) ground (0.0050) for (0.0001) easy (0.0027) child (0.0026) access (0.0016) and (0.0064) comes (0.0047) with (0.0016) side (0.0036) rails (0.0051) for (0.0024) safe (0.0027) and (0.0047) secure (0.0033) sleeping. (-0.0017) a (-0.0012) colorful (0.0059) fairies (0.0044) inspired (0.0083) design (0.0080) theme (0.0031) featuring (0.0079) your (0.0061) child (0.0014) ' (0.0009) s (0.0035) favorite (0.0073) fairies (0.0023) characters (-0.0003) on (0.0027) the (0.0037) headboard (0.0045) and (0.0056) footboard (0.0073) making (0.0010) it (0.0051) a (0.0038) must (0.0100) have. (-0.0025)
~~~~~~

**Node-1.4** (global 33378):

~~~~~~text
product (-0.0055) from (0.0037) amazon (0.0013) platform (-0.0012) with (0.0002) title (0.0019) and (-0.0023) content (-0.0046) : (0.0046) title (0.0035) : (0.0040) disney (-0.0004) princess (-0.0068) 3- (0.0018) in- (0.0004) 1 (0.0000) dream (0.0029) canopy (0.0033) bed- (-0.0003) convertible (0.0018) doll (-0.0015) bed. (0.0061) content (-0.0013) : (0.0050) your (-0.0007) little (-0.0031) girl (0.0039) will (0.0002) love (0.0020) the (-0.0003) disney (-0.0009) princess (-0.0062) 4- (0.0008) in- (-0.0004) 1 (0.0023) princess (-0.0021) bed. (0.0041) with (0.0031) 4 (0.0017) ways (0.0007) to (0.0026) play, (0.0013) she (0.0078) can (0.0017) make (0.0015) the (0.0001) perfect (0.0048) bed (-0.0008) for (-0.0000) her (0.0021) favorite (0.0035) princess! (-0.0050) features (0.0058) a (0.0023) ruffled (0.0015) skirt (0.0023) and (0.0004) a (0.0023) fabric (0.0019) canopy (0.0026) that (0.0020) can (0.0012) be (0.0034) tied (0.0010) back (0.0023) with (0.0032) bows. (0.0051) transformations (-0.0261) include (0.0238) : (0.0047) canopy (0.0060) bed, (0.0036) daybed, (0.0015) crib (0.0009) and (0.0032) canopy (0.0029) crib. (0.0050) fits (0.0045) dolls (0.0081) up (0.0042) to (0.0024) 16 (0.0039) inches. (0.0010) doll (0.0053) not (0.0001) included. (0.0071)
~~~~~~

**Node-1.5** (global 33379):

~~~~~~text
product (-0.0097) from (-0.0038) amazon (0.0021) platform (0.0079) with (-0.0054) title (0.0049) and (-0.0121) content (0.0037) : (0.0040) title (-0.0038) : (-0.0029) " (-0.0211) disney (0.0137) 4 (0.0036) piece (0.0012) minnie (0.0040) ' (0.0011) s (0.0023) fluttery (0.0049) friends (0.0041) toddler (0.0025) bedding (0.0014) set, (0.0030) lavender (0.0006) ". (0.0036) content (-0.0051) : (0.0006) minnie (0.0055) and (0.0002) her (0.0022) fluttery (0.0024) friends (0.0052) float (0.0042) across (0.0008) this (0.0047) sweet (0.0068) toddler (0.0045) bedding (0.0046) set (0.0017) filled (0.0064) with (0.0046) flowers. (0.0017) your (-0.0025) little (0.0036) one (0.0049) will (0.0032) love (0.0064) climbing (0.0043) into (0.0018) bed (0.0048) with (0.0041) minnie (0.0033) and (0.0025) her (0.0053) friends. (-0.0049) this (0.0096) adorable (0.0094) bedding (0.0064) set (0.0015) will (0.0019) surely (0.0069) brighten (0.0038) up (0.0038) your (-0.0029) childs (0.0022) room. (-0.0077) set (0.0020) includes (0.0127) comforter, (0.0020) standard (0.0036) pillowcase, (0.0032) flat (0.0002) top (0.0037) sheet (0.0061) and (0.0022) fitted (0.0122) bottom (0.0039) sheet. (0.0059) 100 (-0.0024) % (0.0103) polyester (0.0089) microfiber. (0.0102) machine (0.0132) wash (-0.0016) seperately (0.0101) in (0.0059) cold (0.0032) water, (0.0069) gentle (0.0163) cycle. (0.0109) use (0.0009) only (-0.0003) non- (0.0050) chlorine (0.0049) bleach (0.0081) when (0.0084) needed. (0.0061) tumble (0.0085) dry (-0.0117) on (-0.0081) low (-0.0022) heat. (0.0096) iron (0.0098) on (0.0008) low (-0.0000) heat (0.0044) when (0.0012) needed. (0.0041)
~~~~~~
