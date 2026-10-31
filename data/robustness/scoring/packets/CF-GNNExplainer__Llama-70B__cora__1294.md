# Reference packet: CF-GNNExplainer__Llama-70B__cora__1294

- Method: CF-GNNExplainer; configuration: Llama-70B; dataset: cora; target node: 1294
- Explanation source: `./robustness_2026-10-30/llama70b/cf/cora/1294.json` (response)
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
Based on the provided information, we can fill the dictionary as follows:

infos = {
    'Target_Node_ID': 1294,
    'Factual_Target_Node_Neighbors': [915],
    'Factual_Target_Node_Features': ['methodolog', 'domain', 'exist', 'pattern', 'broad', 'analysi', 'set', 'insight', 'kad', 'decis', 'type', 'requir', 'relev', 'support', 'represent', 'result', 'thereaft', 'formul', 'infer', 'model', 'compar', 'gain', 'knowledg', 'analyz', 'identifi'],
    'Counterfactual_Target_Node_Neighbors': [915],
    'Counterfactual_Target_Node_Features': ['methodolog', 'domain', 'exist', 'pattern', 'broad', 'analysi', 'set', 'insight', 'kad', 'decis', 'type', 'requir', 'relev', 'support', 'represent', 'result', 'thereaft', 'formul', 'infer', 'model', 'compar', 'gain', 'knowledg', 'analyz', 'identifi'],
    'Factual_Target_Node_Class': 'Probabilistic_Methods',
    'Counterfactual_Target_Node_class': 'Case_Based',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Node_Differences': [1172],
    'Edge_Differences': [(915, 1172)],
    'Natural_Language_Explanation': ''
}

The natural language explanation for the change in classification for the target node 1294 is as follows:

"The target node 1294 was initially classified as Probabilistic_Methods, but after the modification, it was reclassified as Case_Based. This change occurred because the neighboring node 1172, which was previously connected to node 915, became disconnected from the rest of the graph. As a result, the influence of node 1172's features, which were more closely related to Probabilistic_Methods, was removed from the neighborhood of node 1294. Without this influence, the features of node 1294, which include terms like 'methodolog', 'domain', and 'analysi', became more similar to those typically found in Case_Based papers. Therefore, the model reclassified node 1294 as Case_Based."

Note that the change in classification is not due to any changes in the features of node 1294 itself, but rather due to the changes in its neighborhood and the removal of the influence of node 1172's features.
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
given the factual graph: The node 915 is a product titled 'Title: Abstract  
Abstract: Automated decision making is often complicated by the complexity of the' with key attributes: network, involv, uncertain, descript, variat, formal, basic, underli, integr, autom, categor, contextu, complex, decis, complic, phenomena, propos, represent, result, thereaft, attempt, framework, aris, knowledg, repres and is connected with the nodes 1172, 1294 and it is classified as Probabilistic_Methods, it is not the target node. The node 1172 is a product titled 'Title: Introduction to the Special Section on Knowledge-Based Construction of Probabilistic and Deci' with key attributes: reason, network, uncertain, permit, introduct, intl, diagram, influenc, commun, graphic, specif, flexibl, ieee, kad, decis, significantli, special, techniqu, develop, probabilist, model, construct, knowledg and is connected with the node 915 and it is classified as Probabilistic_Methods, it is not the target node. The node 1294 is a product titled 'Title: Representation Requirements for Supporting Decision Model Formulation  
Abstract: This paper' with key attributes: methodolog, domain, exist, pattern, broad, analysi, set, insight, kad, decis, type, requir, relev, support, represent, result, thereaft, formul, infer, model, compar, gain, knowledg, analyz, identifi and is connected with the node 915 and it is classified as Probabilistic_Methods, it is the target node. and given the counterfactual example: The node 915 is a product titled 'Title: Abstract  
Abstract: Automated decision making is often complicated by the complexity of the' with key attributes: network, involv, uncertain, descript, variat, formal, basic, underli, integr, autom, categor, contextu, complex, decis, complic, phenomena, propos, represent, result, thereaft, attempt, framework, aris, knowledg, repres and is connected with the node 1294 and it is classified as Probabilistic_Methods, it is not the target node. The node 1172 is a product titled 'Title: Introduction to the Special Section on Knowledge-Based Construction of Probabilistic and Deci' with key attributes: reason, network, uncertain, permit, introduct, intl, diagram, influenc, commun, graphic, specif, flexibl, ieee, kad, decis, significantli, special, techniqu, develop, probabilist, model, construct, knowledg and is connected with no other nodes and it is classified as Probabilistic_Methods, it is not the target node. The node 1294 is a product titled 'Title: Representation Requirements for Supporting Decision Model Formulation  
Abstract: This paper' with key attributes: methodolog, domain, exist, pattern, broad, analysi, set, insight, kad, decis, type, requir, relev, support, represent, result, thereaft, formul, infer, model, compar, gain, knowledg, analyz, identifi and is connected with the node 915 and it is classified as Case_Based, it is the target node.
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

- ID: 1294
- Title: Representation Requirements for Supporting Decision Model Formulation
- True class (canonical `y`): **Probabilistic_Methods**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Probabilistic_Methods**
- Prediction recorded by this method's pipeline: **Probabilistic_Methods**

Canonical text (`raw_text`):

~~~~~~text
Title: Representation Requirements for Supporting Decision Model Formulation  
Abstract: This paper outlines a methodology for analyzing the representational support for knowledge-based decision-modeling in a broad domain. A relevant set of inference patterns and knowledge types are identified. By comparing the analysis results to existing representations, some insights are gained into a design approach for integrating categorical and uncertain knowledge in a context sensitive manner.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 1 nodes

| node id | true class | title |
|---|---|---|
| 915 | Probabilistic_Methods | Abstract |

### 2-hop (shortest distance exactly 2): 1 nodes

| node id | true class | title |
|---|---|---|
| 1172 | Probabilistic_Methods | Introduction to the Special Section on Knowledge-Based Construction of Probabilistic and Decision Models (IEEE Transactions |

## 5. Method evidence: counterfactual (CF-GNNExplainer, edge removal)

Source: `./llm-graph-cf/data/cora/cf-gnnexplainer-canonical/random_seed_42_*` (key=255).

- Factual class: **Probabilistic_Methods**
- Counterfactual class: **Case_Based**
- Removed edges (global ids, 1): (915, 1172)

### Factual target dict

| field | value |
|---|---|
| Target_Node_ID | 1294 |
| Factual_Target_Node_Neighbors | 915 |
| Factual_Target_Node_Features | methodolog, domain, exist, pattern, broad, analysi, set, insight, kad, decis, type, requir, relev, support, represent, result, thereaft, result, formul, infer, model, compar, gain, knowledg, analyz, identifi |
| Counterfactual_Target_Node_Neighbors | 915 |
| Counterfactual_Target_Node_Features | methodolog, domain, exist, pattern, broad, analysi, set, insight, kad, decis, type, requir, relev, support, represent, result, thereaft, result, formul, infer, model, compar, gain, knowledg, analyz, identifi |
| Factual_Target_Node_Class | Probabilistic_Methods |
| Counterfactual_Target_Node_class | Case_Based |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |

### Counterfactual target dict

| field | value |
|---|---|
| Target_Node_ID | 1294 |
| Factual_Target_Node_Neighbors | 915 |
| Factual_Target_Node_Features | methodolog, domain, exist, pattern, broad, analysi, set, insight, kad, decis, type, requir, relev, support, represent, result, thereaft, result, formul, infer, model, compar, gain, knowledg, analyz, identifi |
| Counterfactual_Target_Node_Neighbors | 915 |
| Counterfactual_Target_Node_Features | methodolog, domain, exist, pattern, broad, analysi, set, insight, kad, decis, type, requir, relev, support, represent, result, thereaft, result, formul, infer, model, compar, gain, knowledg, analyz, identifi |
| Factual_Target_Node_Class | Probabilistic_Methods |
| Counterfactual_Target_Node_class | Case_Based |
| Target_Node_Features_Changed_From_Factual_To_Counterfactual |  |
| Target_Node_Edges_Removed_From_Factual_To_Counterfactual |  |
| Natural_Language_Explanation | None |
