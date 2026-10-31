# Reference packet: GraphXAIN__Llama-70B__cora__1687

- Method: GraphXAIN; configuration: Llama-70B; dataset: cora; target node: 1687
- Explanation source: `./robustness_2026-10-30/llama70b/graphxain/cora/1687.json` (response)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model confidently predicts, with 100% certainty, that the target paper belongs to the "Reinforcement_Learning" category. This prediction is largely driven by the presence of highly relevant keywords such as "Markov," "reinforcement," "mdp," "function," and "decision," which are all strongly associated with the paper's content and title, "Markov games as a framework for multi-agent reinforcement learning." Furthermore, the target paper is closely connected to several influential neighboring papers, including "Learning to take risks," "Reinforcement Learning with Imitation in Heterogeneous Multi-Agent Systems," and "Generalized Markov Decision Processes," all of which share topics related to reinforcement learning and multi-agent systems. These connections likely reinforced the prediction due to their high relevance and proximity to the target paper. Additionally, the broader local graph structure also supports this prediction, with nearly 70% of the target paper's direct neighbors belonging to the same "Reinforcement_Learning" category. Moreover, even 2-hop neighbors like "Reinforcement Learning: A Survey" and "A Unified Analysis of Value-Function-Based Reinforcement-Learning Algorithms" further solidify the connection, highlighting the paper's deep ties within the reinforcement learning community. Overall, these factors collectively drive the model's confident prediction that the target paper falls squarely within the realm of reinforcement learning research.
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

### Target Paper (node 1687):
Title: Markov games as a framework for multi-agent reinforcement learning  
Abstract: In the Markov decision process (MDP) formalization of reinforcement learning, a single adaptive agent interacts with an environment defined by a probabilistic transition function. In this solipsistic view, secondar

### Model Prediction:
{
  "Target Node": 1687,
  "Predicted Class": "Reinforcement_Learning",
  "Confidence": 1.0
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='markov', importance=0.6719, present_in_paper=1
  word='reinforcement', importance=0.6551, present_in_paper=1
  word='result', importance=0.6537, present_in_paper=1
  word='mdp', importance=0.6527, present_in_paper=1
  word='function', importance=0.6518, present_in_paper=1
  word='instanc', importance=0.6517, present_in_paper=1
  word='decision', importance=0.6383, present_in_paper=1

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 13
Label distribution across all 1-hop neighbors (ground-truth class): Reinforcement_Learning=69.2%, Theory=15.4%, Genetic_Algorithms=7.7%, Probabilistic_Methods=7.7%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 870 | edge_importance=0.8137 | class=Reinforcement_Learning | Title: Learning to take risks  
Abstract: Agents that learn about other agents and can exploit this information possess a distinct advantage in competitive situations. Games provide stylized adversari
  Node 773 | edge_importance=0.7219 | class=Reinforcement_Learning | Title: Reinforcement Learning with Imitation in Heterogeneous Multi-Agent Systems  
Abstract: The application of decision making and learning algorithms to multi-agent systems presents many interestin
  Node 1459 | edge_importance=0.6979 | class=Reinforcement_Learning | Title: Generalized Markov Decision Processes: Dynamic-programming and Reinforcement-learning Algorithms  
Abstract: The problem of maximizing the expected total discounted reward in a completely obser
  Node 1137 | edge_importance=0.6893 | class=Reinforcement_Learning | Title: Learning Conventions in Multiagent Stochastic Domains using Likelihood Estimates  
Abstract: Fully cooperative multiagent systemsthose in which agents share a joint utility modelis of special i
  Node 148 | edge_importance=0.6739 | class=Reinforcement_Learning | Title: Multiagent Reinforcement Learning: Theoretical Framework and an Algorithm  
Abstract: In this paper, we adopt general-sum stochastic games as a framework for multiagent reinforcement learning. 
  Node 1632 | edge_importance=0.6681 | class=Reinforcement_Learning | Title: Learning Team Strategies With Multiple Policy-Sharing Agents: A Soccer Case Study  
Abstract: We use simulated soccer to study multiagent learning. Each team's players (agents) share action set
  Node 1649 | edge_importance=0.6528 | class=Reinforcement_Learning | Title: Multi-Agent Reinforcement Learning: Independent vs. Cooperative Agents  
Abstract: Intelligent human agents exist in a cooperative social environment that facilitates learning. They learn not o

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 910 | edge_importance=0.2871 | class=Genetic_Algorithms | Title: Learning Sequential Decision Rules Using Simulation Models and Competition  
Abstract: The problem of learning decision rules for sequential tasks is addressed, focusing on the problem of learn
  Node 415 | edge_importance=0.2816 | class=Genetic_Algorithms | Title: Competitive Environments Evolve Better Solutions for Complex Tasks  
Abstract: University of Wisconsin Computer Sciences Technical Report 876 (September 1989) Abstract In explanation-based lear
  Node 2404 | edge_importance=0.2793 | class=Probabilistic_Methods | Title: A Model for Projection and Action  
Abstract: In designing autonomous agents that deal competently with issues involving time and space, there is a tradeoff to be made between guaranteed respon
  Node 656 | edge_importance=0.2763 | class=Reinforcement_Learning | Title: Reinforcement Learning: A Survey  
Abstract: This paper surveys the field of reinforcement learning from a computer-science perspective. It is written to be accessible to researchers familiar w
  Node 460 | edge_importance=0.2741 | class=Reinforcement_Learning | Title: Learning Roles: Behavioral Diversity in Robot Teams  
Abstract: This paper describes research investigating behavioral specialization in learning robot teams. Each agent is provided a common se
  Node 565 | edge_importance=0.2734 | class=Reinforcement_Learning | Title: Machine Learning Learning to Predict by the Methods of Temporal Differences Keywords: Incremental learning, prediction,
Abstract: This article introduces a class of incremental learning procedu
  Node 1616 | edge_importance=0.2732 | class=Reinforcement_Learning | Title: NeuroDraughts: the role of representation, search, training regime and architecture in a TD draughts player  
Abstract: NeuroDraughts is a draughts playing program similar in approach to NeuroG
  Node 210 | edge_importance=0.2706 | class=Reinforcement_Learning | Title: A Unified Analysis of Value-Function-Based Reinforcement-Learning Algorithms  
Abstract: Reinforcement learning is the problem of generating optimal behavior in a sequential decision-making env
  Node 717 | edge_importance=0.2696 | class=Genetic_Algorithms | Title: Information filtering: Selection mechanisms in learning systems. Machine Learning, 10:113-151, 1993. Generalization as search. Artificial
Abstract: Draft A Brief Introduction to Neural Networks
  Node 508 | edge_importance=0.2687 | class=Theory | Title: Machine Learning by Function Decomposition  
Abstract: We present a new machine learning method that, given a set of training examples, induces a definition of the target concept in terms of a 

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

- ID: 1687
- Title: Markov games as a framework for multi-agent reinforcement learning
- True class (canonical `y`): **Reinforcement_Learning**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Reinforcement_Learning**
- Prediction recorded by this method's pipeline: **Reinforcement_Learning**

Canonical text (`raw_text`):

~~~~~~text
Title: Markov games as a framework for multi-agent reinforcement learning  
Abstract: In the Markov decision process (MDP) formalization of reinforcement learning, a single adaptive agent interacts with an environment defined by a probabilistic transition function. In this solipsistic view, secondary agents can only be part of the environment and are therefore fixed in their behavior. The framework of Markov games allows us to widen this view to include multiple adaptive agents with interacting or competing goals. This paper considers a step in this direction in which exactly two agents with diametrically opposed goals share an environment. It describes a Q-learning-like algorithm for finding optimal policies and demonstrates its application to a simple two-player game in which the optimal policy is probabilistic.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 13 nodes

| node id | true class | title |
|---|---|---|
| 54 | Theory | A Competitive Approach to Game Learning |
| 148 | Reinforcement_Learning | Multiagent Reinforcement Learning: Theoretical Framework and an Algorithm |
| 523 | Genetic_Algorithms | Some studies in machine learning using the game of checkers. IBM Journal, 3(3):211-229, 1959. Some |
| 773 | Reinforcement_Learning | Reinforcement Learning with Imitation in Heterogeneous Multi-Agent Systems |
| 870 | Reinforcement_Learning | Learning to take risks |
| 898 | Probabilistic_Methods | database |
| 1137 | Reinforcement_Learning | Learning Conventions in Multiagent Stochastic Domains using Likelihood Estimates |
| 1189 | Theory | Figure 3: Average model size accepted from a ran-dom prefix-closed samples of various size, and |
| 1228 | Reinforcement_Learning | Team-Partitioned, Opaque-Transition Reinforcement Learning |
| 1459 | Reinforcement_Learning | Generalized Markov Decision Processes: Dynamic-programming and Reinforcement-learning Algorithms |
| 1557 | Reinforcement_Learning | Using Communication to Reduce Locality in Distributed Multi-Agent Learning |
| 1632 | Reinforcement_Learning | Learning Team Strategies With Multiple Policy-Sharing Agents: A Soccer Case Study |
| 1649 | Reinforcement_Learning | Multi-Agent Reinforcement Learning: Independent vs. Cooperative Agents |

### 2-hop (shortest distance exactly 2): 60 nodes

| node id | true class | title |
|---|---|---|
| 45 | Reinforcement_Learning | Acting under Uncertainty: Discrete Bayesian Models for Mobile-Robot Navigation |
| 57 | Reinforcement_Learning | Markov Decision Processes in Large State Spaces |
| 68 | Neural_Networks | DISCOVERING NEURAL NETS WITH LOW KOLMOGOROV COMPLEXITY AND HIGH GENERALIZATION CAPABILITY Neural Networks 10(5):857-873, 1997 |
| 107 | Probabilistic_Methods | Computing upper and lower bounds on likelihoods in intractable networks |
| 108 | Probabilistic_Methods | Recursive algorithms for approximating probabilities in graphical models |
| 163 | Genetic_Algorithms | 4 Implementing Application Specific Routines  Genetic algorithms in search, optimization, and machine learning. Reading, MA: Addison-Wesley. |
| 167 | Reinforcement_Learning | Auto-exploratory Average Reward Reinforcement Learning |
| 188 | Genetic_Algorithms | Coevolving High-Level Representations |
| 210 | Reinforcement_Learning | A Unified Analysis of Value-Function-Based Reinforcement-Learning Algorithms |
| 277 | Reinforcement_Learning | Applying Online Search Techniques to Continuous-State Reinforcement Learning key to the success of the local |
| 283 | Neural_Networks | A Local Learning Algorithm for Dynamic Feedforward and Recurrent Networks |
| 415 | Genetic_Algorithms | Competitive Environments Evolve Better Solutions for Complex Tasks |
| 460 | Reinforcement_Learning | Learning Roles: Behavioral Diversity in Robot Teams |
| 465 | Reinforcement_Learning | Strategy Learning with Multilayer Connectionist Representations 1 |
| 471 | Reinforcement_Learning | In  Improving Elevator Performance Using Reinforcement Learning |
| 473 | Reinforcement_Learning | Improving Policies without Measuring Merits |
| 478 | Case_Based | An Improved Algorithm for Incremental Induction of Decision Trees |
| 508 | Theory | Machine Learning by Function Decomposition |
| 540 | Case_Based | A Model-Based Approach to Blame-Assignment in Design |
| 551 | Reinforcement_Learning | Utilization Filtering a method for reducing the inherent harmfulness of deductively learned knowledge field of |
| 558 | Probabilistic_Methods | A Tutorial on Learning With Bayesian Networks |
| 565 | Reinforcement_Learning | Machine Learning Learning to Predict by the Methods of Temporal Differences Keywords: Incremental learning, prediction, |
| 566 | Reinforcement_Learning | Integrated Architectures for Learning, Planning, and Reacting Based on Approximating Dynamic Programming |
| 615 | Theory | Efficient Algorithms for Learning to Play Repeated Games Against Computationally Bounded Adversaries |
| 633 | Reinforcement_Learning | Chapter 1 Reinforcement Learning for Planning and Control |
| 638 | Theory | Learning a set of primitive actions with an Induction of decision trees. Machine Learning, 1(1):81-106, |
| 650 | Reinforcement_Learning | Learning to Use Selective Attention and Short-Term Memory in Sequential Tasks |
| 656 | Reinforcement_Learning | Reinforcement Learning: A Survey |
| 671 | Reinforcement_Learning | Learning to Achieve Goals |
| 691 | Reinforcement_Learning | Reinforcement Learning in the Multi-Robot Domain |
| 712 | Genetic_Algorithms | Tracking the red queen: Measurements of adaptive progress in co-evolution ary simulations. In Third European |
| 717 | Genetic_Algorithms | Information filtering: Selection mechanisms in learning systems. Machine Learning, 10:113-151, 1993. Generalization as search. Artificial |
| 749 | Reinforcement_Learning | On the Complexity of Solving Markov Decision Problems |
| 775 | Reinforcement_Learning | Asynchronous Modified Policy Iteration with Single-sided Updates |
| 804 | Reinforcement_Learning | Exploration Bonuses and Dual Control |
| 868 | Reinforcement_Learning | Adaptive Load Balancing: A Study in Multi-Agent Learning |
| 882 | Reinforcement_Learning | Learning To Play the Game of Chess |
| 910 | Genetic_Algorithms | Learning Sequential Decision Rules Using Simulation Models and Competition |
| 961 | Genetic_Algorithms | CFS-C: A Package of Domain Independent Subroutines for Implementing Classifier Systems in Arbitrary, User-Defined Environments. |
| 1213 | Reinforcement_Learning | Learning in Multi-Robot Systems |
| 1214 | Case_Based | Learning Problem-Solving Concepts by Reflecting on Problem Solving |
| 1540 | Reinforcement_Learning | MultiPlayer Residual Advantage Learning With General Function Approximation |
| 1616 | Reinforcement_Learning | NeuroDraughts: the role of representation, search, training regime and architecture in a TD draughts player |
| 1643 | Reinforcement_Learning | Learning to coordinate without sharing information |
| 1676 | Neural_Networks | TD Learning of Game Evaluation Functions with Hierarchical Neural Architectures |
| 1688 | Genetic_Algorithms | Co-Evolving Soccer Softbot Team Coordination with Genetic Programming |
| 1693 | Reinforcement_Learning | INCREMENTAL SELF-IMPROVEMENT FOR LIFE-TIME MULTI-AGENT REINFORCEMENT LEARNING |
| 1790 | Genetic_Algorithms | Using Genetic Programming to Evolve Board Evaluation Functions |
| 1921 | Genetic_Algorithms | Computation. Automated Synthesis of Analog Electrical Circuits by Means of Genetic Programming |
| 1931 | Genetic_Algorithms | AUTOMATED TOPOLOGY AND SIZING OF ANALOG CIRCUITS AUTOMATED DESIGN OF BOTH THE TOPOLOGY AND SIZING |
| 2078 | Probabilistic_Methods | Structured Reachability Analysis for Markov Decision Processes |
| 2221 | Probabilistic_Methods | Reasoning about Time and Probability |
| 2334 | Genetic_Algorithms | New Methods for Competitive Coevolution |
| 2404 | Probabilistic_Methods | A Model for Projection and Action |
| 2408 | Reinforcement_Learning | Exploratory Learning in the Game of GO |
| 2442 | Reinforcement_Learning | Using Temporal-Difference Reinforcement Learning to Improve Decision-Theoretic Utilities for Diagnosis |
| 2480 | Reinforcement_Learning | Planning by Incremental Dynamic Programming |
| 2551 | Reinforcement_Learning | The Role of Forgetting in Learning |
| 2600 | Genetic_Algorithms | Evolution of Iteration in Genetic Programming D a v d A The solution to many |
| 2642 | Neural_Networks | Learning to Play Games From Experience: An Application of Artificial Neural Networks and Temporal Difference Learning |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=1687).
Recorded prediction: `{"Target Node": 1687, "Predicted Class": "Reinforcement_Learning", "Confidence": 1.0}`
Recorded graph stats: `{"total_1hop_degree": 13, "neighbor_label_ratio": {"Reinforcement_Learning": 0.692, "Theory": 0.154, "Genetic_Algorithms": 0.077, "Probabilistic_Methods": 0.077}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | markov | 0.6719 | 1 |
| 2 | reinforcement | 0.6551 | 1 |
| 3 | result | 0.6537 | 1 |
| 4 | mdp | 0.6527 | 1 |
| 5 | function | 0.6518 | 1 |
| 6 | instanc | 0.6517 | 1 |
| 7 | decision | 0.6383 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
