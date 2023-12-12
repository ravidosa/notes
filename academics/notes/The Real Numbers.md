field $F$
	set with 2 binary operations ($+$, $\cdot$)
	commutative, associative
	identities, inverses
	distributive
	$\mathbb{R}, \mathbb{C}, \mathbb{Q}$
ordering $P$
	closed subset of field under $+, \cdot$
	no additive identity
	either $x\in P$, $x=0$, $-x\in P$
	$x > y$ if $y - x$ in $P$
	$\mathbb{R}, \mathbb{Q}$ ordered
	$S \subset F$ is bounded above if $\exists a \in F$ such that $\forall x \in S (x \leq a)$ with upper bound $a$, similar principle for bounded below
		least upper bound $\mathrm{sup}(S) \leq a$ for all $a$
			for $\mathbb{R}$, if bounded above, then unique least upper bound exists (axiom of completeness)
			$a = \mathrm{sup}(S)$ iff $\forall \epsilon > 0 ( \exists s \in S ( a - \epsilon < s))$
		archimedean property
			$\mathbb{N} \subset \mathbb{R}$ not bounded above
			for $x \in \mathbb{R}$, there is $n \in \mathbb{N}$ such that $n > x$
			denseness of $\mathbb{Q}$, rational number between two reals
intervals
	open interval $(a, b) = \{x \in \mathbb{R} : a < x < b\}$
	closed interval $[a, b] = \{x \in \mathbb{R} : a \leq x \leq b\}$
		infinite intersection of nested closed intervals is nonempty (nested interval property)
absolute value function $|x| = \begin{cases} x & x \geq 0 \\ -x & x < 0\end{cases}$
	$|x| \geq 0$, $|x| = 0$ iff $x = 0$
	$|x|||y| = |xy|$, $|x + y| \leq |x| + |y|$
cardinality
	same cardinality ($A \sim B$) if one-to-one and onto mapping exists
	countably infinite if $A \sim \mathbb{N}$, uncountably infinite otherwise
		rationals countable, reals uncountable
		subset of countable is countable or finite
		finite union of countable is countable
		arbitrary intersection of countable is countable