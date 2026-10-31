# Reference packet: GraphXAIN__GPT-4o__cora__2635

- Method: GraphXAIN; configuration: GPT-4o; dataset: cora; target node: 2635
- Explanation source: `./robustness_2026-10-30/graphxain_gpt4o/cora/2635.json` (narrative)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model confidently predicted that paper 2635 belongs to the "Case_Based" research area with a high confidence of 99.69%. This decision was primarily influenced by the presence of key words like "explanation" and "assist," which are heavily associated with Case-Based reasoning and were found in the paper. Although the words "knowledge," "given," "article," "attempt," and "basis" were not present, their conceptual connection to problem-solving and explanation likely pushed the classification towards Case-Based reasoning. Further supporting this prediction, one of the target paper's direct neighbors is a paper titled "Explaining Anomalies as a Basis for Knowledge Base Refinement," which is classified under "Case_Based" and underlines the theme of using explanations for understanding and refining knowledge systems. Another direct neighbor, "Theory Refinement Combining Analytical and Empirical Methods," belongs to "Rule_Learning" but introduces concepts that overlap with case-based methods, such as theory refinement and empirical analysis. Additionally, 2-hop neighbors, like papers titled "References Automatic student modeling and bug library construction using theory refinement" and "Abduction, Experience, and Goals: A Model of Everyday Abductive Explanation," further underscore the emphasis on explanation and refinement, both central to Case-Based systems. These factors combined lead the model to conclude that the paper's thematic core aligns most closely with the Case-Based category.
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

### Target Paper (node 2635):
Title: Utilising Explanation to Assist the Refinement of Knowledge-Based Systems  
Abstract: Standard statistical practice ignores model uncertainty. Data analysts typically select a model from some class of models and then proceed as if the selected model had generated the data. This approach ignor

### Model Prediction:
{
  "Target Node": 2635,
  "Predicted Class": "Case_Based",
  "Confidence": 0.9969
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='explanation', importance=0.661, present_in_paper=1
  word='assist', importance=0.6532, present_in_paper=1
  word='knowledg', importance=0.6515, present_in_paper=0
  word='given', importance=0.6513, present_in_paper=0
  word='articl', importance=0.6439, present_in_paper=0
  word='attempt', importance=0.6355, present_in_paper=0
  word='basi', importance=0.6352, present_in_paper=0

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 2
Label distribution across all 1-hop neighbors (ground-truth class): Rule_Learning=50.0%, Case_Based=50.0%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 2231 | edge_importance=0.8346 | class=Case_Based | Title: Explaining Anomalies as a Basis for Knowledge Base Refinement  
Abstract: Explanations play a key role in operationalization-based anomaly detection techniques. In this paper we show that their
  Node 136 | edge_importance=0.6783 | class=Rule_Learning | Title: Theory Refinement Combining Analytical and Empirical Methods  
Abstract: This article describes a comprehensive approach to automatic theory revision. Given an imperfect theory, the approach co

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 1413 | edge_importance=0.8383 | class=Case_Based | Title: References Automatic student modeling and bug library construction using theory refinement. Ph.D. ml/ Symbolic revision
Abstract: ASSERT demonstrates how theory refinement techniques developed 
  Node 244 | edge_importance=0.8322 | class=Neural_Networks | Title: Building Intelligent Agents for Web-Based Tasks: A Theory-Refinement Approach  
Abstract: We present and evaluate an infrastructure with which to rapidly and easily build intelligent software a
  Node 1539 | edge_importance=0.812 | class=Rule_Learning | Title: Finding new rules for incomplete theories: Explicit biases for induction with contextual information. In Proceedings
Abstract: addressed in KBANN (which translates a theory into a neural-net, r
  Node 1102 | edge_importance=0.8089 | class=Rule_Learning | Title: Automated Refinement of First-Order Horn-Clause Domain Theories  
Abstract: Knowledge acquisition is a difficult, error-prone, and time-consuming task. The task of automatically improving an ex
  Node 479 | edge_importance=0.8064 | class=Case_Based | Title: Learning physical descriptions from functional definitions, examples, Learning from examples: The effect of different conceptual
Abstract: Technical Report 94-07 February 7, 1994 (updated April
  Node 92 | edge_importance=0.8053 | class=Reinforcement_Learning | Title: Learning Analytically and Inductively  
Abstract: Learning is a fundamental component of intelligence, and a key consideration in designing cognitive architectures such as Soar [ Laird et al., 
  Node 2399 | edge_importance=0.8015 | class=Case_Based | Title: Abduction, Experience, and Goals: A Model of Everyday Abductive Explanation*  
Abstract: When a reasoner explains surprising events for its internal use, a key motivation for explaining is to p
  Node 1259 | edge_importance=0.2328 | class=Rule_Learning | Title: Finding Accurate Frontiers: A Knowledge-Intensive Approach to Relational Learning  
Abstract: An approach to analytic learning is described that searches for accurate entailments of a Horn Clau
  Node 1479 | edge_importance=0.2213 | class=Probabilistic_Methods | Title: Revising Bayesian Network Parameters Using Backpropagation  
Abstract: The problem of learning Bayesian networks with hidden variables is known to be a hard problem. Even the simpler task of le
  Node 2487 | edge_importance=0.2187 | class=Theory | Title: An Optimized Theory Revision Module  
Abstract: Theory revision systems typically use a set of theory-to-theory transformations f k g to hill-climb from a given initial theory to a new theory w

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

- ID: 2635
- Title: Utilising Explanation to Assist the Refinement of Knowledge-Based Systems
- True class (canonical `y`): **Case_Based**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Case_Based**
- Prediction recorded by this method's pipeline: **Case_Based**

Canonical text (`raw_text`):

~~~~~~text
Title: Utilising Explanation to Assist the Refinement of Knowledge-Based Systems  
Abstract: Standard statistical practice ignores model uncertainty. Data analysts typically select a model from some class of models and then proceed as if the selected model had generated the data. This approach ignores the uncertainty in model selection, leading to over-confident inferences and decisions that are more risky than one thinks they are. Bayesian model averaging (BMA) provides a coherent mechanism for accounting for this model uncertainty. Several methods for implementing BMA have recently emerged. We discuss these methods and present a number of examples. In these examples, BMA provides improved out-of-sample predictive performance. We also provide a catalogue of currently available BMA software. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 2 nodes

| node id | true class | title |
|---|---|---|
| 136 | Rule_Learning | Theory Refinement Combining Analytical and Empirical Methods |
| 2231 | Case_Based | Explaining Anomalies as a Basis for Knowledge Base Refinement |

### 2-hop (shortest distance exactly 2): 17 nodes

| node id | true class | title |
|---|---|---|
| 92 | Reinforcement_Learning | Learning Analytically and Inductively |
| 159 | Theory | Bias-Driven Revision of Logical Domain Theories |
| 244 | Neural_Networks | Building Intelligent Agents for Web-Based Tasks: A Theory-Refinement Approach |
| 479 | Case_Based | Learning physical descriptions from functional definitions, examples, Learning from examples: The effect of different conceptual |
| 986 | Case_Based | Improving accuracy by combining rule-based and case-based reasoning |
| 1102 | Rule_Learning | Automated Refinement of First-Order Horn-Clause Domain Theories |
| 1259 | Rule_Learning | Finding Accurate Frontiers: A Knowledge-Intensive Approach to Relational Learning |
| 1370 | Rule_Learning | From Theory Refinement to KB Maintenance: a Position Statement |
| 1413 | Case_Based | References Automatic student modeling and bug library construction using theory refinement. Ph.D. ml/ Symbolic revision |
| 1479 | Probabilistic_Methods | Revising Bayesian Network Parameters Using Backpropagation |
| 1539 | Rule_Learning | Finding new rules for incomplete theories: Explicit biases for induction with contextual information. In Proceedings |
| 1776 | Rule_Learning | Extending Theory Refinement to M-of-N Rules |
| 2172 | Theory | Tractability of Theory Patching |
| 2399 | Case_Based | Abduction, Experience, and Goals: A Model of Everyday Abductive Explanation* |
| 2487 | Theory | An Optimized Theory Revision Module |
| 2543 | Probabilistic_Methods | Combining Connectionist and Symbolic Learning to Refine Certainty-Factor Rule Bases |
| 2580 | Theory | The Challenge of Revising an Impure Theory |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=2635).
Recorded prediction: `{"Target Node": 2635, "Predicted Class": "Case_Based", "Confidence": 0.9969}`
Recorded graph stats: `{"total_1hop_degree": 2, "neighbor_label_ratio": {"Rule_Learning": 0.5, "Case_Based": 0.5}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | explanation | 0.661 | 1 |
| 2 | assist | 0.6532 | 1 |
| 3 | knowledg | 0.6515 | 0 |
| 4 | given | 0.6513 | 0 |
| 5 | articl | 0.6439 | 0 |
| 6 | attempt | 0.6355 | 0 |
| 7 | basi | 0.6352 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
