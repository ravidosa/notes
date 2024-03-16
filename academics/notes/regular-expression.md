# Regular Expression
regex: pattern matching set of strings
## Formalization
syntax/semantics
	control alphabet $\Delta = \{\cup, (,), ^*, \emptyset, \epsilon\}$, input alphabet $\Sigma$, $\Gamma = \Sigma \cup \Delta$
	regex $R \in \Gamma^*$ if any of following cases:
		$R = b$ for $b \in \Sigma$ ($L(R) = \{b\}$)
		$R = \varepsilon$ ($L(R) = \{\varepsilon\}$)
		$R = \emptyset$ ($L(R) = \{\}$)
		$R = R_1\cup R_2$ ($L(R) = L(R_1) \cup L(R_2)$)
		$R = R_1R_2$ ($L(R) = L(R_1) \circ L(R_2)$)
		$R = R_1^*$ ($L(R) = L(R_1)^*$)
## Equivalence
[NFA](nondeterministic-finite-automaton.md)
	6 elementary automata, connect