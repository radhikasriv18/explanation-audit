# Reference packet: CF-GNNExplainer__Llama-70B__cora__1443

- Method: CF-GNNExplainer; configuration: Llama-70B; dataset: cora; target node: 1443
- Explanation source: `./robustness_2026-10-30/llama70b/cf/cora/1443.json` (response)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, we can fill the dictionary as follows:

infos = {
    'Target_Node_ID': 1443,
    'Factual_Target_Node_Neighbors': [1540],
    'Factual_Target_Node_Features': ['coupl', 'vision', 'imag', 'appli', 'declar', 'sensit', 'sensor', 'effici', 'featur', 'littman', 'attent', 'visual', 'context', 'resolut', 'oper', 'uniform', 'analog', 'control'],
    'Counterfactual_Target_Node_Neighbors': [1540],
    'Counterfactual_Target_Node_Features': ['coupl', 'vision', 'imag', 'appli', 'declar', 'sensit', 'sensor', 'effici', 'featur', 'littman', 'attent', 'visual', 'context', 'resolut', 'oper', 'uniform', 'analog', 'control'],
    'Factual_Target_Node_Class': 'Reinforcement_Learning',
    'Counterfactual_Target_Node_class': 'Neural_Networks',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Node_Differences': [1045, 1459],
    'Edge_Differences': [(1045, 1540), (1459, 1540)],
    'Natural_Language_Explanation': ''
}

The target node 1443 has changed its classification from Reinforcement_Learning to Neural_Networks. Upon examining the neighbors of the target node, we notice that the node 1540 is still connected to the target node in both the factual and counterfactual examples. However, the neighbors of node 1045 and 1459 have changed, as they are no longer connected to any other nodes in the counterfactual example.

The change in classification of the target node can be attributed to the changes in the graph structure, particularly the disconnection of nodes 1045 and 1459 from the rest of the graph. This suggests that the classification of the target node is influenced by the presence or absence of certain neighbors, rather than just its own features.

In the factual example, node 1045 was connected to node 1540, which is a hub node with many connections to other nodes. This connection may have contributed to the classification of node 1443 as Reinforcement_Learning. In the counterfactual example, the disconnection of node 1045 from node 1540 may have reduced the influence of Reinforcement_Learning-related nodes on the classification of node 1443, leading to its reclassification as Neural_Networks.

Similarly, the disconnection of node 1459 from node 1540 may have also contributed to the change in classification of node 1443. Node 1459 is classified as Reinforcement_Learning, and its connection to node 1540 may have reinforced the Reinforcement_Learning classification of node 1443 in the factual example.

Overall, the changes in the graph structure, particularly the disconnections of nodes 1045 and 1459, have led to a change in the classification of the target node 1443 from Reinforcement_Learning to Neural_Networks.
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
given the factual graph: The node 565 is a product titled 'Title: Machine Learning Learning to Predict by the Methods of Temporal Differences Keywords: Increme' with key attributes: predict, futur, past, increment, class, keyword, articl, behavior, wherea, machin, incomplet, system, special, procedur, result, tempor, experi, introduc, known, differ, method, convent and is connected with the nodes 842, 1378, 1540 and it is classified as Reinforcement_Learning, it is not the target node. The node 842 is a product titled 'Title: Metrics for Temporal Difference Learning  
Abstract: For an absorbing Markov chain with a rei' with key attributes: simpl, optim, function, approxim, valu, respect, reinforc, depend, markov, exampl, give, transit, chain, metric, error, obtain, tempor, result, stationari, differ and is connected with the nodes 565, 1540 and it is classified as Reinforcement_Learning, it is not the target node. The node 1045 is a product titled 'Title: Spurious Solutions to the Bellman Equation  
Abstract: Reinforcement learning algorithms ofte' with key attributes: predict, optim, function, frequent, state, satisfi, equat, genet, appli, yield, reinforc, mdp, markov, chain, decis, finit, solut, process, result, action, work, control and is connected with the node 1540 and it is classified as Reinforcement_Learning, it is not the target node. The node 1118 is a product titled 'Title: Adapting Bias by Gradient Descent: An Incremental Version of Delta-Bar-Delta  
Abstract: Appr' with key attributes: increment, genet, effici, descent, view, previou, adapt, bias, appropri, bia, develop, wide, version, result, experi, key, gener, base and is connected with the node 1540 and it is classified as Reinforcement_Learning, it is not the target node. The node 1378 is a product titled 'Title: Generalization in Reinforcement Learning: Safely Approximating the Value Function  
Abstract:' with key attributes: dimension, inform, ed, function, appear, dynam, approxim, valu, reinforc, mit, replac, press, neural, advanc, process, system, program, result, tabl, cambridg, gener and is connected with the nodes 565, 1540 and it is classified as Reinforcement_Learning, it is not the target node. The node 1443 is a product titled 'Title: Residual Q-Learning Applied to Visual Attention  
Abstract: Foveal vision features imagers wi' with key attributes: coupl, vision, imag, appli, declar, sensit, sensor, effici, featur, littman, attent, visual, context, resolut, oper, uniform, analog, control and is connected with the node 1540 and it is classified as Reinforcement_Learning, it is the target node. The node 1459 is a product titled 'Title: Generalized Markov Decision Processes: Dynamic-programming and Reinforcement-learning Algorit' with key attributes: optim, class, maxim, total, expect, markovian, genet, environ, mdp, reward, markov, complet, particular, decis, observ, sequenti, process, develop, model, gener and is connected with the node 1540 and it is classified as Reinforcement_Learning, it is not the target node. The node 1540 is a product titled 'Title: MultiPlayer Residual Advantage Learning With General Function Approximation  
Abstract: A new' with key attributes: function, advantag, updat, approxim, genet, type, singl, requir, improv, result, gener, instanc and is connected with the nodes 565, 842, 1045, 1118, 1378, 1443, 1459 and it is classified as Reinforcement_Learning, it is not the target node. and given the counterfactual example: The node 565 is a product titled 'Title: Machine Learning Learning to Predict by the Methods of Temporal Differences Keywords: Increme' with key attributes: predict, futur, past, increment, class, keyword, articl, behavior, wherea, machin, incomplet, system, special, procedur, result, tempor, experi, introduc, known, differ, method, convent and is connected with the nodes 842, 1378 and it is classified as Reinforcement_Learning, it is not the target node. The node 842 is a product titled 'Title: Metrics for Temporal Difference Learning  
Abstract: For an absorbing Markov chain with a rei' with key attributes: simpl, optim, function, approxim, valu, respect, reinforc, depend, markov, exampl, give, transit, chain, metric, error, obtain, tempor, result, stationari, differ and is connected with the nodes 565, 1540 and it is classified as Reinforcement_Learning, it is not the target node. The node 1045 is a product titled 'Title: Spurious Solutions to the Bellman Equation  
Abstract: Reinforcement learning algorithms ofte' with key attributes: predict, optim, function, frequent, state, satisfi, equat, genet, appli, yield, reinforc, mdp, markov, chain, decis, finit, solut, process, result, action, work, control and is connected with no other nodes and it is classified as Reinforcement_Learning, it is not the target node. The node 1118 is a product titled 'Title: Adapting Bias by Gradient Descent: An Incremental Version of Delta-Bar-Delta  
Abstract: Appr' with key attributes: increment, genet, effici, descent, view, previou, adapt, bias, appropri, bia, develop, wide, version, result, experi, key, gener, base and is connected with the node 1540 and it is classified as Reinforcement_Learning, it is not the target node. The node 1378 is a product titled 'Title: Generalization in Reinforcement Learning: Safely Approximating the Value Function  
Abstract:' with key attributes: dimension, inform, ed, function, appear, dynam, approxim, valu, reinforc, mit, replac, press, neural, advanc, process, system, program, result, tabl, cambridg, gener and is connected with the node 565 and it is classified as Reinforcement_Learning, it is not the target node. The node 1443 is a product titled 'Title: Residual Q-Learning Applied to Visual Attention  
Abstract: Foveal vision features imagers wi' with key attributes: coupl, vision, imag, appli, declar, sensit, sensor, effici, featur, littman, attent, visual, context, resolut, oper, uniform, analog, control and is connected with the node 1540 and it is classified as Neural_Networks, it is the target node. The node 1459 is a product titled 'Title: Generalized Markov Decision Processes: Dynamic-programming and Reinforcement-learning Algorit' with key attributes: optim, class, maxim, total, expect, markovian, genet, environ, mdp, reward, markov, complet, particular, decis, observ, sequenti, process, develop, model, gener and is connected with no other nodes and it is classified as Reinforcement_Learning, it is not the target node. The node 1540 is a product titled 'Title: MultiPlayer Residual Advantage Learning With General Function Approximation  
Abstract: A new' with key attributes: function, advantag, updat, approxim, genet, type, singl, requir, improv, result, gener, instanc and is connected with the nodes 842, 1118, 1443 and it is classified as Reinforcement_Learning, it is not the target node.
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

- ID: 1443
- Title: Residual Q-Learning Applied to Visual Attention
- True class (canonical `y`): **Reinforcement_Learning**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Reinforcement_Learning**
- Prediction recorded by this method's pipeline: **Reinforcement_Learning**

Canonical text (`raw_text`):

~~~~~~text
Title: Residual Q-Learning Applied to Visual Attention  
Abstract: Foveal vision features imagers with graded acuity coupled with context sensitive sensor gaze control, analogous to that prevalent throughout vertebrate vision. Foveal vision operates more efficiently than uniform acuity vision because resolution is treated as a dynamically allocatable resource, but requires a more refined visual attention mechanism. We demonstrate that reinforcement learning (RL) significantly improves the performance of foveal visual attention, and of the overall vision system, for the task of model based target recognition. A simulated foveal vision system is shown to classify targets with fewer fixations by learning strategies for the acquisition of visual information relevant to the task, and learning how to generalize these strategies in ambiguous and unexpected scenario conditions.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 1540 | Reinforcement_Learning | MultiPlayer Residual Advantage Learning With General Function Approximation |

### 2-hop (shortest distance exactly 2): 6 nodes

| node id | true class | title |
|---|---|---|
| 565 | Reinforcement_Learning | Machine Learning Learning to Predict by the Methods of Temporal Differences Keywords: Incremental learning, prediction, |
| 842 | Reinforcement_Learning | Metrics for Temporal Difference Learning |
| 1045 | Reinforcement_Learning | Spurious Solutions to the Bellman Equation |
| 1118 | Neural_Networks | Adapting Bias by Gradient Descent: An Incremental Version of Delta-Bar-Delta |
| 1378 | Reinforcement_Learning | Generalization in Reinforcement Learning: Safely Approximating the Value Function |
| 1459 | Reinforcement_Learning | Generalized Markov Decision Processes: Dynamic-programming and Reinforcement-learning Algorithms |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/cora/cf-gnnexplainer-canonical/random_seed_42_*` (key=282).

- Factual class: **Reinforcement_Learning**
- Counterfactual class: **Neural_Networks**
- Removed edges (global ids, 4): (565, 1540), (1045, 1540), (1378, 1540), (1459, 1540)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 1443 |
| Factual_Target_Node_Neighbors | 1540 |
| Factual_Target_Node_Features | coupl, vision, imag, appli, declar, sensit, sensor, effici, featur, littman, attent, visual, context, resolut, oper, uniform, analog, control |
| Counterfactual_Target_Node_Neighbors | 1540 |
| Counterfactual_Target_Node_Features | coupl, vision, imag, appli, declar, sensit, sensor, effici, featur, littman, attent, visual, context, resolut, oper, uniform, analog, control |
| Factual_Target_Node_Class | Reinforcement_Learning |
| Counterfactual_Target_Node_class | Neural_Networks |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 1443 |
| Factual_Target_Node_Neighbors | 1540 |
| Factual_Target_Node_Features | coupl, vision, imag, appli, declar, sensit, sensor, effici, featur, littman, attent, visual, context, resolut, oper, uniform, analog, control |
| Counterfactual_Target_Node_Neighbors | 1540 |
| Counterfactual_Target_Node_Features | coupl, vision, imag, appli, declar, sensit, sensor, effici, featur, littman, attent, visual, context, resolut, oper, uniform, analog, control |
| Factual_Target_Node_Class | Reinforcement_Learning |
| Counterfactual_Target_Node_class | Neural_Networks |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |
