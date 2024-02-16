# Dirac Delta Function
generalization of [kronecker delta](kronecker-delta.md)
dirac delta function
	generalization of kronecker delta to continuous variable $\delta(x)$
	$\delta(x) \geq 0$
	$\int \delta(x-a) dx = 1$
	$\int f(x)\delta(x-a)=f(a)$
delta function
	$\lim_{\sigma \to 0} \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-a)^2}{2\sigma^2}} = \delta(x-a)$
	$\int_{-\infty}^\infty f(x)\delta(cx) dx = \frac{f(0)}{|c|}$
	$\int_{-\infty}^\infty f(x)\delta(cx+d)dx=\frac{f(-\frac{d}{c})}{|c|}$
	$\int_{-\infty}^\infty f(x)\delta((x-a)(x-b))dx = \frac{f(x-a)+f(x-b)}{|a-b|}$
	for function $g(x)$ with roots $x_i$, $\delta(g(x)) = \sum_i \frac{\delta(x-x_i)}{|g'(x_i)|}$, $\int_{\infty}^{\infty} f(x)\delta(g(x)) = \sum_i \frac{f(x_i)}{|g'(x_i)|}$
	$\int_{-\infty}^\infty f(x)\delta(x^2)dx = \lim_{x\to 0} \frac{f(x)}{|2x|}$
	$g(k) = \frac{1}{2\pi}\int_{-L}^Le^{ikx}dx = \frac{1}{\pi k}\sin{kL} = \delta(k)$ (goes to $\frac{L}{\pi}$ as $k \to 0$)
	$\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}f(x,y,z)\delta(x-x_0)\delta(y-y_0)\delta(z-z_0)dxdydz = f(x_0,y_0,z_0)$
heaviside theta function
	$\Theta(x'-a) = \int_{-\infty}^{x'}\delta(x-a)=0$ if $x'<a$, $1$ if $x'>a$
$\int\phi(x)\delta(x-a)dx = \phi(a)$
$\int_{-\infty}^\infty\phi(x)\delta'(x-a)dx = \phi(x) - \int_{-\infty}^{\infty}\phi'(x)\delta(x-a)dx = -\phi'(a)$
$\phi''(x-a)$→$\phi''(a)$