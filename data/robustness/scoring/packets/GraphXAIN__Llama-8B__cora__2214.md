# Reference packet: GraphXAIN__Llama-8B__cora__2214

- Method: GraphXAIN; configuration: Llama-8B; dataset: cora; target node: 2214
- Explanation source: `./graphxain_schemaaligned_production_2026-08-16/cora/graphxain_cora_llama_2hop_narratives_full.json` ([2214])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model confidently predicted the target paper, titled "Behavior Near Zero of the Distribution of GCV Smoothing Parameter Estimates," to belong to the "Neural Networks" category, with a high confidence level of 99.06%. Key factors contributing to this prediction were several high-importance words present in the paper itself, including "smoothing", which suggests a connection to the technical aspects of neural networks. Notably, "error" was strongly associated with the predicted category despite being absent from the paper itself, implying a deep connection between error correction and neural networks. Additionally, direct citation neighbors such as "Sample Size Calculations for Smoothing Splines" and "Smoothing Spline Models with Correlated Random Errors" reinforced this prediction, as they both belonged to the same category. Furthermore, these influential neighbors were heavily linked to techniques like smoothing splines and random errors, which are all critical components of neural network design. While 2-hop neighbors presented some conflicting signals, the overwhelming majority of the evidence pointed towards a strong link between the target paper's content and the "Neural Networks" category. Overall, the combination of key BOW features, direct citation connections, and related topics led the model to make this confident prediction.
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

### Target Paper (node 2214):
Title: Behavior Near Zero of the Distribution of GCV Smoothing Parameter Estimates 1  
Abstract: Many of today's algorithms for Inductive Logic Programming (ILP) put a heavy burden and responsibility on the user, because their declarative bias have to be defined in a rather low-level fashion. To add

### Model Prediction:
{
  "Target Node": 2214,
  "Predicted Class": "Neural_Networks",
  "Confidence": 0.9906
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='smoothing', importance=0.6898, present_in_paper=1
  word='error', importance=0.6765, present_in_paper=0
  word='correl', importance=0.6658, present_in_paper=0
  word='random', importance=0.6634, present_in_paper=0
  word='confid', importance=0.6619, present_in_paper=0
  word='spline', importance=0.6549, present_in_paper=0
  word='anova', importance=0.6436, present_in_paper=0

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 2
Label distribution across all 1-hop neighbors (ground-truth class): Neural_Networks=100.0%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 420 | edge_importance=0.8586 | class=Neural_Networks | Title: Sample Size Calculations for Smoothing Splines Based on Bayesian Confidence Intervals  
Abstract: Bayesian confidence intervals of a smoothing spline are often used to distinguish two curves. I
  Node 2223 | edge_importance=0.8399 | class=Neural_Networks | Title: Smoothing Spline Models With Correlated Random Errors 1  
Abstract: Reinforcement learning can be used not only to predict rewards, but also to predict states, i.e. to learn a model of the worl

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 190 | edge_importance=0.8382 | class=Neural_Networks | Title: Spline Smoothing For Bivariate Data With Applications To Association Between Hormones  
Abstract: Standard methods for inducing both the structure and weight values of recurrent neural networks
  Node 2590 | edge_importance=0.8348 | class=Probabilistic_Methods | Title: Backfitting in Smoothing Spline ANOVA  
Abstract: A scheme to compute smoothing spline ANOVA estimates for large data sets with a (near) tensor-product structure is proposed. Such data sets are
  Node 510 | edge_importance=0.8307 | class=Probabilistic_Methods | Title: The Bayesian Approach to Tree-Structured Regression  
Abstract: TECHNICAL REPORT NO. 967 August 1996 
  Node 519 | edge_importance=0.8047 | class=Neural_Networks | Title: Smoothing Spline ANOVA for Exponential Families, with Application to the Wisconsin Epidemiological Study of Diabetic
Abstract: In this paper I give a review of ensemble learning using a simple 
  Node 192 | edge_importance=0.7972 | class=Neural_Networks | Title: Smoothing Spline ANOVA with Component-Wise Bayesian "Confidence Intervals" To Appear, J. Computational and Graphical Statistics  
Abstract: We study a multivariate smoothing spline estimate of 
  Node 193 | edge_importance=0.4209 | class=Neural_Networks | Title: Soft Classification, a.k.a. Risk Estimation, via Penalized Log Likelihood and Smoothing Spline Analysis of Variance  
Abstract: We study a multivariate smoothing spline estimate of a function o
  Node 439 | edge_importance=0.1539 | class=Neural_Networks | Title: Adaptive tuning of numerical weather prediction models: Randomized GCV in three and four dimensional data assimilation  
Abstract: This article describes a new system for induction of oblique d
  Node 10 | edge_importance=0.1238 | class=Neural_Networks | Title: GRKPACK: FITTING SMOOTHING SPLINE ANOVA MODELS FOR EXPONENTIAL FAMILIES  
Abstract: Wahba, Wang, Gu, Klein and Klein (1995) introduced Smoothing Spline ANalysis of VAriance (SS ANOVA) method fo

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

- ID: 2214
- Title: Behavior Near Zero of the Distribution of GCV Smoothing Parameter Estimates 1
- True class (canonical `y`): **Neural_Networks**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Neural_Networks**
- Prediction recorded by this method's pipeline: **Neural_Networks**

Canonical text (`raw_text`):

~~~~~~text
Title: Behavior Near Zero of the Distribution of GCV Smoothing Parameter Estimates 1  
Abstract: Many of today's algorithms for Inductive Logic Programming (ILP) put a heavy burden and responsibility on the user, because their declarative bias have to be defined in a rather low-level fashion. To address this issue, we developed a method for generating declarative language bias for top-down ILP systems from high-level declarations. The key feature of our approach is the distinction between a user level and an expert level of language bias declarations. The expert provides abstract meta-declarations, and the user declares the relationship between the meta-level and the given database to obtain a low-level declarative language bias. The suggested languages allow for compact and abstract specifications of the declarative language bias for top-down ILP systems using schemata. We verified several properties of the translation algorithm that generates schemata, and applied it successfully to a few chemical domains. As a consequence, we propose to use a two-level approach to generate declarative language bias.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 2 nodes

| node id | true class | title |
|---|---|---|
| 420 | Neural_Networks | Sample Size Calculations for Smoothing Splines Based on Bayesian Confidence Intervals |
| 2223 | Neural_Networks | Smoothing Spline Models With Correlated Random Errors 1 |

### 2-hop (shortest distance exactly 2): 8 nodes

| node id | true class | title |
|---|---|---|
| 10 | Neural_Networks | GRKPACK: FITTING SMOOTHING SPLINE ANOVA MODELS FOR EXPONENTIAL FAMILIES |
| 190 | Neural_Networks | Spline Smoothing For Bivariate Data With Applications To Association Between Hormones |
| 192 | Neural_Networks | Smoothing Spline ANOVA with Component-Wise Bayesian "Confidence Intervals" To Appear, J. Computational and Graphical Statistics |
| 193 | Neural_Networks | Soft Classification, a.k.a. Risk Estimation, via Penalized Log Likelihood and Smoothing Spline Analysis of Variance |
| 439 | Neural_Networks | Adaptive tuning of numerical weather prediction models: Randomized GCV in three and four dimensional data assimilation |
| 510 | Probabilistic_Methods | The Bayesian Approach to Tree-Structured Regression |
| 519 | Neural_Networks | Smoothing Spline ANOVA for Exponential Families, with Application to the Wisconsin Epidemiological Study of Diabetic |
| 2590 | Probabilistic_Methods | Backfitting in Smoothing Spline ANOVA |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=2214).
Recorded prediction: `{"Target Node": 2214, "Predicted Class": "Neural_Networks", "Confidence": 0.9906}`
Recorded graph stats: `{"total_1hop_degree": 2, "neighbor_label_ratio": {"Neural_Networks": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | smoothing | 0.6898 | 1 |
| 2 | error | 0.6765 | 0 |
| 3 | correl | 0.6658 | 0 |
| 4 | random | 0.6634 | 0 |
| 5 | confid | 0.6619 | 0 |
| 6 | spline | 0.6549 | 0 |
| 7 | anova | 0.6436 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
