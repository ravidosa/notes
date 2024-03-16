# Regular Language
regular: decided by [DFA](deterministic-finite-automaton.md), [NFA](nondeterministic-finite-automaton.md), [regex](regular-expression.md), [RRG](context-free-grammar.md)
## Myhill-Nerode Theorem
separating extension: $xz, yz$ have only one in $L$
	$x, y$ are $L$-separable, $L$-equivalent if no such $z$
	equivalence relation $\sim_L$
regular iff $\sim_L$ partitions into finite number of equivalence classes
## Pumping Lemma
pumping length of regular language $p$
for $w \in L$, $|w| \geq p$, $w = xyz$ where $xy^kz \in L$ for all $k$, $|y| > 0$, $|xy| \leq p$
