# Reference packet: CF-GNNExplainer__Qwen-14B__cora__1294

- Method: CF-GNNExplainer; configuration: Qwen-14B; dataset: cora; target node: 1294
- Explanation source: `./robustness_2026-10-30/production_a100/qwen14b_gptq_int4_cora_Response.json` ([255][1])
- Scored scope (what the claims were extracted from): whole output
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

~~~~~~text
To address the provided scenario, we will first populate the `infos` dictionary based on the given factual and counterfactual examples. Then, we will analyze the changes and provide a natural language explanation.

```python
infos = {
    'Target_Node_ID': '1294',
    'Factual_Target_Node_Neighbors': ['915'],
    'Factual_Target_Node_Features': ['methodolog', 'domain', 'exist', 'pattern', 'broad', 'analysi', 'set', 'insight', 'kad', 'decis', 'type', 'requir', 'relev', 'support', 'represent', 'result', 'thereaft', 'formul', 'infer', 'model', 'compar', 'gain', 'knowledg', 'analyz', 'identifi'],
    'Counterfactual_Target_Node_Neighbors': ['915'],
    'Counterfactual_Target_Node_Features': ['methodolog', 'domain', 'exist', 'pattern', 'broad', 'analysi', 'set', 'insight', 'kad', 'decis', 'type', 'requir', 'relev', 'support', 'represent', 'result', 'thereaft', 'formul', 'infer', 'model', 'compar', 'gain', 'knowledg', 'analyz', 'identifi'],
    'Factual_Target_Node_Class': 'Probabilistic_Methods',
    'Counterfactual_Target_Node_class': 'Case_Based',
    'Target_Node_Features_Changed_From_Factual_To_Counterfactual': [],
    'Natural_Language_Explanation': ''
}
```

### Explanation of Changes

In the factual graph, the target node (node 1294) is classified as "Probabilistic_Methods". In the counterfactual graph, the same node is reclassified as "Case_Based". Let's break down the changes and their implications:

#### Node Differences
- **Node ID**: The target node remains the same (node 1294).
- **Neighbors**:
  - **Factual Neighbors**: Node 1294 is connected to node 915.
  - **Counterfactual Neighbors**: Node 1294 is still connected to node 915, but node 1172 is disconnected from both nodes 915 and 1294.

#### Features
- Both the factual and counterfactual representations of node 1294 have identical features, indicating that the change in classification is not due to any alteration in the node's attributes.

#### Classifications
- **Factual Classification**: Node 1294 is classified as "Probabilistic_Methods".
- **Counterfactual Classification**: Node 1294 is reclassified as "Case_Based".

#### Influence of Neighbors
- **Node 915**: This node remains connected to node 1294 in both scenarios. However, the removal of the connection between node 1172 and node 915 might indirectly influence the classification of node 1294.
- **Node 1172**: In the factual graph, node 1172 is connected to node 915, which provides additional context and information that supports the "Probabilistic_Methods" classification. In the counterfactual graph, node 1172 is isolated, potentially reducing the influence of its "Probabilistic_Methods"-related features on node 1294.

### Natural Language Explanation
The target node (node 1294) was initially classified as "Probabilistic_Methods" in the factual graph. In the counterfactual scenario, the same node is reclassified as "Case_Based." Despite having identical features, the change in classification is influenced by the removal of the connection between node 1172 and node 915. This disconnection reduces the influence of node 1172, which is strongly associated with "Probabilistic_Methods," thereby shifting the classification of node 1294 towards "Case_Based."

Thus, the minimal modification required to change the classification of node 1294 from "Probabilistic_Methods" to "Case_Based" involves disconnecting node 1172 from node 915. This highlights the importance of the graph structure in influencing the classification outcomes in graph-based machine learning models like Graph Neural Networks (GNNs).
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
