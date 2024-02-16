# Legendre Polynomials
legendre's equation: $(1-x^2)y''-2xy'+\ell(\ell+1)y=0$, $-1\leq x\leq 1$
	non singular solutions in interval, $x=\cos\theta$
	$a_{n+2}=-\frac{(\ell - n)(\ell + n + 1)}{(n + 2)(n + 1)}a_n$
	$y(x)=a_0(1 - \frac{\ell(\ell + 1)}{2!}x^2 + \frac{\ell(\ell + 1)(\ell - 2)(\ell + 3)}{4!}x^4 - \ldots) + a_1(x - \frac{(\ell-1)(\ell + 2)}{3!}x^3 + \frac{(\ell-1)(\ell + 2)(\ell - 3)(\ell + 4)}{5!}x^5 - \ldots)$converges for $|x|<1$
legendre polynomials
	set $a_1 = 0$ for even $\ell$, $a_0=0$ for odd $\ell$
	one non-singular solution in $[-1,1]$ for non negative $\ell$
	$P_\ell(x)$ for order $\ell$
	$P_\ell(1) = 1$ (normalization)
	$P_0(x) = 1$, $P_1(x) = x$, $P_2=-\frac{1}{2}(1-3x^2)$, …
	rodrigues formula → normalized legendre function
		$P_\ell(x)=\frac{1}{2^\ell \ell!}\frac{d^\ell}{dx^\ell}(x^2-1)^\ell$
	generating function
		$\Phi(x,h)=\sum_\ell^\infty h^\ell P_\ell(x)=\frac{1}{\sqrt{1-2xh+h^2}}$
	orthogonal on $(-1,1)$
		$\int_{-1}^1 P_\ell(x)P_m(x)dx=0$ ($\ell \neq m$)
	legendre series
		$f(x) = \sum_\ell c_\ell P_\ell(x)$
	recurrence relations
		$lP_l(x)=(2l - 1)xP_{l-1}(x)-(l-1)P_{l-2}(x)$
		$xP'_l(x)-P'_{l-1}(x)=lP_l(x)$
		$P'_l(x)-xP'_{l-1}(x)=lP_{l-1}(x)$
		$(1-x^2)P'_l(x)=lP_{l-1}(x)-lxP_l(x)$
		$(2l + 1)P_l(x)=P'_{l+1}(x)-P'_{l-1}(x)$
		$(1-x^2)P'_{l-1}(x)=lxP_{l-1}(x)-lP_l(x)$