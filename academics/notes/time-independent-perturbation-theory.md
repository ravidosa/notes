# Time-Independent Perturbation Theory
## Nondegenerate Perturbation Theory
perturbation theory: approximate solutions for perturbed problem by building on exact solutions for unperturbed
	$H = H^0 + \lambda H'$ for small $\lambda$
	$\psi_n = \sum_{k=0}\lambda^k\psi_n^k, E_n = \sum_{k=0}\lambda^kE_n^k$
	substitute into $H\psi_n = E\psi_n$, group by $\lambda^k$
	first-order ($\lambda = 1$), second order ($\lambda = 2$)
first-order theory
	$H^0\psi_n^1 + H'\psi_n^0 = E^0_n\psi_n^1 + E^1_n\psi_n^0$
	$E_n^1 = \braket{\psi_n^0|H'|\psi_n^0}$
		first-order correction to energy is expectation of perturbation in unperturbed state
	$\psi_n^1 = \sum_{m\neq n}\frac{\braket{\psi_m^0|H'|\psi_n^0}}{E_n^0 - E_m^0}\psi_m^0$
		assumes unperturbed energy spectrum is nondegenerate
second-order theory
	$H^0\psi_n^2 + H'\psi_n^1 = E_n^0\psi_n^2 + E_n^1\psi_n^1 + E_n^2\psi_n^0$
	$E_n^2 = \sum_{m\neq n}\frac{|\braket{\psi_m^0|H'|\psi_n^0}|^2}{E_n^0 - E_m^0}$
## Degenerate Perturbation Theory
degeneracy: multiple states with same energy
two-fold degeneracy ($\psi_a^0, \psi_b^0$)
	perturbation splits degenerate energy
	split states linear combination of unperturbed "good" states
	$W_{ij} = \braket{\psi_i^0|H'\psi_j^0}, W = \begin{pmatrix} W_{aa} & W_{ab} \\ W_{ba} & W_{bb}\end{pmatrix}$
		eigenvalues are energies, eigenstates are coefficients of good states
		$E_\pm^1 = \frac{1}{2}(W_{aa} + W_{bb} \pm \sqrt{(W_{aa} - W_{bb})^2 + 4|W_{ab}|^2})$
higher-order degeneracy
	increase size of $W$
