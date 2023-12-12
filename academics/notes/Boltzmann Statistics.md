### The Boltzmann Factor
boltzmann factor $e^{-\frac{E(s)}{k_BT}}$
probability of finding atom in microstate $s$ of $N$ total states $\mathcal{P}(s) = \frac{1}{Z}e^{-\frac{E(s)}{k_BT}}$
	boltzmann distribution
		probability dependent on distance from ground state $E_0$
	partition function $Z = \sum_s e^{-\frac{E(s)}{k_BT}}$
	low temp limit ($\frac{E_n - E_0}{k_BT} \gg 1$)
		$\mathcal{P}_n = \begin{cases} 1 & n = 0 \\ 0 & n \neq 0 \end{cases}$
		$Z = 1$
	high temp limit ($\frac{E_n - E_0}{k_BT} \ll 1$)
		$\mathcal{P}_n = \frac{1}{N}$
		$Z = N$
### Average Values
$\overline{E} = \frac{1}{Z}\sum_s E(s)e^{-\beta E(s)} = \sum_s \mathcal{P}(s)e^{-\beta E(s)} = -\frac{\partial}{\partial \beta} \ln \mathcal{Z}$ ($\beta = \frac{1}{k_BT}$)
	generalized $\overline{X} = \frac{1}{Z}\sum_s X(s)e^{-\frac{E(s)}{k_BT}}$
	$U = N\overline{E}$
apply to results for paramagnet
rotation of molecules
	$E(j) = j(j + 1)\epsilon$ ($\epsilon = \frac{\hbar^2}{2I}$)
	$Z_{rot} = \sum_j (2j + 1)e^{-\beta E(j)}$
	for $k_BT \gg \epsilon, Z \gg 1$
		$Z_{rot} \approx \frac{k_BT}{2\epsilon}$ (identical atoms)
		$Z_{rot} \approx \frac{k_BT}{\epsilon}$ (different atoms)
### The Equipartition Theorem
average energy of quadratic degree of freedom is $\overline{E} = \frac{1}{2}k_BT$
does not apply to QM systems
### The Maxwell Speed Distribution
maxwell distribution $\mathcal{D}(v) = (\frac{m}{2\pi k_BT})^{\frac{3}{2}}4\pi v^2 e^{-\frac{mv^2}{2k_BT}}$
	for $x = \frac{v}{v_{max}}$, $\mathcal{D}(v) = \frac{4}{\sqrt{\pi}} \int_{x_{min}}^{\infty} x^2e^{-x^2} \, dx$
### Partition Functions and Free Energy
system in equilibrium with reservoir, $Z = e^{-F\beta}, F = -k_BT\ln Z$
	$S = -(\frac{\partial F}{\partial T})_{V,N}$
	$P = -(\frac{\partial F}{\partial V})_{T,N}$
	$\mu = (\frac{\partial F}{\partial N})_{T,V}$
### Partition Functions for Composite Systems
$Z = Z_1^N$ (noninteracting, distinguishable)
$Z = \frac{1}{N!}Z_1^N$ (noninteracting, indistinguishable)
### Ideal Gas Revisited
$Z_1 = Z_{tr}Z_{rot}$
molecule in 1d box of length $L$
	$\lambda_n = \frac{2L}{n}$
	$p_n = \frac{h}{\lambda_n} = \frac{hn}{2L}$
	$E_n = \frac{p_n^2}{2m} = \frac{h^2n^2}{8mL^2}$
	$Z_{tr} = \sum_n e^{-\beta E_n} \approx \frac{L}{\ell_Q}$, $\ell_Q = \frac{h}{\sqrt{2\pi mk_BT}}$
	generalize to 3d, $v_Q = \ell_Q^3$
		$Z = \frac{1}{N!}(\frac{VZ_{int}}{v_Q})^3$