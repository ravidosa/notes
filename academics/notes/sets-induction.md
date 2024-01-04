# Sets and Induction
sets
	$A = \{x: P(x)\}$
	null set $\varnothing$
	element of $\in$
	subset of (or equal to) $\subseteq$
		$\forall x (x \in A \implies x \in B)$
	power set $\mathcal{P(A)} = \{B: B \subseteq A\}$
	set operations
		union $A \cup B = \{x: x \in A \lor x \in B\}$
		intersection $A \cap B = \{x: x \in A \land x \in B\}$
			disjoint: $A \cap B = \varnothing$
		difference $A - B = \{x: x \in A \land x \notin B\}$
			complement $A^c = U - A$ for universe $U$
		product $A \times B = \{(a,b): a \in A \land B \in B\}$
principle of mathematical induction
	prove base case
	prove that case $n$ implies case $n+1$
