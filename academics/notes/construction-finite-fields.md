# Construction of Finite Fields
modulo equivalence relation using irreducible polynomial gives finite field of polynomials
	irreducible polynomial of degree $n$ in $\mathbb{F}_p[x]$ -> field of order $p^n$
mobius inversion $\pi(n, \mathbb{F}_q)$
	counts number of monic irreducible polynomials of degree $n$ in $\mathbb{F}_q[x]$
	$\frac{q^n - 2(q^{\lfloor \frac{n}{2} \rfloor} - 1)}{n} \leq \pi(n, \mathbb{F}_q) \leq \frac{q^n}{n}$
		$\pi(n, \mathbb{F}_q) = \frac{1}{n}\sum_{d|n} \mu(d)q^{\frac{n}{d}}$
	approximated similar to primes
for prime power $q = p^n$, there exists finite field of size $q$
	direct consequence of mobius inversion, at least one irreducible polynomial of degree $n$ in $\mathbb{F}_p$