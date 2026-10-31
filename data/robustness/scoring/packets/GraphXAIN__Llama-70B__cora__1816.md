# Reference packet: GraphXAIN__Llama-70B__cora__1816

- Method: GraphXAIN; configuration: Llama-70B; dataset: cora; target node: 1816
- Explanation source: `./robustness_2026-10-30/llama70b/graphxain/cora/1816.json` (response)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The GNN model predicted with 99.93% confidence that the target paper belongs to the "Reinforcement_Learning" category. This prediction was strongly influenced by the presence of key words such as "reward," "generalized," "method," and "reinforcement" in the paper, which are highly indicative of the field. Notably, despite being mentioned in the paper, words like "reward" carry significant weight toward indicating a classification. Furthermore, the absence of "function" and "sequent" helps eliminate alternatives, increasing confidence. In terms of local graph structure, direct (1-hop) citation neighbors played a crucial role – most influential were connections to papers focused on reinforcement learning methods like scaling up average reward, updating value functions, and approximating domain models. Specifically, neighbors like "Tight Performance Bounds on Greedy Policies Based on Imperfect Value Functions" and "Scaling Up Average Reward Reinforcement Learning..." were instrumental in informing the classification due to their clear association with reinforcement learning concepts. Lastly, although less pronounced, some indirect (2-hop) neighbors on topics related to planning and adaptation reinforced this interpretation, providing further support for the predicted class.
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

### Target Paper (node 1816):
Title: Generalized Prioritized Sweeping  
Abstract: Prioritized sweeping is a model-based reinforcement learning method that attempts to focus an agent's limited computational resources to achieve a good estimate of the value of environment states. To choose effectively where to spend a costly plann

### Model Prediction:
{
  "Target Node": 1816,
  "Predicted Class": "Reinforcement_Learning",
  "Confidence": 0.9993
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='reward', importance=0.6614, present_in_paper=1
  word='generalized', importance=0.6454, present_in_paper=1
  word='method', importance=0.6439, present_in_paper=1
  word='reinforcement', importance=0.6354, present_in_paper=1
  word='function', importance=0.6345, present_in_paper=0
  word='sequenti', importance=0.634, present_in_paper=0
  word='value', importance=0.6332, present_in_paper=1

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 5
Label distribution across all 1-hop neighbors (ground-truth class): Reinforcement_Learning=60.0%, Probabilistic_Methods=40.0%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 2485 | edge_importance=0.8269 | class=Reinforcement_Learning | Title: Tight Performance Bounds on Greedy Policies Based on Imperfect Value Functions  
Abstract: Consider a given value function on states of a Markov decision problem, as might result from applying 
  Node 559 | edge_importance=0.8212 | class=Reinforcement_Learning | Title: Scaling Up Average Reward Reinforcement Learning by Approximating the Domain Models and the Value Function  
Abstract: Almost all the work in Average-reward Re- inforcement Learning (ARL) so fa
  Node 1934 | edge_importance=0.8123 | class=Probabilistic_Methods | Title: Sequential Update of Bayesian Network Structure  
Abstract: There is an obvious need for improving the performance and accuracy of a Bayesian network as new data is observed. Because of errors 
  Node 566 | edge_importance=0.6286 | class=Reinforcement_Learning | Title: Integrated Architectures for Learning, Planning, and Reacting Based on Approximating Dynamic Programming  
Abstract: This paper extends previous work with Dyna, a class of architectures for int
  Node 558 | edge_importance=0.3185 | class=Probabilistic_Methods | Title: A Tutorial on Learning With Bayesian Networks  
Abstract: Technical Report MSR-TR-95-06 

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 699 | edge_importance=0.8442 | class=Reinforcement_Learning | Title: Adaptive state space quantisation for reinforcement learning of collision-free navigation  
Abstract: The paper describes a self-learning control system for a mobile robot. Based on sensor info
  Node 465 | edge_importance=0.842 | class=Reinforcement_Learning | Title: Strategy Learning with Multilayer Connectionist Representations 1  
Abstract: Results are presented that demonstrate the learning and fine-tuning of search strategies using connectionist mechan
  Node 294 | edge_importance=0.8382 | class=Reinforcement_Learning | Title: References elements that can solve difficult learning control problems. on Simulation of Adaptive Behavior, pages
Abstract: Miller, G. (1956). The magical number seven, plus or minus two: Some 
  Node 858 | edge_importance=0.8348 | class=Case_Based | Title: MULTISTRATEGY LEARNING IN REACTIVE CONTROL SYSTEMS FOR AUTONOMOUS ROBOTIC NAVIGATION  
Abstract: This paper presents a self-improving reactive control system for autonomous robotic navigation. 
  Node 671 | edge_importance=0.8316 | class=Reinforcement_Learning | Title: Learning to Achieve Goals  
Abstract: Temporal difference methods solve the temporal credit assignment problem for reinforcement learning. An important subproblem of general reinforcement learn
  Node 2480 | edge_importance=0.8236 | class=Reinforcement_Learning | Title: Planning by Incremental Dynamic Programming  
Abstract: This paper presents the basic results and ideas of dynamic programming as they relate most directly to the concerns of planning in AI. Th
  Node 575 | edge_importance=0.811 | class=Reinforcement_Learning | Title: Issues in Using Function Approximation for Reinforcement Learning  
Abstract: Reinforcement learning techniques address the problem of learning to select actions in unknown, dynamic environment
  Node 552 | edge_importance=0.7918 | class=Reinforcement_Learning | Title: Learning to Act using Real-Time Dynamic Programming  
Abstract: fl The authors thank Rich Yee, Vijay Gullapalli, Brian Pinette, and Jonathan Bachrach for helping to clarify the relationships be
  Node 1378 | edge_importance=0.7559 | class=Reinforcement_Learning | Title: Generalization in Reinforcement Learning: Safely Approximating the Value Function  
Abstract: To appear in: G. Tesauro, D. S. Touretzky and T. K. Leen, eds., Advances in Neural Information Proc
  Node 1447 | edge_importance=0.2626 | class=Reinforcement_Learning | Title: Model of the Environment to Avoid Local Learning  
Abstract: Pier Luca Lanzi Technical Report N. 97.46 December 20 th , 1997 

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

- ID: 1816
- Title: Generalized Prioritized Sweeping
- True class (canonical `y`): **Reinforcement_Learning**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Reinforcement_Learning**
- Prediction recorded by this method's pipeline: **Reinforcement_Learning**

Canonical text (`raw_text`):

~~~~~~text
Title: Generalized Prioritized Sweeping  
Abstract: Prioritized sweeping is a model-based reinforcement learning method that attempts to focus an agent's limited computational resources to achieve a good estimate of the value of environment states. To choose effectively where to spend a costly planning step, classic prioritized sweeping uses a simple heuristic to focus computation on the states that are likely to have the largest errors. In this paper, we introduce generalized prioritized sweeping, a principled method for generating such estimates in a representation-specific manner. This allows us to extend prioritized sweeping beyond an explicit, state-based representation to deal with compact representations that are necessary for dealing with large state spaces. We apply this method for generalized model approximators (such as Bayesian networks), and describe preliminary experiments that compare our approach with classical prioritized sweeping. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 5 nodes

| node id | true class | title |
|---|---|---|
| 558 | Probabilistic_Methods | A Tutorial on Learning With Bayesian Networks |
| 559 | Reinforcement_Learning | Scaling Up Average Reward Reinforcement Learning by Approximating the Domain Models and the Value Function |
| 566 | Reinforcement_Learning | Integrated Architectures for Learning, Planning, and Reacting Based on Approximating Dynamic Programming |
| 1934 | Probabilistic_Methods | Sequential Update of Bayesian Network Structure |
| 2485 | Reinforcement_Learning | Tight Performance Bounds on Greedy Policies Based on Imperfect Value Functions |

### 2-hop (shortest distance exactly 2): 48 nodes

| node id | true class | title |
|---|---|---|
| 16 | Reinforcement_Learning | Exploration in Active Learning |
| 34 | Reinforcement_Learning | Using a Case Base of Surfaces to Speed-Up Reinforcement Learning |
| 76 | Probabilistic_Methods | A VIEW OF THE EM ALGORITHM THAT JUSTIFIES INCREMENTAL, SPARSE, AND OTHER VARIANTS |
| 167 | Reinforcement_Learning | Auto-exploratory Average Reward Reinforcement Learning |
| 173 | Reinforcement_Learning | An Upper Bound on the Loss from Approximate Optimal-Value Functions |
| 186 | Reinforcement_Learning | Adaptive state space quantisation: adding and removing neurons |
| 274 | Reinforcement_Learning | Some Experiments with a Hybrid Model for Learning Sequential Decision Making |
| 294 | Reinforcement_Learning | References elements that can solve difficult learning control problems. on Simulation of Adaptive Behavior, pages |
| 321 | Reinforcement_Learning | Planning with Closed-Loop Macro Actions |
| 333 | Reinforcement_Learning | A Comparison of Action Selection Learning Methods |
| 376 | Probabilistic_Methods | Bayesian Finite Mixtures for Nonlinear Modeling of Educational data |
| 423 | Probabilistic_Methods | LEARNING BAYESIAN NETWORKS WITH LOCAL STRUCTURE |
| 449 | Case_Based | Correcting Imperfect Domain Theories: A Knowledge-Level Analysis |
| 465 | Reinforcement_Learning | Strategy Learning with Multilayer Connectionist Representations 1 |
| 466 | Reinforcement_Learning | On the Computational Economics of Reinforcement Learning |
| 472 | Reinforcement_Learning | Category: Control, Navigation and Planning. Key words: Reinforcement learning, Exploration, Hidden state. Prefer oral presentation. |
| 477 | Reinforcement_Learning | Forward models: Supervised learning with a distal teacher |
| 483 | Reinforcement_Learning | The Parti-game Algorithm for Variable Resolution Reinforcement Learning in Multidimensional State-spaces |
| 552 | Reinforcement_Learning | Learning to Act using Real-Time Dynamic Programming |
| 557 | Probabilistic_Methods | On the Sample Complexity of Learning Bayesian Networks |
| 565 | Reinforcement_Learning | Machine Learning Learning to Predict by the Methods of Temporal Differences Keywords: Incremental learning, prediction, |
| 575 | Reinforcement_Learning | Issues in Using Function Approximation for Reinforcement Learning |
| 588 | Reinforcement_Learning | LEARNING TO AVOID COLLISIONS: A REINFORCEMENT LEARNING PARADIGM FOR MOBILE ROBOT NAVIGATION |
| 633 | Reinforcement_Learning | Chapter 1 Reinforcement Learning for Planning and Control |
| 671 | Reinforcement_Learning | Learning to Achieve Goals |
| 688 | Reinforcement_Learning | Exploration and Model Building in Mobile Robot Domains |
| 699 | Reinforcement_Learning | Adaptive state space quantisation for reinforcement learning of collision-free navigation |
| 733 | Reinforcement_Learning | Evolutionary Differentiation of Learning Abilities a case study on optimizing parameter values in Q-learning by |
| 749 | Reinforcement_Learning | On the Complexity of Solving Markov Decision Problems |
| 858 | Case_Based | MULTISTRATEGY LEARNING IN REACTIVE CONTROL SYSTEMS FOR AUTONOMOUS ROBOTIC NAVIGATION |
| 905 | Probabilistic_Methods | Compositional Modeling With DPNs |
| 1137 | Reinforcement_Learning | Learning Conventions in Multiagent Stochastic Domains using Likelihood Estimates |
| 1378 | Reinforcement_Learning | Generalization in Reinforcement Learning: Safely Approximating the Value Function |
| 1447 | Reinforcement_Learning | Model of the Environment to Avoid Local Learning |
| 1459 | Reinforcement_Learning | Generalized Markov Decision Processes: Dynamic-programming and Reinforcement-learning Algorithms |
| 1532 | Probabilistic_Methods | Automated Decomposition of Model-based Learning Problems |
| 1544 | Genetic_Algorithms | Monitoring in Embedded Agents |
| 1555 | Probabilistic_Methods | Bayesian and Information-Theoretic Priors for Bayesian Network Parameters |
| 1641 | Probabilistic_Methods | Learning Bayesian Networks from Incomplete Data |
| 1643 | Reinforcement_Learning | Learning to coordinate without sharing information |
| 1782 | Reinforcement_Learning | Least-Squares Temporal Difference Learning |
| 2034 | Probabilistic_Methods | Update rules for parameter estimation in Bayesian networks |
| 2221 | Probabilistic_Methods | Reasoning about Time and Probability |
| 2341 | Probabilistic_Methods | Dynamic Belief Networks for Discrete Monitoring |
| 2463 | Probabilistic_Methods | Learning Belief Networks in the Presence of Missing Values and Hidden Variables |
| 2480 | Reinforcement_Learning | Planning by Incremental Dynamic Programming |
| 2658 | Case_Based | Control Systems Magazine, 14, 1, pp.57-71. Robot Juggling: An Implementation of Memory-based Learning |
| 2660 | Probabilistic_Methods | Discovering Structure in Continuous Variables Using Bayesian Networks |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=1816).
Recorded prediction: `{"Target Node": 1816, "Predicted Class": "Reinforcement_Learning", "Confidence": 0.9993}`
Recorded graph stats: `{"total_1hop_degree": 5, "neighbor_label_ratio": {"Reinforcement_Learning": 0.6, "Probabilistic_Methods": 0.4}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | reward | 0.6614 | 1 |
| 2 | generalized | 0.6454 | 1 |
| 3 | method | 0.6439 | 1 |
| 4 | reinforcement | 0.6354 | 1 |
| 5 | function | 0.6345 | 0 |
| 6 | sequenti | 0.634 | 0 |
| 7 | value | 0.6332 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
