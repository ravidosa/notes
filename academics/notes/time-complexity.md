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
	$f = \Theta(g)$ if $f = O(g), f = \Omega(g)$ (grow at same asymptotic rate)
remove constants, lower order terms, take logs
$1 < \log\log n < \log n < \sqrt{n} < n < n^c < 2^{n^\delta}$

| growth        | terminology     |
| ------------- | --------------- |
| $O(1)$        | constant        |
| $O(\log n)$   | logarithmic     |
| $O\log^k n)$  | polylogarithmic |
| $o(n)$        | sublinear       |
| $O(n)$        | linear          |
| $O(n\log n)$  | log-linear      |
| $O n\log^k n$ | polylog-linear  |
| $O(n^k)$      | polynomial      |
| $\Omega(n^k)$ | superpolynomial |
| $\Omega(a^n)$ | exponential     |

limit lemma
	$L = \lim_{n\to\infty} \frac{f(n)}{g(n)}$
	$L = 0$, $f(n) = O(g(n))$
	$L = \infty$, $f(n) = \Omega(g(n))$
	$L$ is nonzero finite, $f(n) = \Theta(g(n))$
### Divide and Conquer
divide problem into subproblems, solve subproblems recursively, combine to get solution
	merge sort, matrix multiplication, maximum subarray
substitution: guess form, verify by induction, solve for constants
recursion tree: height is number of divisions, number of steps at each level
master theorem
	$T(n) = aT(n/b) + f(n)$
	if $f(n) = O(n^{\log_b a - \epsilon})$ for $\epsilon > 0$, then $T(n) = \Theta(n^{\log_b a})$
	if $f(n) = \Theta(n^{\log_b a})$ for $\epsilon > 0$, then $T(n) = \Theta(n^{\log_b a} \log n)$
	if $f(n) = \Omega(n^{\log_b a + \epsilon})$ for $\epsilon > 0$ and $af(n/b) \leq cf(n)$ conr $c > 1$, then $T(n) = \Theta(f(n))$