# Hydrogen Atom
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
## Hydrogenlike Atoms
neutral atom with atomic number $Z$, electric charge $Z_e$
	$\hat{H} = \sum_{j=1}^Z (-\frac{\hbar^2}{2m}\nabla^2_j - (\frac{1}{4\pi\epsilon_0})\frac{Ze^2}{r_j}) + \frac{1}{2}(\frac{1}{4\pi\epsilon_0})\sum_{j\neq k}^Z \frac{e^2}{|\vec{r}_j - \vec{r}_k|}$
	kinetic and potential energy of each electron, mutual repulsion with other electrons
only solved for hydrogen ($Z = 1$), approximated otherwise by ignoring repulsion term
	$E_n=-Z^2(13.6 eV)\frac{1}{n^2}$
	helium
		parahelium (antisymmetric) vs orthohelium (symmetric)