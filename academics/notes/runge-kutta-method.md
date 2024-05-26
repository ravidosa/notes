# Runge-Kutta Methods
high-order local truncation error without derivatives
$f(t, y)$ as taylor polynomial in two variables (see [Taylor Series](power-series.md#expanding-functions-in-power-series))
order two (local truncation error $O(h^2)$)
	$a_1f(t + \alpha_1, y + \beta_1) \approx T^{(2)}(t, y) = f(t, y) + \frac{h}{2}f'(t, y)$
	$a_1 = 1, \alpha_1 = \frac{h}{2}, \beta_1 = \frac{h}{2}f(t, y)$ (midpoint method)
	modified euler
		$w_0 = \alpha, w_{i+1} = w_i + \frac{h}{2}(f(t_i, w_i) + f(t_{i+1}, w_i + hf(t_i, w_i)))$
order three
	heun's method
order four
	$k_1 = hf(t_i, w_i), k_2 = hf(t_i + \frac{h}{2}, w_i + \frac{k_1}{2}), k_3 = hf(t_i + \frac{h}{2}, w_i + \frac{k_2}{2}), k_4 = hf(t_{i+1}, w_i + k_3)$
	$w_{i+1} = w_i + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)$
local truncation error $O(n^k)$ where $k = \begin{cases}m & 2 \leq m \leq 4 \\ m - 1 & 5 \leq m \leq 7 \\ m - 2 & 8 \leq m \leq 9 \\ m - 3 & 10 \leq m\end{cases}$ where $m$ is number of evaluations per step