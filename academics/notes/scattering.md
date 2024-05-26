# Scattering
luminosity $\mathcal{L} = \frac{N_1N_2f}{A}$
## Cross Sections
cross-sectional area $\sigma$
	sum individual cross sections
	dependent on velocity, impact parameter $b$ (distance from center relates to scattering angle $\theta$)
	$\sigma = \int |\frac{b}{\sin\theta}\frac{db}{d\theta}| \sin\theta \, d\theta \, d\phi$
differential cross section $\sigma(\theta) = \frac{d\sigma}{d\Omega} = |f(\vec{q}^2)|^2$
	$\sigma = \int \sigma(\theta) \ d\Omega$
	momentum transfer $\vec{q} = \vec{p} - \vec{p}'$, $q = 2p\sin\frac{\theta}{2}$
		$f(\vec{q}^2) = -\frac{m}{2\pi \hbar^2}\int V(\vec{x}) e^{\frac{i\vec{q} \cdot \vec{x}}{\hbar}} \, d^3x$
	usually in barns
## Elastic Scattering
used to determine structure of subatomic particles
	intensity of energy level peak translated to differential cross section
rutherford scattering
	spinless nucleus, alpha particle
	coulomb potential
	$f(\vec{q}^2) = -\frac{2mZ_1Ze^2}{q^2 + (\frac{\hbar}{a})^2}, \frac{d\sigma}{d\Omega}_R = \frac{4m^2(Z_1Ze^2)^2}{q^4}$
	born approximation, no target recoil, spinless, point particles
mott scattering
	for spin 1/2 alpha, $|Z_1| = 1$
		$\frac{d\sigma}{d\Omega}_M = 4(Ze^2)^2 \frac{E^2}{(qc)^4}(1 - \beta^2\sin^2\frac{\theta}{2})$
		rutherford in nonrelativistic limit
form factors
	non-point particles
	$\frac{d\sigma}{d\Omega} = \frac{d\sigma}{d\Omega}_M|F(\vec{q}^2)|^2$
	form factor $F(\vec{q}^2) = \int \rho(\vec{r})e^{\frac{i\vec{q} \cdot \vec{r}}{\hbar}} \, d^3r$
		normalized probability density $\rho(\vec{r})$
		mean square radius $\langle r^2 \rangle = \int r^2\rho(r) \, d^3r$
			for medium/heavy nuclei, $\sqrt{\langle r^2 \rangle} \approx r_0A^{\frac{1}{3}}$ (mass number $A$, $r_0 = 0.94$ fm)