# Reference packet: GraphXAIN__Llama-8B__cora__487

- Method: GraphXAIN; configuration: Llama-8B; dataset: cora; target node: 487
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/cora/graphxain_cora_llama_2hop_narratives_full.json` ([487])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on our model, we predict that the target paper, "Language as a dynamical system," belongs to the category of Neural_Networks with a confidence level of 99%. This prediction is largely influenced by the paper's Bag-of-Words (BOW) features, where terms like 'network,' 'neural,' and'model' appear among the top seven most important words. While none of these terms explicitly mention Neural_Networks in the paper itself, they strongly associate with the topic, making a strong contribution to the prediction. Moreover, two direct citation neighbors, including one labeled as "Learning and evolution in neural networks" and another titled "Back Propagation is Sensitive to Initial Conditions," both classified under Neural_Networks, solidify this connection. These references confirm that the paper heavily relies on and extends concepts related to Neural Networks. Furthermore, although 2-hop neighbors offer a mix of diverse topics, including some related to Genetic Algorithms, they do not sufficiently challenge the dominant pattern established by the paper's BOW features and direct citations. Overall, the convergence of influential BOW features and direct citations strongly supports the prediction of Neural_Networks for this paper.
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

### Target Paper (node 487):
Title: Language as a dynamical system  
Abstract: Designers across a variety of domains engage in many of the same creative activities. Since much creativity stems from using old solutions in novel ways, we believe that case-based reasoning can be used to explain many creative design processes. 

### Model Prediction:
{
  "Target Node": 487,
  "Predicted Class": "Neural_Networks",
  "Confidence": 0.9907
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='network', importance=0.7066, present_in_paper=0
  word='neural', importance=0.6705, present_in_paper=0
  word='model', importance=0.6688, present_in_paper=0
  word='real', importance=0.6668, present_in_paper=0
  word='system', importance=0.6643, present_in_paper=1
  word='time', importance=0.6636, present_in_paper=0
  word='weight', importance=0.6573, present_in_paper=0

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 2
Label distribution across all 1-hop neighbors (ground-truth class): Neural_Networks=50.0%, Genetic_Algorithms=50.0%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 538 | edge_importance=0.8316 | class=Genetic_Algorithms | Title: Learning and evolution in neural networks  
Abstract: DIMACS Technical Report 96-56 December 1996 
  Node 291 | edge_importance=0.7554 | class=Neural_Networks | Title: NETWORKS WITH REAL WEIGHTS: ANALOG COMPUTATIONAL COMPLEXITY In contrast to classical computational models, the models
Abstract: Report SYCON-92-05 ABSTRACT We pursue a particular approach to an

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 1738 | edge_importance=0.8231 | class=Genetic_Algorithms | Title: Evolving nonTrivial Behaviors on Real Robots: an Autonomous Robot that Picks up Objects  
Abstract: Recently, a new approach that involves a form of simulated evolution has been proposed for th
  Node 2193 | edge_importance=0.7995 | class=Genetic_Algorithms | Title: Growing neural networks  
Abstract: Selecting a set of features which is optimal for a given task is a problem which plays an important role in a wide variety of contexts including pattern reco
  Node 402 | edge_importance=0.2347 | class=Genetic_Algorithms | Title: The Evolutionary Cost of Learning  
Abstract: Traits that are acquired by members of an evolving population during their lifetime, through adaptive processes such as learning, can become geneti
  Node 1689 | edge_importance=0.2224 | class=Genetic_Algorithms | Title: Selection for Wandering Behavior in a Small Robot  
Abstract: We have evolved artificial neural networks to control the wandering behavior of small robots. The task was to touch as many squares
  Node 129 | edge_importance=0.2165 | class=Genetic_Algorithms | Title: Evolving Networks: Using the Genetic Algorithm with Connectionist Learning  
Abstract: A pilot study is described on the practical application of artificial neural networks. The limit cycle of 
  Node 2309 | edge_importance=0.2156 | class=Reinforcement_Learning | Title: EVOLVING SENSORS IN ENVIRONMENTS OF CONTROLLED COMPLEXITY  
Abstract: 1 . Sensors represent a crucial link between the evolutionary forces shaping a species' relationship with its environment, 
  Node 1204 | edge_importance=0.1988 | class=Genetic_Algorithms | Title: The Role of Development in Genetic Algorithms  
Abstract: Technical Report Number CS94-394 Computer Science and Engineering, U.C.S.D. Abstract The developmental mechanisms transforming genotypi
  Node 15 | edge_importance=0.1838 | class=Neural_Networks | Title: Back Propagation is Sensitive to Initial Conditions  
Abstract: This paper explores the effect of initial weight selection on feed-forward networks learning simple functions with the back-propa
  Node 2165 | edge_importance=0.1687 | class=Genetic_Algorithms | Title: Auto-teaching: networks that develop their own teaching input  
Abstract: Backpropagation learning (Rumelhart, Hinton and Williams, 1986) is a useful research tool but it has a number of undesi
  Node 1036 | edge_importance=0.1471 | class=Genetic_Algorithms | Title: Adaptive Behavior in Competing Co-Evolving Species  
Abstract: Co-evolution of competitive species provides an interesting testbed to study the role of adaptive behavior because it provides unp

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

- ID: 487
- Title: Language as a dynamical system
- True class (canonical `y`): **Neural_Networks**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Neural_Networks**
- Prediction recorded by this method's pipeline: **Neural_Networks**

Canonical text (`raw_text`):

~~~~~~text
Title: Language as a dynamical system  
Abstract: Designers across a variety of domains engage in many of the same creative activities. Since much creativity stems from using old solutions in novel ways, we believe that case-based reasoning can be used to explain many creative design processes. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 2 nodes

| node id | true class | title |
|---|---|---|
| 291 | Neural_Networks | NETWORKS WITH REAL WEIGHTS: ANALOG COMPUTATIONAL COMPLEXITY In contrast to classical computational models, the models |
| 538 | Genetic_Algorithms | Learning and evolution in neural networks |

### 2-hop (shortest distance exactly 2): 10 nodes

| node id | true class | title |
|---|---|---|
| 15 | Neural_Networks | Back Propagation is Sensitive to Initial Conditions |
| 129 | Genetic_Algorithms | Evolving Networks: Using the Genetic Algorithm with Connectionist Learning |
| 402 | Genetic_Algorithms | The Evolutionary Cost of Learning |
| 1036 | Genetic_Algorithms | Adaptive Behavior in Competing Co-Evolving Species |
| 1204 | Genetic_Algorithms | The Role of Development in Genetic Algorithms |
| 1689 | Genetic_Algorithms | Selection for Wandering Behavior in a Small Robot |
| 1738 | Genetic_Algorithms | Evolving nonTrivial Behaviors on Real Robots: an Autonomous Robot that Picks up Objects |
| 2165 | Genetic_Algorithms | Auto-teaching: networks that develop their own teaching input |
| 2193 | Genetic_Algorithms | Growing neural networks |
| 2309 | Reinforcement_Learning | EVOLVING SENSORS IN ENVIRONMENTS OF CONTROLLED COMPLEXITY |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=487).
Recorded prediction: `{"Target Node": 487, "Predicted Class": "Neural_Networks", "Confidence": 0.9907}`
Recorded graph stats: `{"total_1hop_degree": 2, "neighbor_label_ratio": {"Neural_Networks": 0.5, "Genetic_Algorithms": 0.5}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | network | 0.7066 | 0 |
| 2 | neural | 0.6705 | 0 |
| 3 | model | 0.6688 | 0 |
| 4 | real | 0.6668 | 0 |
| 5 | system | 0.6643 | 1 |
| 6 | time | 0.6636 | 0 |
| 7 | weight | 0.6573 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
