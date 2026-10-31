# Reference packet: CF-GNNExplainer__Qwen-14B__cora__262

- Method: CF-GNNExplainer; configuration: Qwen-14B; dataset: cora; target node: 262
- Explanation source: `./robustness_2026-10-30/production_a100/qwen14b_gptq_int4_cora_Response.json` ([47][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
To address the provided scenario, let's analyze the differences between the factual and counterfactual graphs and fill the `infos` dictionary accordingly.

### Factual Graph Analysis

In the factual graph, the target node (Node ID: 262) is titled "EVOLVING REPRESENTATIONS OF DESIGN CASES AND THEIR USE IN CREATIVE DESIGN". It is connected to nodes 188 and 793, and it is classified as `Case_Based`. Its neighbors include:

- **Node 188**: "Coevolving High-Level Representations" (Genetic_Algorithms)
- **Node 793**: "A Survey of Evolution Strategies" (Genetic_Algorithms)

### Counterfactual Graph Analysis

In the counterfactual graph, the same target node (Node ID: 262) is still titled "EVOLVING REPRESENTATIONS OF DESIGN CASES AND THEIR USE IN CREATIVE DESIGN", but it is now classified as `Genetic_Algorithms`. Its connections have changed slightly:

- **Node 188**: "Coevolving High-Level Representations" (Genetic_Algorithms)
- **Node 793**: "A Survey of Evolution Strategies" (Genetic_Algorithms)

However, the connection to node 266 (which was previously connected in the factual graph) has been removed, and the connection to node 793 has been retained.

### Differences in Connections

- **Removed Connection**: Node 262 is no longer connected to Node 266.
- **Retained Connection**: Node 262 remains connected to Node 188 and Node 793.

### Filling the Dictionary

Based on the analysis, we can fill the `infos` dictionary as follows:

```python
infos = {
    'Target_Node_ID': 262,
    'Factual_Target_Node_Neighbors': [188, 266, 793],
    'Factual_Target_Node_Features': ['chang', 'paramet', 'easili', 'evolv', 'suffici', 'autom', 'import', 'set', 'cbr', 'case', 'play', 'role', 'adapt', 'requir', 'design', 'represent', 'creativ', 'task', 'howev'],
    'Counterfactual_Target_Node_Neighbors': [188, 793],
    'Counterfactual_Target_Node_Features': ['chang', 'paramet', 'easili', 'evolv', 'suffici', 'autom', 'import', 'set', 'cbr', 'case', 'play', 'role', 'adapt', 'requir', 'design', 'represent', 'creativ', 'task', 'howev'],
    'Factual_Target_Node_Class': 'Case_Based',
    'Counterfactual_Target_Node_class': 'Genetic_Algorithms',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Natural_Language_Explanation': 'In the factual graph, the target node (ID: 262) is classified as Case_Based and is connected to nodes 188, 266, and 793. In the counterfactual graph, the target node is reclassified as Genetic_Algorithms, and the connection to node 266 is removed, while connections to nodes 188 and 793 are retained. This change suggests that the removal of the connection to node 266 (which is also classified as Case_Based) influenced the classification of the target node towards Genetic_Algorithms.'
}
```

### Explanation of Changes

The target node (Node ID: 262) originally classified as `Case_Based` in the factual graph is reclassified as `Genetic_Algorithms` in the counterfactual graph. This change is primarily driven by the removal of the connection to node 266, which was also classified as `Case_Based`. 

- **Node 266**: Removing this connection reduces the influence of `Case_Based` nodes on the target node.
- **Nodes 188 and 793**: These nodes remain connected and are both classified as `Genetic_Algorithms`, reinforcing the shift towards this category.

Thus, the removal of the connection to node 266, combined with the retention of connections to nodes classified as `Genetic_Algorithms`, leads to the reclassification of the target node from `Case_Based` to `Genetic_Algorithms`.

This counterfactual explanation highlights how altering the graph structure can significantly impact the classification of nodes, providing valuable insights into the decision-making process of the underlying machine learning model.
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
given the factual graph: The node 42 is a product titled 'Title: Evolutionary Module Acquisition  
Abstract: A critical issue for users of Markov Chain Monte' with key attributes: evolutionari, acquisit, modul and is connected with the nodes 163, 188, 189, 793 and it is classified as Genetic_Algorithms, it is not the target node. The node 120 is a product titled 'Title: Genetic Programming Exploratory Power and the Discovery of Functions  
Abstract: Hierarchical' with key attributes: explan, function, exploratori, evolut, modif, behavior, qualit, reli, genet, perspect, divers, hierarch, power, analysi, dual, discoveri, acceler, process, provid, program, result, improv, base and is connected with the node 188 and it is classified as Genetic_Algorithms, it is not the target node. The node 129 is a product titled 'Title: Evolving Networks: Using the Genetic Algorithm with Connectionist Learning  
Abstract: A pilo' with key attributes: network, evolv, connectionist, genet, result and is connected with the nodes 163, 188 and it is classified as Genetic_Algorithms, it is not the target node. The node 139 is a product titled 'Title: Investigating the Generality of Automatically Defined Functions  
Abstract: This paper studie' with key attributes: defin, function, analys, solv, suit, genet, simul, compos, style, anneal, discoveri, investig, contrast, combin, program, result, perform, automat, compar, gener, studi and is connected with the node 188 and it is classified as Genetic_Algorithms, it is not the target node. The node 141 is a product titled 'Title: Hierarchical Self-Organization in Genetic Programming  
Abstract: This paper presents an appr' with key attributes: self, defin, function, evolut, genet, deploy, trace, hierarch, determin, adapt, discoveri, build, program, represent, result, organ, block, automat, gener, base, analyz and is connected with the nodes 163, 188 and it is classified as Genetic_Algorithms, it is not the target node. The node 144 is a product titled 'Title: The Observers Paradox: Apparent Computational Complexity in Physical Systems  
Abstract: Many' with key attributes: appar, physic, comput, complex, observ, system and is connected with the node 188 and it is classified as Genetic_Algorithms, it is not the target node. The node 163 is a product titled 'Title: 4 Implementing Application Specific Routines  Genetic algorithms in search, optimization, and' with key attributes: network, optim, evolutionari, acquisit, modul, artifici, genet, write, submit, concaten, ieee, neural, recurr, search, represent, life, technic, report, construct and is connected with the nodes 42, 129, 141, 188, 189, 266, 380, 415, 523, 717, 757, 793, 856, 1069, 1070, 1110, 1127, 1139, 1205, 1333, 1334, 1380, 1467, 1691, 1715, 1734, 2202 and it is classified as Genetic_Algorithms, it is not the target node. The node 188 is a product titled 'Title: Coevolving High-Level Representations  
Abstract: Rules extracted from trained feedforward ne' with key attributes: write, represent and is connected with the nodes 42, 120, 129, 139, 141, 144, 163, 189, 262, 380, 415, 523, 717, 721, 755, 757 and it is classified as Genetic_Algorithms, it is not the target node. The node 189 is a product titled 'Title: An Evolutionary Algorithm that Constructs Recurrent Neural Networks  
Abstract: Standard meth' with key attributes: network, fit, function, evolutionari, interact, class, weight, valu, necessari, induc, genet, declar, architectur, standard, neural, recurr, understood, assum, structur, result, task, construct, everi, method and is connected with the nodes 42, 163, 188 and it is classified as Genetic_Algorithms, it is not the target node. The node 262 is a product titled 'Title: EVOLVING REPRESENTATIONS OF DESIGN CASES AND THEIR USE IN CREATIVE DESIGN  
Abstract: In case' with key attributes: chang, paramet, easili, evolv, suffici, autom, import, set, cbr, case, play, role, adapt, requir, design, represent, creativ, task, howev and is connected with the nodes 188, 266, 793, 1980 and it is classified as Case_Based, it is the target node. The node 266 is a product titled 'Title: EMERGENT BEHAVIOUR IN CO-EVOLUTIONARY DESIGN  
Abstract: An important aspect of creative desi' with key attributes: research, limit, domain, aspect, artifici, commun, import, emerg, insight, nich, understood, mechan, behaviour, design, result, life, creativ, consid, definit, shape, concept and is connected with the nodes 163, 262 and it is classified as Case_Based, it is not the target node. The node 380 is a product titled 'Title: Fitness Landscapes and Difficulty in Genetic Programming  
Abstract: The structure of the fit' with key attributes: fit, measur, valu, random, genet, walk, determin, landscap, difficulti, oper, program, structur, examin, attempt, recent, rang, correl, known, analyz and is connected with the nodes 163, 188 and it is classified as Genetic_Algorithms, it is not the target node. The node 415 is a product titled 'Title: Competitive Environments Evolve Better Solutions for Complex Tasks  
Abstract: University of' with key attributes: initi, evolv, competit, complex, mutat, solut, refer, better, task, method and is connected with the nodes 163, 188, 523 and it is classified as Genetic_Algorithms, it is not the target node. The node 523 is a product titled 'Title: Some studies in machine learning using the game of checkers. IBM Journal, 3(3):211-229, 1959.' with key attributes: machin, journal, game, result, studi and is connected with the nodes 163, 188, 415, 717 and it is classified as Genetic_Algorithms, it is not the target node. The node 717 is a product titled 'Title: Information filtering: Selection mechanisms in learning systems. Machine Learning, 10:113-151' with key attributes: inform, artifici, machin, mechan, system, search, filter, result, gener, select and is connected with the nodes 163, 188, 523 and it is classified as Genetic_Algorithms, it is not the target node. The node 721 is a product titled 'Title: Learning Representations for Evolutionary Computation an example from the domain of two-dimen' with key attributes: varieti, domain, evolutionari, similar, basic, genet, depend, comput, specif, time, exampl, system, design, search, schedul, represent, result, pursuer, shape, compar, alway, applic, unfortun and is connected with the node 188 and it is classified as Genetic_Algorithms, it is not the target node. The node 755 is a product titled 'Title: of a simulator for evolving morphology are: Universal the simulator should cover an infinite' with key attributes: ed, cover, evolv, evolut, artifici, fourth, infinit, object, simul, mit, comput, press, familiar, program, result, life, confer, knowledg, univers and is connected with the nodes 188, 757 and it is classified as Genetic_Algorithms, it is not the target node. The node 757 is a product titled 'Title: Evolving Self-Supporting Structures Page 18 References Evolution of Visual Control Systems fo' with key attributes: inspir, evolut, guid, particularli, artifici, explor, year, pixel, input, case, visual, observ, robot, exhibit, system, behaviour, mani, sophist, result, control, eye, sever and is connected with the nodes 163, 188, 755 and it is classified as Genetic_Algorithms, it is not the target node. The node 758 is a product titled 'Title: A COMPRESSION ALGORITHM FOR PROBABILITY TRANSITION MATRICES  
Abstract: This paper describes' with key attributes: matrix, appear, compress, level, probabl, genet, transit, describ, error, result, gener, small, high and is connected with the node 1980 and it is classified as Genetic_Algorithms, it is not the target node. The node 793 is a product titled 'Title: A Survey of Evolution Strategies  
Abstract:' with key attributes: survey, evolut, strategi and is connected with the nodes 42, 163, 262, 856, 943, 959, 1069, 1070, 1110, 1127, 1139, 1205, 1249, 1330, 1333, 1334, 1380, 1455, 1467, 1691, 1694, 1715, 1734 and it is classified as Genetic_Algorithms, it is not the target node. The node 856 is a product titled 'Title: Hierarchical priors and mixture models, with application in regression and density estimation' with key attributes: genet, tutori, revis, technic, report and is connected with the nodes 163, 793 and it is classified as Genetic_Algorithms, it is not the target node. The node 943 is a product titled 'Title: Crossover or Mutation?  
Abstract: Genetic algorithms rely on two genetic operators crossover' with key attributes: captur, exist, reli, genet, power, exampl, concern, role, sens, fashion, mutat, oper, shown, crossov, bodi, recent, larg, theoret, convent and is connected with the node 793 and it is classified as Genetic_Algorithms, it is not the target node. The node 959 is a product titled 'Title: Numerical techniques for efficient sonar bearing and range searching in the near field using' with key attributes: numer, estim, target, articl, genet, effici, case, track, locat, describ, search, techniqu, result, rang, larg, compar, field, method, may and is connected with the node 793 and it is classified as Genetic_Algorithms, it is not the target node. The node 1069 is a product titled 'Title: Extended Selection Mechanisms in Genetic Algorithms  
Abstract:' with key attributes: extend, genet, mechan, select and is connected with the nodes 163, 793, 1455 and it is classified as Genetic_Algorithms, it is not the target node. The node 1070 is a product titled 'Title: Extended Selection Mechanisms in Genetic Algorithms  
Abstract: A Genetic Algorithm Tutorial' with key attributes: genet, tutori, revis, technic, report and is connected with the nodes 163, 793 and it is classified as Genetic_Algorithms, it is not the target node. The node 1110 is a product titled 'Title: On The State of Evolutionary Computation  
Abstract: In the past few years the evolutionary c' with key attributes: research, past, chang, evolutionari, interact, group, state, level, comput, year, increas, variou, landscap, idea, simultan, challeng, effect, result, recent, rapidli and is connected with the nodes 163, 793 and it is classified as Genetic_Algorithms, it is not the target node. The node 1127 is a product titled 'Title: Recombination Operator, its Correlation to the Fitness Landscape and Search Performance  
Abs' with key attributes: fit, public, recombin, portion, read, form, landscap, oper, provid, search, materi, associ, perform, correl, author, may, right and is connected with the nodes 163, 793 and it is classified as Genetic_Algorithms, it is not the target node. The node 1139 is a product titled 'Title: Optimal Mutation Rates in Genetic Search  
Abstract: The optimization of a single bit string' with key attributes: encod, simpl, optim, fit, function, bit, best, contin, string, code, genet, respect, iter, mean, discuss, standard, integ, mutat, rate, singl, binari, search, select and is connected with the nodes 163, 793 and it is classified as Genetic_Algorithms, it is not the target node. The node 1205 is a product titled 'Title: The Role of Development in Genetic Algorithms  
Abstract: A Genetic Algorithm Tutorial Darrel' with key attributes: genet, tutori, revis, technic, report and is connected with the nodes 163, 793 and it is classified as Genetic_Algorithms, it is not the target node. The node 1249 is a product titled 'Title: Evolution of Non-Deterministic Incremental Algorithms as a New Approach for Search in State S' with key attributes: defin, increment, abl, space, state, evolut, genet, sequenc, order, read, combinatori, case, choic, solut, search, result, construct, call, select, repres and is connected with the nodes 793, 1734 and it is classified as Genetic_Algorithms, it is not the target node. The node 1330 is a product titled 'Title: Evolving Cellular Automata with Genetic Algorithms: A Review of Recent Work  
Abstract: We re' with key attributes: review, group, evolv, global, automata, genet, appli, classif, comput, coordin, case, requir, design, densiti, task, work, seattl, done, perform, synchron, cellular and is connected with the node 793 and it is classified as Genetic_Algorithms, it is not the target node. The node 1333 is a product titled 'Title: Using Genetic Algorithms for Supervised Concept Learning  
Abstract: Genetic Algorithms (GAs)' with key attributes: measur, interact, refin, rule, genet, environ, classif, explor, set, continu, adapt, system, search, techniqu, result, perform, construct, concept and is connected with the nodes 163, 793, 1467 and it is classified as Genetic_Algorithms, it is not the target node. The node 1334 is a product titled 'Title: THE OPTIONS DESIGN EXPLORATION SYSTEM Reference Manual and User Guide Version B2.1  
Abstract' with key attributes: guid, option, explor, user, refer, system, design, version and is connected with the nodes 163, 793 and it is classified as Genetic_Algorithms, it is not the target node. The node 1380 is a product titled 'Title: Evaluating Evolutionary Algorithms  
Abstract: Test functions are commonly used to evaluate t' with key attributes: defin, function, evolutionari, suit, genet, depend, comparison, compet, comprehens, subject, evalu, search, develop, effect, result, commonli, difficult, differ, goal, howev, unfortun and is connected with the nodes 163, 793 and it is classified as Genetic_Algorithms, it is not the target node. The node 1455 is a product titled 'Title: Self-Adaptation in Genetic Algorithms of external parameters of a GA is seen as a first
Abstr' with key attributes: chang, paramet, indic, evolut, item, basic, genet, set, transfer, seen, adapt, mutat, idea, shortcom, appropri, rate, extern, process, search, result, strategi, experiment and is connected with the nodes 793, 1069, 1694 and it is classified as Genetic_Algorithms, it is not the target node. The node 1467 is a product titled 'Title: Adaptive Strategy Selection for Concept Learning  
Abstract: In this paper, we explore the us' with key attributes: art, refin, rule, genet, environ, classif, explor, continu, learner, adapt, system, result, strategi, perform, construct, call, compar, concept, select and is connected with the nodes 163, 793, 1333 and it is classified as Genetic_Algorithms, it is not the target node. The node 1691 is a product titled 'Title: Evolutionary Algorithms: Some Very Old Strategies for Optimization and Adaptation  
Abstract:' with key attributes: optim, paramet, evolutionari, class, evolut, basic, possibl, genet, natur, discuss, adapt, main, mechan, strategi, model, work, compar, base, differ, applic, repres and is connected with the nodes 163, 793 and it is classified as Genetic_Algorithms, it is not the target node. The node 1694 is a product titled 'Title: Strategy Adaptation by Competing Subpopulations  
Abstract: The breeder genetic algorithm BGA' with key attributes: numer, paramet, robust, genet, depend, effici, compet, set, subpopul, adapt, oper, shown, result, strategi, control, differ and is connected with the nodes 793, 1455 and it is classified as Genetic_Algorithms, it is not the target node. The node 1715 is a product titled 'Title: A Sampling-Based Heuristic for Tree Search Applied to Grammar Induction  
Abstract: In the fi' with key attributes: research, space, tree, grammar, global, random, basic, artifici, intellig, genet, appli, respect, iter, heurist, induct, sampl, oper, design, search, techniqu, field, theori, stochast, base, sever and is connected with the nodes 163, 793, 1734 and it is classified as Genetic_Algorithms, it is not the target node. The node 1734 is a product titled 'Title: A Stochastic Search Approach to Grammar Induction  
Abstract: This paper describes a new samp' with key attributes: inspir, place, tree, grammar, analysi, heurist, competit, induct, name, dfa, describ, search, result, recent, work, perform, stochast and is connected with the nodes 163, 793, 1249, 1715 and it is classified as Genetic_Algorithms, it is not the target node. The node 1980 is a product titled 'Title: An Overview of Evolutionary Computation  
Abstract: Evolutionary computation uses computation' with key attributes: implement, evolutionari, solv, similar, overview, evolut, genet, comput, import, process, system, provid, describ, design, result, model, interest, key, element, sever, current and is connected with the nodes 262, 758, 2202, 2457 and it is classified as Genetic_Algorithms, it is not the target node. The node 2202 is a product titled 'Title: An Evolutionary Approach to Combinatorial Optimization Problems  
Abstract: The paper reports' with key attributes: chang, optim, fit, function, evolutionari, sum, evolut, cut, maximum, minimum, genet, min, combinatori, particular, subset, search, probabilist, model, organ, report, consid, task, base, applic and is connected with the nodes 163, 1980 and it is classified as Genetic_Algorithms, it is not the target node. The node 2457 is a product titled 'Title: In Proceedings of the 1997 Sian Kaan International Workshop on Neural Networks and Neurocontr' with key attributes: network, scienc, workshop, grind, comput, machin, neural, intern, laboratori, depart, mani, model, proceed, result, univers and is connected with the node 1980 and it is classified as Neural_Networks, it is not the target node. and given the counterfactual example: The node 42 is a product titled 'Title: Evolutionary Module Acquisition  
Abstract: A critical issue for users of Markov Chain Monte' with key attributes: evolutionari, acquisit, modul and is connected with the nodes 163, 188, 189, 793 and it is classified as Genetic_Algorithms, it is not the target node. The node 120 is a product titled 'Title: Genetic Programming Exploratory Power and the Discovery of Functions  
Abstract: Hierarchical' with key attributes: explan, function, exploratori, evolut, modif, behavior, qualit, reli, genet, perspect, divers, hierarch, power, analysi, dual, discoveri, acceler, process, provid, program, result, improv, base and is connected with the node 188 and it is classified as Genetic_Algorithms, it is not the target node. The node 129 is a product titled 'Title: Evolving Networks: Using the Genetic Algorithm with Connectionist Learning  
Abstract: A pilo' with key attributes: network, evolv, connectionist, genet, result and is connected with the nodes 163, 188 and it is classified as Genetic_Algorithms, it is not the target node. The node 139 is a product titled 'Title: Investigating the Generality of Automatically Defined Functions  
Abstract: This paper studie' with key attributes: defin, function, analys, solv, suit, genet, simul, compos, style, anneal, discoveri, investig, contrast, combin, program, result, perform, automat, compar, gener, studi and is connected with the node 188 and it is classified as Genetic_Algorithms, it is not the target node. The node 141 is a product titled 'Title: Hierarchical Self-Organization in Genetic Programming  
Abstract: This paper presents an appr' with key attributes: self, defin, function, evolut, genet, deploy, trace, hierarch, determin, adapt, discoveri, build, program, represent, result, organ, block, automat, gener, base, analyz and is connected with the nodes 163, 188 and it is classified as Genetic_Algorithms, it is not the target node. The node 144 is a product titled 'Title: The Observers Paradox: Apparent Computational Complexity in Physical Systems  
Abstract: Many' with key attributes: appar, physic, comput, complex, observ, system and is connected with the node 188 and it is classified as Genetic_Algorithms, it is not the target node. The node 163 is a product titled 'Title: 4 Implementing Application Specific Routines  Genetic algorithms in search, optimization, and' with key attributes: network, optim, evolutionari, acquisit, modul, artifici, genet, write, submit, concaten, ieee, neural, recurr, search, represent, life, technic, report, construct and is connected with the nodes 42, 129, 141, 188, 189, 266, 380, 415, 523, 717, 757, 793, 856, 1069, 1070, 1110, 1127, 1139, 1205, 1333, 1334, 1380, 1467, 1691, 1715, 1734, 2202 and it is classified as Genetic_Algorithms, it is not the target node. The node 188 is a product titled 'Title: Coevolving High-Level Representations  
Abstract: Rules extracted from trained feedforward ne' with key attributes: write, represent and is connected with the nodes 42, 120, 129, 139, 141, 144, 163, 189, 262, 380, 415, 523, 717, 721, 755, 757 and it is classified as Genetic_Algorithms, it is not the target node. The node 189 is a product titled 'Title: An Evolutionary Algorithm that Constructs Recurrent Neural Networks  
Abstract: Standard meth' with key attributes: network, fit, function, evolutionari, interact, class, weight, valu, necessari, induc, genet, declar, architectur, standard, neural, recurr, understood, assum, structur, result, task, construct, everi, method and is connected with the nodes 42, 163, 188 and it is classified as Genetic_Algorithms, it is not the target node. The node 262 is a product titled 'Title: EVOLVING REPRESENTATIONS OF DESIGN CASES AND THEIR USE IN CREATIVE DESIGN  
Abstract: In case' with key attributes: chang, paramet, easili, evolv, suffici, autom, import, set, cbr, case, play, role, adapt, requir, design, represent, creativ, task, howev and is connected with the nodes 188, 793 and it is classified as Genetic_Algorithms, it is the target node. The node 266 is a product titled 'Title: EMERGENT BEHAVIOUR IN CO-EVOLUTIONARY DESIGN  
Abstract: An important aspect of creative desi' with key attributes: research, limit, domain, aspect, artifici, commun, import, emerg, insight, nich, understood, mechan, behaviour, design, result, life, creativ, consid, definit, shape, concept and is connected with the node 163 and it is classified as Genetic_Algorithms, it is not the target node. The node 380 is a product titled 'Title: Fitness Landscapes and Difficulty in Genetic Programming  
Abstract: The structure of the fit' with key attributes: fit, measur, valu, random, genet, walk, determin, landscap, difficulti, oper, program, structur, examin, attempt, recent, rang, correl, known, analyz and is connected with the nodes 163, 188 and it is classified as Genetic_Algorithms, it is not the target node. The node 415 is a product titled 'Title: Competitive Environments Evolve Better Solutions for Complex Tasks  
Abstract: University of' with key attributes: initi, evolv, competit, complex, mutat, solut, refer, better, task, method and is connected with the nodes 163, 188, 523 and it is classified as Genetic_Algorithms, it is not the target node. The node 523 is a product titled 'Title: Some studies in machine learning using the game of checkers. IBM Journal, 3(3):211-229, 1959.' with key attributes: machin, journal, game, result, studi and is connected with the nodes 163, 188, 415, 717 and it is classified as Genetic_Algorithms, it is not the target node. The node 717 is a product titled 'Title: Information filtering: Selection mechanisms in learning systems. Machine Learning, 10:113-151' with key attributes: inform, artifici, machin, mechan, system, search, filter, result, gener, select and is connected with the nodes 163, 188, 523 and it is classified as Genetic_Algorithms, it is not the target node. The node 721 is a product titled 'Title: Learning Representations for Evolutionary Computation an example from the domain of two-dimen' with key attributes: varieti, domain, evolutionari, similar, basic, genet, depend, comput, specif, time, exampl, system, design, search, schedul, represent, result, pursuer, shape, compar, alway, applic, unfortun and is connected with the node 188 and it is classified as Genetic_Algorithms, it is not the target node. The node 755 is a product titled 'Title: of a simulator for evolving morphology are: Universal the simulator should cover an infinite' with key attributes: ed, cover, evolv, evolut, artifici, fourth, infinit, object, simul, mit, comput, press, familiar, program, result, life, confer, knowledg, univers and is connected with the nodes 188, 757 and it is classified as Genetic_Algorithms, it is not the target node. The node 757 is a product titled 'Title: Evolving Self-Supporting Structures Page 18 References Evolution of Visual Control Systems fo' with key attributes: inspir, evolut, guid, particularli, artifici, explor, year, pixel, input, case, visual, observ, robot, exhibit, system, behaviour, mani, sophist, result, control, eye, sever and is connected with the nodes 163, 188, 755 and it is classified as Genetic_Algorithms, it is not the target node. The node 758 is a product titled 'Title: A COMPRESSION ALGORITHM FOR PROBABILITY TRANSITION MATRICES  
Abstract: This paper describes' with key attributes: matrix, appear, compress, level, probabl, genet, transit, describ, error, result, gener, small, high and is connected with the node 1980 and it is classified as Genetic_Algorithms, it is not the target node. The node 793 is a product titled 'Title: A Survey of Evolution Strategies  
Abstract:' with key attributes: survey, evolut, strategi and is connected with the nodes 42, 163, 262, 959, 1127, 1139, 1249, 1691, 1715 and it is classified as Genetic_Algorithms, it is not the target node. The node 856 is a product titled 'Title: Hierarchical priors and mixture models, with application in regression and density estimation' with key attributes: genet, tutori, revis, technic, report and is connected with the node 163 and it is classified as Genetic_Algorithms, it is not the target node. The node 943 is a product titled 'Title: Crossover or Mutation?  
Abstract: Genetic algorithms rely on two genetic operators crossover' with key attributes: captur, exist, reli, genet, power, exampl, concern, role, sens, fashion, mutat, oper, shown, crossov, bodi, recent, larg, theoret, convent and is connected with no other nodes and it is classified as Genetic_Algorithms, it is not the target node. The node 959 is a product titled 'Title: Numerical techniques for efficient sonar bearing and range searching in the near field using' with key attributes: numer, estim, target, articl, genet, effici, case, track, locat, describ, search, techniqu, result, rang, larg, compar, field, method, may and is connected with the node 793 and it is classified as Genetic_Algorithms, it is not the target node. The node 1069 is a product titled 'Title: Extended Selection Mechanisms in Genetic Algorithms  
Abstract:' with key attributes: extend, genet, mechan, select and is connected with the nodes 163, 1455 and it is classified as Genetic_Algorithms, it is not the target node. The node 1070 is a product titled 'Title: Extended Selection Mechanisms in Genetic Algorithms  
Abstract: A Genetic Algorithm Tutorial' with key attributes: genet, tutori, revis, technic, report and is connected with the node 163 and it is classified as Genetic_Algorithms, it is not the target node. The node 1110 is a product titled 'Title: On The State of Evolutionary Computation  
Abstract: In the past few years the evolutionary c' with key attributes: research, past, chang, evolutionari, interact, group, state, level, comput, year, increas, variou, landscap, idea, simultan, challeng, effect, result, recent, rapidli and is connected with the node 163 and it is classified as Genetic_Algorithms, it is not the target node. The node 1127 is a product titled 'Title: Recombination Operator, its Correlation to the Fitness Landscape and Search Performance  
Abs' with key attributes: fit, public, recombin, portion, read, form, landscap, oper, provid, search, materi, associ, perform, correl, author, may, right and is connected with the nodes 163, 793 and it is classified as Genetic_Algorithms, it is not the target node. The node 1139 is a product titled 'Title: Optimal Mutation Rates in Genetic Search  
Abstract: The optimization of a single bit string' with key attributes: encod, simpl, optim, fit, function, bit, best, contin, string, code, genet, respect, iter, mean, discuss, standard, integ, mutat, rate, singl, binari, search, select and is connected with the nodes 163, 793 and it is classified as Genetic_Algorithms, it is not the target node. The node 1205 is a product titled 'Title: The Role of Development in Genetic Algorithms  
Abstract: A Genetic Algorithm Tutorial Darrel' with key attributes: genet, tutori, revis, technic, report and is connected with the node 163 and it is classified as Genetic_Algorithms, it is not the target node. The node 1249 is a product titled 'Title: Evolution of Non-Deterministic Incremental Algorithms as a New Approach for Search in State S' with key attributes: defin, increment, abl, space, state, evolut, genet, sequenc, order, read, combinatori, case, choic, solut, search, result, construct, call, select, repres and is connected with the nodes 793, 1734 and it is classified as Genetic_Algorithms, it is not the target node. The node 1330 is a product titled 'Title: Evolving Cellular Automata with Genetic Algorithms: A Review of Recent Work  
Abstract: We re' with key attributes: review, group, evolv, global, automata, genet, appli, classif, comput, coordin, case, requir, design, densiti, task, work, seattl, done, perform, synchron, cellular and is connected with no other nodes and it is classified as Genetic_Algorithms, it is not the target node. The node 1333 is a product titled 'Title: Using Genetic Algorithms for Supervised Concept Learning  
Abstract: Genetic Algorithms (GAs)' with key attributes: measur, interact, refin, rule, genet, environ, classif, explor, set, continu, adapt, system, search, techniqu, result, perform, construct, concept and is connected with the nodes 163, 1467 and it is classified as Genetic_Algorithms, it is not the target node. The node 1334 is a product titled 'Title: THE OPTIONS DESIGN EXPLORATION SYSTEM Reference Manual and User Guide Version B2.1  
Abstract' with key attributes: guid, option, explor, user, refer, system, design, version and is connected with the node 163 and it is classified as Genetic_Algorithms, it is not the target node. The node 1380 is a product titled 'Title: Evaluating Evolutionary Algorithms  
Abstract: Test functions are commonly used to evaluate t' with key attributes: defin, function, evolutionari, suit, genet, depend, comparison, compet, comprehens, subject, evalu, search, develop, effect, result, commonli, difficult, differ, goal, howev, unfortun and is connected with the node 163 and it is classified as Genetic_Algorithms, it is not the target node. The node 1455 is a product titled 'Title: Self-Adaptation in Genetic Algorithms of external parameters of a GA is seen as a first
Abstr' with key attributes: chang, paramet, indic, evolut, item, basic, genet, set, transfer, seen, adapt, mutat, idea, shortcom, appropri, rate, extern, process, search, result, strategi, experiment and is connected with the nodes 1069, 1694 and it is classified as Genetic_Algorithms, it is not the target node. The node 1467 is a product titled 'Title: Adaptive Strategy Selection for Concept Learning  
Abstract: In this paper, we explore the us' with key attributes: art, refin, rule, genet, environ, classif, explor, continu, learner, adapt, system, result, strategi, perform, construct, call, compar, concept, select and is connected with the nodes 163, 1333 and it is classified as Genetic_Algorithms, it is not the target node. The node 1691 is a product titled 'Title: Evolutionary Algorithms: Some Very Old Strategies for Optimization and Adaptation  
Abstract:' with key attributes: optim, paramet, evolutionari, class, evolut, basic, possibl, genet, natur, discuss, adapt, main, mechan, strategi, model, work, compar, base, differ, applic, repres and is connected with the nodes 163, 793 and it is classified as Genetic_Algorithms, it is not the target node. The node 1694 is a product titled 'Title: Strategy Adaptation by Competing Subpopulations  
Abstract: The breeder genetic algorithm BGA' with key attributes: numer, paramet, robust, genet, depend, effici, compet, set, subpopul, adapt, oper, shown, result, strategi, control, differ and is connected with the node 1455 and it is classified as Genetic_Algorithms, it is not the target node. The node 1715 is a product titled 'Title: A Sampling-Based Heuristic for Tree Search Applied to Grammar Induction  
Abstract: In the fi' with key attributes: research, space, tree, grammar, global, random, basic, artifici, intellig, genet, appli, respect, iter, heurist, induct, sampl, oper, design, search, techniqu, field, theori, stochast, base, sever and is connected with the nodes 163, 793, 1734 and it is classified as Genetic_Algorithms, it is not the target node. The node 1734 is a product titled 'Title: A Stochastic Search Approach to Grammar Induction  
Abstract: This paper describes a new samp' with key attributes: inspir, place, tree, grammar, analysi, heurist, competit, induct, name, dfa, describ, search, result, recent, work, perform, stochast and is connected with the nodes 163, 1249, 1715 and it is classified as Genetic_Algorithms, it is not the target node. The node 1980 is a product titled 'Title: An Overview of Evolutionary Computation  
Abstract: Evolutionary computation uses computation' with key attributes: implement, evolutionari, solv, similar, overview, evolut, genet, comput, import, process, system, provid, describ, design, result, model, interest, key, element, sever, current and is connected with the nodes 758, 2202, 2457 and it is classified as Genetic_Algorithms, it is not the target node. The node 2202 is a product titled 'Title: An Evolutionary Approach to Combinatorial Optimization Problems  
Abstract: The paper reports' with key attributes: chang, optim, fit, function, evolutionari, sum, evolut, cut, maximum, minimum, genet, min, combinatori, particular, subset, search, probabilist, model, organ, report, consid, task, base, applic and is connected with the nodes 163, 1980 and it is classified as Genetic_Algorithms, it is not the target node. The node 2457 is a product titled 'Title: In Proceedings of the 1997 Sian Kaan International Workshop on Neural Networks and Neurocontr' with key attributes: network, scienc, workshop, grind, comput, machin, neural, intern, laboratori, depart, mani, model, proceed, result, univers and is connected with the node 1980 and it is classified as Neural_Networks, it is not the target node.
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

- ID: 262
- Title: EVOLVING REPRESENTATIONS OF DESIGN CASES AND THEIR USE IN CREATIVE DESIGN
- True class (canonical `y`): **Case_Based**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Case_Based**
- Prediction recorded by this method's pipeline: **Case_Based**

Canonical text (`raw_text`):

~~~~~~text
Title: EVOLVING REPRESENTATIONS OF DESIGN CASES AND THEIR USE IN CREATIVE DESIGN  
Abstract: In case-based design, the adaptation of a design case to new design requirements plays an important role. If it is sufficient to adapt a predefined set of design parameters, the task is easily automated. If, however, more far-reaching, creative changes are required, current systems provide only limited success. This paper describes an approach to creative design adaptation based on the notion of creativity as 'goal oriented shift of focus of a search process'. An evolving representation is used to restructure the search space so that designs similar to the example case lie in the focus of the search. This focus is than used as a starting point to create new designs. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 4 nodes

| node id | true class | title |
|---|---|---|
| 188 | Genetic_Algorithms | Coevolving High-Level Representations |
| 266 | Case_Based | EMERGENT BEHAVIOUR IN CO-EVOLUTIONARY DESIGN |
| 793 | Genetic_Algorithms | A Survey of Evolution Strategies |
| 1980 | Genetic_Algorithms | An Overview of Evolutionary Computation |

### 2-hop (shortest distance exactly 2): 38 nodes

| node id | true class | title |
|---|---|---|
| 42 | Genetic_Algorithms | Evolutionary Module Acquisition |
| 120 | Genetic_Algorithms | Genetic Programming Exploratory Power and the Discovery of Functions |
| 129 | Genetic_Algorithms | Evolving Networks: Using the Genetic Algorithm with Connectionist Learning |
| 139 | Genetic_Algorithms | Investigating the Generality of Automatically Defined Functions |
| 141 | Genetic_Algorithms | Hierarchical Self-Organization in Genetic Programming |
| 144 | Neural_Networks | The Observers Paradox: Apparent Computational Complexity in Physical Systems |
| 163 | Genetic_Algorithms | 4 Implementing Application Specific Routines  Genetic algorithms in search, optimization, and machine learning. Reading, MA: Addison-Wesley. |
| 189 | Genetic_Algorithms | An Evolutionary Algorithm that Constructs Recurrent Neural Networks |
| 380 | Genetic_Algorithms | Fitness Landscapes and Difficulty in Genetic Programming |
| 415 | Genetic_Algorithms | Competitive Environments Evolve Better Solutions for Complex Tasks |
| 523 | Genetic_Algorithms | Some studies in machine learning using the game of checkers. IBM Journal, 3(3):211-229, 1959. Some |
| 717 | Genetic_Algorithms | Information filtering: Selection mechanisms in learning systems. Machine Learning, 10:113-151, 1993. Generalization as search. Artificial |
| 721 | Genetic_Algorithms | Learning Representations for Evolutionary Computation an example from the domain of two-dimensional shape designs. In |
| 755 | Genetic_Algorithms | of a simulator for evolving morphology are: Universal the simulator should cover an infinite gen |
| 757 | Genetic_Algorithms | Evolving Self-Supporting Structures Page 18 References Evolution of Visual Control Systems for Robots. To appear |
| 758 | Genetic_Algorithms | A COMPRESSION ALGORITHM FOR PROBABILITY TRANSITION MATRICES |
| 856 | Genetic_Algorithms | Hierarchical priors and mixture models, with application in regression and density estimation |
| 943 | Genetic_Algorithms | Crossover or Mutation? |
| 959 | Genetic_Algorithms | Numerical techniques for efficient sonar bearing and range searching in the near field using genetic algorithms |
| 1069 | Genetic_Algorithms | Extended Selection Mechanisms in Genetic Algorithms |
| 1070 | Genetic_Algorithms | Extended Selection Mechanisms in Genetic Algorithms |
| 1110 | Genetic_Algorithms | On The State of Evolutionary Computation |
| 1127 | Genetic_Algorithms | Recombination Operator, its Correlation to the Fitness Landscape and Search Performance |
| 1139 | Genetic_Algorithms | Optimal Mutation Rates in Genetic Search |
| 1205 | Genetic_Algorithms | The Role of Development in Genetic Algorithms |
| 1249 | Genetic_Algorithms | Evolution of Non-Deterministic Incremental Algorithms as a New Approach for Search in State Spaces |
| 1330 | Genetic_Algorithms | Evolving Cellular Automata with Genetic Algorithms: A Review of Recent Work |
| 1333 | Genetic_Algorithms | Using Genetic Algorithms for Supervised Concept Learning |
| 1334 | Genetic_Algorithms | THE OPTIONS DESIGN EXPLORATION SYSTEM Reference Manual and User Guide Version B2.1 |
| 1380 | Genetic_Algorithms | Evaluating Evolutionary Algorithms |
| 1455 | Genetic_Algorithms | Self-Adaptation in Genetic Algorithms of external parameters of a GA is seen as a first |
| 1467 | Genetic_Algorithms | Adaptive Strategy Selection for Concept Learning |
| 1691 | Genetic_Algorithms | Evolutionary Algorithms: Some Very Old Strategies for Optimization and Adaptation |
| 1694 | Genetic_Algorithms | Strategy Adaptation by Competing Subpopulations |
| 1715 | Genetic_Algorithms | A Sampling-Based Heuristic for Tree Search Applied to Grammar Induction |
| 1734 | Genetic_Algorithms | A Stochastic Search Approach to Grammar Induction |
| 2202 | Genetic_Algorithms | An Evolutionary Approach to Combinatorial Optimization Problems |
| 2457 | Neural_Networks | In Proceedings of the 1997 Sian Kaan International Workshop on Neural Networks and Neurocontrol. Real-Valued |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/cora/cf-gnnexplainer-canonical/random_seed_42_*` (key=47).

- Factual class: **Case_Based**
- Counterfactual class: **Genetic_Algorithms**
- Removed edges (global ids, 16): (262, 266), (262, 1980), (793, 856), (793, 943), (793, 1069), (793, 1070), (793, 1110), (793, 1205), (793, 1330), (793, 1333), (793, 1334), (793, 1380), (793, 1455), (793, 1467), (793, 1694), (793, 1734)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 262 |
| Factual_Target_Node_Neighbors | 188, 266, 793, 1980 |
| Factual_Target_Node_Features | chang, paramet, easili, evolv, suffici, autom, import, set, cbr, case, play, role, adapt, requir, design, represent, creativ, task, howev |
| Counterfactual_Target_Node_Neighbors | 188, 793 |
| Counterfactual_Target_Node_Features | chang, paramet, easili, evolv, suffici, autom, import, set, cbr, case, play, role, adapt, requir, design, represent, creativ, task, howev |
| Factual_Target_Node_Class | Case_Based |
| Counterfactual_Target_Node_class | Genetic_Algorithms |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 266, 1980 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 262 |
| Factual_Target_Node_Neighbors | 188, 266, 793, 1980 |
| Factual_Target_Node_Features | chang, paramet, easili, evolv, suffici, autom, import, set, cbr, case, play, role, adapt, requir, design, represent, creativ, task, howev |
| Counterfactual_Target_Node_Neighbors | 188, 793 |
| Counterfactual_Target_Node_Features | chang, paramet, easili, evolv, suffici, autom, import, set, cbr, case, play, role, adapt, requir, design, represent, creativ, task, howev |
| Factual_Target_Node_Class | Case_Based |
| Counterfactual_Target_Node_class | Genetic_Algorithms |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 266, 1980 |
| Natural_Language_Explanation | None |
