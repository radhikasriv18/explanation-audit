# Reference packet: GraphXAIN__Llama-8B__cora__1294

- Method: GraphXAIN; configuration: Llama-8B; dataset: cora; target node: 1294
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/cora/graphxain_cora_llama_2hop_narratives_full.json` ([1294])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the analysis provided by the GNNExplainer, our model confidently predicted that the research paper titled 'Representation Requirements for Supporting Decision Model Formulation' belongs to the 'Probabilistic Methods' category with a confidence level of 99.01%. This prediction was heavily influenced by the absence of specific key words such as 'phenomena,' 'uncertain,' 'underli,' 'autom,' and 'formal,' which are strongly associated with other areas of computer science. On the other hand, the presence of terms like 'patterns' suggests connections to probabilistic approaches, despite their relatively low occurrence in the Cora dataset. Direct citation neighbors such as Node 915 share similar themes, with Node 915's paper 'Automated decision making' explicitly addressing probabilistic methods. Moreover, papers linked at two hops away, such as Node 1172, further solidify this association due to their shared topics in knowledge-based construction of models. The overwhelming agreement among the paper's own citation links and neighboring structures – particularly its 1-hop neighbors whose ground-truth classes also align with Probabilistic Methods – contribute significantly to the model's conviction in this prediction. Overall, these signals indicate a strong affinity between the target paper and 'Probabilistic Methods,' pointing towards the model's accurate classification result.
~~~~~~

## 2. Prompt the method's model received

`prompt` field of the record (sent as the single user message).

**user:**

~~~~~~text
Your goal is to generate a textual narrative explaining why a GNN model made a certain prediction for a target node, based on the output of a GNNExplainer.

### Machine Learning Task:
Multi-class node classification task that predicts the research area of an academic computer science paper. The model classifies each paper into one of 7 categories: Case_Based, Genetic_Algorithms, Neural_Networks, Probabilistic_Methods, Reinforcement_Learning, Rule_Learning, or Theory.

### Dataset:
The Cora citation network contains 2,708 academic computer science papers. Each paper (node) is represented as a bag-of-words feature vector of 1,433 unique Porter-stemmed words derived from the paper's title and abstract — each feature is binary (1 = word present, 0 = absent). Edges represent undirected citation links between papers. The task is to classify each paper into its research sub-area based on its content and the content of papers it cites or is cited by.

### Target Paper (node 1294):
Title: Representation Requirements for Supporting Decision Model Formulation  
Abstract: This paper outlines a methodology for analyzing the representational support for knowledge-based decision-modeling in a broad domain. A relevant set of inference patterns and knowledge types are identified. By c

### Model Prediction:
{
  "Target Node": 1294,
  "Predicted Class": "Probabilistic_Methods",
  "Confidence": 0.9901
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='phenomena', importance=0.7142, present_in_paper=0
  word='uncertain', importance=0.6906, present_in_paper=0
  word='underli', importance=0.6883, present_in_paper=0
  word='autom', importance=0.6624, present_in_paper=0
  word='patterns', importance=0.6604, present_in_paper=1
  word='formal', importance=0.659, present_in_paper=0
  word='results', importance=0.6576, present_in_paper=1

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 1
Label distribution across all 1-hop neighbors (ground-truth class): Probabilistic_Methods=100.0%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 915 | edge_importance=0.3949 | class=Probabilistic_Methods | Title: Abstract  
Abstract: Automated decision making is often complicated by the complexity of the knowledge involved. Much of this complexity arises from the context-sensitive variations of the unde

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 1172 | edge_importance=0.7882 | class=Probabilistic_Methods | Title: Introduction to the Special Section on Knowledge-Based Construction of Probabilistic and Decision Models (IEEE Transactions
Abstract: Modeling techniques developed recently in the AI and uncert

Generate a fluent, cohesive narrative explaining the prediction. Rules:

**Format rules:**
1) Start the explanation immediately — no preamble.
2) Limit the entire answer to 8 sentences or fewer.
3) Do not use tables or bullet lists — write a single cohesive paragraph.

**Content rules:**
1) State clearly what class the model predicted and with what confidence.
2) Discuss how the top BOW features contributed — note whether each high-importance word is actually present or absent in the paper.
3) Discuss how the most influential direct (1-hop) citation neighbors shaped the prediction, describing them by topic or title.
4) Mention how 2-hop neighbors reinforce the pattern if relevant.
5) Interpret WHY a feature or connection pushed the prediction in a certain direction.
6) Do not quote raw importance numbers; use relative language (e.g., "most influential", "strongly associated").
7) Use clear language that a general audience can understand.

~~~~~~

## 3. Target node

- ID: 1294
- Title: Representation Requirements for Supporting Decision Model Formulation
- True class (canonical `y`): **Probabilistic_Methods**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Probabilistic_Methods**
- Prediction recorded by this method's pipeline: **Probabilistic_Methods**

Canonical text (`raw_text`):

~~~~~~text
Title: Representation Requirements for Supporting Decision Model Formulation  
Abstract: This paper outlines a methodology for analyzing the representational support for knowledge-based decision-modeling in a broad domain. A relevant set of inference patterns and knowledge types are identified. By comparing the analysis results to existing representations, some insights are gained into a design approach for integrating categorical and uncertain knowledge in a context sensitive manner.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 915 | Probabilistic_Methods | Abstract |

### 2-hop (shortest distance exactly 2): 1 nodes

| node id | true class | title |
|---|---|---|
| 1172 | Probabilistic_Methods | Introduction to the Special Section on Knowledge-Based Construction of Probabilistic and Decision Models (IEEE Transactions |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=1294).
Recorded prediction: `{"Target Node": 1294, "Predicted Class": "Probabilistic_Methods", "Confidence": 0.9901}`
Recorded graph stats: `{"total_1hop_degree": 1, "neighbor_label_ratio": {"Probabilistic_Methods": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | phenomena | 0.7142 | 0 |
| 2 | uncertain | 0.6906 | 0 |
| 3 | underli | 0.6883 | 0 |
| 4 | autom | 0.6624 | 0 |
| 5 | patterns | 0.6604 | 1 |
| 6 | formal | 0.659 | 0 |
| 7 | results | 0.6576 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
