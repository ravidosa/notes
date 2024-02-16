# Particle in a Box
see [Schrodinger Equation](schrodinger-equation.md)
$V(x) = \begin{cases} 0 & 0 \leq x \leq a \\ \infty & \text{otherwise}\end{cases}$
boundary conditions $\psi(0) = \psi(a) = 0$
	$E_n = \frac{n^2\pi^2\hbar^2}{2ma^2}$
	$\psi_n(x) = \begin{cases} \sqrt{\frac{2}{a}}\sin(\frac{n\pi}{a}x) & |x| \leq a \\ 0 & |x| > a\end{cases}$
		properties of $\psi_n(x)$
			alternately even/odd
			$\psi_n$ has $n-1$ nodes
			orthonormal: $\int \psi_m(x)^*\psi_n(x) \, dx = \delta_{mn}$
			complete: represent any function (fourier series, dirichlet's theorem)
				$c_n = \int \psi_n(x)^* f(x) \, dx$
3d infinite well
	$E_{n_x,n_y,n_z}=(\frac{n_x^2}{L_x^2} + \frac{n_y^2}{L_y^2} + \frac{n_z^2}{L_z^2})\frac{\pi^2\hbar^2}{2m}$
	cube ($L_x = L_y = L_z$)
		degenerate states: different states with same energy