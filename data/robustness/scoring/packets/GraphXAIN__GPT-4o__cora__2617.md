# Reference packet: GraphXAIN__GPT-4o__cora__2617

- Method: GraphXAIN; configuration: GPT-4o; dataset: cora; target node: 2617
- Explanation source: `./robustness_2026-10-30/graphxain_gpt4o/cora/2617.json` (narrative)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model predicted that the target paper, "Predicting Ordinal Classes in ILP," falls into the "Rule_Learning" category with high confidence of 0.9944. Among the top bag-of-words features, only "ilp" is present in the paper, suggesting a link to Inductive Logic Programming, which is integral to rule learning. While other influential words like "shown," "heurist," and "definit" are absent, their relevance indicates a common context within the rule learning domain. Furthermore, the paper's direct citation network is dominated by works in rule learning, such as "Inverse entailment and Progol," highlighting key methodologies and theories in the field. Papers like "Fossil: A Robust Relational Learner" and "Quinlan, 1990" also focus on logic and learning from relations, directly aligning with the target's subject. Additionally, the second-tier citation network predominantly consists of rule learning research, providing further thematic support. This interconnectedness of papers, both directly and indirectly cited, reinforces the target paper’s alignment with rule learning, explaining the strong predictive confidence.
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

### Target Paper (node 2617):
Title: Predicting Ordinal Classes in ILP  
Abstract: This paper is devoted to the problem of learning to predict ordinal (i.e., ordered discrete) classes in an ILP setting. We start with a relational regression algorithm named SRT (Structural Regression Trees) and study various ways of transforming 

### Model Prediction:
{
  "Target Node": 2617,
  "Predicted Class": "Rule_Learning",
  "Confidence": 0.9944
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='shown', importance=0.6845, present_in_paper=0
  word='heurist', importance=0.6703, present_in_paper=0
  word='definit', importance=0.669, present_in_paper=0
  word='amplif', importance=0.6631, present_in_paper=0
  word='ilp', importance=0.662, present_in_paper=1
  word='enhanc', importance=0.6597, present_in_paper=0
  word='invers', importance=0.6569, present_in_paper=0

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 5
Label distribution across all 1-hop neighbors (ground-truth class): Rule_Learning=60.0%, Genetic_Algorithms=20.0%, Case_Based=20.0%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 1428 | edge_importance=0.8175 | class=Rule_Learning | Title: Inverse entailment and Progol  
Abstract: This paper firstly provides a re-appraisal of the development of techniques for inverting deduction, secondly introduces Mode-Directed Inverse Entailme
  Node 1275 | edge_importance=0.711 | class=Rule_Learning | Title: Fossil: A Robust Relational Learner  
Abstract: The research reported in this paper describes Fossil, an ILP system that uses a search heuristic based on statistical correlation. This algorithm
  Node 344 | edge_importance=0.6484 | class=Rule_Learning | Title: Quinlan, 1990 J.R. Quinlan. Learning logical definitions from relations. Machine Learning, First-order theory revision. In
Abstract: We describe a ranked-model semantics for if-then rules admit
  Node 2091 | edge_importance=0.3726 | class=Case_Based | Title: The Utility of Knowledge in Inductive Learning  Running Head: Knowledge in Inductive Learning  
Abstract: This paper investigates learning in a lifelong context. Lifelong learning addresses sit
  Node 228 | edge_importance=0.3531 | class=Genetic_Algorithms | Title: Cost-Sensitive Classification: Empirical Evaluation of a Hybrid Genetic Decision Tree Induction Algorithm  
Abstract: This paper introduces ICET, a new algorithm for costsensitive classificatio

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 1260 | edge_importance=0.8327 | class=Theory | Title: Transferring and Retraining Learned Information Filters  
Abstract: Any system that learns how to filter documents will suffer poor performance during an initial training phase. One way of addr
  Node 521 | edge_importance=0.8209 | class=Rule_Learning | Title: Covering vs. Divide-and-Conquer for Top-Down Induction of Logic Programs  
Abstract: covering has been formalized and used extensively. In this work, the divide-and-conquer technique is formali
  Node 1881 | edge_importance=0.8166 | class=Rule_Learning | Title: Integrity Constraints in ILP using a Monte Carlo approach  
Abstract: Many state-of-the-art ILP systems require large numbers of negative examples to avoid overgeneralization. This is a conside
  Node 2493 | edge_importance=0.8151 | class=Rule_Learning | Title: Relational Knowledge Discovery in Databases  
Abstract: In this paper, we indicate some possible applications of ILP or similar techniques in the knowledge discovery field, and then discuss sev
  Node 2229 | edge_importance=0.8127 | class=Rule_Learning | Title: Bottom-up induction of logic programs with more than one recursive clause  
Abstract: In this paper we present a bottom-up algorithm called MRI to induce logic programs from their examples. Thi
  Node 335 | edge_importance=0.8093 | class=Rule_Learning | Title: Incremental Reduced Error Pruning  
Abstract: This paper outlines some problems that may occur with Reduced Error Pruning in relational learning algorithms, most notably efficiency. Thereafter 
  Node 2426 | edge_importance=0.8062 | class=Rule_Learning | Title: Inductive Constraint Logic  
Abstract: A novel approach to learning first order logic formulae from positive and negative examples is presented. Whereas present inductive logic programming syst
  Node 2609 | edge_importance=0.8058 | class=Rule_Learning | Title: ILP with Noise and Fixed Example Size: A Bayesian Approach  
Abstract: Current inductive logic programming systems are limited in their handling of noise, as they employ a greedy covering appro
  Node 426 | edge_importance=0.7751 | class=Rule_Learning | Title: Rule Induction with CN2: Some Recent Improvements  
Abstract: The CN2 algorithm induces an ordered list of classification rules from examples using entropy as its search heuristic. In this shor
  Node 2539 | edge_importance=0.7583 | class=Rule_Learning | Title: Mining for Causes of Cancer: Machine Learning Experiments at Various Levels of Detail  
Abstract: This paper presents first results of an interdisciplinary project in scientific data mining. We

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

- ID: 2617
- Title: Predicting Ordinal Classes in ILP
- True class (canonical `y`): **Rule_Learning**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Rule_Learning**
- Prediction recorded by this method's pipeline: **Rule_Learning**

Canonical text (`raw_text`):

~~~~~~text
Title: Predicting Ordinal Classes in ILP  
Abstract: This paper is devoted to the problem of learning to predict ordinal (i.e., ordered discrete) classes in an ILP setting. We start with a relational regression algorithm named SRT (Structural Regression Trees) and study various ways of transforming it into a first-order learner for ordinal classification tasks. Combinations of these algorithm variants with several data preprocessing methods are compared on two ILP benchmark data sets to verify the relative strengths and weaknesses of the strategies and to study the trade-off between optimal categorical classification accuracy (hit rate) and minimum distance-based error. Preliminary results indicate that this is a promising avenue towards algorithms that combine aspects of classification and regression in relational learning.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 5 nodes

| node id | true class | title |
|---|---|---|
| 228 | Genetic_Algorithms | Cost-Sensitive Classification: Empirical Evaluation of a Hybrid Genetic Decision Tree Induction Algorithm |
| 344 | Rule_Learning | Quinlan, 1990 J.R. Quinlan. Learning logical definitions from relations. Machine Learning, First-order theory revision. In |
| 1275 | Rule_Learning | Fossil: A Robust Relational Learner |
| 1428 | Rule_Learning | Inverse entailment and Progol |
| 2091 | Case_Based | The Utility of Knowledge in Inductive Learning  Running Head: Knowledge in Inductive Learning |

### 2-hop (shortest distance exactly 2): 50 nodes

| node id | true class | title |
|---|---|---|
| 1 | Rule_Learning | Applications of machine learning: a medical follow up study |
| 52 | Theory | Theory Revision in Fault Hierarchies |
| 119 | Rule_Learning | Cost-sensitive feature reduction applied to a hybrid genetic algorithm |
| 259 | Case_Based | How to Get a Free Lunch: A Simple Cost Model for Machine Learning Applications |
| 303 | Case_Based | Relating Relational Learning Algorithms |
| 316 | Rule_Learning | Cortical Functionality Emergence:  Self-Organization of Complex Structures: From Individual to Collective Dynamics, |
| 323 | Theory | Learning Active Classifiers |
| 335 | Rule_Learning | Incremental Reduced Error Pruning |
| 348 | Rule_Learning | First Order Regression: Applications in Real-World Domains |
| 378 | Theory | Mingers, 1989 J. Mingers. An empirical comparison of pruning methods for decision tree induction. Machine |
| 426 | Rule_Learning | Rule Induction with CN2: Some Recent Improvements |
| 521 | Rule_Learning | Covering vs. Divide-and-Conquer for Top-Down Induction of Logic Programs |
| 585 | Rule_Learning | An investigation of noise-tolerant relational concept learning algorithms |
| 675 | Rule_Learning | Combining FOIL and EBG to Speed-up Logic Programs |
| 900 | Genetic_Algorithms | Evolution, Learning, and Instinct: 100 Years of the Baldwin Effect Using Learning to Facilitate the |
| 963 | Rule_Learning | Cooperation of Data-driven and Model-based Induction Methods for Relational Learning |
| 1007 | Rule_Learning | Applications of a logical discovery engine |
| 1234 | Rule_Learning | Concept Learning and the Problem of Small |
| 1244 | Rule_Learning | Producing More Comprehensible Models While Retaining Their Performance |
| 1260 | Theory | Transferring and Retraining Learned Information Filters |
| 1267 | Theory | Estimating the Accuracy of Learned Concepts |
| 1312 | Rule_Learning | Learning Trees and Rules with Set-valued Features |
| 1442 | Rule_Learning | Learning Goal-Decomposition Rules using Exercises |
| 1445 | Rule_Learning | Theory-guided Empirical Speedup Learning of Goal Decomposition Rules |
| 1539 | Rule_Learning | Finding new rules for incomplete theories: Explicit biases for induction with contextual information. In Proceedings |
| 1601 | Neural_Networks | Learning the Past Tense of English Verbs: The Symbolic Pattern Associator vs. Connectionist Models |
| 1622 | Rule_Learning | Stochastic Propositionalization of Non-Determinate Background Knowledge |
| 1627 | Rule_Learning | Inductive Learning of Characteristic Concept Descriptions from Small Sets of Classified Examples |
| 1671 | Theory | From: Computational Learning Theory and Natural Systems, Chapter 18, "Cross-validation and Modal Theories", Cross-Validation and |
| 1692 | Theory | Boosting Trees for Cost-Sensitive Classifications |
| 1881 | Rule_Learning | Integrity Constraints in ILP using a Monte Carlo approach |
| 1944 | Rule_Learning | Knowledge Acquisition with a Knowledge-Intensive Machine Learning System |
| 2032 | Rule_Learning | Learning Action-oriented Perceptual Features for Robot Navigation |
| 2079 | Rule_Learning | Extraction of Meta-Knowledge to Restrict the Hypothesis Space for ILP Systems incorporating them in FOIL. |
| 2171 | Rule_Learning | K unstliche Intelligenz Grdt: Enhancing Model-Based Learning for Its Application in Robot Navigation |
| 2215 | Case_Based | Learning Approximate Control Rules Of High Utility |
| 2229 | Rule_Learning | Bottom-up induction of logic programs with more than one recursive clause |
| 2290 | Rule_Learning | A Comparison of Pruning Methods for Relational Concept Learning |
| 2291 | Rule_Learning | Top-Down Pruning in Relational Learning |
| 2329 | Theory | Programming Research Group A LEARNABILITY MODEL FOR UNIVERSAL REPRESENTATIONS |
| 2339 | Rule_Learning | An intelligent search method using Inductive Logic Programming |
| 2424 | Rule_Learning | Which Hypotheses Can Be Found with Inverse Entailment? -Extended Abstract |
| 2426 | Rule_Learning | Inductive Constraint Logic |
| 2438 | Neural_Networks | Integrating Initialization Bias and Search Bias in Neural Network Learning |
| 2441 | Rule_Learning | Distance Induction in First Order Logic used for classification via a k-nearest-neighbor process. Experiments on |
| 2465 | Case_Based | A systematic description of greedy optimisation algorithms for cost sensitive generalisation |
| 2493 | Rule_Learning | Relational Knowledge Discovery in Databases |
| 2539 | Rule_Learning | Mining for Causes of Cancer: Machine Learning Experiments at Various Levels of Detail |
| 2589 | Rule_Learning | Pac-Learning Recursive Logic Programs: Efficient Algorithms |
| 2609 | Rule_Learning | ILP with Noise and Fixed Example Size: A Bayesian Approach |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=2617).
Recorded prediction: `{"Target Node": 2617, "Predicted Class": "Rule_Learning", "Confidence": 0.9944}`
Recorded graph stats: `{"total_1hop_degree": 5, "neighbor_label_ratio": {"Rule_Learning": 0.6, "Genetic_Algorithms": 0.2, "Case_Based": 0.2}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | shown | 0.6845 | 0 |
| 2 | heurist | 0.6703 | 0 |
| 3 | definit | 0.669 | 0 |
| 4 | amplif | 0.6631 | 0 |
| 5 | ilp | 0.662 | 1 |
| 6 | enhanc | 0.6597 | 0 |
| 7 | invers | 0.6569 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
