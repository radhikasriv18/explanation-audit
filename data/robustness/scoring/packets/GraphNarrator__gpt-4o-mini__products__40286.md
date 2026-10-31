# Reference packet: GraphNarrator__gpt-4o-mini__products__40286

- Method: GraphNarrator; configuration: gpt-4o-mini; dataset: products; target node: 40286
- Explanation source: `./robustness_2026-10-30/graphnarrator_gpt4omini/generated_expls-601/150.json` (messages[assistant])
- Scored scope (what the claims were extracted from): ### Free-Text Explanation section
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

Claims were extracted from the `### Free-Text Explanation` section only; the full assistant message is shown here.

~~~~~~text
### Reasoning

0. **Graph Structure Reconstruction:**

In the provided verbalized graph, the ROOT node (first line) is the target for classification. The structure of the graph is as follows:

- ROOT (Giganotosaurus figure)
  - Node-1 (Brachiosaurus figure)
    - Node-1.1 (Tyrannosaurus Rex figure)
    - Node-1.2 (Triceratops figure)
    - Node-1.3 (Safari Ltd Brachiosaurus)
    - Node-1.4 (Papo Plesiosaurus)
    - Node-1.5 (Collecta Diplodocus)

1. **Word-Level Evaluation:**

The ROOT node contains keywords such as "giganotosaurus," "dinosaur," and "figure," which are strongly indicative of a toy or collectible related to dinosaurs. The presence of "playing" and "movable" further suggests that this product is intended for play, aligning it with children's toys. The negative scores for terms like "product," "amazon," and "content" suggest they are less relevant for classification.

2. **Graph-Level Aggregation:**

Node-1 (Brachiosaurus figure) includes keywords like "tallest," "largest," and "replica," reinforcing the idea of collectible dinosaur figures. The direct neighbors of Node-1, such as Node-1.1 (Tyrannosaurus Rex) and Node-1.2 (Triceratops), also emphasize the theme of dinosaur figures, further solidifying the classification context. Additional nodes like Node-1.3 (Safari Ltd Brachiosaurus), Node-1.4 (Papo Plesiosaurus), and Node-1.5 (Collecta Diplodocus) contribute to the overall theme of dinosaur collectibles, confirming the classification as "Books" since many dinosaur figures are often accompanied by educational materials or books about dinosaurs.

### Free-Text Explanation
```markdown
The classification of ROOT into "Books" is supported by its own keywords and the co-purchase neighborhood.

ROOT: The keywords "giganotosaurus" and "dinosaur" clearly indicate that this is a collectible figure related to dinosaurs, which often corresponds with educational books about these creatures. The term "playing" suggests that this figure is intended for children, who frequently engage with books and toys about dinosaurs.
  - Node-1: The Brachiosaurus figure (keywords: "tallest," "largest," "replica") emphasizes the collectible nature of dinosaur figures, which are often paired with books that provide information about these species.
    - Node-1.1: The Tyrannosaurus Rex figure reinforces the theme of dinosaur collectibles, which are commonly featured in children's literature about dinosaurs.
    - Node-1.2: The Triceratops figure further supports the classification, as it is another popular dinosaur often depicted in educational materials.
    - Node-1.3: The Safari Ltd Brachiosaurus adds to the collection of dinosaur figures, which are frequently accompanied by books that educate children about their characteristics and history.
    - Node-1.4: The Papo Plesiosaurus continues the trend of dinosaur figures, which are often marketed alongside books for learning.
    - Node-1.5: The Collecta Diplodocus figure also fits within the theme of educational dinosaur toys, further affirming the connection to books.

In summary, ROOT's keywords indicate a dinosaur collectible, and the entire co-purchase neighborhood consists of various dinosaur figures that are typically associated with educational books, providing strong evidence for the "Books" classification.
```
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/150.json`).

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
<verbalized-graph>ROOT: product(-0.02) amazon(-0.05) platform(-0.08) title(0.08) content(-0.05) title(-0.01) schleich(0.02) giganotosaurus.(0.01) content(-0.04) schleich(0.01) giganotosaurus(0.03) perfect(0.02) size(-0.00) playing,(0.04) movable(0.01) lower(-0.00) jaw.(0.01) small(0.01) quills(0.01) large(0.01) spots(0.02) back,(-0.00) dinosaur(-0.09) quite(0.02) sight.(0.02) gigantosaurus(0.03) three(0.01) claws(0.03) short(-0.01) front(0.02) legs(-0.00) fed(-0.00) herbivores.(-0.00) scientists(-0.08) suspect(-0.02) gigantosaurus(-0.00) able(-0.01) run(0.02) fast(-0.02) thanks(-0.02) thin(-0.03) tail(0.00) held(0.00) upright.(0.01) 
Node-1: product(-0.00) amazon(0.01) platform(0.00) title(0.01) content(0.00) title(0.00) schleich(0.00) brachiosaurus.(0.01) content(0.01) brachiosaurus(-0.00) one(0.01) tallest(0.00) largest(0.01) dinosaurs(-0.02) yet(0.01) found,(0.00) long(0.01) neck,(0.00) small(0.01) head,(0.01) relatively(-0.00) short,(0.01) thick(-0.00) tail.(0.01) hand(0.02) painted(0.02) replica(0.01) comes(0.03) equipped(-0.00) booklet(0.01) containing(0.00) scientific(0.01) data(0.01) brachiosaurus(-0.00) figure(0.01) human(0.01) scale,(0.01) facilitate(0.02) comparison(-0.00) size.(0.01) sculpted(-0.02) close(0.00) cooperation(0.00) natural(0.02) history(0.01) museum(0.02) humboldt-(0.01) university(0.03) berlin.(0.01) 
Node-1.1: product(-0.00) amazon(0.00) platform(-0.00) title(0.00) content(-0.00) title(-0.00) schleich(0.00) tyrannosaurus(0.00) rex.(-0.00) content(-0.00) schleich(0.00) tyrannosaurus(0.00) rex(0.00) perfect(-0.00) size(0.00) playing,(-0.00) although(0.00) tyrannosaurus(0.00) rex(-0.00) looked(0.00) quite(0.00) threatening(0.00) could(0.00) hardly(0.00) use(0.00) front(0.00) legs(0.00) armed(0.00) two(0.00) claws(0.00) since(0.00) even(0.00) reach(0.00) mouth.(-0.00) nearly(0.00) seven(-0.00) metres(0.00) tall(-0.00) thirteen(0.00) metres(0.00) long(0.00) tyrannosaurus(0.00) rex(0.00) probably(0.00) skilled(0.00) hunter(0.00) rather(0.00) scavenger(0.00) probably(0.00) fed(0.00) leavings(0.00) animals.(0.00) fifty(0.00) teeth(0.00) measuring(0.00) 15(0.00) centimetres(0.00) length(0.00) used(0.00) chewing(0.00) rather(0.00) tearing(0.00) since(0.00) swallowed(-0.00) food(-0.00) large(0.00) chunks.(-0.00) improve(0.00) depth-(0.00) perception(0.00) searching(0.00) food(-0.00) eyes(0.00) tyrannosaurus(0.00) rex(0.00) oriented(0.00) toward(-0.00) front(0.00) fields(0.00) vision(0.00) eyes(0.01) overlapped.(-0.00) 
Node-1.2: product(-0.00) amazon(0.00) platform(0.00) title(0.00) content(-0.00) title(0.00) schleich(0.00) triceratops(0.00) figure.(0.00) content(-0.00) triceratops,(0.00) although(-0.00) looked(0.00) fierce,(0.00) fed(0.00) plants(0.00) trees.(0.00) reason,(0.00) hunted(-0.00) tyrannosaurus(0.00) rex.(-0.00) front(0.00) jaw(0.00) formed(0.00) beak,(0.00) similar(0.00) parrot,(0.00) used(0.00) cutting(0.00) vegetation.(0.00) triceratops(0.00) three(0.00) horns(0.00) made(0.00) keratin,(-0.00) protein(0.00) composes(0.00) fingernails(-0.00) hair(0.00) horns(0.00) eyes(0.00) longest,(-0.00) extending(-0.00) almost(0.00) three(-0.00) feet.(-0.00) since(-0.00) head(0.00) equal(0.00) weight(0.00) small(0.00) car(0.00) approximately(0.00) one(0.00) third(0.00) body,(-0.00) tail(0.00) also(-0.00) heavy(0.00) keep(-0.00) thirty(0.00) foot(-0.00) long(0.00) body(0.00) balanced.(0.00) legs(0.00) strong,(0.00) similar(-0.00) elephant(0.00) legs(0.00) today.(-0.00) 
Node-1.3: product(0.00) amazon(0.01) platform(-0.00) title(-0.00) content(0.00) title(0.00) safari(0.00) ltd(-0.00) carnegie(0.00) brachiosaurus.(0.00) content(0.00) 25(0.00) years,(0.00) safari(-0.00) ltd(-0.00) proud(-0.00) provide(0.00) premier(0.00) line(0.00) scale(0.00) model,(0.00) dinosaur(0.00) collectibles.(0.00) safari(-0.00) ltd(0.00) takes(0.00) pride(0.00) providing(0.00) breathtaking,(0.00) innovative(0.00) value(0.00) priced(0.00) figures(0.00) 3(0.00) generations.(0.00) 
Node-1.4: product(-0.00) amazon(-0.00) platform(-0.00) title(-0.00) content(0.00) title(0.00) papo(-0.00) plesiosaurus.(-0.00) content(0.00) papo(0.00) figures(0.00) designed(-0.00) inspire(0.00) creative,(0.00) imaginative(0.00) play(0.00) among(0.00) children(-0.00) ages.(0.00) create(0.00) simple(-0.00) attractive(0.00) toys(0.00) child(-0.00) friendly(-0.00) designs(0.00) encourage(0.00) actively(0.00) use(0.00) imagination(0.00) develop(0.00) active(0.00) play,(0.00) stimulation(0.00) fun.(-0.00) papo(-0.00) figurines(0.00) hand(0.00) painted(0.00) include(0.00) wide(0.00) range(-0.00) including(0.00) knights,(-0.00) animals,(0.00) pirates,(0.00) fantasy(-0.00) well(0.00) many(0.00) others.(-0.00) safety(0.00) tested(0.00) carry(0.00) appropriate(-0.00) certification(0.00) box(0.00) labeling.(0.00) 
Node-1.5: product(-0.00) amazon(0.00) platform(-0.00) title(0.00) content(0.00) title(0.00) collecta(0.00) diplodocus(0.00) dinosaur(-0.00) toy.(-0.00) content(0.00) collecta(0.00) replica(-0.00) diplodocus(-0.00) lifelike(0.00) detailed,(0.00) texture(0.00) skin,(0.00) wrinkles(0.00) belly.(-0.00) whip-(0.00) like(0.00) tail(0.00) long(0.00) neck(-0.00) made(0.00) diplodocus(0.00) one(0.00) familiar(0.00) dinosaurs.(-0.00) creature(0.00) lived(0.00) approximately(0.00) 155-(0.00) 148(0.00) million(0.00) years(0.00) ago,(0.00) may(0.00) 177(0.00) feet(0.00) long,(0.00) probably(0.00) weighed(0.00) 125(0.00) short(0.00) tons.(-0.00) diplodocus(0.00) lived(-0.00) area(0.00) made(0.00) colorado,(0.00) utah,(0.00) montana(0.00) wyoming.(-0.00) beautifully(-0.00) sulpted,(0.00) collectible(-0.00) figure(-0.00) prehistoric(-0.00) life(0.00) collection(-0.00) measurse7.(0.00) 5(-0.00) x(0.00) 9.(0.00) 4(0.00) h.(0.00) carefully(0.00) sculpted(0.00) figure(0.00) approved(0.00) archeologist(0.00) anthony(-0.00) beeson,(0.00) well-(0.00) respected(0.00) expert(-0.00) paleoimagery.(0.00) collecta(0.00) models(0.00) individually(0.00) hand(0.00) crafted(0.00) highest(0.00) standards(0.00) made(0.00) finest(0.00) safest(0.00) materials,(0.00) guarantee</verbalized-graph>

### Classification Label
Books

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 40286
- Title: Schleich Giganotosaurus
- True class (canonical `y`): **Toys & Games**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Toys & Games**
- Prediction recorded by this method's pipeline: **Books**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Schleich Giganotosaurus. Content: Schleich's Giganotosaurus is the perfect size for playing, has movable lower jaw. With small quills and large spots on its back, this dinosaur was quite a sight. The Gigantosaurus had three claws on each of its short front legs and fed on herbivores. Scientists suspect that the Gigantosaurus was able to run very fast thanks to its thin tail which it held upright.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 4 nodes

| node id | true class | title |
|---|---|---|
| 9357 | Toys & Games | Schleich Brachiosaurus |
| 9365 | Books | Walking With Dinosaurs: A Reusable Sticker Book (Walking With Dinosaurs the 3d Movie) |
| 9387 | Toys & Games | Tyrannosaurus Rex Soft Plastic Dinosaur (Large) |
| 9392 | Home & Kitchen | (24x36) Dinosaur Evolution Educational Science Chart Poster |

### 2-hop (shortest distance exactly 2): 20 nodes

| node id | true class | title |
|---|---|---|
| 1118 | Toys & Games | Schleich Tyrannosaurus Rex |
| 1119 | Toys & Games | "Hatch'em (Growing Pet Dinosaur)" |
| 1121 | Books | My Big Dinosaur Book |
| 9385 | Books | How Do Dinosaurs Play with Their Friends? |
| 10599 | Toys & Games | Safari Ltd  Wild Safari Liopleurodon |
| 40284 | Toys & Games | Schleich Triceratops Figure |
| 40285 | Toys & Games | Safari LTD Carnegie Brachiosaurus |
| 40287 | Toys & Games | Papo Plesiosaurus |
| 40288 | Toys & Games | CollectA Diplodocus Dinosaur Toy |
| 40308 | Toys & Games | Spinosaurus |
| 40320 | Toys & Games | Walking With Dinosaurs (Pack of 3) |
| 40321 | Toys & Games | Schleich Triceratops |
| 40322 | Toys & Games | Papo Pachyrhinosaurus |
| 40407 | Toys & Games | Realistic Triceratops 12&quot; by Wild Republic |
| 40408 | Toys & Games | Schleich Velociraptor |
| 40409 | Toys & Games | 12 foam dinosaur masks |
| 40425 | Tools & Home Improvement | Dinosaur Volcano Decorative Outlet Cover |
| 40426 | Books | Dinosaurs and Other Prehistoric Animals (Smithsonian Handbooks) |
| 40427 | Toys & Games | Dinosaurs Match Me Game |
| 40428 | Home & Kitchen | Famous Scientists Poster Print, 24x36 Poster Print, 24x36 |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/150.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Books**, ground truth = **Toys & Games**.
The verbalized graph is 19441 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 40286 | 80 | 0.1026 | yes |
| Node-1 | 1 | 9357 | 79 | 0.0309 | yes |
| Node-1.1 | 5 | 1118 | 145 | 0.0056 | yes |
| Node-1.2 | 6 | 40284 | 130 | 0.0010 | yes |
| Node-1.3 | 7 | 40285 | 53 | 0.0060 | yes |
| Node-1.4 | 8 | 40287 | 93 | 0.0021 | yes |
| Node-1.5 | 9 | 40288 | 187 | 0.0013 | yes |
| Node-2 | 2 | 9365 | 68 | 0.0394 | no |
| Node-2.1 | 10 | 1119 | 95 | 0.0027 | no |
| Node-2.2 | 11 | 10599 | 105 | 0.0023 | no |
| Node-2.3 | 12 | 40320 | 57 | 0.0025 | no |
| Node-2.4 | 13 | 40321 | 142 | 0.0003 | no |
| Node-2.5 | 14 | 40322 | 93 | 0.0028 | no |
| Node-3 | 3 | 9387 | 44 | 0.0186 | no |
| Node-3.1 | 15 | 1121 | 269 | 0.0082 | no |
| Node-3.2 | 16 | 9385 | 153 | 0.0052 | no |
| Node-3.3 | 17 | 40308 | 38 | 0.0040 | no |
| Node-3.4 | 18 | 40407 | 63 | 0.0080 | no |
| Node-3.5 | 19 | 40408 | 110 | 0.0011 | no |
| Node-3.6 | 20 | 40409 | 23 | 0.0139 | no |
| Node-4 | 4 | 9392 | 31 | 0.0239 | no |
| Node-4.1 | 21 | 40425 | 140 | 0.0031 | no |
| Node-4.2 | 22 | 40426 | 44 | 0.0026 | no |
| Node-4.3 | 23 | 40427 | 73 | 0.0037 | no |
| Node-4.4 | 24 | 40428 | 46 | 0.0026 | no |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->ROOT, Node-1.1->Node-1, Node-1.1->Node-2, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, Node-2->Node-1.1, Node-2->Node-2.1, Node-2->Node-2.2, Node-2->Node-2.3, Node-2->Node-2.4, Node-2->Node-2.5, Node-2->ROOT, Node-2.1->Node-2, Node-2.2->Node-2, Node-2.3->Node-2, Node-2.4->Node-2, Node-2.5->Node-2, Node-3->Node-3.1, Node-3->Node-3.2, Node-3->Node-3.3, Node-3->Node-3.4, Node-3->Node-3.5, Node-3->Node-3.6, Node-3->ROOT, Node-3.1->Node-3, Node-3.1->Node-4, Node-3.2->Node-3, Node-3.3->Node-3, Node-3.4->Node-3, Node-3.5->Node-3, Node-3.6->Node-3, Node-4->Node-3.1, Node-4->Node-4.1, Node-4->Node-4.2, Node-4->Node-4.3, Node-4->Node-4.4, Node-4->ROOT, Node-4.1->Node-4, Node-4.2->Node-4, Node-4.3->Node-4, Node-4.4->Node-4, ROOT->Node-1, ROOT->Node-2, ROOT->Node-3, ROOT->Node-4

### Tokens and scores

**ROOT** (global 40286):

~~~~~~text
product (-0.0161) from (0.0342) amazon (-0.0548) platform (-0.0808) with (0.0297) title (0.0755) and (0.0034) content (-0.0463) : (0.1026) title (-0.0063) : (0.0069) schleich (0.0210) giganotosaurus. (0.0124) content (-0.0446) : (0.0113) schleich (0.0119) ' (0.0092) s (-0.0004) giganotosaurus (0.0328) is (-0.0138) the (0.0092) perfect (0.0151) size (-0.0001) for (0.0348) playing, (0.0400) has (-0.0131) movable (0.0119) lower (-0.0030) jaw. (0.0102) with (-0.0137) small (0.0077) quills (0.0072) and (-0.0017) large (0.0078) spots (0.0165) on (0.0217) its (0.0105) back, (-0.0048) this (0.0414) dinosaur (-0.0935) was (0.0243) quite (0.0160) a (-0.0054) sight. (0.0167) the (-0.0101) gigantosaurus (0.0253) had (0.0143) three (0.0095) claws (0.0304) on (0.0038) each (0.0184) of (-0.0076) its (-0.0021) short (-0.0121) front (0.0161) legs (-0.0042) and (0.0005) fed (-0.0037) on (0.0001) herbivores. (-0.0028) scientists (-0.0771) suspect (-0.0247) that (-0.0179) the (0.0250) gigantosaurus (-0.0004) was (0.0211) able (-0.0129) to (-0.0052) run (0.0158) very (-0.0526) fast (-0.0155) thanks (-0.0229) to (-0.0282) its (-0.0362) thin (-0.0253) tail (0.0035) which (-0.0289) it (-0.0268) held (0.0043) upright. (0.0108)
~~~~~~

**Node-1** (global 9357):

~~~~~~text
product (-0.0003) from (0.0011) amazon (0.0097) platform (0.0049) with (-0.0153) title (0.0131) and (0.0008) content (0.0044) : (-0.0026) title (0.0025) : (0.0055) schleich (0.0032) brachiosaurus. (0.0095) content (0.0062) : (0.0008) brachiosaurus (-0.0013) one (0.0075) of (0.0108) the (0.0077) tallest (0.0049) and (0.0071) largest (0.0103) dinosaurs (-0.0157) yet (0.0093) found, (0.0032) had (-0.0000) a (0.0049) long (0.0058) neck, (0.0029) small (0.0128) head, (0.0095) and (0.0088) relatively (-0.0013) short, (0.0121) thick (-0.0001) tail. (0.0092) this (0.0189) hand (0.0219) painted (0.0221) replica (0.0097) comes (0.0309) equipped (-0.0035) with (0.0059) booklet (0.0102) containing (0.0040) scientific (0.0084) data (0.0087) about (0.0060) brachiosaurus (-0.0006) and (0.0076) a (-0.0000) figure (0.0054) of (0.0064) a (0.0020) human (0.0071) in (0.0063) the (0.0008) same (-0.0006) scale, (0.0076) to (0.0078) facilitate (0.0202) comparison (-0.0036) of (0.0133) the (0.0070) size. (0.0146) sculpted (-0.0170) in (0.0182) close (0.0003) cooperation (0.0048) with (0.0070) the (-0.0049) natural (0.0236) history (0.0097) museum (0.0169) of (-0.0009) the (0.0029) humboldt- (0.0090) university (0.0300) berlin. (0.0073)
~~~~~~

**Node-1.1** (global 1118):

~~~~~~text
product (-0.0002) from (0.0038) amazon (0.0032) platform (-0.0033) with (0.0005) title (0.0032) and (0.0014) content (-0.0003) : (-0.0002) title (-0.0015) : (0.0009) schleich (0.0023) tyrannosaurus (0.0030) rex. (-0.0019) content (-0.0009) : (0.0025) schleich (0.0014) ' (0.0024) s (-0.0006) tyrannosaurus (0.0025) rex (0.0010) is (0.0024) the (0.0056) perfect (-0.0002) size (0.0022) for (0.0051) playing, (-0.0010) although (0.0030) the (0.0032) tyrannosaurus (0.0029) rex (-0.0009) looked (0.0005) quite (0.0026) threatening (0.0012) it (0.0023) could (0.0008) hardly (0.0012) use (0.0008) its (0.0007) front (0.0004) legs (0.0007) armed (0.0013) with (0.0013) just (0.0013) two (0.0026) claws (0.0012) since (0.0011) they (0.0023) did (0.0018) not (0.0017) even (0.0020) reach (0.0009) his (0.0027) mouth. (-0.0019) nearly (0.0008) seven (-0.0025) metres (0.0024) tall (-0.0026) and (0.0016) thirteen (0.0003) metres (0.0024) long (0.0013) the (-0.0023) tyrannosaurus (0.0029) rex (0.0014) was (-0.0004) probably (0.0013) not (0.0021) a (-0.0026) very (0.0015) skilled (0.0011) hunter (0.0007) but (0.0024) rather (0.0010) a (-0.0019) scavenger (0.0013) which (0.0031) probably (0.0018) fed (0.0012) on (0.0020) the (-0.0021) leavings (0.0021) of (0.0005) other (0.0007) animals. (0.0023) it (0.0012) had (0.0018) more (0.0019) than (0.0003) fifty (0.0026) teeth (0.0011) measuring (0.0022) more (-0.0002) than (0.0009) 15 (0.0025) centimetres (0.0012) in (0.0009) length (0.0029) which (0.0033) it (0.0015) used (0.0020) not (-0.0001) for (0.0013) chewing (0.0026) but (0.0032) rather (0.0020) for (0.0027) tearing (0.0003) since (0.0017) it (0.0021) swallowed (-0.0001) its (-0.0003) food (-0.0006) in (0.0004) large (0.0003) chunks. (-0.0017) to (0.0018) improve (0.0020) depth- (0.0025) perception (0.0000) when (0.0049) searching (0.0019) for (0.0014) food (-0.0011) the (-0.0026) eyes (0.0006) of (0.0013) the (0.0031) tyrannosaurus (0.0025) rex (0.0000) were (-0.0001) oriented (0.0007) toward (-0.0002) the (0.0010) front (0.0010) such (0.0028) that (0.0007) the (0.0002) fields (0.0014) of (0.0002) vision (0.0002) of (0.0014) both (0.0015) eyes (0.0053) overlapped. (-0.0005)
~~~~~~

**Node-1.2** (global 40284):

~~~~~~text
product (-0.0001) from (0.0000) amazon (0.0010) platform (0.0006) with (0.0000) title (0.0003) and (-0.0003) content (-0.0003) : (-0.0001) title (0.0005) : (-0.0004) schleich (0.0001) triceratops (0.0007) figure. (0.0009) content (-0.0002) : (-0.0018) triceratops, (0.0004) although (-0.0001) it (0.0000) looked (0.0003) fierce, (0.0003) fed (0.0003) on (0.0003) plants (0.0001) and (0.0004) trees. (0.0005) for (-0.0001) this (0.0004) reason, (0.0002) it (0.0003) was (0.0003) hunted (-0.0001) by (0.0004) the (0.0003) tyrannosaurus (0.0006) rex. (-0.0002) the (0.0000) front (0.0002) of (0.0000) its (0.0003) jaw (0.0002) formed (0.0003) a (0.0001) beak, (0.0002) similar (0.0003) to (0.0001) that (0.0002) of (0.0002) a (0.0002) parrot, (0.0003) which (0.0002) it (0.0002) used (0.0002) in (0.0001) cutting (0.0002) vegetation. (0.0007) triceratops (0.0003) had (0.0005) three (0.0001) horns (0.0002) made (0.0005) of (0.0003) keratin, (-0.0001) the (-0.0004) same (0.0002) protein (0.0007) that (0.0002) composes (0.0004) fingernails (-0.0003) and (0.0002) hair (0.0007) : (-0.0002) the (-0.0002) horns (0.0002) above (0.0004) its (0.0002) eyes (0.0005) were (0.0002) the (0.0001) longest, (-0.0000) extending (-0.0001) almost (0.0003) three (-0.0001) feet. (-0.0003) since (-0.0001) its (0.0001) head (0.0005) was (0.0001) equal (0.0003) to (0.0003) the (-0.0002) weight (0.0005) of (0.0002) a (-0.0000) small (0.0006) car (0.0007) and (0.0003) approximately (0.0001) one (0.0004) third (0.0005) of (0.0001) its (0.0004) body, (-0.0000) its (0.0002) tail (0.0002) was (0.0002) also (-0.0001) very (0.0001) heavy (0.0001) to (0.0000) keep (-0.0006) its (0.0001) thirty (0.0006) foot (-0.0004) long (0.0004) body (0.0000) balanced. (0.0003) its (0.0001) legs (0.0003) were (-0.0003) very (0.0007) strong, (0.0001) similar (-0.0001) to (0.0002) an (0.0003) elephant (0.0000) ' (0.0001) s (-0.0000) legs (0.0001) today. (-0.0001)
~~~~~~

**Node-1.3** (global 40285):

~~~~~~text
product (0.0033) from (0.0016) amazon (0.0060) platform (-0.0010) with (0.0024) title (-0.0006) and (0.0014) content (0.0000) : (-0.0001) title (0.0047) : (0.0016) safari (0.0013) ltd (-0.0011) carnegie (0.0035) brachiosaurus. (0.0001) content (0.0040) : (0.0012) for (0.0007) over (0.0010) 25 (0.0021) years, (0.0018) safari (-0.0003) ltd (-0.0019) has (0.0011) been (0.0008) proud (-0.0009) to (0.0032) provide (0.0023) this (0.0034) premier (0.0036) line (0.0006) of (0.0016) scale (0.0041) model, (0.0016) dinosaur (0.0024) collectibles. (0.0011) safari (-0.0014) ltd (0.0034) takes (0.0011) pride (0.0015) in (0.0008) providing (0.0017) breathtaking, (0.0028) innovative (0.0036) and (0.0040) value (0.0012) priced (0.0014) figures (0.0010) for (-0.0017) now (0.0035) over (0.0023) 3 (0.0015) generations. (0.0007)
~~~~~~

**Node-1.4** (global 40287):

~~~~~~text
product (-0.0007) from (0.0003) amazon (-0.0007) platform (-0.0004) with (0.0008) title (-0.0001) and (0.0006) content (0.0017) : (0.0003) title (0.0008) : (0.0005) papo (-0.0003) plesiosaurus. (-0.0002) content (0.0008) : (0.0000) papo (0.0000) figures (0.0004) are (0.0000) designed (-0.0003) to (0.0002) inspire (0.0007) creative, (0.0004) imaginative (0.0001) play (0.0001) among (0.0008) children (-0.0003) of (0.0002) all (-0.0001) ages. (0.0001) that (0.0004) ' (0.0000) s (0.0008) why (-0.0007) they (0.0005) create (0.0005) simple (-0.0001) and (0.0004) attractive (0.0005) toys (0.0000) with (0.0001) child (-0.0004) friendly (-0.0001) designs (0.0004) that (0.0003) encourage (0.0006) them (0.0001) to (0.0002) actively (0.0006) use (0.0002) their (0.0001) imagination (0.0002) and (0.0003) develop (0.0007) through (0.0001) active (0.0002) play, (0.0002) stimulation (0.0006) and (0.0007) above (0.0002) all (0.0005) fun. (-0.0003) papo (-0.0000) figurines (0.0007) are (0.0005) hand (0.0001) painted (0.0007) and (0.0009) and (0.0002) include (0.0006) a (-0.0009) wide (0.0001) range (-0.0000) including (0.0008) knights, (-0.0002) animals, (0.0006) pirates, (0.0001) fantasy (-0.0002) as (0.0002) well (0.0004) as (0.0002) many (0.0002) others. (-0.0007) they (-0.0001) are (0.0001) safety (0.0012) tested (0.0001) and (-0.0001) carry (0.0005) appropriate (-0.0004) certification (0.0012) and (-0.0000) box (0.0003) labeling. (0.0021)
~~~~~~

**Node-1.5** (global 40288):

~~~~~~text
product (-0.0001) from (-0.0008) amazon (0.0003) platform (-0.0001) with (-0.0001) title (0.0005) and (0.0002) content (0.0001) : (0.0005) title (0.0004) : (-0.0008) collecta (0.0012) diplodocus (0.0003) dinosaur (-0.0000) toy. (-0.0006) content (0.0011) : (-0.0005) collecta (0.0008) ' (-0.0005) s (-0.0003) replica (-0.0001) of (0.0005) the (-0.0001) diplodocus (-0.0000) is (0.0002) lifelike (0.0001) and (0.0002) detailed, (0.0000) down (0.0002) to (0.0003) the (0.0001) texture (0.0001) of (0.0003) its (0.0003) skin, (0.0003) and (0.0003) the (0.0000) wrinkles (0.0002) on (0.0002) its (0.0002) belly. (-0.0001) its (0.0004) whip- (0.0003) like (0.0003) tail (0.0001) and (0.0006) long (0.0001) neck (-0.0000) have (0.0003) made (0.0003) the (0.0001) diplodocus (0.0000) one (0.0002) of (0.0004) the (-0.0000) most (0.0004) familiar (0.0005) dinosaurs. (-0.0003) the (0.0004) creature (0.0003) lived (0.0003) approximately (0.0003) 155- (0.0002) 148 (0.0002) million (0.0004) years (0.0003) ago, (0.0002) and (0.0003) may (0.0003) have (0.0003) been (0.0002) 177 (0.0002) feet (0.0002) long, (0.0001) and (0.0002) probably (0.0004) weighed (0.0000) 125 (0.0000) short (0.0006) tons. (-0.0009) the (0.0009) diplodocus (0.0000) lived (-0.0001) in (0.0004) the (0.0002) area (0.0002) now (0.0007) made (0.0003) up (0.0005) of (0.0005) colorado, (0.0004) utah, (0.0003) montana (0.0005) and (0.0005) wyoming. (-0.0003) this (0.0005) beautifully (-0.0001) sulpted, (0.0003) collectible (-0.0000) figure (-0.0002) from (0.0003) our (-0.0009) prehistoric (-0.0001) life (0.0003) collection (-0.0006) measurse7. (0.0001) 5 (-0.0000) ' (-0.0002) ' (-0.0001) x (0.0001) 9. (0.0004) 4 (0.0002) ' (-0.0002) ' (-0.0000) h. (0.0001) the (0.0006) carefully (0.0002) sculpted (0.0003) figure (0.0002) has (0.0001) been (0.0002) approved (0.0003) by (0.0005) archeologist (0.0001) anthony (-0.0002) beeson, (0.0001) a (0.0001) well- (0.0002) respected (0.0001) expert (-0.0003) in (0.0000) paleoimagery. (0.0001) all (0.0005) collecta (0.0001) models (0.0003) are (0.0004) individually (0.0001) hand (0.0000) crafted (0.0004) to (0.0000) the (0.0000) highest (0.0001) standards (0.0004) and (0.0001) made (0.0002) with (0.0002) the (0.0001) finest (0.0003) and (0.0001) safest (0.0001) materials, (0.0001) guaranteed (0.0004) to (0.0004) be (0.0003) phthalate- (0.0002) free (0.0002) and (0.0002) lead- (0.0002) free. (-0.0001) create (0.0005) a (0.0002) natural (0.0001) world (0.0002) in (0.0002) miniature (0.0001) with (0.0003) high (0.0002) quality (0.0004) toy (0.0003) replicas (0.0003) from (0.0006) collecta. (0.0000) our (-0.0005) mission (0.0013) is (0.0008) to (0.0001) educate (0.0005) collectors (-0.0001) and (0.0004) to (0.0001) provide (0.0004) the (0.0002) greatest (0.0002) oppportunity (-0.0002) for (-0.0001) creative (0.0004) play. (0.0002)
~~~~~~

**Node-2** (global 9365):

~~~~~~text
product (-0.0106) from (0.0020) amazon (0.0013) platform (-0.0003) with (-0.0076) title (-0.0010) and (0.0017) content (0.0102) : (-0.0028) title (-0.0012) : (-0.0003) walking (-0.0160) with (0.0066) dinosaurs (-0.0278) : (-0.0223) a (-0.0101) reusable (0.0007) sticker (-0.0070) book (0.0023) ( (0.0163) walking (-0.0103) with (0.0078) dinosaurs (-0.0313) the (-0.0133) 3d (-0.0078) movie (0.0017) ). (0.0107) content (0.0001) : (0.0149) based (-0.0065) on (0.0009) the (-0.0319) major (0.0091) motion (-0.0249) picturewalking (-0.0058) with (0.0148) dinosaurs (-0.0303) : (0.0053) the (-0.0156) 3d (-0.0117) movie, (-0.0011) this (0.0046) reusable (-0.0036) sticker (-0.0037) book (-0.0100) is (0.0032) filled (-0.0142) with (0.0008) games, (-0.0044) puzzles, (-0.0053) and (-0.0015) more (-0.0083) than (0.0020) 50 (0.0080) stickers. (-0.0043) it (0.0009) & (0.0394) # (0.0135) 39 (0.0318) ; (0.0084) s (-0.0109) perfect (0.0136) for (0.0042) dinosaur (-0.0337) fans (0.0020) of (0.0055) all (0.0008) ages! (0.0142)
~~~~~~

**Node-2.1** (global 1119):

~~~~~~text
product (-0.0014) from (0.0001) amazon (-0.0003) platform (-0.0020) with (0.0012) title (0.0018) and (-0.0002) content (-0.0015) : (0.0026) title (0.0022) : (0.0010) " (-0.0003) hatch (-0.0012) ' (-0.0004) em (0.0013) ( (0.0016) growing (0.0003) pet (-0.0011) dinosaur (-0.0021) ) (0.0006) ". (0.0022) content (-0.0005) : (0.0019) just (0.0004) place (0.0003) the (-0.0009) egg (0.0005) in (0.0001) water (0.0014) and (0.0008) in (0.0004) 12 (-0.0001) to (0.0006) 24 (0.0002) hours (0.0013) the (0.0011) dinosaur (-0.0018) will (0.0016) start (0.0011) to (0.0005) crack (0.0011) out (0.0006) of (0.0003) its (0.0015) shell. (0.0012) remove (-0.0010) the (-0.0004) shell (0.0003) and (0.0006) put (0.0006) your (0.0006) hatchling (0.0003) into (0.0012) another (0.0013) container (0.0003) of (0.0003) water. (0.0012) your (-0.0005) baby (0.0020) dinosaur (-0.0015) will (0.0016) grow (0.0009) into (0.0010) full (0.0007) grown (0.0006) adult. (0.0001) now (0.0012) you (0.0006) have (0.0019) a (0.0011) virtual (0.0012) pet (-0.0002) that (0.0016) can (0.0007) be (0.0012) nurtured (-0.0001) and (0.0007) raised (0.0008) as (0.0019) your (0.0014) own. (0.0012) mature (0.0017) dinosaur (-0.0038) measure (0.0020) up (0.0012) to (0.0022) 6 (0.0010) inches. (0.0005) they (0.0011) just (0.0010) love (0.0006) dinosaurs! (0.0011) ages (0.0027) 3 (-0.0013) + (0.0021)
~~~~~~

**Node-2.2** (global 10599):

~~~~~~text
product (-0.0005) from (-0.0008) amazon (0.0004) platform (-0.0001) with (0.0003) title (0.0005) and (0.0006) content (0.0002) : (-0.0000) title (0.0003) : (-0.0010) safari (0.0006) ltd (0.0011) wild (0.0006) safari (0.0006) liopleurodon. (0.0006) content (0.0009) : (-0.0008) play (0.0001) is (0.0005) the (-0.0001) essential (0.0009) joy (-0.0001) of (-0.0001) childhood. (-0.0003) through (0.0004) play (0.0001) children (0.0002) learn (0.0000) about (0.0004) themselves, (0.0001) their (0.0005) environment (0.0002) and (0.0006) the (0.0002) larger (0.0006) world. (-0.0006) at (0.0012) safari (0.0002) ltd. (-0.0008) we (0.0002) design (0.0014) toys (-0.0001) that (0.0010) assist (0.0002) the (0.0001) joy (-0.0002) of (0.0002) play. (-0.0008) in (0.0001) a (-0.0002) highly (-0.0003) technical (0.0003) world, (0.0000) the (-0.0002) most (0.0004) endangered (0.0001) species (0.0004) is (0.0006) the (0.0002) imagination. (-0.0007) perhaps (0.0001) we (0.0006) should (0.0008) spell (-0.0002) that (0.0005) with (0.0006) a (0.0001) capital (0.0010) " (0.0023) i (0.0002) ". (0.0002) without (0.0004) imagination, (-0.0003) the (-0.0007) individual (0.0009) loses (-0.0002) the (0.0001) creative (0.0000) spark. (-0.0003) we (0.0002) intend (0.0004) to (0.0008) never (0.0004) let (0.0003) that (0.0004) happen. (0.0006) we (0.0000) hope (0.0001) your (-0.0004) child (0.0004) will (0.0009) enjoy (0.0002) many (0.0002) hours (0.0006) of (-0.0001) creative (0.0006) play (0.0001) with (0.0008) this (0.0001) hand (-0.0001) painted (0.0011) safarilogy (0.0008) dinosaur (-0.0016) liopleurodon. (0.0015)
~~~~~~

**Node-2.3** (global 40320):

~~~~~~text
product (-0.0002) from (0.0014) amazon (0.0002) platform (-0.0002) with (0.0008) title (0.0007) and (0.0006) content (0.0025) : (-0.0001) title (0.0018) : (0.0012) walking (-0.0017) with (0.0006) dinosaurs (-0.0045) ( (0.0017) pack (0.0008) of (0.0003) 3 (-0.0002) ). (0.0020) content (-0.0003) : (0.0015) collect (-0.0003) all (0.0011) your (-0.0012) favourite (0.0003) dinosaurs (-0.0025) from (0.0013) the (-0.0018) latest (0.0007) walking (-0.0003) with (0.0014) dinosaurs (-0.0034) film. (0.0002) this (0.0022) pack (0.0013) includes (0.0018) the (-0.0013) pachyrhinosaurus (-0.0000) characters (0.0003) patchi, (0.0006) scowler (0.0007) and (0.0015) juniper. (-0.0005) each (-0.0010) comes (0.0009) with (0.0003) their (0.0003) own (0.0010) collector (0.0011) fact (0.0021) card. (0.0014) for (0.0000) ages (-0.0010) 4 (0.0023) years (-0.0027) and (0.0015) over. (0.0009)
~~~~~~

**Node-2.4** (global 40321):

~~~~~~text
product (-0.0002) from (-0.0007) amazon (0.0003) platform (-0.0003) with (0.0002) title (-0.0003) and (-0.0005) content (-0.0003) : (-0.0001) title (-0.0002) : (-0.0007) schleich (-0.0001) triceratops. (-0.0006) content (-0.0007) : (-0.0002) schleich (-0.0002) ' (-0.0001) s (-0.0000) triceratops (-0.0003) is (-0.0003) the (-0.0001) perfect (-0.0005) size (-0.0000) for (-0.0003) playing, (-0.0003) although (-0.0004) the (-0.0001) triceratops (-0.0002) looked (-0.0003) menacing (-0.0004) it (-0.0003) fed (-0.0004) on (-0.0002) plants (-0.0004) and (-0.0002) trees. (-0.0003) as (-0.0003) a (0.0000) herbivore (-0.0001) it (-0.0002) was (-0.0004) hunted (-0.0000) by (-0.0002) tyrannosaurus (-0.0001) rex. (-0.0004) the (-0.0001) front (-0.0002) part (-0.0001) of (-0.0003) its (-0.0002) jaw (-0.0002) was (-0.0001) shaped (-0.0002) like (-0.0003) a (-0.0002) parrot (-0.0002) ' (-0.0000) s (-0.0002) beak (-0.0002) which (-0.0001) it (-0.0002) used (-0.0002) to (-0.0001) tear (-0.0005) apart (-0.0002) the (0.0002) plants (-0.0005) it (-0.0003) ate. (0.0003) the (-0.0001) triceratops (-0.0003) had (0.0000) 3 (-0.0005) horns (-0.0003) made (-0.0002) of (-0.0002) keratin (-0.0003) the (-0.0004) same (0.0001) protein (-0.0011) fingernails (-0.0005) and (-0.0005) hair (-0.0003) are (-0.0003) made (-0.0003) of. (0.0003) the (-0.0001) horns (-0.0001) over (-0.0003) its (-0.0002) eyes (-0.0006) were (0.0001) nearly (-0.0004) a (-0.0001) metre (-0.0005) long. (0.0003) because (-0.0003) its (-0.0003) head (-0.0000) weighed (-0.0005) as (-0.0002) much (-0.0001) as (-0.0001) a (0.0000) small (-0.0003) car (-0.0003) and (-0.0002) made (-0.0003) up (-0.0002) almost (0.0000) one (-0.0003) third (-0.0003) of (-0.0002) its (-0.0003) body (-0.0001) it (-0.0002) also (-0.0003) had (-0.0002) a (-0.0002) very (-0.0001) heavy (-0.0005) tail (-0.0003) to (-0.0001) keep (-0.0003) its (-0.0004) ten (-0.0003) metre (-0.0004) long (-0.0002) body (-0.0004) in (-0.0004) balance. (0.0001) its (-0.0005) legs (0.0001) were (-0.0003) very (-0.0000) strong (-0.0000) like (-0.0002) those (-0.0004) of (-0.0004) a (-0.0004) modern (-0.0003) elephant. (-0.0004)
~~~~~~

**Node-2.5** (global 40322):

~~~~~~text
product (-0.0002) from (0.0005) amazon (0.0003) platform (-0.0006) with (0.0007) title (0.0003) and (0.0003) content (0.0013) : (0.0012) title (0.0008) : (0.0003) papo (0.0001) pachyrhinosaurus. (0.0002) content (0.0003) : (-0.0005) papo (0.0005) figures (0.0001) are (0.0003) designed (0.0001) to (0.0002) inspire (0.0010) creative, (0.0007) imaginative (0.0005) play (0.0003) among (0.0008) children (0.0001) of (0.0003) all (0.0002) ages. (0.0002) that (0.0004) ' (-0.0000) s (0.0005) why (0.0002) they (0.0008) create (0.0007) simple (0.0006) and (0.0006) attractive (0.0007) toys (0.0005) with (0.0005) child (0.0003) friendly (0.0003) designs (0.0009) that (0.0004) encourage (0.0008) them (0.0003) to (0.0003) actively (0.0008) use (0.0003) their (0.0003) imagination (0.0004) and (0.0006) develop (0.0012) through (0.0001) active (0.0006) play, (0.0002) stimulation (0.0014) and (0.0006) above (0.0003) all (0.0003) fun. (-0.0001) papo (0.0010) figurines (0.0008) are (0.0008) hand (0.0001) painted (0.0004) and (0.0009) and (0.0004) include (0.0008) a (-0.0019) wide (0.0007) range (0.0006) including (0.0011) knights, (-0.0000) animals, (0.0009) pirates, (0.0006) fantasy (0.0005) as (0.0005) well (0.0005) as (0.0003) many (0.0005) others. (-0.0003) they (0.0014) are (0.0010) safety (0.0018) tested (0.0007) and (0.0007) carry (0.0010) appropriate (0.0006) certification (0.0028) and (0.0005) box (0.0013) labeling. (0.0008)
~~~~~~

**Node-3** (global 9387):

~~~~~~text
product (0.0028) from (0.0175) amazon (-0.0008) platform (-0.0230) with (0.0126) title (0.0081) and (0.0124) content (0.0030) : (0.0111) title (0.0101) : (0.0135) tyrannosaurus (0.0053) rex (0.0166) soft (0.0040) plastic (0.0053) dinosaur (0.0040) ( (0.0170) large (0.0071) ). (-0.0002) content (0.0004) : (0.0092) this (0.0106) large (0.0075) soft (0.0091) plastic (0.0020) tyrannosaurus (0.0040) is (0.0064) 22 (0.0186) " (0.0043) tall. (0.0065) it (0.0100) ' (0.0022) s (0.0099) soft (0.0095) durable (0.0016) plastic (0.0141) construction (0.0126) will (0.0087) provide (0.0068) endless (0.0112) hours (0.0101) of (0.0003) playtime (0.0051) fun! (0.0095)
~~~~~~

**Node-3.1** (global 1121):

~~~~~~text
product (0.0039) from (0.0012) amazon (-0.0000) platform (-0.0000) with (0.0002) title (0.0003) and (0.0008) content (0.0001) : (-0.0010) title (0.0003) : (-0.0015) my (0.0005) big (-0.0013) dinosaur (-0.0008) book. (0.0000) content (0.0003) : (-0.0018) roger (0.0013) priddy (0.0004) left (-0.0011) school (0.0006) at (0.0002) 16 (-0.0005) with (0.0004) just (-0.0004) one (-0.0004) qualification (0.0047) & (-0.0003) # (-0.0001) 8212 (-0.0011) ; (0.0001) in (-0.0012) art. (-0.0004) & (-0.0013) # (-0.0001) 160 (-0.0015) ; (-0.0013) he (0.0008) went (-0.0005) to (-0.0001) berkshire (0.0001) college (0.0003) of (0.0006) art (-0.0012) and (0.0009) design (-0.0003) and (0.0009) trained (-0.0001) as (0.0001) an (0.0008) illustrator. (0.0004) & (0.0005) # (0.0009) 160 (-0.0016) ; (-0.0010) his (-0.0007) first (0.0007) job (0.0004) in (-0.0002) children (-0.0007) & (-0.0002) # (-0.0006) 8217 (0.0005) ; (-0.0029) s (-0.0019) books (0.0014) was (-0.0001) working (-0.0005) with (-0.0002) the (0.0002) publisher (-0.0015) peter (-0.0012) usborne, (0.0003) at (-0.0003) usborne (-0.0006) publishing, (-0.0001) and (0.0005) then (0.0007) he (0.0000) worked (0.0004) with (0.0004) peter (-0.0015) kindersley (-0.0005) at (-0.0007) dorling (-0.0007) kindersley, (0.0002) where (0.0004) he (0.0003) spent (-0.0002) 16 (-0.0006) years. (-0.0004) & (0.0011) # (-0.0006) 160 (0.0023) ; (0.0007) priddy (0.0006) became (-0.0019) creative (-0.0000) director (0.0002) of (-0.0001) dk (-0.0003) & (-0.0001) # (-0.0010) 8217 (0.0002) ; (-0.0017) s (-0.0004) children (-0.0003) & (-0.0003) # (-0.0001) 8217 (0.0004) ; (-0.0018) s (0.0002) division (0.0014) and (-0.0002) was (0.0006) managing (0.0004) director (-0.0013) of (-0.0002) the (0.0007) children (-0.0014) & (-0.0006) # (-0.0001) 8217 (-0.0006) ; (0.0004) s (-0.0022) mass (0.0014) market (0.0016) publisher (-0.0013) funfax (-0.0002) when (-0.0004) it (-0.0002) was (-0.0004) acquired (0.0008) by (-0.0007) dk. (-0.0006) & (0.0006) # (-0.0009) 160 (-0.0006) ; (0.0030) in (-0.0002) 2000, (0.0014) he (0.0000) created (0.0012) priddy (0.0009) books (0.0007) with (0.0002) john (0.0007) sargent (-0.0004) at (-0.0011) st (-0.0012) martin (0.0005) & (0.0002) # (-0.0001) 8217 (0.0003) ; (0.0008) s (-0.0008) press (-0.0008) to (-0.0001) create (-0.0002) innovative (0.0007) and (0.0009) imaginative (0.0007) titles (-0.0005) for (-0.0007) children, (-0.0002) from (-0.0000) first (0.0001) books (-0.0001) for (0.0011) babies (-0.0008) through (-0.0001) early (-0.0001) reference (-0.0001) titles (-0.0005) for (0.0004) older (-0.0001) children. (0.0005) since (0.0001) then, (0.0004) over (-0.0001) 30 (-0.0008) million (-0.0006) copies (-0.0013) of (0.0002) roger (-0.0007) ' (-0.0009) s (-0.0010) 200 (-0.0005) plus (0.0003) books (-0.0006) have (0.0006) sold (-0.0000) worldwide, (-0.0002) with (0.0002) five (-0.0000) of (-0.0002) his (-0.0003) books (-0.0009) & (0.0003) # (-0.0006) 8212 (0.0009) ; (-0.0006) my (-0.0012) big (0.0002) animal, (-0.0014) my (-0.0008) big (-0.0002) truck, (0.0006) happy (-0.0005) baby (-0.0013) words, (-0.0001) happy (-0.0001) baby (-0.0006) colorsandpuppy (-0.0003) and (0.0003) friends (0.0007) & (0.0002) # (-0.0008) 8212 (0.0003) ; (-0.0006) each (-0.0011) selling (-0.0003) over (-0.0005) one (-0.0005) million (-0.0016) copies. (-0.0010) he (0.0004) is (-0.0011) also (0.0001) the (0.0008) author (-0.0022) ofbig (0.0004) board (-0.0001) first (0.0002) 100 (0.0001) words (-0.0006) ; (0.0000) big (-0.0000) board (-0.0011) books (0.0001) colors, (-0.0010) abc, (0.0003) numbers (-0.0016) ; (-0.0011) andbright (0.0011) baby (-0.0004) noisy (-0.0015) monsters. (-0.0011) his (0.0003) creativity (0.0082) has (-0.0005) been (0.0001) recognized (0.0021) with (-0.0009) numerous (-0.0026) industry (0.0017) awards. (-0.0026) priddy (-0.0034) lives (-0.0043) in (-0.0018) london (-0.0009) with (-0.0009) his (0.0009) wife (0.0010) zena (-0.0000) and (-0.0008) their (-0.0013) four (-0.0002) children. (-0.0001)
~~~~~~

**Node-3.2** (global 9385):

~~~~~~text
product (-0.0011) from (-0.0006) amazon (-0.0014) platform (-0.0005) with (-0.0010) title (0.0003) and (0.0003) content (0.0006) : (0.0000) title (-0.0001) : (0.0004) how (-0.0003) do (0.0009) dinosaurs (-0.0003) play (0.0001) with (-0.0002) their (-0.0003) friends?. (-0.0002) content (0.0010) : (-0.0003) praise (0.0004) for (-0.0003) ' (0.0010) how (0.0001) do (-0.0000) dinosaurs (0.0014) say (-0.0003) good (0.0008) night? (-0.0008) ' (0.0013) : (-0.0003) ' (-0.0001) the (-0.0005) message (0.0030) is (0.0005) useful... (0.0003) while (0.0001) the (-0.0002) illustrations (-0.0011) have (0.0002) detail (0.0007) and (-0.0000) characterisation (0.0003) to (0.0002) savour. (-0.0000) ' (0.0024) children (0.0008) ' (0.0003) s (0.0017) book (0.0004) of (-0.0003) the (0.0003) week, (-0.0006) the (-0.0004) sunday (0.0009) times (0.0023) praise (0.0011) for (0.0002) ' (0.0015) how (0.0018) do (0.0007) dinosaurs (-0.0004) get (0.0009) well (0.0002) soon? (-0.0004) ' (0.0012) : (0.0012) ' (0.0006) children (0.0001) will (0.0004) find (0.0022) these (0.0008) poorly (0.0027) dinosaurs (-0.0009) and (-0.0000) their (0.0002) families (-0.0002) really (0.0008) funny... (-0.0004) the (0.0004) full- (0.0004) page (0.0025) illustrations (-0.0020) are (0.0011) fantastic, (0.0009) too. (0.0030) ' (0.0016) bbc (0.0002) parenting (0.0030) ' (-0.0020) this (-0.0000) is (0.0015) an (0.0005) ingenious (0.0018) book (0.0008) that (0.0026) will (0.0002) get (0.0015) your (0.0021) little (0.0015) ones (0.0016) behaving (0.0008) perfectly (0.0019) when (0.0020) they (0.0018) ' (0.0013) re (0.0006) ill. (0.0008) ' (0.0003) baby (0.0003) & (-0.0008) you (0.0011) ' (0.0018) a (0.0001) perfect (0.0004) get- (-0.0006) well (0.0007) book. (0.0020) ' (0.0002) junior (-0.0009) praise (-0.0005) for (-0.0003) ' (-0.0004) how (0.0016) do (0.0016) dinosaurs (-0.0043) eat (0.0008) their (0.0010) food? (0.0003) ' (0.0012) : (0.0019) ' (0.0009) this (-0.0000) combines (-0.0020) an (0.0007) enchanting (0.0006) rhyme (0.0022) with (0.0002) retro- (-0.0000) looking (0.0004) illustrations. (-0.0016) ' (-0.0000) father (0.0001) ' (0.0006) s (0.0027) quarterly-- (0.0007) this (0.0018) text (0.0017) refers (0.0052) to (-0.0009) an (-0.0000) alternateboard (0.0000) bookedition. (0.0003)
~~~~~~

**Node-3.3** (global 40308):

~~~~~~text
product (0.0006) from (-0.0001) amazon (-0.0004) platform (0.0013) with (0.0010) title (0.0019) and (0.0012) content (0.0013) : (0.0016) title (0.0029) : (0.0033) spinosaurus. (0.0019) content (0.0017) : (0.0023) papo (0.0022) dinosaurs (-0.0016) are (0.0019) exquisite. (0.0017) they (0.0013) have (0.0021) articulated (0.0017) jaws (-0.0002) that (-0.0002) show (0.0015) their (0.0012) ferocious (0.0034) teeth. (0.0004) the (-0.0010) spinosaurus (0.0003) is (0.0023) about (0.0013) 6 (0.0040) " (0.0004) tall, (0.0011) with (0.0010) very (0.0021) realistic (0.0020) detailing. (0.0001)
~~~~~~

**Node-3.4** (global 40407):

~~~~~~text
product (-0.0011) from (0.0018) amazon (-0.0001) platform (-0.0010) with (0.0017) title (0.0026) and (0.0003) content (0.0005) : (0.0027) title (0.0024) : (0.0025) realistic (0.0018) triceratops (0.0016) 12 (0.0013) & (0.0016) quot (-0.0005) ; (0.0035) by (0.0022) wild (-0.0004) republic. (-0.0005) content (0.0004) : (0.0036) wild (-0.0009) republic (0.0023) successfully (0.0016) provides (0.0016) a (0.0008) wide (0.0013) range (0.0014) of (0.0010) interactive (0.0026) and (0.0008) innovative (0.0036) toys (-0.0003) that (0.0020) spark (0.0014) the (0.0015) imagination (0.0024) and (0.0011) make (0.0023) learning (0.0020) fun. (0.0002) wild (0.0006) republic (0.0011) has (0.0019) been (0.0018) delighting (0.0016) and (0.0005) educating (0.0017) children (0.0025) with (0.0016) an (0.0012) expansive (0.0039) collection (0.0013) of (0.0004) nature- (0.0011) related (0.0033) toys (-0.0003) and (-0.0007) gifts (0.0038) since (0.0048) 1979 (0.0080) ' (-0.0108)
~~~~~~

**Node-3.5** (global 40408):

~~~~~~text
product (-0.0006) from (-0.0002) amazon (-0.0006) platform (-0.0006) with (0.0002) title (0.0004) and (0.0007) content (-0.0004) : (0.0004) title (0.0000) : (0.0003) schleich (0.0001) velociraptor. (0.0003) content (-0.0000) : (0.0002) schleich (0.0001) ' (0.0002) s (0.0001) velociraptor (0.0003) is (0.0004) the (0.0008) perfect (-0.0005) size (0.0005) for (0.0008) playing, (0.0000) velociraptors (0.0002) were (0.0003) probably (0.0008) very (0.0001) intelligent (-0.0003) dinosaurs (0.0003) who (0.0001) hunted (-0.0002) in (0.0004) packs. (0.0004) although (0.0005) they (0.0002) were (0.0003) only (0.0004) 70 (0.0003) centimetres (-0.0002) tall (0.0006) these (0.0005) carnivores (0.0002) could (-0.0000) overpower (0.0002) significantly (0.0001) larger (0.0001) prey. (0.0003) these (0.0003) dinosaurs (-0.0006) reached (0.0003) speeds (0.0002) of (0.0002) up (0.0005) to (0.0002) 65 (0.0004) km (0.0003) / (0.0003) hour (0.0003) and (0.0005) were (0.0004) able (0.0002) to (0.0002) make (-0.0003) quick (0.0002) turns (0.0003) thanks (0.0001) to (0.0003) their (0.0001) stiff (0.0004) tails. (0.0003) to (0.0004) eat (-0.0001) their (0.0002) prey (0.0009) velociraptors (0.0004) had (0.0004) 80 (0.0001) sharp (0.0004) curved (0.0005) teeth (0.0004) in (0.0004) their (0.0003) flat (0.0006) snout (0.0011) some (0.0002) of (0.0002) which (0.0002) were (0.0003) 2. (0.0007) 5 (0.0001) cm (0.0001) long. (0.0003) velociraptors (0.0004) are (0.0000) thought (-0.0001) to (0.0001) be (0.0003) one (-0.0004) of (-0.0002) the (0.0011) most (0.0006) intelligent (-0.0007) and (0.0003) swiftest (0.0000) dinosaurs. (0.0002) a (-0.0001) cunning (-0.0023) hunter. (-0.0005)
~~~~~~

**Node-3.6** (global 40409):

~~~~~~text
product (0.0018) from (0.0055) amazon (0.0030) platform (-0.0013) with (0.0048) title (0.0063) and (0.0028) content (0.0026) : (0.0036) title (0.0063) : (0.0028) 12 (0.0072) foam (0.0071) dinosaur (-0.0020) masks. (0.0033) content (0.0022) : (0.0028) 12 (0.0040) assorted (0.0046) dino (0.0001) masks (-0.0056) per (0.0139) order (0.0055)
~~~~~~

**Node-4** (global 9392):

~~~~~~text
product (-0.0087) from (0.0173) amazon (0.0078) platform (-0.0029) with (0.0080) title (0.0164) and (0.0077) content (0.0085) : (0.0077) title (0.0239) : (0.0145) ( (0.0041) 24x36 (0.0060) ) (0.0022) dinosaur (0.0052) evolution (-0.0069) educational (0.0026) science (0.0067) chart (0.0184) poster. (0.0038) content (0.0230) : (0.0127) ( (0.0069) 24x36 (0.0045) ) (0.0135) dinosaur (0.0048) evolution (0.0049) educational (0.0031) science (0.0072) chart (0.0083) poster (0.0160)
~~~~~~

**Node-4.1** (global 40425):

~~~~~~text
product (-0.0007) from (-0.0008) amazon (-0.0009) platform (-0.0005) with (-0.0003) title (0.0003) and (0.0003) content (-0.0006) : (0.0008) title (-0.0002) : (-0.0005) dinosaur (0.0031) volcano (0.0018) decorative (-0.0008) outlet (0.0010) cover. (-0.0006) content (0.0018) : (-0.0002) handcrafted (0.0000) to (0.0006) the (-0.0003) highest (0.0004) standards (0.0002) using (0.0007) the (-0.0021) artistry (0.0005) of (0.0009) the (-0.0010) decoupage (0.0004) technique, (0.0007) artwork (0.0014) is (0.0009) triple (0.0006) sealed (0.0006) with (0.0004) a (0.0001) special (0.0005) sealant (-0.0000) to (0.0004) ensure (0.0004) durability, (0.0003) easy (0.0005) cleaning (0.0005) and (0.0004) obtain (-0.0002) an (-0.0001) enamel (0.0012) like (0.0000) finish. (0.0011) artwork (0.0002) will (0.0007) not (0.0002) fade. (0.0006) our (0.0002) switchplates (0.0001) are (0.0010) heavy (0.0003) duty (0.0005) plastic (0.0007) nylon (0.0004) that (0.0003) is (0.0009) virtually (0.0005) unbreakable (0.0003) and (0.0007) hardware (0.0007) is (0.0003) included. (0.0005) a (-0.0004) cinch (0.0000) to (0.0008) install. (0.0005) each (0.0001) one (-0.0000) of (0.0004) our (0.0007) switchplates (0.0000) is (0.0010) handcrafted (0.0006) with (0.0006) great (0.0010) individual (0.0010) care (0.0010) using (0.0003) licensed (0.0010) materials. (0.0004) we (-0.0004) also (0.0015) offer (-0.0004) matching (0.0014) outlet (0.0006) covers, (0.0007) double (0.0010) size (0.0014) switchplates, (0.0009) triple (0.0008) size (0.0008) switchplates, (0.0007) rocker (0.0013) gfi (-0.0002) covers, (-0.0002) combo (0.0008) switchplates, (0.0002) phone (0.0003) and (0.0004) cable (0.0009) covers. (0.0005) we (-0.0000) guarantee (-0.0001) your (-0.0000) complete (0.0006) satisfaction (0.0002) or (0.0004) money (0.0001) back. (0.0001) we (0.0002) are (0.0009) sure (-0.0000) you (0.0003) will (0.0007) be (0.0009) delighted (0.0013) with (0.0003) these (0.0008) unique (0.0004) items. (0.0010) items (0.0004) will (0.0004) arrive (0.0003) via (0.0003) usps (0.0005) and (0.0003) a (0.0005) tracking (0.0014) # (0.0007) will (0.0005) be (0.0001) sent (-0.0002) to (0.0002) you. (0.0005)
~~~~~~

**Node-4.2** (global 40426):

~~~~~~text
product (0.0024) from (0.0003) amazon (-0.0001) platform (0.0003) with (-0.0005) title (0.0016) and (0.0007) content (0.0012) : (-0.0010) title (0.0009) : (0.0005) dinosaurs (-0.0024) and (0.0004) other (0.0005) prehistoric (-0.0005) animals (-0.0005) ( (0.0001) smithsonian (-0.0022) handbooks (-0.0000) ). (-0.0021) content (0.0026) : (0.0008) the (-0.0032) smithsonian (-0.0035) institution (0.0016) is (0.0012) a (0.0013) center (0.0017) for (-0.0008) research (0.0022) dedicated (0.0005) to (0.0007) public (0.0008) education, (0.0006) national (0.0009) service, (0.0009) and (0.0007) scholarship (0.0004) in (0.0004) the (0.0005) arts, (-0.0002) science, (0.0002) and (0.0004) history. (-0.0015)
~~~~~~

**Node-4.3** (global 40427):

~~~~~~text
product (0.0020) from (0.0003) amazon (-0.0003) platform (0.0008) with (0.0003) title (0.0013) and (0.0006) content (-0.0005) : (0.0031) title (-0.0001) : (0.0022) dinosaurs (-0.0007) match (0.0003) me (-0.0007) game. (0.0007) content (0.0010) : (0.0019) award- (0.0015) winning (-0.0001) match (0.0010) me (0.0005) games (0.0012) engage (0.0011) learners (-0.0011) ' (0.0008) matching, (0.0018) memory, (0.0006) and (0.0010) word (0.0012) / (0.0006) picture (0.0004) recognition (0.0001) skills (0.0011) with (0.0013) fun, (0.0009) interactive (0.0015) play. (0.0001) 1 (0.0002) to (0.0015) 8 (-0.0000) players (0.0012) learn (0.0006) about (0.0011) 16 (0.0009) fascinating (0.0012) dinosaurs (0.0015) by (-0.0002) matching (0.0009) realistic (0.0007) illustrations. (0.0017) pronunciation (-0.0005) guide (0.0016) is (0.0011) included. (0.0016) game (0.0018) plays (0.0012) three (0.0003) ways (-0.0016) in (0.0003) an (-0.0020) easy- (0.0005) to- (0.0006) follow (0.0004) format. (-0.0019) two- (0.0019) sided (0.0002) game (0.0037) boards (0.0012) for (0.0002) multiple (0.0028) skill (-0.0014) level (0.0001) play. (0.0017)
~~~~~~

**Node-4.4** (global 40428):

~~~~~~text
product (-0.0010) from (0.0010) amazon (0.0001) platform (-0.0018) with (0.0007) title (0.0008) and (-0.0006) content (-0.0026) : (0.0008) title (0.0009) : (0.0013) famous (0.0000) scientists (0.0026) poster (0.0006) print, (-0.0010) 24x36 (0.0012) poster (0.0009) print, (-0.0008) 24x36. (0.0008) content (-0.0005) : (0.0023) decorate (-0.0008) your (0.0026) home (0.0001) or (0.0016) office (0.0015) with (0.0007) high (0.0011) quality (0.0018) posters. (-0.0007) famous (0.0003) scientists (-0.0002) poster (0.0015) print, (-0.0005) 24x36 (0.0007) is (-0.0004) that (0.0022) perfect (0.0003) piece (0.0017) that (0.0005) matches (-0.0000) your (0.0015) style, (0.0009) interests, (0.0016) and (0.0013) budget. (0.0005)
~~~~~~
