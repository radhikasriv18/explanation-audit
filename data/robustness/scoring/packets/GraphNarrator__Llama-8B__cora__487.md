# Reference packet: GraphNarrator__Llama-8B__cora__487

- Method: GraphNarrator; configuration: Llama-8B; dataset: cora; target node: 487
- Explanation source: `./graphnarrCora/GraphNarrator/outputs/generated_expls-100/78.json` (messages[assistant])
- Scored scope (what the claims were extracted from): ### Free-Text Explanation section
- Built by `robustness_2026-10-30/scoring/build_packets.py` (read-only on all sources, no model call).

## 1. Explanation (full text)

Claims were extracted from the `### Free-Text Explanation` section only; the full assistant message is shown here.

~~~~~~text
### Graph Structure Reconstruction

In the provided verbalized graph, The ROOT node (first line) is the target for classification.
Single-digit indexed nodes are direct neighbors of ROOT.
Double-digit indexed nodes are:
  - Two hops away from ROOT
  - Direct children of their parent node
More digits indexed nodes follow the same principle as described above.

Thus, the graph structure of this verbalized graph is:

- ROOT
  - Node-1
    - Node-1.1
    - Node-1.2
    - Node-1.3
  - Node-2
    - Node-2.1
    - Node-2.2
    - Node-2.3

### Word-Level Evaluation

Detect important terms for the classification label.
Quantitatively, the importance (saliency) scores behind each word in the verbalized graph are calculated by a post-hoc XAI (explanable AI) algorithm.
Semantically, keywords synonymous with or closely related to label, 'Neural Networks' (such as 'networks', 'neural', and 'computational'), are semantically influential in determining the node's relevance to the 'Neural Networks' category.

### Graph-Level Aggregation

Node 1 contains keywords like 'networks' and 'neural', which are directly related to Neural Networks.
Direct neighbors like Node 2, which contains the keyword 'neural', have a substantial influence on ROOT node classification due to their close proximity to the ROOT node.
Indirect neighbors, Nodes-2.1 to Node-2.3, connected through Node 2, contain keywords like 'neural' and 'networks', which further reinforce the classification of ROOT.

### Free-Text Explanation

The classification of ROOT node into the "Neural Networks" category can be explained as follows:

ROOT: The presence of keywords like "networks" and "neural" within ROOT node suggests that the paper is focused on topics central to neural networks, such as computational complexity and analog computation.

  - Node-1: This node discusses the relationship between classical computational models and analog computation, which is relevant to neural networks.
    - Node-1.1 ~ Node-1.3: they are less relevant to neural networks and thus contribute less to the classification.

  - Node-2: This node focuses on neural networks, including evolving networks and backpropagation, which are key concepts in neural networks.
    - Node-2.1: This node discusses the use of genetic algorithms to evolve neural networks, which is a relevant topic in neural networks.
    - Node-2.2: This node explores the sensitivity of backpropagation to initial conditions, which is an important aspect of neural network training.
    - Node-2.3: This node discusses the co-evolution of competing species, which is a relevant topic in neural networks, particularly in the context of evolutionary algorithms.

In summary, the classification of ROOT node into "Neural Networks" is well-supported by the strong presence of key neural network terms within the node itself and its direct connection to Node 2, which also focuses on neural networks.
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-100/78.json`).

**system:**

~~~~~~text
You are a helpful, reliable and responsible AI assistant.
~~~~~~

**user:**

~~~~~~text
The following verbalized graph contains important words in the text of each nodes. These words (each with corresponding importance score in the bracket) contributes to the classification of Node 0 into one of the seven possible categories (['Case Based', 'Genetic Algorithms', 'Neural Networks', 'Probabilistic Methods', 'Reinforcement Learning', 'Rule Learning', 'Theory']). 
Generate a concise, human-readable explanation that justifies the classification result of Node 0 by identifying and explaining the relevant inner-node features (i.e., keywords) and inter-node relationships (i.e., graph structure). The explanation should focus on how these factors contribute to the classification label.

## Example

### Verbalized Graph
<verbalized-graph>ROOT: title(9.13) experiments(7.56) real(2.52) time(2.41) decision(5.20) algorithms(7.18) abstract(12.01) real(3.17) time(2.82) decision(5.46) algorithms(10.39) class(4.34) incremental(2.60) resource(4.50) bounded(5.79) horvitz,(2.67) 89(4.58) anytime(6.66) dean,(4.92) 93(5.03) algorithms(7.94) evaluating(4.75) influence(7.70) diagrams.(10.34) present(16.50) test(6.61) domain(10.50) real(3.11) time(2.89) decision(5.51) algorithms,(5.84) results(6.80) experiments(7.37) several(2.94) real(1.83) time(1.94) decision(4.34) algorithms(5.16) domain.(8.45) results(10.73) demonstrate(14.65) high(5.51) performance(6.46) two(7.53) algorithms,(6.19) decision(4.79) evaluation(4.18) variant(3.69) incremental(2.25) probabilisitic(2.59) inference(6.22) dambrosio,(3.81) 93(4.42) variant(3.46) algorithm(5.22) suggested(3.74) goldszmidt,(3.28) goldszmidt,(2.38) 95(5.24) ],(3.08) pk(2.77) reduced.(6.20) discuss(13.66) implications(9.36) experimental(9.82) results(9.38) explore(8.79) broader(5.65) applicability(3.44) algorithms.(14.64) 
Node-1: title(12.47) learning(12.87) policies(9.77) partially(3.11) observable(2.82) environments(5.58) scaling(9.39) abstract(10.80) partially(4.42) observable(2.62) markov(4.50) decision(5.75) processes(4.53) pomdp(9.69) model(11.47) decision(7.63) problems(7.18) agent(12.00) tries(3.13) maximize(3.05) reward(6.03) face(2.13) limited(2.17) noisy(8.96) sensor(6.27) feedback.(5.17) study(4.64) pomdp(15.31) motivated(4.24) need(2.26) address(2.23) realistic(4.37) problems,(2.86) existing(3.55) techniques(5.16) finding(4.80) optimal(15.47) behavior(5.35) appear(2.47) scale(3.92) well(2.03) unable(3.29) find(3.00) satisfactory(4.62) policies(7.82) problems(4.45) dozen(4.76) states.(10.45) brief(5.22) review(6.37) pomdp(6.59) s,(4.16) paper(10.26) discusses(7.55) several(5.13) simple(4.01) solution(4.55) methods(5.11) shows(4.13) capable(5.08) finding(4.90) near(3.28) optimal(21.93) policies(18.79) selection(5.62) extremely(5.44) small(4.79) pomdp(23.78) taken(4.85) learning(17.53) literature.(7.03) contrast,(4.73) show(3.74) none(6.38) able(2.67) solve(3.53) slightly(3.31) larger(3.38) noisier(3.47) problem(4.47) based(2.61) robot(20.05) navigation.(10.29) find(4.77) combination(3.98) two(3.96) novel(8.04) approaches(5.12) performs(3.93) well(2.61) problems(5.02) suggest(7.78) methods(5.07) scaling(10.48) even(2.50) larger(2.94) complicated(4.88) domains.(8.93) 
Node-1.1: title(0.95) formal(0.36) framework(0.41) speedup(0.35) learning(0.41) problems(0.48) solutions(0.48) abstract(1.14) speedup(0.33) learning(0.61) seeks(0.57) improve(0.27) computational(0.50) efficiency(0.35) problem(0.37) solving(0.41) experience.(0.57) paper,(0.70) develop(0.53) formal(0.40) framework(0.38) learning(0.37) efficient(0.40) problem(0.34) solving(0.32) random(0.54) problems(0.32) solutions.(0.37) apply(0.42) framework(0.47) two(0.45) different(0.24) representations(0.54) learned(0.64) knowledge,(0.41) namely(0.58) control(0.99) rules(0.73) macro(0.54) operators,(0.48) prove(0.58) theorems(0.38) identify(0.28) sufficient(0.22) conditions(0.28) learning(0.38) representation.(0.46) proofs(0.50) constructive(0.81) accompanied(0.47) learning(0.54) algorithms.(0.65) framework(0.83) captures(1.22) empirical(0.63) explanation(0.81) based(0.44) speedup(0.39) learning(0.67) unified(0.80) fashion.(0.54) illustrate(1.50) framework(0.56) implementations(0.79) two(0.46) domains(0.76) symbolic(0.78) integration(0.70) eight(0.65) puzzle.(0.81) work(1.09) integrates(0.74) many(0.54) strands(1.11) experimental(0.75) theoretical(0.55) work(0.49) machine(0.99) learning,(0.66) including(0.61) empirical(0.82) learning(0.59) control(0.85) rules,(0.83) macro(0.81) operator(1.00) learning,(1.31) 
Node-1.2: title(2.30) acting(0.98) uncertainty(2.31) discrete(1.03) bayesian(1.13) models(0.94) mobile(1.03) robot(1.75) navigation(1.12) abstract(2.80) discrete(1.18) bayesian(0.97) models(0.81) used(0.66) model(0.56) uncertainty(1.79) mobile(0.77) robot(1.55) navigation,(0.66) question(0.64) actions(1.17) chosen(0.67) remains(0.72) largely(0.56) unexplored.(0.74) paper(3.63) presents(1.59) optimal(1.17) solution(1.03) problem,(1.09) formulated(0.96) partially(0.40) observable(0.42) markov(0.90) decision(0.74) process.(0.85) since(1.13) solving(1.17) optimal(1.16) control(0.75) policy(1.02) intractable,(0.74) general,(0.82) goes(1.52) explore(2.04) variety(1.42) heuristic(0.84) control(1.05) strategies.(2.28) control(1.40) strategies(3.63) compared(3.99) experimentally,(1.72) simulation(2.58) runs(1.63) robot.(3.17) 
Node-1.3: title(1.50) incremental(0.64) methods(0.50) computing(0.59) bounds(1.09) partially(0.24) observable(0.21) markov(0.31) decision(0.64) processes(0.38) abstract(0.97) partially(0.25) observable(0.21) markov(0.32) decision(0.58) processes(0.36) pomdps(0.21) allow(0.54) one(0.36) model(0.47) complex(0.38) dynamic(0.60) decision(0.76) control(0.38) problems(0.53) include(0.31) action(0.82) outcome(0.55) uncertainty(0.61) imperfect(0.54) observabil(0.22) ity.(0.36) control(0.47) problem(0.67) formulated(0.87) dynamic(0.63) optimization(1.30) problem(0.58) value(0.33) function(0.28) combining(0.60) costs(0.97) rewards(0.92) multiple(0.37) steps.(0.53) paper(1.77) propose,(0.72) analyse(0.35) test(0.45) various(0.60) incremental(0.42) methods(0.43) computing(0.52) bounds(0.49) value(0.23) function(0.23) control(0.54) problems(0.62) infinite(0.38) discounted(0.33) horizon(0.62) criteria.(0.68) methods(0.60) described(0.81) tested(0.68) include(0.68) novel(1.07) incremental(0.44) versions(0.58) grid(1.00) based(0.30) linear(0.29) interpolation(0.22) method(0.39) simple(0.31) lower(0.28) bound(0.53) method(0.38) sondik(0.34) updates.(0.65) work(0.33) arbitrary(0.38) points(0.47) belief(1.86) space(0.42) enhanced(0.56) various(0.51) heuristic(0.29) point(0.31) selection(0.39) strategies.(0.64) also(0.76) introduced(1.55) new(0.88) method(0.62) computing(0.59) initial(0.46) upper(0.46) bound(0.67) fast(0.43) informed(0.56) bound(0.48) method.(0.56) method(0.44) able(0.39) improve(0.45) significantly(0.33) standard(0.37) commonly(0.37) used(0.21) upper(0.28) bound(0.40) computed(0.73) mdp(0.24) based(0.27) method.(0.41) quality(1.09) resulting(1.01) bounds(1.67) tested(1.72) maze(1.68) navigation(1.34) problem(1.05) 20(0.68) states,(0.88) 6(0.37) actions(1.42) 8(0.69) observations.(1.83) 
Node-1.4: title(0.98) learning(1.07) sorting(1.63) decision(1.56) trees(2.00) pomdps(1.04) abstract(1.34) pomdps(1.10) general(0.42) models(0.59) sequential(0.99) decisions(0.93) actions(0.63) observations(1.27) probabilistic.(0.59) many(0.37) problems(1.06) interest(0.66) formulated(0.98) pomdps,(1.14) yet(0.44) use(0.34) pomdps(0.54) limited(0.33) lack(0.32) effective(0.49) algorithms.(0.73) recently(0.51) started(0.30) change(0.25) number(0.21) problems(0.76) robot(1.39) navigation(0.71) planning(0.60) beginning(0.32) formulated(0.70) solved(0.63) pomdps.(0.59) advantage(0.46) pomdp(0.62) approach(0.80) clean(0.50) semantics(0.85) ability(0.28) produce(0.24) principled(0.33) solutions(0.42) integrate(0.41) physical(0.79) information(0.41) gathering(0.50) actions.(0.71) paper(1.89) pursue(0.91) approach(0.72) context(0.64) two(0.59) learning(0.61) tasks(0.60) learning(0.47) sort(0.46) vector(0.57) numbers(0.48) learning(0.67) decision(2.36) trees(1.73) data.(0.63) problems(1.59) formulated(1.32) pomdps(2.25) solved(0.93) general(0.57) pomdp(1.45) algorithm.(0.82) main(0.56) lessons(1.34) results(0.55) 1(0.48) use(0.39) suitable(0.36) heuristics(0.29) representations(0.49) allows(0.42) solution(0.37) sorting(1.14) classification(0.58) pomdps(0.58) non(0.22) trivial(0.45) sizes,(0.42) 2(0.29) quality(0.31) resulting(0.29) solutions(0.38) competitive(0.37) best(0.32) algorithms,(0.42) 3(0.28) problematic(0.52) aspects(0.42) decision(1.53) tree(1.12) learning(0.63) test(0.45) mis(0.29) classification(0.51) costs,(0.36) noisy(0.76) tests,(0.39) missing(0.32) values(0.36) naturally(0.66) accommodated.(0.88) 
Node-1.5: title(0.90) approximating(0.42) optimal(0.69) policies(0.65) partially(1.13) observable(0.41) stochastic(0.50) domains(0.63) abstract(1.25) problem(0.51) making(0.22) optimal(0.40) decisions(0.42) uncertain(1.01) conditions(0.80) central(0.56) artificial(0.82) intelligence.(0.75) state(0.54) world(0.72) known(0.29) times,(0.22) world(0.61) modeled(0.35) markov(0.48) decision(0.48) process(0.35) mdp(0.20) ).(0.23) mdps(0.32) studied(0.34) extensively(0.41) many(0.26) methods(0.42) known(0.30) determining(0.35) optimal(0.44) courses(0.42) action,(0.41) policies.(0.70) realistic(0.58) case(0.39) state(0.70) information(0.67) partially(0.43) observable,(0.45) partially(0.70) observable(0.31) markov(0.36) decision(0.52) processes(0.40) pomdps(0.22) ),(0.26) received(0.36) much(0.26) less(0.35) attention.(0.54) best(0.50) exact(0.48) algorithms(0.98) problems(0.75) inefficient(0.25) space(0.28) time.(0.51) introduce(2.21) smooth(0.81) partially(1.31) observable(0.52) value(0.48) approximation(0.99) spova(0.26) ),(0.35) new(1.42) approximation(1.16) method(0.80) quickly(0.52) yield(0.42) good(0.32) approximations(0.40) improve(0.33) time.(0.30) method(0.45) combined(0.42) reinforcement(0.76) learning(0.55) methods,(0.41) combination(0.44) effective(0.48) test(0.63) cases.(0.57) 
Node-1.6: title(1.58) efficient(1.08) dynamic(0.83) programming(1.15) updates(2.24) partially(0.70) observable(0.55) markov(0.87) decision(1.19) processes(0.86) abstract(1.67) examine(0.99) problem(0.72) performing(0.50) exact(0.70) dynamic(0.57) programming(0.75) updates(1.48) partially(1.26) observable(0.58) markov(0.78) decision(1.58) processes(0.78) pomdps(1.18) computational(1.04) complexity(0.75) viewpoint.(0.80) dynamic(0.72) programming(0.93) updates(1.74) crucial(0.60) operation(0.47) wide(0.25) range(0.29) pomdp(1.34) solution(0.98) methods(0.64) find(0.43) intractable(0.61) perform(0.44) updates(1.31) piecewise(0.41) linear(0.55) convex(1.90) value(0.88) functions(0.54) general(0.61) pomdps.(1.28) offer(1.36) new(1.15) algorithm,(1.71) called(1.15) witness(7.58) algorithm,(2.37) compute(0.78) updated(1.06) value(0.83) functions(0.60) efficiently(0.83) restricted(0.69) class(0.46) pomdps(0.92) number(0.57) linear(0.66) facets(0.70) great.(1.14) compare(1.60) witness(8.22) algorithm(3.33) existing(1.12) algorithms(1.68) analytically(0.87) empirically(0.88) find(0.95) fastest(1.48) algorithm(1.78) wide(0.44) range(0.44) pomdp(3.93) sizes.(1.29) 
Node-2: title(14.46) efficient(7.56) inference(7.77) bayes(5.83) networks(10.92) combinatorial(4.43) optimization(7.56) problem(7.08) abstract(20.68) number(4.43) exact(10.23) algorithms(14.38) developed(3.37) perform(4.58) probabilistic(5.11) inference(6.22) bayesian(9.36) belief(43.68) networks(17.76) recent(7.91) years.(5.88) techniques(5.10) used(3.03) algorithms(12.62) closely(3.05) related(2.74) network(7.05) structures(5.11) easy(2.52) understand(3.09) implement.(8.30) paper,(12.97) consider(9.07) problem(8.09) combinatorial(3.31) optimization(5.31) point(2.81) view(5.13) state(7.40) efficient(7.68) probabilistic(3.59) inference(7.52) belief(36.55) network(12.91) problem(5.46) finding(3.37) optimal(5.77) factoring(4.62) given(3.44) set(2.39) probability(11.09) distributions.(9.15) viewpoint,(7.21) previously(5.96) developed(4.64) algorithms(8.95) seen(6.21) alternate(6.64) factoring(3.80) strategies.(8.92) paper,(9.32) define(20.14) combinatorial(10.03) optimization(13.81) problem,(10.52) optimal(13.04) factoring(4.44) problem,(5.48) discuss(12.35) application(5.49) problem(8.90) belief(42.48) networks.(16.00) show(9.32) optimal(7.28) factoring(4.10) provides(4.40) insight(7.52) key(3.28) elements(3.51) efficient(10.67) probabilistic(5.69) inference,(7.93) demonstrate(13.60) simple,(4.61) easily(2.91) implemented(3.21) algorithms(9.27) excellent(6.64) performance.(9.49) 
Node-2.1: title(0.96) sensitivities(0.32) alternative(0.73) conditional(0.51) probabilities(0.29) bayesian(0.53) belief(1.27) networks(0.93) abstract(1.29) show(0.82) alternative(0.44) way(0.32) representing(0.60) bayesian(0.48) belief(1.94) network(1.51) sensitivities(0.25) probability(0.69) distributions.(0.55) representation(0.53) equivalent(0.34) traditional(1.06) representation(0.54) conditional(0.36) probabilities,(0.26) makes(0.24) dependencies(0.29) nodes(1.00) apparent(0.68) intuitively(0.28) easy(0.28) understand.(0.69) also(0.53) propose(1.01) qr(0.28) matrix(0.71) representation(0.65) sensitivities(0.26) conditional(0.31) probabilities(0.21) efficient,(0.25) memory(0.44) requirements(0.26) computational(0.35) speed,(0.26) traditional(0.64) representation(0.53) computer(0.52) based(0.21) implementations(0.49) probabilistic(0.21) inference.(0.62) use(0.63) sensitivities(0.51) show(1.23) certain(0.44) class(0.42) binary(0.73) networks,(0.74) computation(0.50) time(0.32) approximate(0.64) probabilistic(0.27) inference(0.62) positive(0.23) upper(0.31) bound(0.30) error(0.45) result(0.25) independent(0.32) size(0.26) network.(0.85) finally,(1.12) alternative(0.86) traditional(0.81) algorithms(1.18) use(0.44) conditional(0.79) probabilities,(0.42) describe(1.47) exact(1.02) algorithm(1.54) probabilistic(0.25) inference(0.98) uses(0.48) qr(0.27) representation(0.54) sensitivities(0.45) updates(1.16) probability(0.89) distributions(0.74) nodes(0.93) network(1.40) according(0.75) messages(1.33) neigh(1.47) bors.(0.88) 
Node-2.2: title(1.81) algebraic(1.21) techniques(0.51) efficient(0.73) inference(0.70) bayesian(0.55) networks(1.04) abstract(1.57) number(0.37) exact(0.77) algorithms(1.75) developed(0.34) perform(0.43) probabilistic(0.35) inference(0.59) bayesian(0.50) belief(1.91) networks(1.06) recent(1.20) years.(0.81) algorithms(0.79) use(0.32) graph(0.60) theoretic(0.24) techniques(0.43) analyze(0.40) exploit(0.42) network(0.50) topology.(0.79) paper,(1.07) examine(1.16) problem(0.52) efficient(0.56) probabilistic(0.25) inference(0.57) belief(1.60) network(0.88) combinatorial(0.29) optimization(1.34) problem,(0.45) finding(0.35) optimal(0.55) factoring(0.70) given(0.46) algebraic(0.78) expression(0.59) set(0.20) probability(0.69) distributions.(1.04) define(1.24) combinatorial(0.33) optimization(1.91) problem,(0.57) optimal(0.55) factoring(0.41) problem,(0.40) discuss(1.22) application(0.49) problem(0.46) belief(1.47) networks.(1.33) show(0.80) optimal(0.56) factoring(0.42) provides(0.29) insight(0.47) key(0.24) elements(0.31) efficient(0.89) probabilistic(0.32) inference,(0.53) present(0.61) simple,(0.35) easily(0.28) implemented(0.31) algorithms(0.82) excellent(0.41) performance.(0.61) also(0.64) show(1.07) use(0.41) algebraic(0.88) perspective(0.65) permits(0.76) significant(0.52) extension(0.70) belief(2.80) net(1.18) representation.(1.00) 
Node-2.3: title(1.43) interpretation(0.76) complex(0.42) scenes(0.80) using(0.46) bayesian(0.87) networks(0.89) abstract(1.12) object(0.85) recognition(1.42) systems,(0.46) interactions(0.45) objects(0.43) scene(0.56) ignored(0.38) best(0.26) interpretation(0.69) considered(0.24) set(0.22) hypothesized(0.20) objects(0.39) matches(0.23) greatest(0.26) number(0.20) image(0.50) features.(0.79) show(0.97) image(0.67) interpretation(1.10) cast(0.81) problem(0.77) finding(0.41) probable(0.63) explanation(0.60) mpe(0.22) bayesian(0.69) network(0.67) models(0.30) visual(0.64) physical(0.45) object(0.71) interactions.(0.83) problem(0.59) determine(0.39) exact(0.40) conditional(1.18) probabilities(0.62) network(1.07) shown(0.68) unimportant,(0.35) since(0.29) goal(0.42) find(0.27) probable(0.47) configuration(0.62) objects,(0.48) calculate(0.56) absolute(0.44) probabilities.(0.50) furthermore(1.36) show(0.88) evaluating(0.71) configurations(1.15) feature(1.08) counting(0.49) equivalent(0.59) calculating(0.52) joint(0.44) probability(0.57) configuration(0.93) using(0.42) restricted(0.62) bayesian(0.57) network,(0.48) derive(1.14) assumptions(0.95) probabilities(0.38) necessary(0.30) make(0.23) bayesian(0.66) formulation(0.85) reasonable.(0.80) 
Node-2.4: title(1.04) case(0.45) based(0.40) probability(0.95) factoring(0.36) bayesian(0.53) belief(1.33) networks(1.03) abstract(1.04) bayesian(0.90) network(0.97) inference(0.87) formulated(0.55) combinatorial(0.30) optimization(0.73) problem,(0.41) concerning(0.65) computation(0.55) optimal(0.54) factoring(0.40) distribution(1.54) represented(0.70) net.(2.87) since(0.28) determination(0.37) optimal(0.35) factoring(0.24) computationally(0.29) hard(0.29) problem,(0.32) heuristic(0.33) greedy(1.22) strategies(0.44) able(0.25) find(0.18) approximations(0.31) optimal(0.36) factoring(0.24) usually(0.31) adopted.(0.54) present(0.98) paper(1.04) investigate(0.86) alternative(0.66) approach(0.77) based(0.53) combination(0.44) genetic(1.07) algorithms(0.92) ga(0.80) case(0.49) based(0.74) reasoning(2.04) cbr(0.46) ).(1.16) show(0.69) use(0.44) genetic(1.01) algorithms(0.80) improve(0.37) quality(0.32) computed(0.71) factoring(0.45) case(0.37) static(0.66) strategy(0.44) used(0.25) mpe(0.28) computation(0.74) ),(0.39) combination(0.50) ga(1.10) cbr(0.60) still(0.33) provide(0.35) advantages(0.58) case(0.34) dynamic(0.64) strategies.(0.77) preliminary(1.21) results(0.84) different(0.69) kinds(0.77) nets(3.99) reported.(1.79) 
</verbalized-graph>

### Classification Label
Probabilistic Methods

### Reasoning

0. Graph Structure Reconstruction:

In the provided verbalized graph, The ROOT node (first line) is the target for classification.
Single-digit indexed nodes are direct neighbors of ROOT.
Double-digit indexed nodes are:
  - Two hops away from ROOT
  - Direct children of their parent node
More digits indexed nodes follow the same principle as described above.

Thus, the graph structure of this verbalized graph is:

- ROOT
  - Node-1
    - Node-1.1
    - Node-1.2
    - Node-1.3
    - Node-1.4
    - Node-1.5
    - Node-1.6
  - Node-2
    - Node-2.1
    - Node-2.2
    - Node-2.3
    - Node-2.4

1. Word-Level Evaluation:

Detect important terms for the classification label.
Quantitatively, the importance (saliency) scores behind each word in the verbalized graph are calculated by a post-hoc XAI (explanable AI) algorithm.
Semantically, keywords synonymous with or closely related to label, 'Probabilistic Methods' (such as 'probabilistic', 'probability', and 'inference'), are sementically influential in determining the classification because they directly indicate the node's relevance to the 'Probabilistic Methods' category.

2. Graph-Level Aggregation:

Node 1 does not contain as many directly relevant keywords. Yet, it still discusses POMDPs, which are probabilistic models, indicating that it contributes to the classification in a less significant way. 
Direct neighbors like Node 2, which contains the keyword 'probabilistic', have a substantial influence on ROOT node classification due to their close proximity to the ROOT node.
Indirect neighbors, Nodes-2.1 to Node-2.4, connected through Node 2, contain keywords like 'probabilistic' and 'probability', which further reinforce the classification of ROOT. 
Meanwhile, the indirect neighbors connected through Node 1, Node-1.1 to Node-1.6, are less relevant because they do not include important keywords directly related to 'Probabilistic Methods'.

### Free-Text Explanation
```markdown
The classification of ROOT node into the "Probabilistic Methods" category can be explained as follows:

ROOT: The presence of keywords like "probabilistic" and "inference" within ROOT node suggests that the paper is focused on topics central to probabilistic methods, such as performing probabilistic inference and evaluating influence diagrams.
  - Node-1: While Node 1 focuses on POMDPs, which are also probabilistic models, it is slightly less directly related to the probabilistic inference methods emphasized in ROOT node.
    - Node-1.1 ~ Node-1.6: they are less relevant to probabilistic methods and thus contribute less to the classification.
  - Node-2: This node discusses "probabilistic inference" and "Bayesian networks," both of which are foundational to probabilistic methods. The strong thematic connection between ROOT node and Node 2 reinforces the classification.
    - Node-2.1 ~ Node-2.4: they also discuss probabilistic topics, further supporting the classification.

In summary, the classification of ROOT node into "Probabilistic Methods" is well-supported by the strong presence of key probabilistic terms within the node itself and its direct connection to Node 2, which also focuses on probabilistic inference. Indirect neighbors through Node 2 further reinforce this classification.
```

## Task

### Verbalized Graph
<verbalized-graph>ROOT: title(0.03) language(0.03) dynamical(0.02) system(0.13) abstract(0.02) designers(0.07) across(-0.01) variety(0.02) domains(0.02) engage(0.02) many(0.05) creative(-0.01) activities.(-0.01) since(0.07) much(0.02) creativity(0.01) stems(0.01) using(0.06) old(0.01) solutions(0.10) novel(0.03) ways,(0.02) believe(0.05) case-(0.02) based(0.03) reasoning(0.17) used(0.03) explain(0.08) many(0.07) creative(0.06) design(0.03) processes.(-0.09) 
Node-1: title(0.00) networks(0.01) real(0.00) weights(-0.00) analog(0.00) computational(0.00) complexity(0.00) contrast(0.00) classical(0.00) computational(0.00) models,(0.00) models(0.00) abstract(0.01) report(0.00) sycon-(0.00) 92-(0.00) 05(-0.00) abstract(0.01) pursue(-0.01) particular(-0.01) approach(-0.00) analog(0.00) computation,(-0.00) based(-0.00) dynamical(0.00) systems(-0.00) type(-0.00) used(-0.00) neural(0.01) networks(0.02) research.(0.00) systems(-0.00) fixed(0.00) structure,(0.00) invariant(-0.01) time,(0.00) corresponding(-0.00) unchanging(-0.00) number(0.00) neurons(-0.02) ".(0.01) allowed(-0.00) exponential(-0.01) time(0.00) computation,(0.00) turn(-0.00) unbounded(-0.00) power.(0.00) however,(-0.00) polynomial-(-0.00) time(0.00) constraints(-0.00) limits(-0.00) capabilities,(-0.01) though(0.00) powerful(0.00) turing(0.01) machines.(-0.01) similar(-0.01) restricted(-0.00) model(-0.01) shown(-0.00) polynomial-(-0.00) time(-0.00) equivalent(-0.00) classical(-0.00) digital(0.00) computation(-0.00) previous(0.01) work(-0.00) 17(0.00) ].(0.00) moreover,(-0.01) precise(0.00) correspondence(-0.01) nets(-0.01) standard(0.00) non-(0.00) uniform(-0.00) circuits(-0.00) equivalent(-0.00) resources,(-0.00) consequence(0.00) one(-0.00) lower(-0.00) bound(0.00) constraints(-0.00) compute.(-0.00) relationship(-0.00) perhaps(0.00) surprising(-0.00) since(0.00) analog(-0.00) devices(0.00) change(0.00) manner(0.00) input(-0.00) size.(0.00) note(-0.01) networks(0.01) likely(-0.00) solve(-0.00) polynomially(0.00) np-(-0.00) hard(0.00) problems,(0.00) equality(-0.01) p(0.01) np(-0.00) model(-0.01) implies(0.00) almost(-0.00) complete(0.00) collapse(-0.00) standard(0.00) polynomial(-0.00) hierarchy.(0.00) 
Node-2: title(0.01) learning(-0.03) evolution(-0.03) neural(-0.07) networks(-0.05) abstract(0.04) dimacs(-0.01) technical(-0.03) report(-0.06) 96-(-0.01) 56(0.01) december(-0.01) 1996(-0.03) 
Node-2.1: title(0.00) evolving(0.00) networks(0.00) using(0.00) genetic(0.00) algorithm(0.00) connectionist(0.00) learning(0.00) abstract(0.00) pilot(-0.00) study(0.00) described(0.00) practical(0.00) application(0.00) artificial(0.00) neural(0.00) networks.(-0.00) limit(0.00) cycle(0.00) attitude(0.00) control(0.00) satellite(0.00) selected(0.00) test(0.00) case.(-0.00) one(0.00) sources(0.00) limit(0.00) cycle(0.00) position(0.00) dependent(0.00) error(0.00) observed(-0.00) attitude.(-0.00) reinforcement(0.00) learning(0.00) method(0.00) selected,(0.00) able(0.00) adapt(-0.00) controller(0.00) cost(0.00) function(0.00) optimised.(-0.00) estimate(-0.00) cost(-0.00) function(0.00) learned(-0.00) neural(0.00) critic(-0.00) '.(-0.00) approach,(-0.00) estimated(0.00) cost(-0.00) function(-0.00) directly(-0.00) represented(-0.00) function(-0.00) parameters(0.00) linear(-0.00) controller.(0.00) critic(-0.00) implemented(-0.00) cmac(-0.00) network.(0.00) results(0.00) simulations(0.00) show(0.00) method(0.00) able(0.00) find(0.00) optimal(-0.00) parameters(0.00) without(0.00) unstable(0.00) behaviour.(-0.00) particular(-0.00) case(0.00) large(-0.00) discontinuities(0.00) attitude(-0.00) measurements,(0.00) method(0.00) shows(0.00) clear(0.00) improvement(0.00) compared(-0.00) conventional(-0.00) approach(0.00) rms(0.00) attitude(0.00) error(0.00) decreases(0.00) approximately(0.00) 30(0.00) %.(-0.00) 
Node-2.2: title(0.00) back(-0.00) propagation(0.00) sensitive(0.00) initial(-0.00) conditions(-0.00) abstract(0.00) paper(-0.00) explores(0.00) effect(0.00) initial(-0.00) weight(-0.00) selection(-0.00) feed-(-0.00) forward(-0.00) networks(-0.00) learning(0.00) simple(0.00) functions(-0.00) back-(0.00) propagation(0.00) technique.(-0.00) first(0.00) demonstrate,(0.00) use(0.00) monte(0.00) carlo(0.00) techniques,(0.00) magnitude(0.00) initial(-0.00) condition(0.00) vector(0.00) weight(0.00) space(-0.00) significant(-0.00) parameter(0.00) convergence(-0.00) time(0.00) variability.(0.00) order(0.00) understand(0.00) result,(0.00) additional(-0.00) deterministic(0.00) experiments(0.00) performed.(-0.00) results(0.00) experiments(0.00) demonstrate(0.00) extreme(0.00) sensitivity(0.00) back(0.00) propagation(0.00) initial(0.00) weight(0.00) configuration.(-0.00) 
Node-2.3: title(0.00) adaptive(-0.00) behavior(-0.00) competing(0.00) co-(0.00) evolving(0.00) species(-0.00) abstract(0.00) co-(0.00) evolution(0.00) competitive(-0.00) species(-0.00) provides(0.00) interesting(0.00) testbed(0.00) study(0.00) role(-0.00) adaptive(-0.00) behavior(-0.00) provides(0.00) unpredictable(-0.00) dynamic(0.00) environments.(0.00) paper(0.00) experimentally(-0.00) investigate(-0.00) arguments(0.00) co-(0.00) evolution(0.00) different(0.00) adaptive(-0.00) protean(-0.00) behaviors(-0.00) competing(-0.00) species(0.00) predators(-0.00) preys.(0.00) species(-0.00) implemented(0.00) simulated(-0.00) mobile(0.00) robots(0.00) kheperas(-0.00) infrared(0.00) proximity(-0.00) sensors,(-0.00) predator(-0.00) additional(0.00) vision(-0.00) module(0.00) whereas(-0.00) prey(-0.00) maximum(0.00) speed(-0.00) set(-0.00) twice(0.00) predator.(0.00) different(0.00) types(0.00) variability(-0.00) life(0.00) neurocontrollers(-0.00) architecture(-0.00) genetic(0.00) length(0.00) compared.(-0.00) shown(-0.00) simple(0.00) forms(-0.00) pro-(0.00) teanism(-0.00) affect(-0.00) co-(0.00) evolutionary(0.00) dynamics(-0.00) preys(-0.00) rather(0.00) exploit(0.00) noisy(0.00) controllers(0.00) generate(0.00) random(0.00) trajectories,(0.00) whereas(0.00) predators(-0.00) benefit(0.00) directional-(-0.00) change(0.00) cont</verbalized-graph>

### Classification Label
Neural_Networks

### Reasoning

### Free-Text Explanation

(P.S.: 1. make sure to complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance to generate the better explanation. However, it is not necessary to directly quote the saliency score.
3. use the *whole* graph structure you constructed during reasoning for the format of the explanation. Indents and node indexes are necessary, which representing the hierarchy of the graph.)

~~~~~~

## 3. Target node

- ID: 487
- Title: Language as a dynamical system
- True class (canonical `y`): **Neural_Networks**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Neural_Networks**
- Prediction recorded by this method's pipeline: **Neural_Networks**

Canonical text (`raw_text`):

~~~~~~text
Title: Language as a dynamical system  
Abstract: Designers across a variety of domains engage in many of the same creative activities. Since much creativity stems from using old solutions in novel ways, we believe that case-based reasoning can be used to explain many creative design processes. 
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 2 nodes

| node id | true class | title |
|---|---|---|
| 291 | Neural_Networks | NETWORKS WITH REAL WEIGHTS: ANALOG COMPUTATIONAL COMPLEXITY In contrast to classical computational models, the models |
| 538 | Genetic_Algorithms | Learning and evolution in neural networks |

### 2-hop (shortest distance exactly 2): 10 nodes

| node id | true class | title |
|---|---|---|
| 15 | Neural_Networks | Back Propagation is Sensitive to Initial Conditions |
| 129 | Genetic_Algorithms | Evolving Networks: Using the Genetic Algorithm with Connectionist Learning |
| 402 | Genetic_Algorithms | The Evolutionary Cost of Learning |
| 1036 | Genetic_Algorithms | Adaptive Behavior in Competing Co-Evolving Species |
| 1204 | Genetic_Algorithms | The Role of Development in Genetic Algorithms |
| 1689 | Genetic_Algorithms | Selection for Wandering Behavior in a Small Robot |
| 1738 | Genetic_Algorithms | Evolving nonTrivial Behaviors on Real Robots: an Autonomous Robot that Picks up Objects |
| 2165 | Genetic_Algorithms | Auto-teaching: networks that develop their own teaching input |
| 2193 | Genetic_Algorithms | Growing neural networks |
| 2309 | Reinforcement_Learning | EVOLVING SENSORS IN ENVIRONMENTS OF CONTROLLED COMPLEXITY |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_cora_eval/78.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Neural_Networks**, ground truth = **Neural_Networks**.
The verbalized graph is 13909 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 487 | 49 | 0.1733 | yes |
| Node-1 | 1 | 291 | 203 | 0.0182 | yes |
| Node-2 | 2 | 538 | 17 | 0.0354 | yes |
| Node-2.1 | 3 | 129 | 170 | 0.0022 | yes |
| Node-2.2 | 4 | 15 | 92 | 0.0027 | yes |
| Node-2.3 | 5 | 1036 | 147 | 0.0015 | yes |
| Node-2.4 | 6 | 1204 | 165 | 0.0018 | no |
| Node-2.5 | 7 | 1689 | 172 | 0.0018 | no |
| Node-2.6 | 8 | 1738 | 126 | 0.0048 | no |
| Node-2.7 | 9 | 2165 | 122 | 0.0025 | no |
| Node-2.8 | 10 | 2193 | 112 | 0.0041 | no |
| Node-2.9 | 11 | 2309 | 223 | 0.0026 | no |

Subgraph edges (src -> dst, as stored): Node-1->ROOT, Node-2->Node-2.1, Node-2->Node-2.2, Node-2->Node-2.3, Node-2->Node-2.4, Node-2->Node-2.5, Node-2->Node-2.6, Node-2->Node-2.7, Node-2->Node-2.8, Node-2->Node-2.9, Node-2->ROOT, Node-2.1->Node-2, Node-2.2->Node-2, Node-2.3->Node-2, Node-2.4->Node-2, Node-2.5->Node-2, Node-2.6->Node-2, Node-2.7->Node-2, Node-2.8->Node-2, Node-2.9->Node-2, ROOT->Node-1, ROOT->Node-2

### Tokens and scores

**ROOT** (global 487):

~~~~~~text
title (0.0296) : (0.0879) language (0.0344) as (0.0568) a (0.0092) dynamical (0.0167) system (0.1290) abstract (0.0226) : (0.0317) designers (0.0726) across (-0.0128) a (0.0099) variety (0.0198) of (0.0270) domains (0.0192) engage (0.0156) in (0.0029) many (0.0469) of (0.0195) the (0.0173) same (0.0231) creative (-0.0097) activities. (-0.0057) since (0.0696) much (0.0220) creativity (0.0060) stems (0.0112) from (0.0025) using (0.0611) old (0.0126) solutions (0.1011) in (0.0139) novel (0.0294) ways, (0.0161) we (0.1151) believe (0.0517) that (0.0672) case- (0.0238) based (0.0257) reasoning (0.1733) can (0.0311) be (0.0375) used (0.0327) to (0.0227) explain (0.0798) many (0.0720) creative (0.0615) design (0.0279) processes. (-0.0905)
~~~~~~

**Node-1** (global 291):

~~~~~~text
title (0.0027) : (-0.0088) networks (0.0147) with (0.0031) real (0.0030) weights (-0.0040) : (-0.0002) analog (0.0013) computational (0.0040) complexity (0.0014) in (-0.0003) contrast (0.0017) to (-0.0016) classical (0.0014) computational (0.0020) models, (0.0040) the (-0.0001) models (0.0015) abstract (0.0057) : (-0.0007) report (0.0028) sycon- (0.0004) 92- (0.0022) 05 (-0.0040) abstract (0.0073) we (0.0033) pursue (-0.0075) a (0.0182) particular (-0.0092) approach (-0.0044) to (-0.0027) analog (0.0009) computation, (-0.0003) based (-0.0010) on (-0.0006) dynamical (0.0001) systems (-0.0035) of (-0.0013) the (-0.0005) type (-0.0001) used (-0.0016) in (0.0017) neural (0.0052) networks (0.0150) research. (0.0048) our (-0.0070) systems (-0.0001) have (-0.0032) a (0.0001) fixed (0.0008) structure, (0.0000) invariant (-0.0081) in (0.0007) time, (0.0027) corresponding (-0.0025) to (-0.0010) an (0.0020) unchanging (-0.0017) number (0.0044) of (-0.0008) " (0.0041) neurons (-0.0209) ". (0.0115) if (-0.0103) allowed (-0.0018) exponential (-0.0065) time (0.0005) for (0.0005) computation, (0.0021) they (-0.0011) turn (-0.0003) out (0.0014) to (-0.0007) have (-0.0018) unbounded (-0.0001) power. (0.0015) however, (-0.0003) under (0.0006) polynomial- (-0.0039) time (0.0012) constraints (-0.0041) there (-0.0021) are (-0.0015) limits (-0.0029) on (-0.0003) their (0.0014) capabilities, (-0.0087) though (0.0033) being (-0.0018) more (0.0030) powerful (0.0010) than (0.0005) turing (0.0111) machines. (-0.0113) ( (0.0101) a (-0.0058) similar (-0.0063) but (-0.0032) more (-0.0028) restricted (-0.0036) model (-0.0055) was (-0.0012) shown (-0.0009) to (-0.0026) be (0.0002) polynomial- (-0.0001) time (-0.0032) equivalent (-0.0028) to (-0.0046) classical (-0.0032) digital (0.0019) computation (-0.0036) in (-0.0061) the (0.0033) previous (0.0053) work (-0.0016) [ (-0.0081) 17 (0.0004) ]. (0.0011) ) (-0.0026) moreover, (-0.0069) there (-0.0002) is (0.0013) a (0.0025) precise (0.0004) correspondence (-0.0073) between (0.0042) nets (-0.0102) and (0.0137) standard (0.0010) non- (0.0012) uniform (-0.0040) circuits (-0.0046) with (0.0016) equivalent (-0.0002) resources, (-0.0002) and (-0.0001) as (0.0019) a (0.0000) consequence (0.0002) one (-0.0025) has (-0.0048) lower (-0.0022) bound (0.0028) constraints (-0.0022) on (-0.0001) what (-0.0006) they (-0.0002) can (0.0009) compute. (-0.0034) this (-0.0004) relationship (-0.0019) is (-0.0024) perhaps (0.0025) surprising (-0.0001) since (0.0004) our (0.0017) analog (-0.0048) devices (0.0014) do (0.0016) not (-0.0005) change (0.0012) in (-0.0010) any (-0.0005) manner (0.0008) with (-0.0023) input (-0.0002) size. (0.0008) we (0.0056) note (-0.0082) that (0.0023) these (-0.0026) networks (0.0059) are (-0.0026) not (-0.0021) likely (-0.0029) to (-0.0029) solve (-0.0002) polynomially (0.0004) np- (-0.0024) hard (0.0013) problems, (0.0014) as (0.0069) the (-0.0004) equality (-0.0066) " (0.0008) p (0.0084) = (0.0028) np (-0.0032) " (0.0010) in (0.0014) our (0.0006) model (-0.0065) implies (0.0036) the (0.0018) almost (-0.0002) complete (0.0005) collapse (-0.0029) of (-0.0003) the (0.0017) standard (0.0022) polynomial (-0.0010) hierarchy. (0.0001)
~~~~~~

**Node-2** (global 538):

~~~~~~text
title (0.0070) : (-0.0386) learning (-0.0335) and (-0.0095) evolution (-0.0297) in (-0.0211) neural (-0.0699) networks (-0.0506) abstract (0.0354) : (0.0085) dimacs (-0.0124) technical (-0.0274) report (-0.0644) 96- (-0.0124) 56 (0.0113) december (-0.0073) 1996 (-0.0316)
~~~~~~

**Node-2.1** (global 129):

~~~~~~text
title (0.0008) : (0.0004) evolving (0.0007) networks (0.0009) : (0.0004) using (0.0009) the (-0.0005) genetic (0.0006) algorithm (0.0010) with (-0.0005) connectionist (0.0004) learning (0.0009) abstract (0.0005) : (0.0009) a (0.0003) pilot (-0.0003) study (0.0000) is (0.0003) described (0.0000) on (0.0001) the (0.0003) practical (0.0004) application (0.0006) of (-0.0000) artificial (0.0013) neural (0.0005) networks. (-0.0008) the (0.0000) limit (0.0000) cycle (0.0003) of (0.0003) the (0.0001) attitude (0.0007) control (0.0002) of (0.0005) a (-0.0003) satellite (0.0002) is (0.0007) selected (0.0006) as (0.0002) the (-0.0002) test (0.0007) case. (-0.0022) one (0.0006) of (-0.0003) the (-0.0004) sources (0.0002) of (0.0000) the (-0.0002) limit (0.0002) cycle (0.0002) is (0.0005) a (-0.0002) position (0.0003) dependent (0.0005) error (0.0001) in (-0.0001) the (0.0000) observed (-0.0003) attitude. (-0.0022) a (0.0004) reinforcement (0.0007) learning (0.0007) method (0.0005) is (0.0002) selected, (0.0005) which (0.0000) is (0.0003) able (0.0002) to (-0.0001) adapt (-0.0006) a (-0.0003) controller (0.0008) such (-0.0003) that (-0.0002) a (-0.0003) cost (0.0003) function (0.0003) is (0.0001) optimised. (-0.0002) an (0.0001) estimate (-0.0007) of (-0.0002) the (0.0002) cost (-0.0011) function (0.0004) is (0.0002) learned (-0.0002) by (-0.0003) a (0.0002) neural (0.0008) ` (-0.0000) critic (-0.0007) '. (-0.0014) in (-0.0015) our (0.0018) approach, (-0.0000) the (-0.0007) estimated (0.0008) cost (-0.0011) function (-0.0002) is (0.0003) directly (-0.0007) represented (-0.0009) as (-0.0008) a (-0.0005) function (-0.0005) of (-0.0003) the (-0.0003) parameters (0.0003) of (-0.0004) a (-0.0003) linear (-0.0003) controller. (0.0008) the (0.0000) critic (-0.0006) is (-0.0001) implemented (-0.0001) as (-0.0002) a (0.0002) cmac (-0.0002) network. (0.0002) results (0.0007) from (0.0002) simulations (0.0004) show (0.0006) that (0.0012) the (0.0006) method (0.0001) is (0.0006) able (0.0001) to (0.0002) find (0.0004) optimal (-0.0003) parameters (0.0008) without (0.0001) unstable (0.0002) behaviour. (-0.0002) in (-0.0001) particular (-0.0005) in (0.0001) the (0.0001) case (0.0004) of (0.0001) large (-0.0000) discontinuities (0.0006) in (0.0001) the (0.0003) attitude (-0.0007) measurements, (0.0002) the (0.0005) method (0.0006) shows (0.0002) a (-0.0003) clear (0.0007) improvement (0.0003) compared (-0.0002) to (-0.0001) the (0.0001) conventional (-0.0006) approach (0.0022) : (0.0011) the (0.0004) rms (0.0006) attitude (0.0014) error (0.0006) decreases (0.0004) approximately (0.0000) 30 (0.0014) %. (-0.0007)
~~~~~~

**Node-2.2** (global 15):

~~~~~~text
title (0.0019) : (0.0012) back (-0.0002) propagation (0.0000) is (0.0006) sensitive (0.0006) to (0.0006) initial (-0.0019) conditions (-0.0006) abstract (0.0018) : (-0.0015) this (-0.0005) paper (-0.0009) explores (0.0008) the (-0.0021) effect (0.0002) of (0.0002) initial (-0.0009) weight (-0.0007) selection (-0.0002) on (0.0001) feed- (-0.0004) forward (-0.0007) networks (-0.0018) learning (0.0019) simple (0.0012) functions (-0.0002) with (0.0004) the (-0.0005) back- (0.0001) propagation (0.0006) technique. (-0.0024) we (-0.0006) first (0.0006) demonstrate, (0.0014) through (-0.0004) the (-0.0001) use (0.0000) of (0.0002) monte (0.0010) carlo (0.0001) techniques, (0.0010) that (0.0007) the (-0.0002) magnitude (0.0011) of (0.0007) the (0.0001) initial (-0.0001) condition (0.0004) vector (0.0009) ( (0.0013) in (0.0006) weight (0.0005) space (-0.0001) ) (0.0012) is (0.0002) a (-0.0002) very (0.0002) significant (-0.0004) parameter (0.0027) in (0.0007) convergence (-0.0003) time (0.0003) variability. (0.0007) in (0.0008) order (0.0001) to (0.0004) further (-0.0001) understand (0.0016) this (0.0005) result, (0.0009) additional (-0.0011) deterministic (0.0002) experiments (0.0005) were (-0.0006) performed. (-0.0002) the (-0.0003) results (0.0008) of (-0.0001) these (0.0007) experiments (0.0017) demonstrate (0.0012) the (-0.0001) extreme (0.0011) sensitivity (0.0005) of (-0.0000) back (0.0019) propagation (0.0013) to (0.0015) initial (0.0007) weight (0.0012) configuration. (-0.0008)
~~~~~~

**Node-2.3** (global 1036):

~~~~~~text
title (0.0008) : (-0.0002) adaptive (-0.0000) behavior (-0.0003) in (0.0004) competing (0.0000) co- (0.0004) evolving (0.0006) species (-0.0007) abstract (0.0003) : (0.0005) co- (0.0001) evolution (0.0001) of (0.0001) competitive (-0.0004) species (-0.0004) provides (0.0002) an (-0.0000) interesting (0.0009) testbed (0.0001) to (-0.0001) study (0.0003) the (0.0004) role (-0.0004) of (-0.0002) adaptive (-0.0002) behavior (-0.0002) because (0.0002) it (0.0002) provides (0.0003) unpredictable (-0.0005) and (0.0000) dynamic (0.0009) environments. (0.0005) in (0.0008) this (0.0003) paper (0.0004) we (-0.0005) experimentally (-0.0000) investigate (-0.0000) some (-0.0004) arguments (0.0008) for (-0.0006) the (-0.0002) co- (0.0002) evolution (0.0002) of (-0.0002) different (0.0002) adaptive (-0.0003) protean (-0.0002) behaviors (-0.0004) in (-0.0001) competing (-0.0001) species (0.0000) of (-0.0005) predators (-0.0013) and (-0.0003) preys. (0.0001) both (0.0004) species (-0.0000) are (0.0001) implemented (0.0011) as (-0.0004) simulated (-0.0003) mobile (0.0001) robots (0.0004) ( (-0.0000) kheperas (-0.0000) ) (0.0004) with (-0.0006) infrared (0.0007) proximity (-0.0005) sensors, (-0.0008) but (-0.0001) the (-0.0006) predator (-0.0009) has (-0.0003) an (-0.0002) additional (0.0003) vision (-0.0000) module (0.0008) whereas (-0.0002) the (-0.0001) prey (-0.0000) has (-0.0002) a (-0.0007) maximum (0.0005) speed (-0.0000) set (-0.0002) to (0.0002) twice (0.0001) that (0.0001) of (-0.0002) the (-0.0003) predator. (0.0001) different (0.0008) types (0.0013) of (-0.0001) variability (-0.0007) during (0.0008) life (0.0010) for (0.0003) neurocontrollers (-0.0006) with (-0.0001) the (-0.0000) same (0.0002) architecture (-0.0001) and (-0.0001) genetic (0.0004) length (0.0006) are (0.0003) compared. (-0.0003) it (0.0007) is (0.0003) shown (-0.0000) that (0.0002) simple (0.0001) forms (-0.0007) of (0.0005) pro- (0.0008) teanism (-0.0006) affect (-0.0005) co- (0.0004) evolutionary (0.0003) dynamics (-0.0005) and (-0.0004) that (0.0006) preys (-0.0000) rather (0.0008) exploit (0.0009) noisy (0.0001) controllers (0.0002) to (0.0001) generate (0.0005) random (0.0003) trajectories, (0.0000) whereas (0.0015) predators (-0.0007) benefit (0.0005) from (-0.0003) directional- (-0.0004) change (0.0000) controllers (-0.0002) to (0.0003) improve (0.0002) pursuit (-0.0003) behavior. (-0.0001)
~~~~~~

**Node-2.4** (global 1204):

~~~~~~text
title (0.0005) : (0.0000) the (0.0005) role (-0.0006) of (-0.0007) development (-0.0002) in (-0.0002) genetic (-0.0000) algorithms (-0.0005) abstract (0.0007) : (0.0001) technical (0.0004) report (0.0003) number (0.0001) cs94- (-0.0003) 394 (-0.0003) computer (-0.0003) science (0.0001) and (-0.0008) engineering, (0.0003) u. (-0.0009) c. (-0.0006) s. (-0.0014) d. (-0.0020) abstract (0.0012) the (0.0001) developmental (0.0011) mechanisms (0.0002) transforming (-0.0004) genotypic (-0.0004) to (-0.0003) phenotypic (0.0002) forms (-0.0002) are (-0.0008) typically (-0.0006) omitted (0.0000) in (-0.0003) formulations (-0.0001) of (0.0003) genetic (0.0001) algorithms (-0.0011) ( (-0.0006) gas (-0.0003) ) (-0.0009) in (0.0001) which (-0.0002) these (-0.0004) two (-0.0001) representational (0.0003) spaces (0.0003) are (0.0001) identical. (-0.0007) we (0.0010) argue (0.0011) that (-0.0004) a (0.0006) careful (-0.0001) analysis (-0.0006) of (-0.0006) developmental (0.0014) mechanisms (-0.0007) is (0.0004) useful (-0.0001) when (-0.0006) understanding (0.0009) the (-0.0018) success (0.0012) of (0.0006) several (0.0008) standard (-0.0001) ga (0.0014) techniques, (-0.0010) and (-0.0010) can (-0.0001) clarify (0.0001) the (0.0003) relationships (-0.0007) between (0.0000) more (-0.0003) recently (-0.0001) proposed (-0.0007) enhancements. (-0.0008) we (-0.0014) provide (0.0004) a (0.0009) framework (0.0006) which (0.0002) distinguishes (-0.0006) between (0.0008) two (-0.0005) developmental (0.0005) mechanisms (-0.0005) | (0.0018) learning (-0.0010) and (-0.0010) maturation (-0.0003) | (0.0002) while (-0.0003) also (-0.0001) showing (0.0005) several (-0.0005) common (-0.0009) effects (-0.0006) on (-0.0008) ga (-0.0021) search. (-0.0016) this (-0.0008) framework (-0.0008) is (-0.0004) used (-0.0005) to (-0.0003) analyze (-0.0005) how (-0.0011) maturation (-0.0001) and (-0.0002) local (-0.0002) search (-0.0006) can (-0.0003) change (-0.0001) the (0.0002) dynamics (-0.0002) of (-0.0002) the (-0.0003) ga. (-0.0001) we (0.0014) observe (-0.0004) that (-0.0002) in (-0.0003) some (-0.0004) contexts, (-0.0003) maturation (-0.0001) and (-0.0009) local (-0.0004) search (-0.0004) can (-0.0002) be (-0.0003) incorporated (-0.0001) into (0.0000) the (-0.0005) fitness (0.0013) evaluation, (0.0003) but (-0.0006) illustrate (0.0010) reasons (-0.0001) for (-0.0003) considering (0.0001) them (0.0003) seperately. (-0.0001) further, (-0.0000) we (0.0005) identify (0.0009) contexts (-0.0004) in (0.0000) which (0.0003) maturation (0.0003) and (0.0001) local (0.0008) search (0.0000) can (0.0001) be (-0.0006) distinguished (-0.0003) from (0.0001) the (0.0002) fitness (0.0005) evaluation. (-0.0008)
~~~~~~

**Node-2.5** (global 1689):

~~~~~~text
title (0.0005) : (0.0007) selection (-0.0006) for (0.0007) wandering (-0.0005) behavior (0.0001) in (0.0005) a (-0.0000) small (0.0001) robot (-0.0008) abstract (0.0004) : (-0.0004) we (0.0002) have (-0.0006) evolved (0.0003) artificial (0.0004) neural (-0.0004) networks (-0.0001) to (0.0004) control (-0.0001) the (0.0003) wandering (0.0000) behavior (-0.0002) of (0.0001) small (-0.0010) robots. (-0.0005) the (-0.0009) task (-0.0006) was (0.0004) to (0.0004) touch (-0.0006) as (0.0003) many (0.0004) squares (-0.0005) in (0.0003) a (0.0003) grid (-0.0001) as (0.0003) possible (0.0001) during (-0.0001) a (0.0001) fixed (0.0002) period (0.0000) of (0.0003) time. (0.0009) a (-0.0001) number (-0.0008) of (-0.0002) the (-0.0012) simulated (-0.0009) robots (-0.0016) were (-0.0011) embodied (0.0017) in (-0.0001) small (0.0008) lego (-0.0016) ( (-0.0002) trademark (0.0005) ) (0.0007) robot, (-0.0002) controlled (0.0004) by (-0.0002) a (0.0000) motorola (0.0003) ( (0.0006) trademark (-0.0000) ) (0.0003) 6811 (-0.0001) processor (-0.0001) ; (-0.0009) and (0.0003) their (0.0005) performance (0.0002) was (0.0001) compared (-0.0005) to (-0.0003) the (-0.0006) simulations. (-0.0010) we (0.0005) observed (0.0000) that (-0.0001) : (0.0003) ( (0.0000) a (0.0006) ) (-0.0001) evolution (0.0010) was (0.0007) an (0.0000) effective (0.0004) means (0.0001) to (0.0002) program (0.0001) control (-0.0003) ; (0.0007) ( (0.0007) b (0.0010) ) (0.0002) progress (0.0016) was (0.0005) characterized (0.0000) by (0.0002) sharply (-0.0003) stepped (0.0008) periods (0.0006) of (0.0002) improvement, (0.0005) separated (0.0002) by (0.0005) periods (0.0012) of (0.0008) stasis (0.0005) that (0.0006) corresponded (0.0012) to (0.0002) levels (0.0012) of (0.0007) behavioral (-0.0002) / (-0.0000) computational (0.0003) complexity (0.0002) ; (0.0004) and (0.0000) ( (0.0018) c (-0.0005) ) (0.0003) the (-0.0007) simulated (-0.0007) and (0.0002) realized (0.0012) robots (-0.0028) behaved (-0.0001) quite (0.0004) similarly, (-0.0001) the (0.0008) realized (-0.0003) robots (-0.0021) in (0.0002) some (0.0001) cases (-0.0005) outperforming (0.0000) the (-0.0004) simulated (-0.0015) ones. (-0.0001) introducing (-0.0016) random (-0.0006) noise (-0.0000) to (0.0009) the (-0.0001) simulations (0.0009) improved (0.0004) the (0.0000) fit (0.0004) somewhat (0.0007) ( (0.0011) from (0.0004) 0. (0.0005) 73 (-0.0001) to (0.0002) 0. (0.0004) 79 (0.0002) ). (0.0008) hybrid (-0.0015) simulated (-0.0000) / (0.0009) embodied (-0.0028) selection (0.0005) regimes (-0.0016) for (0.0008) evolutionary (-0.0001) robots (0.0003) are (0.0005) discussed. (-0.0007)
~~~~~~

**Node-2.6** (global 1738):

~~~~~~text
title (0.0006) : (-0.0014) evolving (-0.0027) nontrivial (0.0004) behaviors (-0.0010) on (-0.0012) real (0.0010) robots (-0.0018) : (0.0009) an (-0.0009) autonomous (-0.0029) robot (-0.0041) that (0.0001) picks (0.0005) up (-0.0001) objects (0.0021) abstract (0.0008) : (0.0001) recently, (0.0007) a (0.0025) new (-0.0002) approach (-0.0003) that (-0.0007) involves (0.0010) a (0.0015) form (0.0003) of (-0.0002) simulated (-0.0003) evolution (-0.0002) has (-0.0014) been (0.0015) proposed (0.0017) for (-0.0004) the (-0.0004) building (0.0000) of (0.0008) autonomous (-0.0051) robots. (-0.0007) however, (0.0001) it (0.0002) is (0.0007) still (0.0002) not (0.0000) clear (0.0000) if (0.0015) this (0.0008) approach (-0.0003) may (0.0005) be (0.0005) adequate (-0.0003) to (0.0002) face (0.0002) real (-0.0007) life (-0.0003) problems. (0.0002) in (0.0006) this (0.0005) paper (-0.0002) we (0.0014) show (0.0013) how (0.0001) control (0.0003) systems (0.0009) that (-0.0002) perform (0.0003) a (-0.0000) nontrivial (0.0002) sequence (0.0007) of (0.0010) behaviors (-0.0002) can (-0.0003) be (0.0003) obtained (0.0000) with (0.0000) this (-0.0003) methodology (-0.0001) by (0.0006) carefully (0.0007) designing (0.0013) the (-0.0012) conditions (0.0016) in (0.0008) which (0.0005) the (-0.0003) evolutionary (0.0002) process (0.0008) operates. (-0.0010) in (0.0010) the (0.0003) experiment (0.0048) described (-0.0005) in (0.0001) the (-0.0008) paper, (0.0004) a (0.0003) mobile (0.0022) robot (-0.0033) is (0.0022) trained (0.0011) to (-0.0003) locate, (0.0003) recognize, (0.0001) and (0.0016) grasp (-0.0002) a (0.0001) target (0.0007) object. (0.0012) the (0.0008) controller (-0.0030) of (-0.0000) the (0.0022) robot (-0.0017) has (0.0037) been (-0.0001) evolved (-0.0007) in (0.0006) simulation (-0.0021) and (-0.0001) then (0.0014) downloaded (-0.0005) and (0.0001) tested (0.0003) on (-0.0008) the (0.0008) real (-0.0019) robot. (-0.0022)
~~~~~~

**Node-2.7** (global 2165):

~~~~~~text
title (-0.0003) : (-0.0000) auto- (0.0008) teaching (-0.0019) : (-0.0001) networks (-0.0004) that (-0.0007) develop (-0.0002) their (0.0004) own (0.0005) teaching (-0.0018) input (0.0006) abstract (-0.0014) : (0.0002) backpropagation (0.0003) learning (-0.0013) ( (0.0008) rumelhart, (-0.0001) hinton (0.0002) and (0.0005) williams, (0.0004) 1986 (-0.0005) ) (0.0011) is (-0.0012) a (-0.0006) useful (0.0000) research (-0.0003) tool (-0.0004) but (0.0001) it (0.0004) has (0.0001) a (0.0006) number (0.0006) of (0.0000) undesiderable (0.0002) features (0.0000) such (0.0007) as (0.0005) having (0.0004) the (0.0009) experimenter (0.0002) decide (0.0005) from (0.0003) outside (0.0014) what (0.0017) should (0.0006) be (0.0000) learned. (-0.0009) we (0.0017) describe (-0.0007) a (0.0008) number (0.0000) of (0.0001) simulations (0.0010) of (0.0006) neural (0.0013) networks (0.0008) that (0.0006) internally (-0.0001) generate (0.0005) their (-0.0003) own (-0.0005) teaching (-0.0016) input. (0.0021) the (-0.0014) networks (-0.0007) generate (0.0007) the (0.0019) teaching (-0.0022) input (0.0001) by (-0.0005) trasforming (0.0004) the (0.0006) network (0.0001) input (0.0002) through (0.0001) connection (-0.0008) weights (0.0009) that (-0.0002) are (0.0004) evolved (0.0007) using (-0.0005) a (0.0005) form (0.0002) of (0.0000) genetic (0.0023) algorithm. (-0.0023) what (0.0008) results (0.0000) is (-0.0005) an (0.0010) innate (0.0006) ( (0.0001) evolved (0.0019) ) (0.0005) capacity (0.0001) not (0.0009) to (0.0001) behave (0.0014) efficiently (0.0008) in (0.0007) an (0.0004) environment (0.0012) but (0.0002) to (0.0008) learn (0.0013) to (0.0002) behave (0.0020) efficiently. (-0.0092) the (0.0025) analysis (0.0016) of (0.0001) what (0.0011) these (0.0009) networks (-0.0011) evolve (0.0005) to (-0.0009) learn (-0.0014) shows (-0.0015) some (0.0007) interesting (-0.0005) results. (-0.0024)
~~~~~~

**Node-2.8** (global 2193):

~~~~~~text
title (-0.0017) : (-0.0013) growing (-0.0010) neural (-0.0008) networks (-0.0018) abstract (-0.0008) : (0.0023) selecting (-0.0004) a (-0.0017) set (0.0005) of (-0.0000) features (0.0009) which (-0.0035) is (0.0026) optimal (-0.0010) for (0.0005) a (-0.0013) given (-0.0002) task (-0.0012) is (0.0029) a (-0.0022) problem (0.0008) which (-0.0025) plays (0.0008) an (-0.0000) important (0.0011) role (-0.0011) in (-0.0009) a (-0.0005) wide (0.0001) variety (0.0006) of (-0.0001) contexts (0.0013) including (-0.0009) pattern (-0.0007) recognition, (0.0010) adaptive (0.0020) control, (0.0006) and (0.0008) machine (0.0015) learning. (0.0019) our (0.0041) experience (0.0008) with (-0.0010) traditional (-0.0006) feature (0.0019) selection (-0.0010) algorithms (-0.0015) in (0.0001) the (-0.0004) domain (0.0016) of (0.0013) machine (0.0004) learning (0.0013) lead (-0.0012) to (0.0000) an (0.0000) appreciation (-0.0008) for (0.0001) their (-0.0004) computational (0.0003) efficiency (0.0013) and (-0.0005) a (-0.0008) concern (0.0003) for (-0.0008) their (-0.0014) brittleness. (0.0007) this (-0.0028) paper (0.0019) describes (-0.0032) an (-0.0002) alternate (0.0018) approach (0.0003) to (-0.0018) feature (0.0002) selection (-0.0006) which (0.0004) uses (0.0009) genetic (0.0010) algorithms (0.0003) as (-0.0008) the (-0.0026) primary (0.0019) search (0.0022) component. (-0.0024) results (0.0004) are (-0.0011) presented (-0.0034) which (-0.0009) suggest (-0.0005) that (-0.0024) genetic (0.0015) algorithms (0.0008) can (-0.0017) be (0.0006) used (0.0002) to (-0.0008) increase (-0.0000) the (-0.0000) robustness (0.0016) of (-0.0031) feature (0.0026) selection (-0.0024) algorithms (-0.0000) without (0.0003) a (-0.0014) significant (0.0008) decrease (0.0013) in (-0.0004) computational (0.0007) efficiency. (-0.0027)
~~~~~~

**Node-2.9** (global 2309):

~~~~~~text
title (0.0003) : (-0.0004) evolving (0.0008) sensors (0.0013) in (0.0005) environments (-0.0001) of (0.0006) controlled (-0.0007) complexity (-0.0001) abstract (-0.0004) : (-0.0010) 1. (0.0025) sensors (0.0010) represent (0.0003) a (0.0005) crucial (-0.0005) link (0.0004) between (0.0003) the (0.0009) evolutionary (-0.0019) forces (0.0004) shaping (0.0007) a (0.0009) species (0.0026) ' (-0.0026) relationship (0.0009) with (-0.0006) its (0.0001) environment, (0.0008) and (0.0001) the (0.0005) individual (-0.0006) ' (0.0002) s (0.0001) cognitive (-0.0002) abilities (-0.0001) to (-0.0004) behave (-0.0001) and (-0.0001) learn. (0.0017) we (-0.0045) report (-0.0025) on (0.0014) experiments (0.0016) using (-0.0008) a (-0.0025) new (0.0007) class (-0.0007) of (0.0005) " (0.0000) latent (0.0004) energy (-0.0001) environments (-0.0002) " (0.0003) ( (0.0014) lee (0.0005) ) (0.0004) models (0.0006) to (0.0000) define (-0.0012) environments (0.0010) of (0.0000) carefully (0.0008) controlled (0.0004) complexity (-0.0006) which (0.0004) allow (0.0005) us (-0.0006) to (0.0003) state (-0.0003) bounds (0.0011) for (-0.0006) random (0.0003) and (0.0004) optimal (0.0005) behaviors (0.0002) that (0.0003) are (0.0012) independent (0.0006) of (0.0002) strategies (0.0009) for (0.0003) achieving (0.0012) the (0.0003) behaviors. (0.0003) using (0.0016) lee (0.0004) ' (-0.0000) s (0.0007) analytic (0.0008) basis (0.0011) for (0.0017) defining (0.0007) environments, (0.0007) we (0.0009) then (0.0021) use (0.0008) neural (0.0018) networks (-0.0007) ( (0.0009) nnets (0.0009) ) (-0.0002) to (0.0019) model (0.0006) individuals (0.0001) and (0.0010) a (-0.0003) steady- (0.0002) state (0.0003) genetic (-0.0007) algorithm (0.0010) to (0.0005) model (0.0014) an (0.0008) evolutionary (-0.0005) process (0.0011) shaping (0.0001) the (0.0005) nnets, (0.0003) in (-0.0003) particular (-0.0000) their (-0.0008) sensors. (0.0013) our (-0.0021) experiments (-0.0058) consider (-0.0009) two (-0.0001) types (-0.0001) of (-0.0000) " (-0.0019) contact (0.0007) " (-0.0006) and (-0.0001) " (-0.0005) ambient (0.0004) " (-0.0004) sensors, (0.0008) and (-0.0002) variants (-0.0002) where (0.0010) the (0.0007) nnets (0.0003) are (0.0008) not (0.0003) allowed (-0.0002) to (0.0007) learn, (0.0001) learn (-0.0003) via (0.0002) error (0.0000) correction (-0.0005) from (0.0004) internal (-0.0005) prediction, (0.0001) and (0.0005) via (0.0002) reinforcement (-0.0018) learning. (0.0017) we (-0.0015) find (0.0002) that (-0.0000) predictive (-0.0004) learning, (-0.0001) even (-0.0001) when (0.0008) using (0.0003) a (0.0002) larger (0.0004) repertoire (-0.0009) of (0.0001) the (0.0007) more (0.0005) sophisticated (-0.0001) ambient (0.0001) sensors, (0.0010) provides (0.0005) no (0.0017) advantage (-0.0005) over (0.0002) nnets (0.0002) unable (0.0007) to (-0.0001) learn. (0.0004) however, (0.0011) reinforcement (-0.0023) learning (-0.0003) using (0.0003) a (0.0000) small (0.0005) number (-0.0001) of (-0.0010) crude (-0.0005) contact (-0.0006) sensors (-0.0003) does (0.0010) provide (-0.0004) a (-0.0002) significant (-0.0001) advantage. (0.0006) our (0.0002) analysis (-0.0005) of (-0.0011) these (0.0014) results (-0.0006) points (-0.0002) to (0.0003) a (-0.0002) tradeoff (-0.0001) between (0.0006) the (0.0007) genetic (-0.0003) " (-0.0008) robustness (0.0006) " (-0.0001) of (0.0002) sensors (0.0004) and (-0.0002) their (0.0007) informativeness (0.0006) to (0.0001) a (0.0004) learning (0.0002) system. (0.0022)
~~~~~~
