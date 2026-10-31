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

FULL NODE TEXT (complete canonical raw_text, no truncation; true label and hop distance from the target):
- node 160 [TARGET] true label: Neural_Networks
    Title: EVALUATION OF GAUSSIAN PROCESSES AND OTHER METHODS FOR NON-LINEAR REGRESSION Abstract: The theory revision problem is the problem of how best to go about revising a deficient domain theory using information contained in examples that expose inaccuracies. In this paper we present our approach to the theory revision problem for propositional domain theories. The approach described here, called PTR, uses probabilities associated with domain theory elements to numerically track the ``ow'' of proof through the theory. This allows us to measure the precise role of a clause or literal in allowing or preventing a (desired or undesired) derivation for a given example. This information is used to efficiently locate and repair awed elements of the theory. PTR is proved to converge to a theory which correctly classifies all examples, and shown experimentally to be fast and accurate even for deep theories.
- node 125 [1-hop (direct neighbor)] true label: Neural_Networks
    Title: Gaussian Processes for Bayesian Classification via Hybrid Monte Carlo Abstract: The full Bayesian method for applying neural networks to a prediction problem is to set up the prior/hyperprior structure for the net and then perform the necessary integrals. However, these integrals are not tractable analytically, and Markov Chain Monte Carlo (MCMC) methods are slow, especially if the parameter space is high-dimensional. Using Gaussian processes we can approximate the weight space integral analytically, so that only a small number of hyperparameters need be integrated over by MCMC methods. We have applied this idea to classification problems, obtaining ex cellent results on the real-world problems investigated so far.
- node 322 [1-hop (direct neighbor)] true label: Theory
    Title: Statistical Tests for Comparing Supervised Classification Learning Algorithms Abstract: This paper reviews five statistical tests for determining whether one learning algorithm outperforms another on a particular learning task. These tests are compared experimentally to determine their probability of incorrectly detecting a difference when no difference exists (type 1 error). Two widely-used statistical tests are shown to have high probability of Type I error in certain situations and should never be used. These tests are (a) a test for the difference of two proportions and (b) a paired-differences t test based on taking several random train/test splits. A third test, a paired-differences t test based on 10-fold cross-validation, exhibits somewhat elevated probability of Type I error. A fourth test, McNemar's test, is shown to have low Type I error. The fifth test is a new test, 5x2cv, based on 5 iterations of 2-fold cross-validation. Experiments show that this test also has good Type I error. The paper also measures the power (ability to detect algorithm differences when they do exist) of these tests. The 5x2cv test is shown to be slightly more powerful than McNemar's test. The choice of the best test is determined by the computational cost of running the learning algorithm. For algorithms that can be executed only once, McNemar's test is the only test with acceptable Type I error. For algorithms that can be executed ten times, the 5x2cv test is recommended, because it is slightly more powerful and because it directly measures variation due to the choice of training set.
- node 469 [1-hop (direct neighbor)] true label: Neural_Networks
    Title: Interpolation Models with Multiple Abstract: A traditional interpolation model is characterized by the choice of reg-ularizer applied to the interpolant, and the choice of noise model. Typically, the regularizer has a single regularization constant ff, and the noise model has a single parameter fi. The ratio ff=fi alone is responsible for determining globally all these attributes of the interpolant: its `complexity', `flexibility', `smoothness', `characteristic scale length', and `characteristic amplitude'. We suggest that interpolation models should be able to capture more than just one flavour of simplicity and complexity. We describe Bayesian models in which the interpolant has a smoothness that varies spatially. We emphasize the importance, in practical implementation, of the concept of `conditional convexity' when designing models with many hyperparameters. We apply the new models to the interpolation of neuronal spike data and demonstrate a substantial improvement in generalization error.
- node 1857 [1-hop (direct neighbor)] true label: Probabilistic_Methods
    Title: Monte Carlo Implementation of Gaussian Process Models for Bayesian Regression and Classification Abstract: Technical Report No. 9702, Department of Statistics, University of Toronto Abstract. Gaussian processes are a natural way of defining prior distributions over functions of one or more input variables. In a simple nonparametric regression problem, where such a function gives the mean of a Gaussian distribution for an observed response, a Gaussian process model can easily be implemented using matrix computations that are feasible for datasets of up to about a thousand cases. Hyperparameters that define the covariance function of the Gaussian process can be sampled using Markov chain methods. Regression models where the noise has a t distribution and logistic or probit models for classification applications can be implemented by sampling as well for latent values underlying the observations. Software is now available that implements these methods using covariance functions with hierarchical parameterizations. Models defined in this way can discover high-level properties of the data, such as which inputs are relevant to predicting the response.
- node 2540 [1-hop (direct neighbor)] true label: Neural_Networks
    Title: Efficient Implementation of Gaussian Processes Abstract: Neural networks and Bayesian inference provide a useful framework within which to solve regression problems. However their parameterization means that the Bayesian analysis of neural networks can be difficult. In this paper, we investigate a method for regression using Gaussian process priors which allows exact Bayesian analysis using matrix manipulations. We discuss the workings of the method in detail. We will also detail a range of mathematical and numerical techniques that are useful in applying Gaussian processes to general problems including efficient approximate matrix inversion methods developed by Skilling.
- node 2681 [1-hop (direct neighbor)] true label: Neural_Networks
    Title: Regression with Input-dependent Noise: A Gaussian Process Treatment Abstract: Technical Report NCRG/98/002, available from http://www.ncrg.aston.ac.uk/ To appear in Advances in Neural Information Processing Systems 10 eds. M. I. Jordan, M. J. Kearns and S. A. Solla. Lawrence Erlbaum (1998). Abstract Gaussian processes provide natural non-parametric prior distributions over regression functions. In this paper we consider regression problems where there is noise on the output, and the variance of the noise depends on the inputs. If we assume that the noise is a smooth function of the inputs, then it is natural to model the noise variance using a second Gaussian process, in addition to the Gaussian process governing the noise-free output value. We show that prior uncertainty about the parameters controlling both processes can be handled and that the posterior distribution of the noise rate can be sampled from using Markov chain Monte Carlo methods. Our results on a synthetic data set give a posterior noise variance that well-approximates the true variance.
- node 78 [2-hop] true label: Theory
    Title: Probabilistic Networks: New Models and New Methods Abstract: In this paper I describe the implementation of a probabilistic regression model in BUGS. BUGS is a program that carries out Bayesian inference on statistical problems using a simulation technique known as Gibbs sampling. It is possible to implement surprisingly complex regression models in this environment. I demonstrate the simultaneous inference of an interpolant and an input-dependent noise level.
- node 157 [2-hop] true label: Theory
    Title: A Practical Bayesian Framework for Backprop Networks Abstract: A quantitative and practical Bayesian framework is described for learning of mappings in feedforward networks. The framework makes possible: (1) objective comparisons between solutions using alternative network architectures; (2) objective stopping rules for network pruning or growing procedures; (3) objective choice of magnitude and type of weight decay terms or additive regularisers (for penalising large weights, etc.); (4) a measure of the effective number of well-determined parameters in a model; (5) quantified estimates of the error bars on network parameters and on network output; (6) objective comparisons with alternative learning and interpolation models such as splines and radial basis functions. The Bayesian `evidence' automatically embodies `Occam's razor,' penalising over-flexible and over-complex models. The Bayesian approach helps detect poor underlying assumptions in learning models. For learning models well matched to a problem, a good correlation between generalisation ability and the Bayesian evidence is obtained. This paper makes use of the Bayesian framework for regularisation and model comparison described in the companion paper `Bayesian interpolation' (MacKay, 1991a). This framework is due to Gull and Skilling (Gull, 1989a).
- node 214 [2-hop] true label: Neural_Networks
    Title: Bayesian Non-linear Modelling for the Prediction Competition Abstract: The 1993 energy prediction competition involved the prediction of a series of building energy loads from a series of environmental input variables. Non-linear regression using `neural networks' is a popular technique for such modeling tasks. Since it is not obvious how large a time-window of inputs is appropriate, or what preprocessing of inputs is best, this can be viewed as a regression problem in which there are many possible input variables, some of which may actually be irrelevant to the prediction of the output variable. Because a finite data set will show random correlations between the irrelevant inputs and the output, any conventional neural network (even with reg-ularisation or `weight decay') will not set the coefficients for these junk inputs to zero. Thus the irrelevant variables will hurt the model's performance. The Automatic Relevance Determination (ARD) model puts a prior over the regression parameters which embodies the concept of relevance. This is done in a simple and `soft' way by introducing multiple regularisation constants, one associated with each input. Using Bayesian methods, the regularisation constants for junk inputs are automatically inferred to be large, preventing those inputs from causing significant overfitting.
- node 394 [2-hop] true label: Neural_Networks
    Title: Prior Information and Generalized Questions Abstract: This report describes research done within the Center for Biological and Computational Learning in the Department of Brain and Cognitive Sciences at the Massachusetts Institute of Technology. This research is sponsored by a grant from National Science Foundation under contract ASC-9217041 and a grant from ONR/ARPA under contract N00014-92-J-1879. The author was supported by a Postdoctoral Fellowship (Le 1014/1-1) from the Deutsche Forschungsgemeinschaft and a NSF/CISE Postdoctoral Fellowship.
- node 2020 [2-hop] true label: Neural_Networks
    Title: Variational Gaussian Process Classifiers Abstract: