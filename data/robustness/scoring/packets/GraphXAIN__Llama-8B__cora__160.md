# Reference packet: GraphXAIN__Llama-8B__cora__160

- Method: GraphXAIN; configuration: Llama-8B; dataset: cora; target node: 160
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/cora/graphxain_cora_llama_2hop_narratives_full.json` ([160])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Given the paper titled "EVALUATION OF GAUSSIAN PROCESSES AND OTHER METHODS FOR NON-LINEAR REGRESSION," the model confidently predicts a classification of "Neural_Networks" with a probability of 94.92%. Top words such as "processes" being present in the paper and other highly associated terms like "parameter," strongly associate the target paper with neural networks. Importantly, the direct neighbors of the target paper, also classified mainly under Neural_Networks, further reinforce this prediction. Specifically, influential citation neighbors include papers discussing topics such as Gaussian Processes, hybrid Monte Carlo methods, and neural network applications. Additionally, while two-hop neighbors span multiple classes, they maintain a strong presence of Neural_Networks titles, solidifying the prediction's basis. These connections demonstrate how the model considered not only the local attributes but also the contextual influence of nearby papers to arrive at its conclusion. Overall, the model has provided a well-supported prediction rooted in the relationships between key papers in the dataset.
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

### Target Paper (node 160):
Title: EVALUATION OF GAUSSIAN PROCESSES AND OTHER METHODS FOR NON-LINEAR REGRESSION  
Abstract: The theory revision problem is the problem of how best to go about revising a deficient domain theory using information contained in examples that expose inaccuracies. In this paper we present our approac

### Model Prediction:
{
  "Target Node": 160,
  "Predicted Class": "Neural_Networks",
  "Confidence": 0.9492
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='parameter', importance=0.6666, present_in_paper=0
  word='provid', importance=0.6619, present_in_paper=0
  word='processes', importance=0.652, present_in_paper=1
  word='input', importance=0.6477, present_in_paper=0
  word='system', importance=0.6476, present_in_paper=0
  word='advanc', importance=0.6463, present_in_paper=0
  word='neural', importance=0.6462, present_in_paper=0

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 6
Label distribution across all 1-hop neighbors (ground-truth class): Neural_Networks=66.7%, Theory=16.7%, Probabilistic_Methods=16.7%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 469 | edge_importance=0.8093 | class=Neural_Networks | Title: Interpolation Models with Multiple  
Abstract: A traditional interpolation model is characterized by the choice of reg-ularizer applied to the interpolant, and the choice of noise model. Typica
  Node 2681 | edge_importance=0.7608 | class=Neural_Networks | Title: Regression with Input-dependent Noise: A Gaussian Process Treatment  
Abstract: Technical Report NCRG/98/002, available from http://www.ncrg.aston.ac.uk/ To appear in Advances in Neural Informa
  Node 2540 | edge_importance=0.7075 | class=Neural_Networks | Title: Efficient Implementation of Gaussian Processes  
Abstract: Neural networks and Bayesian inference provide a useful framework within which to solve regression problems. However their parameteriz
  Node 1857 | edge_importance=0.6812 | class=Probabilistic_Methods | Title: Monte Carlo Implementation of Gaussian Process Models for Bayesian Regression and Classification  
Abstract: Technical Report No. 9702, Department of Statistics, University of Toronto Abstract.
  Node 125 | edge_importance=0.6355 | class=Neural_Networks | Title: Gaussian Processes for Bayesian Classification via Hybrid Monte Carlo  
Abstract: The full Bayesian method for applying neural networks to a prediction problem is to set up the prior/hyperprior
  Node 322 | edge_importance=0.4732 | class=Theory | Title: Statistical Tests for Comparing Supervised Classification Learning Algorithms  
Abstract: This paper reviews five statistical tests for determining whether one learning algorithm outperforms an

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 2020 | edge_importance=0.821 | class=Neural_Networks | Title: Variational Gaussian Process Classifiers  
Abstract:  
  Node 394 | edge_importance=0.7952 | class=Neural_Networks | Title: Prior Information and Generalized Questions  
Abstract: This report describes research done within the Center for Biological and Computational Learning in the Department of Brain and Cognitive 
  Node 78 | edge_importance=0.3018 | class=Theory | Title: Probabilistic Networks: New Models and New Methods  
Abstract: In this paper I describe the implementation of a probabilistic regression model in BUGS. BUGS is a program that carries out Bayesi
  Node 1027 | edge_importance=0.2901 | class=Theory | Title: Pessimistic decision tree pruning based on tree size  
Abstract: In this work we develop a new criteria to perform pessimistic decision tree pruning. Our method is theoretically sound and is ba
  Node 157 | edge_importance=0.2181 | class=Theory | Title: A Practical Bayesian Framework for Backprop Networks  
Abstract: A quantitative and practical Bayesian framework is described for learning of mappings in feedforward networks. The framework mak
  Node 611 | edge_importance=0.2092 | class=Neural_Networks | Title: Learning networks for face analysis and synthesis  
Abstract: This paper presents an overview of the face-related projects in our group. The unifying theme underlying our work is the use of exa
  Node 1644 | edge_importance=0.1904 | class=Neural_Networks | Title: A Comparative Study of ID3 and Backpropagation for English Text-to-Speech Mapping  
Abstract: The performance of the error backpropagation (BP) and ID3 learning algorithms was compared on the t
  Node 2508 | edge_importance=0.1828 | class=Theory | Title: WRAPPERS FOR PERFORMANCE ENHANCEMENT AND OBLIVIOUS DECISION GRAPHS  
Abstract: This paper introduces the idea of clearning, of simultaneously cleaning data and learning the underlying structure
  Node 214 | edge_importance=0.1546 | class=Neural_Networks | Title: Bayesian Non-linear Modelling for the Prediction Competition  
Abstract: The 1993 energy prediction competition involved the prediction of a series of building energy loads from a series of env
  Node 967 | edge_importance=0.1531 | class=Theory | Title: Rigorous Learning Curve Bounds from Statistical Mechanics  
Abstract: In this paper we introduce and investigate a mathematically rigorous theory of learning curves that is based on ideas from 

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

- ID: 160
- Title: EVALUATION OF GAUSSIAN PROCESSES AND OTHER METHODS FOR NON-LINEAR REGRESSION
- True class (canonical `y`): **Neural_Networks**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Neural_Networks**
- Prediction recorded by this method's pipeline: **Neural_Networks**

Canonical text (`raw_text`):

~~~~~~text
Title: EVALUATION OF GAUSSIAN PROCESSES AND OTHER METHODS FOR NON-LINEAR REGRESSION  
Abstract: The theory revision problem is the problem of how best to go about revising a deficient domain theory using information contained in examples that expose inaccuracies. In this paper we present our approach to the theory revision problem for propositional domain theories. The approach described here, called PTR, uses probabilities associated with domain theory elements to numerically track the ``ow'' of proof through the theory. This allows us to measure the precise role of a clause or literal in allowing or preventing a (desired or undesired) derivation for a given example. This information is used to efficiently locate and repair awed elements of the theory. PTR is proved to converge to a theory which correctly classifies all examples, and shown experimentally to be fast and accurate even for deep theories.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 6 nodes

| node id | true class | title |
|---|---|---|
| 125 | Neural_Networks | Gaussian Processes for Bayesian Classification via Hybrid Monte Carlo |
| 322 | Theory | Statistical Tests for Comparing Supervised Classification Learning Algorithms |
| 469 | Neural_Networks | Interpolation Models with Multiple |
| 1857 | Probabilistic_Methods | Monte Carlo Implementation of Gaussian Process Models for Bayesian Regression and Classification |
| 2540 | Neural_Networks | Efficient Implementation of Gaussian Processes |
| 2681 | Neural_Networks | Regression with Input-dependent Noise: A Gaussian Process Treatment |

### 2-hop (shortest distance exactly 2): 11 nodes

| node id | true class | title |
|---|---|---|
| 15 | Neural_Networks | Back Propagation is Sensitive to Initial Conditions |
| 78 | Theory | Probabilistic Networks: New Models and New Methods |
| 157 | Theory | A Practical Bayesian Framework for Backprop Networks |
| 214 | Neural_Networks | Bayesian Non-linear Modelling for the Prediction Competition |
| 394 | Neural_Networks | Prior Information and Generalized Questions |
| 611 | Neural_Networks | Learning networks for face analysis and synthesis |
| 967 | Theory | Rigorous Learning Curve Bounds from Statistical Mechanics |
| 1027 | Theory | Pessimistic decision tree pruning based on tree size |
| 1644 | Neural_Networks | A Comparative Study of ID3 and Backpropagation for English Text-to-Speech Mapping |
| 2020 | Neural_Networks | Variational Gaussian Process Classifiers |
| 2508 | Theory | WRAPPERS FOR PERFORMANCE ENHANCEMENT AND OBLIVIOUS DECISION GRAPHS |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=160).
Recorded prediction: `{"Target Node": 160, "Predicted Class": "Neural_Networks", "Confidence": 0.9492}`
Recorded graph stats: `{"total_1hop_degree": 6, "neighbor_label_ratio": {"Neural_Networks": 0.667, "Theory": 0.167, "Probabilistic_Methods": 0.167}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | parameter | 0.6666 | 0 |
| 2 | provid | 0.6619 | 0 |
| 3 | processes | 0.652 | 1 |
| 4 | input | 0.6477 | 0 |
| 5 | system | 0.6476 | 0 |
| 6 | advanc | 0.6463 | 0 |
| 7 | neural | 0.6462 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
