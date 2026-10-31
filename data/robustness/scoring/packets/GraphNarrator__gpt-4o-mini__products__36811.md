# Reference packet: GraphNarrator__gpt-4o-mini__products__36811

- Method: GraphNarrator; configuration: gpt-4o-mini; dataset: products; target node: 36811
- Explanation source: `./robustness_2026-10-30/graphnarrator_gpt4omini/generated_expls-601/138.json` (messages[assistant])
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

- ROOT (Vogmask)
  - Node-1 (Child Life liquid calcium)
    - Node-1.1 (Child Life probiotics)
    - Node-1.2 (Amerifit culturelle probiotics)
    - Node-1.3 (Thinkbaby cereal bowl)
    - Node-1.4 (La Mer eye concentrate)
    - Node-1.5 (Thermos Funtainer)

1. **Word-Level Evaluation:**

The ROOT node contains keywords with notable saliency scores such as "title" (0.11), "mask" (0.03), "pink" (0.05), "dust" (0.05), and "filtering" (0.06). These terms suggest that the product is a stylish and functional mask, which is primarily associated with health and wellness rather than traditional book categories. The presence of phrases like "stay healthy" and "maximum protection" also indicates a focus on health-related products. 

2. **Graph-Level Aggregation:**

Node-1 (Child Life liquid calcium) features keywords like "calcium," "magnesium," and "healthy," which are relevant to children's health but do not directly relate to books. The subsequent nodes (Node-1.1 to Node-1.5) include various health and wellness products, such as probiotics and feeding items, which further emphasize a focus on health rather than literature. The absence of any keywords or phrases related to reading, education, or literature across the entire graph reinforces the notion that the classification label of "Books" may not be appropriate based on the content.

### Free-Text Explanation
```markdown
The classification of ROOT into "Books" is questionable given the keywords and co-purchase neighborhood.

ROOT: The keywords "mask" (0.03), "filtering" (0.06), and "stay healthy" indicate that this product is a stylish and functional mask designed for health protection, which does not align with the "Books" category.
  - Node-1: The Child Life liquid calcium (keywords: "calcium" (0.01), "healthy" (0.02)) is a health supplement aimed at children, further distancing the product from the book category.
    - Node-1.1: Child Life probiotics (keywords: "probiotics" (0.00), "health" (0.00)) continue the health theme, lacking any relation to books.
    - Node-1.2: Amerifit culturelle probiotics (keywords: "probiotics" (0.00), "healthy" (0.00)) also focus on children's health, reinforcing the non-book context.
    - Node-1.3: The Thinkbaby cereal bowl (keywords: "bowl" (0.00), "feeding" (0.00)) is a feeding accessory, further emphasizing the health and wellness theme.
    - Node-1.4: La Mer eye concentrate (keywords: "eye" (0.00), "treatment" (0.00)) is a skincare product, again unrelated to books.
    - Node-1.5: The Thermos Funtainer (keywords: "stainless" (0.00), "bottle" (0.00)) is a drink container, which does not connect to literature.

In summary, the ROOT's keywords strongly indicate a health-related product, and the entire co-purchase neighborhood consists of health and wellness items, providing insufficient evidence for the "Books" classification.
```
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/138.json`).

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
<verbalized-graph>ROOT: product(-0.01) amazon(-0.06) platform(-0.01) title(0.08) content(-0.04) title(0.11) vogmask(0.01) microfiber(0.00) filtering(-0.03) mask(0.03) pink(0.05) roses.(-0.03) content(0.02) stay(0.02) healthy(0.01) keep(-0.01) airborne(-0.09) particles(-0.13) lungs(-0.02) vogmask,(0.01) first(0.03) dust(-0.00) masks(-0.03) designed(0.07) stylish,(0.02) comfortable(-0.00) reusable.(-0.00) choice(0.01) high-(0.03) tech(0.03) microfiber(0.02) organic(-0.00) cotton,(0.04) comfortable,(0.02) reusable(0.03) masks(0.02) combine(0.03) protection(0.03) style(0.05) like(0.00) never(0.05) before.(0.05) whether(-0.01) seek(0.05) shelter(0.04) perils(0.03) modern(0.06) life(0.04) want(0.05) relief(0.04) allergies,(0.05) vogmask(0.05) covered.(0.00) vogmask(0.07) world(0.06) first(0.05) stylish(0.04) filtering(0.06) dust(0.02) mask,(0.05) made(0.05) finest(0.02) materials(0.01) designed(0.03) comfortable(0.03) dust(0.06) mask(0.01) ever(0.02) providing(-0.02) maximum(-0.00) protection(-0.01) airborne(-0.00) particles.(0.01) 
Node-1: product(-0.01) amazon(0.02) platform(0.00) title(-0.01) content(-0.01) title(0.00) child(-0.00) life(-0.01) liquid(0.01) calcium(-0.02) magnesium,(-0.02) natural(-0.00) orange(-0.01) flavor(-0.00) plastic(-0.00) bottle,(0.00) 16-(-0.01) fl.(-0.00) oz..(0.00) content(0.01) liquid(-0.01) calcium(-0.02) magnesium(-0.02) provides(0.00) two(-0.00) essential(0.00) minerals(-0.01) combined(-0.01) vitamin(-0.02) zinc(-0.03) balanced,(-0.01) absorbable,(-0.00) great(0.00) tasting(-0.01) formula.(-0.02) primary(-0.00) nutrients(-0.00) required(-0.00) supporting(-0.01) child(-0.01) healthy(-0.02) bone(-0.01) growth(0.01) development.(-0.01) child(0.00) grows(0.01) develops,(0.00) calcium(-0.00) abundant(0.00) mineral(0.00) found(0.00) body,(-0.00) comprising(0.02) 1.(0.01) 5-(0.01) 2(0.00) total(0.01) body(0.01) weight(0.01) ),(-0.00) 99(0.00) total(0.01) calcium(0.01) found(0.01) bones(0.01) teeth.(-0.01) optimum(-0.00) absorption(0.01) utilization,(-0.01) calcium(0.00) combined(-0.01) magnesium,(-0.02) vit(0.00) zinc.(-0.00) nutrients(-0.04) help(0.02) support(-0.00) establish(-0.01) foundation,(0.01) child(0.03) structural(0.01) growth(0.00) integrity.(0.00) 
Node-1.1: product(-0.01) amazon(0.00) platform(-0.00) title(-0.00) content(0.00) title(-0.00) child(-0.00) life(-0.00) probiotics(-0.00) plus(-0.00) colostrum(0.00) chewable(0.00) tablets,(0.00) mixed(-0.00) berry(-0.00) flavor,(0.00) 90(-0.00) count.(0.00) content(-0.00) probiotics(-0.00) colostrum(0.00) contains(0.00) stable(-0.00) strains(-0.00) probiotics(0.00) include(-0.00) lactobacillus(-0.00) acidophilus(0.00) bifidobacterium(-0.00) breve(-0.00) bifobacterium(0.00) longum,(0.00) optimum(0.00) intestinal(0.00) health(0.00) immune(0.00) system(0.00) support.(-0.00) 
Node-1.2: product(0.00) amazon(-0.00) platform(-0.00) title(0.00) content(0.00) title(0.00) amerifit(0.00) culturelle(0.00) probiotics(0.00) kids,(0.00) 30(0.00) count.(0.00) content(0.00) developed(-0.00) science,(0.00) trusted(0.00) momsthe(0.00) ingredient(0.00) culturelle(-0.00) kids(0.00) probiotics(-0.00) clinically(0.00) proven(0.00) help(0.00) reduce(-0.00) occasional(-0.00) tummy(0.00) troubles(0.00) like(0.00) gas,(0.00) bloating,(0.00) diarrhea(-0.00) helping(-0.00) restore(-0.00) balance(0.00) good(0.00) not-(0.00) so-(0.00) good(0.00) bacteria(-0.00) digestive(0.00) systems.(0.00) taken(-0.00) regularly,(0.00) actually(-0.00) helps(-0.00) child(0.00) rsquo(0.00) digestive(0.00) immune(-0.00) systems(0.00) work(0.00) better.(0.01) happy(-0.00) tummies,(0.00) healthy(0.00) kids,(0.00) relaxed(0.00) parents.(0.01) support(-0.00) kids(-0.00) rsquo(0.00) natural(-0.00) defenses(0.00) keep(0.00) digestive(0.00) system(0.00) happy(0.00) culturelle(0.00) probiotics.(0.00) benefits(-0.01) culturelle(-0.00) kids(-0.00) packets(-0.00) lactobacillus(0.00) ggcontains(0.00) 100(0.00) naturally(0.00) sourced(0.00) lactobacillus(0.00) gg(0.00) ndash(0.00) 1(0.00) clinically(0.00) studied(0.00) probiotic.(0.01) dagger(0.00) dagger(-0.01) helps(0.00) support(-0.00) kids(0.00) rsquo(0.00) natural(0.00) defense(0.00) systems(0.00) helps(0.00) reduce(0.00) occasional(0.00) digestive(0.00) upset(0.00) easy(0.00) take(0.00) especially(-0.00) little(0.00) ones(0.00) flavorless,(0.00) add(0.00) cool(0.00) liquid(0.00) fooddairy(0.00) gluten(-0.00) free(0.00) 
Node-1.3: product(-0.00) amazon(-0.00) platform(-0.00) title(0.00) content(0.00) title(0.00) thinkbaby(0.00) bpa(0.00) free(0.00) cereal(-0.00) bowl,(0.00) orange.(-0.00) content(0.00) tremendous(0.00) requests,(0.00) thinkbaby(0.00) presents(-0.00) feeding(0.00) set(0.00) items(0.00) separates.(0.00) designed(0.00) free(0.00) toxic(0.00) chemicals(0.00) bisphenol-(0.00) bpa(0.00) ),(0.00) phthalates,(0.00) melamine,(0.00) nitrosamines,(0.00) lead,(0.00) pvc,(0.00) biologically(0.00) harmful(0.00) chemicals.(0.00) thinkbaby(0.00) bowl(0.00) perfect(-0.00) cereal,(0.00) soup(0.00) mealtime(0.00) snack.(0.00) interior(0.00) made(0.00) food(0.00) grade(0.00) stainless(-0.00) steel,(0.00) insulated(0.00) polypropylene.(0.00) bowl(-0.00) also(0.00) outfitted(0.00) lid,(0.00) made(0.00) slightly(0.00) orange(-0.00) easy(0.00) locate(0.00) lid(0.00) drawer.(0.00) perfect(-0.00) beginning(0.00) solid(0.00) food(-0.00) eater(0.00) adults.(-0.00) 
Node-1.4: product(0.00) amazon(0.00) platform(0.00) title(0.00) content(0.01) title(0.00) la(0.00) mer(0.00) eye(-0.00) concentrate(0.01) 3ml(-0.00) x(0.00) 5(-0.00) 15ml.(0.00) content(0.01) ultraluxe(0.00) eye(0.00) treatment(-0.00) dissolves(-0.00) appearance(0.00) lines(-0.00) wrinkles,(-0.00) dark(-0.00) circles(-0.00) puffiness.(-0.00) 
Node-1.5: product(-0.00) amazon(-0.00) platform(0.00) title(0.01) content(0.01) title(0.01) thermos(-0.00) funtainer(0.00) stainless(0.00) steel(0.01) 10(0.00) oz(0.00) leak-(0.01) proof(0.00) straw(0.01) bottle-(0.01) mickey(0.01) mouse.(0.01) content(0.01) thermos(-0.00) funtainer(0.00) stainless(0.00) steel(0.01) 10(0.01) oz(-0.00) leak-(0.01</verbalized-graph>

### Classification Label
Books

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 36811
- Title: Vogmask Microfiber Filtering Mask: Pink Roses
- True class (canonical `y`): **Beauty**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Health & Personal Care**
- Prediction recorded by this method's pipeline: **Books**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Vogmask Microfiber Filtering Mask: Pink Roses. Content: Stay healthy and keep airborne particles out of your lungs with Vogmask, the first dust masks designed to be stylish, comfortable and reusable. With the choice of high-tech microfiber or organic cotton, these comfortable, reusable masks combine protection and style like never before. Whether you seek shelter from the perils of modern life or just want relief from allergies, Vogmask has you covered. Vogmask is the world's first stylish filtering dust mask, made from the finest materials and designed to be the most comfortable dust mask ever while providing maximum protection from airborne particles.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 8361 | Health & Personal Care | Child Life Liquid Calcium/Magnesium,Natural Orange Flavor Plastic Bottle, 16-Fl. Oz. |

### 2-hop (shortest distance exactly 2): 6 nodes

| node id | true class | title |
|---|---|---|
| 983 | Health & Personal Care | Child Life Probiotics Plus Colostrum Chewable Tablets, Mixed Berry Flavor, 90 Count |
| 8389 | Health & Personal Care | Amerifit Culturelle Probiotics for Kids, 30 Count |
| 36810 | Baby | thinkbaby BPA Free Cereal Bowl, Orange |
| 36812 | Beauty | La Mer The Eye Concentrate 3ml x 5 = 15ml |
| 36813 | Baby | Thermos FUNtainer Stainless Steel 10 oz Leak-Proof Straw Bottle - Mickey Mouse |
| 36814 | Beauty | Aveeno Eczema Therapy  Bath Treatment, 3 Count (Pack of 2) |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/138.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Books**, ground truth = **Beauty**.
The verbalized graph is 7446 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 36811 | 117 | 0.1102 | yes |
| Node-1 | 1 | 8361 | 141 | 0.0412 | yes |
| Node-1.1 | 2 | 983 | 53 | 0.0054 | yes |
| Node-1.2 | 3 | 8389 | 174 | 0.0059 | yes |
| Node-1.3 | 4 | 36810 | 111 | 0.0056 | yes |
| Node-1.4 | 5 | 36812 | 39 | 0.0071 | yes |
| Node-1.5 | 6 | 36813 | 37 | 0.0140 | yes |
| Node-1.6 | 7 | 36814 | 134 | 0.0052 | no |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->Node-1.6, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, Node-1.6->Node-1, ROOT->Node-1

### Tokens and scores

**ROOT** (global 36811):

~~~~~~text
product (-0.0120) from (0.0086) amazon (-0.0640) platform (-0.0112) with (-0.0138) title (0.0814) and (0.0177) content (-0.0418) : (0.0346) title (0.1102) : (0.0347) vogmask (0.0050) microfiber (0.0045) filtering (-0.0296) mask (0.0291) : (0.0684) pink (0.0514) roses. (-0.0281) content (0.0163) : (0.0182) stay (0.0224) healthy (0.0086) and (-0.0014) keep (-0.0146) airborne (-0.0876) particles (-0.1326) out (0.0397) of (0.0155) your (-0.0818) lungs (-0.0189) with (0.0149) vogmask, (0.0120) the (-0.0512) first (0.0290) dust (-0.0029) masks (-0.0307) designed (0.0680) to (0.0075) be (0.0155) stylish, (0.0203) comfortable (-0.0011) and (0.0125) reusable. (-0.0028) with (0.0130) the (-0.0006) choice (0.0084) of (0.0152) high- (0.0331) tech (0.0342) microfiber (0.0157) or (0.0168) organic (-0.0030) cotton, (0.0404) these (0.0277) comfortable, (0.0208) reusable (0.0282) masks (0.0195) combine (0.0304) protection (0.0293) and (0.0439) style (0.0497) like (0.0023) never (0.0485) before. (0.0467) whether (-0.0064) you (-0.0332) seek (0.0468) shelter (0.0400) from (0.0305) the (-0.0207) perils (0.0314) of (0.0156) modern (0.0602) life (0.0362) or (0.0363) just (0.0423) want (0.0519) relief (0.0444) from (0.0427) allergies, (0.0477) vogmask (0.0509) has (0.0580) you (-0.0248) covered. (0.0023) vogmask (0.0724) is (0.0481) the (-0.0206) world (0.0607) ' (0.0417) s (0.0572) first (0.0499) stylish (0.0363) filtering (0.0560) dust (0.0212) mask, (0.0523) made (0.0482) from (0.0189) the (-0.0036) finest (0.0204) materials (0.0100) and (0.0365) designed (0.0293) to (0.0063) be (0.0166) the (0.0006) most (0.0264) comfortable (0.0256) dust (0.0570) mask (0.0112) ever (0.0189) while (0.0081) providing (-0.0201) maximum (-0.0026) protection (-0.0135) from (0.0223) airborne (-0.0048) particles. (0.0123)
~~~~~~

**Node-1** (global 8361):

~~~~~~text
product (-0.0052) from (-0.0473) amazon (0.0230) platform (0.0006) with (-0.0242) title (-0.0058) and (-0.0045) content (-0.0078) : (-0.0212) title (0.0038) : (-0.0003) child (-0.0039) life (-0.0064) liquid (0.0064) calcium (-0.0153) / (0.0065) magnesium, (-0.0175) natural (-0.0001) orange (-0.0054) flavor (-0.0005) plastic (-0.0001) bottle, (0.0000) 16- (-0.0132) fl. (-0.0007) oz.. (0.0029) content (0.0079) : (0.0040) liquid (-0.0086) calcium (-0.0171) with (-0.0019) magnesium (-0.0151) provides (0.0041) these (-0.0046) two (-0.0007) essential (0.0016) minerals (-0.0114) combined (-0.0103) with (-0.0094) vitamin (-0.0242) d (-0.0046) and (-0.0066) zinc (-0.0330) in (-0.0069) a (-0.0039) balanced, (-0.0064) very (-0.0010) absorbable, (-0.0049) great (0.0045) tasting (-0.0062) formula. (-0.0225) these (0.0103) are (0.0004) the (-0.0110) primary (-0.0014) nutrients (-0.0035) required (-0.0030) for (-0.0136) supporting (-0.0119) your (-0.0307) child (-0.0086) ' (-0.0101) s (0.0051) healthy (-0.0155) bone (-0.0079) growth (0.0107) and (-0.0030) development. (-0.0115) as (0.0066) your (-0.0061) child (0.0034) grows (0.0139) and (0.0015) develops, (0.0029) calcium (-0.0029) is (0.0036) the (-0.0047) most (0.0085) abundant (0.0002) mineral (0.0044) found (0.0041) in (0.0012) their (-0.0018) body, (-0.0003) ( (0.0056) comprising (0.0167) 1. (0.0090) 5- (0.0068) 2 (0.0042) % (0.0200) of (-0.0060) total (0.0109) body (0.0080) weight (0.0129) ), (-0.0032) with (0.0145) 99 (0.0029) % (0.0189) of (-0.0010) the (-0.0020) total (0.0091) calcium (0.0109) being (0.0124) found (0.0144) in (0.0146) the (0.0045) bones (0.0139) and (0.0118) teeth. (-0.0061) for (0.0048) optimum (-0.0006) absorption (0.0094) and (0.0041) utilization, (-0.0076) calcium (0.0014) should (-0.0366) be (-0.0024) combined (-0.0083) with (0.0213) magnesium, (-0.0227) vit (0.0017) d (0.0039) and (-0.0058) zinc. (-0.0008) these (0.0412) nutrients (-0.0430) help (0.0156) support (-0.0047) and (-0.0164) establish (-0.0080) the (0.0109) very (-0.0256) foundation, (0.0061) for (0.0208) your (-0.0073) child (0.0280) ' (-0.0086) s (0.0005) structural (0.0119) growth (0.0010) and (-0.0068) integrity. (0.0030)
~~~~~~

**Node-1.1** (global 983):

~~~~~~text
product (-0.0060) from (-0.0006) amazon (0.0011) platform (-0.0006) with (-0.0007) title (-0.0027) and (0.0006) content (0.0011) : (-0.0005) title (-0.0019) : (-0.0015) child (-0.0001) life (-0.0013) probiotics (-0.0015) plus (-0.0037) colostrum (0.0004) chewable (0.0002) tablets, (0.0004) mixed (-0.0011) berry (-0.0010) flavor, (0.0012) 90 (-0.0040) count. (0.0004) content (-0.0010) : (0.0019) probiotics (-0.0001) with (-0.0017) colostrum (0.0014) contains (0.0003) the (-0.0026) most (0.0012) stable (-0.0009) strains (-0.0011) of (0.0013) probiotics (0.0005) which (-0.0014) include (-0.0019) : (0.0054) lactobacillus (-0.0003) acidophilus (0.0004) bifidobacterium (-0.0000) breve (-0.0002) & (0.0008) bifobacterium (0.0007) longum, (0.0005) for (0.0005) optimum (0.0010) intestinal (0.0005) health (0.0018) & (0.0018) immune (0.0021) system (0.0020) support. (-0.0020)
~~~~~~

**Node-1.2** (global 8389):

~~~~~~text
product (0.0002) from (-0.0001) amazon (-0.0011) platform (-0.0002) with (-0.0014) title (0.0017) and (0.0001) content (0.0003) : (0.0011) title (0.0002) : (0.0017) amerifit (0.0008) culturelle (0.0007) probiotics (0.0017) for (0.0006) kids, (0.0008) 30 (0.0007) count. (0.0044) content (0.0003) : (0.0022) developed (-0.0002) with (-0.0022) science, (0.0029) trusted (0.0006) by (0.0005) momsthe (0.0005) ingredient (0.0003) in (0.0011) culturelle (-0.0009) kids (0.0005) probiotics (-0.0000) is (0.0005) clinically (0.0009) proven (0.0001) to (-0.0008) help (0.0001) reduce (-0.0002) occasional (-0.0004) tummy (0.0003) troubles (0.0006) like (0.0013) gas, (0.0028) bloating, (0.0009) and (0.0001) diarrhea (-0.0003) by (0.0003) helping (-0.0006) to (-0.0003) restore (-0.0005) the (-0.0033) balance (0.0005) of (0.0007) good (0.0002) and (-0.0000) not- (0.0005) so- (0.0007) good (0.0006) bacteria (-0.0010) in (0.0003) their (0.0008) digestive (0.0001) systems. (0.0041) * (-0.0049) taken (-0.0003) regularly, (0.0000) it (0.0024) actually (-0.0004) helps (-0.0013) your (0.0033) child (0.0000) & (0.0012) rsquo (0.0007) ; (0.0059) s (-0.0006) digestive (0.0001) and (0.0001) immune (-0.0020) systems (0.0016) to (-0.0026) work (0.0006) better. (0.0059) * (-0.0030) happy (-0.0003) tummies, (0.0011) healthy (0.0007) kids, (0.0031) relaxed (0.0016) parents. (0.0056) support (-0.0022) your (0.0042) kids (-0.0029) & (0.0028) rsquo (0.0007) ; (0.0039) natural (-0.0008) defenses (0.0010) and (-0.0001) keep (0.0019) their (0.0028) digestive (0.0007) system (0.0022) happy (0.0004) with (0.0018) culturelle (0.0007) probiotics. (0.0022) benefits (-0.0060) of (-0.0042) culturelle (-0.0021) kids (-0.0015) packets (-0.0023) with (-0.0016) lactobacillus (0.0004) ggcontains (0.0012) 100 (0.0005) % (0.0004) naturally (0.0002) sourced (0.0008) lactobacillus (0.0003) gg (0.0005) & (0.0004) ndash (0.0001) ; (0.0012) the (-0.0048) # (0.0018) 1 (0.0007) most (0.0008) clinically (0.0011) studied (0.0014) probiotic. (0.0052) & (0.0036) dagger (0.0031) ; (0.0028) & (0.0013) dagger (-0.0080) ; (0.0035) helps (0.0015) support (-0.0002) kids (0.0001) & (0.0000) rsquo (0.0004) ; (0.0019) natural (0.0008) defense (0.0006) systems (0.0010) * (0.0029) helps (0.0030) reduce (0.0013) occasional (0.0001) digestive (0.0008) upset (0.0017) * (-0.0014) easy (0.0001) to (0.0008) take (0.0002) ( (0.0003) especially (-0.0006) for (-0.0001) little (0.0009) ones (0.0003) ) (0.0000) flavorless, (0.0010) so (0.0007) you (0.0011) can (0.0002) add (0.0009) to (0.0004) any (0.0002) cool (0.0000) liquid (0.0003) or (0.0014) fooddairy (0.0001) and (0.0004) gluten (-0.0003) free (0.0020)
~~~~~~

**Node-1.3** (global 36810):

~~~~~~text
product (-0.0008) from (-0.0017) amazon (-0.0010) platform (-0.0004) with (0.0011) title (0.0019) and (0.0013) content (0.0026) : (0.0053) title (0.0018) : (0.0030) thinkbaby (0.0001) bpa (0.0001) free (0.0026) cereal (-0.0038) bowl, (0.0016) orange. (-0.0018) content (0.0030) : (0.0019) after (-0.0007) tremendous (0.0019) requests, (0.0008) thinkbaby (0.0006) now (0.0016) presents (-0.0023) its (0.0003) feeding (0.0009) set (0.0011) items (0.0005) as (0.0019) separates. (0.0026) designed (0.0007) free (0.0025) of (0.0012) toxic (0.0001) chemicals (0.0012) such (0.0007) as (0.0015) bisphenol- (0.0011) a (0.0012) ( (0.0015) bpa (0.0009) ), (0.0015) phthalates, (0.0010) melamine, (0.0012) nitrosamines, (0.0007) lead, (0.0018) pvc, (0.0011) and (0.0029) biologically (0.0011) harmful (0.0019) chemicals. (0.0031) the (-0.0009) thinkbaby (0.0017) bowl (0.0001) is (0.0012) perfect (-0.0022) for (0.0028) cereal, (0.0022) soup (0.0001) or (0.0015) any (0.0022) mealtime (0.0014) snack. (0.0005) the (-0.0010) interior (0.0018) is (0.0020) made (0.0002) from (0.0010) food (0.0023) grade (0.0024) stainless (-0.0011) steel, (0.0022) and (0.0005) then (0.0015) insulated (0.0018) with (0.0020) polypropylene. (0.0011) the (0.0001) bowl (-0.0009) is (0.0016) also (0.0025) outfitted (0.0016) with (0.0013) a (0.0008) lid, (0.0003) which (0.0007) we (0.0056) made (0.0015) slightly (0.0012) orange (-0.0002) so (0.0027) that (0.0014) it (0.0016) is (0.0014) easy (0.0019) to (0.0016) locate (0.0029) in (0.0013) the (0.0019) lid (0.0012) drawer. (0.0040) perfect (-0.0019) for (0.0012) the (-0.0008) beginning (0.0003) solid (0.0012) food (-0.0043) eater (0.0006) to (-0.0038) adults. (-0.0007)
~~~~~~

**Node-1.4** (global 36812):

~~~~~~text
product (0.0012) from (0.0024) amazon (0.0037) platform (0.0014) with (0.0028) title (0.0002) and (0.0029) content (0.0057) : (0.0042) title (0.0032) : (0.0044) la (0.0016) mer (0.0024) the (0.0029) eye (-0.0024) concentrate (0.0071) 3ml (-0.0001) x (0.0011) 5 (-0.0021) = (-0.0008) 15ml. (0.0011) content (0.0071) : (-0.0003) an (-0.0017) ultraluxe (0.0008) eye (0.0036) treatment (-0.0026) that (0.0027) dissolves (-0.0004) the (0.0007) appearance (0.0003) of (-0.0004) lines (-0.0009) and (-0.0016) wrinkles, (-0.0001) dark (-0.0034) circles (-0.0008) and (-0.0005) puffiness. (-0.0012)
~~~~~~

**Node-1.5** (global 36813):

~~~~~~text
product (-0.0006) from (0.0031) amazon (-0.0006) platform (0.0015) with (0.0064) title (0.0077) and (0.0025) content (0.0103) : (0.0016) title (0.0140) : (0.0036) thermos (-0.0019) funtainer (0.0024) stainless (0.0019) steel (0.0085) 10 (0.0034) oz (0.0009) leak- (0.0078) proof (0.0047) straw (0.0094) bottle- (0.0057) mickey (0.0069) mouse. (0.0056) content (0.0105) : (0.0054) thermos (-0.0001) funtainer (0.0024) stainless (0.0007) steel (0.0111) 10 (0.0058) oz (-0.0042) leak- (0.0081) proof (0.0036) straw (0.0100) bottle- (0.0048) mickey (-0.0033) mouse (0.0069)
~~~~~~

**Node-1.6** (global 36814):

~~~~~~text
product (0.0027) from (-0.0005) amazon (0.0028) platform (0.0025) with (0.0017) title (0.0012) and (0.0016) content (0.0026) : (0.0008) title (-0.0002) : (0.0014) aveeno (0.0012) eczema (0.0003) therapy (0.0015) bath (0.0012) treatment, (0.0008) 3 (-0.0008) count (-0.0002) ( (0.0012) pack (0.0021) of (0.0000) 2 (-0.0004) ). (-0.0018) content (0.0041) : (0.0002) aveeno (0.0006) eczema (0.0004) therapy (0.0014) bath (0.0006) treatment. (0.0012) effectively (-0.0014) relieves (0.0007) the (-0.0017) itch (0.0008) associated (0.0005) with (0.0006) minor (0.0002) skin (0.0007) irritations (0.0009) such (0.0006) as (0.0006) eczema, (0.0008) rashes (-0.0002) and (0.0017) insect (0.0018) bites. (0.0006) made (0.0014) of (0.0004) 100 (-0.0001) % (0.0004) pure (0.0008) colloidal (0.0003) oatmeal, (0.0004) a (0.0009) long (0.0011) recognized (0.0008) ingredient (0.0015) that (0.0008) relieves (0.0010) itching (0.0009) naturally, (-0.0005) aveeno (-0.0000) eczema (0.0006) therapy (0.0021) bath (0.0005) treatment (0.0008) disperses (0.0006) in (0.0013) your (0.0003) bathwater (0.0017) to (0.0003) treat (0.0006) itchy, (0.0007) dry, (0.0011) or (0.0002) irritated (0.0003) skin. (-0.0006) unlike (0.0006) some (0.0002) sprays (0.0012) and (0.0004) creams, (0.0007) this (0.0015) soothing (0.0038) treatment (0.0009) also (0.0002) gently (0.0011) cleanses (0.0008) and (0.0008) moisturizes (0.0003) for (0.0002) soft, (0.0008) smooth (0.0008) and (0.0006) healthylooking (0.0000) skineven (0.0006) sensitive (0.0018) skin (0.0007) is (0.0008) relieved. (-0.0015) discover (0.0052) aveeno (0.0011) active (0.0007) naturalsingredients (0.0005) derived (-0.0012) from (0.0005) nature (0.0009) and (0.0005) uniquely (0.0006) formulated (0.0017) to (-0.0004) reveal (0.0019) skin (0.0001) ' (-0.0015) s (-0.0004) natural (0.0019) health (0.0013) and (0.0015) beauty. (0.0006) essential (0.0012) active (0.0010) naturals (0.0008) : (0.0021) skinsoothing (0.0021) natural (0.0011) colloidal (0.0001) oatmeal. (0.0010) aveeno (0.0006) dermatologist (0.0019) recommended (0.0007) for (-0.0018) over (0.0010) 60 (-0.0006) years. (0.0001)
~~~~~~
