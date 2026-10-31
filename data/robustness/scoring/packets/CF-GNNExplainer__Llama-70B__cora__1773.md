# Reference packet: CF-GNNExplainer__Llama-70B__cora__1773

- Method: CF-GNNExplainer; configuration: Llama-70B; dataset: cora; target node: 1773
- Explanation source: `./robustness_2026-10-30/llama70b/cf/cora/1773.json` (response)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, we can fill the dictionary as follows:

infos = {
    'Target_Node_ID': 1773,
    'Factual_Target_Node_Neighbors': [2545],
    'Factual_Target_Node_Features': ['paradigm', 'likelihood', 'defin', 'optim', 'fit', 'indic', 'global', 'financi', 'market', 'maximum', 'genet', 'simul', 'statist', 'multivari', 'canon', 'anneal', 'adapt', 'mechan', 'perform', 'eeg'],
    'Counterfactual_Target_Node_Neighbors': [],
    'Counterfactual_Target_Node_Features': ['paradigm', 'likelihood', 'defin', 'optim', 'fit', 'indic', 'global', 'financi', 'market', 'maximum', 'genet', 'simul', 'statist', 'multivari', 'canon', 'anneal', 'adapt', 'mechan', 'perform', 'eeg'],
    'Factual_Target_Node_Class': 'Neural_Networks',
    'Counterfactual_Target_Node_class': 'Probabilistic_Methods',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Node_Differences': [1773],
    'Edge_Differences': [(1773, 2545)],
    'Natural_Language_Explanation': ''
}

The natural language explanation for the change in classification for the target node 1773 is as follows:

"The target node 1773 was initially classified as 'Neural_Networks' due to its connections with node 2545, which is also classified as 'Neural_Networks'. However, when the connection between node 1773 and node 2545 is removed, the classification of node 1773 changes to 'Probabilistic_Methods'. This suggests that the presence of node 2545 in the neighborhood of node 1773 was influencing its classification towards 'Neural_Networks'. The removal of this connection allows the model to focus more on the features of node 1773 itself, leading to a reclassification as 'Probabilistic_Methods'.

It's worth noting that the features of node 1773 remain the same in both the factual and counterfactual scenarios, indicating that the change in classification is primarily driven by the change in the graph structure rather than any changes in the node's attributes.

In terms of the influence of neighboring nodes, it appears that node 2545 was exerting a significant influence on the classification of node 1773. The removal of this connection allows node 1773 to be classified based on its own features, rather than being influenced by the classification of its neighbor. This highlights the importance of considering the graph structure and the influence of neighboring nodes when interpreting the classifications produced by graph-based machine learning models."
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
given the factual graph: The node 1773 is a product titled 'Title: Canonical Momenta Indicators of Financial Markets and Neocortical EEG  
Abstract: A paradigm' with key attributes: paradigm, likelihood, defin, optim, fit, indic, global, financi, market, maximum, genet, simul, statist, multivari, canon, anneal, adapt, mechan, perform, eeg and is connected with the node 2545 and it is classified as Neural_Networks, it is the target node. The node 1794 is a product titled 'Title: NONLINEAR NONEQUILIBRIUM NONQUANTUM NONCHAOTIC STATISTICAL MECHANICS OF NEOCORTICAL INTERACTI' with key attributes: financi, market, statist, mechan, applic and is connected with the nodes 1795, 2178, 2545 and it is classified as Neural_Networks, it is not the target node. The node 1795 is a product titled 'Title: Application of statistical mechanics methodol- ogy to term-structure bond-pricing models, Mat' with key attributes: comput, statist, mechan, model, applic and is connected with the nodes 1794, 2082, 2178, 2545 and it is classified as Neural_Networks, it is not the target node. The node 2082 is a product titled 'Title: %A L. Ingber %T Adaptive simulated annealing (ASA): Lessons learned %J Control and Cybernetic' with key attributes: simul, anneal, adapt, result, control and is connected with the nodes 1795, 2178, 2545 and it is classified as Neural_Networks, it is not the target node. The node 2178 is a product titled 'Title: Statistical Mechanics of Nonlinear Nonequilibrium Financial Markets: Applications to Optimize' with key attributes: paradigm, optim, fit, financi, market, genet, simul, trade, statist, adapt, nonlinear, mechan, publish, mathemat, model, applic and is connected with the nodes 1794, 1795, 2082, 2545 and it is classified as Neural_Networks, it is not the target node. The node 2545 is a product titled 'Title: Volatility of Volatility of Financial Markets  
Abstract: We present empirical evidence for c' with key attributes: empir, issu, futur, treat, financi, market, evid, statist, standard, previou, constant, mechan, process, requir, develop, model, consid, gener, stochast and is connected with the nodes 1773, 1794, 1795, 2082, 2178 and it is classified as Neural_Networks, it is not the target node. and given the counterfactual example: The node 1773 is a product titled 'Title: Canonical Momenta Indicators of Financial Markets and Neocortical EEG  
Abstract: A paradigm' with key attributes: paradigm, likelihood, defin, optim, fit, indic, global, financi, market, maximum, genet, simul, statist, multivari, canon, anneal, adapt, mechan, perform, eeg and is connected with no other nodes and it is classified as Probabilistic_Methods, it is the target node. The node 1794 is a product titled 'Title: NONLINEAR NONEQUILIBRIUM NONQUANTUM NONCHAOTIC STATISTICAL MECHANICS OF NEOCORTICAL INTERACTI' with key attributes: financi, market, statist, mechan, applic and is connected with the nodes 1795, 2178, 2545 and it is classified as Neural_Networks, it is not the target node. The node 1795 is a product titled 'Title: Application of statistical mechanics methodol- ogy to term-structure bond-pricing models, Mat' with key attributes: comput, statist, mechan, model, applic and is connected with the nodes 1794, 2082, 2178, 2545 and it is classified as Neural_Networks, it is not the target node. The node 2082 is a product titled 'Title: %A L. Ingber %T Adaptive simulated annealing (ASA): Lessons learned %J Control and Cybernetic' with key attributes: simul, anneal, adapt, result, control and is connected with the nodes 1795, 2178, 2545 and it is classified as Neural_Networks, it is not the target node. The node 2178 is a product titled 'Title: Statistical Mechanics of Nonlinear Nonequilibrium Financial Markets: Applications to Optimize' with key attributes: paradigm, optim, fit, financi, market, genet, simul, trade, statist, adapt, nonlinear, mechan, publish, mathemat, model, applic and is connected with the nodes 1794, 1795, 2082, 2545 and it is classified as Neural_Networks, it is not the target node. The node 2545 is a product titled 'Title: Volatility of Volatility of Financial Markets  
Abstract: We present empirical evidence for c' with key attributes: empir, issu, futur, treat, financi, market, evid, statist, standard, previou, constant, mechan, process, requir, develop, model, consid, gener, stochast and is connected with the nodes 1794, 1795, 2082, 2178 and it is classified as Neural_Networks, it is not the target node.
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

- ID: 1773
- Title: Canonical Momenta Indicators of Financial Markets and Neocortical EEG
- True class (canonical `y`): **Neural_Networks**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Neural_Networks**
- Prediction recorded by this method's pipeline: **Neural_Networks**

Canonical text (`raw_text`):

~~~~~~text
Title: Canonical Momenta Indicators of Financial Markets and Neocortical EEG  
Abstract: A paradigm of statistical mechanics of financial markets (SMFM) is fit to multivariate financial markets using Adaptive Simulated Annealing (ASA), a global optimization algorithm, to perform maximum likelihood fits of Lagrangians defined by path integrals of multivariate conditional probabilities. Canonical momenta are thereby derived and used as technical indicators in a recursive ASA optimization process to tune trading rules. These trading rules are then used on out-of-sample data, to demonstrate that they can profit from the SMFM model, to illustrate that these markets are likely not efficient. This methodology can be extended to other systems, e.g., electroencephalography. This approach to complex systems emphasizes the utility of blending an intuitive and powerful mathematical-physics formalism to generate indicators which are used by AI-type rule-based models of management. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 2545 | Neural_Networks | Volatility of Volatility of Financial Markets |

### 2-hop (shortest distance exactly 2): 4 nodes

| node id | true class | title |
|---|---|---|
| 1794 | Neural_Networks | NONLINEAR NONEQUILIBRIUM NONQUANTUM NONCHAOTIC STATISTICAL MECHANICS OF NEOCORTICAL INTERACTIONS |
| 1795 | Neural_Networks | Application of statistical mechanics methodol- ogy to term-structure bond-pricing models, Mathl. Comput. Modelling Application of |
| 2082 | Genetic_Algorithms | %A L. Ingber %T Adaptive simulated annealing (ASA): Lessons learned %J Control and Cybernetics Annealing |
| 2178 | Neural_Networks | Statistical Mechanics of Nonlinear Nonequilibrium Financial Markets: Applications to Optimized Trading |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/cora/cf-gnnexplainer-canonical/random_seed_42_*` (key=355).

- Factual class: **Neural_Networks**
- Counterfactual class: **Probabilistic_Methods**
- Removed edges (global ids, 1): (1773, 2545)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 1773 |
| Factual_Target_Node_Neighbors | 2545 |
| Factual_Target_Node_Features | paradigm, likelihood, defin, optim, fit, indic, global, financi, market, maximum, genet, simul, statist, multivari, canon, anneal, adapt, mechan, perform, eeg |
| Counterfactual_Target_Node_Neighbors |  |
| Counterfactual_Target_Node_Features | paradigm, likelihood, defin, optim, fit, indic, global, financi, market, maximum, genet, simul, statist, multivari, canon, anneal, adapt, mechan, perform, eeg |
| Factual_Target_Node_Class | Neural_Networks |
| Counterfactual_Target_Node_class | Probabilistic_Methods |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 2545 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 1773 |
| Factual_Target_Node_Neighbors | 2545 |
| Factual_Target_Node_Features | paradigm, likelihood, defin, optim, fit, indic, global, financi, market, maximum, genet, simul, statist, multivari, canon, anneal, adapt, mechan, perform, eeg |
| Counterfactual_Target_Node_Neighbors |  |
| Counterfactual_Target_Node_Features | paradigm, likelihood, defin, optim, fit, indic, global, financi, market, maximum, genet, simul, statist, multivari, canon, anneal, adapt, mechan, perform, eeg |
| Factual_Target_Node_Class | Neural_Networks |
| Counterfactual_Target_Node_class | Probabilistic_Methods |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 2545 |
| Natural_Language_Explanation | None |
