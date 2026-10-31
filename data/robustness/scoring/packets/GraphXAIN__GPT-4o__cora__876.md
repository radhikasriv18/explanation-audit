# Reference packet: GraphXAIN__GPT-4o__cora__876

- Method: GraphXAIN; configuration: GPT-4o; dataset: cora; target node: 876
- Explanation source: `./robustness_2026-10-30/graphxain_gpt4o/cora/876.json` (narrative)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model predicted the target paper (node 876) belongs to the "Theory" class with absolute confidence. Although none of the top binary bag-of-words features such as 'best', 'measur', and 'infer' were present in the paper, their high importance suggests they are commonly associated with theoretical research. The direct citation neighbors all share a focus on theoretical topics: Node 453 deals with expert advice and multiplicative algorithms, Node 1025 discusses decision tree pruning, and Node 1269 looks into context-sensitive learning. These neighbors, each classified under the "Theory" domain, heavily influenced the prediction by illustrating a consistent theme of theoretical exploration in decision-making and learning algorithms. The influence extends through 2-hop neighbors, like Node 574 which explores learnability and belief revision, further reinforcing the theoretical inclination. The cumulative effect of these connections suggests that the paper's central theme aligns with common research concerns within the theoretical domain, guiding the model toward this confident classification.
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

### Target Paper (node 876):
Title: Using and combining predictors that specialize  
Abstract: We study online learning algorithms that predict by combining the predictions of several subordinate prediction algorithms, sometimes called experts. These simple algorithms belong to the multiplicative weights family of algorithms. T

### Model Prediction:
{
  "Target Node": 876,
  "Predicted Class": "Theory",
  "Confidence": 1.0
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='best', importance=0.6492, present_in_paper=0
  word='measur', importance=0.6418, present_in_paper=0
  word='involv', importance=0.6399, present_in_paper=0
  word='compar', importance=0.6289, present_in_paper=0
  word='expect', importance=0.6279, present_in_paper=0
  word='infer', importance=0.6255, present_in_paper=0
  word='assumpt', importance=0.6239, present_in_paper=0

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 4
Label distribution across all 1-hop neighbors (ground-truth class): Theory=100.0%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 453 | edge_importance=0.8105 | class=Theory | Title: How to Use Expert Advice (Extended Abstract)  
Abstract: We analyze algorithms that predict a binary value by combining the predictions of several prediction strategies, called experts. Our ana
  Node 1025 | edge_importance=0.7765 | class=Theory | Title: Machine Learning 27(1):51-68, 1997. Predicting nearly as well as the best pruning of a decision tree  
Abstract: Many algorithms for inferring a decision tree from data involve a two-phase proc
  Node 1269 | edge_importance=0.5425 | class=Theory | Title: Context-sensitive learning methods for text categorization  
Abstract: Two recently implemented machine learning algorithms, RIPPER and sleeping experts for phrases, are evaluated on a number o
  Node 1006 | edge_importance=0.5205 | class=Theory | Title: Learning Probabilistic Automata with Variable Memory Length  
Abstract: We propose and analyze a distribution learning algorithm for variable memory length Markov processes. These processes can

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 574 | edge_importance=0.8317 | class=Theory | Title: On the Learnability of Discrete Distributions (extended abstract)  
Abstract: We describe a model of iterated belief revision that extends the AGM theory of revision to account for the effect o
  Node 2455 | edge_importance=0.8208 | class=Theory | Title: Learning From a Population of Hypotheses  
Abstract: We introduce a new formal model in which a learning algorithm must combine a collection of potentially poor but statistically independent hy
  Node 2354 | edge_importance=0.8111 | class=Theory | Title: The Power of Team Exploration: Two Robots Can Learn Unlabeled Directed Graphs  
Abstract: We show that two cooperating robots can learn exactly any strongly-connected directed graph with n indi
  Node 2034 | edge_importance=0.8107 | class=Probabilistic_Methods | Title: Update rules for parameter estimation in Bayesian networks  
Abstract: This paper re-examines the problem of parameter estimation in Bayesian networks with missing values and hidden variables f
  Node 2059 | edge_importance=0.8095 | class=Theory | Title: Challenges in Evolving Controllers for Physical Robots  
Abstract: General convergence results for linear discriminant updates Abstract The problem of learning linear discriminant concepts can 
  Node 1358 | edge_importance=0.8017 | class=Theory | Title: On the Complexity of Function Learning  
Abstract: The majority of results in computational learning theory are concerned with concept learning, i.e. with the special case of function learning 
  Node 514 | edge_importance=0.7985 | class=Theory | Title: Gambling in a rigged casino: The adversarial multi-armed bandit problem  
Abstract: In the multi-armed bandit problem, a gambler must decide which arm of K non-identical slot machines to play i
  Node 1566 | edge_importance=0.7979 | class=Theory | Title: Worst-case Quadratic Loss Bounds for Prediction Using Linear Functions and Gradient Descent  
Abstract: In this paper we study the performance of gradient descent when applied to the problem of
  Node 569 | edge_importance=0.7977 | class=Theory | Title: A decision-theoretic generalization of on-line learning and an application to boosting how the weight-update rule
Abstract: We consider the problem of dynamically apportioning resources among a
  Node 9 | edge_importance=0.7966 | class=Theory | Title: Online Learning versus O*ine Learning  
Abstract: We present an off-line variant of the mistake-bound model of learning. Just like in the well studied on-line model, a learner in the offline mo

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

- ID: 876
- Title: Using and combining predictors that specialize
- True class (canonical `y`): **Theory**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Theory**
- Prediction recorded by this method's pipeline: **Theory**

Canonical text (`raw_text`):

~~~~~~text
Title: Using and combining predictors that specialize  
Abstract: We study online learning algorithms that predict by combining the predictions of several subordinate prediction algorithms, sometimes called experts. These simple algorithms belong to the multiplicative weights family of algorithms. The performance of these algorithms degrades only logarithmically with the number of experts, making them particularly useful in applications where the number of experts is very large. However, in applications such as text categorization, it is often natural for some of the experts to abstain from making predictions on some of the instances. We show how to transform algorithms that assume that all experts are always awake to algorithms that do not require this assumption. We also show how to derive corresponding loss bounds. Our method is very general, and can be applied to a large family of online learning algorithms. We also give applications to various prediction models including decision graphs and switching experts. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 4 nodes

| node id | true class | title |
|---|---|---|
| 453 | Theory | How to Use Expert Advice (Extended Abstract) |
| 1006 | Theory | Learning Probabilistic Automata with Variable Memory Length |
| 1025 | Theory | Machine Learning 27(1):51-68, 1997. Predicting nearly as well as the best pruning of a decision tree |
| 1269 | Theory | Context-sensitive learning methods for text categorization |

### 2-hop (shortest distance exactly 2): 33 nodes

| node id | true class | title |
|---|---|---|
| 9 | Theory | Online Learning versus O*ine Learning |
| 242 | Theory | Learning Markov chains with variable memory length from noisy output |
| 418 | Theory | Heterogeneous Uncertainty Sampling for Supervised Learning |
| 472 | Reinforcement_Learning | Category: Control, Navigation and Planning. Key words: Reinforcement learning, Exploration, Hidden state. Prefer oral presentation. |
| 514 | Theory | Gambling in a rigged casino: The adversarial multi-armed bandit problem |
| 549 | Theory | Efficient Distribution-free Learning of Probabilistic Concepts |
| 569 | Theory | A decision-theoretic generalization of on-line learning and an application to boosting how the weight-update rule |
| 574 | Theory | On the Learnability of Discrete Distributions (extended abstract) |
| 591 | Theory | Toward Efficient Agnostic Learning |
| 650 | Reinforcement_Learning | Learning to Use Selective Attention and Short-Term Memory in Sequential Tasks |
| 706 | Theory | Large Margin Classification Using the Perceptron Algorithm |
| 1124 | Theory | ON-LINE LEARNING OF LINEAR FUNCTIONS |
| 1238 | Theory | On Pruning and Averaging Decision Trees |
| 1260 | Theory | Transferring and Retraining Learned Information Filters |
| 1290 | Theory | A THEORY OF LEARNING CLASSIFICATION RULES |
| 1312 | Rule_Learning | Learning Trees and Rules with Set-valued Features |
| 1358 | Theory | On the Complexity of Function Learning |
| 1388 | Theory | A Fast, Bottom-Up Decision Tree Pruning Algorithm with Near-Optimal Generalization |
| 1449 | Theory | Adaptive Mixtures of Probabilistic Transducers |
| 1566 | Theory | Worst-case Quadratic Loss Bounds for Prediction Using Linear Functions and Gradient Descent |
| 1661 | Theory | Simulating Access to Hidden Information while Learning |
| 1712 | Theory | An Efficient Extension to Mixture Techniques for Prediction and Decision Trees |
| 2034 | Probabilistic_Methods | Update rules for parameter estimation in Bayesian networks |
| 2040 | Theory | On the Learnability and Usage of Acyclic Probabilistic Finite Automata |
| 2059 | Theory | Challenges in Evolving Controllers for Physical Robots |
| 2092 | Theory | Universal Portfolios With and Without Transaction Costs |
| 2098 | Theory | Predicting a binary sequence almost as well as the optimal biased coin |
| 2099 | Theory | Game Theory, On-line Prediction and Boosting |
| 2156 | Theory | WORST CASE PREDICTION OVER SEQUENCES UNDER LOG LOSS |
| 2354 | Theory | The Power of Team Exploration: Two Robots Can Learn Unlabeled Directed Graphs |
| 2360 | Theory | Efficient Learning of Typical Finite Automata from Random Walks (Extended Abstract) |
| 2455 | Theory | Learning From a Population of Hypotheses |
| 2618 | Theory | Mistake-Driven Learning in Text Categorization |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=876).
Recorded prediction: `{"Target Node": 876, "Predicted Class": "Theory", "Confidence": 1.0}`
Recorded graph stats: `{"total_1hop_degree": 4, "neighbor_label_ratio": {"Theory": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | best | 0.6492 | 0 |
| 2 | measur | 0.6418 | 0 |
| 3 | involv | 0.6399 | 0 |
| 4 | compar | 0.6289 | 0 |
| 5 | expect | 0.6279 | 0 |
| 6 | infer | 0.6255 | 0 |
| 7 | assumpt | 0.6239 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
