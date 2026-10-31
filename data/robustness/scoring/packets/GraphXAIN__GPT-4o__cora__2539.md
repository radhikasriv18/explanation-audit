# Reference packet: GraphXAIN__GPT-4o__cora__2539

- Method: GraphXAIN; configuration: GPT-4o; dataset: cora; target node: 2539
- Explanation source: `./robustness_2026-10-30/graphxain_gpt4o/cora/2539.json` (narrative)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The GNN model predicted that the target paper, "Mining for Causes of Cancer: Machine Learning Experiments at Various Levels of Detail," belongs to the "Rule_Learning" class with a high confidence of 0.9979. Among the top bag-of-words features, the words "various," "machine," and "data" were present in the paper and contributed significantly to the model's decision, hinting at the data-driven and machine learning aspects typical of Rule Learning. Despite their high importance, the absence of words like "declar," "theori," and "applic" might have slightly muted the association with other classes such as Theory or Applications. The direct citation neighbors provided a strong influence: one neighbor focusing on "Generating Declarative Language Bias for Top-Down ILP Algorithms" and another on "Inverse entailment and Progol," both reinforcing the Rule Learning classification due to their topics related to inductive logic programming and machine learning methodologies. The 2-hop neighbors further reinforced this pattern, with several papers addressing Inductive Logic Programming (ILP) and related methodologies, which are core to Rule Learning, thus strengthening the association through shared research themes and techniques. This combination of content from the paper's features and the research focus of its citation network effectively steered the prediction towards Rule Learning, reflecting a coherent integration of machine learning topics consistent with the field's methods and interests.
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

### Target Paper (node 2539):
Title: Mining for Causes of Cancer: Machine Learning Experiments at Various Levels of Detail  
Abstract: This paper presents first results of an interdisciplinary project in scientific data mining. We analyze data about the carcinogenicity of chemicals derived from the carcinogenesis bioassay progra

### Model Prediction:
{
  "Target Node": 2539,
  "Predicted Class": "Rule_Learning",
  "Confidence": 0.9979
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='declar', importance=0.6709, present_in_paper=0
  word='theori', importance=0.6579, present_in_paper=0
  word='various', importance=0.6477, present_in_paper=1
  word='machine', importance=0.6466, present_in_paper=1
  word='data', importance=0.6421, present_in_paper=1
  word='applic', importance=0.639, present_in_paper=0
  word='address', importance=0.6343, present_in_paper=0

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 3
Label distribution across all 1-hop neighbors (ground-truth class): Rule_Learning=66.7%, Theory=33.3%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 1322 | edge_importance=0.78 | class=Theory | Title: Theory and Applications of Agnostic PAC-Learning with Small Decision Trees  
Abstract: We exhibit a theoretically founded algorithm T2 for agnostic PAC-learning of decision trees of at most 2 l
  Node 2213 | edge_importance=0.6304 | class=Rule_Learning | Title: Generating Declarative Language Bias for Top-Down ILP Algorithms  
Abstract: Many of today's algorithms for Inductive Logic Programming (ILP) put a heavy burden and responsibility on the user, 
  Node 1428 | edge_importance=0.6275 | class=Rule_Learning | Title: Inverse entailment and Progol  
Abstract: This paper firstly provides a re-appraisal of the development of techniques for inverting deduction, secondly introduces Mode-Directed Inverse Entailme

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 1601 | edge_importance=0.8292 | class=Neural_Networks | Title: Learning the Past Tense of English Verbs: The Symbolic Pattern Associator vs. Connectionist Models  
Abstract: Learning the past tense of English verbs | a seemingly minor aspect of language ac
  Node 1622 | edge_importance=0.8275 | class=Rule_Learning | Title: Stochastic Propositionalization of Non-Determinate Background Knowledge  
Abstract: It is a well-known fact that propositional learning algorithms require "good" features to perform well in pra
  Node 1027 | edge_importance=0.7964 | class=Theory | Title: Pessimistic decision tree pruning based on tree size  
Abstract: In this work we develop a new criteria to perform pessimistic decision tree pruning. Our method is theoretically sound and is ba
  Node 1020 | edge_importance=0.7907 | class=Probabilistic_Methods | Title: Error-Based and Entropy-Based Discretization of Continuous Features  
Abstract: We present a comparison of error-based and entropy-based methods for discretization of continuous features. Our s
  Node 2126 | edge_importance=0.7708 | class=Rule_Learning | Title: Applying ILP to Diterpene Structure Elucidation from 13 C NMR Spectra  
Abstract: We present a novel application of ILP to the problem of diterpene structure elucidation from 13 C NMR spectra. 
  Node 2253 | edge_importance=0.7644 | class=Rule_Learning | Title: Top-down Induction of Logical Decision Trees  
Abstract: A first order framework for top-down induction of logical decision trees is introduced. Logical decision trees are more expressive than 
  Node 2493 | edge_importance=0.7631 | class=Rule_Learning | Title: Relational Knowledge Discovery in Databases  
Abstract: In this paper, we indicate some possible applications of ILP or similar techniques in the knowledge discovery field, and then discuss sev
  Node 2617 | edge_importance=0.7556 | class=Rule_Learning | Title: Predicting Ordinal Classes in ILP  
Abstract: This paper is devoted to the problem of learning to predict ordinal (i.e., ordered discrete) classes in an ILP setting. We start with a relational 
  Node 2290 | edge_importance=0.7481 | class=Rule_Learning | Title: A Comparison of Pruning Methods for Relational Concept Learning  
Abstract: Pre-Pruning and Post-Pruning are two standard methods of dealing with noise in concept learning. Pre-Pruning methods 
  Node 2424 | edge_importance=0.7321 | class=Rule_Learning | Title: Which Hypotheses Can Be Found with Inverse Entailment? -Extended Abstract  
Abstract: In this paper we give a completeness theorem of an inductive inference rule inverse entailment proposed by 

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

- ID: 2539
- Title: Mining for Causes of Cancer: Machine Learning Experiments at Various Levels of Detail
- True class (canonical `y`): **Rule_Learning**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Rule_Learning**
- Prediction recorded by this method's pipeline: **Rule_Learning**

Canonical text (`raw_text`):

~~~~~~text
Title: Mining for Causes of Cancer: Machine Learning Experiments at Various Levels of Detail  
Abstract: This paper presents first results of an interdisciplinary project in scientific data mining. We analyze data about the carcinogenicity of chemicals derived from the carcinogenesis bioassay program performed by the US National Institute of Environmental Health Sciences. The database contains detailed descriptions of 6823 tests performed with more than 330 compounds and animals of different species, strains and sexes. The chemical structures are described at the atom and bond level, and in terms of various relevant structural properties. The goal of this paper is to investigate the effects that various levels of detail and amounts of information have on the resulting hypotheses, both quantitatively and qualitatively. We apply relational and propositional machine learning algorithms to learning problems formulated as regression or as classification tasks. In addition, these experiments have been conducted with two learning problems which are at different levels of detail. Quantitatively, our experiments indicate that additional information not necessarily improves accuracy. Qualitatively, a number of potential discoveries have been made by the algorithm for Relational Regression because it can utilize all the information contained in the relations of the database as well as in the numerical dependent variable. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 3 nodes

| node id | true class | title |
|---|---|---|
| 1322 | Theory | Theory and Applications of Agnostic PAC-Learning with Small Decision Trees |
| 1428 | Rule_Learning | Inverse entailment and Progol |
| 2213 | Rule_Learning | Generating Declarative Language Bias for Top-Down ILP Algorithms |

### 2-hop (shortest distance exactly 2): 16 nodes

| node id | true class | title |
|---|---|---|
| 323 | Theory | Learning Active Classifiers |
| 1020 | Probabilistic_Methods | Error-Based and Entropy-Based Discretization of Continuous Features |
| 1027 | Theory | Pessimistic decision tree pruning based on tree size |
| 1259 | Rule_Learning | Finding Accurate Frontiers: A Knowledge-Intensive Approach to Relational Learning |
| 1312 | Rule_Learning | Learning Trees and Rules with Set-valued Features |
| 1601 | Neural_Networks | Learning the Past Tense of English Verbs: The Symbolic Pattern Associator vs. Connectionist Models |
| 1622 | Rule_Learning | Stochastic Propositionalization of Non-Determinate Background Knowledge |
| 2079 | Rule_Learning | Extraction of Meta-Knowledge to Restrict the Hypothesis Space for ILP Systems incorporating them in FOIL. |
| 2126 | Rule_Learning | Applying ILP to Diterpene Structure Elucidation from 13 C NMR Spectra |
| 2229 | Rule_Learning | Bottom-up induction of logic programs with more than one recursive clause |
| 2253 | Rule_Learning | Top-down Induction of Logical Decision Trees |
| 2290 | Rule_Learning | A Comparison of Pruning Methods for Relational Concept Learning |
| 2329 | Theory | Programming Research Group A LEARNABILITY MODEL FOR UNIVERSAL REPRESENTATIONS |
| 2424 | Rule_Learning | Which Hypotheses Can Be Found with Inverse Entailment? -Extended Abstract |
| 2493 | Rule_Learning | Relational Knowledge Discovery in Databases |
| 2617 | Rule_Learning | Predicting Ordinal Classes in ILP |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=2539).
Recorded prediction: `{"Target Node": 2539, "Predicted Class": "Rule_Learning", "Confidence": 0.9979}`
Recorded graph stats: `{"total_1hop_degree": 3, "neighbor_label_ratio": {"Rule_Learning": 0.667, "Theory": 0.333}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | declar | 0.6709 | 0 |
| 2 | theori | 0.6579 | 0 |
| 3 | various | 0.6477 | 1 |
| 4 | machine | 0.6466 | 1 |
| 5 | data | 0.6421 | 1 |
| 6 | applic | 0.639 | 0 |
| 7 | address | 0.6343 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
