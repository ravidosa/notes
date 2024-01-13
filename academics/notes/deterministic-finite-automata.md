# Deterministic Finite Automata
idealized computational device
	no memory beyond finite set of states
		accept and reject states
	starts in certain state, reads one input symbol at a time
	transitions: map current state and symbol to next state
	decides language ($L(D)$), accepts/rejects strings
formalization
	syntax
		deterministic finite automaton (dfa) $D = (Q, \Sigma, \delta, s, F)$
		finite non-empty set of states $Q$
		input alphabet $\Sigma$
		start state $s \in Q$
		accepting states $F \subseteq Q$
		transition function $\delta : Q \times \Sigma \to Q$
			transition table
	semantics
		accepts string $x \in \Sigma^n$ if there is computation sequence $q_0,\ldots q_n \in Q$
			$q_0 = s, q_n \in F, \delta(q_i, x[i + 1]) = q_{i+1}$
			rejects otherwise
		language decided by $D$ $L(D) = \{ x \in \Sigma^* | D \text{ accepts } x\}$
			language $L$ DFA-decidable if some DFA decides $L$
				solvable by algorithm using constant amount of memory in real time
		