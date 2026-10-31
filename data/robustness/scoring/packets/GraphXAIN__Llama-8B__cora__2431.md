# Reference packet: GraphXAIN__Llama-8B__cora__2431

- Method: GraphXAIN; configuration: Llama-8B; dataset: cora; target node: 2431
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/cora/graphxain_cora_llama_2hop_narratives_full.json` ([2431])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model confidently predicts the target paper (node 2431) to belong to the 'Rule_Learning' category with a perfect confidence score of 1.0. The key contributing factor to this prediction lies in the presence of important Bag-of-Words (BOW) features such as'mostly', 'applications', and 'ILP' which are all present in the paper's title and abstract. Additionally, direct citation neighbors like nodes 426, 2426, and 2591, which deal with topics related to rule induction and ILP, strongly reinforced this classification, highlighting the significance of collaboration among researchers working within this specific domain. The fact that all 1-hop neighbors are classified under 'Rule_Learning' supports the model's prediction. Furthermore, 2-hop neighbors with connections to ILP and rule-based reasoning also contribute positively, emphasizing the relevance of these concepts in the broader community of academics cited within the target paper's network. Overall, the accumulation of these supportive indicators demonstrates how the model's prediction of 'Rule_Learning' emerges from both local paper characteristics and structural patterns across the citation graph. By integrating diverse sources of information, the model achieves robust accuracy in this classification task.
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

### Target Paper (node 2431):
Title: Multi-class problems and discretization in ICL Extended abstract  
Abstract: Handling multi-class problems and real numbers is important in practical applications of machine learning to KDD problems. While attribute-value learners address these problems as a rule, very few ILP systems do so. 

### Model Prediction:
{
  "Target Node": 2431,
  "Predicted Class": "Rule_Learning",
  "Confidence": 1.0
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='mostly', importance=0.671, present_in_paper=1
  word='applications', importance=0.6534, present_in_paper=1
  word='ilp', importance=0.648, present_in_paper=1
  word='induct', importance=0.6428, present_in_paper=0
  word='logic', importance=0.6414, present_in_paper=0
  word='address', importance=0.6211, present_in_paper=1
  word='trying', importance=0.6207, present_in_paper=1

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 4
Label distribution across all 1-hop neighbors (ground-truth class): Rule_Learning=100.0%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 426 | edge_importance=0.8183 | class=Rule_Learning | Title: Rule Induction with CN2: Some Recent Improvements  
Abstract: The CN2 algorithm induces an ordered list of classification rules from examples using entropy as its search heuristic. In this shor
  Node 2426 | edge_importance=0.7425 | class=Rule_Learning | Title: Inductive Constraint Logic  
Abstract: A novel approach to learning first order logic formulae from positive and negative examples is presented. Whereas present inductive logic programming syst
  Node 2591 | edge_importance=0.7121 | class=Rule_Learning | Title: Lookahead and Discretization in ILP  
Abstract: We present and evaluate two methods for improving the performance of ILP systems. One of them is discretization of numerical attributes, based on
  Node 1919 | edge_importance=0.5849 | class=Rule_Learning | Title: Inductive Constraint Logic and the Mutagenesis Problem  
Abstract: A novel approach to learning first order logic formulae from positive and negative examples is incorporated in a system named 

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 836 | edge_importance=0.8239 | class=Theory | Title: Unsupervised Constructive Learning  
Abstract: In constructive induction (CI), the learner's problem representation is modified as a normal part of the learning process. This is useful when the
  Node 318 | edge_importance=0.8229 | class=Case_Based | Title: Generalizing from Case Studies: A Case Study  
Abstract: Most empirical evaluations of machine learning algorithms are case studies evaluations of multiple algorithms on multiple databases. Aut
  Node 303 | edge_importance=0.818 | class=Case_Based | Title: Relating Relational Learning Algorithms  
Abstract: Relational learning algorithms are of special interest to members of the machine learning community; they offer practical methods for extendi
  Node 2253 | edge_importance=0.8131 | class=Rule_Learning | Title: Top-down Induction of Logical Decision Trees  
Abstract: A first order framework for top-down induction of logical decision trees is introduced. Logical decision trees are more expressive than 
  Node 2126 | edge_importance=0.8032 | class=Rule_Learning | Title: Applying ILP to Diterpene Structure Elucidation from 13 C NMR Spectra  
Abstract: We present a novel application of ILP to the problem of diterpene structure elucidation from 13 C NMR spectra. 
  Node 937 | edge_importance=0.2334 | class=Case_Based | Title: The RISE System: Conquering Without Separating  
Abstract: Current rule induction systems (e.g. CN2) typically rely on a "separate and conquer" strategy, learning each rule only from still-unco
  Node 1486 | edge_importance=0.2296 | class=Rule_Learning | Title: Induction of decision trees and Bayesian classification applied to diagnosis of sport injuries  
Abstract: Machine learning techniques can be used to extract knowledge from data stored in medic
  Node 344 | edge_importance=0.2291 | class=Rule_Learning | Title: Quinlan, 1990 J.R. Quinlan. Learning logical definitions from relations. Machine Learning, First-order theory revision. In
Abstract: We describe a ranked-model semantics for if-then rules admit
  Node 638 | edge_importance=0.228 | class=Theory | Title: Learning a set of primitive actions with an Induction of decision trees. Machine Learning, 1(1):81-106,
Abstract: Although probabilistic inference in a general Bayesian belief network is an NP-
  Node 2427 | edge_importance=0.2249 | class=Neural_Networks | Title: Solving the Multiple-Instance Problem with Axis-Parallel Rectangles  
Abstract: The multiple instance problem arises in tasks where the training examples are ambiguous: a single example object 

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

- ID: 2431
- Title: Multi-class problems and discretization in ICL Extended abstract
- True class (canonical `y`): **Rule_Learning**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Rule_Learning**
- Prediction recorded by this method's pipeline: **Rule_Learning**

Canonical text (`raw_text`):

~~~~~~text
Title: Multi-class problems and discretization in ICL Extended abstract  
Abstract: Handling multi-class problems and real numbers is important in practical applications of machine learning to KDD problems. While attribute-value learners address these problems as a rule, very few ILP systems do so. The few ILP systems that handle real numbers mostly do so by trying out all real values that are applicable, thus running into efficiency or overfitting problems. This paper discusses some recent extensions of ICL that address these problems. ICL, which stands for Inductive Constraint Logic, is an ILP system that learns first order logic formulae from positive and negative examples. The main charateristic of ICL is its view on examples. These are seen as interpretations which are true or false for the clausal target theory (in CNF). We first argue that ICL can be used for learning a theory in a disjunctive normal form (DNF). With this in mind, a possible solution for handling more than two classes is given (based on some ideas from CN2). Finally, we show how to tackle problems with continuous values by adapting discretization techniques from attribute value learners. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 4 nodes

| node id | true class | title |
|---|---|---|
| 426 | Rule_Learning | Rule Induction with CN2: Some Recent Improvements |
| 1919 | Rule_Learning | Inductive Constraint Logic and the Mutagenesis Problem |
| 2426 | Rule_Learning | Inductive Constraint Logic |
| 2591 | Rule_Learning | Lookahead and Discretization in ILP |

### 2-hop (shortest distance exactly 2): 22 nodes

| node id | true class | title |
|---|---|---|
| 29 | Rule_Learning | Stochastically Guided Disjunctive Version Space Learning |
| 303 | Case_Based | Relating Relational Learning Algorithms |
| 318 | Case_Based | Generalizing from Case Studies: A Case Study |
| 335 | Rule_Learning | Incremental Reduced Error Pruning |
| 344 | Rule_Learning | Quinlan, 1990 J.R. Quinlan. Learning logical definitions from relations. Machine Learning, First-order theory revision. In |
| 638 | Theory | Learning a set of primitive actions with an Induction of decision trees. Machine Learning, 1(1):81-106, |
| 836 | Theory | Unsupervised Constructive Learning |
| 937 | Case_Based | The RISE System: Conquering Without Separating |
| 1007 | Rule_Learning | Applications of a logical discovery engine |
| 1061 | Rule_Learning | Stochastic search in inductive concept learning |
| 1187 | Theory | Rationality and Intelligence |
| 1275 | Rule_Learning | Fossil: A Robust Relational Learner |
| 1486 | Rule_Learning | Induction of decision trees and Bayesian classification applied to diagnosis of sport injuries |
| 1528 | Rule_Learning | Using Qualitative Models to Guide Inductive Learning |
| 1576 | Theory | What do Constructive Learners Really Learn? |
| 1686 | Rule_Learning | Learning with Abduction |
| 2126 | Rule_Learning | Applying ILP to Diterpene Structure Elucidation from 13 C NMR Spectra |
| 2253 | Rule_Learning | Top-down Induction of Logical Decision Trees |
| 2282 | Rule_Learning | The ILP description learning problem: Towards a general model-level definition of data mining in ILP |
| 2369 | Case_Based | Case-Based Sonogram Classification |
| 2427 | Neural_Networks | Solving the Multiple-Instance Problem with Axis-Parallel Rectangles |
| 2493 | Rule_Learning | Relational Knowledge Discovery in Databases |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=2431).
Recorded prediction: `{"Target Node": 2431, "Predicted Class": "Rule_Learning", "Confidence": 1.0}`
Recorded graph stats: `{"total_1hop_degree": 4, "neighbor_label_ratio": {"Rule_Learning": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | mostly | 0.671 | 1 |
| 2 | applications | 0.6534 | 1 |
| 3 | ilp | 0.648 | 1 |
| 4 | induct | 0.6428 | 0 |
| 5 | logic | 0.6414 | 0 |
| 6 | address | 0.6211 | 1 |
| 7 | trying | 0.6207 | 1 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
