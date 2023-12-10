### The Gibbs Factor
gibbs factor $e^{-\frac{E(s) - \mu N(s)}{k_BT}}$
probability of finding atom in microstate $s$ of $N$ total states $\mathcal{P}(s) = \frac{1}{\mathcal{Z}}e^{-\frac{E(s)-\mu N(s)}{k_BT}}$
	grand partition function $\mathcal{Z} = \sum_s e^{-\frac{E(s) - \mu N(s)}{k_BT}}$
	$\Phi = -k_BT\ln \mathcal{Z}$
### Bosons and Fermions
occupancy $\overline{n}$ of state: average number of particles in state
	system = single particle state, reservoir = all other single particle states
	unoccupied ($n = 0, E = 0$) vs occupied ($n \neq 0, E=n\epsilon$)
	$\overline{n} = -\frac{1}{\mathcal{Z}}\frac{\partial\mathcal{Z}}{\partial x}$ for $x = \frac{\epsilon - \mu}{k_BT}$
bosons: can share state
	photon, pion, helium-4 atom, etc
	integer spin
fermions: cannot share state (pauli exclusion principle)
	electron, proton, neutron, helium-3 atom, etc
	half-integer spin
when number of available states much greater than number of particles ($Z_1 \gg N,\frac{V}{N} \gg v_Q$), boson/fermion irrelevant
distribution functions
	fermi-dirac distribution: $\overline{n}_{FD} = \frac{1}{e^{\frac{\epsilon - \mu}{k_BT}} + 1}$
		$\mathcal{Z} = 1 + e^{-\frac{\epsilon - \mu}{k_BT}}$
		goes to $0$ for $\epsilon \gg \mu$, goes to $1$ for small $\epsilon \ll \mu$
	bose-einstein distribution: $\overline{n}_{BE} = \frac{1}{e^{\frac{\epsilon - \mu}{k_BT}} - 1}$
		$\mathcal{Z} = \frac{1}{1 - e^{-\frac{\epsilon - \mu}{k_BT}}}$
		goes to $0$ for $\epsilon \gg \mu$, goes to $\infty$ as $\epsilon \to \mu$
	boltzmann distribution: $\overline{n}_B = e^{-\frac{\epsilon - \mu}{k_BT}}$
		fermi-dirac and bose-einstein reduce to boltzmann for $\frac{\epsilon - \mu}{k_BT} \gg 1$
### Degenerate Fermi Gases