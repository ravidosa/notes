# Bound States
time dependent schrodinger equation
	$-\frac{\hbar^2}{2m}\frac{\delta^2\Psi(x,t)}{\delta x^2} + U(x)\Psi(x,t) = i\hbar\frac{\delta \Psi(x,t)}{\delta t}$
	$\Psi(x,t) = \psi(x)\phi(t)$
		$\phi(t) = e^{-i\frac{C}{\hbar}t}$
		$C = \hbar\omega = E$
		$\Psi(x,t) = \psi(x)e^{-i\frac{E}{\hbar}t}$
		stationary state (location fixed)
		oscillate between classical turning points
	infinite well
		$E = \frac{n^2\pi^2\hbar^2}{2mL^2}$
		$\psi_n(x) = \sqrt{\frac{2}{L}}\sin\frac{n\pi x}{L}$ for $0<x<L$, $=0$ for $x<0,x>L$
	finite potential well
		$\psi(x) = e^{\pm \alpha x}$ where $\alpha = \sqrt{\frac{2m(U_0-E)}{\hbar^2}}$ (outside of well)
			negative kinetic energy
		$\psi(x) = A\sin{kx} + B\cos{kx}$ (inside of well)
		depth of penetration $\delta = \frac{1}{\alpha}$, quantum mechanical tunneling
		quantum harmonic oscillator
			$\psi(x)=Ae^{-ax^2}$
			$E_n = (n + \frac{1}{2})\hbar\omega_0$ for integer $n$, $\omega_0 = \sqrt{\frac{\kappa}{m}}$
	non stationary states
		$\Psi(x,t) = \psi_n(x)e^{i\frac{E_n}{\hbar}t} + \psi_me^{i\frac{E_m}{\hbar}t}$
	expectation value
		$\bar{x^2} = \int_{-\infty}^\infty x^2|\psi(x)|^2dx$
		$(\Delta x)^2 = \bar{x^2} - \bar{x}^2$
		$E[Q] = \bar{Q} = \int_{-\infty}^\infty \Psi^*(x,t)\hat{Q}\Psi(x,t)dx$
		$\hat{p} = -i\hbar\frac{\partial}{\partial x}, \hat{x} = x, \hat{E} = i\hbar\frac{\partial}{\partial t}$