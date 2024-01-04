# Statistical Mechanics
lots of particles → classical and quantum properties needed
particle in box
	$P(L) = P(R) = \frac{1}{2}$
particles in box
	binomial coefficient $W^N_{n_L} = {N \choose n_L}$
	macrostate = binomial coefficient * microstate
	largest probability macrostate is equilibrium, will shift towards equilibrium
entropy
	amount of disorder in system
	$S = k_B\ln{W}$
	additive and proportional to $N$
	$\frac{\partial S}{\partial E} \equiv \frac{1}{T}$
	entropy maximized for equal temps
	always increasing
	$\Delta S = S_f - S_i = \int_1^2 \frac{dQ}{T}$
boltzmann distribution
	$E=\sum_{i=1}^Nn_i\hbar\omega_0 = M\hbar\omega_0$
	stars and bars
	$P(n_i)=\frac{{{(M - n_i) + (N-1) - 1} \choose {M-n_i}}}{{{M+N-1}\choose M}}$
	$N(E_n)=e^{-\frac{E^n}{k_BT}}$
	$P(E_n)=\frac{e^{-\frac{E^n}{k_BT}}}{\sum_n e^{-\frac{E^n}{k_BT}}}$ for very large N
	$\mathcal{N}(E_n)=NAe^{-\frac{E^n}{k_BT}}$ number of particles per state with energy $E_n$
	$\bar{E}=\frac{\hbar\omega_0}{e^{\frac{\hbar\omega_0}{k_BT}}-1}=\frac{\sum_n E_n\mathcal{N}(E_n)}{\sum_n \mathcal{N}(E_n)} = \frac{\int E\mathcal{N}(E)D(E)dE}{\int \mathcal{N}(E)D(E)dE}$
maxwell distribution
	$\bar{f(v)}=\frac{f(v)e^{-\frac{mv^2}{2k_BT}}v^2dv}{\sqrt{\frac{\pi}{2}}(k_BT/m)^\frac{3}{2}}$
	$P(v)_{maxwell}=\sqrt{\frac{2}{\pi}}(\frac{m}{k_BT})^\frac{3}{2}v^2e^{-\frac{mv^2}{2k_BT}}$
indistinguishable
	quantum distributions
		$\mathcal{N}(E)=\frac{1}{Be^\frac{K}{k_BT}}$ (distinguishable)
		$\mathcal{N}(E)=\frac{1}{Be^\frac{K}{k_BT}-1}$ (bose-einstein, bosons)
		$\mathcal{N}(E)=\frac{1}{Be^\frac{K}{k_BT}+1}$(fermi-dirac, fermions)
			fermi energy $\mathcal{N}(E_F)=\frac{1}{2}$
			$B = e^{-\frac{E_F}{k_BT}}$
		converge for large $\frac{E}{k_BT}$
		quantum gas
			$\bar{E}=\frac{3}{2}k_BT(1\mp\frac{\sqrt{2}\pi^2\hbar^3}{(2s+1)(2\pi mk_BT)^\frac{3}{2}}(\frac{N}{V})^1 + \ldots)$
			quantum corrections small as temp increases
		fermi-dirac gas
			$E_F = \frac{\pi^2\hbar^2}{m}(\frac{3}{2\sqrt{2}\pi}\frac{N}{V})^\frac{2}{3}$
		photon gas
			$U_{photon}=\frac{8\pi Vk_B^4T^4}{15h^3c^3}$