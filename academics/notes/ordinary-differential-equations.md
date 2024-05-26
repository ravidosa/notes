# Ordinary Differential Equations
classification
1. order ($y, y', y'' \ldots$)
2. scalar vs system
3. linearity
4. autonomy
5. homogeneity
rules for how quantities change with respect to each other, initial condition
state space
	show changes in quantity
logistic equation (population dynamics)
	$\frac{dN}{dt}=r(1-\frac{N}{k})N$
	$N(0) = N_0$
	parameters
		carrying capacity $k$
		max per capita growth rate $r$
fitzhugh-nagumo equation (neuronal dynamics)
	$\frac{dv}{dt} = -v(v-\alpha)(v-1)-w+\gamma$
	$\frac{dw}{dt} = \varepsilon(v-\beta w)$
	$v(0) = v_0,~w(0) = 0$
	parameters $\alpha,~\beta,~\gamma,~\varepsilon$
lorenz equation (atmospheric dynamics)
	$\frac{dx}{dt} = s(y-x)$
	$\frac{dy}{dt} = rx - y - xz$
	$\frac{dz}{dt} = xy - bz$
	parameters
		vertical temperature difference $r$
scalar autonomous ODE
	solution is scalar function, no explicit time dependence
series solution
	assume series solution for $y(x)$
	differentiate term by term
	substitute into diff eq
	equate coefficients of powers of x
## Dirac Delta Function
kronecker delta
	$\delta_{ij} = 1$ if $i = j$, $0$ if $i \neq j$
	$\sum_i \delta_{ij} = 1$
	$\sum_i f_i(\delta_{ij}) = f_j$
dirac delta function
	generalization of kronecker delta to continuous variable $\delta(x)$
	$\delta(x) \geq 0$
	$\int \delta(x-a) dx = 1$
	$\int f(x)\delta(x-a)=f(a)$
delta function
	$\lim_{\sigma \to 0} \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-a)^2}{2\sigma^2}} = \delta(x-a)$
	$\int_{-\infty}^\infty f(x)\delta(cx) dx = \frac{f(0)}{|c|}$
	$\int_{-\infty}^\infty f(x)\delta(cx+d)dx=\frac{f(-\frac{d}{c})}{|c|}$
	$\int_{-\infty}^\infty f(x)\delta((x-a)(x-b))dx = \frac{f(x-a)+f(x-b)}{|a-b|}$
	for function $g(x)$ with roots $x_i$, $\delta(g(x)) = \sum_i \frac{\delta(x-x_i)}{|g'(x_i)|}$, $\int_{\infty}^{\infty} f(x)\delta(g(x)) = \sum_i \frac{f(x_i)}{|g'(x_i)|}$
	$\int_{-\infty}^\infty f(x)\delta(x^2)dx = \lim_{x\to 0} \frac{f(x)}{|2x|}$
	$g(k) = \frac{1}{2\pi}\int_{-L}^Le^{ikx}dx = \frac{1}{\pi k}\sin{kL} = \delta(k)$ (goes to $\frac{L}{\pi}$ as $k \to 0$)
	$\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}f(x,y,z)\delta(x-x_0)\delta(y-y_0)\delta(z-z_0)dxdydz = f(x_0,y_0,z_0)$
heaviside theta function
	$\Theta(x'-a) = \int_{-\infty}^{x'}\delta(x-a)=0$ if $x'<a$, $1$ if $x'>a$
$\int\phi(x)\delta(x-a)dx = \phi(a)$
$\int_{-\infty}^\infty\phi(x)\delta'(x-a)dx = \phi(x) - \int_{-\infty}^{\infty}\phi'(x)\delta(x-a)dx = -\phi'(a)$
$\phi''(x-a)$→$\phi''(a)$
## IVP Theory
taylor's theorem
	approximation of nth order differentiable function with n degree polynomial (nth order taylor polynomial)
	see [Taylor Series](power-series.md#expanding-functions-in-power-series)
finite differences
	approximate derivative of function at point using points on function close to point
	$u'(x_0) \approx \frac{u(x_0 + h) - u(x_0 - h)}{2h} + O(h^2)$
	system of linear equations to solve for coefficients
		$\sum_i a_i = 0$, $\sum_i a_ii = 1$, $\sum_i a_i\frac{i^2}{2}= 0$
IVP
	solve differential equation given initial conditions
		$y(t), y'(t), \ldots$ 
		$y(\alpha) = \beta$
	lipschitz condition on subset $D$ of $\mathbb{R}^2$
		$|f(t,y_1)-f(t,y_2)|\leq L|y_1-y_2|$ for all $(t,y_1)$, $(t,y_2)$ in $D$, lipschitz constant $L$
		concavity
			$|\frac{\partial}{\partial y}f(t, y)| \leq L$
			convex if points on connecting line also in set
		if lipschitz satisfied, then unique solution
			if continuous, then well-posed
			perturbed problem $\frac{dz}{dt} = f(t, z) + \delta(t)$ has unique solution where $|z(t) - y(t)| < k\epsilon$
picard iteration
	functionals
		$T[y](t) = \alpha + \int_a^t f(s, y(s)) \, ds$
	fixed point for functionals
well-posed problems
	small changes in problem, small changes in solution
	unique solution exists
approximation
	equally spaced time steps with step size