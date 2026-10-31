# Reference packet: GraphNarrator__Llama-8B__products__32166

- Method: GraphNarrator; configuration: Llama-8B; dataset: products; target node: 32166
- Explanation source: `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/116.json` (messages[assistant])
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
  - Node-1 (motorcycle accessory)
    - Node-1.1 (saddlebag liner)
    - Node-1.2 (battery tender)
    - Node-1.3 (cargo net)
    - Node-1.4 (saddlebag)
    - Node-1.5 (luggage tail bag)
    - Node-1.6 (tank bag)

### Word-Level Evaluation

Keywords with high saliency scores in ROOT — "product" (0.05), "amazon" (0.07), "mounts" (0.04), "adapter" (0.04), "ball" (0.03), "custom" (0.03), "gopro" (0.03) — are associated with product information and mounting accessories. However, these terms are not strongly indicative of a specific product category.

### Graph-Level Aggregation

Node-1 (motorcycle accessory, keywords: "motorcycle" (0.00), "tail" (0.01), "bag" (0.00), "black" (0.00)) is a direct neighbor with moderate saliency, identifying a motorcycle-related product. Indirect neighbors — Node-1.1 (saddlebag liner), Node-1.2 (battery tender), Node-1.3 (cargo net), Node-1.4 (saddlebag), Node-1.5 (luggage tail bag), Node-1.6 (tank bag) — are all motorcycle accessories, collectively confirming a motorcycle context across both hops.

### Free-Text Explanation

The classification of ROOT into "Health & Personal Care" is not strongly supported by its own keywords and the co-purchase neighborhood.

ROOT: Keywords like "product" (0.05), "amazon" (0.07), and "adapter" (0.04) are general product-related terms, but they do not clearly indicate a specific product category.
  - Node-1: A motorcycle accessory (keywords: "motorcycle" (0.00), "tail" (0.01), "bag" (0.00)) is a direct neighbor, but its own keywords do not strongly suggest a connection to Health & Personal Care.
    - Node-1.1 ~ Node-1.6: Saddlebag liners, battery tenders, cargo nets, saddlebags, luggage tail bags, and tank bags are all motorcycle accessories, supporting the motorcycle context but not directly related to Health & Personal Care.

In summary, the keywords in ROOT and the co-purchase neighborhood do not provide strong evidence for the "Health & Personal Care" category. The classification result appears to be incorrect based on the provided verbalized graph.
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/116.json`).

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
<verbalized-graph>ROOT: product(0.05) amazon(0.07) platform(0.01) title(0.03) content(0.04) title(0.03) ram(-0.00) mounts(0.04) 1(0.04) quot(0.01) diameter(-0.01) ball(0.03) custom(0.03) gopro(0.03) hero(-0.02) adapter(0.04) rap-(0.03) b-(0.05) 202u-(0.04) gop1.(0.01) content(0.03) consists(0.05) 1(0.01) diameter(0.04) ball,(0.02) connected(0.04) custom(0.04) go(0.02) pro(0.03) adapteradapter(0.04) attaches(0.04) directly(0.05) side(0.02) camera,(0.03) replacing(0.04) factory(0.04) mounting(0.07) bracketall(-0.00) items(0.04) sold(0.09) individually(0.05) unless(0.01) specifically(0.07) described(0.02) otherwise(-0.01) product(0.06) description(-0.00) 
Node-1: product(-0.00) amazon(0.03) platform(0.01) title(-0.00) content(0.01) title(0.00) cortech(-0.00) super(0.01) 2.(0.01) 0(0.00) 24-(-0.01) liter(0.02) motorcycle(0.00) tail(0.01) bag-(-0.00) black(0.00) size(0.01) 13.(0.01) 4(-0.00) l(0.00) x(0.01) 14.(-0.00) 2(-0.01) w(-0.00) x(0.01) 7.(-0.00) 5(0.00) ".(0.02) content(0.01) 1680(-0.01) denier(-0.00) ballistic(0.00) polyester(0.01) 1800(-0.00) denier(0.00) three-(-0.00) lined(-0.00) twill(-0.00) jacquard(0.00) weave(-0.00) side(0.01) pockets(0.01) polyester(0.00) backingwill(-0.00) mount(0.00) cortech(0.00) 2.(0.00) 0(-0.00) sport(-0.01) saddlebags(0.01) themselvesremovable(-0.00) neoprene(0.01) basetwo-(-0.00) tone(0.01) red(0.00) black(0.01) soft(0.01) interior(0.00) liningquick-(0.01) release(0.00) mounting(-0.00) system(0.00) storage(0.00) pockets(0.02) mounting(-0.00) straps(0.01) useeasy(0.00) access,(-0.00) top(0.00) loading(0.02) main(0.00) compartmentexpandable(0.01) main(0.01) compartment(0.01) snap(0.00) lock(0.01) zippersone-(-0.00) way(-0.00) zipper(0.01) main(0.00) compartment(0.02) zipper(0.01) garage(0.00) concealmenttop(0.00) fap(0.01) internal(-0.00) organizer(0.02) pocketphoslite(0.00) refective(0.01) striping(0.00) logocomfortable(0.00) rubberized(0.00) carrying(0.00) handlecortech(0.00) jacquard(0.01) weave(0.01) shoulder(0.00) straprain(-0.00) cover(0.02) included13.(0.01) 4(-0.01) l(-0.00) x(0.02) 14.(-0.00) 2(-0.00) w(0.01) x(0.01) 7.(0.00) 5(-0.01) 24(-0.01) liter(0.01) 
Node-1.1: product(0.00) amazon(0.00) platform(-0.00) title(0.00) content(0.00) title(-0.00) bestem(0.00) lgka-(0.00) nomad-(0.00) sdl-(0.00) r(0.00) black(0.00) regular(0.00) saddlebag(-0.00) liner(-0.00) kawasaki(-0.00) vulcan(0.00) nomad.(0.00) content(0.00) liners(-0.00) constructed(0.00) high(0.00) quality(0.00) weather-(0.00) resistant(0.00) heavy(0.00) duty(-0.00) 1680d(0.00) nylon.(0.00) bag(0.00) never(0.00) sag(0.00) stay(0.00) shape(0.00) even(0.00) empty(0.00) edges(0.00) enforced(0.00) plastic(0.00) pipes.(-0.00) many(0.00) features(0.00) easy(0.00) carrying(0.00) shoulder(0.00) straps(0.00) heavy(0.00) duty(-0.00) carrying(0.00) handles,(0.00) heavy(0.00) duty(-0.00) water-(0.00) proof(0.00) zippers,(0.00) multiple(0.00) pockets,(0.00) liners(0.00) custom(0.00) made(0.00) fit(0.00) bike(-0.00) pannier(-0.00) system(0.00) like(0.00) glove.(-0.00) 
Node-1.2: product(-0.00) amazon(0.02) platform(-0.00) title(0.01) content(0.00) title(0.01) battery(-0.00) tender(-0.00) 081-(0.00) 0069-(0.00) 8(0.00) female(0.00) cigarette(0.01) adaptor(0.00) quick(0.00) disconnect.(0.01) content(0.00) cig(0.00) adaptor-(0.00) female(0.00) use(0.00) battery(0.00) tender(0.00) quick(0.00) disconnect(0.00) features(0.00) female(0.00) cig(0.00) adaptor(0.00) attaches(0.00) directly(0.00) battery(0.00) motorcycle,(0.00) scooter,(0.00) atv,(0.00) boat(0.00) vehicle.(-0.00) female(0.01) cig(0.00) adaptor(0.01) helps(0.01) recharge(0.01) cell(0.00) phones,(0.00) gps(-0.00) devices(0.01) 12(0.00) volt(0.00) accessories(0.01) charge(0.01) traveling(0.01) vehicle(0.01) rest.(0.00) 
Node-1.3: product(-0.00) amazon(0.01) platform(0.00) title(-0.00) content(0.00) title(-0.01) super(-0.01) strong(0.00) stretch(-0.00) heavy-(-0.00) duty(-0.00) 15(-0.00) quot(0.00) cargo(0.00) net(-0.00) motorcycle(0.01) atv-(-0.00) stretches(-0.01) 45(0.00) quot(0.00) ;.(-0.00) content(-0.00) streamled(0.00) using(-0.00) latex(0.00) material,(0.00) much(-0.00) stronger(-0.00) stretchable(0.00) general(-0.00) rubber!(0.01) see,(0.00) stretched(-0.00) 45(0.00) ".(0.01) motorcycle(-0.00) comes(-0.01) cool(0.00) super(-0.00) cargo(0.00) net!(-0.01) 
Node-1.4: product(-0.00) amazon(0.00) platform(0.00) title(0.00) content(0.00) title(0.00) ogio(0.00) saddlebag(0.00) 110093.(0.00) 36.(0.00) content(0.00) heat-(0.00) resistant(0.00) silicone(0.00) impregnated(0.00) bottomsdual(0.00) zipper(0.00) wide(0.00) mouth(0.00) openingseasy(0.00) attach(0.00) web(0.00) mounting(0.00) systemtextured(0.00) neoprene(0.00) pad(0.00) paint(0.00) protectiontwo(-0.00) molded(0.00) side(0.00) pockets220(0.00) cubic(0.00) inches(0.00) expansion(0.00) volume(0.00) sidetop(0.00) organizer(0.00) pocketintegrated(0.00) rain(0.00) hood420d(0.00) dobby(0.00) nylon(0.00) 600d(0.00) poly(0.00) tarpaulin(0.00) textured(0.00) neoprene(0.00) heat-(0.00) resistant(0.00) silicone10.(0.00) 5inh(0.00) x(0.00) 16inw(0.00) x(0.00) 8ind(0.00) 11ind(0.00) expanded(0.00) 1344(-0.00) c.(-0.00) i.(-0.00) 1848(-0.00) c.(0.00) i.(-0.00) expanded(0.00) weight(0.00) 2.(0.00) 6(0.00) lbs(-0.00) 1.(0.00) 8(0.00) kg(0.00) 
Node-1.5: product(-0.00) amazon(-0.01) platform(-0.00) title(0.01) content(-0.01) title(0.00) dowco(0.00) 50144-(0.01) 00(0.00) fastrax(0.00) elite(0.01) series(-0.00) black(-0.00) sport(0.00) adventure(0.00) tour(0.01) luggage(0.00) tail(0.00) bag.(-0.00) content(0.00) none(-0.00) 
Node-1.6: product(0.00) amazon(0.00) platform(-0.00) title(-0.00) content(0.00) title(0.00) missing.(-0.00) content(0.00) dowco(0.00) fastrax(-0.00) value(-0.00) series(-0.00) tank(-0.00) bag(0.00) magnet(0.00) strap(-0.00) mount(0.00) universally(0.00) fit(0.00) use(0.00) metal(0.00) tanks.(0.00) easy(-0.00) use(-0.00) multi-(-0.00) magnet(0.00) design(0.00) strap(0.00) mounting(-0.00) system(-0.00) features(-0.00) non-(-0.00) skid(0.00) base(-0.00) straps(0.00) ensure(-0.00) firm(0.00) tank(-0.00) positio</verbalized-graph>

### Classification Label
Health & Personal Care

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 32166
- Title: RAM Mounts 1&quot; Diameter Ball with Custom GoPro Hero Adapter RAP-B-202U-GOP1
- True class (canonical `y`): **Electronics**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Sports & Outdoors**
- Prediction recorded by this method's pipeline: **Health & Personal Care**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: RAM Mounts 1&quot; Diameter Ball with Custom GoPro Hero Adapter RAP-B-202U-GOP1. Content: Consists of a 1" diameter ball, connected to a custom Go Pro adapterAdapter attaches directly to the under side of the camera, replacing the factory mounting bracketAll items are sold individually unless specifically described otherwise in the product description
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 6986 | Automotive | "Cortech Super 2.0 24-Liter Motorcycle Tail Bag - Black / Size 13.4'' L x 14.2'' W x 7.5'' D" |

### 2-hop (shortest distance exactly 2): 8 nodes

| node id | true class | title |
|---|---|---|
| 815 | Automotive | Bestem LGKA-NOMAD-SDL-R Black Regular Saddlebag Liner for Kawasaki Vulcan Nomad |
| 6902 | Automotive | Battery Tender 081-0069-8 Female Cigarette Adaptor for Quick Disconnect |
| 6903 | Automotive | Super Strong Stretch Heavy-duty 15&quot; Cargo Net for Motorcycle ATV - Stretches to 45&quot; |
| 6969 | Automotive | OGIO Saddlebag 110093.36 |
| 6981 | Automotive | Dowco 50144-00 Fastrax Elite Series Black Sport and Adventure Tour Luggage Tail Bag |
| 6990 | Automotive | missing |
| 32164 | Automotive | Classic Accessories 73807 MotoGear Motorcycle Indoor Dust Cover, Sport |
| 32165 | Automotive | MotoCentric Mototrek Sport Tail Bag - Black |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/116.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Health & Personal Care**, ground truth = **Electronics**.
The verbalized graph is 8274 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 32166 | 70 | 0.0859 | yes |
| Node-1 | 1 | 6986 | 153 | 0.0259 | yes |
| Node-1.1 | 2 | 815 | 97 | 0.0047 | yes |
| Node-1.2 | 3 | 6902 | 82 | 0.0152 | yes |
| Node-1.3 | 4 | 6903 | 71 | 0.0144 | yes |
| Node-1.4 | 5 | 6969 | 91 | 0.0036 | yes |
| Node-1.5 | 6 | 6981 | 28 | 0.0103 | yes |
| Node-1.6 | 7 | 6990 | 105 | 0.0031 | yes |
| Node-1.7 | 8 | 32164 | 23 | 0.0422 | no |
| Node-1.8 | 9 | 32165 | 179 | 0.0108 | no |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->Node-1.6, Node-1->Node-1.7, Node-1->Node-1.8, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, Node-1.6->Node-1, Node-1.7->Node-1, Node-1.8->Node-1, ROOT->Node-1

### Tokens and scores

**ROOT** (global 32166):

~~~~~~text
product (0.0511) from (0.0072) amazon (0.0731) platform (0.0050) with (0.0186) title (0.0339) and (0.0142) content (0.0372) : (0.0751) title (0.0300) : (0.0516) ram (-0.0007) mounts (0.0388) 1 (0.0359) & (0.0194) quot (0.0068) ; (0.0366) diameter (-0.0065) ball (0.0299) with (0.0440) custom (0.0272) gopro (0.0295) hero (-0.0208) adapter (0.0354) rap- (0.0324) b- (0.0498) 202u- (0.0362) gop1. (0.0086) content (0.0340) : (0.0050) consists (0.0530) of (0.0109) a (0.0176) 1 (0.0088) " (0.0302) diameter (0.0403) ball, (0.0225) connected (0.0423) to (0.0172) a (0.0293) custom (0.0393) go (0.0224) pro (0.0333) adapteradapter (0.0413) attaches (0.0422) directly (0.0484) to (0.0240) the (0.0127) under (0.0194) side (0.0235) of (0.0164) the (0.0205) camera, (0.0299) replacing (0.0377) the (-0.0234) factory (0.0373) mounting (0.0715) bracketall (-0.0012) items (0.0429) are (0.0571) sold (0.0859) individually (0.0454) unless (0.0091) specifically (0.0680) described (0.0207) otherwise (-0.0101) in (-0.0193) the (-0.0081) product (0.0638) description (-0.0049)
~~~~~~

**Node-1** (global 6986):

~~~~~~text
product (-0.0028) from (-0.0169) amazon (0.0259) platform (0.0094) with (-0.0062) title (-0.0046) and (-0.0207) content (0.0071) : (0.0048) title (0.0001) : (-0.0068) " (-0.0086) cortech (-0.0027) super (0.0085) 2. (0.0054) 0 (0.0020) 24- (-0.0052) liter (0.0191) motorcycle (0.0031) tail (0.0108) bag- (-0.0036) black (0.0026) / (0.0039) size (0.0081) 13. (0.0069) 4 (-0.0007) ' (-0.0045) ' (-0.0074) l (0.0020) x (0.0113) 14. (-0.0038) 2 (-0.0053) ' (-0.0077) ' (-0.0072) w (-0.0031) x (0.0098) 7. (-0.0003) 5 (0.0014) ' (-0.0087) ' (-0.0117) d (-0.0042) ". (0.0157) content (0.0083) : (-0.0091) 1680 (-0.0125) denier (-0.0005) ballistic (0.0042) polyester (0.0059) and (-0.0232) 1800 (-0.0003) denier (0.0006) three- (-0.0034) lined (-0.0040) twill (-0.0037) jacquard (0.0032) weave (-0.0049) side (0.0067) pockets (0.0088) with (0.0053) a (-0.0493) polyester (0.0027) backingwill (-0.0017) mount (0.0049) to (-0.0017) cortech (0.0011) 2. (0.0046) 0 (-0.0036) sport (-0.0083) saddlebags (0.0056) or (-0.0066) by (-0.0508) themselvesremovable (-0.0005) neoprene (0.0067) basetwo- (-0.0019) tone (0.0116) red (0.0033) and (-0.0115) black (0.0060) soft (0.0058) interior (0.0027) liningquick- (0.0095) release (0.0048) mounting (-0.0027) system (0.0036) with (-0.0057) storage (0.0013) pockets (0.0245) for (-0.0017) mounting (-0.0009) straps (0.0062) when (-0.0092) not (-0.0050) in (-0.0090) useeasy (0.0002) access, (-0.0024) top (0.0010) loading (0.0162) main (0.0037) compartmentexpandable (0.0084) main (0.0085) compartment (0.0114) with (-0.0086) snap (0.0041) lock (0.0071) zippersone- (-0.0005) way (-0.0011) zipper (0.0121) on (-0.0131) main (0.0001) compartment (0.0179) with (-0.0112) ' (-0.0049) ' (-0.0063) zipper (0.0120) garage (0.0021) ' (-0.0082) ' (-0.0059) for (-0.0064) concealmenttop (0.0034) fap (0.0094) internal (-0.0012) organizer (0.0217) pocketphoslite (0.0033) refective (0.0125) striping (0.0009) and (-0.0165) logocomfortable (0.0019) rubberized (0.0042) carrying (0.0001) handlecortech (0.0048) jacquard (0.0058) weave (0.0112) shoulder (0.0045) straprain (-0.0031) cover (0.0167) included13. (0.0123) 4 (-0.0056) " (0.0155) l (-0.0001) x (0.0172) 14. (-0.0009) 2 (-0.0039) " (0.0025) w (0.0067) x (0.0107) 7. (0.0015) 5 (-0.0052) " (0.0031) d (0.0018) ( (-0.0035) 24 (-0.0075) liter (0.0091) ) (-0.0186)
~~~~~~

**Node-1.1** (global 815):

~~~~~~text
product (0.0047) from (0.0029) amazon (0.0009) platform (-0.0027) with (0.0036) title (0.0013) and (0.0007) content (0.0032) : (0.0036) title (-0.0001) : (0.0001) bestem (0.0027) lgka- (0.0005) nomad- (0.0007) sdl- (0.0000) r (0.0019) black (0.0043) regular (0.0028) saddlebag (-0.0003) liner (-0.0018) for (0.0037) kawasaki (-0.0035) vulcan (0.0023) nomad. (0.0003) content (0.0042) : (0.0023) these (0.0017) liners (-0.0008) are (0.0010) constructed (0.0005) from (-0.0006) high (0.0011) quality (0.0030) weather- (0.0005) resistant (0.0029) heavy (0.0011) duty (-0.0013) 1680d (0.0009) nylon. (0.0015) the (0.0000) bag (0.0015) will (-0.0000) never (0.0011) sag (0.0004) and (0.0019) will (0.0008) stay (0.0001) in (0.0010) shape (0.0013) even (0.0013) empty (0.0007) as (0.0010) all (0.0008) edges (0.0014) are (-0.0001) enforced (0.0012) with (-0.0005) plastic (0.0012) pipes. (-0.0024) with (0.0012) so (-0.0015) many (0.0002) features (0.0030) such (0.0002) as (0.0013) easy (0.0014) carrying (0.0008) shoulder (0.0035) straps (0.0014) and (0.0001) heavy (0.0016) duty (-0.0002) carrying (0.0005) handles, (0.0007) heavy (0.0012) duty (-0.0000) water- (0.0003) proof (0.0013) zippers, (0.0007) multiple (0.0018) pockets, (0.0002) these (0.0007) liners (0.0000) are (0.0005) custom (0.0029) made (0.0011) to (-0.0004) fit (0.0020) each (0.0014) bike (-0.0017) ' (0.0032) s (0.0022) pannier (-0.0009) system (0.0010) like (0.0013) a (-0.0013) glove. (-0.0016)
~~~~~~

**Node-1.2** (global 6902):

~~~~~~text
product (-0.0023) from (-0.0048) amazon (0.0152) platform (-0.0027) with (-0.0011) title (0.0082) and (-0.0024) content (0.0013) : (0.0035) title (0.0098) : (0.0075) battery (-0.0015) tender (-0.0002) 081- (0.0035) 0069- (0.0033) 8 (0.0028) female (0.0027) cigarette (0.0077) adaptor (0.0026) for (0.0027) quick (0.0046) disconnect. (0.0056) content (0.0035) : (0.0009) cig (0.0013) adaptor- (0.0042) female (0.0028) for (0.0062) use (0.0037) with (0.0031) battery (0.0014) tender (0.0026) quick (0.0047) disconnect (0.0024) features (0.0000) a (0.0057) female (0.0033) cig (0.0015) adaptor (0.0021) that (0.0028) attaches (0.0012) directly (0.0008) to (0.0013) the (-0.0030) battery (0.0039) of (-0.0000) the (0.0006) motorcycle, (0.0011) scooter, (0.0029) atv, (0.0021) boat (0.0046) or (0.0080) other (0.0031) vehicle. (-0.0048) the (0.0046) female (0.0061) cig (0.0036) adaptor (0.0056) helps (0.0051) to (0.0069) recharge (0.0057) cell (0.0037) phones, (0.0048) gps (-0.0033) devices (0.0091) or (0.0067) other (0.0047) 12 (0.0031) volt (0.0046) accessories (0.0105) and (0.0082) charge (0.0060) them (0.0071) while (0.0076) traveling (0.0092) or (0.0083) when (0.0099) the (0.0011) vehicle (0.0082) is (0.0099) at (0.0079) rest. (0.0027)
~~~~~~

**Node-1.3** (global 6903):

~~~~~~text
product (-0.0022) from (-0.0030) amazon (0.0060) platform (0.0002) with (-0.0009) title (-0.0047) and (-0.0025) content (0.0035) : (0.0003) title (-0.0057) : (0.0008) super (-0.0086) strong (0.0005) stretch (-0.0044) heavy- (-0.0003) duty (-0.0016) 15 (-0.0003) & (0.0004) quot (0.0014) ; (0.0039) cargo (0.0007) net (-0.0006) for (0.0070) motorcycle (0.0144) atv- (-0.0002) stretches (-0.0063) to (0.0002) 45 (0.0007) & (0.0012) quot (0.0018) ;. (-0.0009) content (-0.0014) : (-0.0038) we (-0.0020) ( (-0.0013) streamled (0.0033) ) (-0.0018) are (0.0016) using (-0.0011) latex (0.0010) as (-0.0003) material, (0.0004) much (-0.0002) stronger (-0.0016) and (-0.0002) more (-0.0005) stretchable (0.0008) than (-0.0025) the (-0.0056) general (-0.0011) rubber! (0.0099) as (-0.0046) you (0.0005) see, (0.0001) it (-0.0003) can (0.0015) be (0.0006) stretched (-0.0043) to (0.0005) about (-0.0047) 45 (0.0045) ". (0.0066) your (-0.0113) motorcycle (-0.0021) comes (-0.0105) cool (0.0026) with (-0.0026) this (-0.0026) super (-0.0003) cargo (0.0041) net! (-0.0051)
~~~~~~

**Node-1.4** (global 6969):

~~~~~~text
product (-0.0015) from (-0.0022) amazon (0.0023) platform (0.0013) with (-0.0017) title (0.0013) and (-0.0019) content (0.0008) : (0.0025) title (0.0004) : (-0.0004) ogio (0.0002) saddlebag (0.0009) 110093. (0.0010) 36. (0.0028) content (0.0014) : (0.0005) heat- (0.0003) resistant (0.0009) silicone (0.0005) impregnated (0.0005) bottomsdual (0.0004) zipper (0.0027) wide (0.0012) mouth (0.0002) openingseasy (0.0004) attach (0.0013) web (0.0022) mounting (0.0006) systemtextured (0.0012) neoprene (0.0003) pad (0.0016) for (0.0005) paint (0.0002) protectiontwo (-0.0001) molded (0.0033) side (0.0011) pockets220 (0.0015) cubic (0.0013) inches (0.0012) of (-0.0002) expansion (0.0026) volume (0.0009) on (-0.0006) each (0.0007) sidetop (0.0014) organizer (0.0034) pocketintegrated (0.0015) rain (0.0019) hood420d (0.0005) dobby (0.0000) nylon (0.0023) / (0.0015) 600d (0.0011) poly (0.0011) / (0.0009) tarpaulin (0.0000) / (0.0011) textured (0.0010) neoprene (0.0005) / (0.0005) heat- (0.0004) resistant (0.0010) silicone10. (0.0008) 5inh (0.0005) x (0.0006) 16inw (0.0002) x (0.0003) 8ind (0.0007) ( (-0.0004) 11ind (0.0005) expanded (0.0008) ) (0.0017) 1344 (-0.0002) c. (-0.0003) i. (-0.0029) ( (0.0026) 1848 (-0.0012) c. (0.0013) i. (-0.0002) expanded (0.0008) ) (0.0005) weight (0.0003) : (0.0001) 2. (0.0002) 6 (0.0003) lbs (-0.0028) / (0.0003) 1. (0.0004) 8 (0.0005) kg (0.0036)
~~~~~~

**Node-1.5** (global 6981):

~~~~~~text
product (-0.0038) from (0.0041) amazon (-0.0050) platform (-0.0044) with (0.0011) title (0.0054) and (-0.0006) content (-0.0055) : (0.0070) title (0.0036) : (0.0038) dowco (0.0028) 50144- (0.0056) 00 (0.0004) fastrax (0.0026) elite (0.0103) series (-0.0010) black (-0.0015) sport (0.0021) and (-0.0020) adventure (0.0005) tour (0.0055) luggage (0.0041) tail (0.0019) bag. (-0.0020) content (0.0012) : (0.0043) none (-0.0034)
~~~~~~

**Node-1.6** (global 6990):

~~~~~~text
product (0.0000) from (-0.0021) amazon (0.0011) platform (-0.0006) with (0.0007) title (-0.0006) and (-0.0012) content (0.0003) : (0.0014) title (0.0020) : (-0.0007) missing. (-0.0003) content (0.0017) : (0.0004) dowco (0.0008) fastrax (-0.0004) value (-0.0021) series (-0.0019) tank (-0.0016) bag (0.0009) with (0.0025) magnet (0.0018) and (-0.0005) strap (-0.0001) mount (0.0015) is (0.0015) universally (0.0001) fit (0.0002) for (-0.0003) use (0.0004) with (0.0005) most (-0.0012) metal (0.0004) tanks. (0.0018) easy (-0.0011) to (-0.0002) use (-0.0004) multi- (-0.0005) magnet (0.0012) design (0.0003) and (-0.0006) strap (0.0001) mounting (-0.0013) system (-0.0003) features (-0.0000) a (0.0001) non- (-0.0002) skid (0.0007) base (-0.0006) and (-0.0011) straps (0.0018) to (-0.0004) ensure (-0.0005) a (-0.0015) firm (0.0009) tank (-0.0007) position (-0.0014) and (-0.0008) avoid (-0.0002) abrasion (0.0001) to (-0.0001) the (-0.0018) tank. (0.0008) the (-0.0010) method (-0.0015) you (0.0013) choose (0.0023) to (0.0010) store (0.0031) your (-0.0039) ride (0.0009) and (-0.0021) gear (0.0021) is (0.0004) a (-0.0019) critical (-0.0006) decision. (-0.0026) storing (0.0026) it (-0.0013) outdoor, (-0.0017) indoor (0.0005) or (-0.0006) both, (0.0000) factors (0.0016) like (0.0010) waterproof (0.0008) and (-0.0007) water (0.0006) resistant (0.0005) options (-0.0010) must (-0.0012) be (-0.0006) considered (-0.0014) ; (0.0003) you (-0.0002) also (0.0007) need (-0.0000) to (-0.0006) think (0.0013) about (0.0008) fade (0.0003) resistance (0.0008) and (0.0002) security (0.0010) factors. (0.0016)
~~~~~~

**Node-1.7** (global 32164):

~~~~~~text
product (0.0231) from (0.0017) amazon (0.0038) platform (-0.0082) with (-0.0045) title (0.0151) and (0.0008) content (-0.0173) : (0.0263) title (0.0111) : (0.0209) classic (0.0326) accessories (0.0134) 73807 (0.0270) motogear (0.0117) motorcycle (0.0422) indoor (-0.0383) dust (0.0200) cover, (0.0247) sport. (-0.0012) content (0.0189) : (0.0071) none (-0.0223)
~~~~~~

**Node-1.8** (global 32165):

~~~~~~text
product (0.0003) from (-0.0028) amazon (-0.0019) platform (0.0014) with (-0.0017) title (0.0006) and (0.0000) content (0.0006) : (-0.0006) title (0.0011) : (0.0006) motocentric (0.0016) mototrek (0.0018) sport (-0.0000) tail (0.0016) bag- (-0.0005) black. (0.0013) content (0.0020) : (-0.0024) there (0.0001) are (-0.0002) also (-0.0008) quick (-0.0018) release (-0.0007) buckles (-0.0008) attached (0.0006) to (0.0004) this (0.0011) bag (0.0040) that (-0.0001) also (0.0013) can (0.0002) be (0.0017) used (0.0004) with (0.0011) motocentric (0.0010) ' (-0.0007) s (0.0013) sport (-0.0027) saddlebags (-0.0021) to (0.0012) create (0.0017) a (0.0002) " (-0.0016) full (0.0012) matching (0.0019) luggage (-0.0042) set (0.0029) ". (-0.0001) this (0.0010) is (0.0018) a (-0.0015) piece (0.0027) of (0.0012) luggage (-0.0044) made (0.0015) with (0.0008) the (-0.0030) highest (-0.0009) quality (0.0000) materials (0.0008) and (-0.0012) accessories. (-0.0005) all (0.0013) motocentric (0.0008) luggage (-0.0042) come (0.0020) with (-0.0010) a (-0.0017) " (-0.0024) lifetime (0.0015) warranty (-0.0000) ". (-0.0016) dimensions (0.0065) : (-0.0030) 8 (0.0016) " (-0.0035) h (0.0012) x (0.0021) 13 (-0.0000) " (-0.0008) w (0.0023) x (0.0017) 16. (0.0004) 5 (0.0012) inch (0.0025) l (0.0023) / (0.0028) 8 (0.0008) inch (0.0032) h (0.0033) x (0.0019) 13 (0.0007) " (0.0017) w (0.0026) x (0.0018) 22. (0.0021) 5 (-0.0006) " (0.0024) l (0.0003) expanded (0.0035) capacity (0.0045) : (0.0011) holds (0.0065) 23 (-0.0002) liters (0.0017) / (0.0018) 29 (-0.0008) liters (0.0018) expanded (0.0010) 1680d (0.0006) maxtura (0.0016) & (-0.0021) # (0.0019) 0153 (0.0011) ; (0.0055) ballistic (0.0047) construction (0.0036) for (0.0002) durability (0.0001) soft (0.0001) interior (-0.0004) lining (0.0004) built- (-0.0003) in (-0.0003) bungee (0.0009) cord (-0.0000) hooks (-0.0004) hide (0.0024) away (0.0008) when (0.0001) not (0.0002) in (-0.0013) use (0.0010) detailed (-0.0007) organizer (0.0031) duraflex (-0.0002) buckles (0.0022) for (0.0019) added (0.0008) strength (0.0012) fits (0.0003) most (0.0108) 17 (-0.0036) " (0.0107) laptops (-0.0029) reflect- (-0.0006) a- (-0.0019) light (0.0029) & (-0.0021) # (0.0005) 0153 (0.0030) ; (0.0045) reflective (0.0045) piping (0.0018) customized (0.0048) carrying (0.0006) handle (0.0025) includes (-0.0011) shoulder (0.0029) strap (0.0015) rain (0.0017) cover (0.0008) included (-0.0013) removable (0.0009) protective (-0.0006) base (0.0020) four (-0.0011) quick (0.0021) release (0.0018) attachment (0.0001) side (0.0006) straps (0.0041) to (-0.0016) attach (0.0026) to (0.0003) mototrek (0.0019) sport (0.0049) saddlebags (0.0050)
~~~~~~
