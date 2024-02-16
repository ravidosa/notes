# Vector
definition: quantity with both magnitude and direction
notation: $\vec{A}$, $|\vec{A}| = A$ is magnitude of $\vec{A}$
representation: arrow
components
	$A_x = A\cos{\theta}$
	$A_y = A\sin{\theta}$
addition/subtraction: add individual components
	$\vec{C} = \vec{A} + \vec{B}$
	$C_x = A_x + B_x$
	$C_y = A_y + B_y$
	$C_z = A_z + B_z$
unit vectors: vector with magnitude 1 in same direction
	notation: $\hat{A}$
	representation: arrow with length 1
	$\vec{A} = A\hat{A} = A_x\hat{i} + A_y\hat{j} + A_z\hat{k}$
	column matrices
		$\hat{i} = \begin{pmatrix}1\\0\\0\end{pmatrix}$, $\hat{j} = \begin{pmatrix}0\\1\\0\end{pmatrix}$, $\hat{k} = \begin{pmatrix}0\\0\\1\end{pmatrix}$
		$\hat{A} = \begin{pmatrix}\cos{\theta}\\\sin{\theta}\\0\end{pmatrix}$
linear independence of nonzero vectors
	$c_1\vec{v}_1 + c_2\vec{v}_2 + \ldots + c_n\vec{v}_n = 0$ implies all $c$ are 0
## Operations
addition
	component by component
multiplication
	scalar/dot product
		$\vec{A} \cdot \vec{B} = AB\cos{\theta}$ where $\theta$ is the angle between $\vec{A}$ and $\vec{B}$
		measure of how much vectors are parallel to each other
		$0$ if perpendicular, $AB$ if parallel
		$\vec{A} \cdot \vec{A} = A^2\cos{0^{\circ}} = A^2$
		$\vec{i} \cdot \vec{i} = \vec{j} \cdot \vec{j} = \vec{k} \cdot \vec{k} = 1$
		$\vec{i} \cdot \vec{j} = \vec{j} \cdot \vec{k} = \vec{k} \cdot \vec{i} = 0$
		$\vec{A} \cdot \vec{B} = A_xB_x + A_yB_y + A_zB_z$
		commutative: $\vec{A} \cdot \vec{B} = \vec{B} \cdot \vec{A}$
		result is scalar
	vector/cross product
		$|\vec{A} \times \vec{B}| = AB\sin{\theta}$ where $\theta$ is the angle between $\vec{A}$ and $\vec{B}$
		measure of how much vectors are perpendicular to each other
		$AB$ if perpendicular, $0$ if parallel
		not commutative: $\vec{A} \times \vec{B} \neq \vec{A} \times \vec{B}$
		result is vector
		right hand rule
			index finger is $\vec{A}$, middle finger is $\vec{B}$, thumb is $\vec{A} \times \vec{B}$
		$\vec{A} \times \vec{B} = -\vec{B} \times \vec{A}$
		$\hat{i} \times \hat{j} = \hat{k}$, $\hat{j} \times \hat{k} = \hat{i}$, $\hat{k} \times \hat{i} = \hat{j}$ (right-handed coordinate system)
		$\vec{A} \times \vec{A} = \vec{0}$
		$\vec{A} \times \vec{B} = \begin{pmatrix}A_x\\A_y\\A_z\end{pmatrix} \times \begin{pmatrix}B_x\\B_y\\B_z\end{pmatrix} = \begin{pmatrix}A_yB_z-A_zB_y\\A_zB_x-A_xB_z\\A_xB_y-A_yB_x\end{pmatrix}$
## Covariance and Contravariance
contravariant vector $x^\mu$: original vector
covariant vector $x_\mu$: dual vector