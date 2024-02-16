# The Schrodinger Equation
## Time-Dependent Schrodinger Equation
1d schrodinger equation
	$i\hbar\frac{\partial\Psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\Psi}{\partial x^2} + V\Psi$
	$\hbar = \frac{h}{2\pi} = 1.054573 \cdot 10^{-34}$ Js
3d schrodinger equation
	$\nabla^2 = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}$, $(x, y, z, t) = (\vec{r}, t)$
	$-\frac{\hbar}{2m}\nabla^2\Psi(\vec{r},t)+V(\vec{r},t)\Psi(\vec{r},t)=i\hbar\frac{\partial}{\partial t}\Psi(\vec{r},t)$
## Time-Independent Schrodinger Equation
separation of variables
$\Psi(x, t) = \psi(x)\phi(t)$
1d: $-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V\psi = E\psi$
	$\phi(t) = e^{-\frac{iEt}{\hbar}}$ (wiggle factor)
	$\Psi = \psi \phi = \begin{Bmatrix}\sin{kx} \\ \cos{kx}\end{Bmatrix}e^{-\frac{iEt}{\hbar}}$
3d: $-\frac{\hbar}{2m}\nabla^2\psi(\vec{r})+V(\vec{r})\psi(\vec{r})=E\psi(\vec{r})$
	spherical schrodinger
		$\Phi(\phi) = e^{im_\ell\phi}$, cyclical
		$\Theta(\theta) = \sqrt{\frac{(2\ell + 1)}{4\pi}\frac{(\ell - m)!}{(\ell + m)!}}P_{\ell}^m(\cos\theta)$
		spherical harmonic $Y_{\ell}^m(\theta, \phi) = \Theta(\theta)\Phi(\phi)$
		for central potential ($V$ dependent only on $r$)
			$-\frac{\hbar^2}{2m}\frac{d^2 u}{dr^2} + (V + \frac{\hbar^2}{2m}\frac{\ell(\ell + 1)}{r^2})u = Eu$ (radial equation)
		angular momentum $L_z = m_\ell\hbar$, $|L| = \sqrt{\ell(\ell + 1)\hbar}$
		$C = -\ell(\ell + 1)$, $-\ell < m_\ell < \ell$
stationary states: probability density not time-dependent
	hamiltonian: definite total energy
		$\hat{H} = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x)$
		$\hat{H}\psi = E\psi$, $\langle H \rangle = E$
	general solution is linear combination of separable
		$\Psi(x, t) = \sum_{n=1}^\infty c_n\psi_n(x)\phi_n(t)$
		$|c_n|^2$ probability of energy measurement returning $E_n$
			$\sum_{n=1}^\infty |c_n|^2 = 1$, $\langle H \rangle = \sum_{n=1}^\infty |c_n|^2 E_n$
			probability of energy level, $H$ independent of time, energy conservation
## Formalism
state: wave function, treat as vectors
	vector space of square-integrable functions (hilbert space)
		normalization: $\int_{-\infty}^{\infty} |\Psi|^2 \, dx = 1$
			probability distribution function of particle location
				$P(a \leq x \leq b) = \int_a^b |\Psi|^2 \, dx$
		smooth: function, first derivative continuous
		goes to zero at $\pm\infty$
observables: operators, treat as linear transformations
QM naturally translates to lin alg