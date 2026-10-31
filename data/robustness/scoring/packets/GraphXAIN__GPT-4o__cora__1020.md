# Reference packet: GraphXAIN__GPT-4o__cora__1020

- Method: GraphXAIN; configuration: GPT-4o; dataset: cora; target node: 1020
- Explanation source: `./robustness_2026-10-30/graphxain_gpt4o/cora/1020.json` (narrative)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The GNN model predicted that the target paper, "Error-Based and Entropy-Based Discretization of Continuous Features," falls into the "Probabilistic_Methods" category with a confidence level of 69.12%. Among the top bag-of-words features influencing this prediction, the word 'decision' is the only one present in the paper and has a notable impact, while other important words like 'result', 'commonli', 'work', 'unsupervis', 'user', and 'flexibl' are absent, yet still significant in shaping the prediction. The paper's direct citation network includes influential works like "Targeting Business Users with Decision Table Classifiers," which aligns with the "Probabilistic_Methods" class, and several others classified under "Theory", indicating a methodological overlap that could support the predicted class. Additionally, the indirect citation network includes papers such as "Bayesian Network Classification with Continuous Attributes," which is strongly related to probabilistic methods and further underscores the model's prediction. The presence of decision tables and Bayesian classification themes in both the local and broader citation context helps push the prediction toward probabilistic methods, illustrating a consistent thematic pattern associated with this research area. This layered interplay of influential words and citation links ultimately guides the model to associate the target paper with probabilistic approaches.
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

### Target Paper (node 1020):
Title: Error-Based and Entropy-Based Discretization of Continuous Features  
Abstract: We present a comparison of error-based and entropy-based methods for discretization of continuous features. Our study includes both an extensive empirical comparison as well as an analysis of scenarios where error

### Model Prediction:
{
  "Target Node": 1020,
  "Predicted Class": "Probabilistic_Methods",
  "Confidence": 0.6912
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='result', importance=0.6599, present_in_paper=0
  word='commonli', importance=0.6449, present_in_paper=0
  word='work', importance=0.643, present_in_paper=0
  word='unsupervis', importance=0.6428, present_in_paper=0
  word='user', importance=0.6388, present_in_paper=0
  word='flexibl', importance=0.638, present_in_paper=0
  word='decision', importance=0.6379, present_in_paper=1

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 6
Label distribution across all 1-hop neighbors (ground-truth class): Theory=66.7%, Neural_Networks=16.7%, Probabilistic_Methods=16.7%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 1337 | edge_importance=0.8011 | class=Theory | Title: MLC A Machine Learning Library in C  
Abstract: We present MLC ++ , a library of C ++ classes and tools for supervised Machine Learning. While MLC ++ provides general learning algorithms that c
  Node 1329 | edge_importance=0.7803 | class=Theory | Title: Supervised and Unsupervised Discretization of Continuous Features  
Abstract: Many supervised machine learning algorithms require a discrete feature space. In this paper, we review previous wor
  Node 2577 | edge_importance=0.656 | class=Probabilistic_Methods | Title: Targeting Business Users with Decision Table Classifiers  
Abstract: Business users and analysts commonly use spreadsheets and 2D plots to analyze and understand their data. On-line Analytical 
  Node 1322 | edge_importance=0.4453 | class=Theory | Title: Theory and Applications of Agnostic PAC-Learning with Small Decision Trees  
Abstract: We exhibit a theoretically founded algorithm T2 for agnostic PAC-learning of decision trees of at most 2 l
  Node 430 | edge_importance=0.4401 | class=Theory | Title: Irrelevant Features and the Subset Selection Problem  
Abstract: We address the problem of finding a subset of features that allows a supervised induction algorithm to induce small high-accurac
  Node 1328 | edge_importance=0.3869 | class=Neural_Networks | Title: A Weighted Nearest Neighbor Algorithm for Learning with Symbolic Features  
Abstract: In the past, nearest neighbor algorithms for learning from examples have worked best in domains in which al

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 944 | edge_importance=0.7926 | class=Probabilistic_Methods | Title: Bayesian Network Classification with Continuous Attributes: Getting the Best of Both Discretization and Parametric Fitting  
Abstract: In a recent paper, Friedman, Geiger, and Goldszmidt [8] in
  Node 1049 | edge_importance=0.7905 | class=Rule_Learning | Title: Machine Learning and Inference  
Abstract: Constructive induction divides the problem of learning an inductive hypothesis into two intertwined searches: onefor the best representation space, an
  Node 2127 | edge_importance=0.7836 | class=Probabilistic_Methods | Title: NAIVE BAYESIAN LEARNING  Adapted from  
Abstract: We present a novel application of ILP to the problem of diterpene structure elucidation from 13 C NMR spectra. Diterpenes are organic compounds
  Node 1986 | edge_importance=0.7471 | class=Theory | Title: BOOSTING AND NAIVE BAYESIAN LEARNING  
Abstract: Although so-called naive Bayesian classification makes the unrealistic assumption that the values of the attributes of an example are independen
  Node 2367 | edge_importance=0.6826 | class=Theory | Title: Data Mining using MLC A Machine Learning Library in C http://www.sgi.com/Technology/mlc  
Abstract: Data mining algorithms including machine learning, statistical analysis, and pattern recognit
  Node 1027 | edge_importance=0.6046 | class=Theory | Title: Pessimistic decision tree pruning based on tree size  
Abstract: In this work we develop a new criteria to perform pessimistic decision tree pruning. Our method is theoretically sound and is ba
  Node 2342 | edge_importance=0.4248 | class=Theory | Title: The Power of Decision Tables  
Abstract: We evaluate the power of decision tables as a hypothesis space for supervised learning algorithms. Decision tables are one of the simplest hypothesis sp
  Node 2180 | edge_importance=0.4171 | class=Theory | Title: Oblivious Decision Trees, Graphs, and Top-Down Pruning  
Abstract: We describe a supervised learning algorithm, EODG, that uses mutual information to build an oblivious decision tree. The tree 
  Node 1335 | edge_importance=0.3771 | class=Probabilistic_Methods | Title: A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection  
Abstract: We review accuracy estimation methods and compare the two most common methods: cross-validation
  Node 323 | edge_importance=0.3496 | class=Theory | Title: Learning Active Classifiers  
Abstract: Many classification algorithms are "passive", in that they assign a class-label to each instance based only on the description given, even if that descri

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

- ID: 1020
- Title: Error-Based and Entropy-Based Discretization of Continuous Features
- True class (canonical `y`): **Probabilistic_Methods**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Probabilistic_Methods**
- Prediction recorded by this method's pipeline: **Probabilistic_Methods**

Canonical text (`raw_text`):

~~~~~~text
Title: Error-Based and Entropy-Based Discretization of Continuous Features  
Abstract: We present a comparison of error-based and entropy-based methods for discretization of continuous features. Our study includes both an extensive empirical comparison as well as an analysis of scenarios where error minimization may be an inappropriate discretization criterion. We present a discretization method based on the C4.5 decision tree algorithm and compare it to an existing entropy-based discretization algorithm, which employs the Minimum Description Length Principle, and a recently proposed error-based technique. We evaluate these discretization methods with respect to C4.5 and Naive-Bayesian classifiers on datasets from the UCI repository and analyze the computational complexity of each method. Our results indicate that the entropy-based MDL heuristic outperforms error minimization on average. We then analyze the shortcomings of error-based approaches in comparison to entropy-based methods. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 6 nodes

| node id | true class | title |
|---|---|---|
| 430 | Theory | Irrelevant Features and the Subset Selection Problem |
| 1322 | Theory | Theory and Applications of Agnostic PAC-Learning with Small Decision Trees |
| 1328 | Neural_Networks | A Weighted Nearest Neighbor Algorithm for Learning with Symbolic Features |
| 1329 | Theory | Supervised and Unsupervised Discretization of Continuous Features |
| 1337 | Theory | MLC A Machine Learning Library in C |
| 2577 | Probabilistic_Methods | Targeting Business Users with Decision Table Classifiers |

### 2-hop (shortest distance exactly 2): 66 nodes

| node id | true class | title |
|---|---|---|
| 52 | Theory | Theory Revision in Fault Hierarchies |
| 89 | Theory | NP-Completeness of Searches for Smallest Possible Feature Sets a subset of the set of all |
| 119 | Rule_Learning | Cost-sensitive feature reduction applied to a hybrid genetic algorithm |
| 172 | Case_Based | Efficient Feature Selection in Conceptual Clustering |
| 177 | Theory | Evaluation and Selection of Biases in Machine Learning |
| 208 | Theory | Feature Subset Selection as Search with Probabilistic Estimates |
| 223 | Rule_Learning | Automated model selection |
| 236 | Case_Based | Machine Learning Methods for International Conflict Databases: A Case Study in Predicting Mediation Outcome |
| 256 | Case_Based | Using Decision Trees to Improve Case-Based Learning |
| 323 | Theory | Learning Active Classifiers |
| 381 | Theory | Compression-Based Feature Subset Selection  Keywords: Minimum Description Length Principle, Cross Validation, Noise |
| 524 | Neural_Networks | An Inductive Learning Approach to Prognostic Prediction |
| 547 | Neural_Networks | Expectation-Based Selective Attention for Visual Monitoring and Control of a Robot Vehicle |
| 632 | Probabilistic_Methods | Toward Optimal Feature Selection |
| 634 | Case_Based | Oblivious Decision Trees and Abstract Cases |
| 635 | Theory | Learning Boolean Concepts in the Presence of Many Irrelevant Features |
| 651 | Neural_Networks | A Monotonic Measure for Optimal Feature Selection |
| 683 | Case_Based | On the Greediness of Feature Selection Algorithms |
| 686 | Case_Based | Prototype and Feature Selection by Sampling and Random Mutation Hill Climbing Algorithms |
| 783 | Case_Based | Resolving PP attachment Ambiguities with Memory-Based Learning |
| 785 | Case_Based | RAPID DEVELOPMENT OF NLP MODULES WITH MEMORY-BASED LEARNING |
| 927 | Case_Based | Exemplar-based Music Structure Recognition |
| 944 | Probabilistic_Methods | Bayesian Network Classification with Continuous Attributes: Getting the Best of Both Discretization and Parametric Fitting |
| 947 | Case_Based | An Optimal Weighting Criterion of Case Indexing for Both Numeric and Symbolic Attributes |
| 1027 | Theory | Pessimistic decision tree pruning based on tree size |
| 1031 | Neural_Networks | Protein Secondary Structure Modelling with Probabilistic Networks (Extended Abstract) |
| 1049 | Rule_Learning | Machine Learning and Inference |
| 1071 | Rule_Learning | Machine Learning and Inference |
| 1101 | Case_Based | On Reasoning from Data |
| 1107 | Case_Based | The Possible Contribution of AI to the Avoidance of Crises and Wars: Using CBR Methods |
| 1109 | Theory | Inductive Bias in Case-Based Reasoning Systems |
| 1111 | Case_Based | Towards a Better Understanding of Memory-Based Reasoning Systems |
| 1155 | Case_Based | Memory-Based Lexical Acquisition and Processing |
| 1165 | Rule_Learning | Discovering Compressive Partial Determinations in Mixed Numerical and Symbolic Domains |
| 1173 | Theory | Dynamical Selection of Learning Algorithms |
| 1207 | Genetic_Algorithms | Data Analyses Using Simulated Breeding and Inductive Learning Methods |
| 1270 | Theory | Automatic Parameter Selection by Minimizing Estimated Error |
| 1284 | Neural_Networks | Feature Selection via Mathematical Programming |
| 1335 | Probabilistic_Methods | A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection |
| 1412 | Case_Based | EXPLORING A FRAMEWORK FOR INSTANCE BASED LEARNING AND NAIVE BAYESIAN CLASSIFIERS |
| 1423 | Neural_Networks | Comparison of Regression Methods, Symbolic Induction Methods and Neural Networks in Morbidity Diagnosis and Mortality |
| 1513 | Case_Based | Fast NP Chunking Using Memory-Based Learning Techniques |
| 1568 | Case_Based | The Utility of Feature Weighting in Nearest-Neighbor Algorithms |
| 1569 | Rule_Learning | Estimating Attributes: Analysis and Extensions of RELIEF |
| 1584 | Case_Based | Towards a Theory of Optimal Similarity Measures way of learning a similarity measure from the |
| 1617 | Case_Based | Knowledge Discovery in International Conflict Databases |
| 1622 | Rule_Learning | Stochastic Propositionalization of Non-Determinate Background Knowledge |
| 1637 | Neural_Networks | The Effective Size of a Neural Network: A Principal Component Approach |
| 1644 | Neural_Networks | A Comparative Study of ID3 and Backpropagation for English Text-to-Speech Mapping |
| 1698 | Case_Based | CBET: a Case Base Exploration Tool |
| 1792 | Theory | 21 Using n 2 classifier in constructive induction |
| 1986 | Theory | BOOSTING AND NAIVE BAYESIAN LEARNING |
| 2033 | Neural_Networks | Improving RBF Networks by the Feature Selection Approach EUBAFES |
| 2127 | Probabilistic_Methods | NAIVE BAYESIAN LEARNING  Adapted from |
| 2137 | Case_Based | Search-based Class Discretization |
| 2180 | Theory | Oblivious Decision Trees, Graphs, and Top-Down Pruning |
| 2197 | Theory | MLC Tutorial A Machine Learning library of C classes. |
| 2300 | Rule_Learning | Applying a Machine Learning Workbench: Experience with Agricultural Databases |
| 2342 | Theory | The Power of Decision Tables |
| 2343 | Probabilistic_Methods | Feature Subset Selection Using the Wrapper Method: Overfitting and Dynamic Search Space Topology |
| 2367 | Theory | Data Mining using MLC A Machine Learning Library in C http://www.sgi.com/Technology/mlc |
| 2487 | Theory | An Optimized Theory Revision Module |
| 2508 | Theory | WRAPPERS FOR PERFORMANCE ENHANCEMENT AND OBLIVIOUS DECISION GRAPHS |
| 2539 | Rule_Learning | Mining for Causes of Cancer: Machine Learning Experiments at Various Levels of Detail |
| 2557 | Neural_Networks | Growing Simpler Decision Trees to Facilitate Knowledge Discovery |
| 2593 | Case_Based | Induction of Condensed Determinations |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=1020).
Recorded prediction: `{"Target Node": 1020, "Predicted Class": "Probabilistic_Methods", "Confidence": 0.6912}`
Recorded graph stats: `{"total_1hop_degree": 6, "neighbor_label_ratio": {"Theory": 0.667, "Neural_Networks": 0.167, "Probabilistic_Methods": 0.167}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | result | 0.6599 | 0 |
| 2 | commonli | 0.6449 | 0 |
| 3 | work | 0.643 | 0 |
| 4 | unsupervis | 0.6428 | 0 |
| 5 | user | 0.6388 | 0 |
| 6 | flexibl | 0.638 | 0 |
| 7 | decision | 0.6379 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
