# Fourier Series
countably infinite number of terms
functions for which all derivatives exist
for periodic functions in interval $[-\pi,\pi]$
	$f(x) = \frac{a_0}{2} + \sum_{n=1}^\infty a_n\cos(nx) + \sum_{n=1}^\infty b_n\sin(nx) = \sum_{-\infty}^\infty c_ne^{inx}$
$\sin(nx), \cos(nx)=e^{inx}$ complete set
orthogonality in vector space
	$\frac{1}{2\pi}\int_{-\pi}^\pi e^{-imx}e^{inx}dx = \delta_{m,n}$
	$\frac{1}{2\pi}\int_{-\pi}^\pi \sin{mx}\sin{nx}dx = \frac{1}{2}\delta_{m,n}$
	$\frac{1}{2\pi}\int_{-\pi}^\pi \cos{mx}\cos{nx}dx = \frac{1}{2}\delta_{m,n}$
fourier coefficients
	$a_n = \frac{1}{l}\int_{-l}^l f(x)\cos{\frac{n\pi x}{l}} dx$
	$b_n = \frac{1}{l}\int_{-l}^l f(x)\sin{\frac{n\pi x}{l}} dx$
	$c_n = \frac{1}{2l}\int_{-l}^l f(x)e^{-\frac{in\pi x}{l}} dx$
converges for all functions satisfying dirichlet condition
if odd, 0, if even, 2
	sin odd, cos even
not absolutely convergent bc discontinuities
	converges to mean of left and right limits
$f^*(x) = \sum_{-\infty}^\infty c_n^* e^{-inx} = \sum_{-\infty}^\infty c_{-n}^* e^{inx}$, $c_n = c_{-n}^*$ for real $f(x)$
for even and real $f(x)$, $c_n = c_{-n}$ with real $c_n$ and only cosines, for odd and real $f(x)$, $c_n = -c_{-n}$ and only sines
parseval’s theorem/completeness relation
	$\frac{1}{2l}\int_{-l}^l |f(x)|^2 dx = (\frac{1}{2}a_0)^2 + \frac{1}{2}\sum_1^\infty a_n^2 + \frac{1}{2}\sum_1^\infty b_n^2 = \sum_{-\infty}^\infty |c_n|^2$
representation of function in infinite dimension vector space