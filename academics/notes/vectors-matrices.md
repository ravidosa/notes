# Vectors and Matrices
## Matrix-Vector Multiplication
$m \times n$ matrix $A$, $n \times 1$ column vector $x$
$y = Ax, y_i = \sum_{j=1}^n a_{ij}x_j$
## Matrix-Matrix Multiplication
$m \times k$ matrix $A$, $k \times n$ matrix $B$
$C = AB, C_{ij} = \sum_{s=1}^k a_{is}b_{sj}$
## Inner Product and Vector Norms
1-norm $||x||_1 = \sum_{i=1}^n |x_i|$
2-norm $||x||_2 = \sqrt{\sum_{i=1}^n |x_i|^2}$
max-norm $||x||_\infty = \max_{1\leq i\leq n} |x_i|$
generalized $p$-norm $||x||_p = \sqrt[p]{\sum_{i=1}^n |x_i|^p}$
inner product $(x, y) = x^Ty$
	positive definite, scalar multiples, triangle inequality
	inner product with self is square of 2-norm
projection $\mathrm{proj}_y x = \frac{x^Ty}{||y||_2}y$
absolute and relative error
norm bounding
## Matrix Norms
$|| A || = \mathrm{sup}_{x\neq 0} \frac{||Ax||}{||x||}$
norms of matrix behave like vector inner product
1-norm $||A||_1 = \mathrm{max}_{1\leq j \leq n} \sum_{i=1}^m |a_{ij}|$ (biggest row)
2-norm $||A||_2 = \sqrt{\mathrm{max}_{1\leq i \leq n} \lambda_i(A^TA)}$
infinity-norm $||A||_{\infty} =\mathrm{max}_{1\leq i \leq m} \sum_{j=1}^n |a_{ij}|$ (biggest column)
frobenius norm $||A||_F = \sqrt{\sum_{i=1}^m \sum_{j=1}^n a_{ij}^2}$
## Linear Independence: Bases
see [Bases](vector-spaces.md#bases-and-dimension)
keep linearly independent subset for compression
orthonormalize for numerical stability
## The Rank of a Matrix
rank: number of linearly independent column vectors
outer product $xy^T$ has rank $1$
nonsingular: $n \times n$ matrix with rank $n$, has inverse
	multiplying linearly independent vectors by nonsingular matrix, still linearly independent
four fundamental subspaces, $m \times n$ matrix $A$ with (column/row) rank $r$
	column space $C(A)$, dimension $r$
	row space $C(A^T)$, dimension $r$
	null space $N(A)$, dimension $n - r$
	left null space $N(A^T)$, dimension $m - r$
	