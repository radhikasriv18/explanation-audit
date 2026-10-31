# Reference packet: GraphXAIN__Llama-8B__cora__975

- Method: GraphXAIN; configuration: Llama-8B; dataset: cora; target node: 975
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/cora/graphxain_cora_llama_2hop_narratives_full.json` ([975])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
For the given academic computer science paper, titled "State Reconstruction for Determining Predictability in Driven Nonlinear Acoustical Systems," our machine learning model predicts it belongs to the category of "Neural_Networks" with 100% confidence. The model relies heavily on the presence of specific words in the paper's title and abstract, including "nonlinear," "predictability," "state reconstruction," which are strongly associated with Neural_Networks research. It also considers the paper's local graph structure, where the majority of its direct 1-hop citation neighbors belong to Neural_Networks (60%). Most notably, the model is influenced by direct citations from papers like "Nonlinear Prediction of Chaotic Time Series Using Support Vector Machines" and "Regularization Theory and Neural Networks Architectures," both of which demonstrate a strong association with Neural_Networks topics. Furthermore, many 2-hop neighbors also align with Neural_Networks themes, such as modeling volatility and nonlinear trading models, which reinforces the overall prediction. Overall, these collective cues led the model to confidently attribute this paper to the Neural_Networks category.
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

### Target Paper (node 975):
Title: State Reconstruction for Determining Predictability in Driven Nonlinear Acoustical Systems  
Abstract: Genetic programming is distinguished from other evolutionary algorithms in that it uses tree representations of variable size instead of linear strings of fixed length. The flexible represen

### Model Prediction:
{
  "Target Node": 975,
  "Predicted Class": "Neural_Networks",
  "Confidence": 1.0
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='nonlinear', importance=0.6872, present_in_paper=1
  word='predictability', importance=0.6639, present_in_paper=1
  word='neural', importance=0.6601, present_in_paper=0
  word='reconstruction', importance=0.6575, present_in_paper=1
  word='gate', importance=0.6208, present_in_paper=0
  word='function', importance=0.5969, present_in_paper=0
  word='state', importance=0.5886, present_in_paper=1

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 5
Label distribution across all 1-hop neighbors (ground-truth class): Neural_Networks=60.0%, Probabilistic_Methods=40.0%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 1079 | edge_importance=0.7676 | class=Neural_Networks | Title: Nonlinear Prediction of Chaotic Time Series Using Support Vector Machines  
Abstract: A novel method for regression has been recently proposed by V. Vapnik et al. [8, 9]. The technique, called 
  Node 668 | edge_importance=0.727 | class=Neural_Networks | Title: Nonlinear gated experts for time series: discovering regimes and avoiding overfitting  
Abstract: In: International Journal of Neural Systems 6 (1995) p. 373 - 399. URL of this paper: ftp://ftp
  Node 608 | edge_importance=0.7185 | class=Neural_Networks | Title: Regularization Theory and Neural Networks Architectures  
Abstract: We had previously shown that regularization principles lead to approximation schemes which are equivalent to networks with on
  Node 74 | edge_importance=0.6981 | class=Probabilistic_Methods | Title: Hierarchical Mixtures of Experts and the EM Algorithm  
Abstract: We present a tree-structured architecture for supervised learning. The statistical model underlying the architecture is a hiera
  Node 76 | edge_importance=0.2865 | class=Probabilistic_Methods | Title: A VIEW OF THE EM ALGORITHM THAT JUSTIFIES INCREMENTAL, SPARSE, AND OTHER VARIANTS  
Abstract: The EM algorithm performs maximum likelihood estimation for data in which some variables are unobse

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 518 | edge_importance=0.852 | class=Theory | Title: Developments in Probabilistic Modelling with Neural Networks|Ensemble Learning  
Abstract: In this paper I give a review of ensemble learning using a simple example. 
  Node 2654 | edge_importance=0.2841 | class=Probabilistic_Methods | Title: On the Sample Complexity of Weakly Learning  
Abstract: Convergence Results for the EM Approach to Abstract The Expectation-Maximization (EM) algorithm is an iterative approach to maximum likel
  Node 1315 | edge_importance=0.2833 | class=Neural_Networks | Title: Modeling Volatility using State Space Models  
Abstract: In time series problems, noise can be divided into two categories: dynamic noise which drives the process, and observational noise which
  Node 2562 | edge_importance=0.2788 | class=Neural_Networks | Title: NONLINEAR TRADING MODELS THROUGH SHARPE RATIO MAXIMIZATION  
Abstract: Working Paper IS-97-005, Leonard N. Stern School of Business, New York University. In: Decision Technologies for Financial
  Node 2683 | edge_importance=0.2757 | class=Neural_Networks | Title: Introduction to Radial Basis Function Networks  
Abstract: This document is an introduction to radial basis function (RBF) networks, a type of artificial neural network for application to probl
  Node 1934 | edge_importance=0.2737 | class=Probabilistic_Methods | Title: Sequential Update of Bayesian Network Structure  
Abstract: There is an obvious need for improving the performance and accuracy of a Bayesian network as new data is observed. Because of errors 
  Node 345 | edge_importance=0.2721 | class=Probabilistic_Methods | Title: On Convergence Properties of the EM Algorithm for Gaussian Mixtures  
Abstract: We build up the mathematical connection between the "Expectation-Maximization" (EM) algorithm and gradient-based 
  Node 133 | edge_importance=0.2717 | class=Neural_Networks | Title: PRIOR KNOWLEDGE AND THE CREATION OF "VIRTUAL" EXAMPLES FOR RBF NETWORKS 1  
Abstract: We consider the problem of how to incorporate prior knowledge in supervised learning techniques. We set the
  Node 547 | edge_importance=0.2703 | class=Neural_Networks | Title: Expectation-Based Selective Attention for Visual Monitoring and Control of a Robot Vehicle  
Abstract: Reliable vision-based control of an autonomous vehicle requires the ability to focus atten
  Node 1724 | edge_importance=0.2694 | class=Neural_Networks | Title: Annealed Competition of Experts for a Segmentation and Classification of Switching Dynamics  
Abstract: We present a method for the unsupervised segmentation of data streams originating from di

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

- ID: 975
- Title: State Reconstruction for Determining Predictability in Driven Nonlinear Acoustical Systems
- True class (canonical `y`): **Neural_Networks**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Neural_Networks**
- Prediction recorded by this method's pipeline: **Neural_Networks**

Canonical text (`raw_text`):

~~~~~~text
Title: State Reconstruction for Determining Predictability in Driven Nonlinear Acoustical Systems  
Abstract: Genetic programming is distinguished from other evolutionary algorithms in that it uses tree representations of variable size instead of linear strings of fixed length. The flexible representation scheme is very important because it allows the underlying structure of the data to be discovered automatically. One primary difficulty, however, is that the solutions may grow too big without any improvement of their generalization ability. In this paper we investigate the fundamental relationship between the performance and complexity of the evolved structures. The essence of the parsimony problem is demonstrated empirically by analyzing error landscapes of programs evolved for neural network synthesis. We consider genetic programming as a statistical inference problem and apply the Bayesian model-comparison framework to introduce a class of fitness functions with error and complexity terms. An adaptive learning method is then presented that automatically balances the model-complexity factor to evolve parsimonious programs without losing the diversity of the population needed for achieving the desired training accuracy. The effectiveness of this approach is empirically shown on the induction of sigma-pi neural networks for solving a real-world medical diagnosis problem as well as benchmark tasks. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 5 nodes

| node id | true class | title |
|---|---|---|
| 74 | Probabilistic_Methods | Hierarchical Mixtures of Experts and the EM Algorithm |
| 76 | Probabilistic_Methods | A VIEW OF THE EM ALGORITHM THAT JUSTIFIES INCREMENTAL, SPARSE, AND OTHER VARIANTS |
| 608 | Neural_Networks | Regularization Theory and Neural Networks Architectures |
| 668 | Neural_Networks | Nonlinear gated experts for time series: discovering regimes and avoiding overfitting |
| 1079 | Neural_Networks | Nonlinear Prediction of Chaotic Time Series Using Support Vector Machines |

### 2-hop (shortest distance exactly 2): 67 nodes

| node id | true class | title |
|---|---|---|
| 19 | Neural_Networks | Validation of Average Error Rate Over Classifiers |
| 71 | Probabilistic_Methods | Supervised learning from incomplete data via an EM approach |
| 131 | Probabilistic_Methods | The Expectation-Maximization Algorithm for MAP Estimation |
| 133 | Neural_Networks | PRIOR KNOWLEDGE AND THE CREATION OF "VIRTUAL" EXAMPLES FOR RBF NETWORKS 1 |
| 154 | Neural_Networks | Data-driven Modeling and Synthesis of Acoustical Instruments |
| 179 | Neural_Networks | for Projective Basis Function Networks 2m1 Global Form 2m Local Form With appropriate constant factors, |
| 181 | Theory | Ensemble Learning and Evidence Maximization |
| 193 | Neural_Networks | Soft Classification, a.k.a. Risk Estimation, via Penalized Log Likelihood and Smoothing Spline Analysis of Variance |
| 250 | Probabilistic_Methods | Mean Field Theory for Sigmoid Belief Networks |
| 252 | Reinforcement_Learning | A Modular Q-Learning Architecture for Manipulator Task Decomposition `Data storage in the cerebellar model ar |
| 263 | Neural_Networks | Non-linear Models for Time Series Using Mixtures of Experts |
| 310 | Neural_Networks | Forecasting electricity demand using nonlinear mixture of experts |
| 345 | Probabilistic_Methods | On Convergence Properties of the EM Algorithm for Gaussian Mixtures |
| 377 | Neural_Networks | Constructive Algorithms for Hierarchical Mixtures of Experts |
| 392 | Probabilistic_Methods | DRAFT Cluster-Weighted Modeling for Time Series Prediction and Characterization |
| 394 | Neural_Networks | Prior Information and Generalized Questions |
| 505 | Neural_Networks | From Isolation to Cooperation: An Alternative View of a System of Experts |
| 511 | Probabilistic_Methods | Learning from incomplete data |
| 518 | Theory | Developments in Probabilistic Modelling with Neural Networks\|Ensemble Learning |
| 547 | Neural_Networks | Expectation-Based Selective Attention for Visual Monitoring and Control of a Robot Vehicle |
| 604 | Neural_Networks | First experiments using a mixture of nonlinear experts for time series prediction |
| 611 | Neural_Networks | Learning networks for face analysis and synthesis |
| 622 | Neural_Networks | CLASSIFICATION USING HIERARCHICAL MIXTURES OF EXPERTS |
| 661 | Probabilistic_Methods | A Statistical Approach to Decision Tree Modeling |
| 680 | Neural_Networks | Cortical Mechanisms of Visual Recognition and Learning: A Hierarchical Kalman Filter Model |
| 694 | Neural_Networks | Localist Attractor Networks |
| 787 | Probabilistic_Methods | Hidden Markov decision trees |
| 864 | Neural_Networks | A Sparse Representation for Function Approximation |
| 867 | Neural_Networks | Comparison of Neural and Statistical Classifiers\| Theory and Practice |
| 869 | Probabilistic_Methods | Efficient Stochastic Source Coding and an Application to a Bayesian Network Source Model |
| 871 | Probabilistic_Methods | Factorial Learning and the EM Algorithm |
| 881 | Neural_Networks | Proben1 A Set of Neural Network Benchmark Problems and Benchmarking Rules |
| 906 | Neural_Networks | Memory-based Time Series Recognition  A New Methodology and Real World Applications |
| 949 | Neural_Networks | Classifying Seismic Signals by Integrating Ensembles of Neural Networks |
| 987 | Probabilistic_Methods | Stacked Density Estimation |
| 1009 | Genetic_Algorithms | Induction of decision trees using RELIEFF |
| 1017 | Neural_Networks | Using Neural Networks for Descriptive Statistical Analysis of Educational Data |
| 1024 | Theory | On learning hierarchical classifications |
| 1103 | Neural_Networks | Adaptive Computation Techniques for Time Series Analysis Major Professor: </title> <journal> Dr. Mehdi Zargham </journal> |
| 1128 | Probabilistic_Methods | On Structured Variational Approximations |
| 1220 | Neural_Networks | A Method of Combining Multiple Probabilistic Classifiers through Soft Competition on Different Feature Sets |
| 1315 | Neural_Networks | Modeling Volatility using State Space Models |
| 1389 | Neural_Networks | Support Vector Machines: Training and Applications |
| 1508 | Neural_Networks | Segmenting Time Series using Gated Experts with Simulated Annealing |
| 1548 | Probabilistic_Methods | Free energy coding  In |
| 1634 | Neural_Networks | Combining Linear Discriminant Functions with Neural Networks for Supervised Learning |
| 1676 | Neural_Networks | TD Learning of Game Evaluation Functions with Hierarchical Neural Architectures |
| 1718 | Neural_Networks | PREDICTING SUNSPOTS AND EXCHANGE RATES WITH CONNECTIONIST NETWORKS |
| 1724 | Neural_Networks | Annealed Competition of Experts for a Segmentation and Classification of Switching Dynamics |
| 1928 | Neural_Networks | Mixtures of Probabilistic Principal Component Analysers |
| 1934 | Probabilistic_Methods | Sequential Update of Bayesian Network Structure |
| 2013 | Neural_Networks | Using the Stochastic Gradient Method to Fit Polychotomous Regression Models |
| 2124 | Neural_Networks | A Hierarchical Latent Variable Model for Data Visualization |
| 2230 | Neural_Networks | In Advances in Neural Information Processing Systems 8  Gaussian Processes for Regression |
| 2266 | Probabilistic_Methods | A Gentle Tutorial of the EM Algorithm and its Application to Parameter Estimation for Gaussian |
| 2284 | Neural_Networks | Performance of On-Line Learning Methods in Predicting Multiprocessor Memory Access Patterns |
| 2327 | Theory | A Comparison of New and Old Algorithms for A Mixture Estimation Problem |
| 2335 | Neural_Networks | Function Approximation with Neural Networks and Local Methods: Bias, Variance and Smoothness |
| 2390 | Neural_Networks | A HIERARCHICAL COMMUNITY OF EXPERTS |
| 2413 | Neural_Networks | On-Line Adaptation of a Signal Predistorter through Dual Reinforcement Learning |
| 2414 | Neural_Networks | On-Line Adaptation of a Signal Predistorter through Dual Reinforcement Learning |
| 2421 | Probabilistic_Methods | On Convergence of the EM Algorithm and the Gibbs Sampler  SUMMARY |
| 2513 | Neural_Networks | Avoiding overfitting by locally matching the noise level of the data gating network discovers the |
| 2532 | Probabilistic_Methods | Ensemble Learning for Hidden Markov Models |
| 2562 | Neural_Networks | NONLINEAR TRADING MODELS THROUGH SHARPE RATIO MAXIMIZATION |
| 2654 | Probabilistic_Methods | On the Sample Complexity of Weakly Learning |
| 2683 | Neural_Networks | Introduction to Radial Basis Function Networks |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=975).
Recorded prediction: `{"Target Node": 975, "Predicted Class": "Neural_Networks", "Confidence": 1.0}`
Recorded graph stats: `{"total_1hop_degree": 5, "neighbor_label_ratio": {"Neural_Networks": 0.6, "Probabilistic_Methods": 0.4}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | nonlinear | 0.6872 | 1 |
| 2 | predictability | 0.6639 | 1 |
| 3 | neural | 0.6601 | 0 |
| 4 | reconstruction | 0.6575 | 1 |
| 5 | gate | 0.6208 | 0 |
| 6 | function | 0.5969 | 0 |
| 7 | state | 0.5886 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
