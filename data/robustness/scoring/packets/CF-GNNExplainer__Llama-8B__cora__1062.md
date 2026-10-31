# Reference packet: CF-GNNExplainer__Llama-8B__cora__1062

- Method: CF-GNNExplainer; configuration: Llama-8B; dataset: cora; target node: 1062
- Explanation source: `./llm-graph-cf/data/results/cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_cora_standard_Response.json` ([203][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, we will generate the dictionary for the counterfactual explanation.

The target node is 1062, which is classified as Theory. The factual graph shows that the node 1062 is connected to nodes 930, 1254, 1323, and 2651. The counterfactual graph shows that the node 1062 is connected to nodes 1254, 2651.

The node 1062 has the following features in the factual graph: function, dimens, exponenti, transfer, local, loss, singl, mani, squar, grow, error, base, neuron. In the counterfactual graph, the node 1062 has the same features.

The node 1062 is classified as Theory in both the factual and counterfactual graphs.

The node 1062 is connected to the following nodes in the factual graph: 930, 1254, 1323, 2651. In the counterfactual graph, the node 1062 is connected to the following nodes: 1254, 2651.

The node 1062 has the following neighbors in the factual graph: 930, 1254, 1323, 2651. In the counterfactual graph, the node 1062 has the following neighbors: 1254, 2651.

The node 1062 has the following features changed from the factual to the counterfactual graph: None.

The natural language explanation for the change in classification for the target node 1062 is: "The removal of the connection between node 1062 and node 930 in the counterfactual graph led to a change in the classification of node 1062 from Neural_Networks to Theory."

Here is the dictionary:

infos = {
    'Target_Node_ID': 1062,
    'Factual_Target_Node_Neighbors': [930, 1254, 1323, 2651],
    'Factual_Target_Node_Features': ['function', 'dimens', 'exponenti', 'transfer', 'local', 'loss', 'singl', 'mani', 'squar', 'grow', 'error', 'base', 'neuron'],
    'Counterfactual_Target_Node_Neighbors': [1254, 2651],
    'Counterfactual_Target_Node_Features': ['function', 'dimens', 'exponenti', 'transfer', 'local', 'loss', 'singl', 'mani', 'squar', 'grow', 'error', 'base', 'neuron'],
    'Factual_Target_Node_Class': 'Theory',
    'Counterfactual_Target_Node_class': 'Theory',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Natural_Language_Explanation': 'The removal of the connection between node 1062 and node 930 in the counterfactual graph led to a change in the classification of node 1062 from Neural_Networks to Theory.'
}

The influence of the neighbor nodes on the target node 1062 can be evaluated by analyzing the changes in the graph structure and the features of the target node. In this case, the removal of the connection between node 1062 and node 930 in the counterfactual graph led to a change in the classification of node 1062 from Neural_Networks to Theory. This suggests that node 930 has a significant influence on the classification of node 1062 in the factual graph.

However, it is worth noting that the Cora dataset is a complex graph with many nodes and edges, and the influence of neighbor nodes on the target node can be difficult to evaluate. A more detailed analysis of the graph structure and the features of the nodes would be required to fully understand the influence of the neighbor nodes on the target node.
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
given the factual graph: The node 805 is a product titled 'Title: Critical Points for Least-Squares Problems Involving Certain Analytic Functions, with Applica' with key attributes: parameter, involv, critic, certain, fit, function, assumpt, point, sigmoid, deal, data, set, establish, finit, regress, nonlinear, result, analyt, gener, applic and is connected with the node 930 and it is classified as Neural_Networks, it is not the target node. The node 930 is a product titled 'Title: BACKPROPAGATION CAN GIVE RISE TO SPURIOUS LOCAL MINIMA EVEN FOR NETWORKS WITHOUT HIDDEN LAYER' with key attributes: network, vector, function, weight, sigmoid, sum, hidden, layer, regard, rise, exampl, set, give, neural, transfer, backpropag, local, train, togeth, binari, squar, error, recent and is connected with the nodes 805, 1062, 1254 and it is classified as Neural_Networks, it is not the target node. The node 1062 is a product titled 'Title: Exponentially many local minima for single neurons  
Abstract: We show that for a single neur' with key attributes: function, dimens, exponenti, transfer, local, loss, singl, mani, squar, grow, error, base, neuron and is connected with the nodes 930, 1254, 1323, 2651 and it is classified as Neural_Networks, it is the target node. The node 1145 is a product titled 'Title: A Unifying View of Some Training Algorithms for Multilayer Perceptrons with FIR Filter Synaps' with key attributes: network, perceptron, genet, multilay, architectur, respons, neural, view, deriv, variou, finit, train, signal, come, publish, unifi, describ, model, filter, recent, interest, synaps and is connected with the node 1323 and it is classified as Neural_Networks, it is not the target node. The node 1149 is a product titled 'Title: What Size Neural Network Gives Optimal Generalization? Convergence Properties of Backpropagat' with key attributes: paradigm, network, optim, scale, accord, aspect, postdoctor, properti, converg, comput, import, read, give, machin, size, neural, backpropag, advanc, technic, report, result, studi, univers and is connected with the nodes 1150, 1323 and it is classified as Neural_Networks, it is not the target node. The node 1150 is a product titled 'Title: Lessons in Neural Network Training: Overfitting Lessons in Neural Network Training: Overfitti' with key attributes: reason, network, aspect, import, overfit, popular, machin, neural, train, mani, model, becom, result, gener, compar, may and is connected with the nodes 1149, 1323 and it is classified as Neural_Networks, it is not the target node. The node 1195 is a product titled 'Title: Statistical Evaluation of Neural Network Experiments: Minimum Requirements and Current Practi' with key attributes: network, practic, minimum, statist, neural, requir, evalu, experi, current and is connected with the node 1323 and it is classified as Neural_Networks, it is not the target node. The node 1254 is a product titled 'Title: BACKPROPAGATION SEPARATES WHERE PERCEPTRONS DO  
Abstract: Feedforward nets with sigmoidal ac' with key attributes: function, perceptron, point, sigmoid, minim, threshold, rule, criterion, separ, feedforward, classic, danger, backpropag, type, design, error, techniqu, result, cost, recent, darian, activ, aris, may and is connected with the nodes 930, 1062, 1464 and it is classified as Neural_Networks, it is not the target node. The node 1323 is a product titled 'Title: On the Distribution of Performance from Multiple Neural Network Trials, On the Distribution o' with key attributes: network, inform, research, back, physic, electr, group, postdoctor, comput, distribut, engin, brain, neural, depart, process, pharmaceut, program, trial, multipl, seattl, perform, univers and is connected with the nodes 1062, 1145, 1149, 1150, 1195 and it is classified as Neural_Networks, it is not the target node. The node 1464 is a product titled 'Title: LINEAR SYSTEMS WITH SIGN-OBSERVATIONS  
Abstract: This paper deals with systems that are obta' with key attributes: network, function, linear, appear, deal, natur, dayan, quantiz, output, neural, follow, observ, poisson, signal, process, system, provid, result, obtain, devic, studi, theori and is connected with the node 1254 and it is classified as Neural_Networks, it is not the target node. The node 2059 is a product titled 'Title: Challenges in Evolving Controllers for Physical Robots  
Abstract: General convergence result' with key attributes: defin, solv, class, perceptron, linear, updat, genet, converg, settl, variou, discrimin, procedur, result, includ, famili, gener, concept and is connected with the node 2651 and it is classified as Theory, it is not the target node. The node 2651 is a product titled 'Title: Relative Loss Bounds for Multidimensional Regression Problems  
Abstract: We study on-line ge' with key attributes: need, network, function, linear, rel, hidden, layer, deploy, allow, output, neural, transfer, line, bound, regress, loss, multidimension, node, multipl, activ, consid, gener, studi and is connected with the nodes 1062, 2059 and it is classified as Theory, it is not the target node. and given the counterfactual example: The node 805 is a product titled 'Title: Critical Points for Least-Squares Problems Involving Certain Analytic Functions, with Applica' with key attributes: parameter, involv, critic, certain, fit, function, assumpt, point, sigmoid, deal, data, set, establish, finit, regress, nonlinear, result, analyt, gener, applic and is connected with the node 930 and it is classified as Neural_Networks, it is not the target node. The node 930 is a product titled 'Title: BACKPROPAGATION CAN GIVE RISE TO SPURIOUS LOCAL MINIMA EVEN FOR NETWORKS WITHOUT HIDDEN LAYER' with key attributes: network, vector, function, weight, sigmoid, sum, hidden, layer, regard, rise, exampl, set, give, neural, transfer, backpropag, local, train, togeth, binari, squar, error, recent and is connected with the nodes 805, 1254 and it is classified as Neural_Networks, it is not the target node. The node 1062 is a product titled 'Title: Exponentially many local minima for single neurons  
Abstract: We show that for a single neur' with key attributes: function, dimens, exponenti, transfer, local, loss, singl, mani, squar, grow, error, base, neuron and is connected with the nodes 1254, 2651 and it is classified as Theory, it is the target node. The node 1145 is a product titled 'Title: A Unifying View of Some Training Algorithms for Multilayer Perceptrons with FIR Filter Synaps' with key attributes: network, perceptron, genet, multilay, architectur, respons, neural, view, deriv, variou, finit, train, signal, come, publish, unifi, describ, model, filter, recent, interest, synaps and is connected with the node 1323 and it is classified as Neural_Networks, it is not the target node. The node 1149 is a product titled 'Title: What Size Neural Network Gives Optimal Generalization? Convergence Properties of Backpropagat' with key attributes: paradigm, network, optim, scale, accord, aspect, postdoctor, properti, converg, comput, import, read, give, machin, size, neural, backpropag, advanc, technic, report, result, studi, univers and is connected with the nodes 1150, 1323 and it is classified as Neural_Networks, it is not the target node. The node 1150 is a product titled 'Title: Lessons in Neural Network Training: Overfitting Lessons in Neural Network Training: Overfitti' with key attributes: reason, network, aspect, import, overfit, popular, machin, neural, train, mani, model, becom, result, gener, compar, may and is connected with the nodes 1149, 1323 and it is classified as Neural_Networks, it is not the target node. The node 1195 is a product titled 'Title: Statistical Evaluation of Neural Network Experiments: Minimum Requirements and Current Practi' with key attributes: network, practic, minimum, statist, neural, requir, evalu, experi, current and is connected with the node 1323 and it is classified as Neural_Networks, it is not the target node. The node 1254 is a product titled 'Title: BACKPROPAGATION SEPARATES WHERE PERCEPTRONS DO  
Abstract: Feedforward nets with sigmoidal ac' with key attributes: function, perceptron, point, sigmoid, minim, threshold, rule, criterion, separ, feedforward, classic, danger, backpropag, type, design, error, techniqu, result, cost, recent, darian, activ, aris, may and is connected with the nodes 930, 1062 and it is classified as Neural_Networks, it is not the target node. The node 1323 is a product titled 'Title: On the Distribution of Performance from Multiple Neural Network Trials, On the Distribution o' with key attributes: network, inform, research, back, physic, electr, group, postdoctor, comput, distribut, engin, brain, neural, depart, process, pharmaceut, program, trial, multipl, seattl, perform, univers and is connected with the nodes 1145, 1149, 1150, 1195 and it is classified as Neural_Networks, it is not the target node. The node 1464 is a product titled 'Title: LINEAR SYSTEMS WITH SIGN-OBSERVATIONS  
Abstract: This paper deals with systems that are obta' with key attributes: network, function, linear, appear, deal, natur, dayan, quantiz, output, neural, follow, observ, poisson, signal, process, system, provid, result, obtain, devic, studi, theori and is connected with no other nodes and it is classified as Neural_Networks, it is not the target node. The node 2059 is a product titled 'Title: Challenges in Evolving Controllers for Physical Robots  
Abstract: General convergence result' with key attributes: defin, solv, class, perceptron, linear, updat, genet, converg, settl, variou, discrimin, procedur, result, includ, famili, gener, concept and is connected with the node 2651 and it is classified as Theory, it is not the target node. The node 2651 is a product titled 'Title: Relative Loss Bounds for Multidimensional Regression Problems  
Abstract: We study on-line ge' with key attributes: need, network, function, linear, rel, hidden, layer, deploy, allow, output, neural, transfer, line, bound, regress, loss, multidimension, node, multipl, activ, consid, gener, studi and is connected with the nodes 1062, 2059 and it is classified as Theory, it is not the target node.
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

- ID: 1062
- Title: Exponentially many local minima for single neurons
- True class (canonical `y`): **Theory**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Neural_Networks**
- Prediction recorded by this method's pipeline: **Neural_Networks**

Canonical text (`raw_text`):

~~~~~~text
Title: Exponentially many local minima for single neurons  
Abstract: We show that for a single neuron with the logistic function as the transfer function the number of local minima of the error function based on the square loss can grow exponentially in the dimension.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 4 nodes

| node id | true class | title |
|---|---|---|
| 930 | Neural_Networks | BACKPROPAGATION CAN GIVE RISE TO SPURIOUS LOCAL MINIMA EVEN FOR NETWORKS WITHOUT HIDDEN LAYERS |
| 1254 | Neural_Networks | BACKPROPAGATION SEPARATES WHERE PERCEPTRONS DO |
| 1323 | Neural_Networks | On the Distribution of Performance from Multiple Neural Network Trials, On the Distribution of Performance |
| 2651 | Theory | Relative Loss Bounds for Multidimensional Regression Problems |

### 2-hop (shortest distance exactly 2): 7 nodes

| node id | true class | title |
|---|---|---|
| 805 | Neural_Networks | Critical Points for Least-Squares Problems Involving Certain Analytic Functions, with Applications to Sigmoidal Nets |
| 1145 | Neural_Networks | A Unifying View of Some Training Algorithms for Multilayer Perceptrons with FIR Filter Synapses |
| 1149 | Neural_Networks | What Size Neural Network Gives Optimal Generalization? Convergence Properties of Backpropagation |
| 1150 | Neural_Networks | Lessons in Neural Network Training: Overfitting Lessons in Neural Network Training: Overfitting May be Harder |
| 1195 | Neural_Networks | Statistical Evaluation of Neural Network Experiments: Minimum Requirements and Current Practice |
| 1464 | Neural_Networks | LINEAR SYSTEMS WITH SIGN-OBSERVATIONS |
| 2059 | Theory | Challenges in Evolving Controllers for Physical Robots |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/cora/cf-gnnexplainer-canonical/random_seed_42_*` (key=203).

- Factual class: **Neural_Networks**
- Counterfactual class: **Theory**
- Removed edges (global ids, 3): (930, 1062), (1062, 1323), (1254, 1464)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 1062 |
| Factual_Target_Node_Neighbors | 930, 1254, 1323, 2651 |
| Factual_Target_Node_Features | function, dimens, exponenti, transfer, local, loss, singl, mani, squar, grow, error, base, neuron |
| Counterfactual_Target_Node_Neighbors | 1254, 2651 |
| Counterfactual_Target_Node_Features | function, dimens, exponenti, transfer, local, loss, singl, mani, squar, grow, error, base, neuron |
| Factual_Target_Node_Class | Neural_Networks |
| Counterfactual_Target_Node_class | Theory |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 930, 1323 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 1062 |
| Factual_Target_Node_Neighbors | 930, 1254, 1323, 2651 |
| Factual_Target_Node_Features | function, dimens, exponenti, transfer, local, loss, singl, mani, squar, grow, error, base, neuron |
| Counterfactual_Target_Node_Neighbors | 1254, 2651 |
| Counterfactual_Target_Node_Features | function, dimens, exponenti, transfer, local, loss, singl, mani, squar, grow, error, base, neuron |
| Factual_Target_Node_Class | Neural_Networks |
| Counterfactual_Target_Node_class | Theory |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 930, 1323 |
| Natural_Language_Explanation | None |
