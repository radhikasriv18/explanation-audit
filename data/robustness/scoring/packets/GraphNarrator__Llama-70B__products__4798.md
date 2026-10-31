# Reference packet: GraphNarrator__Llama-70B__products__4798

- Method: GraphNarrator; configuration: Llama-70B; dataset: products; target node: 4798
- Explanation source: `./robustness_2026-10-30/llama70b/graphnarrator/products/4798.json` (response)
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

- ROOT (Bosch power tool)
  - Node-1 (Bosch storage case)
    - Node-1.1 (Bosch starter kit)
    - Node-1.2 (Bosch storage rack)
    - Node-1.3 (Bosch multi-tool blade)
    - Node-1.4 (Bosch impact tough set)
    - Node-1.5 (Bosch reciprocating saw blade)
    - Node-1.6 (Bosch jig saw blade set)
    - Node-1.7 (Bosch foam insert)
    - Node-1.8 (Bosch self-leveling rotary laser)

1. Word-Level Evaluation:

Keywords with high saliency scores in ROOT — "bosch" (0.07), "vibration" (0.02), "control" (0.02), "kit" (0.02), "onboard" (0.06), "dust" (0.04) — are strongly associated with power tools and their accessories. These directly indicate the product belongs to a category related to tools and equipment. More generic terms like "product" (-0.02) and "amazon" (0.02) carry negligible saliency and contribute little.

2. Graph-Level Aggregation:

Node-1 (Bosch storage case, keywords: "bosch" (-0.00), "case" (0.00)) is a direct neighbor with moderate saliency, identifying a storage solution for power tools, whose close proximity to ROOT reinforces the classification. Indirect neighbors — Node-1.1 (Bosch starter kit), Node-1.2 (Bosch storage rack), Node-1.3 (Bosch multi-tool blade), Node-1.4 (Bosch impact tough set), Node-1.5 (Bosch reciprocating saw blade), Node-1.6 (Bosch jig saw blade set), Node-1.7 (Bosch foam insert), Node-1.8 (Bosch self-leveling rotary laser) — are all power tool-related products, collectively confirming a tools and equipment context across both hops.

### Free-Text Explanation
```markdown
The classification of ROOT into "Tools & Home Improvement" is supported by its own keywords and the co-purchase neighborhood.

ROOT: Keywords like "bosch" (0.07), "vibration" (0.02), and "control" (0.02) clearly identify this as a power tool — quintessentially a tool and equipment product.
  - Node-1: A storage case (keywords: "bosch" (-0.00), "case" (0.00)) is a direct power tool accessory, reinforcing the Tools & Home Improvement context.
    - Node-1.1: A starter kit is a power tool-related product, supporting the tools and equipment category.
    - Node-1.2: A storage rack is a power tool storage solution, further confirming the tools and equipment context.
    - Node-1.3: A multi-tool blade is a power tool accessory, collectively affirming the tools and equipment category.
    - Node-1.4: An impact tough set is a power tool-related product, supporting the tools and equipment category.
    - Node-1.5: A reciprocating saw blade is a power tool accessory, further confirming the tools and equipment context.
    - Node-1.6: A jig saw blade set is a power tool accessory, collectively affirming the tools and equipment category.
    - Node-1.7: A foam insert is a power tool storage solution, supporting the tools and equipment category.
    - Node-1.8: A self-leveling rotary laser is a power tool-related product, further confirming the tools and equipment context.

In summary, ROOT's own high-saliency keywords strongly signal power tool use, and the entire co-purchase neighborhood consists of power tool-related products and accessories, providing robust evidence for the "Tools & Home Improvement" category.
```
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/15.json`).

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
<verbalized-graph>ROOT: product(-0.02) amazon(0.02) platform(-0.00) title(0.01) content(0.05) title(0.06) bosch(0.07) ros65vcl(0.00) 5(-0.01) 6-(-0.00) inch(0.02) pads(0.01) rear-(-0.01) handle(-0.00) random(-0.01) orbit(0.00) sander(-0.01) vibration(0.02) control(-0.01) kit.(0.02) content(0.03) industry(0.03) lowest(0.00) vibration,(0.01) highest(0.00) removal(-0.01) rate(0.00) efficient(-0.00) onboard(0.06) dust(-0.01) extraction(-0.01) class,(0.01) ros65vc(0.00) increases(-0.02) user(0.02) productivity,(0.00) helping(0.02) protect(0.01) user(0.01) vibration(0.03) dust.(0.04) 
Node-1: product(-0.01) amazon(-0.00) platform(-0.00) title(0.00) content(0.00) title(0.00) bosch(-0.00) lboxx-(-0.00) 1(-0.00) carrying(-0.00) case.(0.00) content(-0.00) bosch(-0.00) click(-0.00) amp(0.00) go(-0.00) systemthe(-0.00) bosch(-0.00) l-(-0.00) boxx(-0.00) 1(0.00) carrying(-0.00) case(-0.00) part(-0.00) stackable(-0.00) storage(-0.00) system(0.00) designed(-0.00) improve(-0.00) tool(-0.00) organization(0.00) transportation(0.00) jobsite.(0.00) one(-0.00) four(-0.00) different(0.00) cases,(-0.00) l-(-0.00) boxx(-0.00) 1(-0.00) ideal(0.00) storing(0.00) 12-(0.00) volt(0.00) cordless(0.00) drill(-0.00) drivers(0.00) corded(-0.00) jigsaws,(-0.00) room(-0.00) accessories.(0.00) carrying(-0.01) case,(-0.00) simply(0.00) click,(-0.00) stack,(-0.00) go.(-0.00) 
Node-1.1: product(0.00) amazon(-0.00) platform(0.00) title(0.00) content(0.00) title(0.00) bosch(0.00) skc120-(0.00) 202l(0.00) 12-(0.00) volt(0.00) max(0.00) lithium-(0.00) ion(0.00) starter(0.00) kit(0.00) 2(0.00) batteries,(0.00) charger(0.00) l-(0.00) boxx-(0.00) 1.(0.00) content(0.00) none(0.00) 
Node-1.2: product(-0.00) amazon(-0.00) platform(-0.00) title(0.00) content(-0.00) title(0.00) bosch(-0.00) bosch(-0.00) l-(0.00) rack(-0.00) complete(0.00) kit(0.00) 1(0.00) i-(0.00) boxx53,(0.00) 2(0.00) lst72-(0.00) od,(0.00) 3(0.00) l-(0.00) rack-(-0.00) s,(0.00) 1(0.00) l-(0.00) rack-(-0.00) t.(0.00) content(-0.00) bosch(-0.00) click(0.00) go(-0.00) storage(-0.00) system(-0.00) designed(0.00) help(-0.00) stay(-0.00) organized(0.00) get(0.00) tools(0.00) jobsite(0.00) faster,(0.00) spend(-0.00) less(0.00) time(0.00) setting(0.00) time(0.00) productive.(0.00) ultimate(0.00) customized(-0.00) organization(0.00) efficiency.(0.00) organize(-0.00) 90,(0.00) 000(0.00) nuts(0.00) bolts(0.00) house(0.00) 100(0.00) types(0.00) power(0.00) tools.(-0.00) click(-0.00) go(0.00) storage(0.00) system(-0.00) featuring(-0.00) l-(-0.00) boxx(-0.00) available(0.00) 5(0.00) sizes(0.00) fully(-0.00) customizable(-0.00) foam,(0.00) plastic(0.00) inserts,(0.00) drawers(-0.00) exact-(0.00) fit(0.00) insert(0.00) trays(0.00) sold(-0.00) separately.(0.00) every(0.00) l-(0.00) boxx(0.00) quickly(0.00) fits(-0.00) together(0.00) 1-(0.00) click(0.00) stacking.(0.00) l-(0.00) rack(-0.00) allows(0.00) expand(-0.00) current(0.00) system(0.00) instant(0.00) organization(0.00) capability(-0.00) even(0.00) versatility.(0.00) l-(0.00) rack(0.00) customizable(0.00) expansion(0.00) options(0.00) click(0.00) go(0.00) system(0.00) utilizes(0.00) i-(0.00) boxx(0.00) trays(-0.00) drawers(-0.00) adds(-0.00) convenience(-0.00) providing(-0.00) extra(-0.00) storage(-0.00) shelf(0.00) l-(0.00) boxx(0.00) 1,(0.00) 2,(0.00) 3,(0.00) 3d,(0.00) 4(0.00) ).(-0.00) use(-0.00) l-(0.00) cart(0.00) l-(0.00) dolly(0.00) easy(0.00) transport(0.00) job.(0.00) 
Node-1.3: product(0.00) amazon(0.00) platform(0.00) title(0.00) content(0.00) title(0.00) bosch(0.00) osc114c-(0.00) 2(0.00) 1-(0.00) 1(0.00) 4-(0.00) inch(-0.00) multi-(0.00) tool(0.00) carbide(0.00) tooth(0.00) plunge(0.00) cut(0.00) blade,(0.00) 2-(0.00) pack.(0.00) content(0.00) none(0.00) 
Node-1.4: product(-0.00) amazon(0.00) platform(-0.00) title(0.00) content(0.00) title(0.00) bosch(0.00) sbid30(0.00) impact(-0.00) tough(0.00) sdb(0.00) set,(0.00) 30-(0.00) piece.(0.00) content(0.00) bosch(0.00) sbid30(0.00) 30-(0.00) piece(-0.00) impact(-0.00) tough(-0.00) sdb(0.00) set.(0.00) 
Node-1.5: product(0.00) amazon(-0.00) platform(0.00) title(0.00) content(0.00) title(0.00) bosch(0.00) r12v8pk(0.00) 12v(0.00) max(0.00) reciprocating(0.00) saw(0.00) blade,(0.00) 8-(0.00) pack.(-0.00) content(0.00) bosch(0.00) worldwide(0.00) leading(-0.00) manufacturer(-0.00) linear(0.00) edge,(0.00) topping(-0.00) market(-0.00) engineering(-0.00) expertise,(-0.00) manufacturing(-0.00) capabilities(0.00) world(0.00) renowned(0.00) quality.(-0.00) continuing(0.00) path(-0.00) innovation(0.00) engineering(-0.00) excellence,(0.00) bosch(0.00) developed(-0.00) new(0.00) line(-0.00) recipe(0.00) blades.(-0.00) incorporating(0.00) key(-0.00) design(-0.00) features,(-0.00) materials(-0.00) patented(0.00) tooth(0.00) technologies,(-0.00) bosch(0.00) optimizes(0.00) blade(-0.00) cutting(-0.00) efficiency(0.00) fastest(-0.00) cutting(-0.00) longest(-0.00) lasting(-0.00) blades(-0.00) available.(-0.00) 
Node-1.6: product(0.00) amazon(0.00) platform(0.00) title(0.00) content(0.00) title(0.00) bosch(0.00) t18chc(0.00) 18-(0.00) piece(0.00) bosch(0.00) shank(0.00) jig(0.00) saw(0.00) blade(0.00) set(0.00) brute(0.00) case.(0.00) content(0.00) none(0.00) 
Node-1.7: product(0.00) amazon(0.00) platform(0.00) title(0.00) content(0.00) title(0.00) bosch(0.00) foam-(0.00) 201(0.00) pre-(0.00) cut(0.00) foam(0.00) insert(0.00) 136(-0.00) use(0.00) l-(0.00) boxx2,(0.00) part(0.00) click(0.00) go(0.00) mobile(0.00) transport(0.00) system.(0.00) content(0.00) bosch(0.00) click(0.00) amp(0.00) go(0.00) system(0.00) 
Node-1.8: product(-0.00) amazon(-0.00) platform(-0.00) title(0.00) content(0.00) title(0.00) bosch(0.00) grl300hvck(0.00) self-(-0.00) leveling(0.00) rotary(-0.00) laser(-0.00) layout(0.00) beam(0.00) complete(0.00) kit(-0.00) receiver,(0.00) remote,(-0.00) tri-(-0.00) pod(0.00) wall(0.00) mount.(-0.00) content(0.00) since(-0.00) introduction(0.00) first(-0.00) bosch(0.00) measuring(0.00) tool,(-0.00) bosch(-0.00) become(-0.00) worldwide(0.00) leader(0.00) measurement(-0.00) technology(-0.00) innovati</verbalized-graph>

### Classification Label
Cell Phones & Accessories

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 4798
- Title: Bosch ROS65VCL 5 and 6-Inch Pads Rear-Handle Random Orbit Sander with Vibration Control Kit
- True class (canonical `y`): **Tools & Home Improvement**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Health & Personal Care**
- Prediction recorded by this method's pipeline: **Cell Phones & Accessories**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Bosch ROS65VCL 5 and 6-Inch Pads Rear-Handle Random Orbit Sander with Vibration Control Kit. Content: With the industry's lowest vibration, highest removal rate and most efficient onboard dust extraction in its class, the ROS65VC increases user productivity, while helping to protect the user from vibration and dust.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 6 nodes

| node id | true class | title |
|---|---|---|
| 534 | Electronics | Bosch LBOXX-1 Carrying Case |
| 24741 | Tools & Home Improvement | Bosch MX30EL-37 Multi-X 3.0 Amp Oscillating Tool Kit with 37 Accessories |
| 24742 | Tools & Home Improvement | Mirka 23-615-180  5&quot;  8-Hole 180 Grit Dustless Hook &amp; Loop Sanding Discs - 50 Pack |
| 24743 | Appliances | Woodstock D2026 Glue Brush Set, 50-Piece |
| 24744 | Tools & Home Improvement | Bosch MRC23EVSK 2.3 HP Combination Plunge &amp; Fixed-Base Variable Speed Router Pack |
| 24745 | Tools & Home Improvement | Bosch SR6R102 Random Orbit Sander Hook and Loop 6 Hole Disc 6-Inch 100 Grit Sand Paper, Red, 25-Pack |

### 2-hop (shortest distance exactly 2): 13 nodes

| node id | true class | title |
|---|---|---|
| 33 | Automotive | Bosch Bosch L-RACK Complete Kit with (1) i-boxx53, (2) LST72-OD, (3) L-RACK-S, and (1) L-RACK-T |
| 529 | Tools & Home Improvement | Bosch Bare-Tool CFL180 18-Volt Lithium-Ion Flashlight |
| 536 | Home Improvement | Bosch SKC120-202L 12-Volt Max Lithium-Ion Starter Kit with 2 Batteries, Charger and L-BOXX-1 |
| 4716 | Tools & Home Improvement | Bosch Bare-Tool PS60B 12-Volt Max Lithium-Ion Pocket Reciprocating Saw Bare Tool |
| 4722 | Tools & Home Improvement | Bosch OSC114C-2 1-1/4-Inch Multi-Tool Carbide Tooth Plunge Cut Blade, 2-Pack |
| 4747 | Tools & Home Improvement | Bosch SBID30 Impact Tough SDB Set, 30-Piece |
| 4779 | Tools & Home Improvement | Bosch PS50-2A 12-Volt Max Lithium-Ion Multi-X Oscillating Tool Cutting Kit with 2 Batteries, Charger and Case |
| 4787 | Tools & Home Improvement | Bosch DDS181-102L 18-Volt Lithium-Ion 1/2-Inch Compact Tough Drill/Driver Kit with High Capacity Battery, Charger and L-BOXX-2 |
| 4791 | Tools & Home Improvement | Bosch R12V8PK 12V Max Reciprocating Saw Blade, 8-Pack |
| 4795 | Tools & Home Improvement | Bosch T18CHC 18-Piece Bosch Shank Jig Saw Blade Set With Brute Case |
| 4796 | Automotive | Bosch Foam-201 Pre-Cut Foam Insert 136 for use with L-Boxx2, Part of Click and Go Mobile Transport System |
| 4797 | Tools & Home Improvement | Bosch GRL300HVCK Self-Leveling Rotary Laser with Layout Beam Complete Kit with Receiver, Remote, Tri-pod and Wall Mount |
| 4801 | Tools & Home Improvement | Bosch Bare-Tool FL11A 12-Volt Max Lithium-Ion LED Flashlight |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/15.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Cell Phones & Accessories**, ground truth = **Tools & Home Improvement**.
The verbalized graph is 10171 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 4798 | 63 | 0.0675 | yes |
| Node-1 | 1 | 534 | 86 | 0.0097 | yes |
| Node-1.1 | 7 | 536 | 32 | 0.0020 | yes |
| Node-1.2 | 8 | 33 | 222 | 0.0007 | yes |
| Node-1.3 | 9 | 4722 | 31 | 0.0009 | yes |
| Node-1.4 | 10 | 4747 | 29 | 0.0015 | yes |
| Node-1.5 | 11 | 4791 | 85 | 0.0005 | yes |
| Node-1.6 | 12 | 4795 | 27 | 0.0016 | yes |
| Node-1.7 | 13 | 4796 | 43 | 0.0030 | yes |
| Node-1.8 | 14 | 4797 | 146 | 0.0018 | yes |
| Node-1.9 | 15 | 4787 | 40 | 0.0007 | no |
| Node-2 | 2 | 24741 | 28 | 0.0096 | no |
| Node-3 | 3 | 24742 | 90 | 0.0101 | no |
| Node-4 | 4 | 24743 | 54 | 0.0118 | no |
| Node-5 | 5 | 24744 | 83 | 0.0261 | no |
| Node-6 | 6 | 24745 | 60 | 0.0210 | no |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->Node-1.6, Node-1->Node-1.7, Node-1->Node-1.8, Node-1->Node-1.9, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, Node-1.6->Node-1, Node-1.7->Node-1, Node-1.8->Node-1, Node-1.9->Node-1, Node-2->ROOT, Node-3->ROOT, Node-4->ROOT, Node-5->ROOT, Node-6->ROOT, ROOT->Node-1, ROOT->Node-2, ROOT->Node-3, ROOT->Node-4, ROOT->Node-5, ROOT->Node-6

### Tokens and scores

**ROOT** (global 4798):

~~~~~~text
product (-0.0207) from (0.0156) amazon (0.0193) platform (-0.0040) with (0.0158) title (0.0133) and (-0.0134) content (0.0529) : (-0.0068) title (0.0614) : (0.0203) bosch (0.0675) ros65vcl (0.0036) 5 (-0.0084) and (0.0025) 6- (-0.0026) inch (0.0166) pads (0.0135) rear- (-0.0053) handle (-0.0030) random (-0.0081) orbit (0.0029) sander (-0.0052) with (0.0112) vibration (0.0156) control (-0.0068) kit. (0.0194) content (0.0334) : (-0.0374) with (0.0079) the (0.0002) industry (0.0286) ' (0.0078) s (0.0027) lowest (0.0019) vibration, (0.0100) highest (0.0039) removal (-0.0132) rate (0.0050) and (0.0026) most (0.0087) efficient (-0.0019) onboard (0.0637) dust (-0.0145) extraction (-0.0072) in (0.0034) its (-0.0053) class, (0.0106) the (0.0000) ros65vc (0.0013) increases (-0.0185) user (0.0150) productivity, (0.0010) while (-0.0075) helping (0.0237) to (-0.0189) protect (0.0065) the (0.0050) user (0.0108) from (0.0029) vibration (0.0319) and (0.0056) dust. (0.0420)
~~~~~~

**Node-1** (global 534):

~~~~~~text
product (-0.0055) from (-0.0059) amazon (-0.0005) platform (-0.0020) with (-0.0003) title (0.0019) and (-0.0010) content (0.0026) : (0.0006) title (0.0018) : (0.0007) bosch (-0.0017) lboxx- (-0.0023) 1 (-0.0015) carrying (-0.0038) case. (0.0031) content (-0.0033) : (-0.0027) bosch (-0.0028) ' (-0.0012) s (-0.0030) click (-0.0022) & (-0.0008) amp (0.0003) ; (-0.0035) go (-0.0001) systemthe (-0.0010) bosch (-0.0010) l- (-0.0014) boxx (-0.0004) 1 (0.0026) carrying (-0.0031) case (-0.0020) is (-0.0012) part (-0.0012) of (0.0008) a (-0.0044) stackable (-0.0018) storage (-0.0006) system (0.0031) designed (-0.0013) to (0.0002) improve (-0.0019) tool (-0.0049) organization (0.0015) and (-0.0023) transportation (0.0012) on (0.0097) the (-0.0022) jobsite. (0.0040) one (-0.0023) of (0.0001) four (-0.0008) different (0.0023) cases, (-0.0002) the (0.0009) l- (-0.0003) boxx (-0.0012) 1 (-0.0010) is (0.0008) ideal (0.0025) for (-0.0005) storing (0.0006) 12- (0.0002) volt (0.0008) cordless (0.0009) drill (-0.0043) / (-0.0007) drivers (0.0005) and (-0.0006) corded (-0.0013) jigsaws, (-0.0004) with (-0.0015) room (-0.0010) for (-0.0041) accessories. (0.0031) with (0.0002) this (0.0012) carrying (-0.0065) case, (-0.0013) you (0.0039) simply (0.0028) click, (-0.0024) stack, (-0.0033) and (-0.0018) go. (-0.0029)
~~~~~~

**Node-1.1** (global 536):

~~~~~~text
product (0.0002) from (0.0002) amazon (-0.0005) platform (0.0005) with (-0.0002) title (0.0009) and (0.0000) content (0.0012) : (-0.0010) title (0.0011) : (0.0005) bosch (0.0007) skc120- (0.0004) 202l (0.0005) 12- (0.0005) volt (0.0003) max (0.0007) lithium- (0.0005) ion (0.0007) starter (0.0007) kit (0.0002) with (0.0001) 2 (0.0007) batteries, (0.0003) charger (0.0005) and (0.0002) l- (0.0004) boxx- (0.0007) 1. (0.0012) content (0.0001) : (0.0002) none (0.0020)
~~~~~~

**Node-1.2** (global 33):

~~~~~~text
product (-0.0002) from (-0.0002) amazon (-0.0001) platform (-0.0002) with (-0.0002) title (0.0001) and (0.0001) content (-0.0001) : (0.0001) title (0.0001) : (-0.0000) bosch (-0.0000) bosch (-0.0002) l- (0.0000) rack (-0.0000) complete (0.0001) kit (0.0000) with (-0.0001) ( (0.0000) 1 (0.0000) ) (0.0000) i- (0.0001) boxx53, (0.0001) ( (0.0000) 2 (0.0001) ) (-0.0001) lst72- (0.0001) od, (0.0001) ( (0.0001) 3 (0.0000) ) (-0.0001) l- (0.0000) rack- (-0.0000) s, (0.0000) and (0.0001) ( (0.0000) 1 (0.0000) ) (-0.0001) l- (0.0001) rack- (-0.0001) t. (0.0002) content (-0.0001) : (0.0001) the (-0.0001) bosch (-0.0006) click (0.0000) and (-0.0001) go (-0.0001) storage (-0.0001) system (-0.0001) is (-0.0001) designed (0.0002) to (0.0000) help (-0.0000) you (-0.0001) stay (-0.0001) organized (0.0001) and (-0.0000) get (0.0000) your (0.0002) tools (0.0001) on (0.0000) and (-0.0000) off (0.0001) the (0.0002) jobsite (0.0000) faster, (0.0002) so (0.0004) you (0.0002) can (0.0000) spend (-0.0001) less (0.0001) time (0.0001) setting (0.0001) up (0.0001) and (0.0001) more (0.0000) time (0.0001) being (0.0001) productive. (0.0002) it (0.0001) ' (0.0000) s (0.0001) the (0.0001) ultimate (0.0001) in (0.0001) customized (-0.0001) organization (0.0003) and (0.0001) efficiency. (0.0007) organize (-0.0001) over (0.0000) 90, (0.0001) 000 (0.0000) nuts (0.0004) and (0.0002) bolts (0.0003) and (0.0000) house (0.0000) over (0.0001) 100 (0.0002) types (0.0002) of (0.0001) power (0.0003) tools. (-0.0001) the (0.0004) click (-0.0004) and (0.0003) go (0.0002) storage (0.0002) system (-0.0001) featuring (-0.0000) the (-0.0001) l- (-0.0000) boxx (-0.0001) is (0.0001) available (0.0002) in (-0.0000) 5 (0.0002) sizes (0.0000) and (-0.0000) fully (-0.0001) customizable (-0.0000) with (0.0000) foam, (0.0001) plastic (0.0001) inserts, (0.0000) drawers (-0.0001) and (0.0001) exact- (0.0000) fit (0.0000) insert (0.0001) trays (0.0000) sold (-0.0000) separately. (0.0000) every (0.0000) l- (0.0001) boxx (0.0001) quickly (0.0000) fits (-0.0001) together (0.0001) with (-0.0001) just (0.0001) 1- (0.0000) click (0.0002) stacking. (0.0001) the (0.0000) l- (0.0001) rack (-0.0001) allows (0.0001) you (0.0002) to (-0.0000) expand (-0.0001) your (0.0002) current (0.0001) system (0.0001) with (-0.0002) instant (0.0001) organization (0.0001) capability (-0.0001) for (0.0000) even (0.0001) more (0.0001) versatility. (0.0001) the (-0.0000) l- (0.0001) rack (0.0001) ' (-0.0001) s (-0.0000) customizable (0.0001) expansion (0.0002) options (0.0001) for (-0.0000) the (0.0000) click (0.0003) & (0.0001) go (0.0002) system (0.0002) utilizes (0.0001) i- (0.0001) boxx (0.0000) trays (-0.0000) and (0.0001) drawers (-0.0001) and (0.0001) adds (-0.0001) the (0.0001) convenience (-0.0001) of (0.0001) providing (-0.0001) an (0.0001) extra (-0.0001) storage (-0.0000) shelf (0.0001) to (0.0001) any (0.0002) l- (0.0000) boxx (0.0000) ( (0.0001) 1, (0.0001) 2, (0.0001) 3, (0.0001) 3d, (0.0000) or (-0.0000) 4 (0.0004) ). (-0.0001) use (-0.0002) the (0.0002) l- (0.0000) cart (0.0002) or (-0.0000) the (-0.0000) l- (0.0002) dolly (0.0000) for (-0.0001) easy (0.0000) transport (0.0004) on (0.0001) and (-0.0000) off (0.0002) the (0.0000) job. (0.0003)
~~~~~~

**Node-1.3** (global 4722):

~~~~~~text
product (0.0004) from (-0.0004) amazon (0.0008) platform (0.0000) with (-0.0001) title (0.0004) and (0.0001) content (0.0006) : (-0.0006) title (0.0004) : (0.0004) bosch (0.0007) osc114c- (0.0003) 2 (0.0003) 1- (0.0003) 1 (0.0004) / (0.0004) 4- (0.0003) inch (-0.0001) multi- (0.0006) tool (0.0007) carbide (0.0003) tooth (0.0004) plunge (0.0008) cut (0.0003) blade, (0.0006) 2- (0.0004) pack. (0.0009) content (0.0005) : (0.0005) none (0.0006)
~~~~~~

**Node-1.4** (global 4747):

~~~~~~text
product (-0.0008) from (0.0004) amazon (0.0015) platform (-0.0012) with (0.0001) title (0.0006) and (0.0002) content (0.0010) : (-0.0001) title (0.0001) : (0.0004) bosch (0.0011) sbid30 (0.0008) impact (-0.0006) tough (0.0004) sdb (0.0000) set, (0.0000) 30- (0.0009) piece. (0.0005) content (0.0006) : (0.0006) bosch (0.0002) sbid30 (0.0009) 30- (0.0008) piece (-0.0015) impact (-0.0002) tough (-0.0000) sdb (0.0003) set. (0.0014)
~~~~~~

**Node-1.5** (global 4791):

~~~~~~text
product (0.0000) from (-0.0003) amazon (-0.0000) platform (0.0002) with (-0.0000) title (0.0001) and (-0.0002) content (0.0005) : (-0.0000) title (0.0000) : (-0.0001) bosch (0.0000) r12v8pk (0.0001) 12v (0.0000) max (0.0001) reciprocating (0.0001) saw (0.0003) blade, (0.0000) 8- (0.0000) pack. (-0.0004) content (0.0004) : (0.0001) bosch (0.0002) is (-0.0002) the (0.0001) worldwide (0.0001) leading (-0.0001) manufacturer (-0.0001) of (-0.0000) linear (0.0004) edge, (0.0002) topping (-0.0001) the (-0.0001) market (-0.0002) through (-0.0001) engineering (-0.0001) expertise, (-0.0000) manufacturing (-0.0000) capabilities (0.0001) and (0.0000) world (0.0001) renowned (0.0001) quality. (-0.0003) continuing (0.0001) on (0.0002) the (0.0001) path (-0.0001) of (-0.0001) innovation (0.0001) and (-0.0001) engineering (-0.0001) excellence, (0.0002) bosch (0.0005) has (-0.0002) developed (-0.0000) a (-0.0002) new (0.0004) line (-0.0002) of (-0.0002) recipe (0.0004) blades. (-0.0002) by (0.0001) incorporating (0.0002) key (-0.0000) design (-0.0001) features, (-0.0000) materials (-0.0002) and (-0.0001) patented (0.0001) tooth (0.0001) technologies, (-0.0000) bosch (0.0004) optimizes (0.0000) blade (-0.0000) cutting (-0.0002) efficiency (0.0000) for (-0.0001) the (-0.0003) fastest (-0.0003) cutting (-0.0003) and (-0.0002) longest (-0.0001) lasting (-0.0002) blades (-0.0003) available. (-0.0004)
~~~~~~

**Node-1.6** (global 4795):

~~~~~~text
product (0.0014) from (0.0006) amazon (0.0006) platform (0.0005) with (0.0004) title (0.0006) and (0.0008) content (0.0010) : (0.0007) title (0.0005) : (0.0008) bosch (0.0007) t18chc (0.0007) 18- (0.0009) piece (0.0007) bosch (0.0006) shank (0.0005) jig (0.0008) saw (0.0007) blade (0.0015) set (0.0011) with (0.0010) brute (0.0016) case. (0.0001) content (0.0008) : (0.0001) none (0.0008)
~~~~~~

**Node-1.7** (global 4796):

~~~~~~text
product (0.0010) from (-0.0000) amazon (0.0005) platform (0.0003) with (0.0001) title (0.0013) and (-0.0001) content (0.0030) : (-0.0002) title (0.0014) : (0.0006) bosch (0.0017) foam- (0.0008) 201 (0.0008) pre- (0.0009) cut (0.0010) foam (0.0022) insert (0.0010) 136 (-0.0004) for (0.0008) use (0.0008) with (-0.0001) l- (0.0007) boxx2, (0.0006) part (0.0005) of (0.0007) click (0.0002) and (0.0005) go (0.0016) mobile (0.0014) transport (0.0005) system. (0.0022) content (0.0011) : (-0.0004) bosch (0.0002) ' (0.0003) s (0.0009) click (0.0014) & (0.0028) amp (0.0008) ; (0.0015) go (0.0023) system (0.0007)
~~~~~~

**Node-1.8** (global 4797):

~~~~~~text
product (-0.0001) from (-0.0004) amazon (-0.0003) platform (-0.0006) with (-0.0009) title (0.0003) and (-0.0005) content (0.0002) : (-0.0001) title (0.0003) : (-0.0001) bosch (0.0010) grl300hvck (0.0001) self- (-0.0000) leveling (0.0001) rotary (-0.0002) laser (-0.0004) with (-0.0005) layout (0.0002) beam (0.0001) complete (0.0002) kit (-0.0002) with (-0.0002) receiver, (0.0002) remote, (-0.0001) tri- (-0.0000) pod (0.0000) and (-0.0002) wall (0.0001) mount. (-0.0006) content (0.0003) : (0.0005) since (-0.0004) the (0.0000) introduction (0.0004) of (-0.0005) the (-0.0002) first (-0.0001) bosch (0.0007) measuring (0.0000) tool, (-0.0008) bosch (-0.0001) has (-0.0002) become (-0.0001) a (-0.0003) worldwide (0.0006) leader (0.0001) in (-0.0004) measurement (-0.0001) technology (-0.0001) through (0.0002) innovation (0.0004) and (-0.0002) advanced (0.0001) engineering. (-0.0001) the (-0.0002) same (-0.0000) quality, (0.0001) durability (0.0001) and (-0.0000) forward (0.0001) thinking (0.0002) found (0.0002) in (-0.0003) bosch (0.0006) power (0.0002) tools (-0.0000) is (-0.0002) now (0.0000) offered (-0.0002) in (-0.0001) a (0.0002) complete (0.0001) line (-0.0001) of (0.0002) measuring (-0.0002) tools. (-0.0000) with (0.0003) bosch (0.0007) laser (0.0005) technology, (-0.0001) users (0.0004) are (0.0002) able (-0.0003) to (-0.0000) become (-0.0001) more (0.0001) productive (0.0003) and (-0.0003) more (-0.0004) profitable- (0.0002) with (0.0001) great (-0.0002) accuracy (0.0006) and (0.0001) precision (0.0006) on (0.0003) the (-0.0005) jobsite. (-0.0010) by (0.0005) offering (0.0001) an (0.0007) extensive (0.0002) range (0.0005) of (0.0002) line (0.0004) lasers, (-0.0001) laser (-0.0007) distance (0.0003) measurers, (0.0000) rotary (-0.0012) lasers, (-0.0005) point (0.0001) lasers, (-0.0004) digital (-0.0002) levels, (-0.0001) optical (-0.0003) levels (-0.0001) and (-0.0002) measuring (0.0000) tool (-0.0002) accessories, (0.0002) bosch (0.0006) is (0.0000) able (-0.0005) to (0.0000) provide (0.0003) solutions (0.0006) for (-0.0002) a (0.0001) wide (0.0001) variety (0.0000) of (-0.0004) applications. (0.0005) with (-0.0002) bosch (0.0018) measuring (-0.0003) tools, (0.0002) users (0.0005) are (0.0002) able (-0.0003) to (-0.0001) work (0.0004) smarter, (0.0000) not (-0.0003) harder. (0.0003)
~~~~~~

**Node-1.9** (global 4787):

~~~~~~text
product (0.0003) from (0.0001) amazon (-0.0002) platform (0.0002) with (-0.0004) title (0.0003) and (0.0003) content (0.0002) : (-0.0001) title (0.0005) : (0.0004) bosch (-0.0001) dds181- (0.0003) 102l (0.0002) 18- (0.0002) volt (0.0003) lithium- (0.0002) ion (0.0004) 1 (0.0003) / (0.0003) 2- (0.0002) inch (0.0002) compact (0.0002) tough (0.0003) drill (0.0003) / (0.0002) driver (0.0007) kit (0.0005) with (0.0002) high (0.0001) capacity (0.0001) battery, (0.0003) charger (0.0003) and (0.0000) l- (0.0002) boxx- (0.0003) 2. (0.0007) content (0.0007) : (-0.0003) none (0.0006)
~~~~~~

**Node-2** (global 24741):

~~~~~~text
product (-0.0002) from (0.0035) amazon (-0.0081) platform (-0.0014) with (0.0041) title (0.0024) and (0.0018) content (0.0096) : (0.0033) title (0.0042) : (0.0003) bosch (0.0090) mx30el- (0.0025) 37 (0.0002) multi- (0.0058) x (0.0017) 3. (-0.0007) 0 (0.0075) amp (0.0056) oscillating (0.0026) tool (0.0086) kit (0.0000) with (0.0034) 37 (0.0043) accessories. (0.0011) content (-0.0045) : (-0.0061) none (0.0044)
~~~~~~

**Node-3** (global 24742):

~~~~~~text
product (-0.0010) from (0.0004) amazon (0.0082) platform (-0.0034) with (0.0054) title (0.0031) and (-0.0039) content (0.0034) : (0.0101) title (0.0075) : (0.0052) mirka (-0.0000) 23- (0.0011) 615- (-0.0001) 180 (0.0019) 5 (0.0021) & (0.0006) quot (0.0000) ; (0.0001) 8- (0.0015) hole (-0.0008) 180 (0.0002) grit (0.0055) dustless (0.0005) hook (0.0040) & (-0.0004) amp (0.0012) ; (0.0005) loop (0.0019) sanding (0.0001) discs- (0.0025) 50 (-0.0018) pack. (0.0013) content (0.0058) : (0.0030) bulldog (-0.0063) gold (0.0026) ' (0.0041) s (0.0039) grip (0.0062) hook- (0.0012) and- (0.0006) loop (0.0017) sanding (0.0007) discs (0.0044) have (-0.0031) a (0.0024) special (-0.0003) sharp, (0.0022) durable (0.0001) aluminum (0.0034) oxide (0.0004) grain (0.0023) that (0.0019) gives (0.0070) you (0.0060) a (0.0022) fast (0.0041) and (0.0022) exceptionally (0.0043) long- (0.0022) lasting (0.0036) cut. (-0.0026) durable (0.0014) aluminum (0.0027) oxide, (-0.0008) combined (0.0018) with (0.0021) urea (0.0014) resin (0.0061) over (0.0018) glue (0.0028) bonds, (0.0020) and (0.0025) an (0.0009) open (0.0006) coat (0.0028) create (0.0044) a (-0.0003) high (0.0035) performance (0.0009) sandpaper (0.0048) that (0.0033) ' (0.0045) s (0.0044) the (0.0039) envy (0.0057) of (0.0002) the (0.0032) industry. (0.0048)
~~~~~~

**Node-4** (global 24743):

~~~~~~text
product (0.0093) from (0.0014) amazon (0.0012) platform (0.0054) with (0.0008) title (0.0103) and (0.0008) content (-0.0014) : (0.0077) title (0.0064) : (-0.0026) woodstock (0.0108) d2026 (0.0041) glue (-0.0056) brush (-0.0045) set, (0.0046) 50- (0.0046) piece. (0.0024) content (0.0080) : (-0.0067) use (0.0047) these (0.0016) handy (0.0025) disposable (0.0003) 3 (0.0030) / (0.0048) 8- (0.0017) inch (0.0057) and (0.0000) 3 (0.0009) / (0.0039) 4- (0.0001) inch (0.0003) brushes (-0.0006) for (-0.0019) everything (0.0036) from (0.0015) glue (0.0026) to (0.0007) flux. (0.0072) made (-0.0019) with (0.0036) extra (0.0008) long (0.0021) synthetic (0.0088) bristles. (0.0118) in (-0.0084) 50- (0.0040) count (0.0051) packs. (0.0084) 25 (-0.0035) of (0.0028) each (-0.0073) size. (0.0071)
~~~~~~

**Node-5** (global 24744):

~~~~~~text
product (0.0087) from (0.0091) amazon (-0.0159) platform (-0.0361) with (0.0141) title (0.0157) and (0.0211) content (-0.0059) : (0.0261) title (0.0079) : (0.0206) bosch (0.0152) mrc23evsk (0.0039) 2. (0.0073) 3 (0.0142) hp (-0.0193) combination (0.0053) plunge (0.0031) & (0.0033) amp (0.0088) ; (0.0156) fixed- (0.0123) base (0.0095) variable (0.0109) speed (0.0039) router (0.0100) pack. (-0.0041) content (0.0132) : (0.0258) the (-0.0041) bosch (0.0038) 2. (0.0110) 3- (0.0078) horsepower (-0.0172) combination (0.0136) plunge (0.0175) and (0.0127) fixed- (0.0111) base (-0.0000) router (0.0100) pack (0.0114) contains (-0.0031) two (0.0087) efficient, (0.0113) responsive, (0.0044) and (0.0093) precise (0.0090) tools (0.0132) for (-0.0022) woodworking (-0.0159) professionals-- (0.0055) a (0.0091) plunge (-0.0042) router (0.0069) and (0.0163) a (0.0023) fixed- (0.0099) base (-0.0004) router. (0.0022) both (0.0212) routers (0.0103) offer (-0.0054) the (-0.0016) convenience (0.0009) of (0.0042) variable (0.0152) speed (0.0166) operation, (-0.0012) the (-0.0051) ease (0.0128) of (0.0031) accurate (0.0144) adjustments, (0.0080) and (0.0076) the (0.0113) long- (0.0133) term (0.0185) comfort (0.0078) and (0.0160) control (0.0149) of (0.0068) contoured (0.0183) handles. (0.0168)
~~~~~~

**Node-6** (global 24745):

~~~~~~text
product (0.0147) from (0.0076) amazon (-0.0089) platform (-0.0209) with (0.0008) title (0.0032) and (-0.0061) content (0.0084) : (0.0154) title (0.0111) : (0.0124) bosch (0.0058) sr6r102 (0.0020) random (-0.0006) orbit (0.0172) sander (0.0044) hook (0.0050) and (-0.0031) loop (0.0074) 6 (0.0001) hole (0.0097) disc (0.0018) 6- (0.0013) inch (0.0014) 100 (0.0077) grit (0.0156) sand (0.0027) paper, (0.0058) red, (0.0041) 25- (0.0079) pack. (0.0048) content (0.0140) : (-0.0034) bosch (0.0210) offers (0.0048) a (-0.0085) full (0.0038) line (0.0023) of (0.0023) sanding (0.0041) belts, (0.0081) sheets, (0.0040) pads (0.0110) and (0.0016) triangles (0.0097) that (0.0043) fit (0.0063) bosch (0.0141) and (-0.0003) other (0.0070) belt (0.0039) sanders, (0.0040) finishing (0.0039) sanders, (0.0106) random (0.0077) orbit (0.0057) sanders (0.0171) and (0.0043) detail (0.0083) sanders. (0.0018)
~~~~~~
