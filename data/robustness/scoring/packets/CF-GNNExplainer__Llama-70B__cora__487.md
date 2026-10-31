# Reference packet: CF-GNNExplainer__Llama-70B__cora__487

- Method: CF-GNNExplainer; configuration: Llama-70B; dataset: cora; target node: 487
- Explanation source: `./robustness_2026-10-30/llama70b/cf/cora/487.json` (response)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, we can fill the dictionary as follows:

infos = {
    'Target_Node_ID': 487,
    'Factual_Target_Node_Neighbors': [291, 538],
    'Factual_Target_Node_Features': ['dynam', 'system', 'languag'],
    'Counterfactual_Target_Node_Neighbors': [538],
    'Counterfactual_Target_Node_Features': ['dynam', 'system', 'languag'],
    'Factual_Target_Node_Class': 'Neural_Networks',
    'Counterfactual_Target_Node_class': 'Genetic_Algorithms',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Natural_Language_Explanation': 'The target node 487, initially classified as Neural_Networks, has changed its classification to Genetic_Algorithms in the counterfactual scenario. This change can be attributed to the loss of connection with node 291, which was initially connected to the target node. Node 291, classified as Neural_Networks, had a significant influence on the target node\'s initial classification. However, in the counterfactual scenario, the target node is only connected to node 538, which is classified as Genetic_Algorithms. As a result, the target node\'s features, which remain unchanged, are now more closely aligned with the characteristics of Genetic_Algorithms, leading to the change in classification.',
    'Node_Differences': [291],
    'Edge_Differences': [(487, 291)]
}

Explanation:
The target node 487, initially classified as Neural_Networks, has changed its classification to Genetic_Algorithms in the counterfactual scenario. This change can be attributed to the loss of connection with node 291, which was initially connected to the target node. Node 291, classified as Neural_Networks, had a significant influence on the target node's initial classification. However, in the counterfactual scenario, the target node is only connected to node 538, which is classified as Genetic_Algorithms. As a result, the target node's features, which remain unchanged, are now more closely aligned with the characteristics of Genetic_Algorithms, leading to the change in classification.

In terms of neighbor influences, node 291 played a crucial role in the target node's initial classification as Neural_Networks. The loss of this connection in the counterfactual scenario has led to a shift in the target node's classification towards Genetic_Algorithms, which is more closely aligned with the characteristics of node 538.
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
given the factual graph: The node 15 is a product titled 'Title: Back Propagation is Sensitive to Initial Conditions  
Abstract: This paper explores the effec' with key attributes: network, back, condit, simpl, vector, function, space, initi, weight, propag, sensit, explor, feed, techniqu, result, effect, signific, demonstr, compar, select, carlo and is connected with the nodes 129, 538 and it is classified as Genetic_Algorithms, it is not the target node. The node 129 is a product titled 'Title: Evolving Networks: Using the Genetic Algorithm with Connectionist Learning  
Abstract: A pilo' with key attributes: network, evolv, connectionist, genet, result and is connected with the nodes 15, 538, 1204, 2165, 2193 and it is classified as Genetic_Algorithms, it is not the target node. The node 291 is a product titled 'Title: NETWORKS WITH REAL WEIGHTS: ANALOG COMPUTATIONAL COMPLEXITY In contrast to classical computat' with key attributes: network, research, correspond, fix, weight, dynam, nrl, comput, time, classic, neural, particular, complex, real, type, contrast, system, structur, analog, model, report, invari, base and is connected with the node 487 and it is classified as Neural_Networks, it is not the target node. The node 402 is a product titled 'Title: The Evolutionary Cost of Learning  
Abstract: Traits that are acquired by members of an evolv' with key attributes: lifetim, chang, evolutionari, evolv, popul, specifi, thu, level, acquir, genet, explor, time, adapt, idea, shortcom, member, process, result, cost, becom, benefit, gener, gain and is connected with the node 538 and it is classified as Genetic_Algorithms, it is not the target node. The node 487 is a product titled 'Title: Language as a dynamical system  
Abstract: Designers across a variety of domains engage in ma' with key attributes: dynam, system, languag and is connected with the nodes 291, 538 and it is classified as Neural_Networks, it is the target node. The node 538 is a product titled 'Title: Learning and evolution in neural networks  
Abstract: DIMACS Technical Report 96-56 December' with key attributes: network, evolut, neural, result and is connected with the nodes 15, 129, 402, 487, 1036, 1204, 1689, 1738, 2165, 2193, 2309 and it is classified as Genetic_Algorithms, it is not the target node. The node 1036 is a product titled 'Title: Adaptive Behavior in Competing Co-Evolving Species  
Abstract: Co-evolution of competitive sp' with key attributes: dynam, behavior, environ, declar, compet, competit, role, adapt, speci, investig, argument, provid, result, experiment, interest, studi, differ and is connected with the node 538 and it is classified as Genetic_Algorithms, it is not the target node. The node 1204 is a product titled 'Title: The Role of Development in Genetic Algorithms  
Abstract: Technical Report Number CS94-394 Co' with key attributes: space, scienc, genet, comput, transform, typic, engin, analysi, understand, form, role, genotyp, phenotyp, ident, mechan, care, develop, represent, formul, technic, report, argu and is connected with the nodes 129, 538 and it is classified as Genetic_Algorithms, it is not the target node. The node 1689 is a product titled 'Title: Selection for Wandering Behavior in a Small Robot  
Abstract: We have evolved artificial neur' with key attributes: network, fix, period, evolv, behavior, artifici, possibl, simul, grid, time, neural, shortcom, robot, mani, squar, task, seattl, control, small, select and is connected with the nodes 538, 1738 and it is classified as Genetic_Algorithms, it is not the target node. The node 1738 is a product titled 'Title: Evolving nonTrivial Behaviors on Real Robots: an Autonomous Robot that Picks up Objects  
Abs' with key attributes: involv, face, clear, evolv, evolut, behavior, object, simul, form, real, adequ, robot, build, system, autonom, propos, result, life, recent, control, perform, may, howev and is connected with the nodes 538, 1689 and it is classified as Genetic_Algorithms, it is not the target node. The node 2165 is a product titled 'Title: Auto-teaching: networks that develop their own teaching input  
Abstract: Backpropagation lea' with key attributes: network, research, simul, featur, input, neural, intern, backpropag, teach, describ, develop, recent, result, experiment, gener, decid, tool and is connected with the nodes 129, 538, 2193 and it is classified as Genetic_Algorithms, it is not the target node. The node 2193 is a product titled 'Title: Growing neural networks  
Abstract: Selecting a set of features which is optimal for a given' with key attributes: network, neural, cell and is connected with the nodes 129, 538, 2165 and it is classified as Genetic_Algorithms, it is not the target node. The node 2309 is a product titled 'Title: EVOLVING SENSORS IN ENVIRONMENTS OF CONTROLLED COMPLEXITY  
Abstract: 1 . Sensors represent a' with key attributes: behav, latent, defin, abil, link, evolutionari, class, cognit, relationship, evolv, environ, sensor, energi, complex, crucial, forc, model, report, result, control, experi, stationari, shape, repres and is connected with the node 538 and it is classified as Genetic_Algorithms, it is not the target node. and given the counterfactual example: The node 15 is a product titled 'Title: Back Propagation is Sensitive to Initial Conditions  
Abstract: This paper explores the effec' with key attributes: network, back, condit, simpl, vector, function, space, initi, weight, propag, sensit, explor, feed, techniqu, result, effect, signific, demonstr, compar, select, carlo and is connected with the nodes 129, 538 and it is classified as Genetic_Algorithms, it is not the target node. The node 129 is a product titled 'Title: Evolving Networks: Using the Genetic Algorithm with Connectionist Learning  
Abstract: A pilo' with key attributes: network, evolv, connectionist, genet, result and is connected with the nodes 15, 538, 1204, 2165, 2193 and it is classified as Genetic_Algorithms, it is not the target node. The node 291 is a product titled 'Title: NETWORKS WITH REAL WEIGHTS: ANALOG COMPUTATIONAL COMPLEXITY In contrast to classical computat' with key attributes: network, research, correspond, fix, weight, dynam, nrl, comput, time, classic, neural, particular, complex, real, type, contrast, system, structur, analog, model, report, invari, base and is connected with no other nodes and it is classified as Neural_Networks, it is not the target node. The node 402 is a product titled 'Title: The Evolutionary Cost of Learning  
Abstract: Traits that are acquired by members of an evolv' with key attributes: lifetim, chang, evolutionari, evolv, popul, specifi, thu, level, acquir, genet, explor, time, adapt, idea, shortcom, member, process, result, cost, becom, benefit, gener, gain and is connected with the node 538 and it is classified as Genetic_Algorithms, it is not the target node. The node 487 is a product titled 'Title: Language as a dynamical system  
Abstract: Designers across a variety of domains engage in ma' with key attributes: dynam, system, languag and is connected with the node 538 and it is classified as Genetic_Algorithms, it is the target node. The node 538 is a product titled 'Title: Learning and evolution in neural networks  
Abstract: DIMACS Technical Report 96-56 December' with key attributes: network, evolut, neural, result and is connected with the nodes 15, 129, 402, 487, 1036, 1204, 1689, 1738, 2165, 2193, 2309 and it is classified as Genetic_Algorithms, it is not the target node. The node 1036 is a product titled 'Title: Adaptive Behavior in Competing Co-Evolving Species  
Abstract: Co-evolution of competitive sp' with key attributes: dynam, behavior, environ, declar, compet, competit, role, adapt, speci, investig, argument, provid, result, experiment, interest, studi, differ and is connected with the node 538 and it is classified as Genetic_Algorithms, it is not the target node. The node 1204 is a product titled 'Title: The Role of Development in Genetic Algorithms  
Abstract: Technical Report Number CS94-394 Co' with key attributes: space, scienc, genet, comput, transform, typic, engin, analysi, understand, form, role, genotyp, phenotyp, ident, mechan, care, develop, represent, formul, technic, report, argu and is connected with the nodes 129, 538 and it is classified as Genetic_Algorithms, it is not the target node. The node 1689 is a product titled 'Title: Selection for Wandering Behavior in a Small Robot  
Abstract: We have evolved artificial neur' with key attributes: network, fix, period, evolv, behavior, artifici, possibl, simul, grid, time, neural, shortcom, robot, mani, squar, task, seattl, control, small, select and is connected with the nodes 538, 1738 and it is classified as Genetic_Algorithms, it is not the target node. The node 1738 is a product titled 'Title: Evolving nonTrivial Behaviors on Real Robots: an Autonomous Robot that Picks up Objects  
Abs' with key attributes: involv, face, clear, evolv, evolut, behavior, object, simul, form, real, adequ, robot, build, system, autonom, propos, result, life, recent, control, perform, may, howev and is connected with the nodes 538, 1689 and it is classified as Genetic_Algorithms, it is not the target node. The node 2165 is a product titled 'Title: Auto-teaching: networks that develop their own teaching input  
Abstract: Backpropagation lea' with key attributes: network, research, simul, featur, input, neural, intern, backpropag, teach, describ, develop, recent, result, experiment, gener, decid, tool and is connected with the nodes 129, 538, 2193 and it is classified as Genetic_Algorithms, it is not the target node. The node 2193 is a product titled 'Title: Growing neural networks  
Abstract: Selecting a set of features which is optimal for a given' with key attributes: network, neural, cell and is connected with the nodes 129, 538, 2165 and it is classified as Genetic_Algorithms, it is not the target node. The node 2309 is a product titled 'Title: EVOLVING SENSORS IN ENVIRONMENTS OF CONTROLLED COMPLEXITY  
Abstract: 1 . Sensors represent a' with key attributes: behav, latent, defin, abil, link, evolutionari, class, cognit, relationship, evolv, environ, sensor, energi, complex, crucial, forc, model, report, result, control, experi, stationari, shape, repres and is connected with the node 538 and it is classified as Genetic_Algorithms, it is not the target node.
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

- ID: 487
- Title: Language as a dynamical system
- True class (canonical `y`): **Neural_Networks**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Neural_Networks**
- Prediction recorded by this method's pipeline: **Neural_Networks**

Canonical text (`raw_text`):

~~~~~~text
Title: Language as a dynamical system  
Abstract: Designers across a variety of domains engage in many of the same creative activities. Since much creativity stems from using old solutions in novel ways, we believe that case-based reasoning can be used to explain many creative design processes. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 2 nodes

| node id | true class | title |
|---|---|---|
| 291 | Neural_Networks | NETWORKS WITH REAL WEIGHTS: ANALOG COMPUTATIONAL COMPLEXITY In contrast to classical computational models, the models |
| 538 | Genetic_Algorithms | Learning and evolution in neural networks |

### 2-hop (shortest distance exactly 2): 10 nodes

| node id | true class | title |
|---|---|---|
| 15 | Neural_Networks | Back Propagation is Sensitive to Initial Conditions |
| 129 | Genetic_Algorithms | Evolving Networks: Using the Genetic Algorithm with Connectionist Learning |
| 402 | Genetic_Algorithms | The Evolutionary Cost of Learning |
| 1036 | Genetic_Algorithms | Adaptive Behavior in Competing Co-Evolving Species |
| 1204 | Genetic_Algorithms | The Role of Development in Genetic Algorithms |
| 1689 | Genetic_Algorithms | Selection for Wandering Behavior in a Small Robot |
| 1738 | Genetic_Algorithms | Evolving nonTrivial Behaviors on Real Robots: an Autonomous Robot that Picks up Objects |
| 2165 | Genetic_Algorithms | Auto-teaching: networks that develop their own teaching input |
| 2193 | Genetic_Algorithms | Growing neural networks |
| 2309 | Reinforcement_Learning | EVOLVING SENSORS IN ENVIRONMENTS OF CONTROLLED COMPLEXITY |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/cora/cf-gnnexplainer-canonical/random_seed_42_*` (key=78).

- Factual class: **Neural_Networks**
- Counterfactual class: **Genetic_Algorithms**
- Removed edges (global ids, 1): (291, 487)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 487 |
| Factual_Target_Node_Neighbors | 291, 538 |
| Factual_Target_Node_Features | dynam, system, languag |
| Counterfactual_Target_Node_Neighbors | 538 |
| Counterfactual_Target_Node_Features | dynam, system, languag |
| Factual_Target_Node_Class | Neural_Networks |
| Counterfactual_Target_Node_class | Genetic_Algorithms |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 291 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 487 |
| Factual_Target_Node_Neighbors | 291, 538 |
| Factual_Target_Node_Features | dynam, system, languag |
| Counterfactual_Target_Node_Neighbors | 538 |
| Counterfactual_Target_Node_Features | dynam, system, languag |
| Factual_Target_Node_Class | Neural_Networks |
| Counterfactual_Target_Node_class | Genetic_Algorithms |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 291 |
| Natural_Language_Explanation | None |
