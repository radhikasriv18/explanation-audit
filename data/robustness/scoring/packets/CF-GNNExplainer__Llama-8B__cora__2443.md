# Reference packet: CF-GNNExplainer__Llama-8B__cora__2443

- Method: CF-GNNExplainer; configuration: Llama-8B; dataset: cora; target node: 2443
- Explanation source: `./llm-graph-cf/data/results/cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_cora_standard_Response.json` ([480][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
To generate the counterfactual explanation, we need to first identify the target node and its classification in the factual graph. In this case, the target node is 2443, which is classified as Case_Based.

Next, we need to create a counterfactual graph by perturbing the adjacency matrix of the factual graph. Let's assume we perturb the adjacency matrix by adding an edge between nodes 2443 and 2677, which is not present in the original graph.

After perturbing the adjacency matrix, we get the following counterfactual graph:

Node 2443 is now connected to node 2677, which is classified as Case_Based. This change in the graph structure affects the classification of node 2443.

To fill the dictionary, we need to extract the relevant information from the factual and counterfactual graphs.

Node_Differences = [2443]

Edge_Differences = [(2443, 2677)]

Factual_Target_Node_Neighbors = [1339, 2338]
Counterfactual_Target_Node_Neighbors = [1339, 2338, 2677]

Factual_Target_Node_Features = ['condit', 'simpl', 'sometim', 'issu', 'previous', 'independ', 'class', 'attribut', 'data', 'integr', 'classifi', 'mine', 'surprisingli', 'visual', 'shown', 'model', 'bayesian', 'given', 'seattl', 'call', 'built', 'base']
Counterfactual_Target_Node_Features = ['condit', 'simpl', 'sometim', 'issu', 'previous', 'independ', 'class', 'attribut', 'data', 'integr', 'classifi', 'mine', 'surprisingli', 'visual', 'shown', 'model', 'bayesian', 'given', 'seattl', 'call', 'built', 'base']

Factual_Target_Node_Class = 'Case_Based'
Counterfactual_Target_Node_class = 'Case_Based'

Target_Node_Features_Changed_From_Factual_To_Counterfactual = []

Natural_Language_Explanation = "The addition of an edge between node 2443 and node 2677 changes the classification of node 2443 from Case_Based to Case_Based. This is because node 2677 is also classified as Case_Based, and the connection between the two nodes strengthens the Case_Based community in the graph."

Now, let's analyze the influence of the neighboring nodes on the classification of node 2443.

In the factual graph, node 2443 is connected to nodes 1339 and 2338, both of which are classified as Case_Based. However, in the counterfactual graph, node 2443 is connected to nodes 1339, 2338, and 2677, all of which are classified as Case_Based. This increased connectivity within the Case_Based community strengthens the classification of node 2443 as Case_Based.

Therefore, the counterfactual explanation for the change in classification of node 2443 is that the addition of an edge between node 2443 and node 2677 increases the connectivity within the Case_Based community, leading to a stronger classification of node 2443 as Case_Based.

The final answer is: 
infos={
'Target_Node_ID': 2443,
'Factual_Target_Node_Neighbors': [1339, 2338],
'Factual_Target_Node_Features': ['condit', 'simpl', 'sometim', 'issu', 'previous', 'independ', 'class', 'attribut', 'data', 'integr', 'classifi', 'mine', 'surprisingli', 'visual', 'shown', 'model', 'bayesian', 'given', 'seattl', 'call', 'built', 'base'],
'Counterfactual_Target_Node_Neighbors': [1339, 2338, 2677],
'Counterfactual_Target_Node_Features': ['condit', 'simpl', 'sometim', 'issu', 'previous', 'independ', 'class', 'attribut', 'data', 'integr', 'classifi', 'mine', 'surprisingli', 'visual', 'shown', 'model', 'bayesian', 'given', 'seattl', 'call', 'built', 'base'],
'Factual_Target_Node_Class': 'Case_Based',
'Counterfactual_Target_Node_class': 'Case_Based',
'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
'Natural_Language_Explanation': 'The addition of an edge between node 2443 and node 2677 changes the classification of node 2443 from Case_Based to Case_Based. This is because node 2677 is also classified as Case_Based, and the connection between the two nodes strengthens the Case_Based community in the graph.'
}
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
given the factual graph: The node 208 is a product titled 'Title: Feature Subset Selection as Search with Probabilistic Estimates  
Abstract: Irrelevant featur' with key attributes: comprehens, reduc, estim, space, induc, genet, featur, subset, accuraci, evalu, search, relev, probabilist, formul, result, irrelev, concept, select, supervis, may and is connected with the nodes 430, 2343 and it is classified as Theory, it is not the target node. The node 430 is a product titled 'Title: Irrelevant Features and the Subset Selection Problem  
Abstract: We address the problem of fi' with key attributes: literatur, address, induc, genet, notion, allow, featur, machin, induct, categori, subset, adequ, relev, examin, definit, result, irrelev, small, concept, select, partit, supervis and is connected with the nodes 208, 2343 and it is classified as Theory, it is not the target node. The node 434 is a product titled 'Title: Computational Learning in Humans and Machines  
Abstract: In this paper we review research on' with key attributes: research, issu, review, initi, behavior, comput, relat, machin, induct, complex, main, sequenti, result, examin, model, focu, consid, compar, concept, human and is connected with the node 1339 and it is classified as Theory, it is not the target node. The node 1024 is a product titled 'Title: On learning hierarchical classifications  
Abstract: Many significant real-world classificati' with key attributes: involv, hierarchi, librari, classif, topic, hierarch, exampl, classifi, categori, subject, investig, world, document, mani, signific, task, result, benefit, larg, scheme, potenti and is connected with the nodes 1335, 2338 and it is classified as Case_Based, it is not the target node. The node 1111 is a product titled 'Title: Towards a Better Understanding of Memory-Based Reasoning Systems  
Abstract: We quantify both' with key attributes: reason, similar, start, valu, genet, popular, insight, comprehens, classifi, understand, metric, system, better, analyt, capabl, bayesian, experiment, perform, compar, disambigu, gain, differ and is connected with the nodes 1339, 1570 and it is classified as Case_Based, it is not the target node. The node 1335 is a product titled 'Title: A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection  
Abstr' with key attributes: estim, review, bootstrap, restrict, good, artifici, common, data, set, classifi, shown, accuraci, result, model, experiment, compar, studi, theoret, select, method and is connected with the nodes 1024, 1337, 1339, 1478 and it is classified as Probabilistic_Methods, it is not the target node. The node 1337 is a product titled 'Title: MLC A Machine Learning Library in C  
Abstract: We present MLC ++ , a library of C ++ classes' with key attributes: varieti, research, class, genet, object, softwar, librari, increas, user, machin, main, acceler, provid, develop, wide, result, gener, supervis, expert, tool and is connected with the nodes 1335, 2343 and it is classified as Theory, it is not the target node. The node 1339 is a product titled 'Title: An Analysis of Bayesian Classifiers (1988), involves the formulation of average-case models f' with key attributes: involv, simpl, independ, target, genet, specif, analysi, classifi, remark, induct, assum, monoton, mani, conjunct, result, formul, model, bayesian, task, concept and is connected with the nodes 434, 1111, 1335, 1570, 1678, 2443, 2677 and it is classified as Theory, it is not the target node. The node 1478 is a product titled 'Title: Lazy Bayesian Trees  
Abstract: The naive Bayesian classifier is simple and effective, but it' with key attributes: simpl, naiv, independ, assumpt, tree, seek, attribut, genet, classifi, decis, lazi, real, local, build, develop, result, effect, world, bayesian, gener and is connected with the nodes 1335, 2338 and it is classified as Probabilistic_Methods, it is not the target node. The node 1570 is a product titled 'Title: Average-Case Analysis of a Nearest Neighbor Algorithm  
Abstract: In this paper we present an' with key attributes: research, simpl, space, nearest, neighbor, target, attribut, instanc, genet, distribut, analysi, induct, assum, boolean, mani, conjunct, uniform, result, recent, studi, concept, method and is connected with the nodes 1111, 1339, 1678 and it is classified as Theory, it is not the target node. The node 1618 is a product titled 'Title: Selection of Relevant Features and Examples in Machine Learning  
Abstract: In this survey, w' with key attributes: inform, issu, review, handl, survey, data, featur, exampl, set, machin, amount, relev, contain, result, focu, work, larg, key, irrelev, select, method and is connected with the node 2343 and it is classified as Theory, it is not the target node. The node 1678 is a product titled 'Title: Induction of One-Level Decision Trees  
Abstract: In recent years, researchers have made cons' with key attributes: research, simpl, practic, consider, tree, averag, deal, induc, genet, year, analysi, comprehens, case, induct, decis, result, task, worst, theoret, progress, impact and is connected with the nodes 1339, 1570 and it is classified as Theory, it is not the target node. The node 1986 is a product titled 'Title: BOOSTING AND NAIVE BAYESIAN LEARNING  
Abstract: Although so-called naive Bayesian classifica' with key attributes: practic, naiv, independ, assumpt, class, attribut, valu, success, classif, exampl, remark, boost, better, result, bayesian, given, gener, known, method and is connected with the node 2338 and it is classified as Case_Based, it is not the target node. The node 2127 is a product titled 'Title: NAIVE BAYESIAN LEARNING  Adapted from  
Abstract: We present a novel application of ILP to th' with key attributes: naiv, adapt, bayesian, result and is connected with the node 2338 and it is classified as Case_Based, it is not the target node. The node 2338 is a product titled 'Title: Beyond Independence: Conditions for the Optimality of the Simple Bayesian Classifier  
Abstra' with key attributes: appar, condit, simpl, domain, optim, independ, clear, class, good, attribut, depend, classifi, surprisingli, assum, exhibit, mani, contain, result, bayesian, given, commonli, perform and is connected with the nodes 1024, 1478, 1986, 2127, 2443, 2677 and it is classified as Case_Based, it is not the target node. The node 2343 is a product titled 'Title: Feature Subset Selection Using the Wrapper Method: Overfitting and Dynamic Search Space Topol' with key attributes: futur, optim, estim, space, dynam, topolog, guid, genet, overfit, statist, featur, set, heurist, induct, subset, box, search, perform, select, method and is connected with the nodes 208, 430, 1337, 1618, 2443 and it is classified as Neural_Networks, it is not the target node. The node 2443 is a product titled 'Title: Issues in the Integration of Data Mining and Data Visualization Visualizing the Simple Bayesi' with key attributes: condit, simpl, sometim, issu, previous, independ, class, attribut, data, integr, classifi, mine, surprisingli, visual, shown, model, bayesian, given, seattl, call, built, base and is connected with the nodes 1339, 2338, 2343 and it is classified as Theory, it is the target node. The node 2677 is a product titled 'Title: Mining and Model Simplicity: A Case Study in Diagnosis  
Abstract: Proceedings of the 2nd Int' with key attributes: diagnosi, artifici, intellig, data, case, acut, intern, mine, discoveri, publish, result, model, recent, version, proceed, associ, confer, studi, knowledg, right and is connected with the nodes 1339, 2338 and it is classified as Case_Based, it is not the target node. and given the counterfactual example: The node 208 is a product titled 'Title: Feature Subset Selection as Search with Probabilistic Estimates  
Abstract: Irrelevant featur' with key attributes: comprehens, reduc, estim, space, induc, genet, featur, subset, accuraci, evalu, search, relev, probabilist, formul, result, irrelev, concept, select, supervis, may and is connected with the nodes 430, 2343 and it is classified as Theory, it is not the target node. The node 430 is a product titled 'Title: Irrelevant Features and the Subset Selection Problem  
Abstract: We address the problem of fi' with key attributes: literatur, address, induc, genet, notion, allow, featur, machin, induct, categori, subset, adequ, relev, examin, definit, result, irrelev, small, concept, select, partit, supervis and is connected with the nodes 208, 2343 and it is classified as Theory, it is not the target node. The node 434 is a product titled 'Title: Computational Learning in Humans and Machines  
Abstract: In this paper we review research on' with key attributes: research, issu, review, initi, behavior, comput, relat, machin, induct, complex, main, sequenti, result, examin, model, focu, consid, compar, concept, human and is connected with the node 1339 and it is classified as Theory, it is not the target node. The node 1024 is a product titled 'Title: On learning hierarchical classifications  
Abstract: Many significant real-world classificati' with key attributes: involv, hierarchi, librari, classif, topic, hierarch, exampl, classifi, categori, subject, investig, world, document, mani, signific, task, result, benefit, larg, scheme, potenti and is connected with the nodes 1335, 2338 and it is classified as Case_Based, it is not the target node. The node 1111 is a product titled 'Title: Towards a Better Understanding of Memory-Based Reasoning Systems  
Abstract: We quantify both' with key attributes: reason, similar, start, valu, genet, popular, insight, comprehens, classifi, understand, metric, system, better, analyt, capabl, bayesian, experiment, perform, compar, disambigu, gain, differ and is connected with the nodes 1339, 1570 and it is classified as Case_Based, it is not the target node. The node 1335 is a product titled 'Title: A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection  
Abstr' with key attributes: estim, review, bootstrap, restrict, good, artifici, common, data, set, classifi, shown, accuraci, result, model, experiment, compar, studi, theoret, select, method and is connected with the nodes 1024, 1337, 1339, 1478 and it is classified as Probabilistic_Methods, it is not the target node. The node 1337 is a product titled 'Title: MLC A Machine Learning Library in C  
Abstract: We present MLC ++ , a library of C ++ classes' with key attributes: varieti, research, class, genet, object, softwar, librari, increas, user, machin, main, acceler, provid, develop, wide, result, gener, supervis, expert, tool and is connected with the nodes 1335, 2343 and it is classified as Theory, it is not the target node. The node 1339 is a product titled 'Title: An Analysis of Bayesian Classifiers (1988), involves the formulation of average-case models f' with key attributes: involv, simpl, independ, target, genet, specif, analysi, classifi, remark, induct, assum, monoton, mani, conjunct, result, formul, model, bayesian, task, concept and is connected with the nodes 434, 1111, 1335, 1570, 1678, 2443, 2677 and it is classified as Theory, it is not the target node. The node 1478 is a product titled 'Title: Lazy Bayesian Trees  
Abstract: The naive Bayesian classifier is simple and effective, but it' with key attributes: simpl, naiv, independ, assumpt, tree, seek, attribut, genet, classifi, decis, lazi, real, local, build, develop, result, effect, world, bayesian, gener and is connected with the nodes 1335, 2338 and it is classified as Probabilistic_Methods, it is not the target node. The node 1570 is a product titled 'Title: Average-Case Analysis of a Nearest Neighbor Algorithm  
Abstract: In this paper we present an' with key attributes: research, simpl, space, nearest, neighbor, target, attribut, instanc, genet, distribut, analysi, induct, assum, boolean, mani, conjunct, uniform, result, recent, studi, concept, method and is connected with the nodes 1111, 1339, 1678 and it is classified as Theory, it is not the target node. The node 1618 is a product titled 'Title: Selection of Relevant Features and Examples in Machine Learning  
Abstract: In this survey, w' with key attributes: inform, issu, review, handl, survey, data, featur, exampl, set, machin, amount, relev, contain, result, focu, work, larg, key, irrelev, select, method and is connected with the node 2343 and it is classified as Theory, it is not the target node. The node 1678 is a product titled 'Title: Induction of One-Level Decision Trees  
Abstract: In recent years, researchers have made cons' with key attributes: research, simpl, practic, consider, tree, averag, deal, induc, genet, year, analysi, comprehens, case, induct, decis, result, task, worst, theoret, progress, impact and is connected with the nodes 1339, 1570 and it is classified as Theory, it is not the target node. The node 1986 is a product titled 'Title: BOOSTING AND NAIVE BAYESIAN LEARNING  
Abstract: Although so-called naive Bayesian classifica' with key attributes: practic, naiv, independ, assumpt, class, attribut, valu, success, classif, exampl, remark, boost, better, result, bayesian, given, gener, known, method and is connected with the node 2338 and it is classified as Case_Based, it is not the target node. The node 2127 is a product titled 'Title: NAIVE BAYESIAN LEARNING  Adapted from  
Abstract: We present a novel application of ILP to th' with key attributes: naiv, adapt, bayesian, result and is connected with the node 2338 and it is classified as Case_Based, it is not the target node. The node 2338 is a product titled 'Title: Beyond Independence: Conditions for the Optimality of the Simple Bayesian Classifier  
Abstra' with key attributes: appar, condit, simpl, domain, optim, independ, clear, class, good, attribut, depend, classifi, surprisingli, assum, exhibit, mani, contain, result, bayesian, given, commonli, perform and is connected with the nodes 1024, 1478, 1986, 2127, 2443, 2677 and it is classified as Case_Based, it is not the target node. The node 2343 is a product titled 'Title: Feature Subset Selection Using the Wrapper Method: Overfitting and Dynamic Search Space Topol' with key attributes: futur, optim, estim, space, dynam, topolog, guid, genet, overfit, statist, featur, set, heurist, induct, subset, box, search, perform, select, method and is connected with the nodes 208, 430, 1337, 1618 and it is classified as Neural_Networks, it is not the target node. The node 2443 is a product titled 'Title: Issues in the Integration of Data Mining and Data Visualization Visualizing the Simple Bayesi' with key attributes: condit, simpl, sometim, issu, previous, independ, class, attribut, data, integr, classifi, mine, surprisingli, visual, shown, model, bayesian, given, seattl, call, built, base and is connected with the nodes 1339, 2338 and it is classified as Case_Based, it is the target node. The node 2677 is a product titled 'Title: Mining and Model Simplicity: A Case Study in Diagnosis  
Abstract: Proceedings of the 2nd Int' with key attributes: diagnosi, artifici, intellig, data, case, acut, intern, mine, discoveri, publish, result, model, recent, version, proceed, associ, confer, studi, knowledg, right and is connected with the nodes 1339, 2338 and it is classified as Case_Based, it is not the target node.
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

- ID: 2443
- Title: Issues in the Integration of Data Mining and Data Visualization Visualizing the Simple Bayesian Classifier
- True class (canonical `y`): **Probabilistic_Methods**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Theory**
- Prediction recorded by this method's pipeline: **Theory**

Canonical text (`raw_text`):

~~~~~~text
Title: Issues in the Integration of Data Mining and Data Visualization Visualizing the Simple Bayesian Classifier  
Abstract: The simple Bayesian classifier (SBC), sometimes called Naive-Bayes, is built based on a conditional independence model of each attribute given the class. The model was previously shown to be surprisingly robust to obvious violations of this independence assumption, yielding accurate classification models even when there are clear conditional dependencies. The SBC can serve as an excellent tool for initial exploratory data analysis when coupled with a visualizer that makes its structure comprehensible. We describe such a visual representation of the SBC model that has been successfully implemented. We describe the requirements we had for such a visualization and the design decisions we made to satisfy them. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 3 nodes

| node id | true class | title |
|---|---|---|
| 1339 | Theory | An Analysis of Bayesian Classifiers (1988), involves the formulation of average-case models for specific algorithms |
| 2338 | Case_Based | Beyond Independence: Conditions for the Optimality of the Simple Bayesian Classifier |
| 2343 | Probabilistic_Methods | Feature Subset Selection Using the Wrapper Method: Overfitting and Dynamic Search Space Topology |

### 2-hop (shortest distance exactly 2): 14 nodes

| node id | true class | title |
|---|---|---|
| 208 | Theory | Feature Subset Selection as Search with Probabilistic Estimates |
| 430 | Theory | Irrelevant Features and the Subset Selection Problem |
| 434 | Case_Based | Computational Learning in Humans and Machines |
| 1024 | Theory | On learning hierarchical classifications |
| 1111 | Case_Based | Towards a Better Understanding of Memory-Based Reasoning Systems |
| 1335 | Probabilistic_Methods | A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection |
| 1337 | Theory | MLC A Machine Learning Library in C |
| 1478 | Probabilistic_Methods | Lazy Bayesian Trees |
| 1570 | Case_Based | Average-Case Analysis of a Nearest Neighbor Algorithm |
| 1618 | Theory | Selection of Relevant Features and Examples in Machine Learning |
| 1678 | Theory | Induction of One-Level Decision Trees |
| 1986 | Theory | BOOSTING AND NAIVE BAYESIAN LEARNING |
| 2127 | Probabilistic_Methods | NAIVE BAYESIAN LEARNING  Adapted from |
| 2677 | Probabilistic_Methods | Mining and Model Simplicity: A Case Study in Diagnosis |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/cora/cf-gnnexplainer-canonical/random_seed_42_*` (key=480).

- Factual class: **Theory**
- Counterfactual class: **Case_Based**
- Removed edges (global ids, 1): (2343, 2443)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 2443 |
| Factual_Target_Node_Neighbors | 1339, 2338, 2343 |
| Factual_Target_Node_Features | condit, simpl, sometim, issu, previous, independ, class, attribut, data, integr, classifi, mine, surprisingli, visual, shown, model, bayesian, given, seattl, call, built, base |
| Counterfactual_Target_Node_Neighbors | 1339, 2338 |
| Counterfactual_Target_Node_Features | condit, simpl, sometim, issu, previous, independ, class, attribut, data, integr, classifi, mine, surprisingli, visual, shown, model, bayesian, given, seattl, call, built, base |
| Factual_Target_Node_Class | Theory |
| Counterfactual_Target_Node_class | Case_Based |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 2343 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 2443 |
| Factual_Target_Node_Neighbors | 1339, 2338, 2343 |
| Factual_Target_Node_Features | condit, simpl, sometim, issu, previous, independ, class, attribut, data, integr, classifi, mine, surprisingli, visual, shown, model, bayesian, given, seattl, call, built, base |
| Counterfactual_Target_Node_Neighbors | 1339, 2338 |
| Counterfactual_Target_Node_Features | condit, simpl, sometim, issu, previous, independ, class, attribut, data, integr, classifi, mine, surprisingli, visual, shown, model, bayesian, given, seattl, call, built, base |
| Factual_Target_Node_Class | Theory |
| Counterfactual_Target_Node_class | Case_Based |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 2343 |
| Natural_Language_Explanation | None |
