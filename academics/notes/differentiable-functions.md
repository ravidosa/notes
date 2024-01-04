# Differentiable Functions
derivative of $f$ at $c$
	$f'(c) = \lim_{h\to 0} \frac{f(c + h) - f(c)}{h} = \lim_{x\to c} \frac{f(x) - f(c)}{x - c}$
	differentiable where limit exists
	left/right derivatives
		$f'(c^+) = \lim_{h\to 0^+} \frac{f(c + h) - f(c)}{h}$ right, similar for left
	differentiable iff exists linear function $L(h) = Ah$ such that
		$\lim_{h\to 0} \frac{f(c + h) - f(c) - L(h)}{h} = 0$
		$f(c + h) = f(c) + L(h) + r(h)$ where $\lim_{h\to 0} \frac{r(h)}{h} = 0$