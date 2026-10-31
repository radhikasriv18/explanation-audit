# Reference packet: GraphXAIN__GPT-4o__cora__1959

- Method: GraphXAIN; configuration: GPT-4o; dataset: cora; target node: 1959
- Explanation source: `./robustness_2026-10-30/graphxain_gpt4o/cora/1959.json` (narrative)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model predicted that the paper "Evolution-based Discovery of Hierarchical Behaviors" belongs to the "Genetic_Algorithms" category with high confidence, at 99.99%. This prediction is primarily supported by the presence of specific terms in the paper and its citation network. Notably, important words like "representations" and "discovery" are present in the paper and strongly associated with topics in genetic algorithms, suggesting that the paper's content aligns with procedural and exploratory themes common in genetic research. Additionally, the direct citation connections with papers like "Genetic Programming Exploratory Power and the Discovery of Functions" and "An Experimental Analysis of Schema Creation, Propagation and Disruption in Genetic Programming", both of which fall within the genetic algorithms sphere, further reinforce the model's prediction. These neighbors discuss hierarchical genetic programming and schemata, central concepts in genetic algorithms, thereby implying a thematic connection. Furthermore, 2-hop neighbors predominantly belong to the genetic algorithms category, introducing topics such as robust feature selection and schema theories, which are core to the field, adding layers of indirect confirmation to the prediction. Overall, both the textual content of the paper and its position within a network rich in genetic algorithms literature solidified the model's classification decision.
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

### Target Paper (node 1959):
Title: Evolution-based Discovery of Hierarchical Behaviors  
Abstract: Procedural representations of control policies have two advantages when facing the scale-up problem in learning tasks. First they are implicit, with potential for inductive generalization over a very large set of situations. Seco

### Model Prediction:
{
  "Target Node": 1959,
  "Predicted Class": "Genetic_Algorithms",
  "Confidence": 0.9999
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='representations', importance=0.6762, present_in_paper=1
  word='field', importance=0.649, present_in_paper=0
  word='introduct', importance=0.6452, present_in_paper=0
  word='discovery', importance=0.6446, present_in_paper=1
  word='experiment', importance=0.6397, present_in_paper=0
  word='several', importance=0.6388, present_in_paper=1
  word='modularization', importance=0.6322, present_in_paper=1

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 3
Label distribution across all 1-hop neighbors (ground-truth class): Genetic_Algorithms=66.7%, Theory=33.3%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 120 | edge_importance=0.7623 | class=Genetic_Algorithms | Title: Genetic Programming Exploratory Power and the Discovery of Functions  
Abstract: Hierarchical genetic programming (HGP) approaches rely on the discovery, modification, and use of new functions 
  Node 2259 | edge_importance=0.5912 | class=Genetic_Algorithms | Title: An Experimental Analysis of Schema Creation, Propagation and Disruption in Genetic Programming  
Abstract: In this paper we first review the main results in the theory of schemata in Genetic Pr
  Node 177 | edge_importance=0.5886 | class=Theory | Title: Evaluation and Selection of Biases in Machine Learning  
Abstract: In this introduction, we define the term bias as it is used in machine learning systems. We motivate the importance of automat

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 2192 | edge_importance=0.8006 | class=Genetic_Algorithms | Title: #1 Robust Feature Selection Algorithms  
Abstract: Selecting a set of features which is optimal for a given task is a problem which plays an important role in a wide variety of contexts includi
  Node 2175 | edge_importance=0.7881 | class=Genetic_Algorithms | Title: The Troubling Aspects of a Building Block Hypothesis for Genetic Programming  
Abstract: In this paper we carefully formulate a Schema Theorem for Genetic Programming (GP) using a schema defini
  Node 965 | edge_importance=0.785 | class=Genetic_Algorithms | Title: Improving Tactical Plans with Genetic Algorithms  
Abstract:  
  Node 1257 | edge_importance=0.7723 | class=Genetic_Algorithms | Title: The Schema Theorem and Price's Theorem  
Abstract: Holland's Schema Theorem is widely taken to be the foundation for explanations of the power of genetic algorithms (GAs). Yet some dissent has 
  Node 1184 | edge_importance=0.7388 | class=Genetic_Algorithms | Title: Causality in Genetic Programming  
Abstract: Causality relates changes in the structure of an object with the effects of such changes, that is changes in the properties or behavior of the objec
  Node 2271 | edge_importance=0.7196 | class=Genetic_Algorithms | Title: How Fitness Structure Affects Subsolution Acquisition in Genetic Programming  
Abstract: We define fitness structure in genetic programming to be the mapping between the subprograms of a progra
  Node 163 | edge_importance=0.7125 | class=Genetic_Algorithms | Title: 4 Implementing Application Specific Routines  Genetic algorithms in search, optimization, and machine learning. Reading, MA: Addison-Wesley.  
Abstract: To implement a specific application, you
  Node 2261 | edge_importance=0.7061 | class=Genetic_Algorithms | Title: Genetic Programming with One-Point Crossover and Point Mutation  
Abstract: Technical Report: CSRP-97-13 April 1997 Abstract In recent theoretical and experimental work on schemata in genetic p
  Node 635 | edge_importance=0.2339 | class=Theory | Title: Learning Boolean Concepts in the Presence of Many Irrelevant Features  
Abstract: In this paper, we address the problem of case-based learning in the presence of irrelevant features. We review 
  Node 911 | edge_importance=0.2312 | class=Theory | Title: Utilizing Prior Concepts for Learning  
Abstract: The inductive learning problem consists of learning a concept given examples and non-examples of the concept. To perform this learning task, in

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

- ID: 1959
- Title: Evolution-based Discovery of Hierarchical Behaviors
- True class (canonical `y`): **Genetic_Algorithms**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Genetic_Algorithms**
- Prediction recorded by this method's pipeline: **Genetic_Algorithms**

Canonical text (`raw_text`):

~~~~~~text
Title: Evolution-based Discovery of Hierarchical Behaviors  
Abstract: Procedural representations of control policies have two advantages when facing the scale-up problem in learning tasks. First they are implicit, with potential for inductive generalization over a very large set of situations. Second they facilitate modularization. In this paper we compare several randomized algorithms for learning modular procedural representations. The main algorithm, called Adaptive Representation through Learning (ARL) is a genetic programming extension that relies on the discovery of subroutines. ARL is suitable for learning hierarchies of subroutines and for constructing policies to complex tasks. ARL was successfully tested on a typical reinforcement learning problem of controlling an agent in a dynamic and nondeterministic environment where the discovered subroutines correspond to agent behaviors. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 3 nodes

| node id | true class | title |
|---|---|---|
| 120 | Genetic_Algorithms | Genetic Programming Exploratory Power and the Discovery of Functions |
| 177 | Theory | Evaluation and Selection of Biases in Machine Learning |
| 2259 | Genetic_Algorithms | An Experimental Analysis of Schema Creation, Propagation and Disruption in Genetic Programming |

### 2-hop (shortest distance exactly 2): 14 nodes

| node id | true class | title |
|---|---|---|
| 163 | Genetic_Algorithms | 4 Implementing Application Specific Routines  Genetic algorithms in search, optimization, and machine learning. Reading, MA: Addison-Wesley. |
| 188 | Genetic_Algorithms | Coevolving High-Level Representations |
| 430 | Theory | Irrelevant Features and the Subset Selection Problem |
| 635 | Theory | Learning Boolean Concepts in the Presence of Many Irrelevant Features |
| 885 | Theory | Model selection using measure functions |
| 911 | Theory | Utilizing Prior Concepts for Learning |
| 965 | Genetic_Algorithms | Improving Tactical Plans with Genetic Algorithms |
| 1184 | Genetic_Algorithms | Causality in Genetic Programming |
| 1257 | Genetic_Algorithms | The Schema Theorem and Price's Theorem |
| 1489 | Rule_Learning | Dlab: A Declarative Language Bias Formalism |
| 2175 | Genetic_Algorithms | The Troubling Aspects of a Building Block Hypothesis for Genetic Programming |
| 2192 | Genetic_Algorithms | #1 Robust Feature Selection Algorithms |
| 2261 | Genetic_Algorithms | Genetic Programming with One-Point Crossover and Point Mutation |
| 2271 | Genetic_Algorithms | How Fitness Structure Affects Subsolution Acquisition in Genetic Programming |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=1959).
Recorded prediction: `{"Target Node": 1959, "Predicted Class": "Genetic_Algorithms", "Confidence": 0.9999}`
Recorded graph stats: `{"total_1hop_degree": 3, "neighbor_label_ratio": {"Genetic_Algorithms": 0.667, "Theory": 0.333}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | representations | 0.6762 | 1 |
| 2 | field | 0.649 | 0 |
| 3 | introduct | 0.6452 | 0 |
| 4 | discovery | 0.6446 | 1 |
| 5 | experiment | 0.6397 | 0 |
| 6 | several | 0.6388 | 1 |
| 7 | modularization | 0.6322 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
