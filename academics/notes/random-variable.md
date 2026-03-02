# Random Variable
random variable: real valued function from $\Omega$ to $\mathbb{R}$
## Discrete
expectation: $E[X] = \sum_i x_ip(x_i)$
	$E[g(X)] = \sum_i g(x_i)p(x_i)$
variance $\mathrm{Var}[X] = E[X^2] - (E[X])^2$
uniform random variable
	$P(A_i) = \frac{1}{n}$
	$E[X] = \frac{1}{n}\sum_i x_i$
	$\mathrm{Var}[X] = (\frac{1}{n}\sum_i x_i)^2$
bernoulli (indicator) random variable
	$I_A$ is $1$ if $A$ happens (probability $p$)
	$E[I_A] = p$
	$\mathrm{Var}[I_A] = p(1 - p)$
binomial random variable
	number of successes (probability $p$) in $n$ independent trials
	$P(X = i) = {n \choose i}p^i(1-p)^{n-i}$
	$E[X] = np$
	$\mathrm{Var}[X] = np(1 - p)$
	indicator trick: write rv as sum of (maybe dependent) indicator rvs
poisson random variable (parameter $\lambda$)
	$P(X = i) = \frac{\lambda^ie^{-\lambda}}{i!}$
	$E[X] = \lambda$
	$\mathrm{Var}[X] = \lambda$
	approximates binomial for large $n$, small $p$ with $\lambda = np$
		error bounded by $p\mathrm{min}(1, \lambda)$
geometric
	number of trials until success
	$P(X = n) = p(1 - p)^{n-1}$
	$E[X] = \frac{1}{p}$
	$\mathrm{Var}[X] = \frac{1 - p}{p^2}$
	$P(X > n) = (1 - p)^n$
	memoryless
## Continuous
continuous: $P(X \in B) = \int_B f(x) \, dx$
	density function: $f = f_X$
	distribution function: $F = P(X \leq x) = \int_{-\infty}^x f(s) \, ds$
		$F'(x) = f(x)$
expectation: $E[X] = \int_{-\infty}^{\infty} xf(x) \, dx$
	$E[g(X)] = \int_{-\infty}^{\infty} g(x)f(x) \, dx$
variance same as discrete
uniform random variable from $\alpha$ to $\beta$
	$f(x) = \begin{cases} \frac{1}{\beta - \alpha} & x \in [\alpha, \beta] \\ 0 & \text{otherwise}\end{cases}$
	$E[X] = \frac{\alpha + \beta}{2}$
	$\mathrm{Var}[X] = \frac{(\beta - \alpha)^2}{12}$
exponential random variable
	$f(x) = \begin{cases} \lambda e^{-\lambda x} & x \geq 0\\ 0 & \text{otherwise}\end{cases}$
	$E[X] = \frac{1}{\lambda}$
	$\mathrm{Var}[X] = \frac{1}{\lambda^2}$
	$P(X \geq x) = e^{-\lambda x}$
	memoryless
normal random variable (mean $\mu$, std $\sigma$)
	$f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-(x - \mu)^2/2\sigma^2}$
	$E[X] = \mu$
	$\mathrm{Var}[X] = \sigma^2$
	standard normal: $Z = \frac{X - \mu}{\sigma}$
	central limit theorem
		normal is close to binomial for large $n$
	probability to lie in certain range
		special case (countaing gaussian)
			poisson as $\lambda\to\infty$, $m\to\infty$
			$P(x,\lambda) = \frac{1}{2\pi\lambda}e^{-\frac{(x-\lambda)^2}{2\lambda}}$
## Joint Distribution
joint probability mass function $p(x, y) = P(X = x, Y = y)$
	$E[g(X, Y)] = \sum_{x,y} g(x, y)p(x, y)$
	$P(X = x), P(Y = y)$ marginal pmf
	independent if $P(X = x, Y = y) = P(X = x)P(Y = y)$
	conditional: $p_X(x|Y = y) = \frac{P(X = x, Y = y)}{P(Y = y)}$
	$E[X] = \sum_y E[X|Y =  y]P(Y = y)$
jointly continuous $P((X, Y) \in S) = \iint_S f(x, y) \, dx\, dy$
	$E[g(X, Y)] = \iint g(x, y)f(x, y) \, dx \, dy$
	marginal $f_X = \int_{-\infty}^{\infty} f(x, y) \, dy, f_Y = \int_{-\infty}^{\infty} f(x, y) \, dx$
	independent if $f(x, y) = f_X(x)f_Y(y)$
	conditional: $f_X(x|Y = y) = \frac{f(x, y)}{f_Y(y)}$
	$E[X] = \int_{-\infty}^{\infty} E[X|Y=y]f_Y(y) \, dy$
iid with random $N$ terms
	$E[\sum_i^N X_i] = \mu E[N]$
	$\mathrm{Var}[\sum_i^N X_i] = \sigma^2E[N] + \mu^2\mathrm{Var}[N]$
## Moment Generating Functions
$\phi_X(t) = E[e^{tX}] = \sum_x e^{tx}P(X = x)$ for discrete
$\int_{-\infty}^{\infty} f_X(x)e^{tx} \, dx$ for continuous
only meaningful if integral/sum converges
$\phi_{\sum_i X_i}(t) = \prod_i \phi_{X_i}(t)$ if independent
large deviation bound
	$P(\sum_i X_i \geq an) \leq e^{-nI(a)}$
	$I(a) = \sup\{at - \log \phi(t)\} > 0$
if moments equal, CDF equal
if moment converges, then CDF converges if continuous
## Limit Theorems
expectation linear, monotonic
	$E[aX + b] = aE[X] + b$
	$E[\sum_i X_i] = \sum_i E[X_i]$
	$X \leq Y$, then $E[X] \leq E[Y]$
multiplicativity of expectation (independent rv)
	$E[g(X)h(Y)] = E[g(X)]E[h(Y)]$
conditional expectation
	$E[Y|X = x] = \sum_y yP(Y = y|X = x)$ for discrete
	$\int_y yf_Y(y|X = x)$ for continuous
tower property
	$E[Y] = \sum_x E[Y|X = x]P(X = x)$ for discrete
	$E[Y] = \int E[Y|X = x]f_X(x) \, dx$ for continuous
covariance
	$\mathrm{Cov}(X, Y) = E[XY] - E[X]E[Y]$
		zero if independent
	variance-covariance (no ind assumption)
		$E[(\sum_i X_i)^2] = \sum_i E[X_i] + \sum_{i\neq j} E[X_iX_j]$
		$\mathrm{Var}[\sum_i X_i] = \sum_i \mathrm{Var}[X_i] + \sum_{i\neq j}\mathrm{Cov}[X_i, X_j]$
		for independent rv, variances add
weak law of large numbers: mean of iid rv (finite expectation, variance) samples tends to expectation as sample size grows
	$\frac{\sum_i X_i}{n} \to \mu$ in probability
central limit theorem: shape of distribution tends to standard normal as sample size grows
	moment version: $T_n = \frac{\sum_i X_i - n\mu}{\sigma\sqrt{n}}$
		$P(T_n \leq x) \to P(Z \leq x)$ (standard normal $Z$)
		$\phi_{T_n}(t) = e^{t^2/2}$