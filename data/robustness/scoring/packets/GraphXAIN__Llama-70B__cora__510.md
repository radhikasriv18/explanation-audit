# Reference packet: GraphXAIN__Llama-70B__cora__510

- Method: GraphXAIN; configuration: Llama-70B; dataset: cora; target node: 510
- Explanation source: `./robustness_2026-10-30/llama70b/graphxain/cora/510.json` (response)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
The model predicted that the research area of the target paper, "The Bayesian Approach to Tree-Structured Regression," is "Neural Networks" with a high confidence of 99%. The top contributing bag-of-words features were "smooth," "spline," "model," "function," "statist," "anova," and "decomposit," which, despite being absent from the paper, were strongly associated with the predicted class. The absence of these terms suggests that the model relied more heavily on the paper's connections to other papers. Notably, the paper's 1-hop neighbors, such as "Smoothing Spline ANOVA with Component-Wise Bayesian 'Confidence Intervals'" and "A Flexible Model For Human Circadian Rhythms," were all classified as "Neural Networks." The presence of these neural network-focused papers in the target paper's citation neighborhood likely reinforced the model's prediction due to their strong relevance to the field of machine learning. These patterns in the local graph structure, combined with the influence of similarly-themed 2-hop neighbors like "Spline Smoothing For Bivariate Data With Applications To Association Between Hormones," collectively steered the model towards a confident classification as a "Neural Network" paper. Overall, the model's decision was largely driven by the indirect clues gathered from the paper's position within the broader citation network rather than explicit keywords within the text itself.
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

### Target Paper (node 510):
Title: The Bayesian Approach to Tree-Structured Regression  
Abstract: TECHNICAL REPORT NO. 967 August 1996 

### Model Prediction:
{
  "Target Node": 510,
  "Predicted Class": "Neural_Networks",
  "Confidence": 0.9988
}

### Target Node's Categorical Features — Top-7 Most Important BOW Words (GNNExplainer node mask):
All Cora BOW features are binary/categorical (word present or absent) — there are no continuous features for this dataset.
Each entry: word (Porter-stemmed) | importance score | whether the word is present in the paper (1=yes, 0=no).
  word='smooth', importance=0.6694, present_in_paper=0
  word='spline', importance=0.6688, present_in_paper=0
  word='model', importance=0.6639, present_in_paper=0
  word='function', importance=0.6624, present_in_paper=0
  word='statist', importance=0.6605, present_in_paper=0
  word='anova', importance=0.6548, present_in_paper=0
  word='decomposit', importance=0.649, present_in_paper=0

### Target Node's Local Graph Structure:
Total 1-hop citation degree (all direct neighbors, not just those listed below): 4
Label distribution across all 1-hop neighbors (ground-truth class): Neural_Networks=100.0%

### Direct Citation Neighbors — 1-hop (GNNExplainer edge mask, descending importance, top-7 shown):
These are papers directly cited by or citing the target paper.
  Node 192 | edge_importance=0.8301 | class=Neural_Networks | Title: Smoothing Spline ANOVA with Component-Wise Bayesian "Confidence Intervals" To Appear, J. Computational and Graphical Statistics  
Abstract: We study a multivariate smoothing spline estimate of 
  Node 519 | edge_importance=0.8266 | class=Neural_Networks | Title: Smoothing Spline ANOVA for Exponential Families, with Application to the Wisconsin Epidemiological Study of Diabetic
Abstract: In this paper I give a review of ensemble learning using a simple 
  Node 356 | edge_importance=0.7833 | class=Neural_Networks | Title: A Flexible Model For Human Circadian Rhythms  
Abstract: Many hormones and other physiological processes vary in a circadian pattern. Although a sine/cosine function can be used to model these 
  Node 2223 | edge_importance=0.4331 | class=Neural_Networks | Title: Smoothing Spline Models With Correlated Random Errors 1  
Abstract: Reinforcement learning can be used not only to predict rewards, but also to predict states, i.e. to learn a model of the worl

### 2-hop Citation Neighbors (neighbors-of-neighbors, GNNExplainer edge mask, top-10 shown):
These papers are not directly connected to the target but are linked through shared citation partners.
  Node 190 | edge_importance=0.832 | class=Neural_Networks | Title: Spline Smoothing For Bivariate Data With Applications To Association Between Hormones  
Abstract: Standard methods for inducing both the structure and weight values of recurrent neural networks
  Node 193 | edge_importance=0.8268 | class=Neural_Networks | Title: Soft Classification, a.k.a. Risk Estimation, via Penalized Log Likelihood and Smoothing Spline Analysis of Variance  
Abstract: We study a multivariate smoothing spline estimate of a function o
  Node 420 | edge_importance=0.8083 | class=Neural_Networks | Title: Sample Size Calculations for Smoothing Splines Based on Bayesian Confidence Intervals  
Abstract: Bayesian confidence intervals of a smoothing spline are often used to distinguish two curves. I
  Node 2590 | edge_importance=0.8077 | class=Probabilistic_Methods | Title: Backfitting in Smoothing Spline ANOVA  
Abstract: A scheme to compute smoothing spline ANOVA estimates for large data sets with a (near) tensor-product structure is proposed. Such data sets are
  Node 280 | edge_importance=0.7992 | class=Probabilistic_Methods | Title: USING SMOOTHING SPLINE ANOVA TO EXAMINE THE RELATION OF RISK FACTORS TO THE INCIDENCE AND
Abstract: This paper presents recent developments toward a formalism that combines useful properties of
  Node 10 | edge_importance=0.7961 | class=Neural_Networks | Title: GRKPACK: FITTING SMOOTHING SPLINE ANOVA MODELS FOR EXPONENTIAL FAMILIES  
Abstract: Wahba, Wang, Gu, Klein and Klein (1995) introduced Smoothing Spline ANalysis of VAriance (SS ANOVA) method fo
  Node 2448 | edge_importance=0.7886 | class=Neural_Networks | Title: Automatic Smoothing Spline Projection Pursuit  Automatic Smoothing Spline Projection Pursuit.  
Abstract: kj = 1. The standard PPR algorithm of Friedman and Stuet-zle (1981) estimates the smoot
  Node 2608 | edge_importance=0.2135 | class=Neural_Networks | Title: Testing the Generalized Linear Model Null Hypothesis versus `Smooth' Alternatives 1  
Abstract: We previously introduced an exemplar model, named GCM-ISW, that exploits a highly flexible weight
  Node 705 | edge_importance=0.2068 | class=Neural_Networks | Title: EXPERIMENTING WITH THE CHEESEMAN-STUTZ EVIDENCE APPROXIMATION FOR PREDICTIVE MODELING AND DATA MINING  
Abstract: TECHNICAL REPORT NO. 947 June 5, 1995 
  Node 2214 | edge_importance=0.1781 | class=Neural_Networks | Title: Behavior Near Zero of the Distribution of GCV Smoothing Parameter Estimates 1  
Abstract: Many of today's algorithms for Inductive Logic Programming (ILP) put a heavy burden and responsibility 

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

- ID: 510
- Title: The Bayesian Approach to Tree-Structured Regression
- True class (canonical `y`): **Probabilistic_Methods**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Neural_Networks**
- Prediction recorded by this method's pipeline: **Neural_Networks**

Canonical text (`raw_text`):

~~~~~~text
Title: The Bayesian Approach to Tree-Structured Regression  
Abstract: TECHNICAL REPORT NO. 967 August 1996 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 4 nodes

| node id | true class | title |
|---|---|---|
| 192 | Neural_Networks | Smoothing Spline ANOVA with Component-Wise Bayesian "Confidence Intervals" To Appear, J. Computational and Graphical Statistics |
| 356 | Neural_Networks | A Flexible Model For Human Circadian Rhythms |
| 519 | Neural_Networks | Smoothing Spline ANOVA for Exponential Families, with Application to the Wisconsin Epidemiological Study of Diabetic |
| 2223 | Neural_Networks | Smoothing Spline Models With Correlated Random Errors 1 |

### 2-hop (shortest distance exactly 2): 12 nodes

| node id | true class | title |
|---|---|---|
| 10 | Neural_Networks | GRKPACK: FITTING SMOOTHING SPLINE ANOVA MODELS FOR EXPONENTIAL FAMILIES |
| 190 | Neural_Networks | Spline Smoothing For Bivariate Data With Applications To Association Between Hormones |
| 193 | Neural_Networks | Soft Classification, a.k.a. Risk Estimation, via Penalized Log Likelihood and Smoothing Spline Analysis of Variance |
| 280 | Probabilistic_Methods | USING SMOOTHING SPLINE ANOVA TO EXAMINE THE RELATION OF RISK FACTORS TO THE INCIDENCE AND |
| 420 | Neural_Networks | Sample Size Calculations for Smoothing Splines Based on Bayesian Confidence Intervals |
| 439 | Neural_Networks | Adaptive tuning of numerical weather prediction models: Randomized GCV in three and four dimensional data assimilation |
| 705 | Neural_Networks | EXPERIMENTING WITH THE CHEESEMAN-STUTZ EVIDENCE APPROXIMATION FOR PREDICTIVE MODELING AND DATA MINING |
| 2214 | Neural_Networks | Behavior Near Zero of the Distribution of GCV Smoothing Parameter Estimates 1 |
| 2448 | Neural_Networks | Automatic Smoothing Spline Projection Pursuit  Automatic Smoothing Spline Projection Pursuit. |
| 2549 | Neural_Networks | A Generalized Approximate Cross Validation for Smoothing Splines with Non-Gaussian Data 1 |
| 2590 | Probabilistic_Methods | Backfitting in Smoothing Spline ANOVA |
| 2608 | Neural_Networks | Testing the Generalized Linear Model Null Hypothesis versus `Smooth' Alternatives 1 |

## 5. Method evidence: GraphXAIN (GNNExplainer)

Source: the locked schema-aligned prompt (`graphxain_schemaaligned_production_2026-08-16/cora/prompts_dump.jsonl`, target_node=510).
Recorded prediction: `{"Target Node": 510, "Predicted Class": "Neural_Networks", "Confidence": 0.9988}`
Recorded graph stats: `{"total_1hop_degree": 4, "neighbor_label_ratio": {"Neural_Networks": 1.0}}`

### Top-7 features (GNNExplainer node mask), as given to the model

| rank | word | importance | present in target |
|---|---|---|---|
| 1 | smooth | 0.6694 | 0 |
| 2 | spline | 0.6688 | 0 |
| 3 | model | 0.6639 | 0 |
| 4 | function | 0.6624 | 0 |
| 5 | statist | 0.6605 | 0 |
| 6 | anova | 0.6548 | 0 |
| 7 | decomposit | 0.649 | 0 |

The GNNExplainer 1-hop / 2-hop neighbors with edge importance are listed in the prompt (section 2).
