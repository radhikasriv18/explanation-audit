# Reference packet: GraphNarrator__Llama-70B__products__30322

- Method: GraphNarrator; configuration: Llama-70B; dataset: products; target node: 30322
- Explanation source: `./robustness_2026-10-30/llama70b/graphnarrator/products/30322.json` (response)
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

- ROOT (DVD product)
  - Node-1 (Spanish movie)
    - Node-1.1 (Sara Montiel movie)
    - Node-1.2 (Sara Montiel movie)
    - Node-1.3 (DVD product details)
    - Node-1.4 (New factory-sealed DVD)
    - Node-1.5 (Brazilian movie)
    - Node-1.6 (Mexican Revolution movie)

1. Word-Level Evaluation:

Keywords with high saliency scores in ROOT — "platform" (0.04), "title" (0.04), "ahi" (0.01), "viene" (0.00), "martin" (-0.01), "corona" (0.02) — are not strongly associated with any specific product category. However, the presence of "dvd" (-0.07) with a negative saliency score indicates that the product might not be a DVD itself, but rather a related product.

2. Graph-Level Aggregation:

Node-1 (Spanish movie, keywords: "carmen" (-0.04), "la" (0.00), "de" (0.00), "ronda" (0.00), "1959" (-0.04), "audio" (0.02), "spanish" (0.04)) is a direct neighbor with moderate saliency, identifying a movie product whose close proximity to ROOT reinforces the classification. Indirect neighbors — Node-1.1 (Sara Montiel movie), Node-1.2 (Sara Montiel movie), Node-1.5 (Brazilian movie), Node-1.6 (Mexican Revolution movie) — are all movie-related products, collectively confirming a movie context across both hops.

### Free-Text Explanation
```markdown
The classification of ROOT into "Books" is not directly supported by its own keywords, but rather by the co-purchase neighborhood.

ROOT: Although the keywords do not strongly indicate a specific product category, the presence of "dvd" with a negative saliency score suggests that the product might be related to DVDs, but not a DVD itself.
  - Node-1: A Spanish movie (keywords: "carmen", "audio", "spanish") is a direct neighbor, reinforcing the movie context.
    - Node-1.1 ~ Node-1.2: Sara Montiel movies are related products, supporting the movie category.
    - Node-1.3: DVD product details, such as region 0 and NTSC format, provide additional context.
    - Node-1.4: A new factory-sealed DVD is a related product, confirming the DVD context.
    - Node-1.5: A Brazilian movie is another related product, further supporting the movie category.
    - Node-1.6: A Mexican Revolution movie is also a related product, collectively affirming the movie context.

However, considering the entire co-purchase neighborhood consists of movie-related products, and the lack of strong keywords indicating a specific product category in the ROOT node, it is reasonable to conclude that the product is related to movies, but not a movie itself. Given the classification label "Books", it is possible that the product is a book about movies or a related topic.
```
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/112.json`).

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
<verbalized-graph>ROOT: product(0.03) amazon(0.02) platform(0.04) title(0.01) content(0.02) title(0.04) ahi(0.01) viene(0.00) martin(-0.01) corona.(0.02) content(0.02) dvd(-0.07) 
Node-1: product(0.02) amazon(-0.04) platform(-0.03) title(0.02) content(-0.00) title(0.02) carmen(-0.04) la(0.00) de(0.00) ronda(0.00) 1959(-0.04) audio(0.02) spanish(0.04) ].(-0.06) content(0.06) 1959(0.00) release.(-0.07) talented(0.04) actress(-0.04) popular(-0.03) music(-0.02) singer,(-0.01) better(-0.00) known(-0.02) sarita(-0.00) montiel,(-0.00) became(0.00) one(0.00) first(0.00) sex(-0.04) symbols(-0.00) spain(0.03) attract(-0.00) hollywood(-0.02) attention(0.00) captivating(0.00) performances.(0.01) early(0.01) 50s,(0.02) montiel(0.02) settled(0.01) mexico(-0.01) began(0.03) singing(0.01) career(0.01) working(0.00) along(0.01) pedro(0.01) infante,(0.02) manolo(0.02) fabregas(0.02) agustin(0.02) lara.(0.03) 1954,(-0.01) acclaimed(0.01) actress(0.03) opportunity(0.01) work(0.02) along(0.03) gary(0.03) cooper(0.02) burt(0.03) lancaster.(-0.00) montiel(0.03) rose(0.03) latin(0.03) music(0.01) stardom(0.02) release(0.02) el(0.00) ultimo(0.00) cuple(0.00) movie(-0.02) soundtrack.(-0.01) 1970s,(0.03) multi-(-0.01) lingual(0.01) star(-0.01) toured(0.00) world(-0.00) leading(0.01) celebrated(0.02) musicals.(0.00) english(0.04) subtitles(0.06) 
Node-1.1: product(0.01) amazon(-0.00) platform(-0.00) title(0.01) content(-0.00) title(0.00) missing.(0.01) content(0.00) lo(0.00) mejor(0.00) de(0.00) sara(-0.00) montiel(0.01) sara(0.00) montielthis(0.00) product(0.01) manufactured(0.01) demand(0.01) using(0.01) cd-(0.01) r(0.01) recordable(0.01) media.(0.01) amazon.(-0.00) com(0.02) standard(0.01) return(0.00) policy(0.01) apply.(0.00) 
Node-1.2: product(-0.01) amazon(-0.00) platform(0.01) title(-0.00) content(0.00) title(0.00) missing.(-0.00) content(0.00) sus(0.00) pel(0.00) xed(0.00) culas(0.00) el(0.00) xda(0.00) ltimo(0.00) cupl(0.00) xe9(0.00) la(-0.00) violetera(0.00) 1957-(0.00) 1958(-0.00) sara(0.00) montielthis(-0.00) product(0.01) manufactured(0.01) demand(0.00) using(-0.00) cd-(0.00) r(0.00) recordable(0.00) media.(0.01) amazon.(-0.00) com(0.00) standard(0.00) return(0.00) policy(0.00) apply.(0.00) 
Node-1.3: product(-0.00) amazon(-0.00) platform(0.00) title(0.00) content(-0.00) title(-0.00) missing.(0.00) content(0.00) audio(0.00) subtitles(0.00) english.(0.00) audio(0.00) spanish(-0.00) optional(0.00) subtitles(0.00) portuguese.(0.00) region(-0.00) 0(0.00) dvd(0.00) play(0.00) dvd(0.00) players(-0.00) sold(0.00) us(0.00) canada.(0.00) play(0.00) also(0.00) dvd(0.00) players(0.00) worldwide(0.00) plays(0.00) ntsc(0.00) format.(0.00) well,(0.00) film(0.00) dramatic(0.00) intimate.(0.00) may(-0.00) love(0.00) plot,(0.00) may(-0.00) love(0.00) admire(0.00) voice(0.00) sarita(-0.00) montiel-(0.00) everything(0.00) ".(-0.00) quite(0.00) outstanding(0.01) movie,(0.00) although,(0.00) opinion,(0.00) serenade(0.00) 1956(-0.00) greater(0.00) one.(0.00) please(0.00) listen(0.00) sara(-0.00) velvety,(0.00) low,(0.00) womanly(0.00) voice,(0.00) please(0.00) remember(0.00) heart.(0.00) woman(0.00) takes(0.00) away(0.00) other,(0.00) much(0.00) beautiful(0.00) world,(0.00) modulation(0.00) voice,(0.00) movement(0.00) brows(0.00) eyes.(0.00) listen(0.00) her,(0.00) watch(0.00) her.(-0.00) note(0.00) scene,(0.00) closer(0.00) final,(0.00) loses(0.00) lover(0.00) returns(0.00) chantecler,-(0.00) watch(0.00) teared(0.00) playbills(0.00) swaying(0.00) wind(0.00) sea...(0.00) real(0.00) art(0.00) cinema.(-0.00) enjoy(0.00) la(0.00) reina(0.00) del(0.00) chantecler(0.00) serenade(0.00) ",(0.00) among(-0.00) greatest(0.00) pictures(0.00) ever(-0.00) filmed.(0.00) wladislaw(0.00) semyonow(0.00) imdb(0.00) 
Node-1.4: product(0.00) amazon(-0.01) platform(0.00) title(0.00) content(-0.00) title(-0.00) missing.(0.01) content(0.00) new(0.00) factory(0.00) seald(0.00) 
Node-1.5: product(0.00) amazon(-0.00) platform(-0.00) title(0.00) content(-0.00) title(0.00) samba(-0.00) english(-0.00) import(0.00) ].(0.00) content(-0.00) region(0.00) 0(-0.00) dvd(-0.00) play(-0.00) dvd(-0.00) players(0.00) sold(0.00) us(0.00) canada.(0.00) play(-0.00) also(-0.00) dvd(-0.00) players(0.00) worldwide(-0.00) plays(0.00) ntsc(-0.00) format.(0.00) english.(0.00) audio(-0.00) spanish.(-0.00) optional(-0.00) subtitles(-0.00) portuguese.(0.00) brazilian(-0.01) singer(-0.00) laura(-0.01) monteiro(-0.00) murdered(-0.00) dressing-(0.00) room(0.00) jealous(0.01) lover(0.01) joo(0.01) fernandes(0.00) de(-0.00) oliveira(-0.00) discovered(0.00) cheating(0.00) assis(0.00) intends(0.00) escape(0.00) traveling(0.00) buenos(-0.00) aires(-0.00) assis.(0.00) meanwhile,(-0.00) beln(-0.00) moreira,(-0.00) lives(-0.00) favela(0.00) salgueiro(0.00) dead(-0.00) ringer(0.00) laura,(-0.00) goes(0.00) copacabana(-0.00) boyfriend(-0.00) paulo.(0.00) two(0.00) gangsters(0.00) gang(0.00) smuggles(-0.00) precious(-0.00) stones(-0.00) sewn(-0.00) carnival(-0.00) costumes(0.00) see(0.00) beln(-0.00) force(-0.00) president(-0.00) salgueiro(-0.00) samba(0.00) school(-0.00) invite(-0.00) beln(-0.00) perform(-0.00) chica(0.00) da(-0.00) silva(-0.00) carnival(-0.00) parade.(0.00) costume(0.00) prepared(-0.00) real(-0.00) precious(-0.00) stones(-0.00) smuggled(0.00) europe.(0.00) claudio(0.00) carvalho(0.00) imdb(0.00) 
Node-1.6: product(-0.00) amazon(-0.00) platform(-0.00) title(0.00) content(-0.00) title(-0.00) vera(-0.00) cruz.(0.00) content(-0.00) first(-0.00) friend(0.00) ever(-0.00) had,(0.00) grins(0.00) flamboyant(-0.00) mercenary(-0.01) burt(-0.01) lancaster(0.00) lean,(-0.00) laconic(-0.00) gary(-0.00) cooper(-0.00) smile(-0.00) suggests(-0.00) may(-0.00) last.(0.00) pair(-0.00) americans(0.00) abroad(-0.00) looking(-0.00) cash(-0.00) mexican(0.00) revolution(0.00) selling(0.00) services(-0.00) highest(0.00) bidder(-0.00) energetically(-0.00) cynical(-0.00) south-(0.00) of-(0.00) the-(0.00) border(-0.00) western.(0.00) meet(0.00) cute,(0.00) conning,(0.00) robbing,(-0.00) out-(-0.00) witting(-0.00) </verbalized-graph>

### Classification Label
Books

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 30322
- Title: Ahi Viene Martin Corona
- True class (canonical `y`): **Movies & TV**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **CDs & Vinyl**
- Prediction recorded by this method's pipeline: **Books**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Ahi Viene Martin Corona. Content: dvd
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 6463 | Movies & TV | Carmen la de Ronda (1959) [audio in Spanish only] |

### 2-hop (shortest distance exactly 2): 6 nodes

| node id | true class | title |
|---|---|---|
| 743 | CDs & Vinyl | missing |
| 751 | CDs & Vinyl | missing |
| 30318 | Movies & TV | missing |
| 30319 | Movies & TV | missing |
| 30320 | Movies & TV | Samba (NO ENGLISH) [Import] |
| 30321 | Movies & TV | Vera Cruz |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/112.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Books**, ground truth = **Movies & TV**.
The verbalized graph is 7328 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 30322 | 18 | 0.0402 | yes |
| Node-1 | 1 | 6463 | 131 | 0.0611 | yes |
| Node-1.1 | 2 | 743 | 41 | 0.0194 | yes |
| Node-1.2 | 3 | 751 | 62 | 0.0100 | yes |
| Node-1.3 | 4 | 30318 | 230 | 0.0057 | yes |
| Node-1.4 | 5 | 30319 | 18 | 0.0056 | yes |
| Node-1.5 | 6 | 30320 | 185 | 0.0063 | yes |
| Node-1.6 | 7 | 30321 | 243 | 0.0186 | yes |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->Node-1.6, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, Node-1.6->Node-1, ROOT->Node-1

### Tokens and scores

**ROOT** (global 30322):

~~~~~~text
product (0.0272) from (0.0040) amazon (0.0194) platform (0.0361) with (-0.0106) title (0.0075) and (0.0261) content (0.0168) : (-0.0387) title (0.0402) : (0.0348) ahi (0.0108) viene (0.0019) martin (-0.0107) corona. (0.0162) content (0.0159) : (-0.0222) dvd (-0.0662)
~~~~~~

**Node-1** (global 6463):

~~~~~~text
product (0.0154) from (0.0018) amazon (-0.0410) platform (-0.0278) with (0.0089) title (0.0219) and (0.0268) content (-0.0039) : (-0.0010) title (0.0232) : (0.0198) carmen (-0.0379) la (0.0046) de (0.0040) ronda (0.0015) ( (-0.0219) 1959 (-0.0380) ) (-0.0075) [ (0.0158) audio (0.0246) in (0.0153) spanish (0.0371) only (-0.0022) ]. (-0.0627) content (0.0552) : (0.0029) 1959 (0.0034) release. (-0.0676) talented (0.0418) actress (-0.0393) and (-0.0026) popular (-0.0309) music (-0.0248) singer, (-0.0098) better (-0.0022) known (-0.0154) as (0.0022) sarita (-0.0023) montiel, (-0.0008) became (0.0046) one (0.0035) of (-0.0074) the (-0.0029) first (0.0044) sex (-0.0361) symbols (-0.0045) from (0.0064) spain (0.0311) to (0.0092) attract (-0.0037) hollywood (-0.0168) ' (0.0004) s (0.0020) attention (0.0047) with (0.0073) her (0.0140) captivating (0.0041) performances. (0.0060) in (0.0051) the (-0.0007) early (0.0133) ' (-0.0109) 50s, (0.0153) montiel (0.0214) settled (0.0134) in (0.0293) mexico (-0.0148) and (0.0081) began (0.0307) her (0.0131) singing (0.0088) career (0.0141) while (0.0239) working (0.0011) along (0.0080) with (0.0152) pedro (0.0075) infante, (0.0203) manolo (0.0161) fabregas (0.0172) and (0.0360) agustin (0.0234) lara. (0.0269) in (0.0133) 1954, (-0.0066) the (0.0306) acclaimed (0.0064) actress (0.0281) had (0.0433) the (0.0206) opportunity (0.0081) to (0.0358) work (0.0192) along (0.0253) with (0.0250) gary (0.0270) cooper (0.0210) and (0.0308) burt (0.0259) lancaster. (-0.0041) montiel (0.0297) rose (0.0337) to (0.0185) latin (0.0291) music (0.0133) stardom (0.0178) with (0.0266) the (-0.0265) release (0.0153) of (0.0060) el (0.0037) ultimo (0.0036) cuple (0.0011) movie (-0.0191) soundtrack. (-0.0075) during (-0.0016) the (0.0077) 1970s, (0.0259) the (-0.0121) multi- (-0.0132) lingual (0.0077) star (-0.0090) toured (0.0040) the (-0.0091) world (-0.0048) leading (0.0094) celebrated (0.0242) musicals. (0.0006) no (0.0611) english (0.0401) subtitles (0.0596)
~~~~~~

**Node-1.1** (global 743):

~~~~~~text
product (0.0062) from (0.0077) amazon (-0.0021) platform (-0.0011) with (0.0069) title (0.0090) and (0.0129) content (-0.0016) : (0.0060) title (0.0039) : (0.0065) missing. (0.0075) content (0.0007) : (0.0044) lo (0.0046) mejor (0.0039) de (0.0046) sara (-0.0021) montiel (0.0112) by (0.0089) sara (0.0034) montielthis (0.0028) product (0.0075) is (0.0034) manufactured (0.0059) on (0.0131) demand (0.0053) using (0.0114) cd- (0.0097) r (0.0119) recordable (0.0078) media. (0.0088) amazon. (-0.0025) com (0.0194) ' (0.0021) s (0.0064) standard (0.0084) return (0.0022) policy (0.0103) will (0.0024) apply. (0.0005)
~~~~~~

**Node-1.2** (global 751):

~~~~~~text
product (-0.0079) from (0.0010) amazon (-0.0016) platform (0.0100) with (-0.0017) title (-0.0000) and (-0.0007) content (0.0022) : (-0.0031) title (0.0003) : (-0.0025) missing. (-0.0012) content (0.0038) : (-0.0023) sus (0.0027) pel (0.0009) & (0.0046) # (0.0036) xed (0.0024) ; (0.0033) culas (0.0017) : (0.0024) el (0.0025) & (0.0050) # (0.0027) xda (0.0017) ; (0.0033) ltimo (0.0020) cupl (0.0021) & (0.0060) # (0.0031) xe9 (0.0001) ; (0.0014) y (-0.0008) la (-0.0008) violetera (0.0040) ( (0.0016) 1957- (0.0003) 1958 (-0.0011) ) (0.0033) by (0.0001) sara (0.0013) montielthis (-0.0013) product (0.0061) is (0.0053) manufactured (0.0068) on (0.0002) demand (0.0002) using (-0.0020) cd- (0.0022) r (0.0019) recordable (0.0029) media. (0.0091) amazon. (-0.0022) com (0.0009) ' (0.0037) s (0.0058) standard (0.0023) return (0.0050) policy (0.0006) will (-0.0069) apply. (0.0008)
~~~~~~

**Node-1.3** (global 30318):

~~~~~~text
product (-0.0022) from (0.0003) amazon (-0.0012) platform (0.0004) with (0.0007) title (0.0005) and (0.0005) content (-0.0000) : (0.0000) title (-0.0002) : (0.0003) missing. (0.0011) content (0.0005) : (0.0002) no (0.0007) audio (0.0003) or (0.0006) subtitles (0.0011) in (0.0008) english. (0.0011) audio (0.0005) in (0.0007) spanish (-0.0009) and (0.0008) optional (0.0002) subtitles (0.0008) in (0.0009) portuguese. (0.0015) this (0.0013) a (0.0010) region (-0.0004) 0 (0.0006) ( (0.0006) all (0.0004) ) (-0.0003) dvd (0.0019) and (0.0002) it (0.0011) will (0.0002) play (0.0001) on (0.0006) any (0.0003) dvd (0.0011) players (-0.0002) sold (0.0007) in (0.0004) the (0.0001) us (0.0008) or (0.0013) canada. (0.0013) it (0.0007) will (-0.0003) play (0.0002) also (0.0002) on (0.0011) any (0.0005) dvd (0.0004) players (0.0002) worldwide (0.0002) that (0.0006) plays (0.0005) ntsc (0.0003) format. (0.0013) well, (0.0009) this (-0.0004) film (0.0009) is (0.0009) very (0.0008) dramatic (0.0008) and (0.0021) very (-0.0001) intimate. (0.0020) you (0.0012) may (-0.0003) not (0.0009) love (0.0011) the (0.0005) plot, (0.0004) but (0.0009) you (0.0013) may (-0.0002) love (0.0006) and (0.0009) admire (0.0023) the (-0.0009) voice (0.0007) of (0.0001) sarita (-0.0002) montiel- (0.0007) " (-0.0015) our (0.0013) everything (0.0011) ". (-0.0030) she (0.0032) is (0.0011) quite (0.0010) outstanding (0.0057) in (0.0003) this (0.0010) movie, (0.0003) although, (0.0015) in (0.0010) my (0.0029) opinion, (0.0011) " (0.0005) serenade (0.0020) " (-0.0003) ( (0.0007) 1956 (-0.0000) ) (-0.0012) is (-0.0008) a (0.0017) greater (0.0029) one. (0.0022) please (0.0017) listen (0.0012) to (0.0014) sara (-0.0007) ' (0.0002) s (0.0005) velvety, (0.0007) low, (0.0010) very (0.0009) womanly (0.0009) voice, (0.0011) and (0.0021) please (0.0010) remember (0.0012) it (0.0012) in (0.0013) your (-0.0005) heart. (0.0005) she (0.0012) is (0.0004) a (0.0002) woman (0.0003) that (0.0011) takes (0.0006) you (-0.0005) away (0.0008) to (0.0006) the (0.0002) other, (0.0009) much (0.0008) more (0.0009) beautiful (0.0014) world, (0.0013) with (0.0011) only (0.0005) a (0.0013) modulation (0.0019) in (0.0012) her (0.0014) voice, (0.0011) with (0.0017) only (0.0012) a (0.0006) movement (0.0012) of (0.0010) her (0.0014) brows (0.0012) and (0.0017) eyes. (0.0015) listen (0.0009) to (0.0014) her, (0.0015) watch (0.0008) her. (-0.0001) and (0.0018) note (0.0009) the (0.0009) scene, (0.0012) closer (0.0014) to (0.0004) the (0.0008) final, (0.0011) in (0.0009) which (0.0003) she (0.0003) loses (0.0001) her (0.0015) lover (0.0002) and (0.0013) returns (0.0008) to (0.0010) the (-0.0007) chantecler,- (0.0006) watch (0.0009) now (0.0009) teared (0.0001) playbills (0.0008) swaying (0.0018) at (0.0015) the (-0.0001) wind (0.0009) from (0.0011) the (-0.0002) sea... (0.0001) this (0.0014) is (0.0001) the (-0.0013) real (0.0014) art (0.0008) of (0.0005) cinema. (-0.0005) enjoy (0.0027) " (0.0015) la (0.0001) reina (0.0008) del (0.0008) chantecler (0.0005) " (0.0003) and (0.0002) " (-0.0000) serenade (0.0003) ", (0.0020) these (0.0003) are (-0.0003) among (-0.0000) of (0.0011) the (-0.0010) greatest (0.0002) pictures (0.0002) ever (-0.0008) filmed. (0.0021) by (0.0038) wladislaw (0.0001) semyonow (0.0007) at (0.0015) imdb (0.0031)
~~~~~~

**Node-1.4** (global 30319):

~~~~~~text
product (0.0027) from (0.0026) amazon (-0.0095) platform (0.0019) with (0.0016) title (0.0013) and (0.0003) content (-0.0011) : (0.0012) title (-0.0035) : (-0.0002) missing. (0.0056) content (0.0026) : (0.0019) new (0.0048) and (0.0024) factory (0.0014) seald (0.0033)
~~~~~~

**Node-1.5** (global 30320):

~~~~~~text
product (0.0023) from (0.0004) amazon (-0.0031) platform (-0.0001) with (-0.0013) title (0.0007) and (0.0000) content (-0.0011) : (0.0012) title (0.0002) : (0.0007) samba (-0.0004) ( (-0.0005) no (-0.0009) english (-0.0002) ) (-0.0000) [ (0.0026) import (0.0014) ]. (0.0003) content (-0.0015) : (-0.0009) this (-0.0009) is (0.0004) a (-0.0011) region (0.0012) 0 (-0.0042) ( (-0.0013) all (-0.0000) ) (0.0005) dvd (-0.0022) and (-0.0015) it (-0.0007) will (-0.0007) play (-0.0006) on (-0.0006) any (-0.0002) dvd (-0.0016) players (0.0006) sold (0.0007) in (-0.0001) the (-0.0006) us (0.0009) or (0.0000) canada. (0.0004) it (-0.0022) will (-0.0003) play (-0.0003) also (-0.0006) on (-0.0004) any (-0.0004) dvd (-0.0000) players (0.0008) worldwide (-0.0018) that (0.0006) plays (0.0011) ntsc (-0.0001) format. (0.0031) no (-0.0006) english. (0.0023) audio (-0.0027) in (-0.0015) spanish. (-0.0014) optional (-0.0001) subtitles (-0.0002) in (-0.0016) portuguese. (0.0014) the (-0.0097) brazilian (-0.0065) singer (-0.0024) laura (-0.0077) monteiro (-0.0027) is (0.0001) murdered (-0.0031) in (-0.0015) her (0.0008) dressing- (0.0003) room (0.0015) by (0.0019) her (0.0014) jealous (0.0057) lover (0.0063) joo (0.0055) fernandes (0.0013) de (-0.0000) oliveira (-0.0006) that (-0.0002) discovered (0.0020) that (0.0001) she (0.0018) was (0.0002) cheating (0.0023) him (0.0015) with (0.0011) assis (0.0003) and (0.0024) she (0.0012) intends (0.0023) to (0.0012) escape (0.0011) from (0.0035) him (0.0006) traveling (0.0022) to (0.0012) buenos (-0.0002) aires (-0.0011) with (0.0018) assis. (0.0039) meanwhile, (-0.0010) beln (-0.0024) moreira, (-0.0006) who (-0.0008) lives (-0.0004) in (-0.0011) favela (0.0003) do (-0.0004) salgueiro (0.0004) and (-0.0007) is (0.0006) a (-0.0010) dead (-0.0009) ringer (0.0007) of (-0.0002) laura, (-0.0007) goes (0.0024) to (0.0006) copacabana (-0.0011) with (0.0003) her (0.0003) boyfriend (-0.0013) paulo. (0.0009) two (0.0001) gangsters (0.0014) of (-0.0000) a (0.0005) gang (0.0007) that (-0.0005) smuggles (-0.0001) precious (-0.0033) stones (-0.0008) sewn (-0.0001) in (-0.0016) carnival (-0.0009) costumes (0.0026) see (0.0005) beln (-0.0037) and (-0.0004) they (0.0002) force (-0.0002) the (-0.0005) president (-0.0010) of (0.0005) the (-0.0001) salgueiro (-0.0011) samba (0.0009) school (-0.0016) to (-0.0010) invite (-0.0014) beln (-0.0018) to (-0.0002) perform (-0.0011) chica (0.0020) da (-0.0016) silva (-0.0003) in (-0.0017) the (-0.0012) carnival (-0.0013) parade. (0.0002) her (0.0007) costume (0.0007) is (0.0012) prepared (-0.0008) with (0.0001) real (-0.0004) precious (-0.0014) stones (-0.0002) to (-0.0002) be (0.0001) smuggled (0.0009) to (-0.0004) europe. (0.0023) ( (0.0024) claudio (0.0008) carvalho (0.0013) imdb (0.0037) ) (-0.0001)
~~~~~~

**Node-1.6** (global 30321):

~~~~~~text
product (-0.0004) from (-0.0031) amazon (-0.0001) platform (-0.0005) with (-0.0029) title (0.0018) and (-0.0010) content (-0.0027) : (0.0011) title (-0.0012) : (-0.0002) vera (-0.0002) cruz. (0.0026) content (-0.0045) : (-0.0007) " (-0.0005) you (0.0005) ' (-0.0006) re (-0.0006) the (-0.0000) first (-0.0002) friend (0.0000) i (-0.0003) ever (-0.0007) had, (0.0018) " (-0.0035) grins (0.0004) flamboyant (-0.0018) mercenary (-0.0069) burt (-0.0100) lancaster (0.0008) to (-0.0012) lean, (-0.0007) laconic (-0.0009) gary (-0.0000) cooper (-0.0005) with (-0.0006) a (0.0004) smile (-0.0002) that (-0.0001) suggests (-0.0014) that (0.0002) he (-0.0002) may (-0.0007) be (-0.0002) the (-0.0001) last. (0.0004) they (-0.0009) ' (-0.0005) re (-0.0024) a (-0.0024) pair (-0.0000) of (-0.0002) americans (0.0008) abroad (-0.0019) looking (-0.0007) to (0.0009) cash (-0.0014) in (-0.0004) on (0.0000) the (0.0022) mexican (0.0004) revolution (0.0034) by (-0.0012) selling (0.0016) their (-0.0021) services (-0.0014) to (-0.0009) the (0.0007) highest (0.0004) bidder (-0.0011) in (-0.0001) this (-0.0011) energetically (-0.0008) cynical (-0.0018) south- (0.0006) of- (0.0020) the- (0.0019) border (-0.0024) western. (0.0026) they (0.0030) meet (0.0032) cute, (0.0027) conning, (0.0022) robbing, (-0.0019) and (-0.0026) out- (-0.0002) witting (-0.0006) one (-0.0010) another (-0.0008) in (-0.0014) a (-0.0002) bit (-0.0013) of (-0.0003) one- (-0.0022) upmanship (-0.0013) that (-0.0004) bonds (-0.0027) the (0.0024) men (0.0001) in (-0.0007) mutual (0.0003) admiration, (0.0018) and (-0.0017) then (0.0011) team (-0.0015) up (-0.0028) to (-0.0008) escort (-0.0024) a (-0.0031) royal (0.0002) convoy (-0.0042) through (-0.0008) revolutionary (-0.0044) country. (-0.0024) when (-0.0001) they (-0.0004) discover (0.0002) its (0.0025) secret (0.0014) stash (-0.0009) of (-0.0012) gold (-0.0002) bullion, (-0.0005) they (-0.0006) revert (-0.0006) to (0.0006) their (0.0005) old (-0.0007) way, (0.0010) selling (-0.0002) out (0.0044) anyone (-0.0018) it (0.0000) takes (-0.0005) to (0.0002) get (-0.0005) the (0.0005) treasure (0.0035) for (0.0006) themselves, (-0.0000) even (-0.0004) each (0.0018) other. (-0.0010) played (0.0014) out (0.0020) as (-0.0020) a (-0.0014) seat- (-0.0008) of- (-0.0001) the- (0.0001) pants (-0.0005) con (-0.0007) game (0.0002) of (0.0009) shifting (-0.0001) alliances (-0.0008) and (0.0009) double (-0.0011) crosses, (-0.0009) this (-0.0000) is (-0.0007) a (-0.0042) cheerfully (-0.0046) ruthless (-0.0011) tale (0.0006) that (-0.0026) served (-0.0033) as (-0.0011) a (-0.0009) veritable (-0.0001) blueprint (-0.0009) for (-0.0018) the (-0.0012) italian (-0.0004) spaghetti (0.0048) westerns (0.0003) of (-0.0009) the (0.0005) 1960s. (0.0005) director (-0.0027) robert (-0.0039) aldrich (-0.0002) has (0.0014) a (-0.0014) real (0.0004) flair (-0.0017) for (-0.0008) turning (-0.0005) rogues (0.0009) and (0.0002) opportunists (-0.0007) into (-0.0003) deviously (-0.0008) riveting (0.0001) characters, (0.0009) and (-0.0004) went (0.0002) on (0.0002) to (0.0002) work (-0.0008) the (0.0010) same (-0.0007) sort (0.0023) of (0.0029) magic (0.0014) onkiss (-0.0007) me (0.0037) deadlyandthe (-0.0019) dirty (0.0011) dozen. (0.0034) the (0.0015) cast (-0.0021) of (-0.0009) character (-0.0025) actors (0.0014) features (0.0012) ernest (-0.0036) borgnine, (0.0010) charles (-0.0012) bronson, (0.0005) and (-0.0010) jack (-0.0010) elam (-0.0008) in (-0.0007) the (0.0004) gang, (0.0015) george (-0.0009) macready (-0.0000) as (0.0050) emperor (-0.0017) maximilian, (0.0017) and (-0.0025) henry (-0.0018) brandon (-0.0011) as (0.0034) the (0.0025) martinet (-0.0003) german (0.0002) captain (0.0008) danette.-- (-0.0089) sean (0.0167) axmaker (0.0186)
~~~~~~
