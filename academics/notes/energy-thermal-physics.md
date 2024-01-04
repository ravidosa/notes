# Energy in Thermal Physics
## Thermal Equilibrium
temperature
	quantity measured by thermometer (operational definition)
		measurable property of system that varies with temp]
	quantity same for two objects after long contact (theoretical definition)
		thermal equilibrium with system (same temp)
			relaxation time: time to reach equilibrium
		energy exchange (thermal) vs particle exchange (diffusive) vs volume exchange (mechanical)
	measure of tendency of object to spontaneously lose energy (theoretical)
		higher temperature loses
		celsius: based on boiling water
		fahrenheit: based on human experience
		kelvin: constant-volume gas thermometer (linear pressure dependence)
			extrapolate to absolute zero at $-273.15^{\circ} C$
			triple point as reference until 2019
			$1^{\circ}K$  is change in thermal energy of $k_B$ joules
	$\frac{1}{T} = (\frac{\partial S}{\partial U})_{N,V}$
## The Ideal Gas
ideal gas law
	$PV = nRT$ or $PV = Nk_BT$
		pressure $P$, volume $V$, number of moles $n$, ideal gas constant $R$, temp in kelvins $T$, number of molecules $N$, boltzmann constant $k_B = \frac{R}{N_A}$
	valid in limit of low density (space between particles $\gg$ size of particle), $V$ small enough for homogenous $P, T$
equation of states
	relate state variables, no time dependency
	build from microscopic description
translational kinetic energy
	$\bar{K}_{trans} = \frac{3}{2}k_BT$
	$v_{rms} = \sqrt{\frac{3RT}{M}}$
## Equipartition of Energy
equipartition theorem: at temp $T$, average energy of any quadratic degree of freedom is $\frac{1}{2}k_BT$
	DOF
		monatomic gas: $U = K_{trans} = \frac{3}{2}k_BT$
		linear molecules: $K_{rot} = k_BT$
		nonlinear polyatomic molecules: $K_{rot} = \frac{3}{2}k_BT$
		solids: only vibration, $U = 3k_BT$
	$U \neq E_{tot}$
	some vibrational modes frozen at low temperatures
## Heat and Work
heat $Q$: spontaneous flow of energy between obects caused by diff in temp
work $W$: transfer of energy in/out of system
first law of thermodynamics
	$\Delta U = Q + W$
	energy in joules, calories
process of heat transfer
	conduction, convection, radiation
## Compression Work
quasistatic approximation: slow volume change
	$W = -\int_{V_i}^{V_f} P(V) \, dV$
	isothermal compression: temperature remains constant, $\Delta U = 0$
		$W = Nk_BT\ln\frac{V_i}{V_f}$
		$Q = -W = Nk_BT\ln\frac{V_f}{V_i}$
	adiabatic compression: no heat gained/lost, $Q = 0$
		$\Delta U = W$
		$V^{\gamma}P$ constant, adiabatic exponent $\gamma = \frac{f+2}{f}$
	isobaric compression: pressure remains constant
		$W = (V_i - V_f)P$
		$\Delta U = \frac{f}{2}P(V_f - V_i)$
		$Q = \frac{f + 2}{2}P(V_f - V_i)$
	isochoric compression: volume remains constant
		$W = 0$
		$\Delta U =\frac{f}{2}V(P_f - P_i)$
		$Q = \Delta U = \frac{f}{2}V(P_f - P_i)$
## Heat Capacities
heat capacity $C = \frac{Q}{\Delta T}$
	specific heat capacity $c = \frac{C}{m}$
	heat capacity at constant volume
		$C_V = \frac{f}{2}Nk_B$
	heat capacity at constant pressure
		$C_P = \frac{f + 2}{2}Nk_B$
latent heat $L$ heat required to change phase
	specific latent heat $l = \frac{L}{m}$
enthalpy $H = U + PV$
## Rates of Processes
conduction: $\frac{Q}{\Delta t} = -kA\frac{dT}{dx}$
	ideal gas thermal conductivity $k = \frac{1}{2}\frac{C_V}{V}\ell\bar{v}$
viscosity $\frac{|F_x|}{A} = \eta\frac{du_x}{dz}$ in poise
diffusion
	fick's law: $J_x = -D\frac{dn}{dx}$