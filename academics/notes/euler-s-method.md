# Euler's Method
$y_{n+1}=y_n + hf(t_n,y_n)$
local truncation error
	$\frac{y(t_{n+1}) - y(t_n)}{h} - f(t_n, y(t_n)) = \frac{h}{2}y''(\epsilon)$
	first order accurate (power of step size in truncation error)
backwards euler
in reverse, same order accuracy
## Algorithm
approximate solution of $y' = f(t, y)$ for $a \leq t \leq b, y(a) = \alpha$ using $N + 1$ evenly spaced numbers in $[a, b]$ using euler's method
input
	endpoints $a, b$
	steps $N$
	initial condition $\alpha$
```
h = (b - a) / N
t, w = a, alpha
output(t, w)
for i in 1, ..., N:
	w = w + h * f(t, w)
	t = a + i * h
	output(t, w)

```
## Error Bound
satisfies lipschitz with lipschitz constant $L$, $|y''(t)| \leq M$
	$|y(t_i) - w_i| \leq \frac{hM}{2L}(e^{t_i-a} - 1)$
local truncation error $O(h)$
