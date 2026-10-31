# Reference packet: GraphNarrator__gpt-4o-mini__products__19140

- Method: GraphNarrator; configuration: gpt-4o-mini; dataset: products; target node: 19140
- Explanation source: `./robustness_2026-10-30/graphnarrator_gpt4omini/generated_expls-601/65.json` (messages[assistant])
- Scored scope (what the claims were extracted from): ### Free-Text Explanation section
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

Claims were extracted from the `### Free-Text Explanation` section only; the full assistant message is shown here.

~~~~~~text
### Reasoning

0. **Graph Structure Reconstruction:**

In the provided verbalized graph, the ROOT node (first line) is the target for classification. Single-digit indexed nodes are direct neighbors of ROOT. Double-digit indexed nodes are:
  - Two hops away from ROOT
  - Direct children of their parent node

Thus, the graph structure of this verbalized graph is:

- ROOT (polypropylene twine)
  - Node-1 (jute twine)
    - Node-1.1 (wood beads)
    - Node-1.2 (jute skein)
    - Node-1.3 (hemp cord)
    - Node-1.4 (surgical steel earwires)

1. **Word-Level Evaluation:**

Keywords with notable saliency scores in ROOT — "twine," "polypropylene," "heavy duty," and "crafts" — indicate a product used for various practical applications, including gardening and crafts. The presence of terms like "durable" and "general household use" suggests that this product is versatile and commonly used in personal care contexts, which aligns with the "Health & Personal Care" category.

2. **Graph-Level Aggregation:**

Node-1 (jute twine) contains keywords such as "craft" and "projects," which further emphasize the crafting aspect of personal care. The direct neighbors of Node-1, including Node-1.1 (wood beads), Node-1.2 (jute skein), Node-1.3 (hemp cord), and Node-1.4 (surgical steel earwires), all relate to crafting and personal accessories, reinforcing the classification. The presence of surgical steel earwires, which are used in jewelry making and personal adornment, directly ties into the health and personal care context.

### Free-Text Explanation
```markdown
The classification of ROOT into "Health & Personal Care" is supported by its own keywords and the co-purchase neighborhood.

ROOT: Keywords like "twine," "polypropylene," and "heavy duty" suggest this product is a durable crafting material, suitable for various personal care and household applications.
  - Node-1: The jute twine (keywords: "craft," "projects") emphasizes its use in crafting, which is relevant to personal care activities.
    - Node-1.1: Wood beads are commonly used in crafting jewelry, further supporting the personal care context.
    - Node-1.2: A jute skein is another crafting material, reinforcing the versatility of products in this category.
    - Node-1.3: Hemp cord is also used for crafting, particularly in personal accessories, which aligns with health and personal care.
    - Node-1.4: Surgical steel earwires are directly related to jewelry making, indicating a strong connection to personal adornment and care.

In summary, ROOT's keywords indicate a crafting material that supports personal care activities, and the entire co-purchase neighborhood consists of crafting components and accessories, providing robust evidence for the "Health & Personal Care" classification.
```
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/65.json`).

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
<verbalized-graph>ROOT: product(0.00) amazon(0.03) platform(-0.01) title(-0.00) content(0.02) title(0.00) lehigh(0.03) 540w(-0.00) 230-(-0.00) feet(-0.01) polypropylene(0.01) heavy(0.01) duty(0.01) twine,(0.01) brown.(0.01) content(0.01) secure(-0.00) line(0.00) lehigh(0.03) twisted(0.01) polypropylene(0.01) twine.(0.00) great(0.02) hobbies,(0.01) recycling,(0.00) crafts,(0.01) handyman(0.01) work,(0.00) kitchen,(0.01) gardening,(0.01) general(-0.00) household(0.00) commercial(-0.00) use.(0.02) durable(0.00) sisal(0.01) substitute.(0.02) polypropylene(0.01) polyester(0.01) construction.(0.01) easy(0.02) hands.(0.01) unique(0.01) overwrap(0.00) offers(0.00) customers(0.01) dispensing(0.01) feature(-0.00) keeps(0.01) twin(0.00) clean(-0.01) tangle(0.02) free.(0.02) available(-0.02) brown(0.01) color.(0.03) measures(0.02) 230-(0.01) feet(-0.01) length.(0.03) 
Node-1: product(0.04) amazon(0.07) platform(0.04) title(0.02) content(0.03) title(0.03) darice(0.02) 5-(0.04) ply(0.04) craft(0.02) designer(0.04) jute,(0.00) natural.(0.07) content(0.05) jute(0.01) type(0.08) plant(0.10) fiber(0.02) used(0.02) make(0.02) common(0.06) items(0.02) rope(0.11) twine(0.04) rugs(0.06) chair(0.06) coverings.(0.07) ideal(0.05) craft(0.07) projects.(0.06) package(0.09) contains(0.04) 6-(0.03) pound(0.04) 648-(0.04) feet(0.05) 5(0.02) ply(0.05) natural(0.09) jute.(0.05) imported.(0.19) 
Node-1.1: product(-0.01) amazon(0.01) platform(0.01) title(0.00) content(0.01) title(0.00) darice(0.00) 0500-(0.00) 04(-0.00) wood(-0.00) beads,(0.00) large,(-0.00) assorted(-0.01) color.(0.01) content(0.00) large(-0.01) round(0.00) wood(0.00) beads(0.01) assorted(-0.00) sizes(-0.00) ranging(-0.00) 18mm(0.00) 25mm.(0.00) beads(0.01) comes(0.01) assorted(-0.00) colors.(-0.00) 45(0.01) pieces(0.01) per(0.01) package.(-0.03) 
Node-1.2: product(0.00) amazon(-0.00) platform(0.00) title(0.00) content(0.00) title(0.00) darice(0.00) 135-(0.00) feet(0.00) 4(0.00) ply(0.00) jute,(0.00) 1-(0.00) pound.(-0.00) content(0.01) darice(-0.00) 4(0.00) ply(0.00) jute(-0.00) used(0.00) creating(0.00) many(-0.00) craft(-0.01) projects(-0.00) 135(0.00) feet,(0.00) 4(0.00) ply,(-0.00) 1(0.00) pound(-0.00) skein.(0.00) darice(-0.00) jute.(0.00) 
Node-1.3: product(-0.01) amazon(0.01) platform(-0.00) title(0.00) content(0.01) title(0.00) hemtique(0.00) cord(0.01) spool(0.00) 20-(-0.00) pound,(0.00) dark(0.01) brown.(0.01) content(0.01) high(0.00) quality(0.00) variegated(0.00) hemp(0.00) cordage.(0.01) smooth(0.00) six(0.00) strand(0.00) polished(0.01) cord(0.00) perfect(0.00) crafts(-0.00) hobbies(0.00) including(0.00) macrame(0.00) ',(0.00) scrapbooking,(0.00) jewelry,(0.00) gardening(0.00) beading.(-0.00) dyed(-0.00) non(0.01) toxic(0.00) certified(0.00) azo(0.00) free(0.00) dyes,(0.00) use(0.00) hemp(0.01) cord(0.00) stonger(0.00) alternative(0.01) cotton(0.01) synthetic(0.01) twine.(0.01) 20-(0.00) pound.(0.01) weight,(0.00) 1mm,(0.01) 205-(0.01) feet,(0.00) 50-(0.00) gram.(0.01) 
Node-1.4: product(0.01) amazon(0.02) platform(-0.00) title(0.00) content(0.02) title(0.02) surgical(0.00) steel(0.00) earring(0.00) earwires(0.00) hypoallergenic(0.00) shiny(0.00) silver(-0.00) plated(-0.00) fishhook(0.00) 10x3.(0.00) 5mm(-0.00) ball(0.01) coil(0.00) open(0.00) loop,(-0.00) 21(0.00) gauge.(0.01) 100(0.00) pairs.(0.01) 200(0.00) ).(0.01) content(0.03) surgical(0.00) steel(0.00) earring(0.00) earwires(0.00) hypoallergenic(0.00) shiny(-0.00) silver(-0.00) plated(-0.00) fishhook(-0.00) 10x3.(0.01) 5mm(-0.00) ball(0.01) coil(0.00) open(-0.00) loop,(0.00) 21(-0.01) gauge.(0.01) 100(-0.01) pairs.(-0.00) 200(0.02) 
</verbalized-graph>

### Classification Label
Health & Personal Care

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 19140
- Title: Lehigh 540W 230-Feet Polypropylene Heavy Duty Twine, Brown
- True class (canonical `y`): **Office Products**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Arts, Crafts & Sewing**
- Prediction recorded by this method's pipeline: **Health & Personal Care**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Lehigh 540W 230-Feet Polypropylene Heavy Duty Twine, Brown. Content: Secure line by Lehigh twisted polypropylene twine. Great for hobbies, recycling, crafts, handyman work, kitchen, gardening, general household or commercial use. Durable sisal substitute. Polypropylene and polyester construction. Easy on the hands. Unique overwrap offers customers a dispensing feature that keeps twin clean and tangle free. Available in brown color. Measures 230-Feet length.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 3267 | Arts, Crafts & Sewing | Darice 5-Ply Craft Designer Jute, Natural |

### 2-hop (shortest distance exactly 2): 4 nodes

| node id | true class | title |
|---|---|---|
| 339 | Arts, Crafts & Sewing | Darice 0500-04 Wood Beads, Large, Assorted Color |
| 19137 | Office Products | Darice 135-Feet 4 Ply Jute, 1-Pound |
| 19138 | Arts, Crafts & Sewing | Hemtique Cord Spool 20-Pound, Dark Brown |
| 19139 | Arts, Crafts & Sewing | Surgical Steel Earring Earwires Hypoallergenic Shiny Silver Plated Fishhook with 10x3.5mm Ball and Coil with Open Loop, 21 Gauge. 100 Pairs. (200) |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/65.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Health & Personal Care**, ground truth = **Office Products**.
The verbalized graph is 3587 characters; the model saw the first 6000 (the whole graph).
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 19140 | 76 | 0.0340 | yes |
| Node-1 | 1 | 3267 | 60 | 0.1930 | yes |
| Node-1.1 | 2 | 339 | 47 | 0.0132 | yes |
| Node-1.2 | 3 | 19137 | 43 | 0.0125 | yes |
| Node-1.3 | 4 | 19138 | 76 | 0.0123 | yes |
| Node-1.4 | 5 | 19139 | 63 | 0.0273 | yes |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, ROOT->Node-1

### Tokens and scores

**ROOT** (global 19140):

~~~~~~text
product (0.0026) from (-0.0206) amazon (0.0279) platform (-0.0074) with (-0.0064) title (-0.0006) and (0.0020) content (0.0207) : (0.0007) title (0.0017) : (0.0030) lehigh (0.0259) 540w (-0.0037) 230- (-0.0050) feet (-0.0117) polypropylene (0.0052) heavy (0.0118) duty (0.0109) twine, (0.0096) brown. (0.0072) content (0.0096) : (0.0060) secure (-0.0013) line (0.0018) by (0.0020) lehigh (0.0340) twisted (0.0096) polypropylene (0.0091) twine. (0.0038) great (0.0161) for (0.0145) hobbies, (0.0077) recycling, (0.0046) crafts, (0.0097) handyman (0.0141) work, (0.0038) kitchen, (0.0062) gardening, (0.0147) general (-0.0018) household (0.0009) or (0.0073) commercial (-0.0013) use. (0.0155) durable (0.0042) sisal (0.0079) substitute. (0.0175) polypropylene (0.0078) and (0.0083) polyester (0.0079) construction. (0.0129) easy (0.0154) on (0.0121) the (-0.0019) hands. (0.0139) unique (0.0099) overwrap (0.0031) offers (0.0029) customers (0.0053) a (0.0057) dispensing (0.0056) feature (-0.0031) that (0.0076) keeps (0.0105) twin (0.0047) clean (-0.0078) and (0.0041) tangle (0.0189) free. (0.0164) available (-0.0160) in (0.0146) brown (0.0124) color. (0.0287) measures (0.0170) 230- (0.0128) feet (-0.0106) length. (0.0303)
~~~~~~

**Node-1** (global 3267):

~~~~~~text
product (0.0423) from (0.0165) amazon (0.0723) platform (0.0390) with (0.0320) title (0.0154) and (0.0555) content (0.0350) : (0.0113) title (0.0346) : (0.0841) darice (0.0182) 5- (0.0395) ply (0.0380) craft (0.0228) designer (0.0416) jute, (0.0048) natural. (0.0650) content (0.0471) : (0.0354) jute (0.0066) is (0.0350) a (-0.0120) type (0.0751) of (0.0001) plant (0.1042) fiber (0.0224) used (0.0153) to (0.0161) make (0.0235) common (0.0634) items (0.0181) such (0.0597) as (0.0331) rope (0.1080) ; (0.0825) twine (0.0388) ; (0.0467) rugs (0.0623) and (0.0478) chair (0.0563) coverings. (0.0717) ideal (0.0494) for (0.0433) craft (0.0699) projects. (0.0617) this (0.1618) package (0.0922) contains (0.0376) 6- (0.0274) pound (0.0358) / (0.0290) 648- (0.0420) feet (0.0498) of (-0.0065) 5 (0.0160) ply (0.0457) natural (0.0918) jute. (0.0510) imported. (0.1930)
~~~~~~

**Node-1.1** (global 339):

~~~~~~text
product (-0.0143) from (0.0045) amazon (0.0103) platform (0.0084) with (-0.0011) title (0.0031) and (-0.0052) content (0.0066) : (-0.0029) title (0.0043) : (-0.0023) darice (0.0037) 0500- (0.0018) 04 (-0.0032) wood (-0.0017) beads, (0.0021) large, (-0.0007) assorted (-0.0051) color. (0.0088) content (0.0019) : (-0.0058) the (-0.0104) large (-0.0061) round (0.0010) wood (0.0007) beads (0.0110) are (0.0004) assorted (-0.0018) in (0.0036) sizes (-0.0029) ranging (-0.0024) from (0.0004) 18mm (0.0028) to (0.0030) 25mm. (0.0034) the (0.0072) beads (0.0132) comes (0.0077) in (0.0022) assorted (-0.0009) colors. (-0.0010) there (0.0068) are (0.0012) 45 (0.0065) pieces (0.0051) per (0.0119) package. (-0.0267)
~~~~~~

**Node-1.2** (global 19137):

~~~~~~text
product (0.0010) from (0.0010) amazon (-0.0041) platform (0.0045) with (-0.0001) title (0.0001) and (-0.0002) content (0.0009) : (0.0006) title (0.0007) : (0.0028) darice (0.0003) 135- (0.0048) feet (0.0021) 4 (0.0040) ply (0.0009) jute, (0.0012) 1- (0.0017) pound. (-0.0047) content (0.0125) : (-0.0008) darice (-0.0025) ' (-0.0005) s (0.0027) 4 (0.0008) ply (0.0005) jute (-0.0003) is (0.0023) used (0.0001) in (-0.0017) creating (0.0021) many (-0.0008) craft (-0.0128) projects (-0.0004) 135 (0.0001) feet, (0.0017) 4 (0.0000) ply, (-0.0001) 1 (0.0027) pound (-0.0026) skein. (0.0017) darice (-0.0043) jute. (0.0013)
~~~~~~

**Node-1.3** (global 19138):

~~~~~~text
product (-0.0062) from (-0.0063) amazon (0.0111) platform (-0.0004) with (-0.0065) title (0.0033) and (-0.0024) content (0.0057) : (-0.0068) title (0.0016) : (0.0058) hemtique (0.0007) cord (0.0064) spool (0.0029) 20- (-0.0019) pound, (0.0013) dark (0.0051) brown. (0.0069) content (0.0061) : (-0.0040) high (0.0029) quality (0.0006) variegated (0.0035) hemp (0.0036) cordage. (0.0093) smooth (0.0034) six (0.0010) strand (0.0020) polished (0.0058) cord (0.0023) is (0.0110) perfect (0.0024) for (0.0048) all (0.0084) crafts (-0.0043) and (0.0074) hobbies (0.0007) including (0.0021) macrame (0.0012) ', (0.0011) scrapbooking, (0.0016) jewelry, (0.0019) gardening (0.0022) and (0.0088) beading. (-0.0036) dyed (-0.0038) with (0.0033) non (0.0103) toxic (0.0024) certified (0.0029) azo (0.0011) free (0.0036) dyes, (0.0005) you (0.0039) can (0.0021) use (0.0022) hemp (0.0084) cord (0.0038) as (-0.0024) a (-0.0201) stonger (0.0047) more (-0.0009) alternative (0.0084) to (0.0016) cotton (0.0077) or (0.0041) synthetic (0.0065) twine. (0.0092) 20- (0.0037) pound. (0.0074) weight, (0.0017) 1mm, (0.0074) 205- (0.0106) feet, (0.0022) 50- (0.0048) gram. (0.0123)
~~~~~~

**Node-1.4** (global 19139):

~~~~~~text
product (0.0109) from (-0.0181) amazon (0.0249) platform (-0.0046) with (-0.0052) title (0.0017) and (-0.0143) content (0.0218) : (-0.0092) title (0.0166) : (0.0046) surgical (0.0009) steel (0.0004) earring (0.0003) earwires (0.0010) hypoallergenic (0.0035) shiny (0.0012) silver (-0.0023) plated (-0.0010) fishhook (0.0006) with (0.0006) 10x3. (0.0002) 5mm (-0.0002) ball (0.0073) and (-0.0019) coil (0.0013) with (-0.0005) open (0.0040) loop, (-0.0034) 21 (0.0007) gauge. (0.0071) 100 (0.0023) pairs. (0.0079) ( (0.0020) 200 (0.0017) ). (0.0119) content (0.0273) : (0.0048) surgical (0.0015) steel (0.0016) earring (0.0021) earwires (0.0022) hypoallergenic (0.0031) shiny (-0.0039) silver (-0.0021) plated (-0.0010) fishhook (-0.0007) with (0.0005) 10x3. (0.0054) 5mm (-0.0005) ball (0.0081) and (-0.0046) coil (0.0028) with (-0.0008) open (-0.0015) loop, (0.0029) 21 (-0.0054) gauge. (0.0081) 100 (-0.0064) pairs. (-0.0009) ( (0.0088) 200 (0.0241) ) (0.0123)
~~~~~~
