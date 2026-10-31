# Reference packet: CF-GNNExplainer__Llama-70B__cora__1959

- Method: CF-GNNExplainer; configuration: Llama-70B; dataset: cora; target node: 1959
- Explanation source: `./robustness_2026-10-30/llama70b/cf/cora/1959.json` (response)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, the dictionary can be filled as follows:

infos = {
    'Target_Node_ID': 1959,
    'Factual_Target_Node_Neighbors': [177],
    'Factual_Target_Node_Features': ['facilit', 'face', 'advantag', 'second', 'random', 'behavior', 'hierarch', 'set', 'comprehens', 'implicit', 'induct', 'polici', 'modular', 'discoveri', 'procedur', 'represent', 'result', 'task', 'control', 'larg', 'compar', 'situat', 'gener', 'potenti', 'sever'],
    'Counterfactual_Target_Node_Neighbors': [120, 163, 177, 2175, 2259],
    'Counterfactual_Target_Node_Features': ['facilit', 'face', 'advantag', 'second', 'random', 'behavior', 'hierarch', 'set', 'comprehens', 'implicit', 'induct', 'polici', 'modular', 'discoveri', 'procedur', 'represent', 'result', 'task', 'control', 'larg', 'compar', 'situat', 'gener', 'potenti', 'sever'],
    'Factual_Target_Node_Class': 'Theory',
    'Counterfactual_Target_Node_class': 'Genetic_Algorithms',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Natural_Language_Explanation': 'The target node 1959 was initially classified as Theory but changed to Genetic_Algorithms due to the influence of its neighbors. The node 177, which was the only neighbor in the factual graph, is not sufficient to classify the node as Genetic_Algorithms. However, with the addition of new neighbors 120, 163, 2175, and 2259 in the counterfactual graph, the node is now classified as Genetic_Algorithms. These new neighbors are all related to genetic algorithms and programming, which likely influenced the change in classification.',
    'Node_Differences': [1959],
    'Edge_Differences': [(1959, 120), (1959, 163), (1959, 2175), (1959, 2259)]
}

Explanation:
The target node 1959 was initially classified as Theory but changed to Genetic_Algorithms due to the influence of its neighbors. The node 177, which was the only neighbor in the factual graph, is not sufficient to classify the node as Genetic_Algorithms. However, with the addition of new neighbors 120, 163, 2175, and 2259 in the counterfactual graph, the node is now classified as Genetic_Algorithms. These new neighbors are all related to genetic algorithms and programming, which likely influenced the change in classification.

In particular, node 120 is a paper about genetic programming, node 163 is a paper about implementing application-specific routines using genetic algorithms, node 2175 is a paper about the building block hypothesis for genetic programming, and node 2259 is a paper about schema creation, propagation, and disruption in genetic programming. The presence of these nodes as neighbors in the counterfactual graph likely contributed to the reclassification of node 1959 as Genetic_Algorithms.
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
given the factual graph: The node 120 is a product titled 'Title: Genetic Programming Exploratory Power and the Discovery of Functions  
Abstract: Hierarchical' with key attributes: explan, function, exploratori, evolut, modif, behavior, qualit, reli, genet, perspect, divers, hierarch, power, analysi, dual, discoveri, acceler, process, provid, program, result, improv, base and is connected with the nodes 188, 1184, 1959, 2175 and it is classified as Genetic_Algorithms, it is not the target node. The node 163 is a product titled 'Title: 4 Implementing Application Specific Routines  Genetic algorithms in search, optimization, and' with key attributes: network, optim, evolutionari, acquisit, modul, artifici, genet, write, submit, concaten, ieee, neural, recurr, search, represent, life, technic, report, construct and is connected with the nodes 188, 1257, 2175, 2259 and it is classified as Genetic_Algorithms, it is not the target node. The node 177 is a product titled 'Title: Evaluation and Selection of Biases in Machine Learning  
Abstract: In this introduction, we d' with key attributes: research, defin, introduct, motiv, space, autom, import, machin, bias, bia, system, evalu, search, result, term, framework, field, select, method and is connected with the nodes 430, 635, 885, 911, 965, 1489, 1959, 2192 and it is classified as Theory, it is not the target node. The node 188 is a product titled 'Title: Coevolving High-Level Representations  
Abstract: Rules extracted from trained feedforward ne' with key attributes: write, represent and is connected with the nodes 120, 163 and it is classified as Genetic_Algorithms, it is not the target node. The node 430 is a product titled 'Title: Irrelevant Features and the Subset Selection Problem  
Abstract: We address the problem of fi' with key attributes: literatur, address, induc, genet, notion, allow, featur, machin, induct, categori, subset, adequ, relev, examin, definit, result, irrelev, small, concept, select, partit, supervis and is connected with the nodes 177, 635 and it is classified as Theory, it is not the target node. The node 635 is a product titled 'Title: Learning Boolean Concepts in the Presence of Many Irrelevant Features  
Abstract: In this pap' with key attributes: defin, domain, implement, hypothes, possibl, genet, featur, read, induct, appropri, bia, shown, mani, requir, result, prefer, consist, irrelev, studi and is connected with the nodes 177, 430 and it is classified as Theory, it is not the target node. The node 885 is a product titled 'Title: Model selection using measure functions  
Abstract: The concept of measure functions for gene' with key attributes: captur, domain, function, measur, way, state, addit, possibl, altern, comput, classifi, prior, provid, evalu, result, suggest, model, perform, gener, concept, known, select and is connected with the node 177 and it is classified as Theory, it is not the target node. The node 911 is a product titled 'Title: Utilizing Prior Concepts for Learning  
Abstract: The inductive learning problem consists of' with key attributes: previous, genet, exampl, discuss, induct, bias, util, bia, prior, result, given, task, consist, perform, concept, method and is connected with the node 177 and it is classified as Theory, it is not the target node. The node 965 is a product titled 'Title: Improving Tactical Plans with Genetic Algorithms  
Abstract:' with key attributes: genet, plan, improv and is connected with the node 177 and it is classified as Theory, it is not the target node. The node 1184 is a product titled 'Title: Causality in Genetic Programming  
Abstract: Causality relates changes in the structure of an' with key attributes: paradigm, aim, prove, implement, acquisit, interact, way, genet, environ, trace, read, machin, intern, soft, adapt, extern, program, represent, signific, result, work, experi, base, knowledg, analyz and is connected with the node 120 and it is classified as Genetic_Algorithms, it is not the target node. The node 1257 is a product titled 'Title: The Schema Theorem and Price's Theorem  
Abstract: Holland's Schema Theorem is widely taken t' with key attributes: taken, explan, express, review, explain, implic, schema, genet, power, theorem, argument, interpret, recent, wide, perform, foundat and is connected with the nodes 163, 2175, 2259 and it is classified as Genetic_Algorithms, it is not the target node. The node 1489 is a product titled 'Title: Dlab: A Declarative Language Bias Formalism  
Abstract: We describe the principles and functi' with key attributes: defin, function, formal, rule, declar, principl, formula, subspac, order, effici, set, induct, finit, logic, bia, system, languag, describ, proposit, syntact, result, associ and is connected with the node 177 and it is classified as Theory, it is not the target node. The node 1959 is a product titled 'Title: Evolution-based Discovery of Hierarchical Behaviors  
Abstract: Procedural representations of' with key attributes: facilit, face, advantag, second, random, behavior, hierarch, set, comprehens, implicit, induct, polici, modular, discoveri, procedur, represent, result, task, control, larg, compar, situat, gener, potenti, sever and is connected with the nodes 120, 177, 2259 and it is classified as Genetic_Algorithms, it is the target node. The node 2175 is a product titled 'Title: The Troubling Aspects of a Building Block Hypothesis for Genetic Programming  
Abstract: In t' with key attributes: research, length, similar, hypothesi, aspect, schema, genet, natur, account, variabl, theorem, build, interpret, program, manner, represent, result, formul, block, definit, earli and is connected with the nodes 120, 163, 1257, 2259 and it is classified as Genetic_Algorithms, it is not the target node. The node 2192 is a product titled 'Title: #1 Robust Feature Selection Algorithms  
Abstract: Selecting a set of features which is optim' with key attributes: involv, rule, genet, data, classif, explor, featur, machin, size, tradit, induct, complex, real, system, describ, techniqu, result, improv, world, gener, select, tool and is connected with the node 177 and it is classified as Theory, it is not the target node. The node 2259 is a product titled 'Title: An Experimental Analysis of Schema Creation, Propagation and Disruption in Genetic Programmin' with key attributes: review, creation, propag, schema, genet, analysi, form, main, real, program, result, definit, experiment, studi, theori, base and is connected with the nodes 163, 1257, 1959, 2175, 2261, 2271 and it is classified as Genetic_Algorithms, it is not the target node. The node 2261 is a product titled 'Title: Genetic Programming with One-Point Crossover and Point Mutation  
Abstract: Technical Report:' with key attributes: review, point, origin, schema, genet, simpler, strength, main, mutat, weak, theorem, crossov, program, propos, result, obtain, definit, concept, theori and is connected with the node 2259 and it is classified as Genetic_Algorithms, it is not the target node. The node 2271 is a product titled 'Title: How Fitness Structure Affects Subsolution Acquisition in Genetic Programming  
Abstract: We d' with key attributes: map, defin, fit, independ, affect, acquisit, valu, genet, respect, relat, variou, rate, program, structur, result and is connected with the node 2259 and it is classified as Genetic_Algorithms, it is not the target node. and given the counterfactual example: The node 120 is a product titled 'Title: Genetic Programming Exploratory Power and the Discovery of Functions  
Abstract: Hierarchical' with key attributes: explan, function, exploratori, evolut, modif, behavior, qualit, reli, genet, perspect, divers, hierarch, power, analysi, dual, discoveri, acceler, process, provid, program, result, improv, base and is connected with the nodes 188, 1184, 2175 and it is classified as Genetic_Algorithms, it is not the target node. The node 163 is a product titled 'Title: 4 Implementing Application Specific Routines  Genetic algorithms in search, optimization, and' with key attributes: network, optim, evolutionari, acquisit, modul, artifici, genet, write, submit, concaten, ieee, neural, recurr, search, represent, life, technic, report, construct and is connected with the nodes 188, 1257, 2175, 2259 and it is classified as Genetic_Algorithms, it is not the target node. The node 177 is a product titled 'Title: Evaluation and Selection of Biases in Machine Learning  
Abstract: In this introduction, we d' with key attributes: research, defin, introduct, motiv, space, autom, import, machin, bias, bia, system, evalu, search, result, term, framework, field, select, method and is connected with the nodes 430, 635, 885, 911, 965, 1489, 1959, 2192 and it is classified as Theory, it is not the target node. The node 188 is a product titled 'Title: Coevolving High-Level Representations  
Abstract: Rules extracted from trained feedforward ne' with key attributes: write, represent and is connected with the nodes 120, 163 and it is classified as Genetic_Algorithms, it is not the target node. The node 430 is a product titled 'Title: Irrelevant Features and the Subset Selection Problem  
Abstract: We address the problem of fi' with key attributes: literatur, address, induc, genet, notion, allow, featur, machin, induct, categori, subset, adequ, relev, examin, definit, result, irrelev, small, concept, select, partit, supervis and is connected with the nodes 177, 635 and it is classified as Theory, it is not the target node. The node 635 is a product titled 'Title: Learning Boolean Concepts in the Presence of Many Irrelevant Features  
Abstract: In this pap' with key attributes: defin, domain, implement, hypothes, possibl, genet, featur, read, induct, appropri, bia, shown, mani, requir, result, prefer, consist, irrelev, studi and is connected with the nodes 177, 430 and it is classified as Theory, it is not the target node. The node 885 is a product titled 'Title: Model selection using measure functions  
Abstract: The concept of measure functions for gene' with key attributes: captur, domain, function, measur, way, state, addit, possibl, altern, comput, classifi, prior, provid, evalu, result, suggest, model, perform, gener, concept, known, select and is connected with the node 177 and it is classified as Theory, it is not the target node. The node 911 is a product titled 'Title: Utilizing Prior Concepts for Learning  
Abstract: The inductive learning problem consists of' with key attributes: previous, genet, exampl, discuss, induct, bias, util, bia, prior, result, given, task, consist, perform, concept, method and is connected with the node 177 and it is classified as Theory, it is not the target node. The node 965 is a product titled 'Title: Improving Tactical Plans with Genetic Algorithms  
Abstract:' with key attributes: genet, plan, improv and is connected with the node 177 and it is classified as Theory, it is not the target node. The node 1184 is a product titled 'Title: Causality in Genetic Programming  
Abstract: Causality relates changes in the structure of an' with key attributes: paradigm, aim, prove, implement, acquisit, interact, way, genet, environ, trace, read, machin, intern, soft, adapt, extern, program, represent, signific, result, work, experi, base, knowledg, analyz and is connected with the node 120 and it is classified as Genetic_Algorithms, it is not the target node. The node 1257 is a product titled 'Title: The Schema Theorem and Price's Theorem  
Abstract: Holland's Schema Theorem is widely taken t' with key attributes: taken, explan, express, review, explain, implic, schema, genet, power, theorem, argument, interpret, recent, wide, perform, foundat and is connected with the nodes 163, 2175, 2259 and it is classified as Genetic_Algorithms, it is not the target node. The node 1489 is a product titled 'Title: Dlab: A Declarative Language Bias Formalism  
Abstract: We describe the principles and functi' with key attributes: defin, function, formal, rule, declar, principl, formula, subspac, order, effici, set, induct, finit, logic, bia, system, languag, describ, proposit, syntact, result, associ and is connected with the node 177 and it is classified as Theory, it is not the target node. The node 1959 is a product titled 'Title: Evolution-based Discovery of Hierarchical Behaviors  
Abstract: Procedural representations of' with key attributes: facilit, face, advantag, second, random, behavior, hierarch, set, comprehens, implicit, induct, polici, modular, discoveri, procedur, represent, result, task, control, larg, compar, situat, gener, potenti, sever and is connected with the node 177 and it is classified as Theory, it is the target node. The node 2175 is a product titled 'Title: The Troubling Aspects of a Building Block Hypothesis for Genetic Programming  
Abstract: In t' with key attributes: research, length, similar, hypothesi, aspect, schema, genet, natur, account, variabl, theorem, build, interpret, program, manner, represent, result, formul, block, definit, earli and is connected with the nodes 120, 163, 1257, 2259 and it is classified as Genetic_Algorithms, it is not the target node. The node 2192 is a product titled 'Title: #1 Robust Feature Selection Algorithms  
Abstract: Selecting a set of features which is optim' with key attributes: involv, rule, genet, data, classif, explor, featur, machin, size, tradit, induct, complex, real, system, describ, techniqu, result, improv, world, gener, select, tool and is connected with the node 177 and it is classified as Theory, it is not the target node. The node 2259 is a product titled 'Title: An Experimental Analysis of Schema Creation, Propagation and Disruption in Genetic Programmin' with key attributes: review, creation, propag, schema, genet, analysi, form, main, real, program, result, definit, experiment, studi, theori, base and is connected with the nodes 163, 1257, 2175, 2261, 2271 and it is classified as Genetic_Algorithms, it is not the target node. The node 2261 is a product titled 'Title: Genetic Programming with One-Point Crossover and Point Mutation  
Abstract: Technical Report:' with key attributes: review, point, origin, schema, genet, simpler, strength, main, mutat, weak, theorem, crossov, program, propos, result, obtain, definit, concept, theori and is connected with the node 2259 and it is classified as Genetic_Algorithms, it is not the target node. The node 2271 is a product titled 'Title: How Fitness Structure Affects Subsolution Acquisition in Genetic Programming  
Abstract: We d' with key attributes: map, defin, fit, independ, affect, acquisit, valu, genet, respect, relat, variou, rate, program, structur, result and is connected with the node 2259 and it is classified as Genetic_Algorithms, it is not the target node.
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

- ID: 1959
- Title: Evolution-based Discovery of Hierarchical Behaviors
- True class (canonical `y`): **Genetic_Algorithms**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Genetic_Algorithms**
- Prediction recorded by this method's pipeline: **Genetic_Algorithms**

Canonical text (`raw_text`):

~~~~~~text
Title: Evolution-based Discovery of Hierarchical Behaviors  
Abstract: Procedural representations of control policies have two advantages when facing the scale-up problem in learning tasks. First they are implicit, with potential for inductive generalization over a very large set of situations. Second they facilitate modularization. In this paper we compare several randomized algorithms for learning modular procedural representations. The main algorithm, called Adaptive Representation through Learning (ARL) is a genetic programming extension that relies on the discovery of subroutines. ARL is suitable for learning hierarchies of subroutines and for constructing policies to complex tasks. ARL was successfully tested on a typical reinforcement learning problem of controlling an agent in a dynamic and nondeterministic environment where the discovered subroutines correspond to agent behaviors. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 3 nodes

| node id | true class | title |
|---|---|---|
| 120 | Genetic_Algorithms | Genetic Programming Exploratory Power and the Discovery of Functions |
| 177 | Theory | Evaluation and Selection of Biases in Machine Learning |
| 2259 | Genetic_Algorithms | An Experimental Analysis of Schema Creation, Propagation and Disruption in Genetic Programming |

### 2-hop (shortest distance exactly 2): 14 nodes

| node id | true class | title |
|---|---|---|
| 163 | Genetic_Algorithms | 4 Implementing Application Specific Routines  Genetic algorithms in search, optimization, and machine learning. Reading, MA: Addison-Wesley. |
| 188 | Genetic_Algorithms | Coevolving High-Level Representations |
| 430 | Theory | Irrelevant Features and the Subset Selection Problem |
| 635 | Theory | Learning Boolean Concepts in the Presence of Many Irrelevant Features |
| 885 | Theory | Model selection using measure functions |
| 911 | Theory | Utilizing Prior Concepts for Learning |
| 965 | Genetic_Algorithms | Improving Tactical Plans with Genetic Algorithms |
| 1184 | Genetic_Algorithms | Causality in Genetic Programming |
| 1257 | Genetic_Algorithms | The Schema Theorem and Price's Theorem |
| 1489 | Rule_Learning | Dlab: A Declarative Language Bias Formalism |
| 2175 | Genetic_Algorithms | The Troubling Aspects of a Building Block Hypothesis for Genetic Programming |
| 2192 | Genetic_Algorithms | #1 Robust Feature Selection Algorithms |
| 2261 | Genetic_Algorithms | Genetic Programming with One-Point Crossover and Point Mutation |
| 2271 | Genetic_Algorithms | How Fitness Structure Affects Subsolution Acquisition in Genetic Programming |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/cora/cf-gnnexplainer-canonical/random_seed_42_*` (key=390).

- Factual class: **Genetic_Algorithms**
- Counterfactual class: **Theory**
- Removed edges (global ids, 2): (120, 1959), (1959, 2259)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 1959 |
| Factual_Target_Node_Neighbors | 120, 177, 2259 |
| Factual_Target_Node_Features | facilit, face, advantag, second, random, behavior, hierarch, set, comprehens, implicit, induct, polici, modular, discoveri, procedur, represent, result, task, result, control, larg, compar, situat, gener, compar, potenti, sever |
| Counterfactual_Target_Node_Neighbors | 177 |
| Counterfactual_Target_Node_Features | facilit, face, advantag, second, random, behavior, hierarch, set, comprehens, implicit, induct, polici, modular, discoveri, procedur, represent, result, task, result, control, larg, compar, situat, gener, compar, potenti, sever |
| Factual_Target_Node_Class | Genetic_Algorithms |
| Counterfactual_Target_Node_class | Theory |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 120, 2259 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 1959 |
| Factual_Target_Node_Neighbors | 120, 177, 2259 |
| Factual_Target_Node_Features | facilit, face, advantag, second, random, behavior, hierarch, set, comprehens, implicit, induct, polici, modular, discoveri, procedur, represent, result, task, result, control, larg, compar, situat, gener, compar, potenti, sever |
| Counterfactual_Target_Node_Neighbors | 177 |
| Counterfactual_Target_Node_Features | facilit, face, advantag, second, random, behavior, hierarch, set, comprehens, implicit, induct, polici, modular, discoveri, procedur, represent, result, task, result, control, larg, compar, situat, gener, compar, potenti, sever |
| Factual_Target_Node_Class | Genetic_Algorithms |
| Counterfactual_Target_Node_class | Theory |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 120, 2259 |
| Natural_Language_Explanation | None |
