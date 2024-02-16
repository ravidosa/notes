# Infinite Series
geometric series
	$S_n = \frac{a(1-r^n)}{1-r}$
	$S = \lim_{n \to \infty} S_n = \frac{a}{1-r}$
## Convergence
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