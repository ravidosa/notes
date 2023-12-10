mapping $f: X \to Y$
	for $A \subset X$, $f(A) = \{f(x) \in Y : x \in A\} \subset Y$
	for $B \in Y$, $f^{-1}(B) = \{x \in X : f(x) \in B\}$
	$f(A) \subset B$ iff $A \subset f^{-1}(B)$
	continuous if for open $U \subset Y$, $f^{-1}(U)$ open in $X$
		any map in discrete topological space continuous, only constant maps continuous in trivial topological space
		in metric space
			$\forall x \in X, \epsilon > 0 (\exists \delta > 0 (V_{\delta}(x) \subset f^{-1}(V_\epsilon(f(x)))))$
			on $\mathbb{R}$
				$L = \lim_{x\to a}f(x)$ if $\forall \epsilon > 0(\exists \delta > 0 (\forall x (0 < |x - a| < \delta \implies |f(x) - L| < \epsilon)))$
				continuous if $\forall a \in \mathbb{R} (\lim_{x\to a} f(x) = f(a))$
			uniform continuity
				$\forall \epsilon > 0 (\exists \delta > 0 (\forall a, b \in X (d_X(a, b) < \delta \implies d_Y(f(a), f(b)) < \epsilon)))$
				continuous on compact is uniformly continuous
		preimage of closed is closed
		image of compact is compact
			mapping in $\mathbb{R}$ has maximum and minimum over compact subset (extreme value theorem)
		image of connected is connected
			mapping in $\mathbb{R}$ reaches every point between endpoints (intermediate value theorem)
		image of dense is dense for surjective mapping
		composition of continuous is continuous
	right limit $L = \lim_{x\to a^+}$ if $\forall \epsilon > 0 (\exists \delta > 0 (\forall a < x < a + \delta \implies |f(x) - L| < \epsilon))$, similar for left limit
		limit exists iff left and right limit exist and are equal
		discontinuous at $a$ if not continuous at $a$
			removable: limit exists but not equal to function
			jump: left and right limit not equal
			essential: none of the above
	sets of discontinuity
		$F_\sigma$ class of sets written as countable union of closed sets
		$D_f \subset \mathbb{R}$ points where discontinuous is $F_\sigma$
		$\alpha$-continuous at $a$ if $\exists \delta > 0 (\forall x, y \in V_\delta(a) |f(x) - f(y)| < \alpha)$
			$D_f^\alpha \subset \mathbb{R}$ points where not $\alpha$-continuous
				closed
			$D_f = \bigcup_n D_f^{\frac{1}{n}}$