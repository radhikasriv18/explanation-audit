# Reference packet: GraphNarrator__gpt-4o-mini__products__1691

- Method: GraphNarrator; configuration: gpt-4o-mini; dataset: products; target node: 1691
- Explanation source: `./robustness_2026-10-30/graphnarrator_gpt4omini/generated_expls-601/2.json` (messages[assistant])
- Scored scope (what the claims were extracted from): ### Free-Text Explanation section
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

Claims were extracted from the `### Free-Text Explanation` section only; the full assistant message is shown here.

~~~~~~text
### Reasoning

0. Graph Structure Reconstruction:

In the provided verbalized graph, the ROOT node (first line) is the target for classification. Single-digit indexed nodes are direct neighbors of ROOT. Double-digit indexed nodes are:
  - Two hops away from ROOT
  - Direct children of their parent node

Thus, the graph structure of this verbalized graph is:

- ROOT (nursing pads)
  - Node-1 (medicated cooling pads)
    - Node-1.1 (facial tissues)
    - Node-1.2 (postpartum bath herbs)
    - Node-1.3 (hemorrhoids treatment cream)
    - Node-1.4 (witch hazel hemorrhoidal pads)
    - Node-1.5 (nursing gown)

1. Word-Level Evaluation:

The ROOT node contains significant keywords such as "nursing" (0.07), "pads" (0.03), "absorbent" (0.01), and "comfort" (0.01), which are directly related to personal care products, particularly those designed for nursing mothers. The presence of terms like "baby" (0.02) and "bond" (0.01) further emphasizes the product's relevance to health and personal care for new parents. Less impactful terms like "product" (-0.00) and "amazon" (-0.03) do not contribute meaningfully to the classification.

2. Graph-Level Aggregation:

Node-1 (medicated cooling pads) has keywords like "relief" (0.01) and "burning" (0.00), indicating its use in personal care, specifically for discomfort associated with hemorrhoids. The direct neighbors of Node-1, including Node-1.1 (facial tissues), Node-1.2 (postpartum bath herbs), Node-1.3 (hemorrhoids treatment cream), Node-1.4 (witch hazel hemorrhoidal pads), and Node-1.5 (nursing gown), all relate to personal care and health, reinforcing the classification context. Each of these products serves a specific need in health and personal care, particularly for women and new mothers.

### Free-Text Explanation
```markdown
The classification of ROOT into "Health & Personal Care" is strongly supported by its own keywords and the co-purchase neighborhood.

ROOT: Keywords such as "nursing" (0.07), "pads" (0.03), and "absorbent" (0.01) clearly identify this product as nursing pads, which are essential for new mothers' personal care.
  - Node-1: Medicated cooling pads (keywords: "relief" (0.01), "burning" (0.00)) provide comfort and address specific health needs, reinforcing the Health & Personal Care context.
    - Node-1.1: Facial tissues, while less directly related, are often used in personal care routines, supporting the overall category.
    - Node-1.2: Postpartum bath herbs cater to the needs of new mothers, emphasizing care during recovery.
    - Node-1.3: Hemorrhoids treatment cream is a direct health product aimed at providing relief, further solidifying the classification.
    - Node-1.4: Witch hazel hemorrhoidal pads are specifically designed for personal care, addressing discomfort associated with hemorrhoids.
    - Node-1.5: A nursing gown is another personal care item that supports the needs of nursing mothers.

In summary, ROOT's high-saliency keywords strongly indicate a focus on nursing and personal care, while the entire co-purchase neighborhood consists of products that cater to health-related needs, providing robust evidence for the "Health & Personal Care" classification.
```
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/2.json`).

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
<verbalized-graph>ROOT: product(-0.00) amazon(-0.03) platform(-0.00) title(0.02) content(-0.00) title(0.05) johnson(0.07) contour(0.01) nursing(-0.04) pads-(0.03) 36(-0.00) ct(-0.03) ".(-0.04) content(0.03) exclusive(-0.00) contour(0.04) shape(-0.00) 50(-0.00) absorbent(0.01) leading(0.05) brand(0.02) nursing(-0.01) little(0.01) one(0.01) spending(0.00) time(0.01) together(0.01) creates(0.02) special(0.01) bond.(-0.03) enjoying(0.01) time(0.02) baby,(-0.02) continue(0.02) look(0.01) feel(0.01) best(0.01) using(0.02) johnson(0.05) r(0.01) nursing(0.02) pads.(-0.01) designed(0.03) superior(0.01) absorbency,(0.02) comfort,(0.01) complete(0.00) discretion.(-0.01) johnson(0.03) r(-0.01) nursing(0.03) pads(0.03) help(0.03) feel(-0.00) confident(0.02) protected(-0.01) go.(-0.01) know(-0.00) babies(0.01) unique(0.01) skin(0.03) needs.(-0.05) created(0.02) full(-0.00) range(0.00) mild(0.01) gentle(0.01) products(-0.01) especially(-0.01) babies(-0.02) cleanse,(0.01) moisturize(0.00) protect(-0.00) delicate(0.01) skin.(-0.01) held(0.01) high(0.00) standard(0.02) safety,(0.01) unique(-0.02) tears(0.00) r(0.00) formula(0.03) wash(0.03) 1(0.02) choice(0.00) hospitals(0.00) clinically(-0.00) proven(0.01) mildness(0.00) tm(0.01) lotion(0.01) gentle(0.02) enough(0.02) use(0.00) morning(0.01) night.(-0.00) dermatologist(0.01) tested(0.01) hypoallergenic.(-0.00) also(-0.02) look(0.02) members(0.01) johnson(0.01) r(0.01) family,(0.01) johnson(0.04) r(0.01) natural(-0.00) r(-0.01) ),(-0.01) line(0.00) baby(0.01) skincare(0.01) products(-0.01) made(0.02) naturally(-0.00) derived(0.01) ingredients(0.02) 100(0.01) years(0.01) baby(0.02) care(-0.01) expertise.(0.00) 
Node-1: product(0.01) amazon(-0.00) platform(0.00) title(0.00) content(0.01) title(0.00) tucks(0.00) medicated(-0.00) cooling(0.00) pads(0.00) 100(-0.00) pads(-0.00) per(0.00) pack(0.00) pack(-0.00) 2(-0.01) ).(0.00) content(0.00) tucks(-0.00) medicated(0.00) cooling(-0.00) pads(0.00) 100(0.00) pads(0.00) per(-0.00) pack(0.00) pack(0.01) 2(0.00) ).(0.00) hemorrhoidal(0.00) pads(-0.00) witch(0.00) hazel.(0.00) immediate(0.01) relief(0.01) burning(0.00) itching(0.00) caused(0.00) hemrrhoids.(0.00) hazel(0.00) soothes(0.00) protects(0.00) irritated(0.00) areas.(-0.00) 
Node-1.1: product(-0.00) amazon(-0.00) platform(0.00) title(0.00) content(0.00) title(0.00) puffs(0.00) plus(0.00) lotion(0.00) scent(0.00) vicks(0.00) facial(0.00) tissues(0.00) 88(0.00) count(0.00) 1(0.00) family(0.00) box(0.00) 88(-0.00) tissues(0.00) per(0.00) box(0.00) pack(0.00) 24(0.00) ).(0.00) content(0.00) begin(0.00) puffs(-0.00) content(0.00) 
Node-1.2: product(0.00) amazon(0.00) platform(-0.00) title(-0.00) content(0.00) title(0.00) earth(-0.00) mama(0.00) angel(0.00) baby(0.00) postpartum(0.00) bath(0.00) herbs,(0.00) 6(-0.00) count.(0.00) content(0.00) postpartum(0.00) bath(-0.00) herbs(-0.00) padslabor(0.00) make(0.00) feel(0.00) like(0.00) bottom(0.00) gone(0.00) fifteen(0.00) rounds(0.00) prizefighter(-0.00) run(0.00) ny(0.00) marathon(-0.00) once.(0.00) simple(0.00) act(0.00) sitting(0.00) simple(0.00) all.(0.00) usda(0.00) certified(0.00) 100(-0.00) organic(0.00) postpartum(0.00) bath(0.00) herbs(0.00) soothing,(-0.00) comforting(0.00) blend(-0.00) includes(0.00) salts,(-0.00) oatmeal(0.00) organic(0.00) herbs(0.00) historically(0.00) used(0.00) support(0.00) postpartum(0.00) women.(-0.00) wound-(0.00) healing,(0.00) styptic(0.00) antibacterial(0.00) herbs(0.00) salts(0.00) help(0.00) reduce(0.00) swelling(0.00) speed(0.00) healing(0.00) vaginal(0.00) soreness,(-0.00) episiotomy(0.00) perineal(0.00) bruising.(0.00) great(0.00) prenatal(0.00) postpartum(0.00) hemorrhoids(0.00) too.(0.00) suggested(0.00) used(0.00) packed(0.00) easy(0.00) use,(0.00) individual(0.00) herbal(-0.00) pads,(0.00) perfect(0.00) one(0.00) use,(0.00) without(0.00) soggy(0.00) herb(0.00) cleanup(0.00) directly(0.00) childbirth(-0.00) several(0.00) days,(0.00) use(0.00) moistened(0.00) herbal(0.00) pads(0.00) iced(0.00) comfort(0.00) achy(-0.00) lady(0.00) parts.(0.00) later,(0.00) use(0.00) warm,(0.00) sitz(0.00) bath,(0.00) soothing(0.00) relief.(0.00) feel(0.00) better(0.00) sitz(0.00) easier,(0.00) enjoy(0.00) new(0.00) angel,(-0.00) naturally.(0.00) warnings(0.00) keep(0.00) reach(0.00) children.(0.00) dietary(0.00) supplements,(-0.00) consult(0.00) healthcare(0.00) professional(0.00) use.(0.00) see(0.00) product(0.00) label(0.00) information.(0.00) 
Node-1.3: product(0.00) amazon(-0.00) platform(-0.00) title(0.00) content(0.00) title(-0.00) anusol(0.00) haemorrhoids(0.00) piles(0.00) treatment(0.00) cream-(-0.00) 23g.(-0.00) content(0.00) anusol(-0.00) range(-0.00) provides(-0.00) effective(0.00) soothing(-0.00) relief(0.00) piles,(0.00) available(-0.00) three(0.00) types(-0.00) application.(-0.00) one(0.00) contains(-0.00) astringent(0.00) help(-0.00) soothe(-0.00) area(-0.00) reduce(-0.00) swelling,(-0.00) antiseptic(-0.00) reduce(-0.00) risk(-0.00) infection(-0.00) zinc(-0.00) help(-0.00) protect(-0.00) sore(-0.00) skin.(-0.00) 
Node-1.4: product(0.00) amazon(-0.00) platform(0.00) title(0.00) content(0.00) title(0.00) t.(-0.00) n.(-0.00) dickinson(0.00) hemorrhoidal(0.00) pads,(-0.00) witch(-0.00) hazel(0.00) aloe,(0.00) 100-(0.00) count(0.00) packages(-0.00) pack(0.00) 2(0.00) ".(-0.00) content(-0.00) t.(-0.00) n.(-0.00) dickinson(-0.00) witch(-0.00) hazel(0.00) hemorrhoidal(0.00) pads,(-0.00) 100(-0.00) pads.(-0.00) indications(0.00) hemorrhoidal(0.00) medicated(-0.00) pads(-0.00) helps(-0.00) relieve(-0.00) local(-0.00) burning,(0.00) itching(-0.00) discomfort(-0.00) associated(0.00) hemorrhoids.(-0.00) aids(-0.00) protection(0.00) irritated(-0.00) inflamed(0.00) anorectal(-0.00) areas.(-0.00) adults(-0.00) cleanse(-0.00) affect(0.00) area(-0.00) mild(-0.00) soap(-0.00) warm(-0.00) water(-0.00) rinse.(0.00) 
Node-1.5: product(-0.00) amazon(-0.00) platform(-0.00) title(0.00) content(-0.00) title(-0.00) aimee(0.00) gowns(-0.00) original(-0.00) bra-(0.00) less(0.00) nursing(-0.00) gown(-0.00) x-(0.00) lar</verbalized-graph>

### Classification Label
Health & Personal Care

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 1691
- Title: "Johnson's Contour Nursing Pads - 36 ct"
- True class (canonical `y`): **Baby Products**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Beauty**
- Prediction recorded by this method's pipeline: **Health & Personal Care**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: "Johnson's Contour Nursing Pads - 36 ct". Content: Exclusive Contour Shape 50% More Absorbent than the Leading Brand Nursing your little one and spending time together creates a special bond. While enjoying this time with your baby, you can continue to look and feel your best by using Johnson's(R) Nursing Pads. They are designed for superior absorbency, comfort, and complete discretion. Johnson's(R) Nursing Pads help you feel confident that you are protected while you are on the go. We know babies have unique skin needs. That's why we've created a full range of mild and gentle products especially for babies to be cleanse, moisturize and protect their delicate skin. Held to our high standard of safety, our unique No more Tears(R) Formula Wash is the #1 choice of hospitals and our Clinically Proven Mildness(TM) lotion is gentle enough to use both morning and night. Dermatologist tested and hypoallergenic. Also look for the other members of the Johnson's(R) family, such as Johnson's(R) Natural(R), the line of baby skincare products that are made with naturally derived ingredients and over 100 years of baby care expertise.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 6 nodes

| node id | true class | title |
|---|---|---|
| 134 | Health & Personal Care | Tucks Medicated Cooling Pads 100 Pads Per Pack (Pack of 2) |
| 13353 | Baby | Lansinoh Soothies Gel Pads, 2 Count |
| 13618 | Baby | Charlie Banana Nursing Pads, White |
| 13619 | Baby | Waterproof Crib Mattress Pad - Soft Fitted Quilted Cover Pads for Baby - Best Protectors Liner Sheet Toppers Helps Infants From Bed Bugs, Allergies - Long Lasting Size Fits All Cribs Breathable and Absorbent - Extremely Healthy Choice for You Toddler |
| 13620 | Health & Personal Care | Lansinoh Breastmilk Storage Bags, 25-Count Boxes (Pack of 3) |
| 13621 | Baby | Philips AVENT Day Disposable Breast Pads, 60-Count |

### 2-hop (shortest distance exactly 2): 13 nodes

| node id | true class | title |
|---|---|---|
| 0 | Clothing, Shoes & Jewelry | Aimee Gowns Original Bra-less Nursing Gown (X-Large, Fuchsia) |
| 1627 | Baby | Sugar Booger &quot;Numbers&quot; Closet Dividers Set of 5 |
| 1646 | Health & Personal Care | "T.N. Dickinson's Hemorrhoidal Pads, Witch Hazel with Aloe, 100-Count Packages (Pack of 2)" |
| 1680 | Baby Products | Pampers Swaddlers Diapers Size 1 Economy Pack Plus 216 Count |
| 1684 | Health & Personal Care | Puffs Plus Lotion With The Scent Of Vicks Facial Tissues; 88 Count; 1 Family Box (88 Tissues Per Box) (Pack of 24) |
| 1685 | Beauty | Earth Mama Angel Baby Postpartum Bath Herbs, 6 Count |
| 1686 | Health & Personal Care | Anusol Haemorrhoids (Piles) Treatment Cream - 23g |
| 1687 | Health & Personal Care | Always Maxi Overnight Extra Heavy Flow Pads With Wings, 40 Count |
| 1688 | Baby | Fisher-Price My Little Snugakitty Bouncer |
| 1689 | Baby Products | Lansinoh 20265 Disposable Nursing Pads, 60-Count |
| 1690 | Health & Personal Care | Tucks Witch Hazel Hemorrhoidal Pads, 40 ea |
| 1692 | Health & Personal Care | Tucks Hemorrhoid Ointment |
| 5164 | Health & Personal Care | Nelsons Bach Hemorrhoid Cream 1 oz. |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/2.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Health & Personal Care**, ground truth = **Baby Products**.
The verbalized graph is 15330 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 1691 | 233 | 0.0730 | yes |
| Node-1 | 1 | 134 | 60 | 0.0134 | yes |
| Node-1.1 | 7 | 1684 | 46 | 0.0018 | yes |
| Node-1.2 | 8 | 1685 | 207 | 0.0029 | yes |
| Node-1.3 | 9 | 1686 | 66 | 0.0006 | yes |
| Node-1.4 | 10 | 1646 | 83 | 0.0004 | yes |
| Node-1.5 | 11 | 0 | 173 | 0.0006 | yes |
| Node-1.6 | 12 | 1689 | 214 | 0.0005 | no |
| Node-1.7 | 13 | 1690 | 147 | 0.0007 | no |
| Node-1.8 | 14 | 1680 | 24 | 0.0013 | no |
| Node-1.9 | 15 | 1687 | 68 | 0.0006 | no |
| Node-1.10 | 16 | 5164 | 38 | 0.0008 | no |
| Node-2 | 2 | 13353 | 20 | 0.0317 | no |
| Node-2.1 | 17 | 1627 | 101 | 0.0027 | no |
| Node-3 | 3 | 13618 | 22 | 0.0231 | no |
| Node-4 | 4 | 13619 | 308 | 0.0129 | no |
| Node-5 | 5 | 13620 | 26 | 0.0299 | no |
| Node-6 | 6 | 13621 | 22 | 0.0295 | no |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.10, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->Node-1.6, Node-1->Node-1.7, Node-1->Node-1.8, Node-1->Node-1.9, Node-1->ROOT, Node-1.1->Node-1, Node-1.10->Node-1, Node-1.2->Node-1, Node-1.2->Node-2, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, Node-1.6->Node-1, Node-1.7->Node-1, Node-1.8->Node-1, Node-1.9->Node-1, Node-2->Node-1.2, Node-2->Node-2.1, Node-2->ROOT, Node-2.1->Node-2, Node-3->ROOT, Node-4->ROOT, Node-5->ROOT, Node-6->ROOT, ROOT->Node-1, ROOT->Node-2, ROOT->Node-3, ROOT->Node-4, ROOT->Node-5, ROOT->Node-6

### Tokens and scores

**ROOT** (global 1691):

~~~~~~text
product (-0.0031) from (0.0180) amazon (-0.0268) platform (-0.0004) with (0.0094) title (0.0166) and (0.0127) content (-0.0024) : (0.0253) title (0.0485) : (0.0071) " (0.0091) johnson (0.0730) ' (-0.0171) s (0.0096) contour (0.0139) nursing (-0.0382) pads- (0.0260) 36 (-0.0040) ct (-0.0307) ". (-0.0393) content (0.0327) : (0.0030) exclusive (-0.0017) contour (0.0394) shape (-0.0026) 50 (-0.0007) % (-0.0001) more (0.0067) absorbent (0.0134) than (-0.0075) the (-0.0188) leading (0.0453) brand (0.0227) nursing (-0.0084) your (-0.0057) little (0.0062) one (0.0113) and (-0.0005) spending (0.0050) time (0.0104) together (0.0146) creates (0.0213) a (-0.0113) special (0.0096) bond. (-0.0315) while (0.0191) enjoying (0.0076) this (0.0072) time (0.0165) with (0.0002) your (0.0205) baby, (-0.0241) you (0.0005) can (0.0145) continue (0.0155) to (0.0072) look (0.0067) and (0.0013) feel (0.0093) your (0.0289) best (0.0055) by (0.0082) using (0.0220) johnson (0.0513) ' (0.0094) s (0.0152) ( (0.0049) r (0.0052) ) (-0.0144) nursing (0.0156) pads. (-0.0118) they (0.0118) are (0.0178) designed (0.0350) for (-0.0010) superior (0.0066) absorbency, (0.0194) comfort, (0.0109) and (0.0376) complete (0.0044) discretion. (-0.0148) johnson (0.0343) ' (-0.0003) s (0.0041) ( (0.0267) r (-0.0096) ) (-0.0030) nursing (0.0276) pads (0.0314) help (0.0260) you (0.0411) feel (-0.0038) confident (0.0244) that (0.0174) you (0.0339) are (0.0309) protected (-0.0076) while (0.0149) you (0.0502) are (0.0286) on (0.0188) the (-0.0165) go. (-0.0139) we (0.0145) know (-0.0040) babies (0.0123) have (0.0260) unique (0.0121) skin (0.0343) needs. (-0.0470) that (0.0424) ' (0.0149) s (0.0258) why (0.0126) we (0.0050) ' (-0.0051) ve (0.0047) created (0.0166) a (-0.0100) full (-0.0043) range (0.0028) of (-0.0083) mild (0.0086) and (-0.0057) gentle (0.0132) products (-0.0126) especially (-0.0139) for (0.0117) babies (-0.0219) to (-0.0085) be (-0.0015) cleanse, (0.0061) moisturize (0.0045) and (-0.0018) protect (-0.0043) their (-0.0065) delicate (0.0139) skin. (-0.0075) held (0.0067) to (0.0051) our (-0.0372) high (0.0004) standard (0.0184) of (-0.0085) safety, (0.0112) our (-0.0407) unique (-0.0219) no (-0.0025) more (0.0051) tears (0.0045) ( (0.0073) r (0.0003) ) (-0.0083) formula (0.0281) wash (0.0252) is (0.0069) the (-0.0073) # (0.0180) 1 (0.0224) choice (0.0047) of (0.0059) hospitals (0.0015) and (0.0019) our (-0.0678) clinically (-0.0008) proven (0.0078) mildness (0.0016) ( (0.0055) tm (0.0073) ) (0.0200) lotion (0.0083) is (0.0098) gentle (0.0166) enough (0.0218) to (0.0100) use (0.0007) both (0.0026) morning (0.0079) and (-0.0065) night. (-0.0044) dermatologist (0.0081) tested (0.0100) and (0.0029) hypoallergenic. (-0.0003) also (-0.0184) look (0.0163) for (0.0245) the (-0.0058) other (0.0199) members (0.0110) of (0.0056) the (-0.0063) johnson (0.0131) ' (0.0057) s (0.0160) ( (0.0434) r (0.0139) ) (0.0042) family, (0.0140) such (-0.0047) as (-0.0050) johnson (0.0442) ' (-0.0031) s (0.0097) ( (0.0074) r (0.0108) ) (-0.0101) natural (-0.0045) ( (0.0137) r (-0.0131) ), (-0.0066) the (-0.0116) line (0.0042) of (-0.0142) baby (0.0139) skincare (0.0065) products (-0.0132) that (0.0222) are (0.0150) made (0.0186) with (0.0003) naturally (-0.0040) derived (0.0112) ingredients (0.0184) and (0.0076) over (0.0226) 100 (0.0055) years (0.0075) of (-0.0138) baby (0.0242) care (-0.0052) expertise. (0.0002)
~~~~~~

**Node-1** (global 134):

~~~~~~text
product (0.0134) from (0.0045) amazon (-0.0004) platform (0.0002) with (0.0096) title (0.0034) and (0.0036) content (0.0082) : (0.0032) title (0.0026) : (0.0050) tucks (0.0007) medicated (-0.0011) cooling (0.0014) pads (0.0009) 100 (-0.0022) pads (-0.0024) per (0.0016) pack (0.0042) ( (-0.0027) pack (-0.0025) of (-0.0073) 2 (-0.0096) ). (0.0050) content (0.0013) : (0.0037) tucks (-0.0003) medicated (0.0001) cooling (-0.0014) pads (0.0007) 100 (0.0007) pads (0.0026) per (-0.0010) pack (0.0004) ( (-0.0000) pack (0.0099) of (-0.0036) 2 (0.0034) ). (0.0022) hemorrhoidal (0.0008) pads (-0.0000) with (0.0094) witch (0.0033) hazel. (0.0005) immediate (0.0087) relief (0.0079) from (-0.0018) burning (0.0012) and (0.0024) itching (0.0002) caused (0.0017) by (0.0015) hemrrhoids. (0.0016) with (-0.0033) hazel (0.0010) soothes (0.0002) and (0.0036) protects (0.0012) irritated (0.0033) areas. (-0.0036)
~~~~~~

**Node-1.1** (global 1684):

~~~~~~text
product (-0.0005) from (0.0006) amazon (-0.0002) platform (0.0003) with (0.0006) title (0.0006) and (-0.0001) content (0.0014) : (0.0006) title (0.0007) : (-0.0003) puffs (0.0006) plus (0.0003) lotion (0.0003) with (0.0003) the (-0.0001) scent (0.0005) of (0.0001) vicks (0.0004) facial (0.0005) tissues (0.0002) ; (0.0004) 88 (0.0003) count (0.0007) ; (0.0002) 1 (0.0005) family (0.0003) box (0.0003) ( (0.0007) 88 (-0.0000) tissues (0.0008) per (0.0003) box (0.0005) ) (0.0005) ( (0.0006) pack (0.0000) of (0.0004) 24 (0.0002) ). (0.0004) content (0.0007) : (0.0011) begin (0.0000) puffs (-0.0001) a (0.0007) + (0.0003) content (0.0018)
~~~~~~

**Node-1.2** (global 1685):

~~~~~~text
product (0.0003) from (-0.0009) amazon (0.0005) platform (-0.0001) with (-0.0002) title (-0.0003) and (0.0003) content (0.0008) : (0.0007) title (0.0001) : (0.0007) earth (-0.0002) mama (0.0004) angel (0.0001) baby (0.0004) postpartum (0.0003) bath (0.0010) herbs, (0.0002) 6 (-0.0000) count. (0.0002) content (0.0014) : (-0.0002) postpartum (0.0001) bath (-0.0005) herbs (-0.0001) padslabor (0.0003) can (0.0002) make (0.0004) you (0.0001) feel (0.0007) like (0.0004) your (-0.0004) bottom (0.0002) has (0.0005) gone (0.0005) fifteen (0.0002) rounds (0.0006) with (-0.0001) a (0.0004) prizefighter (-0.0001) and (0.0001) run (0.0004) the (0.0007) ny (0.0014) marathon (-0.0008) all (0.0003) at (0.0004) once. (0.0001) and (0.0004) the (0.0007) simple (0.0004) act (0.0003) of (0.0003) sitting (0.0006) isn (0.0007) ' (0.0001) t (0.0002) simple (0.0009) at (0.0000) all. (0.0007) usda (0.0009) certified (0.0008) 100 (-0.0001) % (0.0024) organic (0.0003) postpartum (0.0006) bath (0.0001) herbs (0.0006) is (0.0002) a (0.0015) soothing, (-0.0012) comforting (0.0005) blend (-0.0012) includes (0.0029) salts, (-0.0004) oatmeal (0.0004) and (0.0005) organic (0.0013) herbs (0.0012) that (0.0011) have (0.0004) historically (0.0011) been (0.0001) used (0.0005) to (0.0006) support (0.0009) postpartum (0.0009) women. (-0.0002) wound- (0.0006) healing, (0.0005) styptic (0.0005) and (0.0005) antibacterial (0.0007) herbs (0.0011) and (0.0007) salts (0.0013) help (0.0009) reduce (0.0013) swelling (0.0005) and (0.0005) speed (0.0004) healing (0.0006) of (0.0005) vaginal (0.0000) soreness, (-0.0001) episiotomy (0.0002) and (-0.0001) perineal (0.0002) bruising. (0.0004) great (0.0005) for (-0.0000) both (0.0004) prenatal (0.0004) and (0.0002) postpartum (0.0003) hemorrhoids (0.0004) too. (0.0007) suggested (0.0010) used (0.0008) : (0.0005) packed (0.0007) in (0.0005) easy (0.0010) to (0.0009) use, (0.0004) individual (0.0010) herbal (-0.0003) pads, (0.0009) each (0.0006) is (0.0002) perfect (0.0007) for (-0.0005) one (0.0007) use, (0.0001) without (0.0007) the (0.0005) soggy (0.0005) herb (0.0007) cleanup (0.0005) directly (0.0008) after (0.0003) childbirth (-0.0005) and (0.0003) for (0.0001) several (0.0006) days, (0.0002) use (0.0003) the (0.0002) moistened (0.0006) herbal (0.0014) pads (0.0013) iced (0.0003) to (0.0002) comfort (0.0007) achy (-0.0001) lady (0.0003) parts. (0.0002) later, (0.0003) use (0.0002) it (0.0002) warm, (0.0003) or (0.0006) in (0.0000) a (0.0005) sitz (0.0008) bath, (0.0003) for (0.0002) soothing (0.0002) relief. (0.0011) feel (0.0005) better (0.0007) and (0.0003) sitz (0.0007) easier, (0.0005) so (0.0005) you (-0.0001) can (0.0008) enjoy (0.0004) your (0.0008) new (0.0007) angel, (-0.0003) naturally. (0.0008) warnings (0.0005) : (0.0008) keep (0.0010) out (0.0003) of (-0.0002) reach (0.0005) of (-0.0003) children. (0.0009) as (0.0005) with (0.0003) all (0.0004) dietary (0.0002) supplements, (-0.0003) consult (0.0007) your (-0.0000) healthcare (0.0007) professional (0.0008) before (0.0002) use. (0.0001) see (0.0006) product (0.0013) label (0.0005) for (0.0002) more (0.0008) information. (0.0008)
~~~~~~

**Node-1.3** (global 1686):

~~~~~~text
product (0.0001) from (0.0000) amazon (-0.0003) platform (-0.0001) with (0.0001) title (0.0002) and (-0.0001) content (0.0001) : (0.0003) title (-0.0007) : (-0.0002) anusol (0.0000) haemorrhoids (0.0000) ( (-0.0001) piles (0.0002) ) (0.0000) treatment (0.0001) cream- (-0.0000) 23g. (-0.0002) content (0.0001) : (0.0000) the (-0.0002) anusol (-0.0002) range (-0.0001) provides (-0.0000) effective (0.0001) soothing (-0.0002) relief (0.0001) for (-0.0000) piles, (0.0001) and (0.0000) is (0.0000) available (-0.0003) in (-0.0000) three (0.0003) types (-0.0002) of (-0.0002) application. (-0.0003) each (0.0006) one (0.0004) contains (-0.0003) an (-0.0000) astringent (0.0000) to (-0.0001) help (-0.0001) soothe (-0.0005) the (0.0001) area (-0.0001) and (0.0000) reduce (-0.0001) swelling, (-0.0002) an (0.0000) antiseptic (-0.0002) to (0.0000) reduce (-0.0002) the (0.0002) risk (-0.0002) of (0.0000) infection (-0.0002) and (0.0002) zinc (-0.0001) to (0.0001) help (-0.0001) protect (-0.0003) sore (-0.0001) skin. (-0.0007)
~~~~~~

**Node-1.4** (global 1646):

~~~~~~text
product (0.0004) from (0.0002) amazon (-0.0004) platform (0.0001) with (0.0002) title (0.0002) and (0.0001) content (0.0002) : (0.0004) title (0.0001) : (-0.0000) " (0.0001) t. (-0.0000) n. (-0.0001) dickinson (0.0000) ' (0.0001) s (0.0002) hemorrhoidal (0.0001) pads, (-0.0001) witch (-0.0001) hazel (0.0001) with (0.0001) aloe, (0.0002) 100- (0.0001) count (0.0001) packages (-0.0000) ( (0.0001) pack (0.0001) of (-0.0001) 2 (0.0002) ) (0.0002) ". (-0.0000) content (-0.0001) : (-0.0000) t. (-0.0000) n. (-0.0002) dickinson (-0.0000) : (-0.0000) witch (-0.0001) hazel (0.0001) hemorrhoidal (0.0001) pads, (-0.0000) 100 (-0.0001) pads. (-0.0000) indications (0.0003) : (0.0001) hemorrhoidal (0.0001) medicated (-0.0001) pads (-0.0001) helps (-0.0000) relieve (-0.0002) local (-0.0004) burning, (0.0001) itching (-0.0000) and (0.0001) discomfort (-0.0002) associated (0.0000) with (-0.0001) hemorrhoids. (-0.0000) aids (-0.0001) in (-0.0001) the (-0.0001) protection (0.0001) of (0.0000) irritated (-0.0003) or (0.0001) inflamed (0.0000) anorectal (-0.0001) areas. (-0.0003) adults (-0.0004) : (0.0002) cleanse (-0.0000) the (-0.0003) affect (0.0001) area (-0.0002) with (0.0001) mild (-0.0001) soap (-0.0002) and (-0.0002) warm (-0.0001) water (-0.0004) and (0.0002) rinse. (0.0000)
~~~~~~

**Node-1.5** (global 0):

~~~~~~text
product (-0.0002) from (-0.0001) amazon (-0.0002) platform (-0.0002) with (-0.0003) title (0.0001) and (-0.0001) content (-0.0001) : (0.0005) title (-0.0001) : (0.0002) aimee (0.0001) gowns (-0.0003) original (-0.0001) bra- (0.0000) less (0.0005) nursing (-0.0005) gown (-0.0005) ( (0.0001) x- (0.0000) large, (0.0001) fuchsia (-0.0001) ). (0.0004) content (0.0003) : (0.0000) the (0.0000) one (0.0002) that (0.0001) started (0.0001) it (0.0000) all! (-0.0002) the (-0.0001) nightgown (-0.0000) ' (0.0001) s (0.0002) modern (-0.0001) design (-0.0001) features (0.0001) a (0.0001) split (0.0001) front (0.0001) to (-0.0000) help (-0.0001) facilitate (0.0001) easy (0.0000) access (0.0002) to (0.0001) the (0.0000) breast (0.0001) for (0.0002) the (0.0000) baby. (0.0000) simply (0.0002) pull (0.0001) aside (0.0000) the (0.0001) gown (-0.0001) when (0.0000) you (0.0001) want (0.0002) to (0.0003) nurse. (-0.0003) the (0.0002) gown (-0.0002) holds (0.0000) nursing (-0.0002) pads (0.0000) in (0.0002) place (0.0002) without (-0.0000) having (0.0000) to (0.0001) wear (0.0002) an (-0.0001) uncomfortable (0.0002) bra (0.0001) to (0.0002) bed. (-0.0001) you (0.0005) don (0.0002) ' (0.0001) t (0.0002) even (0.0001) have (0.0001) to (0.0002) be (0.0001) a (0.0004) nursing (-0.0001) mom (0.0003) to (0.0002) wear (0.0003) our (0.0006) gowns! (0.0004) benefits (0.0001) :- (0.0006) you (0.0001) will (0.0002) no (0.0001) longer (0.0003) have (-0.0000) to (0.0000) wear (0.0001) an (0.0001) uncomfortable (0.0002) bra (0.0001) to (0.0002) bed!- (0.0004) less (-0.0000) risk (0.0001) of (0.0001) mastitis (0.0000) as (0.0001) with (-0.0002) tight (-0.0000) fitting (0.0000) bras- (-0.0000) a (0.0002) roomy (-0.0000) design (-0.0002) for (-0.0001) shrinking (0.0000) tummies- (0.0000) easy (0.0001) access (0.0006) to (0.0004) nursing (-0.0005) at (-0.0002) night (0.0001) or (0.0001) any (-0.0000) time (0.0001) of (-0.0000) the (0.0002) day- (0.0001) can (0.0001) be (0.0002) worn (-0.0001) as (0.0002) a (0.0000) lounge (0.0003) dress (-0.0000) or (0.0004) a (0.0001) nightgown- (0.0001) holds (-0.0001) nursing (0.0004) pads (0.0003) secure (0.0001) in (-0.0001) place (0.0000) ( (0.0000) gowns (0.0001) do (0.0002) not (0.0003) come (0.0002) with (-0.0001) robes (-0.0005) as (0.0003) a (0.0002) set, (0.0001) you (0.0002) can (0.0003) purchase (0.0003) the (0.0002) robe (0.0003) separately (0.0002) by (0.0000) clicking (0.0002) aimee (0.0005) gowns (0.0002) products (0.0003) above. (0.0001) ) (0.0001)
~~~~~~

**Node-1.6** (global 1689):

~~~~~~text
product (-0.0001) from (-0.0003) amazon (-0.0000) platform (0.0000) with (0.0000) title (0.0001) and (-0.0000) content (-0.0002) : (0.0001) title (0.0000) : (-0.0001) lansinoh (0.0001) 20265 (0.0000) disposable (0.0000) nursing (0.0001) pads, (0.0001) 60- (-0.0000) count. (0.0002) content (-0.0000) : (0.0002) breastfeeding (-0.0001) mothers (0.0001) know (-0.0000) that (-0.0000) let- (-0.0001) down (0.0001) can (0.0000) occur (0.0000) at (0.0001) the (0.0001) most (0.0000) inopportune (0.0001) times. (0.0001) it (0.0001) can (0.0001) be (0.0001) triggered (0.0001) by (0.0000) missing (0.0001) a (0.0000) scheduled (0.0001) feeding, (0.0000) hearing (0.0000) a (-0.0000) baby (0.0000) crying (0.0000) ( (-0.0002) whether (-0.0002) your (0.0000) own (-0.0000) or (-0.0002) someone (0.0000) else (-0.0000) & (-0.0002) # (-0.0000) x92 (0.0001) ; (-0.0002) s (0.0001) ), (0.0000) or (-0.0000) even (-0.0000) just (0.0000) thinking (-0.0000) about (-0.0000) your (0.0001) baby. (-0.0001) and, (0.0000) of (-0.0001) course, (0.0002) leaks (0.0001) always (-0.0002) seems (0.0000) to (0.0000) happen (-0.0000) when (-0.0002) you (-0.0001) & (-0.0000) # (0.0000) x92 (0.0001) ; (0.0000) re (-0.0000) in (0.0002) the (0.0001) middle (0.0001) of (-0.0000) an (0.0002) important (-0.0001) business (0.0002) presentation (0.0002) or (0.0001) wearing (0.0001) your (0.0001) best (0.0001) silk (0.0002) dress (0.0001) at (0.0001) a (0.0000) friend (0.0001) & (0.0000) # (0.0000) x92 (0.0001) ; (0.0001) s (0.0000) wedding. (0.0001) these (0.0000) extra (0.0000) absorbent (0.0000) disposable (0.0001) nursing (-0.0002) pads (0.0001) have (-0.0000) a (-0.0001) soft, (0.0000) comfortable (-0.0000) lining (0.0000) that (0.0000) rests (0.0000) against (-0.0000) the (-0.0001) skin. (0.0001) the (-0.0000) lining (0.0000) draws (0.0000) excess (-0.0000) moisture (0.0000) away (0.0001) from (0.0000) skin (0.0000) and (-0.0000) into (0.0000) a (0.0000) polymer (-0.0002) core (0.0001) in (0.0001) the (0.0000) center. (0.0000) a (0.0001) laminated (0.0000) waterproof (0.0001) lining (0.0001) against (-0.0000) your (0.0000) clothing (0.0001) prevents (-0.0001) milk (0.0001) from (-0.0001) getting (0.0000) any (0.0000) further. (0.0001) the (0.0001) pads (0.0001) are (0.0001) incredibly (0.0000) thin (0.0001) ( (0.0001) 2 (0.0001) mm (0.0001) ) (0.0001) and (0.0000) contoured (0.0001) like (0.0000) a (0.0001) breast, (0.0001) so (0.0001) they (0.0001) don (0.0003) & (-0.0001) # (0.0000) x92 (0.0000) ; (-0.0001) t (-0.0001) look (0.0001) stiff (0.0000) or (0.0000) unnatural (0.0001) under (0.0001) clothing. (0.0001) adhesive (-0.0001) tape (0.0003) on (0.0001) the (0.0000) back (0.0000) of (0.0001) each (0.0000) pad (0.0000) secures (0.0001) it (0.0001) to (0.0000) undergarments (0.0001) to (-0.0000) keep (-0.0000) it (0.0000) from (0.0001) shifting (0.0001) during (0.0000) the (0.0001) day. (0.0001) each (0.0001) pad (0.0000) comes (0.0001) individually (0.0001) wrapped (0.0001) for (0.0000) hygienically (0.0001) transporting (0.0001) them (0.0001) in (0.0001) a (0.0001) briefcase (0.0003) or (-0.0000) diaper (0.0001) bag.-- (0.0002) cristina (-0.0004) vaamonde (0.0005)
~~~~~~

**Node-1.7** (global 1690):

~~~~~~text
product (-0.0002) from (-0.0001) amazon (0.0001) platform (-0.0003) with (-0.0002) title (0.0000) and (-0.0001) content (-0.0002) : (0.0004) title (0.0002) : (-0.0001) tucks (-0.0000) witch (-0.0002) hazel (-0.0001) hemorrhoidal (-0.0001) pads, (0.0001) 40 (-0.0004) ea. (0.0001) content (-0.0000) : (-0.0002) medicated (-0.0003) cooling (0.0000) padsimmediate (0.0000) relief (0.0000) from (-0.0001) burning (-0.0001) and (-0.0002) itching (-0.0000) caused (-0.0001) by (-0.0001) hemorrhoidswitch (-0.0001) hazel (-0.0002) soothes (0.0000) and (-0.0001) protects (-0.0001) irritated (0.0003) areasbrand (-0.0002) used (-0.0001) by (0.0002) hospitalsyou (0.0001) are (-0.0003) not (0.0002) alonetm. (-0.0001) over (-0.0000) twenty (-0.0000) percent (0.0000) of (0.0000) the (0.0004) adult (-0.0002) population (0.0001) will (-0.0001) get (-0.0000) hemorrhoids. (-0.0000) that (-0.0001) means (-0.0000) one (-0.0001) out (-0.0000) of (-0.0001) five (-0.0000) adults (-0.0000) you (0.0000) know (0.0001) could (0.0001) have (-0.0001) them. (-0.0000) now (0.0001) you (0.0002) have (0.0000) help, (0.0001) you (0.0004) have (-0.0000) tucks. (0.0000) cleanse (0.0000) and (-0.0000) relieve (0.0000) discomfort (-0.0000) with (-0.0002) tucks (0.0001) medicated (0.0001) cooling (-0.0000) pads. (-0.0001) they (-0.0002) are (-0.0002) ph (-0.0001) balanced, (0.0001) hypo- (0.0001) allergenic, (0.0000) dye- (-0.0001) free, (0.0000) and (-0.0001) biodegradable (-0.0001) when (0.0000) flushed. (0.0003) also (0.0002) suitable (-0.0001) for (0.0002) : (-0.0001) hygienic (-0.0001) careuse (-0.0001) tucks (-0.0000) medicated (0.0003) cooling (0.0000) pads (0.0000) daily (-0.0001) to (-0.0001) cleanse (-0.0000) outer (0.0001) rectal (0.0000) and (-0.0001) / (-0.0002) or (-0.0000) vaginal (-0.0001) areas. (0.0002) as (-0.0001) a (0.0004) moist (0.0001) compressfold (-0.0000) and (-0.0001) use (-0.0002) as (-0.0000) a (0.0007) moist (0.0001) compress (0.0000) on (-0.0000) inflamed (0.0000) tissue. (0.0004) tucks (0.0001) medicated (0.0000) cooling (0.0001) pads (0.0000) are (-0.0000) particularly (0.0001) helpful (-0.0001) in (0.0001) relieving (0.0000) discomfort (-0.0001) following (-0.0002) childbirth, (-0.0001) rectal (-0.0001) or (0.0001) vaginal (-0.0000) surgery. (-0.0001) questions? (0.0001) 1- (-0.0001) 800- (-0.0001) 223- (-0.0001) 0182 (-0.0000)
~~~~~~

**Node-1.8** (global 1680):

~~~~~~text
product (0.0009) from (0.0002) amazon (0.0013) platform (-0.0001) with (-0.0003) title (0.0013) and (-0.0003) content (0.0006) : (0.0012) title (0.0006) : (0.0005) pampers (0.0002) swaddlers (0.0004) diapers (0.0005) size (0.0004) 1 (0.0011) economy (0.0003) pack (0.0012) plus (0.0005) 216 (0.0013) count. (0.0008) content (0.0005) : (-0.0005) none (-0.0005)
~~~~~~

**Node-1.9** (global 1687):

~~~~~~text
product (-0.0012) from (0.0002) amazon (-0.0002) platform (-0.0006) with (-0.0001) title (0.0001) and (-0.0004) content (0.0001) : (0.0005) title (0.0004) : (0.0000) always (-0.0003) maxi (0.0001) overnight (-0.0006) extra (-0.0003) heavy (-0.0004) flow (-0.0003) pads (0.0002) with (-0.0001) wings, (-0.0003) 40 (-0.0007) count. (0.0001) content (0.0003) : (-0.0005) our (0.0005) best (0.0002) all (-0.0005) night (0.0001) protection! (0.0001) the (-0.0005) always (0.0003) overnight (-0.0002) extra (0.0000) heavy (-0.0000) flow (-0.0002) pad, (-0.0002) with (-0.0000) it (-0.0002) ' (0.0000) s (-0.0002) unique (-0.0000) heavy (0.0004) nights (0.0002) design, (0.0003) is (0.0001) our (0.0006) longest (0.0004) pad (-0.0000) ( (-0.0001) 15 (0.0006) inches (-0.0003) ), (0.0001) with (0.0000) an (0.0002) extra (0.0000) wide (-0.0001) back (-0.0002) for (-0.0000) night (0.0002) protection, (-0.0004) and (0.0000) the (-0.0002) raised (0.0004) core (0.0003) helps (-0.0003) fit (0.0003) your (0.0005) body. (-0.0000)
~~~~~~

**Node-1.10** (global 5164):

~~~~~~text
product (-0.0005) from (0.0005) amazon (-0.0003) platform (-0.0008) with (0.0006) title (-0.0002) and (-0.0002) content (0.0001) : (0.0005) title (-0.0004) : (-0.0001) nelsons (0.0001) bach (-0.0003) hemorrhoid (0.0001) cream (-0.0003) 1 (0.0008) oz.. (-0.0002) content (-0.0005) : (-0.0003) nelsons (-0.0001) hemorrhoid (-0.0001) cream (-0.0007) is (0.0001) a (-0.0009) soothing (-0.0005) cream (-0.0002) formulated (-0.0006) from (-0.0003) fresh (-0.0002) plant (-0.0001) tinctures (0.0001) to (-0.0001) help (-0.0001) alleviate (-0.0004) the (-0.0003) discomfort (-0.0005) of (0.0002) hemorrhoids. (-0.0001)
~~~~~~

**Node-2** (global 13353):

~~~~~~text
product (0.0317) from (-0.0154) amazon (0.0142) platform (-0.0108) with (-0.0018) title (-0.0047) and (0.0050) content (0.0233) : (-0.0037) title (-0.0101) : (-0.0030) lansinoh (-0.0038) soothies (0.0212) gel (0.0220) pads, (0.0048) 2 (0.0181) count. (-0.0011) content (0.0205) : (-0.0121) none (-0.0085)
~~~~~~

**Node-2.1** (global 1627):

~~~~~~text
product (0.0002) from (-0.0005) amazon (0.0007) platform (0.0004) with (-0.0003) title (-0.0001) and (-0.0003) content (0.0001) : (-0.0003) title (-0.0001) : (0.0001) sugar (-0.0002) booger (0.0002) & (-0.0001) quot (-0.0000) ; (-0.0006) numbers (0.0003) & (0.0002) quot (0.0002) ; (0.0002) closet (-0.0001) dividers (0.0001) set (0.0001) of (0.0002) 5. (0.0000) content (0.0001) : (-0.0003) one (0.0003) of (-0.0001) the (-0.0002) latest (0.0001) collections (0.0001) from (-0.0002) sugarbooger (0.0001) is (0.0000) both (0.0000) charming (-0.0001) and (-0.0003) educational (0.0004) and (-0.0000) provides (0.0002) stylish (0.0000) accessories (0.0000) that (-0.0000) can (0.0000) help (0.0001) kids (-0.0002) learn (-0.0000) their (-0.0001) 1- (-0.0002) 2- (-0.0002) 3 (0.0000) ' (-0.0001) s. (0.0001) set (-0.0001) of (0.0001) 5 (-0.0003) closet (-0.0002) divider (-0.0003) set (0.0002) features (0.0004) the (-0.0004) numbers (-0.0000) collection (0.0003) graphics (0.0001) and (-0.0001) includes (-0.0003) three (0.0000) sets (-0.0001) of (0.0004) stickers (-0.0003) to (-0.0001) organize (-0.0002) by (-0.0000) age (0.0001) range, (-0.0000) clothing (0.0003) type, (-0.0002) or (0.0001) day (-0.0000) of (-0.0002) the (0.0002) week. (-0.0002) plastic, (-0.0002) measures (0.0003) 6 (-0.0002) x (0.0001) 3 (0.0001) " (-0.0001) overall. (0.0006) perfect (-0.0002) shower (-0.0001) gift. (0.0027) winner (0.0005) of (0.0003) mom (0.0001) ' (0.0003) s (-0.0002) best (-0.0001) award (0.0000) 2008. (0.0009)
~~~~~~

**Node-3** (global 13618):

~~~~~~text
product (0.0109) from (0.0129) amazon (0.0027) platform (0.0114) with (0.0026) title (0.0154) and (-0.0019) content (0.0136) : (0.0045) title (0.0231) : (0.0115) charlie (0.0220) banana (0.0198) nursing (0.0051) pads, (0.0082) white. (0.0109) content (0.0225) : (-0.0004) washable, (0.0087) reusable (0.0027) breast (0.0150) pads (0.0055)
~~~~~~

**Node-4** (global 13619):

~~~~~~text
product (-0.0015) from (-0.0040) amazon (-0.0079) platform (-0.0003) with (-0.0039) title (0.0064) and (-0.0025) content (-0.0008) : (0.0028) title (0.0014) : (0.0036) waterproof (-0.0018) crib (0.0001) mattress (-0.0008) pad- (-0.0016) soft (0.0007) fitted (0.0028) quilted (-0.0010) cover (0.0040) pads (0.0032) for (0.0012) baby- (0.0011) best (0.0007) protectors (0.0015) liner (0.0008) sheet (0.0023) toppers (0.0035) helps (0.0002) infants (-0.0006) from (0.0013) bed (0.0033) bugs, (-0.0007) allergies- (0.0004) long (0.0018) lasting (-0.0005) size (0.0004) fits (-0.0010) all (-0.0006) cribs (-0.0002) breathable (0.0038) and (-0.0067) absorbent- (-0.0005) extremely (0.0017) healthy (0.0043) choice (0.0030) for (-0.0025) you (0.0015) toddler. (0.0014) content (0.0038) : (-0.0059) waterproof (0.0020) crib (0.0006) pads (0.0033) that (-0.0010) lets (0.0001) your (0.0025) baby (0.0051) sleeps (0.0013) better (0.0021) and (-0.0013) so (0.0007) do (0.0009) youtailored (0.0026) made (0.0016) to (-0.0008) suit (0.0053) caring (0.0012) mothers (0.0020) who (-0.0008) want (0.0026) the (0.0015) best- (0.0002) made (0.0027) to (0.0006) be (0.0040) strong (0.0045) and (-0.0013) long (0.0029) lasting (-0.0001) with (-0.0012) comfort (0.0058) in (-0.0024) mind- (0.0006) keeps (0.0041) your (0.0037) baby (0.0079) warm (0.0005) thru (0.0041) the (0.0031) extra (0.0024) padding (0.0024) and (-0.0003) absorption- (0.0040) safety (0.0029) from (0.0023) allergies (0.0007) and (0.0012) dust (0.0032) mitesgreat (0.0022) design (0.0053) suits (0.0046) all (0.0000) cribs (0.0012) fitted (-0.0001) easilywith (0.0031) a (0.0033) super (0.0003) soft (-0.0033) padding (-0.0006) and (-0.0003) ultra (0.0036) absorbent (0.0004) materials (0.0013) whilst (0.0061) breathable (-0.0041) all (-0.0004) to (-0.0009) keep (0.0001) the (0.0030) baby (-0.0031) safe (0.0010) and (-0.0007) warm, (0.0024) this (0.0058) waterproof (0.0001) crib (0.0047) pad (-0.0010) has (0.0027) it (0.0023) all. (0.0087) the (0.0025) elastic (-0.0018) under (-0.0007) bottom (0.0021) of (-0.0004) the (0.0018) pad (0.0029) allows (0.0003) this (0.0035) to (0.0001) shape (0.0027) and (-0.0008) mold (0.0019) to (0.0010) any (0.0004) sized (0.0019) crib (0.0041) so (0.0021) you (-0.0001) wont (0.0030) purchase (0.0046) the (0.0039) wrong (0.0036) size, (0.0039) also (0.0001) be (0.0025) able (0.0041) to (-0.0001) remove (0.0017) it (0.0011) fast (0.0025) and (-0.0021) place (0.0015) it (0.0012) in (0.0003) washing (-0.0005) machine (0.0036) this (0.0039) will (0.0032) not (0.0018) fall (0.0029) apart (0.0009) like (0.0023) other (0.0018) brands. (0.0087) apart (0.0011) from (0.0011) this (0.0022) your (0.0016) child (0.0045) will (0.0039) be (0.0029) safe (0.0018) from (-0.0027) health (0.0025) issues (-0.0007) and (-0.0022) that (-0.0001) to (0.0003) us (0.0039) is (0.0033) the (0.0015) main (0.0029) thing (0.0023) here (0.0025) and (-0.0027) in (-0.0002) the (0.0017) mind (-0.0014) of (-0.0020) caring (-0.0009) families. (0.0037) why (-0.0011) choose (0.0020) this (0.0028) product (0.0063) over (0.0008) other (0.0010) brands- (0.0046) you (0.0048) get (0.0024) exactly (0.0037) what (-0.0001) we (0.0019) say (0.0029) here (0.0029) washable (0.0014) and (-0.0017) doesn (0.0032) ' (0.0013) t (0.0021) tear (0.0069) in (-0.0016) the (0.0002) wash- (0.0034) the (0.0017) added (0.0028) padding (0.0027) to (-0.0004) the (-0.0012) quilt (-0.0047) making (0.0020) it (0.0027) softer (0.0027) for (-0.0003) the (0.0018) child (0.0059) also (-0.0004) keeping (-0.0027) the (0.0036) warmth (0.0035) in (-0.0023) so (0.0017) they (0.0027) don (0.0004) ' (0.0011) t (0.0025) get (0.0046) cold- (0.0047) keep (0.0029) its (0.0047) size (0.0025) with (0.0004) no (0.0049) shrinkage (0.0052) doesn (0.0004) ' (0.0020) t (0.0004) ball (0.0034) up (0.0020) and (0.0019) also (0.0016) doesn (0.0025) ' (-0.0001) t (0.0024) leak (0.0041) onto (0.0034) the (0.0024) mattressif (0.0083) the (-0.0028) product (0.0000) is (0.0051) not (0.0032) what (-0.0042) we (0.0064) have (-0.0050) explain (0.0048) send (-0.0029) it (0.0005) back, (0.0016) it (0.0019) comes (0.0016) with (-0.0023) a (0.0027) 5 (-0.0020) year (0.0040) free (0.0023) replacement (0.0047) guaranteeclick (0.0007) the (0.0053) button (-0.0007) at (0.0005) the (0.0038) top (0.0041) of (0.0032) this (0.0041) page (-0.0004) to (0.0000) get (-0.0002) the (0.0031) best (0.0031) possible (0.0031) quality (0.0059) waterproof (0.0018) crib (0.0050) mattress (0.0044) cover (0.0129) now (-0.0053)
~~~~~~

**Node-5** (global 13620):

~~~~~~text
product (0.0165) from (0.0121) amazon (-0.0079) platform (0.0149) with (0.0049) title (0.0098) and (-0.0037) content (0.0232) : (-0.0036) title (0.0153) : (0.0089) lansinoh (0.0042) breastmilk (0.0029) storage (0.0049) bags, (0.0079) 25- (0.0094) count (0.0124) boxes (0.0125) ( (0.0070) pack (0.0165) of (0.0076) 3 (0.0121) ). (0.0106) content (0.0076) : (0.0148) none (0.0299)
~~~~~~

**Node-6** (global 13621):

~~~~~~text
product (0.0230) from (-0.0008) amazon (0.0030) platform (0.0054) with (0.0042) title (0.0126) and (0.0043) content (0.0248) : (-0.0081) title (0.0092) : (0.0040) philips (0.0254) avent (0.0072) day (0.0036) disposable (0.0077) breast (0.0060) pads, (0.0065) 60- (0.0013) count. (0.0168) content (0.0134) : (-0.0071) none (0.0295)
~~~~~~
