# One-Time Pad
key longer than messages
## Encryption Scheme
```
algorithm K(l): # key generation
	K = random({0, 1}^l)
	return K
algorithm E(K, M): # encryption
	static i = 1
	if i + |M| - 1 > |K| then return None
	C = K[i:i + |M| - 1] xor M
	C' = <i, C>
	i = i + |M|
	return C'
algorithm D(K, C'): # decryption
	<i, C> = C'
	if i + |C| > |K| then return None
	M = K[i:i + |C| - 1] xor C
	return M
```