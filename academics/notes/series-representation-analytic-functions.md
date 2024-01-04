# Series Representation of Analytic Functions
now low regularity analytic functions
	if derivative, then derivative of all orders in open set
	taylor series convergence (see [Analytic Functions](analytic-functions.md))
complex FTC holds only for analytic function with continuous derivative
cauchy-goursat theorem: if analytic in simply connected open set, line integral over every closed curve is zero
	cauchy integral formula: $f^{(n)}(z) = \frac{n!}{2\pi i} \oint_C \frac{f(w)}{(w -z)^{n+1}} dw$
	same for every positively oriented curve that winds around $z$ once
weak max principle: if $f$ analytic in closed ball, $f$ bounded by $M$
	max principle: analytic function has max modulus on boundary (also min if no zeros)
cauchy's inequality: if $f$ analytic in closed ball, $f^{(n)}$ bounded by $\frac{n!}{R^n}M$
liouville's theorem: every bounded entire function is constant
	fundamental theorem of algebra: complex polynomial of degree $n \geq 1$ has at least one root
morera: if $f$ continuous and line integral over every closed curve is zero, then $f$ analytic
harmonic functions: $\nabla^2 u = \Delta u  = 0$
	if $u, v$ harmonic and $u + iv$ analytic, $u, v$ are harmonic conjugates
	equal to average on circle
	for harmonic $u$, harmonic conjugate $v$ exists
		if $C^2$, then $C^{\infty}$
		locally expandable as taylor series
FTC extension
	three from classical physics (see [Vector Analysis](vector-analysis.md))
	complex variables fourth: $\oint f'(z) \, dz = f(B) - f(A)$
laurent series: $f(z) = \sum_{n=-\infty}^{\infty} a_n(z - z_0)^n, a_n = \frac{1}{2\pi i} \oint \frac{f(z)}{(z - z_0)^{n+1}} \, dz = \frac{f^{(n)}(z_0)}{n!}$
	converges in annulus $r_1 < |z - z_0| < r_2$
	isolated singularity: $r_1= 0$
		pole: finite number of nonzero $a_{n}$ terms for negative $n$
			simple pole: $\lim_{z\to z_0} (z - z_0)f(z) = a_{-1} \neq 0$
			pole of order $\leq k$
				$|f(z)| \leq \frac{M}{|z - z_0|^k}$
				$\lim_{z\to z_0} (z - z_0)^{k+1}f(z) = 0$, $\lim_{z\to z_0} (z - z_0)^{k}f(z)$ exists
		essential singularity: infinite number of nonzero $a_{n}$ terms for negative $n$ (infinite order pole)
			infinitely many solutions to $f(z) = w$ in deleted neighborhood of $z_0$
		removable singularity: zero nonzero $a_{n}$ terms for negative $n$
			bounded in deleted neighborhood
			$\lim_{z\to z_0} f(z), \lim_{z\to z_0} (z - z_0)f(z)$ exist
		$a_{-1}$ is residue of $f$ at $z_0$
			$\oint f(z) \, dz = 2\pi i \cdot a_{-1}$
		meromorphic: analytic except for poles
		for $f(z), g(z)$ with $n, k$ zeros:
			$\frac{f(z)}{g(z)}$ at $z_0$ is pole of order $k - n$ ($k > n$) or removable singularity with nonzero limit $k = n$, removable singularity with zero of order $n - k$ ($k < n$)