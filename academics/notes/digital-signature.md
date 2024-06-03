# Digital Signature
scheme $\pi = (k, sg, vf)$
	probabilistic key generation $k \to (pk, sk)$, probabilistic signature $sg(sk, M) \to \sigma$, deterministic verifier $vf(pk, M, \sigma) \to \{0, 1\}$
	correctness: if $sg(sk, M) = \sigma$, $vf(pk, M, \sigma) = 1$
	[security notion](security-notion.md)
schemes
	trapdoor for signature
		$(\textunderscore f, \textunderscore g) \twoheadleftarrow \mathcal{K}(k), sg(M) = g(M), vf(M, \sigma) = 1$ if $f(\sigma) = M$
		ex with [RSA](public-key-encryption.md)
	FDH
		hash message to power d mod N
		$\sigma = m^d \mod N$ or $(H(m))^d \mod N$ where $H : \{0, 1\}^* \to \mathrm{Dom}(g)$
	PSS (probabilistic signature scheme): three hashes
	one time signature: sign a bit once $(0, A)$ and $(1, B)$
		lamport signature: extend to multiple, merkle tree