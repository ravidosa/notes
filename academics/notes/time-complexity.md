# Time Complexity
running time: number of steps as a function of input size
time bound $t(n)$ for worst case
$TIME(t)$: languages with TM deciding in running time $O(t)$ 
time hierarchy theorem: if $t_1(n)\log t_1(n) = o(t_2(n))$, $TIME(t_1) \subsetneq TIME(t_2)$
	with more time, more problems solvable
multitape TM is equivalent to single tape within polynomial factor
## Asymptotic Analysis
asymptotic upper bound $O(f), o(f)$
	$f = O(g)$ if $f(n) \leq c \cdot g(n)$ for constant $c$ ($\Omega$ for opposite)
	$f = o(g)$ if $\lim_{n\to\infty} \frac{f(n)}{g(n)} = 0$ ($\omega$ for opposite)
	$f = \Theta(g)$ if $f = O(g), f = \Omega(g)$ (grow at same aymptotic rate)
remove constants, lower order terms, take logs
$1 < \log\log n < \log n < \sqrt{n} < n < n^c < 2^{n^\delta}$
