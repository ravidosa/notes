# Linear Algebra
## Matrices
matrix: $m \times n$ matrix is collection of $mn$ numbers arranged in $m$ rows, $n$ columns
	column vector: $m \times 1$ matrix
	row vector: $1 \times n$ matrix
	square matrix: $m=n$
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
## Vectors
$\vec{v}_1 + \vec{v}_2 = \vec{v}_3$
	$c\vec{v}$
	$\vec{v}_1 \cdot \vec{v}_2 = |\vec{v}_1||\vec{v}_2|\cos\theta$
		$|\vec{v}_1| = \sqrt{\vec{v}_1 \cdot \vec{v}_1} = \vec{v}_1 \cdot \hat{v}_1$
	$\vec{v} = v_x\hat{x} + v_y\hat{y} + v_z\hat{z}$
	linear operator $M$
		$\hat{M}\vec{v} = \vec{v}_1$
		$Mc\vec{v} = c\vec{v}_1$
		$M(\vec{v}+\vec{w}) = \vec{v}_1 + \vec{w}_1$
	odd ($\psi_1 \to -\psi_1$), even ($\psi_2 \to \psi_2$)
		$M = \begin{pmatrix}a & b & c \\ b & a & c \\ c & c & d\end{pmatrix}$
		$\psi_1 = \begin{pmatrix}\alpha \\ -\alpha \\ 0\end{pmatrix}$, $\psi_2 = \begin{pmatrix}\alpha \\ \alpha \\ \beta\end{pmatrix}$
## Matrix Operations
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
## Lines and Planes
system of linear equations
	$a_1x+b_1y=c_1 , a_2x+b_2y=c_2$
	$x = \frac{b_2c_1-b_1c_2}{b_2a_1-b_1a_2}, y = \frac{a_2c_1-a_1c_2}{a_2b_1-a_1a_2}$
	geometric solution: straight line
		unique solution: intersecting lines
		no solution: parallel lines ($-\frac{a_1}{b_1} =-\frac{a_2}{b_2}, c_1 \neq c_2$)
		infinite solutions: overlapping lines ($-\frac{a_1}{b_1} =-\frac{a_2}{b_2} , c_1=c_2$)
	matrix solution
		$M = \begin{bmatrix}a_1 & b_1 \\ a_2 & b_2\end{bmatrix}$, $V = \begin{bmatrix}x \\ y \end{bmatrix}$, $R = \begin{bmatrix}c_1 \\ c_2\end{bmatrix}$
		$MV = R$
		$V = M^{-1}R$
		$\tilde{M} = \begin{bmatrix}c_1 & b_1 \\ c_2 & b_2\end{bmatrix}$
		$x = \frac{\operatorname{det}\tilde{M}}{\operatorname{det}M}$ (cramer’s rule)
## Linear Combinations, Linear Functions, and Linear Operators
rotation operator
	must be orthogonality matrix
		$\begin{bmatrix}\cos\theta & \sin\theta \\ -\sin\theta & \cos\theta\end{bmatrix}$
change of basis
	$\vec{V} = v_1\vec{\psi}_1 + v_2\vec{\psi}_2 = \begin{bmatrix}v_1 \\ v_2\end{bmatrix}$
	$M\vec{V} = \begin{bmatrix}\lambda_1 v_1 \\ \lambda_2 v_2\end{bmatrix}$
	bases must be linearly independent (preferred orthonormal $\hat{v}_i \cdot \hat{v}_j = \delta_{ij}$)
$O|f_1\rangle = |f_2\rangle$
	eg. derivative
non linear operator
	$\hat{O}f(x) \to (f(x))^2$
complex conjugate = anti linear operator
## Linear Dependence and Independence
linear independence of nonzero vectors
	$c_1\vec{v}_1 + c_2\vec{v}_2 + \ldots + c_n\vec{v}_n = 0$ implies all c are 0
functions on vectors
function linear independence
	$c_1f_1(x) + c_2f_2(x) + \ldots + c_nf_n(x) = 0$ implies all c are 0
	wronskian for smooth functions with enough derivatives
		$c_1f_1^{(n-1)}(x) + c_2f_2^{(n-1)}(x) + \ldots + c_nf_n^{(n-1)}(x) = 0$
		system of n linear equations for c
		nonzero determinant
		$W(x) = \begin{vmatrix}f_1(x) & f_2(x) & \cdots & f_n(x) \\ f_1'(x) & f_2'(x) & \cdots & f_n'(x) \\ \vdots \\ f_1^{(n-1)}(x) & f_2^{(n-1)}(x) & \cdots & f_n^{(n-1)}(x)\end{vmatrix} \neq 0$ then linearly independent
## Special Matrices
special matrices
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
				$A^*A = AA^**$
## Linear Vector Spaces
inner product
	$\langle f_1 | f_2 \rangle = \int_a^b f_1(x)f_2(x)dx$ for real functions
	$\langle f_1 | f_2 \rangle = \int_a^b f_1^*(x)f_2(x)dx = \langle f_2 | f_1 \rangle^*$ for complex functions
	$\int_a^b p_1(x)f_1^*(x)f_2(x)dx$ with positive weighting
	inner product with self greater than 0, 0 only if function is 0
	length of vector, norm of function
	functions orthogonal when $\langle f_1 | f_2 \rangle = 0$
	function normalized when $\langle f_1 | f_1 \rangle = 1$
gramm-schmidt
	linearly independent vectors $\psi$ to orthonormal vectors $e$ by linear combination
	$\hat{e}_1 = \frac{\vec{\psi}_1}{|\vec{\psi}_1|}$, $\vec{\psi}_{2,\perp} = \vec{\psi}_2 -(\vec{\psi}_2 \cdot \hat{e}_1)\hat{e}_1$, $\hat{e}_2 = \frac{\vec{\psi}_{2,\perp}}{|\vec{\psi}_{2,\perp}|}$, $\vec{\psi}_{3,\perp} = \vec{\psi}_3 - (\vec{\psi}_3\cdot\hat{e}_1)\hat{e}_1 - (\vec{\psi}_3\cdot\hat{e}_2)\hat{e}_2$, $\hat{e}_3 = \frac{\vec{\psi}_{3,\perp}}{|\vec{\psi}_{3,\perp}|}$…
	subtract parts along other vectors, normalize
## Eigenvalues, Eigenvectors, and Diagonalization
diagonalizing matrix (by similarity transformation)
	eigenvector $\vec{V}$, eigenvalue $\lambda$
		$M\vec{\psi} = \vec{\psi}' = \lambda\vec{\psi}$
		if $\vec{\psi }$ is eigenvector, so is $c\vec{\psi}$
		characteristic equation
			non-trivial solutions
			$|M-\lambda I| = 0$
			as many eigenvalues as rows/columns
			normalized eigenvector → terms squared sum to 1
			eigenvectors real and orthogonal (scalar product is 0) → symmetric matrix (real symmetric vs hermitian)
		matrix multiplied by matrix of eigenvectors is matrix of eigenvectors multiplied by diagonal matrix of eigenvalues ($C^{-1}MC = D)$
	$M = CDC^{-1}$
## Groups
closure
	n linearly independent functions
	$c_1f_1^{(n-1)}(x) + c_2f_2^{(n-1)}(x) + \ldots + c_nf_n^{(n-1)}(x) = f(x)$
	addition, scalar product, null, inverse

	