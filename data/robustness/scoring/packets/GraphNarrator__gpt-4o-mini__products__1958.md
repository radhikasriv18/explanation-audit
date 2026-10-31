# Reference packet: GraphNarrator__gpt-4o-mini__products__1958

- Method: GraphNarrator; configuration: gpt-4o-mini; dataset: products; target node: 1958
- Explanation source: `./robustness_2026-10-30/graphnarrator_gpt4omini/generated_expls-601/4.json` (messages[assistant])
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

- ROOT (Hayabusa fight shorts)
  - Node-1 (Muay Thai ankle support wraps)
    - Node-1.1 (Muay Thai steel cup)
    - Node-1.2 (Muay Thai shorts)
    - Node-1.3 (Ankle brace)
    - Node-1.4 (Piranha gear uniform pants)
    - Node-1.5 (Additional unspecified products)

1. **Word-Level Evaluation:**

The ROOT node contains keywords such as "fabric," "system," "fit," and "durability," which suggest a focus on performance and quality in sports apparel. The term "fight shorts" indicates a specific use case in combat sports, aligning with categories related to athletic wear. The presence of "mechanical," "polydirectional," and "stretch" highlights the functional aspects of the product, which are crucial for athletic performance.

2. **Graph-Level Aggregation:**

Node-1 (Muay Thai ankle support wraps) includes keywords like "support" and "protection," reinforcing the athletic context. Its direct neighbors (Node-1.1 to Node-1.5) further emphasize combat sports and athletic gear, with products like "Muay Thai steel cup" and "ankle brace" being essential for fighters. This interconnectedness among nodes showcases a strong relationship with combat sports, enhancing the classification of ROOT into "Cell Phones & Accessories" as it indicates a niche market focused on specific athletic needs.

### Free-Text Explanation
```markdown
The classification of ROOT into "Cell Phones & Accessories" is supported by its own keywords and the co-purchase neighborhood.

ROOT: Keywords like "fabric," "fit," and "durability" suggest that these Hayabusa fight shorts are designed for high-performance in combat sports, indicating a specialized athletic product.
  - Node-1: The Muay Thai ankle support wraps (keywords: "support," "protection") are directly related to combat sports, reinforcing the athletic context.
    - Node-1.1: The Muay Thai steel cup is a protective gear essential for fighters, further solidifying the connection to combat sports.
    - Node-1.2: Additional Muay Thai shorts emphasize the focus on athletic apparel.
    - Node-1.3: The ankle brace offers support, which is crucial for athletes, enhancing the overall athletic theme.
    - Node-1.4: Piranha gear uniform pants are also linked to martial arts, showcasing a variety of products aimed at combat sports enthusiasts.
    - Node-1.5: Additional unspecified products may also cater to similar athletic needs.

In summary, ROOT's keywords strongly signal its use in combat sports, and the entire co-purchase neighborhood consists of related athletic gear, providing robust evidence for the "Cell Phones & Accessories" category.
```
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/4.json`).

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
<verbalized-graph>ROOT: product(0.01) amazon(-0.02) platform(0.00) title(0.01) content(0.03) title(0.02) hayabusa(0.01) chikara(-0.01) fight(0.00) shorts.(0.00) content(0.02) designed(0.00) mechanical(0.00) polydirectional(0.01) stretch(0.01) fabric.(0.05) innovative(-0.04) tie(0.06) system(0.02) indestructible(0.01) webbing(0.01) distinct(0.02) customized(0.01) fit.(0.04) pro(0.01) performance(0.01) stretch(0.00) panel(0.02) split(-0.00) side(0.01) seams(0.02) unrestricted(0.01) range(0.02) motion.(0.01) contains(0.06) hayabusa(0.02) exclusive(0.02) guard(0.01) lock(0.01) inner(0.01) grip(0.03) waistband(0.05) system.(0.02) reinforced(0.04) t3(0.01) stitching(0.01) ultimate(0.02) strength(0.02) durability.(0.01) extraordinary(-0.01) high-(0.02) iq(0.01) odor(0.01) inhibiting(0.02) effects.(0.03) fiber-(0.02) fused(0.02) printing(0.04) technology(0.00) lasting(0.06) style.(-0.00) 
Node-1: product(0.00) amazon(0.00) platform(-0.00) title(0.00) content(0.01) title(0.00) muay(-0.00) thai(0.00) mma(0.00) ankle(-0.00) support(-0.00) wraps(0.00) pair(0.00) ).(-0.00) content(0.01) meister(0.00) mma(0.00) elastic(-0.00) compression(-0.00) ankle(-0.00) supports(-0.00) ideal(-0.00) use(-0.00) muay(0.00) thai,(0.00) mma,(0.00) wrestling,(0.00) boxing(-0.00) sports(0.00) demanding(-0.00) ankle(0.00) support.(0.00) slip(-0.00) workout(-0.00) session(0.00) give(0.00) ankles(0.00) support(-0.00) protection.(0.00) fit(0.01) men(-0.01) feet(-0.01) sizes(0.01) 7-(0.00) 14.(-0.00) 
Node-1.1: product(-0.00) amazon(0.00) platform(-0.00) title(0.00) content(-0.00) title(0.00) muay(0.00) thai(-0.00) men(-0.00) supporter(0.00) steel(0.00) cup(0.00) ".(0.00) content(0.00) improved(0.00) design(0.00) muay(0.00) thai(0.00) geltech(0.00) men(0.00) supporter(0.00) steel(0.00) cup.(0.00) molded(0.00) cup,(0.00) steel(0.00) construction.(0.00) genuine(0.00) leather(0.00) covering,(0.00) neoprene(0.00) gel(0.00) material(0.00) padded(0.00) along(0.00) edge(-0.00) added(0.00) comfortability,(0.00) thin(0.00) soft(0.00) foam(0.00) lining(0.00) inside(-0.00) cup(0.00) avoid(-0.00) direct(0.00) contact(0.00) metal(0.00) part(0.00) cup,(0.00) new(0.00) style(0.00) supporter.(-0.00) small(0.00) medium(0.00) size(0.00) fits(-0.00) 120-(0.00) 180lbs.(-0.00) large(0.00) x-(0.00) large(0.00) size(0.00) fits(-0.00) 180lbs(0.00) overplease(0.00) send(0.00) us(0.00) message(0.00) size(0.00) need(-0.00) purchase(0.00) sure(0.00) ship(-0.00) required(-0.00) size.(-0.00) 
Node-1.2: product(-0.00) amazon(0.00) platform(-0.00) title(0.00) content(0.00) title(0.00) muay(0.00) thai(-0.00) shorts-(0.00) black.(0.00) content(0.00) size(0.00) chart,(0.00) please(0.00) see(0.00) attached(0.00) photos.(0.00) improved(0.00) design(0.00) 3(0.00) inches(0.00) long(0.00) split(0.00) side(0.00) seams(0.00) unrestricted(0.00) range(0.00) motion.(0.00) lightweight(0.00) satin.(0.00) made(0.00) soft(0.00) lightweight(0.00) satin.(0.00) traditional(-0.00) muay(0.00) thai(-0.00) kickboxing.(0.00) 4(0.00) waistband.(-0.00) muay(0.00) thai(0.00) thai(-0.00) lettering(0.00) across(0.00) front.(0.00) extra(-0.00) wide(0.00) leg(0.00) allows(0.00) room(0.00) kicking.(0.00) hidden(0.00) drawstring(0.00) inside(0.00) waistband.(0.00) 
Node-1.3: product(-0.00) amazon(0.00) platform(0.00) title(0.00) content(-0.00) title(0.00) compression(0.00) support(0.00) ankle(0.00) brace(0.00) size(0.00) small,(0.00) color(-0.00) black.(0.00) content(0.00) 3002-(-0.00) b(0.00) size(0.00) small,(0.00) color(-0.00) black(0.00) features(-0.00) :-(0.00) ankle(-0.00) brace.-(0.00) lightweight.-(0.00) breathable(0.00) material(0.00) four-(0.00) way(0.00) stretch.-(0.00) warm,(0.00) soothing(0.00) uniform(0.00) compression.-(0.00) unique(0.00) knitted(0.00) pattern(0.00) greater(0.00) vertical(0.00) stretch.-(0.00) latex-(0.00) free.-(0.00) measure(0.00) ankle(-0.00) bone.-(0.00) made(-0.00) usa.-(0.00) small(0.00) adjustable(0.00) size(0.00) 7.(0.00) 5(-0.00) "-(0.00) 8.(0.00) 5(-0.00) ".-(0.00) medium(0.00) adjustable(0.00) size(-0.00) 8.(0.00) 5(0.00) "-(0.00) 9.(0.00) 5(-0.00) ".-(0.00) large(0.00) adjustable(0.00) size(0.00) 9.(0.00) 5(0.00) "-(-0.00) 10.(0.00) 5(-0.00) ".-(0.00) x-(0.00) large(0.00) adjustable(0.00) size(-0.00) 10.(0.00) 5(0.00) "-(-0.00) 11.(0.00) 5(0.00) ".(0.00) construction(0.00) :-(0.00) seamless(0.00) construction(0.00) provides(0.00) maximum(0.00) comfort.(0.00) dimensions(0.00) :-(0.00) 8(0.00) h(0.00) x(0.00) 6(0.00) w(0.00) x(0.00) 1(-0.00) 0.(-0.00) 2(0.00) lb.(0.00) 
Node-1.4: product(-0.00) amazon(-0.00) platform(-0.00) title(0.00) content(0.00) title(0.00) piranha(0.00) gear(-0.00) uniform(0.00) pants-(0.00) drawstring(0.00) waist.(0.00) content(-0.00) sizing(-0.00) pants(0.00) may(0.00) expecting.(-0.00) please(0.00) sure(-0.00) check(-0.00) size(-0.00) charts(-0.00) make(-0.00) sure(0.00) going(0.00) get(0.00) good(0.00) fit(0.00) want(0.00) save(0.00) trouble(0.00) exchange.(-0.00) though(0.00) best(0.00) exchange(0.00) policy(-0.00) industry!(0.00) bleached(0.00) white(0.00) cotton(0.00) pants(0.00) made(0.00) jiu-(0.00) jitsu,(-0.00) judo(0.00) aikido.(0.00) reinforced(0.00) seams(0.00) reinforced(0.00) knees(0.00) cross(0.00) stitching(0.00) quilting(0.00) durability.(0.00) made(-0.00) 100(-0.00) cotton(-0.00) atraditional(-0.00) drawstring,(-0.00) pants(0.00) ones(0.00) included(-0.00) single(0.00) weave(0.00) piranha(0.00) gear(-0.00) uniforms.(0.00) carry(0.00) elastic(0.00) drawstring(-0.00) waist(0.00) pants(0.00) too-(0.00) separate(0.00) item-(0.00) though(-0.00) always(0.00) every(-0.00) color.(0.00) anything,(0.00) pants(0.00) run(-0.00) little(0.00) short.(0.00) sizes,(0.00) get(0.00) longer(0.00) bigger(-0.00) size.(-0.00) please(0.00) sure(0.00) check(0.00) size(-0.00) charts(-0.00) order.(-0.00) also(-0.00) keep(0.00) mind(0.00) size(0.00) a2(-0.00) isnot(0.00) sameas(0.00) size(0.00) 2(0.00) ".(-0.00) sure(0.00) checked(0.00) size(0.00) chart(0.00) get(0.00) size(0.00) wanted.(-0.00) 
Node-1.5: product(0.00) amazon(-0.00) platform(-0.00) titl</verbalized-graph>

### Classification Label
Cell Phones & Accessories

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 1958
- Title: Hayabusa Chikara Fight Shorts
- True class (canonical `y`): **Sports & Outdoors**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Sports & Outdoors**
- Prediction recorded by this method's pipeline: **Cell Phones & Accessories**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Hayabusa Chikara Fight Shorts. Content: Designed with Mechanical PolyDirectional stretch fabric. Innovative tie system with indestructible webbing for a distinct customized fit. Pro Performance stretch panel and split side seams for unrestricted range of motion. Contains Hayabusa's exclusive Guard lock inner grip waistband system. Reinforced T3 stitching for ultimate strength and durability. Extraordinary High-IQ odor inhibiting effects. Fiber-fused printing technology for lasting style.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 5 nodes

| node id | true class | title |
|---|---|---|
| 163 | Sports & Outdoors | Muay Thai MMA Ankle Support Wraps (Pair) |
| 164 | Sports & Outdoors | Hand Wrap Wash Bag w/ Bag Clip - Large |
| 165 | Clothing, Shoes & Jewelry | Revgear Muay Thai Shorts |
| 14711 | Clothing, Shoes & Jewelry | Hayabusa 70L Mesh Gear Bag, Black |
| 14712 | Sports & Outdoors | Hayabusa Pro Training Series Kick Shield |

### 2-hop (shortest distance exactly 2): 53 nodes

| node id | true class | title |
|---|---|---|
| 3 | Clothing, Shoes & Jewelry | Muay Thai Shorts-Black |
| 166 | Sports & Outdoors | "Revgear Women's Deluxe Muay Thai Short" |
| 168 | Clothing, Shoes & Jewelry | ARD xTreme MMA Fight Shorts UFC Cage Fight Grappling Muay Thai Boxing Black All Sizes |
| 169 | Clothing, Shoes & Jewelry | Muay Thai Shorts |
| 171 | Health & Personal Care | Namman Muay Thai Boxing Liniment 120ml |
| 1921 | Sports & Outdoors | TITLE Gel World Bag Gloves |
| 1930 | Clothing, Shoes & Jewelry | "Title Boxing Title Mma 8 Limbs Thai Men's Tee, M, Black" |
| 1940 | Sports & Outdoors | TapouT MMA Multipurpose Gloves (Small/Medium) |
| 1942 | Sports & Outdoors | Contender Fight Sports Knee Pads |
| 1947 | Sports & Outdoors | MMA Grappling Gloves Cage Fight Cowhide Leather, US Flag |
| 1948 | Sports & Outdoors | Junior 108&quot; Elastic Cotton MMA Hand Wraps (Pair) |
| 1949 | Sports & Outdoors | 4Q2 MMA Fight Socks |
| 1950 | Sports & Outdoors | Cloth Ankle Guard / Pads - Black - Piranha Gear |
| 1951 | Sports & Outdoors | Mrx MMA Fight Shorts Stretch Penals Black/Grey |
| 1952 | Sports & Outdoors | Piranha Gear Uniform Pants - Drawstring Waist |
| 1953 | Sports & Outdoors | Brute Torq Wrestling Knee Pad |
| 1954 | Clothing, Shoes & Jewelry | Hayabusa Mizuchi Short Sleeve Rashguard Shirt |
| 1955 | Sports & Outdoors | Revgear Thai Style Boxing Gloves |
| 1956 | Health & Personal Care | Compression Support Ankle Brace Size: Small, Color: Black |
| 1957 | Sports & Outdoors | "Muay Thai Men's Supporter with Steel Cup" |
| 1959 | Books | Boxing Mastery: Advanced Technique, Tactics, and Strategies from the Sweet Science |
| 1960 | Sports & Outdoors | Boon Sport Leather Training Gloves |
| 1961 | Health & Personal Care | Clear Gear Sports Spray Bottle, 24-Ounce |
| 1962 | Sports & Outdoors | Titan Competition Headgear |
| 1963 | Sports & Outdoors | Hayabusa Official MMA Shouri Bamboo Mizuchi T-Shirts/Tee |
| 1964 | Sports & Outdoors | Meister Mounted Metal Hand Wrap Roller |
| 1965 | Sports & Outdoors | TITLE Boxing 3/4 Length Stock Satin Robe |
| 1966 | Health & Personal Care | Authentic RDX Ankle Foot Support Anklet Pad MMA Brace Guard |
| 1967 | Sports & Outdoors | Hayabusa Logo T Shirt - White |
| 1968 | Clothing, Shoes & Jewelry | ARD Camo Pro MMA Fight Shorts Camouflage UFC Cage Fight Grappling Kickboxing |
| 1969 | Sports & Outdoors | Revgear Glove Dog Deodorizer |
| 1970 | Sports & Outdoors | Brazilian Jiu Jitsu Uniform or Gi Premium Black or Blue |
| 1971 | Sports & Outdoors | Brazilian Jiu Jitsu Uniform or Gi Premium Black or Blue |
| 1972 | Clothing, Shoes & Jewelry | Revgear Spartan MMA Fight Short |
| 1973 | Clothing, Shoes & Jewelry | "Shock Doctor Men's Power Supporter with BioFlex Cup" |
| 1974 | Health & Personal Care | Namman Muay Thai Boxing Analgesic Balm Massage Relief Ache 100g |
| 1975 | Clothing, Shoes & Jewelry | Muay Thai Shorts |
| 1976 | Sports & Outdoors | TITLE Classic MMA Protective Cup |
| 1986 | Clothing, Shoes & Jewelry | "Title Boxing Title Mma Submit Men's Tee, L, Yellow" |
| 1987 | Clothing, Shoes & Jewelry | Revgear Spartan MMA Fight Short |
| 1988 | Clothing, Shoes & Jewelry | Hayabusa Official MMA Champion Hoodie - Black |
| 1993 | Clothing, Shoes & Jewelry | Meister MMA Compression Rush Fight Shorts w/ Cup Pocket |
| 1994 | Sports & Outdoors | TITLE MMA Digital Interval Timer |
| 2000 | Clothing, Shoes & Jewelry | Hayabusa Flex Fight Shorts |
| 2001 | Sports & Outdoors | Muay Thai Shorts-Blue |
| 2002 | Clothing, Shoes & Jewelry | Lumpinee Muay Thai Kick Boxing Shorts : LUM-002 |
| 2003 | Clothing, Shoes & Jewelry | Revgear Deluxe Muay Thai Shorts |
| 2004 | Clothing, Shoes & Jewelry | New Winner Retro Muay Thai Shorts Kick Boxing K1 MMA Black Satin |
| 2009 | Sports & Outdoors | Muay Thai Shorts-Red |
| 2011 | Sports & Outdoors | Traditional Boxing Trunks, Blue or Red Color. Kids and Adult Sizes |
| 2016 | Sports & Outdoors | Rival d3o Intelli-Shock Pro Training Headgear |
| 2019 | Sports & Outdoors | Combat Sports Thai Style Jump Rope |
| 2021 | Sports & Outdoors | Fairtex Neoprene Shin Pads |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/4.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Cell Phones & Accessories**, ground truth = **Sports & Outdoors**.
The verbalized graph is 27767 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 1958 | 79 | 0.0648 | yes |
| Node-1 | 1 | 163 | 68 | 0.0092 | yes |
| Node-1.1 | 6 | 1957 | 113 | 0.0007 | yes |
| Node-1.2 | 7 | 3 | 74 | 0.0013 | yes |
| Node-1.3 | 8 | 1956 | 131 | 0.0012 | yes |
| Node-1.4 | 9 | 1952 | 213 | 0.0013 | yes |
| Node-1.5 | 10 | 1987 | 65 | 0.0011 | yes |
| Node-1.6 | 11 | 1993 | 117 | 0.0005 | no |
| Node-1.7 | 12 | 2002 | 63 | 0.0052 | no |
| Node-1.8 | 13 | 1942 | 54 | 0.0018 | no |
| Node-1.9 | 14 | 1951 | 78 | 0.0013 | no |
| Node-2 | 2 | 164 | 93 | 0.0150 | no |
| Node-2.1 | 15 | 1930 | 72 | 0.0007 | no |
| Node-2.2 | 16 | 1955 | 66 | 0.0037 | no |
| Node-2.3 | 17 | 1970 | 82 | 0.0015 | no |
| Node-2.4 | 18 | 169 | 68 | 0.0014 | no |
| Node-2.5 | 19 | 1986 | 62 | 0.0018 | no |
| Node-2.6 | 20 | 1960 | 88 | 0.0009 | no |
| Node-2.7 | 21 | 1965 | 65 | 0.0012 | no |
| Node-2.8 | 22 | 2016 | 60 | 0.0017 | no |
| Node-2.9 | 23 | 1964 | 94 | 0.0015 | no |
| Node-3 | 3 | 165 | 88 | 0.0257 | no |
| Node-3.1 | 24 | 1972 | 65 | 0.0019 | no |
| Node-3.2 | 25 | 1971 | 82 | 0.0011 | no |
| Node-3.3 | 26 | 1969 | 56 | 0.0007 | no |
| Node-3.4 | 27 | 171 | 38 | 0.0028 | no |
| Node-3.5 | 28 | 166 | 44 | 0.0028 | no |
| Node-3.6 | 29 | 2001 | 49 | 0.0016 | no |
| Node-3.7 | 30 | 2003 | 36 | 0.0020 | no |
| Node-3.8 | 31 | 2009 | 67 | 0.0014 | no |
| Node-3.9 | 32 | 2011 | 64 | 0.0010 | no |
| Node-4 | 4 | 14711 | 89 | 0.0317 | no |
| Node-4.1 | 33 | 1963 | 47 | 0.0030 | no |
| Node-4.2 | 34 | 1988 | 84 | 0.0016 | no |
| Node-4.3 | 35 | 1994 | 143 | 0.0046 | no |
| Node-4.4 | 36 | 2000 | 121 | 0.0028 | no |
| Node-5 | 5 | 14712 | 227 | 0.0142 | no |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->Node-1.6, Node-1->Node-1.7, Node-1->Node-1.8, Node-1->Node-1.9, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, Node-1.6->Node-1, Node-1.7->Node-1, Node-1.7->Node-3, Node-1.8->Node-1, Node-1.9->Node-1, Node-2->Node-2.1, Node-2->Node-2.2, Node-2->Node-2.3, Node-2->Node-2.4, Node-2->Node-2.5, Node-2->Node-2.6, Node-2->Node-2.7, Node-2->Node-2.8, Node-2->Node-2.9, Node-2->ROOT, Node-2.1->Node-2, Node-2.2->Node-2, Node-2.3->Node-2, Node-2.4->Node-2, Node-2.5->Node-2, Node-2.6->Node-2, Node-2.7->Node-2, Node-2.8->Node-2, Node-2.9->Node-2, Node-3->Node-1.7, Node-3->Node-3.1, Node-3->Node-3.2, Node-3->Node-3.3, Node-3->Node-3.4, Node-3->Node-3.5, Node-3->Node-3.6, Node-3->Node-3.7, Node-3->Node-3.8, Node-3->Node-3.9, Node-3->ROOT, Node-3.1->Node-3, Node-3.1->Node-4, Node-3.2->Node-3, Node-3.3->Node-3, Node-3.4->Node-3, Node-3.5->Node-3, Node-3.6->Node-3, Node-3.7->Node-3, Node-3.8->Node-3, Node-3.9->Node-3, Node-4->Node-3.1, Node-4->Node-4.1, Node-4->Node-4.2, Node-4->Node-4.3, Node-4->Node-4.4, Node-4->ROOT, Node-4.1->Node-4, Node-4.2->Node-4, Node-4.3->Node-4, Node-4.4->Node-4, Node-5->ROOT, ROOT->Node-1, ROOT->Node-2, ROOT->Node-3, ROOT->Node-4, ROOT->Node-5

### Tokens and scores

**ROOT** (global 1958):

~~~~~~text
product (0.0079) from (-0.0700) amazon (-0.0175) platform (0.0042) with (-0.0167) title (0.0140) and (-0.0187) content (0.0269) : (0.0523) title (0.0190) : (-0.0039) hayabusa (0.0110) chikara (-0.0087) fight (0.0015) shorts. (0.0041) content (0.0181) : (0.0297) designed (0.0039) with (0.0211) mechanical (0.0011) polydirectional (0.0078) stretch (0.0133) fabric. (0.0460) innovative (-0.0439) tie (0.0598) system (0.0154) with (0.0071) indestructible (0.0119) webbing (0.0058) for (0.0135) a (0.0303) distinct (0.0233) customized (0.0071) fit. (0.0350) pro (0.0106) performance (0.0135) stretch (0.0045) panel (0.0153) and (0.0086) split (-0.0000) side (0.0094) seams (0.0176) for (0.0114) unrestricted (0.0079) range (0.0214) of (0.0004) motion. (0.0106) contains (0.0572) hayabusa (0.0182) ' (0.0012) s (0.0095) exclusive (0.0179) guard (0.0068) lock (0.0070) inner (0.0142) grip (0.0341) waistband (0.0473) system. (0.0193) reinforced (0.0391) t3 (0.0076) stitching (0.0127) for (0.0198) ultimate (0.0181) strength (0.0204) and (0.0316) durability. (0.0089) extraordinary (-0.0096) high- (0.0189) iq (0.0110) odor (0.0137) inhibiting (0.0193) effects. (0.0257) fiber- (0.0166) fused (0.0241) printing (0.0383) technology (0.0037) for (0.0357) lasting (0.0648) style. (-0.0014)
~~~~~~

**Node-1** (global 163):

~~~~~~text
product (0.0003) from (0.0035) amazon (0.0019) platform (-0.0003) with (0.0024) title (0.0002) and (-0.0028) content (0.0076) : (0.0023) title (0.0044) : (0.0003) muay (-0.0006) thai (0.0006) mma (0.0008) ankle (-0.0014) support (-0.0005) wraps (0.0009) ( (-0.0001) pair (0.0021) ). (-0.0010) content (0.0060) : (-0.0031) meister (0.0014) mma (0.0012) ' (-0.0082) s (-0.0015) elastic (-0.0004) compression (-0.0016) ankle (-0.0023) supports (-0.0003) are (0.0014) ideal (-0.0037) for (0.0046) use (-0.0018) in (-0.0005) muay (0.0009) thai, (0.0004) mma, (0.0006) wrestling, (0.0025) boxing (-0.0013) and (-0.0018) other (-0.0019) sports (0.0002) demanding (-0.0001) ankle (0.0018) support. (0.0028) slip (-0.0001) them (0.0023) on (-0.0003) before (-0.0010) your (0.0046) workout (-0.0001) session (0.0030) to (0.0003) give (0.0050) you (0.0037) ankles (0.0048) support (-0.0000) and (0.0025) protection. (0.0011) fit (0.0092) men (-0.0094) ' (-0.0031) s (-0.0003) feet (-0.0077) sizes (0.0088) 7- (0.0018) 14. (-0.0040)
~~~~~~

**Node-1.1** (global 1957):

~~~~~~text
product (-0.0001) from (0.0004) amazon (0.0006) platform (-0.0002) with (0.0001) title (0.0004) and (0.0004) content (-0.0002) : (0.0006) title (0.0003) : (0.0004) " (-0.0002) muay (0.0001) thai (-0.0001) men (-0.0001) ' (0.0000) s (-0.0003) supporter (0.0003) with (0.0004) steel (0.0001) cup (0.0001) ". (0.0003) content (0.0004) : (0.0001) improved (0.0002) design (0.0003) : (-0.0001) muay (0.0003) thai (0.0002) geltech (0.0005) men (0.0002) ' (0.0001) s (0.0001) supporter (0.0002) with (0.0002) steel (0.0004) cup. (0.0002) molded (0.0006) cup, (0.0002) steel (0.0002) construction. (0.0005) genuine (0.0003) leather (0.0002) covering, (0.0002) neoprene (0.0001) gel (0.0001) material (0.0002) padded (0.0001) along (0.0002) edge (-0.0000) for (0.0002) added (0.0002) comfortability, (0.0002) thin (0.0003) soft (0.0002) foam (0.0002) lining (0.0002) inside (-0.0001) the (-0.0004) cup (0.0002) to (0.0002) avoid (-0.0000) direct (0.0000) contact (0.0000) to (0.0002) metal (0.0001) part (0.0001) of (-0.0001) the (-0.0003) cup, (0.0001) with (0.0001) new (0.0005) style (0.0002) supporter. (-0.0001) small (0.0002) / (0.0004) medium (0.0001) size (0.0002) fits (-0.0000) 120- (0.0001) 180lbs. (-0.0000) large (0.0002) / (0.0007) x- (0.0002) large (0.0002) size (0.0002) fits (-0.0001) 180lbs (0.0001) and (0.0005) overplease (0.0001) send (0.0003) us (0.0000) a (-0.0005) message (0.0001) that (0.0001) what (0.0001) size (0.0002) you (0.0005) need (-0.0000) after (0.0001) your (0.0003) purchase (0.0002) so (0.0001) we (-0.0000) will (0.0001) be (-0.0001) sure (0.0000) to (0.0005) ship (-0.0001) you (0.0003) your (0.0003) required (-0.0004) size. (-0.0005)
~~~~~~

**Node-1.2** (global 3):

~~~~~~text
product (-0.0002) from (0.0002) amazon (0.0003) platform (-0.0002) with (0.0001) title (0.0005) and (0.0001) content (0.0000) : (0.0009) title (0.0002) : (0.0004) muay (0.0000) thai (-0.0005) shorts- (0.0004) black. (0.0006) content (0.0001) : (0.0010) for (-0.0002) size (0.0004) chart, (0.0004) please (0.0000) see (0.0003) attached (0.0001) photos. (0.0009) improved (0.0006) design (0.0003) with (0.0003) 3 (0.0004) inches (0.0007) long (0.0003) split (0.0002) side (0.0001) seams (0.0005) for (0.0003) unrestricted (0.0007) range (0.0009) of (0.0003) motion. (0.0010) lightweight (0.0004) satin. (0.0008) made (0.0003) of (0.0006) soft (0.0008) and (0.0002) lightweight (0.0004) satin. (0.0009) for (0.0001) traditional (-0.0000) muay (0.0003) thai (-0.0004) kickboxing. (0.0004) 4 (0.0011) " (-0.0000) waistband. (-0.0004) " (0.0000) muay (0.0000) thai (0.0003) " (0.0001) in (0.0003) thai (-0.0003) lettering (0.0007) across (0.0010) front. (0.0011) extra (-0.0001) wide (0.0007) leg (0.0006) allows (0.0008) room (0.0000) for (0.0005) kicking. (0.0009) hidden (0.0011) drawstring (0.0006) inside (0.0008) waistband. (0.0013)
~~~~~~

**Node-1.3** (global 1956):

~~~~~~text
product (-0.0006) from (-0.0002) amazon (0.0005) platform (0.0000) with (-0.0002) title (0.0001) and (-0.0001) content (-0.0001) : (0.0003) title (0.0001) : (0.0003) compression (0.0000) support (0.0002) ankle (0.0000) brace (0.0002) size (0.0001) : (-0.0000) small, (0.0002) color (-0.0001) : (0.0000) black. (0.0001) content (0.0002) : (-0.0001) 3002- (-0.0000) b (0.0003) size (0.0001) : (-0.0000) small, (0.0001) color (-0.0001) : (0.0002) black (0.0000) features (-0.0003) :- (0.0001) ankle (-0.0013) brace.- (0.0001) lightweight.- (0.0002) breathable (0.0001) material (0.0001) with (-0.0000) four- (0.0001) way (0.0002) stretch.- (0.0001) warm, (0.0000) soothing (0.0010) and (-0.0001) uniform (0.0001) compression.- (0.0002) unique (0.0004) knitted (0.0001) pattern (0.0001) for (-0.0000) greater (0.0004) vertical (0.0001) stretch.- (0.0003) latex- (0.0002) free.- (0.0003) measure (0.0001) just (0.0002) above (0.0001) the (-0.0003) ankle (-0.0004) bone.- (0.0004) made (-0.0002) in (0.0001) the (-0.0003) usa.- (0.0004) small (0.0005) adjustable (0.0007) size (0.0002) : (0.0003) 7. (0.0002) 5 (-0.0000) "- (0.0001) 8. (0.0002) 5 (-0.0001) ".- (0.0004) medium (0.0002) adjustable (0.0012) size (-0.0000) : (0.0003) 8. (0.0003) 5 (0.0000) "- (0.0001) 9. (0.0002) 5 (-0.0001) ".- (0.0005) large (0.0005) adjustable (0.0009) size (0.0001) : (0.0004) 9. (0.0001) 5 (0.0000) "- (-0.0000) 10. (0.0001) 5 (-0.0001) ".- (0.0001) x- (0.0001) large (0.0002) adjustable (0.0002) size (-0.0002) : (-0.0000) 10. (0.0000) 5 (0.0001) "- (-0.0002) 11. (0.0001) 5 (0.0001) ". (0.0002) construction (0.0009) :- (0.0002) seamless (0.0002) construction (0.0004) provides (0.0002) maximum (0.0003) comfort. (0.0001) dimensions (0.0001) :- (0.0001) 8 (0.0002) " (0.0000) h (0.0002) x (0.0003) 6 (0.0001) " (0.0001) w (0.0002) x (0.0002) 1 (-0.0002) " (0.0001) d (-0.0001) : (0.0001) 0. (-0.0001) 2 (0.0001) lb. (0.0002)
~~~~~~

**Node-1.4** (global 1952):

~~~~~~text
product (-0.0002) from (-0.0004) amazon (-0.0007) platform (-0.0001) with (-0.0003) title (0.0000) and (-0.0002) content (0.0002) : (-0.0004) title (0.0002) : (-0.0004) piranha (0.0001) gear (-0.0003) uniform (0.0000) pants- (0.0000) drawstring (0.0000) waist. (0.0003) content (-0.0001) : (-0.0001) the (0.0002) sizing (-0.0000) on (-0.0001) these (-0.0003) pants (0.0001) may (0.0000) not (0.0000) be (0.0001) what (0.0001) you (0.0001) ' (0.0001) re (0.0001) expecting. (-0.0002) please (0.0003) be (0.0002) sure (-0.0001) to (0.0001) check (-0.0001) our (-0.0002) size (-0.0001) charts (-0.0002) to (-0.0002) make (-0.0000) sure (0.0001) you (0.0002) ' (0.0001) re (-0.0000) going (0.0001) to (0.0001) get (0.0000) a (0.0001) good (0.0000) fit (0.0002) as (0.0000) we (0.0001) want (0.0002) to (0.0001) save (0.0002) you (0.0001) the (0.0001) trouble (0.0002) of (0.0001) doing (0.0003) an (0.0002) exchange. (-0.0001) ( (0.0001) though (0.0000) we (0.0003) do (0.0001) have (0.0001) the (0.0002) best (0.0001) exchange (0.0001) policy (-0.0001) in (0.0001) the (0.0004) industry! (0.0001) ) (-0.0000) these (0.0001) bleached (0.0002) white (0.0000) cotton (0.0002) pants (0.0000) were (-0.0003) made (0.0003) for (0.0001) jiu- (0.0001) jitsu, (-0.0002) judo (0.0013) and (0.0001) aikido. (0.0000) they (-0.0004) have (-0.0002) reinforced (0.0002) seams (0.0003) and (0.0000) reinforced (0.0000) knees (0.0001) with (-0.0001) cross (0.0001) stitching (0.0002) ( (-0.0001) or (0.0002) " (0.0000) quilting (0.0003) " (0.0001) ) (0.0000) for (0.0001) durability. (0.0001) made (-0.0000) of (-0.0001) 100 (-0.0001) % (0.0002) cotton (-0.0003) with (0.0001) atraditional (-0.0001) drawstring, (-0.0002) these (0.0004) pants (0.0002) are (0.0001) the (0.0000) same (0.0001) ones (0.0001) included (-0.0002) with (0.0002) our (0.0001) single (0.0001) weave (0.0003) piranha (0.0006) gear (-0.0005) uniforms. (0.0002) we (-0.0001) do (0.0002) carry (0.0003) " (-0.0000) elastic (0.0001) drawstring (-0.0000) " (0.0002) waist (0.0001) pants (0.0002) too- (0.0000) as (0.0002) a (0.0001) separate (0.0002) item- (0.0001) though (-0.0001) not (0.0002) always (0.0000) in (0.0000) every (-0.0000) color. (0.0003) if (0.0001) anything, (0.0002) these (-0.0001) pants (0.0002) run (-0.0000) a (0.0002) little (0.0000) short. (0.0001) so (0.0000) if (0.0002) you (0.0001) ' (-0.0001) re (-0.0001) between (0.0002) sizes, (0.0000) get (0.0001) the (0.0001) longer (0.0001) / (0.0001) bigger (-0.0000) size. (-0.0001) please (0.0001) be (0.0002) sure (0.0000) to (0.0001) check (0.0001) our (0.0001) size (-0.0001) charts (-0.0000) before (-0.0000) you (0.0003) order. (-0.0000) also (-0.0002) keep (0.0001) in (-0.0000) mind (0.0002) that (0.0001) a (0.0001) size (0.0001) " (-0.0000) a2 (-0.0001) " (-0.0001) isnot (0.0001) the (0.0001) sameas (0.0003) a (0.0004) size (0.0002) " (-0.0001) 2 (0.0001) ". (-0.0004) be (0.0003) sure (0.0003) you (0.0003) checked (0.0002) the (0.0001) size (0.0001) chart (0.0004) to (0.0001) get (0.0004) the (0.0001) size (0.0001) you (-0.0003) wanted. (-0.0003)
~~~~~~

**Node-1.5** (global 1987):

~~~~~~text
product (0.0005) from (-0.0001) amazon (-0.0002) platform (-0.0000) with (-0.0003) title (0.0006) and (0.0001) content (0.0002) : (0.0001) title (0.0002) : (-0.0001) revgear (-0.0002) spartan (-0.0007) mma (0.0005) fight (-0.0010) short. (0.0008) content (0.0009) : (0.0006) made (0.0001) from (-0.0000) high (0.0000) tech (0.0001) stretch (-0.0000) poly (0.0001) material (-0.0000) featuring (0.0006) a (-0.0002) velcro (0.0000) closure (-0.0002) with (0.0005) reinforced (-0.0001) seams. (0.0006) great (0.0002) for (-0.0000) the (-0.0002) cage (-0.0001) or (0.0002) the (-0.0000) pool. (0.0003) the (0.0002) last (0.0007) pair (-0.0002) of (0.0007) shorts (0.0006) you (-0.0024) will (-0.0004) need. (0.0001) sizes (0.0003) : (0.0009) xs- (0.0005) 28, (0.0005) s- (0.0003) 30, (0.0004) m- (0.0004) 32, (0.0003) l- (0.0005) 34, (0.0003) xl- (0.0004) 36, (0.0005) xxl- (0.0004) 38, (0.0005) 3xl- (0.0005) 40, (0.0006) 4xl- (0.0005) 42. (0.0011)
~~~~~~

**Node-1.6** (global 1993):

~~~~~~text
product (0.0003) from (0.0004) amazon (-0.0004) platform (-0.0000) with (0.0000) title (0.0002) and (-0.0000) content (-0.0000) : (-0.0002) title (-0.0000) : (-0.0000) meister (-0.0001) mma (-0.0001) compression (-0.0001) rush (0.0001) fight (0.0002) shorts (0.0000) w (-0.0001) / (0.0001) cup (0.0001) pocket. (0.0003) content (-0.0001) : (-0.0000) meister (-0.0001) mma (0.0004) ' (-0.0002) s (0.0002) new (-0.0000) compression (-0.0000) rush (-0.0000) shorts (-0.0003) are (0.0001) the (-0.0001) pinnacle (0.0003) in (0.0003) compression (-0.0002) fight (-0.0001) attire. (0.0002) these (0.0003) shorts (-0.0002) are (0.0002) designed (0.0003) to (0.0001) move (0.0001) with (0.0001) your (0.0003) body, (0.0000) no (0.0002) matter (0.0000) if (0.0001) you (0.0001) are (0.0001) boxing, (0.0002) grappling, (0.0001) running (0.0001) or (0.0001) going (0.0001) for (0.0000) a (0.0001) flying (0.0000) triangle! (0.0001) the (0.0003) anti- (0.0001) odor (0.0000) fabric (-0.0003) wicks (-0.0005) sweat (-0.0001) and (-0.0002) controls (0.0002) body (-0.0001) temperature. (-0.0004) the (0.0002) thick (0.0003) elastic (0.0002) waistband (-0.0002) creates (0.0000) a (0.0000) comfortable (0.0001) feel (0.0001) that (0.0001) keeps (0.0000) the (0.0002) shorts (-0.0000) well- (0.0001) positioned. (0.0001) meister (-0.0001) ' (0.0001) s (0.0000) rush (0.0001) compression (0.0001) shorts (0.0001) also (-0.0000) feature (0.0002) a (-0.0000) cup (0.0001) pocket (0.0001) that (0.0001) will (0.0002) hold (0.0002) almost (-0.0001) any (0.0001) groin (-0.0002) protector (0.0002) in (-0.0001) ideal (-0.0001) position (0.0001) ( (-0.0001) cup (0.0001) not (0.0000) included (0.0003) ). (0.0004) an (0.0001) incredible (0.0005) value, (-0.0000) get (0.0003) yours (0.0000) today! (0.0005)
~~~~~~

**Node-1.7** (global 2002):

~~~~~~text
product (-0.0011) from (-0.0003) amazon (0.0004) platform (-0.0005) with (-0.0004) title (0.0015) and (-0.0019) content (0.0010) : (-0.0007) title (0.0014) : (-0.0003) lumpinee (0.0001) muay (-0.0001) thai (0.0004) kick (0.0004) boxing (0.0009) shorts (-0.0003) : (0.0005) lum- (0.0005) 002. (0.0008) content (-0.0002) : (0.0002) muay (-0.0003) thai (0.0002) kickboxing (0.0002) shorts (-0.0001) from (0.0008) lumpinee. (0.0007) product (0.0003) made (-0.0000) in (0.0000) thailand. (0.0002) they (0.0007) are (0.0021) perfect (-0.0001) for (-0.0008) training. (0.0019) brand (-0.0000) new. (0.0011) 100 (-0.0003) % (0.0000) soft (0.0007) satin. (0.0023) size (-0.0014) s (0.0001) 26 (-0.0011) ", (0.0013) size (0.0002) m (0.0001) 28 (-0.0003) ", (0.0001) size (0.0003) l (0.0009) 30 (-0.0001) ", (-0.0001) size (0.0004) xl (0.0013) 32 (0.0004) ", (-0.0003) size (0.0003) xxl (-0.0001) 34 (0.0052) " (0.0005)
~~~~~~

**Node-1.8** (global 1942):

~~~~~~text
product (0.0006) from (0.0016) amazon (-0.0005) platform (0.0005) with (0.0011) title (0.0010) and (0.0007) content (-0.0015) : (0.0018) title (0.0004) : (0.0015) contender (0.0009) fight (0.0004) sports (0.0008) knee (0.0003) pads. (0.0016) content (0.0001) : (0.0015) the (-0.0001) contender (0.0007) fight (0.0005) sports (0.0004) knee (0.0004) pads (0.0012) have (0.0009) almost (0.0007) 2 (0.0008) inches (0.0008) of (0.0006) shock (0.0010) absorbing (0.0013) foam (0.0009) over (0.0007) the (-0.0001) knee (0.0008) which (0.0013) keeps (0.0010) you (0.0003) and (0.0011) your (0.0010) training (0.0011) partners (0.0009) safe. (-0.0010) neoprene (0.0011) sleeve (0.0012) keeps (0.0004) the (0.0003) pad (0.0018) sucure (0.0009) yet (0.0012) does (0.0015) not (0.0018) hinder (0.0009) movement. (-0.0018)
~~~~~~

**Node-1.9** (global 1951):

~~~~~~text
product (0.0003) from (-0.0002) amazon (0.0003) platform (-0.0003) with (0.0001) title (0.0004) and (0.0001) content (-0.0004) : (0.0010) title (0.0006) : (0.0006) mrx (0.0002) mma (-0.0006) fight (-0.0008) shorts (0.0003) stretch (0.0007) penals (0.0004) black (0.0003) / (0.0006) grey. (0.0001) content (0.0008) : (0.0007) mma (-0.0011) shorts (0.0004) / (0.0005) grappling (0.0004) shorts (0.0001) made (0.0005) of (0.0000) 100 (0.0001) % (-0.0001) taslan (0.0003) fabric (0.0003) with (0.0004) stretch (0.0011) panels (0.0006) constructed (0.0013) shorts (-0.0003) feature (0.0001) a (0.0002) large (0.0004) dragon (0.0003) snake (0.0004) printed (0.0004) on (0.0003) the (0.0002) left (0.0002) leg (0.0002) and (0.0006) mrx (0.0005) logo (0.0007) on (0.0001) the (-0.0000) right (0.0004) leg. (0.0002) the (0.0000) black- (0.0005) trimmed (0.0007) waistband (0.0007) with (0.0008) woven (0.0010) mrx (0.0001) logo (0.0010) on (0.0003) the (-0.0003) front, (0.0001) has (0.0012) hook (0.0008) / (0.0001) loop (0.0007) closure (0.0004) plus (0.0001) an (0.0006) internal (0.0006) drawstring (0.0004) to (0.0006) reduce (0.0010) shifting. (-0.0002)
~~~~~~

**Node-2** (global 164):

~~~~~~text
product (-0.0081) from (-0.0039) amazon (-0.0078) platform (0.0016) with (-0.0040) title (0.0150) and (-0.0010) content (-0.0028) : (0.0132) title (0.0111) : (0.0010) hand (-0.0002) wrap (0.0018) wash (-0.0004) bag (0.0015) w (-0.0027) / (0.0088) bag (-0.0014) clip- (-0.0012) large. (0.0036) content (0.0051) : (0.0033) don (0.0010) ' (0.0004) t (-0.0003) keep (-0.0004) reusing (0.0005) your (0.0003) sweaty (-0.0012) hand (0.0018) wraps! (0.0009) after (0.0013) your (0.0012) workout (-0.0050) just (0.0024) stuff (0.0014) your (0.0020) wraps (0.0002) into (0.0037) your (-0.0020) meister (-0.0042) mma (0.0081) hand (-0.0029) wrap (-0.0011) wash (0.0036) bag (0.0020) and (0.0055) throw (0.0017) it (0.0034) in (0.0050) the (-0.0066) washer (0.0032) and (0.0058) dryer. (0.0056) keeps (0.0027) your (0.0023) wraps (0.0017) from (0.0046) getting (0.0012) tangled (0.0051) up (0.0003) with (0.0055) all (0.0036) your (-0.0027) laundry. (0.0009) this (0.0016) bag (0.0060) includes (-0.0036) a (-0.0038) swivel (0.0025) bag (0.0019) clip (-0.0029) as (0.0031) well. (-0.0020) constructed (0.0058) of (0.0053) strong (0.0033) double (0.0070) stitched (0.0004) mesh (0.0020) this (0.0027) wash (0.0068) bag (0.0106) will (0.0048) keep (0.0064) you (0.0069) rolling (0.0018) with (0.0028) clean (0.0053) wraps (-0.0021) without (0.0085) the (-0.0037) hassle. (0.0018)
~~~~~~

**Node-2.1** (global 1930):

~~~~~~text
product (-0.0001) from (0.0002) amazon (-0.0002) platform (-0.0000) with (0.0001) title (0.0003) and (-0.0001) content (-0.0001) : (0.0005) title (0.0001) : (0.0002) " (-0.0003) title (-0.0000) boxing (-0.0001) title (0.0001) mma (0.0004) 8 (-0.0002) limbs (0.0003) thai (0.0001) men (0.0000) ' (0.0001) s (-0.0000) tee, (0.0003) m, (0.0002) black (0.0000) ". (-0.0001) content (-0.0000) : (-0.0002) 5. (-0.0003) 6 (-0.0000) oz., (0.0000) 50 (-0.0000) % (0.0001) cotton (0.0003) / (0.0002) 50 (0.0000) % (-0.0000) dryblend (0.0001) polyester (0.0001) jersey (0.0000) knit (0.0003) t- (0.0000) shirt. (0.0002) dryblend (0.0000) moisture (0.0004) wicking (-0.0000) fabric. (0.0003) seamless (0.0001) double- (0.0001) needle (0.0002) stitched (0.0001) rib (0.0002) knit (0.0001) 7 (0.0001) / (0.0003) 8 (0.0003) " (0.0001) collar. (0.0004) taped (0.0001) neck (0.0003) and (0.0000) shoulders. (0.0005) tubular (0.0002) knit (-0.0001) construction. (0.0004) double- (0.0001) needle (0.0004) stitched (0.0002) sleeve (0.0007) and (-0.0001) bottom (0.0007) hems. (0.0004)
~~~~~~

**Node-2.2** (global 1955):

~~~~~~text
product (0.0028) from (0.0004) amazon (0.0004) platform (0.0003) with (0.0006) title (0.0014) and (0.0013) content (0.0008) : (0.0007) title (0.0014) : (0.0005) revgear (0.0010) thai (-0.0003) style (0.0015) boxing (0.0014) gloves. (-0.0016) content (0.0013) : (0.0020) perfect (0.0011) your (0.0019) standup (0.0015) skills (0.0014) in (0.0006) the (-0.0002) gym (0.0006) with (0.0019) the (-0.0001) revgear (0.0007) thai (0.0005) style (0.0013) boxing (0.0008) gloves. (-0.0023) wide (0.0007) fingertip (0.0012) profile (0.0015) open (0.0012) palm (0.0008) for (0.0008) muay (0.0003) thai (-0.0012) clinch (0.0003) unique (0.0003) padding (0.0010) configuration (0.0000) wrap (-0.0004) around (0.0005) ultra- (0.0013) lock (0.0009) hook (0.0001) and (0.0014) loop (0.0003) wristband (0.0011) for (0.0008) greater (0.0012) comfort (0.0000) & (0.0013) support (0.0008) extra- (0.0020) thick (0.0007) pre- (0.0021) curved (0.0023) high (0.0020) impact (0.0013) foam (0.0037) over (0.0030) knuckles (-0.0014)
~~~~~~

**Node-2.3** (global 1970):

~~~~~~text
product (0.0015) from (0.0001) amazon (-0.0005) platform (-0.0012) with (0.0002) title (0.0003) and (0.0005) content (-0.0008) : (0.0003) title (0.0000) : (0.0006) brazilian (0.0006) jiu (-0.0001) jitsu (0.0003) uniform (-0.0006) or (0.0001) gi (0.0010) premium (0.0008) black (0.0000) or (-0.0002) blue. (0.0007) content (-0.0004) : (0.0002) light (0.0003) weight (-0.0003) brazilian (-0.0005) jiu (0.0000) jitsu (0.0003) uniform, (0.0004) great (-0.0003) quality (-0.0001) for (0.0005) a (0.0004) low (0.0005) price (0.0001) you (0.0009) can (0.0001) use (0.0004) it (0.0002) for (0.0001) brazilian (-0.0003) jiujitsu, (0.0001) mixed (0.0001) martial (-0.0000) arts, (0.0002) mma, (-0.0001) training (-0.0003) and (0.0006) competitions (-0.0002) for (0.0003) all (0.0004) mixed (0.0006) martial (0.0003) arts. (-0.0002) seamless (0.0004) on (0.0001) the (0.0002) back (0.0005) of (0.0004) the (0.0002) jacket (0.0009) this (0.0003) brazilian (-0.0001) jiu (-0.0001) jitsu (0.0006) uniform (-0.0005) also (0.0011) has (-0.0002) a (-0.0006) rubberized (0.0002) collar (0.0000) for (0.0002) better (0.0002) grip (-0.0001) and (0.0007) wearing, (0.0002) reinforced (0.0003) in (0.0004) all (-0.0000) seams, (0.0006) strong (-0.0003) pants. (0.0000)
~~~~~~

**Node-2.4** (global 169):

~~~~~~text
product (-0.0000) from (0.0004) amazon (0.0003) platform (-0.0004) with (0.0002) title (0.0008) and (0.0004) content (0.0002) : (0.0003) title (0.0004) : (0.0001) muay (0.0002) thai (0.0000) shorts. (0.0004) content (-0.0000) : (0.0009) improved (0.0004) design (0.0007) with (0.0003) 3 (0.0004) inches (0.0009) long (0.0006) split (0.0005) side (0.0001) seams (0.0005) for (0.0004) unrestricted (0.0008) range (0.0009) of (0.0004) motion. (0.0010) lightweight (0.0006) satin. (0.0006) made (0.0004) of (0.0005) soft (0.0006) and (0.0006) lightweight (0.0007) satin. (0.0013) for (0.0002) traditional (0.0001) muay (0.0004) thai (-0.0000) kickboxing. (0.0005) 4 (0.0007) " (-0.0000) waistband. (-0.0002) " (0.0004) muay (0.0003) thai (0.0007) " (-0.0000) in (0.0006) thai (-0.0000) lettering (0.0007) on (0.0005) front (0.0006) left (0.0004) leg. (0.0009) extra (0.0003) wide (0.0008) leg (0.0006) allows (0.0009) room (0.0002) for (0.0007) kicking. (0.0009) hidden (0.0014) drawstring (0.0008) inside (0.0008) waistband. (0.0013)
~~~~~~

**Node-2.5** (global 1986):

~~~~~~text
product (-0.0002) from (-0.0008) amazon (-0.0007) platform (0.0002) with (0.0003) title (-0.0001) and (-0.0004) content (-0.0007) : (-0.0001) title (0.0001) : (-0.0006) " (-0.0009) title (-0.0003) boxing (0.0008) title (-0.0005) mma (0.0018) submit (0.0007) men (-0.0010) ' (0.0005) s (-0.0011) tee, (-0.0009) l, (0.0000) yellow (-0.0010) ". (-0.0000) content (-0.0010) : (-0.0005) 5. (0.0000) 3 (0.0002) oz., (-0.0003) 100 (-0.0002) % (0.0000) preshrunk (-0.0000) cotton (0.0010) jersey (0.0005) knit (0.0003) t- (-0.0001) shirt. (0.0010) seamless (0.0002) double- (-0.0000) needle (0.0002) stitched (0.0000) rib (0.0001) knit (0.0004) 7 (0.0001) / (-0.0002) 8 (0.0005) " (-0.0003) collar. (-0.0000) taped (0.0004) neck (0.0003) and (-0.0005) shoulders. (0.0005) tubular (0.0003) knit (0.0006) construction. (0.0002) double- (0.0001) needle (-0.0003) stitched (0.0000) sleeve (0.0003) and (-0.0008) bottom (0.0007) hems. (0.0004)
~~~~~~

**Node-2.6** (global 1960):

~~~~~~text
product (-0.0001) from (-0.0006) amazon (0.0004) platform (-0.0003) with (-0.0002) title (0.0002) and (-0.0003) content (0.0006) : (-0.0000) title (0.0004) : (-0.0001) boon (0.0006) sport (0.0000) leather (0.0001) training (-0.0001) gloves. (0.0003) content (0.0005) : (0.0003) authentic (0.0003) genuine (-0.0001) top (0.0000) grain (0.0003) leather (0.0002) professional (-0.0000) hook- (0.0000) and- (0.0002) loop (0.0004) training (-0.0001) gloves. (0.0005) crafted (0.0001) of (-0.0002) select (0.0003) supple, (0.0000) yet (0.0002) durable (0.0002) leather (-0.0002) with (0.0004) approximately (0.0005) 2 (0.0005) " (-0.0007) of (0.0007) integrated (0.0004) layered (0.0004) foams (0.0002) for (0.0005) superb (0.0004) shock (0.0002) absorbency (0.0003) and (0.0005) maximum (0.0002) coverage (0.0003) for (0.0003) intense (-0.0001) athletes. (0.0004) extra (0.0002) wide (0.0000) hook- (0.0002) and- (0.0005) loop (0.0004) wraparound (0.0002) wrist (0.0001) closure (0.0003) assures (0.0001) snug, (0.0003) firm (0.0005) fit. (0.0004) moisture (0.0002) wicking (0.0004) hand (-0.0001) liner (0.0004) keeps (0.0002) hands (0.0000) drier (-0.0001) and (0.0008) cooler (0.0004) during (0.0006) training. (0.0008) handmade (0.0003) in (0.0004) thailand (-0.0019) and (-0.0002) tested (-0.0000) in (0.0009) professional (0.0005) bangkok (0.0005) gyms (0.0003) for (0.0009) performance. (0.0006)
~~~~~~

**Node-2.7** (global 1965):

~~~~~~text
product (-0.0005) from (0.0010) amazon (-0.0002) platform (-0.0004) with (0.0004) title (0.0008) and (0.0001) content (-0.0007) : (0.0006) title (0.0000) : (-0.0001) title (-0.0000) boxing (0.0000) 3 (0.0003) / (-0.0000) 4 (0.0002) length (0.0004) stock (0.0012) satin (0.0006) robe. (0.0012) content (0.0002) : (0.0005) full (0.0001) 100 (0.0001) % (0.0003) satin (0.0003) styling (-0.0001) with (0.0005) professionally (0.0005) tailored (0.0003) seams (0.0003) and (0.0003) craftsmanship. (0.0009) classic (0.0000) above (0.0001) knee (0.0005) 3 (-0.0000) / (0.0003) 4 (0.0000) length (0.0004) complete (0.0004) with (0.0003) pockets, (0.0003) belt (0.0000) and (0.0003) hood. (0.0004) sleeves (0.0005) are (0.0007) cut (0.0001) 3 (-0.0001) / (0.0003) 4 (0.0001) length (0.0002) pro (0.0004) style. (0.0002) in (0.0005) stock (0.0006) for (0.0008) immediate (0.0008) delivery. (0.0010) also (0.0004) available (0.0000) in (0.0006) full (-0.0003) length. (0.0006)
~~~~~~

**Node-2.8** (global 2016):

~~~~~~text
product (0.0005) from (0.0006) amazon (0.0007) platform (-0.0001) with (0.0009) title (0.0006) and (0.0009) content (0.0017) : (0.0004) title (0.0012) : (0.0013) rival (-0.0002) d3o (0.0005) intelli- (0.0010) shock (0.0008) pro (0.0004) training (0.0003) headgear. (-0.0003) content (0.0016) : (0.0016) the (0.0007) rhg10 (0.0010) is (0.0006) the (0.0001) result (0.0009) of (0.0003) 2 (0.0002) years (0.0004) of (0.0004) evolution (0.0009) and (0.0008) heightened (0.0007) improvements, (0.0011) we (0.0002) have (0.0011) worked (0.0008) very (0.0012) closely (0.0005) with (0.0008) a (0.0004) lot (0.0008) of (0.0004) athletes (0.0004) in (0.0003) the (0.0001) boxing (-0.0003) world (0.0014) to (0.0005) bring (0.0003) you (-0.0005) a (0.0001) head (0.0007) gear (0.0016) like (0.0005) no (0.0007) other (0.0007) on (0.0003) the (0.0001) market (0.0004) today. (0.0001)
~~~~~~

**Node-2.9** (global 1964):

~~~~~~text
product (-0.0001) from (-0.0002) amazon (0.0015) platform (0.0003) with (-0.0002) title (0.0004) and (0.0003) content (0.0008) : (0.0005) title (0.0002) : (0.0002) meister (0.0001) mounted (0.0005) metal (0.0002) hand (0.0001) wrap (0.0001) roller. (0.0005) content (0.0008) : (0.0001) tired (0.0005) of (-0.0001) rolling (-0.0001) your (-0.0008) wraps (0.0004) by (-0.0003) hand? (-0.0003) the (0.0006) meister (-0.0000) mma (0.0002) mounted (0.0004) hand (0.0004) wrap (0.0003) roller (0.0001) is (0.0002) the (-0.0001) ideal (0.0005) fixture (-0.0001) for (0.0004) your (0.0003) gym (0.0001) or (0.0004) home. (0.0006) easily (0.0002) mounted, (0.0004) including (0.0002) the (0.0002) hardware (0.0003) you (-0.0001) need (-0.0002) in (0.0004) the (0.0002) package, (0.0002) you (-0.0002) ' (-0.0002) ll (0.0004) be (-0.0000) rolling (-0.0001) your (0.0000) wraps (0.0008) in (0.0002) no (0.0000) time. (-0.0001) simply (0.0001) slide (0.0003) the (0.0003) end (0.0001) of (0.0003) the (0.0001) wrap (0.0005) through (0.0001) the (-0.0001) clasp (0.0004) and (0.0003) crank (0.0002) the (-0.0002) handle (0.0002) to (-0.0001) start (-0.0000) rolling. (-0.0003) the (0.0006) meister (0.0000) mma (0.0003) mounted (0.0008) wrap (0.0010) roller (0.0001) is (0.0001) made (0.0002) solid (0.0006) metal (0.0001) and (0.0002) is (0.0004) built (0.0004) to (-0.0001) last. (0.0004)
~~~~~~

**Node-3** (global 165):

~~~~~~text
product (-0.0002) from (-0.0018) amazon (0.0026) platform (-0.0001) with (0.0050) title (0.0030) and (0.0046) content (0.0065) : (0.0126) title (0.0083) : (0.0080) revgear (0.0029) muay (0.0069) thai (0.0041) shorts. (0.0007) content (0.0061) : (0.0046) revgear (0.0009) professional (0.0078) satin (0.0039) muay (0.0106) thai (0.0004) shorts. (-0.0059) 4 (0.0028) " (-0.0072) muay (0.0071) thai (0.0032) elastic (0.0029) and (0.0049) drawstring (0.0053) waistband (-0.0025) with (0.0044) 7 (0.0029) rows (0.0056) of (0.0068) stitching. (0.0093) cut (0.0027) extra (-0.0031) wide (0.0043) and (0.0065) short (0.0055) for (0.0047) freedom (0.0056) of (0.0013) movement (0.0051) and (0.0068) ease (0.0080) in (0.0068) kicking. (0.0130) authentic (0.0033) thai (-0.0060) appliqu (0.0053) & (0.0034) # (-0.0021) xe9 (-0.0008) ; (0.0257) lettering (0.0016) across (0.0041) the (-0.0196) front (0.0047) ( (0.0067) means (0.0014) " (-0.0024) muay (0.0004) thai (0.0047) " (0.0004) in (0.0100) thai (-0.0061) ) (0.0095) and (0.0104) revgear (0.0029) woven (0.0102) waist (0.0029) patch. (0.0106) available (0.0047) colors (0.0037) : (0.0088) black, (0.0057) red, (0.0058) blue. (0.0172) available (-0.0049) sizes (0.0142) : (0.0233) s, (0.0082) m, (0.0048) l, (0.0094) xl, (0.0088) xxl. (0.0212)
~~~~~~

**Node-3.1** (global 1972):

~~~~~~text
product (0.0016) from (0.0001) amazon (-0.0011) platform (0.0004) with (-0.0004) title (0.0015) and (0.0008) content (-0.0004) : (0.0002) title (0.0004) : (-0.0003) revgear (-0.0002) spartan (-0.0017) mma (0.0013) fight (-0.0003) short. (0.0006) content (0.0018) : (0.0015) made (-0.0001) from (0.0001) high (-0.0004) tech (0.0001) stretch (-0.0003) poly (-0.0000) material (-0.0001) featuring (0.0018) a (-0.0005) velcro (-0.0000) closure (-0.0004) with (0.0011) reinforced (-0.0002) seams. (0.0011) great (0.0001) for (-0.0004) the (-0.0004) cage (-0.0001) or (-0.0001) the (0.0000) pool. (0.0006) the (0.0004) last (0.0013) pair (-0.0000) of (0.0012) shorts (-0.0001) you (-0.0046) will (-0.0007) need. (-0.0007) sizes (0.0013) : (0.0019) xs- (0.0010) 28, (0.0010) s- (0.0008) 30, (0.0008) m- (0.0007) 32, (0.0005) l- (0.0010) 34, (0.0006) xl- (0.0006) 36, (0.0007) xxl- (0.0005) 38, (0.0009) 3xl- (0.0008) 40, (0.0010) 4xl- (0.0008) 42. (0.0015)
~~~~~~

**Node-3.2** (global 1971):

~~~~~~text
product (0.0008) from (0.0005) amazon (0.0003) platform (-0.0011) with (0.0001) title (0.0005) and (0.0006) content (-0.0002) : (0.0006) title (0.0004) : (0.0008) brazilian (0.0003) jiu (-0.0000) jitsu (0.0002) uniform (-0.0000) or (0.0007) gi (0.0010) premium (0.0009) black (0.0002) or (0.0004) blue. (0.0010) content (0.0000) : (0.0004) light (0.0005) weight (0.0003) brazilian (-0.0003) jiu (-0.0000) jitsu (0.0002) uniform, (0.0005) great (-0.0001) quality (0.0003) for (0.0007) a (0.0006) low (0.0007) price (0.0006) you (0.0009) can (0.0003) use (0.0008) it (0.0003) for (0.0003) brazilian (-0.0004) jiujitsu, (0.0002) mixed (0.0003) martial (0.0002) arts, (0.0004) mma, (-0.0001) training (-0.0002) and (0.0010) competitions (0.0000) for (0.0005) all (0.0006) mixed (0.0006) martial (0.0004) arts. (0.0001) seamless (0.0010) on (0.0007) the (-0.0000) back (0.0007) of (0.0003) the (0.0003) jacket (0.0011) this (0.0006) brazilian (-0.0003) jiu (-0.0001) jitsu (0.0002) uniform (0.0002) also (0.0008) has (0.0003) a (-0.0003) rubberized (0.0007) collar (0.0003) for (0.0005) better (0.0001) grip (0.0002) and (0.0008) wearing, (0.0006) reinforced (0.0009) in (0.0006) all (0.0004) seams, (0.0011) strong (-0.0005) pants. (0.0001)
~~~~~~

**Node-3.3** (global 1969):

~~~~~~text
product (-0.0003) from (-0.0001) amazon (0.0001) platform (-0.0003) with (0.0003) title (-0.0006) and (0.0001) content (-0.0001) : (-0.0001) title (-0.0006) : (-0.0002) revgear (-0.0001) glove (0.0003) dog (-0.0002) deodorizer. (-0.0004) content (0.0006) : (0.0003) the (-0.0005) glove (0.0003) dog (-0.0006) dryer (0.0002) and (-0.0002) deodorizer (-0.0004) absorbs (-0.0002) all (-0.0002) around (0.0001) moisture (0.0007) while (-0.0001) deodorizing. (-0.0001) it (-0.0001) gives (-0.0004) longer (-0.0005) glove (0.0004) life, (-0.0004) leaves (-0.0003) fresh (-0.0002) cedar (0.0001) odor, (-0.0004) conforms (-0.0002) to (-0.0001) inner (0.0000) shape (-0.0002) of (-0.0004) your (0.0001) glove. (0.0007) breathable (-0.0000) cotton (0.0000) flannel (-0.0003) shells (-0.0002) filled (-0.0004) with (0.0000) refined, (0.0000) long (-0.0002) lasting (-0.0001) cedar (-0.0005) chips. (-0.0000)
~~~~~~

**Node-3.4** (global 171):

~~~~~~text
product (0.0005) from (0.0008) amazon (0.0016) platform (0.0010) with (0.0010) title (-0.0007) and (0.0000) content (0.0028) : (-0.0007) title (0.0008) : (-0.0001) namman (-0.0006) muay (0.0002) thai (-0.0009) boxing (-0.0003) liniment (-0.0009) 120ml. (0.0011) content (0.0009) : (-0.0004) this (0.0000) rare (-0.0006) muscle (-0.0001) liniment (-0.0005) not (-0.0000) only (0.0002) relieves (0.0004) aches (0.0009) and (0.0008) pains (0.0000) after (0.0009) long (0.0003) workouts, (0.0006) but (0.0001) helps (0.0006) speed (0.0003) up (0.0002) muscle (0.0002) recovery. (-0.0001)
~~~~~~

**Node-3.5** (global 166):

~~~~~~text
product (-0.0001) from (0.0004) amazon (-0.0007) platform (-0.0006) with (0.0003) title (0.0003) and (0.0003) content (-0.0001) : (-0.0009) title (0.0007) : (0.0001) " (0.0005) revgear (0.0000) women (0.0003) ' (-0.0001) s (0.0006) deluxe (-0.0004) muay (0.0005) thai (0.0003) short (0.0010) ". (0.0002) content (0.0009) : (-0.0000) revgear (-0.0001) women (-0.0001) ' (0.0003) s (-0.0001) deluxe (-0.0001) muay (0.0004) thai (0.0001) shorts. (0.0018) available (0.0002) in (0.0006) tahiti (0.0006) blue (-0.0006) and (0.0002) pink. (-0.0001) sizes (0.0023) : (0.0028) s, (-0.0000) m, (0.0004) l, (0.0001) xl, (0.0008) xxl. (0.0004)
~~~~~~

**Node-3.6** (global 2001):

~~~~~~text
product (-0.0003) from (-0.0002) amazon (0.0000) platform (-0.0002) with (0.0003) title (0.0006) and (-0.0002) content (0.0006) : (0.0008) title (0.0004) : (0.0001) muay (0.0001) thai (-0.0003) shorts- (0.0000) blue. (0.0005) content (0.0001) : (0.0008) for (-0.0001) size (-0.0003) chart, (0.0002) please (-0.0007) see (0.0005) attached (0.0001) photos.. (0.0003) made (0.0002) of (-0.0000) soft (0.0003) and (0.0003) lightweight (0.0009) satin. (0.0011) for (-0.0000) traditional (0.0003) muay (0.0001) thai (-0.0002) kickboxing. (0.0004) 4 (0.0003) " (0.0000) waistband. (0.0014) extra (0.0004) wide (0.0006) leg (0.0002) allows (0.0001) room (0.0005) for (0.0001) kicking. (0.0008) hidden (0.0010) drawstring (0.0005) inside (0.0008) waistband. (0.0016)
~~~~~~

**Node-3.7** (global 2003):

~~~~~~text
product (-0.0003) from (0.0009) amazon (0.0009) platform (0.0006) with (0.0010) title (0.0003) and (0.0006) content (0.0018) : (0.0000) title (0.0010) : (0.0009) revgear (-0.0001) deluxe (0.0009) muay (0.0003) thai (0.0006) shorts. (0.0009) content (0.0010) : (0.0003) revgear (0.0003) deluxe (0.0006) muay (0.0002) thai (0.0010) shorts. (0.0004) available (0.0000) in (0.0009) black, (0.0006) blue (0.0001) or (0.0011) gold. (0.0018) sizes (0.0009) : (0.0018) s, (0.0008) m, (0.0003) l, (0.0007) xl, (0.0008) xxl. (0.0020)
~~~~~~

**Node-3.8** (global 2009):

~~~~~~text
product (-0.0017) from (0.0005) amazon (0.0002) platform (-0.0005) with (-0.0000) title (0.0002) and (0.0002) content (0.0001) : (-0.0001) title (0.0003) : (0.0001) muay (-0.0000) thai (-0.0003) shorts- (0.0001) red. (0.0010) content (0.0001) : (0.0008) improved (-0.0005) design (-0.0005) with (-0.0002) 3 (0.0001) inches (0.0005) long (0.0001) split (0.0001) side (-0.0001) seams (-0.0000) for (0.0002) unrestricted (0.0002) range (0.0005) of (0.0003) motion. (0.0010) lightweight (0.0007) satin. (0.0009) made (0.0001) of (0.0002) soft (-0.0002) and (0.0000) lightweight (0.0001) satin. (0.0007) for (0.0001) traditional (0.0001) muay (0.0005) thai (-0.0003) kickboxing. (0.0005) 4 (0.0007) " (0.0002) waistband. (0.0001) " (-0.0000) muay (0.0002) thai (0.0002) " (0.0000) in (0.0008) thai (-0.0004) lettering (0.0007) across (0.0006) front. (0.0009) extra (0.0003) wide (0.0005) leg (0.0004) allows (0.0006) room (0.0000) for (0.0003) kicking. (0.0010) hidden (0.0014) drawstring (0.0005) inside (0.0009) waistband. (0.0009)
~~~~~~

**Node-3.9** (global 2011):

~~~~~~text
product (0.0001) from (0.0003) amazon (0.0009) platform (-0.0001) with (0.0002) title (0.0003) and (0.0000) content (0.0008) : (0.0005) title (0.0003) : (0.0006) traditional (0.0001) boxing (0.0002) trunks, (0.0002) blue (0.0004) or (0.0005) red (0.0003) color. (0.0005) kids (0.0004) and (0.0001) adult (0.0005) sizes. (0.0005) content (0.0008) : (0.0003) traditional (-0.0005) styling, (0.0005) soft (0.0002) and (0.0002) lightweight (0.0003) satin (0.0007) trunks. (0.0004) can (0.0004) be (0.0002) used (0.0007) for (0.0002) boxing, (0.0001) kickboxing, (0.0004) and (0.0002) muay (0.0000) thai. (0.0002) 4 (0.0009) " (-0.0004) waistband. (0.0008) machine (0.0006) washable. (0.0005) full (0.0004) cut (0.0004) to (0.0007) accommodate (0.0004) protective (0.0003) cup. (0.0008) hidden (0.0007) drawstring (0.0003) inside (0.0006) the (-0.0008) waistband. (0.0001) embrioded (0.0004) ring (-0.0001) to (0.0009) cage (0.0005) logo (0.0010) on (0.0007) left (0.0007) leg. (0.0004)
~~~~~~

**Node-4** (global 14711):

~~~~~~text
product (0.0133) from (0.0017) amazon (0.0232) platform (0.0012) with (0.0122) title (0.0033) and (0.0070) content (0.0050) : (0.0229) title (0.0129) : (0.0152) hayabusa (0.0072) 70l (-0.0008) mesh (-0.0191) gear (0.0141) bag, (0.0046) black. (0.0067) content (0.0143) : (0.0009) this (0.0196) heavy- (0.0113) duty (0.0034) black (0.0136) mesh (0.0190) bag (0.0031) constructed (0.0082) with (-0.0013) tough (0.0095) puncture (0.0061) and (0.0099) damage (0.0088) resistant (0.0065) mesh (0.0089) and (0.0141) heavy (0.0107) duty (0.0030) main (0.0078) zipper, (0.0079) extra (0.0050) strong (0.0060) seams (0.0128) and (0.0146) fabric (0.0087) to (0.0046) last (0.0050) a (0.0114) lifetime, (0.0104) and (0.0118) features (0.0084) a (0.0086) draw- (0.0089) string, (0.0041) snap- (0.0097) lock (0.0119) closure, (0.0112) and (0.0133) an (0.0109) attached (0.0094) id (0.0031) tag. (-0.0017) the (-0.0041) mesh (0.0077) gear (0.0222) bag (0.0166) is (0.0096) fully (0.0082) ventilated (0.0080) to (0.0067) maximize (0.0133) the (-0.0056) life (0.0070) of (0.0187) your (-0.0035) gear (0.0317) and (0.0100) aid (0.0062) drying (0.0114) with (0.0154) a (0.0005) water (0.0204) resistant (0.0151) inner (0.0176) pocket (0.0180) for (0.0153) separating (0.0123) valuables (0.0250) and (0.0181) other (0.0165) items (0.0309)
~~~~~~

**Node-4.1** (global 1963):

~~~~~~text
product (0.0021) from (0.0007) amazon (0.0005) platform (-0.0012) with (0.0004) title (0.0001) and (0.0006) content (-0.0007) : (0.0024) title (0.0007) : (0.0021) hayabusa (0.0010) official (-0.0003) mma (0.0008) shouri (0.0021) bamboo (0.0000) mizuchi (0.0010) t- (0.0005) shirts (0.0010) / (-0.0004) tee. (-0.0009) content (0.0010) : (0.0005) ultra (0.0025) comfortable (0.0010) natural (0.0018) bamboo (0.0013) fiber (0.0027) fabricexclusive (0.0025) japanese- (-0.0006) inspired (0.0003) designsmetallic (0.0004) foil, (0.0006) flocked (0.0006) and (0.0007) water (0.0022) based (-0.0008) ink (0.0020) printsofficial (0.0002) hayabusa (0.0005) fightwear- (0.0005) official (0.0012) mma (0.0030) gear (0.0012) of (0.0018) the (-0.0023) ufc (-0.0006)
~~~~~~

**Node-4.2** (global 1988):

~~~~~~text
product (0.0010) from (0.0004) amazon (-0.0006) platform (-0.0001) with (0.0001) title (0.0001) and (0.0005) content (-0.0002) : (0.0005) title (0.0002) : (-0.0001) hayabusa (0.0003) official (-0.0002) mma (-0.0002) champion (-0.0024) hoodie- (0.0002) black. (0.0007) content (0.0012) : (0.0002) reign (-0.0007) supreme (-0.0006) with (0.0003) the (-0.0003) new, (-0.0001) lightweight (-0.0000) hayabusa (-0.0000) champion (-0.0007) hoodie. (0.0005) this (0.0004) throwback, (0.0006) athletic- (-0.0001) fitting (0.0009) hoodie (-0.0003) sports (0.0004) the (-0.0001) traditional (-0.0001) varsity (-0.0005) look (0.0008) and (0.0007) is (0.0002) developed (0.0007) with (0.0001) ultra- (0.0005) fine (0.0007) cotton (0.0011) for (0.0002) extreme (-0.0003) comfort. (0.0011) the (-0.0008) unique (-0.0001) two- (0.0004) tone (-0.0004) design, (0.0006) high- (0.0002) quality (0.0005) embroidery (0.0004) on (-0.0000) the (-0.0009) chest (0.0008) and (0.0005) back (0.0005) and (0.0007) dual- (0.0003) pocket (0.0008) addition (0.0012) give (-0.0005) the (-0.0013) hayabusa (0.0003) champion (-0.0008) hoodie (0.0004) a (-0.0012) style (0.0011) that (0.0004) demands (0.0005) attention. (0.0016) get (-0.0004) yours (0.0003) today! (-0.0003) comfortable (0.0012) 100 (0.0001) % (0.0016) cottonembroidered (0.0003) crestsathletic (0.0002) fit (-0.0043)
~~~~~~

**Node-4.3** (global 1994):

~~~~~~text
product (-0.0011) from (-0.0006) amazon (0.0002) platform (-0.0018) with (-0.0012) title (0.0002) and (-0.0003) content (-0.0004) : (0.0003) title (0.0002) : (-0.0000) title (0.0003) mma (0.0046) digital (-0.0018) interval (0.0001) timer. (-0.0008) content (0.0003) : (0.0001) a (0.0000) necessity (0.0001) for (-0.0003) all (-0.0002) mma (0.0027) training (0.0001) and (-0.0003) gym (0.0007) workouts. (0.0001) the (0.0003) perfect (0.0005) digital (0.0009) countdown (0.0002) timer (-0.0005) has (0.0002) everything (-0.0003) you (0.0001) demand (0.0005) and (-0.0004) more. (0.0000) super (-0.0002) large (-0.0001) 2 (-0.0009) " (0.0000) digital (0.0004) display (0.0000) can (0.0004) be (0.0003) seen (0.0003) easily (-0.0000) in (-0.0000) even (0.0002) the (-0.0001) biggest (-0.0001) gyms (0.0002) or (-0.0002) workout (0.0001) areas. (-0.0002) rounds (0.0006) can (0.0005) be (-0.0001) adjusted (0.0003) from (-0.0000) 1, (-0.0002) 2, (-0.0002) 3, (-0.0004) 4, (-0.0004) 5 (-0.0004) or (-0.0003) 10 (0.0002) minute (0.0005) durations. (0.0003) rest (-0.0001) time (0.0000) can (0.0002) be (0.0002) adjusted (0.0003) from (0.0000) 15 (0.0001) to (0.0001) 75 (0.0001) seconds. (-0.0003) added (0.0001) interval (0.0002) adjustment (0.0004) can (0.0007) be (0.0003) set (0.0002) from (-0.0001) 0 (-0.0002) to (-0.0002) 60 (-0.0005) seconds (-0.0000) for (0.0001) intense (0.0008) training (0.0010) and (-0.0005) workout (0.0010) enhancements. (-0.0003) total (0.0005) rounds (0.0000) can (0.0000) be (0.0001) set (0.0002) for (0.0002) 2, (-0.0003) 3, (-0.0003) 4, (-0.0000) 5 (-0.0005) or (-0.0010) continuous. (0.0010) covers (-0.0002) every (0.0009) training, (0.0008) workout (-0.0002) and (0.0005) fight (0.0007) need (0.0002) you (-0.0009) mandate (0.0007) from (-0.0002) a (0.0013) timer, (-0.0000) and (0.0007) more. (0.0004) added (-0.0007) volume (-0.0003) control (0.0004) on (-0.0003) side (0.0012) lets (0.0013) you (0.0004) adjust (0.0007) to (-0.0003) low, (-0.0000) medium (-0.0002) or (-0.0002) high (-0.0001) depending (-0.0002) on (-0.0004) needs. (0.0001) complete (0.0000) one (0.0014) year (0.0004) warranty. (-0.0001)
~~~~~~

**Node-4.4** (global 2000):

~~~~~~text
product (-0.0010) from (-0.0001) amazon (-0.0013) platform (-0.0023) with (-0.0011) title (0.0001) and (-0.0004) content (-0.0014) : (-0.0002) title (-0.0020) : (-0.0005) hayabusa (-0.0005) flex (-0.0003) fight (-0.0005) shorts. (0.0008) content (-0.0017) : (-0.0003) when (-0.0002) we (0.0013) built (0.0001) the (0.0007) flex (-0.0017) shorts, (-0.0007) we (0.0011) started (0.0004) by (0.0011) & (-0.0012) # (0.0004) xa0 (0.0000) ; (0.0028) taking (-0.0002) things (0.0004) away. (-0.0003) things (0.0003) that (0.0007) fighters (-0.0003) have (0.0001) told (-0.0002) us (-0.0002) they (0.0006) don (-0.0001) ' (0.0001) t (0.0001) want (0.0004) in (0.0003) their (0.0009) fight (0.0002) shorts. (0.0008) for (-0.0004) starters, (-0.0001) you (0.0002) won (0.0001) ' (0.0002) t (0.0002) find (0.0003) any (0.0007) hardware (-0.0006) on (0.0004) the (0.0001) shorts. (0.0004) things (0.0002) like (-0.0001) eyes, (0.0006) exposed (0.0004) laces, (0.0003) metal (0.0006) loops (0.0004) and (0.0008) rivets (0.0002) are (0.0005) out. (0.0011) you (0.0001) don (0.0003) ' (0.0004) t (0.0002) need (0.0004) them (0.0009) weighing (-0.0001) you (-0.0001) down. (0.0006) we (-0.0010) also (0.0004) took (0.0001) away (0.0008) all (0.0003) the (-0.0001) velcro. (0.0012) some (-0.0001) guys (0.0007) like (0.0003) velcro, (0.0007) but (0.0011) let (0.0019) ' (0.0009) s (0.0005) face (0.0003) it (0.0006) ; (0.0028) for (0.0006) some, (0.0012) it (0.0013) ' (0.0006) s (0.0006) a (0.0010) source (0.0005) of (0.0004) chafing (-0.0001) and (0.0004) can (0.0001) lead (-0.0001) to (0.0001) skin (0.0000) abrasions (0.0002) when (0.0001) you (0.0008) ' (-0.0002) re (-0.0002) rolling (-0.0001) on (-0.0004) the (-0.0008) mat. (0.0007)
~~~~~~

**Node-5** (global 14712):

~~~~~~text
product (-0.0076) from (0.0065) amazon (-0.0018) platform (-0.0022) with (0.0031) title (0.0027) and (0.0026) content (0.0024) : (0.0075) title (0.0010) : (0.0090) hayabusa (-0.0016) pro (0.0051) training (-0.0002) series (-0.0001) kick (-0.0009) shield. (0.0007) content (0.0006) : (0.0072) for (0.0036) a (0.0009) well- (0.0031) rounded (0.0027) and (0.0025) effective (0.0039) striking (0.0008) game, (0.0043) you (0.0041) need (0.0018) to (0.0015) have (0.0012) a (0.0017) variety (0.0031) of (0.0033) kicks (0.0024) in (0.0031) your (0.0017) arsenal (0.0051) of (0.0054) attacks (0.0037) to (0.0010) keep (0.0022) your (0.0012) opponent (0.0023) guessing. (0.0052) the (0.0056) hayabusa (0.0004) pro (0.0072) training (0.0022) kick (0.0052) shield (0.0024) is (0.0008) the (0.0035) perfect (0.0019) tool (0.0035) to (-0.0006) help (0.0052) you (0.0019) fine (0.0036) tune (0.0036) your (0.0023) kicks. (0.0002) the (0.0009) multiple (0.0072) handles (-0.0025) on (0.0040) the (0.0019) kick (0.0037) shield (0.0032) allow (0.0060) a (0.0011) fighter (0.0031) to (0.0018) develop (0.0003) a (0.0016) complete (0.0007) kicking (-0.0005) profile. (0.0069) hold (-0.0024) the (0.0011) top (-0.0029) handle (-0.0035) and (0.0042) let (0.0032) the (0.0019) shield (-0.0014) hang (0.0022) low (-0.0011) to (0.0038) perfect (-0.0000) devastating (0.0067) inside (0.0049) and (0.0044) outside (0.0039) leg (0.0047) kicks. (0.0108) the (0.0035) inside (0.0064) top (0.0028) handle (0.0027) is (0.0027) great (0.0052) for (0.0010) perfecting (0.0025) your (-0.0003) push (0.0022) kicks (0.0046) and (0.0038) the (0.0025) inside (0.0042) handles (0.0029) are (-0.0004) well (0.0041) placed (0.0044) for (0.0016) the (0.0027) coach (0.0005) to (-0.0003) brace (0.0024) for (0.0034) powerful (0.0045) body (0.0035) and (0.0027) high (0.0023) kicks. (0.0035) not (0.0018) only (-0.0003) is (0.0003) this (-0.0013) the (-0.0004) most (-0.0008) functional (0.0029) kick (0.0047) shield (0.0022) available, (0.0025) it (0.0012) is (-0.0010) the (0.0002) most (-0.0002) durable (0.0037) and (0.0012) protective (0.0040) shield, (0.0012) period. (0.0061) coaching (-0.0002) a (-0.0025) hard (0.0002) hitting (0.0034) athlete (-0.0020) through (0.0034) an (-0.0001) intense (0.0051) kicking (0.0024) session (0.0029) can (-0.0033) be (0.0001) extremely (0.0037) draining (0.0070) if (0.0022) you (0.0033) do (0.0011) not (-0.0009) use (0.0029) a (-0.0012) shield (-0.0002) that (-0.0003) can (0.0007) properly (0.0000) protect (0.0041) you. (0.0063) the (0.0037) pro (-0.0037) training (0.0008) & (0.0037) # (-0.0013) xa0 (-0.0008) ; (-0.0025) kick (0.0045) shield (0.0010) has (-0.0062) the (0.0009) optimal (0.0013) curvature (0.0050) for (0.0043) the (0.0013) coach (0.0000) and (0.0036) the (0.0031) fighter. (0.0079) the (0.0002) high (-0.0005) impact (0.0016) absorption (0.0022) properties (0.0005) of (0.0028) the (0.0018) inner (0.0039) core (0.0016) ensures (0.0032) maximum (0.0005) protection (0.0028) for (0.0047) the (0.0021) trainer (0.0031) and (0.0045) perfect (0.0017) responsiveness (0.0023) for (0.0068) & (-0.0055) # (-0.0001) xa0 (-0.0011) ; (0.0042) the (0.0051) athlete. (-0.0001) take (0.0049) your (0.0058) striking (0.0038) to (0.0017) new (-0.0009) levels (0.0069) with (0.0003) the (-0.0004) hayabusa (0.0058) pro (0.0091) training (0.0043) kick (0.0075) shield. (0.0142)
~~~~~~
