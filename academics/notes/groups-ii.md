# Groups II
## Cayley's Theorem
operation of group on self transitive and free
cayley's theorem: finite group is isomorphic to subgroup of permutation group (order $n$ to $S_n$)
## Class Equation
centralizer $Z(x)$ = stabilizer
	center: elements that commute with everything
		element in center iff $Z(x) = G, C(x) = \{x\}$
conjugacy class $C(x)$ = orbit
$|G| = |Z(x)||C(x)|$, $|G| = \sum_k |C_k|$ (see [The Counting Formula](symmetry.md#the-counting-formula))
## Conjugation in the Symmetric Group
cycle type of permutation $p \in S_n$ describes how cycle notation partitions $[n]$
conjugacy preserves cycle type
## p-Groups
order of $p$-group is positive power of prime $p$
	center is not trivial group
	operation of $p$-group on set with order not divisible by $p$, element in $p$-group with $p$-group as stabilizer
	if order is $p^2$, group either cyclic or product of cyclics with order $p$, abelian
## Conjugation in the Symmetric Group
elements in symmetic group conjugate iff same cycle type
## The Sylow Theorems
sylow $p$-subgroup: $p$-group with index in group not divisible by $p$
first sylow theorem: finite group with order divisible by prime $p$ contains sylow $p$-subgroup, element of order $p$
second sylow theorem: sylow $p$-subgroups are conjugate subgroups, every $p$-subgroup contained in sylow $p$-subgroup
third sylow theorem: if group has order $n = mp^e$, number of sylow $p$-subgroups $s$ such that $ks = m, s = kp + 1$
## The Free Group
free group: generators satisfy no relations other than axioms
word: finite string of symbols
	reduce by cancelling symbols, unique reduced form
	products of equivalent words equivalent
set of equivalence classes of words is group, juxtaposition as composition
## Generators and Relations
relation $R$: word $r$ that evaluates to $1$
normal subgroup $\mathcal{R}$ generated by $R$ smallest normal subgroup of $G$ containing subset $R$ (obtained by multiplication, inversion, conjugation)
finite group presentation: finitely many generators, relations
free group $\mathcal{F}$ on set $S$ with relations $R$,  group generated by $S$ is $\mathcal{G} = \mathcal{F} / \mathcal{R} = \langle x_1, \ldots, x_n | r_1, \ldots, r_k \rangle$
	mapping property of free group: mapping of $S \to G$ extends uniquely to group homomorphism $\varphi : \mathcal{F} \to G$
	mapping property of quotient groups: generalization of first isomorphism theorem