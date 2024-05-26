# Taylor Methods
difference method
	$w_0 = \alpha, w_{i+1} = w_i + h\phi(t_i, w_i)$
	local truncation error $\tau_i = \frac{y_{i+1} - y_i}{h} - \phi(t_i, y_i)$
		$\tau_{i}(\Delta t) = M\Delta t^n$
		$\phi^{\Delta t}(t_i, w_i) = Lw_i$
	global truncation error $\frac{\hat{e}_i - \hat{e}_{i-1}}{\Delta t} = \tau_i(\Delta t) + \phi^{\Delta t}(t_{i-1}, y(t_{i-1})) - \phi^{\Delta t}(t_{i-1}, w_{i-1})$
order $n$ method
	[eulers](euler-s-method.md) is $n = 1$
	$w_0 = \alpha, w_{i+1} = hT^{(n)}(t_i, w_i)$
		$T^{(n)} = \sum_{i=0}^{n-1} \frac{h^i}{i!}f^{(i)}(t_i, w_i)$
	local truncation error $O(h^n)$
	