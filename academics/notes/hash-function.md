# Hash Function
## Cryptography
$H : \{0, 1\}^* \to \{0, 1\}^n$
	MD4, MD5, SHA1, SHA2, SHA256
collision intractability: nobody knows two messages that hash to same value (formalization of human ignorance)
### Construction
merkle-damgard
	build collision-resistant hash from collision-resistant compression
	apply padding, then break into fixed-size blocks and compress, keep combining blocks and compressing to get hash
davies-meyer: build from [blockcipher](pseudorandom-permutation.md)