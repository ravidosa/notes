# IVP Theory
taylor's theorem
	approximation of nth order differentiable function with n degree polynomial (nth order taylor polynomial)
	see [Taylor Series](power-series.md#expanding-functions-in-power-series)
finite differences
	approximate derivative of function at point using points on function close to point
	$u'(x_0) \approx \frac{u(x_0 + h) - u(x_0 - h)}{2h} + O(h^2)$
	system of linear equations to solve for coefficients
		$\sum_i a_i = 0$, $\sum_i a_ii = 1$, $\sum_i a_i\frac{i^2}{2}= 0$
IVP
	solve differential equation given initial conditions
	lipschitz condition on subset $D$ of $\mathbb{R}^2$
		$|f(t,y_1)-f(t,y_2)|\leq L|y_1-y_2|$ for all $(t,y_1)$, $(t,y_2)$ in $D$, lipschitz constant $L$
		concavity
			convex if points on connecting line also in set
		if lipschitz satisfied, then unique solution
well-posed problems
	small changes in problem, small changes in solution
	unique solution exists
approximation
	equally spaced time steps with step size
	euler's method
		$y_{n+1}=y_n + hf(t_n,y_n)$
		local truncation error
			$\frac{y(t_{n+1}) - y(t_n)}{h} - f(t_n, y(t_n)) = \frac{h}{2}y''(\epsilon)$
			first order accurate (power of step size in truncation error)
	backwards euler
		in reverse, same order accuracy