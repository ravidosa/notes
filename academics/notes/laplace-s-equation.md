# Laplace's Equation
$\nabla^2U(x,y,z)=0$
$T=XY=\begin{Bmatrix}e^{ky} \\ e^{-ky}\end{Bmatrix}\begin{Bmatrix}\sin{kx} \\ \cos{kx}\end{Bmatrix}$
solve for boundary conditions
$\phi(r,\cos\theta)=\sum_{\ell=0}^\infty (A_\ell r^\ell + \frac{B_\ell}{r^{\ell + 1}})P_\ell(\cos\theta)$
	if $r=0$, $B_\ell = 0$
	if $r\to \infty$, $A_\ell = 0$
	if both excluded, both must be considered
generalize to poisson's equation (inhomogenous)
	$\nabla^2 U(x,y,z)=f(x,y,z)$
		electrostatic potential and charge density