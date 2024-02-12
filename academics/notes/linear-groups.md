# Linear Groups
## The Classical Groups
special linear group $SL_n$: real matrices with determinant $1$
orthogonal group $O_n$: real matrices where $PP^T = I$
	special orthogonal group $SO_n$: orthogonal with determinant $1$
unitary group $U_n$: complex matrices where $PP^* = I$
	special unitary group $SU_n$: unitary with determinant $1$
homeomorphism: continuous bijective map with continuous inverse
dimension: degrees of freedom of matrix
## Interlude: Spheres
$n$-dimensional unit sphere $\mathbb{S}^n$: $\sum_{i=0}^n x_i^2 = 1$
stereographic projection $\pi(x) = (\frac{x_i}{1 - x_0})$
bijection between $\mathbb{S}^n$, $\mathbb{R}^n \cup \{\infty\}$
latitude: intersection with $x_0 = c$ hyperplane
	equator $\mathbb{E}$: $c = 0$, isomorphic to $\mathbb{S}^{n-1}$
## The Special Unitary Group $SU_2$
form $P = \begin{bmatrix} a & b \\ -\overline{b} & \overline{a}\end{bmatrix}$ ($\overline{a}a + \overline{b}b = 1$)
bijective correspondence with unit $3$-sphere ($a$ and $b$ as vectors)
basis vectors
	$I$ and quaternion group
		$\mathbf{i} = \begin{bmatrix} i & 0 \\ 0 & -i\end{bmatrix}$
		$\mathbf{j} = \begin{bmatrix} 0 & 1 \\ -1 & 0\end{bmatrix}$
		$\mathbf{k} = \begin{bmatrix} 0 & i \\ i & 0\end{bmatrix}$
	$SU_2$ is set of unit vectors in quaternion algebra 
eigenvalues are complex conjugates with absolute value $1$
	diagonalizable
latitude is matrices with $\mathrm{trace}(A) = 2c$, correspond to $SU_2$ conjugacy classes
if matrix on equator
	zero trace, eigenvalues $\pm i$, $A^2 = -I$ (skew-hermitian)
any element can be written uniquely as $x_0I + x_1\mathbf{i} + x_2\mathbf{j} + x_3\mathbf{k}$
	also as $\alpha_1I + \alpha_2A$ for $A \in \mathbb{E}$, $\alpha_1^2 + \alpha_2^2 = 1$
	longitudes
		diagonal matrices: $x_0 = \cos\theta, x_1 = \sin\theta, x_2 = x_3 = 0$
		real matrices: $x_0 = \cos\theta, x_2 = \sin\theta, x_1 = x_3 = 0$
## The Rotation Group $SO_3$
conjugation by $P \in SO_2$ is rotation of $\mathbb{E}$ (or $\mathbb{S}^2$ or $\mathbb{R}^3$)
	$\gamma_P(Q) = P^*QP$
	surjective homomorphism from $SU_2 \to SO_3$ (spin homomorphism)
		$\pm I$ is kernel, $SO_3$ isomorphic to $SU_2 / \{\pm I\}$ (projective $3$-space $\mathbb{P}^3$)
		$\langle U, V \rangle = -\frac{1}{2}\mathrm{trace}(UV)$
	same angle of rotation if same conjugacy class