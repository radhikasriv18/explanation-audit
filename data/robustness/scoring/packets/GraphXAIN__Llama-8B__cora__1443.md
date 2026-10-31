# Reference packet: GraphXAIN__Llama-8B__cora__1443

- Method: GraphXAIN; configuration: Llama-8B; dataset: cora; target node: 1443
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/cora/graphxain_cora_llama_2hop_narratives_full.json` ([1443])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the given information, our machine learning model predicts the target paper to belong to the class "Reinforcement_Learning" with a high confidence level of 91.81%. The top Binary Word (BOW) features that contribute significantly to this prediction include "instanc," "result," and other related terms like "behavior," "mdp," and "reward." However, upon inspection, we notice that these high-importance words are either absent ("instanc," "result," "behavior") or present ("reward") in the target paper itself. The most influential direct citation neighbor in this case is also strongly associated with the class "Reinforcement_Learning," specifically a paper titled "MultiPlayer Residual Advantage Learning With General Function Approximation," which suggests a close relationship within this topic. Furthermore, another 2-hop neighbor, a paper called "Spurious Solutions to the Bellman Equation," aligns with this pattern, reinforcing the prediction. Overall, the combination of the paper's intrinsic characteristics and its connections with closely related works in the field drive the model towards a strong prediction of the target paper belonging to the class "Reinforcement_Learning." This result implies a significant association between the paper's content and concepts in reinforcement learning.
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

### Target Paper (node 1443):
Title: Residual Q-Learning Applied to Visual Attention  
Abstract: Foveal vision features imagers with graded acuity coupled with context sensitive sensor gaze control, analogous to that prevalent throughout vertebrate vision. Foveal vision operates more efficiently than uniform acuity vision becaus

### Model Prediction:
{
  "Target Node": 1443,
  "Predicted Class": "Reinforcement_Learning",
  "Confidence": 0.9181
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='instanc', importance=0.745, present_in_paper=0
  word='result', importance=0.6963, present_in_paper=0
  word='behavior', importance=0.6848, present_in_paper=0
  word='mdp', importance=0.683, present_in_paper=0
  word='reward', importance=0.6806, present_in_paper=0
  word='littman', importance=0.6756, present_in_paper=1
  word='tempor', importance=0.6643, present_in_paper=0

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 1
Label distribution across all 1-hop neighbors (ground-truth class): Reinforcement_Learning=100.0%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 1540 | edge_importance=0.7926 | class=Reinforcement_Learning | Title: MultiPlayer Residual Advantage Learning With General Function Approximation  
Abstract: A new algorithm, advantage learning, is presented that improves on advantage updating by requiring that a

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 1118 | edge_importance=0.8133 | class=Neural_Networks | Title: Adapting Bias by Gradient Descent: An Incremental Version of Delta-Bar-Delta  
Abstract: Appropriate bias is widely viewed as the key to efficient learning and generalization. I present a new a
  Node 565 | edge_importance=0.7937 | class=Reinforcement_Learning | Title: Machine Learning Learning to Predict by the Methods of Temporal Differences Keywords: Incremental learning, prediction,
Abstract: This article introduces a class of incremental learning procedu
  Node 842 | edge_importance=0.7044 | class=Reinforcement_Learning | Title: Metrics for Temporal Difference Learning  
Abstract: For an absorbing Markov chain with a reinforcement on each transition, Bertsekas (1995a) gives a simple example where the function learned b
  Node 1459 | edge_importance=0.6667 | class=Reinforcement_Learning | Title: Generalized Markov Decision Processes: Dynamic-programming and Reinforcement-learning Algorithms  
Abstract: The problem of maximizing the expected total discounted reward in a completely obser
  Node 1378 | edge_importance=0.6621 | class=Reinforcement_Learning | Title: Generalization in Reinforcement Learning: Safely Approximating the Value Function  
Abstract: To appear in: G. Tesauro, D. S. Touretzky and T. K. Leen, eds., Advances in Neural Information Proc
  Node 1045 | edge_importance=0.6045 | class=Reinforcement_Learning | Title: Spurious Solutions to the Bellman Equation  
Abstract: Reinforcement learning algorithms often work by finding functions that satisfy the Bellman equation. This yields an optimal solution for p

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

- ID: 1443
- Title: Residual Q-Learning Applied to Visual Attention
- True class (canonical `y`): **Reinforcement_Learning**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Reinforcement_Learning**
- Prediction recorded by this method's pipeline: **Reinforcement_Learning**

Canonical text (`raw_text`):

~~~~~~text
Title: Residual Q-Learning Applied to Visual Attention  
Abstract: Foveal vision features imagers with graded acuity coupled with context sensitive sensor gaze control, analogous to that prevalent throughout vertebrate vision. Foveal vision operates more efficiently than uniform acuity vision because resolution is treated as a dynamically allocatable resource, but requires a more refined visual attention mechanism. We demonstrate that reinforcement learning (RL) significantly improves the performance of foveal visual attention, and of the overall vision system, for the task of model based target recognition. A simulated foveal vision system is shown to classify targets with fewer fixations by learning strategies for the acquisition of visual information relevant to the task, and learning how to generalize these strategies in ambiguous and unexpected scenario conditions.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 1540 | Reinforcement_Learning | MultiPlayer Residual Advantage Learning With General Function Approximation |

### 2-hop (shortest distance exactly 2): 6 nodes

| node id | true class | title |
|---|---|---|
| 565 | Reinforcement_Learning | Machine Learning Learning to Predict by the Methods of Temporal Differences Keywords: Incremental learning, prediction, |
| 842 | Reinforcement_Learning | Metrics for Temporal Difference Learning |
| 1045 | Reinforcement_Learning | Spurious Solutions to the Bellman Equation |
| 1118 | Neural_Networks | Adapting Bias by Gradient Descent: An Incremental Version of Delta-Bar-Delta |
| 1378 | Reinforcement_Learning | Generalization in Reinforcement Learning: Safely Approximating the Value Function |
| 1459 | Reinforcement_Learning | Generalized Markov Decision Processes: Dynamic-programming and Reinforcement-learning Algorithms |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=1443).
Recorded prediction: `{"Target Node": 1443, "Predicted Class": "Reinforcement_Learning", "Confidence": 0.9181}`
Recorded graph stats: `{"total_1hop_degree": 1, "neighbor_label_ratio": {"Reinforcement_Learning": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | instanc | 0.745 | 0 |
| 2 | result | 0.6963 | 0 |
| 3 | behavior | 0.6848 | 0 |
| 4 | mdp | 0.683 | 0 |
| 5 | reward | 0.6806 | 0 |
| 6 | littman | 0.6756 | 1 |
| 7 | tempor | 0.6643 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
