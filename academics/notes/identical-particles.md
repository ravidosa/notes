# Identical Particles
## Two-Particle Systems
wavefunction dependent on position of both particles
noninteracting
	sum potentials, solve wavefunction by separation of variables
central potentials
	potential dependent on distance, reduces to one-particle system
bosons and fermions (noninteracting)
	$\psi_{\pm}(\vec{r}_1, \vec{r}_2) = A(\psi_a(\vec{r}_1))\psi_b(\vec{r}_2) \pm \psi_b(\vec{r}_1))\psi_a(\vec{r}_2))$
		bosons are $+$ (symmetric, integer spin), fermions are $-$ (antisymmetric, half-integer spin)
	spin-statistics connection
		see [Quantum Statistics](quantum-statistics.md)
		identical fermions cannot occupy same state (pauli exclusion principle)
	exchange force: bosons attracted, fermions repulsed
spin
	spinors also antisymmetric
		account for spin in pauli exclusion principle
generalized symmetrization principle
	exchange operator
	for $n$ identical particles, symmetric/antisymmetric under interchange
## Atoms
neutral atom with atomic number $Z$, electric charge $Z_e$
	$\hat{H} = \sum_{j=1}^Z (-\frac{\hbar^2}{2m}\nabla^2_j - (\frac{1}{4\pi\epsilon_0})\frac{Ze^2}{r_j}) + \frac{1}{2}(\frac{1}{4\pi\epsilon_0})\sum_{j\neq k}^Z \frac{e^2}{|\vec{r}_j - \vec{r}_k|}$
	kinetic and potential energy of each electron, mutual repulsion with other electrons
only solved for hydrogen ($Z = 1$), approximated otherwise by ignoring repulsion term
	helium
		parahelium (antisymmetric) vs orthohelium (symmetric)
periodic table
	orbitals $(n, \ell, m)$
	shells $n$
		room for certain number of electrons
	spdf
		sharp $s$ ($\ell = 0$)
		principal $p$ ($\ell = 1$)
		diffuse $d$ ($\ell = 1$)
		fundamental $f$ ($\ell = 3$)
		alphebetical, skipping $j$
	hund's rules: total quantum number for atoms