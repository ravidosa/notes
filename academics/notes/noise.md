# Noise
classes of noise
	characterized by frequency spectra
	white noise: $P(f)=\frac{dP}{df} \propto C$
	red noise: $P(f) \propto \frac{1}{f^2}$
	pink noise: $P(f) \propto \frac{1}{f}$
	pickup/oscillation: $P(f) \propto \delta(f)$
	johnson (nyquist) noise: thermal fluctuations in resistor, random
		$v^2(f)\Delta f=4k_BTR\Delta F$
	shot noise: discreteness of electrical charge in current, random statistical
	flicker noise: many causes, rises as $\frac{1}{f}$ at low frequencies
	burst noise: random jumps between levels, device defects
	filtered noise
		$V_{RMS}=\sqrt{\int_0^\infty v_n^2|g(f)|^2 df}$
		sensitive to frequencies outside range transmits more noise
	characterization of noise
		$v^2=v_n^2 + v_a^2 + v_s^2 + \ldots$
		add in quadratune
	signal to noise ratio
		$SNR=20\log_{10}\frac{v_s}{\sqrt{v_n^2 + v_a^2}}$ (signal power vs total noise power)
	noise figure
		$NF=10\log_{10}(1+\frac{v_a^2}{4k_BTR})$
	noise temperature
		temperature needed to generate same noise as amplifier
		$NF=10\log_{10}(1+\frac{T_n}{T})$