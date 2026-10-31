# Reference packet: CF-GNNExplainer__Llama-8B__cora__2257

- Method: CF-GNNExplainer; configuration: Llama-8B; dataset: cora; target node: 2257
- Explanation source: `./llm-graph-cf/data/results/cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_cora_standard_Response.json` ([442][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, we will generate the dictionary for the counterfactual explanation.

The target node is 2257, which is classified as Reinforcement_Learning. To generate the counterfactual explanation, we will perturb the adjacency matrix of the graph to create a new graph where the target node is classified as Genetic_Algorithms.

After perturbing the adjacency matrix, we get the following changes:

Node_Differences = [22, 129, 163, 191, 1790]

Edge_Differences = [(22, 2257), (129, 2257), (163, 2257), (191, 2257), (1790, 2257)]

The node 2257 is now connected to the nodes 22, 129, 163, 191, and 1790, which are all classified as Genetic_Algorithms. This change in connectivity leads to a change in the classification of the target node 2257 from Reinforcement_Learning to Genetic_Algorithms.

Factual_Target_Node_Neighbors = [500, 563, 982, 1117, 1261, 1973, 2446]
Counterfactual_Target_Node_Neighbors = [22, 129, 163, 191, 1790]

Factual_Target_Node_Features = ['network', 'futur', 'solv', 'interact', 'fix', 'way', 'best', 'handl', 'evolv', 'popul', 'instanc', 'standard', 'solut', 'peg', 'result', 'task', 'hard', 'compar']
Counterfactual_Target_Node_Features = ['network', 'evolutionari', 'discov', 'evolut', 'artifici', 'standard', 'neural', 'play', 'complex', 'direct', 'program', 'search', 'develop', 'game', 'strategi', 'seattl', 'base']

Factual_Target_Node_Class = 'Reinforcement_Learning'
Counterfactual_Target_Node_class = 'Genetic_Algorithms'

Target_Node_Features_Changed_From_Factual_To_Counterfactual = ['futur', 'solv', 'interact', 'fix', 'way', 'best', 'handl', 'popul', 'instanc', 'standard', 'solut', 'peg', 'result', 'task', 'hard', 'compar']

Natural_Language_Explanation = "The target node 2257 was classified as Reinforcement_Learning because it was connected to nodes that were focused on reinforcement learning techniques. However, when we perturbed the adjacency matrix to connect it to nodes that were focused on genetic algorithms, the target node's classification changed to Genetic_Algorithms. This suggests that the target node's features and connections played a crucial role in determining its classification."

Here is the filled dictionary:

infos={
'Target_Node_ID': 2257,
'Factual_Target_Node_Neighbors': [500, 563, 982, 1117, 1261, 1973, 2446],
'Factual_Target_Node_Features': ['network', 'futur', 'solv', 'interact', 'fix', 'way', 'best', 'handl', 'evolv', 'popul', 'instanc', 'standard', 'solut', 'peg', 'result', 'task', 'hard', 'compar'],
'Counterfactual_Target_Node_Neighbors': [22, 129, 163, 191, 1790],
'Counterfactual_Target_Node_Features': ['network', 'evolutionari', 'discov', 'evolut', 'artifici', 'standard', 'neural', 'play', 'complex', 'direct', 'program', 'search', 'develop', 'game', 'strategi', 'seattl', 'base'],
'Factual_Target_Node_Class': 'Reinforcement_Learning',
'Counterfactual_Target_Node_class': 'Genetic_Algorithms',
'Target_Node_Features_Changed_From_Factual_To_Counterfactual': ['futur', 'solv', 'interact', 'fix', 'way', 'best', 'handl', 'popul', 'instanc', 'standard', 'solut', 'peg', 'result', 'task', 'hard', 'compar'],
'Natural_Language_Explanation': "The target node 2257 was classified as Reinforcement_Learning because it was connected to nodes that were focused on reinforcement learning techniques. However, when we perturbed the adjacency matrix to connect it to nodes that were focused on genetic algorithms, the target node's classification changed to Genetic_Algorithms. This suggests that the target node's features and connections played a crucial role in determining its classification."}
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
given the factual graph: The node 22 is a product titled 'Title: Discovering Complex Othello Strategies Through Evolutionary Neural Networks  
Abstract: An ap' with key attributes: network, evolutionari, discov, evolut, artifici, standard, neural, play, complex, direct, program, search, develop, game, strategi, seattl, base and is connected with the nodes 129, 163, 191, 1790, 2257 and it is classified as Genetic_Algorithms, it is not the target node. The node 129 is a product titled 'Title: Evolving Networks: Using the Genetic Algorithm with Connectionist Learning  
Abstract: A pilo' with key attributes: network, evolv, connectionist, genet, result and is connected with the nodes 22, 163, 1973, 2446 and it is classified as Genetic_Algorithms, it is not the target node. The node 163 is a product titled 'Title: 4 Implementing Application Specific Routines  Genetic algorithms in search, optimization, and' with key attributes: network, optim, evolutionari, acquisit, modul, artifici, genet, write, submit, concaten, ieee, neural, recurr, search, represent, life, technic, report, construct and is connected with the nodes 22, 129, 191, 563, 982 and it is classified as Genetic_Algorithms, it is not the target node. The node 191 is a product titled 'Title: USING MARKER-BASED GENETIC ENCODING OF NEURAL NETWORKS TO EVOLVE FINITE-STATE BEHAVIOUR  
Abs' with key attributes: encod, network, connect, creatur, evolv, aspect, genet, dna, allow, neural, biolog, mechan, behaviour, propos, node, structur, includ, base and is connected with the nodes 22, 163 and it is classified as Genetic_Algorithms, it is not the target node. The node 247 is a product titled 'Title: Machine Learning,  Efficient Reinforcement Learning through Symbiotic Evolution  
Abstract: T' with key attributes: network, evolv, popul, evolut, articl, genet, reinforc, effici, machin, neural, form, adapt, result, capabl, task, perform, call, neuron, method and is connected with the nodes 500, 563, 982, 1117, 1261, 1973, 2257, 2446 and it is classified as Reinforcement_Learning, it is not the target node. The node 500 is a product titled 'Title: 2-D Pole Balancing with Recurrent Evolutionary Networks  
Abstract: The success of evolutiona' with key attributes: need, network, creat, evolutionari, measur, serv, benchmark, success, effici, classic, standard, recurr, balanc, system, result, recent, task, control, difficult, method and is connected with the nodes 247, 563, 1767, 2444 and it is classified as Reinforcement_Learning, it is not the target node. The node 563 is a product titled 'Title: Evolving Obstacle Avoidance Behavior in a Robot Arm  
Abstract: Existing approaches for learn' with key attributes: exist, avoid, evolv, behavior, reli, declar, obstacl, explicitli, exampl, correct, robot, arm, given, result, control, difficult, hard, supervis, method, howev and is connected with the nodes 163, 247, 500 and it is classified as Reinforcement_Learning, it is not the target node. The node 982 is a product titled 'Title: Evolutionary Neural Networks for Value Ordering in Constraint Satisfaction Problems  
Abstrac' with key attributes: network, cooper, evolutionari, evolv, good, satisfact, valu, order, neural, form, individu, constraint, search, techniqu, develop, strategi, technic, report, call, neuron, method, may and is connected with the nodes 163, 247 and it is classified as Genetic_Algorithms, it is not the target node. The node 1117 is a product titled 'Title: A Coevolutionary Approach to Learning Sequential Decision Rules  
Abstract: We present a coev' with key attributes: independ, evolutionari, advantag, appear, evolv, stabl, rule, altern, simpler, format, complex, decis, sequenti, coevolutionari, direct, provid, result, control, repres and is connected with the nodes 247, 1261 and it is classified as Reinforcement_Learning, it is not the target node. The node 1261 is a product titled 'Title: EVOLVING NEURAL NETWORKS WITH COLLABORATIVE SPECIES  
Abstract: We present a coevolutionary a' with key attributes: network, solv, advantag, evolv, evolut, decompos, artifici, appli, natur, architectur, simpler, neural, speci, coevolutionari, util, techniqu, result, recent, preliminari, work, repres and is connected with the nodes 247, 1117 and it is classified as Reinforcement_Learning, it is not the target node. The node 1767 is a product titled 'Title: Incremental Evolution of Complex General Behavior  
Abstract: Several researchers have demons' with key attributes: network, research, increment, avoid, evolv, turn, evolut, behavior, genet, environ, sequenc, obstacl, specif, neural, complex, action, result, demonstr, gener, howev, sever and is connected with the nodes 500, 2257 and it is classified as Reinforcement_Learning, it is not the target node. The node 1768 is a product titled 'Title: Evolving Neural Networks to Play Go  
Abstract: Go is a difficult game for computers to maste' with key attributes: need, network, best, evolv, averag, comput, neural, tradit, sinc, play, adapt, proven, player, program, techniqu, result, game, difficult, studi, human and is connected with the node 2257 and it is classified as Reinforcement_Learning, it is not the target node. The node 1790 is a product titled 'Title: Using Genetic Programming to Evolve Board Evaluation Functions  
Abstract: The purpose of mos' with key attributes: paradigm, function, enabl, evolv, genet, feasibl, comput, play, employ, program, evalu, result, formul, strategi, term and is connected with the node 22 and it is classified as Genetic_Algorithms, it is not the target node. The node 1973 is a product titled 'Title: ON MCMC METHODS IN BAYESIAN REGRESSION ANALYSIS AND MODEL SELECTION  
Abstract: 1] R.K. Belew' with key attributes: network, ed, back, scienc, evolv, connectionist, propag, artifici, genet, complex, train, addison, life, result, studi and is connected with the nodes 129, 247 and it is classified as Genetic_Algorithms, it is not the target node. The node 2257 is a product titled 'Title: Real-time Interactive Neuro-evolution  
Abstract: In standard neuro-evolution, a population o' with key attributes: network, futur, solv, interact, fix, way, best, handl, evolv, popul, instanc, standard, solut, peg, result, task, hard, compar and is connected with the nodes 22, 247, 1767, 1768, 2444 and it is classified as Reinforcement_Learning, it is the target node. The node 2444 is a product titled 'Title: Symbiotic Evolution of Neural Networks in Sequential Decision Tasks  
Abstract: The simple Ba' with key attributes: network, evolut, neural, decis, sequenti, task and is connected with the nodes 500, 2257 and it is classified as Reinforcement_Learning, it is not the target node. The node 2446 is a product titled 'Title: Simulation of Reduced Precision Arithmetic for Digital Neural Networks Using the RAP Machine' with key attributes: network, ed, back, scienc, evolv, connectionist, propag, artifici, genet, complex, train, addison, life, result, studi and is connected with the nodes 129, 247 and it is classified as Genetic_Algorithms, it is not the target node. and given the counterfactual example: The node 22 is a product titled 'Title: Discovering Complex Othello Strategies Through Evolutionary Neural Networks  
Abstract: An ap' with key attributes: network, evolutionari, discov, evolut, artifici, standard, neural, play, complex, direct, program, search, develop, game, strategi, seattl, base and is connected with the nodes 129, 163, 191, 1790, 2257 and it is classified as Genetic_Algorithms, it is not the target node. The node 129 is a product titled 'Title: Evolving Networks: Using the Genetic Algorithm with Connectionist Learning  
Abstract: A pilo' with key attributes: network, evolv, connectionist, genet, result and is connected with the nodes 22, 163, 1973, 2446 and it is classified as Genetic_Algorithms, it is not the target node. The node 163 is a product titled 'Title: 4 Implementing Application Specific Routines  Genetic algorithms in search, optimization, and' with key attributes: network, optim, evolutionari, acquisit, modul, artifici, genet, write, submit, concaten, ieee, neural, recurr, search, represent, life, technic, report, construct and is connected with the nodes 22, 129, 191, 563, 982 and it is classified as Genetic_Algorithms, it is not the target node. The node 191 is a product titled 'Title: USING MARKER-BASED GENETIC ENCODING OF NEURAL NETWORKS TO EVOLVE FINITE-STATE BEHAVIOUR  
Abs' with key attributes: encod, network, connect, creatur, evolv, aspect, genet, dna, allow, neural, biolog, mechan, behaviour, propos, node, structur, includ, base and is connected with the nodes 22, 163 and it is classified as Genetic_Algorithms, it is not the target node. The node 247 is a product titled 'Title: Machine Learning,  Efficient Reinforcement Learning through Symbiotic Evolution  
Abstract: T' with key attributes: network, evolv, popul, evolut, articl, genet, reinforc, effici, machin, neural, form, adapt, result, capabl, task, perform, call, neuron, method and is connected with the nodes 500, 563, 982, 1117, 1261, 1973, 2257, 2446 and it is classified as Reinforcement_Learning, it is not the target node. The node 500 is a product titled 'Title: 2-D Pole Balancing with Recurrent Evolutionary Networks  
Abstract: The success of evolutiona' with key attributes: need, network, creat, evolutionari, measur, serv, benchmark, success, effici, classic, standard, recurr, balanc, system, result, recent, task, control, difficult, method and is connected with the nodes 247, 563, 1767, 2444 and it is classified as Reinforcement_Learning, it is not the target node. The node 563 is a product titled 'Title: Evolving Obstacle Avoidance Behavior in a Robot Arm  
Abstract: Existing approaches for learn' with key attributes: exist, avoid, evolv, behavior, reli, declar, obstacl, explicitli, exampl, correct, robot, arm, given, result, control, difficult, hard, supervis, method, howev and is connected with the nodes 163, 247, 500 and it is classified as Reinforcement_Learning, it is not the target node. The node 982 is a product titled 'Title: Evolutionary Neural Networks for Value Ordering in Constraint Satisfaction Problems  
Abstrac' with key attributes: network, cooper, evolutionari, evolv, good, satisfact, valu, order, neural, form, individu, constraint, search, techniqu, develop, strategi, technic, report, call, neuron, method, may and is connected with the nodes 163, 247 and it is classified as Genetic_Algorithms, it is not the target node. The node 1117 is a product titled 'Title: A Coevolutionary Approach to Learning Sequential Decision Rules  
Abstract: We present a coev' with key attributes: independ, evolutionari, advantag, appear, evolv, stabl, rule, altern, simpler, format, complex, decis, sequenti, coevolutionari, direct, provid, result, control, repres and is connected with the nodes 247, 1261 and it is classified as Reinforcement_Learning, it is not the target node. The node 1261 is a product titled 'Title: EVOLVING NEURAL NETWORKS WITH COLLABORATIVE SPECIES  
Abstract: We present a coevolutionary a' with key attributes: network, solv, advantag, evolv, evolut, decompos, artifici, appli, natur, architectur, simpler, neural, speci, coevolutionari, util, techniqu, result, recent, preliminari, work, repres and is connected with the nodes 247, 1117 and it is classified as Reinforcement_Learning, it is not the target node. The node 1767 is a product titled 'Title: Incremental Evolution of Complex General Behavior  
Abstract: Several researchers have demons' with key attributes: network, research, increment, avoid, evolv, turn, evolut, behavior, genet, environ, sequenc, obstacl, specif, neural, complex, action, result, demonstr, gener, howev, sever and is connected with the node 500 and it is classified as Reinforcement_Learning, it is not the target node. The node 1768 is a product titled 'Title: Evolving Neural Networks to Play Go  
Abstract: Go is a difficult game for computers to maste' with key attributes: need, network, best, evolv, averag, comput, neural, tradit, sinc, play, adapt, proven, player, program, techniqu, result, game, difficult, studi, human and is connected with no other nodes and it is classified as Neural_Networks, it is not the target node. The node 1790 is a product titled 'Title: Using Genetic Programming to Evolve Board Evaluation Functions  
Abstract: The purpose of mos' with key attributes: paradigm, function, enabl, evolv, genet, feasibl, comput, play, employ, program, evalu, result, formul, strategi, term and is connected with the node 22 and it is classified as Genetic_Algorithms, it is not the target node. The node 1973 is a product titled 'Title: ON MCMC METHODS IN BAYESIAN REGRESSION ANALYSIS AND MODEL SELECTION  
Abstract: 1] R.K. Belew' with key attributes: network, ed, back, scienc, evolv, connectionist, propag, artifici, genet, complex, train, addison, life, result, studi and is connected with the nodes 129, 247 and it is classified as Genetic_Algorithms, it is not the target node. The node 2257 is a product titled 'Title: Real-time Interactive Neuro-evolution  
Abstract: In standard neuro-evolution, a population o' with key attributes: network, futur, solv, interact, fix, way, best, handl, evolv, popul, instanc, standard, solut, peg, result, task, hard, compar and is connected with the nodes 22, 247 and it is classified as Genetic_Algorithms, it is the target node. The node 2444 is a product titled 'Title: Symbiotic Evolution of Neural Networks in Sequential Decision Tasks  
Abstract: The simple Ba' with key attributes: network, evolut, neural, decis, sequenti, task and is connected with the node 500 and it is classified as Reinforcement_Learning, it is not the target node. The node 2446 is a product titled 'Title: Simulation of Reduced Precision Arithmetic for Digital Neural Networks Using the RAP Machine' with key attributes: network, ed, back, scienc, evolv, connectionist, propag, artifici, genet, complex, train, addison, life, result, studi and is connected with the nodes 129, 247 and it is classified as Genetic_Algorithms, it is not the target node.
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

- ID: 2257
- Title: Real-time Interactive Neuro-evolution
- True class (canonical `y`): **Genetic_Algorithms**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Reinforcement_Learning**
- Prediction recorded by this method's pipeline: **Reinforcement_Learning**

Canonical text (`raw_text`):

~~~~~~text
Title: Real-time Interactive Neuro-evolution  
Abstract: In standard neuro-evolution, a population of networks is evolved in the task, and the network that best solves the task is found. This network is then fixed and used to solve future instances of the problem. Networks evolved in this way do not handle real-time interaction very well. It is hard to evolve a solution ahead of time that can cope effectively with all the possible environments that might arise in the future and with all the possible ways someone may interact with it. This paper proposes evolving feedforward neural networks online to create agents that improve their performance through real-time interaction. This approach is demonstrated in a game world where neural-network-controlled individuals play against humans. Through evolution, these individuals learn to react to varying opponents while appropriately taking into account conflicting goals. After initial evaluation offline, the population is allowed to evolve online, and its performance improves considerably. The population not only adapts to novel situations brought about by changing strategies in the opponent and the game layout, but it also improves its performance in situations that it has already seen in offline training. This paper will describe an implementation of online evolution and shows that it is a practical method that exceeds the performance of offline evolution alone. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 5 nodes

| node id | true class | title |
|---|---|---|
| 22 | Genetic_Algorithms | Discovering Complex Othello Strategies Through Evolutionary Neural Networks |
| 247 | Reinforcement_Learning | Machine Learning,  Efficient Reinforcement Learning through Symbiotic Evolution |
| 1767 | Reinforcement_Learning | Incremental Evolution of Complex General Behavior |
| 1768 | Reinforcement_Learning | Evolving Neural Networks to Play Go |
| 2444 | Reinforcement_Learning | Symbiotic Evolution of Neural Networks in Sequential Decision Tasks |

### 2-hop (shortest distance exactly 2): 11 nodes

| node id | true class | title |
|---|---|---|
| 129 | Genetic_Algorithms | Evolving Networks: Using the Genetic Algorithm with Connectionist Learning |
| 163 | Genetic_Algorithms | 4 Implementing Application Specific Routines  Genetic algorithms in search, optimization, and machine learning. Reading, MA: Addison-Wesley. |
| 191 | Genetic_Algorithms | USING MARKER-BASED GENETIC ENCODING OF NEURAL NETWORKS TO EVOLVE FINITE-STATE BEHAVIOUR |
| 500 | Reinforcement_Learning | 2-D Pole Balancing with Recurrent Evolutionary Networks |
| 563 | Reinforcement_Learning | Evolving Obstacle Avoidance Behavior in a Robot Arm |
| 982 | Genetic_Algorithms | Evolutionary Neural Networks for Value Ordering in Constraint Satisfaction Problems |
| 1117 | Genetic_Algorithms | A Coevolutionary Approach to Learning Sequential Decision Rules |
| 1261 | Genetic_Algorithms | EVOLVING NEURAL NETWORKS WITH COLLABORATIVE SPECIES |
| 1790 | Genetic_Algorithms | Using Genetic Programming to Evolve Board Evaluation Functions |
| 1973 | Genetic_Algorithms | ON MCMC METHODS IN BAYESIAN REGRESSION ANALYSIS AND MODEL SELECTION |
| 2446 | Genetic_Algorithms | Simulation of Reduced Precision Arithmetic for Digital Neural Networks Using the RAP Machine |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/cora/cf-gnnexplainer-canonical/random_seed_42_*` (key=442).

- Factual class: **Reinforcement_Learning**
- Counterfactual class: **Genetic_Algorithms**
- Removed edges (global ids, 3): (1767, 2257), (1768, 2257), (2257, 2444)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 2257 |
| Factual_Target_Node_Neighbors | 22, 247, 1767, 1768, 2444 |
| Factual_Target_Node_Features | network, futur, solv, interact, fix, way, best, handl, evolv, popul, instanc, standard, solut, peg, result, task, hard, compar |
| Counterfactual_Target_Node_Neighbors | 22, 247 |
| Counterfactual_Target_Node_Features | network, futur, solv, interact, fix, way, best, handl, evolv, popul, instanc, standard, solut, peg, result, task, hard, compar |
| Factual_Target_Node_Class | Reinforcement_Learning |
| Counterfactual_Target_Node_class | Genetic_Algorithms |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 1767, 1768, 2444 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 2257 |
| Factual_Target_Node_Neighbors | 22, 247, 1767, 1768, 2444 |
| Factual_Target_Node_Features | network, futur, solv, interact, fix, way, best, handl, evolv, popul, instanc, standard, solut, peg, result, task, hard, compar |
| Counterfactual_Target_Node_Neighbors | 22, 247 |
| Counterfactual_Target_Node_Features | network, futur, solv, interact, fix, way, best, handl, evolv, popul, instanc, standard, solut, peg, result, task, hard, compar |
| Factual_Target_Node_Class | Reinforcement_Learning |
| Counterfactual_Target_Node_class | Genetic_Algorithms |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 1767, 1768, 2444 |
| Natural_Language_Explanation | None |
