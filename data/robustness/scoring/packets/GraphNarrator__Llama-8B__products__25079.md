# Reference packet: GraphNarrator__Llama-8B__products__25079

- Method: GraphNarrator; configuration: Llama-8B; dataset: products; target node: 25079
- Explanation source: `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/93.json` (messages[assistant])
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

- ROOT (product)
  - Node-1 (Disney movie)
    - Node-1.1 (missing content)
    - Node-1.2 (Inspector Gadget)
    - Node-1.3 (Disney movie)
    - Node-1.4 (Beverly Hills Chihuahua)

### Word-Level Evaluation:

Keywords with high saliency scores in ROOT — "amazon" (0.02), "platform" (0.02), "title" (0.02), "content" (0.02) — are associated with product information. However, these generic terms carry relatively low saliency and contribute little to the classification. The presence of "chilly" (0.01) and "dogs" (-0.01) suggests a winter or animal theme, but their low scores indicate a weak connection to the classification label.

### Graph-Level Aggregation:

Node-1 (Disney movie, keywords: "disney" (0.00), "snow" (-0.01), "dogs" (-0.01)) is a direct neighbor with moderate saliency, indicating a movie related to winter or animals. Indirect neighbors — Node-1.1 (missing content), Node-1.2 (Inspector Gadget), Node-1.3 (Disney movie), Node-1.4 (Beverly Hills Chihuahua) — are all movies or movie-related content, collectively confirming a movie context across both hops.

### Free-Text Explanation

The classification of ROOT into "Books" is not strongly supported by its own keywords or the co-purchase neighborhood.

ROOT: Keywords like "amazon" (0.02) and "platform" (0.02) are associated with product information, but their low saliency scores indicate a weak connection to the classification label.
  - Node-1: A Disney movie (keywords: "disney" (0.00), "snow" (-0.01), "dogs" (-0.01)) is a direct neighbor with moderate saliency, indicating a movie related to winter or animals.
    - Node-1.1 ~ Node-1.4: Missing content, Inspector Gadget, another Disney movie, and Beverly Hills Chihuahua are all movies or movie-related content, supporting the movie category.
 
In summary, the classification of ROOT into "Books" is not strongly supported by its own keywords or the co-purchase neighborhood. The presence of movie-related content in the graph structure suggests a more likely classification into the "Movies & TV" category.
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-101/93.json`).

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
<verbalized-graph>ROOT: product(-0.00) amazon(0.02) platform(0.02) title(0.00) content(0.01) title(0.02) chilly(0.01) dogs.(-0.01) content(0.02) lovely(-0.00) snowy(-0.01) expanses(0.01) alaska(0.02) setting(0.00) forchilly(-0.01) dogs,(-0.01) goofy(0.00) comedy(0.00) travel(0.01) agency(0.02) clerk(0.00) skeet(0.02) ulrich,(0.05) scream,(-0.01) newton(0.02) boys(0.03) los(-0.00) angeles(0.00) prove(0.02) mettle(0.01) racing(0.01) team(-0.00) mismatched(0.01) sled(0.01) dogs(-0.00) anchorage(0.04) nome.(-0.00) allow(0.01) claim(0.00) grandfather(-0.00) inheritance--(0.01) wily(0.00) lawyer(0.01) leslie(0.00) nielsen,(-0.00) mugging(0.02) shamelessly(0.02) usual(0.02) intends(0.01) claim(0.00) inheritance(0.02) knocking(0.02) clerk(0.01) race.(-0.02) surprising(0.01) see(0.02) ulrich(-0.02) movie(-0.00) full(0.01) clumsy,(-0.00) half-(0.00) baked(-0.00) slapstick(0.00) bodily(-0.00) function(0.02) humor,(0.00) natasha(0.01) henstridge(0.01) species,(0.01) whole(0.02) nine(0.01) yards(0.00) thrown(0.01) away(0.01) bland(0.01) romantic(0.00) foil?(-0.00) intelligence(-0.01) sexy(0.02) tough(0.01) persona(0.02) deserve(-0.01) better--(0.02) provideschilly(0.01) dogswith(0.01) little(0.01) momentum(0.02) has.(-0.02) also(0.03) featuring(0.02) rik(0.01) mayall(0.03) young(0.00) ones(-0.00) ).--(-0.02) bret(-0.04) fetzer(-0.01) 
Node-1: product(0.02) amazon(0.00) platform(-0.03) title(-0.02) content(-0.00) title(-0.01) snow(-0.01) dogs.(-0.01) content(0.02) make(-0.01) bones(-0.01) it--(-0.02) disney(-0.02) snow(-0.02) dogs(-0.01) hilarious,(-0.01) action-(-0.02) packed(-0.05) comedy(0.03) whole(-0.02) family(0.01) love.(-0.00) eight(-0.03) adorable(0.00) mischievous(0.00) dogs(-0.01) get(-0.01) best(-0.00) dog(-0.01) hater(-0.00) ted(-0.02) brooks(-0.01) cuba(0.03) gooding,(-0.02) jr.(-0.01) leaves(-0.03) successful(-0.01) miami(-0.01) beach(-0.04) dental(-0.02) practice(-0.01) wilds(-0.01) alaska(0.01) claim(0.02) inheritance--(-0.02) seven(0.01) siberian(-0.04) huskies(-0.03) border(-0.02) collie--(-0.01) discover(0.00) roots.(-0.04) ted(0.01) life(-0.02) goes(-0.02) dogs,(-0.00) rises(-0.00) occasion(-0.03) vows(-0.03) learn(-0.02) mush(-0.01) inheritance.(0.01) totally(-0.02) element,(-0.01) faces(-0.02) challenges(-0.03) never(0.01) dreamed(-0.04) of.(0.01) blizzard,(0.00) thin(-0.01) ice,(0.01) intimidating(-0.02) crusty(-0.02) old(-0.01) mountain(-0.00) man(-0.01) named(-0.01) thunder(0.00) jack(0.02) james(0.00) coburn(-0.00) ),(0.01) arctic(0.01) challenge(-0.02) sled(0.00) dog(0.01) race(-0.01) two(-0.00) weeks(-0.02) away,(0.00) life-(-0.01) and-(-0.02) death(-0.02) rescue.(0.02) fish-(-0.01) out-(-0.02) water,(-0.00) tail-(-0.02) wagging(-0.01) comedy(-0.00) nothing(-0.04) doggone(-0.00) good(0.02) fun(-0.03) celebration(-0.00) family--(-0.03) human(-0.01) canine!(0.03) 
Node-1.1: product(-0.00) amazon(-0.00) platform(0.00) title(0.00) content(-0.00) title(0.00) missing.(0.00) content(-0.00) air(0.00) bud(0.00) spikes(0.00) back(0.00) disney(0.00) serves(-0.00) another(0.00) adventure(0.00) starring(0.00) everyone(-0.00) favorite(0.00) sports-(0.00) playing(0.00) golden(-0.00) retriever,(0.00) buddy!(-0.00) time,(0.00) masters(0.00) coolest(0.00) sport(0.00) sun...(-0.00) beach(-0.00) volleyball!(0.00) plenty(-0.00) action(0.00) court(0.00) well--(0.00) rash(0.00) mysterious(0.00) crimes(-0.00) puzzling(0.00) everyone...(-0.00) paw(-0.00) prints(0.00) seem(0.00) point(0.00) buddy!(0.00) so,(0.00) buddy(0.00) lead(0.00) authorities(-0.00) real(0.00) culprit!(0.00) special(0.00) appearance(0.00) pro(0.00) volleyball(0.00) champion(0.00) gabrielle(0.00) reece(0.00) heartwarming(0.00) story,(0.00) family(0.00) sure(-0.00) enjoy(-0.00) fun-(0.00) filled(0.00) adventure!(0.00) air(-0.00) bud(-0.00) seventh(0.00) inning(0.00) fetch(0.00) air(0.00) bud(-0.00) knocks(0.00) one(0.00) park(0.00) takes(0.00) baseball(-0.00) fun(0.00) heartwarming(0.00) disney(0.00) adventure!(-0.00) time,(0.00) buddy(0.00) joins(0.00) shows(0.00) natural(0.00) baseball(0.00) player(0.00) major(0.00) league(-0.00) talent!(0.00) midst(-0.00) season,(0.00) however,(0.00) terrible(0.00) discovery(0.00) made(-0.00) buddy(0.00) now-(-0.00) grown(0.00) puppies(0.00) mysteriously(0.00) begun(-0.00) disappear(0.00) new(0.00) homes!(-0.00) buddy(0.00) stop(-0.00) dog-(0.00) nappings(0.00) find(0.00) pups(-0.00) late!(-0.00) 
Node-1.2: product(-0.00) amazon(-0.00) platform(-0.00) title(0.00) content(0.02) title(0.01) inspector(-0.01) gadget.(0.00) content(0.02) inspector(-0.01) gadget(-0.00) 
Node-1.3: product(-0.00) amazon(0.00) platform(0.00) title(0.00) content(-0.00) title(0.00) air(-0.00) bud(0.00) spikes(0.00) back.(-0.00) content(0.01) disney(-0.00) serves(0.00) all-(-0.00) new(-0.00) adventure(-0.00) starring(0.00) everyone(-0.00) favorite(0.00) sports-(-0.00) playing(0.00) golden(-0.00) retriever,(-0.00) buddy!(-0.00) time,(-0.00) masters(-0.00) coolest(0.00) sport(0.00) sun...(0.00) beach(0.00) volleyball!(0.00) plenty(0.00) action(0.00) court(-0.00) well--(-0.00) rash(0.00) mysterious(0.00) crimes(0.00) puzzling(0.00) everyone...(0.00) paw(0.00) prints(0.00) seem(0.00) point(0.00) buddy!(0.00) buddy(0.00) lead(0.00) authorities(0.00) real(0.00) culprit!(0.00) special(0.00) appearance(0.01) pro-(0.00) volleyball(0.00) champion(0.00) gabrielle(0.01) reece(0.01) heartwarming(0.00) story,(-0.00) fun-(-0.00) filled(-0.00) adventure(-0.00) sure(0.00) please(0.00) everyone(0.00) family.(-0.00) 
Node-1.4: product(-0.00) amazon(-0.00) platform(-0.00) title(0.00) content(-0.00) title(-0.00) missing.(-0.00) content(0.00) beverly(0.00) hills(-0.00) chihuahua(-0.00) 2is(0.00) power(-0.00) love(-0.00) family--(-0.00) talking(-0.00) chihuahuas,(0.00) course.(-0.00) sequel(-0.01) tobeverly(-0.00) hills(-0.00) chihuahua,(-0.00) chloe(0.01) papi(-0.00) married(-0.00) grand(-0.00) style,(-0.00) close(-0.00) celebration(-0.00) wishing(0.00) upon(-0.00) falling(-0.00) star.(-0.00) four(0.00) months(0.00) later,(-0.00) two(0.00) happily(0.00) adjust</verbalized-graph>

### Classification Label
Books

### Reasoning

### Free-Text Explanation

(P.S.: 1. complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance. Words with higher scores are more influential for the classification. It is not necessary to quote every score.
3. use the *whole* graph structure you reconstructed during reasoning for the format of the Free-Text Explanation. Indents and node indexes are necessary, representing the hierarchy of the co-purchase graph.)

~~~~~~

## 3. Target node

- ID: 25079
- Title: Chilly Dogs
- True class (canonical `y`): **Movies & TV**
- Predicted class, canonical GraphSAGE (`prediction_agreement/products_canonical_vs_gspell_full.json`): **Movies & TV**
- Prediction recorded by this method's pipeline: **Books**

Canonical text (`raw_text`):

~~~~~~text
Product from Amazon platform with title and content: Title: Chilly Dogs. Content: The lovely snowy expanses of Alaska are the setting forChilly Dogs, a goofy comedy about a travel agency clerk (Skeet Ulrich,Scream,The Newton Boys) from Los Angeles who has to prove his mettle by racing a team of mismatched sled dogs from Anchorage to Nome. Only this will allow him to claim his grandfather's inheritance--and a wily lawyer (Leslie Nielsen, mugging shamelessly as usual) intends to claim that inheritance for himself by knocking the clerk out of the race. It's not surprising to see Ulrich in a movie full of clumsy, half-baked slapstick and bodily function humor, but why is Natasha Henstridge (Species,The Whole Nine Yards) thrown away as a bland romantic foil? Her intelligence and sexy/tough persona deserve better--she providesChilly Dogswith what little momentum it has. Also featuring Rik Mayall (The Young Ones).--Bret Fetzer
~~~~~~

## 4. Neighbors (canonical `edge_index`, `products_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 4884 | Movies & TV | Snow Dogs |

### 2-hop (shortest distance exactly 2): 8 nodes

| node id | true class | title |
|---|---|---|
| 545 | Movies & TV | missing |
| 550 | Movies & TV | Inspector Gadget |
| 551 | Movies & TV | Air Bud Spikes Back |
| 4820 | Movies & TV | missing |
| 4915 | Movies & TV | missing |
| 25078 | Movies & TV | My Favorite Martian |
| 25080 | Movies & TV | missing |
| 25081 | Movies & TV | Eight Below (Widescreen Edition) |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_products/93.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Books**, ground truth = **Movies & TV**.
The verbalized graph is 12737 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 25079 | 170 | 0.0823 | yes |
| Node-1 | 1 | 4884 | 182 | 0.1366 | yes |
| Node-1.1 | 2 | 545 | 213 | 0.0023 | yes |
| Node-1.2 | 3 | 550 | 17 | 0.0183 | yes |
| Node-1.3 | 4 | 551 | 117 | 0.0078 | yes |
| Node-1.4 | 5 | 4820 | 327 | 0.0076 | yes |
| Node-1.5 | 6 | 4915 | 289 | 0.0029 | no |
| Node-1.6 | 7 | 25078 | 19 | 0.0148 | no |
| Node-1.7 | 8 | 25080 | 155 | 0.0156 | no |
| Node-1.8 | 9 | 25081 | 111 | 0.0080 | no |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->Node-1.6, Node-1->Node-1.7, Node-1->Node-1.8, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, Node-1.6->Node-1, Node-1.7->Node-1, Node-1.8->Node-1, ROOT->Node-1

### Tokens and scores

**ROOT** (global 25079):

~~~~~~text
product (-0.0004) from (0.0021) amazon (0.0184) platform (0.0185) with (0.0070) title (0.0037) and (0.0178) content (0.0131) : (0.0217) title (0.0214) : (0.0287) chilly (0.0123) dogs. (-0.0138) content (0.0211) : (0.0239) the (-0.0112) lovely (-0.0004) snowy (-0.0062) expanses (0.0072) of (0.0007) alaska (0.0163) are (0.0085) the (-0.0006) setting (0.0044) forchilly (-0.0094) dogs, (-0.0078) a (-0.0007) goofy (0.0045) comedy (0.0018) about (-0.0001) a (0.0149) travel (0.0064) agency (0.0169) clerk (0.0007) ( (0.0259) skeet (0.0194) ulrich, (0.0544) scream, (-0.0077) the (0.0823) newton (0.0205) boys (0.0306) ) (-0.0058) from (0.0045) los (-0.0009) angeles (0.0000) who (-0.0007) has (-0.0015) to (0.0081) prove (0.0189) his (0.0121) mettle (0.0105) by (0.0009) racing (0.0110) a (-0.0012) team (-0.0031) of (0.0108) mismatched (0.0098) sled (0.0083) dogs (-0.0036) from (0.0190) anchorage (0.0396) to (0.0051) nome. (-0.0020) only (0.0122) this (0.0124) will (0.0050) allow (0.0080) him (0.0047) to (0.0116) claim (0.0003) his (0.0152) grandfather (-0.0049) ' (-0.0009) s (0.0207) inheritance-- (0.0086) and (0.0138) a (-0.0116) wily (0.0028) lawyer (0.0150) ( (0.0040) leslie (0.0038) nielsen, (-0.0022) mugging (0.0203) shamelessly (0.0153) as (0.0173) usual (0.0165) ) (0.0212) intends (0.0113) to (0.0102) claim (0.0046) that (0.0129) inheritance (0.0246) for (0.0144) himself (0.0136) by (0.0202) knocking (0.0183) the (-0.0180) clerk (0.0100) out (0.0144) of (0.0161) the (0.0003) race. (-0.0176) it (0.0266) ' (0.0034) s (-0.0017) not (0.0203) surprising (0.0123) to (0.0186) see (0.0218) ulrich (-0.0194) in (0.0207) a (0.0044) movie (-0.0039) full (0.0077) of (0.0131) clumsy, (-0.0046) half- (0.0043) baked (-0.0008) slapstick (0.0001) and (0.0145) bodily (-0.0001) function (0.0160) humor, (0.0036) but (0.0140) why (0.0183) is (0.0000) natasha (0.0073) henstridge (0.0106) ( (0.0235) species, (0.0103) the (0.0020) whole (0.0167) nine (0.0064) yards (0.0041) ) (0.0193) thrown (0.0099) away (0.0100) as (0.0105) a (-0.0003) bland (0.0115) romantic (0.0005) foil? (-0.0039) her (0.0036) intelligence (-0.0070) and (0.0055) sexy (0.0217) / (0.0173) tough (0.0111) persona (0.0239) deserve (-0.0113) better-- (0.0199) she (0.0002) provideschilly (0.0104) dogswith (0.0123) what (-0.0096) little (0.0072) momentum (0.0216) it (0.0044) has. (-0.0196) also (0.0299) featuring (0.0188) rik (0.0110) mayall (0.0309) ( (0.0125) the (-0.0046) young (0.0001) ones (-0.0048) ).-- (-0.0175) bret (-0.0371) fetzer (-0.0072)
~~~~~~

**Node-1** (global 4884):

~~~~~~text
product (0.0225) from (-0.0142) amazon (0.0046) platform (-0.0328) with (-0.0089) title (-0.0174) and (-0.0023) content (-0.0045) : (-0.0106) title (-0.0130) : (-0.0083) snow (-0.0116) dogs. (-0.0130) content (0.0213) : (0.0133) make (-0.0084) no (-0.0095) bones (-0.0144) about (-0.0166) it-- (-0.0242) disney (-0.0155) ' (-0.0185) s (-0.0086) snow (-0.0246) dogs (-0.0070) is (-0.0192) a (-0.0149) hilarious, (-0.0067) action- (-0.0200) packed (-0.0544) comedy (0.0330) your (-0.0390) whole (-0.0204) family (0.0097) will (-0.0231) love. (-0.0016) eight (-0.0267) adorable (0.0026) but (-0.0120) mischievous (0.0048) dogs (-0.0111) get (-0.0063) the (-0.0244) best (-0.0040) of (-0.0127) dog (-0.0105) hater (-0.0046) ted (-0.0249) brooks (-0.0062) ( (-0.0549) cuba (0.0323) gooding, (-0.0163) jr. (-0.0133) ) (0.1366) when (0.0177) he (-0.0105) leaves (-0.0287) his (-0.0077) successful (-0.0144) miami (-0.0077) beach (-0.0353) dental (-0.0221) practice (-0.0083) for (-0.0218) the (-0.0112) wilds (-0.0101) of (-0.0013) alaska (0.0120) to (-0.0043) claim (0.0224) his (-0.0314) inheritance-- (-0.0193) seven (0.0061) siberian (-0.0354) huskies (-0.0308) and (-0.0117) a (0.0157) border (-0.0174) collie-- (-0.0136) and (-0.0075) discover (0.0018) his (-0.0094) roots. (-0.0398) as (0.0063) ted (0.0143) ' (0.0052) s (0.0072) life (-0.0161) goes (-0.0192) to (-0.0113) the (-0.0137) dogs, (-0.0037) he (-0.0021) rises (-0.0049) to (-0.0191) the (0.0116) occasion (-0.0252) and (-0.0307) vows (-0.0345) to (-0.0343) learn (-0.0174) to (-0.0193) mush (-0.0131) with (-0.0124) his (-0.0092) inheritance. (0.0104) totally (-0.0175) out (-0.0127) of (-0.0147) his (-0.0142) element, (-0.0144) he (-0.0443) faces (-0.0212) challenges (-0.0257) he (-0.0141) ' (-0.0020) s (-0.0015) never (0.0073) dreamed (-0.0375) of. (0.0092) there (-0.0072) ' (-0.0047) s (-0.0054) a (-0.0273) blizzard, (0.0008) thin (-0.0078) ice, (0.0139) an (-0.0097) intimidating (-0.0236) crusty (-0.0157) old (-0.0083) mountain (-0.0044) man (-0.0136) named (-0.0130) thunder (0.0033) jack (0.0207) ( (-0.0474) james (0.0033) coburn (-0.0006) ), (0.0095) the (-0.0314) arctic (0.0116) challenge (-0.0214) sled (0.0008) dog (0.0092) race (-0.0095) that (-0.0061) ' (-0.0009) s (-0.0056) only (-0.0132) two (-0.0012) weeks (-0.0211) away, (0.0001) and (-0.0280) a (0.0058) life- (-0.0065) and- (-0.0227) death (-0.0189) rescue. (0.0249) this (-0.0211) fish- (-0.0055) out- (-0.0231) of (-0.0185) water, (-0.0048) tail- (-0.0150) wagging (-0.0080) comedy (-0.0044) is (-0.0074) nothing (-0.0442) but (-0.0202) doggone (-0.0005) good (0.0207) fun (-0.0338) and (-0.0209) a (0.0001) celebration (-0.0010) of (-0.0188) family-- (-0.0308) both (-0.0173) human (-0.0061) and (-0.0147) canine! (0.0284)
~~~~~~

**Node-1.1** (global 545):

~~~~~~text
product (-0.0008) from (0.0005) amazon (-0.0021) platform (0.0003) with (0.0000) title (0.0002) and (0.0003) content (-0.0008) : (0.0008) title (0.0002) : (0.0010) missing. (0.0004) content (-0.0004) : (0.0016) air (0.0014) bud (0.0014) spikes (0.0012) back (0.0017) : (0.0011) disney (0.0004) serves (-0.0005) up (0.0020) another (0.0008) adventure (0.0005) starring (0.0017) everyone (-0.0001) ' (-0.0001) s (0.0009) favorite (0.0005) sports- (0.0005) playing (0.0004) golden (-0.0000) retriever, (0.0004) buddy! (-0.0000) this (0.0007) time, (0.0004) he (-0.0000) masters (0.0001) the (0.0003) coolest (0.0005) sport (0.0000) under (0.0003) the (0.0000) sun... (-0.0005) beach (-0.0005) volleyball! (0.0009) but (0.0000) there (0.0002) ' (0.0001) s (0.0010) plenty (-0.0001) of (0.0002) action (0.0006) off (0.0005) the (-0.0000) court (0.0000) as (0.0003) well-- (0.0008) a (0.0004) rash (0.0004) of (0.0007) mysterious (0.0012) crimes (-0.0004) have (0.0017) been (0.0010) puzzling (0.0003) everyone... (-0.0009) and (0.0010) the (0.0001) paw (-0.0005) prints (0.0007) seem (0.0001) to (0.0000) point (0.0008) to (-0.0001) buddy! (0.0020) so, (0.0005) it (0.0008) ' (0.0003) s (0.0006) up (0.0012) to (0.0002) buddy (0.0015) to (-0.0001) lead (0.0013) the (0.0005) authorities (-0.0010) to (0.0007) the (0.0001) real (0.0009) culprit! (0.0009) with (0.0009) a (0.0006) special (0.0013) appearance (0.0015) by (0.0013) pro (0.0009) volleyball (0.0006) champion (0.0004) gabrielle (0.0017) reece (0.0009) and (0.0004) a (0.0007) heartwarming (0.0004) story, (0.0016) your (0.0001) family (0.0005) is (0.0006) sure (-0.0004) to (-0.0001) enjoy (-0.0006) this (0.0010) fun- (0.0003) filled (0.0013) adventure! (0.0007) ~ (-0.0029) ~ (-0.0030) air (-0.0011) bud (-0.0002) : (0.0005) seventh (0.0005) inning (0.0003) fetch (0.0000) : (-0.0005) air (0.0004) bud (-0.0006) knocks (0.0005) one (0.0005) out (0.0007) of (0.0007) the (-0.0006) park (0.0004) when (0.0006) he (0.0008) takes (0.0005) up (0.0010) baseball (-0.0002) in (0.0008) this (0.0010) fun (0.0008) and (0.0005) heartwarming (0.0007) disney (0.0014) adventure! (-0.0005) this (0.0004) time, (0.0003) buddy (0.0000) joins (0.0006) in (0.0004) and (0.0004) shows (0.0015) that (0.0007) he (0.0008) ' (0.0006) s (0.0010) a (0.0002) natural (0.0003) baseball (0.0000) player (0.0006) with (0.0004) major (0.0010) league (-0.0002) talent! (0.0009) in (0.0006) the (0.0003) midst (-0.0002) of (0.0006) the (0.0004) season, (0.0009) however, (0.0004) a (0.0010) terrible (0.0002) discovery (0.0019) is (-0.0000) made (-0.0004) : (0.0001) buddy (0.0001) ' (0.0004) s (0.0015) now- (-0.0001) grown (0.0001) puppies (0.0004) have (0.0003) mysteriously (0.0003) begun (-0.0005) to (-0.0002) disappear (0.0001) from (0.0002) their (0.0005) new (0.0005) homes! (-0.0002) now (0.0002) it (0.0009) ' (0.0006) s (-0.0001) up (0.0008) to (-0.0002) buddy (0.0006) to (0.0000) stop (-0.0001) the (-0.0003) dog- (0.0007) nappings (0.0009) and (-0.0000) find (0.0002) his (0.0006) pups (-0.0003) before (-0.0000) it (0.0011) ' (-0.0000) s (0.0001) too (0.0023) late! (-0.0022)
~~~~~~

**Node-1.2** (global 550):

~~~~~~text
product (-0.0025) from (0.0108) amazon (-0.0045) platform (-0.0039) with (0.0183) title (0.0034) and (0.0081) content (0.0169) : (0.0045) title (0.0058) : (0.0100) inspector (-0.0059) gadget. (0.0024) content (0.0154) : (0.0095) inspector (-0.0096) gadget (-0.0017)
~~~~~~

**Node-1.3** (global 551):

~~~~~~text
product (-0.0009) from (-0.0045) amazon (0.0017) platform (0.0021) with (-0.0019) title (0.0029) and (-0.0024) content (-0.0006) : (0.0050) title (0.0020) : (-0.0018) air (-0.0037) bud (0.0013) spikes (0.0009) back. (-0.0014) content (0.0062) : (0.0058) disney (-0.0031) serves (0.0006) up (-0.0018) an (-0.0016) all- (-0.0015) new (-0.0012) adventure (-0.0017) starring (0.0004) everyone (-0.0026) ' (-0.0015) s (0.0004) favorite (0.0014) sports- (-0.0003) playing (0.0036) golden (-0.0006) retriever, (-0.0024) buddy! (-0.0001) this (-0.0022) time, (-0.0006) he (-0.0010) masters (-0.0004) the (-0.0020) coolest (0.0006) sport (0.0003) under (0.0004) the (0.0004) sun... (0.0015) beach (0.0014) volleyball! (0.0024) but (-0.0006) there (-0.0010) ' (-0.0011) s (-0.0008) plenty (0.0006) of (-0.0008) action (0.0013) off (-0.0001) the (0.0005) court (-0.0023) as (0.0018) well-- (-0.0005) a (0.0007) rash (0.0009) of (0.0007) mysterious (0.0017) crimes (0.0017) has (0.0029) been (-0.0007) puzzling (0.0006) everyone... (0.0026) and (0.0002) the (-0.0004) paw (0.0048) prints (0.0020) seem (0.0006) to (0.0007) point (0.0015) to (0.0011) buddy! (0.0003) so (0.0027) it (0.0024) ' (0.0002) s (-0.0005) up (0.0016) to (0.0020) buddy (0.0030) to (0.0016) lead (0.0031) the (0.0003) authorities (0.0004) to (0.0013) the (0.0024) real (0.0019) culprit! (0.0016) with (0.0048) a (0.0021) special (0.0011) appearance (0.0050) by (0.0034) pro- (0.0022) volleyball (0.0040) champion (0.0048) gabrielle (0.0078) reece (0.0077) and (0.0021) a (0.0014) heartwarming (0.0031) story, (-0.0014) this (-0.0030) fun- (-0.0002) filled (-0.0004) adventure (-0.0032) is (-0.0001) sure (0.0016) to (-0.0022) please (0.0004) everyone (0.0045) in (0.0045) your (-0.0147) family. (-0.0028)
~~~~~~

**Node-1.4** (global 4820):

~~~~~~text
product (-0.0014) from (-0.0013) amazon (-0.0005) platform (-0.0016) with (-0.0007) title (0.0007) and (-0.0013) content (-0.0008) : (-0.0006) title (-0.0001) : (-0.0005) missing. (-0.0005) content (0.0001) : (0.0006) beverly (0.0014) hills (-0.0009) chihuahua (-0.0016) 2is (0.0008) all (0.0004) about (0.0003) the (-0.0003) power (-0.0001) of (-0.0001) love (-0.0004) and (0.0008) family-- (-0.0008) and (-0.0000) talking (-0.0034) chihuahuas, (0.0003) of (-0.0007) course. (-0.0017) in (0.0008) this (0.0001) sequel (-0.0084) tobeverly (-0.0008) hills (-0.0020) chihuahua, (-0.0020) chloe (0.0076) and (-0.0011) papi (-0.0007) have (0.0005) just (-0.0003) been (-0.0006) married (-0.0008) in (-0.0009) grand (-0.0003) style, (-0.0012) and (-0.0005) they (0.0001) close (-0.0000) their (-0.0005) celebration (-0.0002) by (-0.0010) wishing (0.0005) upon (-0.0000) a (-0.0007) falling (-0.0007) star. (-0.0011) four (0.0006) months (0.0004) later, (-0.0005) the (0.0004) two (0.0000) are (0.0002) happily (0.0010) adjusting (0.0000) to (-0.0004) their (0.0001) new (-0.0003) roles (0.0010) as (-0.0014) proud (0.0002) parents-- (0.0000) something (0.0006) that (-0.0000) ' (0.0001) s (-0.0004) not (-0.0002) such (-0.0000) an (-0.0002) easy (0.0004) task (-0.0011) for (-0.0011) papi, (0.0002) who (-0.0001) often (-0.0008) seems (0.0004) to (-0.0009) act (-0.0006) more (-0.0006) like (-0.0011) a (-0.0008) sixth (0.0003) puppy (0.0019) than (-0.0007) a (-0.0002) father, (-0.0009) and (-0.0010) whose (-0.0000) stories (-0.0012) of (-0.0008) famous (-0.0024) historical (-0.0005) dogs (0.0001) only (0.0001) seem (-0.0001) to (-0.0008) get (-0.0003) his (-0.0006) overexuberant (-0.0000) puppies (0.0001) into (-0.0007) trouble. (-0.0002) papi (0.0007) ' (-0.0001) s (-0.0013) owner (-0.0012) sam (0.0010) has (0.0000) been (-0.0003) left (-0.0006) in (-0.0002) charge (-0.0001) of (-0.0005) all (0.0002) the (-0.0002) dogs, (-0.0015) while (-0.0011) his (-0.0018) girlfriend (0.0025) rachel (0.0002) and (-0.0007) her (-0.0001) aunt (-0.0005) viv (0.0002) travel (-0.0004) to (-0.0002) the (-0.0008) rainforest (-0.0052) to (-0.0008) do (0.0001) some (-0.0003) important (-0.0003) research. (-0.0010) it (-0.0003) looks (0.0009) like (-0.0003) life (0.0002) for (-0.0009) the (0.0002) new (-0.0005) canine (0.0010) family (-0.0013) will (-0.0005) be (-0.0004) all (-0.0001) fancy (-0.0002) dog (-0.0005) parks (0.0002) and (-0.0003) cute (0.0004) little (0.0002) doggie (-0.0001) outfits (0.0007) until (0.0010) sam (-0.0008) discovers (0.0000) that (-0.0009) his (-0.0017) parents (-0.0003) are (-0.0000) facing (0.0001) foreclosure (-0.0000) on (-0.0010) their (0.0003) home. (0.0003) sam (0.0012) and (0.0004) his (-0.0003) father (0.0005) head (-0.0003) to (0.0006) the (0.0004) bank (0.0006) to (0.0002) see (-0.0000) what (0.0003) can (0.0001) be (-0.0001) done, (-0.0001) while (0.0005) papi (-0.0008) ' (0.0002) s (-0.0000) brother (-0.0006) pedro (0.0009) joins (-0.0001) forces (0.0001) with (-0.0002) sam, (-0.0002) papi, (-0.0004) his (-0.0005) pups, (0.0007) and (-0.0012) the (0.0002) newly (0.0000) arrived (-0.0006) delgado (0.0002) ( (-0.0010) who (0.0002) ' (0.0004) s (0.0003) just (0.0002) shown (-0.0005) up (0.0003) on (-0.0005) his (0.0005) own (-0.0003) important (0.0001) mission (-0.0005) ) (-0.0001) to (0.0005) formulate (0.0001) their (-0.0001) own (0.0001) plan (-0.0003) to (-0.0000) help (-0.0002) sam (0.0003) ' (0.0006) s (-0.0001) parents. (-0.0006) one (0.0006) dog (-0.0011) show (0.0005) and (-0.0005) one (-0.0003) bank (-0.0004) robbery (-0.0007) later, (-0.0001) it (-0.0004) looks (0.0001) like (-0.0001) these (-0.0005) financially (0.0015) turbulent (0.0001) times (-0.0006) will (0.0015) claim (0.0006) not (0.0003) only (0.0001) sam (0.0004) ' (0.0003) s (-0.0002) childhood (0.0003) home, (-0.0001) but (-0.0000) also (-0.0004) his (0.0001) relationship (0.0001) with (-0.0005) rachel. (0.0004) in (-0.0009) the (-0.0016) end, (-0.0002) both (-0.0004) dogs (0.0010) and (-0.0012) humans (-0.0034) learn (-0.0004) some (-0.0009) important (-0.0012) lessons (-0.0006) about (-0.0004) making (0.0005) tough (-0.0009) choices, (0.0007) the (-0.0002) importance (-0.0007) of (0.0003) family (0.0008) and (-0.0002) love, (0.0013) and (-0.0007) the (0.0004) power (0.0015) of (-0.0001) collaboration. (-0.0001) cute (0.0019) talking (0.0015) dogs (0.0014) are (0.0007) always (0.0006) a (0.0012) winner (0.0002) with (-0.0023) young (-0.0003) viewers (-0.0005) and (-0.0001) adults (-0.0001) will (-0.0002) find (-0.0004) the (-0.0008) film (0.0010) easy (-0.0011) enough (0.0009) to (0.0009) sit (0.0006) through, (0.0005) if (-0.0003) not (-0.0010) particularly (0.0001) compelling. (-0.0004) george (-0.0056) lopez (0.0062) returns (0.0021) as (-0.0005) papi, (-0.0008) but (0.0002) virtually (-0.0003) all (-0.0019) the (0.0007) other (-0.0007) roles (0.0005) have (-0.0005) been (-0.0005) recast (0.0022)
~~~~~~

**Node-1.5** (global 4915):

~~~~~~text
product (-0.0006) from (-0.0013) amazon (0.0003) platform (0.0022) with (0.0004) title (0.0011) and (0.0002) content (-0.0002) : (0.0007) title (0.0006) : (-0.0000) missing. (0.0007) content (-0.0003) : (0.0001) a (-0.0003) sort (0.0006) of (0.0004) ananniemeetssanta (-0.0001) buddies, (-0.0021) the (-0.0017) search (-0.0003) for (0.0014) santa (-0.0006) pawsis (-0.0002) a (-0.0013) musical (0.0009) production (0.0016) that (0.0002) tells (0.0003) the (-0.0003) story (0.0006) of (0.0002) how (-0.0013) santa (0.0009) and (0.0007) a (0.0005) young (0.0006) dog (0.0012) named (-0.0005) paws (0.0013) became (0.0001) best (0.0005) friends, (0.0010) and (-0.0003) together (0.0001) forever (0.0004) changed (0.0008) the (-0.0002) lives (0.0003) of (-0.0001) a (-0.0000) houseful (0.0001) of (0.0005) new (0.0006) york (0.0001) city (0.0005) orphans (-0.0024) and (-0.0007) a (0.0003) host (0.0008) of (0.0007) other (0.0005) new (0.0014) yorkers. (-0.0003) the (-0.0013) film (0.0024) chronicles (-0.0001) paws (-0.0008) ' (-0.0006) s (0.0003) desperate (0.0004) attempts (0.0013) to (-0.0001) find (0.0004) santa (-0.0012) when (0.0010) they (0.0001) ' (0.0007) re (-0.0007) separated (0.0014) in (0.0005) new (0.0005) york (0.0000) city, (-0.0005) the (0.0006) important (0.0014) roles (0.0011) both (0.0004) santa (0.0005) and (0.0012) paws (-0.0024) play (0.0008) in (0.0007) spreading (-0.0015) the (-0.0003) christmas (0.0008) spirit (0.0000) to (0.0003) children (0.0002) and (0.0005) adults (0.0009) alike, (-0.0008) and (0.0004) the (0.0008) concern (-0.0006) of (0.0004) mrs. (-0.0017) claus (-0.0006) and (-0.0006) the (0.0008) elves (0.0000) over (0.0020) santa (0.0004) and (0.0007) paws (-0.0022) ' (0.0002) s (-0.0002) longer- (0.0002) than- (0.0004) expected (0.0007) absence (0.0003) from (-0.0004) the (-0.0000) north (0.0009) pole. (0.0001) the (0.0011) film (0.0018) also (0.0016) has (0.0014) some (0.0010) very (0.0009) dark, (0.0010) potentially (-0.0001) distressing (0.0000) scenes (0.0013) in (0.0006) which (0.0003) young (0.0014) orphans (-0.0038) are (0.0004) verbally (0.0000) abused, (0.0010) neglected, (0.0006) and (0.0001) unfairly (0.0000) punished, (0.0003) as (0.0006) well (0.0003) as (0.0004) one (0.0006) particularly (0.0010) scary (0.0014) moment (0.0000) when (0.0008) a (0.0012) young (0.0002) girl (0.0009) endangers (0.0002) her (-0.0004) life (0.0002) by (0.0001) crawling (-0.0002) into (0.0003) a (0.0003) working (0.0004) incinerator. (0.0006) first (0.0011) and (0.0012) foremost (-0.0003) a (0.0005) touching (0.0003) story (-0.0001) about (-0.0004) the (0.0003) power (0.0008) of (0.0007) giving (0.0002) and (0.0008) believing, (-0.0001) the (-0.0001) film (0.0020) is (0.0000) also (0.0005) a (0.0000) treasure (0.0012) trove (-0.0000) of (0.0006) big (0.0008) musical (-0.0003) numbers (0.0020) that (0.0002) feature (0.0011) everything (0.0007) from (0.0004) broadway- (0.0003) style (0.0009) productions (0.0010) to (0.0006) pop- (0.0002) inspired (0.0006) songs (0.0003) and (-0.0001) emotionally (0.0007) charged (0.0003) ballads (0.0015) that (-0.0001) are (0.0005) nicely (0.0006) performed (0.0001) and (-0.0008) choreographed-- (-0.0006) especially (0.0004) those (0.0008) by (-0.0002) madison (-0.0006) pettis, (-0.0006) kaitlyn (-0.0005) maher, (-0.0004) richard (0.0002) riehle, (-0.0003) and (-0.0003) danny (0.0003) woodburn. (-0.0004) the (0.0023) animation (0.0009) is (0.0020) well (0.0005) done (0.0009) and (0.0001) blends (0.0009) seamlessly (0.0012) with (-0.0003) the (-0.0003) live (0.0001) action-- (0.0000) something (0.0006) that (0.0004) ' (-0.0001) s (0.0005) in (0.0004) stark (0.0008) contrast (0.0012) to (0.0003) some (0.0017) of (0.0007) the (0.0010) poorly (0.0008) handled (0.0005) animated (0.0011) scenes (0.0015) found (-0.0007) in (0.0003) the (0.0003) 2009santa (0.0007) buddies. (-0.0011) bonus (-0.0035) features (0.0018) include (0.0029) a (0.0008) pop- (0.0005) up (-0.0008) storybook (0.0008) narrated (0.0023) by (-0.0002) rosebud (-0.0010) of (0.0009) thebuddiesmovies, (-0.0001) a (0.0019) sing- (0.0013) along (-0.0016) option (0.0025) for (0.0010) all (0.0002) the (-0.0001) songs (0.0006) in (-0.0002) the (-0.0006) film, (0.0012) and (0.0011) deleted (0.0024) scenes. (0.0005) ( (0.0011) ages (0.0002) 5 (0.0007) and (0.0014) older (0.0001) )-- (0.0011) tami (0.0010) horiuchi (-0.0024)
~~~~~~

**Node-1.6** (global 25078):

~~~~~~text
product (0.0088) from (0.0033) amazon (-0.0052) platform (0.0148) with (0.0094) title (0.0076) and (0.0074) content (0.0145) : (0.0045) title (0.0098) : (0.0040) my (0.0015) favorite (0.0025) martian. (0.0063) content (0.0112) : (0.0056) my (0.0010) favorite (0.0057) martian (0.0143)
~~~~~~

**Node-1.7** (global 25080):

~~~~~~text
product (-0.0031) from (-0.0007) amazon (-0.0045) platform (0.0026) with (0.0014) title (0.0018) and (0.0010) content (-0.0026) : (0.0030) title (0.0002) : (0.0017) missing. (0.0005) content (-0.0019) : (0.0007) john (0.0022) travolta (0.0005) and (0.0010) robin (0.0015) williams (-0.0014) star (0.0068) in (-0.0002) old (-0.0007) dogs, (-0.0030) the (0.0007) hilarious (0.0013) family (-0.0014) comedy (-0.0035) that (0.0013) will (0.0011) have (0.0017) you (0.0008) howling. (-0.0029) two (0.0010) best (0.0006) friends (0.0001) have (0.0010) their (-0.0006) lives (-0.0003) turned (-0.0000) upside (0.0027) down (0.0009) when (-0.0002) they (0.0018) ' (0.0014) re (-0.0008) unexpectedly (0.0047) charged (0.0029) with (0.0011) the (0.0010) care (0.0008) of (0.0022) seven- (0.0016) year- (0.0023) old (0.0024) twins (-0.0001) while (0.0010) on (0.0021) the (-0.0005) verge (0.0010) of (-0.0000) the (-0.0005) biggest (0.0025) business (0.0016) deal (0.0009) of (0.0015) their (0.0012) lives. (0.0024) the (-0.0032) clueless (0.0016) bachelors (0.0017) stumble (-0.0002) in (0.0012) their (0.0014) efforts (0.0033) to (0.0011) take (0.0012) care (0.0017) of (0.0009) the (-0.0017) children, (0.0013) leading (0.0026) to (0.0021) one (0.0018) debacle (0.0023) after (0.0031) another, (0.0018) with (0.0040) a (0.0013) gorilla (0.0035) and (0.0013) some (0.0025) pecking (0.0005) penguins-- (0.0038) and (0.0010) perhaps (0.0029) to (0.0029) a (0.0007) newfound (0.0008) understanding (0.0031) of (0.0014) what (0.0016) ' (-0.0000) s (0.0014) really (0.0038) important (0.0023) in (0.0037) life. (0.0156) featuring (-0.0024) a (0.0032) riotously (0.0014) funny (0.0007) supporting (-0.0005) cast (-0.0007) including (0.0014) seth (-0.0035) green, (0.0015) kelly (0.0002) preston, (-0.0005) matt (0.0016) dillon (0.0003) and (0.0004) lori (0.0011) laughlin, (0.0032) old (0.0054) dogs (-0.0059) is (-0.0001) a (-0.0015) laugh- (0.0027) a- (0.0022) minute (-0.0007) comedy (-0.0025) filled (-0.0024) with (-0.0003) heart. (-0.0031) bonus (-0.0067) features (0.0012) include (0.0008) deleted (-0.0008) scenes, (0.0022) audio (-0.0006) commentary (0.0023) by (-0.0008) director (0.0017) walt (0.0013) becker, (0.0002) producer (0.0024) andrew (0.0022) panay (0.0019) and (0.0007) writers (0.0012) david (0.0032) diamond (0.0015) and (0.0012) david (0.0022) weissman (0.0038)
~~~~~~

**Node-1.8** (global 25081):

~~~~~~text
product (-0.0019) from (-0.0029) amazon (-0.0012) platform (0.0020) with (0.0027) title (0.0008) and (0.0017) content (-0.0007) : (0.0000) title (0.0037) : (-0.0021) eight (-0.0008) below (-0.0001) ( (0.0006) widescreen (0.0018) edition (0.0016) ). (-0.0028) content (0.0036) : (0.0009) walt (0.0008) disney (0.0015) pictures (0.0051) presents (-0.0028) eight (0.0017) below, (-0.0007) the (-0.0026) thrilling (-0.0003) tale (0.0022) of (0.0001) incredible (0.0016) friendship (-0.0007) between (-0.0005) eight (0.0007) amazing (0.0003) sled (-0.0011) dogs (0.0000) and (0.0022) their (0.0007) guide (0.0011) jerry (0.0000) ( (0.0017) paul (0.0018) walker (-0.0007) ). (0.0080) stranded (-0.0008) in (0.0025) antarctica (-0.0002) during (0.0011) the (-0.0015) most (0.0002) unforgiving (0.0003) winter (-0.0007) on (0.0000) the (-0.0001) planet, (0.0021) jerry (-0.0014) ' (0.0007) s (0.0004) beloved (0.0018) sled (-0.0000) dogs (0.0005) must (0.0006) learn (0.0008) to (0.0010) survive (0.0011) together (0.0002) until (0.0008) jerry-- (0.0008) who (0.0020) will (0.0012) stop (0.0007) at (0.0016) nothing-- (0.0018) rescues (0.0013) them. (0.0026) driven (0.0013) by (0.0023) unwavering (0.0002) bonds (0.0023) of (0.0012) friendship, (0.0006) enormous (0.0035) belief (0.0005) in (0.0019) one (0.0019) another, (0.0007) and (0.0004) tremendous (0.0060) courage, (0.0002) jerry (0.0022) and (0.0004) the (0.0025) dogs (-0.0021) make (0.0021) an (0.0009) incredible (0.0005) journey (0.0010) to (0.0019) reunite (0.0014) in (0.0036) this (0.0028) triumphant (0.0039) and (0.0019) inspiring (0.0022) action- (0.0012) adventure (0.0050) the (0.0005) whole (0.0033) family (0.0028) will (0.0032) treasure. (0.0035)
~~~~~~
