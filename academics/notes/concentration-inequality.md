# [Concentration Inequality](https://en.wikipedia.org/wiki/Concentration_inequality)
for large $n$, behaves like function
sequence converges to $a$ in probability if $P(|X_i - a) \leq \epsilon|) \to 1$ for fixed $\epsilon > 0$
	if $E[X_n] \to a$ and $\mathrm{Var}(X_n) \to 0$, $X_i \to a$ as $n\to\infty$
aggregate behavior of independent random processes is well behaved
$n$ independent samples from reals $X_i$
	LLN: sample mean converges to true mean
	CLT: sample mean distribution converges to [gaussian](random-variable.md#continuous) $\mathcal{N}(\mu, \sigma^2/n)$
concentration inequality/tail bound: upper bound on deviation of sample mean from true mean
## Markov's Inequality
$\mathrm{Pr}(Y \geq a) \leq \frac{\mathbb{E}(Y)}{a}$ for nonnegative random $Y$
## Chebyshev's Inequality
$\mathrm{Pr}(|Y - \mu| \geq a) \leq \frac{\sigma^2}{a}$ for random $Y$
	$\mathrm{Pr}(|\bar{x}_n - \mu| \geq \epsilon) \leq \frac{\sigma^2}{n\epsilon}$
	extend to higher order moment
		$\mathrm{Pr}(|Y - \mu| \geq a) \leq \frac{\mathbb{E}(|Y - \mu|^k)}{a^k}$
		optimal: $\mathrm{Pr}(|Y - \mu| \geq a) \leq \mathrm{min}_k\frac{\mathbb{E}(|Y - \mu|^k)}{a^k}$
## Chernoff Bounds
[moment generating function](https://en.wikipedia.org/wiki/Moment-generating_function): $M_Y(t) = \mathbb{E}(e^{tY}) =\sum_{i=0}^\infty \frac{t^i\mathbb{E}(Y^i)}{i!}$
	$\mathrm{Pr}(Y \geq b) \leq \mathrm{inf}_t \frac{\mathbb{E}(e^{tY})}{e^{tb}}$
	$\mathrm{Pr}(\bar{x}_n \geq \mu + \epsilon) \leq \mathrm{inf}_t \frac{\mathbb{E}(e^{t\bar{x}_n})}{e^{\bar{x}_n(\mu + \epsilon)}}$
poisson trials chernoff bounds
	$X_i$ bernoulli coin with bias $p_i$, independent
	$X = \sum_i X_i$, $\mu =\sum_i p_i$
	$\mathrm{Pr}(X \geq (1 + \delta)\mu) \leq (\frac{e^\delta}{(1 + \delta)^{1 + \delta}})^\mu \leq e^{-\mu\delta^2/3}$
		proof summary: moment generating function, apply chernoff bound, compute infinum (wolfram alpha)
	lower bound
		for any $\kappa \in (0, 1)$
			$\mathrm{Pr}(x \leq (1 - \kappa)\mu) \leq (\frac{e^{-\kappa}}{(1 - \kappa)^{1 - \kappa}})^\mu \leq e^{-\mu\kappa^2/2}$
		if only $\mu_+ \geq \mu$ known, applies with $+\kappa$ and $\mu_+$ (coupling argument)
	application
		decision algorithm $\mathcal{A}$ succeeds with prob $2/3$
		for $\mathcal{A}'$ to succeed up to $\delta$, run $n$ times and majority vote ($n \geq \Theta(\log 1/\delta))$
		algorithm $\mathcal{B}$ outputs $* \pm \epsilon$ with prob 2/3
		for $\mathcal{B}'$ to succeed up to $\delta$, run $n$ times and median ($n \geq \Theta(\log 1/\delta))$
		heuristic: query complexity $q(\delta)$, aim for $q(\delta) \leq O(q(1/3) \log 1/\delta)$