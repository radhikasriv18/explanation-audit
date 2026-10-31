# Reference packet: CF-GNNExplainer__Qwen-14B__cora__2539

- Method: CF-GNNExplainer; configuration: Qwen-14B; dataset: cora; target node: 2539
- Explanation source: `./robustness_2026-10-30/production_a100/qwen14b_gptq_int4_cora_Response.json` ([498][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
To fill the `infos` dictionary and provide a detailed explanation of the changes observed between the factual and counterfactual examples, let's analyze the provided information step-by-step.

### Factual Example

In the factual graph, the target node (node 2539) is titled "Mining for Causes of Cancer: Machine Learning Experiments at Various Levels of Detail." It is classified as `Rule_Learning`. The node is connected to nodes 1322, 1428, and 2213. 

### Counterfactual Example

In the counterfactual graph, the same target node (node 2539) is still titled "Mining for Causes of Cancer: Machine Learning Experiments at Various Levels of Detail," but it is now classified as `Neural_Networks`. The node is only connected to nodes 1322 and 1428.

### Differences Identified

#### Node Differences
- **Node ID:** 2539
- **Factual Classification:** Rule_Learning
- **Counterfactual Classification:** Neural_Networks

#### Edge Differences
- **Factual Connections:** [1322, 1428, 2213]
- **Counterfactual Connections:** [1322, 1428]

The connections to node 2213 were removed in the counterfactual scenario.

### Filling the Dictionary

Based on the above observations, we can fill the `infos` dictionary as follows:

```python
infos = {
    'Target_Node_ID': 2539,
    'Factual_Target_Node_Neighbors': [1322, 1428, 2213],
    'Factual_Target_Node_Features': ['research', 'methodolog', 'point', 'scientif', 'level', 'data', 'project', 'detector', 'detail', 'machin', 'view', 'deriv', 'mine', 'variou', 'pharmaceut', 'program', 'caus', 'result', 'experi', 'studi', 'analyz'],
    'Counterfactual_Target_Node_Neighbors': [1322, 1428],
    'Counterfactual_Target_Node_Features': ['research', 'methodolog', 'point', 'scientif', 'level', 'data', 'project', 'detector', 'detail', 'machin', 'view', 'deriv', 'mine', 'variou', 'pharmaceut', 'program', 'caus', 'result', 'experi', 'studi', 'analyz'],
    'Factual_Target_Node_Class': 'Rule_Learning',
    'Counterfactual_Target_Node_class': 'Neural_Networks',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Natural_Language_Explanation': 'In the counterfactual scenario, the target node (node 2539) was reclassified from Rule_Learning to Neural_Networks. The removal of the connection to node 2213 appears to have influenced this change.'
}
```

### Explanation of Changes

The primary difference between the factual and counterfactual scenarios lies in the classification of the target node (node 2539). In the factual scenario, the node is classified as `Rule_Learning`, while in the counterfactual scenario, it is classified as `Neural_Networks`.

The removal of the connection to node 2213 seems to be a critical factor in this change. Node 2213, which is classified as `Rule_Learning`, likely provided contextual support for the target node to remain within the `Rule_Learning` category. By removing this connection, the influence of `Rule_Learning` nodes diminished, leading the model to classify the target node as `Neural_Networks`.

This shift highlights the importance of the graph structure and the interconnectedness of nodes in influencing the classification outcomes. The removal of a single connection can significantly alter the model's perception of a node's context and thus its classification.

In summary, the counterfactual explanation reveals that altering the graph structure by removing a specific connection can lead to a different classification for the target node, demonstrating the sensitivity of graph-based machine learning models to their input structure.
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
given the factual graph: The node 323 is a product titled 'Title: Learning Active Classifiers  
Abstract: Many classification algorithms are "passive", in that' with key attributes: descript, class, expect, attribut, valu, instanc, assign, genet, classif, comprehens, classifi, incomplet, util, contrast, label, mani, cost, obtain, darian, activ, given, result, decid, base and is connected with the node 1322 and it is classified as Theory, it is not the target node. The node 1020 is a product titled 'Title: Error-Based and Entropy-Based Discretization of Continuous Features  
Abstract: We present a' with key attributes: empir, extens, art, minim, criterion, comparison, featur, analysi, continu, decis, error, includ, studi, base, method, may, discret and is connected with the node 1322 and it is classified as Theory, it is not the target node. The node 1027 is a product titled 'Title: Pessimistic decision tree pruning based on tree size  
Abstract: In this work we develop a ne' with key attributes: chervonenki, motiv, tree, dimens, sound, prune, converg, size, decis, criteria, uniform, develop, result, work, perform, compar, theoret, concept, theori, base, method and is connected with the node 1322 and it is classified as Theory, it is not the target node. The node 1259 is a product titled 'Title: Finding Accurate Frontiers: A Knowledge-Intensive Approach to Relational Learning  
Abstract:' with key attributes: inform, entail, domain, function, accur, guid, appli, climb, relat, set, horn, deriv, oper, claus, describ, evalu, search, analyt, result, perform, theori, base and is connected with the node 2213 and it is classified as Rule_Learning, it is not the target node. The node 1312 is a product titled 'Title: Learning Trees and Rules with Set-valued Features  
Abstract: In most learning systems exampl' with key attributes: extens, vector, tree, valu, rule, instanc, allow, featur, exampl, set, real, compon, system, propos, represent, result, small, repres and is connected with the nodes 1428, 1622 and it is classified as Rule_Learning, it is not the target node. The node 1322 is a product titled 'Title: Theory and Applications of Agnostic PAC-Learning with Small Decision Trees  
Abstract: We exh' with key attributes: tree, linear, pac, level, genet, common, comput, time, set, size, decis, train, world, exhibit, evalu, result, perform, small, theoret, theori, applic and is connected with the nodes 323, 1020, 1027, 1622, 2539 and it is classified as Theory, it is not the target node. The node 1428 is a product titled 'Title: Inverse entailment and Progol  
Abstract: This paper firstly provides a re-appraisal of the d' with key attributes: avail, entail, enhanc, implement, invers, invert, generalis, previou, system, provid, describ, techniqu, develop, result, introduc and is connected with the nodes 1312, 1601, 1622, 2079, 2229, 2329, 2424, 2493, 2539, 2617 and it is classified as Rule_Learning, it is not the target node. The node 1601 is a product titled 'Title: Learning the Past Tense of English Verbs: The Symbolic Pattern Associator vs. Connectionist M' with key attributes: rosenberg, past, symbol, pattern, acquisit, adequaci, aspect, connectionist, sinc, languag, model, recent, becom, result, associ, gener, heat and is connected with the node 1428 and it is classified as Neural_Networks, it is not the target node. The node 1622 is a product titled 'Title: Stochastic Propositionalization of Non-Determinate Background Knowledge  
Abstract: It is a w' with key attributes: practic, domain, good, properti, background, genet, data, fact, settl, featur, engin, major, induct, requir, step, proposit, structur, result, perform, construct, stochast, expert, knowledg, repres and is connected with the nodes 1312, 1322, 1428 and it is classified as Rule_Learning, it is not the target node. The node 2079 is a product titled 'Title: Extraction of Meta-Knowledge to Restrict the Hypothesis Space for ILP Systems incorporating t' with key attributes: inform, predic, advantag, space, hypothesi, restrict, ilp, user, extract, take, form, type, incorpor, argument, system, suppli, mani, result and is connected with the node 1428 and it is classified as Rule_Learning, it is not the target node. The node 2126 is a product titled 'Title: Applying ILP to Diterpene Structure Elucidation from 13 C NMR Spectra  
Abstract: We present' with key attributes: weight, low, ilp, appli, novel, comprehens, carbon, pharmaceut, structur, signific, organ, commerci, interest, base, applic, molecular and is connected with the node 2213 and it is classified as Rule_Learning, it is not the target node. The node 2213 is a product titled 'Title: Generating Declarative Language Bias for Top-Down ILP Algorithms  
Abstract: Many of today's' with key attributes: issu, defin, address, declar, ilp, genet, user, top, respons, induct, fashion, logic, bia, mani, languag, program, develop, result, gener, method and is connected with the nodes 1259, 2126, 2253, 2290, 2539 and it is classified as Rule_Learning, it is not the target node. The node 2229 is a product titled 'Title: Bottom-up induction of logic programs with more than one recursive clause  
Abstract: In this' with key attributes: induc, bottom, recurs, genet, analysi, exampl, induct, logic, claus, program, result, call, compar, small, base, satur, method and is connected with the node 1428 and it is classified as Rule_Learning, it is not the target node. The node 2253 is a product titled 'Title: Top-down Induction of Logical Decision Trees  
Abstract: A first order framework for top-down' with key attributes: introduct, tree, popular, relat, top, machin, induct, decis, contribut, main, logic, program, proposit, techniqu, result, recent, compar and is connected with the node 2213 and it is classified as Rule_Learning, it is not the target node. The node 2290 is a product titled 'Title: A Comparison of Pruning Methods for Relational Concept Learning  
Abstract: Pre-Pruning and P' with key attributes: descript, accur, deal, prune, nois, declar, specif, effici, relat, comparison, typic, comprehens, standard, result, gener, compar, concept, method and is connected with the node 2213 and it is classified as Rule_Learning, it is not the target node. The node 2329 is a product titled 'Title: Programming Research Group A LEARNABILITY MODEL FOR UNIVERSAL REPRESENTATIONS  
Abstract: Thi' with key attributes: research, group, learnabl, program, represent, model, univers and is connected with the node 1428 and it is classified as Rule_Learning, it is not the target node. The node 2424 is a product titled 'Title: Which Hypotheses Can Be Found with Inverse Entailment? -Extended Abstract  
Abstract: In this' with key attributes: entail, hypothesi, invers, rel, hypothes, rule, background, exampl, give, complet, induct, deriv, sens, main, theorem, claus, propos, result, infer, theori and is connected with the node 1428 and it is classified as Rule_Learning, it is not the target node. The node 2493 is a product titled 'Title: Relational Knowledge Discovery in Databases  
Abstract: In this paper, we indicate some possi' with key attributes: pure, link, indic, similar, possibl, ilp, relat, discuss, adapt, discoveri, system, propos, techniqu, result, rang, databas, field, base, method, applic, knowledg, sever and is connected with the node 1428 and it is classified as Rule_Learning, it is not the target node. The node 2539 is a product titled 'Title: Mining for Causes of Cancer: Machine Learning Experiments at Various Levels of Detail  
Abstr' with key attributes: research, methodolog, point, scientif, level, data, project, detector, detail, machin, view, deriv, mine, variou, pharmaceut, program, caus, result, experi, studi, analyz and is connected with the nodes 1322, 1428, 2213 and it is classified as Rule_Learning, it is the target node. The node 2617 is a product titled 'Title: Predicting Ordinal Classes in ILP  
Abstract: This paper is devoted to the problem of learnin' with key attributes: predict, tree, class, way, start, ilp, genet, order, transform, relat, set, ordin, variou, learner, name, regress, mesh, structur, result, studi, discret and is connected with the node 1428 and it is classified as Rule_Learning, it is not the target node. and given the counterfactual example: The node 323 is a product titled 'Title: Learning Active Classifiers  
Abstract: Many classification algorithms are "passive", in that' with key attributes: descript, class, expect, attribut, valu, instanc, assign, genet, classif, comprehens, classifi, incomplet, util, contrast, label, mani, cost, obtain, darian, activ, given, result, decid, base and is connected with the node 1322 and it is classified as Theory, it is not the target node. The node 1020 is a product titled 'Title: Error-Based and Entropy-Based Discretization of Continuous Features  
Abstract: We present a' with key attributes: empir, extens, art, minim, criterion, comparison, featur, analysi, continu, decis, error, includ, studi, base, method, may, discret and is connected with no other nodes and it is classified as Probabilistic_Methods, it is not the target node. The node 1027 is a product titled 'Title: Pessimistic decision tree pruning based on tree size  
Abstract: In this work we develop a ne' with key attributes: chervonenki, motiv, tree, dimens, sound, prune, converg, size, decis, criteria, uniform, develop, result, work, perform, compar, theoret, concept, theori, base, method and is connected with no other nodes and it is classified as Theory, it is not the target node. The node 1259 is a product titled 'Title: Finding Accurate Frontiers: A Knowledge-Intensive Approach to Relational Learning  
Abstract:' with key attributes: inform, entail, domain, function, accur, guid, appli, climb, relat, set, horn, deriv, oper, claus, describ, evalu, search, analyt, result, perform, theori, base and is connected with the node 2213 and it is classified as Rule_Learning, it is not the target node. The node 1312 is a product titled 'Title: Learning Trees and Rules with Set-valued Features  
Abstract: In most learning systems exampl' with key attributes: extens, vector, tree, valu, rule, instanc, allow, featur, exampl, set, real, compon, system, propos, represent, result, small, repres and is connected with the nodes 1428, 1622 and it is classified as Neural_Networks, it is not the target node. The node 1322 is a product titled 'Title: Theory and Applications of Agnostic PAC-Learning with Small Decision Trees  
Abstract: We exh' with key attributes: tree, linear, pac, level, genet, common, comput, time, set, size, decis, train, world, exhibit, evalu, result, perform, small, theoret, theori, applic and is connected with the nodes 323, 2539 and it is classified as Theory, it is not the target node. The node 1428 is a product titled 'Title: Inverse entailment and Progol  
Abstract: This paper firstly provides a re-appraisal of the d' with key attributes: avail, entail, enhanc, implement, invers, invert, generalis, previou, system, provid, describ, techniqu, develop, result, introduc and is connected with the nodes 1312, 1601, 2329, 2539 and it is classified as Neural_Networks, it is not the target node. The node 1601 is a product titled 'Title: Learning the Past Tense of English Verbs: The Symbolic Pattern Associator vs. Connectionist M' with key attributes: rosenberg, past, symbol, pattern, acquisit, adequaci, aspect, connectionist, sinc, languag, model, recent, becom, result, associ, gener, heat and is connected with the node 1428 and it is classified as Neural_Networks, it is not the target node. The node 1622 is a product titled 'Title: Stochastic Propositionalization of Non-Determinate Background Knowledge  
Abstract: It is a w' with key attributes: practic, domain, good, properti, background, genet, data, fact, settl, featur, engin, major, induct, requir, step, proposit, structur, result, perform, construct, stochast, expert, knowledg, repres and is connected with the node 1312 and it is classified as Rule_Learning, it is not the target node. The node 2079 is a product titled 'Title: Extraction of Meta-Knowledge to Restrict the Hypothesis Space for ILP Systems incorporating t' with key attributes: inform, predic, advantag, space, hypothesi, restrict, ilp, user, extract, take, form, type, incorpor, argument, system, suppli, mani, result and is connected with no other nodes and it is classified as Rule_Learning, it is not the target node. The node 2126 is a product titled 'Title: Applying ILP to Diterpene Structure Elucidation from 13 C NMR Spectra  
Abstract: We present' with key attributes: weight, low, ilp, appli, novel, comprehens, carbon, pharmaceut, structur, signific, organ, commerci, interest, base, applic, molecular and is connected with the node 2213 and it is classified as Rule_Learning, it is not the target node. The node 2213 is a product titled 'Title: Generating Declarative Language Bias for Top-Down ILP Algorithms  
Abstract: Many of today's' with key attributes: issu, defin, address, declar, ilp, genet, user, top, respons, induct, fashion, logic, bia, mani, languag, program, develop, result, gener, method and is connected with the nodes 1259, 2126, 2253, 2290 and it is classified as Rule_Learning, it is not the target node. The node 2229 is a product titled 'Title: Bottom-up induction of logic programs with more than one recursive clause  
Abstract: In this' with key attributes: induc, bottom, recurs, genet, analysi, exampl, induct, logic, claus, program, result, call, compar, small, base, satur, method and is connected with no other nodes and it is classified as Rule_Learning, it is not the target node. The node 2253 is a product titled 'Title: Top-down Induction of Logical Decision Trees  
Abstract: A first order framework for top-down' with key attributes: introduct, tree, popular, relat, top, machin, induct, decis, contribut, main, logic, program, proposit, techniqu, result, recent, compar and is connected with the node 2213 and it is classified as Rule_Learning, it is not the target node. The node 2290 is a product titled 'Title: A Comparison of Pruning Methods for Relational Concept Learning  
Abstract: Pre-Pruning and P' with key attributes: descript, accur, deal, prune, nois, declar, specif, effici, relat, comparison, typic, comprehens, standard, result, gener, compar, concept, method and is connected with the node 2213 and it is classified as Rule_Learning, it is not the target node. The node 2329 is a product titled 'Title: Programming Research Group A LEARNABILITY MODEL FOR UNIVERSAL REPRESENTATIONS  
Abstract: Thi' with key attributes: research, group, learnabl, program, represent, model, univers and is connected with the node 1428 and it is classified as Rule_Learning, it is not the target node. The node 2424 is a product titled 'Title: Which Hypotheses Can Be Found with Inverse Entailment? -Extended Abstract  
Abstract: In this' with key attributes: entail, hypothesi, invers, rel, hypothes, rule, background, exampl, give, complet, induct, deriv, sens, main, theorem, claus, propos, result, infer, theori and is connected with no other nodes and it is classified as Rule_Learning, it is not the target node. The node 2493 is a product titled 'Title: Relational Knowledge Discovery in Databases  
Abstract: In this paper, we indicate some possi' with key attributes: pure, link, indic, similar, possibl, ilp, relat, discuss, adapt, discoveri, system, propos, techniqu, result, rang, databas, field, base, method, applic, knowledg, sever and is connected with no other nodes and it is classified as Rule_Learning, it is not the target node. The node 2539 is a product titled 'Title: Mining for Causes of Cancer: Machine Learning Experiments at Various Levels of Detail  
Abstr' with key attributes: research, methodolog, point, scientif, level, data, project, detector, detail, machin, view, deriv, mine, variou, pharmaceut, program, caus, result, experi, studi, analyz and is connected with the nodes 1322, 1428 and it is classified as Neural_Networks, it is the target node. The node 2617 is a product titled 'Title: Predicting Ordinal Classes in ILP  
Abstract: This paper is devoted to the problem of learnin' with key attributes: predict, tree, class, way, start, ilp, genet, order, transform, relat, set, ordin, variou, learner, name, regress, mesh, structur, result, studi, discret and is connected with no other nodes and it is classified as Case_Based, it is not the target node.
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

- ID: 2539
- Title: Mining for Causes of Cancer: Machine Learning Experiments at Various Levels of Detail
- True class (canonical `y`): **Rule_Learning**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Rule_Learning**
- Prediction recorded by this method's pipeline: **Rule_Learning**

Canonical text (`raw_text`):

~~~~~~text
Title: Mining for Causes of Cancer: Machine Learning Experiments at Various Levels of Detail  
Abstract: This paper presents first results of an interdisciplinary project in scientific data mining. We analyze data about the carcinogenicity of chemicals derived from the carcinogenesis bioassay program performed by the US National Institute of Environmental Health Sciences. The database contains detailed descriptions of 6823 tests performed with more than 330 compounds and animals of different species, strains and sexes. The chemical structures are described at the atom and bond level, and in terms of various relevant structural properties. The goal of this paper is to investigate the effects that various levels of detail and amounts of information have on the resulting hypotheses, both quantitatively and qualitatively. We apply relational and propositional machine learning algorithms to learning problems formulated as regression or as classification tasks. In addition, these experiments have been conducted with two learning problems which are at different levels of detail. Quantitatively, our experiments indicate that additional information not necessarily improves accuracy. Qualitatively, a number of potential discoveries have been made by the algorithm for Relational Regression because it can utilize all the information contained in the relations of the database as well as in the numerical dependent variable. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 3 nodes

| node id | true class | title |
|---|---|---|
| 1322 | Theory | Theory and Applications of Agnostic PAC-Learning with Small Decision Trees |
| 1428 | Rule_Learning | Inverse entailment and Progol |
| 2213 | Rule_Learning | Generating Declarative Language Bias for Top-Down ILP Algorithms |

### 2-hop (shortest distance exactly 2): 16 nodes

| node id | true class | title |
|---|---|---|
| 323 | Theory | Learning Active Classifiers |
| 1020 | Probabilistic_Methods | Error-Based and Entropy-Based Discretization of Continuous Features |
| 1027 | Theory | Pessimistic decision tree pruning based on tree size |
| 1259 | Rule_Learning | Finding Accurate Frontiers: A Knowledge-Intensive Approach to Relational Learning |
| 1312 | Rule_Learning | Learning Trees and Rules with Set-valued Features |
| 1601 | Neural_Networks | Learning the Past Tense of English Verbs: The Symbolic Pattern Associator vs. Connectionist Models |
| 1622 | Rule_Learning | Stochastic Propositionalization of Non-Determinate Background Knowledge |
| 2079 | Rule_Learning | Extraction of Meta-Knowledge to Restrict the Hypothesis Space for ILP Systems incorporating them in FOIL. |
| 2126 | Rule_Learning | Applying ILP to Diterpene Structure Elucidation from 13 C NMR Spectra |
| 2229 | Rule_Learning | Bottom-up induction of logic programs with more than one recursive clause |
| 2253 | Rule_Learning | Top-down Induction of Logical Decision Trees |
| 2290 | Rule_Learning | A Comparison of Pruning Methods for Relational Concept Learning |
| 2329 | Theory | Programming Research Group A LEARNABILITY MODEL FOR UNIVERSAL REPRESENTATIONS |
| 2424 | Rule_Learning | Which Hypotheses Can Be Found with Inverse Entailment? -Extended Abstract |
| 2493 | Rule_Learning | Relational Knowledge Discovery in Databases |
| 2617 | Rule_Learning | Predicting Ordinal Classes in ILP |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/cora/cf-gnnexplainer-canonical/random_seed_42_*` (key=498).

- Factual class: **Rule_Learning**
- Counterfactual class: **Neural_Networks**
- Removed edges (global ids, 10): (1020, 1322), (1027, 1322), (1322, 1622), (1428, 1622), (1428, 2079), (1428, 2229), (1428, 2424), (1428, 2493), (1428, 2617), (2213, 2539)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 2539 |
| Factual_Target_Node_Neighbors | 1322, 1428, 2213 |
| Factual_Target_Node_Features | research, methodolog, point, scientif, level, data, project, detector, detail, machin, view, deriv, mine, variou, pharmaceut, program, caus, result, result, result, experi, studi, analyz |
| Counterfactual_Target_Node_Neighbors | 1322, 1428 |
| Counterfactual_Target_Node_Features | research, methodolog, point, scientif, level, data, project, detector, detail, machin, view, deriv, mine, variou, pharmaceut, program, caus, result, result, result, experi, studi, analyz |
| Factual_Target_Node_Class | Rule_Learning |
| Counterfactual_Target_Node_class | Neural_Networks |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 2213 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 2539 |
| Factual_Target_Node_Neighbors | 1322, 1428, 2213 |
| Factual_Target_Node_Features | research, methodolog, point, scientif, level, data, project, detector, detail, machin, view, deriv, mine, variou, pharmaceut, program, caus, result, result, result, experi, studi, analyz |
| Counterfactual_Target_Node_Neighbors | 1322, 1428 |
| Counterfactual_Target_Node_Features | research, methodolog, point, scientif, level, data, project, detector, detail, machin, view, deriv, mine, variou, pharmaceut, program, caus, result, result, result, experi, studi, analyz |
| Factual_Target_Node_Class | Rule_Learning |
| Counterfactual_Target_Node_class | Neural_Networks |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 2213 |
| Natural_Language_Explanation | None |
