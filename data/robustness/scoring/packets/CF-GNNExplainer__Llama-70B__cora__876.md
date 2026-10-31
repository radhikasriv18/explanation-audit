# Reference packet: CF-GNNExplainer__Llama-70B__cora__876

- Method: CF-GNNExplainer; configuration: Llama-70B; dataset: cora; target node: 876
- Explanation source: `./robustness_2026-10-30/llama70b/cf/cora/876.json` (response)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, I will fill the dictionary and provide an explanation about the change in classification for the target node.

**Dictionary:**

infos = {
    "Target_Node_ID": 876,
    "Factual_Target_Node_Neighbors": [453, 1006, 1025, 1269],
    "Factual_Target_Node_Features": ["onlin", "predict", "simpl", "sometime", "weight", "genet", "combin", "special", "predictor", "multipl", "result", "famili", "perform", "call", "studi", "expert", "instanc", "sever"],
    "Counterfactual_Target_Node_Neighbors": [],
    "Counterfactual_Target_Node_Features": ["onlin", "predict", "simpl", "sometime", "weight", "genet", "combin", "special", "predictor", "multipl", "result", "famili", "perform", "call", "studi", "expert", "instanc", "sever"],
    "Factual_Target_Node_Class": "Theory",
    "Counterfactual_Target_Node_class": "Neural_Networks",
    "Target_Node_Features_Changed_From_Factual_To_Counterfactual": [],
    "Natural_Language_Explanation": "",
    "Node_Differences": [876],
    "Edge_Differences": [(876, 453), (876, 1006), (876, 1025), (876, 1269)]
}

**Explanation:**

The target node 876 has changed its classification from "Theory" to "Neural_Networks". This change is likely due to the removal of its connections to neighboring nodes 453, 1006, 1025, and 1269, which were previously influencing its classification.

In the factual graph, node 876 was connected to nodes 453, 1006, 1025, and 1269, which are all classified as "Theory". These connections likely contributed to node 876 being classified as "Theory" as well. However, in the counterfactual graph, these connections have been removed, and node 876 is now isolated.

Without the influence of its former neighbors, node 876's features and attributes are re-evaluated, leading to a change in its classification to "Neural_Networks". This new classification is likely due to the presence of features such as "onlin", "predict", and "combin", which are more commonly associated with neural networks.

It's worth noting that the features of node 876 have not changed between the factual and counterfactual graphs, suggesting that the change in classification is primarily due to the change in its neighborhood and the removal of influential connections.
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
given the factual graph: The node 9 is a product titled 'Title: Online Learning versus O*ine Learning  
Abstract: We present an off-line variant of the mista' with key attributes: aim, onlin, variant, versu, space, unknown, instanc, sequenc, dayan, learner, line, trial, model, recent, result, studi, concept, element and is connected with the node 453 and it is classified as Theory, it is not the target node. The node 242 is a product titled 'Title: Learning Markov chains with variable memory length from noisy output  
Abstract: The problem' with key attributes: length, practic, class, hypothesi, underli, noisi, genet, sequenc, data, dna, markov, output, variabl, chain, observ, assum, direct, complic, process, result, speech, model, memori, gener, select, aris and is connected with the nodes 574, 1006 and it is classified as Theory, it is not the target node. The node 418 is a product titled 'Title: Heterogeneous Uncertainty Sampling for Supervised Learning  
Abstract: Uncertainty sampling m' with key attributes: need, uncertain, reduc, class, best, instanc, despit, iter, classifi, previou, train, sampl, label, result, uncertainti, supervis, expert, method, heterogen and is connected with the nodes 1269, 1312 and it is classified as Theory, it is not the target node. The node 453 is a product titled 'Title: How to Use Expert Advice (Extended Abstract)  
Abstract: We analyze algorithms that predict a' with key attributes: extend, predict, assumpt, measur, expect, way, bit, valu, genet, sequenc, analysi, combin, binari, strategi, perform, call, worst, situat, gener, differ, expert, analyz, sever and is connected with the nodes 9, 514, 549, 591, 706, 876, 1025, 1124, 1269, 1358, 1449, 1566, 1661, 1712, 2034, 2059, 2092, 2098, 2099, 2156, 2354, 2455, 2618 and it is classified as Theory, it is not the target node. The node 472 is a product titled 'Title: Category: Control, Navigation and Planning. Key words: Reinforcement learning, Exploration, H' with key attributes: domain, partial, keep, state, hidden, reinforc, navig, plan, explor, statist, effici, categori, observ, idea, word, mani, techniqu, result, control, prefer, key, applic and is connected with the nodes 650, 1006 and it is classified as Reinforcement_Learning, it is not the target node. The node 514 is a product titled 'Title: Gambling in a rigged casino: The adversarial multi-armed bandit problem  
Abstract: In the mu' with key attributes: simpl, maxim, declar, sequenc, adversari, reward, articul, receiv, classic, machin, attent, play, provid, arm, result, trial, model, recent, decid and is connected with the nodes 453, 569 and it is classified as Theory, it is not the target node. The node 549 is a product titled 'Title: Efficient Distribution-free Learning of Probabilistic Concepts  
Abstract: In this paper we i' with key attributes: neg, uncertain, sometim, function, formal, effici, exampl, classifi, input, machin, investig, posit, exhibit, boolean, probabilist, result, model, concept, may and is connected with the nodes 453, 574, 591 and it is classified as Theory, it is not the target node. The node 569 is a product titled 'Title: A decision-theoretic generalization of on-line learning and an application to boosting how th' with key attributes: resourc, predict, extens, dynam, rule, option, broad, set, boost, traffic, line, interpret, multipl, model, consid, result, worst, gener, framework, studi, applic and is connected with the nodes 514, 1025, 1269, 1712, 2099 and it is classified as Theory, it is not the target node. The node 574 is a product titled 'Title: On the Learnability of Discrete Distributions (extended abstract)  
Abstract: We describe a m' with key attributes: extend, distribut, learnabl, discret and is connected with the nodes 242, 549, 1006, 2040, 2360 and it is classified as Theory, it is not the target node. The node 591 is a product titled 'Title: Toward Efficient Agnostic Learning  
Abstract: In this paper we initiate an investigation of' with key attributes: inform, function, assumpt, initi, target, approxim, probabl, effici, significantli, correct, investig, direct, pac, result, model, term, attempt, gener, goal and is connected with the nodes 453, 549, 1358 and it is classified as Theory, it is not the target node. The node 650 is a product titled 'Title: Learning to Use Selective Attention and Short-Term Memory in Sequential Tasks  
Abstract: Thi' with key attributes: advantag, space, perceptu, address, multiresolut, state, hidden, genet, reinforc, attent, sequenti, simultan, combin, result, task, work, memori, larg, disambigu, select and is connected with the nodes 472, 1006 and it is classified as Reinforcement_Learning, it is not the target node. The node 706 is a product titled 'Title: Large Margin Classification Using the Perceptron Algorithm  
Abstract: We introduce and analy' with key attributes: advantag, perceptron, linear, separ, margin, genet, data, classif, take, classifi, combin, introduc, larg, compar, method, analyz and is connected with the node 453 and it is classified as Theory, it is not the target node. The node 876 is a product titled 'Title: Using and combining predictors that specialize  
Abstract: We study online learning algorithm' with key attributes: onlin, predict, simpl, sometim, weight, genet, combin, special, predictor, multipl, result, famili, perform, call, studi, expert, instanc, sever and is connected with the nodes 453, 1006, 1025, 1269 and it is classified as Theory, it is the target node. The node 1006 is a product titled 'Title: Learning Probabilistic Automata with Variable Memory Length  
Abstract: We propose and analyz' with key attributes: length, motiv, automata, genet, distribut, markov, variabl, name, finit, process, describ, propos, probabilist, result, memori, analyz and is connected with the nodes 242, 472, 574, 650, 876, 1025, 2040, 2360 and it is classified as Theory, it is not the target node. The node 1025 is a product titled 'Title: Machine Learning 27(1):51-68, 1997. Predicting nearly as well as the best pruning of a decisi' with key attributes: involv, predict, reduc, tree, best, second, prune, genet, data, typic, machin, decis, process, mani, infer, phase, result, larg, compar and is connected with the nodes 453, 569, 876, 1006, 1238, 1290, 1388, 1449, 1712 and it is classified as Theory, it is not the target node. The node 1124 is a product titled 'Title: ON-LINE LEARNING OF LINEAR FUNCTIONS  
Abstract: We present an algorithm for the on-line lear' with key attributes: optim, function, linear, sum, robust, genet, sequenc, respect, case, variabl, factor, constant, line, bound, shown, squar, error, trial, result and is connected with the nodes 453, 1566 and it is classified as Theory, it is not the target node. The node 1238 is a product titled 'Title: On Pruning and Averaging Decision Trees  
Abstract: Pruning a decision tree is considered by' with key attributes: empir, research, domain, tree, averag, prune, altern, noisi, import, receiv, comparison, attent, decis, part, build, mani, recent, consid, perform and is connected with the nodes 1025, 1290 and it is classified as Theory, it is not the target node. The node 1260 is a product titled 'Title: Transferring and Retraining Learned Information Filters  
Abstract: Any system that learns ho' with key attributes: inform, address, initi, way, user, read, transfer, fashion, train, shortcom, investig, direct, system, document, suffer, result, filter, phase, perform, exploit and is connected with the nodes 1269, 1312 and it is classified as Theory, it is not the target node. The node 1269 is a product titled 'Title: Context-sensitive learning methods for text categorization  
Abstract: Two recently implement' with key attributes: implement, affect, genet, allow, classif, categor, contextu, classifi, machin, presenc, contribut, context, word, evalu, result, construct, larg, expert, method, howev and is connected with the nodes 418, 453, 569, 876, 1260, 1312, 2618 and it is classified as Theory, it is not the target node. The node 1290 is a product titled 'Title: A THEORY OF LEARNING CLASSIFICATION RULES  
Abstract: This chapter takes a different standpoi' with key attributes: rule, classif, result, theori and is connected with the nodes 1025, 1238, 1712 and it is classified as Theory, it is not the target node. The node 1312 is a product titled 'Title: Learning Trees and Rules with Set-valued Features  
Abstract: In most learning systems exampl' with key attributes: extens, vector, tree, valu, rule, instanc, allow, featur, exampl, set, real, compon, system, propos, represent, result, small, repres and is connected with the nodes 418, 1260, 1269 and it is classified as Theory, it is not the target node. The node 1358 is a product titled 'Title: On the Complexity of Function Learning  
Abstract: The majority of results in computational l' with key attributes: function, exist, class, rel, comput, concern, case, particular, major, complex, special, larger, result, rang, concept, known, theori and is connected with the nodes 453, 591, 1661 and it is classified as Theory, it is not the target node. The node 1388 is a product titled 'Title: A Fast, Bottom-Up Decision Tree Pruning Algorithm with Near-Optimal Generalization  
Abstract' with key attributes: prove, guarante, strong, tree, bottom, prune, genet, effici, decis, singl, requir, fast, error, result, given, work, perform, gener, compar, instanc and is connected with the node 1025 and it is classified as Theory, it is not the target node. The node 1449 is a product titled 'Title: Adaptive Mixtures of Probabilistic Transducers  
Abstract: We describe and analyze a mixture' with key attributes: paramet, estim, indic, genet, simul, mixtur, effici, analysi, adapt, line, describ, structur, probabilist, infer, model, result, compar, theoret, supervis, analyz and is connected with the nodes 453, 1025 and it is classified as Theory, it is not the target node. The node 1566 is a product titled 'Title: Worst-case Quadratic Loss Bounds for Prediction Using Linear Functions and Gradient Descent' with key attributes: predict, prove, function, space, linear, sum, quadrat, appli, descent, variou, line, bound, loss, product, squar, error, result, perform, worst, studi, arbitrari and is connected with the nodes 453, 1124 and it is classified as Theory, it is not the target node. The node 1661 is a product titled 'Title: Simulating Access to Hidden Information while Learning  
Abstract: We introduce a new techniq' with key attributes: inform, solv, class, enabl, suffici, hidden, appli, simul, access, read, learner, open, techniqu, queri, result, introduc, concept and is connected with the nodes 453, 1358 and it is classified as Theory, it is not the target node. The node 1712 is a product titled 'Title: An Efficient Extension to Mixture Techniques for Prediction and Decision Trees  
Abstract: We' with key attributes: extend, onlin, predict, extens, tree, class, weight, alloc, prune, mixtur, effici, decis, maintain, larger, techniqu, includ, method and is connected with the nodes 453, 569, 1025, 1290 and it is classified as Theory, it is not the target node. The node 2034 is a product titled 'Title: Update rules for parameter estimation in Bayesian networks  
Abstract: This paper re-examines' with key attributes: network, paramet, estim, updat, valu, rule, hidden, perspect, continu, variabl, line, unifi, provid, result, model, bayesian, work, framework and is connected with the node 453 and it is classified as Theory, it is not the target node. The node 2040 is a product titled 'Title: On the Learnability and Usage of Acyclic Probabilistic Finite Automata  
Abstract: We propose' with key attributes: certain, state, properti, automata, distinguish, genet, distribut, character, learnabl, finit, propos, probabilist, result, work, hard, known, draft, acycl, analyz and is connected with the nodes 574, 1006, 2360 and it is classified as Theory, it is not the target node. The node 2059 is a product titled 'Title: Challenges in Evolving Controllers for Physical Robots  
Abstract: General convergence result' with key attributes: defin, solv, class, perceptron, linear, updat, genet, converg, settl, variou, discrimin, procedur, result, includ, famili, gener, concept and is connected with the node 453 and it is classified as Theory, it is not the target node. The node 2092 is a product titled 'Title: Universal Portfolios With and Without Transaction Costs  
Abstract: A constant rebalanced por' with key attributes: cover, keep, best, period, portfolio, distribut, set, competit, determin, constant, line, cost, strategi, recent, work, univers and is connected with the node 453 and it is classified as Theory, it is not the target node. The node 2098 is a product titled 'Title: Predicting a binary sequence almost as well as the optimal biased coin  
Abstract: We apply t' with key attributes: predict, optim, bay, weight, best, equival, coin, genet, appli, sequenc, case, deriv, exponenti, bias, loss, binari, introduc and is connected with the nodes 453, 2099, 2156 and it is classified as Theory, it is not the target node. The node 2099 is a product titled 'Title: Game Theory, On-line Prediction and Boosting  
Abstract: We study the close connections betwe' with key attributes: predict, connect, review, close, brief, genet, analysi, boost, play, line, describ, repeat, game, result, studi, theori, base, method and is connected with the nodes 453, 569, 2098 and it is classified as Theory, it is not the target node. The node 2156 is a product titled 'Title: WORST CASE PREDICTION OVER SEQUENCES UNDER LOG LOSS  
Abstract: We consider the game of seque' with key attributes: predict, futur, past, assumpt, rel, minim, assign, probabl, sequenc, data, articul, case, observ, sequenti, loss, log, player, probabilist, game, tri, consid, situat, gener, base and is connected with the nodes 453, 2098 and it is classified as Theory, it is not the target node. The node 2354 is a product titled 'Title: The Power of Team Exploration: Two Robots Can Learn Unlabeled Directed Graphs  
Abstract: We' with key attributes: cooper, certain, expect, recogn, polynomi, sequenc, graph, explor, power, time, read, team, type, exactli, direct, robot, node, result, introduc and is connected with the nodes 453, 2360, 2455 and it is classified as Theory, it is not the target node. The node 2360 is a product titled 'Title: Efficient Learning of Typical Finite Automata from Random Walks (Extended Abstract)  
Abstrac' with key attributes: adopt, random, automata, distinguish, underli, genet, determinist, walk, effici, featur, typic, set, finit, label, describ, result, model, worst and is connected with the nodes 574, 1006, 2040, 2354 and it is classified as Theory, it is not the target node. The node 2455 is a product titled 'Title: Learning From a Population of Hypotheses  
Abstract: We introduce a new formal model in which' with key attributes: question, optim, independ, function, motiv, hypothesi, target, popul, formal, approxim, hypothes, unknown, genet, order, statist, combin, collect, multipl, model, run, includ, result, introduc, potenti and is connected with the nodes 453, 2354 and it is classified as Theory, it is not the target node. The node 2618 is a product titled 'Title: Mistake-Driven Learning in Text Categorization  
Abstract: Learning problems in the text proc' with key attributes: dimension, map, domain, variat, measur, space, dimens, properti, spars, instanc, featur, categor, characterist, process, word, result, activ, compar, concept, high and is connected with the nodes 453, 1269 and it is classified as Theory, it is not the target node. and given the counterfactual example: The node 9 is a product titled 'Title: Online Learning versus O*ine Learning  
Abstract: We present an off-line variant of the mista' with key attributes: aim, onlin, variant, versu, space, unknown, instanc, sequenc, dayan, learner, line, trial, model, recent, result, studi, concept, element and is connected with the node 453 and it is classified as Theory, it is not the target node. The node 242 is a product titled 'Title: Learning Markov chains with variable memory length from noisy output  
Abstract: The problem' with key attributes: length, practic, class, hypothesi, underli, noisi, genet, sequenc, data, dna, markov, output, variabl, chain, observ, assum, direct, complic, process, result, speech, model, memori, gener, select, aris and is connected with the nodes 574, 1006 and it is classified as Theory, it is not the target node. The node 418 is a product titled 'Title: Heterogeneous Uncertainty Sampling for Supervised Learning  
Abstract: Uncertainty sampling m' with key attributes: need, uncertain, reduc, class, best, instanc, despit, iter, classifi, previou, train, sampl, label, result, uncertainti, supervis, expert, method, heterogen and is connected with the nodes 1269, 1312 and it is classified as Theory, it is not the target node. The node 453 is a product titled 'Title: How to Use Expert Advice (Extended Abstract)  
Abstract: We analyze algorithms that predict a' with key attributes: extend, predict, assumpt, measur, expect, way, bit, valu, genet, sequenc, analysi, combin, binari, strategi, perform, call, worst, situat, gener, differ, expert, analyz, sever and is connected with the nodes 9, 514, 549, 591, 706, 1025, 1124, 1269, 1358, 1449, 1566, 1661, 1712, 2034, 2059, 2092, 2098, 2099, 2156, 2354, 2455, 2618 and it is classified as Theory, it is not the target node. The node 472 is a product titled 'Title: Category: Control, Navigation and Planning. Key words: Reinforcement learning, Exploration, H' with key attributes: domain, partial, keep, state, hidden, reinforc, navig, plan, explor, statist, effici, categori, observ, idea, word, mani, techniqu, result, control, prefer, key, applic and is connected with the nodes 650, 1006 and it is classified as Reinforcement_Learning, it is not the target node. The node 514 is a product titled 'Title: Gambling in a rigged casino: The adversarial multi-armed bandit problem  
Abstract: In the mu' with key attributes: simpl, maxim, declar, sequenc, adversari, reward, articul, receiv, classic, machin, attent, play, provid, arm, result, trial, model, recent, decid and is connected with the nodes 453, 569 and it is classified as Theory, it is not the target node. The node 549 is a product titled 'Title: Efficient Distribution-free Learning of Probabilistic Concepts  
Abstract: In this paper we i' with key attributes: neg, uncertain, sometim, function, formal, effici, exampl, classifi, input, machin, investig, posit, exhibit, boolean, probabilist, result, model, concept, may and is connected with the nodes 453, 574, 591 and it is classified as Theory, it is not the target node. The node 569 is a product titled 'Title: A decision-theoretic generalization of on-line learning and an application to boosting how th' with key attributes: resourc, predict, extens, dynam, rule, option, broad, set, boost, traffic, line, interpret, multipl, model, consid, result, worst, gener, framework, studi, applic and is connected with the nodes 514, 1025, 1269, 1712, 2099 and it is classified as Theory, it is not the target node. The node 574 is a product titled 'Title: On the Learnability of Discrete Distributions (extended abstract)  
Abstract: We describe a m' with key attributes: extend, distribut, learnabl, discret and is connected with the nodes 242, 549, 1006, 2040, 2360 and it is classified as Theory, it is not the target node. The node 591 is a product titled 'Title: Toward Efficient Agnostic Learning  
Abstract: In this paper we initiate an investigation of' with key attributes: inform, function, assumpt, initi, target, approxim, probabl, effici, significantli, correct, investig, direct, pac, result, model, term, attempt, gener, goal and is connected with the nodes 453, 549, 1358 and it is classified as Theory, it is not the target node. The node 650 is a product titled 'Title: Learning to Use Selective Attention and Short-Term Memory in Sequential Tasks  
Abstract: Thi' with key attributes: advantag, space, perceptu, address, multiresolut, state, hidden, genet, reinforc, attent, sequenti, simultan, combin, result, task, work, memori, larg, disambigu, select and is connected with the nodes 472, 1006 and it is classified as Reinforcement_Learning, it is not the target node. The node 706 is a product titled 'Title: Large Margin Classification Using the Perceptron Algorithm  
Abstract: We introduce and analy' with key attributes: advantag, perceptron, linear, separ, margin, genet, data, classif, take, classifi, combin, introduc, larg, compar, method, analyz and is connected with the node 453 and it is classified as Theory, it is not the target node. The node 876 is a product titled 'Title: Using and combining predictors that specialize  
Abstract: We study online learning algorithm' with key attributes: onlin, predict, simpl, sometim, weight, genet, combin, special, predictor, multipl, result, famili, perform, call, studi, expert, instanc, sever and is connected with no other nodes and it is classified as Neural_Networks, it is the target node. The node 1006 is a product titled 'Title: Learning Probabilistic Automata with Variable Memory Length  
Abstract: We propose and analyz' with key attributes: length, motiv, automata, genet, distribut, markov, variabl, name, finit, process, describ, propos, probabilist, result, memori, analyz and is connected with the nodes 242, 472, 574, 650, 1025, 2040, 2360 and it is classified as Theory, it is not the target node. The node 1025 is a product titled 'Title: Machine Learning 27(1):51-68, 1997. Predicting nearly as well as the best pruning of a decisi' with key attributes: involv, predict, reduc, tree, best, second, prune, genet, data, typic, machin, decis, process, mani, infer, phase, result, larg, compar and is connected with the nodes 453, 569, 1006, 1238, 1290, 1388, 1449, 1712 and it is classified as Theory, it is not the target node. The node 1124 is a product titled 'Title: ON-LINE LEARNING OF LINEAR FUNCTIONS  
Abstract: We present an algorithm for the on-line lear' with key attributes: optim, function, linear, sum, robust, genet, sequenc, respect, case, variabl, factor, constant, line, bound, shown, squar, error, trial, result and is connected with the nodes 453, 1566 and it is classified as Theory, it is not the target node. The node 1238 is a product titled 'Title: On Pruning and Averaging Decision Trees  
Abstract: Pruning a decision tree is considered by' with key attributes: empir, research, domain, tree, averag, prune, altern, noisi, import, receiv, comparison, attent, decis, part, build, mani, recent, consid, perform and is connected with the nodes 1025, 1290 and it is classified as Theory, it is not the target node. The node 1260 is a product titled 'Title: Transferring and Retraining Learned Information Filters  
Abstract: Any system that learns ho' with key attributes: inform, address, initi, way, user, read, transfer, fashion, train, shortcom, investig, direct, system, document, suffer, result, filter, phase, perform, exploit and is connected with the nodes 1269, 1312 and it is classified as Theory, it is not the target node. The node 1269 is a product titled 'Title: Context-sensitive learning methods for text categorization  
Abstract: Two recently implement' with key attributes: implement, affect, genet, allow, classif, categor, contextu, classifi, machin, presenc, contribut, context, word, evalu, result, construct, larg, expert, method, howev and is connected with the nodes 418, 453, 569, 1260, 1312, 2618 and it is classified as Theory, it is not the target node. The node 1290 is a product titled 'Title: A THEORY OF LEARNING CLASSIFICATION RULES  
Abstract: This chapter takes a different standpoi' with key attributes: rule, classif, result, theori and is connected with the nodes 1025, 1238, 1712 and it is classified as Theory, it is not the target node. The node 1312 is a product titled 'Title: Learning Trees and Rules with Set-valued Features  
Abstract: In most learning systems exampl' with key attributes: extens, vector, tree, valu, rule, instanc, allow, featur, exampl, set, real, compon, system, propos, represent, result, small, repres and is connected with the nodes 418, 1260, 1269 and it is classified as Theory, it is not the target node. The node 1358 is a product titled 'Title: On the Complexity of Function Learning  
Abstract: The majority of results in computational l' with key attributes: function, exist, class, rel, comput, concern, case, particular, major, complex, special, larger, result, rang, concept, known, theori and is connected with the nodes 453, 591, 1661 and it is classified as Theory, it is not the target node. The node 1388 is a product titled 'Title: A Fast, Bottom-Up Decision Tree Pruning Algorithm with Near-Optimal Generalization  
Abstract' with key attributes: prove, guarante, strong, tree, bottom, prune, genet, effici, decis, singl, requir, fast, error, result, given, work, perform, gener, compar, instanc and is connected with the node 1025 and it is classified as Theory, it is not the target node. The node 1449 is a product titled 'Title: Adaptive Mixtures of Probabilistic Transducers  
Abstract: We describe and analyze a mixture' with key attributes: paramet, estim, indic, genet, simul, mixtur, effici, analysi, adapt, line, describ, structur, probabilist, infer, model, result, compar, theoret, supervis, analyz and is connected with the nodes 453, 1025 and it is classified as Theory, it is not the target node. The node 1566 is a product titled 'Title: Worst-case Quadratic Loss Bounds for Prediction Using Linear Functions and Gradient Descent' with key attributes: predict, prove, function, space, linear, sum, quadrat, appli, descent, variou, line, bound, loss, product, squar, error, result, perform, worst, studi, arbitrari and is connected with the nodes 453, 1124 and it is classified as Theory, it is not the target node. The node 1661 is a product titled 'Title: Simulating Access to Hidden Information while Learning  
Abstract: We introduce a new techniq' with key attributes: inform, solv, class, enabl, suffici, hidden, appli, simul, access, read, learner, open, techniqu, queri, result, introduc, concept and is connected with the nodes 453, 1358 and it is classified as Theory, it is not the target node. The node 1712 is a product titled 'Title: An Efficient Extension to Mixture Techniques for Prediction and Decision Trees  
Abstract: We' with key attributes: extend, onlin, predict, extens, tree, class, weight, alloc, prune, mixtur, effici, decis, maintain, larger, techniqu, includ, method and is connected with the nodes 453, 569, 1025, 1290 and it is classified as Theory, it is not the target node. The node 2034 is a product titled 'Title: Update rules for parameter estimation in Bayesian networks  
Abstract: This paper re-examines' with key attributes: network, paramet, estim, updat, valu, rule, hidden, perspect, continu, variabl, line, unifi, provid, result, model, bayesian, work, framework and is connected with the node 453 and it is classified as Theory, it is not the target node. The node 2040 is a product titled 'Title: On the Learnability and Usage of Acyclic Probabilistic Finite Automata  
Abstract: We propose' with key attributes: certain, state, properti, automata, distinguish, genet, distribut, character, learnabl, finit, propos, probabilist, result, work, hard, known, draft, acycl, analyz and is connected with the nodes 574, 1006, 2360 and it is classified as Theory, it is not the target node. The node 2059 is a product titled 'Title: Challenges in Evolving Controllers for Physical Robots  
Abstract: General convergence result' with key attributes: defin, solv, class, perceptron, linear, updat, genet, converg, settl, variou, discrimin, procedur, result, includ, famili, gener, concept and is connected with the node 453 and it is classified as Theory, it is not the target node. The node 2092 is a product titled 'Title: Universal Portfolios With and Without Transaction Costs  
Abstract: A constant rebalanced por' with key attributes: cover, keep, best, period, portfolio, distribut, set, competit, determin, constant, line, cost, strategi, recent, work, univers and is connected with the node 453 and it is classified as Theory, it is not the target node. The node 2098 is a product titled 'Title: Predicting a binary sequence almost as well as the optimal biased coin  
Abstract: We apply t' with key attributes: predict, optim, bay, weight, best, equival, coin, genet, appli, sequenc, case, deriv, exponenti, bias, loss, binari, introduc and is connected with the nodes 453, 2099, 2156 and it is classified as Theory, it is not the target node. The node 2099 is a product titled 'Title: Game Theory, On-line Prediction and Boosting  
Abstract: We study the close connections betwe' with key attributes: predict, connect, review, close, brief, genet, analysi, boost, play, line, describ, repeat, game, result, studi, theori, base, method and is connected with the nodes 453, 569, 2098 and it is classified as Theory, it is not the target node. The node 2156 is a product titled 'Title: WORST CASE PREDICTION OVER SEQUENCES UNDER LOG LOSS  
Abstract: We consider the game of seque' with key attributes: predict, futur, past, assumpt, rel, minim, assign, probabl, sequenc, data, articul, case, observ, sequenti, loss, log, player, probabilist, game, tri, consid, situat, gener, base and is connected with the nodes 453, 2098 and it is classified as Theory, it is not the target node. The node 2354 is a product titled 'Title: The Power of Team Exploration: Two Robots Can Learn Unlabeled Directed Graphs  
Abstract: We' with key attributes: cooper, certain, expect, recogn, polynomi, sequenc, graph, explor, power, time, read, team, type, exactli, direct, robot, node, result, introduc and is connected with the nodes 453, 2360, 2455 and it is classified as Theory, it is not the target node. The node 2360 is a product titled 'Title: Efficient Learning of Typical Finite Automata from Random Walks (Extended Abstract)  
Abstrac' with key attributes: adopt, random, automata, distinguish, underli, genet, determinist, walk, effici, featur, typic, set, finit, label, describ, result, model, worst and is connected with the nodes 574, 1006, 2040, 2354 and it is classified as Theory, it is not the target node. The node 2455 is a product titled 'Title: Learning From a Population of Hypotheses  
Abstract: We introduce a new formal model in which' with key attributes: question, optim, independ, function, motiv, hypothesi, target, popul, formal, approxim, hypothes, unknown, genet, order, statist, combin, collect, multipl, model, run, includ, result, introduc, potenti and is connected with the nodes 453, 2354 and it is classified as Theory, it is not the target node. The node 2618 is a product titled 'Title: Mistake-Driven Learning in Text Categorization  
Abstract: Learning problems in the text proc' with key attributes: dimension, map, domain, variat, measur, space, dimens, properti, spars, instanc, featur, categor, characterist, process, word, result, activ, compar, concept, high and is connected with the nodes 453, 1269 and it is classified as Theory, it is not the target node.
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

- ID: 876
- Title: Using and combining predictors that specialize
- True class (canonical `y`): **Theory**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Theory**
- Prediction recorded by this method's pipeline: **Theory**

Canonical text (`raw_text`):

~~~~~~text
Title: Using and combining predictors that specialize  
Abstract: We study online learning algorithms that predict by combining the predictions of several subordinate prediction algorithms, sometimes called experts. These simple algorithms belong to the multiplicative weights family of algorithms. The performance of these algorithms degrades only logarithmically with the number of experts, making them particularly useful in applications where the number of experts is very large. However, in applications such as text categorization, it is often natural for some of the experts to abstain from making predictions on some of the instances. We show how to transform algorithms that assume that all experts are always awake to algorithms that do not require this assumption. We also show how to derive corresponding loss bounds. Our method is very general, and can be applied to a large family of online learning algorithms. We also give applications to various prediction models including decision graphs and switching experts. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 4 nodes

| node id | true class | title |
|---|---|---|
| 453 | Theory | How to Use Expert Advice (Extended Abstract) |
| 1006 | Theory | Learning Probabilistic Automata with Variable Memory Length |
| 1025 | Theory | Machine Learning 27(1):51-68, 1997. Predicting nearly as well as the best pruning of a decision tree |
| 1269 | Theory | Context-sensitive learning methods for text categorization |

### 2-hop (shortest distance exactly 2): 33 nodes

| node id | true class | title |
|---|---|---|
| 9 | Theory | Online Learning versus O*ine Learning |
| 242 | Theory | Learning Markov chains with variable memory length from noisy output |
| 418 | Theory | Heterogeneous Uncertainty Sampling for Supervised Learning |
| 472 | Reinforcement_Learning | Category: Control, Navigation and Planning. Key words: Reinforcement learning, Exploration, Hidden state. Prefer oral presentation. |
| 514 | Theory | Gambling in a rigged casino: The adversarial multi-armed bandit problem |
| 549 | Theory | Efficient Distribution-free Learning of Probabilistic Concepts |
| 569 | Theory | A decision-theoretic generalization of on-line learning and an application to boosting how the weight-update rule |
| 574 | Theory | On the Learnability of Discrete Distributions (extended abstract) |
| 591 | Theory | Toward Efficient Agnostic Learning |
| 650 | Reinforcement_Learning | Learning to Use Selective Attention and Short-Term Memory in Sequential Tasks |
| 706 | Theory | Large Margin Classification Using the Perceptron Algorithm |
| 1124 | Theory | ON-LINE LEARNING OF LINEAR FUNCTIONS |
| 1238 | Theory | On Pruning and Averaging Decision Trees |
| 1260 | Theory | Transferring and Retraining Learned Information Filters |
| 1290 | Theory | A THEORY OF LEARNING CLASSIFICATION RULES |
| 1312 | Rule_Learning | Learning Trees and Rules with Set-valued Features |
| 1358 | Theory | On the Complexity of Function Learning |
| 1388 | Theory | A Fast, Bottom-Up Decision Tree Pruning Algorithm with Near-Optimal Generalization |
| 1449 | Theory | Adaptive Mixtures of Probabilistic Transducers |
| 1566 | Theory | Worst-case Quadratic Loss Bounds for Prediction Using Linear Functions and Gradient Descent |
| 1661 | Theory | Simulating Access to Hidden Information while Learning |
| 1712 | Theory | An Efficient Extension to Mixture Techniques for Prediction and Decision Trees |
| 2034 | Probabilistic_Methods | Update rules for parameter estimation in Bayesian networks |
| 2040 | Theory | On the Learnability and Usage of Acyclic Probabilistic Finite Automata |
| 2059 | Theory | Challenges in Evolving Controllers for Physical Robots |
| 2092 | Theory | Universal Portfolios With and Without Transaction Costs |
| 2098 | Theory | Predicting a binary sequence almost as well as the optimal biased coin |
| 2099 | Theory | Game Theory, On-line Prediction and Boosting |
| 2156 | Theory | WORST CASE PREDICTION OVER SEQUENCES UNDER LOG LOSS |
| 2354 | Theory | The Power of Team Exploration: Two Robots Can Learn Unlabeled Directed Graphs |
| 2360 | Theory | Efficient Learning of Typical Finite Automata from Random Walks (Extended Abstract) |
| 2455 | Theory | Learning From a Population of Hypotheses |
| 2618 | Theory | Mistake-Driven Learning in Text Categorization |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/cora/cf-gnnexplainer-canonical/random_seed_42_*` (key=164).

- Factual class: **Theory**
- Counterfactual class: **Neural_Networks**
- Removed edges (global ids, 4): (453, 876), (876, 1006), (876, 1025), (876, 1269)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 876 |
| Factual_Target_Node_Neighbors | 453, 1006, 1025, 1269 |
| Factual_Target_Node_Features | onlin, predict, simpl, sometim, weight, genet, combin, special, predictor, multipl, result, famili, perform, call, studi, expert, instanc, sever |
| Counterfactual_Target_Node_Neighbors |  |
| Counterfactual_Target_Node_Features | onlin, predict, simpl, sometim, weight, genet, combin, special, predictor, multipl, result, famili, perform, call, studi, expert, instanc, sever |
| Factual_Target_Node_Class | Theory |
| Counterfactual_Target_Node_class | Neural_Networks |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 453, 1006, 1025, 1269 |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 876 |
| Factual_Target_Node_Neighbors | 453, 1006, 1025, 1269 |
| Factual_Target_Node_Features | onlin, predict, simpl, sometim, weight, genet, combin, special, predictor, multipl, result, famili, perform, call, studi, expert, instanc, sever |
| Counterfactual_Target_Node_Neighbors |  |
| Counterfactual_Target_Node_Features | onlin, predict, simpl, sometim, weight, genet, combin, special, predictor, multipl, result, famili, perform, call, studi, expert, instanc, sever |
| Factual_Target_Node_Class | Theory |
| Counterfactual_Target_Node_class | Neural_Networks |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual | 453, 1006, 1025, 1269 |
| Natural_Language_Explanation | None |
