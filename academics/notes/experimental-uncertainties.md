# Experimental Uncertainties
report uncertainties w one sig digit, unless first digit is 1, then two
gaussian distribution
	use z-score to find probability of lying between sigmas
		$\mathrm{erf}(z) = \frac{1}{\pi} \int_{-z}^z e^{-t^2} \, dt$
common probabilities

| interval        | integrated probability |
| --------------- | ---------------------- |
| $\pm 1\sigma$   | $68.3\%$               |
| $\pm 1.5\sigma$ | $86.6\%$               |
| $\pm 2\sigma$   | $95.4\%$               |
| $\pm 3\sigma$   | $99.7\%$               |
| $\pm 5\sigma$   | $99.9\%$               |

propagation
	$\langle f(x) \rangle = \int f(x)P(x) \, dx$
	$\langle f(x,y) \rangle = \int\int f(x,y)P(x,y) \, dx \, dy$
		$\langle f(x,y) \rangle = \int\int f(x)P(x)P(y) \, dx \, dy$ for independent $x$ and $y$
	summation
		$\langle f(x) + g(y) \rangle = \langle f(x) \rangle + \langle g(y) \rangle$
		$\sigma^2(x+y) = \sigma^2(x) + \sigma^2(y)$, $\sigma(x+y) = \sqrt{\sigma^2(x) + \sigma^2(y)}$ for independent $x$ and $y$
	multiplication
		$\langle f(x) \cdot g(y) \rangle = \langle f(x) \rangle \cdot \langle g(y) \rangle$
		$\sigma(kx) = k\sigma_x$, $\mu_{kx} = k\mu_x$
		
	