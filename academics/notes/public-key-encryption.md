# Public Key Cryptography
## Syntax
encryption scheme $\pi = (\mathcal{G}, \mathcal{E}, \mathcal{D})$
	probabilistic key generation algorithm $\mathcal{G} \to (pk, sk)$, probabilistic encryption algorithm $\mathcal{E}_{pk}(M) \to C$, deterministic decryption algorithm $\mathcal{D}_{sk}(C) \to M$
	correctness: if $\mathcal{E}_{pk}(M) = C$, $\mathcal{D}_{sk}(C) = M$
	[security notion](security-notion.md)
	ephemeral public key for [diffie hellman](key-exchange#diffie-hellman-key-exchange)
[computational and decisional diffie hellman](security-notion.md)
	elgamal
		key generation: generator $g$ of cyclic group $G$ with order $q$, compute $h = g^x$ for random $x$, public key $(G, q, g, h)$, secret key $x$
		encryption: map message to group element $m$, shared secret $s = h^y$ for random $y$, $c_1 = g^y, c_2 = m \cdot s$, ciphertext $(c_1, c_2)$
		decryption: compute $s = c_1^x, s^{-1}$, then $m = c_2s^{-1}$
trapdoor permutation: easy to compute, hard to reverse
	not good for encryption (deterministic), not good way to sign (limited domain)
	given by generator $\mathcal{G}$
		gives $\textunderscore f, \textunderscore g$ given security parameter $k$ where $f, g$ are inverses
		[security notion](security-notion.md)
	RSA
		primes $p, q$
		$n = pq, \varphi(n) = (p - 1)(q - 1)$
		$e, d \in \mathrm{Z}_{\varphi(n)}^\times$ where $ed = 1$
		$f(x) = x^e \mod n, g(y) = y^d \mod n$
	encryption
		RSA-DAEP (ind security, malleability)
```
algorithm E(pk, M):
	R = random(Dom(f))
	Y = f(R)
	return Y || H(R) xor M
```
random oracle model
	imagine everyone has access to public random oracle
	prove security in this world, then instantiate with real world hash function