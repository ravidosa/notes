### The Lorentz Force Law
source charges move, generate magnetic field
for magnetostatics, assume constant currents and $\vec{B}$
	$\vec{\nabla} \cdot \vec{B} = 0$
	$\vec{\nabla} \times \vec{B} \mu_0\vec{J} + \mu_0\epsilon_0\frac{\partial\vec{E}}{\partial t} = \mu_0\vec{J}$ (Ampere's Law)
use RHR for magnetic field lines
current in opposite directions repel, same direction attract
lorentz force
	$\vec{F}_{mag} = q(\vec{v}\times\vec{B})$
	$\vec{F} = q(\vec{E}+\vec{v}\times\vec{B})$
	magnetic forces do no work
cyclotron frequency $\omega = \frac{qB}{m}$
current
	conventionally in direction of motion of positive charges
	$\vec{I} = \lambda \vec{v}$
	$\vec{F}_{mag} = \int I(\vec{dl} \times \vec{B})$
	surface current density $\vec{K} = \frac{dI}{dl_{\perp}} = \sigma\vec{v}$
		$I = \int \vec{K} \, dl_{\perp}$
		$\vec{F}_{mag} = \int(\vec{K}\times\vec{B}) \, da$
	volume current density $\vec{J} = \frac{dI}{da_{\perp}}$
		$I = \int \vec{J} \, \vec{da}$
		$\vec{F}_{mag} = \int (\vec{J} \times \vec{B}) \, d\tau$
### The Biot-Savart Law
$\vec{B} = \frac{\mu_0}{4\pi}\int \frac{\vec{I}\times\hat{\mathbf{r}}}{\mathbf{r}^2} \, dl'$
	surface current density
		$\vec{B} = \frac{\mu_0}{4\pi}\int \frac{\vec{K}(\vec{r}')\times\hat{\mathbf{r}}}{\mathbf{r}^2} \, da'$
	volume current density
		$\vec{B} = \frac{\mu_0}{4\pi}\int \frac{\vec{J}(\vec{r}')\times\hat{\mathbf{r}}}{\mathbf{r}^2} \, d\tau'$
	permeability of free space $\mu_0 \approx 4\pi*10^{-7}$
field lines originate at positive charges, terminate at negative charges
	no magnetic monopoles
### The Divergence and Curl of $\vec{B}$
ampere's law
	$\oint \vec{B} \cdot d\vec{l} = \mu_0I_{enc}$
	$\nabla^2 \vec{A} = -\mu_0\vec{J}$
### Magnetic Vector Potential
$\vec{B} = \vec{\nabla} \times \vec{A}$
	can add any function with zero curl (gauge freedom)
		$\vec{\nabla}\cdot \vec{A} = 0$ (coulomb gauge)
		$\vec{B} = 0$ at $r=\infty$, gauge complete
$\vec{A}(\vec{r}) = \frac{\mu_0}{4\pi} \int \frac{\vec{J}(\vec{r}')}{\mathbf{r}} \, d\tau'$
	$\vec{A}$ mimics direction of currents, $\frac{1}{2}\vec{B}\times\vec{r}'$ for uniform $\vec{B}$
$\vec{B}_{above} - \vec{B}_{below} = \mu_0\vec{K}\times\hat{n}$
$\vec{A}$ continuous across boundaries
mutipole expansion
	$\vec{A}(\vec{r}) = \frac{\mu_0I}{4\pi} \sum_{n=0}^\infty \frac{1}{r^{n+1}} \oint (r')^n P_n(\cos\alpha) \,d\vec{l}'$
	$\vec{A}_{mon}(\vec{r}) = 0$
	$\vec{A}_{dip}(\vec{r}) = \frac{\mu_0}{4\pi}\frac{m\times \hat{r}}{r^2}$ (independent of choice of origin)
	magnetic dipole moment
		$\vec{m} = I\int \, d\vec{a} = I\vec{a} = \frac{1}{2}\int\vec{r}'\times\vec{J}(\vec{r}') \, d\tau'$
		$\vec{B}_{dip} = \vec{\nabla} \times \vec{A}_{dip} = \frac{\mu_0m}{4\pi r^3}(2\cos\theta\hat{r} + \sin\theta\hat{\theta}) = \frac{\mu_0}{4\pi}\frac{3(\vec{m}\cdot\hat{r})\hat{r} - \vec{m}}{r^3}$ 		