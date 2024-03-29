# Groups
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
## Subgroups of Additive Group of Integers
either trivial subgroup or form $\mathbb{Z}a$ where $a$ is smallest positive integer in subgroup
euclidean algorithm for gcd
relatively prime $a, b$: $ra + sb = 1$ for integer $r, s$
	if prime $p$ divides $ab$, $p$ divides $a$ or $b$
## Cyclic Groups
cyclic subgroup $\langle x \rangle \subseteq G$ generated by $x$: $\{\ldots, x^{-2}, x^{-1}, 1, x, x^2, \ldots\}$
	$S = \{k : x^k = 1\}$ is subgroup of $\mathbb{Z}^+$
		$x^r = x^s$ iff $x^{r-s} = 1$
		$S$ not trivial subgroup, then $S = \mathbb{Z}n$, $\langle x \rangle$ has order $n$
			order $n$: $n$ is smallest positive integer such that $x^n = 1$
			if $x^n \neq 1$ for all $n \neq 0$, infinite order,  infinite cyclic
klein four group, quaternion group
## Homomorphisms
homomorphism: map $G \to G'$, $\varphi(ab) = \varphi(a)\varphi(b)$
	determinant, sign homomorphism, exponential map, absolute value map
	trivial homomorphism: maps everything to identity
	inclusion map: subgroup to group, $i(x) = x$
	extendable to multiple: $\varphi(a_1\ldots a_k) = \varphi(a_1)\ldots\varphi(a_k)$
	maps identity to identity: $\varphi(e_G) = e_{G'}$
	maps inverses to inverses: $\varphi(a^{-1}) = \varphi(a)^{-1}$
	image $\mathrm{im} \varphi = \{x \in G' : \exists a \in G (\varphi(a)  = x)\}$: image of domain, subgroup of $G'$
	kernel $\mathrm{ker} \varphi = \{a \in G : \varphi(a) = 1\}$: elements mapped to identity, subgroup of $G$
		kernel of $GL_n$ is $SL_n$, kernel of sign homomorphism $S_n$ is alternating group ($A_n$, even permutations)
cosets
	left coset of $H \leq G$: $aH = \{g \in G : \exists h \in H (g = ah)\}$ (similar for right coset)
	$\varphi(a) = \varphi(b)$,  $a^{-1}b$ in kernel $K$, $b$ in $aK$, $bK = aK$
	injective iff kernel is trivial subgroup
normal subgroup $N \unlhd G$
	conjugate by $g$: $gag^{-1}$
	all conjugates by element of $G$ are in $N$
	kernel is normal subgroup
	all subgroups normal for abelian $G$
## Isomorphisms
isomorphism: bijective homomorphism
	inverse map also isomorphism
	isomorphic groups $G \approx G'$: isomorphism exists between $G$ and $G'$
		isomorphism class of $G$
	endomorphism: homomorphism to self
		automorphism: endo + iso
commutator $aba^{-1}b^{-1}$: elements commute iff commutator is identity
	center of group: commutes with everything
		set of diagonal matrices
## Equivalence Relations and Partitions
see [Relations and Partitions](relations-partitions.md)
equivalence classes of $S$ partition $S$
## Cosets
left/right cosets partition group
all left/right cosets have same order
	index $[G : H]$: number of cosets of $H$
	$|G| = |H|[G : H]$
		$[G : K] = [G : H][H : K]$
	$|G| = |\mathrm{ker}\varphi|\cdot|\mathrm{im}\varphi|$
cyclic group of prime order generated by any non-identity element
right cosets
	$H$ is normal, $gHg^{-1} = H$, $gH = Hg$, left coset is also right coset
	if single subgroup, then normal
## Modular Arithmetic
see
## The Correspondence Theorem
equivalence relation of elements mapped to same element (preimage)
restriction map: restrict mapping $\varphi$ to homomorphism of $H \unlhd G$ as $\varphi\vert_H$, kernel is $\mathrm{ker}\varphi \cap H$, image is $\varphi(H)$

correspondence theorem: surjective group homomorphism $\varphi : G \to \mathcal{G}$, bijective map between subgroups of $G$ containing kernel $K$ and subgroups of $\mathcal{G}$
	$\mathcal{H}$ bijectively corresponds to $H = \varphi^{-1}(\mathcal{H})$
	corresponding subgroups $H, \mathcal{H}$, $H \unlhd G$ iff $\mathcal{H} \unlhd \mathcal{G}$, $|H| = |\mathcal{H}||K|$
## Product Groups
component-wise multiplication
	$i_A(a)=(a, 1)$
	$i_B(b) = (1, b)$
	$p_A(a, b) = a$
	$p_B(a, b) = b$
relatively prime $a, b$, cylic group of order $ab$ isormophic to product of cyclic $a$ and cyclic $b$
product groups $HK$ for $H, K \leq G$
	injective iff $H \cap K =  \{e\}$
	homomorphism iff commute
	if $H$ normal,  product group is subgroup
	isomorphism iff injective, $HK = G$, $H, K \unlhd G$
## Quotient Groups
set of cosets of normal subgroup form group $\overline{G} = G / N$
	law of composition that turns $\overline{G}$ into group with surjective homomorphism canonical map $\pi(g) = \overline{g}$ with kernel $N$
	for cosets $aN, bN$, $abN = (aN)(bN)$
first isomorphism theorem
	for surjective homomorphism $\varphi : G \to G'$ with kernel $N$, $\overline{G}$ isomorphic to $G'$ with unique isomorphism $\overline{\varphi} : \overline{G} \to G'$ with $\varphi = \overline{\varphi} \circ \pi$
	$\varphi$ factors through $\overline{G}$
	$G / \mathrm{ker} \varphi \approx \mathrm{im} \varphi$, if $\varphi$ surjective $G' \approx G / \mathrm{ker} \varphi$