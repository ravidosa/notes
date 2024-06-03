# Pseudorandom Function
## Syntax
$F : \{0, 1\}^k \times \{0, 1\}^n \to \{0, 1\}^m$
	$|\mathrm{Func}(n, m)| = 2^{m \cdot 2^n}$
	[security notion](security-notion.md)
## Encryption
ex [ChaCha20](https://en.wikipedia.org/wiki/ChaCha20-Poly1305) ($k = 256, n = 128, m = 512$)
birthday paradox
	for $N$ items, collisions after $\sqrt{N}$ trials
```
algorithm E(K, M):
	R = random({0, 1}^n)
	C = M xor F(K, R)[1:|M|]
	C' = R || C
	return C'

algorithm D(K, C'):
	R || C = C'
	M = C xor F(K, R)[1:|C|]
	return M

algorithm ChaChaEncrypt(K, M):
	if |M| > 2^(32 + 9) then return None
	R = random({0, 1}^n)
	Pad = ChaCha20(K, R || 0) || ChaCha20(K, R || 1) || ...
	C = M xor Pad
	C' = R || C
	return C'
```