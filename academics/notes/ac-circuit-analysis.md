# AC Circuit Analysis
capacitors
	gauss’ law: $\oint \vec{E} \cdot d\vec{A} = EA = \frac{Q_{enc}}{\epsilon_0}$
	$E = \frac{Q_{enc}}{A\epsilon_0}$
	$V = Ed = \frac{Q}{\frac{\epsilon_0 A}{d}} = \frac{Q}{C}$ for $C = \epsilon_0 \frac{A}{d}$ (parallel-plate capacitor)
	relative permittivity of dielectric
		$C = \epsilon \frac{A}{d} = \frac{\epsilon}{\epsilon_0} C_0$
	variable capacitors → changing capacitance by changing distance/plate area
	polarized capacitors → only work with one polarity (like diodes)
	sign convention for capacitors
		assume direction flows from higher to lower charge, voltage
	capacitors in series and parallel
		series: reciprocal of sum of reciprocal of component capacitors (common current)
		parallel: sum of component capacitors (common voltage)
RC circuits
	discharging
		$Q(t) = V_0Ce^{-\frac{t}{RC}} = Q_0e^{-\frac{t}{RC}}$
		$I(t) = -\frac{dQ}{dt} = \frac{Q_0}{RC}e^{-\frac{t}{RC}} = \frac{V_0}{R}e^{-\frac{t}{RC}} = I_0e^{-\frac{t}{RC}}$
	charging
		$Q(t) = V_0C(1-e^{-\frac{t}{RC}}) = Q_0(1-e^{-\frac{t}{RC}})$
		$I(t) = \frac{dQ}{dt} = \frac{Q_0}{RC}e^{-\frac{t}{RC}} = \frac{V_0}{R}e^{-\frac{t}{RC}} = I_0e^{-\frac{t}{RC}}$
	negative vs positive → direction of charge flow wrt current in charging
inductors
	ampere’s law: $\oint \vec{B} \cdot d\vec{l} = \mu_0I_{enc}$
	$B = \mu_0In$
	$\Phi = NBA = N(\mu_0\frac{N}{d}I)A = \mu_0N^2\frac{A}{d}I$
	faraday’s law: $\oint \vec{E} \cdot d\vec{l} = -\frac{d}{dt}\oint \vec{B} \cdot d\vec{A} = -\frac{d\Phi}{dt}$
	$-\Delta V = -\mu_0N^2\frac{A}{d} \frac{dI}{dt} = -L\frac{dI}{dt}$ for $L = \mu_0 N^2 \frac{A}{d}$
	relative permeability of magnetically permeable material
		$L = \frac{\mu}{\mu_0} L_0$
	variable inductors → changing inductance by inserting permeable rod or changing contact point
	sign convention for inductors
		assume direction flows from higher to lower voltage
	inductors in series and parallel
		series: sum of component inductors (common current)
		parallel: reciprocal of sum of reciprocal of component inductors (common voltage)
RL circuits
	$I(t) = \frac{V_0}{R}(1-e^{-\frac{t}{\frac{L}{R}}})$
power and energy
	$P = IV = I^2R = \frac{V^2}{R}$ (resistors)
	$E = \frac{1}{2}\frac{Q^2}{C} = \frac{1}{2}CV^2 = \frac{1}{2}QV$ (capacitors)
	$U = \frac{1}{2}LI^2$ (inductors)
conservation of energy
	energy delivered by voltage source = energy stored in capacitor + energy dissipated in resistor
LC circuits
	$Q(t) = CV_0\cos(\omega_0 t)$ for $\omega_0 = \frac{1}{\sqrt{LC}}$
	$V(t) = \frac{Q(t)}{C} = V_0\cos(\omega_0 t)$
	$I(t) = -\frac{dQ}{dt} = V_0 \sqrt{\frac{C}{L}}\sin(\omega_0 t)$
conservation of energy
	energy delivered by voltage source = energy stored in capacitor + energy stored in inductor
driven RLC circuits
	$V(t) = L\frac{d^2Q}{dt^2}+R\frac{dQ}{dt}+\frac{1}{C}Q$
	for constant $V(t)$:
		$Q(t) = CV_0 + h(t)$ where $h(t)$ is solution for non driven
	$V(t) = \operatorname{Re}(V_0e^{i\omega t})$ for $V_0 = |V_0|e^{i\phi_0}$, $Q(t)=\operatorname{Re}(Q_0e^{i\omega t})$ for $Q_0 = |Q_0|e^{i\delta}$, $I(t) = \operatorname{Re}(I_0e^{i\omega t})$
	$Z(\omega) = R+iX(\omega) - |Z(\omega)|e^{i\delta}$ for $|Z(\omega)| = \sqrt{R^2 + X^2}$ and $\delta = \tan^{-1}(\frac{X}{R})$
	$I(t) = \frac{V(t)}{Z(\omega)} = |\frac{V_0}{Z(\omega)}|e^{i((\omega t + \phi_0)-\delta)}$, $Z(\omega) = R(1+i(\tau_{RL}\omega_0)((\frac{\omega}{\omega_0})-(\frac{\omega_0}{\omega})))$
	resonant frequency $\omega_0 = \frac{1}{\sqrt{LC}}$
		if $\omega \ll \omega_0$
			$Z = R - i\infty$
			$-\delta = \frac{\pi}{2}$
			capacitor dominates
		if $\omega = \omega_0$
			$Z = R$
			$-\delta = 0$
			purely resistive
		if $\omega \gg \omega_0$
			$Z = R - i\infty$
			$-\delta = \frac{\pi}{2}$
			inductor dominates
	impedances behave like resistors
		$V = IZ$
		$Z_R = R$, $Z_C = \frac{1}{i\omega C}$, $Z_L = i\omega L$
		$P = |I_0|^2|Z|\cos(\omega t + \phi)\cos(\omega t + \phi + \delta)$, $\phi = 0$
		$P_R = \frac{1}{2}|I_0|^2R$, $P_C = 0$, $P_L = 0$
		series and parallel
		generalize voltage divider to impedances
	filters
		low-pass filter → below certain frequency
		high-pass filter → above certain frequency
		band-pass filter → between certain frequency
		band-stop filter → outside of certain frequency
		limitations of RC filters
	Q factor
		$Q = 2\pi\frac{energy~stored}{energy~lost} = \omega_0\frac{U}{\langle P_{loss}\rangle}$
		$Q = \frac{1}{R}\sqrt{\frac{L}{C}}$
		$Q = \frac{f_0}{f_{+3dB} - f_{-3dB}}$
	tank resonator
		$Q = R\sqrt{\frac{C}{L}}$
		$V = |V_0|e^{i\omega t}$
		$I = |\frac{V_0}{Z}|e^{i(\omega t-\delta)}$
		$P = \frac{|V_0|^2}{|Z|}\cos(\omega t)\cos(\omega t -\delta)$