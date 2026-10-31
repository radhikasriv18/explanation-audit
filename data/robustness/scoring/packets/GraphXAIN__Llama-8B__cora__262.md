# Reference packet: GraphXAIN__Llama-8B__cora__262

- Method: GraphXAIN; configuration: Llama-8B; dataset: cora; target node: 262
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/cora/graphxain_cora_llama_2hop_narratives_full.json` ([262])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Our machine learning model predicts that the target paper "Evolving Representations of Design Cases and Their Use in Creative Design" falls under the category "Case_Based" with a high confidence level of 99.92%. This prediction is strongly supported by the top Bag-of-Words (BOW) features, including words such as "cases," "task," and "creative", all of which are indeed present in the paper. Notably, the absence of certain words like "similar" is also highlighted by the GNNExplainer, indicating their potential relevance to other research areas. The model also takes cues from the direct citation neighbors, particularly papers titled "EMERGENT BEHAVIOUR IN CO-EVOLUTIONARY DESIGN" and "An Overview of Evolutionary Computation", both of which deal with evolutionary computation. These papers are labeled as "Case_Based" or "Genetic_Algorithms", respectively, reinforcing the model's confidence in the prediction. Furthermore, the majority of 2-hop neighbors, whose topics revolve around genetic algorithms and evolutionary computation, further solidify the link between the target paper and the "Case_Based" class. Overall, the accumulation of evidence from these factors convinces our model of the predicted outcome.
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

### Target Paper (node 262):
Title: EVOLVING REPRESENTATIONS OF DESIGN CASES AND THEIR USE IN CREATIVE DESIGN  
Abstract: In case-based design, the adaptation of a design case to new design requirements plays an important role. If it is sufficient to adapt a predefined set of design parameters, the task is easily automated. If,

### Model Prediction:
{
  "Target Node": 262,
  "Predicted Class": "Case_Based",
  "Confidence": 0.9992
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='similar', importance=0.6592, present_in_paper=0
  word='task', importance=0.6508, present_in_paper=1
  word='cases', importance=0.6507, present_in_paper=1
  word='aspect', importance=0.6461, present_in_paper=0
  word='creative', importance=0.6358, present_in_paper=1
  word='definit', importance=0.6335, present_in_paper=0
  word='cbr', importance=0.6275, present_in_paper=1

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 4
Label distribution across all 1-hop neighbors (ground-truth class): Genetic_Algorithms=75.0%, Case_Based=25.0%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 1980 | edge_importance=0.7882 | class=Genetic_Algorithms | Title: An Overview of Evolutionary Computation  
Abstract: Evolutionary computation uses computational models of evolution - ary processes as key elements in the design and implementation of computer-
  Node 266 | edge_importance=0.6566 | class=Case_Based | Title: EMERGENT BEHAVIOUR IN CO-EVOLUTIONARY DESIGN  
Abstract: An important aspect of creative design is the concept of emergence. Though emergence is important, its mechanism is either not well unde
  Node 793 | edge_importance=0.3101 | class=Genetic_Algorithms | Title: A Survey of Evolution Strategies  
Abstract:  
  Node 188 | edge_importance=0.2459 | class=Genetic_Algorithms | Title: Coevolving High-Level Representations  
Abstract: Rules extracted from trained feedforward networks can be used for explanation, validation, and cross-referencing of network output decisions. T

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 1334 | edge_importance=0.8315 | class=Genetic_Algorithms | Title: THE OPTIONS DESIGN EXPLORATION SYSTEM Reference Manual and User Guide Version B2.1  
Abstract: Genetic Algorithms (GAs) have traditionally been used for non-symbolic learning tasks. In this cha
  Node 717 | edge_importance=0.8286 | class=Genetic_Algorithms | Title: Information filtering: Selection mechanisms in learning systems. Machine Learning, 10:113-151, 1993. Generalization as search. Artificial
Abstract: Draft A Brief Introduction to Neural Networks
  Node 42 | edge_importance=0.8284 | class=Genetic_Algorithms | Title: Evolutionary Module Acquisition  
Abstract: A critical issue for users of Markov Chain Monte Carlo (MCMC) methods in applications is how to determine when it is safe to stop sampling and use th
  Node 1249 | edge_importance=0.8271 | class=Genetic_Algorithms | Title: Evolution of Non-Deterministic Incremental Algorithms as a New Approach for Search in State Spaces  
Abstract: Let us call a non-deterministic incremental algorithm one that is able to construc
  Node 1734 | edge_importance=0.8259 | class=Genetic_Algorithms | Title: A Stochastic Search Approach to Grammar Induction  
Abstract: This paper describes a new sampling-based heuristic for tree search named SAGE and presents an analysis of its performance on the p
  Node 1455 | edge_importance=0.8252 | class=Genetic_Algorithms | Title: Self-Adaptation in Genetic Algorithms of external parameters of a GA is seen as a first
Abstract: In this paper a new approach is presented, which transfers a basic idea from Evolution Strategi
  Node 1070 | edge_importance=0.2586 | class=Genetic_Algorithms | Title: Extended Selection Mechanisms in Genetic Algorithms  
Abstract: A Genetic Algorithm Tutorial Darrell Whitley Technical Report CS-93-103 (Revised) November 10, 1993 
  Node 758 | edge_importance=0.2533 | class=Genetic_Algorithms | Title: A COMPRESSION ALGORITHM FOR PROBABILITY TRANSITION MATRICES  
Abstract: This paper describes a compression algorithm for probability transition matrices. The compressed matrix is itself a proba
  Node 2202 | edge_importance=0.2524 | class=Genetic_Algorithms | Title: An Evolutionary Approach to Combinatorial Optimization Problems  
Abstract: The paper reports on the application of genetic algorithms, probabilistic search algorithms based on the model of org
  Node 139 | edge_importance=0.2455 | class=Genetic_Algorithms | Title: Investigating the Generality of Automatically Defined Functions  
Abstract: This paper studies how well the combination of simulated annealing and ADFs solves genetic programming (GP) style pro

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

- ID: 262
- Title: EVOLVING REPRESENTATIONS OF DESIGN CASES AND THEIR USE IN CREATIVE DESIGN
- True class (canonical `y`): **Case_Based**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Case_Based**
- Prediction recorded by this method's pipeline: **Case_Based**

Canonical text (`raw_text`):

~~~~~~text
Title: EVOLVING REPRESENTATIONS OF DESIGN CASES AND THEIR USE IN CREATIVE DESIGN  
Abstract: In case-based design, the adaptation of a design case to new design requirements plays an important role. If it is sufficient to adapt a predefined set of design parameters, the task is easily automated. If, however, more far-reaching, creative changes are required, current systems provide only limited success. This paper describes an approach to creative design adaptation based on the notion of creativity as 'goal oriented shift of focus of a search process'. An evolving representation is used to restructure the search space so that designs similar to the example case lie in the focus of the search. This focus is than used as a starting point to create new designs. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 4 nodes

| node id | true class | title |
|---|---|---|
| 188 | Genetic_Algorithms | Coevolving High-Level Representations |
| 266 | Case_Based | EMERGENT BEHAVIOUR IN CO-EVOLUTIONARY DESIGN |
| 793 | Genetic_Algorithms | A Survey of Evolution Strategies |
| 1980 | Genetic_Algorithms | An Overview of Evolutionary Computation |

### 2-hop (shortest distance exactly 2): 38 nodes

| node id | true class | title |
|---|---|---|
| 42 | Genetic_Algorithms | Evolutionary Module Acquisition |
| 120 | Genetic_Algorithms | Genetic Programming Exploratory Power and the Discovery of Functions |
| 129 | Genetic_Algorithms | Evolving Networks: Using the Genetic Algorithm with Connectionist Learning |
| 139 | Genetic_Algorithms | Investigating the Generality of Automatically Defined Functions |
| 141 | Genetic_Algorithms | Hierarchical Self-Organization in Genetic Programming |
| 144 | Neural_Networks | The Observers Paradox: Apparent Computational Complexity in Physical Systems |
| 163 | Genetic_Algorithms | 4 Implementing Application Specific Routines  Genetic algorithms in search, optimization, and machine learning. Reading, MA: Addison-Wesley. |
| 189 | Genetic_Algorithms | An Evolutionary Algorithm that Constructs Recurrent Neural Networks |
| 380 | Genetic_Algorithms | Fitness Landscapes and Difficulty in Genetic Programming |
| 415 | Genetic_Algorithms | Competitive Environments Evolve Better Solutions for Complex Tasks |
| 523 | Genetic_Algorithms | Some studies in machine learning using the game of checkers. IBM Journal, 3(3):211-229, 1959. Some |
| 717 | Genetic_Algorithms | Information filtering: Selection mechanisms in learning systems. Machine Learning, 10:113-151, 1993. Generalization as search. Artificial |
| 721 | Genetic_Algorithms | Learning Representations for Evolutionary Computation an example from the domain of two-dimensional shape designs. In |
| 755 | Genetic_Algorithms | of a simulator for evolving morphology are: Universal the simulator should cover an infinite gen |
| 757 | Genetic_Algorithms | Evolving Self-Supporting Structures Page 18 References Evolution of Visual Control Systems for Robots. To appear |
| 758 | Genetic_Algorithms | A COMPRESSION ALGORITHM FOR PROBABILITY TRANSITION MATRICES |
| 856 | Genetic_Algorithms | Hierarchical priors and mixture models, with application in regression and density estimation |
| 943 | Genetic_Algorithms | Crossover or Mutation? |
| 959 | Genetic_Algorithms | Numerical techniques for efficient sonar bearing and range searching in the near field using genetic algorithms |
| 1069 | Genetic_Algorithms | Extended Selection Mechanisms in Genetic Algorithms |
| 1070 | Genetic_Algorithms | Extended Selection Mechanisms in Genetic Algorithms |
| 1110 | Genetic_Algorithms | On The State of Evolutionary Computation |
| 1127 | Genetic_Algorithms | Recombination Operator, its Correlation to the Fitness Landscape and Search Performance |
| 1139 | Genetic_Algorithms | Optimal Mutation Rates in Genetic Search |
| 1205 | Genetic_Algorithms | The Role of Development in Genetic Algorithms |
| 1249 | Genetic_Algorithms | Evolution of Non-Deterministic Incremental Algorithms as a New Approach for Search in State Spaces |
| 1330 | Genetic_Algorithms | Evolving Cellular Automata with Genetic Algorithms: A Review of Recent Work |
| 1333 | Genetic_Algorithms | Using Genetic Algorithms for Supervised Concept Learning |
| 1334 | Genetic_Algorithms | THE OPTIONS DESIGN EXPLORATION SYSTEM Reference Manual and User Guide Version B2.1 |
| 1380 | Genetic_Algorithms | Evaluating Evolutionary Algorithms |
| 1455 | Genetic_Algorithms | Self-Adaptation in Genetic Algorithms of external parameters of a GA is seen as a first |
| 1467 | Genetic_Algorithms | Adaptive Strategy Selection for Concept Learning |
| 1691 | Genetic_Algorithms | Evolutionary Algorithms: Some Very Old Strategies for Optimization and Adaptation |
| 1694 | Genetic_Algorithms | Strategy Adaptation by Competing Subpopulations |
| 1715 | Genetic_Algorithms | A Sampling-Based Heuristic for Tree Search Applied to Grammar Induction |
| 1734 | Genetic_Algorithms | A Stochastic Search Approach to Grammar Induction |
| 2202 | Genetic_Algorithms | An Evolutionary Approach to Combinatorial Optimization Problems |
| 2457 | Neural_Networks | In Proceedings of the 1997 Sian Kaan International Workshop on Neural Networks and Neurocontrol. Real-Valued |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=262).
Recorded prediction: `{"Target Node": 262, "Predicted Class": "Case_Based", "Confidence": 0.9992}`
Recorded graph stats: `{"total_1hop_degree": 4, "neighbor_label_ratio": {"Genetic_Algorithms": 0.75, "Case_Based": 0.25}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | similar | 0.6592 | 0 |
| 2 | task | 0.6508 | 1 |
| 3 | cases | 0.6507 | 1 |
| 4 | aspect | 0.6461 | 0 |
| 5 | creative | 0.6358 | 1 |
| 6 | definit | 0.6335 | 0 |
| 7 | cbr | 0.6275 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
