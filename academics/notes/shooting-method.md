# Shooting Method
see [BVP Theory](ordinary-differential-equations.md#bvp-theory)
## Linear Shooting
linear when $y'' = f(x, y, y') = p(x)y' + q(x)y + r(x)$
endpoint conditions $t(a) = \alpha, y(b) = \beta$
replace with IVPs
	$y'' = p(x)y' + q(x)y + r(x), y(a) = \alpha, y'(a) = 0$
	$y'' = p(x)y' + q(x)y, y(a) = 0, y'(a) = 1$
	solve with IVP methods
## Nonlinear Shooting
solve sequence of IVPs by varying $t$ until $y(b) \approx \beta$
	$y'' = f(x, y, y'), y(a) = \alpha, y'(a) = t$
newton iteration
	$y''(x, t) = f(x, y(x, t), y'(x, t)), y(a, t) = \alpha, y'(a, t) = t$
	$z''(x, t) = \frac{\partial f}{\partial y}(x, y, y')z(x, t) + \frac{\partial f}{\partial y'}z'(x, t), z(a, t) = 0, z'(a, t) = 1$
	$t_k = t_{k-1} - \frac{y(b, t_{k-1}) - \beta}{\frac{dy}{dt}(b, t_{k-1})}$
	