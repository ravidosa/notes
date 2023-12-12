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
degenerate gas: $\frac{V}{N} \ll v_Q$, treat as $T = 0$
	fermi-dirac distribution becomes step function (fermi energy $\epsilon_F = \mu$)
		all states below $\epsilon_F$ occupied, all above unoccupied
		allowed energies $\epsilon = \frac{h^2}{8mL^2}(n_x^2 + n_y^2 + n_z^2)$
		fermi temperature $T_F = \frac{\epsilon_F}{k_B}$
		degeneracy pressure $P = \frac{2N\epsilon_F}{5V} = \frac{2U}{3V}$
		bulk modulus $B = -V(\frac{\partial P}{\partial V})_T = \frac{10U}{9V}$
		heat capacity $C_V = \frac{\pi^2 Nk_B^2T}{2\epsilon_F}$
	density of states $g(\epsilon) = \frac{\pi}{2}(\frac{8mL^2}{h^2})^{\frac{3}{2}}\sqrt{\epsilon}$
		$U = \int_0^{\epsilon_F} \epsilon g(\epsilon) \, d\epsilon$
		at $T = 0$, $N = \int_0^{\epsilon_F} g(\epsilon) \, d\epsilon$
		$\mu = \epsilon_F$ only at $T = 0$
		sommerfeld expansion
### Blackbody Radiation
ultraviolet catastrophe: theoretically infinite thermal energy in electromagnetic wave
planck distribution
	$E_n = nhf$
	$\overline{E} = \frac{hf}{e^{\frac{hf}{k_BT}} - 1}, \overline{n} = \frac{1}{e^{\frac{hf}{k_BT}} - 1}$
	photon  gas: treat $\mu = 0$
		density of energy $u(\epsilon) = \frac{8\pi}{(hc)^3}\frac{\epsilon^3}{e^{\frac{\epsilon}{k_BT}} - 1}$
			$\frac{U}{V} = \int_0^{\infty} u(\epsilon) \, d\epsilon$
			wien's law: peak at $\epsilon = 2.82k_BT$
		$S(T) = \frac{32\pi^5}{45}V(\frac{k_BT}{hc})^3k_B$
stefan-boltzmann constant: $\sigma = \frac{2\pi^5k_B^4}{15h^3c^2} \approx 5.67 \cdot 10^{-8}$ W/m^2K^4
	$P = \sigma eA T^4$ (weighted average of $\epsilon$ over all wavelengths)
### Debye Theory of Solids
atoms in crystal do not vibrate independently
debye temperature $T_D = \frac{hc_s}{2k_BT}(\frac{6N}{\pi V})^{\frac{1}{3}}T$
	agree with einstein model in large temp limit
### Bose-Einstein Condensation
one spin instead of two (divide $g(\epsilon)$ by 2)
condensation temperature $T_c = \frac{0.527}{k_B}(\frac{h^2}{2\pi m})(\frac{N}{V})^{\frac{2}{3}}$
	$N$ increases exponentially to $T_c$, then flattens out
	balance between excited and unexcited states