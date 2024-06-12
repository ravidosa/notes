# Group
## Laws of Composition
law of composition: maps $S \times S \to S$
	product/sum of $a$ and $b$
	associative: $(ab)c = a(bc)$
	commutative: $ab = ba$
	identity: $ea = ae = a$
	inverse: $aa^{-1} = a^{-1}a = e$
		invertible if both left and right inverse
		unique inverse
		$(ab)^{-1} = b^{-1}a^{-1}$
## Groups and Subgroups
group: set $G$ + law of composition $\circ$
	composition associative
	identity element
	every element has inverse
	abelian: composition commutative
		$\mathbb{Z}^+, \mathbb{R}^+, \mathbb{R}^\times, \mathbb{C}^+, \mathbb{C}^\times$
	order $|G|$: number of elements in $G$, aka cardinality
		finite or infinite
	cancellation: $ab = ac$ or $ba = ca$ implies $b = c$
	$n \times n$ general linear group $GL_n$: set of all invertible $n \times n$ matrices
	symmetric group $S_n$: set of all permutations of $\{1, 2, \ldots, n\}$
subgroup: $H \subseteq G$
	closure
	identity
	inverses
	circle group $S^1$, $n \times n$ special linear group $SL_n$ (matrices with determinant $1$)
	intersection of subgroups is subgroup
	order of subgroup divides order of group
## Cyclic Groups
cyclic subgroup $\langle x \rangle \subseteq G$ generated by $x$: $\{\ldots, x^{-2}, x^{-1}, 1, x, x^2, \ldots\}$
	$S = \{k : x^k = 1\}$ is subgroup of $\mathbb{Z}^+$
		$x^r = x^s$ iff $x^{r-s} = 1$
		$S$ not trivial subgroup, then $S = \mathbb{Z}n$, $\langle x \rangle$ has order $n$
			order $n$: $n$ is smallest positive integer such that $x^n = 1$
			if $x^n \neq 1$ for all $n \neq 0$, infinite order,  infinite cyclic
klein four group, quaternion group
## Examples
$Z_N$ subgroups of additive group of integers
	either trivial subgroup or form $\mathbb{Z}a$ where $a$ is smallest positive integer in subgroup
	euclidean algorithm for gcd
	relatively prime $a, b$: $ra + sb = 1$ for integer $r, s$
		if prime $p$ divides $ab$, $p$ divides $a$ or $b$
$Z_2$, $+ = \oplus$
	$Z_2^n$ for $n$-bit strings, $\oplus$ as group operation
	$a \oplus b$ uniformly distributed if $a$ uniformly distributed, if $a \oplus b'$ uniformly distributed