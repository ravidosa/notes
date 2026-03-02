# [Fourier Transform](https://en.wikipedia.org/wiki/Fourier_transform)
nonperiodic function
	limit of period to infinity
	[discrete](fourier-series.md) to continuous: $f(x) = \lim_{l\to \infty} \sum_{k_n = -\infty}^{\infty} c(k_n)e^{ik_nx} = \frac{2L}{2\pi}\int_{-\infty}^\infty c(k)e^{ikx}dk = \int_{-\infty}^\infty g(k)e^{ikx}dk$
		$k_n = \frac{2n\pi}{2l}$, $\frac{2\pi}{2l}g(k) = c(k) = \frac{1}{2l}\int_{-l}^l f(x)e^{\frac{-in\pi x}{l}}dx$
fourier transform
	$g(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty f(x)e^{-ikx}dx$
	$f(x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty g(k)e^{ikx} dk$
	transformations:
		$f(x - x_0)$, $g(k) \rightarrow e^{-ikx_0}g(k)$
		$f(ax)$, $g(k) \rightarrow \frac{g(k/a)}{|a|}$
		$f'(x)$, $g(k) \rightarrow ikg(k)$ and $g'(k)$, $f(x) \rightarrow ixf(x)$
			using fourier space can turn calculus into algebra (derivative turns into constant multiple), reduce pde to ode
width
	average: $x_0 = \frac{\int_{-\infty}^{\infty} x f(x) \, dx}{\int_{-\infty}^{\infty} f(x) \, dx}$
		complex/negative: $\bar{x} = \frac{\int_{-\infty}^{\infty} x f(x)f^*(x) \, dx}{\int_{-\infty}^{\infty} f(x)f^*(x) \, dx}=\frac{\braket{f|x|f}}{\braket{f|f}}$
	standard deviation (width): $\sqrt{\frac{\int_{-\infty}^{\infty} (x - x_0)^2 f(x) \, dx}{\int_{-\infty}^{\infty} f(x) \, dx}}$
		complex/negative: $\sqrt{\frac{\int_{-\infty}^{\infty} (x - x_0)^2 f(x)f^*(x) \, dx}{\int_{-\infty}^{\infty} f(x)f^*(x) \, dx}}=\sqrt{\frac{\braket{f|(x - x_0)^2|f}}{\braket{f|f}}}=\sqrt{\bar{x^2} - \bar{x}^2}$
	inverse widths in fourier space
	connects to [heisenberg uncertainty principle](heisenberg-uncertainty-principle.md)
[delta function](ordinary-differential-equations.md#dirac-delta-function)
	$g(k) = \int_{-\infty}^\infty g(k')dk'\delta(k-k')$, $\delta(k-k') = \frac{1}{2\pi}\int_{-\infty}^\infty e^{-i(k-k')x}dx$ with integrable, normalizable $f(x)$
convolution
	fourier transform of $f_3(x) = f_1(x)f_2(x)$ is $g_3(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} g(k')g_2(k-k') \, dk'$
	green function, response function, transfer function
	action at a distance, history dependence
feature comparison
	$x$ and $t$ vs $k$ and $w$
	$T$ vs $\frac{2\pi}{T}$
	finite length, time vs minimum $k$/$\omega$ width/minimum $x$/$t$ width, finite $k$, $\omega$ range
	size $a$ vs size $\frac{2\pi}{a}$
	check with discrete fourier transform (sample $t$, perform numerical exponential)
		amplitude spectrum and angular frequency spectrum