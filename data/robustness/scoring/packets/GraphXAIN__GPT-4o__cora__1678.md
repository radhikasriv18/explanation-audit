# Reference packet: GraphXAIN__GPT-4o__cora__1678

- Method: GraphXAIN; configuration: GPT-4o; dataset: cora; target node: 1678
- Explanation source: `./robustness_2026-10-30/graphxain_gpt4o/cora/1678.json` (narrative)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model predicted the class "Theory" for the target paper with high confidence (0.9999). The presence of the words "trees," "researchers," "worst," and "induction" in the paper's text, combined with their significant importance, strongly aligns with the characteristics of theoretical research, often associated with formal analysis and inductive methodologies. Though some highly influential words like "target," "conjunct," and "boolean" are absent, their relevance suggests a theoretical context is considered. Furthermore, the paper's direct citation network, dominated by works such as "An Analysis of Bayesian Classifiers" and "In Defense of C4.5," all belonging to the Theory class, reinforces the paper's positioning within theoretical discourse, emphasizing analytical and methodological discussions. This pattern is supported by the predominance of Theory-class papers among its 2-hop citation neighbors, such as "Induction of Oblique Decision Trees," which further suggests a shared thematic focus on decision tree methodologies and theoretical analysis. The combined impact of these features and connections suggests a strong inclination towards a theoretical framework, underlining the prediction's rationale.
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

### Target Paper (node 1678):
Title: Induction of One-Level Decision Trees  
Abstract: In recent years, researchers have made considerable progress on the worst-case analysis of inductive learning tasks, but for theoretical results to have impact on practice, they must deal with the average case. In this paper we present an aver

### Model Prediction:
{
  "Target Node": 1678,
  "Predicted Class": "Theory",
  "Confidence": 0.9999
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='target', importance=0.6654, present_in_paper=0
  word='trees', importance=0.6543, present_in_paper=1
  word='researchers', importance=0.6542, present_in_paper=1
  word='conjunct', importance=0.6322, present_in_paper=0
  word='worst', importance=0.6292, present_in_paper=1
  word='induction', importance=0.6274, present_in_paper=1
  word='boolean', importance=0.6258, present_in_paper=0

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 4
Label distribution across all 1-hop neighbors (ground-truth class): Theory=75.0%, Case_Based=25.0%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 1339 | edge_importance=0.8183 | class=Theory | Title: An Analysis of Bayesian Classifiers (1988), involves the formulation of average-case models for specific algorithms
Abstract: In this paper we present an average-case analysis of the Bayesian c
  Node 861 | edge_importance=0.7685 | class=Theory | Title: In Defense of C4.5: Notes on Learning One-Level Decision Trees  
Abstract: We discuss the implications of Holte's recently-published article, which demonstrated that on the most commonly used d
  Node 378 | edge_importance=0.6214 | class=Theory | Title: Mingers, 1989 J. Mingers. An empirical comparison of pruning methods for decision tree induction. Machine
Abstract: Ourston and Mooney, 1990b ] D. Ourston and R. J. Mooney. Improving shared rul
  Node 1570 | edge_importance=0.586 | class=Case_Based | Title: Average-Case Analysis of a Nearest Neighbor Algorithm  
Abstract: In this paper we present an average-case analysis of the nearest neighbor algorithm, a simple induction method that has been st

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 1027 | edge_importance=0.8399 | class=Theory | Title: Pessimistic decision tree pruning based on tree size  
Abstract: In this work we develop a new criteria to perform pessimistic decision tree pruning. Our method is theoretically sound and is ba
  Node 2042 | edge_importance=0.8275 | class=Neural_Networks | Title: Fast Bounded Smooth Regression with Lazy Neural Trees  
Abstract: We propose the lazy neural tree (LNT) as the appropriate architecture for the realization of smooth regression systems. The LNT
  Node 227 | edge_importance=0.822 | class=Theory | Title: Induction of Oblique Decision Trees  
Abstract: This paper introduces a randomized technique for partitioning examples using oblique hyperplanes. Standard decision tree techniques, such as ID3 
  Node 1431 | edge_importance=0.8121 | class=Neural_Networks | Title: Learning to Represent Codons: A Challenge Problem for Constructive Induction  
Abstract: The ability of an inductive learning system to find a good solution to a given problem is dependent upon
  Node 1236 | edge_importance=0.5707 | class=Theory | Title: Exploring the Decision Forest: An Empirical Investigation of Occam's Razor in Decision Tree Induction  
Abstract: We report on a series of experiments in which all decision trees consistent wit
  Node 2290 | edge_importance=0.2516 | class=Rule_Learning | Title: A Comparison of Pruning Methods for Relational Concept Learning  
Abstract: Pre-Pruning and Post-Pruning are two standard methods of dealing with noise in concept learning. Pre-Pruning methods 
  Node 1539 | edge_importance=0.2457 | class=Rule_Learning | Title: Finding new rules for incomplete theories: Explicit biases for induction with contextual information. In Proceedings
Abstract: addressed in KBANN (which translates a theory into a neural-net, r
  Node 1290 | edge_importance=0.2422 | class=Theory | Title: A THEORY OF LEARNING CLASSIFICATION RULES  
Abstract: This chapter takes a different standpoint to address the problem of learning. We will here reason only in terms of probability, and make ex
  Node 1238 | edge_importance=0.2387 | class=Theory | Title: On Pruning and Averaging Decision Trees  
Abstract: Pruning a decision tree is considered by some researchers to be the most important part of tree building in noisy domains. While, there are m
  Node 286 | edge_importance=0.2376 | class=Rule_Learning | Title: The Estimation of Probabilities in Attribute Selection Measures for Decision Tree Induction  
Abstract: In this paper we analyze two well-known measures for attribute selection in decision tree

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

- ID: 1678
- Title: Induction of One-Level Decision Trees
- True class (canonical `y`): **Theory**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Theory**
- Prediction recorded by this method's pipeline: **Theory**

Canonical text (`raw_text`):

~~~~~~text
Title: Induction of One-Level Decision Trees  
Abstract: In recent years, researchers have made considerable progress on the worst-case analysis of inductive learning tasks, but for theoretical results to have impact on practice, they must deal with the average case. In this paper we present an average-case analysis of a simple algorithm that induces one-level decision trees for concepts defined by a single relevant attribute. Given knowledge about the number of training instances, the number of irrelevant attributes, the amount of class and attribute noise, and the class and attribute distributions, we derive the expected classification accuracy over the entire instance space. We then examine the predictions of this analysis for different settings of these domain parameters, comparing them to exper imental results to check our reasoning. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 4 nodes

| node id | true class | title |
|---|---|---|
| 378 | Theory | Mingers, 1989 J. Mingers. An empirical comparison of pruning methods for decision tree induction. Machine |
| 861 | Theory | In Defense of C4.5: Notes on Learning One-Level Decision Trees |
| 1339 | Theory | An Analysis of Bayesian Classifiers (1988), involves the formulation of average-case models for specific algorithms |
| 1570 | Case_Based | Average-Case Analysis of a Nearest Neighbor Algorithm |

### 2-hop (shortest distance exactly 2): 35 nodes

| node id | true class | title |
|---|---|---|
| 178 | Rule_Learning | Learning Decision Trees from Decision Rules: |
| 218 | Probabilistic_Methods | Learning Classification Trees |
| 227 | Theory | Induction of Oblique Decision Trees |
| 286 | Rule_Learning | The Estimation of Probabilities in Attribute Selection Measures for Decision Tree Induction |
| 335 | Rule_Learning | Incremental Reduced Error Pruning |
| 396 | Rule_Learning | Geometric Comparison of Classifications and Rule Sets* |
| 434 | Case_Based | Computational Learning in Humans and Machines |
| 585 | Rule_Learning | An investigation of noise-tolerant relational concept learning algorithms |
| 634 | Case_Based | Oblivious Decision Trees and Abstract Cases |
| 692 | Theory | Decision Tree Induction: How Effective is the Greedy Heuristic? |
| 960 | Rule_Learning | Proceedings of the First International Workshop on Intelligent Adaptive Systems (IAS-95) Constructive Induction-based Learning Agents: |
| 1027 | Theory | Pessimistic decision tree pruning based on tree size |
| 1061 | Rule_Learning | Stochastic search in inductive concept learning |
| 1109 | Theory | Inductive Bias in Case-Based Reasoning Systems |
| 1111 | Case_Based | Towards a Better Understanding of Memory-Based Reasoning Systems |
| 1164 | Theory | PAC Analyses of a `Similarity Learning' IBL Algorithm |
| 1207 | Genetic_Algorithms | Data Analyses Using Simulated Breeding and Inductive Learning Methods |
| 1236 | Theory | Exploring the Decision Forest: An Empirical Investigation of Occam's Razor in Decision Tree Induction |
| 1238 | Theory | On Pruning and Averaging Decision Trees |
| 1275 | Rule_Learning | Fossil: A Robust Relational Learner |
| 1290 | Theory | A THEORY OF LEARNING CLASSIFICATION RULES |
| 1335 | Probabilistic_Methods | A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection |
| 1431 | Neural_Networks | Learning to Represent Codons: A Challenge Problem for Constructive Induction |
| 1539 | Rule_Learning | Finding new rules for incomplete theories: Explicit biases for induction with contextual information. In Proceedings |
| 1644 | Neural_Networks | A Comparative Study of ID3 and Backpropagation for English Text-to-Speech Mapping |
| 1963 | Rule_Learning | Learning Problem-Oriented Decision Structures from Decision Rules: The AQDT-2 System |
| 2012 | Theory | Multivariate Decision Trees |
| 2042 | Neural_Networks | Fast Bounded Smooth Regression with Lazy Neural Trees |
| 2195 | Rule_Learning | LEARNING FOR DECISION MAKING: The FRD Approach and a Comparative Study  Machine Learning and Inference Laboratory |
| 2290 | Rule_Learning | A Comparison of Pruning Methods for Relational Concept Learning |
| 2291 | Rule_Learning | Top-Down Pruning in Relational Learning |
| 2443 | Probabilistic_Methods | Issues in the Integration of Data Mining and Data Visualization Visualizing the Simple Bayesian Classifier |
| 2447 | Case_Based | New Roles for Machine Learning in Design for Design of Educational Computing New roles for |
| 2583 | Theory | Dynamic Automatic Model Selection |
| 2677 | Probabilistic_Methods | Mining and Model Simplicity: A Case Study in Diagnosis |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=1678).
Recorded prediction: `{"Target Node": 1678, "Predicted Class": "Theory", "Confidence": 0.9999}`
Recorded graph stats: `{"total_1hop_degree": 4, "neighbor_label_ratio": {"Theory": 0.75, "Case_Based": 0.25}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | target | 0.6654 | 0 |
| 2 | trees | 0.6543 | 1 |
| 3 | researchers | 0.6542 | 1 |
| 4 | conjunct | 0.6322 | 0 |
| 5 | worst | 0.6292 | 1 |
| 6 | induction | 0.6274 | 1 |
| 7 | boolean | 0.6258 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
