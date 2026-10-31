# Reference packet: GraphXAIN__GPT-4o__cora__2135

- Method: GraphXAIN; configuration: GPT-4o; dataset: cora; target node: 2135
- Explanation source: `./robustness_2026-10-30/graphxain_gpt4o/cora/2135.json` (narrative)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The GNN model predicted that the target paper, node 2135, belongs to the "Neural_Networks" category with high confidence (96.53%). This decision is influenced by key words from the paper's content, such as "produce", "unlimit", "functions", "feature", "training", and "linear", all of which are present and integral to the topic of learning and modeling, closely aligning with techniques often associated with neural networks. Although the word "connectionist", directly related to neural networks, is notably absent from the paper, its high importance suggests that its presence would have further strengthened the prediction towards this class. The direct citation neighbors also significantly impact the decision; among the top cited works, there are papers like "Gain Adaptation Beats Least Squares?" and "Classification of EEG Signals Using a Sparse Polynomial Builder", both associated with neural network methodologies. These connections draw a parallel between the target paper's emphasis on regression and feature construction and similar neural network strategies. Further supporting this classification, 2-hop neighbors such as "Multivariate versus Univariate Decision Trees" and "From Isolation to Cooperation: An Alternative View of a System of Experts" also focus on neural networks, reinforcing the paper’s connection to this research area. Overall, the target node's emphasis on advanced regression techniques, shared methodologies in citation networks, and the presence of neural network-focused concepts create a compelling case for its classification as part of the Neural_Networks category.
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

### Target Paper (node 2135):
Title: Learning Polynomial Functions by Feature Construction  
Abstract: We present a method for learning higher-order polynomial functions from examples using linear regression and feature construction. Regression is used on a set of training instances to produce a weight vector for a linear functi

### Model Prediction:
{
  "Target Node": 2135,
  "Predicted Class": "Neural_Networks",
  "Confidence": 0.9653
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='connectionist', importance=0.6304, present_in_paper=0
  word='produce', importance=0.6288, present_in_paper=1
  word='unlimit', importance=0.6288, present_in_paper=1
  word='functions', importance=0.6175, present_in_paper=1
  word='feature', importance=0.6168, present_in_paper=1
  word='training', importance=0.6157, present_in_paper=1
  word='linear', importance=0.6087, present_in_paper=1

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 5
Label distribution across all 1-hop neighbors (ground-truth class): Theory=60.0%, Neural_Networks=40.0%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 2583 | edge_importance=0.8174 | class=Theory | Title: Dynamic Automatic Model Selection  
Abstract: COINS Technical Report 92-30 February 1992 Abstract The problem of how to learn from examples has been studied throughout the history of machine le
  Node 2333 | edge_importance=0.79 | class=Theory | Title: Recursive Automatic Algorithm Selection for Inductive Learning  
Abstract: COINS Technical Report 94-61 August 1994 
  Node 2012 | edge_importance=0.7214 | class=Theory | Title: Multivariate Decision Trees  
Abstract: COINS Technical Report 92-82 December 1992 Abstract Multivariate decision trees overcome a representational limitation of univariate decision trees: univ
  Node 134 | edge_importance=0.6957 | class=Neural_Networks | Title: Gain Adaptation Beats Least Squares?  
Abstract: I present computational results suggesting that gain-adaptation algorithms based in part on connectionist learning methods may improve over leas
  Node 2023 | edge_importance=0.4968 | class=Neural_Networks | Title: Classification of EEG Signals Using a Sparse Polynomial Builder  
Abstract: Edward S. Orosz and Charles W. Anderson Technical Report CS-94-111 April 27, 1994 

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 102 | edge_importance=0.8414 | class=Neural_Networks | Title: Multivariate versus Univariate Decision Trees  
Abstract: COINS Technical Report 92-8 January 1992 Abstract In this paper we present a new multivariate decision tree algorithm LMDT, which combi
  Node 505 | edge_importance=0.827 | class=Neural_Networks | Title: From Isolation to Cooperation: An Alternative View of a System of Experts  
Abstract: We introduce a constructive, incremental learning system for regression problems that models data by means 
  Node 318 | edge_importance=0.2606 | class=Case_Based | Title: Generalizing from Case Studies: A Case Study  
Abstract: Most empirical evaluations of machine learning algorithms are case studies evaluations of multiple algorithms on multiple databases. Aut
  Node 378 | edge_importance=0.2336 | class=Theory | Title: Mingers, 1989 J. Mingers. An empirical comparison of pruning methods for decision tree induction. Machine
Abstract: Ourston and Mooney, 1990b ] D. Ourston and R. J. Mooney. Improving shared rul
  Node 1423 | edge_importance=0.2269 | class=Neural_Networks | Title: Comparison of Regression Methods, Symbolic Induction Methods and Neural Networks in Morbidity Diagnosis and Mortality
Abstract: Classifier induction algorithms differ on what inductive hypothes
  Node 1118 | edge_importance=0.2122 | class=Neural_Networks | Title: Adapting Bias by Gradient Descent: An Incremental Version of Delta-Bar-Delta  
Abstract: Appropriate bias is widely viewed as the key to efficient learning and generalization. I present a new a
  Node 1173 | edge_importance=0.1917 | class=Theory | Title: Dynamical Selection of Learning Algorithms  
Abstract: Determining the conditions for which a given learning algorithm is appropriate is an open problem in machine learning. Methods for selecti
  Node 1782 | edge_importance=0.1644 | class=Reinforcement_Learning | Title: Least-Squares Temporal Difference Learning  
Abstract: Submitted to NIPS-98 TD() is a popular family of algorithms for approximate policy evaluation in large MDPs. TD() works by incrementally u
  Node 2310 | edge_importance=0.1637 | class=Case_Based | Title: Machine Learning: An Annotated Bibliography for the 1995 AI Statistics Tutorial on Machine Learning (Version 1)  
Abstract: This is a brief annotated bibliography that I wanted to make availabl

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

- ID: 2135
- Title: Learning Polynomial Functions by Feature Construction
- True class (canonical `y`): **Neural_Networks**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Neural_Networks**
- Prediction recorded by this method's pipeline: **Neural_Networks**

Canonical text (`raw_text`):

~~~~~~text
Title: Learning Polynomial Functions by Feature Construction  
Abstract: We present a method for learning higher-order polynomial functions from examples using linear regression and feature construction. Regression is used on a set of training instances to produce a weight vector for a linear function over the feature set. If this hypothesis is imperfect, a new feature is constructed by forming the product of the two features that most effectively predict the squared error of the current hypothesis. The algorithm is then repeated. In an extension to this method, the specific pair of features to combine is selected by measuring their joint ability to predict the hypothesis' error.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 5 nodes

| node id | true class | title |
|---|---|---|
| 134 | Neural_Networks | Gain Adaptation Beats Least Squares? |
| 2012 | Theory | Multivariate Decision Trees |
| 2023 | Neural_Networks | Classification of EEG Signals Using a Sparse Polynomial Builder |
| 2333 | Theory | Recursive Automatic Algorithm Selection for Inductive Learning |
| 2583 | Theory | Dynamic Automatic Model Selection |

### 2-hop (shortest distance exactly 2): 9 nodes

| node id | true class | title |
|---|---|---|
| 102 | Neural_Networks | Multivariate versus Univariate Decision Trees |
| 318 | Case_Based | Generalizing from Case Studies: A Case Study |
| 378 | Theory | Mingers, 1989 J. Mingers. An empirical comparison of pruning methods for decision tree induction. Machine |
| 505 | Neural_Networks | From Isolation to Cooperation: An Alternative View of a System of Experts |
| 1118 | Neural_Networks | Adapting Bias by Gradient Descent: An Incremental Version of Delta-Bar-Delta |
| 1173 | Theory | Dynamical Selection of Learning Algorithms |
| 1423 | Neural_Networks | Comparison of Regression Methods, Symbolic Induction Methods and Neural Networks in Morbidity Diagnosis and Mortality |
| 1782 | Reinforcement_Learning | Least-Squares Temporal Difference Learning |
| 2310 | Case_Based | Machine Learning: An Annotated Bibliography for the 1995 AI Statistics Tutorial on Machine Learning (Version 1) |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=2135).
Recorded prediction: `{"Target Node": 2135, "Predicted Class": "Neural_Networks", "Confidence": 0.9653}`
Recorded graph stats: `{"total_1hop_degree": 5, "neighbor_label_ratio": {"Theory": 0.6, "Neural_Networks": 0.4}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | connectionist | 0.6304 | 0 |
| 2 | produce | 0.6288 | 1 |
| 3 | unlimit | 0.6288 | 1 |
| 4 | functions | 0.6175 | 1 |
| 5 | feature | 0.6168 | 1 |
| 6 | training | 0.6157 | 1 |
| 7 | linear | 0.6087 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
