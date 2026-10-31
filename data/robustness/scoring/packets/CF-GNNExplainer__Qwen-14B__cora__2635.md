# Reference packet: CF-GNNExplainer__Qwen-14B__cora__2635

- Method: CF-GNNExplainer; configuration: Qwen-14B; dataset: cora; target node: 2635
- Explanation source: `./robustness_2026-10-30/production_a100/qwen14b_gptq_int4_cora_Response.json` ([523][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
To address the provided scenario, let's first populate the `infos` dictionary based on the given factual and counterfactual graphs, and then analyze the changes in the target node's classification.

### Populating the Dictionary

Given the factual and counterfactual graphs, we need to identify the differences in the target node (node 2635) and its neighbors. Here's the populated dictionary:

```python
infos = {
    'Target_Node_ID': '2635',
    'Factual_Target_Node_Neighbors': ['136', '2231'],
    'Factual_Target_Node_Features': ['explan', 'refin', 'kad', 'assist', 'system'],
    'Counterfactual_Target_Node_Neighbors': ['136'],
    'Counterfactual_Target_Node_Features': ['explan', 'refin', 'kad', 'assist', 'system'],
    'Factual_Target_Node_Class': 'Case_Based',
    'Counterfactual_Target_Node_class': 'Rule_Learning',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Natural_Language_Explanation': ''
}
```

### Explanation of Changes

#### Target Node ID: 2635
- **Factual Classification**: The target node (node 2635) was originally classified as `Case_Based`.
- **Counterfactual Classification**: In the counterfactual scenario, the same node is reclassified as `Rule_Learning`.

#### Neighbors of Target Node
- **Factual Neighbors**: Nodes 136 and 2231.
- **Counterfactual Neighbors**: Only node 136 remains connected; node 2231 is disconnected.

#### Features of Target Node
- **Factual Features**: `['explan', 'refin', 'kad', 'assist', 'system']`
- **Counterfactual Features**: No change in features (`['explan', 'refin', 'kad', 'assist', 'system']`).

### Analysis of Changes

In the factual graph, node 2635 is classified as `Case_Based`, which aligns with its neighbors (nodes 136 and 2231). Both nodes 136 and 2231 are classified as `Case_Based` and `Probabilistic_Methods`, respectively, indicating a mix of theoretical and practical approaches to knowledge refinement.

In the counterfactual graph, node 2635 retains the same features but is now classified as `Rule_Learning`. The only neighbor retained is node 136, which is classified as `Rule_Learning`. Node 2231, previously connected, is removed, suggesting that the removal of this neighbor influenced the classification shift.

### Influence of Neighbors

- **Node 136**: Retained in both scenarios, classified as `Rule_Learning`. Its influence likely contributed to the reclassification of node 2635 to `Rule_Learning` in the counterfactual scenario.
- **Node 2231**: Removed in the counterfactual scenario. This node was classified as `Case_Based`, and its removal may have weakened the `Case_Based` influence on node 2635, leading to a shift towards `Rule_Learning`.

### Natural Language Explanation

The natural language explanation for the change in classification of node 2635 from `Case_Based` to `Rule_Learning` can be summarized as follows:

"In the factual scenario, node 2635 ('Utilising Explanation to Assist the Refinement of Knowledge-Based Systems') is classified as `Case_Based` due to its connections with nodes 136 and 2231, both of which contribute to a mixed theoretical and practical context. However, in the counterfactual scenario, the removal of node 2231 and the retention of node 136, which is classified as `Rule_Learning`, shifts the classification of node 2635 to `Rule_Learning`. This change highlights the importance of the neighboring nodes in influencing the classification of a node within a graph-based learning model."

This detailed explanation provides insight into how the structural changes in the graph, specifically the removal of a neighbor node, can significantly impact the classification of a target node.
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
given the factual graph: The node 92 is a product titled 'Title: Learning Analytically and Inductively  
Abstract: Learning is a fundamental component of inte' with key attributes: question, consider, explain, barn, cognit, intellig, architectur, induct, fundament, appropri, compon, mechan, chapter, design, result, analyt, consid, interest, stationari, key and is connected with the nodes 136, 479, 1259 and it is classified as Rule_Learning, it is not the target node. The node 136 is a product titled 'Title: Theory Refinement Combining Analytical and Empirical Methods  
Abstract: This article describ' with key attributes: empir, explan, comprehens, imperfect, refin, articl, fail, portion, order, exampl, classifi, fault, combin, describ, result, analyt, attempt, revis, given, automat, correl, theori, method, identifi and is connected with the nodes 92, 159, 244, 479, 986, 1102, 1259, 1370, 1413, 1479, 1539, 1776, 2172, 2231, 2399, 2487, 2543, 2580, 2635 and it is classified as Rule_Learning, it is not the target node. The node 159 is a product titled 'Title: Bias-Driven Revision of Logical Domain Theories  
Abstract: The theory revision problem is th' with key attributes: inform, domain, best, probabl, exampl, logic, describ, proposit, contain, result, revis, associ, call, theori and is connected with the nodes 136, 2172, 2543 and it is classified as Theory, it is not the target node. The node 244 is a product titled 'Title: Building Intelligent Agents for Web-Based Tasks: A Theory-Refinement Approach  
Abstract: We' with key attributes: agent, implement, function, easili, accur, highli, basic, intellig, softwar, center, heurist, standard, lead, build, system, evalu, design, search, given, task, rapidli and is connected with the node 136 and it is classified as Rule_Learning, it is not the target node. The node 479 is a product titled 'Title: Learning physical descriptions from functional definitions, examples, Learning from examples:' with key attributes: descript, function, physic, conceptu, exampl, effect, definit, result, differ and is connected with the nodes 92, 136 and it is classified as Case_Based, it is not the target node. The node 986 is a product titled 'Title: Improving accuracy by combining rule-based and case-based reasoning  
Abstract: An architectu' with key attributes: reason, nonprofit, similar, aspect, target, approxim, behavior, rule, appli, architectur, novel, read, cbr, idea, system, combin, improv, model, central, known and is connected with the node 136 and it is classified as Case_Based, it is not the target node. The node 1102 is a product titled 'Title: Automated Refinement of First-Order Horn-Clause Domain Theories  
Abstract: Knowledge acquisi' with key attributes: domain, exist, acquisit, class, address, refin, autom, system, mesh, result, improv, task, perform, difficult, automat, theori, base, method, knowledg and is connected with the nodes 136, 1370, 1413, 1479 and it is classified as Rule_Learning, it is not the target node. The node 1259 is a product titled 'Title: Finding Accurate Frontiers: A Knowledge-Intensive Approach to Relational Learning  
Abstract:' with key attributes: inform, entail, domain, function, accur, guid, appli, climb, relat, set, horn, deriv, oper, claus, describ, evalu, search, analyt, result, perform, theori, base and is connected with the nodes 92, 136 and it is classified as Rule_Learning, it is not the target node. The node 1370 is a product titled 'Title: From Theory Refinement to KB Maintenance: a Position Statement  
Abstract: Since we consider' with key attributes: methodolog, descript, clear, explain, overview, refin, actual, possibl, tri, give, kad, view, sinc, posit, structur, search, result, mainten, consid, key, concept, theori and is connected with the nodes 136, 1102 and it is classified as Rule_Learning, it is not the target node. The node 1413 is a product titled 'Title: References Automatic student modeling and bug library construction using theory refinement. P' with key attributes: symbol, refin, tutor, intellig, librari, assert, machin, refer, build, system, student, techniqu, develop, result, model, revis, demonstr, construct, automat, theori, applic and is connected with the nodes 136, 1102 and it is classified as Case_Based, it is not the target node. The node 1479 is a product titled 'Title: Revising Bayesian Network Parameters Using Backpropagation  
Abstract: The problem of learnin' with key attributes: network, condit, paramet, hidden, probabl, dayan, simpler, variabl, backpropag, result, revis, bayesian, task, hard, known and is connected with the nodes 136, 1102, 2543 and it is classified as Probabilistic_Methods, it is not the target node. The node 1539 is a product titled 'Title: Finding new rules for incomplete theories: Explicit biases for induction with contextual info' with key attributes: inform, back, connect, unit, address, initi, translat, refin, rule, hidden, explicit, induct, backpropag, incomplet, bias, requir, result, proceed, theori, howev and is connected with the node 136 and it is classified as Rule_Learning, it is not the target node. The node 1776 is a product titled 'Title: Extending Theory Refinement to M-of-N Rules  
Abstract: In recent years, machine learning res' with key attributes: extend, research, domain, address, start, refin, rule, year, set, input, machin, modifi, learner, incomplet, recent, result, consist, known, theori, base, goal, repres and is connected with the nodes 136, 2543 and it is classified as Rule_Learning, it is not the target node. The node 2172 is a product titled 'Title: Tractability of Theory Patching  
Abstract: In this paper we consider the problem of theory p' with key attributes: correctli, domain, indic, possibl, exampl, set, train, compon, tractabl, label, result, revis, given, consid, concept, theori, instanc and is connected with the nodes 136, 159 and it is classified as Theory, it is not the target node. The node 2231 is a product titled 'Title: Explaining Anomalies as a Basis for Knowledge Base Refinement  
Abstract: Explanations play a' with key attributes: explan, limit, explain, refin, basi, guid, detect, autom, comprehens, take, play, role, procedur, techniqu, result, introduc, key, small, base, knowledg and is connected with the nodes 136, 2635 and it is classified as Case_Based, it is not the target node. The node 2399 is a product titled 'Title: Abduction, Experience, and Goals: A Model of Everyday Abductive Explanation*  
Abstract: When' with key attributes: abduct, model, experi, goal and is connected with the node 136 and it is classified as Case_Based, it is not the target node. The node 2487 is a product titled 'Title: An Optimized Theory Revision Module  
Abstract: Theory revision systems typically use a set o' with key attributes: empir, optim, initi, modul, maximum, instanc, climb, transform, typic, set, local, train, process, system, label, accuraci, evalu, revis, given, compar, theori and is connected with the node 136 and it is classified as Case_Based, it is not the target node. The node 2543 is a product titled 'Title: Combining Connectionist and Symbolic Learning to Refine Certainty-Factor Rule Bases  
Abstrac' with key attributes: symbol, refin, connectionist, rule, modifi, factor, backpropag, system, combin, describ, probabilist, result, revis, version, base, method, knowledg and is connected with the nodes 136, 159, 1479, 1776 and it is classified as Probabilistic_Methods, it is not the target node. The node 2580 is a product titled 'Title: The Challenge of Revising an Impure Theory  
Abstract: A pure rule-based program will return' with key attributes: reason, pure, nonprofit, return, cut, rule, set, answer, oper, mani, program, challeng, revis, includ, theori, differ, howev and is connected with the node 136 and it is classified as Rule_Learning, it is not the target node. The node 2635 is a product titled 'Title: Utilising Explanation to Assist the Refinement of Knowledge-Based Systems  
Abstract: Standar' with key attributes: explan, refin, kad, assist, system and is connected with the nodes 136, 2231 and it is classified as Case_Based, it is the target node. and given the counterfactual example: The node 92 is a product titled 'Title: Learning Analytically and Inductively  
Abstract: Learning is a fundamental component of inte' with key attributes: question, consider, explain, barn, cognit, intellig, architectur, induct, fundament, appropri, compon, mechan, chapter, design, result, analyt, consid, interest, stationari, key and is connected with the nodes 479, 1259 and it is classified as Rule_Learning, it is not the target node. The node 136 is a product titled 'Title: Theory Refinement Combining Analytical and Empirical Methods  
Abstract: This article describ' with key attributes: empir, explan, comprehens, imperfect, refin, articl, fail, portion, order, exampl, classifi, fault, combin, describ, result, analyt, attempt, revis, given, automat, correl, theori, method, identifi and is connected with the nodes 159, 1259, 1370, 1413, 1479, 1776, 2231, 2487, 2543, 2580, 2635 and it is classified as Rule_Learning, it is not the target node. The node 159 is a product titled 'Title: Bias-Driven Revision of Logical Domain Theories  
Abstract: The theory revision problem is th' with key attributes: inform, domain, best, probabl, exampl, logic, describ, proposit, contain, result, revis, associ, call, theori and is connected with the nodes 136, 2172, 2543 and it is classified as Theory, it is not the target node. The node 244 is a product titled 'Title: Building Intelligent Agents for Web-Based Tasks: A Theory-Refinement Approach  
Abstract: We' with key attributes: agent, implement, function, easili, accur, highli, basic, intellig, softwar, center, heurist, standard, lead, build, system, evalu, design, search, given, task, rapidli and is connected with no other nodes and it is classified as Neural_Networks, it is not the target node. The node 479 is a product titled 'Title: Learning physical descriptions from functional definitions, examples, Learning from examples:' with key attributes: descript, function, physic, conceptu, exampl, effect, definit, result, differ and is connected with the node 92 and it is classified as Case_Based, it is not the target node. The node 986 is a product titled 'Title: Improving accuracy by combining rule-based and case-based reasoning  
Abstract: An architectu' with key attributes: reason, nonprofit, similar, aspect, target, approxim, behavior, rule, appli, architectur, novel, read, cbr, idea, system, combin, improv, model, central, known and is connected with no other nodes and it is classified as Case_Based, it is not the target node. The node 1102 is a product titled 'Title: Automated Refinement of First-Order Horn-Clause Domain Theories  
Abstract: Knowledge acquisi' with key attributes: domain, exist, acquisit, class, address, refin, autom, system, mesh, result, improv, task, perform, difficult, automat, theori, base, method, knowledg and is connected with the nodes 1370, 1413, 1479 and it is classified as Rule_Learning, it is not the target node. The node 1259 is a product titled 'Title: Finding Accurate Frontiers: A Knowledge-Intensive Approach to Relational Learning  
Abstract:' with key attributes: inform, entail, domain, function, accur, guid, appli, climb, relat, set, horn, deriv, oper, claus, describ, evalu, search, analyt, result, perform, theori, base and is connected with the nodes 92, 136 and it is classified as Rule_Learning, it is not the target node. The node 1370 is a product titled 'Title: From Theory Refinement to KB Maintenance: a Position Statement  
Abstract: Since we consider' with key attributes: methodolog, descript, clear, explain, overview, refin, actual, possibl, tri, give, kad, view, sinc, posit, structur, search, result, mainten, consid, key, concept, theori and is connected with the nodes 136, 1102 and it is classified as Rule_Learning, it is not the target node. The node 1413 is a product titled 'Title: References Automatic student modeling and bug library construction using theory refinement. P' with key attributes: symbol, refin, tutor, intellig, librari, assert, machin, refer, build, system, student, techniqu, develop, result, model, revis, demonstr, construct, automat, theori, applic and is connected with the nodes 136, 1102 and it is classified as Case_Based, it is not the target node. The node 1479 is a product titled 'Title: Revising Bayesian Network Parameters Using Backpropagation  
Abstract: The problem of learnin' with key attributes: network, condit, paramet, hidden, probabl, dayan, simpler, variabl, backpropag, result, revis, bayesian, task, hard, known and is connected with the nodes 136, 1102, 2543 and it is classified as Probabilistic_Methods, it is not the target node. The node 1539 is a product titled 'Title: Finding new rules for incomplete theories: Explicit biases for induction with contextual info' with key attributes: inform, back, connect, unit, address, initi, translat, refin, rule, hidden, explicit, induct, backpropag, incomplet, bias, requir, result, proceed, theori, howev and is connected with no other nodes and it is classified as Rule_Learning, it is not the target node. The node 1776 is a product titled 'Title: Extending Theory Refinement to M-of-N Rules  
Abstract: In recent years, machine learning res' with key attributes: extend, research, domain, address, start, refin, rule, year, set, input, machin, modifi, learner, incomplet, recent, result, consist, known, theori, base, goal, repres and is connected with the nodes 136, 2543 and it is classified as Rule_Learning, it is not the target node. The node 2172 is a product titled 'Title: Tractability of Theory Patching  
Abstract: In this paper we consider the problem of theory p' with key attributes: correctli, domain, indic, possibl, exampl, set, train, compon, tractabl, label, result, revis, given, consid, concept, theori, instanc and is connected with the node 159 and it is classified as Theory, it is not the target node. The node 2231 is a product titled 'Title: Explaining Anomalies as a Basis for Knowledge Base Refinement  
Abstract: Explanations play a' with key attributes: explan, limit, explain, refin, basi, guid, detect, autom, comprehens, take, play, role, procedur, techniqu, result, introduc, key, small, base, knowledg and is connected with the node 136 and it is classified as Case_Based, it is not the target node. The node 2399 is a product titled 'Title: Abduction, Experience, and Goals: A Model of Everyday Abductive Explanation*  
Abstract: When' with key attributes: abduct, model, experi, goal and is connected with no other nodes and it is classified as Probabilistic_Methods, it is not the target node. The node 2487 is a product titled 'Title: An Optimized Theory Revision Module  
Abstract: Theory revision systems typically use a set o' with key attributes: empir, optim, initi, modul, maximum, instanc, climb, transform, typic, set, local, train, process, system, label, accuraci, evalu, revis, given, compar, theori and is connected with the node 136 and it is classified as Case_Based, it is not the target node. The node 2543 is a product titled 'Title: Combining Connectionist and Symbolic Learning to Refine Certainty-Factor Rule Bases  
Abstrac' with key attributes: symbol, refin, connectionist, rule, modifi, factor, backpropag, system, combin, describ, probabilist, result, revis, version, base, method, knowledg and is connected with the nodes 136, 159, 1479, 1776 and it is classified as Probabilistic_Methods, it is not the target node. The node 2580 is a product titled 'Title: The Challenge of Revising an Impure Theory  
Abstract: A pure rule-based program will return' with key attributes: reason, pure, nonprofit, return, cut, rule, set, answer, oper, mani, program, challeng, revis, includ, theori, differ, howev and is connected with the node 136 and it is classified as Rule_Learning, it is not the target node. The node 2635 is a product titled 'Title: Utilising Explanation to Assist the Refinement of Knowledge-Based Systems  
Abstract: Standar' with key attributes: explan, refin, kad, assist, system and is connected with the node 136 and it is classified as Rule_Learning, it is the target node.
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

- ID: 2635
- Title: Utilising Explanation to Assist the Refinement of Knowledge-Based Systems
- True class (canonical `y`): **Case_Based**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Case_Based**
- Prediction recorded by this method's pipeline: **Case_Based**

Canonical text (`raw_text`):

~~~~~~text
Title: Utilising Explanation to Assist the Refinement of Knowledge-Based Systems  
Abstract: Standard statistical practice ignores model uncertainty. Data analysts typically select a model from some class of models and then proceed as if the selected model had generated the data. This approach ignores the uncertainty in model selection, leading to over-confident inferences and decisions that are more risky than one thinks they are. Bayesian model averaging (BMA) provides a coherent mechanism for accounting for this model uncertainty. Several methods for implementing BMA have recently emerged. We discuss these methods and present a number of examples. In these examples, BMA provides improved out-of-sample predictive performance. We also provide a catalogue of currently available BMA software. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 2 nodes

| node id | true class | title |
|---|---|---|
| 136 | Rule_Learning | Theory Refinement Combining Analytical and Empirical Methods |
| 2231 | Case_Based | Explaining Anomalies as a Basis for Knowledge Base Refinement |

### 2-hop (shortest distance exactly 2): 17 nodes

| node id | true class | title |
|---|---|---|
| 92 | Reinforcement_Learning | Learning Analytically and Inductively |
| 159 | Theory | Bias-Driven Revision of Logical Domain Theories |
| 244 | Neural_Networks | Building Intelligent Agents for Web-Based Tasks: A Theory-Refinement Approach |
| 479 | Case_Based | Learning physical descriptions from functional definitions, examples, Learning from examples: The effect of different conceptual |
| 986 | Case_Based | Improving accuracy by combining rule-based and case-based reasoning |
| 1102 | Rule_Learning | Automated Refinement of First-Order Horn-Clause Domain Theories |
| 1259 | Rule_Learning | Finding Accurate Frontiers: A Knowledge-Intensive Approach to Relational Learning |
| 1370 | Rule_Learning | From Theory Refinement to KB Maintenance: a Position Statement |
| 1413 | Case_Based | References Automatic student modeling and bug library construction using theory refinement. Ph.D. ml/ Symbolic revision |
| 1479 | Probabilistic_Methods | Revising Bayesian Network Parameters Using Backpropagation |
| 1539 | Rule_Learning | Finding new rules for incomplete theories: Explicit biases for induction with contextual information. In Proceedings |
| 1776 | Rule_Learning | Extending Theory Refinement to M-of-N Rules |
| 2172 | Theory | Tractability of Theory Patching |
| 2399 | Case_Based | Abduction, Experience, and Goals: A Model of Everyday Abductive Explanation* |
| 2487 | Theory | An Optimized Theory Revision Module |
| 2543 | Probabilistic_Methods | Combining Connectionist and Symbolic Learning to Refine Certainty-Factor Rule Bases |
| 2580 | Theory | The Challenge of Revising an Impure Theory |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/cora/cf-gnnexplainer-canonical/random_seed_42_*` (key=523).

- Factual class: **Case_Based**
- Counterfactual class: **Rule_Learning**
- Removed edges (global ids, 9): (92, 136), (136, 244), (136, 479), (136, 986), (136, 1102), (136, 1539), (136, 2172), (136, 2399), (2231, 2635)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 2635 |
| Factual_Target_Node_Neighbors | 136, 2231 |
| Factual_Target_Node_Features | explan, refin, kad, assist, system |
| Counterfactual_Target_Node_Neighbors | 136 |
| Counterfactual_Target_Node_Features | explan, refin, kad, assist, system |
| Factual_Target_Node_Class | Case_Based |
| Counterfactual_Target_Node_class | Rule_Learning |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 2231 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 2635 |
| Factual_Target_Node_Neighbors | 136, 2231 |
| Factual_Target_Node_Features | explan, refin, kad, assist, system |
| Counterfactual_Target_Node_Neighbors | 136 |
| Counterfactual_Target_Node_Features | explan, refin, kad, assist, system |
| Factual_Target_Node_Class | Case_Based |
| Counterfactual_Target_Node_class | Rule_Learning |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 2231 |
| Natural_Language_Explanation | None |
