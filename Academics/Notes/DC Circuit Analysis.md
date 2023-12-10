### Electric Field
see [Electrostatics](Electrostatics.md)
electron charge $q_{e^-}=1.6\times 10^{-19}$
### Electric Potential
see [Electrostatics](Electrostatics.md#Electric%20Potential)
$U_{A \to B}=-W_{A \to B}=-\int_A^B \vec{F} \cdot \, d\vec{r}$
electric potential difference
	$V_{A \to B}=\frac{U_{A \to B}}{q}=-\int_A^B \vec{E} \cdot \, d\vec{r}$
	measured in volts (V)
electric potential vs electric potential difference
electron-volt: energy needed to move electron through 1 V potential difference
### Conductors and Resistors
current (amount of charge per unit time)
	$I=\frac{dq}{dt}$
	measured in amperes (A)
kirchoff's law
	$V=IR$
current density ($\vec{J}$) and conductivity ($\sigma$)
	$I = \int \vec{J} \cdot d\vec{A}$
	$\vec{J} = \sigma \vec{E} = -\sigma \nabla V$
resistors
	sign convention: current flows from higher to lower voltage
	series (voltage divider)
		$R_{eff}=\sum_i R_i$
	parallel (current divider)
		$\frac{1}{R_{eff}}=\sum_i \frac{1}{R_i}$
### Kirchoff's Laws
current/junction law
	$\sum_k I_k = 0$
	sum of currents into node is zero
	current in equals current out
voltage/loop law
	$\sum_k V_k = 0$
	zero drop in potential around closed loop
### Superposition
consider one voltage source at a time (short others)
add to get equivalent
### Sources, Loads, I-V Curves, and Power
source
	network containing voltage
	positive current leaving positive terminal
load
	network containing resistor, etc
	positive current entering positive terminal
I-V curves
	intersection of lines is operating point
### Thevenin Equivalent Circuit
thevenin voltage $V_{th}$ is open-circuit voltage across terminals
short circuit current $I_{sc}$ is short-circuit current through terminals
$V_{th} = I_{sc}R_{th}$
multiple voltage/current sources
	treat voltage sources as short circuit, current sources as open circuit
	apply superposition
