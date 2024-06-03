# Cryptography
cryptography: communication with an adversary $\mathcal{A}$
## Trust Models
encryption scheme $\mathcal{E}$, plaintext $M$, ciphertext $C$, shared key $K$
	$(pk, sk) \twoheadleftarrow \mathcal{G}$ (probabilistic)
	probabilistic scheme
		keygen, encryption probabilistic, decryption deterministic
malleability: given message ciphertext pair, produce ciphertext where plaintext meaningfully related to first plaintext

| model                   | privacy                                                            | authenticity                                            |
| ----------------------- | ------------------------------------------------------------------ | ------------------------------------------------------- |
| symmetric (shared key)  | symmetric encryption (blockcipher, one way function)               | MAC (blockcipher, one way function)                     |
| asymmetric (public key) | asymmetric encryption (diffie hellman/trapdoor and hash, trapdoor) | digital signature (trapdoor and hash, one way function) |
symmetric encryption
	sender and receiver share $K$
	sender sends $C = \mathcal{E}_K(M)$ to receiver, find $\mathcal{D}_K(C)$ to decrypt
[asymmetric encryption](public-key-encryption.md)
	receiver shares $pk$ of secret-public pair with everyone
	sender sends $C = \mathcal{E}_{pk}(M)$ to receiver, find $\mathcal{D}_{sk}(C)$ to decrypt
[MAC](message-authentication-code.md)
	sender and receiver share $K$
	sender sends $M, T = \mathrm{MAC}_K(M)$ to receiver, check if $M = \mathcal{D}_K(C)$ otherwise inauthentic
digital signature
	sender shares $pk$ of secret-public pair with everyone
	sender sends $M, \gamma = \mathrm{sign}_{sk}(M)$, check if $\mathrm{verify}_{pk}(M, \gamma)$