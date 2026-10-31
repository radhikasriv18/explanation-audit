# Reference packet: GraphNarrator__Llama-8B__products__38815

- Method: GraphNarrator; configuration: Llama-8B; dataset: products; target node: 38815
- Explanation source: `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/145.json` (messages[assistant])
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

- ROOT (flashlight)
  - Node-1 (keychain flashlight)
    - Node-1.1 (sewing kit)
    - Node-1.2 (pepper spray)

### Word-Level Evaluation:

Keywords with high saliency scores in ROOT — "quark" (0.02), "series" (0.03), "array" (0.04), "options" (0.01), "accessories" (0.01), "interchangeability" (0.00), "waterproof" (0.03), "constructed" (0.02), "aircraft-grade" (0.03), "aluminum" (0.00), "impact-resistant" (0.03), "lenses" (0.03), "lights" (0.00), "tough" (0.05), "enough" (0.02), "challenge" (0.04) — are strongly associated with lighting equipment. However, these keywords are not as indicative of a specific category as those in the classification label "Beauty".

### Graph-Level Aggregation:

Node-1 (keychain flashlight, keywords: "light" (0.01), "nano" (0.02), "keychain" (0.00), "flashlight" (0.01)) is a direct neighbor with moderate saliency, identifying a type of flashlight. Indirect neighbors — Node-1.1 (sewing kit), Node-1.2 (pepper spray) — are unrelated to the category "Beauty".

### Free-Text Explanation

The classification of ROOT into "Beauty" is not strongly supported by its own keywords and the co-purchase neighborhood.

ROOT: Keywords like "quark" (0.02) and "series" (0.03) suggest a product line, but they do not clearly identify a beauty-related product.
  - Node-1: A keychain flashlight (keywords: "light" (0.01), "nano" (0.02), "keychain" (0.00), "flashlight" (0.01)) is a type of flashlight, which is not typically classified under "Beauty".
    - Node-1.1 ~ Node-1.2: A sewing kit and a pepper spray are unrelated to the category "Beauty".

In summary, ROOT's own keywords and the co-purchase neighborhood do not strongly support the "Beauty" category. The keywords in ROOT are more indicative of a lighting product, and the indirect neighbors are unrelated to beauty products.
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/145.json`).

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
<verbalized-graph>ROOT: product(0.02) amazon(0.01) platform(-0.01) title(0.03) content(0.06) title(0.05) foursevens(0.01) quark(0.02) aa(-0.00) sup2(0.00) pro(0.02) qp2a-(0.01) x(0.02) black(0.02) finish(0.00) cool(0.01) white(0.01) led(-0.01) 2xaa(0.01) 280(0.03) lumens.(-0.02) content(0.06) quark(0.01) series(0.03) offers(0.01) staggering(0.01) array(0.04) options,(0.01) accessories(0.01) interchangeability.(0.00) wide(-0.00) range(0.01) led,(0.00) battery(-0.00) clip(-0.01) choices,(0.02) get(0.01) features(0.00) want(-0.01) without(0.00) compromise.(0.01) waterproof(0.03) constructed(0.02) aircraft-(0.01) grade(0.03) aluminum(0.00) impact-(0.02) resistant(0.03) lenses,(0.03) quark(0.01) lights(0.00) tough(0.05) enough(0.02) meet(0.00) challenge.(0.04) 
Node-1: product(0.01) amazon(-0.00) platform(0.01) title(0.01) content(0.01) title(0.01) streamlight(0.00) 73001(0.01) nano(0.02) light(0.00) miniature(0.00) keychain(0.00) led(0.01) flashlight,(-0.00) black.(0.00) content(0.00) extremely(0.00) small(0.00) super-(0.01) bright(0.00) light,(0.00) streamlight(0.01) nano(0.02) light(-0.00) keychain(-0.00) flashlight(0.01) lightweight,(0.00) easy-(0.00) to-(0.00) access(0.01) flashlight(0.01) everyday(0.00) tasks(0.01) work(0.00) home.(-0.00) nonrotating(0.00) snap(0.00) hook(-0.00) attaching(0.00) key(0.00) rings,(0.00) backpacks,(0.00) clothing,(0.00) more,(0.00) nano(0.01) light(0.00) features(0.00) high-(0.00) intensity,(0.00) 100,(0.00) 000-(0.00) hour(0.00) led(0.00) last(-0.00) eight(-0.00) hours(-0.00) four(-0.00) alkaline(0.00) button(0.00) cell(0.00) batteries(0.00) included(-0.00) ).(-0.02) nano(0.02) lightkeychain(0.01) flashlightat(-0.00) glance(0.01) small(0.00) lightweight(-0.01) keychain(0.00) lightrotating(0.01) head(0.01) switchbright(0.01) powerful(0.00) 100,(0.00) 000-(0.00) hour(0.00) lednonrotating(0.01) snap(0.01) hook(0.00) attaches(0.00) detaches(0.00) quickly(0.01) one(0.00) handdurable(0.01) construction(0.01) extended(0.01) uselimited(0.01) lifetime(0.01) warrantya(0.00) snap(0.01) hook(0.01) easily(0.00) attaches(0.00) detaches(0.00) one(0.00) hand.(0.01) view(0.01) larger.(0.01) though(0.00) less(0.01) 2(0.00) inches(0.01) long,(0.00) flashlight(0.01) produce(0.00) continuous(-0.00) light(0.00) eight(0.00) hours.(0.00) view(-0.00) larger.(0.00) powerful(0.00) performance(-0.00) petite(0.02) packageat(0.00) just.(0.00) 36(-0.00) ounces(-0.01) 1.(0.00) 47(0.00) inches(0.01) long,(0.00) streamlight(0.00) nano(0.02) light(0.00) keychain(0.00) flashlight(0.01) ideal(0.01) carrying(0.01) key(0.00) ring(0.00) storing(0.02) pocket,(0.01) glove(-0.00) compartment,(0.00) purse,(0.01) backpack,(0.01) tool(0.00) bag.(0.00) powered(-0.01) four(0.00) iec-(0.01) lr41(0.00) coin(0.01) cells(0.01) included(-0.02) ),(-0.01) nanolight(0.01) produces(-0.01) 10(-0.00) lumens(-0.00) light(0.01) battery(0.01) run(0.00) time(0.00) eight(0.00) hours.(0.00) advantages(0.00) led(0.01) lightan(0.01) led(0.01) ideal(0.03) lights(-0.00) used(-0.00) often(0.01) extended(0.00) period(0.00) time.(0.01) worry(0.01) breaking(0.00) light,(-0.01) since(-0.00) glass(0.00) filament,(-0.00) rarely(0.00) replace(-0.01) leds(-0.00) last(-0.00) lifetime.(-0.00) save(-0.02) time(0.01) money(0.01) batteries(-0.00) well--(-0.01) last(0.02) much(0.01) longer(-0.01) 
Node-1.1: product(0.01) amazon(0.01) platform(0.00) title(0.00) content(0.01) title(0.01) singer(-0.00) sewing(-0.01) kit(-0.00) egg(0.01) shaped(0.00) storage(0.00) case.(0.00) content(0.01) singer(0.00) sewing(-0.00) kit(0.00) small(0.00) reusable,(0.00) colorful(0.00) stylish(0.00) egg(0.01) shaped(0.00) plastic(0.01) box(0.00) great(0.00) travel(0.01) sewing(-0.01) kit(-0.00) quick(0.01) easy(0.01) repairs.(-0.00) storage(0.00) box(0.01) helps(0.01) keep(0.00) everything(0.01) need(0.00) small(0.00) container(0.01) easily(0.01) fits(0.01) purse,(0.01) briefcase(0.01) luggage.(-0.00) kit(-0.00) includes(-0.00) small(0.00) scissor,(-0.00) 25-(0.00) inch(0.00) tape(0.00) measure,(0.00) 1(0.00) needle(0.00) threaders,(0.00) 3(0.00) needles,(0.00) 2(0.00) safety(-0.00) pins,(0.01) 3(0.00) straight(0.01) pins,(0.01) 4(0.00) buttons(0.01) 10(0.00) spools(0.01) assorted(0.01) colors(0.01) polyester(0.00) thread-(0.00) 3-(0.00) yards(-0.01) 
Node-1.2: product(0.00) amazon(0.00) platform(0.00) title(0.00) content(0.00) title(0.00) cold(0.00) steel(0.00) inferno.(-0.00) 38(0.00) oz.(-0.00) keyring(0.00) hardcase(0.00) unit(-0.00) pepper(-0.00) spray.(0.00) content(0.00) inferno(0.00) new(0.00) pepper(0.00) canister(0.00) weapon(-0.00) cold(0.00) steel(0.00) turn(-0.00) biggest,(0.00) meanest,(0.00) violent(0.00) criminal(-0.00) helpless(0.00) molten(0.00) wax(0.00) feet.(0.00) unlike(-0.00) pepper(-0.00) sprays(0.00) may(0.00) heard(0.00) about,(0.00) inferno(0.00) deploys(0.00) highly(0.00) targetable(0.00) foam(0.00) contains(0.00) 8(-0.00) oleoresin(0.00) capsicum(-0.00) 2(-0.00) black(0.00) pepper.(-0.00) dissolves(-0.00) liquid(0.00) contact(0.00) liquefaction(0.00) effect(0.00) tactically(0.00) important,(0.00) since(0.00) sprays(0.00) remain(0.00) foamy(-0.00) "-(0.00) like(0.00) pie(0.00) face-(-0.00) make(0.00) possible(0.00) assailant(-0.00) wipe(0.00) foam(-0.00) face(-0.00) chuck(0.00) ).(0.00) one(0.00) good(0.00) shot(0.00) face(0.00) inferno(-0.00) dilate(0.00) capillaries(0.00) eyes(0.00) causing(0.00) temporary(0.00) blindness.(0.00) induce(-0.00) choking,(0.00) coughing(0.00) nausea(0.00) importantly(-0.00) trigger(-0.00) immediate(0.00) massive(0.00) sneeze(0.00) reflex(0.00) due(0.00) atomized(0.00) black(0.00) pepper(0.00) particles(0.00) drag(0.00) super(0.00) hot(0.00) habanero(0.00) chili(0.00) extract(0.00) deep(-0.00) mucous(0.00) membranes(0.00) sinus(0.00) cavities(0.00) nose,(0.00) throat(0.00) lungs(0.00) causing(0.00) swell(0.00) prevent(0.00) desperate(0.00) life(0.00) support(0.00) breathing.(0.00) short(0.00) inferno(-0.00) melt(0.00) attacker(0.00) ground(0.00) leave(0.00) totally(0.00) incapacitated(0.00) considerable(0.00) period(-0.</verbalized-graph>

### Classification Label
Beauty

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 38815
- Title: FOURSEVENS Quark AA&sup2;/ Pro QP2A-X Black Finish / Cool White LED; 2XAA; 280 Lumens
- True class (canonical `y`): **Tools & Home Improvement**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Tools & Home Improvement**
- Prediction recorded by this method's pipeline: **Beauty**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: FOURSEVENS Quark AA&sup2;/ Pro QP2A-X Black Finish / Cool White LED; 2XAA; 280 Lumens. Content: The Quark series offers a staggering array of options, accessories and interchangeability. With a wide range of LED, battery and clip choices, you get the features you want without compromise. Waterproof and constructed with aircraft-grade aluminum and impact-resistant lenses, Quark lights are tough enough to meet any challenge.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 8935 | Tools & Home Improvement | Streamlight 73001 Nano Light Miniature Keychain LED Flashlight, Black |

### 2-hop (shortest distance exactly 2): 5 nodes

| node id | true class | title |
|---|---|---|
| 1053 | Arts, Crafts & Sewing | Singer Sewing Kit in Egg Shaped Storage Case |
| 38813 | Sports & Outdoors | Cold Steel Inferno .38 oz. Keyring Hardcase Unit Pepper Spray |
| 38814 | Sports & Outdoors | Kelty Redwing 50 Internal Frame Pack (Black, Small/Medium -14.5 - 18.5-Inch Torso) |
| 38816 | Tools & Home Improvement | MECO(TM) Mini CREE Led Flashlight Torch Adjustable Zoom Light Lamp |
| 38817 | Sports & Outdoors | Light My Fire Swedish Firesteel Mini 1,500 Strike Ultralight Fire Starter |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/145.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Beauty**, ground truth = **Tools & Home Improvement**.
The verbalized graph is 8753 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 38815 | 84 | 0.0624 | yes |
| Node-1 | 1 | 8935 | 291 | 0.0318 | yes |
| Node-1.1 | 2 | 1053 | 114 | 0.0141 | yes |
| Node-1.2 | 3 | 38813 | 247 | 0.0051 | yes |
| Node-1.3 | 4 | 38814 | 84 | 0.0158 | no |
| Node-1.4 | 5 | 38816 | 99 | 0.0197 | no |
| Node-1.5 | 6 | 38817 | 126 | 0.0078 | no |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, ROOT->Node-1

### Tokens and scores

**ROOT** (global 38815):

~~~~~~text
product (0.0173) from (-0.0246) amazon (0.0056) platform (-0.0106) with (0.0236) title (0.0302) and (-0.0138) content (0.0554) : (0.0499) title (0.0471) : (0.0071) foursevens (0.0139) quark (0.0176) aa (-0.0002) & (0.0197) sup2 (0.0026) ; (0.0194) / (-0.0056) pro (0.0179) qp2a- (0.0100) x (0.0154) black (0.0215) finish (0.0028) / (0.0020) cool (0.0097) white (0.0054) led (-0.0105) ; (0.0102) 2xaa (0.0120) ; (0.0111) 280 (0.0255) lumens. (-0.0176) content (0.0624) : (0.0417) the (-0.0200) quark (0.0051) series (0.0293) offers (0.0081) a (0.0115) staggering (0.0082) array (0.0446) of (0.0252) options, (0.0142) accessories (0.0055) and (0.0329) interchangeability. (0.0020) with (-0.0026) a (-0.0234) wide (-0.0007) range (0.0125) of (0.0124) led, (0.0028) battery (-0.0036) and (0.0227) clip (-0.0061) choices, (0.0156) you (-0.0358) get (0.0150) the (-0.0204) features (0.0040) you (-0.0045) want (-0.0054) without (0.0009) compromise. (0.0081) waterproof (0.0268) and (-0.0058) constructed (0.0239) with (0.0128) aircraft- (0.0113) grade (0.0269) aluminum (0.0003) and (0.0120) impact- (0.0233) resistant (0.0295) lenses, (0.0262) quark (0.0113) lights (0.0025) are (-0.0135) tough (0.0453) enough (0.0167) to (0.0156) meet (0.0036) any (-0.0021) challenge. (0.0416)
~~~~~~

**Node-1** (global 8935):

~~~~~~text
product (0.0093) from (-0.0026) amazon (-0.0014) platform (0.0138) with (0.0019) title (0.0111) and (-0.0010) content (0.0051) : (0.0126) title (0.0072) : (-0.0001) streamlight (0.0049) 73001 (0.0095) nano (0.0171) light (0.0010) miniature (0.0038) keychain (0.0021) led (0.0055) flashlight, (-0.0018) black. (0.0032) content (0.0040) : (-0.0166) an (0.0042) extremely (0.0022) small (0.0034) and (0.0019) super- (0.0059) bright (0.0027) light, (0.0043) the (-0.0106) streamlight (0.0063) nano (0.0230) light (-0.0020) keychain (-0.0002) flashlight (0.0148) is (-0.0053) a (-0.0054) lightweight, (0.0007) easy- (0.0029) to- (0.0006) access (0.0067) flashlight (0.0110) for (-0.0013) everyday (0.0041) tasks (0.0079) at (0.0012) work (0.0042) or (0.0004) at (0.0024) home. (-0.0020) with (-0.0040) a (0.0002) nonrotating (0.0031) snap (0.0043) hook (-0.0023) for (-0.0006) attaching (0.0026) to (-0.0010) key (0.0046) rings, (0.0035) backpacks, (0.0028) clothing, (0.0047) and (0.0099) more, (0.0029) the (-0.0008) nano (0.0137) light (0.0022) features (0.0027) a (0.0048) high- (0.0017) intensity, (0.0025) 100, (0.0006) 000- (0.0019) hour (0.0025) led (0.0024) that (0.0006) will (0.0019) last (-0.0005) up (-0.0038) to (0.0024) eight (-0.0020) hours (-0.0014) on (0.0007) four (-0.0019) alkaline (0.0035) button (0.0022) cell (0.0039) batteries (0.0008) ( (-0.0099) included (-0.0031) ). (-0.0227) nano (0.0181) lightkeychain (0.0082) flashlightat (-0.0009) a (0.0118) glance (0.0073) : (0.0124) small (0.0034) and (-0.0007) lightweight (-0.0104) keychain (0.0027) lightrotating (0.0057) on (0.0042) / (0.0038) off (0.0002) head (0.0053) switchbright (0.0144) and (0.0005) powerful (0.0029) 100, (0.0020) 000- (0.0001) hour (0.0041) lednonrotating (0.0066) snap (0.0055) hook (0.0015) attaches (0.0023) and (0.0002) detaches (0.0049) quickly (0.0064) with (-0.0031) one (0.0040) handdurable (0.0069) construction (0.0115) for (-0.0023) extended (0.0090) uselimited (0.0112) lifetime (0.0054) warrantya (0.0018) snap (0.0065) hook (0.0050) easily (0.0016) attaches (0.0036) and (0.0008) detaches (0.0049) with (-0.0002) one (0.0044) hand. (0.0057) view (0.0119) larger. (0.0145) though (0.0046) less (0.0061) than (0.0081) 2 (0.0034) inches (0.0120) long, (0.0004) this (0.0043) flashlight (0.0103) can (0.0009) produce (0.0029) continuous (-0.0014) light (0.0017) for (0.0023) up (-0.0009) to (0.0035) eight (0.0045) hours. (0.0019) view (-0.0026) larger. (0.0012) powerful (0.0036) performance (-0.0003) in (-0.0004) a (0.0009) petite (0.0205) packageat (0.0010) just. (0.0005) 36 (-0.0004) ounces (-0.0087) and (0.0028) 1. (0.0039) 47 (0.0007) inches (0.0069) long, (0.0012) the (-0.0007) streamlight (0.0033) nano (0.0181) light (0.0014) keychain (0.0030) flashlight (0.0072) is (-0.0019) ideal (0.0065) for (0.0055) carrying (0.0081) on (0.0008) your (0.0007) key (0.0049) ring (0.0011) or (-0.0016) storing (0.0171) in (0.0045) your (0.0000) pocket, (0.0060) glove (-0.0021) compartment, (0.0037) purse, (0.0064) backpack, (0.0070) or (-0.0075) tool (0.0045) bag. (0.0022) powered (-0.0078) by (-0.0012) four (0.0011) iec- (0.0142) lr41 (0.0013) coin (0.0053) cells (0.0101) ( (0.0028) included (-0.0204) ), (-0.0097) the (0.0111) nanolight (0.0104) produces (-0.0081) 10 (-0.0019) lumens (-0.0002) of (0.0025) light (0.0085) with (0.0020) a (0.0037) battery (0.0085) run (0.0030) time (0.0031) of (0.0038) up (0.0039) to (0.0085) eight (0.0025) hours. (0.0044) the (0.0057) advantages (0.0021) of (0.0187) led (0.0070) lightan (0.0121) led (0.0053) is (0.0023) ideal (0.0318) for (-0.0096) lights (-0.0023) that (-0.0069) are (-0.0105) used (-0.0004) often (0.0131) and (0.0035) over (0.0074) an (0.0014) extended (0.0037) period (0.0018) of (0.0043) time. (0.0067) you (0.0091) don (0.0087) ' (0.0026) t (0.0035) have (-0.0003) to (0.0022) worry (0.0078) about (-0.0007) breaking (0.0022) the (0.0010) light, (-0.0061) since (-0.0019) there (0.0019) is (0.0053) no (0.0051) glass (0.0030) or (0.0011) filament, (-0.0005) and (-0.0044) you (0.0206) rarely (0.0007) have (0.0064) to (0.0021) replace (-0.0080) leds (-0.0016) because (-0.0096) they (0.0011) can (-0.0086) last (-0.0002) a (-0.0157) lifetime. (-0.0014) save (-0.0175) time (0.0136) and (0.0134) money (0.0089) on (0.0239) batteries (-0.0018) as (-0.0072) well-- (-0.0146) they (0.0105) will (0.0201) last (0.0182) much (0.0123) longer (-0.0056) with (0.0136)
~~~~~~

**Node-1.1** (global 1053):

~~~~~~text
product (0.0141) from (0.0056) amazon (0.0096) platform (0.0021) with (0.0075) title (0.0028) and (0.0077) content (0.0105) : (0.0025) title (0.0134) : (-0.0003) singer (-0.0012) sewing (-0.0071) kit (-0.0007) in (0.0035) egg (0.0087) shaped (0.0027) storage (0.0045) case. (0.0005) content (0.0050) : (0.0038) the (0.0032) singer (0.0034) sewing (-0.0010) kit (0.0013) in (0.0037) a (0.0066) small (0.0049) reusable, (0.0033) colorful (0.0043) and (0.0113) stylish (0.0035) egg (0.0059) shaped (0.0039) plastic (0.0084) box (0.0043) is (0.0037) a (0.0079) great (0.0027) travel (0.0056) sewing (-0.0075) kit (-0.0025) for (0.0064) quick (0.0082) and (0.0066) easy (0.0080) repairs. (-0.0035) the (0.0057) storage (0.0024) box (0.0077) helps (0.0065) to (0.0043) keep (0.0049) everything (0.0059) you (0.0006) need (0.0039) in (0.0044) a (-0.0040) small (0.0046) container (0.0056) that (0.0066) easily (0.0076) fits (0.0072) in (0.0023) you (-0.0034) purse, (0.0052) briefcase (0.0070) or (0.0044) luggage. (-0.0028) each (0.0074) kit (-0.0007) includes (-0.0007) a (-0.0046) small (0.0047) scissor, (-0.0006) 25- (0.0010) inch (0.0039) tape (0.0017) measure, (0.0010) ( (0.0058) 1 (0.0018) ) (-0.0031) needle (0.0011) threaders, (0.0031) ( (0.0068) 3 (0.0050) ) (-0.0003) needles, (0.0034) ( (0.0042) 2 (0.0029) ) (0.0046) safety (-0.0001) pins, (0.0055) ( (0.0050) 3 (0.0034) ) (0.0021) straight (0.0070) pins, (0.0052) ( (0.0043) 4 (0.0038) ) (0.0027) buttons (0.0060) and (0.0078) ( (0.0052) 10 (0.0027) ) (0.0026) spools (0.0079) assorted (0.0081) colors (0.0076) polyester (0.0030) thread- (0.0044) 3- (0.0038) yards (-0.0146) each (-0.0019)
~~~~~~

**Node-1.2** (global 38813):

~~~~~~text
product (0.0001) from (-0.0040) amazon (0.0030) platform (0.0033) with (-0.0004) title (0.0029) and (0.0006) content (0.0000) : (0.0025) title (0.0009) : (0.0014) cold (0.0001) steel (0.0006) inferno. (-0.0006) 38 (0.0028) oz. (-0.0040) keyring (0.0034) hardcase (0.0004) unit (-0.0032) pepper (-0.0018) spray. (0.0009) content (0.0020) : (-0.0035) inferno (0.0016) is (-0.0000) a (-0.0006) new (0.0013) pepper (0.0002) canister (0.0002) weapon (-0.0005) from (0.0008) cold (0.0019) steel (0.0017) that (0.0006) will (0.0005) turn (-0.0000) the (-0.0002) biggest, (0.0010) meanest, (0.0015) most (0.0015) violent (0.0013) criminal (-0.0037) into (0.0010) helpless (0.0017) molten (0.0025) wax (0.0010) at (-0.0011) your (0.0012) feet. (0.0027) unlike (-0.0005) other (0.0006) pepper (-0.0009) sprays (0.0015) you (0.0019) may (0.0010) have (0.0013) heard (0.0014) about, (0.0008) inferno (0.0014) deploys (0.0014) a (0.0002) highly (0.0004) targetable (0.0013) foam (0.0000) that (0.0002) contains (0.0006) 8 (-0.0011) % (0.0029) oleoresin (0.0001) capsicum (-0.0009) and (0.0010) 2 (-0.0012) % (0.0017) black (0.0003) pepper. (-0.0000) it (0.0022) dissolves (-0.0003) into (0.0009) a (0.0001) liquid (0.0011) on (0.0001) contact (0.0006) ( (0.0004) this (0.0040) liquefaction (0.0007) effect (0.0025) is (0.0029) tactically (0.0013) important, (0.0012) since (0.0012) other (0.0023) sprays (0.0009) remain (0.0016) " (0.0006) foamy (-0.0004) "- (0.0011) like (0.0022) a (0.0014) pie (0.0020) in (0.0000) the (0.0010) face- (-0.0001) and (-0.0001) make (0.0002) it (0.0014) possible (0.0005) for (0.0048) your (0.0007) assailant (-0.0002) to (0.0004) wipe (0.0009) the (0.0016) foam (-0.0015) from (-0.0004) his (0.0004) face (-0.0011) and (0.0006) chuck (0.0012) it (0.0016) at (0.0012) you (0.0027) ). (0.0014) one (0.0025) good (0.0009) shot (0.0001) in (0.0012) the (0.0009) face (0.0003) with (0.0005) inferno (-0.0020) will (0.0005) dilate (0.0015) the (-0.0004) capillaries (0.0002) of (0.0006) the (0.0004) eyes (0.0017) causing (0.0007) temporary (0.0010) blindness. (0.0007) it (0.0008) will (-0.0007) induce (-0.0011) choking, (0.0016) coughing (0.0016) and (0.0011) nausea (0.0012) and (0.0012) most (0.0033) importantly (-0.0001) trigger (-0.0004) and (0.0023) immediate (0.0006) and (0.0009) massive (0.0002) sneeze (0.0007) reflex (0.0009) ( (0.0010) due (0.0016) to (0.0005) the (0.0007) atomized (0.0000) black (0.0013) pepper (0.0003) particles (0.0013) ) (-0.0008) that (0.0006) will (0.0016) drag (0.0002) the (-0.0009) super (0.0011) hot (0.0010) habanero (0.0020) chili (0.0008) extract (0.0018) deep (-0.0012) into (-0.0001) the (0.0004) mucous (0.0006) membranes (0.0003) of (0.0002) the (0.0005) sinus (0.0010) cavities (0.0004) of (0.0002) the (0.0006) nose, (0.0012) throat (0.0009) and (0.0003) lungs (0.0006) causing (0.0000) them (0.0012) to (-0.0000) swell (0.0014) up (0.0013) and (0.0000) prevent (0.0002) all (0.0008) but (0.0011) desperate (0.0001) life (0.0009) support (0.0009) breathing. (0.0007) in (0.0002) short (0.0010) inferno (-0.0006) will (0.0013) melt (0.0008) any (0.0006) attacker (0.0003) ( (0.0013) s (-0.0003) ) (-0.0031) into (0.0003) the (0.0005) ground (0.0005) and (0.0008) leave (0.0001) them (0.0006) totally (0.0003) incapacitated (0.0009) for (0.0003) a (0.0004) considerable (0.0005) period (-0.0003) of (-0.0028) time (0.0012) giving (0.0015) you (0.0029) ample (-0.0016) opportunity (-0.0000) to (0.0009) escape (0.0024) and (0.0006) summon (0.0002) the (0.0023) police. (-0.0094) descriptioninferno. (0.0031) 38 (-0.0011) ox. (-0.0006) ( (0.0048) 11. (0.0005) 3 (-0.0011) gram (0.0051) ) (0.0015) keyring (-0.0008) unit (0.0046)
~~~~~~

**Node-1.3** (global 38814):

~~~~~~text
product (0.0058) from (-0.0029) amazon (0.0078) platform (0.0013) with (0.0026) title (0.0044) and (0.0010) content (0.0054) : (0.0065) title (0.0060) : (0.0049) kelty (0.0049) redwing (0.0048) 50 (0.0065) internal (0.0009) frame (0.0005) pack (0.0077) ( (0.0018) black, (0.0033) small (0.0044) / (0.0044) medium- (0.0054) 14. (0.0004) 5- (0.0058) 18. (0.0013) 5- (0.0047) inch (0.0084) torso (0.0049) ). (0.0017) content (0.0110) : (0.0055) the (-0.0031) proven (0.0092) redwing (0.0053) is (0.0021) the (0.0008) most (0.0089) popular (0.0013) pack (-0.0015) on (0.0060) the (-0.0027) trail. (0.0007) revered (0.0020) for (0.0015) its (0.0013) roomy (0.0036) main (0.0016) compartment, (0.0042) convenient (0.0053) organizational (0.0087) pockets, (0.0036) sturdy (0.0074) lightbeam (0.0081) & (-0.0015) # (-0.0009) x2122 (0.0072) ; (0.0063) ii (0.0012) stay (0.0009) and (0.0026) suspension (0.0091) system, (-0.0012) and (0.0040) comfortable (0.0050) design, (0.0036) it (0.0056) & (-0.0023) # (0.0037) x2019 (0.0094) ; (0.0073) s (-0.0069) no (0.0158) wonder (0.0107) this (0.0031) classic, (0.0075) which (0.0053) just (0.0081) got (0.0072) a (-0.0090) facelift, (0.0029) consistently (0.0132) earns (0.0118) top (0.0096) scores. (0.0094)
~~~~~~

**Node-1.4** (global 38816):

~~~~~~text
product (0.0024) from (-0.0023) amazon (0.0011) platform (-0.0042) with (-0.0013) title (0.0061) and (-0.0029) content (0.0049) : (0.0051) title (0.0073) : (0.0053) meco (0.0022) ( (0.0053) tm (0.0032) ) (-0.0028) mini (0.0134) cree (0.0079) led (-0.0021) flashlight (0.0168) torch (0.0098) adjustable (0.0085) zoom (0.0105) light (0.0104) lamp. (0.0071) content (0.0006) : (0.0018) features (0.0046) : (0.0051) * (0.0002) waterproofing (0.0047) design (0.0083) * (0.0030) aluminum (0.0035) alloy (0.0065) casing (0.0049) * (0.0031) aluminum (0.0053) alloy (0.0062) reflector (0.0072) * (0.0042) switch (0.0066) mode (0.0047) : (0.0030) on (0.0020) / (0.0043) off (0.0046) ; (0.0061) zoom (0.0053) in (0.0017) & (0.0094) amp (0.0086) ; (0.0036) zoom (0.0076) out (0.0064) * (0.0065) model (0.0059) of (-0.0056) battery (0.0091) required (0.0062) : (-0.0015) 1x (0.0037) aa (0.0029) battery (0.0064) or (0.0026) 1x (0.0035) 14500 (0.0052) 3. (0.0002) 6v (0.0026) battery (0.0059) ( (0.0061) not (0.0011) included (-0.0024) ) (0.0096) * (-0.0038) model (0.0057) of (0.0045) led (-0.0028) : (0.0081) cree (0.0087) q5 (0.0074) led (-0.0003) * (0.0089) color (0.0119) : (0.0091) blue (0.0058) * (0.0133) external (0.0095) dimension (0.0197) : (0.0083) approx (0.0054) 24mm (0.0071) x (0.0087) 92mmpackage (0.0136) contains (0.0101) : (0.0066) * (0.0013) 1 (0.0039) x (0.0071) flashlight (0.0150)
~~~~~~

**Node-1.5** (global 38817):

~~~~~~text
product (-0.0014) from (0.0003) amazon (-0.0009) platform (0.0028) with (0.0027) title (0.0059) and (0.0023) content (0.0022) : (0.0028) title (0.0030) : (0.0016) light (0.0018) my (0.0017) fire (0.0033) swedish (-0.0010) firesteel (0.0005) mini (0.0010) 1, (0.0007) 500 (0.0038) strike (0.0008) ultralight (0.0032) fire (0.0026) starter. (-0.0012) content (0.0057) : (0.0035) originally (0.0027) developed (0.0014) for (0.0023) the (-0.0020) swedish (-0.0002) department (-0.0013) of (0.0031) defense, (0.0032) swedish (-0.0034) fire (0.0029) steel (0.0025) is (0.0025) a (-0.0001) flash (0.0002) of (0.0015) genius. (-0.0018) its (0.0030) 3, (0.0017) 000- (0.0010) degree (0.0024) c (0.0034) spark (0.0024) makes (0.0002) fire (0.0054) building (0.0043) easy (0.0047) in (0.0018) any (0.0016) weather, (0.0035) at (0.0016) any (0.0031) altitude. (0.0033) used (0.0049) by (0.0024) a (-0.0008) number (0.0014) of (0.0024) armies (0.0056) around (0.0012) the (-0.0025) world, (0.0035) swedish (-0.0053) fire (0.0048) steel (0.0018) ' (0.0012) s (0.0021) dependability (0.0042) has (0.0033) already (0.0020) made (0.0006) it (0.0033) a (-0.0060) favorite (0.0034) of (0.0016) survival (0.0031) experts, (0.0071) hunters, (0.0026) fishermen (0.0019) and (0.0048) campers. (-0.0020) it (0.0038) has (0.0050) also (0.0025) found (0.0042) its (0.0036) way (0.0012) into (0.0034) cabins (0.0040) and (0.0025) backyards (0.0035) as (0.0030) a (-0.0016) fool- (0.0074) proof (0.0067) way (0.0032) to (0.0058) light (0.0078) stoves (0.0062) and (0.0044) gas- (0.0056) barbecues. (0.0020) the (0.0018) mini (0.0036) weighs (0.0030) only (0.0014) 14 (0.0038) grams (-0.0005) ( (0.0016) 0. (0.0009) 5 (0.0026) ounces (0.0029) ), (0.0007) making (0.0019) it (0.0050) essential (0.0023) for (0.0019) every (-0.0001) camper (0.0024) ' (0.0018) s (0.0030) kit. (0.0045)
~~~~~~
