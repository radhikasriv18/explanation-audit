# Reference packet: CF-GNNExplainer__Qwen-14B__cora__1191

- Method: CF-GNNExplainer; configuration: Qwen-14B; dataset: cora; target node: 1191
- Explanation source: `./robustness_2026-10-30/production_a100/qwen14b_gptq_int4_cora_Response.json` ([237][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
To address the provided scenario, we will first identify the differences between the factual and counterfactual graphs, focusing on the target node (node 1191). Then, we will fill the `infos` dictionary accordingly and provide a natural language explanation for the changes.

### Differences Between Factual and Counterfactual Graphs

#### Target Node (Node 1191)
- **Factual Classification**: Theory
- **Counterfactual Classification**: Neural_Networks

#### Neighbor Changes
- **Factual Neighbors**: 661, 692, 1053, 1290, 2423
- **Counterfactual Neighbors**: 661

#### Node Features
- **Factual Features**: measur, tree, genet, statist, machin, varianc, decis, visual, bia, result, term, wide, field, differ
- **Counterfactual Features**: measur, tree, genet, statist, machin, varianc, decis, visual, bia, result, term, wide, field, differ

### Filling the Dictionary

```python
infos = {
    'Target_Node_ID': 1191,
    'Factual_Target_Node_Neighbors': [661, 692, 1053, 1290, 2423],
    'Factual_Target_Node_Features': ['measur', 'tree', 'genet', 'statist', 'machin', 'varianc', 'decis', 'visual', 'bia', 'result', 'term', 'wide', 'field', 'differ'],
    'Counterfactual_Target_Node_Neighbors': [661],
    'Counterfactual_Target_Node_Features': ['measur', 'tree', 'genet', 'statist', 'machin', 'varianc', 'decis', 'visual', 'bia', 'result', 'term', 'wide', 'field', 'differ'],
    'Factual_Target_Node_Class': 'Theory',
    'Counterfactual_Target_Node_class': 'Neural_Networks',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Natural_Language_Explanation': 'In the factual graph, node 1191 is classified as Theory and is connected to nodes 661, 692, 1053, 1290, and 2423. In the counterfactual graph, node 1191 is reclassified as Neural_Networks and only retains a connection with node 661. The removal of connections with nodes 692, 1053, 1290, and 2423 likely influenced the change in classification.'
}
```

### Natural Language Explanation

In the factual graph, node 1191, titled "Machine Learning Bias, Statistical Bias, and Statistical Variance of Decision Tree Algorithms," is classified as Theory and is connected to nodes 661, 692, 1053, 1290, and 2423. These connections suggest that the node is part of a broader theoretical discussion involving decision trees and statistical biases.

In the counterfactual graph, the same node retains its title and features but is reclassified as Neural_Networks. The primary difference lies in the reduced connectivity; node 1191 now only connects to node 661. The removal of connections with nodes 692, 1053, 1290, and 2423 significantly alters the context and influence of node 1191. 

Nodes 692, 1053, 1290, and 2423 are primarily classified as Theory, indicating a strong theoretical foundation around decision trees and learning algorithms. By removing these connections, the node loses its theoretical grounding and gains a more specialized focus aligned with neural networks, leading to the reclassification as Neural_Networks.

This change highlights the importance of neighboring nodes in influencing the classification of a node within a graph-based learning model. The reduction in theoretical connections shifts the node towards a more specialized classification, demonstrating the impact of structural changes on the overall classification outcome.
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
given the factual graph: The node 71 is a product titled 'Title: Supervised learning from incomplete data via an EM approach  
Abstract: Real-world learning t' with key attributes: involv, likelihood, estim, pattern, dimension, maximum, data, mixtur, set, incomplet, world, presidenti, result, densiti, model, task, framework, base, supervis, may, arbitrari and is connected with the nodes 74, 661 and it is classified as Probabilistic_Methods, it is not the target node. The node 74 is a product titled 'Title: Hierarchical Mixtures of Experts and the EM Algorithm  
Abstract: We present a tree-structure' with key attributes: likelihood, linear, treat, maximum, underli, genet, architectur, hierarch, mixtur, statist, coeffici, particular, compon, presidenti, model, result, gener, supervis, expert and is connected with the nodes 71, 661, 881, 1024 and it is classified as Neural_Networks, it is not the target node. The node 76 is a product titled 'Title: A VIEW OF THE EM ALGORITHM THAT JUSTIFIES INCREMENTAL, SPARSE, AND OTHER VARIANTS  
Abstract:' with key attributes: neg, likelihood, variant, paramet, function, estim, increment, maxim, maximum, spars, genet, respect, data, energi, view, variabl, presidenti, step, result, model, perform and is connected with the node 661 and it is classified as Neural_Networks, it is not the target node. The node 218 is a product titled 'Title: Learning Classification Trees  
Abstract: Algorithms for learning classification trees have h' with key attributes: tree, averag, split, artifici, intellig, genet, smooth, success, classif, year, statist, deriv, mani, techniqu, result, thereaft, bayesian, introduc and is connected with the nodes 378, 1290 and it is classified as Probabilistic_Methods, it is not the target node. The node 296 is a product titled 'Title: Lookahead and Pathology in Decision Tree Induction  
Abstract: The standard approach to decis' with key attributes: limit, optim, tree, systemat, altern, greedi, genet, top, standard, induct, decis, local, node, result, larg, compar, studi, decid and is connected with the nodes 438, 692 and it is classified as Theory, it is not the target node. The node 378 is a product titled 'Title: Mingers, 1989 J. Mingers. An empirical comparison of pruning methods for decision tree induct' with key attributes: empir, domain, tree, barn, share, rule, prune, artifici, intellig, concaten, comparison, machin, induct, categori, decis, improv, multipl, technic, report, theori, method and is connected with the nodes 218, 692, 1238, 1290, 1644 and it is classified as Theory, it is not the target node. The node 423 is a product titled 'Title: LEARNING BAYESIAN NETWORKS WITH LOCAL STRUCTURE  
Abstract: We examine a novel addition to th' with key attributes: network, condit, addit, probabl, data, explicitli, distribut, novel, qualiti, local, structur, result, examin, improv, bayesian, known, method, repres and is connected with the node 1290 and it is classified as Probabilistic_Methods, it is not the target node. The node 429 is a product titled 'Title: Classifiers: A Theoretical and Empirical Study  
Abstract: This paper describes how a competi' with key attributes: empir, tree, approxim, principl, genet, statist, classifi, competit, deriv, decis, solut, describ, result, bayesian, task, famili, experi, compar, studi, theoret, sever and is connected with the node 1290 and it is classified as Probabilistic_Methods, it is not the target node. The node 438 is a product titled 'Title: A System for Induction of Oblique Decision Trees  
Abstract: This article describes a new sys' with key attributes: hyperplan, tree, good, random, split, articl, climb, determinist, form, induct, decis, system, combin, describ, node, result and is connected with the nodes 296, 550, 692 and it is classified as Theory, it is not the target node. The node 550 is a product titled 'Title: LEARNING BY USING DYNAMIC FEATURE COMBINATION AND SELECTION  
Abstract:' with key attributes: dynam, featur, combin, result, select and is connected with the nodes 438, 2423 and it is classified as Theory, it is not the target node. The node 661 is a product titled 'Title: A Statistical Approach to Decision Tree Modeling  
Abstract: A statistical approach to decisi' with key attributes: likelihood, map, fit, estim, measur, tree, good, yield, sequenc, allow, parametr, statist, input, output, decis, process, describ, result, model, gener and is connected with the nodes 71, 74, 76, 1191 and it is classified as Neural_Networks, it is not the target node. The node 692 is a product titled 'Title: Decision Tree Induction: How Effective is the Greedy Heuristic?  
Abstract: Most existing dec' with key attributes: reason, optim, exist, tree, good, split, induc, greedi, believ, produc, induct, decis, local, system, node, effect, attempt, work, everi, current and is connected with the nodes 296, 378, 438, 1191 and it is classified as Theory, it is not the target node. The node 853 is a product titled 'Title: Error-Correcting Output Codes for Local Learners  
Abstract: Error-correcting output codes (E' with key attributes: encod, function, correspond, class, bit, code, genet, est, classif, set, output, learner, local, combin, binari, task, result, partit, repres and is connected with the nodes 1019, 1053, 1732, 2423 and it is classified as Theory, it is not the target node. The node 862 is a product titled 'Title: Language-Independent Data-Oriented Grapheme-to-Phoneme Conversion  
Abstract: We describe an' with key attributes: reason, intrigu, abl, interact, convers, achiev, order, sourc, variou, assum, convert, word, accuraci, better, techniqu, represent, result, perform, base, supervis, method, knowledg and is connected with the nodes 1019, 2423 and it is classified as Case_Based, it is not the target node. The node 881 is a product titled 'Title: Proben1 A Set of Neural Network Benchmark Problems and Benchmarking Rules  
Abstract: Proben1' with key attributes: network, domain, function, pattern, carri, similar, approxim, rule, data, benchmark, classif, set, neural, collect, contain, result, differ, convent and is connected with the nodes 74, 2423 and it is classified as Neural_Networks, it is not the target node. The node 893 is a product titled 'Title: LEARNING LOGICAL EXCEPTIONS IN CHESS  
Abstract: c flMIT Media Lab Perceptual Computing / Lea' with key attributes: logic, result and is connected with the node 1290 and it is classified as Theory, it is not the target node. The node 931 is a product titled 'Title: MAJORITY VOTE CLASSIFIERS: THEORY AND APPLICATIONS  
Abstract: We give an example of a neural' with key attributes: vote, classifi, major, theori, applic and is connected with the nodes 1053, 1463 and it is classified as Theory, it is not the target node. The node 1019 is a product titled 'Title: Bibliography "SMART: Support Management Automated Reasoning Technology for COMPAQ Customer Se' with key attributes: reason, multiresolut, genet, custom, autom, technolog, machin, manag, support, result and is connected with the nodes 853, 862, 1290 and it is classified as Case_Based, it is not the target node. The node 1024 is a product titled 'Title: On learning hierarchical classifications  
Abstract: Many significant real-world classificati' with key attributes: involv, hierarchi, librari, classif, topic, hierarch, exampl, classifi, categori, subject, investig, world, document, mani, signific, task, result, benefit, larg, scheme, potenti and is connected with the nodes 74, 1053 and it is classified as Theory, it is not the target node. The node 1025 is a product titled 'Title: Machine Learning 27(1):51-68, 1997. Predicting nearly as well as the best pruning of a decisi' with key attributes: involv, predict, reduc, tree, best, second, prune, genet, data, typic, machin, decis, process, mani, infer, phase, result, larg, compar and is connected with the nodes 1238, 1290, 1712 and it is classified as Theory, it is not the target node. The node 1053 is a product titled 'Title: Bias Plus Variance Decomposition for Zero-One Loss Functions  
Abstract: We present a bias-va' with key attributes: function, expect, misclassif, serv, quadrat, genet, classif, import, decomposit, varianc, rate, loss, bia, result, commonli, known, supervis, tool, analyz and is connected with the nodes 853, 931, 1024, 1191, 1197, 1463, 1568, 1607 and it is classified as Theory, it is not the target node. The node 1161 is a product titled 'Title: Inductive Learning by Selection of Minimal Complexity Representations  
Abstract: Behavioural' with key attributes: minim, induct, complex, represent, result, select and is connected with the nodes 2423, 2657 and it is classified as Theory, it is not the target node. The node 1191 is a product titled 'Title: Machine Learning Bias, Statistical Bias, and Statistical Variance of Decision Tree Algorithms' with key attributes: measur, tree, genet, statist, machin, varianc, decis, visual, bia, result, term, wide, field, differ and is connected with the nodes 661, 692, 1053, 1290, 2423 and it is classified as Theory, it is the target node. The node 1197 is a product titled 'Title: Why Does Bagging Work? A Bayesian Account and its Implications bagging's success, both in a
A' with key attributes: empir, vote, explan, extra, reduc, bootstrap, implic, altern, success, classif, account, learner, sampl, bag, rate, combin, error, uniform, result, multipl, model, bayesian, databas, base and is connected with the nodes 1053, 1290 and it is classified as Theory, it is not the target node. The node 1226 is a product titled 'Title: On Learning Multiple Descriptions of a Concept  
Abstract: In sparse data environments, great' with key attributes: descript, class, good, achiev, greater, rule, spars, environ, data, classif, set, combin, accuraci, mani, search, multipl, result, gener, concept, stochast, tool, sever and is connected with the node 1290 and it is classified as Rule_Learning, it is not the target node. The node 1238 is a product titled 'Title: On Pruning and Averaging Decision Trees  
Abstract: Pruning a decision tree is considered by' with key attributes: empir, research, domain, tree, averag, prune, altern, noisi, import, receiv, comparison, attent, decis, part, build, mani, recent, consid, perform and is connected with the nodes 378, 1025, 1290 and it is classified as Theory, it is not the target node. The node 1290 is a product titled 'Title: A THEORY OF LEARNING CLASSIFICATION RULES  
Abstract: This chapter takes a different standpoi' with key attributes: rule, classif, result, theori and is connected with the nodes 218, 378, 423, 429, 893, 1019, 1025, 1191, 1197, 1226, 1238, 1644, 1712, 1918, 2080, 2169, 2329 and it is classified as Theory, it is not the target node. The node 1463 is a product titled 'Title: Bias, variance and prediction error for classification rules  
Abstract: We study the notions' with key attributes: predict, estim, bootstrap, rule, natur, notion, classif, decomposit, comprehens, deriv, varianc, follow, illustr, compon, bia, behaviour, describ, error, develop, studi and is connected with the nodes 931, 1053 and it is classified as Theory, it is not the target node. The node 1568 is a product titled 'Title: The Utility of Feature Weighting in Nearest-Neighbor Algorithms  
Abstract: Nearest-neighbor' with key attributes: space, distanc, weight, option, genet, depend, featur, set, investig, util, direct, metric, come, describ, search, result, small, known, heavili, discret and is connected with the node 1053 and it is classified as Theory, it is not the target node. The node 1601 is a product titled 'Title: Learning the Past Tense of English Verbs: The Symbolic Pattern Associator vs. Connectionist M' with key attributes: rosenberg, past, symbol, pattern, acquisit, adequaci, aspect, connectionist, sinc, languag, model, recent, becom, result, associ, gener, heat and is connected with the nodes 1644, 2423 and it is classified as Neural_Networks, it is not the target node. The node 1607 is a product titled 'Title: Characterizing the generalization performance of model selection strategies  
Abstract: We in' with key attributes: class, hypothesi, sequenc, decomposit, essenti, particular, understand, character, varianc, investig, bia, lead, structur, result, strategi, model, task, perform, gener, select and is connected with the node 1053 and it is classified as Theory, it is not the target node. The node 1644 is a product titled 'Title: A Comparative Study of ID3 and Backpropagation for English Text-to-Speech Mapping  
Abstract:' with key attributes: rosenberg, map, code, genet, distribut, comparison, output, backpropag, prop, shown, error, develop, task, result, seattl, consist, perform, compar, stress and is connected with the nodes 378, 1290, 1601, 1732, 2423 and it is classified as Neural_Networks, it is not the target node. The node 1712 is a product titled 'Title: An Efficient Extension to Mixture Techniques for Prediction and Decision Trees  
Abstract: We' with key attributes: extend, onlin, predict, extens, tree, class, weight, alloc, prune, mixtur, effici, decis, maintain, larger, techniqu, includ, method and is connected with the nodes 1025, 1290 and it is classified as Theory, it is not the target node. The node 1732 is a product titled 'Title: Improving the Performance of Radial Basis Function Networks by Learning Center Locations  
Ab' with key attributes: network, function, radial, basi, center, locat, improv, result, perform and is connected with the nodes 853, 1644, 2225, 2423 and it is classified as Neural_Networks, it is not the target node. The node 1918 is a product titled 'Title: Stochastic Logic Programs  
Abstract: One way to represent a machine learning algorithm's bia' with key attributes: taken, space, way, hypothesi, instanc, probabl, ilp, distribut, machin, induct, pair, logic, bia, system, program, result, recent, bayesian, framework, stochast, scheme, howev, repres and is connected with the nodes 1290, 2329 and it is classified as Theory, it is not the target node. The node 2080 is a product titled 'Title: Learning from positive data  
Abstract: Gold showed in 1967 that not even regular grammars ca' with key attributes: alon, grammar, natur, data, exampl, sinc, exactli, posit, regular, support, result, recent, theoret, known, theori, human, identifi and is connected with the nodes 1290, 2329 and it is classified as Theory, it is not the target node. The node 2169 is a product titled 'Title: Theory Refinement on Bayesian Networks  
Abstract: Theory refinement is the task of updating' with key attributes: network, belief, domain, reduc, review, increment, light, updat, refin, statist, case, context, assist, revis, bayesian, task, result, done, uncertainti, automat, theori, expert and is connected with the node 1290 and it is classified as Probabilistic_Methods, it is not the target node. The node 2225 is a product titled 'Title: Error-Correcting Output Coding Corrects Bias and Variance  
Abstract: Previous research has s' with key attributes: research, class, point, code, genet, data, classif, classifi, output, previou, varianc, correct, investig, bia, shown, accuraci, techniqu, result, improv, recent, call, supervis and is connected with the nodes 1732, 2423 and it is classified as Theory, it is not the target node. The node 2329 is a product titled 'Title: Programming Research Group A LEARNABILITY MODEL FOR UNIVERSAL REPRESENTATIONS  
Abstract: Thi' with key attributes: research, group, learnabl, program, represent, model, univers and is connected with the nodes 1290, 1918, 2080 and it is classified as Theory, it is not the target node. The node 2423 is a product titled 'Title: Error-Correcting Output Codes: A General Method for Improving Multiclass Inductive Learning P' with key attributes: involv, function, class, valu, acquir, code, unknown, exampl, set, output, induct, train, program, collect, contain, improv, rang, definit, result, larg, gener, studi, method, discret and is connected with the nodes 550, 853, 862, 881, 1161, 1191, 1601, 1644, 1732, 2225, 2627, 2657 and it is classified as Theory, it is not the target node. The node 2627 is a product titled 'Title: Probability Estimation via Error-Correcting Output Coding  
Abstract: Previous research has s' with key attributes: extend, research, estim, class, point, code, probabl, genet, data, classif, classifi, output, previou, shown, accuraci, techniqu, result, improv, recent, call, supervis and is connected with the node 2423 and it is classified as Theory, it is not the target node. The node 2657 is a product titled 'Title: Learning Complex Boolean Functions: Algorithms and Applications  
Abstract: The most commonly' with key attributes: need, network, abil, implement, function, point, restrict, valu, suit, genet, declar, digit, exampl, neural, complex, direct, oper, boolean, node, model, result, commonli, perform, larg, gener, applic and is connected with the nodes 1161, 2423 and it is classified as Theory, it is not the target node. and given the counterfactual example: The node 71 is a product titled 'Title: Supervised learning from incomplete data via an EM approach  
Abstract: Real-world learning t' with key attributes: involv, likelihood, estim, pattern, dimension, maximum, data, mixtur, set, incomplet, world, presidenti, result, densiti, model, task, framework, base, supervis, may, arbitrari and is connected with the nodes 74, 661 and it is classified as Probabilistic_Methods, it is not the target node. The node 74 is a product titled 'Title: Hierarchical Mixtures of Experts and the EM Algorithm  
Abstract: We present a tree-structure' with key attributes: likelihood, linear, treat, maximum, underli, genet, architectur, hierarch, mixtur, statist, coeffici, particular, compon, presidenti, model, result, gener, supervis, expert and is connected with the nodes 71, 661, 881, 1024 and it is classified as Neural_Networks, it is not the target node. The node 76 is a product titled 'Title: A VIEW OF THE EM ALGORITHM THAT JUSTIFIES INCREMENTAL, SPARSE, AND OTHER VARIANTS  
Abstract:' with key attributes: neg, likelihood, variant, paramet, function, estim, increment, maxim, maximum, spars, genet, respect, data, energi, view, variabl, presidenti, step, result, model, perform and is connected with no other nodes and it is classified as Probabilistic_Methods, it is not the target node. The node 218 is a product titled 'Title: Learning Classification Trees  
Abstract: Algorithms for learning classification trees have h' with key attributes: tree, averag, split, artifici, intellig, genet, smooth, success, classif, year, statist, deriv, mani, techniqu, result, thereaft, bayesian, introduc and is connected with the nodes 378, 1290 and it is classified as Probabilistic_Methods, it is not the target node. The node 296 is a product titled 'Title: Lookahead and Pathology in Decision Tree Induction  
Abstract: The standard approach to decis' with key attributes: limit, optim, tree, systemat, altern, greedi, genet, top, standard, induct, decis, local, node, result, larg, compar, studi, decid and is connected with the nodes 438, 692 and it is classified as Theory, it is not the target node. The node 378 is a product titled 'Title: Mingers, 1989 J. Mingers. An empirical comparison of pruning methods for decision tree induct' with key attributes: empir, domain, tree, barn, share, rule, prune, artifici, intellig, concaten, comparison, machin, induct, categori, decis, improv, multipl, technic, report, theori, method and is connected with the nodes 218, 692, 1238, 1290, 1644 and it is classified as Theory, it is not the target node. The node 423 is a product titled 'Title: LEARNING BAYESIAN NETWORKS WITH LOCAL STRUCTURE  
Abstract: We examine a novel addition to th' with key attributes: network, condit, addit, probabl, data, explicitli, distribut, novel, qualiti, local, structur, result, examin, improv, bayesian, known, method, repres and is connected with the node 1290 and it is classified as Probabilistic_Methods, it is not the target node. The node 429 is a product titled 'Title: Classifiers: A Theoretical and Empirical Study  
Abstract: This paper describes how a competi' with key attributes: empir, tree, approxim, principl, genet, statist, classifi, competit, deriv, decis, solut, describ, result, bayesian, task, famili, experi, compar, studi, theoret, sever and is connected with the node 1290 and it is classified as Probabilistic_Methods, it is not the target node. The node 438 is a product titled 'Title: A System for Induction of Oblique Decision Trees  
Abstract: This article describes a new sys' with key attributes: hyperplan, tree, good, random, split, articl, climb, determinist, form, induct, decis, system, combin, describ, node, result and is connected with the nodes 296, 550, 692 and it is classified as Theory, it is not the target node. The node 550 is a product titled 'Title: LEARNING BY USING DYNAMIC FEATURE COMBINATION AND SELECTION  
Abstract:' with key attributes: dynam, featur, combin, result, select and is connected with the nodes 438, 2423 and it is classified as Theory, it is not the target node. The node 661 is a product titled 'Title: A Statistical Approach to Decision Tree Modeling  
Abstract: A statistical approach to decisi' with key attributes: likelihood, map, fit, estim, measur, tree, good, yield, sequenc, allow, parametr, statist, input, output, decis, process, describ, result, model, gener and is connected with the nodes 71, 74, 1191 and it is classified as Neural_Networks, it is not the target node. The node 692 is a product titled 'Title: Decision Tree Induction: How Effective is the Greedy Heuristic?  
Abstract: Most existing dec' with key attributes: reason, optim, exist, tree, good, split, induc, greedi, believ, produc, induct, decis, local, system, node, effect, attempt, work, everi, current and is connected with the nodes 296, 378, 438 and it is classified as Theory, it is not the target node. The node 853 is a product titled 'Title: Error-Correcting Output Codes for Local Learners  
Abstract: Error-correcting output codes (E' with key attributes: encod, function, correspond, class, bit, code, genet, est, classif, set, output, learner, local, combin, binari, task, result, partit, repres and is connected with the nodes 1019, 1053, 1732, 2423 and it is classified as Theory, it is not the target node. The node 862 is a product titled 'Title: Language-Independent Data-Oriented Grapheme-to-Phoneme Conversion  
Abstract: We describe an' with key attributes: reason, intrigu, abl, interact, convers, achiev, order, sourc, variou, assum, convert, word, accuraci, better, techniqu, represent, result, perform, base, supervis, method, knowledg and is connected with the nodes 1019, 2423 and it is classified as Case_Based, it is not the target node. The node 881 is a product titled 'Title: Proben1 A Set of Neural Network Benchmark Problems and Benchmarking Rules  
Abstract: Proben1' with key attributes: network, domain, function, pattern, carri, similar, approxim, rule, data, benchmark, classif, set, neural, collect, contain, result, differ, convent and is connected with the nodes 74, 2423 and it is classified as Neural_Networks, it is not the target node. The node 893 is a product titled 'Title: LEARNING LOGICAL EXCEPTIONS IN CHESS  
Abstract: c flMIT Media Lab Perceptual Computing / Lea' with key attributes: logic, result and is connected with the node 1290 and it is classified as Theory, it is not the target node. The node 931 is a product titled 'Title: MAJORITY VOTE CLASSIFIERS: THEORY AND APPLICATIONS  
Abstract: We give an example of a neural' with key attributes: vote, classifi, major, theori, applic and is connected with the nodes 1053, 1463 and it is classified as Theory, it is not the target node. The node 1019 is a product titled 'Title: Bibliography "SMART: Support Management Automated Reasoning Technology for COMPAQ Customer Se' with key attributes: reason, multiresolut, genet, custom, autom, technolog, machin, manag, support, result and is connected with the nodes 853, 862, 1290 and it is classified as Case_Based, it is not the target node. The node 1024 is a product titled 'Title: On learning hierarchical classifications  
Abstract: Many significant real-world classificati' with key attributes: involv, hierarchi, librari, classif, topic, hierarch, exampl, classifi, categori, subject, investig, world, document, mani, signific, task, result, benefit, larg, scheme, potenti and is connected with the nodes 74, 1053 and it is classified as Theory, it is not the target node. The node 1025 is a product titled 'Title: Machine Learning 27(1):51-68, 1997. Predicting nearly as well as the best pruning of a decisi' with key attributes: involv, predict, reduc, tree, best, second, prune, genet, data, typic, machin, decis, process, mani, infer, phase, result, larg, compar and is connected with the nodes 1238, 1290, 1712 and it is classified as Theory, it is not the target node. The node 1053 is a product titled 'Title: Bias Plus Variance Decomposition for Zero-One Loss Functions  
Abstract: We present a bias-va' with key attributes: function, expect, misclassif, serv, quadrat, genet, classif, import, decomposit, varianc, rate, loss, bia, result, commonli, known, supervis, tool, analyz and is connected with the nodes 853, 931, 1024, 1197, 1463, 1568, 1607 and it is classified as Theory, it is not the target node. The node 1161 is a product titled 'Title: Inductive Learning by Selection of Minimal Complexity Representations  
Abstract: Behavioural' with key attributes: minim, induct, complex, represent, result, select and is connected with the nodes 2423, 2657 and it is classified as Theory, it is not the target node. The node 1191 is a product titled 'Title: Machine Learning Bias, Statistical Bias, and Statistical Variance of Decision Tree Algorithms' with key attributes: measur, tree, genet, statist, machin, varianc, decis, visual, bia, result, term, wide, field, differ and is connected with the node 661 and it is classified as Neural_Networks, it is the target node. The node 1197 is a product titled 'Title: Why Does Bagging Work? A Bayesian Account and its Implications bagging's success, both in a
A' with key attributes: empir, vote, explan, extra, reduc, bootstrap, implic, altern, success, classif, account, learner, sampl, bag, rate, combin, error, uniform, result, multipl, model, bayesian, databas, base and is connected with the nodes 1053, 1290 and it is classified as Theory, it is not the target node. The node 1226 is a product titled 'Title: On Learning Multiple Descriptions of a Concept  
Abstract: In sparse data environments, great' with key attributes: descript, class, good, achiev, greater, rule, spars, environ, data, classif, set, combin, accuraci, mani, search, multipl, result, gener, concept, stochast, tool, sever and is connected with the node 1290 and it is classified as Rule_Learning, it is not the target node. The node 1238 is a product titled 'Title: On Pruning and Averaging Decision Trees  
Abstract: Pruning a decision tree is considered by' with key attributes: empir, research, domain, tree, averag, prune, altern, noisi, import, receiv, comparison, attent, decis, part, build, mani, recent, consid, perform and is connected with the nodes 378, 1025, 1290 and it is classified as Theory, it is not the target node. The node 1290 is a product titled 'Title: A THEORY OF LEARNING CLASSIFICATION RULES  
Abstract: This chapter takes a different standpoi' with key attributes: rule, classif, result, theori and is connected with the nodes 218, 378, 423, 429, 893, 1019, 1025, 1197, 1226, 1238, 1644, 1712, 1918, 2080, 2169, 2329 and it is classified as Theory, it is not the target node. The node 1463 is a product titled 'Title: Bias, variance and prediction error for classification rules  
Abstract: We study the notions' with key attributes: predict, estim, bootstrap, rule, natur, notion, classif, decomposit, comprehens, deriv, varianc, follow, illustr, compon, bia, behaviour, describ, error, develop, studi and is connected with the nodes 931, 1053 and it is classified as Theory, it is not the target node. The node 1568 is a product titled 'Title: The Utility of Feature Weighting in Nearest-Neighbor Algorithms  
Abstract: Nearest-neighbor' with key attributes: space, distanc, weight, option, genet, depend, featur, set, investig, util, direct, metric, come, describ, search, result, small, known, heavili, discret and is connected with the node 1053 and it is classified as Theory, it is not the target node. The node 1601 is a product titled 'Title: Learning the Past Tense of English Verbs: The Symbolic Pattern Associator vs. Connectionist M' with key attributes: rosenberg, past, symbol, pattern, acquisit, adequaci, aspect, connectionist, sinc, languag, model, recent, becom, result, associ, gener, heat and is connected with the nodes 1644, 2423 and it is classified as Neural_Networks, it is not the target node. The node 1607 is a product titled 'Title: Characterizing the generalization performance of model selection strategies  
Abstract: We in' with key attributes: class, hypothesi, sequenc, decomposit, essenti, particular, understand, character, varianc, investig, bia, lead, structur, result, strategi, model, task, perform, gener, select and is connected with the node 1053 and it is classified as Theory, it is not the target node. The node 1644 is a product titled 'Title: A Comparative Study of ID3 and Backpropagation for English Text-to-Speech Mapping  
Abstract:' with key attributes: rosenberg, map, code, genet, distribut, comparison, output, backpropag, prop, shown, error, develop, task, result, seattl, consist, perform, compar, stress and is connected with the nodes 378, 1290, 1601, 1732, 2423 and it is classified as Neural_Networks, it is not the target node. The node 1712 is a product titled 'Title: An Efficient Extension to Mixture Techniques for Prediction and Decision Trees  
Abstract: We' with key attributes: extend, onlin, predict, extens, tree, class, weight, alloc, prune, mixtur, effici, decis, maintain, larger, techniqu, includ, method and is connected with the nodes 1025, 1290 and it is classified as Theory, it is not the target node. The node 1732 is a product titled 'Title: Improving the Performance of Radial Basis Function Networks by Learning Center Locations  
Ab' with key attributes: network, function, radial, basi, center, locat, improv, result, perform and is connected with the nodes 853, 1644, 2225, 2423 and it is classified as Neural_Networks, it is not the target node. The node 1918 is a product titled 'Title: Stochastic Logic Programs  
Abstract: One way to represent a machine learning algorithm's bia' with key attributes: taken, space, way, hypothesi, instanc, probabl, ilp, distribut, machin, induct, pair, logic, bia, system, program, result, recent, bayesian, framework, stochast, scheme, howev, repres and is connected with the nodes 1290, 2329 and it is classified as Theory, it is not the target node. The node 2080 is a product titled 'Title: Learning from positive data  
Abstract: Gold showed in 1967 that not even regular grammars ca' with key attributes: alon, grammar, natur, data, exampl, sinc, exactli, posit, regular, support, result, recent, theoret, known, theori, human, identifi and is connected with the nodes 1290, 2329 and it is classified as Theory, it is not the target node. The node 2169 is a product titled 'Title: Theory Refinement on Bayesian Networks  
Abstract: Theory refinement is the task of updating' with key attributes: network, belief, domain, reduc, review, increment, light, updat, refin, statist, case, context, assist, revis, bayesian, task, result, done, uncertainti, automat, theori, expert and is connected with the node 1290 and it is classified as Probabilistic_Methods, it is not the target node. The node 2225 is a product titled 'Title: Error-Correcting Output Coding Corrects Bias and Variance  
Abstract: Previous research has s' with key attributes: research, class, point, code, genet, data, classif, classifi, output, previou, varianc, correct, investig, bia, shown, accuraci, techniqu, result, improv, recent, call, supervis and is connected with the nodes 1732, 2423 and it is classified as Theory, it is not the target node. The node 2329 is a product titled 'Title: Programming Research Group A LEARNABILITY MODEL FOR UNIVERSAL REPRESENTATIONS  
Abstract: Thi' with key attributes: research, group, learnabl, program, represent, model, univers and is connected with the nodes 1290, 1918, 2080 and it is classified as Theory, it is not the target node. The node 2423 is a product titled 'Title: Error-Correcting Output Codes: A General Method for Improving Multiclass Inductive Learning P' with key attributes: involv, function, class, valu, acquir, code, unknown, exampl, set, output, induct, train, program, collect, contain, improv, rang, definit, result, larg, gener, studi, method, discret and is connected with the nodes 550, 853, 862, 881, 1161, 1601, 1644, 1732, 2225, 2627, 2657 and it is classified as Theory, it is not the target node. The node 2627 is a product titled 'Title: Probability Estimation via Error-Correcting Output Coding  
Abstract: Previous research has s' with key attributes: extend, research, estim, class, point, code, probabl, genet, data, classif, classifi, output, previou, shown, accuraci, techniqu, result, improv, recent, call, supervis and is connected with the node 2423 and it is classified as Theory, it is not the target node. The node 2657 is a product titled 'Title: Learning Complex Boolean Functions: Algorithms and Applications  
Abstract: The most commonly' with key attributes: need, network, abil, implement, function, point, restrict, valu, suit, genet, declar, digit, exampl, neural, complex, direct, oper, boolean, node, model, result, commonli, perform, larg, gener, applic and is connected with the nodes 1161, 2423 and it is classified as Theory, it is not the target node.
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

- ID: 1191
- Title: Machine Learning Bias, Statistical Bias, and Statistical Variance of Decision Tree Algorithms
- True class (canonical `y`): **Theory**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Theory**
- Prediction recorded by this method's pipeline: **Theory**

Canonical text (`raw_text`):

~~~~~~text
Title: Machine Learning Bias, Statistical Bias, and Statistical Variance of Decision Tree Algorithms  
Abstract: The term "bias" is widely used|and with different meanings|in the fields of machine learning and statistics. This paper clarifies the uses of this term and shows how to measure and visualize the statistical bias and variance of learning algorithms. Statistical bias and variance can be applied to diagnose problems with machine learning bias, and the paper shows four examples of this. Finally, the paper discusses methods of reducing bias and variance. Methods based on voting can reduce variance, and the paper compares Breiman's bagging method and our own tree randomization method for voting decision trees. Both methods uniformly improve performance on data sets from the Irvine repository. Tree randomization yields perfect performance on the Letter Recognition task. A weighted nearest neighbor algorithm based on the infinite bootstrap is also introduced. In general, decision tree algorithms have moderate-to-high variance, so an important implication of this work is that variance|rather than appropriate or inappropriate machine learning bias|is an important cause of poor performance for decision tree algorithms. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 5 nodes

| node id | true class | title |
|---|---|---|
| 661 | Probabilistic_Methods | A Statistical Approach to Decision Tree Modeling |
| 692 | Theory | Decision Tree Induction: How Effective is the Greedy Heuristic? |
| 1053 | Theory | Bias Plus Variance Decomposition for Zero-One Loss Functions |
| 1290 | Theory | A THEORY OF LEARNING CLASSIFICATION RULES |
| 2423 | Theory | Error-Correcting Output Codes: A General Method for Improving Multiclass Inductive Learning Programs |

### 2-hop (shortest distance exactly 2): 36 nodes

| node id | true class | title |
|---|---|---|
| 71 | Probabilistic_Methods | Supervised learning from incomplete data via an EM approach |
| 74 | Probabilistic_Methods | Hierarchical Mixtures of Experts and the EM Algorithm |
| 76 | Probabilistic_Methods | A VIEW OF THE EM ALGORITHM THAT JUSTIFIES INCREMENTAL, SPARSE, AND OTHER VARIANTS |
| 218 | Probabilistic_Methods | Learning Classification Trees |
| 296 | Theory | Lookahead and Pathology in Decision Tree Induction |
| 378 | Theory | Mingers, 1989 J. Mingers. An empirical comparison of pruning methods for decision tree induction. Machine |
| 423 | Probabilistic_Methods | LEARNING BAYESIAN NETWORKS WITH LOCAL STRUCTURE |
| 429 | Probabilistic_Methods | Classifiers: A Theoretical and Empirical Study |
| 438 | Theory | A System for Induction of Oblique Decision Trees |
| 550 | Theory | LEARNING BY USING DYNAMIC FEATURE COMBINATION AND SELECTION |
| 853 | Theory | Error-Correcting Output Codes for Local Learners |
| 862 | Case_Based | Language-Independent Data-Oriented Grapheme-to-Phoneme Conversion |
| 881 | Neural_Networks | Proben1 A Set of Neural Network Benchmark Problems and Benchmarking Rules |
| 893 | Rule_Learning | LEARNING LOGICAL EXCEPTIONS IN CHESS |
| 931 | Theory | MAJORITY VOTE CLASSIFIERS: THEORY AND APPLICATIONS |
| 1019 | Theory | Bibliography "SMART: Support Management Automated Reasoning Technology for COMPAQ Customer Service," "Instance-Based Learning Algorithms," Machine |
| 1024 | Theory | On learning hierarchical classifications |
| 1025 | Theory | Machine Learning 27(1):51-68, 1997. Predicting nearly as well as the best pruning of a decision tree |
| 1161 | Theory | Inductive Learning by Selection of Minimal Complexity Representations |
| 1197 | Theory | Why Does Bagging Work? A Bayesian Account and its Implications bagging's success, both in a |
| 1226 | Rule_Learning | On Learning Multiple Descriptions of a Concept |
| 1238 | Theory | On Pruning and Averaging Decision Trees |
| 1463 | Probabilistic_Methods | Bias, variance and prediction error for classification rules |
| 1568 | Case_Based | The Utility of Feature Weighting in Nearest-Neighbor Algorithms |
| 1601 | Neural_Networks | Learning the Past Tense of English Verbs: The Symbolic Pattern Associator vs. Connectionist Models |
| 1607 | Theory | Characterizing the generalization performance of model selection strategies |
| 1644 | Neural_Networks | A Comparative Study of ID3 and Backpropagation for English Text-to-Speech Mapping |
| 1712 | Theory | An Efficient Extension to Mixture Techniques for Prediction and Decision Trees |
| 1732 | Neural_Networks | Improving the Performance of Radial Basis Function Networks by Learning Center Locations |
| 1918 | Theory | Stochastic Logic Programs |
| 2080 | Theory | Learning from positive data |
| 2169 | Probabilistic_Methods | Theory Refinement on Bayesian Networks |
| 2225 | Theory | Error-Correcting Output Coding Corrects Bias and Variance |
| 2329 | Theory | Programming Research Group A LEARNABILITY MODEL FOR UNIVERSAL REPRESENTATIONS |
| 2627 | Theory | Probability Estimation via Error-Correcting Output Coding |
| 2657 | Theory | Learning Complex Boolean Functions: Algorithms and Applications |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/cora/cf-gnnexplainer-canonical/random_seed_42_*` (key=237).

- Factual class: **Theory**
- Counterfactual class: **Neural_Networks**
- Removed edges (global ids, 5): (76, 661), (692, 1191), (1053, 1191), (1191, 1290), (1191, 2423)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 1191 |
| Factual_Target_Node_Neighbors | 661, 692, 1053, 1290, 2423 |
| Factual_Target_Node_Features | measur, tree, genet, statist, machin, varianc, decis, visual, bia, result, term, wide, result, field, differ |
| Counterfactual_Target_Node_Neighbors | 661 |
| Counterfactual_Target_Node_Features | measur, tree, genet, statist, machin, varianc, decis, visual, bia, result, term, wide, result, field, differ |
| Factual_Target_Node_Class | Theory |
| Counterfactual_Target_Node_class | Neural_Networks |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 692, 1053, 1290, 2423 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 1191 |
| Factual_Target_Node_Neighbors | 661, 692, 1053, 1290, 2423 |
| Factual_Target_Node_Features | measur, tree, genet, statist, machin, varianc, decis, visual, bia, result, term, wide, result, field, differ |
| Counterfactual_Target_Node_Neighbors | 661 |
| Counterfactual_Target_Node_Features | measur, tree, genet, statist, machin, varianc, decis, visual, bia, result, term, wide, result, field, differ |
| Factual_Target_Node_Class | Theory |
| Counterfactual_Target_Node_class | Neural_Networks |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 692, 1053, 1290, 2423 |
| Natural_Language_Explanation | None |
