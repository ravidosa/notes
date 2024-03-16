# Context-free Grammar
context-free grammars: productions for replacing variables
right regular grammar
	all rules either $\varepsilon$ or $bC$ for $b \in \Sigma, c \in \Gamma$
left regular grammars are also regular
## Formalization
syntax
	context-free grammar $G = (\gamma, \Sigma, S, \rho)$
	variables $\Gamma$, terminals $\Sigma$
	start symbol $S \in \Gamma$
	rules $\rho \subset \Gamma \times (\gamma \cup \Sigma)^*$
semantics
	accepts string $x$ if there is sequence of derived strings $x_1, \ldots x_k \in (\Gamma \cup \Sigma)^*$
		$x_1 = S, x_k \in \Sigma^*, x_i \Rightarrow x_{i+1}$
## Equivalence
[NFA](nondeterministic-finite-automaton.md)
	NFA with no $\varepsilon$-transitions