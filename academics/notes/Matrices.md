# Matrices
matrix
	$m \times n$ rectangular array, entries identified by indices (row, column)
	row vector: $1 \times n$ matrix (similar for column vector)
	solve matrix equations through row reduction
	transpose: switch rows and columns
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