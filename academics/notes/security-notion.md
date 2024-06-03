# Security Notion
advantage of adversary
	between 0 and 1 (1 good, 0 bad)
prove security notions equivalent/stronger through reduction
	if breaking A breaks B, A stronger than B
	reasonable (polytime) adversary
	hybrid argument
		one way to random point, other way past that point (triangle inequality)
perfect privacy/LR security
	$\mathrm{Pr}[C = C_0 | M - M_0] = \mathrm{Pr}[C = C_0 | M = M_1]$
	$L(\cdot, \cdot)$ encrypts left input, $R(\cdot, \cdot)$ encrypt right input
	$\mathrm{Adv}_{\pi}^{lr}(\mathcal{A}) = \mathrm{Pr}[\mathcal{A}^{L(\cdot,\cdot)} \to 1] - \mathrm{Pr}[\mathcal{A}^{R(\cdot,\cdot)} \to 1]$
		perfect privacy if $0$ advantage
	can't tell which input encrypted
```
algorithm L(M0, M1): # left oracle
	if |M0| != |M1| then return None
	if undef(K) then K = K(l)
	C = E(K, M0)
	return C
	
algorithm R(M0, M1): # right oracle
	if |M0| != |M1| then return None
	if undef(K) then K = K(l)
	C = E(K, M1)
	return C
```
ind0 security
	$\mathrm{Adv}_{\pi}^{ind0}(\mathcal{A}) = \mathrm{Pr}[\mathcal{A}^{\mathcal{E}_K(\cdot)} \to 1] - \mathrm{Pr}[\mathcal{A}^{\mathcal{E}_K(0^{|\cdot|})} \to 1]$ (symmetric)
	$\mathrm{Adv}_{\pi}^{ind}(\mathcal{A}, \mathcal{K}) = \mathrm{Pr}[(pk, sk) \twoheadleftarrow \mathcal{K}(k) : \mathcal{A}^{\mathcal{E}_{pk}(\cdot)} \to 1] - \mathrm{Pr}[(pk, sk) \twoheadleftarrow \mathcal{K}(k) : \mathcal{A}^{\mathcal{E}_{pk}(0^{|\cdot|})} \to 1]$
	can't tell if input or zeros encrypted
ind enc$ security
	$\mathrm{Adv}_{\pi}^{ind~enc\$}(\mathcal{A}) = \mathrm{Pr}[\mathcal{A}^{\mathcal{E}_K(\cdot)} \to 1] - \mathrm{Pr}[\mathcal{A}^{\mathcal{E}_K(\$^{|\cdot|})} \to 1]$
	can't tell if input or random string encrypted
ind$ security
	$\mathrm{Adv}_{\pi}^{ind\$}(\mathcal{A}) = \mathrm{Pr}[\mathcal{A}^{\mathcal{E}_K(\cdot)} \to 1] - \mathrm{Pr}[\mathcal{A}^{\$^{|\cdot| + C}} \to 1]$ ($|\mathcal{E}_K(M)| = |M| + C$)
	can't tell if encrypted input or random string
	stronger than ind0, ind enc$, lr, semantic security
semantic security
	negligible info abount plaintext extractable from ciphertext
[prg](pseudorandom-generator.md)1 security
	$\mathrm{Adv}_G^{prg1}(\mathcal{A}) = \mathrm{Pr}[s \twoheadleftarrow \{0, 1\}^\ell : \mathcal{A}(G(s)) \to 1] - \mathrm{Pr}[R \twoheadleftarrow \{0, 1\}^L : \mathcal{A}(R) \to 1]$
	distinguish from truly random generator
	broken if P=NP
		easily verifiable, therefore easily solvable
[prf](pseudorandom-function.md) security
	$\mathrm{Adv}_F^{prf}(\mathcal{A}) = \mathrm{Pr}[k \twoheadleftarrow K : \mathcal{A}^{F_K(\cdot)} \to 1] - \mathrm{Pr}[\rho \twoheadleftarrow \mathrm{Func}(n, m) : \mathcal{A}^{\rho(\cdot)} \to 1]$
	distinguish from truly random function
[prp](pseudorandom-permutation.md) security
	$\mathrm{Adv}_E^{prp}(\mathcal{A}) = \mathrm{Pr}[k \twoheadleftarrow K : \mathcal{A}^{E_K(\cdot)} \to 1] - \mathrm{Pr}[\pi \twoheadleftarrow \mathrm{Perm}(n) : \mathcal{A}^{P(\cdot)} \to 1]$
	distinguish from truly random permutation
MAC security
	$\mathrm{Adv}_F^{mac}(\mathcal{A}) = \mathrm{Pr}[K \twoheadleftarrow \mathcal{K} : \mathcal{A}^{F_K(\cdot)} \text{ forges}]$
	adversary asks some queries to receive message-tag pairs, forges by getting valid message-tag pair not queried
digital signature security
	$\mathrm{Adv}_\pi^{sig}(\mathcal{A}, \mathcal{R}) = \mathrm{Pr}[(pk, sk) \twoheadleftarrow \mathcal{K}(k) : \mathcal{A}^{sg(sk, \cdot)}(pk) \text{ forges}]$
decisional [diffie-hellman](key-exchange#diffie-hellman-key-exchange) (DDH)
	$\mathrm{Adv}^{dh-ddh}(\mathcal{A}) = \mathrm{Pr}[a, b \twoheadleftarrow [0, \ldots, p-2] : \mathcal{A}(g6a, g^b, g^{ab}) \to 1] - \mathrm{Pr}[a, b, c \twoheadleftarrow [0, \ldots, p-2] : \mathcal{A}(g^a, g^b, g^c) \to 1]$
	not true in $\mathrm{Z}_p^\times$
computational diffie-hellman
	$\mathrm{Adv}^{cdf}(\mathcal{A}) = \mathrm{Pr}[a, b, \twoheadleftarrow [0, \ldots, p-2] : \mathcal{A}(g^a, g^b) \to g^{ab}]$
trapdoor permutation
	$\mathrm{Adv}_{\mathcal{G}}(\mathcal{A}, \mathcal{K}) = \mathrm{Pr}[(\textunderscore f, \textunderscore g) \twoheadleftarrow \mathcal{G}(k), c \twoheadleftarrow \mathrm{Dom}(f) : \mathcal{A}(\textunderscore f, f(x)) \to x]$
	hardness to reverse