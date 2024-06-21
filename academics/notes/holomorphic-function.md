# Holomorphic Function
holomorphic iff analytic
$\mathbb{C}$ limit/convergence
	$\lim_{n\to\infty} z_n = z_0$ iff $|z_n - z_0| \to 0$
	extend convergence of series to convergence of functions
continuation sequences
	if functions holomorphic, agree on nonempty open subset then agree on whole
	overlapping/equal pairs of open disks and functions $(f, U)$ to form continuation sequence
		germ: collection of pairs o/e to pair
	parametrization
	analytic relations (differentiation, integration)
sequence of analytic functions locally uniformly conveging if $\epsilon$ bound holds in some neighborhood, locally uniformly bounded if bounded in some neighborhood
	hurwitz theorem: if sequence locally uniformly converging to nonconstant function, $f_n(z_n) = f(z), \lim_{n\to\infty} z_n = z$
	dogwalking lemma: analytic functions that stay within bound of each other have same winding number
	if $f_n$ analytic and bounded by $1$ on $\Delta$, with pointwise convergence, converges locally uniformly to $f$
		similar for subset, with different bound $M$
		if converges on open subset, then on whole set
## FTC in $\mathbb{C}$
$\int_a^b f(t) \, dt = F(b) - F(a), F(x) = \int_a^x f(t) \, dt$ ($F'(x) = f(x)$)
different geometrical interpretation, but FTC holds
	complex FTC holds only for analytic function with continuous derivative
	FTC extension
		three from classical physics (see [Vector Analysis](vector-analysis.md))
		complex variables fourth: $\oint f'(z) \, dz = f(B) - f(A)$
complex line integral
	$\int f(z) \, dz = \int u \, dx - v \, dy + i\int v \, dx + u \, dy$
	if conservative vector fields, line integral reduces to value of potentials at endpoints
		conservative iff CR eqs fulfilled
		conservative iff zero curl in simply connected domain, no point singularities
## Cauchy-Riemann Equations
complex function defines vector field on $\mathbb{R}^2$
	$f(z) = u(x, y) + iv(x, y)$
$f'(z) = \lim_{\Delta z \to 0} \frac{f(z + \Delta z) - f(z)}{\Delta z}$
for limits to converge to same complex number, function must satisfy cauchy-riemann equations
	$u_x = v_y, v_x = -u_y$
	$f'(z) = u_x + iv_x$
power, product, quotient rules, properties of limits hold
complex analytic function is infinitely smooth ($C^\infty$)
if two functions have same derivative, differ by constant
positively oriented curve of $\frac{1}{z}$ going around $z = 0$ $n$ times has integral $2\pi n$
	winding number $n = \frac{1}{2\pi i} \oint \frac{1}{z} \, dz$
	simple closed curve, no crossings
	$\oint z^n \, dz = 0$ for integer $n > 1$
	related to number of zeros
[laurent expansion](laurent-series.md)
differentiable implies CR
	take $\Delta z = \Delta x$ and $\Delta z = i\Delta y$, set equal
CR implies differentiable
	$u$ and $v$ differentiable, have tangent planes in every direction
	$u(\vec{x}) - u(\vec{x}_0) = \nabla u_0 \cdot (\vec{x} - \vec{x}_0) + o(1)|\vec{x} - \vec{x}_0|$ (similar for $v$)
	$J(\vec{x}_0) = \begin{bmatrix} u_x & u_y \\ v_x & v_y \end{bmatrix}$
inverse function theorem
	inverse holomorphic when derivative nonzero, bijective, holomorphic, and smooth, $f^{-1'}(w) = \frac{1}{f'(z)}$
	if holomorphic, determinant of jacobian is nonzero
maximum modulus theorem: analytic function relative maximum on boundary
	if also in boundary, then constant on closure
	schwarz's lemma
		analytic, bounded by $1$ for $|z| < 1$, $f(0) = 0$
		either $|f(z)| < |z|, |f'(0)| < 1$ or $f(z) = cz$ where $|c| = 1$
		approximately linear functions: approximate one-to-one map of disk has bounded derivative
		bounded region has unit disk as universal covering
			[riemann mapping theorem](projective-space.md#c)
			continuous mapping of sequence without limit point has no limit point
			lindelof's theorem: holomorphic function on half-strip is bounded if bounded on boundary and derivative bounded
harmonic functions: $\nabla^2 u = \Delta u  = 0$
	if $u, v$ harmonic and $u + iv$ analytic, $u, v$ are harmonic conjugates
	equal to average on circle
	for harmonic $u$, harmonic conjugate $v$ exists
		if $C^2$, then $C^{\infty}$
		locally expandable as taylor series
## Elementary Functions
treat exponential as power series (due to uniform convergence)
	same for sine/cosine
	$e^{iy} = \cos y + i \sin y, e^z = e^x(\cos y + i \sin y)$
	same properties as real exponential
		$e^{z + w} = e^ze^w, |e^z| = e^x, e^z \neq 0, \overline{e^z} = e^{\overline{z}}$
		$(e^{iy})^n = e^{iny}$ (de moivre)
	$2\pi$ periodic in $y$
		$e^{i\pi} + 1 = 0$
exponential form
	$z = re^{i\theta}, |z| = r$ ($\theta$ restricted to $2\pi$ interval gives unique expression)
	geometric interpretation of multiplication
		$z_1 \cdot z_2 = r_1r_2e^{i(\theta_1 + \theta_2)}$
sine and cosine (without power series)
	$\sin z = \frac{e^{iz} - e^{-iz}}{2i}, \cos z = \frac{e^{iz} + e^{-iz}}{2}$ (CR satisfied)
entire function: complex derivative define for whole complex plane
complex logarithm
	restrict to domain where injective
	$\log(z) = \ln r + i\theta$
roots
	rational exponent
		$z^n = r^ne^{in\theta}$, $w= z^{\frac{1}{n}}$ when $w^n = z$
		$n$ nth roots
		equispaced about unit circle
		$z^{\frac{m}{n}}$ has $n$ solutions when $\frac{m}{n}$ reduced to lowest terms
	irrational exponent
		$z^a = e^{a\log z}$, $\log z = \ln r + i\theta$
		when irrational, infinite solutions
	complex exponent
		choose branch of $\log z$