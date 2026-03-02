# Calculus of Variations
functional: function of a function
	ex: euler-lagrange equation
		see [lagrangian method](lagrangian-method.md)
		minimize $I[y] = \int_{x_0}^{x_1} F(x, y, y') \, dx$ ($y(x_0) = y_0, y(x_1) = x_1$)
		small wiggle $y = y + \epsilon\eta, y' = y' + \epsilon\eta'$
			$\frac{\partial F}{\partial y} = \frac{d}{dx}\frac{\partial F}{\partial y'}$
			$F = y'\frac{\partial F}{\partial y'} + C$ (bellremi's formula when $F(y, y')$)
	ex: brachistochrone
		minimize $I[y] = \int_{x_0}^{x_1} \sqrt{\frac{1 + (y')^2}{2g(y - y_0)}} \, dx$
	fundamental lemma
		if $\int_{x_0}^{x_1} G(x)\eta(x) \, dx = 0$ then $G(x) = 0$
constrained variational problems
	extrema of $I[y] = \int_{x_0}^{x_1} F(x, y, y') \, dx$ subject to usual conditions and constraint of form $J[y] = \int_{x_0}^{x_1} G(x, y, y') \, dx = C$
	lagrange multipliers
		$H(x, y, y') = F(x, y, y') + \lambda G(x, y, y')$, consider $K(y) = \int_{x_0}^{x_1}H(x, y, y') \, dx$
			same stationary functions, minimizers
	ex: isoperimetric
		maximize $I[y] = \int_{-1}^{1} y \, dx$, $J[y] = \int_{-1}^{1} \sqrt{1 + (y')^2} \, dx$