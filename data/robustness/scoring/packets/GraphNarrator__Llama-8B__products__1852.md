# Reference packet: GraphNarrator__Llama-8B__products__1852

- Method: GraphNarrator; configuration: Llama-8B; dataset: products; target node: 1852
- Explanation source: `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/3.json` (messages[assistant])
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

- ROOT (office supplies)
  - Node-1 (calculator)
    - Node-1.1 (plunger)
    - Node-1.2 (adhesive label)
    - Node-1.3 (electronic calculator)
    - Node-1.4 (security envelopes)
    - Node-1.5 (scissors)
    - Node-1.6 (calculator)

### Word-Level Evaluation

Keywords with high saliency scores in ROOT — "amazon" (0.06), "platform" (0.03), "title" (0.08), and "content" (0.06) — are associated with online shopping and product descriptions, but do not directly indicate a specific product category. However, the presence of "amazon" suggests an online shopping context, which is common in Health & Personal Care products.

### Graph-Level Aggregation

Node-1 (calculator, keywords: "calculator" (0.00), "digital" (0.00), "electronic" (0.00)) is a direct neighbor with moderate saliency, identifying a type of office supply. Indirect neighbors — Node-1.1 (plunger), Node-1.2 (adhesive label), Node-1.3 (electronic calculator), Node-1.4 (security envelopes), Node-1.5 (scissors), and Node-1.6 (calculator) — are all office supplies, collectively confirming an office supply context across both hops.

### Free-Text Explanation

The classification of ROOT into "Health & Personal Care" is not strongly supported by its own keywords or the co-purchase neighborhood.

ROOT: Keywords like "amazon" (0.06) and "platform" (0.03) suggest an online shopping context, but do not directly indicate a specific product category.

- Node-1: A calculator (keywords: "calculator" (0.00), "digital" (0.00), "electronic" (0.00)) is an office supply, reinforcing the office supply context.
  - Node-1.1 ~ Node-1.6: A plunger, adhesive label, electronic calculator, security envelopes, scissors, and another calculator are all office supplies, supporting the office supply category.

In summary, ROOT's own keywords do not strongly signal Health & Personal Care, and the entire co-purchase neighborhood consists of office supplies, providing evidence for the "Office Products" category.
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/3.json`).

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
<verbalized-graph>ROOT: product(0.01) amazon(0.06) platform(0.03) title(0.08) content(0.06) title(0.04) pendaflex(0.01) essentials(-0.01) file(0.02) folders,(0.00) 1(0.03) 3(0.05) cut,(0.00) top(0.03) tab,(-0.01) letter,(0.02) manila,(0.08) 100(-0.01) per(0.02) box,(0.00) 752(0.01) 1(0.02) 3(0.03) ).(0.11) content(-0.07) none(0.05) 
Node-1: product(-0.00) amazon(0.00) platform(0.00) title(0.00) content(0.00) title(0.00) jumbo(0.00) 12-(0.00) digit(-0.00) desktop(-0.00) calculator.(-0.00) content(0.00) 12(-0.00) digits(0.00) calculator(0.00) simple(0.00) calculator(0.00) supposed(0.00) quite(0.00) handily(0.00) easily(0.00) accomplishes(0.00) basic(0.00) mathematical(0.00) functions(0.00) via(0.00) keypad(0.00) large(0.00) key(0.00) size(0.00) provision(0.00) memory(0.00) calculations,(0.00) working(0.00) percentages,(0.00) finding(0.00) square(-0.00) roots.(0.00) jumbo(0.00) size(0.00) measuring(0.00) 5.(-0.00) 75(0.00) 7.(0.00) 25(-0.00) inches(-0.00) boasting(0.00) large,(0.00) upright(0.00) display,(0.00) easy(0.00) use,(0.00) easy(0.00) read(0.00) well-(0.00) lit(0.00) rooms.(0.00) powered(-0.00) solar(0.00) cell,(-0.00) also(0.00) contains(0.00) alkaline(0.00) battery(0.00) allows(-0.00) unit(0.00) used(0.00) lighting(-0.00) conditions.(-0.00) battery(-0.00) life(-0.00) dependent(0.00) upon(0.00) usage,(0.00) though(0.00) alkaline(-0.00) battery(0.00) discharged(0.00) calculator(-0.00) still(0.00) used(0.00) solar(-0.00) power.(-0.00) help(0.00) conserve(-0.00) battery(-0.00) power,(0.00) unit(0.00) automatically(0.00) turns(0.00) used(0.00) eight(0.00) minutes.(0.00) tap(0.00) n(0.00) c(0.00) key(0.00) turns(0.00) back(-0.00) on.(0.00) 
Node-1.1: product(0.00) amazon(0.00) platform(-0.00) title(0.00) content(0.00) title(0.00) 2-(0.00) pack(0.00) neiko(0.00) patented(0.00) heavy-(0.00) duty(0.00) all-(0.00) angle(0.00) super-(0.00) power(0.00) plunger.(-0.00) content(0.00) essential(0.00) plunger(-0.00) made(0.00) better(0.00) powerful,(0.00) versatile(0.00) effective!(-0.00) super-(0.00) pliable(0.00) industrial-(0.00) rubber(0.00) cup(0.00) tiered(0.00) ridges(0.00) forms(0.00) ultra-(0.00) tight(0.00) seal(0.00) size(0.00) drain.(0.00) heavy-(0.00) duty(0.00) steel(0.00) handle(0.00) allows(0.00) maximum(0.00) pressure(0.00) forced(0.00) drain(0.00) source(0.00) clog.(-0.00) designed(0.00) work(0.00) effectively(0.00) angle(0.00) hard-(0.00) to-(0.00) reach,(0.00) low-(0.00) clearance(0.00) applications.(0.00) pays(0.00) many(0.00) times(0.00) one(0.00) use!(0.00) rinses(0.00) clean,(0.00) stores(0.00) easily(0.00) next(0.00) use.(0.00) 
Node-1.2: product(-0.00) amazon(-0.00) platform(-0.00) title(-0.00) content(0.00) title(0.00) smartsign(0.00) adhesive(-0.00) vinyl(-0.00) label,(-0.00) legend(-0.00) quot(-0.00) smoking(-0.00) quot(0.00) graphic,(0.00) 10(-0.00) quot(0.00) high(0.00) x(0.00) 7(0.00) quot(0.00) wide,(0.00) black(0.00) red(-0.00) white.(-0.00) content(0.00) lyle(0.00) signs(-0.00) leading(0.00) manufacturer(-0.00) traffic(-0.00) safety(-0.00) signs(0.00) usa(-0.00) 100(0.00) years.(-0.00) lyle(0.00) safety(-0.00) decal(-0.00) manufactured(0.00) using(0.00) quality(0.00) non-(0.00) reflective(0.00) vinyl(-0.00) films.(0.00) decal(-0.00) meets(0.00) osha(0.00) 1910.(0.00) 145(0.00) requirements.(0.00) decal(0.00) designed(0.00) last(0.00) 4(0.00) years(0.00) outdoor(-0.00) applications(0.00) longer(0.00) indoor(-0.00) applications.(0.00) lyle(-0.00) signs(0.00) supplies(0.00) decal(0.00) pressure-(0.00) sensitive(0.00) adhesive(-0.00) easy(0.00) application.(0.00) lyle(-0.00) signs(-0.00) 10,(-0.00) 000(-0.00) stock(-0.00) legends(-0.00) available(-0.00) various(0.00) sizes,(-0.00) colors(-0.00) materials.(0.00) lyle(-0.00) safety(0.00) decal(0.00) intended(0.00) used(0.00) commercial,(-0.00) industrial,(0.00) manufacturing(0.00) utility(0.00) environments.(0.00) designed(0.00) help(0.00) prevent(0.00) injuries,(0.00) warn(0.00) hazardous(0.00) situations,(0.00) improve(0.00) safety(0.00) reduce(0.00) downtime.(0.00) color(0.00) red(0.00) black(0.00) white.(-0.00) legend(0.00) smoking(-0.00) symbol(0.00) ".(-0.00) 
Node-1.3: product(-0.00) amazon(-0.00) platform(-0.00) title(0.00) content(-0.00) title(0.00) easy-(-0.00) see(-0.00) electronic(-0.00) digital(-0.00) calculator-(-0.00) large(-0.00) tilt(-0.00) display-(-0.00) big(0.00) buttons.(-0.00) content(0.00) none(-0.00) 
Node-1.4: product(-0.00) amazon(0.00) platform(0.00) title(0.00) content(0.00) title(0.00) columbian(0.00) co128(0.00) 10(0.00) 4-(0.00) 1(0.00) 8x9-(0.00) 1(0.00) 2-(0.00) inch(0.00) security(0.00) tinted(0.00) white(0.00) envelopes,(0.00) 500(0.00) count.(0.00) content(0.00) envelope(0.00) ideal(0.00) business,(0.00) professional(0.00) personal(0.00) correspondence.(0.00) features(0.00) security(0.00) tinted(0.00) added(0.00) privacy(0.00) confidentiality.(0.00) executive(0.00) style(0.00) diagonal(0.00) seam(0.00) v-(0.00) flap(0.00) construction.(0.00) premium(0.00) 24lb(0.00) white(0.00) wove(0.00) stock.(0.00) moisture(0.00) activated(0.00) gummed(0.00) seal.(0.00) sized(0.00) 10(0.00) 4-(0.00) 1(0.00) 8(0.00) x(0.00) 9-(0.00) 1(0.00) 2(0.00) ".(0.00) quantity(0.00) 500(-0.00) envelopes.(0.00) 
Node-1.5: product(0.00) amazon(0.00) platform(0.00) title(0.00) content(0.00) title(0.00) fiskars(0.00) recycled(0.00) 8(0.00) inch(0.00) strait(0.00) scissors(0.00) 01-(0.00) 004253j(0.00) ).(-0.00) content(0.00) none(-0.00) 
Node-1.6: product(-0.00) amazon(-0.00) platform(-0.00) title(0.00) content(-0.00) title(0.00) canon(0.00) ls-(0.00) 82z(-0.00) calculator.(0.00) content(0.00) canon(0.00) compact(0.00) ls82z(-0.00) calculator(0.00) provides(0.00) range(0.00) functions(0.00) quick(0.00) calculations(0.00) easy(0.00) figuring(0.00) finances.(0.00) ideal(0.00) tool(0.00) home,(0.00) office,(0.00) school,(0.00) providing(0.00) basics(0.00) calculation(0.00) addition,(0.00) subtraction,(0.00) multiplication,(0.00) division,(0.00) constant(0.00) multiplication,(0.00) division(0.00) percentage(0.00) calculations,(0.00)</verbalized-graph>

### Classification Label
Health & Personal Care

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 1852
- Title: Pendaflex Essentials File Folders, 1/3 Cut, Top Tab, Letter, Manila, 100 Per Box, (752 1/3)
- True class (canonical `y`): **Office Products**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Health & Personal Care**
- Prediction recorded by this method's pipeline: **Health & Personal Care**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Pendaflex Essentials File Folders, 1/3 Cut, Top Tab, Letter, Manila, 100 Per Box, (752 1/3). Content: None
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 9 nodes

| node id | true class | title |
|---|---|---|
| 151 | Electronics | Jumbo 12-Digit Desktop Calculator |
| 1820 | Office Products | &quot;Package of Two&quot; Texas Instruments TI-5142, 5150, 5630, 8230 and 8630 Ink Roller, Compatible, Black |
| 1907 | Office Products | NEW Compatible Nukote BR80C Calculator Ribbon Black/Red (2-pack) For Canon MP-11 DX |
| 6192 | Electronics | Centon DSP4GB10PK&nbsp;10 x 4GB Multi-pack Pro USB Flash Drive (Grey) |
| 14323 | Office Products | V4INK&#65533; New Compatible HP 131A Toner Cartridge-Black (CF210A) for Hp Laserjet Pro M251 M276 Toner Printers |
| 14324 | Office Products | Alliance Sterling Ergonomically Correct Rubber Bands, #105, 0.625 x 5 Inches, 70 per 1lb Box (25055) |
| 14325 | Office Products | Quartet Prestige Colored Cork Bulletin Board, 3 x 2 Feet, Graphite Finish Frame (B243G) |
| 14326 | Office Products | TOPS Spiral Steno Books, 6 x 9 Inches, Gregg Rule, White Paper, Assorted Covers, 80 Sheets per Book, 4 Books per Pack (80220) |
| 14327 | Office Products | TOPS Weekly Time Cards, Green Ink Front, 3.5 x 9 Inches, 500-Count, Manila (1256) |

### 2-hop (shortest distance exactly 2): 24 nodes

| node id | true class | title |
|---|---|---|
| 1 | Office Products | Casio DR-270TM 2-Color Professional Desktop Printing Calculator |
| 147 | Office Products | Casio Inc. HR-100TM Business Calculator |
| 150 | Office Products | Canon P23-DH V 2 color mini-Desktop Printing Calculator |
| 156 | Office & School Supplies | 6 PK Calculator Ink Rollers, IR-40T / Canon CP13 / NU-KOTE NR42 / NR422 for Various Sharp, VICTOR, ADLER-ROYAL, CANON, CASIO, AURORA, CITIZEN, OLIVETTI, TEXAS INSTRUMENTS Calculators |
| 713 | Electronics | Case Logic VNA-216 16-Inch Laptop Attache (Black) |
| 1851 | Home & Kitchen | 2-Pack Neiko Patented Heavy-Duty All-Angle Super-Power Plunger |
| 1853 | Industrial & Scientific | SmartSign Adhesive Vinyl Label, Legend &quot;No Smoking&quot; with Graphic, 10&quot; high x 7&quot; wide, Black/Red on White |
| 1854 | Office Products | Easy-See Electronic Digital Calculator - Large Tilt Display - Big Buttons |
| 1855 | Office Products | Columbian CO128 (#10) 4-1/8x9-1/2-Inch Security Tinted White Envelopes, 500 Count |
| 1856 | Arts, Crafts & Sewing | Fiskars Recycled 8 Inch Strait Scissors (01-004253J) |
| 1857 | Office Products | Canon LS-82Z Calculator |
| 1858 | Health & Personal Care | Long Reach Comfort Wipe (1) |
| 1859 | Office Products | Swingline Deluxe Staple Remover, Extra Wide, Steel Jaws, Black (S7038101) |
| 1860 | label 25 | missing |
| 1878 | Office Products | Calculator Plain Paper |
| 1904 | Office Products | Compatible Universal Calculator Spool EPC B / R Black and Red Ribbons, Works for Casio DR 210 HD, Casio DR 210 HT, Casio DR 210 TM, Casio DR 220 |
| 14001 | Electronics | SanDisk Cruzer Blade 4GB (10 pack) USB 2.0 Flash Drive Jump Drive Thumb Drive SDCZ50-004G-10PK w/ (5) Everything But Stromboli (TM) Lanyard |
| 14185 | Office Products | HP 05A Black Original LaserJet Toner Cartridge |
| 14186 | Office Products | PM Company Perfection POS/Calculator Rolls, 2.25 Inches x 150 Feet, White, 12/Pack (08835) |
| 14255 | Office Products | ACCO Economy Jumbo Paper Clips, Smooth, Jumbo, 100/Box, 10 Boxes (72580) |
| 14550 | Office Products | NEW Compatible Nukote BR80C Calculator Ribbon Black/Red (6-pack) For Canon MP-11 DX |
| 14551 | Office Products | Columbian CO790 9x12-Inch Clasp Brown Kraft Envelopes, 100 Count |
| 29325 | Electronics | Logitech MK710 Wireless Desktop Mouse and Keyboard Combo |
| 29326 | Electronics | Endust Multi-Surface Electronics Anti-Static Cleaner - 12 Pack (096000P12) |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/3.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Health & Personal Care**, ground truth = **Office Products**.
The verbalized graph is 30390 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 1852 | 35 | 0.1065 | yes |
| Node-1 | 1 | 151 | 164 | 0.0027 | yes |
| Node-1.1 | 10 | 1851 | 99 | 0.0005 | yes |
| Node-1.2 | 11 | 1853 | 178 | 0.0007 | yes |
| Node-1.3 | 12 | 1854 | 24 | 0.0005 | yes |
| Node-1.4 | 13 | 1855 | 89 | 0.0007 | yes |
| Node-1.5 | 14 | 1856 | 24 | 0.0018 | yes |
| Node-1.6 | 15 | 1857 | 142 | 0.0005 | yes |
| Node-1.7 | 16 | 1858 | 82 | 0.0008 | no |
| Node-1.8 | 17 | 1859 | 51 | 0.0007 | no |
| Node-1.9 | 18 | 1860 | 37 | 0.0008 | no |
| Node-2 | 2 | 1820 | 60 | 0.0113 | no |
| Node-2.1 | 19 | 147 | 20 | 0.0011 | no |
| Node-2.2 | 20 | 150 | 298 | 0.0009 | no |
| Node-2.3 | 21 | 1878 | 25 | 0.0072 | no |
| Node-2.4 | 22 | 14185 | 27 | 0.0028 | no |
| Node-2.5 | 23 | 14186 | 85 | 0.0012 | no |
| Node-3 | 3 | 1907 | 60 | 0.0165 | no |
| Node-3.1 | 24 | 156 | 213 | 0.0011 | no |
| Node-3.2 | 25 | 1904 | 76 | 0.0074 | no |
| Node-3.3 | 26 | 14255 | 80 | 0.0007 | no |
| Node-3.4 | 27 | 14550 | 60 | 0.0016 | no |
| Node-3.5 | 28 | 14551 | 82 | 0.0007 | no |
| Node-4 | 4 | 6192 | 198 | 0.0270 | no |
| Node-4.1 | 29 | 713 | 25 | 0.0026 | no |
| Node-4.2 | 30 | 14001 | 319 | 0.0012 | no |
| Node-4.3 | 31 | 29325 | 22 | 0.0029 | no |
| Node-4.4 | 32 | 29326 | 158 | 0.0019 | no |
| Node-5 | 5 | 14323 | 59 | 0.0189 | no |
| Node-6 | 6 | 14324 | 100 | 0.0104 | no |
| Node-7 | 7 | 14325 | 30 | 0.0431 | no |
| Node-8 | 8 | 14326 | 197 | 0.0054 | no |
| Node-9 | 9 | 14327 | 155 | 0.0050 | no |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->Node-1.6, Node-1->Node-1.7, Node-1->Node-1.8, Node-1->Node-1.9, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, Node-1.6->Node-1, Node-1.7->Node-1, Node-1.8->Node-1, Node-1.9->Node-1, Node-2->Node-2.1, Node-2->Node-2.2, Node-2->Node-2.3, Node-2->Node-2.4, Node-2->Node-2.5, Node-2->ROOT, Node-2.1->Node-2, Node-2.2->Node-2, Node-2.3->Node-2, Node-2.3->Node-3, Node-2.4->Node-2, Node-2.5->Node-2, Node-3->Node-2.3, Node-3->Node-3.1, Node-3->Node-3.2, Node-3->Node-3.3, Node-3->Node-3.4, Node-3->Node-3.5, Node-3->ROOT, Node-3.1->Node-3, Node-3.2->Node-3, Node-3.3->Node-3, Node-3.4->Node-3, Node-3.5->Node-3, Node-4->Node-4.1, Node-4->Node-4.2, Node-4->Node-4.3, Node-4->Node-4.4, Node-4->ROOT, Node-4.1->Node-4, Node-4.2->Node-4, Node-4.3->Node-4, Node-4.4->Node-4, Node-5->ROOT, Node-6->ROOT, Node-7->ROOT, Node-8->ROOT, Node-9->ROOT, ROOT->Node-1, ROOT->Node-2, ROOT->Node-3, ROOT->Node-4, ROOT->Node-5, ROOT->Node-6, ROOT->Node-7, ROOT->Node-8, ROOT->Node-9

### Tokens and scores

**ROOT** (global 1852):

~~~~~~text
product (0.0144) from (0.0016) amazon (0.0565) platform (0.0348) with (0.0080) title (0.0816) and (-0.0124) content (0.0631) : (-0.0422) title (0.0392) : (-0.0065) pendaflex (0.0054) essentials (-0.0102) file (0.0183) folders, (0.0048) 1 (0.0253) / (0.0182) 3 (0.0456) cut, (0.0026) top (0.0268) tab, (-0.0096) letter, (0.0192) manila, (0.0756) 100 (-0.0091) per (0.0230) box, (0.0039) ( (0.0389) 752 (0.0076) 1 (0.0163) / (0.0204) 3 (0.0285) ). (0.1065) content (-0.0683) : (-0.0065) none (0.0469)
~~~~~~

**Node-1** (global 151):

~~~~~~text
product (-0.0003) from (0.0001) amazon (0.0019) platform (0.0001) with (0.0004) title (0.0021) and (0.0013) content (0.0022) : (0.0027) title (0.0015) : (0.0019) jumbo (0.0008) 12- (0.0012) digit (-0.0004) desktop (-0.0006) calculator. (-0.0002) content (0.0018) : (0.0012) this (-0.0001) 12 (-0.0007) digits (0.0004) calculator (0.0005) does (0.0005) what (0.0013) a (-0.0002) simple (0.0007) calculator (0.0008) is (0.0006) supposed (0.0012) to (0.0002) do (0.0003) quite (0.0007) handily (0.0003) : (0.0015) it (0.0007) easily (0.0011) accomplishes (0.0006) basic (0.0005) mathematical (0.0000) functions (0.0007) via (0.0019) a (-0.0002) keypad (0.0010) with (0.0002) large (0.0004) key (0.0009) size (0.0010) and (0.0009) has (0.0009) provision (0.0003) for (0.0004) memory (0.0004) calculations, (0.0006) working (0.0009) with (0.0012) percentages, (0.0019) and (0.0003) finding (0.0019) square (-0.0002) roots. (0.0004) jumbo (0.0027) size (0.0013) measuring (0.0014) 5. (-0.0005) 75 (0.0004) by (0.0010) 7. (0.0002) 25 (-0.0000) inches (-0.0002) and (0.0008) boasting (0.0007) a (-0.0011) large, (0.0008) upright (0.0003) display, (0.0009) it (0.0012) is (0.0022) easy (0.0013) to (0.0011) use, (0.0009) and (0.0011) is (0.0022) easy (0.0014) to (0.0014) read (0.0025) in (0.0005) well- (0.0010) lit (0.0011) rooms. (0.0022) powered (-0.0004) by (0.0009) a (-0.0001) solar (0.0012) cell, (-0.0008) it (0.0000) also (0.0015) contains (0.0018) an (-0.0001) alkaline (0.0011) battery (0.0010) which (0.0001) allows (-0.0005) the (-0.0001) unit (0.0007) to (-0.0002) be (0.0011) used (0.0011) under (-0.0005) most (0.0005) lighting (-0.0005) conditions. (-0.0005) battery (-0.0010) life (-0.0008) is (0.0002) dependent (0.0003) upon (0.0000) usage, (0.0003) though (0.0009) once (0.0001) the (-0.0016) alkaline (-0.0002) battery (0.0009) is (0.0018) discharged (0.0020) the (-0.0009) calculator (-0.0001) can (-0.0003) still (0.0005) be (0.0012) used (0.0004) on (0.0000) solar (-0.0001) power. (-0.0008) to (0.0006) help (0.0007) conserve (-0.0008) battery (-0.0001) power, (0.0004) the (0.0004) unit (0.0011) automatically (0.0025) turns (0.0010) itself (-0.0002) off (-0.0000) if (0.0012) it (0.0008) is (0.0013) not (0.0010) used (0.0009) for (-0.0001) eight (0.0002) minutes. (0.0002) a (0.0015) tap (0.0011) on (-0.0005) the (-0.0006) n (0.0012) / (0.0016) c (0.0010) key (0.0014) turns (0.0009) it (0.0008) back (-0.0011) on. (0.0009)
~~~~~~

**Node-1.1** (global 1851):

~~~~~~text
product (0.0000) from (0.0002) amazon (0.0002) platform (-0.0001) with (0.0000) title (0.0003) and (0.0003) content (0.0002) : (0.0004) title (0.0002) : (0.0003) 2- (0.0002) pack (0.0004) neiko (0.0002) patented (0.0002) heavy- (0.0003) duty (0.0001) all- (0.0002) angle (0.0001) super- (0.0002) power (0.0001) plunger. (-0.0000) content (0.0003) : (0.0003) the (-0.0002) essential (0.0002) plunger (-0.0001) made (0.0002) better (0.0001) : (0.0001) more (0.0001) powerful, (0.0002) more (0.0001) versatile (0.0003) and (0.0003) more (0.0003) effective! (-0.0002) super- (0.0002) pliable (0.0002) industrial- (0.0001) rubber (0.0002) cup (0.0002) with (0.0001) tiered (0.0001) ridges (0.0004) forms (0.0001) ultra- (0.0003) tight (0.0002) seal (0.0002) on (0.0001) any (0.0001) size (0.0001) drain. (0.0001) heavy- (0.0001) duty (0.0000) steel (0.0001) handle (0.0002) allows (0.0004) for (0.0000) maximum (0.0001) pressure (0.0001) forced (0.0001) down (-0.0001) drain (0.0001) to (0.0000) source (0.0001) of (0.0000) clog. (-0.0000) designed (0.0004) to (0.0000) work (0.0001) effectively (0.0002) at (0.0002) any (0.0002) angle (0.0001) for (0.0001) hard- (0.0002) to- (0.0002) reach, (0.0000) low- (0.0001) clearance (0.0001) applications. (0.0002) pays (0.0001) for (-0.0001) itself (0.0001) many (0.0003) times (0.0002) over (0.0001) with (0.0003) just (0.0002) one (0.0002) use! (0.0002) rinses (0.0001) clean, (0.0002) stores (0.0001) easily (0.0005) for (0.0004) next (0.0001) use. (0.0003)
~~~~~~

**Node-1.2** (global 1853):

~~~~~~text
product (-0.0001) from (-0.0003) amazon (-0.0002) platform (-0.0002) with (-0.0002) title (-0.0000) and (-0.0001) content (0.0000) : (-0.0001) title (0.0000) : (0.0002) smartsign (0.0001) adhesive (-0.0001) vinyl (-0.0004) label, (-0.0001) legend (-0.0001) & (-0.0000) quot (-0.0000) ; (0.0001) no (0.0001) smoking (-0.0000) & (-0.0000) quot (0.0000) ; (0.0001) with (0.0000) graphic, (0.0001) 10 (-0.0001) & (-0.0000) quot (0.0001) ; (0.0000) high (0.0001) x (0.0002) 7 (0.0001) & (0.0000) quot (0.0001) ; (0.0000) wide, (0.0001) black (0.0000) / (0.0001) red (-0.0000) on (0.0002) white. (-0.0015) content (0.0005) : (-0.0008) lyle (0.0003) signs (-0.0010) is (0.0001) a (-0.0002) leading (0.0002) manufacturer (-0.0000) of (-0.0001) traffic (-0.0004) and (-0.0001) safety (-0.0001) signs (0.0003) in (-0.0001) the (0.0001) usa (-0.0002) for (0.0001) over (0.0001) 100 (0.0001) years. (-0.0004) this (-0.0001) lyle (0.0004) safety (-0.0002) decal (-0.0001) is (0.0003) manufactured (0.0001) using (0.0001) quality (0.0002) non- (0.0001) reflective (0.0002) vinyl (-0.0001) films. (0.0003) this (0.0000) decal (-0.0001) meets (0.0004) osha (0.0003) 1910. (0.0003) 145 (0.0003) requirements. (0.0002) this (0.0002) decal (0.0001) is (0.0003) designed (0.0004) to (0.0000) last (0.0001) up (0.0001) to (0.0001) 4 (0.0001) years (0.0001) for (0.0002) outdoor (-0.0001) applications (0.0003) and (0.0001) longer (0.0002) for (0.0002) indoor (-0.0000) applications. (0.0001) lyle (-0.0001) signs (0.0004) supplies (0.0005) your (-0.0001) decal (0.0001) with (0.0001) pressure- (0.0002) sensitive (0.0000) adhesive (-0.0000) for (0.0000) easy (0.0001) application. (0.0007) lyle (-0.0005) signs (-0.0001) has (0.0004) more (0.0001) than (-0.0001) 10, (-0.0000) 000 (-0.0002) stock (-0.0003) legends (-0.0005) available (-0.0001) to (0.0000) you (0.0003) in (-0.0000) various (0.0001) sizes, (-0.0000) colors (-0.0000) and (0.0000) materials. (0.0001) this (0.0002) lyle (-0.0005) safety (0.0002) decal (0.0002) is (0.0003) intended (0.0001) to (-0.0000) be (0.0001) used (0.0001) in (-0.0001) commercial, (-0.0000) industrial, (0.0001) manufacturing (0.0000) and (0.0000) utility (0.0003) environments. (0.0000) it (0.0001) is (0.0002) designed (0.0003) to (0.0000) help (0.0002) prevent (0.0001) injuries, (0.0002) warn (0.0002) of (0.0000) hazardous (0.0001) situations, (0.0001) improve (0.0001) safety (0.0002) and (0.0000) reduce (0.0002) downtime. (0.0000) the (0.0002) color (0.0001) is (0.0002) red (0.0001) and (0.0000) black (0.0001) on (0.0001) white. (-0.0001) the (0.0001) legend (0.0002) is (-0.0001) " (0.0000) no (-0.0002) smoking (-0.0001) with (-0.0001) symbol (0.0002) ". (-0.0002)
~~~~~~

**Node-1.3** (global 1854):

~~~~~~text
product (-0.0012) from (0.0002) amazon (-0.0022) platform (-0.0005) with (-0.0004) title (0.0003) and (-0.0006) content (-0.0006) : (0.0002) title (0.0001) : (-0.0007) easy- (-0.0003) see (-0.0003) electronic (-0.0002) digital (-0.0005) calculator- (-0.0003) large (-0.0005) tilt (-0.0002) display- (-0.0006) big (0.0005) buttons. (-0.0011) content (0.0003) : (0.0001) none (-0.0008)
~~~~~~

**Node-1.4** (global 1855):

~~~~~~text
product (-0.0000) from (-0.0000) amazon (0.0001) platform (0.0001) with (-0.0001) title (0.0003) and (-0.0002) content (0.0003) : (-0.0002) title (0.0002) : (0.0001) columbian (0.0003) co128 (0.0001) ( (0.0001) # (-0.0001) 10 (0.0001) ) (-0.0001) 4- (0.0000) 1 (0.0000) / (-0.0000) 8x9- (0.0001) 1 (0.0000) / (0.0000) 2- (0.0000) inch (0.0002) security (0.0001) tinted (0.0001) white (0.0001) envelopes, (0.0001) 500 (0.0007) count. (0.0002) content (0.0003) : (-0.0003) envelope (0.0004) is (0.0002) ideal (0.0001) for (-0.0000) all (0.0001) business, (0.0001) professional (0.0002) and (-0.0000) personal (0.0001) correspondence. (0.0004) features (0.0002) : (0.0001) security (0.0002) tinted (0.0002) for (-0.0000) added (0.0001) privacy (0.0002) and (0.0000) confidentiality. (0.0001) executive (0.0001) style (0.0001) diagonal (0.0002) seam (0.0002) v- (0.0001) flap (0.0005) construction. (0.0003) premium (0.0003) 24lb (0.0001) white (0.0002) wove (0.0002) stock. (0.0003) moisture (0.0002) activated (0.0002) gummed (0.0001) seal. (0.0003) sized (0.0002) : (0.0003) ( (0.0002) # (0.0001) 10 (0.0001) ) (-0.0000) 4- (0.0001) 1 (0.0001) / (0.0001) 8 (0.0001) " (-0.0000) x (0.0001) 9- (0.0001) 1 (0.0001) / (0.0001) 2 (0.0003) ". (0.0004) quantity (0.0006) = (0.0001) 500 (-0.0002) envelopes. (0.0003)
~~~~~~

**Node-1.5** (global 1856):

~~~~~~text
product (0.0011) from (0.0002) amazon (0.0008) platform (0.0001) with (0.0002) title (0.0005) and (0.0003) content (0.0008) : (0.0006) title (0.0005) : (0.0008) fiskars (0.0003) recycled (0.0017) 8 (0.0004) inch (0.0014) strait (0.0006) scissors (0.0018) ( (0.0007) 01- (0.0001) 004253j (0.0006) ). (-0.0004) content (0.0009) : (0.0000) none (-0.0000)
~~~~~~

**Node-1.6** (global 1857):

~~~~~~text
product (-0.0000) from (-0.0002) amazon (-0.0003) platform (-0.0000) with (0.0000) title (0.0000) and (-0.0000) content (-0.0000) : (-0.0002) title (0.0000) : (-0.0001) canon (0.0001) ls- (0.0001) 82z (-0.0000) calculator. (0.0001) content (0.0001) : (0.0001) canon (0.0003) ' (-0.0000) s (0.0002) compact (0.0000) ls82z (-0.0005) calculator (0.0000) provides (0.0001) a (0.0001) range (0.0001) of (-0.0000) functions (0.0001) for (-0.0001) quick (0.0002) calculations (0.0000) and (-0.0001) easy (0.0002) figuring (0.0002) of (-0.0002) finances. (0.0000) it (0.0000) ' (-0.0000) s (0.0003) an (-0.0001) ideal (0.0002) tool (0.0002) for (0.0001) home, (0.0001) office, (0.0002) and (-0.0001) school, (0.0001) providing (0.0000) all (0.0001) the (-0.0001) basics (0.0001) of (-0.0001) calculation (0.0001) : (0.0002) addition, (0.0001) subtraction, (0.0001) multiplication, (0.0002) division, (0.0002) constant (0.0002) multiplication, (0.0002) division (0.0000) and (0.0002) percentage (0.0003) calculations, (0.0003) percentage (0.0004) add- (0.0002) on, (0.0003) and (0.0002) discount (0.0005) calculations. (0.0001) the (-0.0001) extra- (0.0003) large (0.0004) lcd (0.0003) display (0.0003) is (0.0004) angled (0.0002) to (0.0002) improve (0.0004) desktop (0.0001) viewing (0.0003) and (0.0001) to (0.0002) reduce (0.0003) glare (0.0003) and (0.0002) eyestrain (0.0003) ; (0.0002) the (-0.0004) numbers (0.0004) look (0.0003) crisp (0.0003) even (0.0002) in (0.0003) low (0.0003) light. (0.0000) special (0.0005) function (0.0002) keys (0.0002) and (-0.0000) a (0.0001) comfortable (0.0003) keyboard (-0.0001) design, (0.0001) with (0.0001) large (0.0002) bold (-0.0000) colors, (0.0001) also (0.0001) increase (-0.0000) your (-0.0002) speed (0.0000) and (-0.0001) accuracy. (-0.0002) the (0.0002) ls82z (0.0004) measures (-0.0002) approximately (-0.0002) 3. (0.0001) 5 (0.0000) by (-0.0002) 4. (0.0000) 5 (0.0001) by (-0.0000) 2. (0.0001) 25 (0.0001) inches (0.0002) and (-0.0000) features (0.0001) an (0.0001) automatic (0.0002) power (0.0002) selection (0.0002) that (0.0001) shifts (-0.0000) between (0.0001) solar (0.0001) and (-0.0001) battery (0.0001) power (0.0001) as (0.0004) needed. (0.0001)
~~~~~~

**Node-1.7** (global 1858):

~~~~~~text
product (0.0003) from (0.0002) amazon (0.0004) platform (-0.0001) with (0.0004) title (0.0001) and (0.0003) content (-0.0002) : (0.0002) title (0.0004) : (0.0002) long (0.0003) reach (0.0003) comfort (0.0003) wipe (-0.0005) ( (0.0008) 1 (0.0004) ). (-0.0001) content (0.0002) : (0.0001) jb5231 (0.0001) features (-0.0001) :- (0.0002) long (0.0000) reach (0.0002) comfort (-0.0001) wipe.- (0.0001) answer (-0.0000) to (0.0001) personal (0.0002) hygiene (0.0002) when (0.0004) reaching (0.0001) is (0.0000) difficult.- (0.0001) ergonomic (0.0002) shape (0.0001) helps (0.0001) those (0.0002) with (0.0001) limited (0.0002) dexterity.- (0.0001) soft (0.0001) flexible (0.0002) head (-0.0001) grips (0.0001) toilet (0.0001) paper, (0.0000) tissue (0.0000) or (0.0001) pre- (0.0000) moistened (0.0000) wipes (0.0002) securely.- (0.0002) contains (-0.0000) a (0.0002) unique (-0.0002) release (0.0002) button (0.0002) for (0.0000) fast (0.0005) sanitary (0.0000) disposal.- (0.0002) dimensions (-0.0001) : (0.0001) 1. (0.0001) 38 (-0.0002) ' (-0.0001) ' (-0.0002) h (0.0002) x (0.0005) 1. (0.0002) 97 (0.0000) ' (-0.0002) ' (-0.0001) w (0.0000) x (0.0000) 15. (0.0001) 75 (-0.0006) ' (0.0005) ' (-0.0000) d. (0.0005)
~~~~~~

**Node-1.8** (global 1859):

~~~~~~text
product (0.0003) from (0.0005) amazon (0.0007) platform (-0.0004) with (-0.0000) title (0.0002) and (-0.0002) content (0.0001) : (0.0000) title (0.0003) : (0.0001) swingline (0.0003) deluxe (0.0006) staple (0.0005) remover, (0.0001) extra (0.0002) wide, (0.0004) steel (0.0003) jaws, (0.0002) black (0.0002) ( (0.0005) s7038101 (0.0002) ). (0.0003) content (0.0004) : (0.0002) standard (0.0005) design (0.0005) stapler (0.0002) remover (-0.0000) enhanced (0.0003) with (-0.0001) textured (0.0003) non- (0.0004) slip (0.0003) surface. (0.0005) durable (-0.0001) steel (0.0004) jaws (0.0002) and (0.0000) extra- (0.0002) wide (0.0006) finger (-0.0001) grips (0.0005) make (-0.0005) removing (0.0002) standard (0.0006) and (-0.0000) mini- (0.0003) size (0.0007) staples (0.0004) easier. (0.0004)
~~~~~~

**Node-1.9** (global 1860):

~~~~~~text
product (-0.0003) from (0.0001) amazon (0.0004) platform (0.0004) with (-0.0001) title (0.0004) and (-0.0002) content (0.0005) : (0.0001) title (-0.0000) : (0.0004) missing. (0.0002) content (0.0005) : (0.0000) 5 (-0.0002) pack (0.0001) large (0.0008) print, (-0.0001) low (0.0005) vision (0.0002) transaction (-0.0001) registers (0.0001) for (0.0004) checkbooks. (0.0007) works (0.0006) with (-0.0003) any (-0.0005) standard, (-0.0001) top- (0.0002) tear (0.0005) checkbook (0.0006) cover. (0.0003) calendars (0.0002) for (0.0004) 2014- (0.0005) 2015- (0.0004) 2016. (0.0006)
~~~~~~

**Node-2** (global 1820):

~~~~~~text
product (0.0005) from (-0.0001) amazon (0.0076) platform (-0.0037) with (0.0017) title (0.0022) and (0.0019) content (0.0017) : (0.0077) title (0.0043) : (0.0038) & (0.0042) quot (-0.0016) ; (0.0061) package (-0.0002) of (0.0016) two (0.0075) & (-0.0031) quot (-0.0006) ; (0.0033) texas (0.0028) instruments (0.0046) ti- (0.0017) 5142, (0.0035) 5150, (0.0027) 5630, (0.0033) 8230 (0.0037) and (0.0037) 8630 (0.0042) ink (0.0034) roller, (0.0050) compatible, (0.0026) black. (-0.0080) content (0.0113) : (0.0022) this (0.0066) ink (0.0081) roller (0.0011) works (0.0043) with (-0.0017) the (0.0045) texas (0.0044) instruments (0.0049) 5142, (0.0016) 5150, (0.0013) 5630, (0.0018) 8230 (0.0020) and (0.0053) 8630 (0.0010) calculators. (-0.0019) we (0.0065) refund (0.0084) a (0.0035) portion (0.0042) of (0.0067) shipping (0.0018) for (0.0035) purchasing (0.0080) multiple (0.0014) items. (0.0018)
~~~~~~

**Node-2.1** (global 147):

~~~~~~text
product (0.0002) from (0.0009) amazon (0.0003) platform (0.0002) with (-0.0001) title (0.0006) and (-0.0008) content (0.0011) : (-0.0005) title (0.0001) : (-0.0007) casio (0.0001) inc. (0.0005) hr- (0.0007) 100tm (0.0003) business (0.0001) calculator. (0.0011) content (-0.0003) : (-0.0003) none (0.0010)
~~~~~~

**Node-2.2** (global 150):

~~~~~~text
product (0.0000) from (-0.0000) amazon (0.0002) platform (0.0001) with (-0.0001) title (0.0001) and (0.0003) content (0.0000) : (0.0003) title (0.0001) : (0.0003) canon (-0.0001) p23- (0.0002) dh (-0.0001) v (0.0001) 2 (0.0001) color (-0.0001) mini- (0.0001) desktop (-0.0001) printing (0.0000) calculator. (0.0001) content (0.0001) : (-0.0000) cnmp23dhv. (0.0002) the (0.0000) next (-0.0000) generation (-0.0000) portable (0.0002) printing (0.0002) calculator (0.0001) has (0.0000) arrived. (0.0003) features (0.0002) time (0.0001) calculation (0.0003) where (0.0002) time (0.0002) based (0.0002) fee (-0.0003) structures (0.0001) are (0.0001) needed. (0.0002) delivers (0.0001) high (0.0001) performance (0.0002) for (-0.0000) your (0.0001) everyday (-0.0000) calculations. (0.0001) time (0.0000) and (0.0001) date (-0.0001) function (0.0001) enables (0.0003) you (0.0002) to (0.0001) view (0.0001) the (-0.0003) time (0.0001) and (0.0001) date (0.0001) with (-0.0001) a (0.0001) quick (0.0002) glance. (0.0002) ability (0.0004) to (0.0000) perform (0.0001) profit (0.0002) margin (0.0001) calculations (0.0003) with (0.0000) the (-0.0002) touch (0.0001) of (-0.0001) just (0.0001) a (0.0000) few (0.0002) keys. (-0.0001) builtin (0.0001) low (0.0001) battery (-0.0001) indicator (0.0002) to (0.0000) alert (-0.0000) you (0.0001) when (-0.0000) it (0.0001) ' (0.0001) s (0.0002) time (0.0001) to (-0.0001) change (0.0000) the (-0.0002) batteries. (-0.0004) calculator (-0.0000) type (0.0001) : (0.0003) printing (-0.0002) ; (0.0001) global (0.0003) product (0.0001) type (0.0001) : (0.0004) calculators (-0.0001) ; (0.0001) calculator (-0.0001) style (0.0000) : (0.0001) n (-0.0000) / (0.0001) a (0.0002) ; (0.0002) power (-0.0000) source (0.0001) ( (0.0002) s (-0.0000) ) (0.0001) : (0.0001) ac (-0.0001) ; (-0.0000) battery. (0.0001) product (0.0000) details (0.0001) : (0.0001) markup (0.0000) / (0.0000) down (0.0001) key (0.0001) : (0.0002) no. (0.0002) time (-0.0000) / (0.0002) date (-0.0000) : (0.0002) yes. (0.0003) ribbon (-0.0000) / (0.0001) roller (0.0001) printer (-0.0001) : (0.0001) roller. (0.0001) replacement (0.0001) roll (0.0001) paper (0.0002) : (0.0000) unv35720. (0.0001) pre (0.0002) consumer (-0.0002) recycled (-0.0001) content (0.0001) percent (-0.0000) : (0.0002) 0 (0.0000) pct. (0.0001) fraction (0.0000) / (0.0001) decimal (-0.0001) conversions (0.0001) : (0.0001) no. (0.0001) fraction (0.0003) calculations (0.0002) : (0.0001) no. (0.0002) power (0.0000) source (0.0001) ( (0.0009) s (0.0000) ) (0.0000) : (0.0002) ac, (0.0000) battery. (0.0001) percent (-0.0002) key (0.0001) ( (0.0001) s (0.0001) ) (-0.0001) : (0.0001) no. (0.0000) global (-0.0000) product (0.0002) type (0.0001) : (0.0000) calculators (0.0001) printing. (0.0001) calculator (0.0001) type (0.0001) : (-0.0001) printing. (-0.0001) total (0.0001) recycled (-0.0001) content (0.0001) percent (-0.0000) : (0.0001) 0 (-0.0000) pct. (0.0001) size (0.0001) : (-0.0000) 6 (0.0001) 2 (0.0001) / (0.0000) 5w (0.0000) x (0.0001) 9 (0.0001) 1 (0.0001) / (0.0000) 10d. (0.0000) display (0.0002) notation (-0.0001) : (-0.0000) numeric. (0.0001) number (0.0000) of (-0.0001) display (0.0000) digits (0.0001) : (-0.0000) 12. (-0.0000) replacement (-0.0000) batteries (-0.0000) : (0.0001) 4 (0.0000) aa, (0.0001) evee91bp4. (0.0001) tax (-0.0000) calculation (-0.0001) : (0.0003) yes. (0.0001) decimal (0.0000) function (0.0004) : (0.0001) yes. (0.0001) + (-0.0001) / (-0.0001) switch (0.0002) key (0.0000) : (0.0000) yes. (0.0001) display (-0.0000) characters (-0.0001) height (-0.0001) : (-0.0001) 18. (0.0000) 0 (0.0001) mm. (0.0001) post (0.0002) consumer (0.0000) recycled (-0.0000) content (-0.0001) percent (-0.0004) : (0.0002) 0 (0.0000) pct. (0.0002) item (0.0003) count (-0.0001) function (-0.0002) : (0.0000) yes. (0.0000) print (0.0000) color (-0.0000) ( (0.0001) s (0.0001) ) (0.0001) : (0.0001) purple, (0.0001) red. (0.0001) display (0.0002) angle (0.0001) : (0.0000) fixed. (0.0002) double (0.0000) zero (0.0001) key (0.0001) : (0.0001) yes. (0.0002) grand (0.0002) total (-0.0001) key (0.0001) : (0.0000) no. (0.0001) replacement (0.0001) ribbon (-0.0001) / (-0.0000) roller (0.0002) : (0.0000) nuknr42. (0.0001) print (0.0000) speed (-0.0001) ( (0.0000) lines (-0.0001) per (0.0002) second (0.0002) ) (0.0002) : (0.0002) 2. (-0.0001) 0. (0.0002) display (-0.0001) types (0.0009)
~~~~~~

**Node-2.3** (global 1878):

~~~~~~text
product (-0.0018) from (0.0006) amazon (0.0034) platform (-0.0016) with (0.0022) title (0.0051) and (0.0009) content (0.0012) : (0.0021) title (0.0025) : (0.0001) calculator (0.0008) plain (0.0021) paper. (0.0030) content (-0.0006) : (0.0021) universal (0.0001) office (0.0014) products (-0.0020) calculator (0.0024) plain (0.0023) paper (0.0030) 35720 (0.0058) printing (0.0072) media (0.0025)
~~~~~~

**Node-2.4** (global 14185):

~~~~~~text
product (0.0005) from (-0.0002) amazon (0.0021) platform (-0.0001) with (-0.0000) title (0.0015) and (-0.0004) content (0.0011) : (0.0004) title (0.0021) : (0.0002) hp (-0.0005) 05a (0.0007) black (0.0006) original (-0.0001) laserjet (0.0010) toner (0.0008) cartridge. (0.0028) content (0.0018) : (-0.0002) hp (0.0007) 05a (0.0003) black (0.0008) original (0.0007) laserjet (0.0017) toner (0.0010) cartridge (-0.0001)
~~~~~~

**Node-2.5** (global 14186):

~~~~~~text
product (-0.0006) from (-0.0001) amazon (0.0012) platform (-0.0000) with (0.0000) title (0.0004) and (0.0001) content (0.0001) : (0.0005) title (0.0001) : (0.0003) pm (0.0001) company (-0.0002) perfection (0.0012) pos (-0.0000) / (-0.0001) calculator (-0.0001) rolls, (-0.0001) 2. (0.0001) 25 (-0.0000) inches (-0.0003) x (-0.0001) 150 (-0.0000) feet, (-0.0001) white, (-0.0000) 12 (-0.0001) / (-0.0001) pack (-0.0001) ( (0.0005) 08835 (0.0000) ). (0.0001) content (0.0004) : (-0.0001) sold (0.0003) as (0.0002) a (-0.0000) pack (0.0000) of (0.0001) 12 (0.0000) pos (0.0002) / (-0.0001) calculator (0.0001) / (-0.0002) add (0.0000) rolls. (0.0001) 2 (-0.0001) 1 (-0.0001) / (-0.0001) 4 (0.0000) inches (0.0001) x (0.0002) 150 (-0.0002) feet (0.0002) top (0.0001) quality, (0.0000) white, (0.0002) lint- (-0.0001) free (0.0005) rolls (0.0000) for (0.0003) use (0.0002) in (0.0002) plain (0.0004) paper (0.0003) calculators (0.0002) and (0.0002) adding (0.0004) machines. (0.0009) each (0.0003) roll (0.0005) has (0.0005) a (0.0003) convenient (0.0006) end (-0.0001) of (0.0002) roll (0.0002) warning (0.0006) stripe. (-0.0003) all (0.0001) rolls (0.0009) converted (0.0008) in (0.0005) the (-0.0001) united (-0.0001) states. (-0.0003)
~~~~~~

**Node-3** (global 1907):

~~~~~~text
product (0.0129) from (0.0039) amazon (-0.0063) platform (0.0027) with (0.0077) title (0.0051) and (-0.0013) content (-0.0223) : (0.0046) title (0.0149) : (0.0154) new (0.0049) compatible (0.0069) nukote (0.0049) br80c (0.0079) calculator (0.0099) ribbon (0.0128) black (-0.0039) / (0.0038) red (0.0029) ( (0.0066) 2- (0.0037) pack (0.0019) ) (0.0051) for (-0.0069) canon (-0.0196) mp- (0.0012) 11 (0.0038) dx. (0.0121) content (0.0051) : (0.0075) new (0.0069) compatible (-0.0014) nukote (0.0077) br80c (0.0090) univeral (0.0109) calculator (0.0092) ribbon (0.0165) spool (0.0115) black (0.0040) / (0.0008) red (0.0074) nylon (0.0032) 1 (0.0068) / (0.0076) 2 (0.0060) in. (0.0024) x (0.0077) 21 (0.0068) ft. (0.0048) ( (0.0102) 2 (0.0078) per (-0.0008) pack (-0.0011) ) (-0.0090) for (0.0054) canon (0.0020) mp- (0.0060) 11 (0.0034) dx (0.0143)
~~~~~~

**Node-3.1** (global 156):

~~~~~~text
product (-0.0000) from (-0.0005) amazon (-0.0001) platform (-0.0004) with (-0.0005) title (-0.0000) and (-0.0001) content (-0.0000) : (0.0000) title (0.0001) : (0.0000) 6 (0.0001) pk (0.0000) calculator (-0.0001) ink (-0.0003) rollers, (-0.0001) ir- (0.0002) 40t (-0.0000) / (-0.0002) canon (-0.0000) cp13 (-0.0001) / (-0.0001) nu- (0.0001) kote (-0.0000) nr42 (-0.0002) / (-0.0000) nr422 (-0.0001) for (-0.0005) various (-0.0001) sharp, (0.0001) victor, (0.0001) adler- (0.0001) royal, (-0.0001) canon, (-0.0000) casio, (0.0000) aurora, (-0.0004) citizen, (0.0001) olivetti, (0.0000) texas (0.0002) instruments (-0.0003) calculators. (0.0001) content (-0.0000) : (0.0002) compatible (0.0000) seiko (-0.0000) ir- (0.0001) 40t (0.0003) black (0.0001) / (-0.0001) red (0.0000) ink (-0.0002) rollersthe (0.0001) ir- (0.0000) 40t (0.0002) is (-0.0000) also (0.0004) known (0.0007) as (0.0000) the (0.0007) following (-0.0001) part (0.0001) numbers (-0.0001) : (0.0004) adler- (-0.0001) royal (0.0001) 906042 (-0.0008) best (-0.0009) ribbon (-0.0003) corp (-0.0007) 200040 (0.0002) bushnell (-0.0001) ribbon (-0.0002) corp (-0.0002) ir40t (0.0000) california (-0.0001) ribbon (0.0000) ir40tb (0.0001) / (0.0000) r (0.0002) canon (-0.0000) cp13 (0.0002) carma (0.0000) no- (0.0001) uk (0.0001) 9851 (-0.0001) casio (-0.0001) ad4150 (-0.0000) commander (-0.0001) imaging (-0.0001) prod (0.0000) 130 (0.0000) dataproducts (0.0000) llc (-0.0001) e1427 (0.0001) din (-0.0001) group (0.0001) no- (0.0001) germany (-0.0001) 745 (0.0000) distinguished (0.0003) brands (0.0001) 430 (-0.0001) fine (0.0001) line (0.0000) ribbon (0.0000) corp (-0.0003) rr13 (-0.0002) grc (-0.0000) / (-0.0001) monroe (0.0000) r842irbr (-0.0000) ko- (0.0001) rec- (0.0001) type (-0.0000) ir40t (0.0000) marathon (-0.0004) ribbon (-0.0002) corp (0.0001) 390600 (0.0001) nashua (-0.0001) imaging (-0.0000) 20123 (0.0001) ncr (0.0001) 151755 (0.0000) nu- (0.0001) kote (0.0001) intl. (0.0000) nr42 (0.0001) nu- (0.0001) kote (0.0001) intl. (0.0001) nr422 (0.0000) olivetti (0.0001) 75142 (0.0001) olympia (-0.0001) 82154 (0.0001) olympia (-0.0000) ir123 (0.0001) pelikan (0.0001) z380 (0.0001) performance (0.0001) plus (0.0001) 70125 (0.0000) porelon (0.0001) 11203 (0.0001) porelon (0.0001) 11204 (0.0000) porelon (0.0001) 478 (0.0001) porelon (0.0001) pr42 (0.0001) radio (-0.0001) shack (-0.0001) rd0281 (0.0001) royal (0.0001) 13110 (-0.0000) seiko (-0.0000) ir40t (0.0001) sharp (0.0003) ea772r (0.0001) victor (0.0000) 10738001 (0.0001) viking (0.0000) vpr42 (0.0001) printers (0.0001) use (0.0006) the (0.0011) ir- (0.0002) 40tadler (0.0000) 4212 (0.0001) adler (0.0001) 4212pd (0.0001) adler (-0.0001) 4212pdcarat (0.0001) adler (-0.0003) 4212pdnova (0.0001) adler- (0.0000) royal (-0.0004) 906042 (-0.0003) allen (-0.0002) r (-0.0000) c (-0.0000) 7 (0.0000) aurora (-0.0002) 14pd (-0.0000) aurora (-0.0002) 87pd (-0.0001) aurora (-0.0001) pr190 (0.0002) best (-0.0002) ribbon (-0.0001) corp (-0.0000) 200040 (0.0001) bushnell (0.0001) ribbon (-0.0001) corp (-0.0001) ir40t (0.0002) california (0.0001) ribbon (0.0000) ir40tb (0.0002) / (-0.0002) r (0.0002) canon (-0.0000) cp13 (0.0000) canon (-0.0001) mp120dh (0.0001) canon (-0.0000) mp120dl (0.0000) canon (0.0000) mp120dle (0.0001) canon (0.0000) mp12d (0.0002) canon (-0.0000)
~~~~~~

**Node-3.2** (global 1904):

~~~~~~text
product (-0.0005) from (-0.0007) amazon (0.0002) platform (-0.0009) with (-0.0008) title (-0.0001) and (-0.0011) content (0.0006) : (0.0001) title (0.0008) : (-0.0004) compatible (0.0006) universal (-0.0001) calculator (0.0004) spool (-0.0001) epc (0.0002) b (-0.0001) / (0.0003) r (-0.0000) black (-0.0000) and (-0.0004) red (0.0001) ribbons, (0.0003) works (-0.0001) for (-0.0003) casio (-0.0000) dr (0.0000) 210 (-0.0001) hd, (0.0001) casio (0.0001) dr (0.0001) 210 (0.0001) ht, (-0.0000) casio (0.0001) dr (0.0000) 210 (-0.0000) tm, (-0.0000) casio (0.0001) dr (-0.0010) 220. (0.0016) content (0.0007) : (-0.0011) share (0.0003) your (-0.0006) own (0.0002) related (0.0004) images (0.0004) compatible (-0.0001) universal (0.0001) calculator (0.0004) spool (0.0000) epc (0.0002) b (-0.0001) / (0.0001) r (0.0002) black (0.0001) and (-0.0007) red (0.0003) ribbons, (0.0003) works (0.0001) for (-0.0004) casio (0.0000) dr (0.0002) 210 (0.0001) hd, (0.0001) casio (0.0002) dr (0.0001) 210 (0.0003) ht, (0.0001) casio (0.0003) dr (-0.0004) 210 (0.0004) tm, (0.0003) casio (0.0008) dr (-0.0001) 220 (0.0074)
~~~~~~

**Node-3.3** (global 14255):

~~~~~~text
product (0.0003) from (-0.0002) amazon (0.0003) platform (-0.0005) with (-0.0000) title (0.0006) and (0.0004) content (-0.0006) : (0.0003) title (0.0001) : (0.0001) acco (0.0000) economy (0.0005) jumbo (-0.0001) paper (-0.0002) clips, (0.0000) smooth, (0.0001) jumbo, (0.0002) 100 (0.0004) / (-0.0002) box, (0.0003) 10 (0.0005) boxes (0.0004) ( (0.0004) 72580 (0.0004) ). (0.0006) content (-0.0003) : (0.0001) standard (0.0003) wire (0.0002) construction (0.0005) jumbo (0.0001) paper (0.0002) clips (-0.0001) hold (-0.0001) 20 (0.0001) sheets, (0.0003) that (0.0003) is (0.0005) twice (0.0004) as (0.0005) much (0.0003) as (0.0004) standard (0.0002) size (0.0002) clips, (-0.0004) are (0.0003) still (0.0003) offered (0.0005) at (0.0004) a (-0.0003) great (0.0002) price. (0.0003) great (-0.0004) for (0.0001) big (0.0002) projects (0.0002) and (0.0000) available (0.0002) in (-0.0000) smooth (0.0000) or (0.0004) with (0.0002) non- (0.0001) skid (0.0001) ridged (0.0000) wire (0.0003) to (0.0003) further (0.0000) eliminate (0.0007) risk (0.0003) of (0.0004) slipping. (-0.0001) silver (-0.0001) finish, (-0.0000) 100 (0.0002) paper (-0.0004) clips (-0.0004) per (0.0003) box. (0.0006)
~~~~~~

**Node-3.4** (global 14550):

~~~~~~text
product (0.0011) from (0.0005) amazon (-0.0007) platform (0.0003) with (0.0007) title (0.0006) and (-0.0003) content (-0.0020) : (0.0003) title (0.0016) : (0.0015) new (0.0005) compatible (0.0006) nukote (0.0005) br80c (0.0008) calculator (0.0009) ribbon (0.0012) black (-0.0003) / (0.0004) red (0.0001) ( (0.0007) 6- (0.0005) pack (-0.0000) ) (0.0004) for (-0.0005) canon (-0.0018) mp- (0.0001) 11 (0.0003) dx. (0.0013) content (0.0005) : (0.0007) new (0.0007) compatible (-0.0002) nukote (0.0008) br80c (0.0009) univeral (0.0011) calculator (0.0009) ribbon (0.0016) spool (0.0011) black (0.0004) / (0.0001) red (0.0007) nylon (0.0003) 1 (0.0005) / (0.0008) 2 (0.0005) in. (0.0005) x (0.0006) 21 (0.0006) ft. (0.0005) ( (0.0007) 6 (0.0006) per (-0.0000) pack (-0.0000) ) (-0.0008) for (0.0005) canon (0.0001) mp- (0.0005) 11 (0.0002) dx (0.0012)
~~~~~~

**Node-3.5** (global 14551):

~~~~~~text
product (-0.0000) from (0.0002) amazon (-0.0004) platform (0.0002) with (0.0000) title (0.0003) and (-0.0002) content (0.0000) : (0.0002) title (-0.0000) : (0.0002) columbian (0.0001) co790 (0.0001) 9x12- (0.0000) inch (0.0001) clasp (-0.0001) brown (-0.0000) kraft (-0.0001) envelopes, (-0.0000) 100 (-0.0001) count. (0.0005) content (-0.0001) : (0.0000) a (0.0000) durable (-0.0001) multi- (0.0001) purpose (0.0001) envelope. (0.0002) dual (0.0001) purpose (0.0000) seal (-0.0001) allows (-0.0001) for (-0.0002) multiple (0.0002) uses. (-0.0000) use (0.0000) the (0.0002) moisture (-0.0001) activated (0.0001) gummed (0.0000) seal (-0.0000) for (0.0002) mailing (0.0001) or (-0.0000) the (0.0000) strong (0.0001) metal (0.0002) clasp (-0.0001) for (0.0000) repeated (0.0002) use (0.0001) and (0.0000) storage (0.0001) purposes. (-0.0001) features (0.0003) : (0.0002) extra (-0.0002) heavy- (0.0000) duty (0.0000) opaque (-0.0000) 32lb (-0.0000) brown (-0.0001) kraft (-0.0002) material (0.0003) provides (0.0002) privacy (0.0002) of (-0.0000) contents. (0.0003) open (-0.0001) end (-0.0001) closure. (0.0002) sized (0.0002) : (0.0001) 9 (-0.0000) " (-0.0001) x (0.0001) 12 (-0.0001) ". (-0.0000) quantity (0.0007) = (0.0000) 100 (-0.0004) envelopes. (-0.0000)
~~~~~~

**Node-4** (global 6192):

~~~~~~text
product (-0.0013) from (-0.0034) amazon (0.0017) platform (-0.0013) with (-0.0002) title (0.0029) and (-0.0002) content (0.0005) : (0.0004) title (-0.0015) : (-0.0006) centon (0.0011) dsp4gb10pk (0.0014) & (0.0013) nbsp (0.0010) ; (0.0006) 10 (0.0035) x (-0.0034) 4gb (0.0001) multi- (0.0047) pack (0.0032) pro (0.0066) usb (0.0002) flash (0.0027) drive (-0.0004) ( (0.0031) grey (0.0026) ). (0.0008) content (-0.0031) : (0.0003) centon (0.0014) ' (-0.0022) s (0.0023) datastick (-0.0044) pro (0.0109) is (0.0017) made (0.0020) with (-0.0009) a (-0.0075) sturdy (0.0010) aluminum (-0.0019) casing (0.0033) and (0.0008) is (0.0017) available (0.0000) in (-0.0017) multiple (0.0037) colors (0.0010) and (0.0015) a (-0.0111) full (0.0028) range (0.0017) of (-0.0007) capacities. (0.0042) this (0.0049) affordable (0.0013) drive (0.0029) is (0.0035) ideal (-0.0026) for (0.0034) personal (-0.0007) use, (0.0029) small (0.0054) business (0.0049) and (-0.0028) schools. (0.0020) usb (0.0018) datastick (0.0050) pro (-0.0043) line (0.0014) is (0.0021) reliable (0.0045) and (-0.0000) affordableproduct (0.0022) featuresdurable (0.0045) brushed (0.0091) aluminum (0.0070) casingled (0.0091) indicator (0.0052) lightlanyard (0.0039) / (0.0036) keychain (0.0040) connectorspecspart (0.0031) number (0.0023) : (0.0019) dsp4gb10pkupc (0.0018) : (0.0038) 731969300855dimensions (0.0009) : (0.0017) h (0.0017) 4. (0.0025) 00 (0.0008) x (0.0004) w (0.0018) 6. (0.0021) 75 (0.0003) x (-0.0010) d (0.0012) 1. (0.0013) 25weight (0.0059) : (0.0002) 0. (0.0019) 300color (0.0027) : (0.0002) greywarranty (0.0017) : (0.0036) lifetimehow (-0.0003) much (0.0051) can (-0.0002) i (-0.0065) store (-0.0057) on (-0.0029) my (0.0052) 4gb (-0.0002) datastick (0.0045) pro (-0.0009) usb (0.0003) flash (0.0069) drive? (0.0023) photos (0.0037) * (0.0015) 6 (0.0070) megapixel14607 (0.0007) megapixel13008 (0.0010) megapixel116010 (0.0004) megapixel88012 (0.0004) megapixel680songs (0.0005) ( (-0.0009) 4 (0.0008) minutes (0.0006) ) (-0.0004) * (0.0026) 128 (-0.0015) kbps (0.0007) ( (0.0028) better (0.0002) than (-0.0037) fm (-0.0086) ) (-0.0021) 960video (-0.0021) * (0.0036) standard (0.0003) sp (0.0037) mpeg2 (-0.0057) ( (0.0009) 6 (0.0004) mbps (-0.0009) ) (-0.0046) 82hd (-0.0010) standard (0.0043) avchd (0.0005) / (0.0013) h. (0.0018) 264 (-0.0009) ( (-0.0025) 9mbps (0.0007) ) (0.0022) 60voice (0.0006) recording (-0.0052) * (0.0024) 32k (0.0011) wav (0.0018) ( (0.0002) voice (-0.0018) quality (0.0032) ) (0.0027) 17536 (0.0037) * (0.0081) number (0.0019) of (-0.0044) photos, (-0.0057) songs, (-0.0060) and (-0.0000) minutes (0.0023) will (0.0089) vary (0.0011) depending (-0.0050) on (0.0027) formatted (-0.0005) capacity, (0.0025) device (-0.0016) model, (0.0004) format (-0.0003) resolution, (0.0003) type (0.0047) of (0.0007) compression (-0.0003) and (-0.0010) pre- (0.0042) loaded (0.0103) software. (-0.0238) included (0.0135) accessories10 (0.0270) x (0.0049) 4gb (0.0033) usb (-0.0060) flash (0.0079) drive (-0.0002)
~~~~~~

**Node-4.1** (global 713):

~~~~~~text
product (0.0016) from (-0.0006) amazon (0.0018) platform (-0.0008) with (-0.0001) title (0.0002) and (0.0006) content (0.0008) : (0.0019) title (0.0002) : (0.0009) case (0.0004) logic (0.0023) vna- (0.0003) 216 (-0.0001) 16- (-0.0004) inch (0.0002) laptop (0.0008) attache (0.0026) ( (0.0023) black (-0.0001) ). (-0.0020) content (0.0010) : (-0.0005) none (0.0002)
~~~~~~

**Node-4.2** (global 14001):

~~~~~~text
product (-0.0001) from (-0.0002) amazon (-0.0004) platform (-0.0003) with (-0.0002) title (-0.0001) and (0.0005) content (-0.0001) : (-0.0006) title (0.0001) : (-0.0009) sandisk (0.0003) cruzer (0.0005) blade (-0.0002) 4gb (0.0001) ( (0.0005) 10 (0.0002) pack (-0.0002) ) (0.0002) usb (-0.0007) 2. (0.0003) 0 (-0.0000) flash (0.0000) drive (0.0001) jump (0.0001) drive (0.0003) thumb (-0.0003) drive (0.0001) sdcz50- (-0.0000) 004g- (0.0000) 10pk (0.0001) w (0.0002) / (0.0001) ( (0.0003) 5 (0.0002) ) (0.0001) everything (0.0001) but (0.0001) stromboli (0.0001) ( (0.0002) tm (0.0001) ) (0.0001) lanyard. (0.0003) content (0.0001) : (0.0001) from (-0.0002) the (0.0004) manufacturer? (-0.0005) with (-0.0003) usb (-0.0005) ports (-0.0003) popping (-0.0003) up (-0.0000) everywhere (-0.0004) you (0.0001) look, (0.0000) you (-0.0002) need (0.0001) a (0.0004) simple (0.0001) and (0.0002) reliable (-0.0001) way (-0.0001) to (0.0001) store (-0.0000) and (0.0001) share (0.0002) your (0.0001) photos, (0.0000) videos (-0.0001) and (0.0001) music (0.0003) on (-0.0001) the (0.0003) fly. (-0.0000) the (0.0001) sandisk (0.0003) cruzer (0.0012) usb (-0.0010) flash (0.0000) drive (0.0001) is (0.0005) your (0.0003) answer. (-0.0005) because (0.0000) it (0.0002) works (0.0005) with (-0.0000) virtually (-0.0003) any (0.0000) computer (0.0001) or (-0.0001) electronic (0.0001) device (-0.0002) with (-0.0001) a (0.0005) usb (-0.0006) slot, (0.0002) this (0.0007) flash (-0.0001) drive (0.0003) lets (-0.0000) you (0.0004) leave (0.0000) your (-0.0001) laptop (-0.0005) at (-0.0003) home (-0.0000) but (0.0003) still (-0.0001) take (-0.0001) your (-0.0003) vast (-0.0001) amounts (-0.0002) of (0.0000) content (-0.0001) with (-0.0002) you (-0.0001) to (0.0001) share (0.0000) with (-0.0002) family (0.0000) and (0.0002) friends. (0.0002) whether (0.0001) you (0.0000) need (-0.0001) to (0.0002) transport (0.0000) your (-0.0002) latest (-0.0001) mp3 (-0.0009) downloads, (-0.0003) vacation (0.0002) videos, (-0.0001) or (0.0004) your (-0.0001) college (-0.0000) thesis, (0.0000) the (0.0006) sandisk (0.0001) cruzer (-0.0001) usb (-0.0004) flash (0.0001) drive (0.0002) offers (-0.0001) portable (-0.0001) storage (0.0001) that (0.0001) you (0.0001) can (0.0001) trust. (0.0005) convenient (-0.0001) storage (0.0001) and (0.0001) portability (-0.0001) with (-0.0003) usb (-0.0003) ports (-0.0001) on (-0.0002) computers, (-0.0001) to (0.0002) new (0.0001) ports (-0.0002) popping (-0.0001) up (0.0001) on (-0.0003) cars, (-0.0002) dvd (-0.0005) players, (0.0001) tvs, (0.0001) photo (0.0000) frames, (0.0000) and (0.0002) more, (-0.0000) the (0.0003) need (-0.0000) for (-0.0001) a (0.0002) fast (0.0001) and (0.0002) reliable (0.0000) way (-0.0002) to (0.0002) share (-0.0000) your (-0.0002) digital (0.0001) content (-0.0001) on (-0.0001) a (0.0001) moment (-0.0000) ' (-0.0001) s (0.0003) notice (0.0001) is (0.0000) greater (0.0001) than (-0.0004) ever. (0.0002) the (0.0003) sandisk (0.0000) cruzer (0.0001) usb (-0.0006) flash (-0.0000) drive (0.0001) meets (-0.0001) that (0.0002) need. (-0.0001) this (0.0004) reliable (0.0001) flash (0.0001) drive (0.0001) fits (0.0001) in (-0.0001) the (0.0002) palm (0.0002) of (-0.0000) your (-0.0001) hand (0.0002) and (0.0001) gives (-0.0002) you (-0.0000) the (0.0003) storage (-0.0000) capacity (0.0002) you (0.0001) need (0.0000) to (0.0002) store (-0.0004) and (0.0000) transfer (0.0001) up (0.0001) to (0.0002) 4 (0.0002) gb (-0.0001) of (-0.0003) data. (0.0001) while (-0.0001) the (0.0004) drive (0.0000) is (0.0002) optimized (0.0001) for (0.0005) laptops (-0.0001) and (-0.0001) devices (-0.0004) with (-0.0002) usb (-0.0005) 2. (0.0003) 0 (0.0001) port, (0.0000) it (0.0001) is (0.0002) backwards (-0.0000) compatible (-0.0004) with (-0.0001) older (0.0001) devices (-0.0004) that (0.0000) have (0.0001) usb (-0.0006) 1. (0.0004) 1 (0.0001) ports, (0.0000) so (0.0000) you (0.0002) can (0.0000) be (0.0005) assured (-0.0002) of (-0.0005) near (-0.0000) universal (0.0001) compatibility. (-0.0002) view (0.0002) videos (-0.0001) without (-0.0001) extra (0.0001) software (0.0003) or (-0.0002) setup (-0.0003) with (0.0002) the (0.0001) sandisk (0.0006) cruzer (0.0003) usb (-0.0008) flash (-0.0001) drive, (-0.0002) you (-0.0000) can (0.0001) transfer (0.0003) your (-0.0001) favorite (0.0001) video (0.0001) from (0.0000) one (0.0001) device (-0.0000) to (0.0002) another (0.0001) easily (0.0001) and (0.0001) conveniently, (0.0000) without (-0.0004) any (0.0002) additional (-0.0001) software (-0.0004) or (-0.0000) setup. (-0.0004) the (0.0009) drive (0.0000) offers (0.0001) drag- (0.0004) and- (0.0002) drop (0.0002) convenience, (-0.0002) which (-0.0002) means (-0.0001) you (-0.0000) can (0.0003) simply (-0.0001) drag (0.0005)
~~~~~~

**Node-4.3** (global 29325):

~~~~~~text
product (0.0029) from (-0.0013) amazon (0.0005) platform (-0.0019) with (-0.0011) title (-0.0010) and (-0.0005) content (-0.0001) : (-0.0001) title (-0.0014) : (-0.0006) logitech (0.0002) mk710 (0.0001) wireless (0.0005) desktop (0.0008) mouse (0.0003) and (-0.0014) keyboard (0.0013) combo. (0.0001) content (-0.0004) : (-0.0007) none (-0.0006)
~~~~~~

**Node-4.4** (global 29326):

~~~~~~text
product (0.0000) from (-0.0003) amazon (-0.0009) platform (-0.0004) with (-0.0013) title (0.0007) and (-0.0004) content (0.0002) : (0.0004) title (0.0000) : (0.0002) endust (-0.0006) multi- (-0.0000) surface (0.0000) electronics (-0.0006) anti- (0.0002) static (0.0011) cleaner- (0.0001) 12 (0.0010) pack (-0.0003) ( (0.0010) 096000p12 (-0.0002) ). (-0.0017) content (0.0007) : (0.0008) endust (-0.0012) for (0.0002) electronics (0.0002) multi- (0.0003) surface (-0.0000) anti- (0.0002) static (0.0004) screen (-0.0004) and (0.0001) electronics (-0.0005) cleaner. (0.0004) trusted (0.0012) endust (0.0003) brand (-0.0005) cleans (0.0002) virtually (0.0000) every (-0.0001) surface (0.0003) in (0.0000) your (0.0003) office (0.0010) including (-0.0010) all (-0.0000) types (0.0006) of (-0.0002) screens. (0.0008) picks (0.0004) up (-0.0002) dust (0.0007) and (-0.0002) gently (0.0012) cleans (0.0004) away (0.0005) fingerprints. (-0.0001) helps (0.0003) prevent (0.0004) build- (-0.0002) up (0.0001) of (-0.0003) static (0.0011) charges. (-0.0014) ultimate (0.0011) cleaner (0.0003) makes (0.0004) it (0.0010) easy (0.0002) to (0.0003) go (0.0010) from (0.0004) cleaning (0.0004) your (0.0010) screen, (0.0007) keyboard, (0.0003) desk, (0.0001) phone, (0.0005) smart- (0.0003) phone, (0.0004) copier, (0.0002) fax, (0.0001) to (0.0005) printer (-0.0000) and (0.0004) more. (0.0002) new (0.0004) alcohol, (0.0006) wax, (0.0006) oil, (0.0004) residue, (0.0004) and (0.0004) ammonia- (0.0001) free (-0.0001) formula (0.0001) is (0.0002) streak- (0.0001) free (0.0003) and (0.0005) anti- (-0.0002) static. (0.0003) aerosol (0.0005) makes (-0.0001) cleaning (-0.0013) and (-0.0001) dusting (0.0002) easier (-0.0003) than (0.0006) ever. (0.0008) stays (0.0004) where (0.0001) you (0.0000) spray (0.0002) it (0.0002) ( (0.0004) won (-0.0003) ' (-0.0002) t (0.0001) run (0.0004) ). (0.0002) so (0.0003) you (0.0002) can (0.0002) clean (0.0004) where (0.0001) you (0.0003) want (0.0003) when (0.0002) you (0.0005) want. (0.0013) the (-0.0014) only (0.0008) aerosol (0.0003) anti- (0.0007) static (0.0011) cleaner (0.0003) that (0.0002) repels (0.0007) dust (0.0009) once (0.0002) applied (0.0006) and (0.0002) helps (0.0004) keep (-0.0000) your (0.0001) screens (0.0005) and (0.0007) equipment (-0.0004) dust (0.0005) and (0.0012) static (0.0014) free. (0.0006) made (0.0019) in (-0.0008) the (-0.0011) usa. (0.0009)
~~~~~~

**Node-5** (global 14323):

~~~~~~text
product (-0.0028) from (-0.0041) amazon (0.0035) platform (-0.0045) with (-0.0114) title (0.0025) and (-0.0079) content (-0.0041) : (0.0017) title (0.0014) : (-0.0004) v4ink (0.0011) & (0.0037) # (0.0036) 65533 (0.0017) ; (0.0172) new (0.0008) compatible (-0.0033) hp (-0.0004) 131a (0.0032) toner (-0.0026) cartridge- (0.0040) black (0.0007) ( (0.0069) cf210a (0.0026) ) (0.0064) for (0.0028) hp (0.0007) laserjet (0.0048) pro (0.0011) m251 (0.0052) m276 (0.0041) toner (0.0048) printers. (0.0182) content (-0.0066) : (0.0015) v4ink (0.0047) & (0.0065) # (0.0060) xfffd (0.0017) ; (0.0095) new (0.0005) compatible (-0.0014) hp (0.0033) 131a (0.0012) toner (0.0023) cartridge- (0.0036) black (0.0005) ( (0.0010) cf210a (-0.0019) ) (-0.0015) for (-0.0072) hp (0.0022) laserjet (0.0090) pro (0.0022) m251 (0.0070) m276 (0.0054) toner (0.0039) printers (0.0189)
~~~~~~

**Node-6** (global 14324):

~~~~~~text
product (-0.0013) from (-0.0089) amazon (0.0032) platform (-0.0000) with (-0.0021) title (0.0041) and (0.0012) content (0.0025) : (0.0031) title (0.0033) : (0.0070) alliance (0.0022) sterling (0.0002) ergonomically (0.0008) correct (-0.0026) rubber (0.0023) bands, (-0.0000) # (-0.0004) 105, (0.0001) 0. (0.0017) 625 (-0.0007) x (0.0012) 5 (0.0007) inches, (0.0009) 70 (0.0013) per (0.0018) 1lb (-0.0000) box (0.0020) ( (0.0038) 25055 (0.0029) ). (0.0005) content (0.0022) : (0.0021) the (-0.0012) best (-0.0011) value (0.0020) per (0.0001) rubber (0.0054) band. (-0.0005) sterling (0.0029) bands (-0.0009) have (0.0006) a (0.0010) high (-0.0000) percentage (0.0018) of (0.0008) rubber (0.0005) content (0.0013) and (0.0021) an (0.0014) excellent (0.0011) count (0.0010) per (0.0012) pound. (0.0041) long (-0.0009) regarded (0.0018) as (0.0017) an (0.0008) ergonomically (0.0012) correct (0.0014) band (0.0006) due (0.0011) to (0.0011) its (0.0011) high (-0.0001) rubber (0.0011) content (0.0044) and (0.0024) inherent (0.0054) soft (-0.0020) stretch (-0.0018) compared (0.0008) to (0.0025) standard (0.0042) industrial (0.0029) grade (0.0003) bands, (0.0096) sterling (0.0018) bands (0.0017) are (0.0018) highly (0.0015) recommended (0.0005) for (0.0021) fast (0.0021) application (0.0067) and (0.0016) repeat (0.0056) use. (-0.0053) packed (0.0103) in (0.0041) a (0.0006) 1 (0.0028) lb (0.0041) box. (-0.0026) made (0.0030) in (0.0038) the (0.0104) u. (0.0023) s. (-0.0146) a. (-0.0172)
~~~~~~

**Node-7** (global 14325):

~~~~~~text
product (-0.0024) from (-0.0031) amazon (-0.0014) platform (-0.0323) with (-0.0260) title (0.0200) and (0.0020) content (-0.0494) : (0.0287) title (-0.0054) : (-0.0117) quartet (0.0431) prestige (-0.0096) colored (-0.0088) cork (0.0193) bulletin (0.0250) board, (-0.0122) 3 (0.0004) x (0.0000) 2 (0.0036) feet, (0.0104) graphite (0.0133) finish (0.0075) frame (-0.0000) ( (-0.0010) b243g (0.0064) ). (-0.0372) content (0.0114) : (-0.0051) none (-0.0339)
~~~~~~

**Node-8** (global 14326):

~~~~~~text
product (0.0009) from (0.0016) amazon (-0.0016) platform (-0.0008) with (0.0009) title (0.0007) and (-0.0005) content (-0.0000) : (0.0014) title (0.0010) : (0.0012) tops (0.0008) spiral (0.0005) steno (0.0006) books, (0.0008) 6 (0.0000) x (-0.0000) 9 (0.0003) inches, (0.0016) gregg (0.0001) rule, (0.0016) white (-0.0000) paper, (0.0008) assorted (0.0003) covers, (0.0003) 80 (0.0004) sheets (-0.0001) per (-0.0003) book, (0.0007) 4 (0.0004) books (0.0008) per (0.0003) pack (-0.0003) ( (0.0010) 80220 (0.0009) ). (-0.0009) content (0.0009) : (0.0026) since (0.0014) 1952, (0.0017) tops (-0.0006) has (0.0004) provided (0.0004) quality (-0.0014) products (-0.0007) and (0.0016) services (0.0005) to (0.0008) businesses (0.0007) throughout (0.0015) the (0.0011) world. (0.0050) tops (-0.0008) continues (-0.0009) that (0.0001) commitment (0.0004) providing (0.0004) innovative, (0.0012) high (0.0007) quality (-0.0004) value- (0.0009) added (0.0001) paper (-0.0003) products (-0.0010) for (0.0015) the (0.0019) office, (0.0014) school (-0.0032) and (0.0010) home. (0.0021) tops (0.0011) steno (0.0005) books (0.0016) feature (0.0003) precisely (0.0021) printed (0.0009) gregg (0.0033) rulings (0.0012) for (-0.0003) guidance (0.0016) and (0.0007) shorthand (0.0007) style (0.0018) preference. (-0.0020) the (0.0016) margin (-0.0038) line (-0.0013) creates (0.0032) two (-0.0007) columns (0.0009) for (0.0003) notes, (0.0009) while (-0.0008) a (0.0002) snag- (0.0012) proof (0.0015) coil- (0.0008) lock (0.0017) wire (0.0020) binding (0.0015) prevents (0.0009) scratched (0.0024) desktops (0.0016) or (0.0008) pulled (0.0005) clothing. (0.0011) they (0.0013) are (0.0005) top (0.0007) bound, (0.0005) making (0.0006) them (0.0015) ideal (0.0002) for (0.0003) both (0.0002) right (0.0004) and (0.0002) left (-0.0000) handed (0.0014) writers. (0.0009) a (0.0006) durable (0.0005) cover (0.0003) ensures (-0.0002) privacy (0.0008) and (-0.0002) protection, (0.0005) while (-0.0008) the (0.0016) rigid (0.0009) chipboard (0.0005) back (0.0008) adds (0.0007) stability. (0.0009) the (0.0013) 6 (0.0004) x (0.0002) 9 (0.0002) size (0.0010) fits (0.0005) easily (0.0009) in (0.0005) desks, (0.0007) briefcases, (0.0006) portfolios (0.0010) and (0.0007) backpacks. (-0.0007) tops (0.0018) steno (0.0010) books (0.0014) have (-0.0004) smooth (0.0007) white (0.0002) pages, (0.0012) with (0.0006) 80 (0.0004) sheets (0.0000) per (0.0009) book, (0.0007) and (0.0008) are (0.0001) available (0.0003) in (0.0003) a (0.0007) convenient (0.0013) 4- (0.0010) pack. (0.0008) whether (0.0007) it (0.0006) ' (0.0001) s (-0.0005) a (0.0005) multi- (0.0008) part (0.0001) form, (0.0008) notebooks, (0.0006) writing (-0.0001) pads, (0.0010) record (0.0010) books, (0.0007) or (0.0005) any (0.0004) of (0.0004) the (0.0008) hundreds (0.0012) of (0.0008) items (0.0001) we (0.0019) offer, (0.0008) you (0.0020) can (-0.0010) count (0.0004) on (-0.0017) tops (-0.0015) products (-0.0027) to (0.0012) help! (0.0054)
~~~~~~

**Node-9** (global 14327):

~~~~~~text
product (0.0004) from (0.0020) amazon (-0.0021) platform (-0.0006) with (0.0019) title (-0.0005) and (0.0015) content (0.0002) : (-0.0009) title (0.0004) : (-0.0024) tops (-0.0020) weekly (0.0004) time (0.0008) cards, (0.0007) green (0.0008) ink (0.0011) front, (-0.0001) 3. (-0.0005) 5 (0.0007) x (-0.0001) 9 (-0.0007) inches, (-0.0008) 500- (0.0008) count, (0.0018) manila (0.0011) ( (0.0035) 1256 (0.0007) ). (0.0030) content (0.0018) : (0.0025) since (0.0006) 1952, (0.0045) tops (0.0005) has (0.0005) provided (0.0014) quality (-0.0016) products (0.0006) and (0.0036) services (0.0022) to (0.0017) businesses (0.0015) throughout (0.0014) the (-0.0007) world. (0.0019) tops (0.0002) continues (0.0019) that (-0.0002) commitment (0.0021) providing (0.0012) innovative, (0.0019) high (0.0016) quality (0.0003) value- (0.0012) added (0.0006) products (0.0006) for (0.0022) the (-0.0023) office, (0.0011) school (0.0043) and (0.0031) home. (0.0038) tops (-0.0001) time (-0.0000) cards (-0.0008) are (0.0047) the (0.0002) equivalent (-0.0044) to (0.0012) time (0.0007) clock (0.0024) manufacturers (0.0023) time (0.0005) cards. (0.0033) made (0.0034) from (0.0047) 150 (-0.0031) pound (0.0021) manila (0.0050) stock, (0.0037) these (0.0018) cards (0.0020) are (0.0030) printed (0.0019) on (0.0015) the (-0.0017) front (0.0020) with (0.0014) green (0.0017) ink (0.0022) and (0.0009) feature (0.0015) a (0.0003) seven (0.0023) day (0.0015) time (0.0009) period (0.0035) to (0.0009) record (0.0023) regular (0.0028) hours (0.0016) and (0.0005) overtime. (-0.0018) these (0.0049) time (0.0014) cards (0.0026) replace (0.0008) card (0.0047) # (0.0036) 10- (0.0017) 800292. (0.0017) each (0.0016) card (0.0001) measures (-0.0001) 3. (0.0007) 5 (0.0007) x (0.0012) 9 (0.0024) inches, (0.0005) and (0.0013) there (0.0021) are (0.0021) 500 (0.0016) time (-0.0002) cards (-0.0004) per (-0.0013) pack. (-0.0017) whether (0.0015) it (-0.0001) ' (-0.0008) s (0.0009) notebooks, (0.0012) writing (0.0024) pads, (0.0018) record (0.0017) books, (0.0000) time (0.0005) cards, (0.0001) or (0.0025) any (0.0001) of (0.0003) the (-0.0012) hundreds (0.0014) of (-0.0009) items (0.0006) we (0.0019) offer, (-0.0003) you (-0.0007) can (0.0025) count (0.0015) on (0.0014) tops (-0.0017) products (0.0012) to (0.0001) help. (0.0034)
~~~~~~
