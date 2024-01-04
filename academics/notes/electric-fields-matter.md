# Electric Fields in Matter
## Polarization
induced dipole
	$\vec{p}_{induced} = \alpha\vec{E}$ for polarizability $\alpha$ in $C^2\cdot m/N$ for neutral atom
	$\vec{p}$ not parallel to $\vec{E}$ for neutral molecule
	molecules, crystals can have permanent dipole moment
	torque about origin
		$\vec{N} = \vec{p} \times \vec{E}$
		$\vec{F} = (\vec{p} \cdot \vec{\nabla})\vec{E}$
			$U = -\vec{p}\cdot\vec{E}$
dielectric material
	lots of atoms/molecules, tend to align with electric field
	polarization $\vec{P}$
		$\vec{p} = \int_V \vec{P} \, d\tau'$
	ferroelectric materials can have spontaneous polarization
## The Field of a Polarized Object
polarized volume with zero total charge equivalent to volume with $\rho_b = -\vec{\nabla}\cdot\vec{P}$ and $\sigma_b = \vec{P}\hat{n}$
		$V(\vec{r}) = \frac{1}{4\pi\epsilon_0}\int_V \frac{\vec{p}(\vec{r'})\mathbf{\hat{r}}}{\mathbf{r}^2} \, d\tau' = \frac{1}{4\pi\epsilon_0}(\oint_S \frac{\sigma}{\mathbf{r}} \, da' + \int_V \frac{\rho}{\mathbf{r}} \, d\tau')$
		boundary constraints from poisson's, potential at boundary
## The Electric Displacement
gauss' law in presence of dielectrics
	electric displacement $\vec{D} = \epsilon_0\vec{E} + \vec{P}$
		continuous at boundary of dielectric
	$\vec{\nabla}\cdot\vec{D} = \rho_f$
	$\oint \vec{D} \, \vec{da} = Q_{f,enc}$
	$\rho = \rho_b + \rho_f$ where $\rho_f$ is free charges
## Linear Dielectrics
electric susceptibility $\chi_e$, relative permittivity/dielectric constant $\epsilon_r$, electric permittivity $\epsilon$
	$\vec{P} = \epsilon_0\chi_e\vec{E}$
	$\vec{D} = \epsilon_0(1+\chi_e)\vec{E} = \epsilon_0\epsilon_r\vec{E}  =\epsilon\vec{E}$
	measure of ease of polarization (nonpolar hard, polar easy)
		vaccuum has $\epsilon_r =  1$, $\chi_e = 0$
		$\vec{E}$ smaller in dielectric than in vacuum, partial shielding
	non-linear
		$\epsilon_r$ dependent on $\vec{E}$ (electro-optic response)
		index of refraction $n = \sqrt{\mu_r\epsilon_r}$
	field, polarization, displacement zero in conductor
boundary conditions
	$D_{\perp,above}-D_{\perp,below}=\sigma_f$, $D_{\parallel,above}-D_{\parallel,below} = P_{\parallel,above}-P_{\parallel,below}$
energy
	capacitance $C = \epsilon_r C_{vac}$
	$W = \frac{1}{2}C(\Delta V)^2 = \frac{1}{2}\frac{Q^2}{C} = \frac{1}{2}Q\Delta V$
	$W = \frac{1}{2}\int \vec{D}\cdot\vec{E} \, d\tau$
force
	inserting dielectric into (disconnected) capacitor
		electric field/potential inside and outside dielectric equal (no $\sigma$ at boundary, parallel to $\vec{E}$)
		differing top $\sigma$, $\vec{D}$, proportional to $\epsilon$
		$C = \epsilon_0\frac{A}{d}(L+\chi_e x)$, $F = -\nabla W = \frac{1}{2}\frac{Q^2}{C^2}\epsilon_0\frac{a}{d}\chi_e$
	inserting into (connected) capacitor
		use work equation with constant quantity, add to work done by battery to keep $\Delta V$ constant
			$F = \frac{1}{2}\Delta V^2 \epsilon_0 \frac{a}{d}\chi_e$