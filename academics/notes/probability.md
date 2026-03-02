# Probability
$P(E) = \frac{m}{n}$ (good outcomes $m$, all outcomes $n$)
probability space $(\Omega, \mathcal{F}, P)$
	sample space $\Omega$
	events $\mathcal{F}$
		subsets of $\Omega$
	probability $P$
		$P(A) \geq 0$, $P(\Omega) = 1$
		if pairwise disjoint, $P(\bigcup_i A_i) = \sum_i P(A_i)$
		$P(\emptyset) = 0$
		$P(A^c) = 1 - P(A)$
inclusion exclusion formula
	$P(\bigcup_i^n A_i) = \sum_{k=1}^n (-1)^{k+1} \sum_{1\leq i_1<\ldots<i_k\leq n} P(\bigcap_{j=1}^k A_{i_j})$
	birthday problem: $\sqrt{n}$
	coupon collector: $\frac{n!}{n^k}S_{k,n}$
conditional probability
	$P(A|B) = \frac{P(A \cap B)}{P(B)}$
	bayes formula: $P(A) = \sum_i P(F_i)P(A|F_i)$ (pairwise disjoint $F_i$ where $\bigcup_i F_i = \Omega$)
		second bayes formula: $P(F_j|A) = \frac{P(A|F_j)P(F_j)}{\sum_i P(F_i)P(A|F_i)}$
independence
	$P(A \cap B) = P(A)P(B)$ or $P(A|B) =  P(A)$
	bernoulli
		$n$ trials with success probability $p$, $P(k\text{  successes}) = {n \choose k}p^k(1-p)^{n-k}$
		