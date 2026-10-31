# Reference packet: GraphXAIN__GPT-4o__cora__2257

- Method: GraphXAIN; configuration: GPT-4o; dataset: cora; target node: 2257
- Explanation source: `./robustness_2026-10-30/graphxain_gpt4o/cora/2257.json` (narrative)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model predicted that the target paper, "Real-time Interactive Neuro-evolution," falls under the "Reinforcement_Learning" category with a high confidence of 98.8%. The paper prominently features terms like "population" and "interactive," which are often associated with evolutionary techniques, and "handle," which ties into adaptive systems, both present in the paper and aligning with topics found in reinforcement learning research. Words such as "future" also contribute by indicating the forward-thinking aspect of reinforcement strategies. The paper’s citation network further strengthens the prediction: key direct citation neighbors are heavily focused on reinforcement learning, including papers like "Incremental Evolution of Complex General Behavior" and "Machine Learning, Efficient Reinforcement Learning through Symbiotic Evolution," which all explore neuro-evolution and adaptive systems. These connections suggest a thematic alignment between the target paper and its cited works. Additionally, many influential 2-hop neighbors, such as "Evolving Obstacle Avoidance Behavior in a Robot Arm," are rooted in reinforcement learning, reinforcing the thematic presence across the citation network. The strong presence of reinforcement learning themes in both direct and indirect citations indicates a consistent focus on adaptive and evolutionary learning, supporting the model's confident classification.
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

### Target Paper (node 2257):
Title: Real-time Interactive Neuro-evolution  
Abstract: In standard neuro-evolution, a population of networks is evolved in the task, and the network that best solves the task is found. This network is then fixed and used to solve future instances of the problem. Networks evolved in this way do not

### Model Prediction:
{
  "Target Node": 2257,
  "Predicted Class": "Reinforcement_Learning",
  "Confidence": 0.988
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='population', importance=0.6695, present_in_paper=1
  word='need', importance=0.6563, present_in_paper=0
  word='interactive', importance=0.6543, present_in_paper=1
  word='future', importance=0.6535, present_in_paper=1
  word='complex', importance=0.6512, present_in_paper=0
  word='handle', importance=0.6512, present_in_paper=1
  word='peg', importance=0.641, present_in_paper=1

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 5
Label distribution across all 1-hop neighbors (ground-truth class): Reinforcement_Learning=80.0%, Genetic_Algorithms=20.0%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 1767 | edge_importance=0.7848 | class=Reinforcement_Learning | Title: Incremental Evolution of Complex General Behavior  
Abstract: Several researchers have demonstrated how complex action sequences can be learned through neuro-evolution (i.e. evolving neural net
  Node 22 | edge_importance=0.7735 | class=Genetic_Algorithms | Title: Discovering Complex Othello Strategies Through Evolutionary Neural Networks  
Abstract: An approach to develop new game playing strategies based on artificial evolution of neural networks is pr
  Node 2444 | edge_importance=0.7582 | class=Reinforcement_Learning | Title: Symbiotic Evolution of Neural Networks in Sequential Decision Tasks  
Abstract: The simple Bayesian classifier (SBC), sometimes called Naive-Bayes, is built based on a conditional independence 
  Node 247 | edge_importance=0.741 | class=Reinforcement_Learning | Title: Machine Learning,  Efficient Reinforcement Learning through Symbiotic Evolution  
Abstract: This article presents a new reinforcement learning method called SANE (Symbiotic, Adaptive Neuro-Evol
  Node 1768 | edge_importance=0.735 | class=Reinforcement_Learning | Title: Evolving Neural Networks to Play Go  
Abstract: Go is a difficult game for computers to master, and the best go programs are still weaker than the average human player. Since the traditional ga

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 563 | edge_importance=0.8164 | class=Reinforcement_Learning | Title: Evolving Obstacle Avoidance Behavior in a Robot Arm  
Abstract: Existing approaches for learning to control a robot arm rely on supervised methods where correct behavior is explicitly given. It
  Node 500 | edge_importance=0.7819 | class=Reinforcement_Learning | Title: 2-D Pole Balancing with Recurrent Evolutionary Networks  
Abstract: The success of evolutionary methods on standard control learning tasks has created a need for new benchmarks. The classic pol
  Node 163 | edge_importance=0.2972 | class=Genetic_Algorithms | Title: 4 Implementing Application Specific Routines  Genetic algorithms in search, optimization, and machine learning. Reading, MA: Addison-Wesley.  
Abstract: To implement a specific application, you
  Node 191 | edge_importance=0.2273 | class=Genetic_Algorithms | Title: USING MARKER-BASED GENETIC ENCODING OF NEURAL NETWORKS TO EVOLVE FINITE-STATE BEHAVIOUR  
Abstract: A new mechanism for genetic encoding of neural networks is proposed, which is loosely based o
  Node 1790 | edge_importance=0.2254 | class=Genetic_Algorithms | Title: Using Genetic Programming to Evolve Board Evaluation Functions  
Abstract: The purpose of most architecture optimization schemes is to improve generalization. In this presentation we suggest to
  Node 1261 | edge_importance=0.2138 | class=Genetic_Algorithms | Title: EVOLVING NEURAL NETWORKS WITH COLLABORATIVE SPECIES  
Abstract: We present a coevolutionary architecture for solving decomposable problems and apply it to the evolution of artificial neural net
  Node 129 | edge_importance=0.2138 | class=Genetic_Algorithms | Title: Evolving Networks: Using the Genetic Algorithm with Connectionist Learning  
Abstract: A pilot study is described on the practical application of artificial neural networks. The limit cycle of 
  Node 1973 | edge_importance=0.2063 | class=Genetic_Algorithms | Title: ON MCMC METHODS IN BAYESIAN REGRESSION ANALYSIS AND MODEL SELECTION  
Abstract: 1] R.K. Belew, J. McInerney, and N. Schraudolph, Evolving networks: using the genetic algorithm with connectionis
  Node 982 | edge_importance=0.2019 | class=Genetic_Algorithms | Title: Evolutionary Neural Networks for Value Ordering in Constraint Satisfaction Problems  
Abstract: Technical Report AI94-218 May 1994 Abstract A new method for developing good value-ordering strat
  Node 2446 | edge_importance=0.1817 | class=Genetic_Algorithms | Title: Simulation of Reduced Precision Arithmetic for Digital Neural Networks Using the RAP Machine  
Abstract: 1] R.K. Belew, J. McInerney, and N. Schraudolph, Evolving networks: using the genetic al

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

- ID: 2257
- Title: Real-time Interactive Neuro-evolution
- True class (canonical `y`): **Genetic_Algorithms**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Reinforcement_Learning**
- Prediction recorded by this method's pipeline: **Reinforcement_Learning**

Canonical text (`raw_text`):

~~~~~~text
Title: Real-time Interactive Neuro-evolution  
Abstract: In standard neuro-evolution, a population of networks is evolved in the task, and the network that best solves the task is found. This network is then fixed and used to solve future instances of the problem. Networks evolved in this way do not handle real-time interaction very well. It is hard to evolve a solution ahead of time that can cope effectively with all the possible environments that might arise in the future and with all the possible ways someone may interact with it. This paper proposes evolving feedforward neural networks online to create agents that improve their performance through real-time interaction. This approach is demonstrated in a game world where neural-network-controlled individuals play against humans. Through evolution, these individuals learn to react to varying opponents while appropriately taking into account conflicting goals. After initial evaluation offline, the population is allowed to evolve online, and its performance improves considerably. The population not only adapts to novel situations brought about by changing strategies in the opponent and the game layout, but it also improves its performance in situations that it has already seen in offline training. This paper will describe an implementation of online evolution and shows that it is a practical method that exceeds the performance of offline evolution alone. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 5 nodes

| node id | true class | title |
|---|---|---|
| 22 | Genetic_Algorithms | Discovering Complex Othello Strategies Through Evolutionary Neural Networks |
| 247 | Reinforcement_Learning | Machine Learning,  Efficient Reinforcement Learning through Symbiotic Evolution |
| 1767 | Reinforcement_Learning | Incremental Evolution of Complex General Behavior |
| 1768 | Reinforcement_Learning | Evolving Neural Networks to Play Go |
| 2444 | Reinforcement_Learning | Symbiotic Evolution of Neural Networks in Sequential Decision Tasks |

### 2-hop (shortest distance exactly 2): 11 nodes

| node id | true class | title |
|---|---|---|
| 129 | Genetic_Algorithms | Evolving Networks: Using the Genetic Algorithm with Connectionist Learning |
| 163 | Genetic_Algorithms | 4 Implementing Application Specific Routines  Genetic algorithms in search, optimization, and machine learning. Reading, MA: Addison-Wesley. |
| 191 | Genetic_Algorithms | USING MARKER-BASED GENETIC ENCODING OF NEURAL NETWORKS TO EVOLVE FINITE-STATE BEHAVIOUR |
| 500 | Reinforcement_Learning | 2-D Pole Balancing with Recurrent Evolutionary Networks |
| 563 | Reinforcement_Learning | Evolving Obstacle Avoidance Behavior in a Robot Arm |
| 982 | Genetic_Algorithms | Evolutionary Neural Networks for Value Ordering in Constraint Satisfaction Problems |
| 1117 | Genetic_Algorithms | A Coevolutionary Approach to Learning Sequential Decision Rules |
| 1261 | Genetic_Algorithms | EVOLVING NEURAL NETWORKS WITH COLLABORATIVE SPECIES |
| 1790 | Genetic_Algorithms | Using Genetic Programming to Evolve Board Evaluation Functions |
| 1973 | Genetic_Algorithms | ON MCMC METHODS IN BAYESIAN REGRESSION ANALYSIS AND MODEL SELECTION |
| 2446 | Genetic_Algorithms | Simulation of Reduced Precision Arithmetic for Digital Neural Networks Using the RAP Machine |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=2257).
Recorded prediction: `{"Target Node": 2257, "Predicted Class": "Reinforcement_Learning", "Confidence": 0.988}`
Recorded graph stats: `{"total_1hop_degree": 5, "neighbor_label_ratio": {"Reinforcement_Learning": 0.8, "Genetic_Algorithms": 0.2}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | population | 0.6695 | 1 |
| 2 | need | 0.6563 | 0 |
| 3 | interactive | 0.6543 | 1 |
| 4 | future | 0.6535 | 1 |
| 5 | complex | 0.6512 | 0 |
| 6 | handle | 0.6512 | 1 |
| 7 | peg | 0.641 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
