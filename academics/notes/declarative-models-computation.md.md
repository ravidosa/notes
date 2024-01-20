# Declarative Models of Computation
imperative: programming as series of commands
declarative: declare what should be accepted
## Regular Expressions
regex: pattern matching set of strings
formalization
	syntax/semantics
		control alphabet $\Delta = \{\cup, (,), ^*, \emptyset, \epsilon\}$, input alphabet $\Sigma$, $\Gamma = \Sigma \cup \Delta$
		regex $R \in \Gamma^*$ if any of following cases:
			$R = b$ for $b \in \Sigma$ ($L(R) = \{b\}$)
			$R = \varepsilon$ ($L(R) = \{\varepsilon\}$)
			$R = \emptyset$ ($L(R) = \{\}$)
			$R = R_1\cup R_2$ ($L(R) = L(R_1) \cup L(R_2)$)
			$R = R_1R_2$ ($L(R) = L(R_1) \circ L(R_2)$)
			$R = R_1^*$ ($L(R) = L(R_1)^*$)
## Context-free Grammars
context-free grammars: productions for replacing variables
formalization
	syntax
		context-free grammar $G = (\gamma, \Sigma, S, \rho)$
		variables $\Gamma$, terminals $\Sigma$
		start symbol $S \in \Gamma$
		rules $\rho \subset \Gamma \times (\gamma \cup \Sigma)^*$
	semantics
		accepts string $x$ if there is sequence of derived strings $x_1, \ldots x_k \in (\Gamma \cup \Sigma)^*$
			$x_1 = S, x_k \in \Sigma^*, x_i \Rightarrow x_{i+1}$
right regular grammar
	all rules either $\varepsilon$ or $bC$ for $b \in \Sigma, c \in \Gamma$
## Nondeterministic Finite Automata
similar to DFA but with $\varepsilon$ transitions, multiple transitions, missing transitions
formalization
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