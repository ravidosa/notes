# Hadamard Factorization Theorem
represent nonconstant entire function as product of entire functions and exponential
product of infinite sequence: similar to sums
	$\lim_{n\to\infty} a_n = 1$ necessary for convergence
	convergent iff $\sum \log a_n$ converges
	converges absolutely if converges for any rearrangement, if $\sum |\log a_n|$ converges
	$\prod (1 + a_n)$ converges iff $\sum |a_n|$ converges
product of sequence of entire functions with bounded absolutely convergent sum converges locally uniformly
weierstrass product theorem: for isolates $z_n$, there is some sequence $m_n$, $P(z) = z^k\prod_{n=1}^\infty E(\frac{z}{z_n}, m_n)$ where $P(z)$ is entire with root of multiplicity $k$ at $z = 0$ and roots at $z_n$
	weierstrass primary factor $E(z, m) = (1 - z)e^{\sum_{i=1}^m \frac{x^i}{i}}$
	weierstrass factorization theorem: $f(z) = z^ke^{g(z)}\prod_n E(\frac{z}{z_n}, m_n)$ for entire $f(z)$ (reverse of product theorem)
order of functions
	finite order if $|f(z)| \leq Ae^{B|z|^a}$, order is lower bound of $a$
		$e^{p(z)}$ for polynomial $p$ has order of degree of polynomial
		$e^{e^z}$ not finite order
		$\cos z, \sin z$ have finite order
		$\cos\sqrt{z}$ has order $\frac{1}{2}$
		order of sum and product is at most max of orders, linear shift has same order, polynomial shift has multiple of order
exponent of convergence: $\sum_n |z_n|^{-a}$ is finite (at most order, exponent is greatest lower bound)
	$\mu = 1$ for $z_n = n, n\log^2 n$, $z_n = \log n$ not finite EOC, $\mu = 0$ for $z_n = 2^n$
	$\sin \pi z = \pi z\prod_n (1 - \frac{z^2}{n^2})$
	jensen's formula: $\log|f(0)| = \frac{1}{2\pi}\int_0^{2\pi} \log|f(Re^{i\theta})| \, d\theta + \sum_{k=1}^n \log |\frac{z_k}{R}|$
	borel-caratheodory lemma: if real part of analytic function bounded by $M$ on boundary ball of radius $R + \epsilon$ around $0$, $|f^{(n)}(0)| \leq \frac{2n!}{R^n}(M - u(0))$
hadamard factorization theorem
	$p = \begin{cases}\mu - 1 & \mu \in \mathbb{Z}, \mu \text{ is at least EOC} \\ \lfloor \mu \rfloor & \text{otherwise}\end{cases}$
	canonical product $P(z) = \prod_n E(\frac{z}{z_n}, p)$
	$f(z) = z^ke^{g(z)}P(z)$
		$k \geq 0$ is order of zero at $z = 0$
		$P(z)$ is canonical product formed by sequence of nonzero zeros
		$g$ has degree at most the order
[gamma function](gamma-function.md)
