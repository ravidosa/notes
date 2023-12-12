### Temperature
$\frac{\partial S_A}{\partial U_A} = \frac{\partial S_B}{\partial U_B}$ at equilibrium
	$\frac{1}{T} = (\frac{\partial S}{\partial U})_{N,V}$
	temperature = willingness to give energy away
		normal vs miserly vs enlightened
	$U = q\epsilon$
### Entropy and Heat
predicting heat capacity
	find $\Omega$ in terms of $U, V, N$
	$S = Nk_B\ln\Omega$
	$T = (\frac{\partial S}{\partial U})^{-1}$
	solve for $U(T)$
	$C_V = \frac{\partial U}{\partial T}$
$\Delta S = \int_{T_i}^{T_f} \frac{C_V}{T} \, dT$
	at zero temperature, system in lowest state $\Omega = 1, S = 0$ (3rd law)
	residual entropy
### Paramagnetism
$U = \mu B(N_{\downarrow} - N_{\uparrow}) = \mu B(N - 2N_{\uparrow}) = -N\mu B\tanh\frac{\mu B}{k_BT}$
$M = \mu(N_{\uparrow} - N_{\downarrow}) = -\frac{U}{B} = N\mu\tanh\frac{\mu  B}{k_B T} \approx \frac{N\mu^2B}{k_BT}$ (curie's law,  $\frac{\mu B}{k_BT} \ll 1$)
$\Omega = \frac{N!}{N_{\uparrow}!N_{\downarrow}!}$
$C_B = Nk\frac{(\frac{\mu B}{k_B T})^2}{\cosh^2\frac{\mu B}{k_B T}}$, goes to $0$ at low and high $T$
$S, \Omega$ maximized for $N_{\downarrow} = N_{\uparrow}, U = 0$
$\mu_B = \frac{e\hbar}{4\pi m_e}$ (electronic paramagnet)
temperature goes negative (negative > positive)
### Mechanical Equilibrium and Pressure
mechanical equilibrium: equal pressures
$p = T(\frac{\partial S}{\partial V})_{U,N}$ when volume changing
thermodynamic identity
	$dU = T \, dS - P \, dV$ (with all else fixed)
isentropic: adiabatic + quasistatic, no change in entropy
### Diffusive Equilibrium and Chemical Potential
diffusive equilibrium: chemical potential $\mu = -T(\frac{\partial S}{\partial N})_{U,V}$ equal
	chemical potential: amount by which energy changes when particle added for fixed $S$, $V$
		for monatomic gas: $\mu = -k_BT\ln(\frac{V}{N}(\frac{2\pi mk_BT}{h^2})^{\frac{3}{2}})$
	flow from higher potential to lower potential (diffusion)
	$dU = T \, dS - P \, dV + \mu \, dN$
		$dU = T \, dS - P \, dV + \sum_i \mu_i \, dN_i$ (generalized to multiple types of particles)
	