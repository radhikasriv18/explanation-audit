# Reference packet: GraphNarrator__Llama-70B__products__19356

- Method: GraphNarrator; configuration: Llama-70B; dataset: products; target node: 19356
- Explanation source: `./robustness_2026-10-30/llama70b/graphnarrator/products/19356.json` (response)
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

- ROOT (balsa wood sheets)
  - Node-1 (balsa sheets)
    - Node-1.1 (spring clothespins)
    - Node-1.2 (wood cement)
    - Node-1.3 (balsa strips)
    - Node-1.4 (heavy density balsa wood strips)
    - Node-1.5 (project woods balsa and basswood strip economy bag)

1. Word-Level Evaluation:

Keywords with high saliency scores in ROOT — "balsa" (0.00), "sheets" (0.00), "wood" (0.01), "construction" (0.00), "models" (0.01), "crafts" (0.02), "modeling" (0.03) — are strongly associated with crafting and modeling. These directly indicate the product belongs to a crafting or hobby-related category. More generic terms like "product" (0.02) and "amazon" (0.01) carry negligible saliency and contribute little.

2. Graph-Level Aggregation:

Node-1 (balsa sheets, keywords: "sheets" (0.02), "balsa" (0.00), "wood" (0.02), "construction" (0.03), "models" (0.02)) is a direct neighbor with moderate saliency, identifying crafting-specific accessories whose close proximity to ROOT reinforces the classification. Indirect neighbors — Node-1.1 (spring clothespins), Node-1.2 (wood cement), Node-1.3 (balsa strips), Node-1.4 (heavy density balsa wood strips), Node-1.5 (project woods balsa and basswood strip economy bag) — are all crafting or hobby-related components, collectively confirming a crafting context across both hops.

### Free-Text Explanation
```markdown
The classification of ROOT into "Beauty" is not strongly supported by its own keywords and the co-purchase neighborhood.

ROOT: Keywords like "balsa" (0.00), "sheets" (0.00), and "wood" (0.01) identify this as a crafting or hobby-related product, but do not directly relate to beauty.
  - Node-1: Balsa sheets (keywords: "sheets" (0.02), "balsa" (0.00), "wood" (0.02)) are a direct crafting component, reinforcing the crafting context.
    - Node-1.1: Spring clothespins are a crafting tool, supporting the crafting category.
    - Node-1.2: Wood cement is a crafting supply, further confirming the crafting context.
    - Node-1.3: Balsa strips are another crafting component, collectively affirming the crafting category.
    - Node-1.4: Heavy density balsa wood strips are a specialized crafting material, supporting the crafting context.
    - Node-1.5: A project woods balsa and basswood strip economy bag is a crafting supply kit, providing robust evidence for the crafting category.

However, the classification label "Beauty" does not align with the crafting context provided by the keywords and co-purchase neighborhood. A more fitting classification would be "Arts, Crafts & Sewing" or "Crafting".
```
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/66.json`).

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
<verbalized-graph>ROOT: product(0.02) amazon(0.01) platform(0.01) title(0.02) content(0.02) title(0.01) balsa(0.00) sheets(0.00) 3(0.00) 32(0.01) x(0.02) 4(0.00) x(0.01) 36(-0.00) 15(-0.00) ).(-0.00) content(0.02) midwest(0.01) wood(-0.00) offers(0.01) premium(0.04) quality(0.00) wood(0.01) construction(0.00) models,(0.01) doll(0.00) houses,(0.01) bazaar(0.01) crafts(0.02) much(0.02) more!(0.01) sheets(0.01) strips(0.01) bundled(0.02) shrink-(0.01) wrapped.(0.01) individual(0.01) piece(0.01) upc(0.01) coded.(0.01) balsa(0.00) wood(0.01) carefully(0.02) dried(0.01) special(0.01) kilns,(0.01) reducing(0.00) water(0.01) content(0.00) leave(0.01) light(0.01) wood(0.01) high(0.00) strength(0.01) weight(0.01) ratio.(0.01) premier(-0.01) wood(0.02) types(0.02) modeling(0.03) projects,(-0.00) balsa(0.00) cuts(0.00) easily(0.03) hobby(0.02) knife(0.01) may(0.00) stained(0.01) painted(0.01) represent(0.01) wood(0.01) type.(0.02) 
Node-1: product(0.06) amazon(-0.06) platform(0.00) title(0.07) content(0.05) title(0.05) balsa(0.00) sheets(-0.03) 1(-0.01) 16(0.01) x(0.04) 6(0.02) x(0.04) 36(0.01) 10(0.02) ).(-0.09) content(0.09) midwest(0.00) wood(-0.05) offers(0.00) premium(0.07) quality(0.01) wood(0.02) construction(0.03) models,(0.02) doll(0.05) houses,(0.02) bazaar(0.04) crafts(0.04) much(0.05) more!(-0.01) sheets(0.02) strips(0.03) bundled(0.08) shrink-(0.02) wrapped.(0.01) individual(0.05) piece(0.04) upc(0.00) coded.(0.02) balsa(0.02) wood(-0.00) carefully(0.05) dried(-0.00) special(0.02) kilns,(0.02) reducing(0.02) water(0.02) content(0.01) leave(0.03) light(0.02) wood(0.01) high(0.02) strength(0.02) weight(0.04) ratio.(0.13) premier(-0.05) wood(0.02) types(0.02) modeling(0.09) projects,(0.05) balsa(0.01) cuts(0.04) easily(0.08) hobby(0.09) knife(0.06) may(0.04) stained(0.07) painted(0.06) represent(0.06) wood(0.05) type.(0.14) 
Node-1.1: product(0.00) amazon(0.00) platform(-0.00) title(0.00) content(0.00) title(0.00) loew(0.00) cornell(0.01) 1021178(0.00) woodsies(-0.00) spring(0.00) clothespins,(0.00) 40(0.00) count.(0.00) content(0.00) woodsies(-0.00) 40-(0.00) count(0.00) spring(-0.00) clothespins(0.00) great(0.00) use(0.00) classroom(0.01) projects,(0.00) party(0.00) crafts,(0.00) camp(0.00) crafts.(-0.00) clothespins(0.00) measure(0.00) 2.(-0.00) 88-(0.00) inches(0.00) height(0.00) natural(0.00) raw(0.00) wood.(-0.00) ideal(0.00) crafters,(0.00) teachers,(-0.00) students.(-0.00) made(-0.00) birch(0.00) wood,(-0.00) non(0.00) food(0.00) safe.(-0.00) 
Node-1.2: product(-0.00) amazon(0.02) platform(0.01) title(0.01) content(0.01) title(0.02) wood(0.00) cement(-0.00) extra(0.01) fast,(0.01) 5(0.00) 8(0.01) oz.(-0.02) content(0.02) 5(-0.00) 8(-0.00) ounce(0.00) tube(-0.00) testors(0.00) cement(-0.00) wood(-0.00) models.(0.01) strong(0.00) fast(0.00) drying(0.00) cement(0.01) specially(0.00) formulated(-0.00) joining(0.00) wood.(-0.02) hot(0.01) fuel(0.00) proof,(0.00) extra(0.00) fast(0.01) drying(-0.00) formula(-0.00) cuts(-0.01) drying(0.00) time(-0.00) half(0.00) twelve(0.01) hours(0.00) six(-0.00) hours.(-0.03) applying(0.03) surfaces(0.01) joined,(-0.01) allow(-0.01) dry(0.00) seconds,(0.01) press(0.00) together,(0.00) allow(-0.01) twelve(0.00) hours(0.01) maximum(0.00) bonding(-0.01) strength.(-0.00) please(0.00) read(-0.01) instructions(-0.03) using.(-0.00) 
Node-1.3: product(0.01) amazon(0.01) platform(-0.00) title(0.02) content(0.00) title(0.02) balsa(0.01) strips(0.02) 1(0.01) 8(0.01) x(0.01) 1(0.00) 8(0.00) x(0.01) 36(0.00) 36(0.01) ).(-0.02) content(0.02) grown(0.01) privately(0.00) owned(0.00) farm(0.00) warm,(0.01) humid(0.00) tropics(0.01) south(0.00) america,(0.02) midwest(-0.01) balsa(0.01) finest(0.01) balsa(0.01) wood(-0.00) available.(-0.00) carefully(0.01) dried(0.00) special(0.00) kilns,(0.01) reducing(0.00) water(0.01) content(0.00) leaving(0.00) light(0.00) wood(0.01) high(0.00) strength(0.01) weight(0.00) ratio.(0.00) perfect(-0.00) wood(-0.00) types(0.01) modeling(0.00) projects(0.01) cuts(0.01) easily,(-0.00) painted,(0.00) even(0.01) stained(0.01) represent(0.00) types(0.01) wood.(-0.02) also(0.02) available(0.02) blocks(0.01) sheets.(0.00) 
Node-1.4: product(-0.00) amazon(-0.01) platform(0.01) title(0.00) content(0.01) title(0.00) pitsco(-0.00) heavy(0.00) density(0.00) balsa(-0.00) wood(-0.00) strips(0.00) pack(0.00) 100(0.00) ).(0.01) content(0.01) none(0.01) 
Node-1.5: product(0.00) amazon(0.00) platform(0.00) title(0.01) content(0.00) title(0.00) midwest(0.01) products(0.01) project(0.00) woods(-0.00) balsa(0.00) amp(0.00) basswood(0.00) strip(0.01) economy(0.00) bag.(-0.00) content(0.00) economy(0.01) bag(-0.00) balsa(0.00) basswood(0.00) strips(0.00) includes(-0.00) various(-0.00) sizes(0.00) shapes(0.00) types(0.00) hobby,(0.00) craft,(0.00) school(0.00) art(0.00) projects.(0.00) basswood(0.01) domestic(0.00) wood(0.00) cut(0.00) northern(0.00) michigan(0.00) wisconsin.(0.00) desired(0.00) economy,(0.00) workability(0.00) finishing(0.00) qualities(0.00) close,(0.00) tight(0.00) homogenous(0.00) grain(0.01) structure.(0.00) balsa(0.00) grown(0.00) south(0.00) american(0.00) rain(0.00) forests(0.00) kiln(0.00) dried(0.00) produce(0.01) light(0.00) weight(0.00) high(0.00) strength-(0.00) to-(0.00) weight(0.00) ratio(0.01) wood.(-0.00) economy(0.01) bag(0.01) includes(0.01) 36(0.00) cubic(0.01) inch(0.01) 1(0.00) 4(0.00) board(0.00) foot(0.00) random(0.01) size(0.00) shape(0.00) strips(-0.00) 
</verbalized-graph>

### Classification Label
Beauty

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 19356
- Title: Balsa Sheets 3/32 x 4 x 36 (15)
- True class (canonical `y`): **Arts, Crafts & Sewing**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Arts, Crafts & Sewing**
- Prediction recorded by this method's pipeline: **Beauty**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Balsa Sheets 3/32 x 4 x 36 (15). Content: Midwest Wood offers premium quality wood for the construction of models, doll houses, bazaar crafts and so much more! All sheets and strips are bundled and shrink-wrapped. Each individual piece is UPC coded. Balsa wood is carefully dried in special kilns, reducing the water content to leave a light wood with a high strength to weight ratio. The premier wood for all types of modeling projects, Balsa cuts easily with a hobby knife and may be stained or painted to represent any wood type.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 3315 | Toys & Games | Balsa Sheets 1/16 x 6 x 36 (10) |

### 2-hop (shortest distance exactly 2): 5 nodes

| node id | true class | title |
|---|---|---|
| 344 | Arts, Crafts & Sewing | Loew Cornell 1021178 Woodsies Spring Clothespins, 40 count |
| 19355 | Toys & Games | Wood Cement Extra Fast,5/8 oz |
| 19357 | Toys & Games | Balsa Strips 1/8 x 1/8 x 36 (36) |
| 19358 | Office Products | Pitsco Heavy Density Balsa Wood Strips (Pack of 100) |
| 19359 | Arts, Crafts & Sewing | Midwest Products Project Woods Balsa &amp; Basswood Strip Economy Bag |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/66.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Beauty**, ground truth = **Arts, Crafts & Sewing**.
The verbalized graph is 5404 characters; the model saw the first 6000 (the whole graph).
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 19356 | 110 | 0.0397 | yes |
| Node-1 | 1 | 3315 | 110 | 0.1395 | yes |
| Node-1.1 | 2 | 344 | 63 | 0.0057 | yes |
| Node-1.2 | 3 | 19355 | 92 | 0.0330 | yes |
| Node-1.3 | 4 | 19357 | 110 | 0.0192 | yes |
| Node-1.4 | 5 | 19358 | 25 | 0.0133 | yes |
| Node-1.5 | 6 | 19359 | 119 | 0.0089 | yes |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, ROOT->Node-1

### Tokens and scores

**ROOT** (global 19356):

~~~~~~text
product (0.0201) from (0.0072) amazon (0.0060) platform (0.0099) with (0.0026) title (0.0167) and (0.0029) content (0.0188) : (0.0190) title (0.0149) : (0.0084) balsa (0.0020) sheets (0.0007) 3 (0.0048) / (0.0048) 32 (0.0061) x (0.0190) 4 (0.0048) x (0.0148) 36 (-0.0003) ( (0.0092) 15 (-0.0049) ). (-0.0005) content (0.0240) : (0.0093) midwest (0.0115) wood (-0.0020) offers (0.0096) premium (0.0397) quality (0.0006) wood (0.0146) for (0.0110) the (0.0091) construction (0.0041) of (0.0041) models, (0.0066) doll (0.0001) houses, (0.0062) bazaar (0.0130) crafts (0.0179) and (0.0139) so (0.0119) much (0.0161) more! (0.0141) all (0.0134) sheets (0.0095) and (0.0186) strips (0.0140) are (0.0141) bundled (0.0220) and (0.0141) shrink- (0.0109) wrapped. (0.0073) each (0.0110) individual (0.0068) piece (0.0145) is (0.0126) upc (0.0053) coded. (0.0095) balsa (0.0032) wood (0.0072) is (0.0128) carefully (0.0158) dried (0.0078) in (-0.0028) special (0.0070) kilns, (0.0084) reducing (0.0010) the (-0.0008) water (0.0097) content (0.0016) to (0.0086) leave (0.0105) a (-0.0042) light (0.0085) wood (0.0132) with (0.0114) a (-0.0056) high (0.0050) strength (0.0059) to (0.0102) weight (0.0135) ratio. (0.0095) the (-0.0050) premier (-0.0065) wood (0.0176) for (0.0092) all (0.0007) types (0.0197) of (-0.0161) modeling (0.0306) projects, (-0.0022) balsa (0.0004) cuts (0.0025) easily (0.0309) with (0.0136) a (-0.0175) hobby (0.0170) knife (0.0089) and (0.0143) may (0.0049) be (0.0128) stained (0.0055) or (0.0117) painted (0.0071) to (0.0091) represent (0.0092) any (0.0114) wood (0.0079) type. (0.0208)
~~~~~~

**Node-1** (global 3315):

~~~~~~text
product (0.0648) from (0.0511) amazon (-0.0598) platform (0.0031) with (0.0353) title (0.0707) and (0.0232) content (0.0478) : (0.0373) title (0.0453) : (-0.0132) balsa (0.0044) sheets (-0.0344) 1 (-0.0086) / (0.0033) 16 (0.0143) x (0.0387) 6 (0.0167) x (0.0430) 36 (0.0140) ( (-0.0063) 10 (0.0247) ). (-0.0864) content (0.0874) : (0.0805) midwest (0.0025) wood (-0.0499) offers (0.0045) premium (0.0686) quality (0.0074) wood (0.0209) for (0.0118) the (0.0413) construction (0.0323) of (-0.0199) models, (0.0209) doll (0.0499) houses, (0.0206) bazaar (0.0420) crafts (0.0392) and (0.0392) so (0.0546) much (0.0468) more! (-0.0088) all (0.0266) sheets (0.0249) and (0.0542) strips (0.0349) are (0.0474) bundled (0.0845) and (0.0489) shrink- (0.0207) wrapped. (0.0145) each (0.0571) individual (0.0472) piece (0.0394) is (0.0781) upc (0.0028) coded. (0.0201) balsa (0.0202) wood (-0.0035) is (0.0486) carefully (0.0488) dried (-0.0024) in (0.0168) special (0.0166) kilns, (0.0245) reducing (0.0155) the (0.0386) water (0.0213) content (0.0142) to (0.0421) leave (0.0275) a (0.0243) light (0.0159) wood (0.0065) with (0.0644) a (0.0197) high (0.0204) strength (0.0231) to (0.0395) weight (0.0400) ratio. (0.1335) the (-0.0484) premier (-0.0465) wood (0.0179) for (0.0145) all (0.0306) types (0.0244) of (-0.0509) modeling (0.0864) projects, (0.0507) balsa (0.0139) cuts (0.0371) easily (0.0767) with (0.0218) a (-0.0027) hobby (0.0915) knife (0.0554) and (0.0465) may (0.0421) be (0.0400) stained (0.0724) or (0.0404) painted (0.0584) to (0.0659) represent (0.0627) any (0.0396) wood (0.0471) type. (0.1395)
~~~~~~

**Node-1.1** (global 344):

~~~~~~text
product (0.0017) from (0.0004) amazon (0.0011) platform (-0.0005) with (0.0004) title (0.0028) and (-0.0005) content (0.0010) : (0.0042) title (0.0020) : (0.0026) loew (0.0031) cornell (0.0053) 1021178 (0.0004) woodsies (-0.0011) spring (0.0004) clothespins, (0.0026) 40 (0.0012) count. (0.0024) content (0.0046) : (0.0034) woodsies (-0.0029) 40- (0.0018) count (0.0026) spring (-0.0005) clothespins (0.0035) are (0.0020) great (0.0003) for (-0.0002) use (0.0022) in (0.0005) classroom (0.0057) projects, (0.0012) party (0.0001) crafts, (0.0000) and (-0.0000) camp (0.0014) crafts. (-0.0014) clothespins (0.0002) measure (0.0022) 2. (-0.0019) 88- (0.0016) inches (0.0010) in (-0.0004) height (0.0014) and (0.0005) are (0.0018) natural (0.0029) raw (0.0019) wood. (-0.0008) ideal (0.0013) for (0.0043) crafters, (0.0014) teachers, (-0.0006) and (0.0034) students. (-0.0010) made (-0.0007) of (0.0019) birch (0.0012) wood, (-0.0012) non (0.0022) food (0.0028) safe. (-0.0019)
~~~~~~

**Node-1.2** (global 19355):

~~~~~~text
product (-0.0007) from (0.0042) amazon (0.0166) platform (0.0066) with (0.0045) title (0.0104) and (0.0109) content (0.0064) : (0.0135) title (0.0159) : (0.0198) wood (0.0017) cement (-0.0004) extra (0.0062) fast, (0.0094) 5 (0.0015) / (0.0023) 8 (0.0070) oz. (-0.0181) content (0.0177) : (0.0017) this (0.0092) is (-0.0035) the (0.0042) 5 (-0.0009) / (0.0046) 8 (-0.0005) ounce (0.0023) tube (-0.0002) of (0.0070) testors (0.0042) cement (-0.0008) for (-0.0060) wood (-0.0028) models. (0.0076) strong (0.0010) fast (0.0029) drying (0.0013) cement (0.0109) is (-0.0006) specially (0.0033) formulated (-0.0001) for (0.0007) joining (0.0025) wood. (-0.0227) hot (0.0100) fuel (0.0032) proof, (0.0037) extra (0.0014) fast (0.0090) drying (-0.0040) formula (-0.0018) cuts (-0.0067) drying (0.0028) time (-0.0028) in (0.0079) half (0.0037) from (-0.0015) twelve (0.0091) hours (0.0027) to (0.0152) six (-0.0040) hours. (-0.0337) applying (0.0330) to (0.0232) both (0.0085) surfaces (0.0061) to (0.0040) be (0.0002) joined, (-0.0088) allow (-0.0064) to (-0.0023) dry (0.0026) for (-0.0001) a (-0.0090) few (-0.0042) seconds, (0.0077) press (0.0012) together, (0.0019) allow (-0.0098) twelve (0.0016) hours (0.0075) for (-0.0092) maximum (0.0039) bonding (-0.0118) strength. (-0.0030) please (0.0007) read (-0.0067) all (0.0016) instructions (-0.0268) before (-0.0023) using. (-0.0034)
~~~~~~

**Node-1.3** (global 19357):

~~~~~~text
product (0.0090) from (0.0069) amazon (0.0104) platform (-0.0010) with (0.0115) title (0.0175) and (0.0140) content (0.0021) : (0.0151) title (0.0163) : (0.0072) balsa (0.0096) strips (0.0168) 1 (0.0100) / (0.0040) 8 (0.0068) x (0.0074) 1 (0.0040) / (0.0046) 8 (0.0025) x (0.0077) 36 (0.0033) ( (0.0054) 36 (0.0074) ). (-0.0182) content (0.0153) : (0.0015) grown (0.0101) on (0.0088) a (0.0080) privately (0.0029) owned (0.0049) farm (0.0020) in (0.0075) the (0.0068) warm, (0.0055) humid (0.0036) tropics (0.0062) of (0.0085) south (0.0033) america, (0.0192) midwest (-0.0123) ' (0.0075) s (0.0055) balsa (0.0143) is (0.0045) the (0.0019) finest (0.0062) balsa (0.0088) wood (-0.0024) available. (-0.0039) it (0.0043) has (0.0071) been (0.0005) carefully (0.0095) dried (0.0008) in (0.0031) special (0.0049) kilns, (0.0069) reducing (0.0004) the (-0.0010) water (0.0071) content (0.0011) and (0.0030) leaving (0.0016) a (0.0001) light (0.0038) wood (0.0111) with (0.0034) a (-0.0025) high (0.0040) strength (0.0093) to (0.0030) weight (0.0031) ratio. (0.0007) this (-0.0033) is (-0.0028) the (-0.0075) perfect (-0.0002) wood (-0.0031) for (0.0023) all (0.0053) types (0.0112) of (0.0069) modeling (0.0012) projects (0.0102) ; (0.0032) it (0.0009) cuts (0.0066) easily, (-0.0003) can (0.0023) be (0.0053) painted, (0.0046) and (0.0064) can (0.0095) even (0.0067) be (0.0043) stained (0.0121) to (0.0049) represent (0.0018) other (0.0077) types (0.0090) of (0.0026) wood. (-0.0159) also (0.0181) available (0.0191) in (0.0040) blocks (0.0087) and (0.0071) sheets. (0.0046)
~~~~~~

**Node-1.4** (global 19358):

~~~~~~text
product (-0.0021) from (0.0108) amazon (-0.0073) platform (0.0083) with (0.0060) title (0.0008) and (0.0001) content (0.0096) : (-0.0008) title (0.0026) : (0.0018) pitsco (-0.0024) heavy (0.0035) density (0.0027) balsa (-0.0002) wood (-0.0043) strips (0.0023) ( (-0.0003) pack (0.0044) of (0.0019) 100 (0.0046) ). (0.0050) content (0.0067) : (0.0087) none (0.0133)
~~~~~~

**Node-1.5** (global 19359):

~~~~~~text
product (0.0011) from (0.0009) amazon (0.0018) platform (0.0031) with (0.0033) title (0.0059) and (0.0031) content (0.0027) : (0.0074) title (0.0047) : (0.0027) midwest (0.0058) products (0.0065) project (0.0034) woods (-0.0007) balsa (0.0029) & (0.0051) amp (0.0034) ; (0.0061) basswood (0.0014) strip (0.0052) economy (0.0039) bag. (-0.0037) content (0.0034) : (-0.0018) this (0.0030) economy (0.0051) bag (-0.0021) of (0.0018) balsa (0.0028) and (0.0049) basswood (0.0027) strips (0.0037) includes (-0.0024) various (-0.0007) sizes (0.0032) and (0.0050) shapes (0.0029) for (0.0021) all (0.0034) types (0.0045) of (0.0025) hobby, (0.0028) craft, (0.0028) school (0.0031) and (0.0061) art (0.0044) projects. (0.0032) basswood (0.0063) is (0.0014) a (-0.0036) domestic (0.0021) wood (0.0006) cut (0.0042) in (0.0036) northern (0.0026) michigan (0.0012) and (0.0065) wisconsin. (0.0013) it (0.0065) is (0.0049) desired (0.0035) for (0.0024) its (0.0011) economy, (0.0033) workability (0.0029) and (0.0052) finishing (0.0021) qualities (0.0031) with (0.0044) its (0.0030) close, (0.0023) tight (0.0013) homogenous (0.0006) grain (0.0063) structure. (0.0037) balsa (0.0029) is (0.0031) grown (0.0015) in (0.0051) south (0.0042) american (0.0018) rain (0.0024) forests (0.0036) and (0.0067) is (0.0047) kiln (0.0030) dried (0.0033) to (0.0025) produce (0.0062) a (-0.0073) light (0.0028) weight (0.0046) and (0.0028) high (0.0033) strength- (0.0049) to- (0.0037) weight (0.0048) ratio (0.0070) wood. (-0.0046) economy (0.0080) bag (0.0079) includes (0.0054) 36 (0.0001) cubic (0.0069) inch (0.0060) ( (0.0045) 1 (0.0020) / (0.0012) 4 (0.0011) board (0.0013) foot (0.0032) ) (0.0027) of (0.0029) random (0.0089) size (0.0044) and (0.0040) shape (0.0016) strips (-0.0002)
~~~~~~
