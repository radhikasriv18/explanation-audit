# Reference packet: GraphXAIN__Llama-8B__cora__2074

- Method: GraphXAIN; configuration: Llama-8B; dataset: cora; target node: 2074
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/cora/graphxain_cora_llama_2hop_narratives_full.json` ([2074])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Our model predicts that the paper "The Management of Context-Sensitive Features: A Review of Strategies" belongs to the research area of "Theory" with a high level of confidence, at 97.98%. Several key factors contribute to this prediction. Among the top seven Bag-of-Words (BOW) features, four notable ones relate to "methods", "examples", "strategies", and the absence of the word "concept". The presence of these terms strongly associates with theoretical discussions and reviews. Furthermore, our analysis reveals that the paper's direct citation neighbors demonstrate a strong influence in this prediction. Specifically, neighboring papers discussing topics like context-sensitivity, incremental meta-learning, and adaptive neural networks reinforce the idea that the paper pertains to theory rather than practice. Additionally, the distant connections between the target paper and other papers further support this trend, strengthening the model's confidence in assigning the paper to the "Theory" category. These diverse signals collectively point to a theoretical focus in the paper's discussion. By taking into account the content of both the target paper and its variously connected peers, our model arrives at this accurate classification prediction.
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

### Target Paper (node 2074):
Title: The Management of Context-Sensitive Features: A Review of Strategies  
Abstract: In this paper, we review five heuristic strategies for handling context-sensitive features in supervised machine learning from examples. We discuss two methods for recovering lost (implicit) contextual informatio

### Model Prediction:
{
  "Target Node": 2074,
  "Predicted Class": "Theory",
  "Confidence": 0.9798
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='methods', importance=0.6801, present_in_paper=1
  word='examples', importance=0.6548, present_in_paper=1
  word='concept', importance=0.652, present_in_paper=0
  word='consist', importance=0.6402, present_in_paper=0
  word='error', importance=0.637, present_in_paper=0
  word='exploit', importance=0.6366, present_in_paper=0
  word='strategies', importance=0.6366, present_in_paper=1

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 4
Label distribution across all 1-hop neighbors (ground-truth class): Case_Based=50.0%, Theory=25.0%, Neural_Networks=25.0%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 1647 | edge_importance=0.8185 | class=Theory | Title: Recognition and Exploitation of Contextual Clues via Incremental Meta-Learning (Extended Version)  
Abstract: Daily experience shows that in the real world, the meaning of many concepts heavily
  Node 1636 | edge_importance=0.7933 | class=Case_Based | Title: Context-Sensitive Feature Selection for Lazy Learners  
Abstract:  
  Node 2607 | edge_importance=0.7925 | class=Case_Based | Title: Concept Learning and Flexible Weighting  
Abstract: We previously introduced an exemplar model, named GCM-ISW, that exploits a highly flexible weighting scheme. Our simulations showed that it r
  Node 2615 | edge_importance=0.746 | class=Neural_Networks | Title: A Patient-Adaptive Neural Network ECG Patient Monitoring Algorithm  
Abstract: The patient-adaptive classifier was compared with a well-established baseline algorithm on six major databases, co

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 245 | edge_importance=0.8582 | class=Case_Based | Title: ICML-96 Workshop "Learning in context-sensitive domains" Bari, Italy. Dynamically Adjusting Concepts to Accommodate Changing Contexts  
Abstract: In concept learning, objects in a domain are gr
  Node 1073 | edge_importance=0.8215 | class=Rule_Learning | Title: An adaptation of Relief for attribute estimation in regression  
Abstract: Heuristic measures for estimating the quality of attributes mostly assume the independence of attributes so in domains
  Node 1684 | edge_importance=0.8163 | class=Rule_Learning | Title: Context-sensitive attribute estimation in regression  
Abstract: One of key issues in both discrete and continuous class prediction and in machine learning in general seems to be the problem of
  Node 1987 | edge_importance=0.8156 | class=Case_Based | Title: Improving Minority Class Prediction Using Case-Specific Feature Weights  
Abstract: This paper addresses the problem of handling skewed class distributions within the case-based learning (CBL) 
  Node 928 | edge_importance=0.2271 | class=Case_Based | Title: Learning to Refine Case Libraries:  
Abstract: Initial Results Abstract. Conversational case-based reasoning (CBR) systems, which incrementally extract a query description through a user-direct
  Node 1908 | edge_importance=0.2168 | class=Probabilistic_Methods | Title: Induction of Selective Bayesian Classifiers  
Abstract: In this paper, we examine previous work on the naive Bayesian classifier and review its limitations, which include a sensitivity to corre
  Node 2084 | edge_importance=0.193 | class=Neural_Networks | Title: Synthesize, Optimize, Analyze, Repeat (SOAR): Application of Neural Network Tools to ECG Patient Monitoring  
Abstract: Results are reported from the application of tools for synthesizing, opti
  Node 2310 | edge_importance=0.1913 | class=Case_Based | Title: Machine Learning: An Annotated Bibliography for the 1995 AI Statistics Tutorial on Machine Learning (Version 1)  
Abstract: This is a brief annotated bibliography that I wanted to make availabl
  Node 2586 | edge_importance=0.1827 | class=Reinforcement_Learning | Title: Learning One More Thing  
Abstract: Most research on machine learning has focused on scenarios in which a learner faces a single, isolated learning task. The lifelong learning framework assumes
  Node 983 | edge_importance=0.1593 | class=Case_Based | Title: Refining Conversational Case Libraries  
Abstract: Conversational case-based reasoning (CBR) shells (e.g., Inference's CBR Express) are commercially successful tools for supporting the developm

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

- ID: 2074
- Title: The Management of Context-Sensitive Features: A Review of Strategies
- True class (canonical `y`): **Case_Based**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Theory**
- Prediction recorded by this method's pipeline: **Theory**

Canonical text (`raw_text`):

~~~~~~text
Title: The Management of Context-Sensitive Features: A Review of Strategies  
Abstract: In this paper, we review five heuristic strategies for handling context-sensitive features in supervised machine learning from examples. We discuss two methods for recovering lost (implicit) contextual information. We mention some evidence that hybrid strategies can have a synergetic effect. We then show how the work of several machine learning researchers fits into this framework. While we do not claim that these strategies exhaust the possibilities, it appears that the framework includes all of the techniques that can be found in the published literature on context sensitive learning.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 4 nodes

| node id | true class | title |
|---|---|---|
| 1636 | Case_Based | Context-Sensitive Feature Selection for Lazy Learners |
| 1647 | Theory | Recognition and Exploitation of Contextual Clues via Incremental Meta-Learning (Extended Version) |
| 2607 | Case_Based | Concept Learning and Flexible Weighting |
| 2615 | Neural_Networks | A Patient-Adaptive Neural Network ECG Patient Monitoring Algorithm |

### 2-hop (shortest distance exactly 2): 11 nodes

| node id | true class | title |
|---|---|---|
| 245 | Case_Based | ICML-96 Workshop "Learning in context-sensitive domains" Bari, Italy. Dynamically Adjusting Concepts to Accommodate Changing Contexts |
| 928 | Case_Based | Learning to Refine Case Libraries: |
| 983 | Case_Based | Refining Conversational Case Libraries |
| 1073 | Rule_Learning | An adaptation of Relief for attribute estimation in regression |
| 1684 | Rule_Learning | Context-sensitive attribute estimation in regression |
| 1908 | Probabilistic_Methods | Induction of Selective Bayesian Classifiers |
| 1987 | Case_Based | Improving Minority Class Prediction Using Case-Specific Feature Weights |
| 2084 | Neural_Networks | Synthesize, Optimize, Analyze, Repeat (SOAR): Application of Neural Network Tools to ECG Patient Monitoring |
| 2310 | Case_Based | Machine Learning: An Annotated Bibliography for the 1995 AI Statistics Tutorial on Machine Learning (Version 1) |
| 2369 | Case_Based | Case-Based Sonogram Classification |
| 2586 | Reinforcement_Learning | Learning One More Thing |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=2074).
Recorded prediction: `{"Target Node": 2074, "Predicted Class": "Theory", "Confidence": 0.9798}`
Recorded graph stats: `{"total_1hop_degree": 4, "neighbor_label_ratio": {"Case_Based": 0.5, "Theory": 0.25, "Neural_Networks": 0.25}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | methods | 0.6801 | 1 |
| 2 | examples | 0.6548 | 1 |
| 3 | concept | 0.652 | 0 |
| 4 | consist | 0.6402 | 0 |
| 5 | error | 0.637 | 0 |
| 6 | exploit | 0.6366 | 0 |
| 7 | strategies | 0.6366 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
