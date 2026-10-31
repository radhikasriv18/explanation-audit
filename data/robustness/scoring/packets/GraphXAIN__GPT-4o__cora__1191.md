# Reference packet: GraphXAIN__GPT-4o__cora__1191

- Method: GraphXAIN; configuration: GPT-4o; dataset: cora; target node: 1191
- Explanation source: `./robustness_2026-10-30/graphxain_gpt4o/cora/1191.json` (narrative)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The GNN model predicted with complete confidence that the target paper (node 1191) belongs to the "Theory" research area. This prediction was significantly influenced by the presence of the word "bias" in the paper, which, coupled with other related terms like "measure" and "machine" also present in the paper, signals a theoretical discussion about biases in machine learning. Despite not being present, high-importance terms like "classif" and "loss" hint at the theoretical exploration of classification methodologies. The most influential direct citation neighbors bolster this prediction, particularly papers like "Decision Tree Induction: How Effective is the Greedy Heuristic?" and "A THEORY OF LEARNING CLASSIFICATION RULES," both rooted in theoretical discussions. Additionally, these neighbors largely belong to the Theory category themselves, suggesting a network of theoretical discourse. Further supporting the prediction, 2-hop neighbors like "On learning hierarchical classifications" continue this theoretical theme, reinforcing the model's confidence in classifying the paper under the Theory category. These connections and features collectively push the model towards a Theory prediction, highlighting an academic conversation centered around theoretical concepts in decision tree analysis and bias-variance discussions.
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

### Target Paper (node 1191):
Title: Machine Learning Bias, Statistical Bias, and Statistical Variance of Decision Tree Algorithms  
Abstract: The term "bias" is widely used|and with different meanings|in the fields of machine learning and statistics. This paper clarifies the uses of this term and shows how to measure and visual

### Model Prediction:
{
  "Target Node": 1191,
  "Predicted Class": "Theory",
  "Confidence": 1.0
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='bias', importance=0.6546, present_in_paper=1
  word='classif', importance=0.6381, present_in_paper=0
  word='loss', importance=0.63, present_in_paper=0
  word='good', importance=0.6292, present_in_paper=0
  word='node', importance=0.6273, present_in_paper=0
  word='measure', importance=0.6263, present_in_paper=1
  word='machine', importance=0.6214, present_in_paper=1

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 5
Label distribution across all 1-hop neighbors (ground-truth class): Theory=80.0%, Probabilistic_Methods=20.0%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 692 | edge_importance=0.8093 | class=Theory | Title: Decision Tree Induction: How Effective is the Greedy Heuristic?  
Abstract: Most existing decision tree systems use a greedy approach to induce trees | locally optimal splits are induced at eve
  Node 661 | edge_importance=0.8069 | class=Probabilistic_Methods | Title: A Statistical Approach to Decision Tree Modeling  
Abstract: A statistical approach to decision tree modeling is described. In this approach, each decision in the tree is modeled parametrically
  Node 2423 | edge_importance=0.7215 | class=Theory | Title: Error-Correcting Output Codes: A General Method for Improving Multiclass Inductive Learning Programs  
Abstract: Multiclass learning problems involve finding a definition for an unknown functio
  Node 1290 | edge_importance=0.6593 | class=Theory | Title: A THEORY OF LEARNING CLASSIFICATION RULES  
Abstract: This chapter takes a different standpoint to address the problem of learning. We will here reason only in terms of probability, and make ex
  Node 1053 | edge_importance=0.5608 | class=Theory | Title: Bias Plus Variance Decomposition for Zero-One Loss Functions  
Abstract: We present a bias-variance decomposition of expected misclassification rate, the most commonly used loss function in sup

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 1601 | edge_importance=0.829 | class=Neural_Networks | Title: Learning the Past Tense of English Verbs: The Symbolic Pattern Associator vs. Connectionist Models  
Abstract: Learning the past tense of English verbs | a seemingly minor aspect of language ac
  Node 1024 | edge_importance=0.8282 | class=Theory | Title: On learning hierarchical classifications  
Abstract: Many significant real-world classification tasks involve a large number of categories which are arranged in a hierarchical structure; for ex
  Node 296 | edge_importance=0.8229 | class=Theory | Title: Lookahead and Pathology in Decision Tree Induction  
Abstract: The standard approach to decision tree induction is a top-down, greedy algorithm that makes locally optimal, irrevocable decisions
  Node 71 | edge_importance=0.819 | class=Probabilistic_Methods | Title: Supervised learning from incomplete data via an EM approach  
Abstract: Real-world learning tasks may involve high-dimensional data sets with arbitrary patterns of missing data. In this paper w
  Node 550 | edge_importance=0.2426 | class=Theory | Title: LEARNING BY USING DYNAMIC FEATURE COMBINATION AND SELECTION  
Abstract:  
  Node 1644 | edge_importance=0.2409 | class=Neural_Networks | Title: A Comparative Study of ID3 and Backpropagation for English Text-to-Speech Mapping  
Abstract: The performance of the error backpropagation (BP) and ID3 learning algorithms was compared on the t
  Node 2627 | edge_importance=0.2367 | class=Theory | Title: Probability Estimation via Error-Correcting Output Coding  
Abstract: Previous research has shown that a technique called error-correcting output coding (ECOC) can dramatically improve the clas
  Node 881 | edge_importance=0.2365 | class=Neural_Networks | Title: Proben1 A Set of Neural Network Benchmark Problems and Benchmarking Rules  
Abstract: Proben1 is a collection of problems for neural network learning in the realm of pattern classification and 
  Node 429 | edge_importance=0.2335 | class=Probabilistic_Methods | Title: Classifiers: A Theoretical and Empirical Study  
Abstract: This paper describes how a competitive tree learning algorithm can be derived from first principles. The algorithm approximates the Ba
  Node 853 | edge_importance=0.233 | class=Theory | Title: Error-Correcting Output Codes for Local Learners  
Abstract: Error-correcting output codes (ECOCs) represent classes with a set of output bits, where each bit encodes a binary classification ta

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

- ID: 1191
- Title: Machine Learning Bias, Statistical Bias, and Statistical Variance of Decision Tree Algorithms
- True class (canonical `y`): **Theory**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Theory**
- Prediction recorded by this method's pipeline: **Theory**

Canonical text (`raw_text`):

~~~~~~text
Title: Machine Learning Bias, Statistical Bias, and Statistical Variance of Decision Tree Algorithms  
Abstract: The term "bias" is widely used|and with different meanings|in the fields of machine learning and statistics. This paper clarifies the uses of this term and shows how to measure and visualize the statistical bias and variance of learning algorithms. Statistical bias and variance can be applied to diagnose problems with machine learning bias, and the paper shows four examples of this. Finally, the paper discusses methods of reducing bias and variance. Methods based on voting can reduce variance, and the paper compares Breiman's bagging method and our own tree randomization method for voting decision trees. Both methods uniformly improve performance on data sets from the Irvine repository. Tree randomization yields perfect performance on the Letter Recognition task. A weighted nearest neighbor algorithm based on the infinite bootstrap is also introduced. In general, decision tree algorithms have moderate-to-high variance, so an important implication of this work is that variance|rather than appropriate or inappropriate machine learning bias|is an important cause of poor performance for decision tree algorithms. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 5 nodes

| node id | true class | title |
|---|---|---|
| 661 | Probabilistic_Methods | A Statistical Approach to Decision Tree Modeling |
| 692 | Theory | Decision Tree Induction: How Effective is the Greedy Heuristic? |
| 1053 | Theory | Bias Plus Variance Decomposition for Zero-One Loss Functions |
| 1290 | Theory | A THEORY OF LEARNING CLASSIFICATION RULES |
| 2423 | Theory | Error-Correcting Output Codes: A General Method for Improving Multiclass Inductive Learning Programs |

### 2-hop (shortest distance exactly 2): 36 nodes

| node id | true class | title |
|---|---|---|
| 71 | Probabilistic_Methods | Supervised learning from incomplete data via an EM approach |
| 74 | Probabilistic_Methods | Hierarchical Mixtures of Experts and the EM Algorithm |
| 76 | Probabilistic_Methods | A VIEW OF THE EM ALGORITHM THAT JUSTIFIES INCREMENTAL, SPARSE, AND OTHER VARIANTS |
| 218 | Probabilistic_Methods | Learning Classification Trees |
| 296 | Theory | Lookahead and Pathology in Decision Tree Induction |
| 378 | Theory | Mingers, 1989 J. Mingers. An empirical comparison of pruning methods for decision tree induction. Machine |
| 423 | Probabilistic_Methods | LEARNING BAYESIAN NETWORKS WITH LOCAL STRUCTURE |
| 429 | Probabilistic_Methods | Classifiers: A Theoretical and Empirical Study |
| 438 | Theory | A System for Induction of Oblique Decision Trees |
| 550 | Theory | LEARNING BY USING DYNAMIC FEATURE COMBINATION AND SELECTION |
| 853 | Theory | Error-Correcting Output Codes for Local Learners |
| 862 | Case_Based | Language-Independent Data-Oriented Grapheme-to-Phoneme Conversion |
| 881 | Neural_Networks | Proben1 A Set of Neural Network Benchmark Problems and Benchmarking Rules |
| 893 | Rule_Learning | LEARNING LOGICAL EXCEPTIONS IN CHESS |
| 931 | Theory | MAJORITY VOTE CLASSIFIERS: THEORY AND APPLICATIONS |
| 1019 | Theory | Bibliography "SMART: Support Management Automated Reasoning Technology for COMPAQ Customer Service," "Instance-Based Learning Algorithms," Machine |
| 1024 | Theory | On learning hierarchical classifications |
| 1025 | Theory | Machine Learning 27(1):51-68, 1997. Predicting nearly as well as the best pruning of a decision tree |
| 1161 | Theory | Inductive Learning by Selection of Minimal Complexity Representations |
| 1197 | Theory | Why Does Bagging Work? A Bayesian Account and its Implications bagging's success, both in a |
| 1226 | Rule_Learning | On Learning Multiple Descriptions of a Concept |
| 1238 | Theory | On Pruning and Averaging Decision Trees |
| 1463 | Probabilistic_Methods | Bias, variance and prediction error for classification rules |
| 1568 | Case_Based | The Utility of Feature Weighting in Nearest-Neighbor Algorithms |
| 1601 | Neural_Networks | Learning the Past Tense of English Verbs: The Symbolic Pattern Associator vs. Connectionist Models |
| 1607 | Theory | Characterizing the generalization performance of model selection strategies |
| 1644 | Neural_Networks | A Comparative Study of ID3 and Backpropagation for English Text-to-Speech Mapping |
| 1712 | Theory | An Efficient Extension to Mixture Techniques for Prediction and Decision Trees |
| 1732 | Neural_Networks | Improving the Performance of Radial Basis Function Networks by Learning Center Locations |
| 1918 | Theory | Stochastic Logic Programs |
| 2080 | Theory | Learning from positive data |
| 2169 | Probabilistic_Methods | Theory Refinement on Bayesian Networks |
| 2225 | Theory | Error-Correcting Output Coding Corrects Bias and Variance |
| 2329 | Theory | Programming Research Group A LEARNABILITY MODEL FOR UNIVERSAL REPRESENTATIONS |
| 2627 | Theory | Probability Estimation via Error-Correcting Output Coding |
| 2657 | Theory | Learning Complex Boolean Functions: Algorithms and Applications |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=1191).
Recorded prediction: `{"Target Node": 1191, "Predicted Class": "Theory", "Confidence": 1.0}`
Recorded graph stats: `{"total_1hop_degree": 5, "neighbor_label_ratio": {"Theory": 0.8, "Probabilistic_Methods": 0.2}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | bias | 0.6546 | 1 |
| 2 | classif | 0.6381 | 0 |
| 3 | loss | 0.63 | 0 |
| 4 | good | 0.6292 | 0 |
| 5 | node | 0.6273 | 0 |
| 6 | measure | 0.6263 | 1 |
| 7 | machine | 0.6214 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
