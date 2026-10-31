# Reference packet: GraphNarrator__Llama-8B__cora__2214

- Method: GraphNarrator; configuration: Llama-8B; dataset: cora; target node: 2214
- Explanation source: `./graphnarrCora/GraphNarrator/outputs/generated_expls-100/433.json` (messages[assistant])
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

### Word-Level Evaluation

Detect important terms for the classification label.
Quantitatively, the importance (saliency) scores behind each word in the verbalized graph are calculated by a post-hoc XAI (explanable AI) algorithm.
Semantically, keywords synonymous with or closely related to label, 'Neural Networks' (such as 'neural', 'network', and 'classification'), are semantically influential in determining the classification because they directly indicate the node's relevance to the 'Neural Networks' category.

### Graph-Level Aggregation

Node 1 does not contain as many directly relevant keywords. Yet, it still discusses smoothing splines, which are related to the field of statistics, indicating that it contributes to the classification in a less significant way. 
Direct neighbors like Node-1.1 and Node-1.2, which contain keywords like 'anova' and 'bayesian confidence intervals', have a substantial influence on ROOT node classification due to their close proximity to the ROOT node.
Indirect neighbors, Node-1.3, connected through Node 1, contains keywords like 'classification', which further reinforce the classification of ROOT. 

### Free-Text Explanation

The classification of ROOT node into the "Neural Networks" category can be explained as follows:

ROOT: The presence of keywords like "classification" within ROOT node suggests that the paper is focused on topics central to neural networks, such as classification.

  - Node-1: While Node 1 focuses on smoothing splines, which are related to statistics, it is slightly less directly related to neural networks.
    - Node-1.1 ~ Node-1.3: they are less relevant to neural networks and thus contribute less to the classification.
      - Node-1.1: This node discusses "anova" and "bayesian confidence intervals", which are related to statistical analysis, but not directly related to neural networks.
      - Node-1.2: This node also discusses "anova" and "bayesian confidence intervals", which are related to statistical analysis, but not directly related to neural networks.
      - Node-1.3: This node discusses "classification", which is directly related to neural networks.

In summary, the classification of ROOT node into "Neural Networks" is well-supported by the presence of key neural network terms within the node itself and its direct connection to Node-1.3, which also focuses on classification.
~~~~~~

## 2. Prompt the method's model received

Chat messages sent to the model (system message as sent by FreeTextExpGenerator.gen; user message verbatim from `./graphnarrCora/GraphNarrator/outputs/generated_expls-100/433.json`).

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
<verbalized-graph>ROOT: title(0.00) behavior(0.01) near(-0.01) zero(0.00) distribution(-0.01) gcv(-0.00) smoothing(0.00) parameter(0.00) estimates(-0.02) 1(-0.03) abstract(-0.01) many(0.00) today(-0.01) algorithms(-0.01) inductive(-0.00) logic(-0.01) programming(-0.01) ilp(0.01) put(-0.01) heavy(0.01) burden(-0.02) responsibility(0.01) user,(-0.01) declarative(-0.01) bias(-0.01) defined(0.00) rather(-0.01) low-(-0.01) level(-0.01) fashion.(-0.01) address(0.00) issue,(-0.01) developed(0.01) method(-0.00) generating(-0.02) declarative(-0.00) language(0.00) bias(0.00) top-(-0.03) ilp(-0.00) systems(0.00) high-(-0.00) level(-0.00) declarations.(-0.00) key(0.01) feature(-0.00) approach(0.00) distinction(-0.01) user(-0.00) level(-0.00) expert(-0.01) level(0.00) language(-0.00) bias(-0.00) declarations.(-0.00) expert(-0.00) provides(-0.02) abstract(0.01) meta-(-0.01) declarations,(-0.01) user(0.01) declares(-0.02) relationship(-0.00) meta-(-0.00) level(-0.01) given(-0.00) database(0.00) obtain(0.00) low-(-0.00) level(-0.01) declarative(0.00) language(-0.01) bias.(-0.02) suggested(-0.00) languages(-0.01) allow(0.00) compact(-0.00) abstract(-0.00) specifications(0.01) declarative(-0.00) language(-0.00) bias(0.00) top-(0.01) ilp(-0.00) systems(-0.01) using(-0.01) schemata.(0.01) verified(-0.00) several(-0.00) properties(-0.01) translation(0.00) algorithm(0.00) generates(0.00) schemata,(-0.00) applied(0.00) successfully(0.00) chemical(-0.01) domains.(0.01) consequence,(-0.01) propose(-0.03) use(-0.01) two-(-0.00) level(-0.01) approach(-0.02) generate(-0.01) declarative(-0.00) language(-0.00) bias.(-0.01) 
Node-1: title(-0.00) sample(0.00) size(0.02) calculations(-0.00) smoothing(0.01) splines(0.01) based(0.01) bayesian(0.01) confidence(0.02) intervals(-0.00) abstract(0.02) bayesian(0.01) confidence(0.01) intervals(-0.00) smoothing(0.05) spline(0.01) often(-0.00) used(-0.01) distinguish(-0.00) two(0.01) curves.(-0.02) paper,(-0.00) provide(0.01) asymptotic(0.01) formula(0.01) sample(-0.00) size(0.01) calculations(-0.02) based(0.01) bayesian(0.01) confidence(0.01) intervals.(0.00) approximations(0.01) simulations(0.01) special(0.01) functions(0.01) indicate(0.02) asymptotic(0.01) formula(0.01) reasonably(0.03) accurate.(-0.03) key(0.02) words(0.01) bayesian(0.01) confidence(-0.01) intervals(-0.01) sample(0.01) size(-0.01) smoothing(-0.03) spline.(0.04) fl(0.03) address(0.00) department(0.03) statistics(0.03) applied(0.00) probability,(0.01) university(-0.01) california,(-0.02) santa(0.02) barbara,(0.02) ca(0.01) 93106-(0.02) 3110.(0.02) tel.(0.00) 805(0.01) 893-(0.01) 4870.(0.02) fax(0.01) 805(0.00) 893-(0.00) 2334.(0.01) e-(0.01) mail(-0.01) yuedong(0.02) pstat.(0.00) ucsb.(0.00) edu.(0.00) supported(-0.01) national(0.00) institute(0.01) health(0.02) grants(-0.00) r01(0.00) ey09946,(0.00) p60(0.01) dk20572(0.01) p30(-0.00) hd18258.(0.00) 
Node-1.1: title(0.00) grkpack(0.00) fitting(-0.00) smoothing(-0.00) spline(0.00) anova(-0.00) models(0.00) exponential(-0.00) families(-0.00) abstract(-0.00) wahba,(0.00) wang,(-0.00) gu,(0.00) klein(-0.00) klein(0.00) 1995(-0.00) introduced(-0.00) smoothing(-0.00) spline(0.00) analysis(-0.00) variance(0.00) ss(0.00) anova(-0.00) method(0.00) data(0.00) exponential(0.00) families.(-0.00) based(0.00) rkpack,(0.00) fits(-0.00) ss(0.00) anova(-0.00) models(0.00) gaussian(-0.00) data,(0.00) introduce(-0.00) grkpack(-0.00) collection(0.00) fortran(0.00) subroutines(0.00) binary,(-0.00) binomial,(0.00) poisson(0.00) gamma(-0.00) data.(0.00) also(0.00) show(0.00) calculate(0.00) bayesian(0.00) confidence(-0.00) intervals(0.00) ss(0.00) anova(-0.00) estimates.(0.00) 
Node-1.2: title(-0.00) smoothing(0.00) spline(0.00) anova(0.00) component-(0.01) wise(0.00) bayesian(0.00) confidence(0.00) intervals(-0.00) appear,(0.00) j.(-0.00) computational(0.00) graphical(-0.00) statistics(-0.00) abstract(-0.00) study(0.00) multivariate(0.00) smoothing(0.00) spline(0.00) estimate(0.00) function(0.00) several(0.00) variables,(0.00) based(0.00) anova(-0.00) decomposition(0.00) sums(0.00) main(0.00) effect(0.00) functions(0.00) one(0.00) variable(0.00) ),(-0.00) two-(0.00) factor(0.00) interaction(-0.00) functions(0.00) two(0.00) variables(0.00) ),(0.00) etc.(0.00) derive(-0.00) bayesian(0.00) confidence(-0.00) intervals(-0.00) components(0.00) decomposition(0.00) demonstrate(0.00) that,(0.00) even(0.00) multiple(0.00) smoothing(-0.00) parameters,(0.00) efficiently(0.00) computed(0.00) using(0.00) publicly(0.00) available(0.00) code(0.00) rkpack,(0.00) originally(0.00) designed(0.00) compute(0.00) estimates.(0.00) carry(0.00) small(0.00) monte(-0.00) carlo(-0.00) study(0.00) see(-0.00) closely(0.00) actual(0.00) properties(0.00) component-(0.00) wise(-0.00) confidence(-0.00) intervals(-0.00) match(-0.00) nominal(0.00) confidence(-0.00) levels.(-0.00) lastly,(-0.00) analyze(0.00) lake(0.00) acidity(-0.00) data(0.00) function(0.00) calcium(0.00) concentration,(0.00) latitude,(0.00) longitude,(0.00) using(0.00) polynomial(0.00) thin(0.00) plate(-0.00) spline(0.00) main(0.00) effects(0.00) model.(0.00) 
Node-1.3: title(-0.00) soft(0.00) classification,(-0.00) a.(-0.00) k.(-0.00) a.(-0.00) risk(0.00) estimation,(-0.00) via(-0.00) penalized(-0.00) log(0.00) likelihood(0.00) smoothing(-0.00) spline(-0.00) analysis(0.00) variance(-0.00) abstract(0.00) study(0.00) multivariate(0.00) smoothing(-0.00) spline(0.00) estimate(0.00) function(-0.00) several(-0.00) variables,(-0.00) based(-0.00) anova(-0.00) decomposition(0.00) sums(-0.00) main(-0.00) effect(-0.00) functions(-0.00) one(-0.00) variable(0.00) ),(-0.00) two-(-0.00) factor(0.00) interaction(0.00) functions(0.00) two(0.00) variables(0.00) ),(-0.00) etc.(-0.00) derive(0.00) bayesian(-0.00) confidence(0.00) intervals(0.00) components(0.00) decomposition(-0.00) demonstrate(-0.00) that,(-0.00) even(-0.00) multiple(0.00) smoothing(0.00) parameters,(-0.00) efficiently(-0.00) computed(0.00) using(-0.00) publicly(-0.00) available(-0.00) code(-0.00) rkpack,(-0.00) origin</verbalized-graph>

### Classification Label
Neural_Networks

### Reasoning

### Free-Text Explanation

(P.S.: 1. make sure to complete both the reasoning section and then Free-Text Explanation section with the same structure as exemplified above.
2. make good use of the importance (saliency) score behind each word as your guidance to generate the better explanation. However, it is not necessary to directly quote the saliency score.
3. use the *whole* graph structure you constructed during reasoning for the format of the explanation. Indents and node indexes are necessary, which representing the hierarchy of the graph.)

~~~~~~

## 3. Target node

- ID: 2214
- Title: Behavior Near Zero of the Distribution of GCV Smoothing Parameter Estimates 1
- True class (canonical `y`): **Neural_Networks**
- Predicted class, canonical GraphSAGE (`prediction_agreement/cora_canonical_vs_gspell_full.json`): **Neural_Networks**
- Prediction recorded by this method's pipeline: **Neural_Networks**

Canonical text (`raw_text`):

~~~~~~text
Title: Behavior Near Zero of the Distribution of GCV Smoothing Parameter Estimates 1  
Abstract: Many of today's algorithms for Inductive Logic Programming (ILP) put a heavy burden and responsibility on the user, because their declarative bias have to be defined in a rather low-level fashion. To address this issue, we developed a method for generating declarative language bias for top-down ILP systems from high-level declarations. The key feature of our approach is the distinction between a user level and an expert level of language bias declarations. The expert provides abstract meta-declarations, and the user declares the relationship between the meta-level and the given database to obtain a low-level declarative language bias. The suggested languages allow for compact and abstract specifications of the declarative language bias for top-down ILP systems using schemata. We verified several properties of the translation algorithm that generates schemata, and applied it successfully to a few chemical domains. As a consequence, we propose to use a two-level approach to generate declarative language bias.
~~~~~~

## 4. Neighbors (canonical `edge_index`, `cora_canonical.pt`)

### 1-hop: 2 nodes

| node id | true class | title |
|---|---|---|
| 420 | Neural_Networks | Sample Size Calculations for Smoothing Splines Based on Bayesian Confidence Intervals |
| 2223 | Neural_Networks | Smoothing Spline Models With Correlated Random Errors 1 |

### 2-hop (shortest distance exactly 2): 8 nodes

| node id | true class | title |
|---|---|---|
| 10 | Neural_Networks | GRKPACK: FITTING SMOOTHING SPLINE ANOVA MODELS FOR EXPONENTIAL FAMILIES |
| 190 | Neural_Networks | Spline Smoothing For Bivariate Data With Applications To Association Between Hormones |
| 192 | Neural_Networks | Smoothing Spline ANOVA with Component-Wise Bayesian "Confidence Intervals" To Appear, J. Computational and Graphical Statistics |
| 193 | Neural_Networks | Soft Classification, a.k.a. Risk Estimation, via Penalized Log Likelihood and Smoothing Spline Analysis of Variance |
| 439 | Neural_Networks | Adaptive tuning of numerical weather prediction models: Randomized GCV in three and four dimensional data assimilation |
| 510 | Probabilistic_Methods | The Bayesian Approach to Tree-Structured Regression |
| 519 | Neural_Networks | Smoothing Spline ANOVA for Exponential Families, with Application to the Wisconsin Epidemiological Study of Diabetic |
| 2590 | Probabilistic_Methods | Backfitting in Smoothing Spline ANOVA |

## 5. Method evidence: GraphNarrator saliency scores per token

Source: `./graphnarrCora/GraphNarrator/outputs/pkls_cora_eval/433.pkl` (verified: the verbalized graph of this pkl, cut at 6000 characters as in generation, appears verbatim in the prompt).
GraphNarrator's own GNN recorded prediction = **Neural_Networks**, ground truth = **Neural_Networks**.
The verbalized graph is 11473 characters; the model saw the first 6000, so nodes marked 'no' below were cut from its prompt.
Scores are the per-token importance values stored in the pkl (`node.importance_scores`), rounded to 4 decimals.

### Subgraph nodes

| label | local idx | global id | n tokens | max score | in prompt |
|---|---|---|---|---|---|
| ROOT | 0 | 2214 | 180 | 0.0168 | yes |
| Node-1 | 1 | 420 | 127 | 0.0475 | yes |
| Node-1.1 | 3 | 10 | 79 | 0.0028 | yes |
| Node-1.2 | 4 | 192 | 158 | 0.0057 | yes |
| Node-1.3 | 5 | 193 | 157 | 0.0068 | yes |
| Node-1.4 | 6 | 439 | 140 | 0.0080 | no |
| Node-1.5 | 7 | 519 | 33 | 0.0107 | no |
| Node-1.6 | 8 | 2590 | 110 | 0.0027 | no |
| Node-2 | 2 | 2223 | 96 | 0.0603 | no |
| Node-2.1 | 9 | 190 | 135 | 0.0066 | no |
| Node-2.2 | 10 | 510 | 17 | 0.0191 | no |

Subgraph edges (src -> dst, as stored): Node-1->Node-1.1, Node-1->Node-1.2, Node-1->Node-1.3, Node-1->Node-1.4, Node-1->Node-1.5, Node-1->Node-1.6, Node-1->ROOT, Node-1.1->Node-1, Node-1.2->Node-1, Node-1.3->Node-1, Node-1.4->Node-1, Node-1.5->Node-1, Node-1.5->Node-2, Node-1.6->Node-1, Node-2->Node-1.5, Node-2->Node-2.1, Node-2->Node-2.2, Node-2->ROOT, Node-2.1->Node-2, Node-2.2->Node-2, ROOT->Node-1, ROOT->Node-2

### Tokens and scores

**ROOT** (global 2214):

~~~~~~text
title (0.0036) : (-0.0039) behavior (0.0070) near (-0.0104) zero (0.0017) of (-0.0173) the (-0.0046) distribution (-0.0112) of (-0.0146) gcv (-0.0011) smoothing (0.0029) parameter (0.0028) estimates (-0.0211) 1 (-0.0308) abstract (-0.0072) : (0.0051) many (0.0029) of (-0.0217) today (-0.0053) ' (-0.0012) s (0.0060) algorithms (-0.0054) for (-0.0093) inductive (-0.0012) logic (-0.0078) programming (-0.0053) ( (-0.0119) ilp (0.0088) ) (0.0040) put (-0.0055) a (-0.0109) heavy (0.0050) burden (-0.0171) and (-0.0106) responsibility (0.0089) on (-0.0055) the (-0.0043) user, (-0.0053) because (-0.0108) their (0.0033) declarative (-0.0077) bias (-0.0122) have (0.0015) to (-0.0065) be (0.0086) defined (0.0026) in (-0.0045) a (-0.0045) rather (-0.0081) low- (-0.0067) level (-0.0079) fashion. (-0.0087) to (-0.0042) address (0.0008) this (0.0041) issue, (-0.0122) we (-0.0077) developed (0.0069) a (-0.0064) method (-0.0005) for (-0.0138) generating (-0.0206) declarative (-0.0041) language (0.0007) bias (0.0039) for (-0.0208) top- (-0.0286) down (0.0010) ilp (-0.0003) systems (0.0016) from (-0.0332) high- (-0.0003) level (-0.0042) declarations. (-0.0012) the (-0.0040) key (0.0073) feature (-0.0003) of (-0.0017) our (-0.0096) approach (0.0025) is (-0.0010) the (-0.0012) distinction (-0.0088) between (-0.0118) a (-0.0095) user (-0.0036) level (-0.0040) and (-0.0058) an (-0.0100) expert (-0.0132) level (0.0039) of (-0.0230) language (-0.0043) bias (-0.0016) declarations. (-0.0032) the (-0.0149) expert (-0.0040) provides (-0.0152) abstract (0.0063) meta- (-0.0066) declarations, (-0.0108) and (-0.0127) the (0.0031) user (0.0096) declares (-0.0200) the (0.0045) relationship (-0.0030) between (-0.0080) the (-0.0036) meta- (-0.0049) level (-0.0080) and (-0.0036) the (-0.0069) given (-0.0037) database (0.0037) to (-0.0048) obtain (0.0040) a (0.0021) low- (-0.0003) level (-0.0141) declarative (0.0026) language (-0.0137) bias. (-0.0180) the (-0.0115) suggested (-0.0030) languages (-0.0125) allow (0.0042) for (-0.0028) compact (-0.0022) and (0.0016) abstract (-0.0023) specifications (0.0073) of (-0.0045) the (0.0095) declarative (-0.0023) language (-0.0027) bias (0.0008) for (-0.0046) top- (0.0128) down (-0.0087) ilp (-0.0038) systems (-0.0116) using (-0.0125) schemata. (0.0075) we (-0.0416) verified (-0.0037) several (-0.0049) properties (-0.0080) of (-0.0004) the (-0.0008) translation (0.0028) algorithm (0.0004) that (0.0151) generates (0.0034) schemata, (-0.0002) and (0.0012) applied (0.0025) it (-0.0020) successfully (0.0008) to (0.0088) a (0.0168) few (0.0058) chemical (-0.0085) domains. (0.0121) as (0.0161) a (0.0090) consequence, (-0.0054) we (-0.0138) propose (-0.0269) to (0.0006) use (-0.0109) a (-0.0237) two- (-0.0014) level (-0.0076) approach (-0.0239) to (-0.0146) generate (-0.0060) declarative (-0.0020) language (-0.0043) bias. (-0.0079)
~~~~~~

**Node-1** (global 420):

~~~~~~text
title (-0.0038) : (0.0162) sample (0.0030) size (0.0240) calculations (-0.0028) for (0.0031) smoothing (0.0119) splines (0.0101) based (0.0059) on (-0.0021) bayesian (0.0122) confidence (0.0176) intervals (-0.0017) abstract (0.0168) : (0.0113) bayesian (0.0101) confidence (0.0092) intervals (-0.0006) of (-0.0054) a (-0.0187) smoothing (0.0475) spline (0.0097) are (-0.0029) often (-0.0008) used (-0.0069) to (-0.0022) distinguish (-0.0046) two (0.0142) curves. (-0.0160) in (0.0076) this (-0.0002) paper, (-0.0013) we (0.0423) provide (0.0056) an (-0.0196) asymptotic (0.0098) formula (0.0093) for (0.0043) sample (-0.0026) size (0.0086) calculations (-0.0209) based (0.0094) on (0.0099) bayesian (0.0140) confidence (0.0099) intervals. (0.0049) approximations (0.0143) and (0.0139) simulations (0.0098) on (0.0112) special (0.0051) functions (0.0129) indicate (0.0173) that (0.0154) this (0.0099) asymptotic (0.0113) formula (0.0141) is (0.0198) reasonably (0.0262) accurate. (-0.0344) key (0.0227) words (0.0066) : (0.0270) bayesian (0.0119) confidence (-0.0061) intervals (-0.0084) ; (0.0299) sample (0.0066) size (-0.0066) ; (0.0431) smoothing (-0.0302) spline. (0.0396) fl (0.0336) address (0.0003) : (0.0003) department (0.0286) of (0.0117) statistics (0.0294) and (0.0162) applied (0.0038) probability, (0.0071) university (-0.0117) of (0.0104) california, (-0.0212) santa (0.0169) barbara, (0.0155) ca (0.0121) 93106- (0.0230) 3110. (0.0214) tel. (0.0017) : (0.0257) ( (0.0076) 805 (0.0115) ) (0.0051) 893- (0.0103) 4870. (0.0208) fax (0.0058) : (0.0082) ( (-0.0000) 805 (0.0027) ) (-0.0075) 893- (0.0032) 2334. (0.0051) e- (0.0120) mail (-0.0125) : (0.0126) yuedong (0.0205) @ (0.0001) pstat. (0.0028) ucsb. (0.0013) edu. (0.0044) supported (-0.0085) by (-0.0166) the (-0.0449) national (0.0014) institute (0.0113) of (0.0089) health (0.0216) under (0.0043) grants (-0.0025) r01 (0.0028) ey09946, (0.0044) p60 (0.0070) dk20572 (0.0067) and (0.0002) p30 (-0.0020) hd18258. (0.0027)
~~~~~~

**Node-1.1** (global 10):

~~~~~~text
title (0.0025) : (0.0000) grkpack (0.0002) : (-0.0005) fitting (-0.0000) smoothing (-0.0011) spline (0.0007) anova (-0.0001) models (0.0006) for (0.0012) exponential (-0.0005) families (-0.0006) abstract (-0.0002) : (0.0025) wahba, (0.0007) wang, (-0.0010) gu, (0.0010) klein (-0.0010) and (0.0028) klein (0.0022) ( (-0.0036) 1995 (-0.0031) ) (0.0018) introduced (-0.0025) smoothing (-0.0002) spline (0.0009) analysis (-0.0003) of (0.0011) variance (0.0003) ( (0.0010) ss (0.0007) anova (-0.0001) ) (-0.0005) method (0.0006) for (0.0002) data (0.0006) from (0.0017) exponential (0.0001) families. (-0.0011) based (0.0020) on (0.0006) rkpack, (0.0004) which (0.0007) fits (-0.0006) ss (0.0007) anova (-0.0003) models (0.0001) to (0.0015) gaussian (-0.0001) data, (0.0006) we (0.0001) introduce (-0.0006) grkpack (-0.0005) : (0.0014) a (0.0005) collection (0.0014) of (0.0003) fortran (0.0022) subroutines (0.0001) for (0.0001) binary, (-0.0007) binomial, (0.0002) poisson (0.0011) and (-0.0006) gamma (-0.0012) data. (0.0007) we (0.0023) also (0.0008) show (0.0010) how (0.0014) to (0.0010) calculate (0.0018) bayesian (0.0001) confidence (-0.0008) intervals (0.0000) for (-0.0007) ss (0.0005) anova (-0.0003) estimates. (0.0009)
~~~~~~

**Node-1.2** (global 192):

~~~~~~text
title (-0.0023) : (0.0001) smoothing (0.0000) spline (0.0016) anova (0.0005) with (-0.0013) component- (0.0057) wise (0.0007) bayesian (0.0013) " (0.0002) confidence (0.0012) intervals (-0.0005) " (0.0000) to (0.0019) appear, (0.0004) j. (-0.0030) computational (0.0018) and (-0.0001) graphical (-0.0035) statistics (-0.0013) abstract (-0.0010) : (0.0031) we (-0.0029) study (0.0009) a (-0.0013) multivariate (0.0008) smoothing (0.0030) spline (0.0008) estimate (0.0010) of (0.0004) a (-0.0003) function (0.0013) of (0.0007) several (0.0006) variables, (0.0009) based (0.0007) on (0.0006) an (0.0008) anova (-0.0002) decomposition (0.0040) as (0.0014) sums (0.0003) of (0.0010) main (0.0017) effect (0.0011) functions (0.0012) ( (0.0016) of (0.0003) one (0.0002) variable (0.0001) ), (-0.0001) two- (0.0015) factor (0.0005) interaction (-0.0004) functions (0.0006) ( (0.0016) of (0.0014) two (0.0009) variables (0.0001) ), (0.0005) etc. (0.0030) we (-0.0009) derive (-0.0016) the (-0.0003) bayesian (0.0001) " (-0.0010) confidence (-0.0001) intervals (-0.0018) " (-0.0005) for (0.0011) the (-0.0021) components (0.0010) of (0.0006) this (0.0027) decomposition (0.0032) and (0.0014) demonstrate (0.0002) that, (0.0013) even (0.0022) with (0.0027) multiple (0.0040) smoothing (-0.0022) parameters, (0.0023) they (0.0009) can (0.0024) be (0.0031) efficiently (0.0012) computed (0.0049) using (0.0019) the (-0.0019) publicly (0.0018) available (0.0002) code (0.0015) rkpack, (0.0019) which (0.0016) was (0.0004) originally (0.0012) designed (0.0035) just (0.0025) to (0.0028) compute (0.0038) the (-0.0006) estimates. (0.0010) we (0.0002) carry (0.0043) out (-0.0001) a (-0.0009) small (0.0016) monte (-0.0001) carlo (-0.0004) study (0.0014) to (0.0010) see (-0.0007) how (0.0003) closely (0.0002) the (-0.0016) actual (0.0000) properties (0.0011) of (0.0017) these (0.0047) component- (0.0005) wise (-0.0026) confidence (-0.0024) intervals (-0.0042) match (-0.0019) their (-0.0007) nominal (0.0006) confidence (-0.0018) levels. (-0.0022) lastly, (-0.0000) we (-0.0058) analyze (0.0045) some (0.0021) lake (0.0048) acidity (-0.0001) data (0.0024) as (0.0013) a (-0.0012) function (0.0023) of (0.0010) calcium (0.0014) concentration, (0.0024) latitude, (0.0014) and (0.0032) longitude, (0.0009) using (0.0019) both (0.0025) polynomial (0.0020) and (0.0018) thin (0.0015) plate (-0.0006) spline (0.0010) main (0.0009) effects (0.0030) in (0.0005) the (-0.0029) same (0.0016) model. (0.0009)
~~~~~~

**Node-1.3** (global 193):

~~~~~~text
title (-0.0011) : (-0.0003) soft (0.0007) classification, (-0.0007) a. (-0.0008) k. (-0.0005) a. (-0.0016) risk (0.0022) estimation, (-0.0002) via (-0.0004) penalized (-0.0002) log (0.0001) likelihood (0.0012) and (0.0008) smoothing (-0.0017) spline (-0.0002) analysis (0.0006) of (0.0011) variance (-0.0007) abstract (0.0008) : (-0.0003) we (0.0004) study (0.0023) a (0.0008) multivariate (0.0002) smoothing (-0.0002) spline (0.0002) estimate (0.0013) of (-0.0005) a (-0.0005) function (-0.0001) of (-0.0000) several (-0.0005) variables, (-0.0001) based (-0.0004) on (-0.0000) an (-0.0002) anova (-0.0001) decomposition (0.0006) as (-0.0004) sums (-0.0002) of (-0.0001) main (-0.0008) effect (-0.0007) functions (-0.0001) ( (-0.0006) of (-0.0002) one (-0.0006) variable (0.0010) ), (-0.0001) two- (-0.0001) factor (0.0000) interaction (0.0004) functions (0.0001) ( (-0.0004) of (0.0001) two (0.0004) variables (0.0010) ), (-0.0008) etc. (-0.0030) we (0.0010) derive (0.0001) the (-0.0004) bayesian (-0.0003) " (-0.0002) confidence (0.0005) intervals (0.0017) " (-0.0001) for (-0.0004) the (0.0005) components (0.0011) of (-0.0007) this (-0.0002) decomposition (-0.0004) and (-0.0000) demonstrate (-0.0009) that, (-0.0008) even (-0.0007) with (-0.0011) multiple (0.0000) smoothing (0.0022) parameters, (-0.0007) they (-0.0007) can (0.0001) be (0.0001) efficiently (-0.0004) computed (0.0008) using (-0.0007) the (-0.0011) publicly (-0.0003) available (-0.0001) code (-0.0015) rkpack, (-0.0002) which (-0.0006) was (-0.0008) originally (-0.0015) designed (-0.0017) just (-0.0006) to (-0.0006) compute (-0.0007) the (-0.0003) estimates. (0.0068) we (-0.0027) carry (-0.0000) out (-0.0011) a (-0.0011) small (-0.0008) monte (-0.0003) carlo (0.0009) study (0.0004) to (-0.0000) see (0.0003) how (0.0002) closely (0.0001) the (0.0006) actual (-0.0002) properties (0.0004) of (-0.0003) these (0.0003) component- (0.0000) wise (0.0004) confidence (0.0019) intervals (0.0017) match (0.0000) their (-0.0002) nominal (0.0006) confidence (0.0018) levels. (0.0004) lastly, (0.0011) we (0.0036) analyze (0.0027) some (0.0018) lake (0.0001) acidity (0.0007) data (0.0003) as (0.0004) a (-0.0000) function (0.0002) of (-0.0003) calcium (0.0005) concentration, (0.0003) latitude, (0.0001) and (0.0004) longitude, (-0.0012) using (0.0005) both (0.0000) polynomial (0.0006) and (0.0002) thin (0.0005) plate (0.0001) spline (0.0005) main (-0.0003) effects (0.0003) in (0.0001) the (-0.0012) same (-0.0000) model. (-0.0003)
~~~~~~

**Node-1.4** (global 439):

~~~~~~text
title (0.0018) : (-0.0008) adaptive (-0.0011) tuning (-0.0021) of (-0.0028) numerical (-0.0035) weather (0.0008) prediction (-0.0016) models (-0.0015) : (0.0010) randomized (-0.0014) gcv (-0.0007) in (-0.0007) three (-0.0017) and (-0.0005) four (-0.0004) dimensional (0.0000) data (-0.0004) assimilation (-0.0053) abstract (-0.0004) : (0.0036) this (-0.0021) article (-0.0053) describes (0.0007) a (-0.0001) new (-0.0017) system (0.0021) for (-0.0013) induction (0.0011) of (-0.0091) oblique (-0.0008) decision (0.0080) trees. (-0.0022) this (0.0010) system, (-0.0011) oc1, (-0.0000) combines (0.0017) deterministic (-0.0003) hill- (-0.0001) climbing (-0.0007) with (-0.0000) two (0.0008) forms (0.0002) of (-0.0003) randomization (-0.0014) to (-0.0004) find (-0.0000) a (-0.0015) good (0.0000) oblique (0.0004) split (0.0011) ( (-0.0002) in (0.0009) the (0.0002) form (-0.0007) of (-0.0009) a (-0.0007) hyperplane (0.0014) ) (-0.0006) at (-0.0003) each (0.0008) node (-0.0013) of (-0.0003) a (-0.0012) decision (0.0008) tree. (0.0067) oblique (0.0063) decision (-0.0007) tree (0.0016) methods (-0.0010) are (0.0015) tuned (-0.0019) especially (0.0002) for (0.0006) domains (0.0012) in (0.0003) which (0.0003) the (-0.0007) attributes (0.0030) are (0.0006) numeric, (0.0007) although (0.0007) they (0.0018) can (0.0008) be (0.0002) adapted (0.0008) to (-0.0004) symbolic (-0.0009) or (-0.0002) mixed (0.0008) symbolic (-0.0021) / (0.0001) numeric (0.0003) attributes. (-0.0004) we (-0.0026) present (-0.0021) extensive (0.0008) empirical (-0.0010) studies, (-0.0020) using (0.0027) both (0.0005) real (0.0000) and (-0.0018) artificial (-0.0005) data, (-0.0025) that (0.0007) analyze (-0.0031) oc1 (0.0004) ' (-0.0020) s (0.0020) ability (-0.0012) to (0.0014) construct (0.0052) oblique (-0.0018) trees (-0.0029) that (-0.0004) are (-0.0001) smaller (-0.0008) and (-0.0011) more (-0.0005) accurate (-0.0019) than (-0.0009) their (-0.0004) axis- (0.0010) parallel (-0.0013) counterparts. (0.0004) we (-0.0083) also (0.0007) examine (-0.0041) the (0.0001) benefits (0.0008) of (0.0009) randomization (-0.0022) for (-0.0011) the (-0.0005) construction (0.0016) of (-0.0002) oblique (0.0017) decision (-0.0010) trees. (0.0004)
~~~~~~

**Node-1.5** (global 519):

~~~~~~text
title (0.0006) : (-0.0031) smoothing (0.0029) spline (-0.0018) anova (-0.0004) for (-0.0000) exponential (-0.0005) families, (0.0028) with (0.0005) application (0.0017) to (0.0002) the (-0.0056) wisconsin (-0.0060) epidemiological (-0.0005) study (0.0006) of (-0.0002) diabetic (-0.0011) abstract (-0.0029) : (0.0003) in (0.0039) this (0.0002) paper (0.0056) i (0.0088) give (0.0068) a (-0.0051) review (-0.0019) of (0.0003) ensemble (0.0107) learning (-0.0083) using (-0.0032) a (-0.0068) simple (-0.0054) example. (-0.0029)
~~~~~~

**Node-1.6** (global 2590):

~~~~~~text
title (0.0006) : (0.0009) backfitting (0.0000) in (0.0013) smoothing (0.0026) spline (0.0003) anova (-0.0009) abstract (0.0019) : (-0.0027) a (0.0016) scheme (0.0007) to (0.0016) compute (0.0008) smoothing (0.0020) spline (0.0004) anova (-0.0006) estimates (0.0020) for (0.0001) large (0.0006) data (0.0009) sets (0.0005) with (0.0010) a (0.0003) ( (0.0010) near (0.0003) ) (0.0006) tensor- (0.0001) product (0.0021) structure (0.0010) is (-0.0000) proposed. (-0.0004) such (0.0018) data (0.0007) sets (0.0004) are (0.0002) common (0.0008) in (0.0010) spatial- (0.0010) temporal (0.0009) analysis (0.0008) and (0.0011) image (0.0007) analysis. (0.0006) this (-0.0002) scheme (0.0008) combines (-0.0002) backfitting (0.0008) algorithm (0.0027) with (0.0009) iterative (0.0010) imputation (0.0012) algorithm (0.0025) in (0.0007) order (0.0006) to (0.0004) save (0.0003) both (0.0007) computational (0.0007) space (0.0005) and (0.0011) time. (0.0002) the (0.0002) convergence (0.0002) of (-0.0001) this (0.0003) algorithm (0.0014) and (0.0003) various (-0.0004) ways (0.0009) to (0.0007) further (0.0009) speed (0.0008) it (0.0007) up, (0.0006) such (0.0004) as (0.0007) collapsing (-0.0003) component (0.0016) functions (0.0008) and (0.0012) successive (0.0014) over- (0.0011) relaxation, (0.0003) are (0.0002) discussed. (-0.0042) issues (-0.0001) related (0.0007) to (0.0011) its (0.0009) application (0.0003) in (0.0009) spatial- (0.0012) temporal (0.0014) analysis (0.0005) are (0.0011) discussed (-0.0009) too. (0.0004) an (-0.0002) application (-0.0010) to (0.0026) a (0.0004) global (-0.0008) analysis (0.0007) of (0.0004) historical (0.0001) surface (0.0008) temperature (0.0002) data (0.0009) is (0.0021) described. (0.0004)
~~~~~~

**Node-2** (global 2223):

~~~~~~text
title (0.0450) : (0.0269) smoothing (0.0377) spline (0.0047) models (0.0262) with (0.0103) correlated (0.0264) random (0.0196) errors (0.0046) 1 (-0.0076) abstract (0.0016) : (0.0398) reinforcement (0.0051) learning (0.0411) can (0.0073) be (0.0243) used (0.0306) not (0.0182) only (0.0140) to (0.0063) predict (0.0076) rewards, (0.0140) but (0.0398) also (0.0064) to (0.0272) predict (0.0172) states, (-0.0045) i. (-0.0055) e. (-0.0473) to (0.0145) learn (-0.0006) a (0.0018) model (0.0122) of (-0.0008) the (0.0124) world (0.0026) ' (-0.0145) s (0.0149) dynamics. (0.0014) models (-0.0101) can (0.0134) be (-0.0003) defined (0.0139) at (0.0091) different (-0.0005) levels (0.0000) of (-0.0128) temporal (-0.0487) abstraction. (0.0307) multi- (0.0040) time (0.0100) models (0.0378) are (-0.0038) models (0.0323) that (-0.0020) focus (0.0154) on (-0.0002) predicting (0.0307) what (0.0183) will (0.0026) happen, (0.0053) rather (0.0138) than (0.0028) when (0.0174) a (-0.0296) certain (0.0305) event (0.0183) will (0.0044) take (0.0017) place. (0.0150) based (0.0154) on (0.0141) multi- (0.0185) time (0.0147) models, (-0.0257) we (0.0024) can (0.0505) define (0.0492) abstract (0.0002) actions, (0.0370) which (0.0063) enable (0.0603) planning (0.0211) ( (-0.0070) presumably (-0.0004) in (0.0185) a (-0.0337) more (0.0076) efficient (0.0303) way (0.0057) ) (0.0023) at (0.0117) various (0.0102) levels (0.0280) of (0.0108) abstraction. (0.0443)
~~~~~~

**Node-2.1** (global 190):

~~~~~~text
title (0.0003) : (0.0031) spline (0.0004) smoothing (0.0004) for (0.0009) bivariate (0.0002) data (0.0011) with (0.0037) applications (0.0006) to (0.0010) association (-0.0010) between (-0.0001) hormones (-0.0011) abstract (0.0016) : (0.0066) standard (0.0008) methods (0.0002) for (0.0018) inducing (0.0002) both (0.0015) the (0.0009) structure (-0.0009) and (0.0026) weight (0.0012) values (0.0018) of (0.0013) recurrent (-0.0003) neural (0.0008) networks (0.0002) fit (0.0003) an (0.0016) assumed (0.0013) class (0.0002) of (0.0005) architectures (-0.0007) to (0.0009) every (-0.0001) task. (0.0034) this (-0.0029) simplification (-0.0007) is (-0.0002) necessary (-0.0010) because (0.0010) the (0.0002) interactions (0.0002) between (-0.0007) network (-0.0009) structure (0.0006) and (0.0003) function (0.0010) are (0.0005) not (-0.0002) well (0.0015) understood. (-0.0035) evolutionary (0.0017) computation, (-0.0013) which (0.0017) includes (0.0001) genetic (0.0003) algorithms (-0.0020) and (0.0024) evolutionary (0.0003) programming, (-0.0004) is (-0.0008) a (-0.0002) population- (-0.0002) based (-0.0001) search (0.0016) method (0.0004) that (0.0006) has (0.0020) shown (-0.0005) promise (-0.0029) in (0.0012) such (0.0014) complex (-0.0005) tasks. (-0.0006) this (0.0005) paper (0.0011) argues (-0.0011) that (0.0026) genetic (-0.0007) algorithms (-0.0000) are (0.0020) inappropriate (-0.0014) for (0.0033) network (0.0001) acquisition (-0.0011) and (0.0015) describes (0.0004) an (0.0001) evolutionary (-0.0003) program, (0.0004) called (-0.0003) gnarl, (0.0009) that (-0.0001) simultaneously (0.0004) acquires (-0.0006) both (-0.0006) the (-0.0014) structure (-0.0005) and (-0.0010) weights (0.0014) for (0.0004) recurrent (0.0011) networks. (0.0001) this (-0.0003) algorithms (0.0009) empirical (-0.0043) acquisition (-0.0001) method (0.0001) allows (0.0002) for (-0.0015) the (-0.0001) emergence (-0.0012) of (-0.0010) complex (0.0005) behaviors (0.0017) and (0.0016) topologies (0.0005) that (0.0022) are (0.0011) potentially (0.0002) excluded (0.0002) by (0.0006) the (0.0002) artificial (0.0002) architectural (-0.0026) constraints (0.0009) imposed (0.0007) in (0.0012) standard (0.0010) network (0.0011) induction (-0.0020) methods. (0.0021)
~~~~~~

**Node-2.2** (global 510):

~~~~~~text
title (0.0016) : (0.0156) the (-0.0029) bayesian (0.0112) approach (0.0115) to (0.0060) tree- (0.0068) structured (0.0122) regression (0.0046) abstract (0.0143) : (-0.0046) technical (0.0191) report (0.0075) no. (0.0037) 967 (-0.0015) august (-0.0130) 1996 (0.0058)
~~~~~~
