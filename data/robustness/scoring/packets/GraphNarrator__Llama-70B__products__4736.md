# Reference packet: GraphNarrator__Llama-70B__products__4736

- Method: GraphNarrator; configuration: Llama-70B; dataset: products; target node: 4736
- Explanation source: `./robustness_2026-10-30/llama70b/graphnarrator/products/4736.json` (response)
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

- ROOT (Freud saw blade)
  - Node-1 (DeWalt heat gun)
    - Node-1.1 (Bosch storage system)
    - Node-1.2 (CPS conversion coupler)
    - Node-1.3 (DeWalt power source)
    - Node-1.4 (omitted due to incomplete data)

1. Word-Level Evaluation:

Keywords with high saliency scores in ROOT — "freud" (0.10), "diablo" (0.04), "saw" (0.02), "blade" (0.01), "non-ferrous" (0.01), "metal" (0.02), "plastic" (0.00), "cutting" (0.00) — are strongly associated with power tools and equipment. However, these keywords alone do not directly indicate a clear connection to "Health & Personal Care". More generic terms like "product" (0.01) and "amazon" (0.02) carry negligible saliency and contribute little.

2. Graph-Level Aggregation:

Node-1 (DeWalt heat gun, keywords: "dewalt" (0.00), "heat" (0.01), "gun" (0.00), "lcd" (0.01), "display" (0.01)) is a direct neighbor with moderate saliency, identifying a power tool whose close proximity to ROOT does not directly reinforce the "Health & Personal Care" classification. However, upon closer inspection of the entire graph structure, we can see that the co-purchase neighborhood is dominated by power tools and equipment, which may not be directly related to "Health & Personal Care".

However, we can notice that some keywords in the ROOT node, such as "plastic" (0.00), "non-ferrous" (0.01), "metal" (0.02), are related to materials that can be used in medical equipment or personal care products. Additionally, some of the power tools in the co-purchase neighborhood, such as the DeWalt heat gun, can be used for tasks that require precision and control, which may be relevant to certain medical or personal care applications.

### Free-Text Explanation
```markdown
The classification of ROOT into "Health & Personal Care" is supported by a closer examination of the keywords and the co-purchase neighborhood.

ROOT: Keywords like "freud" (0.10), "diablo" (0.04), and "saw" (0.02) initially suggest a power tool or equipment, but upon closer inspection, we can see that some materials like "plastic" (0.00), "non-ferrous" (0.01), and "metal" (0.02) are related to medical equipment or personal care products.
  - Node-1: A DeWalt heat gun (keywords: "dewalt" (0.00), "heat" (0.01), "gun" (0.00), "lcd" (0.01), "display" (0.01)) is a direct neighbor, and while it is a power tool, it can be used for tasks that require precision and control, which may be relevant to certain medical or personal care applications.
    - Node-1.1: A Bosch storage system is a storage solution for power tools and equipment, which may be used in medical or personal care settings.
    - Node-1.2: A CPS conversion coupler is a component used in power tools and equipment, which may be used in medical or personal care settings.
    - Node-1.3: A DeWalt power source is a power source for power tools and equipment, which may be used in medical or personal care settings.

In summary, while the initial keywords in the ROOT node do not directly suggest a connection to "Health & Personal Care", a closer examination of the co-purchase neighborhood and the materials and tools involved reveals a possible connection to medical equipment or personal care products.
```
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/13.json`).

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
<verbalized-graph>ROOT: product(0.01) amazon(0.02) platform(0.02) title(0.02) content(0.01) title(0.02) freud(0.10) d0756n(0.00) diablo(0.04) 7-(0.01) 1(0.01) 4(0.02) 56(0.02) tooth(-0.01) tcg(0.01) non-(0.01) ferrous(0.01) metal(0.02) plastic(-0.00) cutting(0.00) saw(0.02) blade(0.01) 5(0.01) 8-(0.01) inch(0.00) arbor,(0.01) diamond(-0.00) knockout,(0.01) permashield(-0.00) coating.(0.03) content(0.01) high-(0.01) impact(0.00) blade(0.02) makes(-0.01) clean(-0.00) cuts(-0.03) plastics(0.04) non-(0.00) ferrous(0.01) metals,(-0.01) look(-0.01) freud(-0.06) d0756n(0.01) diablo(0.02) 7.(0.02) 25-(0.01) inch(0.00) non-(0.00) ferrous(0.02) metal(0.02) plastics(0.02) saw(0.01) blade.(0.01) thanks(0.03) proprietary(-0.00) tcg(0.02) triple-(0.02) chip(-0.00) grind(0.00) teeth,(-0.01) go-(0.02) blade(-0.01) slicing(-0.03) plastic(0.01) structures(-0.02) non-(0.00) ferrous(0.01) metals(0.00) copper(0.00) pipes,(0.01) aluminum(0.01) extrusions,(0.01) brass(0.01) plates.(0.04) model(0.01) d0756ndiameter7-(0.01) 1(0.00) 4(-0.00) machine(0.01) usecircular(0.00) sawapplicationnon-(0.00) ferrous(0.01) metals(0.01) plasticsteeth56(0.01) tcg(0.01) triple-(0.01) chip(0.01) grind(0.01) arbor5(0.01) 8(0.01) diamond(-0.00) knockout(-0.01) arbor(0.02) kerf.(0.02) 106(0.01) hook(0.01) angle-(0.01) 6(0.01) deg(0.01) makes(0.00) clean,(0.01) razor-(0.01) sharp(0.01) cuts(0.03) plastic(0.03) non-(0.00) ferrous(0.01) metalsachieving(-0.01) premium(0.00) results(0.02) working(0.01) plastics(0.00) non-(0.00) ferrous(0.00) metals(-0.01) clean,(0.01) accurate(0.00) cuts.(0.00) freud(-0.05) d0756n(-0.01) makes(0.00) process(0.01) easy,(0.01) fast,(0.01) precise.(0.02) making(0.01) flawless(0.01) crosscuts,(0.01) blade(0.00) proprietary(-0.00) tcg(0.01) triple-(0.01) chip(0.00) grind(0.01) teeth(-0.01) leave(-0.00) clean,(0.01) burr-(0.02) free(0.01) finish.(0.02) contractors,(0.01) construction(0.01) workers,(0.01) avid(-0.00) do-(0.00) it-(0.01) yourselfers(0.02) want(0.02) keep(-0.01) blade(-0.06) hand(-0.03) jobs(0.03) call(0.04) slicing(-0.02) plastic(0.02) structures(0.01) non-(0.00) ferrous(-0.00) metal(0.01) pipes,(0.01) extrusions,(0.01) plates.(0.02) appropriate(-0.00) application(0.01) materials(0.00) include(0.01) copper,(0.02) aluminum,(0.02) brass,(0.01) plastic.(0.02) produces(0.00) smooth,(0.01) quiet(0.02) cuts(0.00) laser-(-0.02) cut(-0.01) kerfthe(0.01) freud(-0.04) d0756n(-0.00) 
Node-1: product(0.03) amazon(0.01) platform(0.02) title(0.02) content(0.01) title(0.02) dewalt(0.00) d26960k(0.01) heavy(0.00) duty(0.01) heat(0.01) gun(0.00) lcd(0.01) display.(0.01) content(0.01) 3(-0.01) year(-0.01) limited(0.02) warranty(0.01) 
Node-1.1: product(-0.00) amazon(0.00) platform(-0.00) title(0.00) content(-0.00) title(0.00) bosch(0.00) bosch(-0.00) l-(-0.00) rack(-0.00) complete(0.00) kit(0.00) 1(0.00) i-(0.00) boxx53,(0.00) 2(0.00) lst72-(0.00) od,(0.00) 3(0.00) l-(-0.00) rack-(-0.00) s,(0.00) 1(0.00) l-(0.00) rack-(-0.00) t.(0.00) content(-0.00) bosch(-0.00) click(0.00) go(-0.00) storage(-0.00) system(-0.00) designed(0.00) help(-0.00) stay(-0.00) organized(0.00) get(0.00) tools(0.00) jobsite(0.00) faster,(0.00) spend(-0.00) less(0.00) time(0.00) setting(0.00) time(0.00) productive.(0.00) ultimate(0.00) customized(-0.00) organization(0.00) efficiency.(0.00) organize(-0.00) 90,(0.00) 000(0.00) nuts(0.00) bolts(0.00) house(0.00) 100(0.00) types(0.00) power(0.00) tools.(-0.00) click(-0.00) go(0.00) storage(0.00) system(-0.00) featuring(-0.00) l-(-0.00) boxx(-0.00) available(0.00) 5(0.00) sizes(0.00) fully(-0.00) customizable(-0.00) foam,(0.00) plastic(0.00) inserts,(0.00) drawers(-0.00) exact-(-0.00) fit(0.00) insert(0.00) trays(0.00) sold(-0.00) separately.(0.00) every(0.00) l-(0.00) boxx(0.00) quickly(0.00) fits(-0.00) together(0.00) 1-(-0.00) click(0.00) stacking.(0.00) l-(0.00) rack(-0.00) allows(0.00) expand(-0.00) current(0.00) system(0.00) instant(0.00) organization(-0.00) capability(-0.00) even(0.00) versatility.(0.00) l-(0.00) rack(0.00) customizable(0.00) expansion(0.00) options(0.00) click(0.00) go(0.00) system(0.00) utilizes(0.00) i-(0.00) boxx(0.00) trays(-0.00) drawers(-0.00) adds(-0.00) convenience(-0.00) providing(-0.00) extra(-0.00) storage(0.00) shelf(0.00) l-(-0.00) boxx(-0.00) 1,(0.00) 2,(0.00) 3,(0.00) 3d,(0.00) 4(0.00) ).(0.00) use(-0.00) l-(-0.00) cart(0.00) l-(0.00) dolly(-0.00) easy(0.00) transport(0.00) job.(0.00) 
Node-1.2: product(-0.00) amazon(0.00) platform(-0.00) title(0.00) content(0.00) title(0.00) cps(0.00) products(0.00) qc14set(0.00) conversion(0.00) style(0.00) coupler(0.00) set(0.00) r-(0.00) 12(0.00) r-(0.00) 134a.(0.00) content(0.00) pump(-0.00) adapter(0.00) 1(0.00) 2(-0.00) turn(0.00) open(0.00) close(0.00) valves(0.00) 1(0.00) 4(0.00) ".(0.00) 
Node-1.3: product(-0.00) amazon(0.00) platform(-0.00) title(0.00) content(-0.00) title(0.00) dewalt(0.00) dcb090(0.00) 12v(0.00) 20v(0.00) max(-0.00) usb(-0.00) power(-0.00) source.(-0.00) content(-0.00) dewalt(-0.00) dcb090(0.00) 12v(0.00) 20v(0.00) max(-0.00) usb(0.00) power(0.00) source(0.00) durable(0.00) enough(0.00) withstand(-0.00) jobsite(0.00) abuse.(-0.00) able(0.00) charge(0.00) 2(0.00) small(0.00) usb(-0.00) compatible(0.00) electronic(0.00) devices(0.00) jobsite(0.00) 12v(0.00) 20v(-0.00) max(0.00) batteries(-0.00) ac(0.00) power(0.00) available.(-0.00) unit(0.00) allows(0.00) work(0.00) dewalt(0.00) slide(0.00) style(0.00) battery(-0.00) packs.(-0.00) indicator(0.00) tells(0.00) unit(-0.00) powered(0.00) ready(0.00) charge(0.00) devices.(0.00) and,(0.00) similar(0.00) fuel(0.00) gauge,(0.00) indicates(0.00) amount(-0.00) power(-0.00) remaining(-0.00) battery.(0.00) commonly(-0.00) used(0.00) charging(-0.00) mobile(-0.00) phones,(-0.00) charging(0.00) digital(0.00) audio(-0.00) devises(-0.00) mp3(-0.00) players,(0.00) charging(0.00) digital(0.00) cameras,(0.00) charging(0.00) small(0.00) electronic(0.00) devices(-0.00) power(0.00) available.(0.00) 
Node-1.4: product(-0.00) amazon(0.00) platform(-0.00) title(0.00) content(0.00) title(0</verbalized-graph>

### Classification Label
Health & Personal Care

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 4736
- Title: Freud D0756N Diablo 7-1/4 56 Tooth TCG Non-Ferrous Metal and Plastic Cutting Saw Blade with 5/8-Inch Arbor, Diamond Knockout, and PermaShield Coating
- True class (canonical `y`): **Tools & Home Improvement**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Industrial & Scientific**
- Prediction recorded by this method's pipeline: **Health & Personal Care**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Freud D0756N Diablo 7-1/4 56 Tooth TCG Non-Ferrous Metal and Plastic Cutting Saw Blade with 5/8-Inch Arbor, Diamond Knockout, and PermaShield Coating. Content: For a high-impact blade that makes clean cuts in plastics and non-ferrous metals, look no further than the Freud D0756N Diablo 7.25-Inch Non-Ferrous Metal and Plastics Saw Blade. Thanks to its proprietary TCG (triple-chip grind) teeth, this is your go-to blade for slicing through plastic structures and non-ferrous metals such as copper pipes, aluminum extrusions, and brass plates.Model #D0756NDiameter7-1/4"Machine UseCircular SawApplicationNon-Ferrous Metals/PlasticsTeeth56 TCG(Triple-Chip Grind)Arbor5/8"(Diamond knockout arbor)Kerf.106"Hook Angle-6&deg;Makes Clean, Razor-Sharp Cuts in Plastic and Non-Ferrous MetalsAchieving premium results when working with plastics and non-ferrous metals is all about clean, accurate cuts. The Freud D0756N makes this process easy, fast, and precise. For making flawless crosscuts, this blade's proprietary TCG (triple-chip grind) teeth leave a clean, burr-free finish.Contractors, construction workers, and avid do-it-yourselfers will want to keep this blade on hand for jobs that call for slicing through plastic structures and non-ferrous metal pipes, extrusions, and plates. Appropriate application materials include copper, aluminum, brass, and plastic.Produces Smooth, Quiet Cuts with Laser-Cut KerfThe Freud D0756N's clean-cutting design means that you can enjoy the comfort of smooth performance. The thin 0.106-inch kerf between the blade's 56 TCG (triple-chip grind) teeth is laser cut to provide ease of feed, so you have more control over the blade's position. This helps maximize both the accuracy of the cut and the efficiency of your work, so you enjoy a job well done and the ability to complete more tasks in less time.An added bonus, the blade's laser-cut stabilizer vents reduce noise and vibration during operation, keeping your work environment more relaxed and your hands more in control. This feature also reduces friction and warping, helping to extend the blade's cutting life.Features Shock-Resistant Carbide for Long-Lasting PrecisionSo you can count on it over the long term, the Freud D0756N is designed for durability. The blade's hardy teeth are protected by Freud's exclusive shock-resistant TiCo Hi-Density Carbide formula, which helps fight wear and tear and maintains blade sharpness up to four times longer than standard carbide. And protecting the blade is Perma-Shield Non-Stick Coating that provides resistance to heat and corrosion.Fits Circular SawsThe Freud D0756N is a great addition to your workshop because it's designed with the versatility to fit a variety of circular saws.This product is covered by Freud's Limited Lifetime Warranty.What's in the BoxFreud D0756N Diablo 7.25-Inch Non-Ferrous Metal and Plastic Saw Blade.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 6 nodes

| node id | true class | title |
|---|---|---|
| 526 | Tools & Home Improvement | DEWALT D26960K Heavy Duty Heat Gun with LCD Display |
| 24539 | Tools & Home Improvement | Freud LU94M010 10-Inch 80 Tooth MTCG Plexiglass and Plastic Cutting Saw Blade with 5/8-Inch Arbor |
| 24540 | Tools & Home Improvement | Freud D1084L 10-Inch Diameter 84t TCG Saw Blade with 5/8-Inch Arbor |
| 24541 | Tools & Home Improvement | DEWALT DWE575SB 7-1/4-Inch Lightweight Circular Saw with Electric Brake |
| 24542 | Automotive | "Extra-Large 72&quot; x 96&quot; Cargo Net with 28 Hooks - Stretches to 10' x 14'!" |
| 24543 | Industrial & Scientific | IPS AAB4 Weld-On 1.25 oz Applicator Bottle with Needle |

### 2-hop (shortest distance exactly 2): 10 nodes

| node id | true class | title |
|---|---|---|
| 33 | Automotive | Bosch Bosch L-RACK Complete Kit with (1) i-boxx53, (2) LST72-OD, (3) L-RACK-S, and (1) L-RACK-T |
| 4730 | Tools & Home Improvement | DEWALT DWS520K 6-1/2-Inch TrackSaw Kit |
| 4731 | Automotive | CPS Products QC14SET Conversion Style Coupler Set R-12 to R-134A |
| 4732 | Tools & Home Improvement | DEWALT DCB090 12V/20V Max USB Power Source |
| 4733 | Automotive | ATD Tools 393 Heat Shrink Tube Assortment |
| 4734 | Home & Kitchen | Bench Dog Tools 10-054 Cookie Cone |
| 4735 | Tools & Home Improvement | DEWALT DWHT62512 4 Piece Screwdriver Set |
| 4737 | Tools & Home Improvement | DEWALT DCD740C1 20-Volt MAX Li-Ion Compact Right Angle 1.5 Ah Drill Kit |
| 4738 | Tools & Home Improvement | MICRO MESH 5&quot; - 8-HOLE 9 PC SANDING DISC ASSORTMENT PACK |
| 4739 | Patio, Lawn & Garden | King Canopy HC1020PC 10-Feet by 20-Feet Hercules 8-Leg Canopy, White |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/13.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Health & Personal Care**, ground truth = **Tools & Home Improvement**.
The verbalized graph is 18912 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 4736 | 259 | 0.1019 | yes |
| Node-1 | 1 | 526 | 26 | 0.0250 | yes |
| Node-1.1 | 7 | 33 | 222 | 0.0010 | yes |
| Node-1.2 | 8 | 4731 | 41 | 0.0012 | yes |
| Node-1.3 | 9 | 4732 | 141 | 0.0009 | yes |
| Node-1.4 | 10 | 4733 | 120 | 0.0027 | yes |
| Node-1.5 | 11 | 4734 | 82 | 0.0008 | no |
| Node-1.6 | 12 | 4730 | 117 | 0.0008 | no |
| Node-1.7 | 13 | 4737 | 273 | 0.0007 | no |
| Node-1.8 | 14 | 4738 | 116 | 0.0006 | no |
| Node-1.9 | 15 | 4739 | 51 | 0.0013 | no |
| Node-2 | 2 | 24539 | 250 | 0.0310 | no |
| Node-3 | 3 | 24540 | 255 | 0.0141 | no |
| Node-4 | 4 | 24541 | 27 | 0.0117 | no |
| Node-5 | 5 | 24542 | 67 | 0.0158 | no |
| Node-6 | 6 | 24543 | 82 | 0.0102 | no |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->Node-1.6, Node-1->Node-1.7, Node-1->Node-1.8, Node-1->Node-1.9, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, Node-1.6->Node-1, Node-1.7->Node-1, Node-1.8->Node-1, Node-1.9->Node-1, Node-2->ROOT, Node-3->ROOT, Node-4->ROOT, Node-5->ROOT, Node-6->ROOT, ROOT->Node-1, ROOT->Node-2, ROOT->Node-3, ROOT->Node-4, ROOT->Node-5, ROOT->Node-6

### Tokens and scores

**ROOT** (global 4736):

~~~~~~text
product (0.0097) from (-0.0268) amazon (0.0164) platform (0.0213) with (-0.0160) title (0.0170) and (0.0080) content (0.0085) : (0.0167) title (0.0204) : (-0.0309) freud (0.1019) d0756n (0.0044) diablo (0.0387) 7- (0.0101) 1 (0.0056) / (0.0208) 4 (0.0175) 56 (0.0219) tooth (-0.0113) tcg (0.0061) non- (0.0075) ferrous (0.0088) metal (0.0181) and (0.0059) plastic (-0.0019) cutting (0.0028) saw (0.0151) blade (0.0056) with (-0.0169) 5 (0.0079) / (0.0123) 8- (0.0095) inch (0.0024) arbor, (0.0122) diamond (-0.0023) knockout, (0.0070) and (0.0014) permashield (-0.0008) coating. (0.0254) content (0.0116) : (-0.0275) for (-0.0175) a (-0.0023) high- (0.0060) impact (0.0016) blade (0.0226) that (-0.0147) makes (-0.0118) clean (-0.0010) cuts (-0.0259) in (-0.0170) plastics (0.0380) and (0.0004) non- (0.0026) ferrous (0.0078) metals, (-0.0111) look (-0.0063) no (0.0206) further (0.0208) than (-0.0196) the (-0.0118) freud (-0.0571) d0756n (0.0052) diablo (0.0161) 7. (0.0155) 25- (0.0082) inch (0.0023) non- (0.0025) ferrous (0.0161) metal (0.0169) and (-0.0065) plastics (0.0218) saw (0.0054) blade. (0.0132) thanks (0.0301) to (0.0018) its (0.0116) proprietary (-0.0047) tcg (0.0166) ( (-0.0096) triple- (0.0158) chip (-0.0005) grind (0.0033) ) (0.0055) teeth, (-0.0077) this (-0.0008) is (0.0230) your (-0.0534) go- (0.0209) to (-0.0033) blade (-0.0103) for (0.0003) slicing (-0.0320) through (0.0129) plastic (0.0088) structures (-0.0227) and (0.0214) non- (0.0049) ferrous (0.0065) metals (0.0026) such (-0.0001) as (-0.0070) copper (0.0041) pipes, (0.0084) aluminum (0.0091) extrusions, (0.0136) and (0.0147) brass (0.0061) plates. (0.0432) model (0.0126) # (0.0462) d0756ndiameter7- (0.0055) 1 (0.0011) / (0.0027) 4 (-0.0014) " (0.0171) machine (0.0126) usecircular (0.0025) sawapplicationnon- (0.0044) ferrous (0.0110) metals (0.0085) / (0.0143) plasticsteeth56 (0.0121) tcg (0.0119) ( (0.0123) triple- (0.0148) chip (0.0057) grind (0.0127) ) (0.0091) arbor5 (0.0138) / (0.0128) 8 (0.0063) " (-0.0033) ( (0.0177) diamond (-0.0032) knockout (-0.0117) arbor (0.0209) ) (0.0078) kerf. (0.0198) 106 (0.0091) " (0.0132) hook (0.0079) angle- (0.0122) 6 (0.0119) & (0.0078) deg (0.0054) ; (0.0599) makes (0.0001) clean, (0.0140) razor- (0.0137) sharp (0.0126) cuts (0.0269) in (-0.0094) plastic (0.0275) and (0.0009) non- (0.0019) ferrous (0.0118) metalsachieving (-0.0133) premium (0.0010) results (0.0155) when (-0.0216) working (0.0094) with (-0.0121) plastics (0.0032) and (-0.0053) non- (0.0000) ferrous (0.0015) metals (-0.0112) is (0.0145) all (0.0015) about (-0.0028) clean, (0.0053) accurate (0.0025) cuts. (0.0017) the (-0.0656) freud (-0.0453) d0756n (-0.0051) makes (0.0014) this (0.0037) process (0.0133) easy, (0.0084) fast, (0.0075) and (0.0096) precise. (0.0182) for (-0.0235) making (0.0078) flawless (0.0069) crosscuts, (0.0109) this (0.0111) blade (0.0012) ' (-0.0069) s (0.0185) proprietary (-0.0037) tcg (0.0081) ( (0.0069) triple- (0.0133) chip (0.0015) grind (0.0105) ) (0.0117) teeth (-0.0069) leave (-0.0044) a (0.0060) clean, (0.0100) burr- (0.0173) free (0.0084) finish. (0.0173) contractors, (0.0057) construction (0.0122) workers, (0.0092) and (0.0096) avid (-0.0022) do- (0.0036) it- (0.0056) yourselfers (0.0162) will (0.0096) want (0.0178) to (0.0036) keep (-0.0134) this (-0.0130) blade (-0.0574) on (0.0225) hand (-0.0257) for (-0.0219) jobs (0.0271) that (0.0122) call (0.0403) for (-0.0016) slicing (-0.0157) through (-0.0394) plastic (0.0158) structures (0.0088) and (0.0293) non- (0.0009) ferrous (-0.0002) metal (0.0096) pipes, (0.0105) extrusions, (0.0116) and (0.0220) plates. (0.0156) appropriate (-0.0023) application (0.0083) materials (0.0040) include (0.0112) copper, (0.0152) aluminum, (0.0155) brass, (0.0054) and (0.0061) plastic. (0.0247) produces (0.0015) smooth, (0.0068) quiet (0.0235) cuts (0.0008) with (-0.0279) laser- (-0.0158) cut (-0.0117) kerfthe (0.0051) freud (-0.0371) d0756n (-0.0015)
~~~~~~

**Node-1** (global 526):

~~~~~~text
product (0.0250) from (0.0122) amazon (0.0095) platform (0.0160) with (0.0051) title (0.0172) and (0.0157) content (0.0121) : (0.0181) title (0.0189) : (0.0145) dewalt (0.0007) d26960k (0.0093) heavy (0.0036) duty (0.0056) heat (0.0083) gun (0.0048) with (-0.0024) lcd (0.0066) display. (0.0119) content (0.0145) : (0.0018) 3 (-0.0086) year (-0.0076) limited (0.0154) warranty (0.0102)
~~~~~~

**Node-1.1** (global 33):

~~~~~~text
product (-0.0003) from (-0.0002) amazon (0.0000) platform (-0.0003) with (-0.0002) title (0.0001) and (0.0001) content (-0.0001) : (0.0001) title (0.0002) : (-0.0000) bosch (0.0000) bosch (-0.0003) l- (-0.0000) rack (-0.0001) complete (0.0001) kit (0.0000) with (-0.0001) ( (0.0000) 1 (0.0000) ) (0.0000) i- (0.0001) boxx53, (0.0001) ( (0.0001) 2 (0.0001) ) (-0.0001) lst72- (0.0001) od, (0.0001) ( (0.0001) 3 (0.0000) ) (-0.0002) l- (-0.0001) rack- (-0.0000) s, (0.0000) and (0.0001) ( (0.0000) 1 (0.0000) ) (-0.0002) l- (0.0001) rack- (-0.0001) t. (0.0002) content (-0.0001) : (0.0000) the (-0.0001) bosch (-0.0007) click (0.0000) and (-0.0001) go (-0.0001) storage (-0.0002) system (-0.0001) is (-0.0002) designed (0.0002) to (0.0000) help (-0.0001) you (-0.0002) stay (-0.0001) organized (0.0002) and (-0.0000) get (0.0000) your (0.0003) tools (0.0000) on (0.0000) and (-0.0001) off (0.0002) the (0.0002) jobsite (0.0001) faster, (0.0002) so (0.0005) you (0.0003) can (-0.0000) spend (-0.0001) less (0.0001) time (0.0002) setting (0.0001) up (0.0001) and (0.0001) more (0.0001) time (0.0001) being (0.0000) productive. (0.0003) it (0.0001) ' (0.0000) s (0.0002) the (0.0001) ultimate (0.0001) in (0.0001) customized (-0.0004) organization (0.0004) and (0.0000) efficiency. (0.0010) organize (-0.0003) over (-0.0000) 90, (0.0001) 000 (0.0001) nuts (0.0005) and (0.0003) bolts (0.0004) and (0.0001) house (0.0001) over (0.0001) 100 (0.0003) types (0.0002) of (0.0001) power (0.0004) tools. (-0.0006) the (0.0007) click (-0.0004) and (0.0003) go (0.0002) storage (0.0003) system (-0.0004) featuring (-0.0000) the (-0.0002) l- (-0.0001) boxx (-0.0001) is (0.0002) available (0.0004) in (0.0000) 5 (0.0002) sizes (0.0000) and (-0.0000) fully (-0.0001) customizable (-0.0001) with (0.0000) foam, (0.0001) plastic (0.0001) inserts, (0.0000) drawers (-0.0002) and (0.0001) exact- (-0.0000) fit (0.0000) insert (0.0001) trays (0.0000) sold (-0.0000) separately. (0.0000) every (0.0000) l- (0.0000) boxx (0.0001) quickly (0.0001) fits (-0.0001) together (0.0001) with (-0.0001) just (0.0001) 1- (-0.0000) click (0.0001) stacking. (0.0001) the (0.0001) l- (0.0001) rack (-0.0001) allows (0.0002) you (0.0003) to (-0.0000) expand (-0.0001) your (0.0003) current (0.0001) system (0.0001) with (-0.0002) instant (0.0001) organization (-0.0000) capability (-0.0002) for (-0.0000) even (0.0001) more (0.0001) versatility. (0.0001) the (-0.0000) l- (0.0001) rack (0.0002) ' (-0.0001) s (0.0000) customizable (0.0000) expansion (0.0003) options (0.0001) for (-0.0000) the (0.0001) click (0.0003) & (0.0001) go (0.0002) system (0.0002) utilizes (0.0000) i- (0.0001) boxx (0.0000) trays (-0.0000) and (0.0000) drawers (-0.0002) and (0.0001) adds (-0.0001) the (0.0002) convenience (-0.0001) of (0.0000) providing (-0.0001) an (0.0002) extra (-0.0001) storage (0.0000) shelf (0.0001) to (0.0002) any (0.0003) l- (-0.0000) boxx (-0.0000) ( (0.0001) 1, (0.0001) 2, (0.0001) 3, (0.0001) 3d, (0.0001) or (-0.0001) 4 (0.0004) ). (0.0000) use (-0.0003) the (0.0002) l- (-0.0000) cart (0.0002) or (0.0000) the (0.0000) l- (0.0002) dolly (-0.0001) for (-0.0000) easy (0.0001) transport (0.0004) on (0.0003) and (-0.0001) off (0.0004) the (0.0002) job. (0.0004)
~~~~~~

**Node-1.2** (global 4731):

~~~~~~text
product (-0.0005) from (0.0009) amazon (0.0012) platform (-0.0002) with (-0.0004) title (0.0006) and (-0.0000) content (0.0001) : (0.0006) title (0.0005) : (0.0007) cps (0.0000) products (0.0001) qc14set (0.0005) conversion (0.0002) style (0.0002) coupler (0.0000) set (0.0004) r- (0.0001) 12 (0.0003) to (0.0003) r- (0.0000) 134a. (0.0005) content (0.0011) : (0.0002) with (-0.0001) pump (-0.0000) adapter (0.0002) 1 (0.0001) / (-0.0001) 2 (-0.0002) " (0.0002) turn (0.0002) open (0.0000) / (0.0005) close (0.0006) valves (0.0001) 1 (0.0004) / (-0.0005) 4 (0.0002) ". (0.0004)
~~~~~~

**Node-1.3** (global 4732):

~~~~~~text
product (-0.0007) from (-0.0002) amazon (0.0005) platform (-0.0000) with (-0.0001) title (0.0002) and (0.0002) content (-0.0003) : (0.0002) title (0.0004) : (0.0004) dewalt (0.0001) dcb090 (0.0001) 12v (0.0001) / (-0.0000) 20v (0.0001) max (-0.0000) usb (-0.0002) power (-0.0000) source. (-0.0001) content (-0.0001) : (-0.0000) the (-0.0001) dewalt (-0.0001) dcb090 (0.0001) 12v (0.0001) / (0.0000) 20v (0.0001) max (-0.0000) usb (0.0000) power (0.0000) source (0.0001) is (0.0003) durable (0.0002) enough (0.0003) to (0.0002) withstand (-0.0001) jobsite (0.0005) abuse. (-0.0003) able (0.0005) to (0.0001) charge (0.0001) up (0.0002) to (0.0003) 2 (0.0003) small (0.0001) usb (-0.0001) compatible (0.0002) electronic (0.0001) devices (0.0001) on (0.0002) / (0.0001) at (0.0003) the (-0.0003) jobsite (0.0004) off (0.0003) your (0.0001) 12v (0.0000) or (0.0003) 20v (-0.0000) max (0.0000) batteries (-0.0003) when (0.0002) ac (0.0001) power (0.0000) is (0.0002) not (0.0001) available. (-0.0000) this (0.0003) unit (0.0004) allows (0.0001) you (0.0003) to (0.0001) work (0.0005) with (0.0004) all (0.0003) dewalt (0.0001) slide (0.0009) style (0.0006) battery (-0.0002) packs. (-0.0001) it (0.0006) has (0.0004) an (0.0002) indicator (0.0008) that (0.0003) tells (0.0008) you (0.0005) when (0.0002) unit (-0.0001) is (0.0002) powered (0.0001) on (0.0003) and (0.0003) ready (0.0002) to (0.0001) charge (0.0002) devices. (0.0004) and, (0.0004) similar (0.0004) to (0.0002) a (-0.0000) fuel (0.0000) gauge, (0.0001) it (0.0004) indicates (0.0003) the (-0.0003) amount (-0.0002) of (-0.0001) power (-0.0000) remaining (-0.0002) in (0.0001) the (0.0004) battery. (0.0002) commonly (-0.0007) used (0.0005) for (0.0002) : (-0.0003) charging (-0.0001) mobile (-0.0004) phones, (-0.0001) charging (0.0001) digital (0.0001) audio (-0.0001) devises (-0.0001) / (-0.0000) mp3 (-0.0005) players, (0.0002) charging (0.0001) digital (0.0004) cameras, (0.0001) and (0.0002) charging (0.0003) small (0.0001) electronic (0.0002) devices (-0.0001) when (-0.0002) power (0.0000) is (0.0001) not (0.0003) available. (0.0003)
~~~~~~

**Node-1.4** (global 4733):

~~~~~~text
product (-0.0005) from (-0.0005) amazon (0.0027) platform (-0.0000) with (0.0001) title (0.0006) and (0.0003) content (0.0005) : (0.0001) title (0.0006) : (0.0008) atd (0.0002) tools (-0.0002) 393 (0.0002) heat (-0.0000) shrink (-0.0006) tube (0.0002) assortment. (-0.0009) content (0.0009) : (0.0010) the (0.0001) tubes (-0.0001) shrink (-0.0001) to (0.0001) fit (0.0004) over (0.0004) cable (0.0005) splices (0.0004) and (0.0004) can (0.0002) be (0.0004) used (0.0003) for (0.0003) wire (0.0004) harnessing, (0.0003) covering, (0.0006) marking (0.0003) and (0.0007) bundling (0.0000) of (0.0000) wires. (0.0006) they (0.0008) can (0.0001) be (0.0003) used (0.0003) for (0.0004) auto, (0.0003) marine, (0.0003) plane, (0.0001) home, (0.0004) industrial (-0.0003) and (0.0008) computer (0.0002) use. (0.0006) the (-0.0010) assortment (-0.0006) includes (0.0004) the (-0.0008) following (0.0003) sizes (0.0011) in (0.0003) multi- (0.0003) colors (0.0002) : (-0.0003) ( (-0.0002) 40 (-0.0005) )- (-0.0001) 3 (0.0003) / (0.0003) 32 (0.0003) inch, (0.0002) ( (0.0003) 55 (0.0004) )- (0.0002) 1 (0.0003) / (0.0004) 8 (0.0001) inch, (0.0001) ( (0.0005) 55 (0.0003) )- (0.0003) 3 (0.0004) / (0.0005) 16 (0.0001) inch, (0.0002) ( (0.0005) 55 (0.0001) )- (0.0003) 1 (0.0003) / (0.0006) 4 (0.0004) inch, (0.0004) ( (0.0008) 5 (0.0003) )- (0.0005) 5 (0.0003) / (0.0008) 8 (0.0002) inch, (0.0004) ( (0.0008) 10 (0.0002) )- (0.0006) 3 (0.0004) / (0.0004) 8 (0.0004) inch, (0.0001) ( (0.0005) 10 (0.0002) )- (0.0002) 1 (0.0005) / (0.0002) 2 (0.0005) inch, (0.0002) ( (0.0006) 5 (0.0004) )- (0.0002) 3 (0.0005) / (0.0001) 4 (0.0000) inch. (0.0004)
~~~~~~

**Node-1.5** (global 4734):

~~~~~~text
product (0.0000) from (-0.0003) amazon (0.0004) platform (0.0002) with (-0.0001) title (-0.0000) and (-0.0003) content (0.0008) : (0.0008) title (0.0002) : (0.0007) bench (0.0002) dog (0.0001) tools (0.0002) 10- (0.0001) 054 (0.0000) cookie (0.0003) cone. (0.0001) content (0.0005) : (0.0002) bench (0.0002) dog (-0.0001) bench (0.0003) cookie (0.0003) cones (0.0003) lift (0.0007) your (-0.0004) project (0.0002) off (-0.0001) your (0.0002) bench (0.0002) with (0.0001) minimal (0.0001) surface (0.0001) contact, (0.0002) keeping (0.0002) it (0.0002) stable (0.0000) during (-0.0001) the (0.0000) entire (0.0001) finishing (-0.0000) process. (0.0001) custom (0.0001) sized (0.0002) to (-0.0000) fit (0.0001) snugly (0.0002) over (-0.0000) the (0.0002) incredibly (0.0007) popular (0.0002) bench (0.0001) dog (0.0004) bench (0.0001) cookie (0.0002) work (0.0006) grippers. (-0.0002) team (0.0005) a (0.0007) set (0.0001) of (0.0002) bench (0.0003) cookie (0.0002) cones (0.0000) with (0.0001) a (0.0002) set (0.0001) of (0.0002) bench (0.0000) cookie (0.0002) work (0.0004) grippers (0.0002) for (0.0002) a (0.0005) fail- (0.0002) safe (-0.0000) project (0.0007) finishing (-0.0002) system. (-0.0000) patent (-0.0008) pending. (0.0004)
~~~~~~

**Node-1.6** (global 4730):

~~~~~~text
product (0.0004) from (-0.0001) amazon (0.0003) platform (-0.0002) with (-0.0002) title (0.0002) and (0.0001) content (0.0004) : (0.0001) title (0.0001) : (0.0004) dewalt (0.0001) dws520k (0.0000) 6- (0.0002) 1 (0.0001) / (0.0001) 2- (0.0002) inch (-0.0001) tracksaw (0.0004) kit. (0.0000) content (0.0001) : (0.0002) the (-0.0001) 12 (0.0002) amp (-0.0002) 6- (0.0002) 1 (0.0001) / (0.0003) 2- (0.0003) inch (0.0002) tracksaw (0.0002) delivers (0.0004) table (0.0001) saw (-0.0001) precision, (0.0003) panel (0.0002) saw (0.0006) capacity, (0.0003) and (0.0004) hand (0.0004) saw (0.0004) portability. (-0.0001) the (-0.0000) zero- (0.0003) clearance (-0.0001) track (0.0002) system (0.0003) and (0.0003) dual (0.0002) anti- (0.0003) splinter (0.0000) edges (0.0003) ensure (-0.0007) perfectly (0.0003) straight, (0.0003) splinter- (-0.0001) free (0.0001) cuts. (-0.0010) the (0.0005) specially (-0.0001) designed (0.0005) transmission (0.0003) and (0.0005) precision- (0.0004) ground, (0.0003) laser- (0.0001) cut (0.0001) woodworking (0.0001) blade (0.0000) minimize (0.0004) deflection (0.0001) to (0.0002) deliver (0.0005) a (0.0001) finished (0.0001) edge, (-0.0000) just (-0.0002) like (0.0002) a (0.0001) table (0.0002) saw. (0.0008) make (-0.0005) any (-0.0001) cut, (0.0002) anywhere, (0.0000) at (0.0005) any (0.0002) angle, (0.0002) even (0.0003) bevel (0.0003) or (0.0003) inside (0.0003) plunge (0.0004) cuts, (0.0002) as (0.0002) easily (-0.0001) as (0.0001) connecting (0.0000) the (-0.0000) dots. (0.0001) attach (-0.0005) a (0.0007) vacuum (0.0002) and (0.0001) up (0.0002) to (0.0001) 90 (0.0001) % (0.0003) of (0.0002) the (-0.0000) dust (0.0001) gets (0.0003) collected (0.0002) to (0.0000) minimize (0.0004) clean (0.0003) up. (0.0002)
~~~~~~

**Node-1.7** (global 4737):

~~~~~~text
product (-0.0000) from (-0.0002) amazon (-0.0001) platform (0.0001) with (-0.0001) title (0.0000) and (0.0000) content (0.0002) : (-0.0000) title (0.0000) : (0.0000) dewalt (-0.0000) dcd740c1 (0.0000) 20- (0.0000) volt (0.0000) max (-0.0000) li- (0.0000) ion (-0.0001) compact (0.0001) right (0.0001) angle (0.0000) 1. (-0.0000) 5 (0.0000) ah (0.0002) drill (-0.0004) kit. (0.0002) content (-0.0000) : (-0.0001) dewalt (-0.0000) & (0.0000) rsquo (-0.0000) ; (-0.0005) s (-0.0001) dcd740c1 (0.0001) 20- (0.0000) volt (-0.0000) max (0.0001) lithium- (0.0001) ion (0.0001) compact (0.0002) 1. (0.0000) 5 (-0.0000) ah (0.0001) right (0.0000) angle (0.0000) drill (0.0006) kit (-0.0002) comes (-0.0002) equipped (0.0000) with (-0.0003) advanced (0.0001) technology (0.0001) and (-0.0002) innovative (0.0002) features (-0.0000) that (-0.0001) make (0.0000) it (-0.0000) ideal (0.0001) for (-0.0001) remodelers, (0.0000) carpenters, (0.0000) steel (0.0001) stud (0.0002) framers, (0.0001) woodworkers, (0.0000) electricians, (0.0001) and (-0.0001) plumbers. (-0.0000) its (0.0001) compact (0.0000) size (0.0000) and (-0.0000) two- (0.0000) speed (-0.0000) transmission (0.0001) make (-0.0001) it (-0.0000) easy (0.0001) to (-0.0000) get (0.0001) big (0.0000) jobs (0.0001) done (0.0000) in (-0.0000) small (0.0001) spaces. (-0.0000) dcd740c1 (0.0001) 20- (0.0001) volt (0.0000) maxlithium- (0.0001) ion (0.0000) compactright (0.0002) angle (-0.0000) drill (0.0006) kitat (-0.0003) a (-0.0000) glance (0.0002) : (0.0000) compact (0.0002) and (-0.0001) ergonomic (0.0002) design (0.0002) that (-0.0001) doesn (-0.0000) & (-0.0001) rsquo (0.0001) ; (-0.0000) t (0.0001) compromise (0.0003) on (-0.0001) powertwo- (0.0001) speed (-0.0000) transmission (0.0001) delivers (0.0001) 0- (0.0001) 650 (-0.0000) rpm (-0.0000) and (0.0000) 0- (0.0000) 2, (0.0001) 000 (0.0000) rpmfour- (0.0002) inch (0.0001) length (0.0001) allows (0.0002) users (0.0001) to (-0.0000) fit (0.0001) into (0.0000) hard- (0.0001) to- (0.0000) reach (0.0002) spacesone- (-0.0001) year (0.0001) free (0.0001) service (0.0002) contract (0.0001) and (0.0000) three- (0.0000) year (0.0001) limited (0.0001) warranty90- (0.0001) day (0.0001) money- (0.0001) back (0.0001) guaranteethe (0.0002) dcd740c1 (0.0001) 20- (0.0001) volt (0.0000) max (0.0000) lithium- (0.0001) ion (0.0000) compact (0.0002) 1. (0.0001) 5 (-0.0000) ah (-0.0000) right (0.0000) angle (0.0001) drill (0.0004) is (0.0001) small (0.0001) enough (0.0000) to (0.0000) get (-0.0000) into (0.0001) tight (-0.0000) spaces (0.0002) but (0.0000) powerful (0.0001) enough (-0.0000) to (-0.0000) get (0.0000) the (-0.0000) job (0.0001) done (-0.0000) ( (0.0002) view (0.0002) larger (0.0001) ). (0.0001) compact (0.0002) controlweighing (0.0001) in (-0.0001) at (-0.0001) only (0.0000) 3. (0.0002) 8 (0.0001) pounds (0.0001) and (-0.0001) measuring (0.0002) four (0.0000) inches (0.0002) in (-0.0000) length (0.0001) from (0.0001) front (0.0000) to (0.0001) back, (0.0001) the (0.0000) dcd740cl (-0.0002) has (0.0001) been (0.0002) designed (0.0001) for (0.0000) projects (0.0001) that (0.0000) involve (0.0001) prolonged (0.0001) work (0.0002) in (-0.0002) tight (-0.0001) places. (0.0002) it (0.0002) features (-0.0001) a (-0.0001) 3 (0.0001) / (-0.0001) 8- (-0.0000) inch- (0.0001) deep (0.0000) hex (0.0000) pocket, (0.0001) which (-0.0004) allows (0.0001) a (0.0001) 2- (-0.0000) inch (0.0000) hex (0.0000) bit (0.0002) to (0.0000) be (0.0001) installed (-0.0000) almost (0.0002) all (0.0000) the (0.0001) way (0.0001) into (0.0000) the (-0.0002) chuck, (0.0007) providing (0.0000) quality (0.0001) performance (0.0000) and (-0.0000) allowing (0.0002) for (-0.0000) steady (0.0002) control (0.0002) without (0.0000) compromising (0.0001) on (-0.0000) size. (0.0003) the (0.0003) slim (0.0001) and (-0.0001) ergonomic (0.0002) handle (0.0001) makes (-0.0001) the (-0.0001) drill (0.0006) easy (-0.0001) to (-0.0001) grip (-0.0001) for (-0.0001) long (0.0001) periods (0.0001) of (-0.0001) time, (-0.0000) thus (-0.0003) increasing (0.0000) productivity (0.0002) and (-0.0003) promoting (0.0002) user (0.0001)
~~~~~~

**Node-1.8** (global 4738):

~~~~~~text
product (0.0002) from (0.0001) amazon (0.0001) platform (-0.0001) with (0.0000) title (0.0000) and (0.0001) content (0.0003) : (-0.0000) title (0.0000) : (0.0002) micro (0.0002) mesh (-0.0001) 5 (-0.0000) & (-0.0000) quot (0.0002) ;- (0.0003) 8- (0.0002) hole (0.0002) 9 (-0.0001) pc (-0.0000) sanding (0.0002) disc (0.0001) assortment (0.0005) pack. (0.0002) content (-0.0000) : (0.0000) micro- (0.0002) mesh (-0.0003) is (0.0003) a (0.0002) unique (0.0002) cushioned (0.0002) abrasive (0.0001) capable (0.0001) of (0.0002) giving (0.0002) very (0.0001) fine (0.0002) & (0.0002) very (0.0002) controlled (0.0002) scratch (0.0003) patterns. (-0.0000) the (0.0002) grits (0.0003) range (0.0001) from (0.0001) 1500 (0.0002) to (0.0002) 12000. (-0.0000) the (0.0002) 1500 (0.0003) is (0.0002) slightly (0.0002) more (0.0002) coarse (0.0002) than (0.0003) a (0.0000) conventional (0.0003) 600 (0.0001) grit (0.0002) sandpaper (0.0002) & (0.0001) the (0.0000) 12000 (0.0001) will (0.0003) leave (0.0001) scratch (0.0004) patterns (0.0005) that (0.0002) cannot (0.0003) be (0.0002) detected (0.0003) by (0.0002) the (-0.0000) human (0.0004) eye. (0.0000) micro- (0.0004) mesh (-0.0001) abrasives (0.0003) can (0.0004) polish (0.0002) to (0.0002) an (0.0002) optically (0.0004) clear, (0.0002) reflective (0.0003) state (0.0002) or (0.0001) through (0.0004) the (0.0001) use (0.0003) of (0.0001) a (0.0001) more (0.0002) coarse (0.0006) grit, (0.0002) leave (0.0002) a (0.0002) matte (0.0002) or (0.0005) satin (0.0003) finish. (0.0006) excellent (0.0005) product (0.0000) to (0.0002) use (0.0003) as (0.0002) a (0.0001) final (0.0000) rub (0.0002) for (-0.0000) water- (0.0002) based (0.0002) finishes. (-0.0000)
~~~~~~

**Node-1.9** (global 4739):

~~~~~~text
product (0.0005) from (0.0007) amazon (0.0011) platform (0.0003) with (0.0006) title (0.0003) and (0.0008) content (0.0008) : (0.0012) title (0.0003) : (0.0005) king (0.0003) canopy (0.0013) hc1020pc (0.0008) 10- (0.0003) feet (0.0009) by (0.0003) 20- (0.0002) feet (0.0008) hercules (0.0002) 8- (0.0005) leg (0.0005) canopy, (0.0008) white. (0.0009) content (0.0012) : (0.0002) the (0.0004) hercules (-0.0000) line (0.0010) are (0.0012) durable (0.0006) and (0.0004) easy (0.0009) to (0.0004) assemble (0.0009) units (0.0001) with (0.0003) 2- (0.0006) inch (0.0007) frames. (0.0003) great (0.0002) for (0.0007) gatherings, (0.0010) quick (0.0011) shade (0.0007) or (0.0007) use (0.0006) as (0.0006) a (0.0001) detachable (0.0007) carport. (0.0007)
~~~~~~

**Node-2** (global 24539):

~~~~~~text
product (-0.0013) from (-0.0090) amazon (-0.0108) platform (0.0001) with (-0.0104) title (-0.0004) and (-0.0069) content (-0.0051) : (-0.0012) title (-0.0021) : (-0.0054) freud (0.0210) lu94m010 (0.0031) 10- (-0.0021) inch (-0.0054) 80 (0.0002) tooth (-0.0090) mtcg (-0.0041) plexiglass (-0.0072) and (-0.0173) plastic (-0.0004) cutting (-0.0113) saw (-0.0012) blade (-0.0091) with (-0.0071) 5 (0.0031) / (-0.0030) 8- (0.0008) inch (-0.0068) arbor. (0.0098) content (0.0042) : (-0.0100) the (-0.0112) 10- (-0.0018) inch (-0.0086) freud (0.0310) lu94m010 (-0.0015) plexiglass (-0.0006) and (-0.0166) plastic (0.0033) cutting (-0.0108) saw (0.0042) blade (0.0173) is (0.0089) a (-0.0006) heavy- (0.0012) duty, (0.0022) industrial (0.0041) blade (-0.0018) designed (0.0051) to (-0.0063) make (0.0017) smooth, (-0.0015) clean (0.0042) cuts (0.0066) when (-0.0145) working (0.0058) with (-0.0046) a (0.0089) wide (0.0074) range (0.0012) of (0.0005) plastics. (-0.0030) it (-0.0036) features (0.0041) a (0.0026) modified, (0.0058) application- (0.0033) specific, (-0.0015) triple- (0.0050) chip (0.0022) tooth (-0.0006) grind, (-0.0170) the (-0.0033) long- (0.0034) term (0.0088) dependability (0.0052) of (0.0010) tico (0.0029) high- (0.0030) density (0.0093) carbide, (-0.0008) and (-0.0179) the (0.0086) anti- (0.0087) friction (0.0118) performance (0.0124) of (-0.0029) freud (0.0044) ' (0.0070) s (0.0065) silver (-0.0027) i. (0.0017) c. (0.0024) e. (-0.0019) coating. (-0.0027) and (-0.0024) since (0.0063) it (-0.0016) produces (-0.0023) less (0.0027) heat (0.0028) than (-0.0018) standard (-0.0005) blades, (-0.0107) you (0.0061) don (-0.0013) ' (-0.0029) t (-0.0002) have (0.0010) to (-0.0010) worry (0.0029) about (0.0036) synthetic (-0.0037) work (0.0046) surfaces (-0.0009) melting. (0.0082) lu94m010 (0.0022) plexiglass (-0.0017) and (0.0024) plastic (-0.0108) cutting (0.0059) saw (-0.0172) bladeat (0.0021) a (0.0104) glance (-0.0165) : (-0.0070) ideal (-0.0014) for (0.0043) plexiglass, (0.0046) acrylic, (0.0004) polycarbonate, (0.0001) and (-0.0023) other (-0.0016) plastic (0.0067) from (-0.0010) 1 (-0.0004) / (0.0022) 4 (0.0017) to (0.0003) 1- (0.0002) 5 (0.0021) / (0.0005) 8 (0.0022) inches (0.0018) thickheavy- (0.0021) duty (0.0010) plate (0.0062) with (-0.0072) laser- (-0.0016) cut, (-0.0025) anti- (0.0040) vibration (-0.0004) slotssilver (0.0032) i. (0.0009) c. (-0.0005) e. (-0.0007) coating (-0.0034) reduces (-0.0008) friction (0.0037) and (-0.0046) prevents (-0.0009) gummingtechnical (0.0016) specs (-0.0010) : (0.0022) coatingsilver (0.0004) icediameter10 (-0.0004) " (0.0021) teeth80 (-0.0003) mtcgarbor5 (-0.0002) / (-0.0028) 8 (0.0024) " (-0.0142) kerf (-0.0018) ( (0.0035) k (0.0032) ). (-0.0012) 110plate (0.0032) ( (0.0046) p (0.0080) ). (0.0004) 087depth (0.0028) of (-0.0034) cutmodified (-0.0007) triple (0.0032) chip (0.0089) grind (0.0063) ( (0.0107) mtcg (0.0021) ) (-0.0042) tooth (0.0089) designfor (0.0124) long (-0.0026) life (0.0016) and (-0.0045) chipfree (0.0046) cuts (0.0085) in (0.0029) thick (0.0058) stock (0.0033) manmade (0.0015) materialsnegative (0.0037) hook (0.0032) angleminimizes (-0.0013) chipping (-0.0069) in (-0.0047) laminates (0.0005) and (-0.0053) melaminespecial (0.0021) grind (0.0054) and (0.0009) negative (0.0027) hook (0.0100) angle (0.0065) prevent (-0.0025) meltingbuilt (0.0009) to (0.0033) leave (0.0026) a (0.0117) crisp, (0.0006) high- (0.0010) quality (0.0027) finish (0.0047) when (-0.0093) cutting (-0.0087) acrylics, (0.0013) polycarbonates (0.0071) and (0.0045) other (0.0034) plastics, (-0.0021) this (0.0052) blade (-0.0073) features (0.0046) 80 (0.0083) teeth (0.0079) with (0.0022) a (0.0172) special, (0.0057) modified (0.0053) triple- (0.0064) chip (-0.0024) grind. (0.0109) based (0.0090) on (-0.0094) the (-0.0001) results (0.0027) of (0.0129) extensive (0.0178) computer (0.0183) simulations, (-0.0041)
~~~~~~

**Node-3** (global 24540):

~~~~~~text
product (-0.0008) from (0.0060) amazon (0.0086) platform (0.0034) with (0.0039) title (0.0039) and (0.0067) content (-0.0007) : (0.0046) title (0.0054) : (0.0025) freud (0.0086) d1084l (0.0012) 10- (0.0015) inch (0.0034) diameter (0.0032) 84t (0.0011) tcg (0.0003) saw (0.0003) blade (-0.0016) with (-0.0004) 5 (-0.0007) / (0.0024) 8- (0.0013) inch (0.0042) arbor. (0.0038) content (0.0004) : (-0.0030) for (0.0027) a (0.0041) clean- (0.0022) cutting (0.0020) blade (0.0031) that (-0.0021) makes (-0.0004) non- (0.0029) abrasive (0.0029) cuts (-0.0042) in (-0.0016) coarse (-0.0008) flooring (-0.0010) materials (0.0036) and (0.0046) non- (0.0024) ferrous (0.0003) metals, (0.0029) look (0.0022) no (0.0012) further (0.0036) than (0.0013) the (0.0005) freud (0.0016) d1084l (0.0011) 10- (0.0022) inch (0.0018) laminates, (0.0029) melamines, (0.0009) and (0.0067) non- (0.0025) ferrous (0.0008) metals (-0.0009) saw (0.0030) blade. (0.0024) this (0.0006) is (0.0033) your (0.0058) go- (0.0052) to (0.0035) blade (-0.0016) for (0.0031) thick (0.0010) flooring (0.0030) such (0.0024) as (0.0047) laminates (0.0032) and (0.0029) non- (0.0040) ferrous (0.0025) metals (0.0021) such (0.0056) as (0.0057) copper. (-0.0055) made (-0.0014) to (0.0085) cut (0.0029) flawlessly, (0.0082) this (0.0065) blade (0.0001) ' (0.0045) s (0.0018) proprietary (-0.0068) tcg (0.0001) ( (-0.0039) triple- (0.0033) chip (0.0009) grind (-0.0048) ) (-0.0022) teeth (0.0015) leave (0.0012) a (0.0022) smooth (0.0042) finish (0.0035) with (0.0027) no (0.0009) tear- (0.0014) out. (0.0021) model (-0.0005) # (-0.0010) d1084ldiameter10 (-0.0008) " (0.0067) machine (-0.0015) usemiter (0.0016) / (0.0028) slide (0.0028) miter (0.0020) saw, (0.0023) table (-0.0024) sawapplicationnon- (0.0015) ferrous (0.0009) metals, (0.0006) laminates (0.0007) & (0.0030) amp (0.0026) ; (-0.0045) laminate (0.0008) flooringteeth84 (-0.0014) tcg (0.0020) ( (0.0002) triple- (0.0013) chip (-0.0013) grind (-0.0004) ) (0.0001) arbor5 (-0.0003) / (0.0026) 8 (-0.0030) " (0.0019) kerf. (0.0044) 098 (0.0002) " (0.0034) hook (0.0013) angle5 (0.0022) & (0.0018) deg (0.0038) ; (-0.0034) cleanly (0.0004) cuts (0.0003) laminates, (0.0023) melamines, (0.0014) and (0.0071) non- (0.0018) ferrous (0.0004) metalsachieving (-0.0011) premium (0.0038) results (0.0034) when (0.0029) working (0.0020) with (0.0048) coarse (0.0020) flooring (-0.0017) materials (0.0005) and (0.0061) non- (0.0006) ferrous (-0.0005) metals (-0.0027) is (0.0008) all (0.0022) about (0.0049) clean, (0.0030) accurate (0.0002) cuts. (0.0008) the (-0.0077) freud (0.0011) d1084l (-0.0015) makes (-0.0021) this (0.0010) process (-0.0001) easy, (0.0050) fast, (0.0055) and (0.0067) precise. (0.0059) plus, (0.0026) this (0.0002) expertly (0.0027) constructed (0.0028) blade (-0.0075) boasts (0.0026) teeth (0.0012) with (0.0018) a (-0.0148) tcg (0.0023) ( (0.0069) triple- (0.0011) chip (0.0010) grind (-0.0005) ) (-0.0008) design (0.0031) that (0.0014) slice (0.0034) easily (0.0041) through (-0.0006) harsh (0.0117) flooring (0.0047) and (0.0050) non- (0.0034) ferrous (0.0002) metals (-0.0018) without (0.0039) creating (0.0009) tear- (0.0009) out. (-0.0029) contractors, (0.0009) construction (-0.0049) workers, (-0.0026) and (0.0063) avid (0.0013) do- (-0.0002) it- (0.0008) yourselfers (0.0019) will (-0.0034) want (0.0045) to (0.0012) keep (0.0014) this (0.0015) blade (-0.0145) on (0.0021) hand (0.0006) for (0.0007) jobs (0.0059) that (0.0024) call (0.0014) for (0.0034) creating (0.0030) clean, (0.0026) no- (0.0025) chip (-0.0025) cuts (-0.0007) in (0.0053) coarse (-0.0062) flooring (0.0037) and (0.0079) non- (0.0022) ferrous (0.0007) metals. (0.0141) appropriate (-0.0063) application (-0.0059) materials (-0.0003) include (0.0001) both (0.0014) single- (-0.0012) and (0.0045) double- (-0.0011) sided (-0.0017) varieties (0.0019) of (-0.0231) mel (-0.0192)
~~~~~~

**Node-4** (global 24541):

~~~~~~text
product (-0.0073) from (0.0117) amazon (-0.0052) platform (0.0034) with (0.0045) title (-0.0021) and (-0.0023) content (0.0007) : (0.0028) title (0.0053) : (0.0025) dewalt (0.0039) dwe575sb (0.0024) 7- (-0.0053) 1 (0.0055) / (0.0018) 4- (-0.0010) inch (0.0018) lightweight (0.0034) circular (0.0015) saw (-0.0014) with (0.0049) electric (0.0031) brake. (0.0044) content (-0.0050) : (-0.0017) none (0.0098)
~~~~~~

**Node-5** (global 24542):

~~~~~~text
product (0.0027) from (0.0158) amazon (0.0034) platform (-0.0031) with (0.0069) title (-0.0004) and (0.0028) content (0.0070) : (0.0068) title (0.0041) : (0.0081) " (0.0042) extra- (0.0021) large (0.0086) 72 (0.0017) & (0.0020) quot (0.0003) ; (0.0071) x (0.0057) 96 (-0.0012) & (0.0026) quot (0.0016) ; (0.0078) cargo (0.0077) net (0.0109) with (0.0029) 28 (0.0011) hooks- (0.0097) stretches (0.0107) to (0.0016) 10 (0.0017) ' (-0.0018) x (0.0051) 14 (0.0007) '! (0.0026) ". (0.0129) content (0.0048) : (0.0006) extra- (0.0052) large (0.0054) size (0.0074) for (0.0035) securing (0.0061) big (0.0104) payloads (0.0091) ; (0.0051) highly- (0.0055) versatile (-0.0056) tool (0.0080) that (-0.0002) ' (-0.0009) s (-0.0006) essential (0.0038) when (0.0065) you (-0.0009) need (0.0058) it-- (0.0073) takes (0.0039) up (0.0067) very (0.0032) little (0.0047) space (0.0129) when (0.0029) you (-0.0049) don (-0.0049) ' (0.0072) t. (0.0005)
~~~~~~

**Node-6** (global 24543):

~~~~~~text
product (-0.0034) from (0.0002) amazon (0.0028) platform (-0.0044) with (-0.0023) title (-0.0002) and (-0.0041) content (-0.0013) : (-0.0021) title (0.0005) : (-0.0025) ips (-0.0010) aab4 (-0.0009) weld- (0.0009) on (-0.0032) 1. (0.0019) 25 (-0.0010) oz (-0.0025) applicator (-0.0007) bottle (-0.0050) with (0.0022) needle. (0.0022) content (0.0013) : (-0.0040) 1- (-0.0003) 1 (-0.0005) / (0.0022) 4 (0.0013) fluid (0.0019) ounce (0.0031) oval (0.0024) polyethtylene (0.0002) squeeze- (0.0030) type (0.0015) applicator (0.0005) bottle (0.0015) with (0.0004) a (-0.0052) 25 (0.0006) gauge (-0.0005) 1- (-0.0007) inch (0.0013) stainless (-0.0002) steel (0.0022) needle. (0.0042) applicator (0.0002) bottle (0.0005) is (0.0045) ideal (-0.0004) for (-0.0009) precision (0.0025) cementing, (0.0020) solvent (0.0001) dispensing, (0.0023) and (0.0009) oiling. (0.0069) size (0.0010) of (0.0025) bottle (-0.0024) & (0.0029) # (-0.0007) 0058 (0.0051) ; (0.0020) 1- (0.0027) 1 (0.0015) / (0.0047) 4 (0.0019) fl (0.0041) oz (-0.0025) ( (-0.0023) 37 (-0.0001) ml (0.0008) ) (0.0028) length (-0.0065) of (-0.0011) needle (0.0102) & (0.0007) # (0.0033) 0058 (0.0061) ; (0.0042) 1- (-0.0000) in (-0.0012)
~~~~~~
