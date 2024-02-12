# Bilinear Forms
## Bilinear Forms
bilinear form $\langle v, w \rangle$ on vector space is real-valued function of two vectors
	standard form $v^Tw$
	$\langle v, w\rangle = v^TAw$ for basis matrix $A$
	linear in both variables
	addition, scalar multiplication "distributes"
	ex. dot product, $A = I$
symmetric form if matrix is symmetric (skew-symmetric is similar)
change of basis
	$A$ to $P^TAP$
	if $P$ orthogonal, preserves dot product
## Symmetric Forms
positive definite: $\langle v, v\rangle > 0$, semi-definite $\geq 0$ (nonzero $v$)
	similar for negative (semi-)definite
	if not positive definite, then indefinite
symmetric, positive definite $A$ equivalent to dot product for some basis
## Hermitian Forms
extend from real-valued to complex-valued
	conjugate linear in first variable, linear in second variable hermitian symmetric
	standard form $v^*w$
	$A$ is hermitian matrix
		$\langle v, v \rangle$, eigenvalues trace, determinant are real
	unitary matrix: adjoint is inverse
		columns orthonormal wrt to standard
		preserves standard hermitian form
## Orthogonality
orthogonal: $\langle v, w \rangle = 0$
	orthogonal space to subspace: vectors orthogonal to every vector in subspace
	orthogonal basis: mutually orthogonal, span vector space
	null space: orthogonal space of vector space
	nondegenerate form: nullspace is zero space
		symmetric form only degenerate if zero matrix, orthogonal basis exists
orthogonal projection: just like with vectors (orthonormalize basis first)
	for symmetric: exists basis with $P^TAP$ diagonal entries $0, \pm 1$
## Euclidean Spaces and Hermitian Spaces
euclidean space: vector space with positive definite symmetric form
	standard $\mathbb{R}^n$
hermitian space: same thing with hermitian, not definite
	standard $\mathbb{C}^n$
nondegenerate on all subspaces
length, angle between vector interpretation
## The Spectral Theorem
linear operator: linear map from vector space to itself
conjugation by unitary matrix preserves normal/hermitian/unitary matrix
linear operator on hermitian space
	$\langle Tv, w \rangle = \langle v, T^*w\rangle$
	normal ($TT^* = T^*T$): $\langle Tv, Tw\rangle = \langle T^*v, T^*w \rangle$
		same eigenvectors, conjugate eigenvalues
	hermitian ($T^* = T$): $\langle Tv, w \rangle = \langle v, Tw\rangle$
	unitary ($TT^* = I$): $\langle Tv, Tw\rangle = \langle v, w \rangle$
$T$-invariant is $TW \subseteq W$
	$W^{\perp}$ is $T^*$-invariant
spectral theorem (normal operators)
	orthonormal eigenvector basis
	matrix diagonalizable for unitary $P$
spectral theorem (hermitian operators)
	same as normal, but eigenvalues are real
spectral theorem (symmetric operators)
	same as hermitian, matrix is real