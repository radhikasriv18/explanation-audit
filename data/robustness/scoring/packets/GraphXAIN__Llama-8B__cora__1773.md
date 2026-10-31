# Reference packet: GraphXAIN__Llama-8B__cora__1773

- Method: GraphXAIN; configuration: Llama-8B; dataset: cora; target node: 1773
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/cora/graphxain_cora_llama_2hop_narratives_full.json` ([1773])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
For node 1773, our machine learning model predicted a research sub-area classification of "Neural Networks" with extremely high confidence at 99.25%. This outcome is largely driven by the presence of key terms in the paper's abstract, such as "mechanics" and "paradigm," which are strongly associated with the field of Neural Networks. Furthermore, upon examining the paper's direct citation neighbors, we find that they overwhelmingly belong to the same category - over 90% share a label of "Neural Networks". Specifically, papers like "Volatility of Volatility of Financial Markets" make explicit connections between volatility analysis and neural networks, reinforcing our initial interpretation. Additionally, two-hop neighbors also tend towards this category, as exemplified by papers discussing applications of statistical mechanics methodology and optimal trading strategies in financial systems. The overall evidence from both local graph structure and key neighboring relationships leads us to believe that the predictive force behind our model decision lies in recognizing these patterns of terminology usage and structural associations, lending credence to our final conclusion.
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

### Target Paper (node 1773):
Title: Canonical Momenta Indicators of Financial Markets and Neocortical EEG  
Abstract: A paradigm of statistical mechanics of financial markets (SMFM) is fit to multivariate financial markets using Adaptive Simulated Annealing (ASA), a global optimization algorithm, to perform maximum likelihood f

### Model Prediction:
{
  "Target Node": 1773,
  "Predicted Class": "Neural_Networks",
  "Confidence": 0.9925
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='mechanics', importance=0.6194, present_in_paper=1
  word='model', importance=0.6111, present_in_paper=0
  word='process', importance=0.6098, present_in_paper=0
  word='paradigm', importance=0.6032, present_in_paper=1
  word='markets', importance=0.5925, present_in_paper=1
  word='financial', importance=0.5834, present_in_paper=1
  word='canonical', importance=0.5722, present_in_paper=1

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 1
Label distribution across all 1-hop neighbors (ground-truth class): Neural_Networks=100.0%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 2545 | edge_importance=0.8775 | class=Neural_Networks | Title: Volatility of Volatility of Financial Markets  
Abstract: We present empirical evidence for considering volatility of Eurodollar futures as a stochastic process, requiring a generalization of t

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 1795 | edge_importance=0.7843 | class=Neural_Networks | Title: Application of statistical mechanics methodol- ogy to term-structure bond-pricing models, Mathl. Comput. Modelling Application of
Abstract: The work in progress reported by Wright & Liley shows
  Node 2178 | edge_importance=0.3131 | class=Neural_Networks | Title: Statistical Mechanics of Nonlinear Nonequilibrium Financial Markets: Applications to Optimized Trading  
Abstract: A paradigm of statistical mechanics of financial markets (SMFM) using nonlinea
  Node 2082 | edge_importance=0.1981 | class=Genetic_Algorithms | Title: %A L. Ingber %T Adaptive simulated annealing (ASA): Lessons learned %J Control and Cybernetics Annealing
Abstract:  
  Node 1794 | edge_importance=0.1953 | class=Neural_Networks | Title: NONLINEAR NONEQUILIBRIUM NONQUANTUM NONCHAOTIC STATISTICAL MECHANICS OF NEOCORTICAL INTERACTIONS  
Abstract: The work in progress reported by Wright & Liley shows great promise, primarily becau

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

- ID: 1773
- Title: Canonical Momenta Indicators of Financial Markets and Neocortical EEG
- True class (canonical `y`): **Neural_Networks**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Neural_Networks**
- Prediction recorded by this method's pipeline: **Neural_Networks**

Canonical text (`raw_text`):

~~~~~~text
Title: Canonical Momenta Indicators of Financial Markets and Neocortical EEG  
Abstract: A paradigm of statistical mechanics of financial markets (SMFM) is fit to multivariate financial markets using Adaptive Simulated Annealing (ASA), a global optimization algorithm, to perform maximum likelihood fits of Lagrangians defined by path integrals of multivariate conditional probabilities. Canonical momenta are thereby derived and used as technical indicators in a recursive ASA optimization process to tune trading rules. These trading rules are then used on out-of-sample data, to demonstrate that they can profit from the SMFM model, to illustrate that these markets are likely not efficient. This methodology can be extended to other systems, e.g., electroencephalography. This approach to complex systems emphasizes the utility of blending an intuitive and powerful mathematical-physics formalism to generate indicators which are used by AI-type rule-based models of management. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 2545 | Neural_Networks | Volatility of Volatility of Financial Markets |

### 2-hop (shortest distance exactly 2): 4 nodes

| node id | true class | title |
|---|---|---|
| 1794 | Neural_Networks | NONLINEAR NONEQUILIBRIUM NONQUANTUM NONCHAOTIC STATISTICAL MECHANICS OF NEOCORTICAL INTERACTIONS |
| 1795 | Neural_Networks | Application of statistical mechanics methodol- ogy to term-structure bond-pricing models, Mathl. Comput. Modelling Application of |
| 2082 | Genetic_Algorithms | %A L. Ingber %T Adaptive simulated annealing (ASA): Lessons learned %J Control and Cybernetics Annealing |
| 2178 | Neural_Networks | Statistical Mechanics of Nonlinear Nonequilibrium Financial Markets: Applications to Optimized Trading |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=1773).
Recorded prediction: `{"Target Node": 1773, "Predicted Class": "Neural_Networks", "Confidence": 0.9925}`
Recorded graph stats: `{"total_1hop_degree": 1, "neighbor_label_ratio": {"Neural_Networks": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | mechanics | 0.6194 | 1 |
| 2 | model | 0.6111 | 0 |
| 3 | process | 0.6098 | 0 |
| 4 | paradigm | 0.6032 | 1 |
| 5 | markets | 0.5925 | 1 |
| 6 | financial | 0.5834 | 1 |
| 7 | canonical | 0.5722 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
