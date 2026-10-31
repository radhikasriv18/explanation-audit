# Reference packet: CF-GNNExplainer__Qwen-14B__cora__2334

- Method: CF-GNNExplainer; configuration: Qwen-14B; dataset: cora; target node: 2334
- Explanation source: `./robustness_2026-10-30/production_a100/qwen14b_gptq_int4_cora_Response.json` ([463][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
To address the provided scenario, we will first identify the differences between the factual and counterfactual examples, focusing on the target node (node 2334). We will then analyze the changes in its classification and the influence of its neighboring nodes.

### Factual Example Analysis

In the factual graph, node 2334 is titled "New Methods for Competitive Coevolution" and is classified as Genetic_Algorithms. It is connected to several nodes, including 54, 209, 602, 1588, 1790, 1832, 1836, 1917, 2103, 2332, and 2353.

### Counterfactual Example Analysis

In the counterfactual graph, node 2334 retains the same title but is reclassified as Theory. Its connections have changed slightly, now only connecting to nodes 54 and 2332.

### Differences Identification

#### Node Differences
- **Node ID:** 2334
- **Factual Classification:** Genetic_Algorithms
- **Counterfactual Classification:** Theory

#### Edge Differences
- **Factual Connections:** [54, 209, 602, 1588, 1790, 1832, 1836, 1917, 2103, 2332, 2353]
- **Counterfactual Connections:** [54, 2332]

### Filling the Dictionary

Based on the analysis, we can fill the `infos` dictionary as follows:

```python
infos = {
    'Target_Node_ID': 2334,
    'Factual_Target_Node_Neighbors': [54, 209, 602, 1588, 1790, 1832, 1836, 1917, 2103, 2332, 2353],
    'Factual_Target_Node_Features': ['fit', 'independ', 'evolv', 'popul', 'level', 'increas', 'drive', 'coevolut', 'competit', 'anoth', 'complex', 'individu', 'direct', 'lead', 'arm', 'consid', 'perform', 'race', 'base', 'select', 'method'],
    'Counterfactual_Target_Node_Neighbors': [54, 2332],
    'Counterfactual_Target_Node_Features': ['fit', 'independ', 'evolv', 'popul', 'level', 'increas', 'drive', 'coevolut', 'competit', 'anoth', 'complex', 'individu', 'direct', 'lead', 'arm', 'consid', 'perform', 'race', 'base', 'select', 'method'],
    'Factual_Target_Node_Class': 'Genetic_Algorithms',
    'Counterfactual_Target_Node_class': 'Theory',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Natural_Language_Explanation': 'Node 2334 was originally classified as Genetic_Algorithms and was connected to multiple nodes. In the counterfactual scenario, it is reclassified as Theory and only connected to nodes 54 and 2332. This change suggests that the context and connectivity of node 2334 influenced its classification.'
}
```

### Explanation of Changes

The primary difference lies in the classification of node 2334. In the factual graph, it is classified as Genetic_Algorithms, indicating its relevance to optimization and search algorithms inspired by natural selection and genetics. However, in the counterfactual graph, it is reclassified as Theory, suggesting a shift towards theoretical studies and foundational aspects of machine learning.

This reclassification can be attributed to the reduced connectivity and the nature of the remaining connected nodes. Specifically, node 54, which is connected in both scenarios, is classified as Theory, implying a strong influence on the classification of node 2334. Additionally, node 2332, which is connected in the counterfactual scenario, is also classified as Genetic_Algorithms, but its influence seems less dominant compared to the broader context of the original connections.

Thus, the minimal change in connectivity from multiple nodes to just two nodes, particularly with one being classified as Theory, significantly alters the classification of node 2334 from Genetic_Algorithms to Theory. This highlights the importance of the neighborhood structure and the classification of neighboring nodes in determining the overall classification of a node within a graph-based learning model.
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
Abstract: An ap' with key attributes: network, evolutionari, discov, evolut, artifici, standard, neural, play, complex, direct, program, search, develop, game, strategi, seattl, base and is connected with the nodes 163, 1790 and it is classified as Genetic_Algorithms, it is not the target node. The node 54 is a product titled 'Title: A Competitive Approach to Game Learning  
Abstract: Machine learning of game strategies has o' with key attributes: genet, depend, machin, continu, competit, previou, compon, develop, repeat, game, strategi, capabl, recent, consid, definit, result, framework, compar, method and is connected with the nodes 523, 615, 712, 1687, 2334 and it is classified as Theory, it is not the target node. The node 55 is a product titled 'Title: A Comparison of Selection Schemes used in Genetic Algorithms  
Abstract: TIK-Report Nr. 11, D' with key attributes: edit, genet, comparison, version, select, scheme and is connected with the nodes 163, 1832 and it is classified as Genetic_Algorithms, it is not the target node. The node 163 is a product titled 'Title: 4 Implementing Application Specific Routines  Genetic algorithms in search, optimization, and' with key attributes: network, optim, evolutionari, acquisit, modul, artifici, genet, write, submit, concaten, ieee, neural, recurr, search, represent, life, technic, report, construct and is connected with the nodes 22, 55, 415, 523, 602, 1114, 1831 and it is classified as Genetic_Algorithms, it is not the target node. The node 209 is a product titled 'Title: 17 Massively Parallel Genetic Programming  
Abstract: As the field of Genetic Programming (GP' with key attributes: need, today, implement, necessari, genet, absolut, increas, massiv, system, chapter, program, propos, recent, becom, field, applic, parallel and is connected with the nodes 415, 2334, 2704 and it is classified as Genetic_Algorithms, it is not the target node. The node 415 is a product titled 'Title: Competitive Environments Evolve Better Solutions for Complex Tasks  
Abstract: University of' with key attributes: initi, evolv, competit, complex, mutat, solut, refer, better, task, method and is connected with the nodes 163, 209, 523, 712, 1790, 1832, 1836, 2103, 2353 and it is classified as Genetic_Algorithms, it is not the target node. The node 523 is a product titled 'Title: Some studies in machine learning using the game of checkers. IBM Journal, 3(3):211-229, 1959.' with key attributes: machin, journal, game, result, studi and is connected with the nodes 54, 163, 415, 565, 1687, 1790 and it is classified as Reinforcement_Learning, it is not the target node. The node 565 is a product titled 'Title: Machine Learning Learning to Predict by the Methods of Temporal Differences Keywords: Increme' with key attributes: predict, futur, past, increment, class, keyword, articl, behavior, wherea, machin, incomplet, system, special, procedur, result, tempor, experi, introduc, known, differ, method, convent and is connected with the nodes 523, 1790 and it is classified as Reinforcement_Learning, it is not the target node. The node 602 is a product titled 'Title: Every Niching Method has its Niche: Fitness Sharing and Implicit Sharing Compared  
Abstract:' with key attributes: fit, extens, space, share, genet, natur, nich, implicit, variou, mani, manag, search, contain, attempt, recent, rang, result, compar, everi, method, sever and is connected with the nodes 163, 1114, 2334 and it is classified as Genetic_Algorithms, it is not the target node. The node 615 is a product titled 'Title: Efficient Algorithms for Learning to Play Repeated Games Against Computationally Bounded Adve' with key attributes: research, optim, class, chosen, unknown, automata, genet, line, adversari, effici, play, contribut, finit, bound, surpris, repeat, game, result, studi and is connected with the node 54 and it is classified as Theory, it is not the target node. The node 712 is a product titled 'Title: Tracking the red queen: Measurements of adaptive progress in co-evolution ary simulations. In' with key attributes: fit, measur, interact, popul, simul, rise, read, give, nich, adapt, landscap, significantli, track, complic, effect, introduc, progress and is connected with the nodes 54, 415 and it is classified as Genetic_Algorithms, it is not the target node. The node 1114 is a product titled 'Title: Using Genetic Algorithms to Explore Pattern Recognition in the Immune System  COMMENTS WELCOM' with key attributes: place, pattern, level, string, genet, explor, take, understand, individu, speci, direct, process, system, binari, describ, recognit, model, result, comment, base, univers and is connected with the nodes 163, 602, 1117, 1588 and it is classified as Genetic_Algorithms, it is not the target node. The node 1117 is a product titled 'Title: A Coevolutionary Approach to Learning Sequential Decision Rules  
Abstract: We present a coev' with key attributes: independ, evolutionari, advantag, appear, evolv, stabl, rule, altern, simpler, format, complex, decis, sequenti, coevolutionari, direct, provid, result, control, repres and is connected with the nodes 1114, 1588, 2332 and it is classified as Genetic_Algorithms, it is not the target node. The node 1588 is a product titled 'Title: Automatic Modularization by Speciation  
Abstract: Real-world problems are often too difficul' with key attributes: network, reduc, solv, total, imag, artifici, natur, success, exampl, neural, complex, modular, world, process, singl, system, mani, speech, difficult, automat and is connected with the nodes 1114, 1117, 2334 and it is classified as Genetic_Algorithms, it is not the target node. The node 1687 is a product titled 'Title: Markov games as a framework for multi-agent reinforcement learning  
Abstract: In the Markov' with key attributes: agent, defin, function, interact, formal, environ, reinforc, mdp, markov, view, transit, decis, adapt, part, process, singl, probabilist, result, game, framework, instanc and is connected with the nodes 54, 523 and it is classified as Reinforcement_Learning, it is not the target node. The node 1790 is a product titled 'Title: Using Genetic Programming to Evolve Board Evaluation Functions  
Abstract: The purpose of mos' with key attributes: paradigm, function, enabl, evolv, genet, feasibl, comput, play, employ, program, evalu, result, formul, strategi, term and is connected with the nodes 22, 415, 523, 565, 2334 and it is classified as Genetic_Algorithms, it is not the target node. The node 1796 is a product titled 'Title: Evaluating and Improving Steady State Evolutionary Algorithms on Constraint Satisfaction Prob' with key attributes: evolutionari, state, satisfact, genet, constraint, evalu, improv and is connected with the node 1917 and it is classified as Genetic_Algorithms, it is not the target node. The node 1831 is a product titled 'Title: Some Training Subset Selection Methods for Supervised Learning in Genetic Programming  
Abstr' with key attributes: need, reduc, carri, popul, genet, set, case, size, subset, train, describ, program, evalu, result, difficult, larg, compar, select, supervis, method and is connected with the nodes 163, 1832, 1836 and it is classified as Genetic_Algorithms, it is not the target node. The node 1832 is a product titled 'Title: Tackling the Boolean Even N Parity Problem with Genetic Programming and Limited-Error Fitness' with key attributes: limit, fit, score, modif, asymmetr, remain, genet, order, set, standard, case, train, boolean, mani, program, error, result, base, supervis and is connected with the nodes 55, 415, 1831, 1836, 2334 and it is classified as Genetic_Algorithms, it is not the target node. The node 1836 is a product titled 'Title: Small Populations over Many Generations can beat Large Populations over Few Generations in Ge' with key attributes: resourc, literatur, appear, dynam, popul, possibl, genet, effici, subset, mani, requir, program, result, memori, larg, gener, small, select, look and is connected with the nodes 415, 1831, 1832, 2334 and it is classified as Genetic_Algorithms, it is not the target node. The node 1917 is a product titled 'Title: Go and Genetic Programming Playing Go with Filter Functions  
Abstract: A neural network mode' with key attributes: function, genet, play, program, filter and is connected with the nodes 1796, 2334 and it is classified as Genetic_Algorithms, it is not the target node. The node 2103 is a product titled 'Title: The Evolution of Communication Schemes Over Continuous Channels  
Abstract: As the field of G' with key attributes: need, today, implement, necessari, genet, absolut, architectur, increas, system, program, propos, recent, becom, field, applic, parallel and is connected with the nodes 415, 2334 and it is classified as Genetic_Algorithms, it is not the target node. The node 2332 is a product titled 'Title: Improved Hoeffding-Style Performance Guarantees for Accurate Classifiers  
Abstract: Evolving' with key attributes: cooper, solv, group, evolv, agent, genet, common, coordin, concurr, nich, distinct, sourc, complex, individu, system, requir, result, effect, multipl, run, preliminari, task, perform and is connected with the nodes 1117, 2334 and it is classified as Genetic_Algorithms, it is not the target node. The node 2334 is a product titled 'Title: New Methods for Competitive Coevolution  
Abstract: We consider "competitive coevolution," in' with key attributes: fit, independ, evolv, popul, level, increas, drive, coevolut, competit, anoth, complex, individu, direct, lead, arm, consid, perform, race, base, select, method and is connected with the nodes 54, 209, 602, 1588, 1790, 1832, 1836, 1917, 2103, 2332, 2353 and it is classified as Genetic_Algorithms, it is the target node. The node 2353 is a product titled 'Title: Dynamics of Co-evolutionary Learning  
Abstract: Co-evolutionary learning, which involves the' with key attributes: involv, agent, fit, dynam, artifici, environ, success, technolog, nich, adapt, solut, robot, mani, embed, result, progress, potenti, sever and is connected with the nodes 415, 2334 and it is classified as Genetic_Algorithms, it is not the target node. The node 2704 is a product titled 'Title: A Genome Compiler for High Performance Genetic Programming  
Abstract: Genetic Programming is' with key attributes: compil, desir, expens, possibl, genet, effici, time, machin, genom, major, individu, candid, solut, surpris, describ, program, evalu, perform, compar, high, applic and is connected with the node 209 and it is classified as Genetic_Algorithms, it is not the target node. and given the counterfactual example: The node 22 is a product titled 'Title: Discovering Complex Othello Strategies Through Evolutionary Neural Networks  
Abstract: An ap' with key attributes: network, evolutionari, discov, evolut, artifici, standard, neural, play, complex, direct, program, search, develop, game, strategi, seattl, base and is connected with the nodes 163, 1790 and it is classified as Genetic_Algorithms, it is not the target node. The node 54 is a product titled 'Title: A Competitive Approach to Game Learning  
Abstract: Machine learning of game strategies has o' with key attributes: genet, depend, machin, continu, competit, previou, compon, develop, repeat, game, strategi, capabl, recent, consid, definit, result, framework, compar, method and is connected with the nodes 523, 615, 712, 1687, 2334 and it is classified as Theory, it is not the target node. The node 55 is a product titled 'Title: A Comparison of Selection Schemes used in Genetic Algorithms  
Abstract: TIK-Report Nr. 11, D' with key attributes: edit, genet, comparison, version, select, scheme and is connected with the nodes 163, 1832 and it is classified as Genetic_Algorithms, it is not the target node. The node 163 is a product titled 'Title: 4 Implementing Application Specific Routines  Genetic algorithms in search, optimization, and' with key attributes: network, optim, evolutionari, acquisit, modul, artifici, genet, write, submit, concaten, ieee, neural, recurr, search, represent, life, technic, report, construct and is connected with the nodes 22, 55, 415, 523, 602, 1114, 1831 and it is classified as Genetic_Algorithms, it is not the target node. The node 209 is a product titled 'Title: 17 Massively Parallel Genetic Programming  
Abstract: As the field of Genetic Programming (GP' with key attributes: need, today, implement, necessari, genet, absolut, increas, massiv, system, chapter, program, propos, recent, becom, field, applic, parallel and is connected with the nodes 415, 2704 and it is classified as Genetic_Algorithms, it is not the target node. The node 415 is a product titled 'Title: Competitive Environments Evolve Better Solutions for Complex Tasks  
Abstract: University of' with key attributes: initi, evolv, competit, complex, mutat, solut, refer, better, task, method and is connected with the nodes 163, 209, 523, 712, 1790, 1832, 1836, 2103, 2353 and it is classified as Genetic_Algorithms, it is not the target node. The node 523 is a product titled 'Title: Some studies in machine learning using the game of checkers. IBM Journal, 3(3):211-229, 1959.' with key attributes: machin, journal, game, result, studi and is connected with the nodes 54, 163, 415, 565, 1687, 1790 and it is classified as Reinforcement_Learning, it is not the target node. The node 565 is a product titled 'Title: Machine Learning Learning to Predict by the Methods of Temporal Differences Keywords: Increme' with key attributes: predict, futur, past, increment, class, keyword, articl, behavior, wherea, machin, incomplet, system, special, procedur, result, tempor, experi, introduc, known, differ, method, convent and is connected with the nodes 523, 1790 and it is classified as Reinforcement_Learning, it is not the target node. The node 602 is a product titled 'Title: Every Niching Method has its Niche: Fitness Sharing and Implicit Sharing Compared  
Abstract:' with key attributes: fit, extens, space, share, genet, natur, nich, implicit, variou, mani, manag, search, contain, attempt, recent, rang, result, compar, everi, method, sever and is connected with the nodes 163, 1114 and it is classified as Genetic_Algorithms, it is not the target node. The node 615 is a product titled 'Title: Efficient Algorithms for Learning to Play Repeated Games Against Computationally Bounded Adve' with key attributes: research, optim, class, chosen, unknown, automata, genet, line, adversari, effici, play, contribut, finit, bound, surpris, repeat, game, result, studi and is connected with the node 54 and it is classified as Theory, it is not the target node. The node 712 is a product titled 'Title: Tracking the red queen: Measurements of adaptive progress in co-evolution ary simulations. In' with key attributes: fit, measur, interact, popul, simul, rise, read, give, nich, adapt, landscap, significantli, track, complic, effect, introduc, progress and is connected with the nodes 54, 415 and it is classified as Genetic_Algorithms, it is not the target node. The node 1114 is a product titled 'Title: Using Genetic Algorithms to Explore Pattern Recognition in the Immune System  COMMENTS WELCOM' with key attributes: place, pattern, level, string, genet, explor, take, understand, individu, speci, direct, process, system, binari, describ, recognit, model, result, comment, base, univers and is connected with the nodes 163, 602, 1117, 1588 and it is classified as Genetic_Algorithms, it is not the target node. The node 1117 is a product titled 'Title: A Coevolutionary Approach to Learning Sequential Decision Rules  
Abstract: We present a coev' with key attributes: independ, evolutionari, advantag, appear, evolv, stabl, rule, altern, simpler, format, complex, decis, sequenti, coevolutionari, direct, provid, result, control, repres and is connected with the nodes 1114, 1588, 2332 and it is classified as Genetic_Algorithms, it is not the target node. The node 1588 is a product titled 'Title: Automatic Modularization by Speciation  
Abstract: Real-world problems are often too difficul' with key attributes: network, reduc, solv, total, imag, artifici, natur, success, exampl, neural, complex, modular, world, process, singl, system, mani, speech, difficult, automat and is connected with the nodes 1114, 1117 and it is classified as Genetic_Algorithms, it is not the target node. The node 1687 is a product titled 'Title: Markov games as a framework for multi-agent reinforcement learning  
Abstract: In the Markov' with key attributes: agent, defin, function, interact, formal, environ, reinforc, mdp, markov, view, transit, decis, adapt, part, process, singl, probabilist, result, game, framework, instanc and is connected with the nodes 54, 523 and it is classified as Reinforcement_Learning, it is not the target node. The node 1790 is a product titled 'Title: Using Genetic Programming to Evolve Board Evaluation Functions  
Abstract: The purpose of mos' with key attributes: paradigm, function, enabl, evolv, genet, feasibl, comput, play, employ, program, evalu, result, formul, strategi, term and is connected with the nodes 22, 415, 523, 565 and it is classified as Genetic_Algorithms, it is not the target node. The node 1796 is a product titled 'Title: Evaluating and Improving Steady State Evolutionary Algorithms on Constraint Satisfaction Prob' with key attributes: evolutionari, state, satisfact, genet, constraint, evalu, improv and is connected with the node 1917 and it is classified as Genetic_Algorithms, it is not the target node. The node 1831 is a product titled 'Title: Some Training Subset Selection Methods for Supervised Learning in Genetic Programming  
Abstr' with key attributes: need, reduc, carri, popul, genet, set, case, size, subset, train, describ, program, evalu, result, difficult, larg, compar, select, supervis, method and is connected with the nodes 163, 1832, 1836 and it is classified as Genetic_Algorithms, it is not the target node. The node 1832 is a product titled 'Title: Tackling the Boolean Even N Parity Problem with Genetic Programming and Limited-Error Fitness' with key attributes: limit, fit, score, modif, asymmetr, remain, genet, order, set, standard, case, train, boolean, mani, program, error, result, base, supervis and is connected with the nodes 55, 415, 1831, 1836 and it is classified as Genetic_Algorithms, it is not the target node. The node 1836 is a product titled 'Title: Small Populations over Many Generations can beat Large Populations over Few Generations in Ge' with key attributes: resourc, literatur, appear, dynam, popul, possibl, genet, effici, subset, mani, requir, program, result, memori, larg, gener, small, select, look and is connected with the nodes 415, 1831, 1832 and it is classified as Genetic_Algorithms, it is not the target node. The node 1917 is a product titled 'Title: Go and Genetic Programming Playing Go with Filter Functions  
Abstract: A neural network mode' with key attributes: function, genet, play, program, filter and is connected with the node 1796 and it is classified as Genetic_Algorithms, it is not the target node. The node 2103 is a product titled 'Title: The Evolution of Communication Schemes Over Continuous Channels  
Abstract: As the field of G' with key attributes: need, today, implement, necessari, genet, absolut, architectur, increas, system, program, propos, recent, becom, field, applic, parallel and is connected with the node 415 and it is classified as Genetic_Algorithms, it is not the target node. The node 2332 is a product titled 'Title: Improved Hoeffding-Style Performance Guarantees for Accurate Classifiers  
Abstract: Evolving' with key attributes: cooper, solv, group, evolv, agent, genet, common, coordin, concurr, nich, distinct, sourc, complex, individu, system, requir, result, effect, multipl, run, preliminari, task, perform and is connected with the node 1117 and it is classified as Genetic_Algorithms, it is not the target node. The node 2334 is a product titled 'Title: New Methods for Competitive Coevolution  
Abstract: We consider "competitive coevolution," in' with key attributes: fit, independ, evolv, popul, level, increas, drive, coevolut, competit, anoth, complex, individu, direct, lead, arm, consid, perform, race, base, select, method and is connected with the node 54 and it is classified as Theory, it is the target node. The node 2353 is a product titled 'Title: Dynamics of Co-evolutionary Learning  
Abstract: Co-evolutionary learning, which involves the' with key attributes: involv, agent, fit, dynam, artifici, environ, success, technolog, nich, adapt, solut, robot, mani, embed, result, progress, potenti, sever and is connected with the node 415 and it is classified as Genetic_Algorithms, it is not the target node. The node 2704 is a product titled 'Title: A Genome Compiler for High Performance Genetic Programming  
Abstract: Genetic Programming is' with key attributes: compil, desir, expens, possibl, genet, effici, time, machin, genom, major, individu, candid, solut, surpris, describ, program, evalu, perform, compar, high, applic and is connected with the node 209 and it is classified as Genetic_Algorithms, it is not the target node.
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

- ID: 2334
- Title: New Methods for Competitive Coevolution
- True class (canonical `y`): **Genetic_Algorithms**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Genetic_Algorithms**
- Prediction recorded by this method's pipeline: **Genetic_Algorithms**

Canonical text (`raw_text`):

~~~~~~text
Title: New Methods for Competitive Coevolution  
Abstract: We consider "competitive coevolution," in which fitness is based on direct competition among individuals selected from two independently evolving populations of "hosts" and "parasites." Competitive coevolution can lead to an "arms race," in which the two populations reciprocally drive one another to increasing levels of performance and complexity. We use the games of Nim and 3-D Tic-Tac-Toe as test problems to explore three new techniques in competitive coevolution. "Competitive fitness sharing" changes the way fitness is measured, "shared sampling" provides a method for selecting a strong, diverse set of parasites, and the "hall of fame" encourages arms races by saving good individuals from prior generations. We provide several different motivations for these methods, and mathematical insights into their use. Experimental comparisons are done, and a detailed analysis of these experiments is presented in terms of testing issues, diversity, extinction, arms race progress measurements, and drift. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 11 nodes

| node id | true class | title |
|---|---|---|
| 54 | Theory | A Competitive Approach to Game Learning |
| 209 | Genetic_Algorithms | 17 Massively Parallel Genetic Programming |
| 602 | Genetic_Algorithms | Every Niching Method has its Niche: Fitness Sharing and Implicit Sharing Compared |
| 1588 | Genetic_Algorithms | Automatic Modularization by Speciation |
| 1790 | Genetic_Algorithms | Using Genetic Programming to Evolve Board Evaluation Functions |
| 1832 | Genetic_Algorithms | Tackling the Boolean Even N Parity Problem with Genetic Programming and Limited-Error Fitness standard GP |
| 1836 | Genetic_Algorithms | Small Populations over Many Generations can beat Large Populations over Few Generations in Genetic Programming |
| 1917 | Genetic_Algorithms | Go and Genetic Programming Playing Go with Filter Functions |
| 2103 | Genetic_Algorithms | The Evolution of Communication Schemes Over Continuous Channels |
| 2332 | Genetic_Algorithms | Improved Hoeffding-Style Performance Guarantees for Accurate Classifiers |
| 2353 | Genetic_Algorithms | Dynamics of Co-evolutionary Learning |

### 2-hop (shortest distance exactly 2): 14 nodes

| node id | true class | title |
|---|---|---|
| 22 | Genetic_Algorithms | Discovering Complex Othello Strategies Through Evolutionary Neural Networks |
| 55 | Genetic_Algorithms | A Comparison of Selection Schemes used in Genetic Algorithms |
| 163 | Genetic_Algorithms | 4 Implementing Application Specific Routines  Genetic algorithms in search, optimization, and machine learning. Reading, MA: Addison-Wesley. |
| 415 | Genetic_Algorithms | Competitive Environments Evolve Better Solutions for Complex Tasks |
| 523 | Genetic_Algorithms | Some studies in machine learning using the game of checkers. IBM Journal, 3(3):211-229, 1959. Some |
| 565 | Reinforcement_Learning | Machine Learning Learning to Predict by the Methods of Temporal Differences Keywords: Incremental learning, prediction, |
| 615 | Theory | Efficient Algorithms for Learning to Play Repeated Games Against Computationally Bounded Adversaries |
| 712 | Genetic_Algorithms | Tracking the red queen: Measurements of adaptive progress in co-evolution ary simulations. In Third European |
| 1114 | Genetic_Algorithms | Using Genetic Algorithms to Explore Pattern Recognition in the Immune System  COMMENTS WELCOME |
| 1117 | Genetic_Algorithms | A Coevolutionary Approach to Learning Sequential Decision Rules |
| 1687 | Reinforcement_Learning | Markov games as a framework for multi-agent reinforcement learning |
| 1796 | Genetic_Algorithms | Evaluating and Improving Steady State Evolutionary Algorithms on Constraint Satisfaction Problems |
| 1831 | Genetic_Algorithms | Some Training Subset Selection Methods for Supervised Learning in Genetic Programming |
| 2704 | Genetic_Algorithms | A Genome Compiler for High Performance Genetic Programming |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/cora/cf-gnnexplainer-canonical/random_seed_42_*` (key=463).

- Factual class: **Genetic_Algorithms**
- Counterfactual class: **Theory**
- Removed edges (global ids, 10): (209, 2334), (602, 2334), (1588, 2334), (1790, 2334), (1832, 2334), (1836, 2334), (1917, 2334), (2103, 2334), (2332, 2334), (2334, 2353)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 2334 |
| Factual_Target_Node_Neighbors | 54, 209, 602, 1588, 1790, 1832, 1836, 1917, 2103, 2332, 2353 |
| Factual_Target_Node_Features | fit, independ, evolv, popul, level, increas, drive, coevolut, competit, anoth, complex, individu, direct, lead, arm, consid, perform, race, base, select, method |
| Counterfactual_Target_Node_Neighbors | 54 |
| Counterfactual_Target_Node_Features | fit, independ, evolv, popul, level, increas, drive, coevolut, competit, anoth, complex, individu, direct, lead, arm, consid, perform, race, base, select, method |
| Factual_Target_Node_Class | Genetic_Algorithms |
| Counterfactual_Target_Node_class | Theory |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 209, 602, 1588, 1790, 1832, 1836, 1917, 2103, 2332, 2353 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 2334 |
| Factual_Target_Node_Neighbors | 54, 209, 602, 1588, 1790, 1832, 1836, 1917, 2103, 2332, 2353 |
| Factual_Target_Node_Features | fit, independ, evolv, popul, level, increas, drive, coevolut, competit, anoth, complex, individu, direct, lead, arm, consid, perform, race, base, select, method |
| Counterfactual_Target_Node_Neighbors | 54 |
| Counterfactual_Target_Node_Features | fit, independ, evolv, popul, level, increas, drive, coevolut, competit, anoth, complex, individu, direct, lead, arm, consid, perform, race, base, select, method |
| Factual_Target_Node_Class | Genetic_Algorithms |
| Counterfactual_Target_Node_class | Theory |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 209, 602, 1588, 1790, 1832, 1836, 1917, 2103, 2332, 2353 |
| Natural_Language_Explanation | None |
