# Laurent Series
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
		