multivariable PDE
	temperature, sound waves, gravitational potential, electrostatic potential
laplace’s equation
	$\nabla^2U(x,y,z)=0$
	$T=XY=\begin{Bmatrix}e^{ky} \\ e^{-ky}\end{Bmatrix}\begin{Bmatrix}\sin{kx} \\ \cos{kx}\end{Bmatrix}$
	solve for boundary conditions
	$\phi(r,\cos\theta)=\sum_{\ell=0}^\infty (A_\ell r^\ell + \frac{B_\ell}{r^{\ell + 1}})P_\ell(\cos\theta)$
		if $r=0$, $B_\ell = 0$
		if $r\to \infty$, $A_\ell = 0$
		if both excluded, both must be considered
poisson’s equation (inhomogenous)
	$\nabla^2 U(x,y,z)=f(x,y,z)$
	electrostatic potential and charge density
diffusion equation
	$\nabla^2 U(x,y,z,t)=\frac{1}{\alpha^2}\frac{\partial U}{\partial t}(x,y,z,t)$
	$U=TF=e^{-k^2\alpha^2t}\begin{Bmatrix}\sin{kx} \\ \cos{kx}\end{Bmatrix}$
helmholtz equation
	$(\nabla^2 + k^2)U(x,y,z)=0$
	space (time independent) of diffusion/wave
wave equation
	$\nabla^2 U(x,y,z,t)=\frac{1}{v^2}\frac{\partial^2 U(x,y,z,t)}{\partial t^2}$
	$Y=XT=\begin{Bmatrix}\sin{kx} \\ \cos{kx}\end{Bmatrix}\begin{Bmatrix}\sin{kvt} \\ \cos{kvt}\end{Bmatrix}$
schrodingers equation
	see [Schrodinger Equation](Waves%20and%20Particles%20II.md#Schrodinger%20Equation)
	$\Psi = \psi T = \begin{Bmatrix}\sin{kx} \\ \cos{kx}\end{Bmatrix}e^{-\frac{iEt}{\hbar}}$
linear homogenous PDE
	linear comb of solutions is also solution
	$\nabla^2 U = \frac{\partial^2}{\partial x^2}U + \frac{\partial^2}{\partial y^2}U + \frac{\partial^2}{\partial z^2}U$