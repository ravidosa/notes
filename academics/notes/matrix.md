# Matrix
matrix
	$m \times n$ rectangular array, entries identified by indices (row, column)
		square matrix: $m=n$
	row vector: $1 \times n$ matrix (similar for column vector)
	solve matrix equations through row reduction
	transpose: switch rows and columns
## Determinants
for $2 \times 2 \begin{bmatrix}a & b \\ c & d\end{bmatrix}$: $ad - bc$
cofactor matrix $M$
	$m_{ij} = (-1)^{i+j}$(determinant of $(m-1)\times(n-1)$ matrix obtained by deleting $i$th row and $j$th column of A)
$\operatorname{det}A = \sum_{j=1}^n a_{ij}m_{ij}$ for any $i$ (can be done for any column)
totally antisymmetric tensor
	$\epsilon_{i_1i_2\ldots i_n} = 0$$\epsilon_{i_1i_2\ldots i_N} = 0$ if any two $i_n$ same, $=1$ for $i_1=1, i_2=2, \ldots i_N=n$, $=\pm 1$ based on number of permutations needed
	$\operatorname{det}A = \sum_{i_1=1}^n \sum_{i_N=1}^N \epsilon_{i_1i_2\ldots i_N}a_{1,i_1}a_{2,i_2}\ldots a_{n,i_N}$
properties
	0 if row or column has only zeroes
	changes sign if rows/columns interchanged
	0 if two rows/columns identical
	unchanged by adding multiples of rows to other rows
	$\operatorname{det}kA = k^n\operatorname{det}A$
	determinant of transpose $A^T$ (interchange rows and columns) is same
$\operatorname{det}(AB) = \operatorname{det}(A)\operatorname{det}(B)$
## Operations
transpose: $M^T_{ij} = M_{ji}$
	$(AB)^T = B^TA^T$
	$(e^A)^T = e^{(A^T)}$
complex conjugate $A^*$ is complex conjugate of every element
addition
	$A+B=C$
	$A$ is $m \times n$, $B$ is $m \times n$, $C$ is $m \times n$
	$A_{ij} + B_{ij} = C_{ij}$
scalar multiplication
	$kA = B$
	$A$ is $m \times n$, $B$ is $m \times n$
	$kA_{ij} = B_{ij}$
matrix multiplication
	$A \cdot B = C$
	$A$ is $m \times n$, $B$ is $n \times p$, $C$ is $m \times p$
	$C_{ij} = \sum_{k=1}^n a_{ik}b_{kj}$
inverse matrix
	only for square matrix w nonzero determinant
	$A^{-1}A = AA^{-1} = I$
	$A^{-1} = \frac{1}{\operatorname{det}A} M^T$

matrix group: group with matrix elements
	matrix multiplication as composition operation
	identity matrix
	inverses
		nonzero determinant
			$\mathrm{det}(A)\mathrm{det}(B) = \mathrm{det}(AB)$
		right inverse = left inverse
		$(AB)^{-1} = B^{-1}A^{-1}$
	represent more general groups (representation theory)
	does not commute (non-abelian)
	rotation matrices as transformation group
permutations
	bijective map from set to itself
	cycle notation $(a~b~c)$: $a$ goes to $b$, $b$ goes to $c$,$c$ goes to $a$
		2-cycles = transpositions
		composition right to left
	permutation matrix
		single $1$ in each row + column, zeros otherwise
		determinant $\pm 1$
			sign: $1$ even = even # of transpositions, $-1$ odd = odd numbr of transpositions
		composition of permutations = product of matrices
## Special Matrices
orthogonal
	$O^T = O^{-1}$
unitary (complex matrix)
	$U^\dagger = U^{-1}$
real symmetric
	$A^T = A$
hermitian
	hermitian inner product
	diagonalized by unitary transformation
		$C = \begin{bmatrix}\psi_1 & \psi_2\end{bmatrix}$
		$C^{-1} = \begin{bmatrix}\psi_1^\dagger \\ \psi_2^\dagger\end{bmatrix} = C^\dagger$
	normal matrix
		hermitian conjugate $M^\dagger$
			transpose and complex conjugate
			$M^*_{ij} = M^*_{ji}$ (commutable)
			$(M^\dagger)^\dagger = M$
			$(AB)^\dagger = B^\dagger A^\dagger$
		$A^*A = (AA^*)^*$