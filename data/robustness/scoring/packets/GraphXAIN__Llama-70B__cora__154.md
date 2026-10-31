# Reference packet: GraphXAIN__Llama-70B__cora__154

- Method: GraphXAIN; configuration: Llama-70B; dataset: cora; target node: 154
- Explanation source: `./robustness_2026-10-30/llama70b/graphxain/cora/154.json` (response)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model predicted that the research area of the target paper, "Data-driven Modeling and Synthesis of Acoustical Instruments," is Neural Networks with a confidence of 74.09%. Although none of the top important bag-of-words (BOW) features - coefficients, linear, result, supervisory - were present in the paper, their strong association with Neural Networks likely influenced the prediction. Conversely, the presence of analysis, space, and constructor in the paper reinforced this prediction, as they are also relevant to Neural Networks. However, the most influential direct citation neighbors strongly pointed towards Probabilistic Methods, particularly papers on cluster-weighted modeling for time series prediction and hierarchical mixtures of experts. Despite these conflicting signals, 2-hop neighbors, including papers on mixture of experts and neural networks for descriptive statistical analysis, tipped the balance towards Neural Networks, suggesting a broader context where neural networks were applied to various tasks, including some related to probabilistic methods. It appears that the model weighed the aggregate evidence from both local graph structure and content features to make its prediction.
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

### Target Paper (node 154):
Title: Data-driven Modeling and Synthesis of Acoustical Instruments  
Abstract: We present a framework for the analysis and synthesis of acoustical instruments based on data-driven probabilistic inference modeling. Audio time series and boundary conditions of a played instrument are recorded and the

### Model Prediction:
{
  "Target Node": 154,
  "Predicted Class": "Neural_Networks",
  "Confidence": 0.7409
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='coeffici', importance=0.6863, present_in_paper=0
  word='linear', importance=0.6687, present_in_paper=0
  word='result', importance=0.6683, present_in_paper=0
  word='supervis', importance=0.6467, present_in_paper=0
  word='analysis', importance=0.638, present_in_paper=1
  word='space', importance=0.6357, present_in_paper=1
  word='constructor', importance=0.6336, present_in_paper=1

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 2
Label distribution across all 1-hop neighbors (ground-truth class): Probabilistic_Methods=100.0%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 392 | edge_importance=0.6736 | class=Probabilistic_Methods | Title: DRAFT Cluster-Weighted Modeling for Time Series Prediction and Characterization  
Abstract:  
  Node 74 | edge_importance=0.5821 | class=Probabilistic_Methods | Title: Hierarchical Mixtures of Experts and the EM Algorithm  
Abstract: We present a tree-structured architecture for supervised learning. The statistical model underlying the architecture is a hiera

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 345 | edge_importance=0.8407 | class=Probabilistic_Methods | Title: On Convergence Properties of the EM Algorithm for Gaussian Mixtures  
Abstract: We build up the mathematical connection between the "Expectation-Maximization" (EM) algorithm and gradient-based 
  Node 871 | edge_importance=0.8353 | class=Probabilistic_Methods | Title: Factorial Learning and the EM Algorithm  
Abstract: Many real world learning problems are best characterized by an interaction of multiple independent causes or factors. Discovering such causal
  Node 71 | edge_importance=0.8319 | class=Probabilistic_Methods | Title: Supervised learning from incomplete data via an EM approach  
Abstract: Real-world learning tasks may involve high-dimensional data sets with arbitrary patterns of missing data. In this paper w
  Node 1017 | edge_importance=0.8217 | class=Neural_Networks | Title: Using Neural Networks for Descriptive Statistical Analysis of Educational Data  
Abstract: In this paper we discuss the methodological issues of using a class of neural networks called Mixture 
  Node 310 | edge_importance=0.8169 | class=Neural_Networks | Title: Forecasting electricity demand using nonlinear mixture of experts  
Abstract: In this paper we study a forecasting model based on mixture of experts for predicting the French electric daily con
  Node 661 | edge_importance=0.8161 | class=Probabilistic_Methods | Title: A Statistical Approach to Decision Tree Modeling  
Abstract: A statistical approach to decision tree modeling is described. In this approach, each decision in the tree is modeled parametrically
  Node 604 | edge_importance=0.8155 | class=Neural_Networks | Title: First experiments using a mixture of nonlinear experts for time series prediction  
Abstract: This paper investigates the advantages and disadvantages of the mixture of experts (ME) model (intr
  Node 252 | edge_importance=0.8155 | class=Reinforcement_Learning | Title: A Modular Q-Learning Architecture for Manipulator Task Decomposition `Data storage in the cerebellar model ar
Abstract: Compositional Q-Learning (CQ-L) (Singh 1992) is a modular approach to lea
  Node 881 | edge_importance=0.8138 | class=Neural_Networks | Title: Proben1 A Set of Neural Network Benchmark Problems and Benchmarking Rules  
Abstract: Proben1 is a collection of problems for neural network learning in the realm of pattern classification and 
  Node 377 | edge_importance=0.8063 | class=Neural_Networks | Title: Constructive Algorithms for Hierarchical Mixtures of Experts  
Abstract: We present two additions to the hierarchical mixture of experts (HME) architecture. We view the HME as a tree structured

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

- ID: 154
- Title: Data-driven Modeling and Synthesis of Acoustical Instruments
- True class (canonical `y`): **Neural_Networks**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Neural_Networks**
- Prediction recorded by this method's pipeline: **Neural_Networks**

Canonical text (`raw_text`):

~~~~~~text
Title: Data-driven Modeling and Synthesis of Acoustical Instruments  
Abstract: We present a framework for the analysis and synthesis of acoustical instruments based on data-driven probabilistic inference modeling. Audio time series and boundary conditions of a played instrument are recorded and the non-linear mapping from the control data into the audio space is inferred using the general inference framework of Cluster-Weighted Modeling. The resulting model is used for real-time synthesis of audio sequences from new input data.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 2 nodes

| node id | true class | title |
|---|---|---|
| 74 | Probabilistic_Methods | Hierarchical Mixtures of Experts and the EM Algorithm |
| 392 | Probabilistic_Methods | DRAFT Cluster-Weighted Modeling for Time Series Prediction and Characterization |

### 2-hop (shortest distance exactly 2): 40 nodes

| node id | true class | title |
|---|---|---|
| 19 | Neural_Networks | Validation of Average Error Rate Over Classifiers |
| 71 | Probabilistic_Methods | Supervised learning from incomplete data via an EM approach |
| 76 | Probabilistic_Methods | A VIEW OF THE EM ALGORITHM THAT JUSTIFIES INCREMENTAL, SPARSE, AND OTHER VARIANTS |
| 193 | Neural_Networks | Soft Classification, a.k.a. Risk Estimation, via Penalized Log Likelihood and Smoothing Spline Analysis of Variance |
| 252 | Reinforcement_Learning | A Modular Q-Learning Architecture for Manipulator Task Decomposition `Data storage in the cerebellar model ar |
| 263 | Neural_Networks | Non-linear Models for Time Series Using Mixtures of Experts |
| 310 | Neural_Networks | Forecasting electricity demand using nonlinear mixture of experts |
| 345 | Probabilistic_Methods | On Convergence Properties of the EM Algorithm for Gaussian Mixtures |
| 377 | Neural_Networks | Constructive Algorithms for Hierarchical Mixtures of Experts |
| 505 | Neural_Networks | From Isolation to Cooperation: An Alternative View of a System of Experts |
| 511 | Probabilistic_Methods | Learning from incomplete data |
| 547 | Neural_Networks | Expectation-Based Selective Attention for Visual Monitoring and Control of a Robot Vehicle |
| 604 | Neural_Networks | First experiments using a mixture of nonlinear experts for time series prediction |
| 622 | Neural_Networks | CLASSIFICATION USING HIERARCHICAL MIXTURES OF EXPERTS |
| 661 | Probabilistic_Methods | A Statistical Approach to Decision Tree Modeling |
| 680 | Neural_Networks | Cortical Mechanisms of Visual Recognition and Learning: A Hierarchical Kalman Filter Model |
| 787 | Probabilistic_Methods | Hidden Markov decision trees |
| 867 | Neural_Networks | Comparison of Neural and Statistical Classifiers\| Theory and Practice |
| 871 | Probabilistic_Methods | Factorial Learning and the EM Algorithm |
| 881 | Neural_Networks | Proben1 A Set of Neural Network Benchmark Problems and Benchmarking Rules |
| 906 | Neural_Networks | Memory-based Time Series Recognition  A New Methodology and Real World Applications |
| 949 | Neural_Networks | Classifying Seismic Signals by Integrating Ensembles of Neural Networks |
| 975 | Neural_Networks | State Reconstruction for Determining Predictability in Driven Nonlinear Acoustical Systems |
| 987 | Probabilistic_Methods | Stacked Density Estimation |
| 1017 | Neural_Networks | Using Neural Networks for Descriptive Statistical Analysis of Educational Data |
| 1024 | Theory | On learning hierarchical classifications |
| 1103 | Neural_Networks | Adaptive Computation Techniques for Time Series Analysis Major Professor: </title> <journal> Dr. Mehdi Zargham </journal> |
| 1220 | Neural_Networks | A Method of Combining Multiple Probabilistic Classifiers through Soft Competition on Different Feature Sets |
| 1634 | Neural_Networks | Combining Linear Discriminant Functions with Neural Networks for Supervised Learning |
| 1676 | Neural_Networks | TD Learning of Game Evaluation Functions with Hierarchical Neural Architectures |
| 1928 | Neural_Networks | Mixtures of Probabilistic Principal Component Analysers |
| 2013 | Neural_Networks | Using the Stochastic Gradient Method to Fit Polychotomous Regression Models |
| 2124 | Neural_Networks | A Hierarchical Latent Variable Model for Data Visualization |
| 2266 | Probabilistic_Methods | A Gentle Tutorial of the EM Algorithm and its Application to Parameter Estimation for Gaussian |
| 2284 | Neural_Networks | Performance of On-Line Learning Methods in Predicting Multiprocessor Memory Access Patterns |
| 2335 | Neural_Networks | Function Approximation with Neural Networks and Local Methods: Bias, Variance and Smoothness |
| 2390 | Neural_Networks | A HIERARCHICAL COMMUNITY OF EXPERTS |
| 2421 | Probabilistic_Methods | On Convergence of the EM Algorithm and the Gibbs Sampler  SUMMARY |
| 2513 | Neural_Networks | Avoiding overfitting by locally matching the noise level of the data gating network discovers the |
| 2654 | Probabilistic_Methods | On the Sample Complexity of Weakly Learning |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=154).
Recorded prediction: `{"Target Node": 154, "Predicted Class": "Neural_Networks", "Confidence": 0.7409}`
Recorded graph stats: `{"total_1hop_degree": 2, "neighbor_label_ratio": {"Probabilistic_Methods": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | coeffici | 0.6863 | 0 |
| 2 | linear | 0.6687 | 0 |
| 3 | result | 0.6683 | 0 |
| 4 | supervis | 0.6467 | 0 |
| 5 | analysis | 0.638 | 1 |
| 6 | space | 0.6357 | 1 |
| 7 | constructor | 0.6336 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
