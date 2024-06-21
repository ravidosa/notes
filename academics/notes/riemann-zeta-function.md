# Riemann Zeta Function
dirichlet series: $\varphi(s) = \sum_n \frac{a_n}{n^s}$
number-theoretic function: $f(1), f(2), \ldots$
	[mobius function](mobius-function.md)
	if $g(n) = \sum_{d|n}f(d)$, $f(n) = \sum_{d|n} g(d)\mu(\frac{n}{d})$ (mobius inversion)
prime number theorem
	$\pi(x)$ is number of primes $\leq x$
	$\lim_{x\to\infty} \frac{\pi(x)\log x}{x} = 1$
riemann zeta function
	$\zeta(s) = \sum_n \frac{1}{n^s} = \prod_k \frac{1}{1 - p_k^{-s}}$ where $p_k$ is $k$th positive prime (second only if $\mathrm{Re}(s) > 1$)
	simple pole at $1$ with residue $1$
		$\zeta(s) = \frac{1}{s - 1} + g(s)$ for entire $g(s)$
	riemann hypothesis: zeros only when $s = -2, -4, \ldots$ (trivial zeros) and $s = \frac{1}{2} + ti$
		critical strip ($0 < \mathrm{Re}(s) < 1$)
			infinte in critical strip, none when $\mathrm{Re}(s) = 1$
	[order](hadamard-factorization-theorem.md) $1$
riemann functional equation
	$\zeta(s) = 2^s\pi^{s-1}\sin\frac{\pi s}{2}\Gamma(1 - s)\zeta(1 - s)$