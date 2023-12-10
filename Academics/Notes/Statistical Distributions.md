data vs prediction
normalization: total probability is 1
probability distribution density function (PDF): $P()$
probability distributions
	binomial (2 options)
		$P(m,n,\epsilon) = {n \choose m} \epsilon^m (1 - \epsilon)^{n-m}$
		$\bar{m} = n\epsilon$
		$\sigma^2 = n\epsilon(1 - \epsilon)$
	poisson (counting)
		$\epsilon = \frac{\lambda}{n}$
		$P(m,\lambda) = {n \choose m}(\frac{\lambda}{n})^m(1 - \frac{\lambda}{n})^{n-m}$, $\lim_{n\to\infty}P(m,\lambda) = \frac{\lambda^m}{m!}e^{-\lambda}$
		$\bar{m} = \lambda$
		$\sigma^2 = \lambda$
	gaussian/normal
		$P(x,\mu,\sigma) = \frac{1}{\sqrt{2pi}\sigma}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$
			probability to lie in certain range
			special case (countaing gaussian)
				poisson as $\lambda\to\infty$, $m\to\infty$
				$P(x,\lambda) = \frac{1}{2\pi\lambda}e^{-\frac{(x-\lambda)^2}{2\lambda}}$