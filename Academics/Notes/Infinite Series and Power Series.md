### Geometric Series
geometric series
	$S_n = \frac{a(1-r^n)}{1-r}$
	$S = \lim_{n \to \infty} S_n = \frac{a}{1-r}$
### Convergent and Divergent Series
convergence of series of positive terms
	$S = a_1 + a_2 + \ldots$
### Convergence Tests
preliminary test
	if $\lim_{n \to \infty} a_n \neq 0$, $S$ diverges
	otherwise, test further
comparison test
	if $|a_n| \leq m_n$ for converging $m$ series, $S$ converges
	if $|a_n| \geq d_n$ for diverging $d$ series, $S$ diverges
integral test
	if $0 < a_{n+1} \leq a_n$ for $n > N$, $\sum_N^\infty a_n$ converges if $\int^\infty a_n dn$ is finite, diverges if infinite
ratio test
	$\rho = \lim_{n \to \infty} |\frac{a_{n+1}}{a_n}|$
	if $\rho < 1$, $S$ converges
	if $\rho = 1$, use a different test
	if $\rho > 1$, $S$ diverges
special comparison test
	if $\sum_{n=1}^\infty b_n$ is convergent and positive terms and $a_n \geq 0$ and $\lim_{n \to \infty} \frac{a_n}{b_n}$ is finite, $\sum_{n=1}^\infty a_n$ converges
	if $\sum_{n=1}^\infty d_n$ is divergent and positive terms and $a_n \geq 0$ and $\lim_{n \to \infty} \frac{a_n}{d_n}$ is greater than 0 (or $\infty$), $\sum_{n=1}^\infty a_n$ diverges
### Absolute and Conditional Convergence
convergence of alternating series that does not converge absolutely
	$S = |a_1| - |a_2| + |a_3| + \ldots$
	$S_2 = |a_1| + |a_2| + |a_3| + \ldots$
	if $S_2$ converges, $S$ converges
	if $S_2$ diverges, $S$ converges (at least conditionally) if $a_n \to 0$ as $n \to \infty$ and $|a_{n+1}| < |a_n|$
### Power Series and Interval of Convergence
power series
	$S(x) = a_0 + a_1x + a_2x^2 + \ldots$
	radius of convergence
		$R = \lim_{n \to \infty} |\frac{a_{n+1}}{a_n}|x < 1$
		$x = \lim_{n \to \infty} |\frac{a_n}{a_{n+1}}|$
	test endpoint separately
	entire function converges everywhere
### Expanding Functions in Power Series
taylor series
	$f(x) = f(a) + f'(a)(x-a) + f''(a)\frac{(x-a)^2}{2!} + \ldots = \sum_{n=0}^\infty f^{(n)}(a)\frac{(x-a)^n}{n!}$
	$f(x,y)=f(0,0) + x\frac{\delta f}{\delta x}(0,0) + y\frac{\delta f}{\delta y}(0,0) + x^2\frac{\delta ^2f}{\delta x^2}(0,0) + 2xy\frac{\delta ^2f}{\delta x\delta y}(0,0) + y^2\frac{\delta ^2f}{\delta y^2}(0,0) + \ldots = \sum_{n=0}^\infty \frac{1}{n!}((x-a)\frac{\delta}{\delta x} + (y-b)\frac{\delta}{\delta y})^n f(a,b)$maclaurin series (taylor for $a=0$)
		$f(x) = f(0) + f'(0)x + f''(0)\frac{x^2}{2!} + \ldots = \sum_{n=0}^\infty f^{(n)}(0)\frac{x^n}{n!}$
#### Common Maclaurin series
| **Function**                                    | **Maclaurin series (series form)**                 | **Maclaurin series (polynomial form)**         |
| ----------------------------------------------- | -------------------------------------------------- | --------------------------------------------- |
| $\sin{x}$                                       | $\sum_{n=0}^\infty \frac{(-1)^nx^{2n+1}}{(2n+1)!}$ | $x - \frac{x^3}{3!} + \frac{x^5}{5!} - \ldots$  |
| $\cos x$ | $\sum_{n=0}^\infty \frac{(-1)^n x^{2n}}{(2n)!}$ | $1 - \frac{x^2}{2!} + \frac{x^4}{4!} + \ldots$     |
| $e^x$                                           | $\sum_{n=0}^\infty \frac{x^n}{n!}$                 | $1 + x + \frac{x^2}{2!} + \ldots$   |
| $\ln(1+x)$                                      | $\sum_{n=1}^\infty \frac{(-1)^{n+1}x^n}{n}$        | $x - \frac{x^2}{2} + \frac{x^3}{3} - \ldots$ |
| $(1+x)^p$ for real $p$, infinite for non-integral $p$ | $\sum_{n=0}^\infty {p \choose n}x^n$               | $1 + px + \frac{p(p-1)}{2!}x^2 + \ldots$ |                    

division
	valid if ratio finite as $x \to  0$