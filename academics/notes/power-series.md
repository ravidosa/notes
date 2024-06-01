# Power Series
power series
	$S(x) = a_0 + a_1x + a_2x^2 + \ldots$
	radius of convergence
		$R = \lim_{n \to \infty} |\frac{a_{n+1}}{a_n}|x < 1$
		$x = \lim_{n \to \infty} |\frac{a_n}{a_{n+1}}|$
	test endpoint separately
	entire function converges everywhere
same for complex
## Operations
addition/subtraction standard
multiplication
	term by term
division
	valid if ratio finite as $x \to  0$
## Taylor Series
taylor series
	$f(x) = f(a) + f'(a)(x-a) + f''(a)\frac{(x-a)^2}{2!} + \ldots = \sum_{n=0}^\infty f^{(n)}(a)\frac{(x-a)^n}{n!}$
	$f(x,y)=f(0,0) + x\frac{\delta f}{\delta x}(0,0) + y\frac{\delta f}{\delta y}(0,0) + x^2\frac{\delta ^2f}{\delta x^2}(0,0) + 2xy\frac{\delta ^2f}{\delta x\delta y}(0,0) + y^2\frac{\delta ^2f}{\delta y^2}(0,0) + \ldots = \sum_{n=0}^\infty \frac{1}{n!}((x-a)\frac{\delta}{\delta x} + (y-b)\frac{\delta}{\delta y})^n f(a,b)$maclaurin series (taylor for $a=0$)
		$f(x) = f(0) + f'(0)x + f''(0)\frac{x^2}{2!} + \ldots = \sum_{n=0}^\infty f^{(n)}(0)\frac{x^n}{n!}$
### Common Maclaurin Series
| **Function**                                          | **Maclaurin series (series form)**                 | **Maclaurin series (polynomial form)**         |
| ----------------------------------------------------- | -------------------------------------------------- | ---------------------------------------------- |
| $\sin{x}$                                             | $\sum_{n=0}^\infty \frac{(-1)^nx^{2n+1}}{(2n+1)!}$ | $x - \frac{x^3}{3!} + \frac{x^5}{5!} - \ldots$ |
| $\cos x$                                              | $\sum_{n=0}^\infty \frac{(-1)^n x^{2n}}{(2n)!}$    | $1 - \frac{x^2}{2!} + \frac{x^4}{4!} + \ldots$ |
| $e^x$                                                 | $\sum_{n=0}^\infty \frac{x^n}{n!}$                 | $1 + x + \frac{x^2}{2!} + \ldots$              |
| $\ln(1+x)$                                            | $\sum_{n=1}^\infty \frac{(-1)^{n+1}x^n}{n}$        | $x - \frac{x^2}{2} + \frac{x^3}{3} - \ldots$   |
| $(1+x)^p$ for real $p$, infinite for non-integral $p$ | $\sum_{n=0}^\infty {p \choose n}x^n$               | $1 + px + \frac{p(p-1)}{2!}x^2 + \ldots$       |