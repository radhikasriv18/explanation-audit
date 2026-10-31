# Reference packet: GraphNarrator__gpt-4o-mini__products__8728

- Method: GraphNarrator; configuration: gpt-4o-mini; dataset: products; target node: 8728
- Explanation source: `./robustness_2026-10-30/graphnarrator_gpt4omini/generated_expls-601/32.json` (messages[assistant])
- Scored scope (what the claims were extracted from): ### Free-Text Explanation section
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

Claims were extracted from the `### Free-Text Explanation` section only; the full assistant message is shown here.

~~~~~~text
### Reasoning

0. **Graph Structure Reconstruction:**

In the provided verbalized graph, the ROOT node (first line) is the target for classification. The single-digit indexed nodes are direct neighbors of ROOT, while the double-digit indexed nodes are:
  - Two hops away from ROOT
  - Direct children of their parent node

Thus, the graph structure of this verbalized graph is:

- ROOT (paradise makeup)
  - Node-1 (barrier spray)
    - Node-1.1 (liquid face paint)
    - Node-1.2 (slim pro pencil)
    - Node-1.3 (barrier spray refill)
    - Node-1.4 (ultrafine setting powder)
    - Node-1.5 (multi-purpose brush set)

1. **Word-Level Evaluation:**

The ROOT node contains keywords such as "makeup" (0.02), "unique" (0.02), "blend" (0.01), and "ingredients" (0.00), which are strongly associated with beauty products. The term "paradise makeup" suggests a cosmetic product, reinforcing its classification in the beauty category. Other terms like "water" (0.00) and "activated" (0.01) are less influential but still contribute to the context of the product.

2. **Graph-Level Aggregation:**

Node-1 (barrier spray) includes keywords like "makeup" (0.00), "protects" (0.00), and "sensitive skin" (0.01), indicating its role in makeup application and maintenance, which is relevant to beauty. The presence of multiple child nodes (Node-1.1 to Node-1.5) further supports the classification:
- Node-1.1 (liquid face paint) emphasizes the cosmetic aspect with terms like "face paint" and "water-based," aligning with beauty products.
- Node-1.2 (slim pro pencil) indicates makeup application tools, reinforcing the beauty context.
- Node-1.3 (barrier spray refill) and Node-1.4 (ultrafine setting powder) highlight products that enhance makeup longevity and finish.
- Node-1.5 (multi-purpose brush set) suggests tools for applying makeup, further solidifying the beauty classification.

### Free-Text Explanation
```markdown
The classification of ROOT into "Beauty" is strongly supported by its own keywords and the co-purchase neighborhood.

ROOT: Keywords like "makeup" (0.02), "unique" (0.02), and "blend" (0.01) clearly identify this product as a cosmetic item, which is central to the beauty category.
  - Node-1: The barrier spray (keywords: "protects" (0.00), "sensitive skin" (0.01)) is designed for makeup application, reinforcing the beauty context.
    - Node-1.1: The liquid face paint (keywords: "face paint") indicates a cosmetic application product, aligning with beauty.
    - Node-1.2: The slim pro pencil is a makeup tool specifically for outlining and drawing, further supporting the beauty classification.
    - Node-1.3: The barrier spray refill continues the theme of makeup maintenance, essential for beauty products.
    - Node-1.4: The ultrafine setting powder (keywords: "setting powder") is crucial for achieving a smooth makeup finish, confirming its beauty relevance.
    - Node-1.5: The multi-purpose brush set is a fundamental tool for makeup application, further affirming the classification.

In summary, ROOT's high-saliency keywords strongly signal its identity as a beauty product, and the entire co-purchase neighborhood consists of makeup items and application tools, providing robust evidence for the "Beauty" category.
```
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/32.json`).

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
<verbalized-graph>ROOT: product(-0.02) amazon(0.01) platform(0.01) title(0.04) content(0.01) title(0.04) missing.(0.01) content(0.03) paradise(-0.01) makeup(0.02) aq(-0.02) semi-(0.02) soft,(0.01) water(0.00) activated,(0.01) moist(-0.00) cake(0.01) makeup.(-0.00) unique(0.02) blend(0.01) ingredients(0.00) includes(0.01) aloe(0.00) chamomile(0.01) help(0.00) make(0.01) paradise(-0.00) makeup(0.02) aq(-0.01) safe(0.01) gentle(0.01) skin.(-0.01) glycerin,(0.00) avocado(0.01) oil(0.00) cocoa(0.00) butter(0.01) provide(0.01) rich,(0.01) vibrant,(0.00) color-(0.01) saturated(-0.00) coverage.(0.01) requires(-0.00) special(0.01) removers(0.00) washes(0.00) easily(0.01) soap(0.00) water.(-0.01) 
Node-1: product(0.01) amazon(-0.01) platform(0.01) title(0.01) content(0.01) title(0.01) mehron(0.00) barrier(0.01) spray(0.00) 2(0.00) oz(0.01) pump(0.01) ).(0.00) content(0.01) mehron(0.00) barrier(0.01) spray(0.00) clear(0.00) liquid(0.01) sets(0.01) makeup(0.00) protects(0.00) sensitive(0.01) skin(0.00) makeup,(0.00) latex(0.00) adhesives.(0.01) apply(0.01) clean(0.01) skin(0.01) makeup(0.01) prevent(0.00) sweat(0.01) coming(0.01) makeup(0.01) spray(0.01) face(0.01) paint(0.01) minimize(0.00) rubbing(0.01) costumes.(0.02) 2(0.00) oz.(0.01) pump(0.01) spray(0.01) bottle.(0.01) sorry,(0.02) air,(0.02) priority(-0.01) international(0.01) shipping(0.01) item.(0.01) 
Node-1.1: product(0.00) amazon(0.00) platform(-0.00) title(-0.00) content(0.00) title(-0.00) mehron(0.00) liquid(-0.00) face(-0.00) paints-(0.00) white(0.00) w(0.00) 4.(-0.00) 5(0.00) oz(0.00) ).(-0.00) content(-0.00) water(0.00) based(-0.00) mehron(0.00) liquid(0.00) face(-0.00) paint(-0.00) used(-0.00) airbrush(0.00) ideal(-0.00) full(-0.00) body(0.00) painting.(-0.00) also(0.00) handy(0.00) face(-0.00) painting(-0.00) crowds(-0.00) faces(0.00) parties,(-0.00) carnivals(-0.00) events.(-0.00) applied(-0.00) brushes,(-0.00) sponges(-0.00) airbrush.(-0.00) made(-0.00) quality(-0.00) fda(-0.00) approved(-0.00) ingredients,(-0.00) mehron(0.00) liquid(-0.00) makeup(0.00) include(-0.00) alcohol,(-0.00) safe(-0.00) gentle(-0.00) skin.(-0.00) water(-0.00) activation(-0.00) liquid(-0.00) face(-0.00) paint(-0.00) move(-0.00) quickly(-0.00) face(-0.00) paint(-0.00) designs.(-0.00) mehron(0.00) liquid(0.00) paint(-0.00) dries(0.00) quickly(-0.00) smooth(0.00) crack(0.00) resistant(0.00) finish.(-0.00) mehron(0.00) liquid(-0.00) makeup(-0.00) also(-0.00) great(-0.00) fx(-0.00) makeup(0.00) mixed(-0.00) liquid(-0.00) latex(0.00) 3d(0.00) gel.(-0.00) 4.(-0.00) 5(-0.00) ounce(0.00) bottle(-0.00) mehron(0.00) liquid(-0.00) face(-0.00) paint(-0.00) bottle(0.00) come(-0.00) applicator(0.00) brush,(0.00) perfect(0.00) refilling(-0.00) smaller(-0.00) bottles(-0.00) really(-0.00) large(0.00) jobs.(-0.00) 
Node-1.2: product(0.00) amazon(-0.00) platform(0.00) title(0.00) content(-0.00) title(0.00) mehron(0.00) slim(0.00) pro-(0.00) pencil(0.00) makeup-(0.00) black.(0.00) content(-0.00) ultra(0.00) soft(0.00) makeup(0.00) pencils(0.00) created(0.00) specifically(0.00) outlining(-0.00) drawing(0.00) face(-0.00) body(0.00) designs.(-0.00) glide(-0.00) easily(0.00) enclosed(0.00) sturdy(-0.00) casing(0.00) peels(-0.00) sharpened.(0.00) best(0.00) used(-0.00) pro(-0.00) pencil(-0.00) sharpener.(-0.00) 
Node-1.3: product(-0.00) amazon(0.00) platform(-0.00) title(0.00) content(0.00) title(0.00) mehron(-0.00) barrier(-0.00) spray(0.00) 9(0.00) oz(-0.00) refill(0.00) bottle.(0.00) content(0.00) clear(0.00) liquid(0.00) sets(-0.00) makeup(-0.00) protects(0.00) sensitive(-0.00) skin(0.00) makeup,(0.00) latex(0.00) adhesives.(0.00) apply(0.00) clean(0.00) skin(0.00) makeup(0.00) prevent(-0.00) sweat(0.00) coming(0.00) makeup(0.00) use(0.00) seal(0.00) makeup(0.00) spray(0.00) powdered(0.00) cream(0.00) grease(0.00) makeup(0.00) water(0.00) based(0.00) makeup(0.00) ).(0.00) prevents(-0.00) makeup(0.00) rubbing(0.00) costumes.(0.00) 9(0.00) oz.(0.00) refill(0.00) bottle.(0.00) 
Node-1.4: product(0.00) amazon(0.00) platform(-0.00) title(0.00) content(0.00) title(0.00) mehron(0.00) ultrafine(0.00) setting(0.00) powder(0.00) 2(-0.00) oz(-0.00) neutral(0.00) translucent(-0.00) ).(0.00) content(0.00) finely(0.00) processed,(-0.00) clump(0.00) free(-0.00) setting(-0.00) powder(0.00) another(0.00) innovation(0.00) mehron(0.00) makeup.(-0.00) retains(0.00) smoothness(0.00) makeup(0.00) available(0.00) traditional(0.00) neutral-(0.00) transparent(0.00) tone(0.00) special(0.00) ultra(0.00) white(0.00) whiteface(0.00) makeup(0.00) used(-0.00) clowns(0.00) mimes.(0.00) mehron(0.00) ultrafine(0.00) setting(0.00) powder(-0.00) comes(0.00) convenient(0.00) shaker(0.00) container(0.00) allows(0.00) maximum(-0.00) control(0.00) quantity(0.00) used(0.00) avoids(0.00) messy(0.00) spills.(0.00) 2(0.00) oz(0.00) shaker(0.00) bottle.(0.00) 
Node-1.5: product(0.00) amazon(0.00) platform(0.00) title(0.00) content(-0.00) title(0.00) pro(-0.00) arte(-0.00) scholar(0.00) multi(-0.00) purpose(-0.00) brush(-0.00) set.(-0.00) content(0.00) 34wa(0.00) all-(-0.00) purpose(0.00) brush(-0.00) set(0.00) supplied(0.00) handy(0.00) pvc(0.00) wallet(0.00) protects(0.00) brushes(0.00) shows(0.00) brushes(0.00) full(0.00) potential(0.00) allowing(0.00) purchsed(0.00) sole(0.00) use(0.00) perfect(0.00) gift(0.00) artist(-0.00) craft(0.00) painter.(0.00) synthetic(-0.00) blended(0.00) white(0.00) nylon(0.00) fibres(0.00) give(0.00) nice(-0.00) springy(0.00) feel(-0.00) allowing(0.00) good(-0.00) color(0.00) flow(0.00) control.(0.00) set(0.00) comprises(-0.00) four(0.00) round(0.00) brushes,(-0.00) flat.(0.00) round(-0.00) brushes(-0.00) sizes(0.00) 2,(-0.00) 4,(0.00) 6(-0.00) 8.(0.00) flat(-0.00) 1(0.00) 2(-0.00) ".(0.00) great(0.00) value,(0.00) budget(0.00) brushes(0.00) perform(0.00) superbly(0.00) well.(0.00) designed(0.00) multi(0.00) purpose(-0.00) tool(-0.00) student,(-0.00) beginner(0.00) craft(0.00) painter(0.00) mind.(0.00) brilliant(0.00) glass(-0.00) painting,(0.00) ceramic(0.00) painting,(0.00) face(0.00) painting,(0.00) mod</verbalized-graph>

### Classification Label
Beauty

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 8728
- Title: missing
- True class (canonical `y`): **label 25**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Beauty**
- Prediction recorded by this method's pipeline: **Beauty**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: missing. Content: Paradise Makeup AQ is a semi-soft, water activated, moist cake makeup. Our unique blend of ingredients includes aloe and chamomile to help make Paradise Makeup AQ safe and gentle to the skin. Glycerin, avocado oil and cocoa butter provide rich, vibrant, color-saturated coverage. It requires no special removers and washes off easily with just soap and water.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 6 nodes

| node id | true class | title |
|---|---|---|
| 1027 | Beauty | Mehron Barrier Spray (2 oz pump) |
| 8776 | label 25 | missing |
| 38123 | Arts, Crafts & Sewing | Snazaroo Face Paint 12ml Face - Body Glitter Gel, Silver |
| 38134 | label 25 | missing |
| 38135 | Toys & Games | Snazaroo High Density Face Painting Sponge (10 Pack) |
| 38136 | Toys & Games | Mehron Liquid Face Paints - Glow In The Dark GL (1 oz) |

### 2-hop (shortest distance exactly 2): 20 nodes

| node id | true class | title |
|---|---|---|
| 78 | Beauty | Mehron CreamBlend Stick Makeup .75 oz (Light Buff) |
| 1032 | Beauty | Mehron Ultrafine Makeup Setting Powder - Neutral/Translucent (0.6 Oz) |
| 8717 | Toys & Games | Mehron Liquid Face Paints - White W (4.5 oz) |
| 8719 | Beauty | Mehron Slim Pro-Pencil Makeup - Black |
| 8723 | Toys & Games | 18ML DARK GREY Classic Snazaroo Classic Face Paint |
| 8726 | Beauty | Mehron Barrier Spray 9 oz Refill Bottle |
| 8727 | All Beauty | Mehron Ultrafine Setting Powder 2 oz (Neutral/Translucent) |
| 8729 | Beauty | Ben Nye Final Seal Matte Makeup Sealer 2oz Spray |
| 8730 | Arts, Crafts & Sewing | Pro Arte Scholar Multi Purpose Brush Set |
| 8731 | Toys & Games | Mehron Liquid Face Paints - Red R (1 oz) |
| 8732 | Health & Personal Care | Maxim Antiperspirant Towelette Antiperspirant Deodorant - Clinical Strength Wipes |
| 8733 | Arts, Crafts & Sewing | Paradise Palette Basic |
| 8734 | Clothing, Shoes & Jewelry | Ben Nye Clown White Makeup (2.25 oz) |
| 8735 | Arts, Crafts & Sewing | Snazaroo Face Paint Stipple Sponge, 2 Pack |
| 8818 | Beauty | Mehron CreamBlend Stick Makeup - Black (0.75 oz) |
| 38287 | Arts, Crafts & Sewing | Petal Sponge 8 PACK Snazaroo Face Painting Sponge |
| 38288 | Arts, Crafts & Sewing | TAG Split Cakes - Berry Wine and Pink (50 gm) |
| 38289 | Books | Fun Face Painting Ideas for Kids: 40 Step-by-Step Demos |
| 38290 | label 25 | missing |
| 38291 | Toys & Games | Mehron Paradise AQ Pro Face Paint Palettes (30 Colors) |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/32.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Beauty**, ground truth = **label 25**.
The verbalized graph is 18929 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 8728 | 73 | 0.0738 | yes |
| Node-1 | 1 | 1027 | 81 | 0.0237 | yes |
| Node-1.1 | 7 | 8717 | 171 | 0.0004 | yes |
| Node-1.2 | 8 | 8719 | 57 | 0.0014 | yes |
| Node-1.3 | 9 | 8726 | 79 | 0.0015 | yes |
| Node-1.4 | 10 | 8727 | 91 | 0.0013 | yes |
| Node-1.5 | 11 | 8730 | 209 | 0.0004 | yes |
| Node-1.6 | 12 | 8733 | 30 | 0.0008 | no |
| Node-1.7 | 13 | 8731 | 153 | 0.0013 | no |
| Node-1.8 | 14 | 8734 | 45 | 0.0010 | no |
| Node-1.9 | 15 | 8735 | 54 | 0.0010 | no |
| Node-2 | 2 | 8776 | 73 | 0.0224 | no |
| Node-2.1 | 16 | 1032 | 78 | 0.0007 | no |
| Node-2.2 | 17 | 38287 | 43 | 0.0007 | no |
| Node-2.3 | 18 | 38288 | 164 | 0.0007 | no |
| Node-2.4 | 19 | 38289 | 201 | 0.0006 | no |
| Node-2.5 | 20 | 38290 | 53 | 0.0012 | no |
| Node-2.6 | 21 | 38291 | 30 | 0.0017 | no |
| Node-3 | 3 | 38123 | 56 | 0.0114 | no |
| Node-3.1 | 22 | 8723 | 163 | 0.0021 | no |
| Node-4 | 4 | 38134 | 45 | 0.0585 | no |
| Node-5 | 5 | 38135 | 144 | 0.0175 | no |
| Node-6 | 6 | 38136 | 97 | 0.0282 | no |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->Node-1.6, Node-1->Node-1.7, Node-1->Node-1.8, Node-1->Node-1.9, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, Node-1.6->Node-1, Node-1.7->Node-1, Node-1.8->Node-1, Node-1.9->Node-1, Node-2->Node-2.1, Node-2->Node-2.2, Node-2->Node-2.3, Node-2->Node-2.4, Node-2->Node-2.5, Node-2->Node-2.6, Node-2->ROOT, Node-2.1->Node-2, Node-2.2->Node-2, Node-2.3->Node-2, Node-2.4->Node-2, Node-2.5->Node-2, Node-2.6->Node-2, Node-3->Node-3.1, Node-3->ROOT, Node-3.1->Node-3, Node-4->ROOT, Node-5->ROOT, Node-6->ROOT, ROOT->Node-1, ROOT->Node-2, ROOT->Node-3, ROOT->Node-4, ROOT->Node-5, ROOT->Node-6

### Tokens and scores

**ROOT** (global 8728):

~~~~~~text
product (-0.0226) from (0.0208) amazon (0.0066) platform (0.0114) with (0.0019) title (0.0424) and (0.0048) content (0.0148) : (0.0609) title (0.0352) : (0.0306) missing. (0.0113) content (0.0307) : (0.0384) paradise (-0.0136) makeup (0.0213) aq (-0.0165) is (0.0162) a (0.0029) semi- (0.0154) soft, (0.0107) water (0.0003) activated, (0.0142) moist (-0.0004) cake (0.0056) makeup. (-0.0023) our (0.0738) unique (0.0238) blend (0.0083) of (0.0019) ingredients (0.0043) includes (0.0062) aloe (0.0017) and (0.0145) chamomile (0.0055) to (0.0030) help (0.0010) make (0.0070) paradise (-0.0027) makeup (0.0197) aq (-0.0081) safe (0.0068) and (0.0131) gentle (0.0123) to (0.0063) the (-0.0106) skin. (-0.0051) glycerin, (0.0029) avocado (0.0067) oil (0.0019) and (0.0076) cocoa (0.0020) butter (0.0089) provide (0.0099) rich, (0.0090) vibrant, (0.0040) color- (0.0122) saturated (-0.0014) coverage. (0.0099) it (0.0207) requires (-0.0001) no (0.0026) special (0.0103) removers (0.0040) and (0.0132) washes (0.0043) off (0.0095) easily (0.0080) with (0.0035) just (0.0208) soap (0.0013) and (0.0095) water. (-0.0090)
~~~~~~

**Node-1** (global 1027):

~~~~~~text
product (0.0055) from (0.0035) amazon (-0.0080) platform (0.0139) with (0.0065) title (0.0120) and (0.0046) content (0.0112) : (0.0051) title (0.0134) : (0.0056) mehron (0.0022) barrier (0.0052) spray (0.0044) ( (0.0057) 2 (0.0043) oz (0.0090) pump (0.0058) ). (0.0048) content (0.0111) : (0.0087) mehron (0.0019) barrier (0.0090) spray (0.0032) is (0.0039) a (0.0051) clear (0.0011) liquid (0.0087) that (0.0070) both (0.0031) sets (0.0065) makeup (0.0043) and (0.0045) protects (0.0038) sensitive (0.0075) skin (0.0040) from (0.0057) makeup, (0.0045) latex (0.0034) and (0.0067) adhesives. (0.0060) apply (0.0072) to (0.0065) clean (0.0099) skin (0.0053) before (0.0044) makeup (0.0059) to (0.0046) prevent (0.0014) sweat (0.0059) from (0.0057) coming (0.0077) through (0.0077) the (-0.0038) makeup (0.0060) or (0.0062) spray (0.0083) over (0.0047) face (0.0054) paint (0.0079) to (0.0084) minimize (0.0038) rubbing (0.0098) off (0.0108) on (0.0132) costumes. (0.0157) 2 (0.0008) oz. (0.0099) pump (0.0085) spray (0.0086) bottle. (0.0090) sorry, (0.0237) no (0.0146) air, (0.0161) priority (-0.0138) or (0.0129) international (0.0128) shipping (0.0122) on (0.0106) this (0.0147) item. (0.0103)
~~~~~~

**Node-1.1** (global 8717):

~~~~~~text
product (0.0001) from (0.0002) amazon (0.0002) platform (-0.0001) with (0.0002) title (-0.0004) and (0.0003) content (0.0001) : (0.0001) title (-0.0004) : (0.0001) mehron (0.0003) liquid (-0.0000) face (-0.0002) paints- (0.0001) white (0.0000) w (0.0001) ( (-0.0000) 4. (-0.0000) 5 (0.0000) oz (0.0004) ). (-0.0000) content (-0.0000) : (0.0001) water (0.0003) based (-0.0004) mehron (0.0001) liquid (0.0000) face (-0.0001) paint (-0.0001) can (0.0003) be (0.0000) used (-0.0000) with (0.0001) an (0.0002) airbrush (0.0002) and (-0.0001) is (-0.0000) ideal (-0.0001) for (-0.0000) full (-0.0000) body (0.0001) painting. (-0.0002) it (-0.0000) is (-0.0001) also (0.0001) handy (0.0000) for (-0.0002) face (-0.0001) painting (-0.0003) crowds (-0.0003) of (-0.0000) faces (0.0001) at (-0.0000) parties, (-0.0002) carnivals (-0.0003) and (0.0001) other (-0.0001) events. (-0.0003) it (-0.0002) can (0.0000) be (-0.0001) applied (-0.0001) with (0.0000) brushes, (-0.0001) sponges (-0.0001) or (-0.0000) an (-0.0000) airbrush. (-0.0001) made (-0.0003) from (-0.0004) quality (-0.0001) fda (-0.0011) approved (-0.0003) ingredients, (-0.0003) mehron (0.0001) liquid (-0.0003) makeup (0.0000) does (-0.0003) not (-0.0000) include (-0.0004) alcohol, (-0.0002) so (-0.0001) it (-0.0002) ' (-0.0001) s (-0.0000) safe (-0.0001) and (-0.0000) gentle (-0.0003) on (0.0000) skin. (-0.0000) there (-0.0001) is (-0.0003) no (-0.0003) water (-0.0001) activation (-0.0001) with (-0.0000) liquid (-0.0003) face (-0.0001) paint (-0.0002) so (-0.0001) you (-0.0004) can (-0.0001) move (-0.0003) quickly (-0.0002) through (-0.0001) your (-0.0004) face (-0.0000) paint (-0.0002) designs. (-0.0004) mehron (0.0002) liquid (0.0003) paint (-0.0000) dries (0.0000) quickly (-0.0001) and (0.0001) has (0.0000) a (0.0001) smooth (0.0000) crack (0.0001) resistant (0.0002) finish. (-0.0002) mehron (0.0000) liquid (-0.0006) makeup (-0.0003) is (-0.0005) also (-0.0001) a (0.0001) great (-0.0003) fx (-0.0001) makeup (0.0003) that (0.0002) can (-0.0000) be (-0.0000) mixed (-0.0002) with (0.0001) liquid (-0.0001) latex (0.0000) or (0.0001) 3d (0.0001) gel. (-0.0000) this (0.0001) 4. (-0.0001) 5 (-0.0001) ounce (0.0002) bottle (-0.0001) of (-0.0001) mehron (0.0000) liquid (-0.0002) face (-0.0000) paint (-0.0002) bottle (0.0001) does (0.0002) not (0.0001) come (-0.0001) with (-0.0001) an (0.0000) applicator (0.0002) brush, (0.0000) but (-0.0002) is (-0.0000) perfect (0.0000) for (-0.0002) refilling (-0.0000) smaller (-0.0000) bottles (-0.0001) or (0.0000) for (0.0001) really (-0.0004) large (0.0002) jobs. (-0.0002)
~~~~~~

**Node-1.2** (global 8719):

~~~~~~text
product (0.0014) from (0.0006) amazon (-0.0001) platform (0.0006) with (0.0004) title (0.0003) and (0.0006) content (-0.0011) : (0.0008) title (0.0008) : (0.0003) mehron (0.0004) slim (0.0005) pro- (0.0007) pencil (0.0002) makeup- (0.0009) black. (0.0004) content (-0.0005) : (0.0000) ultra (0.0006) soft (0.0007) makeup (0.0007) pencils (0.0009) created (0.0005) specifically (0.0001) for (0.0005) outlining (-0.0000) and (0.0004) drawing (0.0004) face (-0.0002) and (0.0001) body (0.0001) designs. (-0.0002) they (0.0006) glide (-0.0002) on (0.0005) easily (0.0005) and (0.0006) are (-0.0000) enclosed (0.0005) in (0.0003) a (0.0003) sturdy (-0.0003) casing (0.0003) that (0.0003) " (-0.0002) peels (-0.0000) off (0.0002) " (0.0001) when (-0.0002) sharpened. (0.0005) best (0.0006) used (-0.0004) with (0.0006) pro (-0.0009) pencil (-0.0001) sharpener. (-0.0005)
~~~~~~

**Node-1.3** (global 8726):

~~~~~~text
product (-0.0003) from (0.0004) amazon (0.0004) platform (-0.0002) with (-0.0008) title (0.0005) and (-0.0002) content (0.0007) : (-0.0003) title (0.0005) : (0.0003) mehron (-0.0002) barrier (-0.0001) spray (0.0002) 9 (0.0014) oz (-0.0008) refill (0.0003) bottle. (0.0005) content (0.0014) : (0.0002) a (0.0003) clear (0.0000) liquid (0.0001) that (0.0005) sets (-0.0002) makeup (-0.0001) and (0.0003) protects (0.0002) sensitive (-0.0001) skin (0.0002) from (0.0004) makeup, (0.0003) latex (0.0001) and (0.0003) adhesives. (0.0003) apply (0.0008) to (0.0004) clean (0.0002) skin (0.0000) before (0.0004) makeup (0.0003) to (0.0003) prevent (-0.0000) sweat (0.0001) from (0.0003) coming (0.0001) through (0.0003) the (-0.0002) makeup (0.0006) or (0.0000) use (0.0002) to (0.0001) seal (0.0002) the (-0.0001) makeup (0.0002) ( (0.0006) spray (0.0007) over (0.0002) powdered (0.0004) cream (0.0002) / (0.0006) grease (0.0003) makeup (0.0004) or (0.0002) water (0.0004) based (0.0006) makeup (0.0004) ). (0.0003) prevents (-0.0001) makeup (0.0003) from (0.0005) rubbing (0.0007) off (0.0000) on (0.0015) costumes. (0.0000) 9 (0.0006) oz. (0.0003) refill (0.0006) bottle. (0.0007)
~~~~~~

**Node-1.4** (global 8727):

~~~~~~text
product (0.0003) from (0.0000) amazon (0.0013) platform (-0.0003) with (-0.0001) title (0.0006) and (-0.0002) content (0.0001) : (0.0008) title (0.0007) : (0.0000) mehron (0.0000) ultrafine (0.0004) setting (0.0003) powder (0.0003) 2 (-0.0004) oz (-0.0006) ( (0.0005) neutral (0.0004) / (0.0002) translucent (-0.0002) ). (0.0003) content (0.0006) : (-0.0003) this (0.0004) finely (0.0001) processed, (-0.0000) clump (0.0001) free (-0.0003) setting (-0.0010) powder (0.0000) is (0.0003) another (0.0008) innovation (0.0001) from (0.0002) mehron (0.0002) makeup. (-0.0000) it (0.0001) retains (0.0004) the (-0.0001) smoothness (0.0003) of (0.0001) your (0.0003) makeup (0.0006) and (0.0001) is (0.0005) available (0.0001) in (0.0001) a (0.0003) traditional (0.0005) neutral- (0.0003) transparent (0.0004) tone (0.0001) or (0.0003) a (0.0001) special (0.0002) ultra (0.0003) white (0.0002) for (0.0002) whiteface (0.0003) makeup (0.0006) used (-0.0000) by (0.0005) clowns (0.0007) and (0.0002) mimes. (0.0000) mehron (0.0004) ultrafine (0.0002) setting (0.0004) powder (-0.0002) comes (0.0008) in (0.0002) a (-0.0001) convenient (0.0003) shaker (0.0003) container (0.0004) that (0.0003) allows (0.0002) maximum (-0.0000) control (0.0001) of (0.0003) quantity (0.0000) used (0.0005) and (0.0002) avoids (0.0006) messy (0.0008) spills. (0.0005) 2 (0.0000) oz (0.0003) shaker (0.0001) bottle. (0.0001)
~~~~~~

**Node-1.5** (global 8730):

~~~~~~text
product (0.0002) from (0.0000) amazon (0.0000) platform (0.0001) with (0.0001) title (0.0001) and (0.0001) content (-0.0000) : (0.0001) title (0.0001) : (0.0001) pro (-0.0001) arte (-0.0000) scholar (0.0001) multi (-0.0001) purpose (-0.0000) brush (-0.0000) set. (-0.0000) content (0.0000) : (0.0001) the (-0.0000) 34wa (0.0001) all- (-0.0000) purpose (0.0000) brush (-0.0000) set (0.0000) is (0.0000) supplied (0.0001) in (-0.0000) a (0.0000) handy (0.0002) pvc (0.0000) wallet (0.0000) which (0.0001) protects (0.0000) the (0.0001) brushes (0.0001) and (0.0001) shows (0.0001) the (0.0000) brushes (0.0000) to (0.0000) their (0.0000) full (0.0000) potential (0.0000) allowing (0.0000) them (0.0000) to (0.0000) be (0.0000) purchsed (0.0001) for (0.0000) sole (0.0001) use (0.0000) or (0.0001) as (0.0000) the (0.0001) perfect (0.0001) gift (0.0000) for (0.0000) any (0.0001) artist (-0.0001) or (0.0001) craft (0.0001) painter. (0.0002) the (0.0001) synthetic (-0.0001) blended (0.0000) white (0.0000) nylon (0.0000) fibres (0.0000) give (0.0000) a (-0.0001) nice (-0.0000) springy (0.0000) feel (-0.0000) allowing (0.0001) good (-0.0001) color (0.0000) flow (0.0002) and (-0.0001) control. (0.0001) the (-0.0001) set (0.0001) comprises (-0.0001) of (-0.0000) four (0.0000) round (0.0000) brushes, (-0.0001) and (0.0002) a (-0.0001) flat. (0.0003) the (-0.0002) round (-0.0000) brushes (-0.0002) are (0.0000) sizes (0.0001) 2, (-0.0000) 4, (0.0001) 6 (-0.0000) & (0.0001) 8. (0.0001) the (0.0000) flat (-0.0001) is (-0.0000) 1 (0.0000) / (0.0000) 2 (-0.0000) ". (0.0003) these (-0.0001) are (-0.0000) great (0.0000) value, (0.0002) budget (0.0000) brushes (0.0000) that (0.0001) will (0.0000) perform (0.0000) superbly (0.0000) well. (0.0001) it (0.0000) was (0.0001) designed (0.0000) as (-0.0000) a (0.0000) multi (0.0001) purpose (-0.0001) tool (-0.0001) with (0.0000) the (-0.0001) student, (-0.0001) beginner (0.0000) and (0.0000) craft (0.0000) painter (0.0001) in (0.0001) mind. (0.0000) brilliant (0.0001) for (-0.0000) glass (-0.0000) painting, (0.0000) ceramic (0.0000) painting, (0.0000) face (0.0001) painting, (0.0000) model (-0.0000) painting (0.0000) or (0.0001) general (0.0000) artistic (0.0000) work. (0.0000) watercolor, (0.0001) acrylic, (0.0000) enamel (-0.0000) etc. (-0.0001) thank (0.0003) you (0.0001) for (-0.0000) looking (0.0001) at (0.0001) this (0.0000) great (-0.0001) pro (-0.0000) arte (0.0001) product. (-0.0000) if (0.0002) you (-0.0000) want (-0.0000) to (0.0000) see (0.0000) more (0.0000) by (-0.0000) this (0.0001) great (0.0000) british (0.0001) brush (-0.0000) manufacturer (0.0004) then (0.0001) click (0.0001) the (-0.0000) " (-0.0001) supplier (0.0000) " (0.0001) link (0.0000) to (0.0000) see (-0.0000) the (-0.0001) full (-0.0000) range (0.0000) that (0.0000) we (0.0000) currently (0.0000) stock. (0.0000) if (0.0001) you (-0.0002) dont (-0.0001) find (-0.0000) exactly (0.0001) what (0.0000) you (-0.0001) want, (-0.0000) keep (0.0000) looking (-0.0001) as (0.0001) we (-0.0001) are (-0.0001) always (0.0000) adding (-0.0001) new (-0.0002) products! (0.0004)
~~~~~~

**Node-1.6** (global 8733):

~~~~~~text
product (-0.0013) from (0.0008) amazon (0.0007) platform (0.0002) with (0.0001) title (-0.0002) and (-0.0002) content (-0.0000) : (-0.0001) title (-0.0002) : (-0.0002) paradise (0.0007) palette (-0.0002) basic. (0.0001) content (0.0003) : (-0.0002) 8 (-0.0001) colors (-0.0001) basic (-0.0000) palette (-0.0003) 56grams (0.0003) water (0.0007) soluble, (0.0001) color (0.0000) saturated, (0.0001) semi (-0.0001) soft, (0.0001) moist (-0.0001) cake (-0.0004) makeup. (0.0003)
~~~~~~

**Node-1.7** (global 8731):

~~~~~~text
product (0.0001) from (0.0000) amazon (-0.0000) platform (-0.0001) with (-0.0001) title (0.0001) and (0.0001) content (0.0000) : (0.0002) title (0.0004) : (-0.0001) mehron (0.0001) liquid (0.0002) face (0.0000) paints- (0.0000) red (0.0000) r (0.0000) ( (-0.0000) 1 (-0.0001) oz (-0.0000) ). (-0.0004) content (0.0004) : (-0.0003) water (-0.0001) based (0.0002) mehron (-0.0000) liquid (0.0001) face (-0.0001) paint (-0.0000) can (-0.0001) be (0.0001) used (0.0001) with (0.0001) an (0.0001) airbrush (-0.0002) and (0.0001) is (0.0003) ideal (0.0002) for (0.0000) full (-0.0000) body (0.0001) painting. (-0.0001) it (0.0002) is (0.0002) also (0.0000) handy (0.0003) for (-0.0001) face (0.0000) painting (0.0000) crowds (0.0000) of (-0.0001) faces (0.0001) at (0.0002) parties, (-0.0001) carnivals (0.0001) and (0.0002) other (0.0001) events. (0.0001) it (0.0002) can (0.0001) be (0.0002) applied (0.0001) with (0.0002) brushes, (0.0001) sponges (0.0001) or (0.0002) an (0.0001) airbrush. (-0.0000) made (0.0002) from (0.0003) quality (0.0001) fda (0.0013) approved (-0.0002) ingredients, (0.0001) mehron (0.0000) liquid (0.0001) makeup (0.0000) does (0.0002) not (0.0001) include (0.0002) alcohol, (0.0001) so (0.0001) it (0.0002) ' (0.0001) s (0.0002) safe (0.0001) and (0.0002) gentle (0.0004) on (0.0002) skin. (0.0001) there (0.0002) is (0.0004) no (0.0003) water (0.0003) activation (0.0003) with (0.0002) liquid (0.0004) face (0.0002) paint (0.0001) so (0.0004) you (0.0003) can (0.0003) move (0.0003) quickly (0.0002) through (0.0003) your (0.0005) face (0.0001) paint (0.0002) designs. (0.0001) mehron (-0.0001) liquid (-0.0001) paint (0.0001) dries (0.0001) quickly (-0.0002) and (0.0001) has (0.0001) a (0.0002) smooth (0.0002) crack (0.0001) resistant (-0.0000) finish. (-0.0000) mehron (-0.0001) liquid (0.0002) makeup (0.0002) is (0.0003) also (0.0001) a (0.0000) great (0.0002) fx (0.0004) makeup (-0.0004) that (0.0004) can (0.0001) be (0.0002) mixed (0.0000) with (0.0000) liquid (0.0003) latex (0.0001) or (0.0003) 3d (0.0000) gel. (0.0000) the (0.0001) 1 (0.0002) ounce (-0.0001) mehron (-0.0002) liquid (0.0003) face (-0.0001) paint (-0.0001) bottle (0.0002) comes (0.0000) with (-0.0000) an (0.0000) applicator (0.0001) brush. (-0.0001)
~~~~~~

**Node-1.8** (global 8734):

~~~~~~text
product (-0.0011) from (0.0001) amazon (0.0004) platform (-0.0005) with (0.0005) title (0.0004) and (-0.0002) content (-0.0002) : (-0.0001) title (0.0006) : (0.0003) ben (0.0005) nye (-0.0002) clown (0.0002) white (-0.0009) makeup (-0.0008) ( (-0.0002) 2. (0.0006) 25 (0.0002) oz (-0.0007) ). (0.0007) content (0.0003) : (0.0005) clown (0.0007) makeup (-0.0005) available (-0.0000) in (0.0003) three (-0.0004) sizes (0.0003) 2. (0.0005) 5 (0.0000) oz, (0.0002) 8 (0.0007) oz (-0.0001) and (0.0001) 16 (-0.0002) oz (0.0004) white (-0.0006) creme (0.0010) / (0.0003) grease (-0.0015) paint (-0.0006) gentle (-0.0005) on (-0.0019) skin (0.0005)
~~~~~~

**Node-1.9** (global 8735):

~~~~~~text
product (0.0010) from (0.0003) amazon (0.0003) platform (0.0002) with (0.0004) title (0.0000) and (0.0002) content (-0.0001) : (0.0005) title (-0.0002) : (0.0003) snazaroo (0.0002) face (0.0001) paint (0.0003) stipple (0.0002) sponge, (-0.0002) 2 (0.0002) pack. (-0.0005) content (0.0007) : (0.0004) snazaroo (0.0000) offers (0.0001) the (0.0001) world (0.0004) ' (0.0003) s (0.0001) safest (0.0003) and (0.0002) easiest (-0.0000) to (0.0002) use (0.0004) face (0.0003) paints! (-0.0001) the (-0.0005) products (0.0002) are (0.0000) water- (0.0003) based, (0.0002) dry (-0.0001) to (0.0001) the (0.0002) touch (0.0002) in (0.0001) one (0.0002) minute (0.0000) and (0.0003) wash (0.0004) off (0.0000) easily (0.0000) with (-0.0002) mild (0.0000) soap (-0.0000) and (0.0001) water. (-0.0003)
~~~~~~

**Node-2** (global 8776):

~~~~~~text
product (-0.0005) from (0.0051) amazon (0.0044) platform (0.0015) with (0.0033) title (0.0118) and (-0.0007) content (0.0019) : (0.0169) title (0.0077) : (0.0066) missing. (0.0038) content (0.0076) : (0.0098) paradise (-0.0020) makeup (0.0031) aq (-0.0037) is (0.0013) a (0.0010) semi- (0.0020) soft, (0.0024) water (-0.0002) activated, (0.0029) moist (0.0065) cake (0.0104) makeup. (-0.0012) our (0.0224) unique (0.0067) blend (0.0043) of (-0.0005) ingredients (0.0052) includes (-0.0004) aloe (0.0008) and (0.0020) chamomile (0.0009) to (-0.0009) help (-0.0010) make (0.0016) paradise (0.0001) makeup (0.0057) aq (-0.0001) safe (0.0021) and (0.0024) gentle (0.0032) to (-0.0001) the (-0.0005) skin. (-0.0011) glycerin, (0.0002) avocado (0.0010) oil (0.0013) and (0.0016) cocoa (-0.0011) butter (0.0030) provide (0.0013) rich, (0.0006) vibrant, (-0.0002) color- (0.0019) saturated (0.0006) coverage. (0.0020) it (0.0008) requires (-0.0004) no (-0.0003) special (0.0019) removers (-0.0001) and (0.0003) washes (0.0003) off (-0.0003) easily (0.0023) with (-0.0022) just (0.0020) soap (0.0017) and (0.0008) water. (-0.0021)
~~~~~~

**Node-2.1** (global 1032):

~~~~~~text
product (-0.0005) from (0.0005) amazon (0.0001) platform (-0.0000) with (0.0002) title (0.0007) and (0.0001) content (0.0000) : (0.0004) title (0.0005) : (0.0003) mehron (-0.0001) ultrafine (-0.0001) makeup (-0.0001) setting (-0.0006) powder- (0.0001) neutral (-0.0001) / (0.0001) translucent (0.0001) ( (0.0003) 0. (0.0000) 6 (-0.0001) oz (-0.0003) ). (0.0001) content (0.0003) : (0.0003) mehron (-0.0000) ultrafine (0.0001) neutral (0.0002) setting (0.0001) powder (-0.0002) can (0.0000) be (-0.0001) used (0.0002) to (0.0000) set (0.0001) all (0.0002) colors (0.0002) of (0.0001) grease (0.0003) or (0.0002) cream (-0.0002) makeup (0.0002) and (0.0002) includes (-0.0001) an (0.0000) antiperspirant (0.0002) for (0.0006) stage (0.0004) performers. (-0.0003) mehron (-0.0001) neutral (-0.0003) setting (-0.0002) powder (-0.0002) is (0.0000) very (0.0001) fine (0.0000) and (-0.0000) clump (0.0000) free (-0.0001) and (0.0002) comes (-0.0002) in (0.0001) a (-0.0002) handy (0.0001) shaker (-0.0002) container (0.0002) to (0.0000) minimize (0.0001) mess (-0.0002) and (0.0001) control (0.0004) dispersal. (-0.0001) 0. (0.0002) 6 (0.0002) ounce (0.0001) shaker (0.0000) bottle. (0.0005)
~~~~~~

**Node-2.2** (global 38287):

~~~~~~text
product (-0.0000) from (0.0001) amazon (0.0001) platform (0.0004) with (-0.0001) title (0.0001) and (-0.0003) content (0.0006) : (-0.0005) title (0.0005) : (-0.0001) petal (0.0001) sponge (0.0002) 8 (-0.0000) pack (-0.0001) snazaroo (-0.0002) face (-0.0004) painting (-0.0001) sponge. (0.0002) content (0.0004) : (-0.0004) use (-0.0002) one (-0.0001) sponge (0.0007) per (-0.0002) color. (0.0001) with (0.0002) this (0.0002) set (0.0001) you (0.0002) get (-0.0003) all (-0.0001) 8 (0.0001) colors (-0.0001) white, (-0.0001) black, (0.0001) red, (0.0000) blue, (-0.0000) yellow, (0.0000) green, (-0.0000) orange (-0.0001) and (-0.0002) pink. (-0.0001)
~~~~~~

**Node-2.3** (global 38288):

~~~~~~text
product (-0.0005) from (0.0000) amazon (-0.0001) platform (-0.0004) with (0.0003) title (0.0003) and (0.0003) content (-0.0000) : (0.0002) title (0.0004) : (0.0002) tag (0.0003) split (0.0003) cakes- (0.0005) berry (-0.0001) wine (0.0002) and (0.0006) pink (0.0004) ( (0.0003) 50 (0.0003) gm (-0.0001) ). (0.0004) content (0.0001) : (0.0002) tag (0.0003) combines (-0.0001) berry (-0.0000) wine (-0.0000) and (0.0007) pink (0.0000) face (0.0003) paint (0.0004) to (0.0002) create (0.0000) this (0.0005) exciting (0.0001) tag (0.0001) split (0.0007) cake. (-0.0013) the (0.0003) colors (0.0004) can (0.0002) be (0.0003) used (0.0002) individually (0.0001) or (0.0004) together (-0.0001) to (0.0002) create (-0.0002) exciting (-0.0006) face (0.0001) paint (-0.0000) designs. (-0.0011) tag (0.0001) face (-0.0000) paint (-0.0000) is (0.0001) very (0.0004) easy (0.0002) to (0.0002) blend, (0.0001) soft (0.0002) on (0.0001) the (-0.0002) skin (0.0002) and (0.0003) does (0.0002) not (0.0002) crack (0.0002) or (0.0002) peel. (-0.0001) most (0.0004) of (0.0003) tags (-0.0003) face (0.0003) painting (-0.0003) colors (0.0002) are (0.0004) great (-0.0000) for (0.0006) line (0.0000) work (0.0002) and (0.0005) lighter (0.0003) face (0.0003) painting (0.0001) colors (0.0002) show (0.0003) very (0.0004) well (0.0004) even (0.0003) when (0.0002) over (0.0004) darker (0.0001) colors. (0.0002) tag (0.0004) facepaint (0.0002) has (0.0006) a (0.0002) wax (0.0003) base, (0.0001) so (0.0005) your (0.0005) face (0.0005) painting (0.0000) design (0.0003) flexes (0.0002) with (0.0005) movement (0.0003) instead (0.0003) of (0.0002) cracking, (0.0001) remains (0.0002) colorful (0.0003) and (0.0006) is (0.0006) comfortable (0.0004) to (0.0001) wear. (0.0003) tag (-0.0002) is (0.0003) a (0.0001) very (0.0001) soft (0.0002) creamy (0.0003) face (-0.0000) paint (0.0001) and (0.0003) needs (-0.0000) less (0.0004) water (0.0003) to (0.0004) activate (-0.0001) than (0.0004) normal (0.0001) face (0.0001) paint. (0.0001) tag (0.0006) face (0.0003) paint (0.0004) is (-0.0002) hypoallergenic (0.0002) and (0.0005) made (0.0003) with (0.0003) non- (0.0004) toxic, (0.0001) skin (0.0003) safe (0.0003) ingredients. (0.0001) each (0.0005) 2 (0.0002) color (0.0004) 50 (0.0004) gram (0.0003) tag (0.0003) split (0.0002) cake (0.0002) is (0.0005) good (0.0001) for (0.0000) 100- (0.0005) 250 (0.0004) applications. (0.0000)
~~~~~~

**Node-2.4** (global 38289):

~~~~~~text
product (-0.0000) from (-0.0001) amazon (0.0000) platform (-0.0004) with (-0.0000) title (0.0002) and (-0.0000) content (0.0002) : (0.0002) title (0.0000) : (-0.0001) fun (0.0002) face (-0.0000) painting (0.0000) ideas (0.0002) for (0.0001) kids (0.0002) : (0.0002) 40 (0.0000) step- (0.0002) by- (0.0001) step (0.0001) demos. (-0.0002) content (0.0004) : (0.0001) award- (0.0003) winning, (0.0001) world- (0.0001) renowned (0.0003) artists (-0.0003) / (0.0002) instructors (-0.0002) andextreme (0.0000) face (-0.0000) paintingauthorsbrian (0.0001) and (0.0001) nick (0.0006) wolfeare (0.0000) known (-0.0000) for (0.0001) their (0.0005) fast- (0.0003) paced (-0.0001) face (-0.0005) and (0.0002) body (-0.0002) art (0.0001) techniques. (-0.0010) after (0.0004) contributing (0.0003) to (-0.0000) face- (0.0001) painting (-0.0001) publications, (0.0001) teaching (0.0002) classes (0.0001) and (0.0001) attending (0.0001) conventions, (0.0004) the (0.0001) twins (-0.0006) were (0.0001) offered (0.0001) an (0.0000) endorsement (0.0004) deal (0.0002) with (0.0001) a (0.0000) marketing (0.0006) and (0.0002) development (0.0003) company, (0.0001) and (0.0002) wolfe (0.0000) brothers (-0.0001) face (0.0001) art (0.0001) & (0.0004) fx (0.0004) was (0.0003) born. (0.0003) nick (0.0003) and (0.0004) brian (-0.0001) worked (0.0003) with (0.0001) them (-0.0001) for (0.0002) 4 (-0.0001) years, (-0.0001) flying (0.0002) around (0.0000) the (-0.0000) world, (0.0000) sharing (0.0002) their (0.0003) techniques (-0.0002) and (0.0001) products, (0.0000) and (0.0002) employing (0.0001) some (0.0001) of (0.0000) the (-0.0000) finest (-0.0001) artists (0.0001) in (-0.0000) the (-0.0001) industry. (0.0001) brian (0.0003) won (-0.0001) first (-0.0001) prize (-0.0001) at (-0.0000) the (-0.0001) asian (-0.0004) world (-0.0001) body (-0.0002) painting (0.0000) festival (0.0001) 2008, (0.0001) and (-0.0001) the (-0.0002) twins (-0.0008) took (0.0000) second (-0.0001) at (0.0003) the (-0.0000) face (0.0002) and (0.0000) body (-0.0000) art (-0.0000) painting (-0.0001) convention (-0.0000) 2007. (0.0001) they (0.0002) are (-0.0002) members (0.0002) of (0.0001) the (0.0000) face (0.0001) painting (0.0001) and (0.0001) body (-0.0000) art (0.0001) association, (0.0000) with (0.0001) over (0.0002) 900 (0.0000) members (0.0001) throughout (0.0001) the (0.0000) world. (-0.0002) they (0.0004) also (0.0001) won (0.0003) first (-0.0000) place (0.0001) at (0.0001) the (0.0000) world (0.0000) bodypainting (0.0000) festival (0.0001) for (0.0000) the (0.0000) world (0.0001) bodypainting (0.0000) award (0.0004) championship (0.0001) in (0.0001) seeboden, (0.0000) austria (-0.0001) in (0.0000) 2009 (0.0001) ; (0.0003) and (0.0003) brian (-0.0001) won (0.0003) first (0.0000) place (0.0000) in (0.0001) 2011 (-0.0000) at (0.0001) the (-0.0001) world (0.0002) bodypainting (-0.0000) festival (0.0001) in (0.0000) portschach, (0.0001) austria. (-0.0002) visit (0.0003) their (-0.0001) website (0.0000) at (-0.0001) http (0.0003) : (0.0001) / (-0.0001) / (-0.0000) www. (0.0002) eviltwinfx. (-0.0000) com. (0.0000)
~~~~~~

**Node-2.5** (global 38290):

~~~~~~text
product (-0.0007) from (0.0005) amazon (-0.0001) platform (-0.0003) with (0.0003) title (-0.0001) and (0.0001) content (-0.0002) : (0.0005) title (0.0001) : (0.0002) missing. (0.0007) content (-0.0004) : (0.0004) our (0.0007) glitters (0.0000) are (0.0010) great (-0.0001) for (-0.0004) that (0.0006) extra (0.0002) shimmering (0.0005) effect (0.0004) on (0.0003) all (0.0002) your (0.0012) designs. (0.0005) the (-0.0004) glitters (0.0005) are (0.0001) polyester, (-0.0001) octagon (-0.0002) cut, (0.0000) high (-0.0001) quality (-0.0001) cosmetic (0.0005) glitter. (0.0001) because (-0.0000) of (-0.0002) this (0.0002) they (-0.0002) are (0.0006) safe (0.0004) for (0.0000) usage (0.0003) on (-0.0002) the (0.0003) face (0.0002) and (-0.0001) even (0.0005) around (0.0000) the (0.0005) eyes. (-0.0000)
~~~~~~

**Node-2.6** (global 38291):

~~~~~~text
product (-0.0005) from (0.0010) amazon (0.0004) platform (0.0007) with (0.0004) title (-0.0006) and (-0.0001) content (0.0009) : (-0.0014) title (0.0000) : (0.0000) mehron (-0.0001) paradise (0.0000) aq (-0.0005) pro (0.0005) face (0.0002) paint (0.0007) palettes (0.0005) ( (0.0001) 30 (-0.0001) colors (0.0000) ). (0.0008) content (0.0017) : (-0.0004) 7 (0.0001) gram (0.0002) palette (0.0001) sized (0.0004) color (-0.0000) refill (0.0002)
~~~~~~

**Node-3** (global 38123):

~~~~~~text
product (0.0057) from (0.0058) amazon (0.0114) platform (0.0107) with (0.0058) title (0.0067) and (0.0047) content (0.0073) : (0.0071) title (0.0077) : (0.0068) snazaroo (0.0049) face (0.0020) paint (0.0027) 12ml (0.0048) face- (0.0062) body (0.0065) glitter (0.0045) gel, (0.0048) silver. (0.0038) content (0.0061) : (0.0092) snazaroo (0.0036) offers (0.0048) the (0.0014) world (0.0033) ' (0.0046) s (0.0020) safest (0.0049) and (0.0071) easiest (0.0021) to (0.0035) use (0.0056) face (0.0037) paints! (0.0038) the (-0.0000) products (0.0060) are (0.0020) water- (0.0048) based, (0.0056) dry (0.0014) to (0.0029) the (0.0030) touch (0.0034) in (0.0043) one (0.0060) minute (0.0012) and (0.0062) wash (0.0064) off (0.0050) easily (0.0053) with (0.0034) mild (0.0056) soap (0.0044) and (0.0059) water. (0.0005)
~~~~~~

**Node-3.1** (global 8723):

~~~~~~text
product (-0.0010) from (0.0001) amazon (0.0002) platform (-0.0007) with (-0.0002) title (0.0007) and (0.0001) content (0.0002) : (0.0005) title (0.0008) : (-0.0002) 18ml (0.0006) dark (0.0006) grey (-0.0001) classic (0.0004) snazaroo (0.0006) classic (0.0002) face (0.0001) paint. (0.0003) content (0.0006) : (-0.0009) face (0.0004) painting (0.0016) is (0.0000) becoming (0.0007) more (0.0001) and (-0.0000) more (0.0005) a (0.0006) standard (0.0012) feature (0.0008) at (0.0001) parties, (0.0008) halloween, (-0.0003) holidays, (0.0005) sports, (0.0005) fund (-0.0002) raisers (0.0007) and (0.0011) the (0.0000) amusement (0.0011) world. (0.0002) almost (0.0006) everywhere, (0.0006) children (0.0009) are (0.0007) having (0.0007) a (0.0003) great (0.0005) time (0.0001) getting (-0.0007) their (0.0003) faces (0.0019) painted- (0.0009) adults (0.0002) too! (-0.0016) snazaroo (0.0006) has (0.0011) the (0.0005) largest (0.0002) range (-0.0001) of (0.0008) colors (0.0009) in (0.0006) the (-0.0004) industry (0.0020) with (-0.0001) 65 (0.0002) colors (0.0010) to (-0.0005) choose (0.0012) from (0.0008) : (0.0010) 38 (-0.0005) classic (-0.0002) colors, (0.0004) 12 (0.0004) sparkle (0.0006) colors, (0.0002) 7 (0.0003) metallic (0.0015) and (0.0006) electric (0.0007) colors (0.0013) and (0.0004) 8 (-0.0000) uv (0.0002) black (0.0004) light (0.0013) colors (0.0009) snazaroo (0.0014) is (0.0009) the (-0.0002) world (0.0016) ' (0.0018) ' (0.0021) s (0.0021) safest (0.0013) and (0.0006) easiest (0.0019) to (0.0010) use (-0.0000) face (0.0011) paint! (-0.0019) it (0.0001) is (0.0008) water- (0.0008) based, (0.0004) easy- (0.0008) on (0.0003) & (0.0010) easy- (0.0001) off (-0.0002) and (0.0007) non- (0.0002) toxic. (0.0002) it (0.0007) applies (0.0001) easily (0.0006) with (0.0002) water (0.0006) and (0.0004) a (-0.0002) brush (0.0006) or (0.0006) sponge (0.0001) and (0.0006) washs (0.0007) off (-0.0004) easily (0.0002) with (-0.0000) mild (-0.0002) soap (0.0007) and (0.0006) water. (0.0006) snazaroo (0.0006) colors (0.0003) blend (-0.0010) extremely (-0.0002) well. (0.0003) colors (-0.0001) also (-0.0001) can (0.0005) be (0.0004) painted (0.0006) over (0.0001) each (-0.0000) other. (0.0002) it (-0.0004) is (-0.0001) best (0.0008) to (0.0009) apply (0.0003) light (0.0008) colors (0.0000) before (0.0000) darker (-0.0001) colors (0.0006) as (0.0005) you (-0.0006) create (0.0010) your (-0.0002) design. (0.0002)
~~~~~~

**Node-4** (global 38134):

~~~~~~text
product (-0.0347) from (0.0269) amazon (0.0077) platform (0.0065) with (0.0150) title (0.0123) and (0.0051) content (0.0258) : (0.0099) title (0.0135) : (-0.0156) missing. (0.0137) content (0.0268) : (0.0409) superior (0.0242) products (-0.0110) for (0.0060) the (-0.0234) professional (0.0060) artist (-0.0111) maximum (0.0585) coverage- (0.0209) extreme (0.0065) color- (0.0097) total (0.0132) control (-0.0001) wolfe (-0.0007) product (-0.0111) are (0.0191) top (0.0088) quality (0.0043) professional (0.0077) make (-0.0132) up (0.0084) that (0.0168) covers (-0.0027) very (0.0080) well (0.0045) and (-0.0061) removes (-0.0024) easily (0.0129) with (0.0101) soap (-0.0039) and (0.0017) water. (0.0342)
~~~~~~

**Node-5** (global 38135):

~~~~~~text
product (-0.0116) from (-0.0007) amazon (0.0057) platform (0.0012) with (-0.0048) title (0.0067) and (-0.0013) content (-0.0035) : (0.0021) title (0.0044) : (-0.0028) snazaroo (0.0038) high (0.0040) density (0.0014) face (-0.0043) painting (0.0165) sponge (0.0031) ( (0.0014) 10 (0.0045) pack (-0.0005) ). (0.0105) content (0.0033) : (-0.0038) use (0.0008) the (0.0021) professional (0.0089) quality (0.0043) high (0.0043) density (0.0060) sponge (0.0041) to (0.0017) apply (-0.0000) your (-0.0091) snazaroo (0.0060) facepaint. (-0.0071) all (0.0030) snazaroo (0.0065) face (0.0091) paints (0.0018) are (-0.0001) made (0.0027) by (0.0038) hand (0.0033) from (0.0043) the (-0.0018) finest (0.0048) quality (0.0070) ingredients, (0.0027) this (0.0011) enable (0.0026) us (0.0020) to (0.0023) create (0.0038) a (-0.0016) greater (0.0023) variety (0.0018) of (0.0047) colours (-0.0034) with (0.0022) a (-0.0026) more (0.0028) vivid (0.0044) finish. (0.0015) safety (0.0080) and (0.0027) comfort (0.0134) are (0.0088) paramount (-0.0036) to (0.0123) us, (0.0088) our (0.0050) products (0.0049) are (0.0053) manufactured (0.0075) using (0.0043) non- (0.0075) toxic, (0.0005) cosmetically (0.0035) approved (0.0033) ingredients, (0.0074) compliant (0.0065) with (0.0105) eu (0.0169) and (0.0050) fda (0.0041) regulations. (0.0053) snazaroo (0.0101) paints (0.0101) are (0.0024) all (0.0088) water- (0.0060) based, (0.0046) this (0.0051) makes (0.0109) them (0.0020) as (0.0050) easy (0.0108) to (0.0057) get (0.0073) off (0.0055) as (0.0040) they (0.0054) are (0.0060) to (0.0025) put (0.0014) on, (-0.0015) they (0.0029) are (0.0006) removable (0.0008) with (0.0003) soap (-0.0036) and (-0.0017) water (0.0022) without (-0.0014) the (-0.0021) need (-0.0016) for (0.0001) special (-0.0009) products. (0.0175) snazaroo (0.0034) face (0.0010) paints (0.0025) are (0.0035) longer (-0.0065) lasting, (-0.0030) only (0.0042) one (0.0045) coat (0.0048) is (0.0026) needed (0.0005) and (0.0044) once (0.0004) the (-0.0005) packaging (0.0016) is (-0.0002) open (-0.0019) the (0.0001) product (0.0015) won (-0.0017) ' (-0.0011) t (0.0052) crack (0.0012) or (0.0050) evaporate. (-0.0001)
~~~~~~

**Node-6** (global 38136):

~~~~~~text
product (-0.0025) from (-0.0067) amazon (0.0092) platform (-0.0046) with (-0.0099) title (0.0026) and (-0.0038) content (-0.0027) : (-0.0068) title (0.0086) : (-0.0030) mehron (0.0007) liquid (0.0069) face (0.0060) paints- (0.0017) glow (0.0106) in (0.0030) the (-0.0066) dark (0.0058) gl (-0.0003) ( (0.0074) 1 (0.0026) oz (-0.0046) ). (0.0026) content (0.0072) : (-0.0135) mehron (-0.0014) fantasy (0.0080) fx (-0.0178) glow (0.0046) in (0.0021) the (-0.0043) dark (-0.0017) face (-0.0022) paint (0.0008) is (0.0069) a (-0.0020) high (-0.0013) quality, (-0.0005) intensely (0.0070) pigmented, (-0.0013) liquid (-0.0006) makeup (0.0020) in (-0.0024) squeeze (-0.0004) tubes. (-0.0012) fantasy (-0.0000) fx (-0.0014) tube (-0.0096) makeup (-0.0037) can (0.0020) be (0.0013) used (0.0029) without (-0.0014) water (0.0016) activation. (0.0013) just (0.0037) squeeze (0.0004) and (0.0019) go! (0.0035) mehron (0.0007) fx (-0.0066) makeup (-0.0004) applies (-0.0002) easily, (-0.0036) dries (-0.0007) in (0.0005) less (-0.0030) then (0.0049) a (-0.0129) minute, (-0.0033) and (-0.0091) washes (0.0001) off (0.0031) cleanly. (-0.0056) mehron (0.0052) fantasy (0.0107) fx (-0.0015) makeup (0.0129) is (0.0116) ideal (0.0087) for (0.0041) year (0.0027) round (0.0008) face (0.0029) painting (0.0118) or (-0.0113) supporting (-0.0035) your (0.0002) favorite (0.0000) team (0.0019) at (0.0103) sporting (0.0010) events. (0.0282) 1 (0.0033) ounce (-0.0537) size. (-0.0099)
~~~~~~
