# Fourier Transforms and Convolutions
see [Fourier Series and Transforms](fourier-series-transforms.md)
discrete transformations
	express periodic function as sum of infinite series of sines and cosines
	$f(t+T) = f(t) = \sum_{n=0}^\infty C_n\cos(n\omega_0t+\delta_n)$ for fundamental frequency $\omega_0 = 2\pi, f_0 = 2\pi\frac{1}{T}$, period $T$
	$f(t) = a_0 + \sum_{n=1}^\infty a_n\cos(n\omega_0t)+b_n\sin(n\omega_0t)$
	$a_0 = \frac{1}{T}\int_0^Tf(t)dt$, $a_n = \frac{2}{T}\int_0^T f(t)\cos(n\omega_0t)dt$
	$b_n = \frac{2}{T}\int_0^T f(t)\sin(n\omega_0t)dt$
	complex representation
		$a_n\cos{\omega_nt}+b_n\sin{\omega_nt} = c_ne^{i\omega_nt} + c_{-n}e^{i\omega_{-n}t}$
		if real, then $\bar{c_n} = c_n^*$
continuous transformations (ignoring normalization)
	as $T \to \infty$, $\Delta\omega \to 0$
	$\tilde{f}(\omega) = \int_{-\infty}^\infty f(t)e^{-i\omega t}dt$
	$f(t) = \int_{-\infty}^\infty \tilde{f}(\omega)e^{i\omega t}dt$
	time domain and frequency domain
decibel scale
	$dB = 10\log_{10}(\frac{P_{out}}{P_{in}}) = 20\log_{10}(\frac{V_{out}}{V_{in}})$
	$0 dB = 10^{-12} W/m^2$, $120dB = 1W/m^2$
	filters
		characteristic frequency (power halved)
			$dB = 10\log_{10}(\frac{1}{2}) = -3dB$
power
	$P \propto \langle v^2 \rangle$
	$\langle v^2(t) \rangle = \langle \sum_{n=-\infty}^\infty (c_ne^{i\omega_n t})^2 \rangle = \sum_{n=0}^\infty |s_n|^2$
time invariant linear systems
	$h(t) = g(f(t))$
	$h(kf(t)) = kg(f(t))$
	$f(f_1(t)+f_2(t)) = g(f_1(t))+g(f_2(t))$
	only multiplication, differentiation, integration
	convolution
		$f(t) = \delta(t)$
		$h(t) = g(t)$
		if linear
			$f(t) = a_0\delta(t-t_0)+b_0\delta(t-t_1)$
			$h(t) = a_0g(t-t_0)+b_0g(t-t_1)$
		$h(t) = \int_{-\infty}^t f(\tau)g(t-\tau)d\tau = f(t) * g(t)$
		$\tilde{h}(\omega) = \tilde{f}(\omega)\tilde{g}(\omega)$
	point by point multiplication of spectral content of input and circuit
	enhance/reduce, but no new components
	filter: select certain range, reject others
	order does not matter in sequential