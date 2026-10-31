# Reference packet: GraphXAIN__Llama-8B__cora__2334

- Method: GraphXAIN; configuration: Llama-8B; dataset: cora; target node: 2334
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/cora/graphxain_cora_llama_2hop_narratives_full.json` ([2334])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on our analysis, the model confidently predicted the target paper, "New Methods for Competitive Coevolution," to belong to the category "Genetic_Algorithms" with perfect certainty. This prediction was primarily driven by the top BoW features, including absence of 'genet' despite its relatively high importance, presence of strongly associated terms such as 'fitness', 'coevolution', and 'competitive'. Furthermore, the model strongly linked this paper to highly influential direct citation neighbors, several of whom share similar titles like "Dynamics of Co-evolutionary Learning" and "Small Populations over Many Generations can beat Large Populations over Few Generations". These 1-hop neighbors were overwhelmingly classified as belonging to the same category, solidifying the model's prediction. Additionally, some of the more distant citations reinforced this trend, featuring more papers focused on genetic programming and evolutionary algorithms. By combining these patterns, the model inferred that the core concepts explored within the paper align closely with existing work in genetic algorithms, thereby generating its prediction. Overall, the model effectively utilized both local graph structure and the content features to reach a precise conclusion.
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

### Target Paper (node 2334):
Title: New Methods for Competitive Coevolution  
Abstract: We consider "competitive coevolution," in which fitness is based on direct competition among individuals selected from two independently evolving populations of "hosts" and "parasites." Competitive coevolution can lead to an "arms race," in 

### Model Prediction:
{
  "Target Node": 2334,
  "Predicted Class": "Genetic_Algorithms",
  "Confidence": 1.0
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='genet', importance=0.7056, present_in_paper=0
  word='fitness', importance=0.679, present_in_paper=1
  word='coevolution', importance=0.6355, present_in_paper=1
  word='competitive', importance=0.6296, present_in_paper=1
  word='selected', importance=0.6276, present_in_paper=1
  word='individuals', importance=0.6075, present_in_paper=1
  word='evolving', importance=0.6054, present_in_paper=1

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 11
Label distribution across all 1-hop neighbors (ground-truth class): Genetic_Algorithms=90.9%, Theory=9.1%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 2353 | edge_importance=0.8304 | class=Genetic_Algorithms | Title: Dynamics of Co-evolutionary Learning  
Abstract: Co-evolutionary learning, which involves the embedding of adaptive learning agents in a fitness environment which dynamically responds to their 
  Node 1836 | edge_importance=0.8278 | class=Genetic_Algorithms | Title: Small Populations over Many Generations can beat Large Populations over Few Generations in Genetic Programming  
Abstract: This paper looks at the use of small populations in Genetic Programmin
  Node 1588 | edge_importance=0.8238 | class=Genetic_Algorithms | Title: Automatic Modularization by Speciation  
Abstract: Real-world problems are often too difficult to be solved by a single monolithic system. There are many examples of natural and artificial syst
  Node 1790 | edge_importance=0.8051 | class=Genetic_Algorithms | Title: Using Genetic Programming to Evolve Board Evaluation Functions  
Abstract: The purpose of most architecture optimization schemes is to improve generalization. In this presentation we suggest to
  Node 1917 | edge_importance=0.8031 | class=Genetic_Algorithms | Title: Go and Genetic Programming Playing Go with Filter Functions  
Abstract: A neural network model called LISSOM for the cooperative self-organization of afferent and lateral connections in cortica
  Node 2103 | edge_importance=0.7948 | class=Genetic_Algorithms | Title: The Evolution of Communication Schemes Over Continuous Channels  
Abstract: As the field of Genetic Programming (GP) matures and its breadth of application increases, the need for parallel impl
  Node 2332 | edge_importance=0.7914 | class=Genetic_Algorithms | Title: Improved Hoeffding-Style Performance Guarantees for Accurate Classifiers  
Abstract: Evolving Cooperative Groups: Preliminary Results Abstract Multi-agent systems require coordination of source

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 55 | edge_importance=0.8435 | class=Genetic_Algorithms | Title: A Comparison of Selection Schemes used in Genetic Algorithms  
Abstract: TIK-Report Nr. 11, December 1995 Version 2 (2. Edition) 
  Node 523 | edge_importance=0.8384 | class=Genetic_Algorithms | Title: Some studies in machine learning using the game of checkers. IBM Journal, 3(3):211-229, 1959. Some
Abstract: covering has been formalized and used extensively. In this work, the divide-and-conq
  Node 163 | edge_importance=0.8266 | class=Genetic_Algorithms | Title: 4 Implementing Application Specific Routines  Genetic algorithms in search, optimization, and machine learning. Reading, MA: Addison-Wesley.  
Abstract: To implement a specific application, you
  Node 415 | edge_importance=0.2479 | class=Genetic_Algorithms | Title: Competitive Environments Evolve Better Solutions for Complex Tasks  
Abstract: University of Wisconsin Computer Sciences Technical Report 876 (September 1989) Abstract In explanation-based lear
  Node 1117 | edge_importance=0.2466 | class=Genetic_Algorithms | Title: A Coevolutionary Approach to Learning Sequential Decision Rules  
Abstract: We present a coevolutionary approach to learning sequential decision rules which appears to have a number of advantag
  Node 1114 | edge_importance=0.2363 | class=Genetic_Algorithms | Title: Using Genetic Algorithms to Explore Pattern Recognition in the Immune System  COMMENTS WELCOME  
Abstract: This paper describes an immune system model based on binary strings. The purpose of th
  Node 615 | edge_importance=0.2335 | class=Theory | Title: Efficient Algorithms for Learning to Play Repeated Games Against Computationally Bounded Adversaries  
Abstract: We study the problem of efficiently learning to play a game optimally against an
  Node 712 | edge_importance=0.2324 | class=Genetic_Algorithms | Title: Tracking the red queen: Measurements of adaptive progress in co-evolution ary simulations. In Third European
Abstract: Current expert systems cannot properly handle imprecise and incomplete inf
  Node 2704 | edge_importance=0.2309 | class=Genetic_Algorithms | Title: A Genome Compiler for High Performance Genetic Programming  
Abstract: Genetic Programming is very computationally expensive. For most applications, the vast majority of time is spent evaluatin
  Node 22 | edge_importance=0.227 | class=Genetic_Algorithms | Title: Discovering Complex Othello Strategies Through Evolutionary Neural Networks  
Abstract: An approach to develop new game playing strategies based on artificial evolution of neural networks is pr

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

- ID: 2334
- Title: New Methods for Competitive Coevolution
- True class (canonical `y`): **Genetic_Algorithms**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Genetic_Algorithms**
- Prediction recorded by this method's pipeline: **Genetic_Algorithms**

Canonical text (`raw_text`):

~~~~~~text
Title: New Methods for Competitive Coevolution  
Abstract: We consider "competitive coevolution," in which fitness is based on direct competition among individuals selected from two independently evolving populations of "hosts" and "parasites." Competitive coevolution can lead to an "arms race," in which the two populations reciprocally drive one another to increasing levels of performance and complexity. We use the games of Nim and 3-D Tic-Tac-Toe as test problems to explore three new techniques in competitive coevolution. "Competitive fitness sharing" changes the way fitness is measured, "shared sampling" provides a method for selecting a strong, diverse set of parasites, and the "hall of fame" encourages arms races by saving good individuals from prior generations. We provide several different motivations for these methods, and mathematical insights into their use. Experimental comparisons are done, and a detailed analysis of these experiments is presented in terms of testing issues, diversity, extinction, arms race progress measurements, and drift. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 11 nodes

| node id | true class | title |
|---|---|---|
| 54 | Theory | A Competitive Approach to Game Learning |
| 209 | Genetic_Algorithms | 17 Massively Parallel Genetic Programming |
| 602 | Genetic_Algorithms | Every Niching Method has its Niche: Fitness Sharing and Implicit Sharing Compared |
| 1588 | Genetic_Algorithms | Automatic Modularization by Speciation |
| 1790 | Genetic_Algorithms | Using Genetic Programming to Evolve Board Evaluation Functions |
| 1832 | Genetic_Algorithms | Tackling the Boolean Even N Parity Problem with Genetic Programming and Limited-Error Fitness standard GP |
| 1836 | Genetic_Algorithms | Small Populations over Many Generations can beat Large Populations over Few Generations in Genetic Programming |
| 1917 | Genetic_Algorithms | Go and Genetic Programming Playing Go with Filter Functions |
| 2103 | Genetic_Algorithms | The Evolution of Communication Schemes Over Continuous Channels |
| 2332 | Genetic_Algorithms | Improved Hoeffding-Style Performance Guarantees for Accurate Classifiers |
| 2353 | Genetic_Algorithms | Dynamics of Co-evolutionary Learning |

### 2-hop (shortest distance exactly 2): 14 nodes

| node id | true class | title |
|---|---|---|
| 22 | Genetic_Algorithms | Discovering Complex Othello Strategies Through Evolutionary Neural Networks |
| 55 | Genetic_Algorithms | A Comparison of Selection Schemes used in Genetic Algorithms |
| 163 | Genetic_Algorithms | 4 Implementing Application Specific Routines  Genetic algorithms in search, optimization, and machine learning. Reading, MA: Addison-Wesley. |
| 415 | Genetic_Algorithms | Competitive Environments Evolve Better Solutions for Complex Tasks |
| 523 | Genetic_Algorithms | Some studies in machine learning using the game of checkers. IBM Journal, 3(3):211-229, 1959. Some |
| 565 | Reinforcement_Learning | Machine Learning Learning to Predict by the Methods of Temporal Differences Keywords: Incremental learning, prediction, |
| 615 | Theory | Efficient Algorithms for Learning to Play Repeated Games Against Computationally Bounded Adversaries |
| 712 | Genetic_Algorithms | Tracking the red queen: Measurements of adaptive progress in co-evolution ary simulations. In Third European |
| 1114 | Genetic_Algorithms | Using Genetic Algorithms to Explore Pattern Recognition in the Immune System  COMMENTS WELCOME |
| 1117 | Genetic_Algorithms | A Coevolutionary Approach to Learning Sequential Decision Rules |
| 1687 | Reinforcement_Learning | Markov games as a framework for multi-agent reinforcement learning |
| 1796 | Genetic_Algorithms | Evaluating and Improving Steady State Evolutionary Algorithms on Constraint Satisfaction Problems |
| 1831 | Genetic_Algorithms | Some Training Subset Selection Methods for Supervised Learning in Genetic Programming |
| 2704 | Genetic_Algorithms | A Genome Compiler for High Performance Genetic Programming |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=2334).
Recorded prediction: `{"Target Node": 2334, "Predicted Class": "Genetic_Algorithms", "Confidence": 1.0}`
Recorded graph stats: `{"total_1hop_degree": 11, "neighbor_label_ratio": {"Genetic_Algorithms": 0.909, "Theory": 0.091}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | genet | 0.7056 | 0 |
| 2 | fitness | 0.679 | 1 |
| 3 | coevolution | 0.6355 | 1 |
| 4 | competitive | 0.6296 | 1 |
| 5 | selected | 0.6276 | 1 |
| 6 | individuals | 0.6075 | 1 |
| 7 | evolving | 0.6054 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
