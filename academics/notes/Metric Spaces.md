metric $d: X \times X \to \mathbb{R}$
	positive definite $d(x, y) \geq 0$, $d(x, y) = 0$ iff $x = y$
	symmetric $d(x, y) = d(y, x)$
	triangle inequality $d(x, z)\leq d(x, y) + d(y, z)$
	examples
		$d(x, y) = \begin{cases} 0 & x = y \\ 1 & x \neq y\end{cases}$  on any $X$
		$d(x, y) = |x - y|$ on $\mathbb{R}$
		$d((x_1, x_2), (y_1, y_2)) = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2}$  on $\mathbb{R}^2$
	open ball $V_{\epsilon}(x_0) = \{x \in X : d(x, x_0) < \epsilon\}$
		open intervals with euclidean metric on $\mathbb{R}$
	closed ball $B_{\epsilon}(x_0) = \{x \in X : d(x, x_0) \leq \epsilon \}$
	sequence $(x_n)$ in $(X, d)$
		converges to $L \in X$ if $\forall \epsilon > 0 (\exists N \in \mathbb{N} (n > N \implies d(x_n, L) < \epsilon))$
		cauchy if  $\forall \epsilon > 0 (\exists N \in \mathbb{N} (m, n > N \implies d(x_m, x_n) < \epsilon))$
		bounded if $\exists M > 0, x_0 \in X  d(x_n, x_0) < M)$
		$d(a, b) < c$ equivalent to $a \in V_c(b)$
		metric space complete if any cauchy sequence converges