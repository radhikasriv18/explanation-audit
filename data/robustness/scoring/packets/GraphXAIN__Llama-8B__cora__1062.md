# Reference packet: GraphXAIN__Llama-8B__cora__1062

- Method: GraphXAIN; configuration: Llama-8B; dataset: cora; target node: 1062
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/cora/graphxain_cora_llama_2hop_narratives_full.json` ([1062])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model confidently predicted that paper 1062 falls under the category of Neural_Networks, reaching a high level of accuracy at 99.89%. This prediction was largely driven by the presence of key terms in the paper's content, such as 'local','single', 'function', 'neurons', which all relate to neural networks. Although the term 'neural' itself is absent from the paper, other strongly associated terms suggest its relevance. Furthermore, the model drew significant insights from the paper's direct citation connections, where the majority of these neighboring papers also belong to the Neural_Networks category. For instance, the highly influential neighbor 'BACKPROPAGATION CAN GIVE RISE TO SPURIOUS LOCAL MINIMA EVEN FOR NETWORKS WITHOUT HIDDEN LAYERS' strongly supports the prediction, likely due to its discussion of backpropagation and local minima - core concepts within neural networks. The model did consider distant connections, too, noting how related topics were picked up in 2-hop citations like 'What Size Neural Network Gives Optimal Generalization?' and 'LESSONS IN NEURAL NETWORK TRAINING'. Overall, these cues collectively contributed to a strong association with the Neural_Networks category.
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

### Target Paper (node 1062):
Title: Exponentially many local minima for single neurons  
Abstract: We show that for a single neuron with the logistic function as the transfer function the number of local minima of the error function based on the square loss can grow exponentially in the dimension.

### Model Prediction:
{
  "Target Node": 1062,
  "Predicted Class": "Neural_Networks",
  "Confidence": 0.9989
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='neural', importance=0.6623, present_in_paper=0
  word='local', importance=0.637, present_in_paper=1
  word='single', importance=0.6357, present_in_paper=1
  word='brain', importance=0.6158, present_in_paper=0
  word='function', importance=0.6136, present_in_paper=1
  word='neurons', importance=0.6043, present_in_paper=1
  word='classic', importance=0.5891, present_in_paper=0

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 4
Label distribution across all 1-hop neighbors (ground-truth class): Neural_Networks=75.0%, Theory=25.0%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 2651 | edge_importance=0.8452 | class=Theory | Title: Relative Loss Bounds for Multidimensional Regression Problems  
Abstract: We study on-line generalized linear regression with multidimensional outputs, i.e., neural networks with multiple outpu
  Node 1254 | edge_importance=0.8075 | class=Neural_Networks | Title: BACKPROPAGATION SEPARATES WHERE PERCEPTRONS DO  
Abstract: Feedforward nets with sigmoidal activation functions are often designed by minimizing a cost criterion. It has been pointed out before
  Node 1323 | edge_importance=0.5736 | class=Neural_Networks | Title: On the Distribution of Performance from Multiple Neural Network Trials, On the Distribution of Performance
Abstract: Andrew D. Back was with the Department of Electrical and Computer Engineerin
  Node 930 | edge_importance=0.5468 | class=Neural_Networks | Title: BACKPROPAGATION CAN GIVE RISE TO SPURIOUS LOCAL MINIMA EVEN FOR NETWORKS WITHOUT HIDDEN LAYERS  
Abstract: We give an example of a neural net without hidden layers and with a sigmoid transfer f

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 1149 | edge_importance=0.8251 | class=Neural_Networks | Title: What Size Neural Network Gives Optimal Generalization? Convergence Properties of Backpropagation  
Abstract: Technical Report UMIACS-TR-96-22 and CS-TR-3617 Institute for Advanced Computer Stud
  Node 1150 | edge_importance=0.8003 | class=Neural_Networks | Title: Lessons in Neural Network Training: Overfitting Lessons in Neural Network Training: Overfitting May be Harder
Abstract: For many reasons, neural networks have become very popular AI machine lea
  Node 1464 | edge_importance=0.7546 | class=Neural_Networks | Title: LINEAR SYSTEMS WITH SIGN-OBSERVATIONS  
Abstract: This paper deals with systems that are obtained from linear time-invariant continuous-or discrete-time devices followed by a function that just
  Node 2059 | edge_importance=0.2502 | class=Theory | Title: Challenges in Evolving Controllers for Physical Robots  
Abstract: General convergence results for linear discriminant updates Abstract The problem of learning linear discriminant concepts can 
  Node 805 | edge_importance=0.2049 | class=Neural_Networks | Title: Critical Points for Least-Squares Problems Involving Certain Analytic Functions, with Applications to Sigmoidal Nets  
Abstract: This paper deals with nonlinear least-squares problems involving
  Node 1195 | edge_importance=0.1923 | class=Neural_Networks | Title: Statistical Evaluation of Neural Network Experiments: Minimum Requirements and Current Practice  
Abstract:  
  Node 1145 | edge_importance=0.1717 | class=Neural_Networks | Title: A Unifying View of Some Training Algorithms for Multilayer Perceptrons with FIR Filter Synapses  
Abstract: Recent interest has come about in deriving various neural network architectures for m

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

- ID: 1062
- Title: Exponentially many local minima for single neurons
- True class (canonical `y`): **Theory**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Neural_Networks**
- Prediction recorded by this method's pipeline: **Neural_Networks**

Canonical text (`raw_text`):

~~~~~~text
Title: Exponentially many local minima for single neurons  
Abstract: We show that for a single neuron with the logistic function as the transfer function the number of local minima of the error function based on the square loss can grow exponentially in the dimension.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 4 nodes

| node id | true class | title |
|---|---|---|
| 930 | Neural_Networks | BACKPROPAGATION CAN GIVE RISE TO SPURIOUS LOCAL MINIMA EVEN FOR NETWORKS WITHOUT HIDDEN LAYERS |
| 1254 | Neural_Networks | BACKPROPAGATION SEPARATES WHERE PERCEPTRONS DO |
| 1323 | Neural_Networks | On the Distribution of Performance from Multiple Neural Network Trials, On the Distribution of Performance |
| 2651 | Theory | Relative Loss Bounds for Multidimensional Regression Problems |

### 2-hop (shortest distance exactly 2): 7 nodes

| node id | true class | title |
|---|---|---|
| 805 | Neural_Networks | Critical Points for Least-Squares Problems Involving Certain Analytic Functions, with Applications to Sigmoidal Nets |
| 1145 | Neural_Networks | A Unifying View of Some Training Algorithms for Multilayer Perceptrons with FIR Filter Synapses |
| 1149 | Neural_Networks | What Size Neural Network Gives Optimal Generalization? Convergence Properties of Backpropagation |
| 1150 | Neural_Networks | Lessons in Neural Network Training: Overfitting Lessons in Neural Network Training: Overfitting May be Harder |
| 1195 | Neural_Networks | Statistical Evaluation of Neural Network Experiments: Minimum Requirements and Current Practice |
| 1464 | Neural_Networks | LINEAR SYSTEMS WITH SIGN-OBSERVATIONS |
| 2059 | Theory | Challenges in Evolving Controllers for Physical Robots |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=1062).
Recorded prediction: `{"Target Node": 1062, "Predicted Class": "Neural_Networks", "Confidence": 0.9989}`
Recorded graph stats: `{"total_1hop_degree": 4, "neighbor_label_ratio": {"Neural_Networks": 0.75, "Theory": 0.25}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | neural | 0.6623 | 0 |
| 2 | local | 0.637 | 1 |
| 3 | single | 0.6357 | 1 |
| 4 | brain | 0.6158 | 0 |
| 5 | function | 0.6136 | 1 |
| 6 | neurons | 0.6043 | 1 |
| 7 | classic | 0.5891 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
