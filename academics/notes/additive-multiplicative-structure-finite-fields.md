# Additive and Multiplicative Structure of Finite Fields
see [Group Theory](groups-i.md#cyclic-groups)
for all $\alpha \in \mathbb{F}_q$, $q\alpha = 0, \alpha^q = \alpha$
## Additive Structure
characteristic of field: order of $1$
	characteristic zero: $1$ has infinite order under addition
		smallest $\mathbb{Q}$
	if finite, order/characteristic $p$ is prime
		smallest $\mathbb{F}_p$
		additive group isomorphic to $C_p^r$, $|F| = p^r$
			monic polynomials of degree $< k$ form basis for field generated from monic irreducible polynomial of degree $k$
			subfield of field of size $p^k$ has size $p^d$ for $d|k$
## Multiplicative Structure
$\mathbb{F}_q$ is cyclic, has $\phi(q - 1)$ generators (primitives in the field)
	determine using trial and error
	extend to polynomial finite fields
		primitives facilitate multiplication over finite fields
## Applications
squares in finite fields
	for $q = 2^r$, every element has square root
	for odd $q$, even powers of primitives have square root, $\frac{q - 1}{2}$ nonzero squares
		if $q \equiv 1 \mod 4$, $-1$ has square root
		if $q \equiv 3 \mod 4$, $-1$ does not have square root
			if $q$ prime, set of nonzero squares if difference set (parameters $(4n + 3, 2n + 1, n)$), $n$ ways of representing as difference of squares