# Reference packet: GraphXAIN__GPT-4o__cora__1440

- Method: GraphXAIN; configuration: GPT-4o; dataset: cora; target node: 1440
- Explanation source: `./robustness_2026-10-30/graphxain_gpt4o/cora/1440.json` (narrative)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model confidently predicted the paper titled "Value Function Approximations and Job-Shop Scheduling" to fall under the "Reinforcement_Learning" category with a confidence level of 1.0. Among the bag-of-words features, "processing" and "task" were present and highly influential, likely due to their strong association with typical reinforcement learning applications such as scheduling and function approximation, which are core aspects of the paper's content. Although other important words like "differ", "increment", and "tempor" were absent, their relevance to incremental learning and methods common in reinforcement learning frameworks likely contributed indirectly to the classification. The direct citation neighbors, such as the paper on "A Reinforcement Learning Approach to Job-shop Scheduling", and others focused on reinforcement learning methods, further solidified the prediction as they explore similar topics like job-shop scheduling and value function approximation. The presence of influential 2-hop neighbors, which also focus heavily on reinforcement learning themes such as "Robust Value Function Approximation by Working Backwards", reinforced the connection between the target paper and the reinforcement learning domain. This consistent pattern among both direct and indirect citation relationships highlighted a rich interconnection with the reinforcement learning community, thereby validating the model's prediction.
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

### Target Paper (node 1440):
Title: Value Function Approximations and Job-Shop Scheduling  
Abstract: We report a successful application of TD() with value function approximation to the task of job-shop scheduling. Our scheduling problems are based on the problem of scheduling payload processing steps for the NASA space shuttle

### Model Prediction:
{
  "Target Node": 1440,
  "Predicted Class": "Reinforcement_Learning",
  "Confidence": 1.0
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='differ', importance=0.6883, present_in_paper=0
  word='increment', importance=0.6728, present_in_paper=0
  word='tempor', importance=0.6639, present_in_paper=0
  word='processing', importance=0.6555, present_in_paper=1
  word='convent', importance=0.6487, present_in_paper=0
  word='method', importance=0.6398, present_in_paper=0
  word='task', importance=0.6345, present_in_paper=1

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 3
Label distribution across all 1-hop neighbors (ground-truth class): Reinforcement_Learning=100.0%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 82 | edge_importance=0.7482 | class=Reinforcement_Learning | Title: A Reinforcement Learning Approach to Job-shop Scheduling  
Abstract: We apply reinforcement learning methods to learn domain-specific heuristics for job shop scheduling. A repair-based schedule
  Node 1378 | edge_importance=0.6726 | class=Reinforcement_Learning | Title: Generalization in Reinforcement Learning: Safely Approximating the Value Function  
Abstract: To appear in: G. Tesauro, D. S. Touretzky and T. K. Leen, eds., Advances in Neural Information Proc
  Node 565 | edge_importance=0.6156 | class=Reinforcement_Learning | Title: Machine Learning Learning to Predict by the Methods of Temporal Differences Keywords: Incremental learning, prediction,
Abstract: This article introduces a class of incremental learning procedu

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 239 | edge_importance=0.8425 | class=Reinforcement_Learning | Title: Robust Value Function Approximation by Working Backwards Computing an accurate value function is the key
Abstract: In this paper, we examine the intuition that TD() is meant to operate by appro
  Node 410 | edge_importance=0.8347 | class=Reinforcement_Learning | Title: High-Performance Job-Shop Scheduling With A Time-Delay TD() Network  
Abstract: Job-shop scheduling is an important task for manufacturing industries. We are interested in the particular task o
  Node 21 | edge_importance=0.3042 | class=Reinforcement_Learning | Title: Decision Tree Function Approximation in Reinforcement Learning  
Abstract: We present a decision tree based approach to function approximation in reinforcement learning. We compare our approach
  Node 548 | edge_importance=0.2957 | class=Reinforcement_Learning | Title: Value Function Based Production Scheduling  
Abstract: Production scheduling, the problem of sequentially configuring a factory to meet forecasted demands, is a critical problem throughout the 
  Node 2642 | edge_importance=0.281 | class=Neural_Networks | Title: Learning to Play Games From Experience: An Application of Artificial Neural Networks and Temporal Difference Learning  
Abstract: We use a simulated evolution search (genetic programming) for t
  Node 477 | edge_importance=0.2777 | class=Reinforcement_Learning | Title: Forward models: Supervised learning with a distal teacher  
Abstract: Internal models of the environment have an important role to play in adaptive systems in general and are of particular impo
  Node 2628 | edge_importance=0.277 | class=Reinforcement_Learning | Title: Generalizing in TD() learning  
Abstract: Previous research has shown that a technique called error-correcting output coding (ECOC) can dramatically improve the classification accuracy of super
  Node 1859 | edge_importance=0.2757 | class=Reinforcement_Learning | Title: Self-Improving Factory Simulation using Continuous-time Average-Reward Reinforcement Learning  
Abstract: Many factory optimization problems, from inventory control to scheduling and reliabilit
  Node 1790 | edge_importance=0.2751 | class=Genetic_Algorithms | Title: Using Genetic Programming to Evolve Board Evaluation Functions  
Abstract: The purpose of most architecture optimization schemes is to improve generalization. In this presentation we suggest to
  Node 523 | edge_importance=0.2732 | class=Genetic_Algorithms | Title: Some studies in machine learning using the game of checkers. IBM Journal, 3(3):211-229, 1959. Some
Abstract: covering has been formalized and used extensively. In this work, the divide-and-conq

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

- ID: 1440
- Title: Value Function Approximations and Job-Shop Scheduling
- True class (canonical `y`): **Reinforcement_Learning**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Reinforcement_Learning**
- Prediction recorded by this method's pipeline: **Reinforcement_Learning**

Canonical text (`raw_text`):

~~~~~~text
Title: Value Function Approximations and Job-Shop Scheduling  
Abstract: We report a successful application of TD() with value function approximation to the task of job-shop scheduling. Our scheduling problems are based on the problem of scheduling payload processing steps for the NASA space shuttle program. The value function is approximated by a 2-layer feedforward network of sigmoid units. A one-step lookahead greedy algorithm using the learned evaluation function outperforms the best existing algorithm for this task, which is an iterative repair method incorporating simulated annealing. To understand the reasons for this performance improvement, this paper introduces several measurements of the learning process and discusses several hypotheses suggested by these measurements. We conclude that the use of value function approximation is not a source of difficulty for our method, and in fact, it may explain the success of the method independent of the use of value iteration. Additional experiments are required to discriminate among our hypotheses. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 3 nodes

| node id | true class | title |
|---|---|---|
| 82 | Reinforcement_Learning | A Reinforcement Learning Approach to Job-shop Scheduling |
| 565 | Reinforcement_Learning | Machine Learning Learning to Predict by the Methods of Temporal Differences Keywords: Incremental learning, prediction, |
| 1378 | Reinforcement_Learning | Generalization in Reinforcement Learning: Safely Approximating the Value Function |

### 2-hop (shortest distance exactly 2): 80 nodes

| node id | true class | title |
|---|---|---|
| 2 | Reinforcement_Learning | Submitted to NIPS96, Section: Applications. Preference: Oral presentation Reinforcement Learning for Dynamic Channel Allocation in |
| 21 | Reinforcement_Learning | Decision Tree Function Approximation in Reinforcement Learning |
| 34 | Reinforcement_Learning | Using a Case Base of Surfaces to Speed-Up Reinforcement Learning |
| 39 | Reinforcement_Learning | Finding Structure in Reinforcement Learning |
| 57 | Reinforcement_Learning | Markov Decision Processes in Large State Spaces |
| 60 | Reinforcement_Learning | The Efficient Learning of Multiple Task Sequences |
| 85 | Reinforcement_Learning | Q-Learning with Hidden-Unit Restarting |
| 92 | Reinforcement_Learning | Learning Analytically and Inductively |
| 103 | Reinforcement_Learning | NEUROCONTROL BY REINFORCEMENT LEARNING |
| 118 | Reinforcement_Learning | Learning to Race: Experiments with a Simulated Race Car |
| 128 | Reinforcement_Learning | Optimal Attitude Control of Satellites by Artificial Neural Networks: a Pilot Study |
| 173 | Reinforcement_Learning | An Upper Bound on the Loss from Approximate Optimal-Value Functions |
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
| 554 | Reinforcement_Learning | Reinforcement Learning Algorithms for Average-Payoff Markovian Decision Processes |
| 559 | Reinforcement_Learning | Scaling Up Average Reward Reinforcement Learning by Approximating the Domain Models and the Value Function |
| 564 | Reinforcement_Learning | Reinforcement Learning with Soft State Aggregation |
| 566 | Reinforcement_Learning | Integrated Architectures for Learning, Planning, and Reacting Based on Approximating Dynamic Programming |
| 575 | Reinforcement_Learning | Issues in Using Function Approximation for Reinforcement Learning |
| 601 | Reinforcement_Learning | Active Gesture Recognition using Partially Observable Markov Decision Processes |
| 621 | Reinforcement_Learning | Reinforcement Learning Methods for Continuous-Time Markov Decision Problems |
| 633 | Reinforcement_Learning | Chapter 1 Reinforcement Learning for Planning and Control |
| 644 | Reinforcement_Learning | Multi-criteria reinforcement learning |
| 671 | Reinforcement_Learning | Learning to Achieve Goals |
| 691 | Reinforcement_Learning | Reinforcement Learning in the Multi-Robot Domain |
| 738 | Reinforcement_Learning | On the Convergence of Stochastic Iterative Dynamic Programming Algorithms |
| 773 | Reinforcement_Learning | Reinforcement Learning with Imitation in Heterogeneous Multi-Agent Systems |
| 842 | Reinforcement_Learning | Metrics for Temporal Difference Learning |
| 882 | Reinforcement_Learning | Learning To Play the Game of Chess |
| 910 | Genetic_Algorithms | Learning Sequential Decision Rules Using Simulation Models and Competition |
| 970 | Genetic_Algorithms | Generality versus Size in Genetic Programming |
| 1012 | Reinforcement_Learning | TDLeaf(): Combining Temporal Difference learning with game-tree search. |
| 1213 | Reinforcement_Learning | Learning in Multi-Robot Systems |
| 1316 | Reinforcement_Learning | KnightCap: A chess program that learns by combining TD() with minimax search |
| 1373 | Neural_Networks | Direct Multi-Step Time Series Prediction Using TD() |
| 1376 | Reinforcement_Learning | Near-Optimal Performance for Reinforcement Learning in Polynomial Time |
| 1401 | Case_Based | Using Case-Based Reasoning as a Reinforcement Learning Framework for Optimization with Changing Criteria |
| 1438 | Reinforcement_Learning | Learning from undiscounted delayed rewards |
| 1529 | Reinforcement_Learning | Explanation Based Learning: A Comparison of Symbolic and Neural Network Approaches |
| 1540 | Reinforcement_Learning | MultiPlayer Residual Advantage Learning With General Function Approximation |
| 1546 | Reinforcement_Learning | Analytical Mean Squared Error Curves in Temporal Difference Learning |
| 1553 | Case_Based | Learning to Predict User Operations for Adaptive Scheduling |
| 1585 | Reinforcement_Learning | Q-Learning for Bandit Problems |
| 1616 | Reinforcement_Learning | NeuroDraughts: the role of representation, search, training regime and architecture in a TD draughts player |
| 1676 | Neural_Networks | TD Learning of Game Evaluation Functions with Hierarchical Neural Architectures |
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

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=1440).
Recorded prediction: `{"Target Node": 1440, "Predicted Class": "Reinforcement_Learning", "Confidence": 1.0}`
Recorded graph stats: `{"total_1hop_degree": 3, "neighbor_label_ratio": {"Reinforcement_Learning": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | differ | 0.6883 | 0 |
| 2 | increment | 0.6728 | 0 |
| 3 | tempor | 0.6639 | 0 |
| 4 | processing | 0.6555 | 1 |
| 5 | convent | 0.6487 | 0 |
| 6 | method | 0.6398 | 0 |
| 7 | task | 0.6345 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
