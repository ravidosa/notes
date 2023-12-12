sequence $(a_n)$
	function with domain $\mathbb{N}$
	sequence converges to $\lim_{n\to\infty} a_n = a$ if $\forall \epsilon > 0 (\exists N \in \mathbb{N} (n \geq N \implies |a_n - a| < \epsilon))$
		limit, if exists is unique
		if sequence does not converge, it diverges
		$\epsilon$-neighborhood/open ball $V_{\epsilon}(a) = \{ x \in \mathbb{R} :: |x - a| < \epsilon \}$
			converges if every $\epsilon$-neighborhood of $a$ contains all terms in sequence after some point
		algebraic limit theorem
			$\lim ca_n = c\lim a_n$
			$\lim a_n + b_n = a + b$
			$\lim a_nb_n = ab$
			$\lim\frac{a_n}{b_n} = \frac{a}{b}$
		order limit theorem
			if $a_n \geq 0$, $a \geq 0$
			if $a_n \leq b_n$, $a \leq b$
			limit greater than lower bound, less than upper bound
	sequence bounded if $\exists M > 0 (\forall n \in \mathbb{N} (|a_n| \leq M))$
		all convergent sequences bounded, but not vice versa
	monotonicity
		increasing if $a_{n+1} \geq a_n$, similar for decreasing, monotone if increasing or decreasing
			if monotone and bounded, then convergent (monotone convergence theorem)
	subsequence $(a_{n_k})$, terms in same order without repetitions
		converge to same limit as original, if subsequences with different limit then divergent
		bolzano-weierstrass theorem: every bounded sequence contains convergent subsequence
series $\sum_{n=1}^{\infty} a_n = A$
	converges to limit of sequence from partial sums
		cauchy condensation test
			decreasing positive sequence $(b_n)$ converges if $\sum_{n=0}^{\infty} 2^nb_{2^n}$ converges
		algebraic limit theorem
			$\sum ca_k = c\sum a_k$
			$\sum a_k + b_k = A + B$
		doubly indexed series
			if $\sum_{i=1}^{\infty}\sum_{j=1}^{\infty} |a_{ij}|$ converges, $\sum_{i=1}^{\infty}\sum_{j=1}^{\infty} a_{ij}$ and $\sum_{j=1}^{\infty}\sum_{i=1}^{\infty} a_{ij}$ converge
			$\sum_{i=1}^{\infty}\sum_{j=1}^{\infty} a_ib_j = AB$
		see [Infinite Series and Power Series](Infinite%20Series%20and%20Power%20Series.md)
cauchy criterion
	cauchy sequence $(a_n)$ if $\forall \epsilon > 0 (\exists N \in \mathbb{N} (m, n \geq N \implies |a_n - a_m| < \epsilon))$
	all convergent sequences are cauchy
		sequence in $\mathbb{R}$ converges iff cauchy
		real number is equivalence class of cauchy sequences
	all cauchy sequences bounded
