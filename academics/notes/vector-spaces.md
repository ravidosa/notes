# Vector Spaces
## Subspaces of $\mathbb{R}^n$
vector addition, scalar multiplication
subspace
	closed under addition + scalar multiplication, contains zero vector
	proper subspace: not $\{0\}$ or $\mathbb{R}^n$
		distinct proper subspaces only have zero vector in common
linear maps preserve structure
### Fields
ring
	see [Rings](rings.md)
field
	see [Fields](fields.md)
## Vector Spaces
vector space $V$ over field $F$ with addition, scalar multiplication as laws of composition
	addition commutative
	multiplication identity, associative
	multiplication distributes over addition
## Bases and Dimension
linear combination of ordered set of vectors (hypervector): vector expressible as sum and scalar multiple of set vectors
	span of hypervector: all vectors that can be expressed as linear combination
	if hypervector in subspace, span in subspace
	linearly independent: no vector is linear combination of other vectors, only trivial combination is zero vector
basis of $V$: linearly independent vectors that span $V$
	every vector expressible as unique linear combination
	all bases have same order
finite-dimensional vs infinite-dimensional
	subspace has at most dimension of $V$
spanning subset has at least as many elements as independent subset, basis subset in between
	$|S| \geq |B| \geq |L|$
## Computing with Bases
isomorphism sending vector to vector in basis
change of basis matrix
	find coordinate vector of every old basis vector in new basis
## Direct Sums
sum of subspaces $\otimes$: span but with subspaces
	combine bases
	dimension of sum at most sum of dimension
## Infinite-Dimensional Spaces
ex. complex exponentials (see [Fourier Series](fourier-series.md#fourier-series-and-transforms))