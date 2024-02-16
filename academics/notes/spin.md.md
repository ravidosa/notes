# Spin
orbital momentum vs spin ($s$) momentum
algebra of spin identical to (orbital) [angular momentum](angular-momentum.md#quantum-mechanics) (replace $\ell$ with $s$)
	permits half-integer for $s$, $m$
	label states with $(n, \ell, m_\ell, m_s)$
every elementary particle has specific $s$ value
	$s = \frac{1}{2}$ for electron, proton
	photon spin 1, higgs boson spin 0
## Spin 1/2
spin up and spin down eigenstates
general state represented as spinor
	coefficients of up and down
spin operators are $2 \times 2$ matrices (pauli spin matrices)
	$\hat{S}_z = \frac{\hbar}{2}\begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}$
	$\hat{S}_+ = \hbar\begin{pmatrix}0 & 1 \\ 0 & 0\end{pmatrix}$
	$\hat{S}_- = \hbar\begin{pmatrix}0 & 0 \\ 1 & 0\end{pmatrix}$
	$\hat{S}_x = \frac{\hbar}{2}\begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}$
	$\hat{S}_y = \frac{\hbar}{2}\begin{pmatrix}0 & -i \\ i & 0\end{pmatrix}$
	eigenspinors are spin up (eigenvalue $\frac{\hbar}{2}$), spin down ($-\frac{\hbar}{2}$)
electron in a magnetic field
dipole moment $\mu = \gamma S$ (gyromagnetic ration $\gamma$)
	torque $-\mu \times B$, enery $-\gamma B \cdot S$
adding angular momenta
clebsch-gordan coefficients
applied group theory (representation theory, lie groups)
## Selection Rules
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
			bose einstein condensates
				any number of bosons in same quantum state
				superconductivity, superfluidity
			multielectron atoms
				electron orbitals fill up in order of energy
				higher $\ell$ states have slightly higher energy
				ground state orbital energies change with Z
	exchange force: bosons attracted, fermions repulsed
spin
	spinors also antisymmetric
		account for spin in pauli exclusion principle
generalized symmetrization principle
	exchange operator
	for $n$ identical particles, symmetric/antisymmetric under interchange