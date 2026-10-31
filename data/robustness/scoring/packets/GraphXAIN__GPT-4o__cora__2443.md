# Reference packet: GraphXAIN__GPT-4o__cora__2443

- Method: GraphXAIN; configuration: GPT-4o; dataset: cora; target node: 2443
- Explanation source: `./robustness_2026-10-30/graphxain_gpt4o/cora/2443.json` (narrative)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model predicted that the target paper would be classified under the "Theory" category with a confidence level of 56.11%. Among the most significant words influencing this prediction, "model" was present in the paper and aligns with theoretical discussions, while the absence of words like "exhibit" and "method" suggests a more theoretical than applied focus. The direct citation neighbor most strongly influencing the prediction was a Theory paper on Bayesian classifiers, which likely reinforced the target paper's theoretical connections due to its related topic. Another influential neighbor discussed feature selection and was classified under Probabilistic Methods, further supporting a conceptual orientation. In the 2-hop neighborhood, papers such as those discussing irrelevant features in Theory add layers of conceptual context that align with the predicted category. The cumulative effect of these connections and features suggests the paper is engaged in theoretical discourse, which is characteristic of works dealing with conceptual models and analytical methods.
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

### Target Paper (node 2443):
Title: Issues in the Integration of Data Mining and Data Visualization Visualizing the Simple Bayesian Classifier  
Abstract: The simple Bayesian classifier (SBC), sometimes called Naive-Bayes, is built based on a conditional independence model of each attribute given the class. The model was previo

### Model Prediction:
{
  "Target Node": 2443,
  "Predicted Class": "Theory",
  "Confidence": 0.5611
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='exhibit', importance=0.6965, present_in_paper=0
  word='model', importance=0.691, present_in_paper=1
  word='conjunct', importance=0.6884, present_in_paper=0
  word='mani', importance=0.6854, present_in_paper=0
  word='good', importance=0.6846, present_in_paper=0
  word='genet', importance=0.6738, present_in_paper=0
  word='method', importance=0.6695, present_in_paper=0

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 3
Label distribution across all 1-hop neighbors (ground-truth class): Theory=33.3%, Case_Based=33.3%, Probabilistic_Methods=33.3%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 2343 | edge_importance=0.814 | class=Probabilistic_Methods | Title: Feature Subset Selection Using the Wrapper Method: Overfitting and Dynamic Search Space Topology  
Abstract: In the wrapper approach to feature subset selection, a search for an optimal set of 
  Node 1339 | edge_importance=0.7156 | class=Theory | Title: An Analysis of Bayesian Classifiers (1988), involves the formulation of average-case models for specific algorithms
Abstract: In this paper we present an average-case analysis of the Bayesian c
  Node 2338 | edge_importance=0.3277 | class=Case_Based | Title: Beyond Independence: Conditions for the Optimality of the Simple Bayesian Classifier  
Abstract: The simple Bayesian classifier (SBC) is commonly thought to assume that attributes are independe

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 2677 | edge_importance=0.8452 | class=Probabilistic_Methods | Title: Mining and Model Simplicity: A Case Study in Diagnosis  
Abstract: Proceedings of the 2nd International Conference on Knowledge Discovery and Data Mining (KDD), 1996. The official version of th
  Node 434 | edge_importance=0.8317 | class=Case_Based | Title: Computational Learning in Humans and Machines  
Abstract: In this paper we review research on machine learning and its relation to computational models of human learning. We focus initially on 
  Node 430 | edge_importance=0.7848 | class=Theory | Title: Irrelevant Features and the Subset Selection Problem  
Abstract: We address the problem of finding a subset of features that allows a supervised induction algorithm to induce small high-accurac
  Node 1337 | edge_importance=0.7773 | class=Theory | Title: MLC A Machine Learning Library in C  
Abstract: We present MLC ++ , a library of C ++ classes and tools for supervised Machine Learning. While MLC ++ provides general learning algorithms that c
  Node 1678 | edge_importance=0.7608 | class=Theory | Title: Induction of One-Level Decision Trees  
Abstract: In recent years, researchers have made considerable progress on the worst-case analysis of inductive learning tasks, but for theoretical result
  Node 1570 | edge_importance=0.7546 | class=Case_Based | Title: Average-Case Analysis of a Nearest Neighbor Algorithm  
Abstract: In this paper we present an average-case analysis of the nearest neighbor algorithm, a simple induction method that has been st
  Node 1335 | edge_importance=0.7038 | class=Probabilistic_Methods | Title: A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection  
Abstract: We review accuracy estimation methods and compare the two most common methods: cross-validation
  Node 1024 | edge_importance=0.2992 | class=Theory | Title: On learning hierarchical classifications  
Abstract: Many significant real-world classification tasks involve a large number of categories which are arranged in a hierarchical structure; for ex
  Node 1111 | edge_importance=0.2772 | class=Case_Based | Title: Towards a Better Understanding of Memory-Based Reasoning Systems  
Abstract: We quantify both experimentally and analytically the performance of memory-based reasoning (MBR) algorithms. To star
  Node 1478 | edge_importance=0.2474 | class=Probabilistic_Methods | Title: Lazy Bayesian Trees  
Abstract: The naive Bayesian classifier is simple and effective, but its attribute independence assumption is often violated in the real world. A number of approaches have

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

- ID: 2443
- Title: Issues in the Integration of Data Mining and Data Visualization Visualizing the Simple Bayesian Classifier
- True class (canonical `y`): **Probabilistic_Methods**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Theory**
- Prediction recorded by this method's pipeline: **Theory**

Canonical text (`raw_text`):

~~~~~~text
Title: Issues in the Integration of Data Mining and Data Visualization Visualizing the Simple Bayesian Classifier  
Abstract: The simple Bayesian classifier (SBC), sometimes called Naive-Bayes, is built based on a conditional independence model of each attribute given the class. The model was previously shown to be surprisingly robust to obvious violations of this independence assumption, yielding accurate classification models even when there are clear conditional dependencies. The SBC can serve as an excellent tool for initial exploratory data analysis when coupled with a visualizer that makes its structure comprehensible. We describe such a visual representation of the SBC model that has been successfully implemented. We describe the requirements we had for such a visualization and the design decisions we made to satisfy them. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 3 nodes

| node id | true class | title |
|---|---|---|
| 1339 | Theory | An Analysis of Bayesian Classifiers (1988), involves the formulation of average-case models for specific algorithms |
| 2338 | Case_Based | Beyond Independence: Conditions for the Optimality of the Simple Bayesian Classifier |
| 2343 | Probabilistic_Methods | Feature Subset Selection Using the Wrapper Method: Overfitting and Dynamic Search Space Topology |

### 2-hop (shortest distance exactly 2): 14 nodes

| node id | true class | title |
|---|---|---|
| 208 | Theory | Feature Subset Selection as Search with Probabilistic Estimates |
| 430 | Theory | Irrelevant Features and the Subset Selection Problem |
| 434 | Case_Based | Computational Learning in Humans and Machines |
| 1024 | Theory | On learning hierarchical classifications |
| 1111 | Case_Based | Towards a Better Understanding of Memory-Based Reasoning Systems |
| 1335 | Probabilistic_Methods | A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection |
| 1337 | Theory | MLC A Machine Learning Library in C |
| 1478 | Probabilistic_Methods | Lazy Bayesian Trees |
| 1570 | Case_Based | Average-Case Analysis of a Nearest Neighbor Algorithm |
| 1618 | Theory | Selection of Relevant Features and Examples in Machine Learning |
| 1678 | Theory | Induction of One-Level Decision Trees |
| 1986 | Theory | BOOSTING AND NAIVE BAYESIAN LEARNING |
| 2127 | Probabilistic_Methods | NAIVE BAYESIAN LEARNING  Adapted from |
| 2677 | Probabilistic_Methods | Mining and Model Simplicity: A Case Study in Diagnosis |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=2443).
Recorded prediction: `{"Target Node": 2443, "Predicted Class": "Theory", "Confidence": 0.5611}`
Recorded graph stats: `{"total_1hop_degree": 3, "neighbor_label_ratio": {"Theory": 0.333, "Case_Based": 0.333, "Probabilistic_Methods": 0.333}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | exhibit | 0.6965 | 0 |
| 2 | model | 0.691 | 1 |
| 3 | conjunct | 0.6884 | 0 |
| 4 | mani | 0.6854 | 0 |
| 5 | good | 0.6846 | 0 |
| 6 | genet | 0.6738 | 0 |
| 7 | method | 0.6695 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
