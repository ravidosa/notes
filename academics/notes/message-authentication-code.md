# Message Authentication Code
$\mathrm{MAC} : \mathcal{K} \times \mathcal{M} \to \{0, 1\}^n$
	[security notion](security-notion.md)
	secure PRF always secure MAC
	AEAD (authenticated encryption with associated data)
		encrypt, then MAC
		key $K$, nonce $N$, associated data $A$
schemes
	CBC MAC
		xor each encrypted block with next block
		forge by asking $(0^n, T)$, forging $(0^n||T, T)$
		for fixed length message space, CBC MAC secure if [block cipher](pseudorandom-permutation.md) secure
		almost universal hash function (probability of collision less than epsilon for all message, all hash functions in family)
	carter-wegman MAC: xor encrypted message block with encryption of counter
	black rogaway: xor message block with multiples of encryption of $0^n$
	GMAC: use polynomial with message blocks as coefficients
		efficient evaluation