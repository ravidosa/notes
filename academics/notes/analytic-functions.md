# Analytic Functions
$\mathbb{C}$ is $\mathbb{R}^2$ with multiplication defined, unordered field
	$\mathbb{R}$ is $\mathbb{C}$ with zero imaginary part
	all polynomials factorizable into product of linear terms
	$\mathbb{C} = \{z = x + iy : x, y \in \mathbb{R}\}, i^2 = -1$
	addition $z_1 + z_2 = (x_1 + x_2) + i(y_1 + y_2)$ ($-z = -x - iy$)
	multiplication $z_1 \cdot z_2 = (x_1x_2 - y_1y_2) + i(x_1y_2 + x_2y_1)$ ($z^{-1} = \frac{x}{x^2 + y^2} - i\frac{y}{x^2 + y^2}$)
	complex conjugate $\overline{z} = x - iy, |z|^2 = z\overline{z} = x^2 + y^2$
		$\overline{z_1 \cdot z_2} = \overline{z}_1 \cdot \overline{z}_2, \overline{z_1 + z_2} = \overline{z}_1 + \overline{z}_2$
		$\frac{1}{2}(z + \overline{z}) = x, \frac{1}{2}(z - \overline{z}) = iy$
		$|z| \geq 0$ unless $z = 0$
$\mathbb{R}^2$ limit/convergence
	$\vec{x}_n \to \vec{x}_0$ iff $\lim_{n\to\infty} ||\vec{x}_n - \vec{x}_0 || = 0$
	distance between points tends to 0
	for open ball of any size, after some $N$, all points in ball
	$\vec{x}_n \to \vec{x}_0$ iff $x_n \to x_0$ and $y_n \to y_0$
$\mathbb{C}$ limit/convergence
	$\lim_{n\to\infty} z_n = z_0$ iff $|z_n - z_0| \to 0$
	extend convergence of series to convergence of functions
FTC in $\mathbb{C}$
	$\int_a^b f(t) \, dt = F(b) - F(a), F(x) = \int_a^x f(t) \, dt$ ($F'(x) = f(x)$)
	different geometrical interpretation, but FTC holds
	complex function defines vector field on $\mathbb{R}^2$
		$f(z) = u(x, y) + iv(x, y)$
	$f'(z) = \lim_{\Delta z \to 0} \frac{f(z + \Delta z) - f(z)}{\Delta z}$
	for limits to converge to same complex number, function must satisfy cauchy-riemann equations
		$u_x = v_y, v_x = -u_y$
		$f'(z) = u_x + iv_x$
	power, product, quotient rules, properties of limits hold
	complex line integral
		$\int f(z) \, dz = \int u \, dx - v \, dy + i\int v \, dx + u \, dy$
		if conservative vector fields, line integral reduces to value of potentials at endpoints
			conservative iff CR eqs fulfilled
			conservative iff zero curl in simply connected domain, no point singularities
	complex analytic function is infinitely smooth ($C^\infty$)
	if two functions have same derivative, differ by constant
	positively oriented curve of $\frac{1}{z}$ going around $z = 0$ $n$ times has integral $2\pi n$
		winding number $n = \frac{1}{2\pi i} \oint \frac{1}{z} \, dz$
		simple closed curve, no crossings
		$\oint z^n \, dz = 0$ for integer $n > 1$
	laurent expansion
	$f(z) = \sum_{k=-\infty}^{\infty} a_kz_k$ for $0 < |z| < R$
	converges in annulus
	$a_{-1}$ is residue at singularity $z = 0$
		complex integral around isolated singularity is just calculating residue ($\oint f(z)\, dz = a_{-1}2\pi i$)
		residue theorem: analytic except at $j$ finite isolated singularities, $\oint f(z) \, dz = 2\pi i (\sum_{k=1}^j a_{-1}^j$)
differentiable implies CR
	take $\Delta z = \Delta x$ and $\Delta z = i\Delta y$, set equal
CR implies differentiable
	$u$ and $v$ differentiable, have tangent planes in every direction
	$u(\vec{x}) - u(\vec{x}_0) = \nabla u_0 \cdot (\vec{x} - \vec{x}_0) + o(1)|\vec{x} - \vec{x}_0|$ (similar for $v$)
	$J(\vec{x}_0) = \begin{bmatrix} u_x & u_y \\ v_x & v_y \end{bmatrix}$