# Turing Machine
finite automaton with unbounded read/write tape memory
	blank cells
turing-recognizable language: some TM accepts string in language, rejects/loops otherwise
decidable language: some TM accepts string in language, rejects otherwise
variants
	equivalent: multitape, 2-way infinite, multiple tape heads, 2d tape, RAM, right or reset, two stacks, queue, three counters
	less power: one stack, two counters, bounded memory
church-turing thesis: all functions that are computable can be computed by turing machine
## Formalization
syntax
	turing machine $M = (Q, \Sigma, \Gamma, \delta, s, q_a, q_r)$
	finite set of states $Q$
	input alphabet $\Sigma$
	tape alphabet $\Gamma$, $\Sigma \subset \Gamma$, blank in $\Gamma \backslash \Sigma$
	start state $s$, accept state $q_a$, reject state $q_r$
	transition function $\delta : (Q \backslash \{q_a, q_r\}) \times \Gamma \to Q \times \Gamma \times \{L, R, S\}$
semantics
	configuration $C = (q, p, w)$
		current state $q$, tape head position $p$, tape content $w$
		$\delta(q, w[p]) = (q', w'[p], m)$, move tape head position and leave rest of tape unchanged
		accepting if $q = q_a$, rejecting if $q = q_r$, halting if accepting or rejecting
	accepts string $x \in \Sigma^*$ if there is configuration sequence with first initial configuration, last accepting, intermediate transition to next