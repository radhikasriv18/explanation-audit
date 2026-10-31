# Reference packet: CF-GNNExplainer__Qwen-14B__cora__2135

- Method: CF-GNNExplainer; configuration: Qwen-14B; dataset: cora; target node: 2135
- Explanation source: `./robustness_2026-10-30/production_a100/qwen14b_gptq_int4_cora_Response.json` ([417][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
To address the provided scenario, we will first populate the `infos` dictionary based on the given factual and counterfactual examples. Then, we will analyze the changes and their implications.

### Populating the Dictionary

Given the factual and counterfactual graphs, we need to identify the differences in the target node (node 2135) and its neighbors. Here is the populated dictionary:

```python
infos = {
    'Target_Node_ID': '2135',
    'Factual_Target_Node_Neighbors': ['134', '2012', '2023', '2333', '2583'],
    'Factual_Target_Node_Features': ['vector', 'function', 'imperfect', 'linear', 'weight', 'hypothesi', 'polynomi', 'instanc', 'unlimit', 'featur', 'exampl', 'set', 'produc', 'regress', 'train', 'result', 'construct', 'method'],
    'Counterfactual_Target_Node_Neighbors': ['2012', '2333', '2583'],
    'Counterfactual_Target_Node_Features': ['vector', 'function', 'imperfect', 'linear', 'weight', 'hypothesi', 'polynomi', 'instanc', 'unlimit', 'featur', 'exampl', 'set', 'produc', 'regress', 'train', 'result', 'construct', 'method'],
    'Factual_Target_Node_Class': 'Neural_Networks',
    'Counterfactual_Target_Node_class': 'Theory',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Natural_Language_Explanation': 'In the factual graph, the target node (node 2135) is classified as "Neural_Networks" and is connected to nodes 134, 2012, 2023, 2333, and 2583. In the counterfactual graph, the same node is reclassified as "Theory," and its connections are reduced to nodes 2012, 2333, and 2583.'
}
```

### Explanation of Changes

#### Target Node Classification Change

In the factual graph, the target node (node 2135) is classified as "Neural_Networks." However, in the counterfactual graph, it is reclassified as "Theory." This change in classification suggests that the removal of certain connections has altered the model's prediction for this node.

#### Influence of Neighbors

- **Removed Connections**: In the factual graph, node 2135 was connected to nodes 134, 2023, and 1782. These connections were removed in the counterfactual graph. Specifically, node 134 and node 2023, which are both classified as "Neural_Networks," were disconnected from node 2135. This disconnection likely influenced the model's decision to reclassify node 2135 from "Neural_Networks" to "Theory."

- **Remaining Connections**: Node 2135 still maintains connections with nodes 2012, 2333, and 2583 in the counterfactual graph. These nodes are classified as "Theory," which aligns with the new classification of node 2135. This suggests that the remaining connections are more influential in determining the new classification.

### Natural Language Explanation

In the factual graph, the target node (node 2135) is classified as "Neural_Networks" and is connected to nodes 134, 2012, 2023, 2333, and 2583. In the counterfactual graph, the same node is reclassified as "Theory," and its connections are reduced to nodes 2012, 2333, and 2583. The removal of connections to nodes 134 and 2023, which are both classified as "Neural_Networks," significantly alters the classification of node 2135. The remaining connections to nodes 2012, 2333, and 2583, all classified as "Theory," now dominate the classification decision, leading to the reclassification of node 2135 as "Theory."

This counterfactual explanation highlights the importance of the graph structure and the influence of neighboring nodes on the classification of a target node. By removing specific connections, we can observe how the model's prediction changes, providing valuable insights into the decision-making process of the graph-based model.
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
given the factual graph: The node 102 is a product titled 'Title: Multivariate versus Univariate Decision Trees  
Abstract: COINS Technical Report 92-8 January' with key attributes: versu, tree, linear, coin, genet, machin, multivari, decis, train, combin, elimin, result, januari, technic, report, construct and is connected with the nodes 2012, 2333, 2583 and it is classified as Neural_Networks, it is not the target node. The node 134 is a product titled 'Title: Gain Adaptation Beats Least Squares?  
Abstract: I present computational results suggesting t' with key attributes: linear, dimens, connectionist, genet, respect, comput, classic, adapt, part, system, squar, evalu, result, suggest, improv, gain, stochast, base, method, may and is connected with the nodes 505, 1118, 1782, 2135 and it is classified as Neural_Networks, it is not the target node. The node 318 is a product titled 'Title: Generalizing from Case Studies: A Case Study  
Abstract: Most empirical evaluations of machin' with key attributes: empir, pattern, hypothes, genet, explicitli, case, machin, significantli, evalu, better, result, suggest, multipl, perform, databas, gener, studi, author and is connected with the nodes 1173, 2310, 2333 and it is classified as Case_Based, it is not the target node. The node 378 is a product titled 'Title: Mingers, 1989 J. Mingers. An empirical comparison of pruning methods for decision tree induct' with key attributes: empir, domain, tree, barn, share, rule, prune, artifici, intellig, concaten, comparison, machin, induct, categori, decis, improv, multipl, technic, report, theori, method and is connected with the nodes 2012, 2583 and it is classified as Theory, it is not the target node. The node 505 is a product titled 'Title: From Isolation to Cooperation: An Alternative View of a System of Experts  
Abstract: We intr' with key attributes: cooper, predict, independ, increment, linear, altern, data, mean, compet, view, local, regress, train, shortcom, contrast, system, requir, model, queri, result, introduc, construct, expert, instanc, isol and is connected with the node 134 and it is classified as Neural_Networks, it is not the target node. The node 1118 is a product titled 'Title: Adapting Bias by Gradient Descent: An Incremental Version of Delta-Bar-Delta  
Abstract: Appr' with key attributes: increment, genet, effici, descent, view, previou, adapt, bias, appropri, bia, develop, wide, version, result, experi, key, gener, base and is connected with the node 134 and it is classified as Neural_Networks, it is not the target node. The node 1173 is a product titled 'Title: Dynamical Selection of Learning Algorithms  
Abstract: Determining the conditions for which a' with key attributes: predict, condit, limit, domain, class, dynam, genet, success, exampl, machin, determin, appropri, locat, open, propos, result, given, select, method and is connected with the nodes 318, 2583 and it is classified as Theory, it is not the target node. The node 1423 is a product titled 'Title: Comparison of Regression Methods, Symbolic Induction Methods and Neural Networks in Morbidity' with key attributes: network, symbol, space, diagnosi, hypothes, genet, comparison, comprehens, classifi, neural, induct, placement, anoth, regress, search, better, result, select, differ, method, repres and is connected with the node 2583 and it is classified as Neural_Networks, it is not the target node. The node 1782 is a product titled 'Title: Least-Squares Temporal Difference Learning  
Abstract: Submitted to NIPS-98 TD() is a popular' with key attributes: drawback, function, increment, updat, approxim, valu, tune, genet, data, mdp, submit, popular, user, major, transit, polici, observ, requir, evalu, recent, tempor, result, work, famili, larg, differ and is connected with the node 134 and it is classified as Neural_Networks, it is not the target node. The node 2012 is a product titled 'Title: Multivariate Decision Trees  
Abstract: COINS Technical Report 92-82 December 1992 Abstract M' with key attributes: limit, overcom, space, tree, restrict, coin, split, instanc, discuss, multivari, decis, represent, result, technic, report and is connected with the nodes 102, 378, 2135 and it is classified as Theory, it is not the target node. The node 2023 is a product titled 'Title: Classification of EEG Signals Using a Sparse Polynomial Builder  
Abstract: Edward S. Orosz a' with key attributes: polynomi, spars, april, classif, signal, technic, report, eeg and is connected with the node 2135 and it is classified as Neural_Networks, it is not the target node. The node 2135 is a product titled 'Title: Learning Polynomial Functions by Feature Construction  
Abstract: We present a method for lea' with key attributes: vector, function, imperfect, linear, weight, hypothesi, polynomi, instanc, unlimit, featur, exampl, set, produc, regress, train, result, construct, method and is connected with the nodes 134, 2012, 2023, 2333, 2583 and it is classified as Neural_Networks, it is the target node. The node 2310 is a product titled 'Title: Machine Learning: An Annotated Bibliography for the 1995 AI Statistics Tutorial on Machine Le' with key attributes: avail, question, workshop, brief, tutori, note, statist, read, machin, result, version, pleas and is connected with the nodes 318, 2583 and it is classified as Theory, it is not the target node. The node 2333 is a product titled 'Title: Recursive Automatic Algorithm Selection for Inductive Learning  
Abstract: COINS Technical Re' with key attributes: coin, recurs, genet, august, induct, technic, report, result, automat, select and is connected with the nodes 102, 318, 2135, 2583 and it is classified as Theory, it is not the target node. The node 2583 is a product titled 'Title: Dynamic Automatic Model Selection  
Abstract: COINS Technical Report 92-30 February 1992 Abst' with key attributes: dynam, coin, februari, genet, success, receiv, exampl, machin, attent, histori, mani, develop, model, recent, technic, report, given, task, result, automat, studi, select and is connected with the nodes 102, 378, 1173, 1423, 2135, 2310, 2333 and it is classified as Theory, it is not the target node. and given the counterfactual example: The node 102 is a product titled 'Title: Multivariate versus Univariate Decision Trees  
Abstract: COINS Technical Report 92-8 January' with key attributes: versu, tree, linear, coin, genet, machin, multivari, decis, train, combin, elimin, result, januari, technic, report, construct and is connected with no other nodes and it is classified as Neural_Networks, it is not the target node. The node 134 is a product titled 'Title: Gain Adaptation Beats Least Squares?  
Abstract: I present computational results suggesting t' with key attributes: linear, dimens, connectionist, genet, respect, comput, classic, adapt, part, system, squar, evalu, result, suggest, improv, gain, stochast, base, method, may and is connected with the nodes 505, 1118, 1782 and it is classified as Neural_Networks, it is not the target node. The node 318 is a product titled 'Title: Generalizing from Case Studies: A Case Study  
Abstract: Most empirical evaluations of machin' with key attributes: empir, pattern, hypothes, genet, explicitli, case, machin, significantli, evalu, better, result, suggest, multipl, perform, databas, gener, studi, author and is connected with the nodes 1173, 2310, 2333 and it is classified as Case_Based, it is not the target node. The node 378 is a product titled 'Title: Mingers, 1989 J. Mingers. An empirical comparison of pruning methods for decision tree induct' with key attributes: empir, domain, tree, barn, share, rule, prune, artifici, intellig, concaten, comparison, machin, induct, categori, decis, improv, multipl, technic, report, theori, method and is connected with the nodes 2012, 2583 and it is classified as Theory, it is not the target node. The node 505 is a product titled 'Title: From Isolation to Cooperation: An Alternative View of a System of Experts  
Abstract: We intr' with key attributes: cooper, predict, independ, increment, linear, altern, data, mean, compet, view, local, regress, train, shortcom, contrast, system, requir, model, queri, result, introduc, construct, expert, instanc, isol and is connected with the node 134 and it is classified as Neural_Networks, it is not the target node. The node 1118 is a product titled 'Title: Adapting Bias by Gradient Descent: An Incremental Version of Delta-Bar-Delta  
Abstract: Appr' with key attributes: increment, genet, effici, descent, view, previou, adapt, bias, appropri, bia, develop, wide, version, result, experi, key, gener, base and is connected with the node 134 and it is classified as Neural_Networks, it is not the target node. The node 1173 is a product titled 'Title: Dynamical Selection of Learning Algorithms  
Abstract: Determining the conditions for which a' with key attributes: predict, condit, limit, domain, class, dynam, genet, success, exampl, machin, determin, appropri, locat, open, propos, result, given, select, method and is connected with the nodes 318, 2583 and it is classified as Theory, it is not the target node. The node 1423 is a product titled 'Title: Comparison of Regression Methods, Symbolic Induction Methods and Neural Networks in Morbidity' with key attributes: network, symbol, space, diagnosi, hypothes, genet, comparison, comprehens, classifi, neural, induct, placement, anoth, regress, search, better, result, select, differ, method, repres and is connected with no other nodes and it is classified as Neural_Networks, it is not the target node. The node 1782 is a product titled 'Title: Least-Squares Temporal Difference Learning  
Abstract: Submitted to NIPS-98 TD() is a popular' with key attributes: drawback, function, increment, updat, approxim, valu, tune, genet, data, mdp, submit, popular, user, major, transit, polici, observ, requir, evalu, recent, tempor, result, work, famili, larg, differ and is connected with the node 134 and it is classified as Neural_Networks, it is not the target node. The node 2012 is a product titled 'Title: Multivariate Decision Trees  
Abstract: COINS Technical Report 92-82 December 1992 Abstract M' with key attributes: limit, overcom, space, tree, restrict, coin, split, instanc, discuss, multivari, decis, represent, result, technic, report and is connected with the nodes 378, 2135 and it is classified as Theory, it is not the target node. The node 2023 is a product titled 'Title: Classification of EEG Signals Using a Sparse Polynomial Builder  
Abstract: Edward S. Orosz a' with key attributes: polynomi, spars, april, classif, signal, technic, report, eeg and is connected with no other nodes and it is classified as Neural_Networks, it is not the target node. The node 2135 is a product titled 'Title: Learning Polynomial Functions by Feature Construction  
Abstract: We present a method for lea' with key attributes: vector, function, imperfect, linear, weight, hypothesi, polynomi, instanc, unlimit, featur, exampl, set, produc, regress, train, result, construct, method and is connected with the nodes 2012, 2333, 2583 and it is classified as Theory, it is the target node. The node 2310 is a product titled 'Title: Machine Learning: An Annotated Bibliography for the 1995 AI Statistics Tutorial on Machine Le' with key attributes: avail, question, workshop, brief, tutori, note, statist, read, machin, result, version, pleas and is connected with the node 318 and it is classified as Case_Based, it is not the target node. The node 2333 is a product titled 'Title: Recursive Automatic Algorithm Selection for Inductive Learning  
Abstract: COINS Technical Re' with key attributes: coin, recurs, genet, august, induct, technic, report, result, automat, select and is connected with the nodes 318, 2135 and it is classified as Theory, it is not the target node. The node 2583 is a product titled 'Title: Dynamic Automatic Model Selection  
Abstract: COINS Technical Report 92-30 February 1992 Abst' with key attributes: dynam, coin, februari, genet, success, receiv, exampl, machin, attent, histori, mani, develop, model, recent, technic, report, given, task, result, automat, studi, select and is connected with the nodes 378, 1173, 2135 and it is classified as Theory, it is not the target node.
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

- ID: 2135
- Title: Learning Polynomial Functions by Feature Construction
- True class (canonical `y`): **Neural_Networks**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Neural_Networks**
- Prediction recorded by this method's pipeline: **Neural_Networks**

Canonical text (`raw_text`):

~~~~~~text
Title: Learning Polynomial Functions by Feature Construction  
Abstract: We present a method for learning higher-order polynomial functions from examples using linear regression and feature construction. Regression is used on a set of training instances to produce a weight vector for a linear function over the feature set. If this hypothesis is imperfect, a new feature is constructed by forming the product of the two features that most effectively predict the squared error of the current hypothesis. The algorithm is then repeated. In an extension to this method, the specific pair of features to combine is selected by measuring their joint ability to predict the hypothesis' error.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 5 nodes

| node id | true class | title |
|---|---|---|
| 134 | Neural_Networks | Gain Adaptation Beats Least Squares? |
| 2012 | Theory | Multivariate Decision Trees |
| 2023 | Neural_Networks | Classification of EEG Signals Using a Sparse Polynomial Builder |
| 2333 | Theory | Recursive Automatic Algorithm Selection for Inductive Learning |
| 2583 | Theory | Dynamic Automatic Model Selection |

### 2-hop (shortest distance exactly 2): 9 nodes

| node id | true class | title |
|---|---|---|
| 102 | Neural_Networks | Multivariate versus Univariate Decision Trees |
| 318 | Case_Based | Generalizing from Case Studies: A Case Study |
| 378 | Theory | Mingers, 1989 J. Mingers. An empirical comparison of pruning methods for decision tree induction. Machine |
| 505 | Neural_Networks | From Isolation to Cooperation: An Alternative View of a System of Experts |
| 1118 | Neural_Networks | Adapting Bias by Gradient Descent: An Incremental Version of Delta-Bar-Delta |
| 1173 | Theory | Dynamical Selection of Learning Algorithms |
| 1423 | Neural_Networks | Comparison of Regression Methods, Symbolic Induction Methods and Neural Networks in Morbidity Diagnosis and Mortality |
| 1782 | Reinforcement_Learning | Least-Squares Temporal Difference Learning |
| 2310 | Case_Based | Machine Learning: An Annotated Bibliography for the 1995 AI Statistics Tutorial on Machine Learning (Version 1) |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/cora/cf-gnnexplainer-canonical/random_seed_42_*` (key=417).

- Factual class: **Neural_Networks**
- Counterfactual class: **Theory**
- Removed edges (global ids, 8): (102, 2012), (102, 2333), (102, 2583), (134, 2135), (1423, 2583), (2023, 2135), (2310, 2583), (2333, 2583)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 2135 |
| Factual_Target_Node_Neighbors | 134, 2012, 2023, 2333, 2583 |
| Factual_Target_Node_Features | vector, function, imperfect, linear, weight, hypothesi, polynomi, instanc, unlimit, featur, exampl, set, produc, regress, train, result, result, construct, method |
| Counterfactual_Target_Node_Neighbors | 2012, 2333, 2583 |
| Counterfactual_Target_Node_Features | vector, function, imperfect, linear, weight, hypothesi, polynomi, instanc, unlimit, featur, exampl, set, produc, regress, train, result, result, construct, method |
| Factual_Target_Node_Class | Neural_Networks |
| Counterfactual_Target_Node_class | Theory |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 134, 2023 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 2135 |
| Factual_Target_Node_Neighbors | 134, 2012, 2023, 2333, 2583 |
| Factual_Target_Node_Features | vector, function, imperfect, linear, weight, hypothesi, polynomi, instanc, unlimit, featur, exampl, set, produc, regress, train, result, result, construct, method |
| Counterfactual_Target_Node_Neighbors | 2012, 2333, 2583 |
| Counterfactual_Target_Node_Features | vector, function, imperfect, linear, weight, hypothesi, polynomi, instanc, unlimit, featur, exampl, set, produc, regress, train, result, result, construct, method |
| Factual_Target_Node_Class | Neural_Networks |
| Counterfactual_Target_Node_class | Theory |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 134, 2023 |
| Natural_Language_Explanation | None |
