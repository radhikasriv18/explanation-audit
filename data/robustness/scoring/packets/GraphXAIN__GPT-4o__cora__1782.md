# Reference packet: GraphXAIN__GPT-4o__cora__1782

- Method: GraphXAIN; configuration: GPT-4o; dataset: cora; target node: 1782
- Explanation source: `./robustness_2026-10-30/graphxain_gpt4o/cora/1782.json` (narrative)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The GNN model predicted with high confidence (0.9999) that the target paper "Least-Squares Temporal Difference Learning" belongs to the Reinforcement_Learning category. Among the top Bag-of-Words features, "works," "observed," "resulting," and "requires" are present in the paper, contributing to the prediction by signaling discussions about learning algorithms and procedures common in Reinforcement Learning, whereas the absence of "system," "reinforc," and "classic" likely provided less direct reinforcement to this class but didn't detract due to the strong presence of related terms. The target node's direct citation neighbors heavily influenced the prediction, particularly papers such as "A Comparison of Direct and Model-Based Reinforcement Learning" and "Machine Learning Learning to Predict by the Methods of Temporal Differences," which are centered on Reinforcement Learning methods, thereby reinforcing the classification. Although a single neighbor, "Gain Adaptation Beats Least Squares?" from the Neural_Networks domain offered some alternative classification pressure, it was not enough to override the dominance of Reinforcement_Learning contexts among citations. The 2-hop neighbors further consolidate this prediction, as they mostly pertain to studies and discussions within the Reinforcement Learning realm, thus echoing the thematic focus and making a strong case for the final classification.
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

### Target Paper (node 1782):
Title: Least-Squares Temporal Difference Learning  
Abstract: Submitted to NIPS-98 TD() is a popular family of algorithms for approximate policy evaluation in large MDPs. TD() works by incrementally updating the value function after each observed transition. It has two major drawbacks: it makes inef

### Model Prediction:
{
  "Target Node": 1782,
  "Predicted Class": "Reinforcement_Learning",
  "Confidence": 0.9999
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='system', importance=0.6755, present_in_paper=0
  word='works', importance=0.6639, present_in_paper=1
  word='reinforc', importance=0.6528, present_in_paper=0
  word='observed', importance=0.6495, present_in_paper=1
  word='resulting', importance=0.6486, present_in_paper=1
  word='requires', importance=0.6434, present_in_paper=1
  word='classic', importance=0.6407, present_in_paper=0

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 5
Label distribution across all 1-hop neighbors (ground-truth class): Reinforcement_Learning=80.0%, Neural_Networks=20.0%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 134 | edge_importance=0.7181 | class=Neural_Networks | Title: Gain Adaptation Beats Least Squares?  
Abstract: I present computational results suggesting that gain-adaptation algorithms based in part on connectionist learning methods may improve over leas
  Node 2328 | edge_importance=0.6915 | class=Reinforcement_Learning | Title: A Comparison of Direct and Model-Based Reinforcement Learning  
Abstract: This paper compares direct reinforcement learning (no explicit model) and model-based reinforcement learning on a simpl
  Node 566 | edge_importance=0.655 | class=Reinforcement_Learning | Title: Integrated Architectures for Learning, Planning, and Reacting Based on Approximating Dynamic Programming  
Abstract: This paper extends previous work with Dyna, a class of architectures for int
  Node 565 | edge_importance=0.6203 | class=Reinforcement_Learning | Title: Machine Learning Learning to Predict by the Methods of Temporal Differences Keywords: Incremental learning, prediction,
Abstract: This article introduces a class of incremental learning procedu
  Node 295 | edge_importance=0.5757 | class=Reinforcement_Learning | Title: A Neuro-Dynamic Programming Approach to Retailer Inventory Management 1  
Abstract: Miller, G. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing in

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 738 | edge_importance=0.29 | class=Reinforcement_Learning | Title: On the Convergence of Stochastic Iterative Dynamic Programming Algorithms  
Abstract: Recent developments in the area of reinforcement learning have yielded a number of new algorithms for the p
  Node 477 | edge_importance=0.2848 | class=Reinforcement_Learning | Title: Forward models: Supervised learning with a distal teacher  
Abstract: Internal models of the environment have an important role to play in adaptive systems in general and are of particular impo
  Node 1373 | edge_importance=0.2835 | class=Neural_Networks | Title: Direct Multi-Step Time Series Prediction Using TD()  
Abstract: This paper explores the application of Temporal Difference (TD) learning (Sutton, 1988) to forecasting the behavior of dynamical 
  Node 465 | edge_importance=0.2786 | class=Reinforcement_Learning | Title: Strategy Learning with Multilayer Connectionist Representations 1  
Abstract: Results are presented that demonstrate the learning and fine-tuning of search strategies using connectionist mechan
  Node 410 | edge_importance=0.2777 | class=Reinforcement_Learning | Title: High-Performance Job-Shop Scheduling With A Time-Delay TD() Network  
Abstract: Job-shop scheduling is an important task for manufacturing industries. We are interested in the particular task o
  Node 633 | edge_importance=0.2772 | class=Reinforcement_Learning | Title: Chapter 1 Reinforcement Learning for Planning and Control  
Abstract: In this paper, we examine a method for feature subset selection based on Information Theory. Initially, a framework for def
  Node 882 | edge_importance=0.2771 | class=Reinforcement_Learning | Title: Learning To Play the Game of Chess  
Abstract: This paper presents NeuroChess, a program which learns to play chess from the final outcome of games. NeuroChess learns chess board evaluation fun
  Node 2135 | edge_importance=0.2767 | class=Neural_Networks | Title: Learning Polynomial Functions by Feature Construction  
Abstract: We present a method for learning higher-order polynomial functions from examples using linear regression and feature constructi
  Node 2629 | edge_importance=0.2754 | class=Reinforcement_Learning | Title: Towards a Reactive Critic  
Abstract: In this paper we propose a reactive critic, that is able to respond to changing situations. We will explain why this is usefull in reinforcement learning, 
  Node 733 | edge_importance=0.2725 | class=Reinforcement_Learning | Title: Evolutionary Differentiation of Learning Abilities a case study on optimizing parameter values in Q-learning by
Abstract: This paper describes the first stage of our study on evolution of learn

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

- ID: 1782
- Title: Least-Squares Temporal Difference Learning
- True class (canonical `y`): **Reinforcement_Learning**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Reinforcement_Learning**
- Prediction recorded by this method's pipeline: **Reinforcement_Learning**

Canonical text (`raw_text`):

~~~~~~text
Title: Least-Squares Temporal Difference Learning  
Abstract: Submitted to NIPS-98 TD() is a popular family of algorithms for approximate policy evaluation in large MDPs. TD() works by incrementally updating the value function after each observed transition. It has two major drawbacks: it makes inefficient use of data, and it requires the user to manually tune a stepsize schedule for good performance. For the case of linear value function approximations and = 0, the Least-Squares TD (LSTD) algorithm of Bradtke and Barto [5] eliminates all stepsize parameters and improves data efficiency. This paper extends Bradtke and Barto's work in three significant ways. First, it presents a simpler derivation of the LSTD algorithm. Second, it generalizes from = 0 to arbitrary values of ; at the extreme of = 1, the resulting algorithm is shown to be a practical formulation of supervised linear regression. Third, it presents a novel, intuitive interpretation of LSTD as a model-based reinforcement learning technique.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 5 nodes

| node id | true class | title |
|---|---|---|
| 134 | Neural_Networks | Gain Adaptation Beats Least Squares? |
| 295 | Reinforcement_Learning | A Neuro-Dynamic Programming Approach to Retailer Inventory Management 1 |
| 565 | Reinforcement_Learning | Machine Learning Learning to Predict by the Methods of Temporal Differences Keywords: Incremental learning, prediction, |
| 566 | Reinforcement_Learning | Integrated Architectures for Learning, Planning, and Reacting Based on Approximating Dynamic Programming |
| 2328 | Reinforcement_Learning | A Comparison of Direct and Model-Based Reinforcement Learning |

### 2-hop (shortest distance exactly 2): 102 nodes

| node id | true class | title |
|---|---|---|
| 2 | Reinforcement_Learning | Submitted to NIPS96, Section: Applications. Preference: Oral presentation Reinforcement Learning for Dynamic Channel Allocation in |
| 16 | Reinforcement_Learning | Exploration in Active Learning |
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
| 186 | Reinforcement_Learning | Adaptive state space quantisation: adding and removing neurons |
| 197 | Reinforcement_Learning | Optimal Navigation in a Probibalistic World |
| 210 | Reinforcement_Learning | A Unified Analysis of Value-Function-Based Reinforcement-Learning Algorithms |
| 220 | Reinforcement_Learning | Learning sorting and decision trees with POMDPs |
| 239 | Reinforcement_Learning | Robust Value Function Approximation by Working Backwards Computing an accurate value function is the key |
| 244 | Neural_Networks | Building Intelligent Agents for Web-Based Tasks: A Theory-Refinement Approach |
| 274 | Reinforcement_Learning | Some Experiments with a Hybrid Model for Learning Sequential Decision Making |
| 283 | Neural_Networks | A Local Learning Algorithm for Dynamic Feedforward and Recurrent Networks |
| 294 | Reinforcement_Learning | References elements that can solve difficult learning control problems. on Simulation of Adaptive Behavior, pages |
| 305 | Reinforcement_Learning | Solving Combinatorial Optimization Tasks by Reinforcement Learning: A General Methodology Applied to Resource-Constrained Scheduling |
| 306 | Reinforcement_Learning | Learning Curve Bounds for Markov Decision Processes with Undiscounted Rewards |
| 321 | Reinforcement_Learning | Planning with Closed-Loop Macro Actions |
| 333 | Reinforcement_Learning | A Comparison of Action Selection Learning Methods |
| 367 | Reinforcement_Learning | Machine Learning,  Explanation-Based Learning and Reinforcement Learning: A Unified View |
| 385 | Reinforcement_Learning | Modeling the Student with Reinforcement Learning |
| 410 | Reinforcement_Learning | High-Performance Job-Shop Scheduling With A Time-Delay TD() Network |
| 425 | Reinforcement_Learning | Reinforcement Learning, Neural Networks and PI Control Applied to a Heating Coil |
| 449 | Case_Based | Correcting Imperfect Domain Theories: A Knowledge-Level Analysis |
| 465 | Reinforcement_Learning | Strategy Learning with Multilayer Connectionist Representations 1 |
| 466 | Reinforcement_Learning | On the Computational Economics of Reinforcement Learning |
| 471 | Reinforcement_Learning | In  Improving Elevator Performance Using Reinforcement Learning |
| 472 | Reinforcement_Learning | Category: Control, Navigation and Planning. Key words: Reinforcement learning, Exploration, Hidden state. Prefer oral presentation. |
| 477 | Reinforcement_Learning | Forward models: Supervised learning with a distal teacher |
| 478 | Case_Based | An Improved Algorithm for Incremental Induction of Decision Trees |
| 483 | Reinforcement_Learning | The Parti-game Algorithm for Variable Resolution Reinforcement Learning in Multidimensional State-spaces |
| 492 | Reinforcement_Learning | Approximating Optimal Policies for Partially Observable Stochastic Domains |
| 502 | Reinforcement_Learning | Fast Online Q() |
| 505 | Neural_Networks | From Isolation to Cooperation: An Alternative View of a System of Experts |
| 523 | Genetic_Algorithms | Some studies in machine learning using the game of checkers. IBM Journal, 3(3):211-229, 1959. Some |
| 548 | Reinforcement_Learning | Value Function Based Production Scheduling |
| 554 | Reinforcement_Learning | Reinforcement Learning Algorithms for Average-Payoff Markovian Decision Processes |
| 564 | Reinforcement_Learning | Reinforcement Learning with Soft State Aggregation |
| 575 | Reinforcement_Learning | Issues in Using Function Approximation for Reinforcement Learning |
| 588 | Reinforcement_Learning | LEARNING TO AVOID COLLISIONS: A REINFORCEMENT LEARNING PARADIGM FOR MOBILE ROBOT NAVIGATION |
| 601 | Reinforcement_Learning | Active Gesture Recognition using Partially Observable Markov Decision Processes |
| 621 | Reinforcement_Learning | Reinforcement Learning Methods for Continuous-Time Markov Decision Problems |
| 633 | Reinforcement_Learning | Chapter 1 Reinforcement Learning for Planning and Control |
| 644 | Reinforcement_Learning | Multi-criteria reinforcement learning |
| 671 | Reinforcement_Learning | Learning to Achieve Goals |
| 688 | Reinforcement_Learning | Exploration and Model Building in Mobile Robot Domains |
| 691 | Reinforcement_Learning | Reinforcement Learning in the Multi-Robot Domain |
| 699 | Reinforcement_Learning | Adaptive state space quantisation for reinforcement learning of collision-free navigation |
| 733 | Reinforcement_Learning | Evolutionary Differentiation of Learning Abilities a case study on optimizing parameter values in Q-learning by |
| 738 | Reinforcement_Learning | On the Convergence of Stochastic Iterative Dynamic Programming Algorithms |
| 773 | Reinforcement_Learning | Reinforcement Learning with Imitation in Heterogeneous Multi-Agent Systems |
| 842 | Reinforcement_Learning | Metrics for Temporal Difference Learning |
| 858 | Case_Based | MULTISTRATEGY LEARNING IN REACTIVE CONTROL SYSTEMS FOR AUTONOMOUS ROBOTIC NAVIGATION |
| 882 | Reinforcement_Learning | Learning To Play the Game of Chess |
| 910 | Genetic_Algorithms | Learning Sequential Decision Rules Using Simulation Models and Competition |
| 1012 | Reinforcement_Learning | TDLeaf(): Combining Temporal Difference learning with game-tree search. |
| 1118 | Neural_Networks | Adapting Bias by Gradient Descent: An Incremental Version of Delta-Bar-Delta |
| 1213 | Reinforcement_Learning | Learning in Multi-Robot Systems |
| 1316 | Reinforcement_Learning | KnightCap: A chess program that learns by combining TD() with minimax search |
| 1373 | Neural_Networks | Direct Multi-Step Time Series Prediction Using TD() |
| 1376 | Reinforcement_Learning | Near-Optimal Performance for Reinforcement Learning in Polynomial Time |
| 1378 | Reinforcement_Learning | Generalization in Reinforcement Learning: Safely Approximating the Value Function |
| 1401 | Case_Based | Using Case-Based Reasoning as a Reinforcement Learning Framework for Optimization with Changing Criteria |
| 1438 | Reinforcement_Learning | Learning from undiscounted delayed rewards |
| 1440 | Reinforcement_Learning | Value Function Approximations and Job-Shop Scheduling |
| 1447 | Reinforcement_Learning | Model of the Environment to Avoid Local Learning |
| 1459 | Reinforcement_Learning | Generalized Markov Decision Processes: Dynamic-programming and Reinforcement-learning Algorithms |
| 1529 | Reinforcement_Learning | Explanation Based Learning: A Comparison of Symbolic and Neural Network Approaches |
| 1540 | Reinforcement_Learning | MultiPlayer Residual Advantage Learning With General Function Approximation |
| 1544 | Genetic_Algorithms | Monitoring in Embedded Agents |
| 1546 | Reinforcement_Learning | Analytical Mean Squared Error Curves in Temporal Difference Learning |
| 1585 | Reinforcement_Learning | Q-Learning for Bandit Problems |
| 1616 | Reinforcement_Learning | NeuroDraughts: the role of representation, search, training regime and architecture in a TD draughts player |
| 1643 | Reinforcement_Learning | Learning to coordinate without sharing information |
| 1676 | Neural_Networks | TD Learning of Game Evaluation Functions with Hierarchical Neural Architectures |
| 1727 | Theory | Machine Learning, 22(1/2/3):95-121, 1996. On the Worst-case Analysis of Temporal-difference Learning Algorithms |
| 1741 | Reinforcement_Learning | Reinforcement Learning Algorithm for Partially Observable Markov Decision Problems |
| 1790 | Genetic_Algorithms | Using Genetic Programming to Evolve Board Evaluation Functions |
| 1816 | Reinforcement_Learning | Generalized Prioritized Sweeping |
| 1859 | Reinforcement_Learning | Self-Improving Factory Simulation using Continuous-time Average-Reward Reinforcement Learning |
| 1957 | Reinforcement_Learning | AVERAGED REWARD REINFORCEMENT LEARNING APPLIED TO FUZZY RULE TUNING |
| 1975 | Reinforcement_Learning | Associative Reinforcement Learning: Functions in k-DNF |
| 2027 | Reinforcement_Learning | Coordinating Reactive Behaviors  keywords: reactive systems, planning and learning |
| 2078 | Probabilistic_Methods | Structured Reachability Analysis for Markov Decision Processes |
| 2118 | Reinforcement_Learning | On Step-Size and Bias in Temporal-Difference Learning |
| 2135 | Neural_Networks | Learning Polynomial Functions by Feature Construction |
| 2221 | Probabilistic_Methods | Reasoning about Time and Probability |
| 2442 | Reinforcement_Learning | Using Temporal-Difference Reinforcement Learning to Improve Decision-Theoretic Utilities for Diagnosis |
| 2472 | Reinforcement_Learning | Toward an Ideal Trainer* |
| 2480 | Reinforcement_Learning | Planning by Incremental Dynamic Programming |
| 2485 | Reinforcement_Learning | Tight Performance Bounds on Greedy Policies Based on Imperfect Value Functions |
| 2628 | Reinforcement_Learning | Generalizing in TD() learning |
| 2629 | Reinforcement_Learning | Towards a Reactive Critic |
| 2642 | Neural_Networks | Learning to Play Games From Experience: An Application of Artificial Neural Networks and Temporal Difference Learning |
| 2658 | Case_Based | Control Systems Magazine, 14, 1, pp.57-71. Robot Juggling: An Implementation of Memory-based Learning |
| 2672 | Neural_Networks | REINFORCEMENT LEARNING FOR COORDINATED REACTIVE CONTROL |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=1782).
Recorded prediction: `{"Target Node": 1782, "Predicted Class": "Reinforcement_Learning", "Confidence": 0.9999}`
Recorded graph stats: `{"total_1hop_degree": 5, "neighbor_label_ratio": {"Reinforcement_Learning": 0.8, "Neural_Networks": 0.2}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | system | 0.6755 | 0 |
| 2 | works | 0.6639 | 1 |
| 3 | reinforc | 0.6528 | 0 |
| 4 | observed | 0.6495 | 1 |
| 5 | resulting | 0.6486 | 1 |
| 6 | requires | 0.6434 | 1 |
| 7 | classic | 0.6407 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
