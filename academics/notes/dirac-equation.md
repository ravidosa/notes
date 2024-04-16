# The Dirac Equation
[schrodinger's equation](schrodinger-equation.md) for relativistic QM, spin 1/2
	$i\hbar\gamma^\mu\partial_{\mu}\psi - mc\psi = 0$
	bispinor $\psi$
		helicity spinors
			helicity $h = \frac{\vec{S} \cdot \vec{p}}{p}$ ($\frac{1}{2}$ right handed $-\frac{1}{2} left handed)
	if independent of position (particle at rest), solutions are electron/positron with spin up/down
	if plane wave, solutions are particle ($u$) and antiparticle ($v$)
gamma matrices
	$\gamma^0 = \begin{pmatrix} 1 & 0 \\ 0 & -1\end{pmatrix}, \gamma^i = \begin{pmatrix}0 & \sigma_i \\ -\sigma_i & 0 \end{pmatrix}$
invariant $\bar{\psi}\psi$
	$\bar{\psi} = (\psi_1^*\psi_2^* - \psi_3^* - \psi_4^*)  = \psi^\dagger \gamma^0$
		probability density $\rho = \psi^\dagger\psi$
		current density $j^\mu = \bar{\psi}\gamma^\mu\psi$ (bilinear covariant)
	pseudoscalar $\bar{\psi}\gamma^5\psi$
		$\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$
feynman-stuckelberg interpretation
	negative energy particle propagating backwards in time = positive energy antiparticle propagating forwards in time
	$e^{-iEt} = e^{-i(-E)(-t)}$