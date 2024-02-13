# Quantum Mechanics in Three Dimensions
## The Schrodinger Equation
3d schrodinger equation
	$\nabla^2 = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}$, $(x, y, z, t) = (\vec{r}, t)$
	$-\frac{\hbar}{2m}\nabla^2\Psi(\vec{r},t)+V(\vec{r},t)\Psi(\vec{r},t)=i\hbar\frac{\partial}{\partial t}\Psi(\vec{r},t)$
	time independent: $-\frac{\hbar}{2m}\nabla^2\psi(\vec{r})+V(\vec{r})\psi(\vec{r})=E\psi(\vec{r})$
spherical schrodinger
	$\Phi(\phi) = e^{im_\ell\phi}$, cyclical
	$\Theta(\theta) = \sqrt{\frac{(2\ell + 1)}{4\pi}\frac{(\ell - m)!}{(\ell + m)!}}P_{\ell}^m(\cos\theta)$
	spherical harmonic $Y_{\ell}^m(\theta, \phi) = \Theta(\theta)\Phi(\phi)$
	for central potential ($V$ dependent only on $r$)
		$-\frac{\hbar^2}{2m}\frac{d^2 u}{dr^2} + (V + \frac{\hbar^2}{2m}\frac{\ell(\ell + 1)}{r^2})u = Eu$ (radial equation)
	angular momentum $L_z = m_\ell\hbar$, $|L| = \sqrt{\ell(\ell + 1)\hbar}$
	$C = -\ell(\ell + 1)$, $-\ell < m_\ell < \ell$
3d infinite well
	$E_{n_x,n_y,n_z}=(\frac{n_x^2}{L_x^2} + \frac{n_y^2}{L_y^2} + \frac{n_z^2}{L_z^2})\frac{\pi^2\hbar^2}{2m}$
	cube ($L_x = L_y = L_z$)
		degenerate states: different states with same energy
## The Hydrogen Atom
$E_n = -(\frac{m_e}{2\hbar^2}(\frac{e^2}{4\pi\epsilon_0})^2)\frac{1}{n^2} = \frac{E_1}{n^2}$ for integer $n$
	bohr radius $a = \frac{4\pi\epsilon_0\hbar^2}{m_ee^2}$
	ground state $E_1 = -13.6$ eV (binding energy)
		$\psi_{1~0~0} = \frac{1}{\sqrt{\pi a^3}}e^{-\frac{r}{a}}$
		$\psi_{n~\ell~m} = \sqrt{(\frac{2}{na})^3\frac{(n - \ell - 1)!}{2n(n + \ell)!}}e^{-\frac{r}{na}}(\frac{2r}{na})^{\ell}L^{2\ell + 1}_{n-\ell-1}(\frac{2r}{na})Y_{\ell}^m(\theta, \phi)$
			(associated) laguerre polynomial $L_q^p(x)$
hydrogen spectrum
	$\frac{1}{\lambda} = \mathcal{R}(\frac{1}{n_1^2} - \frac{1}{n_2^2})$ for $n_1 \neq n_2$ (rydberg constant $\mathcal{R}$)
	only balmer series ($n=2$) visible
		lyman ($n = 1$), paschen ($n = 3$)
	electron is charge orbiting proton
spectroscopic notation
	spdf
electron radial probability density
	$P(r) = \frac{4r^2}{a_0^3}e^{-\frac{2r}{a_0}}$
hydrogen like ions
	$E_n=-Z^2(13.6 eV)\frac{1}{n^2}$
## Angular Momentum
angular momentum operators
	$[\hat{L}_i, \hat{L}_j] - i\hbar\epsilon_{ijk}\hat{L}_k$
	$L^2$ compatible with everything
	ladder operators $\hat{L}_{\pm} = \hat{L}_x \pm i\hat{L}_y$
	eigens
		$\hat{L}^2f_\ell^m = \hbar^2\ell(\ell + 1)Y_\ell^m, \hat{L}_zf_\ell^m = \hbar mY_\ell^m$
			$\hat{L}^2$ is the spherical part of hamiltonian
		 integer $\ell$, $m \in \{-\ell, -\ell + 1, \ldots, \ell - 1, \ell\}$
## Spin
orbital momentum vs spin ($s$) momentum
algebra of spin identical to (orbital) angular momentum
	permits half-integer for $s$, $m$
every elementary particle has specific $s$ value
spin 1/2
	spin up and spin down eigenstates
	general state represented as spinor
		coefficients of up and down
	spin operators are $2 \times 2$ matrices (pauli spin matrices)
		$\hat{S}_z = \frac{\hbar}{2}\begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}$
		$\hat{S}_+ = \hbar\begin{pmatrix}0 & 1 \\ 0 & 0\end{pmatrix}$
		$\hat{S}_- = \hbar\begin{pmatrix}0 & 0 \\ 1 & 0\end{pmatrix}$
		$\hat{S}_x = \frac{\hbar}{2}\begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}$
		$\hat{S}_y = \frac{\hbar}{2}\begin{pmatrix}0 & -i \\ i & 0\end{pmatrix}$
		eigenspinors are spin up (eigenvalue $\frac{\hbar}{2}$), spin down ($-\frac{\hbar}{2}$)
electron in a magnetic field
	dipole moment $\mu = \gamma S$ (gyromagnetic ration $\gamma$)
		torque $-\mu \times B$, enery $-\gamma B \cdot S$
adding angular momenta
	clebsch-gordan coefficients
	applied group theory (representation theory, lie groups)