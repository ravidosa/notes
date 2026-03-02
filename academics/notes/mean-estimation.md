# Mean Estimation
continuous case
	 prb 19.1: iid samples of distribution $\mathcal{D}$ over $\mathbb{R}$
		minimum number of samples$n$  needed to estimate true mean $\mu$ within additive error $\epsilon$ with probability at least $1 - \delta$
		rephrased: for fixed $n, \delta$, what is minimum $\epsilon$?
	assumptions about $\mathcal{D}$
		finite $\mu$, $\sigma^2$ (sample mean converges to gaussian by CLT, use as benchmark)
	find big $O$ optimal estimator with sharp constant
		median of means satisfies big $O$ but bad constant
		tight constant achieved in Lee and Valiant 2022
	gaussian mean estimation (special case)
		hardest estimation problem (easy algorithmically, difficult information-theoretically)
		samples from gaussian also gaussian with different variance
		upper bound
			fact 19.2: for $x > 1$, $\frac{1}{2x\sqrt{2\pi}}e^{-x^2/2} \leq P(\mathcal{N}(0, 1) > x) \leq \frac{1}{2}e^{-x^2/2}$\
				upper bound by drawing samples, taking mean
			prop 19.3: $n=2\frac{\sigma^2}{\epsilon^2}\log 1/\delta$ samples suffice
				$P(|\bar{x}_n - \mu| > \sigma\sqrt{\frac{2\log 1/\delta}{n}}) \leq \delta$
				prove with 19.2
		lower bound (applies to general case)
			cannot distinguish between $\mathcal{N}(0, \sigma^2)$ and $\mathcal{N}(2\epsilon, \sigma^2)$ with prob $1 - \delta$ with fewer than $n \leq (2 - o(1))\frac{\sigma^2}{\epsilon^2}\log 1/\delta$
			$n$-fold product, bound TV distance by neyman-pearson and rescale
			note 19.5: assuming finite variance, upper bound since moment finite
	optimal subgaussian performance (alg 19.6)
		take $n$ samples, compute median of means $\kappa$
		find solution $\alpha$ to $\sum_i \mathrm{min}(\alpha(x_i - \kappa)^2, 1) = \frac{1}{3}\log 1/\delta$
		$\hat{\mu} = \kappa + \frac{1}{n-\frac{1}{3}\log 1/\delta}\sum_i (x_i - \kappa)\mathrm{min}(1 - \mathrm{min}(\alpha(x_i - \chi)^2, 1))$
		thm 19.7: alg 19.6 outputs $\hat{\mu}$ with error at most $\sigma(1+o(1))\sqrt{\frac{2\log 1/\delta}{\eta}}$ with prob $1-\delta$
		