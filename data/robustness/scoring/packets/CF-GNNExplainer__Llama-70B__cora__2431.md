# Reference packet: CF-GNNExplainer__Llama-70B__cora__2431

- Method: CF-GNNExplainer; configuration: Llama-70B; dataset: cora; target node: 2431
- Explanation source: `./robustness_2026-10-30/llama70b/cf/cora/2431.json` (response)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, the target node is node 2431, which is classified as Theory in the factual graph but has a different classification in the counterfactual graph.

To fill the dictionary, we need to identify the changes in the graph structure and node features that led to the change in classification.

infos = {
    'Target_Node_ID': 2431,
    'Factual_Target_Node_Neighbors': [426],
    'Factual_Target_Node_Features': ['extend', 'practic', 'address', 'handl', 'valu', 'thu', 'rule', 'ilp', 'mostli', 'import', 'tri', 'machin', 'learner', 'real', 'system', 'result', 'xof', 'compar', 'applic', 'discret'],
    'Counterfactual_Target_Node_Neighbors': [426],
    'Counterfactual_Target_Node_Features': ['extend', 'practic', 'address', 'handl', 'valu', 'thu', 'rule', 'ilp', 'mostli', 'import', 'tri', 'machin', 'learner', 'real', 'system', 'result', 'xof', 'compar', 'applic', 'discret'],
    'Factual_Target_Node_Class': 'Theory',
    'Counterfactual_Target_Node_class': 'Rule_Learning',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Node_Differences': [2431],
    'Edge_Differences': [(2431, 426)],
    'Natural_Language_Explanation': ''
}

The natural language explanation for the change in classification is:

"The target node 2431 was initially classified as Theory, but after analyzing the graph structure and node features, it was found that the node's features are more closely related to Rule_Learning. The node's neighbors, particularly node 426, which is classified as Rule_Learning, had a significant influence on the reclassification. The node's features, such as 'rule', 'ilp', and 'machin', are more characteristic of Rule_Learning than Theory. Therefore, the target node 2431 is reclassified as Rule_Learning."

Note that the 'Node_Differences' and 'Edge_Differences' fields only contain the target node ID and its connection to node 426, respectively, since the counterfactual graph does not provide any additional information about changes in the graph structure or node features.
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
given the factual graph: The node 29 is a product titled 'Title: Stochastically Guided Disjunctive Version Space Learning  
Abstract: This paper presents an i' with key attributes: descript, increment, space, overlap, address, disjunct, guid, genet, tradit, induct, main, idea, accuraci, mani, result, multipl, version, central, concept, stochast, high and is connected with the node 426 and it is classified as Rule_Learning, it is not the target node. The node 303 is a product titled 'Title: Relating Relational Learning Algorithms  
Abstract: Relational learning algorithms are of spe' with key attributes: extend, involv, practic, issu, solv, address, genet, explor, offer, relat, comprehens, machin, member, special, represent, task, result, interest, supervis, method, current and is connected with the node 426 and it is classified as Case_Based, it is not the target node. The node 318 is a product titled 'Title: Generalizing from Case Studies: A Case Study  
Abstract: Most empirical evaluations of machin' with key attributes: empir, pattern, hypothes, genet, explicitli, case, machin, significantli, evalu, better, result, suggest, multipl, perform, databas, gener, studi, author and is connected with the nodes 426, 2427 and it is classified as Case_Based, it is not the target node. The node 335 is a product titled 'Title: Incremental Reduced Error Pruning  
Abstract: This paper outlines some problems that may occu' with key attributes: domain, reduc, increment, address, prune, noisi, genet, effici, relat, mani, propos, error, result, thereaft, occur, attempt, experi, method, may and is connected with the nodes 344, 426 and it is classified as Rule_Learning, it is not the target node. The node 344 is a product titled 'Title: Quinlan, 1990 J.R. Quinlan. Learning logical definitions from relations. Machine Learning, Fi' with key attributes: relat, machin, amplif, logic, mesh, revis, definit, result, theori and is connected with the nodes 335, 1007, 1275, 2426 and it is classified as Rule_Learning, it is not the target node. The node 426 is a product titled 'Title: Rule Induction with CN2: Some Recent Improvements  
Abstract: The CN2 algorithm induces an or' with key attributes: function, estim, short, list, rule, induc, altern, genet, entropi, classif, order, exampl, heurist, induct, describ, evalu, search, error, result, improv and is connected with the nodes 29, 303, 318, 335, 836, 937, 1061, 1187, 1275, 1486, 1528, 1576, 2126, 2369, 2431 and it is classified as Rule_Learning, it is not the target node. The node 638 is a product titled 'Title: Learning a set of primitive actions with an Induction of decision trees. Machine Learning, 1(' with key attributes: comprehens, chang, tree, refin, rule, machin, induct, decis, theori and is connected with the nodes 1919, 2426 and it is classified as Rule_Learning, it is not the target node. The node 836 is a product titled 'Title: Unsupervised Constructive Learning  
Abstract: In constructive induction (CI), the learner's' with key attributes: initi, normal, allow, backtrack, induct, distinct, modifi, unsupervis, part, process, propos, represent, result, model, clean, construct, theoret, argu, method and is connected with the node 426 and it is classified as Theory, it is not the target node. The node 937 is a product titled 'Title: The RISE System: Conquering Without Separating  
Abstract: Current rule induction systems (e.' with key attributes: avail, affect, rule, reli, separ, rise, success, typic, exampl, induct, system, result, strategi, explanatori, instanc, current and is connected with the node 426 and it is classified as Case_Based, it is not the target node. The node 1007 is a product titled 'Title: Applications of a logical discovery engine  
Abstract: The clausal discovery engine claudien' with key attributes: paradigm, space, discov, declar, data, mean, order, engin, induct, discoveri, logic, regular, program, larger, search, theori, applic, repres and is connected with the nodes 344, 1919, 2426 and it is classified as Rule_Learning, it is not the target node. The node 1061 is a product titled 'Title: Stochastic search in inductive concept learning  
Abstract: Concept learning can be viewed as' with key attributes: descript, space, hypothesi, genet, standard, view, determin, induct, local, oper, languag, structur, search, result, perform, concept, stochast and is connected with the node 426 and it is classified as Rule_Learning, it is not the target node. The node 1187 is a product titled 'Title: Rationality and Intelligence  
Abstract: Design and Evaluation of the RISE 1.0 Learning Syste' with key attributes: august, rise, system, evalu, design, technic, report, result and is connected with the node 426 and it is classified as Theory, it is not the target node. The node 1275 is a product titled 'Title: Fossil: A Robust Relational Learner  
Abstract: The research reported in this paper describes' with key attributes: extend, research, simpl, independ, properti, criterion, robust, ilp, natur, statist, power, relat, heurist, discuss, learner, train, system, shown, describ, search, result, report, interest, correl, base, sever and is connected with the nodes 344, 426 and it is classified as Rule_Learning, it is not the target node. The node 1486 is a product titled 'Title: Induction of decision trees and Bayesian classification applied to diagnosis of sport injurie' with key attributes: tree, diagnosi, genet, appli, store, data, classif, medic, extract, machin, induct, variou, decis, diagnost, techniqu, support, bayesian, result, databas, applic, knowledg and is connected with the node 426 and it is classified as Case_Based, it is not the target node. The node 1528 is a product titled 'Title: Using Qualitative Models to Guide Inductive Learning  
Abstract: This paper presents a method' with key attributes: domain, reduc, explain, accur, qualit, rule, guid, induc, respect, object, time, induct, process, result, model, method, instanc, exploit, knowledg and is connected with the node 426 and it is classified as Theory, it is not the target node. The node 1576 is a product titled 'Title: What do Constructive Learners Really Learn?  
Abstract: In constructive induction (CI), the l' with key attributes: initi, appear, highli, necessari, normal, backtrack, induct, distinct, modifi, learner, part, process, represent, result, construct, method, may, convent, howev, sever and is connected with the node 426 and it is classified as Theory, it is not the target node. The node 1686 is a product titled 'Title: Learning with Abduction  
Abstract: We investigate how abduction and induction can be integra' with key attributes: entail, extens, target, ilp, background, notion, common, integr, case, abduct, induct, investig, logic, program, result, framework, concept, theori and is connected with the nodes 2282, 2426 and it is classified as Rule_Learning, it is not the target node. The node 1919 is a product titled 'Title: Inductive Constraint Logic and the Mutagenesis Problem  
Abstract: A novel approach to learni' with key attributes: neg, target, formula, wherea, order, novel, exampl, view, induct, name, logic, posit, true, incorpor, constraint, system, interpret, result, theori and is connected with the nodes 638, 1007, 2426, 2431 and it is classified as Rule_Learning, it is not the target node. The node 2126 is a product titled 'Title: Applying ILP to Diterpene Structure Elucidation from 13 C NMR Spectra  
Abstract: We present' with key attributes: weight, low, ilp, appli, novel, comprehens, carbon, pharmaceut, structur, signific, organ, commerci, interest, base, applic, molecular and is connected with the nodes 426, 2426, 2591 and it is classified as Rule_Learning, it is not the target node. The node 2253 is a product titled 'Title: Top-down Induction of Logical Decision Trees  
Abstract: A first order framework for top-down' with key attributes: introduct, tree, popular, relat, top, machin, induct, decis, contribut, main, logic, program, proposit, techniqu, result, recent, compar and is connected with the node 2591 and it is classified as Rule_Learning, it is not the target node. The node 2282 is a product titled 'Title: The ILP description learning problem: Towards a general model-level definition of data mining' with key attributes: research, ed, descript, workshop, group, discov, ilp, data, machin, mine, special, report, definit, task, result, interest, gener and is connected with the nodes 1686, 2426 and it is classified as Rule_Learning, it is not the target node. The node 2369 is a product titled 'Title: Case-Based Sonogram Classification  
Abstract: This report replicates and extends results rep' with key attributes: extend, reason, empir, analys, imag, classif, center, novel, comprehens, cbr, standard, air, system, result, obtain, report, automat, compar, studi and is connected with the node 426 and it is classified as Case_Based, it is not the target node. The node 2426 is a product titled 'Title: Inductive Constraint Logic  
Abstract: A novel approach to learning first order logic formula' with key attributes: neg, target, formula, fact, wherea, order, novel, exampl, view, induct, ground, employ, logic, posit, true, claus, constraint, system, interpret, program, result, theori and is connected with the nodes 344, 638, 1007, 1686, 1919, 2126, 2282, 2431, 2493 and it is classified as Rule_Learning, it is not the target node. The node 2427 is a product titled 'Title: Solving the Multiple-Instance Problem with Axis-Parallel Rectangles  
Abstract: The multiple' with key attributes: vector, solv, instanc, altern, object, classif, featur, respons, exampl, observ, train, singl, mani, describ, result, multipl, task, aris, may and is connected with the nodes 318, 2591 and it is classified as Theory, it is not the target node. The node 2431 is a product titled 'Title: Multi-class problems and discretization in ICL Extended abstract  
Abstract: Handling multi-c' with key attributes: extend, practic, address, handl, valu, thu, rule, ilp, mostli, import, tri, machin, learner, real, system, result, xof, compar, applic, discret and is connected with the nodes 426, 1919, 2426, 2591 and it is classified as Rule_Learning, it is the target node. The node 2493 is a product titled 'Title: Relational Knowledge Discovery in Databases  
Abstract: In this paper, we indicate some possi' with key attributes: pure, link, indic, similar, possibl, ilp, relat, discuss, adapt, discoveri, system, propos, techniqu, result, rang, databas, field, base, method, applic, knowledg, sever and is connected with the node 2426 and it is classified as Rule_Learning, it is not the target node. The node 2591 is a product titled 'Title: Lookahead and Discretization in ILP  
Abstract: We present and evaluate two methods for impro' with key attributes: extend, numer, way, second, aspect, attribut, ilp, relat, adapt, system, evalu, improv, occur, result, perform, base, method, instanc, discret and is connected with the nodes 2126, 2253, 2427, 2431 and it is classified as Rule_Learning, it is not the target node. and given the counterfactual example: The node 29 is a product titled 'Title: Stochastically Guided Disjunctive Version Space Learning  
Abstract: This paper presents an i' with key attributes: descript, increment, space, overlap, address, disjunct, guid, genet, tradit, induct, main, idea, accuraci, mani, result, multipl, version, central, concept, stochast, high and is connected with the node 426 and it is classified as Rule_Learning, it is not the target node. The node 303 is a product titled 'Title: Relating Relational Learning Algorithms  
Abstract: Relational learning algorithms are of spe' with key attributes: extend, involv, practic, issu, solv, address, genet, explor, offer, relat, comprehens, machin, member, special, represent, task, result, interest, supervis, method, current and is connected with the node 426 and it is classified as Case_Based, it is not the target node. The node 318 is a product titled 'Title: Generalizing from Case Studies: A Case Study  
Abstract: Most empirical evaluations of machin' with key attributes: empir, pattern, hypothes, genet, explicitli, case, machin, significantli, evalu, better, result, suggest, multipl, perform, databas, gener, studi, author and is connected with the nodes 426, 2427 and it is classified as Case_Based, it is not the target node. The node 335 is a product titled 'Title: Incremental Reduced Error Pruning  
Abstract: This paper outlines some problems that may occu' with key attributes: domain, reduc, increment, address, prune, noisi, genet, effici, relat, mani, propos, error, result, thereaft, occur, attempt, experi, method, may and is connected with the nodes 344, 426 and it is classified as Rule_Learning, it is not the target node. The node 344 is a product titled 'Title: Quinlan, 1990 J.R. Quinlan. Learning logical definitions from relations. Machine Learning, Fi' with key attributes: relat, machin, amplif, logic, mesh, revis, definit, result, theori and is connected with the nodes 335, 1007, 1275, 2426 and it is classified as Rule_Learning, it is not the target node. The node 426 is a product titled 'Title: Rule Induction with CN2: Some Recent Improvements  
Abstract: The CN2 algorithm induces an or' with key attributes: function, estim, short, list, rule, induc, altern, genet, entropi, classif, order, exampl, heurist, induct, describ, evalu, search, error, result, improv and is connected with the nodes 29, 303, 318, 335, 836, 937, 1187, 1486, 1528, 1576, 2369, 2431 and it is classified as Rule_Learning, it is not the target node. The node 638 is a product titled 'Title: Learning a set of primitive actions with an Induction of decision trees. Machine Learning, 1(' with key attributes: comprehens, chang, tree, refin, rule, machin, induct, decis, theori and is connected with the nodes 1919, 2426 and it is classified as Rule_Learning, it is not the target node. The node 836 is a product titled 'Title: Unsupervised Constructive Learning  
Abstract: In constructive induction (CI), the learner's' with key attributes: initi, normal, allow, backtrack, induct, distinct, modifi, unsupervis, part, process, propos, represent, result, model, clean, construct, theoret, argu, method and is connected with the node 426 and it is classified as Theory, it is not the target node. The node 937 is a product titled 'Title: The RISE System: Conquering Without Separating  
Abstract: Current rule induction systems (e.' with key attributes: avail, affect, rule, reli, separ, rise, success, typic, exampl, induct, system, result, strategi, explanatori, instanc, current and is connected with the node 426 and it is classified as Case_Based, it is not the target node. The node 1007 is a product titled 'Title: Applications of a logical discovery engine  
Abstract: The clausal discovery engine claudien' with key attributes: paradigm, space, discov, declar, data, mean, order, engin, induct, discoveri, logic, regular, program, larger, search, theori, applic, repres and is connected with the nodes 344, 1919, 2426 and it is classified as Rule_Learning, it is not the target node. The node 1061 is a product titled 'Title: Stochastic search in inductive concept learning  
Abstract: Concept learning can be viewed as' with key attributes: descript, space, hypothesi, genet, standard, view, determin, induct, local, oper, languag, structur, search, result, perform, concept, stochast and is connected with no other nodes and it is classified as Rule_Learning, it is not the target node. The node 1187 is a product titled 'Title: Rationality and Intelligence  
Abstract: Design and Evaluation of the RISE 1.0 Learning Syste' with key attributes: august, rise, system, evalu, design, technic, report, result and is connected with the node 426 and it is classified as Theory, it is not the target node. The node 1275 is a product titled 'Title: Fossil: A Robust Relational Learner  
Abstract: The research reported in this paper describes' with key attributes: extend, research, simpl, independ, properti, criterion, robust, ilp, natur, statist, power, relat, heurist, discuss, learner, train, system, shown, describ, search, result, report, interest, correl, base, sever and is connected with the node 344 and it is classified as Rule_Learning, it is not the target node. The node 1486 is a product titled 'Title: Induction of decision trees and Bayesian classification applied to diagnosis of sport injurie' with key attributes: tree, diagnosi, genet, appli, store, data, classif, medic, extract, machin, induct, variou, decis, diagnost, techniqu, support, bayesian, result, databas, applic, knowledg and is connected with the node 426 and it is classified as Case_Based, it is not the target node. The node 1528 is a product titled 'Title: Using Qualitative Models to Guide Inductive Learning  
Abstract: This paper presents a method' with key attributes: domain, reduc, explain, accur, qualit, rule, guid, induc, respect, object, time, induct, process, result, model, method, instanc, exploit, knowledg and is connected with the node 426 and it is classified as Theory, it is not the target node. The node 1576 is a product titled 'Title: What do Constructive Learners Really Learn?  
Abstract: In constructive induction (CI), the l' with key attributes: initi, appear, highli, necessari, normal, backtrack, induct, distinct, modifi, learner, part, process, represent, result, construct, method, may, convent, howev, sever and is connected with the node 426 and it is classified as Theory, it is not the target node. The node 1686 is a product titled 'Title: Learning with Abduction  
Abstract: We investigate how abduction and induction can be integra' with key attributes: entail, extens, target, ilp, background, notion, common, integr, case, abduct, induct, investig, logic, program, result, framework, concept, theori and is connected with the nodes 2282, 2426 and it is classified as Rule_Learning, it is not the target node. The node 1919 is a product titled 'Title: Inductive Constraint Logic and the Mutagenesis Problem  
Abstract: A novel approach to learni' with key attributes: neg, target, formula, wherea, order, novel, exampl, view, induct, name, logic, posit, true, incorpor, constraint, system, interpret, result, theori and is connected with the nodes 638, 1007, 2426 and it is classified as Rule_Learning, it is not the target node. The node 2126 is a product titled 'Title: Applying ILP to Diterpene Structure Elucidation from 13 C NMR Spectra  
Abstract: We present' with key attributes: weight, low, ilp, appli, novel, comprehens, carbon, pharmaceut, structur, signific, organ, commerci, interest, base, applic, molecular and is connected with the nodes 2426, 2591 and it is classified as Rule_Learning, it is not the target node. The node 2253 is a product titled 'Title: Top-down Induction of Logical Decision Trees  
Abstract: A first order framework for top-down' with key attributes: introduct, tree, popular, relat, top, machin, induct, decis, contribut, main, logic, program, proposit, techniqu, result, recent, compar and is connected with the node 2591 and it is classified as Rule_Learning, it is not the target node. The node 2282 is a product titled 'Title: The ILP description learning problem: Towards a general model-level definition of data mining' with key attributes: research, ed, descript, workshop, group, discov, ilp, data, machin, mine, special, report, definit, task, result, interest, gener and is connected with the nodes 1686, 2426 and it is classified as Rule_Learning, it is not the target node. The node 2369 is a product titled 'Title: Case-Based Sonogram Classification  
Abstract: This report replicates and extends results rep' with key attributes: extend, reason, empir, analys, imag, classif, center, novel, comprehens, cbr, standard, air, system, result, obtain, report, automat, compar, studi and is connected with the node 426 and it is classified as Case_Based, it is not the target node. The node 2426 is a product titled 'Title: Inductive Constraint Logic  
Abstract: A novel approach to learning first order logic formula' with key attributes: neg, target, formula, fact, wherea, order, novel, exampl, view, induct, ground, employ, logic, posit, true, claus, constraint, system, interpret, program, result, theori and is connected with the nodes 344, 638, 1007, 1686, 1919, 2126, 2282, 2493 and it is classified as Rule_Learning, it is not the target node. The node 2427 is a product titled 'Title: Solving the Multiple-Instance Problem with Axis-Parallel Rectangles  
Abstract: The multiple' with key attributes: vector, solv, instanc, altern, object, classif, featur, respons, exampl, observ, train, singl, mani, describ, result, multipl, task, aris, may and is connected with the nodes 318, 2591 and it is classified as Theory, it is not the target node. The node 2431 is a product titled 'Title: Multi-class problems and discretization in ICL Extended abstract  
Abstract: Handling multi-c' with key attributes: extend, practic, address, handl, valu, thu, rule, ilp, mostli, import, tri, machin, learner, real, system, result, xof, compar, applic, discret and is connected with the node 426 and it is classified as Theory, it is the target node. The node 2493 is a product titled 'Title: Relational Knowledge Discovery in Databases  
Abstract: In this paper, we indicate some possi' with key attributes: pure, link, indic, similar, possibl, ilp, relat, discuss, adapt, discoveri, system, propos, techniqu, result, rang, databas, field, base, method, applic, knowledg, sever and is connected with the node 2426 and it is classified as Rule_Learning, it is not the target node. The node 2591 is a product titled 'Title: Lookahead and Discretization in ILP  
Abstract: We present and evaluate two methods for impro' with key attributes: extend, numer, way, second, aspect, attribut, ilp, relat, adapt, system, evalu, improv, occur, result, perform, base, method, instanc, discret and is connected with the nodes 2126, 2253, 2427 and it is classified as Rule_Learning, it is not the target node.
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

- ID: 2431
- Title: Multi-class problems and discretization in ICL Extended abstract
- True class (canonical `y`): **Rule_Learning**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Rule_Learning**
- Prediction recorded by this method's pipeline: **Rule_Learning**

Canonical text (`raw_text`):

~~~~~~text
Title: Multi-class problems and discretization in ICL Extended abstract  
Abstract: Handling multi-class problems and real numbers is important in practical applications of machine learning to KDD problems. While attribute-value learners address these problems as a rule, very few ILP systems do so. The few ILP systems that handle real numbers mostly do so by trying out all real values that are applicable, thus running into efficiency or overfitting problems. This paper discusses some recent extensions of ICL that address these problems. ICL, which stands for Inductive Constraint Logic, is an ILP system that learns first order logic formulae from positive and negative examples. The main charateristic of ICL is its view on examples. These are seen as interpretations which are true or false for the clausal target theory (in CNF). We first argue that ICL can be used for learning a theory in a disjunctive normal form (DNF). With this in mind, a possible solution for handling more than two classes is given (based on some ideas from CN2). Finally, we show how to tackle problems with continuous values by adapting discretization techniques from attribute value learners. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 4 nodes

| node id | true class | title |
|---|---|---|
| 426 | Rule_Learning | Rule Induction with CN2: Some Recent Improvements |
| 1919 | Rule_Learning | Inductive Constraint Logic and the Mutagenesis Problem |
| 2426 | Rule_Learning | Inductive Constraint Logic |
| 2591 | Rule_Learning | Lookahead and Discretization in ILP |

### 2-hop (shortest distance exactly 2): 22 nodes

| node id | true class | title |
|---|---|---|
| 29 | Rule_Learning | Stochastically Guided Disjunctive Version Space Learning |
| 303 | Case_Based | Relating Relational Learning Algorithms |
| 318 | Case_Based | Generalizing from Case Studies: A Case Study |
| 335 | Rule_Learning | Incremental Reduced Error Pruning |
| 344 | Rule_Learning | Quinlan, 1990 J.R. Quinlan. Learning logical definitions from relations. Machine Learning, First-order theory revision. In |
| 638 | Theory | Learning a set of primitive actions with an Induction of decision trees. Machine Learning, 1(1):81-106, |
| 836 | Theory | Unsupervised Constructive Learning |
| 937 | Case_Based | The RISE System: Conquering Without Separating |
| 1007 | Rule_Learning | Applications of a logical discovery engine |
| 1061 | Rule_Learning | Stochastic search in inductive concept learning |
| 1187 | Theory | Rationality and Intelligence |
| 1275 | Rule_Learning | Fossil: A Robust Relational Learner |
| 1486 | Rule_Learning | Induction of decision trees and Bayesian classification applied to diagnosis of sport injuries |
| 1528 | Rule_Learning | Using Qualitative Models to Guide Inductive Learning |
| 1576 | Theory | What do Constructive Learners Really Learn? |
| 1686 | Rule_Learning | Learning with Abduction |
| 2126 | Rule_Learning | Applying ILP to Diterpene Structure Elucidation from 13 C NMR Spectra |
| 2253 | Rule_Learning | Top-down Induction of Logical Decision Trees |
| 2282 | Rule_Learning | The ILP description learning problem: Towards a general model-level definition of data mining in ILP |
| 2369 | Case_Based | Case-Based Sonogram Classification |
| 2427 | Neural_Networks | Solving the Multiple-Instance Problem with Axis-Parallel Rectangles |
| 2493 | Rule_Learning | Relational Knowledge Discovery in Databases |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/cora/cf-gnnexplainer-canonical/random_seed_42_*` (key=476).

- Factual class: **Rule_Learning**
- Counterfactual class: **Theory**
- Removed edges (global ids, 6): (426, 1061), (426, 1275), (426, 2126), (1919, 2431), (2426, 2431), (2431, 2591)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 2431 |
| Factual_Target_Node_Neighbors | 426, 1919, 2426, 2591 |
| Factual_Target_Node_Features | extend, practic, address, handl, valu, thu, rule, ilp, mostli, import, tri, machin, learner, real, system, result, xof, compar, applic, discret |
| Counterfactual_Target_Node_Neighbors | 426 |
| Counterfactual_Target_Node_Features | extend, practic, address, handl, valu, thu, rule, ilp, mostli, import, tri, machin, learner, real, system, result, xof, compar, applic, discret |
| Factual_Target_Node_Class | Rule_Learning |
| Counterfactual_Target_Node_class | Theory |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 1919, 2426, 2591 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 2431 |
| Factual_Target_Node_Neighbors | 426, 1919, 2426, 2591 |
| Factual_Target_Node_Features | extend, practic, address, handl, valu, thu, rule, ilp, mostli, import, tri, machin, learner, real, system, result, xof, compar, applic, discret |
| Counterfactual_Target_Node_Neighbors | 426 |
| Counterfactual_Target_Node_Features | extend, practic, address, handl, valu, thu, rule, ilp, mostli, import, tri, machin, learner, real, system, result, xof, compar, applic, discret |
| Factual_Target_Node_Class | Rule_Learning |
| Counterfactual_Target_Node_class | Theory |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 1919, 2426, 2591 |
| Natural_Language_Explanation | None |
