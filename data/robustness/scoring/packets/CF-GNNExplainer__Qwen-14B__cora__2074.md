# Reference packet: CF-GNNExplainer__Qwen-14B__cora__2074

- Method: CF-GNNExplainer; configuration: Qwen-14B; dataset: cora; target node: 2074
- Explanation source: `./robustness_2026-10-30/production_a100/qwen14b_gptq_int4_cora_Response.json` ([410][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
To address the provided scenario, let's first identify the differences between the factual and counterfactual examples, focusing on the target node (node 2074). 

In the factual graph, node 2074 is classified as Theory and is connected to nodes 1636, 1647, 2607, and 2615. In the counterfactual graph, node 2074 is reclassified as Case_Based and is only connected to nodes 1636 and 2607.

### Differences in Node Connections

**Factual Example:**
- Node 2074 is connected to nodes 1636, 1647, 2607, and 2615.
- Node 2074 is classified as Theory.

**Counterfactual Example:**
- Node 2074 is connected to nodes 1636 and 2607.
- Node 2074 is reclassified as Case_Based.

### Node Differences

The primary difference lies in the connections and classification of node 2074. Specifically, the removal of edges connecting node 2074 to nodes 1647 and 2615 leads to a change in its classification from Theory to Case_Based.

### Filling the Dictionary

Based on the provided information, we can fill the `infos` dictionary as follows:

```python
infos = {
    'Target_Node_ID': '2074',
    'Factual_Target_Node_Neighbors': ['1636', '1647', '2607', '2615'],
    'Factual_Target_Node_Features': ['inform', 'review', 'handl', 'evid', 'featur', 'exampl', 'heurist', 'contextu', 'discuss', 'machin', 'implicit', 'manag', 'result', 'effect', 'strategi', 'work', 'supervis', 'method', 'hybrid'],
    'Counterfactual_Target_Node_Neighbors': ['1636', '2607'],
    'Counterfactual_Target_Node_Features': ['inform', 'review', 'handl', 'evid', 'featur', 'exampl', 'heurist', 'contextu', 'discuss', 'machin', 'implicit', 'manag', 'result', 'effect', 'strategi', 'work', 'supervis', 'method', 'hybrid'],
    'Factual_Target_Node_Class': 'Theory',
    'Counterfactual_Target_Node_class': 'Case_Based',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Natural_Language_Explanation': 'Node 2074 was originally classified as Theory and was connected to nodes 1636, 1647, 2607, and 2615. In the counterfactual scenario, node 2074 is reclassified as Case_Based after removing connections to nodes 1647 and 2615. The removal of these connections alters the influence of neighboring nodes, leading to a change in classification.'
}
```

### Explanation of Changes

In the factual graph, node 2074 is classified as Theory due to its connections to nodes 1636, 1647, 2607, and 2615. These connections likely indicate a broader theoretical context, possibly involving discussions on context-sensitive features and strategies.

In the counterfactual graph, the removal of connections to nodes 1647 and 2615 reduces the influence of nodes that are more aligned with theoretical and neural network themes. This shift in connectivity emphasizes the remaining connections to nodes 1636 and 2607, which are more closely associated with case-based reasoning and methodologies. Consequently, the classification of node 2074 changes from Theory to Case_Based, reflecting a stronger alignment with case-based reasoning principles.

This change highlights the importance of the graph structure and the influence of neighboring nodes in determining the classification of a node within a graph-based learning model.
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
given the factual graph: The node 245 is a product titled 'Title: ICML-96 Workshop "Learning in context-sensitive domains" Bari, Italy. Dynamically Adjusting C' with key attributes: domain, chang, exist, similar, group, dynam, attribut, object, set, determin, adjust, learner, advanc, context, togeth, requir, describ, result, darian, concept, known, base and is connected with the node 1636 and it is classified as Theory, it is not the target node. The node 928 is a product titled 'Title: Learning to Refine Case Libraries:  
Abstract: Initial Results Abstract. Conversational case-' with key attributes: reason, descript, increment, initi, convers, good, refin, librari, extract, effici, cbr, case, system, design, result, queri, precis, perform, difficult, larg, howev and is connected with the nodes 983, 1636 and it is classified as Case_Based, it is not the target node. The node 983 is a product titled 'Title: Refining Conversational Case Libraries  
Abstract: Conversational case-based reasoning (CBR)' with key attributes: reason, captur, express, nonprofit, convers, refin, rule, librari, success, relat, cbr, comprehens, case, contrast, system, develop, support, commerci, expert, applic, knowledg, tool and is connected with the nodes 928, 1636 and it is classified as Case_Based, it is not the target node. The node 1073 is a product titled 'Title: An adaptation of Relief for attribute estimation in regression  
Abstract: Heuristic measures' with key attributes: correctli, domain, extens, independ, estim, strong, measur, attribut, mostli, depend, classif, heurist, qualiti, adapt, assum, regress, capabl, perform and is connected with the node 1636 and it is classified as Rule_Learning, it is not the target node. The node 1636 is a product titled 'Title: Context-Sensitive Feature Selection for Lazy Learners  
Abstract:' with key attributes: featur, contextu, learner, lazi, select and is connected with the nodes 245, 928, 983, 1073, 1684, 2074 and it is classified as Case_Based, it is not the target node. The node 1647 is a product titled 'Title: Recognition and Exploitation of Contextual Clues via Incremental Meta-Learning (Extended Vers' with key attributes: extend, domain, chang, increment, depend, mean, implicit, real, context, mani, requir, caus, recognit, world, version, result, experi, concept, exploit, heavili and is connected with the nodes 1684, 1908, 2074, 2586, 2615 and it is classified as Theory, it is not the target node. The node 1684 is a product titled 'Title: Context-sensitive attribute estimation in regression  
Abstract: One of key issues in both di' with key attributes: reason, predict, issu, domain, independ, estim, strong, measur, class, attribut, mostli, depend, heurist, comprehens, contextu, machin, continu, qualiti, assum, regress, result, key, gener, discret and is connected with the nodes 1636, 1647 and it is classified as Rule_Learning, it is not the target node. The node 1908 is a product titled 'Title: Induction of Selective Bayesian Classifiers  
Abstract: In this paper, we examine previous wo' with key attributes: limit, naiv, review, carri, space, greedi, genet, sensit, featur, classifi, induct, previou, search, embed, result, examin, includ, bayesian, work, correl, select, scheme and is connected with the node 1647 and it is classified as Probabilistic_Methods, it is not the target node. The node 1987 is a product titled 'Title: Improving Minority Class Prediction Using Case-Specific Feature Weights  
Abstract: This pape' with key attributes: predict, class, address, weight, handl, genet, appli, natur, data, distribut, featur, set, cbr, process, languag, result, improv, framework and is connected with the node 2607 and it is classified as Case_Based, it is not the target node. The node 2074 is a product titled 'Title: The Management of Context-Sensitive Features: A Review of Strategies  
Abstract: In this pape' with key attributes: inform, review, handl, evid, featur, exampl, heurist, contextu, discuss, machin, implicit, manag, result, effect, strategi, work, supervis, method, hybrid and is connected with the nodes 1636, 1647, 2607, 2615 and it is classified as Theory, it is the target node. The node 2084 is a product titled 'Title: Synthesize, Optimize, Analyze, Repeat (SOAR): Application of Neural Network Tools to ECG Pati' with key attributes: network, optim, nonprofit, patient, monitor, neural, repeat, result, report, task, seattl, applic, tool, analyz and is connected with the node 2615 and it is classified as Neural_Networks, it is not the target node. The node 2310 is a product titled 'Title: Machine Learning: An Annotated Bibliography for the 1995 AI Statistics Tutorial on Machine Le' with key attributes: avail, question, workshop, brief, tutori, note, statist, read, machin, result, version, pleas and is connected with the node 2607 and it is classified as Case_Based, it is not the target node. The node 2369 is a product titled 'Title: Case-Based Sonogram Classification  
Abstract: This report replicates and extends results rep' with key attributes: extend, reason, empir, analys, imag, classif, center, novel, comprehens, cbr, standard, air, system, result, obtain, report, automat, compar, studi and is connected with the node 2607 and it is classified as Case_Based, it is not the target node. The node 2586 is a product titled 'Title: Learning One More Thing  
Abstract: Most research on machine learning has focused on scenario' with key attributes: lifetim, research, face, focus, thing, encount, relat, machin, opportun, transfer, learner, assum, singl, provid, result, recent, task, framework, knowledg, isol and is connected with the node 1647 and it is classified as Theory, it is not the target node. The node 2607 is a product titled 'Title: Concept Learning and Flexible Weighting  
Abstract: We previously introduced an exemplar mode' with key attributes: faster, limit, abil, previous, weight, highli, higher, artifici, exemplar, simul, flexibl, categor, name, rate, accuraci, model, asymptot, task, result, introduc, concept, record, scheme, exploit, sever and is connected with the nodes 1987, 2074, 2310, 2369 and it is classified as Case_Based, it is not the target node. The node 2615 is a product titled 'Title: A Patient-Adaptive Neural Network ECG Patient Monitoring Algorithm  
Abstract: The patient-ad' with key attributes: network, reduc, initi, addit, genet, patient, monitor, classifi, neural, major, train, error, seattl, consist, databas, compar, record and is connected with the nodes 1647, 2074, 2084 and it is classified as Neural_Networks, it is not the target node. and given the counterfactual example: The node 245 is a product titled 'Title: ICML-96 Workshop "Learning in context-sensitive domains" Bari, Italy. Dynamically Adjusting C' with key attributes: domain, chang, exist, similar, group, dynam, attribut, object, set, determin, adjust, learner, advanc, context, togeth, requir, describ, result, darian, concept, known, base and is connected with the node 1636 and it is classified as Theory, it is not the target node. The node 928 is a product titled 'Title: Learning to Refine Case Libraries:  
Abstract: Initial Results Abstract. Conversational case-' with key attributes: reason, descript, increment, initi, convers, good, refin, librari, extract, effici, cbr, case, system, design, result, queri, precis, perform, difficult, larg, howev and is connected with the nodes 983, 1636 and it is classified as Case_Based, it is not the target node. The node 983 is a product titled 'Title: Refining Conversational Case Libraries  
Abstract: Conversational case-based reasoning (CBR)' with key attributes: reason, captur, express, nonprofit, convers, refin, rule, librari, success, relat, cbr, comprehens, case, contrast, system, develop, support, commerci, expert, applic, knowledg, tool and is connected with the nodes 928, 1636 and it is classified as Case_Based, it is not the target node. The node 1073 is a product titled 'Title: An adaptation of Relief for attribute estimation in regression  
Abstract: Heuristic measures' with key attributes: correctli, domain, extens, independ, estim, strong, measur, attribut, mostli, depend, classif, heurist, qualiti, adapt, assum, regress, capabl, perform and is connected with the node 1636 and it is classified as Rule_Learning, it is not the target node. The node 1636 is a product titled 'Title: Context-Sensitive Feature Selection for Lazy Learners  
Abstract:' with key attributes: featur, contextu, learner, lazi, select and is connected with the nodes 245, 928, 983, 1073, 1684, 2074 and it is classified as Case_Based, it is not the target node. The node 1647 is a product titled 'Title: Recognition and Exploitation of Contextual Clues via Incremental Meta-Learning (Extended Vers' with key attributes: extend, domain, chang, increment, depend, mean, implicit, real, context, mani, requir, caus, recognit, world, version, result, experi, concept, exploit, heavili and is connected with the nodes 1684, 1908, 2586, 2615 and it is classified as Theory, it is not the target node. The node 1684 is a product titled 'Title: Context-sensitive attribute estimation in regression  
Abstract: One of key issues in both di' with key attributes: reason, predict, issu, domain, independ, estim, strong, measur, class, attribut, mostli, depend, heurist, comprehens, contextu, machin, continu, qualiti, assum, regress, result, key, gener, discret and is connected with the nodes 1636, 1647 and it is classified as Rule_Learning, it is not the target node. The node 1908 is a product titled 'Title: Induction of Selective Bayesian Classifiers  
Abstract: In this paper, we examine previous wo' with key attributes: limit, naiv, review, carri, space, greedi, genet, sensit, featur, classifi, induct, previou, search, embed, result, examin, includ, bayesian, work, correl, select, scheme and is connected with the node 1647 and it is classified as Probabilistic_Methods, it is not the target node. The node 1987 is a product titled 'Title: Improving Minority Class Prediction Using Case-Specific Feature Weights  
Abstract: This pape' with key attributes: predict, class, address, weight, handl, genet, appli, natur, data, distribut, featur, set, cbr, process, languag, result, improv, framework and is connected with the node 2607 and it is classified as Case_Based, it is not the target node. The node 2074 is a product titled 'Title: The Management of Context-Sensitive Features: A Review of Strategies  
Abstract: In this pape' with key attributes: inform, review, handl, evid, featur, exampl, heurist, contextu, discuss, machin, implicit, manag, result, effect, strategi, work, supervis, method, hybrid and is connected with the nodes 1636, 2607 and it is classified as Case_Based, it is the target node. The node 2084 is a product titled 'Title: Synthesize, Optimize, Analyze, Repeat (SOAR): Application of Neural Network Tools to ECG Pati' with key attributes: network, optim, nonprofit, patient, monitor, neural, repeat, result, report, task, seattl, applic, tool, analyz and is connected with the node 2615 and it is classified as Neural_Networks, it is not the target node. The node 2310 is a product titled 'Title: Machine Learning: An Annotated Bibliography for the 1995 AI Statistics Tutorial on Machine Le' with key attributes: avail, question, workshop, brief, tutori, note, statist, read, machin, result, version, pleas and is connected with the node 2607 and it is classified as Case_Based, it is not the target node. The node 2369 is a product titled 'Title: Case-Based Sonogram Classification  
Abstract: This report replicates and extends results rep' with key attributes: extend, reason, empir, analys, imag, classif, center, novel, comprehens, cbr, standard, air, system, result, obtain, report, automat, compar, studi and is connected with the node 2607 and it is classified as Case_Based, it is not the target node. The node 2586 is a product titled 'Title: Learning One More Thing  
Abstract: Most research on machine learning has focused on scenario' with key attributes: lifetim, research, face, focus, thing, encount, relat, machin, opportun, transfer, learner, assum, singl, provid, result, recent, task, framework, knowledg, isol and is connected with the node 1647 and it is classified as Theory, it is not the target node. The node 2607 is a product titled 'Title: Concept Learning and Flexible Weighting  
Abstract: We previously introduced an exemplar mode' with key attributes: faster, limit, abil, previous, weight, highli, higher, artifici, exemplar, simul, flexibl, categor, name, rate, accuraci, model, asymptot, task, result, introduc, concept, record, scheme, exploit, sever and is connected with the nodes 1987, 2074, 2310, 2369 and it is classified as Case_Based, it is not the target node. The node 2615 is a product titled 'Title: A Patient-Adaptive Neural Network ECG Patient Monitoring Algorithm  
Abstract: The patient-ad' with key attributes: network, reduc, initi, addit, genet, patient, monitor, classifi, neural, major, train, error, seattl, consist, databas, compar, record and is connected with the nodes 1647, 2084 and it is classified as Neural_Networks, it is not the target node.
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

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/cora/cf-gnnexplainer-canonical/random_seed_42_*` (key=410).

- Factual class: **Theory**
- Counterfactual class: **Case_Based**
- Removed edges (global ids, 2): (1647, 2074), (2074, 2615)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 2074 |
| Factual_Target_Node_Neighbors | 1636, 1647, 2607, 2615 |
| Factual_Target_Node_Features | inform, review, handl, evid, featur, exampl, heurist, contextu, discuss, machin, implicit, manag, result, effect, strategi, result, work, supervis, method, hybrid |
| Counterfactual_Target_Node_Neighbors | 1636, 2607 |
| Counterfactual_Target_Node_Features | inform, review, handl, evid, featur, exampl, heurist, contextu, discuss, machin, implicit, manag, result, effect, strategi, result, work, supervis, method, hybrid |
| Factual_Target_Node_Class | Theory |
| Counterfactual_Target_Node_class | Case_Based |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 1647, 2615 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 2074 |
| Factual_Target_Node_Neighbors | 1636, 1647, 2607, 2615 |
| Factual_Target_Node_Features | inform, review, handl, evid, featur, exampl, heurist, contextu, discuss, machin, implicit, manag, result, effect, strategi, result, work, supervis, method, hybrid |
| Counterfactual_Target_Node_Neighbors | 1636, 2607 |
| Counterfactual_Target_Node_Features | inform, review, handl, evid, featur, exampl, heurist, contextu, discuss, machin, implicit, manag, result, effect, strategi, result, work, supervis, method, hybrid |
| Factual_Target_Node_Class | Theory |
| Counterfactual_Target_Node_class | Case_Based |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 1647, 2615 |
| Natural_Language_Explanation | None |
