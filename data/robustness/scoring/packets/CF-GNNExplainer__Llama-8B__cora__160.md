# Reference packet: CF-GNNExplainer__Llama-8B__cora__160

- Method: CF-GNNExplainer; configuration: Llama-8B; dataset: cora; target node: 160
- Explanation source: `./llm-graph-cf/data/results/cf-gnnexplainer-canonical_Meta-Llama-3.1-8B-Instruct_cora_standard_Response.json` ([29][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, we will generate the dictionary for the counterfactual explanation.

The target node is 160, which is classified as Theory. We need to find the differences between the factual and counterfactual graphs to explain why the classification changed.

First, let's identify the nodes and edges that were added or removed in the counterfactual graph. By comparing the factual and counterfactual graphs, we can see that the only difference is in the connections between nodes 160 and 157.

In the factual graph, node 157 is connected to nodes 78, 214, and 2540. However, in the counterfactual graph, node 157 is connected to nodes 125, 394, 1857, and 2020.

The Node_Differences dictionary should contain the nodes where the change occurred:

Node_Differences = {'160'}

The Edge_Differences dictionary should contain the edges that were added or removed:

Edge_Differences = [(157, 125), (157, 394), (157, 1857), (157, 2020)]

Now, let's analyze the influence of the neighboring nodes on the target node 160.

In the factual graph, the neighbors of node 160 are nodes 125, 322, 469, 2540, 2681. These nodes are all classified as Theory, except for node 125, which is classified as Probabilistic_Methods.

In the counterfactual graph, the neighbors of node 160 are nodes 125, 322, 469, 2540. The only difference is that node 2681 was removed.

The Factual_Target_Node_Neighbors dictionary should contain the neighbors of the target node in the factual graph:

Factual_Target_Node_Neighbors = [125, 322, 469, 2540, 2681]

The Counterfactual_Target_Node_Neighbors dictionary should contain the neighbors of the target node in the counterfactual graph:

Counterfactual_Target_Node_Neighbors = [125, 322, 469, 2540]

The Factual_Target_Node_Features dictionary should contain the features of the target node in the factual graph:

Factual_Target_Node_Features = ['network', 'gaussian', 'organis', 'regress', 'process', 'evalu', 'method']

The Counterfactual_Target_Node_Features dictionary should contain the features of the target node in the counterfactual graph:

Counterfactual_Target_Node_Features = ['network', 'gaussian', 'organis', 'regress', 'process', 'evalu', 'method']

The Target_Node_Features_Changed_From_Factual_To_Counterfactual dictionary should be empty since there are no changes in the features of the target node.

The Natural_Language_Explanation dictionary should contain a natural language explanation for the change in classification:

Natural_Language_Explanation = "The change in classification for node 160 from Theory to Theory is due to the removal of node 2681 from its neighborhood, which had a significant impact on the target node's features and connections."

Here is the completed dictionary:

infos={
'Target_Node_ID': 160,
Factual_Target_Node_Neighbors: [125, 322, 469, 2540, 2681],
Factual_Target_Node_Features: ['network', 'gaussian', 'organis', 'regress', 'process', 'evalu', 'method'],
Counterfactual_Target_Node_Neighbors: [125, 322, 469, 2540],
Counterfactual_Target_Node_Features: ['network', 'gaussian', 'organis', 'regress', 'process', 'evalu', 'method'],
Target_Node_Features_Changed_From_Factual_To_Counterfactual: {},
Natural_Language_Explanation: "The change in classification for node 160 from Theory to Theory is due to the removal of node 2681 from its neighborhood, which had a significant impact on the target node's features and connections."}
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
Abstract: This paper explores the effec' with key attributes: network, back, condit, simpl, vector, function, space, initi, weight, propag, sensit, explor, feed, techniqu, result, effect, signific, demonstr, compar, select, carlo and is connected with the node 322 and it is classified as Theory, it is not the target node. The node 78 is a product titled 'Title: Probabilistic Networks: New Models and New Methods  
Abstract: In this paper I describe the i' with key attributes: network, implement, gibb, carri, possibl, environ, simul, statist, surprisingli, complex, regress, sampl, describ, program, techniqu, probabilist, result, infer, model, bayesian, known, method and is connected with the nodes 157, 214, 469, 2681 and it is classified as Theory, it is not the target node. The node 125 is a product titled 'Title: Gaussian Processes for Bayesian Classification via Hybrid Monte Carlo  
Abstract: The full Ba' with key attributes: network, predict, gaussian, necessari, appli, full, integr, classif, markov, mcmc, set, neural, chain, process, tractabl, structur, analyt, bayesian, perform, method, howev, carlo, hybrid and is connected with the nodes 160, 394, 1857 and it is classified as Probabilistic_Methods, it is not the target node. The node 157 is a product titled 'Title: A Practical Bayesian Framework for Backprop Networks  
Abstract: A quantitative and practical' with key attributes: network, practic, map, quantit, rule, prune, possibl, altern, object, feedforward, comparison, choic, solut, describ, grow, bayesian, result, framework and is connected with the nodes 78, 214, 2540 and it is classified as Theory, it is not the target node. The node 160 is a product titled 'Title: EVALUATION OF GAUSSIAN PROCESSES AND OTHER METHODS FOR NON-LINEAR REGRESSION  
Abstract: The' with key attributes: gaussian, organis, regress, process, evalu, method and is connected with the nodes 125, 322, 469, 1857, 2540, 2681 and it is classified as Neural_Networks, it is the target node. The node 214 is a product titled 'Title: Bayesian Non-linear Modelling for the Prediction Competition  
Abstract: The 1993 energy pred' with key attributes: involv, predict, load, environment, organis, popular, input, energi, competit, variabl, sinc, regress, build, techniqu, model, bayesian, task, larg, seri and is connected with the nodes 78, 157, 469 and it is classified as Neural_Networks, it is not the target node. The node 322 is a product titled 'Title: Statistical Tests for Comparing Supervised Classification Learning Algorithms  
Abstract: Thi' with key attributes: review, exist, approxim, probabl, genet, detect, classif, statist, particular, determin, anoth, type, error, result, task, experiment, compar, differ, supervis and is connected with the nodes 15, 160, 967, 1027, 1644, 2508 and it is classified as Theory, it is not the target node. The node 394 is a product titled 'Title: Prior Information and Generalized Questions  
Abstract: This report describes research done w' with key attributes: inform, research, question, scienc, cognit, postdoctor, aaai, comput, technolog, center, brain, biolog, depart, prior, describ, result, grant, report, done, gener, foundat and is connected with the node 125 and it is classified as Probabilistic_Methods, it is not the target node. The node 469 is a product titled 'Title: Interpolation Models with Multiple  
Abstract: A traditional interpolation model is character' with key attributes: paramet, alon, nois, appli, ratio, interpol, typic, respons, tradit, character, constant, choic, regular, singl, multipl, model, recent and is connected with the nodes 78, 160, 214 and it is classified as Theory, it is not the target node. The node 611 is a product titled 'Title: Learning networks for face analysis and synthesis  
Abstract: This paper presents an overview' with key attributes: network, face, descript, synthesi, group, overview, imag, underli, detect, project, analysi, exampl, unifi, label, result, work, method, analyz and is connected with the node 2540 and it is classified as Neural_Networks, it is not the target node. The node 967 is a product titled 'Title: Rigorous Learning Curve Bounds from Statistical Mechanics  
Abstract: In this paper we introd' with key attributes: chervonenki, consider, reflect, advantag, curv, statist, case, bound, idea, investig, true, mechan, mathemat, mani, result, introduc, theori, base and is connected with the node 322 and it is classified as Theory, it is not the target node. The node 1027 is a product titled 'Title: Pessimistic decision tree pruning based on tree size  
Abstract: In this work we develop a ne' with key attributes: chervonenki, motiv, tree, dimens, sound, prune, converg, size, decis, criteria, uniform, develop, result, work, perform, compar, theoret, concept, theori, base, method and is connected with the node 322 and it is classified as Theory, it is not the target node. The node 1644 is a product titled 'Title: A Comparative Study of ID3 and Backpropagation for English Text-to-Speech Mapping  
Abstract:' with key attributes: rosenberg, map, code, genet, distribut, comparison, output, backpropag, prop, shown, error, develop, task, result, seattl, consist, perform, compar, stress and is connected with the node 322 and it is classified as Neural_Networks, it is not the target node. The node 1857 is a product titled 'Title: Monte Carlo Implementation of Gaussian Process Models for Bayesian Regression and Classificat' with key attributes: simpl, defin, gaussian, implement, function, way, natur, classif, distribut, statist, nonparametr, input, variabl, regress, depart, process, prior, model, technic, report, bayesian, carlo, univers and is connected with the nodes 125, 160, 2020, 2540, 2681 and it is classified as Probabilistic_Methods, it is not the target node. The node 2020 is a product titled 'Title: Variational Gaussian Process Classifiers  
Abstract:' with key attributes: gaussian, variat, classifi, process and is connected with the node 1857 and it is classified as Neural_Networks, it is not the target node. The node 2508 is a product titled 'Title: WRAPPERS FOR PERFORMANCE ENHANCEMENT AND OBLIVIOUS DECISION GRAPHS  
Abstract: This paper int' with key attributes: enhanc, graph, decis, perform and is connected with the node 322 and it is classified as Theory, it is not the target node. The node 2540 is a product titled 'Title: Efficient Implementation of Gaussian Processes  
Abstract: Neural networks and Bayesian infer' with key attributes: parameter, network, gaussian, implement, solv, allow, mean, effici, analysi, neural, regress, investig, process, prior, provid, result, infer, bayesian, exact, difficult, framework, method, howev and is connected with the nodes 157, 160, 611, 1857 and it is classified as Neural_Networks, it is not the target node. The node 2681 is a product titled 'Title: Regression with Input-dependent Noise: A Gaussian Process Treatment  
Abstract: Technical Rep' with key attributes: inform, ed, avail, gaussian, besov, appear, nois, natur, distribut, neural, regress, advanc, treatment, process, system, prior, provid, technic, report and is connected with the nodes 78, 160, 1857 and it is classified as Neural_Networks, it is not the target node. and given the counterfactual example: The node 15 is a product titled 'Title: Back Propagation is Sensitive to Initial Conditions  
Abstract: This paper explores the effec' with key attributes: network, back, condit, simpl, vector, function, space, initi, weight, propag, sensit, explor, feed, techniqu, result, effect, signific, demonstr, compar, select, carlo and is connected with the node 322 and it is classified as Theory, it is not the target node. The node 78 is a product titled 'Title: Probabilistic Networks: New Models and New Methods  
Abstract: In this paper I describe the i' with key attributes: network, implement, gibb, carri, possibl, environ, simul, statist, surprisingli, complex, regress, sampl, describ, program, techniqu, probabilist, result, infer, model, bayesian, known, method and is connected with the nodes 157, 214, 469, 2681 and it is classified as Theory, it is not the target node. The node 125 is a product titled 'Title: Gaussian Processes for Bayesian Classification via Hybrid Monte Carlo  
Abstract: The full Ba' with key attributes: network, predict, gaussian, necessari, appli, full, integr, classif, markov, mcmc, set, neural, chain, process, tractabl, structur, analyt, bayesian, perform, method, howev, carlo, hybrid and is connected with the nodes 160, 394, 1857 and it is classified as Probabilistic_Methods, it is not the target node. The node 157 is a product titled 'Title: A Practical Bayesian Framework for Backprop Networks  
Abstract: A quantitative and practical' with key attributes: network, practic, map, quantit, rule, prune, possibl, altern, object, feedforward, comparison, choic, solut, describ, grow, bayesian, result, framework and is connected with the nodes 78, 214, 2540 and it is classified as Theory, it is not the target node. The node 160 is a product titled 'Title: EVALUATION OF GAUSSIAN PROCESSES AND OTHER METHODS FOR NON-LINEAR REGRESSION  
Abstract: The' with key attributes: gaussian, organis, regress, process, evalu, method and is connected with the nodes 125, 322, 469, 2540 and it is classified as Theory, it is the target node. The node 214 is a product titled 'Title: Bayesian Non-linear Modelling for the Prediction Competition  
Abstract: The 1993 energy pred' with key attributes: involv, predict, load, environment, organis, popular, input, energi, competit, variabl, sinc, regress, build, techniqu, model, bayesian, task, larg, seri and is connected with the nodes 78, 157, 469 and it is classified as Neural_Networks, it is not the target node. The node 322 is a product titled 'Title: Statistical Tests for Comparing Supervised Classification Learning Algorithms  
Abstract: Thi' with key attributes: review, exist, approxim, probabl, genet, detect, classif, statist, particular, determin, anoth, type, error, result, task, experiment, compar, differ, supervis and is connected with the nodes 15, 160, 967, 1027, 1644, 2508 and it is classified as Theory, it is not the target node. The node 394 is a product titled 'Title: Prior Information and Generalized Questions  
Abstract: This report describes research done w' with key attributes: inform, research, question, scienc, cognit, postdoctor, aaai, comput, technolog, center, brain, biolog, depart, prior, describ, result, grant, report, done, gener, foundat and is connected with the node 125 and it is classified as Probabilistic_Methods, it is not the target node. The node 469 is a product titled 'Title: Interpolation Models with Multiple  
Abstract: A traditional interpolation model is character' with key attributes: paramet, alon, nois, appli, ratio, interpol, typic, respons, tradit, character, constant, choic, regular, singl, multipl, model, recent and is connected with the nodes 78, 160, 214 and it is classified as Theory, it is not the target node. The node 611 is a product titled 'Title: Learning networks for face analysis and synthesis  
Abstract: This paper presents an overview' with key attributes: network, face, descript, synthesi, group, overview, imag, underli, detect, project, analysi, exampl, unifi, label, result, work, method, analyz and is connected with no other nodes and it is classified as Neural_Networks, it is not the target node. The node 967 is a product titled 'Title: Rigorous Learning Curve Bounds from Statistical Mechanics  
Abstract: In this paper we introd' with key attributes: chervonenki, consider, reflect, advantag, curv, statist, case, bound, idea, investig, true, mechan, mathemat, mani, result, introduc, theori, base and is connected with the node 322 and it is classified as Theory, it is not the target node. The node 1027 is a product titled 'Title: Pessimistic decision tree pruning based on tree size  
Abstract: In this work we develop a ne' with key attributes: chervonenki, motiv, tree, dimens, sound, prune, converg, size, decis, criteria, uniform, develop, result, work, perform, compar, theoret, concept, theori, base, method and is connected with the node 322 and it is classified as Theory, it is not the target node. The node 1644 is a product titled 'Title: A Comparative Study of ID3 and Backpropagation for English Text-to-Speech Mapping  
Abstract:' with key attributes: rosenberg, map, code, genet, distribut, comparison, output, backpropag, prop, shown, error, develop, task, result, seattl, consist, perform, compar, stress and is connected with the node 322 and it is classified as Neural_Networks, it is not the target node. The node 1857 is a product titled 'Title: Monte Carlo Implementation of Gaussian Process Models for Bayesian Regression and Classificat' with key attributes: simpl, defin, gaussian, implement, function, way, natur, classif, distribut, statist, nonparametr, input, variabl, regress, depart, process, prior, model, technic, report, bayesian, carlo, univers and is connected with the nodes 125, 2020, 2681 and it is classified as Probabilistic_Methods, it is not the target node. The node 2020 is a product titled 'Title: Variational Gaussian Process Classifiers  
Abstract:' with key attributes: gaussian, variat, classifi, process and is connected with the node 1857 and it is classified as Neural_Networks, it is not the target node. The node 2508 is a product titled 'Title: WRAPPERS FOR PERFORMANCE ENHANCEMENT AND OBLIVIOUS DECISION GRAPHS  
Abstract: This paper int' with key attributes: enhanc, graph, decis, perform and is connected with the node 322 and it is classified as Theory, it is not the target node. The node 2540 is a product titled 'Title: Efficient Implementation of Gaussian Processes  
Abstract: Neural networks and Bayesian infer' with key attributes: parameter, network, gaussian, implement, solv, allow, mean, effici, analysi, neural, regress, investig, process, prior, provid, result, infer, bayesian, exact, difficult, framework, method, howev and is connected with the nodes 157, 160 and it is classified as Neural_Networks, it is not the target node. The node 2681 is a product titled 'Title: Regression with Input-dependent Noise: A Gaussian Process Treatment  
Abstract: Technical Rep' with key attributes: inform, ed, avail, gaussian, besov, appear, nois, natur, distribut, neural, regress, advanc, treatment, process, system, prior, provid, technic, report and is connected with the nodes 78, 1857 and it is classified as Neural_Networks, it is not the target node.
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

- ID: 160
- Title: EVALUATION OF GAUSSIAN PROCESSES AND OTHER METHODS FOR NON-LINEAR REGRESSION
- True class (canonical `y`): **Neural_Networks**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Neural_Networks**
- Prediction recorded by this method's pipeline: **Neural_Networks**

Canonical text (`raw_text`):

~~~~~~text
Title: EVALUATION OF GAUSSIAN PROCESSES AND OTHER METHODS FOR NON-LINEAR REGRESSION  
Abstract: The theory revision problem is the problem of how best to go about revising a deficient domain theory using information contained in examples that expose inaccuracies. In this paper we present our approach to the theory revision problem for propositional domain theories. The approach described here, called PTR, uses probabilities associated with domain theory elements to numerically track the ``ow'' of proof through the theory. This allows us to measure the precise role of a clause or literal in allowing or preventing a (desired or undesired) derivation for a given example. This information is used to efficiently locate and repair awed elements of the theory. PTR is proved to converge to a theory which correctly classifies all examples, and shown experimentally to be fast and accurate even for deep theories.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 6 nodes

| node id | true class | title |
|---|---|---|
| 125 | Neural_Networks | Gaussian Processes for Bayesian Classification via Hybrid Monte Carlo |
| 322 | Theory | Statistical Tests for Comparing Supervised Classification Learning Algorithms |
| 469 | Neural_Networks | Interpolation Models with Multiple |
| 1857 | Probabilistic_Methods | Monte Carlo Implementation of Gaussian Process Models for Bayesian Regression and Classification |
| 2540 | Neural_Networks | Efficient Implementation of Gaussian Processes |
| 2681 | Neural_Networks | Regression with Input-dependent Noise: A Gaussian Process Treatment |

### 2-hop (shortest distance exactly 2): 11 nodes

| node id | true class | title |
|---|---|---|
| 15 | Neural_Networks | Back Propagation is Sensitive to Initial Conditions |
| 78 | Theory | Probabilistic Networks: New Models and New Methods |
| 157 | Theory | A Practical Bayesian Framework for Backprop Networks |
| 214 | Neural_Networks | Bayesian Non-linear Modelling for the Prediction Competition |
| 394 | Neural_Networks | Prior Information and Generalized Questions |
| 611 | Neural_Networks | Learning networks for face analysis and synthesis |
| 967 | Theory | Rigorous Learning Curve Bounds from Statistical Mechanics |
| 1027 | Theory | Pessimistic decision tree pruning based on tree size |
| 1644 | Neural_Networks | A Comparative Study of ID3 and Backpropagation for English Text-to-Speech Mapping |
| 2020 | Neural_Networks | Variational Gaussian Process Classifiers |
| 2508 | Theory | WRAPPERS FOR PERFORMANCE ENHANCEMENT AND OBLIVIOUS DECISION GRAPHS |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/cora/cf-gnnexplainer-canonical/random_seed_42_*` (key=29).

- Factual class: **Neural_Networks**
- Counterfactual class: **Theory**
- Removed edges (global ids, 4): (160, 1857), (160, 2681), (611, 2540), (1857, 2540)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 160 |
| Factual_Target_Node_Neighbors | 125, 322, 469, 1857, 2540, 2681 |
| Factual_Target_Node_Features | gaussian, organis, regress, process, evalu, method |
| Counterfactual_Target_Node_Neighbors | 125, 322, 469, 2540 |
| Counterfactual_Target_Node_Features | gaussian, organis, regress, process, evalu, method |
| Factual_Target_Node_Class | Neural_Networks |
| Counterfactual_Target_Node_class | Theory |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 1857, 2681 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 160 |
| Factual_Target_Node_Neighbors | 125, 322, 469, 1857, 2540, 2681 |
| Factual_Target_Node_Features | gaussian, organis, regress, process, evalu, method |
| Counterfactual_Target_Node_Neighbors | 125, 322, 469, 2540 |
| Counterfactual_Target_Node_Features | gaussian, organis, regress, process, evalu, method |
| Factual_Target_Node_Class | Neural_Networks |
| Counterfactual_Target_Node_class | Theory |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 1857, 2681 |
| Natural_Language_Explanation | None |
