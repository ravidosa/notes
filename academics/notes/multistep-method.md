# Multistep Methods
characteristic polynomial based on $m$ approximations
	$w_{i + 1} = \sum_{j=0}^{m-1} a_{m-j-1}w_{i-j} + h(\sum_{k=0}^{m}b_{m-0}f(t_{i+1-k}, w_{i+1-k}))$
	explicit/open when $b_m = 0$ (only in previously determined values)
	implicit more stable
adams-bashforth (explicit)
	two-step (lte $O(h^2)$)
		$w_0 = \alpha, w_1 = \alpha_1$
		$w_{i+1} = w_i + \frac{h}{2}(3f(t_i, w_i) - f(t_{i-1}, w_{i-1}))$
	three-step (lte $O(h^3)$)
		$w_0 = \alpha, w_1 = \alpha_1, w_2 = \alpha_2$
		$w_{i+1} = w_i + \frac{h}{12}(23f(t_i, w_i) - 16f(t_{i-1}, w_{i-1}) + 5f(t_{i-2}, w_{i-2}))$
	four-step (lte $O(h^4)$)
		$w_0 = \alpha, w_1 = \alpha_1, w_2 = \alpha_2, w_3 = \alpha_3$
		$w_{i+1} = w_i + \frac{h}{24}(55f(t_i, w_i) - 59f(t_{i-1}, w_{i-1}) + 37f(t_{i-1}, w_{i-2}) - 9f(t_{i-3}, w_{i-3}))$
	five-step (lte $O(h^5)$)
		$w_0 = \alpha, w_1 = \alpha_1, w_2 = \alpha_2, w_3 = \alpha_3, w_4 = \alpha_4$
		$w_{i+1} = w_i + \frac{h}{720}(1901f(t_i, w_i) - 2774f(t_{i-1}, w_{i-1}) + 2616f(t_{i-1}, w_{i-2}) - 1274f(t_{i-3}, w_{i-3}) + 251f(t_{i-4}, w_{i-4}))$
	error
		$|y(t_i) - w_i| \leq \sum_{n=0}^{m-1} |y(t_i) - w_i| + \mathrm{max}_n |\tau_{n+1}(\Delta t)|$
		$\tau_{n+1}(\Delta t) = \frac{y^{(m + 1)}(]mu_n)}{m!}\int_0^1 \prod_{j=1}^m (\hat{s} - j + 1) \, d\hat{s}$
 adams-moulton (implicit)
	 two-step (lte $O(h^3)$)
		 $w_0 = \alpha, w_1 = \alpha_1$
		 $w_{i+1} = w_i + \frac{h}{12}(5f(t_{i+1}, w_{i+1}) + 8f(t_i, w_i) - f(t_{i-1}, w_{i-1}))$
	 three-step (lte $O(h^4)$)
		$w_0 = \alpha, w_1 = \alpha_1, w_2 = \alpha_2$
		$w_{i+1} = w_i + \frac{h}{24}(9f(t_{i+1}, w_{i+1}) + 19f(t_i, w_i) - 5f(t_{i-1}, w_{i-1}) + f(t_{i-1}, w_{i-2}))$
	four-step (lte $O(h^5)$)
		$w_0 = \alpha, w_1 = \alpha_1, w_2 = \alpha_2, w_3 = \alpha_3$
		$w_{i+1} = w_i + \frac{h}{720}(251f(t_{i+1}, w_{i+1}) + 646f(t_i, w_i) - 264f(t_{i-1}, w_{i-1}) + 106f(t_{i-1}, w_{i-2}) - 19f(t_{i-3}, w_{i-3}))$
predictor-corrector methods
	use explicit to predict, then implicit to correct