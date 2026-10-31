# Reference packet: CF-GNNExplainer__Llama-70B__cora__510

- Method: CF-GNNExplainer; configuration: Llama-70B; dataset: cora; target node: 510
- Explanation source: `./robustness_2026-10-30/llama70b/cf/cora/510.json` (response)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, we can fill the dictionary as follows:

infos = {
    'Target_Node_ID': 510,
    'Factual_Target_Node_Neighbors': [192, 356, 519, 2223],
    'Factual_Target_Node_Features': ['august', 'technic', 'report'],
    'Counterfactual_Target_Node_Neighbors': [],
    'Counterfactual_Target_Node_Features': ['august', 'technic', 'report'],
    'Factual_Target_Node_Class': 'Neural_Networks',
    'Counterfactual_Target_Node_class': 'Theory',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Natural_Language_Explanation': 'The target node 510 has changed its classification from Neural_Networks to Theory. This change is likely due to the removal of its connections with neighboring nodes 192, 356, 519, and 2223, which were previously influencing its classification as Neural_Networks. Without these connections, the node's features, which include words like "august", "technic", and "report", are more consistent with the Theory class.',
    'Node_Differences': [510],
    'Edge_Differences': [(510, 192), (510, 356), (510, 519), (510, 2223)]
}

Explanation:
The target node 510 has changed its classification from Neural_Networks to Theory. This change is likely due to the removal of its connections with neighboring nodes 192, 356, 519, and 2223, which were previously influencing its classification as Neural_Networks. Without these connections, the node's features, which include words like "august", "technic", and "report", are more consistent with the Theory class.

In the factual graph, node 510 was connected to nodes 192, 356, 519, and 2223, which are all classified as Neural_Networks. These connections likely influenced the classification of node 510 as Neural_Networks. However, in the counterfactual graph, these connections have been removed, and node 510 is now isolated. Without the influence of its former neighbors, the features of node 510 are more consistent with the Theory class.

It's worth noting that the features of node 510 did not change between the factual and counterfactual graphs. The change in classification is solely due to the change in the node's connections. This highlights the importance of considering the graph structure when making predictions or classifications in graph-based learning tasks.
~~~~~~

## 2. Prompt the method's model received

Chat messages (system + user) built by llm-graph-cf's prompt code; identical for every CF configuration.

**system:**

~~~~~~text
You are a language model that generates responses in a coherent and well-structured discourse style. Avoid using bullet points, lists, or numerical outlines. Provide your responses in complete sentences and paragraphs, explaining concepts clearly and concisely in a continuous flow.You must take a factual example , a graph, and its counterfactual example, another graph, generated via adjacency matrix perturbation and you must explain the differences.Counterfactual Explanation: A counterfactual explanation refers to a type of explanation in machine learning and artificial intelligence that describes how altering certain input features can change the output of a model. It answers 'what if' scenarios by identifying minimal changes necessary to achieve a different desired outcome. Counterfactual explanations provide insights into the decision-making process of complex models, enhancing transparency and interpretability.For example, consider a credit scoring model that denies a loan application. A counterfactual explanation might be: 'If your annual income had been $50,000 instead of $45,000, your loan would have been approved.' This helps the applicant understand what specific change could lead to a different decision.Counterfactual Explanations in Graphs: Graphs are data structures consisting of nodes (vertices) and edges that represent relationships between entities. Graphs are prevalent in various domains such as social networks, biological networks, and knowledge graphs. When machine learning models, particularly Graph Neural Networks (GNNs), are applied to graph data, interpreting their predictions becomes challenging due to the complexity of the graph structure.Counterfactual explanations in graphs aim to provide insights into how changes in the graph's structure or node features can alter the model's predictions. This involves identifying minimal modifications to the graph that would change the outcome for a specific node or the entire graph.You MUST fill this dictionary taking into account that Node_Differences must contain JUST the nodes' id where the change happen, the Edge_Differences must contain a list of tuple representing the nodes involved in the edges:  infos={Target_Node_ID:'', Factual_Target_Node_Neighbors: [], Factual_Target_Node_Features: [], Counterfactual_Target_Node_Neighbors: [],
    Counterfactual_Target_Node_Features: [], Factual_Target_Node_Class: '', Counterfactual_Target_Node_class: '', Target_Node_Features_Changed_From_Factual_To_Counterfactual: [], Natural_Language_Explanation: ''}
~~~~~~

**user:**

~~~~~~text
given the factual graph: The node 10 is a product titled 'Title: GRKPACK: FITTING SMOOTHING SPLINE ANOVA MODELS FOR EXPONENTIAL FAMILIES  
Abstract: Wahba, Wa' with key attributes: fit, anova, smooth, exponenti, model, spline, famili and is connected with the nodes 192, 193, 280, 420, 519 and it is classified as Neural_Networks, it is not the target node. The node 190 is a product titled 'Title: Spline Smoothing For Bivariate Data With Applications To Association Between Hormones  
Abstr' with key attributes: smooth, data, spline, associ, applic and is connected with the nodes 356, 519, 2223 and it is classified as Neural_Networks, it is not the target node. The node 192 is a product titled 'Title: Smoothing Spline ANOVA with Component-Wise Bayesian "Confidence Intervals" To Appear, J. Comp' with key attributes: function, estim, anova, interact, appear, sum, smooth, comput, decomposit, graphic, statist, variabl, multivari, main, interv, effect, spline, bayesian, studi, base, confid, sever and is connected with the nodes 10, 193, 280, 420, 439, 510, 519, 705 and it is classified as Neural_Networks, it is not the target node. The node 193 is a product titled 'Title: Soft Classification, a.k.a. Risk Estimation, via Penalized Log Likelihood and Smoothing Splin' with key attributes: inform, ed, limit, anova, appear, tune, smooth, classif, machin, neural, advanc, publish, process, system, structur, result, recent, spline and is connected with the nodes 10, 192, 280, 420, 519, 2549 and it is classified as Neural_Networks, it is not the target node. The node 280 is a product titled 'Title: USING SMOOTHING SPLINE ANOVA TO EXAMINE THE RELATION OF RISK FACTORS TO THE INCIDENCE AND
Abs' with key attributes: anova, smooth, relat, factor, risk, examin, spline and is connected with the nodes 10, 192, 193, 519, 2549 and it is classified as Neural_Networks, it is not the target node. The node 356 is a product titled 'Title: A Flexible Model For Human Circadian Rhythms  
Abstract: Many hormones and other physiologica' with key attributes: function, pattern, period, flexibl, form, vari, appropri, process, mani, describ, result, model, spline, phase, human and is connected with the nodes 190, 510 and it is classified as Neural_Networks, it is not the target node. The node 420 is a product titled 'Title: Sample Size Calculations for Smoothing Splines Based on Bayesian Confidence Intervals  
Abstr' with key attributes: bootstrap, smooth, comparison, interv, spline, bayesian, confid and is connected with the nodes 10, 192, 193, 439, 519, 2214, 2590 and it is classified as Neural_Networks, it is not the target node. The node 439 is a product titled 'Title: Adaptive tuning of numerical weather prediction models: Randomized GCV in three and four dime' with key attributes: numer, dimension, predict, random, tune, data, adapt, model and is connected with the nodes 192, 420 and it is classified as Neural_Networks, it is not the target node. The node 510 is a product titled 'Title: The Bayesian Approach to Tree-Structured Regression  
Abstract: TECHNICAL REPORT NO. 967 Augu' with key attributes: august, technic, report and is connected with the nodes 192, 356, 519, 2223 and it is classified as Neural_Networks, it is the target node. The node 519 is a product titled 'Title: Smoothing Spline ANOVA for Exponential Families, with Application to the Wisconsin Epidemiolo' with key attributes: anova, smooth, exponenti, spline, famili, studi, applic and is connected with the nodes 10, 190, 192, 193, 280, 420, 510, 705, 2223, 2448, 2549, 2590, 2608 and it is classified as Neural_Networks, it is not the target node. The node 705 is a product titled 'Title: EXPERIMENTING WITH THE CHEESEMAN-STUTZ EVIDENCE APPROXIMATION FOR PREDICTIVE MODELING AND DAT' with key attributes: june, technic, report and is connected with the nodes 192, 519 and it is classified as Neural_Networks, it is not the target node. The node 2214 is a product titled 'Title: Behavior Near Zero of the Distribution of GCV Smoothing Parameter Estimates 1  
Abstract: Man' with key attributes: paramet, estim, behavior, smooth, distribut, zero and is connected with the nodes 420, 2223 and it is classified as Neural_Networks, it is not the target node. The node 2223 is a product titled 'Title: Smoothing Spline Models With Correlated Random Errors 1  
Abstract: Reinforcement learning ca' with key attributes: random, smooth, error, model, spline, correl and is connected with the nodes 190, 510, 519, 2214 and it is classified as Neural_Networks, it is not the target node. The node 2448 is a product titled 'Title: Automatic Smoothing Spline Projection Pursuit  Automatic Smoothing Spline Projection Pursuit.' with key attributes: function, estim, linear, genet, smooth, project, nonparametr, standard, pursuit, max, model, spline, construct, automat and is connected with the node 519 and it is classified as Neural_Networks, it is not the target node. The node 2549 is a product titled 'Title: A Generalized Approximate Cross Validation for Smoothing Splines with Non-Gaussian Data 1  
A' with key attributes: approxim, smooth, data, spline, gener, valid, hoeffd and is connected with the nodes 193, 280, 519, 2608 and it is classified as Neural_Networks, it is not the target node. The node 2590 is a product titled 'Title: Backfitting in Smoothing Spline ANOVA  
Abstract: A scheme to compute smoothing spline ANOVA' with key attributes: anova, temperatur, global, smooth, data, spline, applic and is connected with the nodes 420, 519 and it is classified as Neural_Networks, it is not the target node. The node 2608 is a product titled 'Title: Testing the Generalized Linear Model Null Hypothesis versus `Smooth' Alternatives 1  
Abstrac' with key attributes: versu, linear, hypothesi, altern, model, gener and is connected with the nodes 519, 2549 and it is classified as Neural_Networks, it is not the target node. and given the counterfactual example: The node 10 is a product titled 'Title: GRKPACK: FITTING SMOOTHING SPLINE ANOVA MODELS FOR EXPONENTIAL FAMILIES  
Abstract: Wahba, Wa' with key attributes: fit, anova, smooth, exponenti, model, spline, famili and is connected with the nodes 192, 193, 280, 420, 519 and it is classified as Neural_Networks, it is not the target node. The node 190 is a product titled 'Title: Spline Smoothing For Bivariate Data With Applications To Association Between Hormones  
Abstr' with key attributes: smooth, data, spline, associ, applic and is connected with the nodes 356, 519, 2223 and it is classified as Neural_Networks, it is not the target node. The node 192 is a product titled 'Title: Smoothing Spline ANOVA with Component-Wise Bayesian "Confidence Intervals" To Appear, J. Comp' with key attributes: function, estim, anova, interact, appear, sum, smooth, comput, decomposit, graphic, statist, variabl, multivari, main, interv, effect, spline, bayesian, studi, base, confid, sever and is connected with the nodes 10, 193, 280, 420, 439, 519, 705 and it is classified as Neural_Networks, it is not the target node. The node 193 is a product titled 'Title: Soft Classification, a.k.a. Risk Estimation, via Penalized Log Likelihood and Smoothing Splin' with key attributes: inform, ed, limit, anova, appear, tune, smooth, classif, machin, neural, advanc, publish, process, system, structur, result, recent, spline and is connected with the nodes 10, 192, 280, 420, 519, 2549 and it is classified as Neural_Networks, it is not the target node. The node 280 is a product titled 'Title: USING SMOOTHING SPLINE ANOVA TO EXAMINE THE RELATION OF RISK FACTORS TO THE INCIDENCE AND
Abs' with key attributes: anova, smooth, relat, factor, risk, examin, spline and is connected with the nodes 10, 192, 193, 519, 2549 and it is classified as Neural_Networks, it is not the target node. The node 356 is a product titled 'Title: A Flexible Model For Human Circadian Rhythms  
Abstract: Many hormones and other physiologica' with key attributes: function, pattern, period, flexibl, form, vari, appropri, process, mani, describ, result, model, spline, phase, human and is connected with the node 190 and it is classified as Neural_Networks, it is not the target node. The node 420 is a product titled 'Title: Sample Size Calculations for Smoothing Splines Based on Bayesian Confidence Intervals  
Abstr' with key attributes: bootstrap, smooth, comparison, interv, spline, bayesian, confid and is connected with the nodes 10, 192, 193, 439, 519, 2214, 2590 and it is classified as Neural_Networks, it is not the target node. The node 439 is a product titled 'Title: Adaptive tuning of numerical weather prediction models: Randomized GCV in three and four dime' with key attributes: numer, dimension, predict, random, tune, data, adapt, model and is connected with the nodes 192, 420 and it is classified as Neural_Networks, it is not the target node. The node 510 is a product titled 'Title: The Bayesian Approach to Tree-Structured Regression  
Abstract: TECHNICAL REPORT NO. 967 Augu' with key attributes: august, technic, report and is connected with no other nodes and it is classified as Theory, it is the target node. The node 519 is a product titled 'Title: Smoothing Spline ANOVA for Exponential Families, with Application to the Wisconsin Epidemiolo' with key attributes: anova, smooth, exponenti, spline, famili, studi, applic and is connected with the nodes 10, 190, 192, 193, 280, 420, 705, 2223, 2448, 2549, 2590, 2608 and it is classified as Neural_Networks, it is not the target node. The node 705 is a product titled 'Title: EXPERIMENTING WITH THE CHEESEMAN-STUTZ EVIDENCE APPROXIMATION FOR PREDICTIVE MODELING AND DAT' with key attributes: june, technic, report and is connected with the nodes 192, 519 and it is classified as Neural_Networks, it is not the target node. The node 2214 is a product titled 'Title: Behavior Near Zero of the Distribution of GCV Smoothing Parameter Estimates 1  
Abstract: Man' with key attributes: paramet, estim, behavior, smooth, distribut, zero and is connected with the nodes 420, 2223 and it is classified as Neural_Networks, it is not the target node. The node 2223 is a product titled 'Title: Smoothing Spline Models With Correlated Random Errors 1  
Abstract: Reinforcement learning ca' with key attributes: random, smooth, error, model, spline, correl and is connected with the nodes 190, 519, 2214 and it is classified as Neural_Networks, it is not the target node. The node 2448 is a product titled 'Title: Automatic Smoothing Spline Projection Pursuit  Automatic Smoothing Spline Projection Pursuit.' with key attributes: function, estim, linear, genet, smooth, project, nonparametr, standard, pursuit, max, model, spline, construct, automat and is connected with the node 519 and it is classified as Neural_Networks, it is not the target node. The node 2549 is a product titled 'Title: A Generalized Approximate Cross Validation for Smoothing Splines with Non-Gaussian Data 1  
A' with key attributes: approxim, smooth, data, spline, gener, valid, hoeffd and is connected with the nodes 193, 280, 519, 2608 and it is classified as Neural_Networks, it is not the target node. The node 2590 is a product titled 'Title: Backfitting in Smoothing Spline ANOVA  
Abstract: A scheme to compute smoothing spline ANOVA' with key attributes: anova, temperatur, global, smooth, data, spline, applic and is connected with the nodes 420, 519 and it is classified as Neural_Networks, it is not the target node. The node 2608 is a product titled 'Title: Testing the Generalized Linear Model Null Hypothesis versus `Smooth' Alternatives 1  
Abstrac' with key attributes: versu, linear, hypothesi, altern, model, gener and is connected with the nodes 519, 2549 and it is classified as Neural_Networks, it is not the target node.
                    and given the knowledge base about the dataset: 
The Cora dataset is a widely used benchmark for graph-based learning tasks, specifically node classification in citation networks. It consists of 2,708 scientific publications classified into seven distinct research topics. The dataset is represented as a graph where each node corresponds to a paper, and edges represent citation links between papers. If a paper cites or is cited by another paper, an undirected edge is created between the two corresponding nodes.
Features:
Each node is described by a 1,433-dimensional binary feature vector, where each dimension indicates the presence or absence of a specific word from the paper’s abstract. This feature representation helps capture the content of each publication.In the current format the nodes features are represented by a list of the words in the word vector that have value 1.
Classes:
The nodes are categorized into seven classes, which correspond to the research topic of each paper:
1. Case_Based: Papers focused on case-based learning and case-based reasoning methods.
2. Genetic_Algorithms: Research related to optimization and search algorithms inspired by natural selection and genetics.
3. Neural_Networks: Publications on neural network architectures, learning algorithms, and their applications.
4. Probabilistic_Methods: Papers covering probabilistic models, including Bayesian networks and probabilistic graphical models.
5. Reinforcement_Learning: Research discussing methods for training agents to make sequential decisions in dynamic environments.
6. Rule_Learning: Publications on rule-based learning methods, including decision rules and logic programming.
7. Theory: Theoretical studies, including mathematical foundations of machine learning and algorithmic theory.
Graph Structure:
Nodes: 2,708 papers, each labeled with one of the seven classes.
Edges: 5,429 citation links between papers, forming a sparse and undirected graph structure., fill the dictionary!
                    and provide an explanation about the change in classification for the target node, please evaluate also the influences of neighbors nodes.
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

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/cora/cf-gnnexplainer-canonical/random_seed_42_*` (key=85).

- Factual class: **Neural_Networks**
- Counterfactual class: **Theory**
- Removed edges (global ids, 4): (192, 510), (356, 510), (510, 519), (510, 2223)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 510 |
| Factual_Target_Node_Neighbors | 192, 356, 519, 2223 |
| Factual_Target_Node_Features | august, technic, report |
| Counterfactual_Target_Node_Neighbors |  |
| Counterfactual_Target_Node_Features | august, technic, report |
| Factual_Target_Node_Class | Neural_Networks |
| Counterfactual_Target_Node_class | Theory |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 192, 356, 519, 2223 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 510 |
| Factual_Target_Node_Neighbors | 192, 356, 519, 2223 |
| Factual_Target_Node_Features | august, technic, report |
| Counterfactual_Target_Node_Neighbors |  |
| Counterfactual_Target_Node_Features | august, technic, report |
| Factual_Target_Node_Class | Neural_Networks |
| Counterfactual_Target_Node_class | Theory |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 192, 356, 519, 2223 |
| Natural_Language_Explanation | None |
