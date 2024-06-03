# Key Exchange
correctness: if $C = \mathcal{E}_K(M)$, then $\mathcal{D}_K(C) = M$
	decryption needs to give correct plaintext
## Diffie-Hellman Key Exchange
$A$ has $a$ and shares $\alpha$, $B$ has $b$ and shares $\beta$
$K = F_A(a, \alpha, \beta) = F_B(b, \alpha, \beta)$
ex $\mathrm{Z}_p^\times$ for prime $p$, fix generator $g$
	$a, b \twoheadleftarrow [1, \ldots, p - 1]$
	$\alpha = g^a, \beta = g^b$
	$K = \alpha^b = \beta^a = g^{ab}$
[security notion](security-notion.md)
## Multiparty Computation
mean salary
	consider mod $N$ for large $N$
	partition salary randomly, send part to all other parties