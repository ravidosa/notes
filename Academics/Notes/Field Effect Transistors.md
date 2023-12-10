$\beta$ not infinite for bipolar transistors
	signals too small/currents too high
	impractical power draw
fet vs bipolar
	base = gate, emitter =source, collector = drain
	metal oxide semiconductor fet (mosfet)
		depletion mode (n-channel)
			conducts when $V_{gate} \geq V_{source}$
			depleted, stops conducting when $V_{gate} < V_{source}$
		enhancement mode (n-channel)
			depleted when $V_{gate} \leq V_{source}$
			starts conducting when $V_{gate} > V_{source}$
		enhancement mode (p-channel)
			depleted when $V_{gate} \geq V_{source}$
			starts conducting when $V_{gate} < V_{source}$
		characterized by on resistance
		rapid turn on, hard for linear circuit
	junction fet (jfet)
		always depletion mode (n-channel or p-channel)
		$\Delta i_D = g_m\Delta V_{GS}$
		source follower
			$I_G = I_D = \frac{|V_{GS}|}{R_S}$
		common source amplifier
			input frequencies above $\frac{1}{2\pi RC}$, source voltage fixed
			$G = -R_Dg_m$