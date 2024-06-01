# The Dirac Equation
[schrodinger's equation](schrodinger-equation.md) for relativistic QM, spin 1/2
	$i\hbar\gamma^\mu\partial_{\mu}\psi - mc\psi = 0$
	bispinor $\psi$
		helicity spinors
			helicity $h = \frac{\vec{S} \cdot \vec{p}}{p}$ ($\frac{1}{2}$ right handed $-\frac{1}{2} left handed)
	if independent of position (particle at rest), solutions are electron/positron with spin up/down
	if plane wave, solutions are particle ($u$) and antiparticle ($v$)
solutions
	$(\gamma^\mu p_\mu - m)u = 0$
	particle at rest
		$\psi_1 = N\begin{pmatrix} 1 \\ 0 \\ 0 \\ 0\end{pmatrix}e^{-imt}, \psi_2 = N\begin{pmatrix} 0 \\ 1 \\ 0 \\ 0\end{pmatrix}e^{-imt}, \psi_3 = N\begin{pmatrix} 0 \\ 0 \\ 1 \\ 0\end{pmatrix}e^{-imt}, \psi_4 = N\begin{pmatrix} 0 \\ 0 \\ 0 \\ 1\end{pmatrix}e^{-imt}$
	general free particle
		$u_1 = N_1\begin{pmatrix} 1 \\ 0 \\ \frac{p_z}{E + m} \\ \frac{p_x + ip_y}{E + m}\end{pmatrix}, u_2 = N_2\begin{pmatrix} 0 \\ 1 \\ \frac{p_x - ip_y}{E + m} \\ \frac{-p_z}{E + m}\end{pmatrix}$
		$v_1 = N_3\begin{pmatrix} \frac{p_z}{E - m} \\ \frac{p_x + ip_y}{E - m} \\ 1 \\ 0\end{pmatrix}, v_2 = N_4\begin{pmatrix} \frac{p_x -ip_y}{E - m} \\ \frac{-p_z}{E - m} \\ 1 \\ 0\end{pmatrix}$
		$u_1, u_2$ positive energy $v_1, v_2$ negative energy
gamma matrices
	$\gamma^0 = \begin{pmatrix} 1 & 0 \\ 0 & -1\end{pmatrix}, \gamma^i = \begin{pmatrix}0 & \sigma_i \\ -\sigma_i & 0 \end{pmatrix}$
invariant $\bar{\psi}\psi$
	$\bar{\psi} = (\psi_1^*\psi_2^* - \psi_3^* - \psi_4^*)  = \psi^\dagger \gamma^0$
		probability density $\rho = \psi^\dagger\psi$
		current density $j^\mu = \bar{\psi}\gamma^\mu\psi$ (bilinear covariant)
	pseudoscalar $\bar{\psi}\gamma^5\psi$
		$\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$
charge conjugation
	particle-antiparticle mapping
	$\psi' = \hat{C}\psi = i\gamma^2\psi^*$
intrinsic parity
	spatial inversion through origin
	$\psi' = \hat{P}\psi = \gamma^0\psi$
	convention of particles having positive parity, antiparticles negative parity
spin and helicity
	$u_1, v_1$ spin up, $u_2, v_2$ spin down
	helicity $h = \frac{\vec{S} \cdot \vec{p}}{p}$
	right handed up, left handed down ($c = \cos\frac{\theta}{2}, s = \sin\frac{\theta}{2}$)
		$u_{\uparrow} = \sqrt{E + m}\begin{pmatrix}c \\ se^{i\phi} \\ \frac{p}{E + m}c \\ \frac{p}{E + m}se^{i\phi}\end{pmatrix}, u_{\downarrow} = \sqrt{E + m}\begin{pmatrix}-s \\ ce^{i\phi} \\ \frac{p}{E + m}s \\ -\frac{p}{E + m}ce^{i\phi}\end{pmatrix}$
		$v_{\uparrow} = \sqrt{E + m}\begin{pmatrix}\frac{p}{E + m}s \\ -\frac{p}{E + m}ce^{i\phi} \\ -s \\ ce^{i\phi}\end{pmatrix}, u_{\downarrow} = \sqrt{E + m}\begin{pmatrix}\frac{p}{E + m}c \\ \frac{p}{E + m}se^{i\phi} \\ c \\ se^{i\phi}\end{pmatrix}$
interpretations
	dirac sea interpretation
		negative energy solutions as holes in vacuum
	feynman-stuckelberg interpretation
		negative energy particle propagating backwards in time = positive energy antiparticle propagating forwards in time
		$e^{-iEt} = e^{-i(-E)(-t)}$
		