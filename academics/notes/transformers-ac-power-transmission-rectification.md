# Transformers, AC Power Transmission, and Rectification
large wastage of power using DC
	increasing transmission voltage
	high voltage low current to low voltage high current
	transformers
		magnetic yoke, constrains magnetic field using primary and secondary coil
		$\frac{V_s}{V_p} = \frac{N_s}{N_p} = \frac{I_p}{I_s}$, $P_s = P_p$
		ground isolation
power
	$P = \frac{V_p^2}{R}\cos^2(2\pi * 60t)$
	$\langle P\rangle = \frac{V_{RMS}^2}{r}$
	RMS voltage usually specified
rectifier
	AC power to DC power
	half-wave rectifier → only half of sine wave
	center-tap rectifier → alternates side of tap driving load
	full-wave bridge rectifier
		power coupled through transformer, output always positive
		blocking capacitor stabilized output
			$V_p = V_s - 2V_{diode}$
			$V_{ripple} = \frac{1}{2fC}\frac{V_p}{R_{load}}$
			$\frac{V_{ripple}}{V_{load}} = \frac{1}{2RCf}$