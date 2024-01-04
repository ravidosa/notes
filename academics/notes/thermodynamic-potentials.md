# Thermodynamic Potentials
## Free Energy and Chemical Thermodynamics
see [Enthalpy](energy-thermal-physics.md#heat-capacities)
helmholtz free energy $F = U - TS$: energy to be provided as work to create system/energy freed after annihilating system
	$\Delta F \leq W$ for constant $T$
gibbs free energy $G = U - TS + PV$: helmholtz + atmospheric work
	$\Delta G \leq W_{other}$ for constant $T, P$
thermodynamic potentials $U, H, F, G$
thermodynamic identities
	see [Thermodynamic Identity](interactions-and-implications.md#mechanical-equilibrium-and-pressure)
	legendre transformation
	$dH = T \, dS + V \, dP + \mu \, dN$
	$dF = -S \, dT - P \, dV + \mu \, dN$
	$dG = -S \, dT + V \, dP + \mu \, dN$
maxwell relations (second derivative with respect to thermal natural variables ($T, S$ and $P, V$)
	$(\frac{\partial T}{\partial V})_S = -(\frac{\partial P}{\partial S})_V = \frac{\partial^2 U}{\partial S \partial V}$
	$(\frac{\partial T}{\partial P})_S = (\frac{\partial V}{\partial S})_P = \frac{\partial^2 H}{\partial S \partial P}$
	$(\frac{\partial S}{\partial V})_T = (\frac{\partial P}{\partial T})_V = \frac{\partial^2 F}{\partial T \partial V}$
	$-(\frac{\partial S}{\partial P})_T = (\frac{\partial V}{\partial T})_P = \frac{\partial^2 G}{\partial T \partial P}$
## Free Energy as a Force toward Equilibrium
nonisolated system, energy can pass between system and environment
	for fixed $T, V, N$, increase in $S$ of universe = decrease in $F$ of system
	for fixed $T, P, N$, increase in $S$ of universe = decrease in $G$ of system
extensive quantities: proportional to amount of matter ($V, N, S, U, H, F, G, m$)
intensive quantities: not proportional ($T, P, \mu, \rho$)
$\mu$ is gibbs free energy per particle