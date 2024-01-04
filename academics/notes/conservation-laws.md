# Conservation Laws
continuity equation
	global conservation of charge
	$\frac{\partial \rho}{\partial t} = -\nabla \cdot \vec{J}$
poynting's theorem
	poynting vector $\vec{S} = \frac{1}{\mu_0}(\vec{E} \times \vec{B})$
		represents energy flux density
		$P = \frac{dW}{dt} = -\frac{d}{dt}\int_V u \,d\tau - \oint_S \vec{S} \cdot d\vec{a}$
maxwell's stress tensor
	$T_{ij} = \epsilon_0(E_iE_j - \frac{1}{2}\delta_{ij}E^2) + \frac{1}{\mu_0}(B_iB_j - \frac{1}{2}\delta_{ij}B^2)$
	diagonal pressures, off-diagonal shears
conservation of momentum
	momentum density $\vec{g} = \mu_0\epsilon_0\vec{S} = \epsilon_0(\vec{E} \times \vec{B})$
	$\vec{p} = \int_V \vec{g} \, d\tau = \mu_0\epsilon_0 \int_V \vec{S} \, d\tau$
	angular momentum density $\vec{\ell} = \vec{r} \times \vec{g} = \epsilon_0(\vec{r} \times (\vec{E} \times \vec{B}))$
	$\vec{L} = \int_V \vec{\ell} \, d\tau = \epsilon_0 \int_V (\vec{r} \times (\vec{E} \times \vec{B})) \, d\tau$