# Pseudorandom Permutation
## Syntax
$E : \{0, 1\}^k \times \{0, 1\}^n \to \{0, 1\}^n$ where $E_K$ is permutation on $\{0, 1\}^n$
	$|\mathrm{Perm}(n)| = 2^n!$
		$|\mathrm{Cycle}(n)| = (2^n - 1)!$
	[security notion](security-notion.md)
DES (data encryption standard) ($k = 56, n = 64$)
	feistel network
		round function: data and subkey, run on half, xor with other half
		guaranteed invertible, even for noninvertible round
	short so that breakable by government, hardware centric
AES (advanced encryption standard) ($k = 128, n = 128$)
	add round key, 10 x (sub bytes, shift rows, mix columns, add round key)
# Encryption
ECB (electronic codebook) mode: split message ($10^*$ padding), encipher each block
counter mode: increment counter and encipher, xor with message
	secure if $E$ prp-secure
	[malleable](cryptography.md) (not ind secure), $M_1 \to IV_1 || C_1, M_1' \to (IV_1 + 1) \oplus C_1$
	faster than CBC since parallelizable
CBC (cipherblock chaining) mode: nonce $IV$, xor with each block of message before encryption
		CBC$ (random IV) is ind$ secure
```
algorithm CTR(K, M):
	static ctr = 0
	m = ceil(|M| / n)
	if ctr + m >= 2^n then return None
	Pad = E(K, ctr) || E(K, ctr + 1) ... [1:|M|]
	C = M xor Pad
	C' = ctr || C
	return C'
```
prp/[prf](pseudorandom-function.md) switching lemme
	for prp, difference in prp vs prf advantage for adversary that asks at most $q$ queries is $\frac{q^2}{2^{n+1}}$
	below birthday bound, prp and prf behave similarly
	gameplaying approach
		if query in domain, return result
		else get random for result, if in range then bad (prf, not prp)
tweakable blockcipher
	tweak $T$ , similar to $IV$/nonce