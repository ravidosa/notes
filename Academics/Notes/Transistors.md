amplification
	small signal creates larger signal
diode tubes
	filament heats cathode, boiling off electrons
	power rectification, AM demodulation
triode tubes
	grid controls current between anode and cathode
	amplification
NPN
	$V_C > V_B$
	right/top diode back-biased
	no current if $V_B - V_E < 0.6$
	small current $I_B$, large current $I_C$
	$I_C = \beta I_B$, $I_E = I_C + I_B \approx \beta I_B$
	ideal transistor
		approximate as $\beta \to \infty$
		$I_B \approx 0$
	transistor switch
		turns LED using source w/o necessary voltage/current
	emitter follower
		high impedance drives low impedance load
	common emitter amplifier
		$I_E = \frac{V_{in} - 0.6}{R_E} = I_C$
		$\Delta V_{out} = -\frac{R_C}{R_E}\Delta V_{in}$
	AC coupling
		input biased by connected to upstream signal with high pass filter
PNP
	NPN but reversed
	$V_C < V_E, V_B$
	no current if $V_E - V_B < 0.6$