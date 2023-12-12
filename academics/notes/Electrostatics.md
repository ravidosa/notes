### Electric Field
coulomb's law
	source charges (may be moving) exert force on test charge
	net force is sum of forces from individual charges (principle of superposition)
		$\vec{F}=\sum_i \vec{F}_i$
	for electrostatics, assume stationary point charges and test charge
	electric force (coulomb's law)
		$\vec{F} = \frac{qQ}{4\pi\epsilon_0}\frac{\vec{\mathbf{r}}}{\mathbf{r}^3}$
	can be attractive or repulsive
	permittivity of vacuum $\epsilon_0 = 8.85 \times 10^{-12}$ 
electric field $\vec{E}$: force per unit charge exerted on test charge
$\vec{E}$ for $n$ point charges
	$\vec{F}=Q\vec{E}$
	$\vec{E}(\vec{r})=\frac{1}{4\pi\epsilon_0}\sum_{i=1}^n \frac{q_i}{\mathbf{r}^2}\hat{\mathbf{r}}$
	depends on position of test charge, not dependent on value/sign
$\vec{E}$ for continuous charge distribution
	electric field for continuous charge distribution
		$\vec{E}(\vec{r})=\frac{1}{4\pi\epsilon_0}\int\frac{1}{\mathbf{r}^2}\hat{\mathbf{r}} \, dq$
	line charge density $\lambda$
		$\vec{E}(\vec{r})=\frac{1}{4\pi\epsilon_0}\int\frac{\lambda(\vec{r'})}{\mathbf{r}^2}\hat{\mathbf{r}} \, dl'$
	surface charge density $\sigma$
		$\vec{E}(\vec{r})=\frac{1}{4\pi\epsilon_0}\int\frac{\sigma(\vec{r'})}{\mathbf{r}^2}\hat{\mathbf{r}} \, da'$
	volume charge density $\rho$
		$\vec{E}(\vec{r})=\frac{1}{4\pi\epsilon_0}\int\frac{\rho(\vec{r'})}{\mathbf{r}^2}\hat{\mathbf{r}} \, d\tau'$
#### Useful Integrals
	$\int \frac{1}{\sqrt{x^2+a^2}} \, dx = \ln(x+\sqrt{x^2+a^2}) + c$
	$\int \frac{1}{x^2+a^2} \, dx = \frac{1}{a}\tan^{-1}(\frac{x}{a}) + c$
	$\int \frac{1}{(x^2+a^2)^{\frac{3}{2}}} \, dx = \frac{1}{a^2}\frac{x}{\sqrt{x^2+a^2}} + c$
	$\int \frac{x}{\sqrt{x^2+a^2}} \, dx = \sqrt{x^2+a^2} + c$
	$\int \frac{x}{x^2+a^2} \, dx = \frac{1}{2}\ln(x^2+a^2) + c$
	$\int \frac{x}{(x^2+a^2)^{\frac{3}{2}}} \, dx = -\frac{1}{\sqrt{x^2+a^2}} + c$
### Divergence and Curl of Electrostatic Fields
field lines
	go outward from positive, inward to negative
	proportional to $q$
	never cross
	extend to infinity or start/stop at charges
electric flux (amount of electric field lines passing through area)
	$\phi_E = \underset{S}{\int} \vec{E} \, \vec{da}$ (open surface)
	$\phi_E = \underset{S}{\oint} \vec{E} \, \vec{da}$ (closed surface)
gauss's law (generalizable to any number of charges inside closed(gaussian) surface)
	$\phi_E = \underset{S}{\oint} \vec{E} \, \vec{da} = \frac{q_{enc}}{\epsilon_0}$
	$\vec{\nabla} \cdot \vec{E} = \frac{\rho}{\epsilon_0}$
	not dependent on surface 
faraday's law
	$\vec{\nabla} \times \vec{E} = -\frac{\partial \vec{B}}{dt}= 0$ (for electrostatics)
### Electric Potential
electric potential
	$\vec{E} = -\vec{\nabla}V$
	$V(\vec{r}) = -\int_0^{\vec{r}} \vec{E}  \, \vec{dl}$
	not path dependent
	not every vector can be a valid electrostatic electric field (need 0 curl, scalar V)
	point charge at origin
		$V(\vec{r}) = \frac{1}{4\pi \epsilon_0}\frac{q}{r}$ (ref point at $\infty$)
	point charge at $\vec{r'}$
		$V(\vec{r}) = \frac{1}{4\pi \epsilon_0}\frac{q}{\mathbf{r}}$ (ref point at $\infty$)
	n point charges
		$V(\vec{r}) = \frac{1}{4\pi \epsilon_0}\sum_{i=0}^n\frac{q_i}{\mathbf{r_i}}$ (ref point at $\infty$)
	line charge
		$V(\vec{r}) = \frac{1}{4\pi \epsilon_0}\int \frac{\lambda(\vec{r'})}{\mathbf{r}} \, dl'$
	surface charge
		$V(\vec{r}) = \frac{1}{4\pi \epsilon_0}\int \frac{\sigma(\vec{r'})}{\mathbf{r}} \, da'$
	volume charge
		$V(\vec{r}) = \frac{1}{4\pi \epsilon_0}\int \frac{\rho(\vec{r'})}{\mathbf{r}} \, d\tau'$
poisson's equation
	$\nabla^2 V = -\frac{\rho}{\epsilon_0}$
	for no charge ($\rho = 0$), $V = 0$ (laplace's equation)
electric field discontinuous at boundary ($\frac{\sigma}{\epsilon_0}$), electric potential continuous
### Work and Energy
work
	$W = -\int_a^b \vec{F} \, \vec{dl} = Q(V(\vec{b}) - V(\vec{a}))$
	conservative, only depends on potential, not path
electric potential energy
	electric potential is potential energy per unit charge
	point charge (at $\infty$)
		potential from other charges
		$W = U_0 + \frac{1}{2}\sum_{i=1}^n q_iV(\vec{r}_i)$
	line charge
		$W = \frac{1}{2}\int \lambda V(\vec{r}) \, dl'$
	surface charge
		$W = \frac{1}{2}\int \sigma V(\vec{r}) \, da'$
	volume charge
		$W = \frac{1}{2}\int \rho V(\vec{r}) \, d\tau'$
### Conductors
conductor
	electrons free to roam
	$\vec{E}_{inside = 0}$
		induced charges build up field that cancels original field
	$\rho = 0$
		no electric field, electrically neutral inside
		net charge on surface
	constant $V$ (equipotential)
		electric field = gradient of potential, is 0
	$\vec{E}_{outside} = \frac{\sigma}{\epsilon_0}\hat{n}$
		$\sigma = -\epsilon_0\frac{\partial V}{\partial n}$
	electrostatic pressure on charged surface
		$\frac{\vec{F}}{da} = \sigma\frac{\vec{E}_{above} + \vec{E}_{below}}{2}$
		$P = \frac{\epsilon_0}{2}E^2$
	charged bodies attract conductors
charge in cavity
	field like individual charge