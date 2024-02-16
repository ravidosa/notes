# Angular Momentum
## Classical Mechanics
$\vec{L}=I\vec{\omega}$
rotational impulse-momentum theorem
	$\int_{t_A}^{t_B}\vec{\tau}_{net}dt=\Delta \vec{L}=\vec{J}$
	dependent on reference frame
conservation of angular momentum for $\vec{\tau}_{ext}=0$
single particle
	$\vec{L}=m\vec{r}\times \vec{v}=\vec{r}\times\vec{p}$
	$L=mr_{\perp}v=r_{\perp}p$
multiple particle
	$\vec{L}=\sum \vec{L}_i$
rigid non-rotating object
	$\vec{L}=M\vec{r}_{cm}\times\vec{v}_{cm}=\vec{r}_{cm}\times\vec{p}_{cm}$
	$L=Mr_{\perp,cm}v_{cm}=r_{\perp,cm}p_{cm}$
rigid object rotating around fixed axis
	$\vec{L}=I_{pivot}\vec{\omega}$
	$\vec{L}=\vec{r}\times\vec{p}_{cm}+I_{pivot}\vec{\omega}$ (ref point not at pivot, same for fixed center of mass)
rigid object rotating around moving axis
		$\vec{L}=I_{pivot}\vec{\omega}+\vec{r}_{cm}\times\vec{p}_{cm}$
effects of torque
	$\Delta \vec{L}=\int_{t_A}^{t_B}\vec{\tau}_{net} dt$
	$\vec{\tau}_{net}=\frac{d\vec{L}}{dt}=\frac{d}{dt}(I\vec{\omega})=\frac{dL}{dt}\hat{L} + \frac{d\hat{L}}{dt}L$ (change in angular speed, change in direction)
	gyroscopic precession
		$\omega_p = \frac{\tau}{L}$
		faster spin, faster precess
		torque constant, angular momentum changes at constant rate
## Quantum Mechanics
angular momentum quantized
	behave like small magnets ($\bar{\mu}_L = -\frac{e}{2m_e}\bar{L}$)
stern-gerlach experiment
	magnetic dipole moment for hydrogen in ground state
angular momentum [operators](operator-physics.md)
	$[\hat{L}_i, \hat{L}_j] - i\hbar\epsilon_{ijk}\hat{L}_k$
	$L^2$ compatible with everything
	ladder operators $\hat{L}_{\pm} = \hat{L}_x \pm i\hat{L}_y$
	eigens
		$\hat{L}^2Y_\ell^m = \hbar^2\ell(\ell + 1)Y_\ell^m, \hat{L}_zY_\ell^m = \hbar mY_\ell^m$
			$\hat{L}^2$ is the spherical part of hamiltonian
		 integer $\ell$, $m \in \{-\ell, -\ell + 1, \ldots, \ell - 1, \ell\}$