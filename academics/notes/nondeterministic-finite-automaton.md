# Nondeterministic Finite Automaton
similar to [DFA](deterministic-finite-automaton.md) but with $\varepsilon$ transitions, multiple transitions, missing transitions
## Formalization
syntax
	deterministic finite automaton (nfa) $N = (Q, \Sigma, \Delta, s, F)$
	finite non-empty set of states $Q$
	input alphabet $\Sigma$
	start state $s \in Q$
	accepting states $F \subseteq Q$
	transition function $\delta : Q \times \Sigma_{\varepsilon} \to \mathcal{P}(Q)$
		transition table
semantics
	accepts string $x = x_1\ldots x_n \in \Sigma^n$ if there is computation sequence $q_0,\ldots q_n \in Q$
		$q_0 = s, q_n \in F, q_{i+1} \in \delta(q_i, x_{i + 1})$
		rejects otherwise
## Closure
union
	$\varepsilon$-transition to either start state from start state
concatenation
	$\varepsilon$-transition from first accept states to second start state
kleene star
	$\varepsilon$-transition from accept states to start state, new start state to start state
## Equivalence
[DFA](deterministic-finite-automaton.md)
	subset construction
	exponential blowup in states
[regex](regular-expression.md)
	expression automata