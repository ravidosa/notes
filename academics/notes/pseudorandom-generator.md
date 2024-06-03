# Pseudorandom Generator
## Syntax
$G : \{0, 1\}^\ell \to \{0, 1\}^L$
	[security notion](security-notion.md)
seed as input, generate keystream
	finite (concrete)/infinite (asymptotic) stretch
	stream cipher, vernam cipher
	[RC4](https://en.wikipedia.org/wiki/RC4)
		insecure (biased second byte), signature inconvenient, slow
key scheduling
good prg if [1-bit stretch security](security-notion.md)
```
algorithm G(s):
	for i = 1 to infinity do
		s = g(s)
		b = s[n + 1]
		s = s[1:n]
		output b

algorithm G(s):
	s_0 = s
	for i = 1 to L do
		s_i || b_i = g(s_i-1)
	return b_1...b_L
```