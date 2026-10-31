# Reference packet: GraphXAIN__Llama-8B__cora__1585

- Method: GraphXAIN; configuration: Llama-8B; dataset: cora; target node: 1585
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/cora/graphxain_cora_llama_2hop_narratives_full.json` ([1585])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the analysis, the GNN model confidently predicted the target paper, titled "Q-Learning for Bandit Problems," to fall under the class of "Reinforcement_Learning" with a staggering 99.87% confidence. The top bag-of-words features strongly supported this prediction, with words such as "control" and "markov" being present in the paper, both concepts being key elements in reinforcement learning methods. Additionally, the presence of related terms like "increment" and absence of less relevant words like "articl" further reinforced this association. Looking at the direct citation neighbors, two highly influential papers, one on "Exploration Bonuses and Dual Control" and another on "Machine Learning Learning to Predict by the Methods of Temporal Differences", demonstrate a strong affinity towards reinforcement learning techniques. These connections strongly emphasize the link between the target paper and the chosen class. Moreover, secondary citations also appear to corroborate this trend, although their influence seems somewhat diluted. Overall, the combination of key textual features and strategic citation patterns led the GNN model to convincingly assign the target paper to the category of reinforcement learning methods. The model effectively leveraged these informative cues to arrive at its accurate prediction.
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

### Target Paper (node 1585):
Title: Q-Learning for Bandit Problems  
Abstract: Multi-armed bandits may be viewed as decompositionally-structured Markov decision processes (MDP's) with potentially very-large state sets. A particularly elegant methodology for computing optimal policies was developed over twenty ago by Gittins [Gi

### Model Prediction:
{
  "Target Node": 1585,
  "Predicted Class": "Reinforcement_Learning",
  "Confidence": 0.9987
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='increment', importance=0.6979, present_in_paper=0
  word='control', importance=0.6858, present_in_paper=1
  word='markov', importance=0.6723, present_in_paper=1
  word='exist', importance=0.6693, present_in_paper=0
  word='articl', importance=0.6652, present_in_paper=0
  word='wherea', importance=0.665, present_in_paper=0
  word='incomplet', importance=0.6649, present_in_paper=0

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 3
Label distribution across all 1-hop neighbors (ground-truth class): Reinforcement_Learning=100.0%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 804 | edge_importance=0.7497 | class=Reinforcement_Learning | Title: Exploration Bonuses and Dual Control  
Abstract: Finding the Bayesian balance between exploration and exploitation in adaptive optimal control is in general intractable. This paper shows how to
  Node 565 | edge_importance=0.6525 | class=Reinforcement_Learning | Title: Machine Learning Learning to Predict by the Methods of Temporal Differences Keywords: Incremental learning, prediction,
Abstract: This article introduces a class of incremental learning procedu
  Node 738 | edge_importance=0.4159 | class=Reinforcement_Learning | Title: On the Convergence of Stochastic Iterative Dynamic Programming Algorithms  
Abstract: Recent developments in the area of reinforcement learning have yielded a number of new algorithms for the p

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 2629 | edge_importance=0.7367 | class=Reinforcement_Learning | Title: Towards a Reactive Critic  
Abstract: In this paper we propose a reactive critic, that is able to respond to changing situations. We will explain why this is usefull in reinforcement learning, 
  Node 1459 | edge_importance=0.7048 | class=Reinforcement_Learning | Title: Generalized Markov Decision Processes: Dynamic-programming and Reinforcement-learning Algorithms  
Abstract: The problem of maximizing the expected total discounted reward in a completely obser
  Node 1697 | edge_importance=0.6815 | class=Neural_Networks | Title: Neural Network Exploration Using Optimal Experiment Design  
Abstract: We consider the question "How should one act when the only goal is to learn as much as possible?" Building on the theoreti
  Node 621 | edge_importance=0.3553 | class=Reinforcement_Learning | Title: Reinforcement Learning Methods for Continuous-Time Markov Decision Problems  
Abstract: Semi-Markov Decision Problems are continuous time generalizations of discrete time Markov Decision Proble
  Node 552 | edge_importance=0.3547 | class=Reinforcement_Learning | Title: Learning to Act using Real-Time Dynamic Programming  
Abstract: fl The authors thank Rich Yee, Vijay Gullapalli, Brian Pinette, and Jonathan Bachrach for helping to clarify the relationships be
  Node 575 | edge_importance=0.3301 | class=Reinforcement_Learning | Title: Issues in Using Function Approximation for Reinforcement Learning  
Abstract: Reinforcement learning techniques address the problem of learning to select actions in unknown, dynamic environment
  Node 1741 | edge_importance=0.313 | class=Reinforcement_Learning | Title: Reinforcement Learning Algorithm for Partially Observable Markov Decision Problems  
Abstract: Increasing attention has been paid to reinforcement learning algorithms in recent years, partly du
  Node 1727 | edge_importance=0.2992 | class=Theory | Title: Machine Learning, 22(1/2/3):95-121, 1996. On the Worst-case Analysis of Temporal-difference Learning Algorithms  
Abstract: We study the behavior of a family of learning algorithms based on Sut
  Node 1183 | edge_importance=0.2849 | class=Reinforcement_Learning | Title: Hierarchical Reinforcement Learning with the MAXQ Value Function Decomposition  
Abstract: This paper describes the MAXQ method for hierarchical reinforcement learning based on a hierarchical d
  Node 1664 | edge_importance=0.2717 | class=Neural_Networks | Title: "What is the best thing to do right now?": getting beyond greedy exploration  
Abstract: Genetic programming is a methodology for program development, consisting of a special form of genetic al

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

- ID: 1585
- Title: Q-Learning for Bandit Problems
- True class (canonical `y`): **Reinforcement_Learning**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Reinforcement_Learning**
- Prediction recorded by this method's pipeline: **Reinforcement_Learning**

Canonical text (`raw_text`):

~~~~~~text
Title: Q-Learning for Bandit Problems  
Abstract: Multi-armed bandits may be viewed as decompositionally-structured Markov decision processes (MDP's) with potentially very-large state sets. A particularly elegant methodology for computing optimal policies was developed over twenty ago by Gittins [Gittins & Jones, 1974]. Gittins' approach reduces the problem of finding optimal policies for the original MDP to a sequence of low-dimensional stopping problems whose solutions determine the optimal policy through the so-called "Gittins indices." Katehakis and Veinott [Katehakis & Veinott, 1987] have shown that the Gittins index for a process in state i may be interpreted as a particular component of the maximum-value function associated with the "restart-in-i" process, a simple MDP to which standard solution methods for computing optimal policies, such as successive approximation, apply. This paper explores the problem of learning the Git-tins indices on-line without the aid of a process model; it suggests utilizing process-state-specific Q-learning agents to solve their respective restart-in-state-i subproblems, and includes an example in which the online reinforcement learning approach is applied to a problem of stochastic scheduling|one instance drawn from a wide class of problems that may be formulated as bandit problems.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 3 nodes

| node id | true class | title |
|---|---|---|
| 565 | Reinforcement_Learning | Machine Learning Learning to Predict by the Methods of Temporal Differences Keywords: Incremental learning, prediction, |
| 738 | Reinforcement_Learning | On the Convergence of Stochastic Iterative Dynamic Programming Algorithms |
| 804 | Reinforcement_Learning | Exploration Bonuses and Dual Control |

### 2-hop (shortest distance exactly 2): 82 nodes

| node id | true class | title |
|---|---|---|
| 2 | Reinforcement_Learning | Submitted to NIPS96, Section: Applications. Preference: Oral presentation Reinforcement Learning for Dynamic Channel Allocation in |
| 34 | Reinforcement_Learning | Using a Case Base of Surfaces to Speed-Up Reinforcement Learning |
| 57 | Reinforcement_Learning | Markov Decision Processes in Large State Spaces |
| 60 | Reinforcement_Learning | The Efficient Learning of Multiple Task Sequences |
| 82 | Reinforcement_Learning | A Reinforcement Learning Approach to Job-shop Scheduling |
| 85 | Reinforcement_Learning | Q-Learning with Hidden-Unit Restarting |
| 92 | Reinforcement_Learning | Learning Analytically and Inductively |
| 103 | Reinforcement_Learning | NEUROCONTROL BY REINFORCEMENT LEARNING |
| 118 | Reinforcement_Learning | Learning to Race: Experiments with a Simulated Race Car |
| 128 | Reinforcement_Learning | Optimal Attitude Control of Satellites by Artificial Neural Networks: a Pilot Study |
| 173 | Reinforcement_Learning | An Upper Bound on the Loss from Approximate Optimal-Value Functions |
| 210 | Reinforcement_Learning | A Unified Analysis of Value-Function-Based Reinforcement-Learning Algorithms |
| 239 | Reinforcement_Learning | Robust Value Function Approximation by Working Backwards Computing an accurate value function is the key |
| 244 | Neural_Networks | Building Intelligent Agents for Web-Based Tasks: A Theory-Refinement Approach |
| 283 | Neural_Networks | A Local Learning Algorithm for Dynamic Feedforward and Recurrent Networks |
| 294 | Reinforcement_Learning | References elements that can solve difficult learning control problems. on Simulation of Adaptive Behavior, pages |
| 295 | Reinforcement_Learning | A Neuro-Dynamic Programming Approach to Retailer Inventory Management 1 |
| 305 | Reinforcement_Learning | Solving Combinatorial Optimization Tasks by Reinforcement Learning: A General Methodology Applied to Resource-Constrained Scheduling |
| 306 | Reinforcement_Learning | Learning Curve Bounds for Markov Decision Processes with Undiscounted Rewards |
| 333 | Reinforcement_Learning | A Comparison of Action Selection Learning Methods |
| 367 | Reinforcement_Learning | Machine Learning,  Explanation-Based Learning and Reinforcement Learning: A Unified View |
| 385 | Reinforcement_Learning | Modeling the Student with Reinforcement Learning |
| 410 | Reinforcement_Learning | High-Performance Job-Shop Scheduling With A Time-Delay TD() Network |
| 425 | Reinforcement_Learning | Reinforcement Learning, Neural Networks and PI Control Applied to a Heating Coil |
| 465 | Reinforcement_Learning | Strategy Learning with Multilayer Connectionist Representations 1 |
| 466 | Reinforcement_Learning | On the Computational Economics of Reinforcement Learning |
| 477 | Reinforcement_Learning | Forward models: Supervised learning with a distal teacher |
| 478 | Case_Based | An Improved Algorithm for Incremental Induction of Decision Trees |
| 492 | Reinforcement_Learning | Approximating Optimal Policies for Partially Observable Stochastic Domains |
| 502 | Reinforcement_Learning | Fast Online Q() |
| 523 | Genetic_Algorithms | Some studies in machine learning using the game of checkers. IBM Journal, 3(3):211-229, 1959. Some |
| 548 | Reinforcement_Learning | Value Function Based Production Scheduling |
| 552 | Reinforcement_Learning | Learning to Act using Real-Time Dynamic Programming |
| 554 | Reinforcement_Learning | Reinforcement Learning Algorithms for Average-Payoff Markovian Decision Processes |
| 564 | Reinforcement_Learning | Reinforcement Learning with Soft State Aggregation |
| 566 | Reinforcement_Learning | Integrated Architectures for Learning, Planning, and Reacting Based on Approximating Dynamic Programming |
| 575 | Reinforcement_Learning | Issues in Using Function Approximation for Reinforcement Learning |
| 601 | Reinforcement_Learning | Active Gesture Recognition using Partially Observable Markov Decision Processes |
| 621 | Reinforcement_Learning | Reinforcement Learning Methods for Continuous-Time Markov Decision Problems |
| 633 | Reinforcement_Learning | Chapter 1 Reinforcement Learning for Planning and Control |
| 644 | Reinforcement_Learning | Multi-criteria reinforcement learning |
| 671 | Reinforcement_Learning | Learning to Achieve Goals |
| 691 | Reinforcement_Learning | Reinforcement Learning in the Multi-Robot Domain |
| 773 | Reinforcement_Learning | Reinforcement Learning with Imitation in Heterogeneous Multi-Agent Systems |
| 842 | Reinforcement_Learning | Metrics for Temporal Difference Learning |
| 882 | Reinforcement_Learning | Learning To Play the Game of Chess |
| 910 | Genetic_Algorithms | Learning Sequential Decision Rules Using Simulation Models and Competition |
| 1012 | Reinforcement_Learning | TDLeaf(): Combining Temporal Difference learning with game-tree search. |
| 1183 | Reinforcement_Learning | Hierarchical Reinforcement Learning with the MAXQ Value Function Decomposition |
| 1213 | Reinforcement_Learning | Learning in Multi-Robot Systems |
| 1316 | Reinforcement_Learning | KnightCap: A chess program that learns by combining TD() with minimax search |
| 1373 | Neural_Networks | Direct Multi-Step Time Series Prediction Using TD() |
| 1376 | Reinforcement_Learning | Near-Optimal Performance for Reinforcement Learning in Polynomial Time |
| 1378 | Reinforcement_Learning | Generalization in Reinforcement Learning: Safely Approximating the Value Function |
| 1401 | Case_Based | Using Case-Based Reasoning as a Reinforcement Learning Framework for Optimization with Changing Criteria |
| 1438 | Reinforcement_Learning | Learning from undiscounted delayed rewards |
| 1440 | Reinforcement_Learning | Value Function Approximations and Job-Shop Scheduling |
| 1459 | Reinforcement_Learning | Generalized Markov Decision Processes: Dynamic-programming and Reinforcement-learning Algorithms |
| 1529 | Reinforcement_Learning | Explanation Based Learning: A Comparison of Symbolic and Neural Network Approaches |
| 1540 | Reinforcement_Learning | MultiPlayer Residual Advantage Learning With General Function Approximation |
| 1546 | Reinforcement_Learning | Analytical Mean Squared Error Curves in Temporal Difference Learning |
| 1616 | Reinforcement_Learning | NeuroDraughts: the role of representation, search, training regime and architecture in a TD draughts player |
| 1664 | Neural_Networks | "What is the best thing to do right now?": getting beyond greedy exploration |
| 1676 | Neural_Networks | TD Learning of Game Evaluation Functions with Hierarchical Neural Architectures |
| 1697 | Neural_Networks | Neural Network Exploration Using Optimal Experiment Design |
| 1727 | Theory | Machine Learning, 22(1/2/3):95-121, 1996. On the Worst-case Analysis of Temporal-difference Learning Algorithms |
| 1741 | Reinforcement_Learning | Reinforcement Learning Algorithm for Partially Observable Markov Decision Problems |
| 1782 | Reinforcement_Learning | Least-Squares Temporal Difference Learning |
| 1790 | Genetic_Algorithms | Using Genetic Programming to Evolve Board Evaluation Functions |
| 1859 | Reinforcement_Learning | Self-Improving Factory Simulation using Continuous-time Average-Reward Reinforcement Learning |
| 1957 | Reinforcement_Learning | AVERAGED REWARD REINFORCEMENT LEARNING APPLIED TO FUZZY RULE TUNING |
| 1975 | Reinforcement_Learning | Associative Reinforcement Learning: Functions in k-DNF |
| 2027 | Reinforcement_Learning | Coordinating Reactive Behaviors  keywords: reactive systems, planning and learning |
| 2118 | Reinforcement_Learning | On Step-Size and Bias in Temporal-Difference Learning |
| 2442 | Reinforcement_Learning | Using Temporal-Difference Reinforcement Learning to Improve Decision-Theoretic Utilities for Diagnosis |
| 2472 | Reinforcement_Learning | Toward an Ideal Trainer* |
| 2480 | Reinforcement_Learning | Planning by Incremental Dynamic Programming |
| 2485 | Reinforcement_Learning | Tight Performance Bounds on Greedy Policies Based on Imperfect Value Functions |
| 2628 | Reinforcement_Learning | Generalizing in TD() learning |
| 2629 | Reinforcement_Learning | Towards a Reactive Critic |
| 2642 | Neural_Networks | Learning to Play Games From Experience: An Application of Artificial Neural Networks and Temporal Difference Learning |
| 2672 | Neural_Networks | REINFORCEMENT LEARNING FOR COORDINATED REACTIVE CONTROL |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=1585).
Recorded prediction: `{"Target Node": 1585, "Predicted Class": "Reinforcement_Learning", "Confidence": 0.9987}`
Recorded graph stats: `{"total_1hop_degree": 3, "neighbor_label_ratio": {"Reinforcement_Learning": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | increment | 0.6979 | 0 |
| 2 | control | 0.6858 | 1 |
| 3 | markov | 0.6723 | 1 |
| 4 | exist | 0.6693 | 0 |
| 5 | articl | 0.6652 | 0 |
| 6 | wherea | 0.665 | 0 |
| 7 | incomplet | 0.6649 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
