# RLC Circuits Transient Response
RLC circuit
	$Q + RC\frac{dQ}{dt} + LC\frac{d^2Q}{dt^2} = 0$
	$Q = Ae^{at}$ (damped harmonic oscillator)
	$a = -\frac{1}{2\tau_{RL}}(1\pm\sqrt{1-4\frac{\tau_{RL}}{\tau_{RC}}})$ for $\tau_{RL} = \frac{L}{R}, \tau_{RC} = RC$
	overdamping ($\tau_{RC} \gg \tau_{RL}$)
		$a = -\frac{1}{\tau_{RC}}, -\frac{1}{\tau_{RL}}$
		$Q(t) = Ae^{-\frac{1}{\tau_{RC}}t} + Be^{-\frac{1}{\tau_{RL}}t}$
		$I_0 = 0$ so $B = -A\frac{\tau_{RL}}{\tau_{RC}} \ll A$
		$I(t) = \frac{V_0}{R}(e^{-\frac{t}{\tau_{RC}}}-e^{-\frac{t}{\tau_{RL}}})$
		$Q(t) = \frac{Q_0}{\tau_{RC} - \tau_{LC}}(\tau_{RC}e^{-\frac{t}{\tau_{RC}}} - \tau_{RL}e^{-\frac{t}{\tau_{RL}}}) \approx Q_0e^{-\frac{t}{\tau_{RC}}}$
	critical damping ($\tau_{RC} = 4\tau_{RL}$)
		$a = -\frac{2}{\tau_{RC}}$
		$Q(t) = Ae^{-\frac{2}{\tau_{RC}}t} + Bte^{-\frac{2}{\tau_{RC}}t}$
		$I_0 = 0$ so $B = A\frac{2}{\tau_{RC}}$
		$I(t) = 4\frac{V_0}{R}\frac{t}{\tau_{RC}}e^{-\frac{2}{\tau_{RC}}t}$
		$Q(t) = Q_0(1-\frac{2}{\tau_{RC}}t)e^{-\frac{2}{\tau_{RC}}t}$
	underdamping ($\tau_{RL} \gg \tau_{RC}$)
		$a = -\frac{1}{2\tau_{RL}}\pm i\omega_0$
		$Q(t) = (Ae^{i\omega_0t}+A^*e^{-i\omega_0t})e^{-\frac{t}{2\tau_{RL}}} = a\cos\omega_0t + b\sin\omega_0t$
		$I_0 = 0$ so $b = \frac{1}{2}\sqrt{\frac{\tau_{RC}}{\tau_{RL}}}a \ll a$
		$I(t) = V_0\sqrt{\frac{C}{L}}\sin(\omega_0 t)$
		$Q(t) = Q_0\cos(\omega_0t)e^{-\frac{t}{2\tau_{RL}}}$
	$R_{crit} = 2\omega_0L = \frac{2}{\omega_0C}$