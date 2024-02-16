# Fourier Transform
$f(x) = \lim_{l\to \infty} \sum_{k_n = -\infty}^{\infty} c(k_n)e^{ik_nx} = \frac{2L}{2\pi}\int_{-\infty}^\infty c(k)e^{ikx}dk = \int_{-\infty}^\infty g(k)e^{ikx}dk$ for $k_n = \frac{2n\pi}{2l}$, $\frac{2\pi}{2l}g(k) = c(k) = \frac{1}{2l}\int_{-l}^l f(x)e^{\frac{-in\pi x}{l}}dx$
$g(k) = \frac{1}{2\pi}\int_{-\infty}^\infty f(x)e^{-ikx}dx$
$f(x) = \int_{-\infty}^\infty g(k)e^{ikx} dk$
$g(k) = \int_{-\infty}^\infty g(k')dk'\delta(k-k')$, $\delta(k-k') = \frac{1}{2\pi}\int_{-\infty}^\infty e^{-i(k-k')x}dx$ with integrable, normalizable $f(x)$