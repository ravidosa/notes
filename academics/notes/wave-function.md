# The Wave Function
## The Schrodinger Equation
wave function $\Psi(x, t)$
	solution to schrodinger equation $i\hbar\frac{\partial\Psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\Psi}{\partial x^2} + V\Psi$
	$\hbar = \frac{h}{2\pi} = 1.054573 \cdot 10^{-34}$
## The Statistical Interpretation
probability distribution function of particle location
	$P(a \leq x \leq b) = \int_a^b |\Psi|^2 \, dx$
indeterminate position
	realist vs orthodox position
	wavefunction collapses when measurement made
## Probability
see [Probability](../s23/mat135a.md)
## Normalization
$\int_{-\infty}^{\infty} |\Psi|^2 \, dx = 1$
	particles must be square integrable
## Momentum
$\langle x \rangle = \int_{-\infty}^{\infty} x|\Psi|^2 \, dx$
	average of measurements performed on particles in same state
	$\langle p \rangle = \int \Psi^* (-i\hbar(\frac{\partial}{\partial x}))\Psi \, dx$
		position operator $x$, momentum operator $-i\hbar(\frac{\partial}{\partial x})$
	$\langle Q(x, p) \rangle = \int \Psi^*(Q(x,-i\hbar(\frac{\partial}{\partial x}) )\Psi \, dx$
## Uncertainty Principle
de broglie formula
	$p = \frac{h}{\lambda}$
heisenberg uncertainty principle
	$\sigma_x\sigma_p \geq \frac{\hbar}{2}$